# long-message-chain snippets for scikit-learn

# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_species_distributions.py
# Line: 96

names = F.readline().decode("ascii").strip().split(",")

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_arff_parser.py
# Line: 371

if line.decode("utf-8").lower().startswith("@data"):

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_lfw.py
# Line: 438

split_lines = [ln.decode().strip().split("\t") for ln in index_file]

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_samples_generator.py
# Line: 540

cumulative_p_w_sample = p_w_c.take(y, axis=1).sum(axis=1).cumsum()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/metrics/cluster/_supervised.py
# Line: 257

C[1, 0] = contingency.transpose().dot(n_c).sum() - sum_squares

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/_arff.py
# Line: 779

s = s.strip('\r\n ').replace('\r\n', '\n').split('\n')

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/calibration.py
# Line: 552

MetadataRouter(owner=self.__class__.__name__)
.add_self_request(self)
.add(
    estimator=self._get_estimator(),
    method_mapping=MethodMapping().add(caller="fit", callee="fit"),
)
.add(
    splitter=self.cv,
    method_mapping=MethodMapping().add(caller="fit", callee="split"),
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/multioutput.py
# Line: 339

method_mapping=MethodMapping()
.add(caller="partial_fit", callee="partial_fit")
.add(caller="fit", callee="fit"),

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/feature_selection/_from_model.py
# Line: 503

method_mapping=MethodMapping()
.add(caller="partial_fit", callee="partial_fit")
.add(caller="fit", callee="fit"),

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/feature_selection/_rfe.py
# Line: 550

method_mapping=MethodMapping()
.add(caller="fit", callee="fit")
.add(caller="predict", callee="predict")
.add(caller="score", callee="score"),

# ==================================================
# Line: 1008

method_mapping=MethodMapping()
.add(caller="fit", callee="score")
.add(caller="score", callee="score"),

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/manifold/_t_sne.py
# Line: 539

NearestNeighbors(n_neighbors=n_neighbors)
.fit(X_embedded)
.kneighbors(return_distance=False)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_forest.py
# Line: 1124

self.oob_prediction_ = super()._compute_oob_predictions(X, y).squeeze(axis=1)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/compose/_target.py
# Line: 387

method_mapping=MethodMapping()
.add(caller="fit", callee="fit")
.add(caller="predict", callee="predict"),

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/compose/_column_transformer.py
# Line: 1304

method_mapping.add(caller="fit", callee="fit")
.add(caller="fit", callee="transform")
.add(caller="fit_transform", callee="fit")
.add(caller="fit_transform", callee="transform")

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/multiclass.py
# Occurrences: Lines 625-631 (2 instances)

MetadataRouter(owner=self.__class__.__name__)
.add_self_request(self)
.add(
    estimator=self.estimator,
    method_mapping=MethodMapping()
    .add(caller="fit", callee="fit")
    .add(caller="partial_fit", callee="partial_fit"),
)

# ==================================================
# Occurrences: Lines 1029-1035 (2 instances)

MetadataRouter(owner=self.__class__.__name__)
.add_self_request(self)
.add(
    estimator=self.estimator,
    method_mapping=MethodMapping()
    .add(caller="fit", callee="fit")
    .add(caller="partial_fit", callee="partial_fit"),
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/pipeline.py
# Occurrences: Lines 1354-1376 (3 instances)

method_mapping.add(caller="fit", callee="fit_transform")
.add(caller="fit_transform", callee="fit_transform")
.add(caller="fit_predict", callee="fit_transform")

# ==================================================
# Line: 1394

method_mapping.add(caller="fit", callee="fit")
.add(caller="predict", callee="predict")
.add(caller="fit_predict", callee="fit_predict")
.add(caller="predict_proba", callee="predict_proba")
.add(caller="decision_function", callee="decision_function")
.add(caller="predict_log_proba", callee="predict_log_proba")
.add(caller="transform", callee="transform")
.add(caller="inverse_transform", callee="inverse_transform")
.add(caller="score", callee="score")

# ==================================================
# Line: 2105

method_mapping=MethodMapping()
.add(caller="fit", callee="fit")
.add(caller="fit_transform", callee="fit_transform")
.add(caller="fit_transform", callee="fit")
.add(caller="fit_transform", callee="transform")
.add(caller="transform", callee="transform"),

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/model_selection/_validation.py
# Line: 357

MetadataRouter(owner="cross_validate")
.add(
    splitter=cv,
    method_mapping=MethodMapping().add(caller="fit", callee="split"),
)
.add(
    estimator=estimator,
    # TODO(SLEP6): also pass metadata to the predict method for
    # scoring?
    method_mapping=MethodMapping().add(caller="fit", callee="fit"),
)
.add(
    scorer=scorers,
    method_mapping=MethodMapping().add(caller="fit", callee="score"),
)

# ==================================================
# Line: 1175

MetadataRouter(owner="cross_val_predict")
.add(
    splitter=cv,
    method_mapping=MethodMapping().add(caller="fit", callee="split"),
)
.add(
    estimator=estimator,
    # TODO(SLEP6): also pass metadata for the predict method.
    method_mapping=MethodMapping().add(caller="fit", callee="fit"),
)

# ==================================================
# Line: 1634

MetadataRouter(owner="permutation_test_score")
.add(
    estimator=estimator,
    # TODO(SLEP6): also pass metadata to the predict method for
    # scoring?
    method_mapping=MethodMapping().add(caller="fit", callee="fit"),
)
.add(
    splitter=cv,
    method_mapping=MethodMapping().add(caller="fit", callee="split"),
)
.add(
    scorer=scorer,
    method_mapping=MethodMapping().add(caller="fit", callee="score"),
)

# ==================================================
# Occurrences: Lines 1979-1986 (2 instances)

MetadataRouter(owner="learning_curve")
.add(
    estimator=estimator,
    # TODO(SLEP6): also pass metadata to the predict method for
    # scoring?
    method_mapping=MethodMapping()
    .add(caller="fit", callee="fit")
    .add(caller="fit", callee="partial_fit"),
)
.add(
    splitter=cv,
    method_mapping=MethodMapping().add(caller="fit", callee="split"),
)
.add(
    scorer=scorer,
    method_mapping=MethodMapping().add(caller="fit", callee="score"),
)

# ==================================================
# Line: 2433

MetadataRouter(owner="validation_curve")
.add(
    estimator=estimator,
    method_mapping=MethodMapping().add(caller="fit", callee="fit"),
)
.add(
    splitter=cv,
    method_mapping=MethodMapping().add(caller="fit", callee="split"),
)
.add(
    scorer=scorer,
    method_mapping=MethodMapping().add(caller="fit", callee="score"),
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/model_selection/_classification_threshold.py
# Line: 867

MetadataRouter(owner=self.__class__.__name__)
.add(
    estimator=self.estimator,
    method_mapping=MethodMapping().add(callee="fit", caller="fit"),
)
.add(
    splitter=self.cv,
    method_mapping=MethodMapping().add(callee="split", caller="fit"),
)
.add(
    scorer=self._get_curve_scorer(),
    method_mapping=MethodMapping().add(callee="score", caller="fit"),
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/model_selection/_search.py
# Line: 1218

method_mapping=MethodMapping()
.add(caller="score", callee="score")
.add(caller="fit", callee="score"),

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_coordinate_descent.py
# Line: 1903

MetadataRouter(owner=self.__class__.__name__)
.add_self_request(self)
.add(
    splitter=check_cv(self.cv),
    method_mapping=MethodMapping().add(caller="fit", callee="split"),
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_ridge.py
# Line: 2486

MetadataRouter(owner=self.__class__.__name__)
.add_self_request(self)
.add(
    scorer=self.scoring,
    method_mapping=MethodMapping().add(caller="fit", callee="score"),
)
.add(
    splitter=self.cv,
    method_mapping=MethodMapping().add(caller="fit", callee="split"),
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_ransac.py
# Line: 712

method_mapping=MethodMapping()
.add(caller="fit", callee="fit")
.add(caller="fit", callee="score")
.add(caller="score", callee="score")
.add(caller="predict", callee="predict"),

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_logistic.py
# Occurrences: Lines 2292-2302 (2 instances)

MetadataRouter(owner=self.__class__.__name__)
.add_self_request(self)
.add(
    splitter=self.cv,
    method_mapping=MethodMapping().add(caller="fit", callee="split"),
)
.add(
    scorer=self._get_scorer(),
    method_mapping=MethodMapping()
    .add(caller="score", callee="score")
    .add(caller="fit", callee="score"),
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/impute/_base.py
# Line: 573

if not self.keep_empty_features and ma.getmask(masked_X).all(axis=0).any():

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/semi_supervised/_self_training.py
# Line: 608

MethodMapping()
.add(callee="fit", caller="fit")
.add(callee="score", caller="fit")
.add(callee="predict", caller="predict")
.add(callee="predict_proba", caller="predict_proba")
.add(callee="decision_function", caller="decision_function")
.add(callee="predict_log_proba", caller="predict_log_proba")
.add(callee="score", caller="score")

# ==================================================
