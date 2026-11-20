// Tailwind v3: merge into tailwind.config.js
module.exports = {
  "theme": {
    "extend": {
      "colors": {
        "primary": {
          "50": "#ECEBFA",
          "100": "#DEDDF6",
          "200": "#C3C1EF",
          "300": "#9F9CE3",
          "400": "#7672D2",
          "500": "#524EC0",
          "600": "#3C38AE",
          "700": "#2E2BA0",
          "800": "#24218A",
          "900": "#1C1A70",
          "950": "#14143F"
        },
        "neutral": {
          "0": "#FFFFFF",
          "25": "#FAFAFD",
          "50": "#F5F5FA",
          "100": "#EEEFF5",
          "200": "#E1E2EC",
          "300": "#C5CCD8",
          "400": "#84899A",
          "500": "#5E6178",
          "600": "#525570",
          "700": "#3A4256",
          "800": "#252740",
          "900": "#14152B"
        },
        "accent": {
          "100": "#FEF3DC",
          "400": "#F5B43C",
          "600": "#C98A12"
        },
        "go": {
          "fg": "#12795A",
          "bg": "#E7F5EF",
          "border": "#B7DFCC",
          "solid": "#12795A"
        },
        "caution": {
          "fg": "#A35C00",
          "bg": "#FFF4E0",
          "border": "#F0D3A0",
          "solid": "#A35C00"
        },
        "stop": {
          "fg": "#C0362C",
          "bg": "#FDECEA",
          "border": "#F3C1BC",
          "solid": "#C0362C"
        },
        "info": {
          "fg": "#2457A6",
          "bg": "#EAF1FB",
          "border": "#C3D5EF",
          "solid": "#2457A6"
        },
        "ink": {
          "DEFAULT": "#14152B",
          "secondary": "#525570",
          "muted": "#5E6178"
        },
        "canvas": "#F5F5FA",
        "surface": "#FFFFFF",
        "sunken": "#EEEFF5",
        "line": {
          "DEFAULT": "#E1E2EC",
          "strong": "#C5CCD8",
          "input": "#84899A"
        },
        "practice": {
          "bg": "#E8EBF1",
          "pill": "#3A4256"
        }
      },
      "fontFamily": {
        "sans": [
          "Onest",
          "Noto Sans",
          "system-ui",
          "sans-serif"
        ],
        "mono": [
          "JetBrains Mono",
          "ui-monospace",
          "monospace"
        ]
      },
      "fontSize": {
        "display": [
          "40px",
          {
            "lineHeight": "48px",
            "fontWeight": "700",
            "letterSpacing": "-0.02em"
          }
        ],
        "h1": [
          "28px",
          {
            "lineHeight": "36px",
            "fontWeight": "700",
            "letterSpacing": "-0.015em"
          }
        ],
        "h2": [
          "22px",
          {
            "lineHeight": "30px",
            "fontWeight": "600",
            "letterSpacing": "-0.01em"
          }
        ],
        "h3": [
          "18px",
          {
            "lineHeight": "26px",
            "fontWeight": "600"
          }
        ],
        "bodyLg": [
          "18px",
          {
            "lineHeight": "28px",
            "fontWeight": "400"
          }
        ],
        "body": [
          "16px",
          {
            "lineHeight": "24px",
            "fontWeight": "400"
          }
        ],
        "bodySm": [
          "14px",
          {
            "lineHeight": "20px",
            "fontWeight": "400"
          }
        ],
        "label": [
          "14px",
          {
            "lineHeight": "20px",
            "fontWeight": "500"
          }
        ],
        "caption": [
          "13px",
          {
            "lineHeight": "18px",
            "fontWeight": "400"
          }
        ],
        "overline": [
          "12px",
          {
            "lineHeight": "16px",
            "fontWeight": "600",
            "letterSpacing": "0.06em"
          }
        ],
        "amountXl": [
          "32px",
          {
            "lineHeight": "40px",
            "fontWeight": "700",
            "letterSpacing": "-0.01em"
          }
        ],
        "amount": [
          "16px",
          {
            "lineHeight": "24px",
            "fontWeight": "600"
          }
        ],
        "code": [
          "14px",
          {
            "lineHeight": "20px",
            "fontWeight": "400"
          }
        ]
      },
      "borderRadius": {
        "sm": "6px",
        "md": "10px",
        "lg": "14px",
        "xl": "20px"
      },
      "boxShadow": {
        "xs": "0 1px 2px rgba(20,21,43,0.06)",
        "sm": "0 1px 3px rgba(20,21,43,0.08), 0 1px 2px rgba(20,21,43,0.04)",
        "md": "0 4px 12px rgba(20,21,43,0.08), 0 1px 3px rgba(20,21,43,0.05)",
        "lg": "0 12px 32px rgba(20,21,43,0.12), 0 2px 6px rgba(20,21,43,0.06)",
        "focus": "0 0 0 2px #FFFFFF, 0 0 0 4px #2E2BA0"
      }
    }
  }
};
