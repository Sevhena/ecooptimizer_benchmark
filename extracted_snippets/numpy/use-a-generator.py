# use-a-generator snippets for numpy

# File: /root/ecooptimizer/numpy/numpy/distutils/ccompiler_opt.py
# Occurrences: Lines 2107-2117 (2 instances)

if not all([
    self.feature_is_exist(tar) for tar in targets
]) :

# ==================================================
# Line: 2136

is_base = all([
    f in self.parse_baseline_names
    for f in tar
])

# ==================================================
# Line: 2200

can = all([
    self.feature_can_autovec(t)
    for t in tar
])

# ==================================================
