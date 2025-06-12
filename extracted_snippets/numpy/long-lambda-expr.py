# long-lambda-expr snippets for numpy

# File: /root/ecooptimizer/numpy/numpy/lib/_function_base_impl.py
# Line: 96

'fix_gamma': lambda gamma, _: _get_gamma_mask(
    shape=gamma.shape,
    default_value=1.,
    conditioned_value=0.5,
    where=gamma == 0),

# ==================================================
# Line: 155

'fix_gamma': lambda gamma, index: _get_gamma_mask(
    shape=gamma.shape,
    default_value=0.5,
    conditioned_value=0.,
    where=index % 1 == 0),

# ==================================================
