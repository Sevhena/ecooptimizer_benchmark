# string-concat-loop snippets for seaborn

# File: /root/ecooptimizer/seaborn/seaborn/palettes.py
# Line: 86

for i, c in enumerate(self.as_hex()):
    html += (
        f'<rect x="{i * s}" y="0" width="{s}" height="{s}" style="fill:{c};'
        'stroke-width:2;stroke:rgb(255,255,255)"/>'
    )

# ==================================================
