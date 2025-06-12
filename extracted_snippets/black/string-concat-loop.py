# string-concat-loop snippets for black

# File: /root/ecooptimizer/black/src/black/lines.py
# Occurrences: Lines 488-490 (2 instances)

for leaf in leaves:
    res += str(leaf)

# ==================================================
# File: /root/ecooptimizer/black/src/black/trans.py
# Line: 1681

for leaf in LL[string_idx + 1 :]:
    temp_value += str(leaf)
    if leaf.type == token.LPAR:
        break


# ==================================================
