import json, os
from decimal import Decimal as D, ROUND_HALF_UP
OUT='/workspace/hackathon/data/declarant/demo-sets'
T=json.load(open('/workspace/hackathon/data/tariff/tariff_demo.json')); TR={r['code10']:r for r in T['rows']}
F=json.load(open('/workspace/hackathon/data/tariff/fees.json'))
BHM=D(440000)
RATES={'USD':D('12100.00'),'CNY':D('1700.00')}
RATE_NOTE="EXAMPLE exchange rates (not CBU data): 1 USD = 12 100.00 UZS, 1 CNY = 1 700.00 UZS. Replace with the CBU rate on the GTD acceptance date (Customs Code Art. 326; Instruction 2773 grafa 23)."
SYN="SYNTHETIC DEMO DATA – fictitious companies, people, TINs, PINFLs, plates and document numbers. Not real. Do not file."
q2=lambda x: x.quantize(D('0.01'),ROUND_HALF_UP); q3=lambda x: x.quantize(D('0.001'),ROUND_HALF_UP)
def fee_band(usd):
    for b in F['customs_clearance_fee']['bands']:
        lo=D(str(b['usd_from'] or 0)); hi=b['usd_to']
        if usd>=lo and (hi is None or usd<D(str(hi))): return D(str(b['bhm_multiplier'])), b['text_as_written']
def S(x): return str(x)
def calc(set_id, cur, items, addbacks, deductions, packages_by_item):
    rate=RATES[cur]; usd=RATES['USD']
    tot_gross=sum(i['gross'] for i in items)
    res=[]; 
    for i in items:
        share=i['gross']/tot_gross
        add=q2(addbacks*share) if addbacks else D(0); ded=q2(deductions*share) if deductions else D(0)
        res.append(dict(i=i,add=add,ded=ded))
    # fix rounding remainder on last item
    if addbacks: res[-1]['add']+=addbacks-sum(r['add'] for r in res)
    if deductions: res[-1]['ded']+=deductions-sum(r['ded'] for r in res)
    lines=[]; tot_cv=D(0)
    for r in res:
        i=r['i']; inv=i['amount']; cv=q2(inv+r['add']-r['ded']); tot_cv+=cv
        cv_uzs=q2(cv*rate); tr=TR[i['code']]
        adv=q2(cv_uzs*D(str(tr['ad_valorem_pct']))/100)
        spec=None; duty=adv; basis="ad valorem"
        sm=tr.get('specific_min')
        if sm:
            unit=sm['unit']; qty= i['qty'] if unit in('dona','juft') else i['net']
            spec=q2(D(str(sm['amount']))*qty*usd); 
            if spec>adv: duty=spec; basis=f"specific minimum {sm['amount']} USD/{unit} (> ad valorem)"
        vat=q2((cv_uzs+duty)*D('0.12'))
        stat=q3((cv*rate/usd)/1000) # thousand USD; assumes CV ≈ CIF border value
        lines.append(dict(item_no=i['no'],code10=i['code'],invoice_value=S(q2(inv)),addback=S(r['add']),deduction=S(r['ded']),customs_value=S(cv),customs_value_uzs=S(cv_uzs),
          duty=dict(code='20',rate_ad_valorem_pct=tr['ad_valorem_pct'],ad_valorem_uzs=S(adv),specific_min=sm,specific_min_uzs=S(spec) if spec is not None else None,applied=basis,amount_uzs=S(duty)),
          vat=dict(code='29',rate_pct=12,base_uzs=S(cv_uzs+duty),amount_uzs=S(vat)),statistical_value_kusd=S(stat),
          rate_source=dict(file='data/tariff/tariff_demo.json',source_doc=tr['source_doc'],url=tr['source_url'],checked=tr['source_checked_date'],verified=tr['verified'],notes=tr['notes'])))
    tot_cv_usd=q2(tot_cv*rate/usd); mult,txt=fee_band(tot_cv_usd); fee=q2(BHM*mult)
    return lines,tot_cv,tot_cv_usd,dict(code='10',band=txt,multiplier_bhm=S(mult),bhm_uzs=S(BHM),amount_uzs=S(fee),shown_on='item 1 only (Instruction 2773 grafa 47)',source='VM No. 55 Annex 1 pos.1(a) via data/tariff/fees.json',url='https://lex.uz/docs/-7357270',preliminary_discount_applied=False,band_edge_note=F['customs_clearance_fee']['engine_convention'])
def w(path,obj): 
    os.makedirs(os.path.dirname(path),exist_ok=True); json.dump(obj,open(path,'w'),ensure_ascii=False,indent=2)
