# EK10 (export) grafa map from Instruction 2773 ch.4 points 20-22. Generated 2026-11-18 (Asia/Tashkent).
import json, re, sys
sys.path.insert(0,'/workspace/bojxona')
OUT='/workspace/hackathon/data/declarant/'
UZ_DOC="https://lex.uz/uz/docs/2924955"; RU_DOC="https://lex.uz/docs/2924953"; BK="https://lex.uz/docs/2876354"
S=json.load(open('/workspace/bojxona/ch4_split.json'))      # parsed from ru.html / y.html (lex.uz element ids)
IM=json.load(open(OUT+'grafa-map.json')); IMG={g['grafa']:g for g in IM['grafas']}
def tr(s):
    m={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'j','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'x','ц':'ts','ч':'ch','ш':'sh','ъ':'ʼ','ь':'','э':'e','ю':'yu','я':'ya','ў':'oʻ','қ':'q','ғ':'gʻ','ҳ':'h'}
    o=''
    for i,ch in enumerate(s):
        lo=ch.lower()
        if lo in m:
            r=m[lo]
            if lo=='е' and (i==0 or not s[i-1].isalpha()): r='ye'
            if ch.isupper(): r=r.upper() if (i+1<len(s) and s[i+1].isupper()) else r[:1].upper()+r[1:]
            o+=r
        else: o+=ch
    return o
KEY={'17a':'17а','C':'«С»'}
def head(g):
    k=KEY.get(g,g); ru=S['ru'][k]; uz=S['uz'][KEY.get(g,g) if g!='C' else 'C']
    nr=' / '.join(x for x in re.findall(r'«([^»]+)»',ru['head']) if x!='С') or None
    nu=' / '.join(x for x in re.findall(r'«([^»]+)»',uz['head']) if x!='С') or None
    sub=ru['head'].split(')')[0]
    return nu,nr,f"{UZ_DOC}#{uz['id']}",f"{RU_DOC}#{ru['id']}",sub
G=[]
def add(g,level,fmt,rule,src,diff,example=None,classifier=None,checks=None,notes=None,filled_by="declarant",uncertain=None,same=False):
    nu,nr,uu,ur,sub=head(g)
    untitled=False
    if nu is None:
        untitled=True; h={'13':'(untitled) USD/UZS rate','43':'(untitled) own-production flag','C':'«С» (untitled)'}[g]; nu=nr=h
    G.append(dict(grafa=g,name_uz_cyrl=nu,name_uz_latn=tr(nu),name_ru=nr,untitled_in_official_text=untitled or None,level=level,filled_by=filled_by,
      format=fmt,rule_en=rule,source_documents=src,classifier=classifier,example=example,cross_checks=checks or [],notes=notes,uncertain=uncertain,
      vs_im40=dict(status=diff[0],difference=diff[1]),
      legal_source=dict(doc="Instruction No. 2773 (06.04.2016) on filling the BYD/GTD",point=f"Ch.4, point 22, sub-point {sub}",url_uz=uu,url_ru=ur)))
def reuse(g,diff=("same","Same text as IM40 (ch.5 p.25), apart from cross-references."),example=None,checks=None,notes=None,uncertain=None):
    m=IMG[g]
    add(g,m['level'],m['format'],m['rule_en'],m['source_documents'],diff,example=example,classifier=m['classifier'],
        checks=m['cross_checks'] if checks is None else checks,notes=m['notes'] if notes is None else notes,filled_by=m['filled_by'],uncertain=uncertain)
SY=" (SYNTHETIC)"
add('1','header','3 subfields: [ЭК] [2-digit regime code] [empty]',"Subfield 1: direction 'ЭК'. Subfield 2: two-digit regime code per Annex 3 (export = 10). Subfield 3 is not filled.",["calculated"],("different","Direction 'ЭК' instead of 'ИМ'; regime 10 instead of 40."),example="ЭК | 10 |",classifier="Annex 3 – customs regimes (10 = export; https://lex.uz/docs/2924953#2928883)")
add('2','header','free text, e-GTD separate fields + upper-right code after № + bottom: № TIN/PINFL / district code',
 "Consignor AND exporter (Uzbek side). Same person: individual – full name, permanent address, phone; legal entity – short name, legal address, phone, e-mail (if any). A branch acting for the exporter: branch details, then the legal entity's details. Different persons (consignor ships on the exporter's instruction): consignor name, address, phone, then 'по поручению' + exporter name and address; if grafa 9 already shows the exporter, it need not be repeated here. Upper-right after '№': 00000001 resident individual, 00000002 non-resident individual, 00000003 organisation with state share, 99999999 diplomatic/consular, 88888888 international/government organisation offices, otherwise empty. Bottom after '№': consignor TIN (PINFL for an individual; branch TIN if a branch acts) '/' district (city) code per Annex 15 by legal address; no TIN/PINFL → 999999999. Not filled on additional paper sheets.",
 ["contract","invoice","company_profile"],("different","IM40 grafa 2 = FOREIGN consignor (no TIN/district). In EK10 grafa 2 is the UZBEK consignor/exporter with the upper-right status code and the bottom TIN/PINFL + district code (those fields sit in grafa 8 for IM40)."),
 example="«PAXTA TEKS» MChJ"+SY+", Ташкентская обл., Ташкентский р-н, ул. Навои 1, тел. +998 71 000 00 00 | № 100000009/1727265",classifier="Annex 15 – districts and cities",checks=["= seller in contract and invoice","TIN 9 digits / PINFL 14 digits","district code exists in Annex 15"])
reuse('3',example="1/1 (1 item)")
reuse('5',example="1")
add('7','header','5-digit post code (declarant); customs appends /DD.MM.YYYY/serial',"5-digit code (Annex 4) of the customs post where the GTD WILL BE filed. Customs completes the registration number (point 90).",["user_input"],("same","Same as IM40."),example="26010 (declarant)",classifier="Annex 4 – customs posts",filled_by="declarant+customs")
add('8','header','free text; e-GTD separate fields per party',"Person named as consignee in the transport documents (foreign buyer side): individual – full name, residence (country short name per Annex 5 + address); legal entity – short name and location (country short name + address). If the consignee receives on behalf of another person: consignee first, then 'по поручению' + that person. E-GTD: consignee, the person on whose behalf it receives (the contract party with the grafa-9 person) and other persons from the accompanying documents each in its own field. Not filled on additional paper sheets.",
 ["cmr","contract","invoice"],("different","IM40 grafa 8 = Uzbek importer with status code and TIN/district. EK10 grafa 8 = FOREIGN consignee: name + country + address only – the text read has NO TIN/district bottom part and no upper-right status code."),
 example="TOO «Almaty Textile Trade»"+SY+", Казахстан, г. Алматы, пр. Абая 100",checks=["= CMR box 2 consignee","= buyer in contract (or 'по поручению' chain)"],uncertain="Whether the live ed2 form still shows a TIN field for the foreign consignee – not described in point 22 ⚠️.")
reuse('9',diff=("same","Same text as IM40; in practice this is the Uzbek exporter (contract party)."),example="«PAXTA TEKS» MChJ"+SY+" | № 100000009/1727265",checks=["= seller/exporter in contract","= grafa 2 exporter (if same person)"])
reuse('11',diff=("same","Same text; here it is the BUYER's country."),example="398 | 2",checks=["buyer country in contract = code"])
reuse('12'); reuse('13')
reuse('14',example="«PAXTA TEKS» MChJ"+SY+" | № 100000009")
add('17','header','country short name (Annex 5)',"Short name of the country of destination = the last country to which the goods are to be delivered.",["contract","cmr"],("ek10_only","Not used for IM40 (IM40 uses 15/15a country of dispatch instead)."),example="Казахстан",classifier="Annex 5 – countries")
add('17a','header','3-digit numeric (Annex 5)',"Numeric code of the destination country.",["contract","cmr"],("ek10_only","Not used for IM40."),example="398",classifier="Annex 5 – countries",checks=["= code of grafa 17 name"])
add('18','header','left: "<count> <TRANSPORT>: plate[/trailer]; ..."; right: country code; e-GTD extra fields',
 "Vehicle(s) on which the goods are loaded for delivery to the border crossing point (or, if transhipped before the border, to the transhipment place). Left: number of vehicles, space, short transport name (Annex 6), colon, identifiers separated by ';' (vessel name, flight, wagon no., plate …); road trains: trailers after '/'. Right: numeric country code of the vehicle (of the tractor unit for road trains); several countries → '999' (paper: 'см. на обороте'; e-GTD: no reference, all data in fields). Pipeline / power line: 'ТРУБОПРОВОД' / 'ЛЭП'. Additionally (e-GTD separate fields): gross kg of goods in the vehicle; 2-digit vehicle type code (10 car ≤8 seats, 21 truck ≤10 t, 22 truck 10–20 t, 23 truck >20 t, 31/32/33 buses by seats, 40 minibus, 50 tractor, 60 motorcycle, 70 special); VIN; numeric code of the country where carriage ends; carrier (individual: full name, PINFL, passport series/no.; legal entity: name, TIN) and driver (full name, PINFL, passport). Non-resident carrier/driver without TIN/PINFL → '99999999999999'.",
 ["cmr","transport_order","user_input"],("different","IM40 grafa 18 = vehicle that carried the goods inside Uzbekistan to the clearing post, without the extra carrier/driver/VIN/vehicle-type fields. EK10 adds gross-in-vehicle, vehicle type code, VIN, end-of-carriage country, carrier and driver identity (sub-point 14 as amended by 2773-9, 2023)."),
 example="1 АВТО: 10A123BC/10XY456 | 860; extra: 18450.000 кг; 23; VIN XTC00000000000000; 398; carrier «TRANS YO'L» MChJ"+SY+" TIN 100000010; driver Rahimov Bobur"+SY+", PINFL 30000000000000, AA0000000",classifier="Annex 6 – transport types; Annex 5 – countries",checks=["plate = CMR box 25","gross in vehicle ≥ Σ grafa 35 of this GTD"],uncertain="The vehicle-type code list in the text read ends at '70'; check ed2 for further codes ⚠️.")
reuse('19',example="0")
add('20','header','3 subfields: [numeric Incoterms code] [letter code + place] [settlement form/dispatch form]',
 "1st: numeric delivery-terms code (Annex 7). 2nd: letter code + geographic place. 3rd (per contract): 2-digit settlement form, '/', 2-digit dispatch form (separate e-GTD fields). Settlement form: 10 prepayment; 20 letter of credit; 30 bank guarantee; 40 export-contract insurance policy (political & commercial risks); 50 payment after export; 60 consignment; 70 barter; 80 free-of-charge. Mixed forms → the one with the largest absolute amount. Dispatch form: 01 goods sent directly to the contract party; 02 not sent directly to the contract party. Gratuitous supplies: terms from accompanying documents.",
 ["contract","invoice"],("different","EK10-only third subfield: settlement-form code + dispatch-form code. IM40 grafa 20 has no such subfield."),example="02 | FCA Ташкентский р-н | 10/01",classifier="Annex 7 – delivery terms",checks=["Incoterms = contract = invoice","settlement form consistent with contract payment terms"],uncertain="No Annex 7 code for Incoterms 2020 DPU (same issue as IM40) ⚠️.")
reuse('22',example="840 | 24000.00"); reuse('23',example="1/12100,00 (EXAMPLE rate, not CBU)"); reuse('24',example="01 | 840")
add('25','header','2-digit code (Annex 6)',"Transport type code of the vehicle on which the goods WILL actually cross the Uzbek customs border.",["cmr","user_input"],("different","IM40: code of the grafa-21 vehicle that DID cross (not filled for change of regime). EK10 has no grafa 21; grafa 25 is the planned border-crossing vehicle type."),example="30",classifier="Annex 6 – transport types")
reuse('26',example="30"); reuse('28')
add('29','header','5-digit code + name (Annex 4)',"Code and name of the customs post through which the goods WILL leave Uzbekistan. Pipeline / power line: the control post.",["user_input","cmr"],("different","IM40: entry post (already crossed). EK10: planned exit post."),example="27001 Яллама",classifier="Annex 4 – customs posts")
reuse('30',example="Ташкентская обл., Ташкентский р-н, ул. Навои 1 (склад экспортёра)"+SY+" | 1727265")
add('31','item','numbered lines 1–5 + bottom-left producer TIN/district + bottom-right supplementary quantity',
 "Description sufficient for unambiguous 10-digit classification; each element on a new numbered line. 1: trade name, trademark/brand, model, article, grade, standards, technical and commercial characteristics, composition (e-GTD: brand in separate field; 'без марки'/'без бренда' if none); parameters in other units and production date if needed for payments or prohibitions/restrictions. The generic heading text of the TN VED is not allowed. 2: packages – number of packages, packing type and number of packings ('часть коробки' if not whole); bulk: 01 насыпью, 02 навалом, 03 наливом; not filled for pipeline/power line. 3: container numbers ('часть' if partly). 4: excise stamps – series, numbers (ranges with hyphen) and quantity. 5: pipeline/power line: 'Поставка в период с … по …'. Bottom-left (separate field): TIN (PINFL) of the PRODUCER (manufacturer/grower) '/' district code (Annex 15) by legal address; for HS 07, 08, 0904, 1202, 1008, 1207409000, 2008191900 the district where the produce was GROWN per the phytosanitary certificate – one item per district if several. Producer unknown or several producers → consignor's TIN (PINFL) and territory code. Bottom-right: quantity in supplementary unit + symbol (code in grafa 41; e-GTD quantity only); 2 decimals, <0.01 → 6 decimals; kg-only codes → empty.",
 ["invoice","packing_list","classification","company_profile","phytosanitary_certificate"],("different","IM40 grafa 31 has lines 1–11 (incl. energy-efficiency class etc.) and the bottom-left shows the importer/consumer side. EK10: lines 1–5; bottom-left = PRODUCER TIN/district (growing district for listed agri codes)."),
 example="1) Футболка мужская трикотажная, 100% хлопок, модель PT-01, бренд PAXTA TEKS\n2) 200 мест, картонные коробки\n | 100000009/1727265 | 4000 шт",checks=["packages = packing list = CMR","quantity = invoice = packing list","producer TIN present"],uncertain="Lines 6–11 of IM40 are absent from point 22 in the edition read; confirm ed2 does not require them for EK10 ⚠️.")
reuse('32',example="1")
reuse('33',example="6109100000",notes="Right part of grafa 33 is not described in point 22 for EK10 – leave empty unless the cabinet requires it ⚠️.",checks=["code exists in the TN VED","first 6 digits vs invoice HS – warn on mismatch"])
reuse('34',example="860",checks=["= certificate of origin (702 СПТЭК) country, if issued","= invoice origin"],notes="For own-produced Uzbek goods normally 860 (UZ).")
reuse('35',example="2150.000",notes="Gross excludes containers and other transport equipment (sub-point 30); pallets not stated ⚠️.")
add('37','item','7 digits',"Procedure code = declared regime (2 digits, Annex 3) + previous regime (2 digits; '00' if none) + movement-feature code (3 digits, Annex 11).",["calculated"],("different","Starts with 10 instead of 40. The IM40 text's remark that customs transit counts as 'no previous regime' is not repeated in point 22 (sub-point 32)."),example="1000000",classifier="Annex 3, Annex 11",uncertain="'000' = no movement feature is our reading of Annex 11 (as for IM40) ⚠️.")
reuse('38',example="2000.000",checks=["net ≤ gross","= packing list net","= invoice net"])
reuse('39',example="(empty)")
add('40','item','"ГТД post/date/number — item — gross kg — net kg — supp qty"',"Only if the goods were under ANOTHER customs regime before export: code 'ГТД', previous GTD registration number, item number (grafa 32), gross kg, net kg, supplementary quantity + symbol. Goods previously split over several GTDs → one line per GTD. Example from the text: 'ГТД 14010/31.03.2012/0353761 — 2 — 5980 кг — 5900 кг — 250,2 м3'.",
 ["previous_gtd"],("different","IM40 grafa 40 almost always holds the transit document (ТД …) or delivery-control book (ККДГ/МДП). EK10 grafa 40 only refers to a previous GTD; for goods produced in Uzbekistan it stays empty (our reading)."),example="(empty – own production, no previous regime)",uncertain="'Empty when no previous regime' is our reading of 'Если товары до заявляемого таможенного режима были помещены…' – confirm on ed2 ⚠️.")
reuse('41',example="796 (шт) ⚠️ verify unit code")
reuse('42',example="24000.00")
add('43','item','0 or 1',"'0' – the consignor exports goods NOT of its own production; '1' – the consignor exports goods of its OWN production.",["company_profile","user_input"],("different","Same box, different meaning: IM40 '1' = imported for own needs / '0' = not for own needs. EK10 '1' = exporter is the manufacturer / '0' = not the manufacturer."),example="1",checks=["if 1: grafa 31 bottom-left producer TIN should equal grafa 2 TIN"],uncertain="The rule speaks of the 'грузоотправитель' (consignor); if consignor ≠ exporter, which party's production counts is not stated ⚠️.")
add('44','item','one document per line: "<code> <short> № ... от DD.MM.YYYY"',
 "Documents for each item with Annex-12 code (each on a new line): a) licence (101 ЛИЦЕНЗИЯ … срок); b) transport and commercial documents (e.g. 202 СМР, 205 АВИА, 220 ИНВ); c) contract (301 КНТ) and the transport contract with a non-resident carrier + its e-system ID; d) permits/certificates of other authorities (417 ССТ, 419 ФТСС phytosanitary …); e) registration of the contract / individual-entrepreneur certificate (501, 502); f) benefit: '6' + payment code (Annex 13) + Annex-14 act code (empty if no exemption or no rate); g) certificate of origin – export example 702 СПТЭК; h) other documents (deferral, commission/pledge contract, fine decision or 'form-2', etc.).",
 ["contract","invoice","cmr","certificates","certificate_of_origin"],("similar","Same lettered structure a)–h) as IM40; export-specific examples: 702 СПТЭК (export certificate of origin) instead of 701 СПТИМ, 419 ФТСС phytosanitary certificate. Code 904 МЕТОД: see grafa-map.json (IM40) note – not mentioned for EK10 either ⚠️."),
 example="202 СМР № UZ-KZ-0001 от 10.12.2026\n220 ИНВ № PT-2026-001 от 09.12.2026\n301 КНТ № PT-KZ/01 от 01.10.2026\n702 СПТЭК № UZKZ00000000 от 09.12.2026"+SY,classifier="Annex 12 – document types; Annex 13; Annex 14",checks=["contract, invoice and CMR present","certificate of origin present if buyer needs preference"])
add('45','item','decimal(2), contract currency (right subfield)',"Right subfield: customs value of the item in the contract currency (gratuitous / no contract → currency of accompanying documents), determined under the Customs Code. Rounded to 2 decimals.",["invoice","calculated"],("similar","Same format; for export the Customs Code rules for EXPORTED goods apply – our pointer: Arts. 315–317 ("+BK+"), not the import methods 302–313."),example="24000.00",uncertain="Left subfield not described (as for IM40) ⚠️.")
add('46','item','decimal(3), thousand USD',"Statistical value in thousand USD, converted from grafa 45 at the CBU rate on the GTD acceptance date, rounded to 3 decimals.",["calculated","cbu_rate"],("same","Same rule as IM40 (wording differs slightly)."),example="24.000")
add('47','item','table rows: Вид | Основа начисления | Ставка | Сумма | СП',"Per item and per payment type; the clearance fee always on the main sheet / item 1. 'Вид' = Annex 13 code – for export typically 10 (clearance fee); 25 export customs duty and 28 excise on exported goods only where a rate is set. 'Основа' in UZS (grafa 12/45 at CBU rate on acceptance date) unless set in foreign currency or non-money units. 'Ставка' = applied rate. 'Сумма' in UZS (or foreign currency if law requires). 'СП' codes as IM40 (БН, КТ, … ОП deferral, РП instalments, ВЗ VAT offset, ОО no payment). No row if no rate, zero rate, or the regime creates no obligation.",
 ["calculated","fee_table"],("similar","Same columns/СП codes. Payment codes differ: import duty 20/21, import excise 27 and VAT 29 do not arise for export; export duty 25 / export excise 28 only where rates exist (Annex 13: https://lex.uz/docs/2924953#8356110)."),example="10 | 1 ГТД | <fee per VM 55 band> | … | БН",classifier="Annex 13 – customs payments",uncertain="Export clearance fee band/amount not re-checked here – use data/tariff/fees.json and confirm it applies to export ⚠️.")
add('48','item','"XX.DD.MM.YYYY" per payment; instalments "ПН.ХХ.ДД.ММ.ГГГГ.СУММА"',"Deferral: payment code + final due date per payment type, one line each. Instalments: month no., payment code, due date, amount per instalment, one line each.",["customs_decision"],("same","Same scheme as IM40 (amendments 2773-10 / 2773-12)."),example="(empty)")
reuse('49',example="(empty)"); reuse('50'); reuse('54')
add('C','header','line 1 only',"1: identification number of the foreign-trade contract in the Unified Electronic Information System of Foreign Trade Operations.",["contract"],("different","IM40 grafa C has a 2nd line (date of import = border stamp date). EK10 has only line 1."),example="1) 0000000000"+SY)
ru_order=[ (KEY.get(g['grafa'],g['grafa'])) for g in G]
meta=dict(title="BYD (GTD) grafa map for EK10 – export",generated="2026-11-18",tz="Asia/Tashkent",
 synthetic_examples="All example values are SYNTHETIC (fictitious exporter «PAXTA TEKS», buyer in Almaty, TINs, plates, numbers). Exchange rate is an EXAMPLE, not CBU data.",
 source=dict(name_ru=IM['meta']['source']['name_ru'],name_uz=IM['meta']['source']['name_uz'],url_uz=UZ_DOC,url_ru=RU_DOC,edition_read=IM['meta']['source']['edition_read'],
   chapter="Ch. 4 (points 20–22) – export",chapter_url_ru=f"{RU_DOC}#2925168",chapter_url_uz=f"{UZ_DOC}#2925089",
   point20_url_ru=f"{RU_DOC}#2925169",point20_url_uz=f"{UZ_DOC}#2925742",point21_list_url_ru=f"{RU_DOC}#4303369",point21_list_url_uz=f"{UZ_DOC}#4294922",point22_url_ru=f"{RU_DOC}#3908316",point22_url_uz=f"{UZ_DOC}#3854674",
   customs_filled_point89_url_ru=IM['meta']['source']['customs_filled_point89_url_ru'],regime_code_annex3_ru=f"{RU_DOC}#2928883"),
 point21_list="1, 2, 3, 5, 7 (post code), 8, 9, 11, 12, 13, 14, 17, 17a, 18, 19, 20, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 54, «С»",
 related_law=dict(export_regime="Customs Code Arts. 29–31 (export regime, conditions, documents) – "+BK,export_documents="Customs Code Art. 19 (documents on exit) – "+BK,export_valuation="Customs Code Arts. 315–317 – "+BK),
 anchor_note=IM['meta']['anchor_note'],uz_latin_note=IM['meta']['uz_latin_note'],
 subpoint_note="Point 22 sub-points 17, 31 and 47 are absent in the edition read (numbering jumps 16→18, 30→32, 46→48); presumably repealed or empty ⚠️.")
im40=set(IMG); ek=set(g['grafa'] for g in G)
diff_summary=dict(
 only_im40=sorted(im40-ek,key=lambda x:(len(x),x)),only_ek10=sorted(ek-im40),
 changed=[dict(grafa=g['grafa'],difference=g['vs_im40']['difference']) for g in G if g['vs_im40']['status'] in('different','similar')],
 same=[g['grafa'] for g in G if g['vs_im40']['status']=='same'])
out=dict(meta=meta,general_rules_note="General rules of ch.1 (points 4–14: one GTD per transport document, ≤100 items, item definition, Latin script, etc.) apply as in grafa-map.json (IM40).",
 grafas=G,diff_vs_im40=diff_summary,
 not_filled_by_declarant_for_ek10="Every grafa not in the point-21 list (e.g. 4, 6, 10, 15, 15a, 16, 21, 27, 36, 51–53) is not filled by the declaring person for EK10.",
 customs_only=IM['customs_only'],classifiers=IM['classifiers'])
json.dump(out,open(OUT+'grafa-map-ek10.json','w'),ensure_ascii=False,indent=2)
esc=lambda s:(s or '').replace('|','\\|').replace('\n','<br>')
L=[f"# {meta['title']}","","*Generated 2026-11-18 (Asia/Tashkent). Machine-readable twin: `grafa-map-ek10.json`. Import counterpart: `grafa-map.md`. Examples are **SYNTHETIC**.*","",
 f"**Legal source:** Instruction No. 2773, Chapter 4, points 20–22 – [ch.4 uz]({meta['source']['chapter_url_uz']}) · [ch.4 ru]({meta['source']['chapter_url_ru']}); point 21 list [uz]({meta['source']['point21_list_url_uz']}) · [ru]({meta['source']['point21_list_url_ru']}); point 22 [uz]({meta['source']['point22_url_uz']}) · [ru]({meta['source']['point22_url_ru']}). Edition: {meta['source']['edition_read']}. Regime code 10 = export (Annex 3, [ru]({meta['source']['regime_code_annex3_ru']})).","",
 f"**Point 21 – grafas filled by the declaring person for EK10:** {meta['point21_list']}.","",
 "> Uzbek names are the official Cyrillic headings; Latin = mechanical transliteration (not official). Anchors are lex.uz element ids. ⚠️ = uncertain / our reading.","",
 "## Differences vs IM40 (highlight)","",
 f"- **Only in IM40:** {', '.join(diff_summary['only_im40'])} (country of dispatch, border vehicle).",
 f"- **Only in EK10:** {', '.join(diff_summary['only_ek10'])} (country of destination name / code).",""]
L+=["| Grafa | IM40 → EK10 |","|---|---|"]+[f"| **{d['grafa']}** | {esc(d['difference'])} |" for d in diff_summary['changed']]
L+=["",f"- **Same as IM40:** {', '.join(diff_summary['same'])}.","","## Grafa table","","| Grafa | Name (uz) | Name (ru) | vs IM40 | Format | Source docs | Example (synthetic) | Rule source |","|---|---|---|---|---|---|---|---|"]
for g in G:
    ls=g['legal_source']; st={'same':'same','similar':'≈ similar','different':'**DIFFERENT**','ek10_only':'**EK10 only**'}[g['vs_im40']['status']]
    L.append(f"| **{g['grafa']}** | {esc(g['name_uz_cyrl'])}<br>*{esc(g['name_uz_latn'])}* | {esc(g['name_ru'])} | {st} | {esc(g['format'])} | {', '.join(g['source_documents'])} | {esc(g['example'])} | [uz]({ls['url_uz']}) · [ru]({ls['url_ru']}) ({ls['point']}) |")
L+=["","## Filling rules per grafa (summary of the official text, EK10)",""]
for g in G:
    L.append(f"### Grafa {g['grafa']} — {g['name_ru']} / {g['name_uz_latn']}")
    L.append(f"- **Rule:** {g['rule_en']}")
    if g['vs_im40']['status']!='same': L.append(f"- **vs IM40 ({g['vs_im40']['status']}):** {g['vs_im40']['difference']}")
    if g['classifier']: L.append(f"- **Classifier:** {g['classifier']}")
    if g['cross_checks']: L.append("- **Checks:** "+'; '.join(g['cross_checks']))
    if g['notes']: L.append(f"- **Notes:** {g['notes']}")
    if g['uncertain']: L.append(f"- ⚠️ **Uncertain:** {g['uncertain']}")
    L.append(f"- **Source:** {g['legal_source']['point']} — [uz]({g['legal_source']['url_uz']}), [ru]({g['legal_source']['url_ru']})"); L.append("")
L+=["## Not filled by the declarant for EK10","",out['not_filled_by_declarant_for_ek10'],"","## Filled by customs only (same as IM40, points 89–90)",""]+[f"- **{c['grafa']}**: {c['rule']}" for c in out['customs_only']]
L+=["","## Related law (lex.uz)",""]+[f"- {v}" for v in meta['related_law'].values()]
L+=["","## Uncertainties","",f"- {meta['subpoint_note']}"]+[f"- Grafa {g['grafa']}: {g['uncertain']}" for g in G if g['uncertain']]
open(OUT+'grafa-map-ek10.md','w').write('\n'.join(L))
print(len(G),diff_summary['only_im40'],diff_summary['only_ek10'])
