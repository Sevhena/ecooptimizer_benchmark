# long-lambda-expression snippets for numpy

# File: /root/ecooptimizer/numpy/numpy/lib/_function_base_impl.py
# Line: 152

'get_virtual_index': lambda n, quantiles: 0.5 * (
        np.floor((n - 1) * quantiles)
        + np.ceil((n - 1) * quantiles)),

# ==================================================
# Line: 4702

gamma_fun = lambda gamma, index: (gamma == 0) & (np.floor(index) % 2 == 1)

# ==================================================
