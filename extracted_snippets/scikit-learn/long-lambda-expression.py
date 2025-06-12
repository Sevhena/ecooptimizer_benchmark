# long-lambda-expression snippets for scikit-learn

# File: /root/ecooptimizer/scikit-learn/sklearn/externals/_scipy/sparse/csgraph/_laplacian.py
# Line: 388

lambda v: v * d[:, np.newaxis]
- m @ v
- np.transpose(np.conjugate(np.transpose(np.conjugate(v)) @ m))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_extra/_lib/_funcs.py
# Occurrences: Lines 546-548 (2 instances)

lambda a, b: mxp.isinf(a) & mxp.isinf(b) & (mxp.sign(a) == mxp.sign(b)),  # pyright: ignore[reportUnknownArgumentType]

# ==================================================
