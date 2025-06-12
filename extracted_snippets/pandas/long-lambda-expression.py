# long-lambda-expression snippets for pandas

# File: /root/ecooptimizer/pandas/pandas/core/array_algos/replace.py
# Line: 90

lambda x: bool(re.search(b, x))
if isinstance(x, str) and isinstance(b, (str, Pattern))
else False,

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/reshape/merge.py
# Occurrences: Lines 1548-1549 (2 instances)

is_lkey = lambda x: isinstance(x, _known) and len(x) == len(left)

# ==================================================
# File: /root/ecooptimizer/pandas/pandas/core/frame.py
# Line: 9963

mylen = lambda x: len(x) if (is_list_like(x) and len(x) > 0) else 1

# ==================================================