def build(cfg):
    d=f"{OUT}/{cfg['id']}"; cur=cfg['currency']
    items=cfg['items']
    for i in items: i['amount']=q2(i['qty']*i['price'])
    inv_lines=[dict(line=i['no'],description=i['desc_en'],brand=i['brand'],model=i['model'],hs_code=i['inv_hs'],origin=cfg['origin_name'],qty=S(i['qty']),unit=i['unit'],unit_price=S(i['price']),amount=S(i['inv_amount'] if 'inv_amount' in i else i['amount']),net_kg=S(i['net']),gross_kg=S(i['gross']),packages=i['pk_inv']) for i in items]
    inv_total=sum(D(l['amount']) for l in inv_lines)
    invoice=dict(_synthetic=SYN,doc_type="commercial_invoice",number=cfg['inv_no'],date=cfg['inv_date'],seller=cfg['seller'],buyer=cfg['buyer_inv'],contract=dict(number=cfg['contract_no'],date=cfg['contract_date']),
      incoterms=cfg['incoterms_inv'],currency=cur,payment_terms=cfg['payment_terms'],lines=inv_lines,total_amount=S(cfg.get('inv_total_override',inv_total)),total_packages=sum(i['pk_inv'] for i in items),
      total_net_kg=S(sum(i['net'] for i in items)),total_gross_kg=S(sum(i['gross'] for i in items)),notes=cfg.get('inv_notes'))
    pl_lines=[dict(line=i['no'],description=i['desc_en'],model=i['model'],qty=S(i.get('pl_qty',i['qty'])),unit=i['unit'],packages=i.get('pl_pk',i['pk_inv']),package_type=i['pk_type'],net_kg=S(i.get('pl_net',i['net'])),gross_kg=S(i.get('pl_gross',i['gross'])),carton_marks=i['marks']) for i in items]
    pl=dict(_synthetic=SYN,doc_type="packing_list",number=cfg['pl_no'],date=cfg['inv_date'],invoice_ref=cfg['inv_no'],seller=cfg['seller']['name'],buyer=cfg['buyer_inv']['name'],lines=pl_lines,
      total_packages=sum(l['packages'] for l in pl_lines),total_net_kg=S(sum(D(l['net_kg']) for l in pl_lines)),total_gross_kg=S(sum(D(l['gross_kg']) for l in pl_lines)))
    cmr=dict(_synthetic=SYN,doc_type="CMR",number=cfg['cmr_no'],date=cfg['cmr_date'],box1_sender=cfg['seller']['name']+', '+cfg['seller']['address'],box2_consignee=cfg['buyer']['name']+', '+cfg['buyer']['address'],
      box3_place_of_delivery=cfg['cmr_delivery'],box4_place_date_taking_over=cfg['cmr_takeover'],box5_documents_attached=[f"Invoice {cfg['inv_no']}",f"Packing list {cfg['pl_no']}"]+cfg.get('cmr_docs',[]),
      box6_marks=f"{cfg['marks_cmr']}",box7_number_of_packages=cfg['cmr_packages'],box8_packing="cartons",box9_goods=cfg['cmr_goods'],box10_hs=cfg['cmr_hs'],box11_gross_kg=S(cfg['cmr_gross']),box12_volume_m3=cfg.get('cmr_m3'),
      box16_carrier=cfg['carrier'],vehicle=dict(tractor=cfg['truck'],trailer=cfg['trailer'],country=cfg['truck_country']),border_crossing=dict(post=cfg['border_post'],date=cfg['border_date'],stamp="SYNTHETIC"),
      invoice_value_per_code=cfg['cmr_value_per_code'])
    support=dict(_synthetic=SYN,contract=dict(number=cfg['contract_no'],date=cfg['contract_date'],e_system_id=cfg['contract_id'],seller=cfg['seller']['name'],buyer=cfg['buyer']['name'],incoterms=cfg['incoterms_inv'],currency=cur,settlement_currency=cur,payment_form=cfg['payment_form']),
      certificate_of_origin=cfg['coo'],other_certificates=cfg.get('certs',[]),transit_declaration=cfg['td'],freight=cfg.get('freight'),
      arrival=dict(destination_post=cfg['dest_post'],presented_on=cfg['presented'],delivery_confirmed=cfg['confirmed']),
      importer_profile=cfg['buyer'],responsible_person=cfg['resp'])
    lines,tot_cv,tot_cv_usd,fee=calc(cfg['id'],cur,[dict(no=i['no'],code=i['code'],amount=i['amount'],gross=i['gross'],net=i['net'],qty=i['qty']) for i in items],cfg.get('addback',D(0)),cfg.get('deduction',D(0)),None)
    n=len(items); sheets=1+(-(-(n-1)//3)) if n>1 else 1
    head={ '1':'ИМ | 40 |','2':f"{cfg['seller']['name']}, {cfg['seller']['country_ru']}, {cfg['seller']['address']}",'3':f"1/{sheets}",'5':str(n),'7':f"{cfg['dest_post']['code']} (declarant) – rest assigned by customs",
      '8':f"{cfg['buyer']['name']}, {cfg['buyer']['address']}, тел. {cfg['buyer']['phone']}, {cfg['buyer']['email']} | upper №: (empty) | № {cfg['buyer']['tin']}/{cfg['buyer']['district_code']}",
      '9':f"{cfg['buyer']['name']} ... | № {cfg['buyer']['tin']}/{cfg['buyer']['district_code']}",'11':f"{cfg['origin_code']} | 2",'12':S(tot_cv),'13':"12100,00 (EXAMPLE)",'14':f"{cfg['buyer']['name']} (self-filing) | № {cfg['buyer']['tin']}",
      '15':cfg['dispatch_ru'],'15a':cfg['origin_code'],'18':f"1 АВТО: {cfg['truck']}/{cfg['trailer']} | {cfg['truck_country']}",'19':'0','20':cfg['g20'],'21':f"1 АВТО: {cfg['truck']}/{cfg['trailer']} | {cfg['truck_country']}",
      '22':f"{cfg['cur_code']} | {S(sum(i['amount'] for i in items))}",'23':f"1/{S(RATES[cur]).replace('.',',')} (EXAMPLE)",'24':f"01 | {cfg['cur_code']}",'25':'30','26':'30','28':cfg['buyer']['tin'],'29':f"{cfg['border_post']['code']} {cfg['border_post']['name']}",
      '30':f"{cfg['goods_location']} | {cfg['goods_location_district']}",'50':f"Ответственность за представленные документы и сведения несет {cfg['resp']['name']}, {cfg['resp']['position']}, {cfg['resp']['phone']} | ПИНФЛ {cfg['resp']['pinfl']}",
      '54':f"1) {cfg['place']}\n2) {cfg['resp']['name']}, {cfg['buyer']['email']}\n3) {cfg['resp']['phone']}\n5) {cfg['resp']['pinfl']}/{cfg['filing_date_ddmmyyyy']}/{cfg['own_serial']}",
      'C':f"1) {cfg['contract_id']}\n2) {cfg['border_date_ddmmyyyy']}"}
    item_g=[]
    for i,l in zip(items,lines):
        pk=i['pk_inv']
        g47=[]
        if i['no']==1: g47.append(dict(vid='10',osnova=f"1 ГТД (band: total CV ≈ {S(tot_cv_usd)} USD)",stavka=f"{fee['multiplier_bhm']} БРВ",summa=fee['amount_uzs'],sp='БН',note='⚠️ how the fee base is written in the cabinet is not specified'))
        g47.append(dict(vid='20',osnova=l['customs_value_uzs'] if 'specific' not in l['duty']['applied'] else f"{S(i['qty'])} {i['unit_ru']}",stavka=(f"{l['duty']['rate_ad_valorem_pct']}%" if 'specific' not in l['duty']['applied'] else f"{l['duty']['specific_min']['amount']} USD/{l['duty']['specific_min']['unit']}"),summa=l['duty']['amount_uzs'],sp='БН'))
        g47.append(dict(vid='29',osnova=l['vat']['base_uzs'],stavka='12%',summa=l['vat']['amount_uzs'],sp='БН'))
        item_g.append({'32':str(i['no']),'31':f"1) {i['desc_ru']}\n2) {pk} мест, {i['pk_type_ru']}\n11) 02",'31_bottom_left':f"{cfg['buyer']['tin']}/{cfg['buyer']['district_code']}",'31_bottom_right':S(i['qty']),
          '33':i['code'],'34':cfg['origin_code'],'35':S(q3(i['gross'])),'37':'4000000','38':S(q3(i['net'])),'40':f"ТД {cfg['td']['number']} — {cfg['td']['item_for'][i['no']]} — {S(i['gross'])} кг — {S(i['net'])} кг — {S(i['qty'])} {i['unit_ru']}",
          '41':'796 (шт) ⚠️ verify unit code','42':S(i['amount']),'43':'0','44':cfg['g44'],'45':l['customs_value'],'46':l['statistical_value_kusd'],'47':g47,
          'hs_reasoning':i['hs_reasoning']})
    totals=dict(customs_value=S(tot_cv),currency=cur,customs_value_usd_equiv=S(tot_cv_usd),fee_uzs=fee['amount_uzs'],duty_uzs=S(sum(D(l['duty']['amount_uzs']) for l in lines)),vat_uzs=S(sum(D(l['vat']['amount_uzs']) for l in lines)))
    totals['grand_total_uzs']=S(D(totals['fee_uzs'])+D(totals['duty_uzs'])+D(totals['vat_uzs']))
    key=dict(_synthetic=SYN,set_id=cfg['id'],title=cfg['title'],scenario=cfg['scenario'],rates_note=RATE_NOTE,
      assumptions=cfg['assumptions']+["UZS amounts rounded half-up to 2 decimals – official rounding rule for grafa 47 not confirmed ⚠️.","VAT = 12% × (customs value + duty + excise) per Tax Code Arts. 254, 258 as used in data/tariff (no excise for these codes).","Additional duty (code 21, Customs Code Art. 300¹ per data/tariff) NOT applied: origin is documented and the country is on the MFN list (data/tariff/tariff_demo.json common.mfn_list_url).","Grafa 46 computed from customs value (assumes customs value ≈ CIP/CIF border value) ⚠️."],
      expected_cross_checks=cfg['expected_checks'],seeded_discrepancies=cfg['seeded'],expected_outcome=cfg['outcome'],
      expected_gtd=dict(header=head,items=item_g),payments=dict(per_item=lines,fee=fee,totals=totals),deadline=cfg['deadline'])
    w(f"{d}/invoice.json",invoice); w(f"{d}/packing-list.json",pl); w(f"{d}/cmr.json",cmr); w(f"{d}/supporting-docs.json",support); w(f"{d}/answer-key.json",key)
    # md
    M=[f"# {cfg['title']}","",f"**⚠️ {SYN}**","",cfg['scenario'],"","## Invoice "+cfg['inv_no'],"",f"Seller: {cfg['seller']['name']} ({cfg['seller']['address']}, TIN {cfg['seller']['tin']}) · Buyer: {invoice['buyer']['name']} · Contract {cfg['contract_no']} of {cfg['contract_date']} · Incoterms {cfg['incoterms_inv']} · Currency {cur}","",
       "| # | Description | HS (seller) | Qty | Price | Amount | Net kg | Gross kg | Pkgs |","|---|---|---|---|---|---|---|---|---|"]
    M+=[f"| {l['line']} | {l['description']} ({l['brand']} {l['model']}) | {l['hs_code']} | {l['qty']} {l['unit']} | {l['unit_price']} | {l['amount']} | {l['net_kg']} | {l['gross_kg']} | {l['packages']} |" for l in inv_lines]
    M+=[f"| | **Total** | | | | **{invoice['total_amount']}** | {invoice['total_net_kg']} | {invoice['total_gross_kg']} | {invoice['total_packages']} |","",
       "## Packing list "+cfg['pl_no'],"","| # | Model | Qty | Pkgs | Net kg | Gross kg |","|---|---|---|---|---|---|"]+[f"| {l['line']} | {l['model']} | {l['qty']} | {l['packages']} | {l['net_kg']} | {l['gross_kg']} |" for l in pl_lines]
    M+=[f"| | **Total** | | {pl['total_packages']} | {pl['total_net_kg']} | {pl['total_gross_kg']} |","","## CMR "+cfg['cmr_no'],"",f"Taking over: {cfg['cmr_takeover']} · Delivery: {cfg['cmr_delivery']} · Packages: {cfg['cmr_packages']} · Gross: {cfg['cmr_gross']} kg · HS: {cfg['cmr_hs']} · Vehicle: {cfg['truck']}/{cfg['trailer']} ({cfg['truck_country']}) · Border: {cfg['border_post']['code']} {cfg['border_post']['name']} on {cfg['border_date']}","",
       "## Answer key (summary)","",f"**Outcome:** {cfg['outcome']}",""]
    if cfg['seeded']: M+=["**Seeded discrepancies:**",""]+[f"- `{s['check_id']}`: {s['what']} → {s['expected_severity']}" for s in cfg['seeded']]+[""]
    M+=["**Expected cross-checks:**",""]+[f"- `{c['check_id']}`: {c['result']} — {c['detail']}" for c in cfg['expected_checks']]+["",
       "| Item | Code | HS reasoning | Customs value | Duty (UZS) | VAT (UZS) |","|---|---|---|---|---|---|"]
    M+=[f"| {g['32']} | {g['33']} | {g['hs_reasoning']} | {l['customs_value']} {cur} | {l['duty']['amount_uzs']} ({l['duty']['applied']}) | {l['vat']['amount_uzs']} |" for g,l in zip(item_g,lines)]
    M+=["",f"Fee (code 10): {fee['amount_uzs']} UZS ({fee['multiplier_bhm']} BHM; band '{fee['band']}'). **Total payable (EXAMPLE rates): {totals['grand_total_uzs']} UZS.**","",RATE_NOTE,"",f"Deadline: {cfg['deadline']}","","Full expected grafa values: `answer-key.json` → `expected_gtd`."]
    open(f"{d}/README.md",'w').write('\n'.join(M))
    return key
BUY_A=dict(name="«UYJIHOZ SAVDO» MChJ (SYNTHETIC)",address="г. Ташкент, Чиланзарский р-н, ул. Бунёдкор, 1 (SYNTHETIC)",tin="100000001",district_code="1726294",phone="+998 71 000 00 01",email="info@uyjihoz.example")
A=dict(id="set-A-furniture-cn-truck",title="Set A – Wooden furniture from China by truck (clean golden path)",currency="USD",cur_code="840",origin_code="156",origin_name="China",dispatch_ru="КИТАЙ",
 scenario="Small Tashkent furniture retailer imports dining tables and sideboards from Foshan (FCA), Uzbek carrier, enters at Dustlik (Andijan) under transit, cleared at Sergeli inland post. All documents consistent. Shows: two models under ONE code must be two items (Instruction 2773 point 8); freight to the border added to customs value (Customs Code Art. 304(a)); specific-minimum check (0.4 USD/kg) loses to ad valorem.",
 seller=dict(name="Foshan Mingde Furniture Co., Ltd. (SYNTHETIC)",address="Longjiang Rd 88, Shunde, Foshan, Guangdong, China",tin="91440606SYNTH0001",country_ru="Китай"),
 buyer=BUY_A,buyer_inv=BUY_A,contract_no="15/2026",contract_date="2026-09-05",contract_id="2026-UZ-000000123 (SYNTHETIC)",inv_no="MD-2026-118",inv_date="2026-10-28",pl_no="MD-PL-118",
 incoterms_inv="FCA Foshan (Incoterms 2010)",payment_terms="100% prepayment",payment_form="10/01",g20="02 | FCA Foshan | 10/01",
 items=[dict(no=1,code="9403601000",desc_en="Dining table, solid rubberwood, 1600x900x750 mm, lacquered",desc_ru="Стол обеденный из массива гевеи, лакированный, 1600x900x750 мм, модель DT-1600, бренд MINGDE",brand="MINGDE",model="DT-1600",inv_hs="9403.60",qty=D(40),unit="pcs",unit_ru="шт",price=D('145.00'),net=D('1520.000'),gross=D('1760.000'),pk_inv=80,pk_type="cartons (top + legs)",pk_type_ru="картонные коробки",marks="MD-DT 1-80",
     hs_reasoning="GRI 1/6: furniture, not seats (9401) → 9403; wooden → 9403 60; dining-room furniture → 9403 60 100 0 ('ошхона ва яшаш хоналари учун ёғоч мебель', PQ-181 Annex 1)."),
   dict(no=2,code="9403601000",desc_en="Sideboard / TV stand, solid pine, 1200x450x600 mm",desc_ru="Тумба-комод из массива сосны, 1200x450x600 мм, модель SB-1200, бренд MINGDE",brand="MINGDE",model="SB-1200",inv_hs="9403.60",qty=D(30),unit="pcs",unit_ru="шт",price=D('210.00'),net=D('1560.000'),gross=D('1740.000'),pk_inv=30,pk_type="cartons",pk_type_ru="картонные коробки",marks="MD-SB 81-110",
     hs_reasoning="Same as item 1 (living-room wooden furniture → 9403 60 100 0). Separate item because model/name differ (Instruction 2773 point 8).")],
 cmr_no="CN-UZ-77812",cmr_date="2026-11-01",cmr_takeover="Foshan, China, 01.11.2026",cmr_delivery="Tashkent, Uzbekistan",cmr_packages=110,cmr_gross=D('3500'),cmr_hs="940360",cmr_goods="Wooden furniture (dining tables, sideboards)",marks_cmr="MD 1-110",cmr_m3="38.5",
 cmr_value_per_code={"940360":"12100.00 USD"},carrier="«TRANS SILK LOGISTICS» MChJ (SYNTHETIC), Toshkent",truck="01A123BC",trailer="01XY456",truck_country="860",
 border_post=dict(code="03002",name="Дустлик"),border_date="2026-11-10",border_date_ddmmyyyy="10.11.2026",
 td=dict(number="03002/10.11.2026/0012345",type="ТД",from_post="03002",to_post="26010",item_for={1:1,2:1},note="SYNTHETIC; one TD item for code 9403601000"),
 dest_post=dict(code="26010",name="Сергели"),presented="2026-11-12",confirmed="2026-11-12T10:40+05:00",goods_location="г. Ташкент, Сергелийский р-н, зона таможенного контроля поста «Сергели» (SYNTHETIC address)",goods_location_district="1726283",
 coo=dict(code="701 СПТИМ",number="CCPIT-SYN-2026-0001",date="2026-10-30",country="China",note="SYNTHETIC"),
 freight=dict(carrier_invoice="TSL-2026-559 (SYNTHETIC)",total_usd="4600.00",to_border_usd="3900.00",border_to_tashkent_usd="700.00",insurance="none paid"),
 addback=D('3900.00'),resp=dict(name="Каримов Азиз Бахромович (SYNTHETIC)",position="директор",phone="+998 90 000 00 01",pinfl="30000000000001"),place="г. Ташкент",filing_date_ddmmyyyy="13.11.2026",own_serial="000017",
 g44="202 СМР № CN-UZ-77812 от 01.11.2026\n220 ИНВ № MD-2026-118 от 28.10.2026\n222 УПЛИСТ № MD-PL-118 от 28.10.2026\n301 КНТ № 15/2026 от 05.09.2026\n701 СПТИМ № CCPIT-SYN-2026-0001 от 30.10.2026\n(+ freight invoice for Art. 304 add-back – document code to confirm ⚠️)",
 assumptions=["Freight to the border (3 900 USD of 4 600 USD) added per Customs Code Art. 304(a); 700 USD inside Uzbekistan not added (Art. 305 – documented separately). Allocation between items by gross weight = PROPOSAL (no allocation rule found) ⚠️.","Specific minimum 0.4 USD/kg computed on NET kg (data/tariff marks net/gross UNVERIFIED); on gross it is also below ad valorem, so the outcome does not change.","Conformity-certificate requirement for furniture not verified – check Single Window list ⚠️ (none included)."],
 expected_checks=[dict(check_id=c,result="pass",detail=t) for c,t in [("pkg_count","110 = 110 = 110"),("qty_supp_unit","40/30 pcs match"),("value_sum","5800+6300 = 12100.00"),("gross_weight_docs","3500 = 3500 kg"),("net_weight_docs","3080 = 3080 kg"),("net_le_gross","ok"),("hs_prefix","940360 = 940360"),("origin","CN everywhere"),("currency_incoterms","USD, FCA, 15/2026"),("customs_value_logic","CV = 12100 + 3900 = 16000.00 USD"),("invoice_annex1a","all 12 items present"),("dates","05.09 ≤ 28.10 ≤ 01.11 ≤ 10.11 ≤ 13.11")]],
 seeded=[],outcome="All checks pass → ready for review & ERI signing (green-path candidate; actual risk lane is decided by customs).",
 deadline="Presented 12.11.2026 (Thu) → file by 26.11.2026 (conservative) / legal max 27.11.2026 (next-day reading). See deadlines.json.")
BUY_B=dict(name="«MODA TEKSTIL TRADE» MChJ (SYNTHETIC)",address="г. Ташкент, Юнусабадский р-н, ул. Амира Темура, 100 (SYNTHETIC)",tin="100000002",district_code="1726266",phone="+998 71 000 00 02",email="info@modatekstil.example")
B=dict(id="set-B-tshirts-tr-truck",title="Set B – Cotton T-shirts from Turkey by truck (2 seeded discrepancies + HS warning)",currency="USD",cur_code="840",origin_code="792",origin_name="Türkiye",dispatch_ru="ТУРЦИЯ",
 scenario="Clothing wholesaler imports knitted cotton T-shirts from Istanbul, CPT Tashkent, Turkish truck, enters at Alat (Bukhara), cleared at Tashkent-tovarniy. CMR is wrong on packages and gross weight; seller's invoice shows the wrong HS subheading. Shows: specific minimum (0.5 USD/pc) beats ad valorem; inland-freight deduction under Art. 305.",
 seller=dict(name="Anka Tekstil Sanayi ve Ticaret A.Ş. (SYNTHETIC)",address="Merter Mah. 12, Güngören, İstanbul, Türkiye",tin="TR-SYN-1234567890",country_ru="Турция"),
 buyer=BUY_B,buyer_inv=BUY_B,contract_no="TR-07/2026",contract_date="2026-08-20",contract_id="2026-UZ-000000456 (SYNTHETIC)",inv_no="ANK-2026-0917",inv_date="2026-11-02",pl_no="ANK-PL-0917",
 incoterms_inv="CPT Tashkent (Incoterms 2010)",payment_terms="30% prepayment, 70% within 30 days after import",payment_form="50/01 (mixed – larger share 'upon import')",g20="07 | CPT Tashkent | 50/01",
 inv_notes="Price includes carriage to Tashkent. Carrier statement attached: carriage from UZ border (Alat) to Tashkent = 450.00 USD.",
 items=[dict(no=1,code="6109100000",desc_en="Men's T-shirt, knitted single jersey, 100% cotton, 160 g/m2, sizes S-XXL, assorted colours",desc_ru="Футболки мужские трикотажные (кулирная гладь), 100% хлопок, 160 г/м2, размеры S-XXL, бренд ANKA BASIC, арт. AB-100",brand="ANKA BASIC",model="AB-100",inv_hs="6109.90",qty=D(6000),unit="pcs",unit_ru="шт",price=D('2.10'),net=D('1260.000'),gross=D('1344.000'),pk_inv=120,pk_type="cartons, 50 pcs each",pk_type_ru="картонные коробки",marks="ANK 1-120",
     hs_reasoning="Knitted → Chapter 61; T-shirt → 6109; 100% cotton → 6109 10 → 6109 10 000 0. Seller's 6109.90 ('other textile materials') contradicts the composition → warn.")],
 cmr_no="TR-UZ-20931",cmr_date="2026-11-03",cmr_takeover="İstanbul, Türkiye, 03.11.2026",cmr_delivery="Tashkent, Uzbekistan",cmr_packages=118,cmr_gross=D('1430'),cmr_hs="610990",cmr_goods="Cotton T-shirts",marks_cmr="ANK 1-120",cmr_m3="9.6",
 cmr_value_per_code={"610990":"12600.00 USD"},carrier="Anadolu Lojistik Ltd. (SYNTHETIC)",truck="34ABC123",trailer="34XYZ45",truck_country="792",
 border_post=dict(code="06010",name="Алат"),border_date="2026-11-19",border_date_ddmmyyyy="19.11.2026",
 td=dict(number="06010/19.11.2026/0004567",type="ТД",from_post="06010",to_post="26002",item_for={1:1},note="SYNTHETIC"),
 dest_post=dict(code="26002",name="Ташкент-товарный"),presented="2026-11-21",confirmed="2026-11-21T11:15+05:00",goods_location="г. Ташкент, Юнусабадский р-н, зона таможенного контроля (SYNTHETIC address)",goods_location_district="1726266",
 coo=dict(code="701 СПТИМ",number="TR-ITO-SYN-778899",date="2026-11-02",country="Türkiye",note="SYNTHETIC; 6109 not in Turkey PTA Annex I-B → no preference, MFN rate applies (data/tariff)"),
 freight=dict(carrier_statement="AL-STM-2026-118 (SYNTHETIC)",border_to_tashkent_usd="450.00"),deduction=D('450.00'),
 resp=dict(name="Usmonova Dilnoza Rustamovna (SYNTHETIC)",position="директор",phone="+998 90 000 00 02",pinfl="40000000000002"),place="г. Ташкент",filing_date_ddmmyyyy="24.11.2026",own_serial="000003",
 g44="202 СМР № TR-UZ-20931 от 03.11.2026 (after correction)\n220 ИНВ № ANK-2026-0917 от 02.11.2026\n222 УПЛИСТ № ANK-PL-0917 от 02.11.2026\n301 КНТ № TR-07/2026 от 20.08.2026\n701 СПТИМ № TR-ITO-SYN-778899 от 02.11.2026",
 assumptions=["Packing list and invoice are correct; CMR is the erroneous document (carrier must issue a corrected CMR or the declarant must explain) – expected GTD values below assume the corrected state.","Inland carriage 450 USD deducted under Customs Code Art. 305 (separately documented). Without the carrier statement CV would be 12 600 USD.","Specific minimum 0.5 USD/pc × 6 000 = 3 000 USD > 20% × 12 150 = 2 430 USD → specific applies (Customs Code Art. 293 'not less than', per data/tariff)."],
 expected_checks=[dict(check_id="pkg_count",result="FAIL – error_blocking",detail="invoice 120, packing list 120, CMR 118"),dict(check_id="gross_weight_docs",result="FAIL – error_blocking",detail="packing list 1344 kg vs CMR 1430 kg: diff 86 kg = 6.40%; T = max(1% × 1344, 20) = 20 kg → 86 > 20"),
   dict(check_id="hs_prefix",result="WARN – warning_ack",detail="invoice/CMR 610990 vs chosen 610910 (100% cotton)"),dict(check_id="qty_supp_unit",result="pass",detail="6000 = 6000"),dict(check_id="value_sum",result="pass",detail="6000 × 2.10 = 12600.00"),
   dict(check_id="net_weight_docs",result="pass",detail="1260 = 1260"),dict(check_id="customs_value_logic",result="pass",detail="12600 − 450 (Art. 305) = 12150.00 USD"),dict(check_id="origin",result="pass",detail="TR"),dict(check_id="invoice_annex1a",result="pass",detail="all 12 items present (HS present but wrong subheading)"),dict(check_id="dates",result="pass",detail="20.08 ≤ 02.11 ≤ 03.11 ≤ 19.11 ≤ 24.11")],
 seeded=[dict(check_id="pkg_count",what="CMR box 7 says 118 packages; invoice and packing list say 120",expected_severity="error_blocking",fix="Recount at unloading; corrected CMR or carrier act; if 2 cartons really missing → declare 5 900 pcs and use VMQ 605 cl. 30 amendment route"),
   dict(check_id="gross_weight_docs",what="CMR box 11 gross 1 430 kg vs packing list 1 344 kg (+6.4%)",expected_severity="error_blocking",fix="Ask carrier; weigh if needed; do not copy CMR weight into grafa 35"),
   dict(check_id="hs_prefix",what="Seller HS 6109.90 vs composition 100% cotton (→ 6109.10)",expected_severity="warning_ack",fix="Declare 6109100000 with reason; same duty row (6109 → 20% / 0.5 USD) so no payment impact, but description must match")],
 outcome="BLOCKED at review: 2 blocking errors + 1 warning. After a corrected CMR (120 pkgs, 1 344 kg) and acknowledging the HS warning, the expected GTD values below apply.",
 deadline="Presented 21.11.2026 (Sat) → day 15 conservative = 05.12.2026 (Sat) → shifted to Mon 07.12.2026 if the post is closed at weekends; legal max reading also 07.12.2026. See deadlines.json.")
BUY_C=dict(name="«TEXNO UY SAVDO» MChJ (SYNTHETIC)",address="Ташкентская обл., Ташкентский р-н, пос. Келес, ул. Навои, 5 (SYNTHETIC)",tin="100000003",district_code="1727265",phone="+998 71 000 00 03",email="info@texnouy.example")
BUY_C_INV={k:v for k,v in BUY_C.items() if k!='phone'}
C=dict(id="set-C-electronics-cn-truck",title="Set C – Microwave ovens + LED lamps from China by truck (CNY contract; 2 seeded issues)",currency="CNY",cur_code="156",origin_code="156",origin_name="China",dispatch_ru="КИТАЙ",
 scenario="Appliance shop imports microwave ovens and LED bulbs from Ningbo, DAP Yallama (border), contract in CNY, enters at Yallama, cleared at Keles. Packing list under-states LED quantity; invoice lacks buyer phone (VMQ 605 Annex 1a item 2). Shows: non-USD currency, fee band via USD equivalent, specific minimum (5 USD/pc) for microwaves.",
 seller=dict(name="Ningbo Hanshi Electric Appliance Co., Ltd. (SYNTHETIC)",address="No. 66 Kexue Rd, Yinzhou, Ningbo, Zhejiang, China",tin="91330212SYNTH0003",country_ru="Китай"),
 buyer=BUY_C,buyer_inv=BUY_C_INV,contract_no="HS-UZ-2026/03",contract_date="2026-09-15",contract_id="2026-UZ-000000789 (SYNTHETIC)",inv_no="HS-INV-26-0311",inv_date="2026-10-25",pl_no="HS-PL-26-0311",
 incoterms_inv="DAP Yallama border crossing, Uzbekistan (Incoterms 2010)",payment_terms="100% prepayment by T/T",payment_form="10/01",g20="14 | DAP Яллама | 10/01",
 items=[dict(no=1,code="8516500000",desc_en="Microwave oven, 20 L, 700 W, mechanical control, 220 V",desc_ru="Печь микроволновая бытовая, 20 л, 700 Вт, механическое управление, 220 В, модель MW-20S, бренд HANSHI",brand="HANSHI",model="MW-20S",inv_hs="8516.50",qty=D(300),unit="pcs",unit_ru="шт",price=D('260.00'),net=D('3150.000'),gross=D('3690.000'),pk_inv=300,pk_type="cartons",pk_type_ru="картонные коробки",marks="HS-MW 1-300",
     hs_reasoning="Electro-thermic domestic appliance → 8516; microwave ovens → 8516 50 → 8516 50 000 0. ⚠️ Energy-efficiency class may be required in grafa 31 if microwaves are in the CM Res. 86/2015 annex – not verified."),
   dict(no=2,code="8539520009",desc_en="LED lamp bulb A60, E27, 9 W, 806 lm, 6500 K (SMD chips, not filament)",desc_ru="Лампа светодиодная A60, цоколь E27, 9 Вт, 806 лм, 6500 K, SMD (не филаментная), модель LB-9W, бренд HANSHI",brand="HANSHI",model="LB-9W",inv_hs="8539.52",qty=D(2400),unit="pcs",unit_ru="шт",price=D('4.50'),net=D('84.000'),gross=D('108.000'),pk_inv=24,pk_type="cartons, 100 pcs each",pk_type_ru="картонные коробки",marks="HS-LB 301-324",pl_qty=D(2000),pl_pk=20,pl_net=D('70.000'),pl_gross=D('90.000'),
     hs_reasoning="LED light source/lamp → 8539 52; not phosphor-coated filament with ≥24 LEDs (…1), not straight tube ≥25 mm (…2) → 8539 52 000 9 (data/tariff notes 8539520000 does not exist).")],
 cmr_no="CN-KZ-UZ-44120",cmr_date="2026-10-28",cmr_takeover="Ningbo, China, 28.10.2026",cmr_delivery="Keles, Tashkent region, Uzbekistan",cmr_packages=324,cmr_gross=D('3798'),cmr_hs="851650; 853952",cmr_goods="Microwave ovens; LED lamps",marks_cmr="HS 1-324",cmr_m3="31.2",
 cmr_value_per_code={"851650":"78000.00 CNY","853952":"10800.00 CNY"},carrier="«TASHKENT EXPRESS CARGO» MChJ (SYNTHETIC)",truck="10A777CA",trailer="10XZ321",truck_country="860",
 border_post=dict(code="27001",name="Яллама"),border_date="2026-11-14",border_date_ddmmyyyy="14.11.2026",
 td=dict(number="27001/14.11.2026/0007788",type="ТД",from_post="27001",to_post="27020",item_for={1:1,2:2},note="SYNTHETIC"),
 dest_post=dict(code="27020",name="Келес"),presented="2026-11-16",confirmed="2026-11-16T09:20+05:00",goods_location="Ташкентская обл., Ташкентский р-н, зона таможенного контроля поста «Келес» (SYNTHETIC address)",goods_location_district="1727265",
 coo=dict(code="701 СПТИМ",number="CCPIT-SYN-2026-0003",date="2026-10-26",country="China",note="SYNTHETIC"),
 certs=[dict(code="417 ССТ",number="UZ.SMT.SYN.0001 (SYNTHETIC)",scope="microwave ovens, LED lamps",note="Whether a conformity certificate is mandatory for these codes was NOT verified – check Single Window / mandatory certification list ⚠️. Included only to show grafa 44 format.")],
 resp=dict(name="Rahimov Jasur Olimovich (SYNTHETIC)",position="директор",phone="+998 90 000 00 03",pinfl="50000000000003"),place="Ташкентская обл., Келес",filing_date_ddmmyyyy="18.11.2026",own_serial="000041",
 g44="202 СМР № CN-KZ-UZ-44120 от 28.10.2026\n220 ИНВ № HS-INV-26-0311 от 25.10.2026 (corrected)\n222 УПЛИСТ № HS-PL-26-0311 от 25.10.2026 (corrected)\n301 КНТ № HS-UZ-2026/03 от 15.09.2026\n417 ССТ № UZ.SMT.SYN.0001 (SYNTHETIC; requirement unverified)\n701 СПТИМ № CCPIT-SYN-2026-0003 от 26.10.2026",
 assumptions=["Invoice and CMR are correct (2 400 LED lamps, 24 cartons, 324 packages); packing list line 2 is the error.","DAP Yallama = delivered to the place of entry, so no Art. 304 add-back; CV = invoice value.","Fee band uses USD equivalent via UZS cross-rate: 88 800 CNY × 1 700 / 12 100 = 12 476.03 USD → band 10–20k (ASSUMPTION on conversion, see data/tariff/fees.json).","Microwave: 10% × 132 600 000 = 13 260 000 UZS < 5 USD × 300 × 12 100 = 18 150 000 UZS → specific minimum applies."],
 expected_checks=[dict(check_id="qty_supp_unit",result="FAIL – error_blocking",detail="LED lamps: invoice 2400 vs packing list 2000"),dict(check_id="pkg_count",result="FAIL – error_blocking",detail="invoice 324 = CMR 324 vs packing list 320"),
   dict(check_id="gross_weight_docs",result="WARN – warning_ack",detail="packing list 3780 kg vs CMR/invoice 3798 kg: 18 kg = 0.47%; T = max(1% × 3798, 20) = 37.98 kg → 1 < 18 ≤ 37.98 (proposal band → explain)"),dict(check_id="net_weight_docs",result="FAIL – error_blocking",detail="LED net: invoice 84 kg vs packing list 70 kg (14 kg = 16.7%; per-line T = max(0.5% × 84, 5) = 5 kg → 14 > 5; total 3234 vs 3220 would only warn, worst severity wins)"),
   dict(check_id="invoice_annex1a",result="FAIL – error_blocking",detail="buyer phone number missing (Annex 1a item 2)"),dict(check_id="value_sum",result="pass",detail="78000 + 10800 = 88800.00 CNY"),dict(check_id="hs_prefix",result="pass",detail="851650 / 853952 match"),
   dict(check_id="origin",result="pass",detail="CN"),dict(check_id="currency_incoterms",result="pass",detail="CNY, DAP"),dict(check_id="customs_value_logic",result="pass",detail="DAP border → CV = invoice"),dict(check_id="dates",result="pass",detail="15.09 ≤ 25.10 ≤ 28.10 ≤ 14.11 ≤ 18.11")],
 seeded=[dict(check_id="qty_supp_unit / pkg_count / net_weight_docs",what="Packing list line 2 shows 2 000 LED lamps in 20 cartons (70 kg net / 90 kg gross) instead of 2 400 in 24 cartons (84 / 108)",expected_severity="error_blocking",fix="Get a corrected packing list from the seller (one root cause, three failed checks – UI should group them)"),
   dict(check_id="invoice_annex1a",what="Invoice buyer block has no phone number (VMQ 605 Annex 1a item 2 requires name, legal address, TIN and phone)",expected_severity="error_blocking",fix="Corrected invoice from the seller")],
 outcome="BLOCKED at review: 4 blocking errors from 2 root causes + 1 weight warning. After corrected packing list and invoice, the expected GTD values below apply.",
 deadline="Presented 16.11.2026 (Mon) → file by 30.11.2026 (conservative) / legal max 01.12.2026 (next-day reading).")
keys=[build(x) for x in (A,B,C)]
summ=[dict(set=k['set_id'],outcome=k['expected_outcome'],totals=k['payments']['totals']) for k in keys]
json.dump(dict(_synthetic=SYN,rates_note=RATE_NOTE,sets=summ),open(f"{OUT}/index.json",'w'),ensure_ascii=False,indent=2)
for s in summ: print(s['set'],s['totals'])
