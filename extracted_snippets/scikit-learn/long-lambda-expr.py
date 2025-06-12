# long-lambda-expr snippets for scikit-learn

# File: /root/ecooptimizer/scikit-learn/sklearn/feature_selection/_rfe.py
# Line: 55

lambda estimator, features: _score(
    estimator,
    X_test[:, features],
    y_test,
    scorer,
    score_params=score_params,
),

# ==================================================
