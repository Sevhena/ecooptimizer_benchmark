# string-concat-loop snippets for matplotlib

# File: /root/ecooptimizer/matplotlib/lib/matplotlib/backends/backend_ps.py
# Line: 343

for i, name in enumerate(go):
    s += f'/{name} {i} def\n'

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/_layoutgrid.py
# Line: 109

for j in range(self.ncols):
    str += f'{i}, {j}: '\
           f'L{self.lefts[j].value():1.3f}, ' \
           f'B{self.bottoms[i].value():1.3f}, ' \
           f'R{self.rights[j].value():1.3f}, ' \
           f'T{self.tops[i].value():1.3f}, ' \
           f'ML{self.margins["left"][j].value():1.3f}, ' \
           f'MR{self.margins["right"][j].value():1.3f}, ' \
           f'MB{self.margins["bottom"][i].value():1.3f}, ' \
           f'MT{self.margins["top"][i].value():1.3f}, \n'

# ==================================================
# File: /root/ecooptimizer/matplotlib/lib/matplotlib/sphinxext/figmpl_directive.py
# Occurrences: Lines 205-209 (3 instances)

for mult, src in srcset.items():
    nm = PurePath(src[1:]).name
    # ../../_images/plot_1_2_0x.png
    path = f'{imagerel}/{rel}{nm}'
    srcsetst += path
    if mult == 0:
        srcsetst += ', '
    else:
        srcsetst += f' {mult:1.2f}x, '

    if mult > maxmult:
        maxmult = mult
        maxsrc = path


# ==================================================
