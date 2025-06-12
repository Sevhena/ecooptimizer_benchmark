# use-a-generator snippets for scikit-learn

# File: /root/ecooptimizer/scikit-learn/sklearn/utils/estimator_checks.py
# Line: 2931

if not any([isinstance(c, Interval) for c in contamination_constraints]):

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/inspection/_plot/partial_dependence.py
# Line: 1253

if any([k not in valid_kinds for k in kind]):

# ==================================================
# Line: 1331

if any([kind_plot == "both" for kind_plot in kind]):

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/impute/_base.py
# Line: 470

if not self.keep_empty_features and any(
    [all(missing_mask[:, i].data) for i in range(missing_mask.shape[1])]
):

# ==================================================
