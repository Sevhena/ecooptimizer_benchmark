# cached-repeated-calls snippets for black

# File: /root/ecooptimizer/black/src/black/__init__.py
# Line: 1010

then = datetime.now(timezone.utc)

# ==================================================
# Line: 1035

now = datetime.now(timezone.utc)

# ==================================================
# File: /root/ecooptimizer/black/src/black/linegen.py
# Line: 425

docstring = normalize_string_prefix(leaf.value)

# ==================================================
# Line: 502

leaf.value = normalize_string_prefix(leaf.value)

# ==================================================
# Line: 1315

current_line = _safe_add_trailing_comma(
    trailing_comma_safe, delimiter_priority, current_line
)

# ==================================================
# Line: 1333

current_line = _safe_add_trailing_comma(
    trailing_comma_safe, delimiter_priority, current_line
)

# ==================================================
# File: /root/ecooptimizer/black/src/black/trans.py
# Occurrences: Lines 1633-1633 (2 instances)

or next_value != self._normalize_f_string(next_value, prefix)

# ==================================================
# Occurrences: Lines 1642-1642 (2 instances)

next_value = self._normalize_f_string(next_value, prefix)

# ==================================================
# Line: 1650

next_line = line.clone()

# ==================================================
# Line: 1671

last_line = line.clone()

# ==================================================
# Line: 1699

non_string_line = line.clone()

# ==================================================
# Line: 2181

first_line = line.clone()

# ==================================================
# Line: 2230

right_leaves.pop()

# ==================================================
# Line: 2237

old_rpar_leaf = right_leaves.pop()

# ==================================================
# Line: 2255

right_leaves.pop()

# ==================================================
# Line: 2262

last_line = line.clone()

# ==================================================
# File: /root/ecooptimizer/black/src/black/handle_ipynb_magics.py
# Occurrences: Lines 216-219 (2 instances)

token = create_token(n_chars)

# ==================================================
# File: /root/ecooptimizer/black/src/black/nodes.py
# Line: 215

prevp = preceding_leaf(p)

# ==================================================
# Line: 307

prevp = preceding_leaf(p)

# ==================================================
# Line: 329

prevp = preceding_leaf(p)

# ==================================================
# Line: 344

prevp = preceding_leaf(p)

# ==================================================
# Line: 383

prevp = preceding_leaf(p)

# ==================================================
# File: /root/ecooptimizer/black/src/black/ranges.py
# Line: 396

line_end = _leaf_line_end(last)

# ==================================================
# Line: 408

return set(range(first.lineno, _leaf_line_end(last) + 1))

# ==================================================
# File: /root/ecooptimizer/black/src/black/parsing.py
# Line: 142

for version in sorted(versions, reverse=True):

# ==================================================
# Line: 150

for version in sorted(versions, reverse=True):

# ==================================================
# File: /root/ecooptimizer/black/src/blib2to3/pgen2/driver.py
# Line: 206

res = "".join(lines)

# ==================================================
# Line: 223

return "".join(lines), current_line

# ==================================================
# File: /root/ecooptimizer/black/src/blib2to3/pgen2/pgen.py
# Line: 274

a, z = self.parse_alt()

# ==================================================
# Line: 284

a, z = self.parse_alt()

# ==================================================
# Occurrences: Lines 291-293 (2 instances)

a, b = self.parse_item()

# ==================================================
# Occurrences: Lines 344-346 (2 instances)

tup = next(self.generator)

# ==================================================
# File: /root/ecooptimizer/black/src/blib2to3/pgen2/parse.py
# Occurrences: Lines 384-386 (2 instances)

self.stack.pop()

# ==================================================
# File: /root/ecooptimizer/black/src/blib2to3/pgen2/conv.py
# Line: 135

n, m, k = list(map(int, mo.groups()))

# ==================================================
# Line: 141

i, j = list(map(int, mo.groups()))

# ==================================================
# Line: 149

s, t = list(map(int, mo.groups()))

# ==================================================
# Line: 156

k, n, m = list(map(int, mo.groups()))

# ==================================================
# Line: 170

ndfas = int(mo.group(1))

# ==================================================
# Occurrences: Lines 202-207 (2 instances)

nlabels = int(mo.group(1))

# ==================================================
# Line: 224

ndfas = int(mo.group(1))

# ==================================================
# Occurrences: Lines 231-236 (2 instances)

nlabels = int(mo.group(1))

# ==================================================
