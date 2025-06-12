# cached-repeated-calls snippets for scikit-learn

# File: /root/ecooptimizer/scikit-learn/sklearn/_loss/loss.py
# Occurrences: Lines 358-359 (2 instances)

gradient_out = np.empty_like(raw_prediction)

# ==================================================
# Line: 501

gradient = np.empty(shape=shape, dtype=dtype, order=order)

# ==================================================
# Line: 510

hessian = np.empty(shape=shape, dtype=dtype, order=order)

# ==================================================
# Occurrences: Lines 1079-1080 (2 instances)

gradient_out = np.empty_like(raw_prediction)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_base.py
# Occurrences: Lines 1256-1264 (4 instances)

header_exercise = f.readline().split()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_species_distributions.py
# Occurrences: Lines 264-266 (4 instances)

train = _load_csv(fhandle)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_svmlight_format_io.py
# Occurrences: Lines 212-219 (2 instances)

actual_dtype, data, ind, indptr, labels, query = _load_svmlight_file(
    f, dtype, multilabel, zero_based, query_id, offset, length
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_twenty_newsgroups.py
# Occurrences: Lines 370-372 (2 instances)

data_lst = np.array(data.data, dtype=object)

# ==================================================
# Occurrences: Lines 381-383 (2 instances)

data_lst = np.array(data.data, dtype=object)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_openml.py
# Line: 157

fsrc = _retry_on_network_error(n_retries, delay, req.full_url)(urlopen)(req)

# ==================================================
# Line: 174

_retry_on_network_error(n_retries, delay, req.full_url)(urlopen)(
    req
)

# ==================================================
# Line: 303

json_data = _get_json_content_from_openml_api(
    url,
    error_msg,
    data_home=data_home,
    n_retries=n_retries,
    delay=delay,
)

# ==================================================
# Line: 344

json_data = _get_json_content_from_openml_api(
    url,
    error_msg,
    data_home=data_home,
    n_retries=n_retries,
    delay=delay,
)

# ==================================================
# Line: 520

gzip_file = _open_openml_url(url, data_home, n_retries=n_retries, delay=delay)

# ==================================================
# Line: 536

gzip_file = _open_openml_url(url, data_home, n_retries=n_retries, delay=delay)

# ==================================================
# Line: 550

X, y, frame, categories = _open_url_and_load_gzip_file(
    url, data_home, n_retries, delay, arff_params
)

# ==================================================
# Line: 566

X, y, frame, categories = _open_url_and_load_gzip_file(
    url, data_home, n_retries, delay, arff_params
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_samples_generator.py
# Occurrences: Lines 1092-1097 (2 instances)

centers = generator.uniform(
    center_box[0], center_box[1], size=(n_centers, n_features)
)

# ==================================================
# Line: 1105

centers = generator.uniform(
    center_box[0], center_box[1], size=(n_centers, n_features)
)

# ==================================================
# Line: 1119

centers = check_array(centers)

# ==================================================
# Occurrences: Lines 1143-1144 (2 instances)

X = np.empty(shape=(sum(n_samples_per_center), n_features), dtype=np.float64)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_indexing.py
# Occurrences: Lines 114-116 (2 instances)

key = np.asarray(key).tolist()

# ==================================================
# Line: 131

key = np.asarray(key)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/estimator_checks.py
# Line: 281

tags = get_tags(transformer)

# ==================================================
# Line: 291

if get_tags(transformer).requires_fit:

# ==================================================
# Line: 988

yield sparse_format, X_csr.asformat(sparse_format)

# ==================================================
# Line: 997

X = X_csr.asformat(sparse_format)

# ==================================================
# Line: 1073

est_xp = clone(est)

# ==================================================
# Line: 1135

est_fitted_with_as_array = clone(est).fit(X_xp, y_xp)

# ==================================================
# Line: 1292

estimator = clone(estimator_orig)

# ==================================================
# Line: 1298

estimator = clone(estimator_orig)

# ==================================================
# Occurrences: Lines 1501-1502 (2 instances)

estimator_weighted = clone(estimator_orig)

# ==================================================
# Line: 1929

y = _enforce_estimator_tags_y(estimator, y)

# ==================================================
# Line: 1942

y = _enforce_estimator_tags_y(estimator, y)

# ==================================================
# Occurrences: Lines 2068-2071 (2 instances)

X_pred3 = transformer.fit_transform(X, y=y_)

# ==================================================
# Occurrences: Lines 2319-2323 (3 instances)

estimator_orig, rnd.uniform(size=(10, 3))

# ==================================================
# Line: 2481

decision = estimator.decision_function(X)

# ==================================================
# Line: 2495

y_prob = estimator.predict_proba(X)

# ==================================================
# Occurrences: Lines 2519-2520 (2 instances)

y_proba = estimator.predict_proba(X)[:, i]

# ==================================================
# Occurrences: Lines 2619-2621 (2 instances)

X_pred1 = clusterer.fit(X).predict(X)

# ==================================================
# Occurrences: Lines 2631-2632 (2 instances)

X_train = rnd.uniform(size=(10, 3))

# ==================================================
# Occurrences: Lines 2661-2662 (2 instances)

X_train = rnd.uniform(size=(10, 10))

# ==================================================
# Occurrences: Lines 2864-2869 (2 instances)

y_pred = estimator.predict(X)

# ==================================================
# Line: 2906

y_pred = estimator.predict(X)

# ==================================================
# Line: 2915

decision = estimator.decision_function(X)

# ==================================================
# Line: 3256

y_pred = estimator.predict(X)

# ==================================================
# Line: 3265

y_pred_2d = estimator.predict(X)

# ==================================================
# Line: 3365

y_names_binary = np.take(labels_binary, y_binary)

# ==================================================
# Line: 3377

y_names_binary = np.take(labels_binary, y_binary)

# ==================================================
# Occurrences: Lines 3386-3392 (4 instances)

rnd = np.random.RandomState(0)

# ==================================================
# Occurrences: Lines 3535-3539 (2 instances)

y_pred = classifier.predict(X_test)

# ==================================================
# Line: 3566

coef_balanced = classifier.fit(X, y).coef_.copy()

# ==================================================
# Line: 3577

coef_manual = classifier.fit(X, y).coef_.copy()

# ==================================================
# Line: 3596

params = estimator.get_params()

# ==================================================
# Line: 3603

new_params = estimator.get_params()

# ==================================================
# Occurrences: Lines 3673-3678 (2 instances)

pred_orig = est.predict(X)

# ==================================================
# Line: 3684

pred = est.predict(X)

# ==================================================
# Occurrences: Lines 3731-3732 (2 instances)

estimator_1 = clone(estimator_orig)

# ==================================================
# Line: 3740

y_ = _NotAnArray(np.asarray(y))

# ==================================================
# Line: 3749

y_ = np.asarray(y)

# ==================================================
# Line: 3850

old_params = estimator.get_params()

# ==================================================
# Line: 3857

params = estimator.get_params()

# ==================================================
# Occurrences: Lines 4083-4087 (2 instances)

orig_params = estimator.get_params(deep=False)

# ==================================================
# Occurrences: Lines 4117-4117 (3 instances)

curr_params = estimator.get_params(deep=False)

# ==================================================
# Occurrences: Lines 4127-4127 (3 instances)

curr_params = estimator.get_params(deep=False)

# ==================================================
# Line: 4210

y_pred = estimator.fit_predict(X)

# ==================================================
# Line: 4228

y_pred = estimator.fit_predict(X)

# ==================================================
# Line: 4285

method: getattr(estimator, method)(X_test)

# ==================================================
# Line: 4296

new_result = getattr(estimator, method)(X_test)

# ==================================================
# Line: 4415

estimator = clone(estimator_orig)

# ==================================================
# Line: 4491

estimator = clone(estimator_orig)

# ==================================================
# Line: 4593

estimator = clone(estimator_orig)

# ==================================================
# Line: 4707

estimator = clone(estimator_orig)

# ==================================================
# Occurrences: Lines 4969-4969 (2 instances)

X_trans_no_setting = transform_method(transformer)

# ==================================================
# Occurrences: Lines 4976-4976 (2 instances)

X_trans_default = transform_method(transformer)

# ==================================================
# Occurrences: Lines 5022-5024 (4 instances)

X_trans, _ = transformer.fit_transform(data, y)

# ==================================================
# Occurrences: Lines 5145-5152 (3 instances)

transformer_default = clone(transformer).set_output(transform="default")

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/optimize.py
# Line: 143

dri0 = np.dot(ri, ri)

# ==================================================
# Line: 187

dri1 = np.dot(ri, ri)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/fixes.py
# Line: 228

frame = frame.fillna(value=np.nan)

# ==================================================
# Line: 234

frame = frame.fillna(value=np.nan).infer_objects(**infer_objects_kwargs)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_user_interface.py
# Occurrences: Lines 55-57 (2 instances)

start = timeit.default_timer()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/extmath.py
# Line: 810

a = np.ravel(a)

# ==================================================
# Occurrences: Lines 820-824 (3 instances)

scores = np.unique(np.ravel(a))  # get ALL unique values

# ==================================================
# Occurrences: Lines 1154-1164 (4 instances)

correction = _safe_accumulator_op(
    np.matmul, sample_weight, np.where(X_nan_mask, 0, temp)
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_testing.py
# Occurrences: Lines 878-879 (4 instances)

type_items = defaultdict(lambda: defaultdict(list))

# ==================================================
# Line: 1015

pd = pytest.importorskip("pandas", minversion=minversion)

# ==================================================
# Line: 1022

pa = pytest.importorskip("pyarrow", minversion=minversion)

# ==================================================
# Line: 1037

pl = pytest.importorskip("polars", minversion=minversion)

# ==================================================
# Occurrences: Lines 1044-1053 (4 instances)

pd = pytest.importorskip("pandas", minversion=minversion)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_encode.py
# Line: 296

valid_mask = xp.ones(len(values), dtype=xp.bool)

# ==================================================
# Line: 310

valid_mask = xp.ones(len(values), dtype=xp.bool)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/random.py
# Occurrences: Lines 42-43 (2 instances)

data = array.array("i")

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_pprint.py
# Line: 240

next_ent = next(it)

# ==================================================
# Line: 252

next_ent = next(it)

# ==================================================
# Line: 297

next_ent = next(it)

# ==================================================
# Line: 309

next_ent = next(it)

# ==================================================
# Line: 361

return repr(object), True, False

# ==================================================
# Line: 367

objid = id(object)

# ==================================================
# Occurrences: Lines 381-386 (2 instances)

krepr, kreadable, krecur = saferepr(
    k, context, maxlevels, level, changed_only=changed_only
)

# ==================================================
# Line: 407

objid = id(object)

# ==================================================
# Line: 431

objid = id(object)

# ==================================================
# Occurrences: Lines 449-454 (2 instances)

krepr, kreadable, krecur = saferepr(
    k, context, maxlevels, level, changed_only=changed_only
)

# ==================================================
# Line: 462

rep = repr(object)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/validation.py
# Occurrences: Lines 1123-1130 (2 instances)

array = _asarray_with_order(
    array, dtype=dtype, order=order, copy=True, xp=xp
)

# ==================================================
# Occurrences: Lines 1179-1181 (2 instances)

array = array.copy(**copy_params)

# ==================================================
# Line: 2061

max_real_abs = np.abs(np.real(lambdas)).max()

# ==================================================
# Line: 2082

lambdas = np.real(lambdas)

# ==================================================
# Occurrences: Lines 2587-2589 (2 instances)

n_unexpeced = len(unexpected_feature_names)

# ==================================================
# Line: 2736

feature_names_in = _get_feature_names(X)

# ==================================================
# Line: 2746

X_feature_names = _get_feature_names(X)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/multiclass.py
# Line: 451

if not np.array_equal(clf.classes_, unique_labels(classes)):

# ==================================================
# Line: 459

clf.classes_ = unique_labels(classes)

# ==================================================
# Occurrences: Lines 561-562 (2 instances)

votes = np.zeros((n_samples, n_classes))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_response.py
# Line: 201

prediction_method = _check_response_method(estimator, response_method)

# ==================================================
# Line: 214

y_pred = prediction_method(X)

# ==================================================
# Occurrences: Lines 231-232 (2 instances)

prediction_method = _check_response_method(estimator, response_method)

# ==================================================
# Line: 242

y_pred, pos_label = prediction_method(X), None

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/sparsefuncs.py
# Occurrences: Lines 639-641 (2 instances)

return np.dot(np.diff(X.indptr), sample_weight)

# ==================================================
# Line: 650

weights = np.repeat(sample_weight, np.diff(X.indptr))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/class_weight.py
# Line: 71

weight = np.ones(classes.shape[0], dtype=np.float64, order="C")

# ==================================================
# Line: 87

weight = np.ones(classes.shape[0], dtype=np.float64, order="C")

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_repr_html/estimator.py
# Occurrences: Lines 310-314 (2 instances)

est_block = _get_visual_block(estimator)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/metrics/_base.py
# Occurrences: Lines 171-174 (2 instances)

pair_scores = np.empty(n_pairs)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/metrics/_ranking.py
# Line: 435

return auc(fpr, tpr)

# ==================================================
# Line: 445

partial_auc = auc(fpr, tpr)

# ==================================================
# Line: 1999

if y_type == "binary" and labels is not None and len(labels) > 2:

# ==================================================
# Line: 2020

n_classes = len(classes)

# ==================================================
# Occurrences: Lines 2032-2033 (2 instances)

n_labels = len(labels)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/metrics/_plot/confusion_matrix.py
# Line: 183

display_labels = np.arange(n_classes)

# ==================================================
# Occurrences: Lines 189-190 (2 instances)

xticks=np.arange(n_classes),

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/metrics/pairwise.py
# Occurrences: Lines 190-208 (2 instances)

X = Y = check_array(
    X,
    accept_sparse=accept_sparse,
    dtype=dtype,
    copy=copy,
    ensure_all_finite=ensure_all_finite,
    estimator=estimator,
    ensure_2d=ensure_2d,
)

# ==================================================
# Line: 1998

out[i, j] = metric(x, y, **kwds)

# ==================================================
# Line: 2021

out[i, j] = metric(x, y, **kwds)

# ==================================================
# Line: 2209

n_samples_X = _num_samples(X)

# ==================================================
# Line: 2246

D_chunk.flat[sl.start :: _num_samples(X) + 1] = 0

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/metrics/_classification.py
# Line: 96

xp, _ = get_namespace(y_true, y_pred)

# ==================================================
# Line: 120

xp, _ = get_namespace(y_true, y_pred)

# ==================================================
# Line: 2926

labels = unique_labels(y_true, y_pred)

# ==================================================
# Line: 2934

not labels_given or (set(labels) >= set(unique_labels(y_true, y_pred)))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/base.py
# Line: 101

estimator_type = type(estimator)

# ==================================================
# Line: 121

"'get_params' method." % (repr(estimator), type(estimator))

# ==================================================
# Line: 393

right_lim = re.match(regex, repr_[::-1]).end()

# ==================================================
# Line: 405

right_lim = re.match(regex, repr_[::-1]).end()

# ==================================================
# Occurrences: Lines 426-429 (2 instances)

state = self.__dict__.copy()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_compat/common/_helpers.py
# Line: 745

x_device = getattr(x, "device", None)

# ==================================================
# Line: 754

x_device = getattr(x, "device", None)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_compat/torch/_aliases.py
# Occurrences: Lines 88-91 (2 instances)

dtype = result_type(x1, x2)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/_arff.py
# Occurrences: Lines 616-619 (4 instances)

if len(row) > 0 and max(row) >= num_attributes:

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/_scipy/sparse/csgraph/_laplacian.py
# Line: 427

m = _linearoperator(md, shape=graph.shape, dtype=dtype)

# ==================================================
# Line: 439

m = _linearoperator(md, shape=graph.shape, dtype=dtype)

# ==================================================
# Line: 465

m = m.tocoo(copy=needs_copy)

# ==================================================
# Line: 476

m = m.tocoo(copy=needs_copy)

# ==================================================
# Line: 509

m = _linearoperator(md, shape=graph.shape, dtype=dtype)

# ==================================================
# Line: 521

m = _linearoperator(md, shape=graph.shape, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_extra/_lib/_utils/_helpers.py
# Line: 189

xb = xp.asarray(b)

# ==================================================
# Line: 196

xa, xb = xp.asarray(a), xp.asarray(b)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_extra/_lib/_at.py
# Line: 290

writeable = None if copy else is_writeable_array(x)

# ==================================================
# Line: 309

out = xp.astype(out, x.dtype, copy=False)

# ==================================================
# Line: 329

return xp.astype(out, x.dtype, copy=False)

# ==================================================
# Line: 341

writeable = is_writeable_array(x)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/array_api_extra/_lib/_lazy.py
# Line: 248

delayed_out = wrapped(*args, **kwargs)

# ==================================================
# Line: 295

out = wrapped(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/neural_network/_rbm.py
# Line: 421

begin = time.time()

# ==================================================
# Line: 427

end = time.time()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/tree/_classes.py
# Line: 281

is_classification = is_classifier(self)

# ==================================================
# Line: 295

y = np.copy(y)

# ==================================================
# Line: 301

y_original = np.copy(y)

# ==================================================
# Line: 418

if is_classifier(self):

# ==================================================
# Line: 441

if is_classifier(self):

# ==================================================
# Line: 474

if self.n_outputs_ == 1 and is_classifier(self):

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/tree/_export.py
# Occurrences: Lines 358-361 (2 instances)

value_text = np.around(value, self.precision)

# ==================================================
# Line: 367

value_text = np.around(value, self.precision)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/tree/_reingold_tilford.py
# Line: 76

v.x = v.lbrother().x + distance

# ==================================================
# Line: 89

w = v.lbrother()

# ==================================================
# Occurrences: Lines 109-113 (10 instances)

while vil.right() and vir.left():

# ==================================================
# Occurrences: Lines 124-129 (6 instances)

if vil.right() and not vor.right():

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/calibration.py
# Occurrences: Lines 347-354 (2 instances)

predictions = predictions.reshape(-1, 1)

# ==================================================
# Line: 426

clone(estimator),

# ==================================================
# Line: 439

this_estimator = clone(estimator)

# ==================================================
# Occurrences: Lines 463-470 (2 instances)

predictions = predictions.reshape(-1, 1)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/dummy.py
# Line: 185

if self._strategy == "uniform" and sp.issparse(y):

# ==================================================
# Line: 197

self.sparse_output_ = sp.issparse(y)

# ==================================================
# Occurrences: Lines 377-377 (2 instances)

out = np.zeros((n_samples, n_classes_[k]), dtype=np.float64)

# ==================================================
# Occurrences: Lines 392-392 (2 instances)

out = np.zeros((n_samples, n_classes_[k]), dtype=np.float64)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/multioutput.py
# Occurrences: Lines 707-708 (2 instances)

Y_output_chain = np.zeros((X.shape[0], len(self.estimators_)))

# ==================================================
# Occurrences: Lines 785-788 (2 instances)

X_aug = sp.hstack((X, Y_pred_chain), format="lil")

# ==================================================
# Occurrences: Lines 804-808 (2 instances)

X_aug = sp.hstack((X, Y_pred_chain), format="lil")

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_function_transformer.py
# Line: 266

feature_names_out = self.get_feature_names_out()

# ==================================================
# Line: 297

f"{list(self.get_feature_names_out())}. "

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_polynomial.py
# Occurrences: Lines 1008-1008 (2 instances)

XBS_sparse = XBS_sparse.tolil()

# ==================================================
# Occurrences: Lines 1030-1030 (2 instances)

XBS_sparse = XBS_sparse.tolil()

# ==================================================
# Occurrences: Lines 1059-1059 (2 instances)

XBS_sparse = XBS_sparse.tolil()

# ==================================================
# Occurrences: Lines 1071-1071 (2 instances)

XBS_sparse = XBS_sparse.tolil()

# ==================================================
# Occurrences: Lines 1099-1099 (3 instances)

XBS_sparse = XBS_sparse.tolil()

# ==================================================
# Occurrences: Lines 1110-1110 (3 instances)

XBS_sparse = XBS_sparse.tolil()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_encoders.py
# Occurrences: Lines 1164-1164 (2 instances)

unknown = np.asarray(sub.sum(axis=1) == 0).flatten()

# ==================================================
# Occurrences: Lines 1179-1179 (2 instances)

dropped = np.asarray(sub.sum(axis=1) == 0).flatten()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_data.py
# Line: 258

mean_1 = np.nanmean(Xr, axis=0)

# ==================================================
# Line: 277

mean_2 = np.nanmean(Xr, axis=0)

# ==================================================
# Line: 2582

data = np.concatenate((np.full(n_samples, value), X.data))

# ==================================================
# Line: 2592

data = np.concatenate((np.full(n_samples, value), X.data))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_discretization.py
# Occurrences: Lines 342-342 (2 instances)

bin_edges[jj] = np.linspace(col_min, col_max, n_bins[jj] + 1)

# ==================================================
# Occurrences: Lines 379-379 (2 instances)

uniform_edges = np.linspace(col_min, col_max, n_bins[jj] + 1)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/preprocessing/_label.py
# Line: 537

n_classes = len(classes)

# ==================================================
# Line: 548

elif len(classes) >= 3:

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/feature_selection/_base.py
# Occurrences: Lines 257-259 (2 instances)

importances = safe_sqr(importances)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/feature_selection/_mutual_info.py
# Occurrences: Lines 118-124 (4 instances)

radius = np.empty(n_samples)

# ==================================================
# Line: 136

n_samples = np.sum(mask)

# ==================================================
# Line: 277

discrete_features = issparse(X)

# ==================================================
# Line: 291

if np.any(continuous_mask) and issparse(X):

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/feature_selection/_from_model.py
# Occurrences: Lines 62-64 (2 instances)

reference = np.median(importances)

# ==================================================
# Occurrences: Lines 71-74 (2 instances)

threshold = np.median(importances)

# ==================================================
# Occurrences: Lines 374-378 (2 instances)

self.estimator_ = clone(self.estimator)

# ==================================================
# Occurrences: Lines 455-458 (2 instances)

self.estimator_ = clone(self.estimator)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/feature_selection/_rfe.py
# Line: 330

estimator = clone(self.estimator)

# ==================================================
# Line: 363

self.estimator_ = clone(self.estimator)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/kernel_approximation.py
# Line: 779

X_step = np.zeros_like(X)

# ==================================================
# Occurrences: Lines 790-794 (4 instances)

X_step = np.zeros_like(X)

# ==================================================
# Line: 806

X_step = sp.csr_matrix(
    (data_step, indices, indptr), shape=X.shape, dtype=X.dtype, copy=False
)

# ==================================================
# Occurrences: Lines 818-826 (4 instances)

X_step = sp.csr_matrix(
    (data_step, indices, indptr), shape=X.shape, dtype=X.dtype, copy=False
)

# ==================================================
# Occurrences: Lines 1086-1087 (4 instances)

if getattr(self, param) is not None:

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/manifold/_locally_linear.py
# Line: 258

neighbors = nbrs.kneighbors(
    X, n_neighbors=n_neighbors + 1, return_distance=False
)

# ==================================================
# Line: 278

Ci = np.dot(Gi, Gi.T)

# ==================================================
# Line: 296

nbrs_x, nbrs_y = np.meshgrid(neighbors[i], neighbors[i])

# ==================================================
# Line: 303

neighbors = nbrs.kneighbors(
    X, n_neighbors=n_neighbors + 1, return_distance=False
)

# ==================================================
# Line: 395

nbrs_x, nbrs_y = np.meshgrid(neighbors[i], neighbors[i])

# ==================================================
# Line: 403

neighbors = nbrs.kneighbors(
    X, n_neighbors=n_neighbors + 1, return_distance=False
)

# ==================================================
# Occurrences: Lines 427-429 (2 instances)

GiGiT = np.dot(Gi, Gi.T)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/manifold/_mds.py
# Line: 129

distances = euclidean_distances(X)

# ==================================================
# Occurrences: Lines 142-142 (2 instances)

distances_flat = distances.ravel()

# ==================================================
# Occurrences: Lines 172-178 (6 instances)

distances = euclidean_distances(X)

# ==================================================
# Occurrences: Lines 186-186 (2 instances)

sum_squared_distances = (distances.ravel() ** 2).sum()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/manifold/_t_sne.py
# Line: 98

t0 = time()

# ==================================================
# Line: 123

duration = time() - t0

# ==================================================
# Line: 394

tic = time()

# ==================================================
# Line: 412

toc = time()

# ==================================================
# Occurrences: Lines 974-976 (2 instances)

t0 = time()

# ==================================================
# Occurrences: Lines 984-986 (2 instances)

t0 = time()

# ==================================================
# Line: 1086

params, kl_divergence, it = _gradient_descent(obj_func, params, **opt_args)

# ==================================================
# Line: 1102

params, kl_divergence, it = _gradient_descent(obj_func, params, **opt_args)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/manifold/_spectral_embedding.py
# Occurrences: Lines 55-61 (6 instances)

connected_nodes = np.zeros(n_node, dtype=bool)

# ==================================================
# Line: 345

laplacian = _set_diag(laplacian, 1, norm_laplacian)

# ==================================================
# Occurrences: Lines 389-392 (2 instances)

laplacian = check_array(
    laplacian, dtype=[np.float64, np.float32], accept_sparse=True
)

# ==================================================
# Occurrences: Lines 414-416 (3 instances)

X = random_state.standard_normal(size=(laplacian.shape[0], n_components + 1))

# ==================================================
# Line: 428

laplacian = check_array(
    laplacian, dtype=[np.float64, np.float32], accept_sparse=True
)

# ==================================================
# Occurrences: Lines 443-451 (4 instances)

laplacian = _set_diag(laplacian, 1, norm_laplacian)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/neighbors/_base.py
# Occurrences: Lines 1251-1259 (3 instances)

neigh_dist_chunks, neigh_ind_chunks = zip(*chunked_results)

# ==================================================
# Line: 1282

neigh_ind, neigh_dist = tuple(zip(*chunked_results))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/neighbors/_nca.py
# Line: 297

t_train = time.time()

# ==================================================
# Line: 327

t_train = time.time() - t_train

# ==================================================
# Line: 412

init_time = time.time()

# ==================================================
# Line: 432

print("done in {:5.2f}s".format(time.time() - init_time))

# ==================================================
# Line: 487

t_funcall = time.time()

# ==================================================
# Line: 511

t_funcall = time.time() - t_funcall

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/mixture/_base.py
# Line: 112

resp = np.zeros((n_samples, self.n_components), dtype=X.dtype)

# ==================================================
# Line: 127

resp = np.zeros((n_samples, self.n_components), dtype=X.dtype)

# ==================================================
# Line: 133

resp = np.zeros((n_samples, self.n_components), dtype=X.dtype)

# ==================================================
# Occurrences: Lines 243-243 (2 instances)

best_params = self._get_parameters()

# ==================================================
# Occurrences: Lines 266-266 (2 instances)

best_params = self._get_parameters()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/mixture/_gaussian_mixture.py
# Occurrences: Lines 484-493 (4 instances)

log_prob = np.empty((n_samples, n_components), dtype=X.dtype)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/mixture/_bayesian_mixture.py
# Line: 492

self.covariance_prior_ = check_array(
    self.covariance_prior, dtype=[np.float64, np.float32], ensure_2d=False
)

# ==================================================
# Line: 502

self.covariance_prior_ = check_array(
    self.covariance_prior, dtype=[np.float64, np.float32], ensure_2d=False
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/decomposition/_lda.py
# Occurrences: Lines 680-685 (2 instances)

doc_topics_distr, _ = self._e_step(
    X, cal_sstats=False, random_init=False, parallel=parallel
)

# ==================================================
# Occurrences: Lines 701-706 (2 instances)

doc_topics_distr, _ = self._e_step(
    X, cal_sstats=False, random_init=False, parallel=parallel
)

# ==================================================
# Occurrences: Lines 921-923 (2 instances)

word_cnt = X.sum() * (float(self.total_samples) / current_samples)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/decomposition/_factor_analysis.py
# Line: 445

comp_rot = np.dot(components, rotation_matrix)

# ==================================================
# Line: 457

return np.dot(components, rotation_matrix).T

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/decomposition/_nmf.py
# Line: 129

res = squared_norm(X - np.dot(W, H)) / 2.0

# ==================================================
# Line: 141

WH = np.dot(W, H)

# ==================================================
# Occurrences: Lines 304-305 (2 instances)

avg = np.sqrt(X.mean() / n_components)

# ==================================================
# Occurrences: Lines 359-364 (3 instances)

avg = X.mean()

# ==================================================
# Line: 814

start_time = time.time()

# ==================================================
# Line: 827

error_at_init = _beta_divergence(X, W, H, beta_loss, square_root=True)

# ==================================================
# Occurrences: Lines 873-876 (2 instances)

error = _beta_divergence(X, W, H, beta_loss, square_root=True)

# ==================================================
# Line: 888

end_time = time.time()

# ==================================================
# Occurrences: Lines 2281-2284 (2 instances)

H_buffer = H.copy()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/decomposition/_dict_learning.py
# Line: 121

err_mgt = np.seterr(all="ignore")

# ==================================================
# Line: 169

err_mgt = np.seterr(all="ignore")

# ==================================================
# Line: 573

t0 = time.time()

# ==================================================
# Line: 608

dt = time.time() - t0

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/decomposition/_pca.py
# Occurrences: Lines 518-520 (2 instances)

n_components = min(X.shape)

# ==================================================
# Line: 532

elif 1 <= n_components < 0.8 * min(X.shape):

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/inspection/_partial_dependence.py
# Occurrences: Lines 325-330 (2 instances)

predictions = predictions.reshape(n_samples, -1)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/inspection/_plot/partial_dependence.py
# Line: 1233

kind = [self.kind] * len(self.features)

# ==================================================
# Occurrences: Lines 1244-1249 (2 instances)

if len(kind) != len(self.features):

# ==================================================
# Line: 1319

n_features = len(self.features)

# ==================================================
# Occurrences: Lines 1353-1362 (6 instances)

self.axes_ = np.empty((n_rows, n_cols), dtype=object)

# ==================================================
# Occurrences: Lines 1386-1391 (4 instances)

self.lines_ = np.empty_like(ax, dtype=object)

# ==================================================
# Occurrences: Lines 1397-1402 (3 instances)

self.deciles_vlines_ = np.empty_like(self.axes_, dtype=object)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_bagging.py
# Occurrences: Lines 1451-1452 (2 instances)

predictions = np.zeros((n_samples,))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_gb.py
# Occurrences: Lines 199-204 (3 instances)

neg_g = neg_gradient.take(indices, axis=0)

# ==================================================
# Line: 211

neg_g = neg_gradient.take(indices, axis=0)

# ==================================================
# Occurrences: Lines 220-223 (2 instances)

numerator = np.average(neg_g, weights=sw)

# ==================================================
# Occurrences: Lines 229-231 (2 instances)

neg_g = neg_gradient.take(indices, axis=0)

# ==================================================
# Occurrences: Lines 554-555 (2 instances)

self.oob_improvement_ = np.zeros((self.n_estimators), dtype=np.float64)

# ==================================================
# Occurrences: Lines 598-601 (2 instances)

self.oob_improvement_ = np.zeros(
    (total_n_estimators,), dtype=np.float64
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py
# Line: 437

is_categorical = np.zeros(n_features, dtype=bool)

# ==================================================
# Line: 458

is_categorical = np.zeros(n_features, dtype=bool)

# ==================================================
# Line: 558

fit_start_time = time()

# ==================================================
# Occurrences: Lines 607-608 (2 instances)

self._random_seed = rng.randint(np.iinfo(np.uint32).max, dtype="u8")

# ==================================================
# Occurrences: Lines 895-895 (2 instances)

iteration_start_time = time()

# ==================================================
# Occurrences: Lines 976-978 (6 instances)

tic_pred = time()

# ==================================================
# Line: 1032

duration = time() - fit_start_time

# ==================================================
# Line: 1233

tic = time()

# ==================================================
# Line: 1241

toc = time()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_hist_gradient_boosting/grower.py
# Line: 405

tic = time()

# ==================================================
# Occurrences: Lines 424-426 (2 instances)

self.total_compute_hist_time += time() - tic

# ==================================================
# Line: 460

self.total_find_split_time += time() - tic

# ==================================================
# Line: 500

tic = time()

# ==================================================
# Line: 506

self.total_apply_split_time += time() - tic

# ==================================================
# Line: 618

tic = time()

# ==================================================
# Occurrences: Lines 632-639 (3 instances)

self.total_compute_hist_time += time() - tic

# ==================================================
# Occurrences: Lines 727-732 (2 instances)

binned_left_cat_bitsets = np.zeros(
    (self.n_categorical_splits, 8), dtype=X_BITSET_INNER_DTYPE
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/ensemble/_forest.py
# Occurrences: Lines 832-836 (2 instances)

y = np.copy(y)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/multiclass.py
# Line: 503

pred = _predict_binary(e, X)

# ==================================================
# Line: 512

indices.extend(np.where(_predict_binary(e, X) > thresh)[0])

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/model_selection/_search_successive_halving.py
# Line: 274

n_required_iterations = 1 + floor(log(len(candidate_params), self.factor))

# ==================================================
# Line: 326

n_candidates = len(candidate_params)

# ==================================================
# Line: 364

self.n_remaining_candidates_ = len(candidate_params)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/model_selection/_validation.py
# Occurrences: Lines 470-472 (4 instances)

results[i]["test_scores"] = formatted_error.copy()

# ==================================================
# Line: 849

start_time = time.time()

# ==================================================
# Line: 863

fit_time = time.time() - start_time

# ==================================================
# Occurrences: Lines 880-884 (2 instances)

fit_time = time.time() - start_time

# ==================================================
# Occurrences: Lines 2198-2206 (6 instances)

start_fit = time.time()

# ==================================================
# Occurrences: Lines 2228-2228 (2 instances)

score_time = time.time() - start_score

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/model_selection/_split.py
# Line: 616

n_groups = len(unique_groups)

# ==================================================
# Line: 646

group_to_fold = np.zeros(len(unique_groups))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/model_selection/_classification_threshold.py
# Occurrences: Lines 760-762 (3 instances)

self.estimator_ = clone(self.estimator)

# ==================================================
# Line: 769

train_idx, _ = next(cv.split(X, y, **routed_params.splitter.split))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/model_selection/_search.py
# Occurrences: Lines 873-877 (2 instances)

return scorers._accept_sample_weight()

# ==================================================
# Occurrences: Lines 1087-1092 (2 instances)

refit_start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/discriminant_analysis.py
# Occurrences: Lines 73-75 (2 instances)

s = empirical_covariance(X)

# ==================================================
# Line: 604

U, S, Vt = svd(X, full_matrices=False)

# ==================================================
# Line: 619

_, S, Vt = svd(X, full_matrices=False)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cluster/_affinity_propagation.py
# Occurrences: Lines 56-58 (4 instances)

(np.arange(n_samples), np.arange(n_samples), 0)

# ==================================================
# Occurrences: Lines 70-73 (3 instances)

A = np.zeros((n_samples, n_samples))

# ==================================================
# Line: 83

ind = np.arange(n_samples)

# ==================================================
# Occurrences: Lines 147-148 (2 instances)

c = np.argmax(S[:, I], axis=1)

# ==================================================
# Occurrences: Lines 155-156 (2 instances)

c = np.argmax(S[:, I], axis=1)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cluster/_birch.py
# Occurrences: Lines 56-71 (4 instances)

new_subcluster1 = _CFSubcluster()

# ==================================================
# Occurrences: Lines 562-577 (2 instances)

self.root_ = _CFNode(
    threshold=threshold,
    branching_factor=branching_factor,
    is_leaf=True,
    n_features=n_features,
    dtype=X.dtype,
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cluster/_bicluster.py
# Occurrences: Lines 158-168 (6 instances)

random_state = check_random_state(self.random_state)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cluster/_bisect_k_means.py
# Line: 413

self._X_mean = X.mean(axis=0)

# ==================================================
# Line: 419

center=X.mean(axis=0),

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cluster/_optics.py
# Occurrences: Lines 1102-1102 (2 instances)

sdas = _update_filter_sdas(sdas, mib, xi_complement, reachability_plot)

# ==================================================
# Occurrences: Lines 1112-1112 (2 instances)

sdas = _update_filter_sdas(sdas, mib, xi_complement, reachability_plot)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cluster/_mean_shift.py
# Occurrences: Lines 554-558 (2 instances)

labels = idxs.flatten()

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cluster/_hdbscan/hdbscan.py
# Line: 378

outlier_count = len(non_finite)

# ==================================================
# Line: 392

outlier_tree = np.zeros(len(non_finite), dtype=HIERARCHY_dtype)

# ==================================================
# Occurrences: Lines 925-927 (2 instances)

self.centroids_ = np.empty((n_clusters, X.shape[1]), dtype=np.float64)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cluster/_kmeans.py
# Line: 518

weight_in_clusters = np.zeros(n_clusters, dtype=X.dtype)

# ==================================================
# Line: 527

center_shift = np.zeros(n_clusters, dtype=X.dtype)

# ==================================================
# Line: 574

inertia = _inertia(X, sample_weight, centers, labels, n_threads)

# ==================================================
# Line: 616

inertia = _inertia(X, sample_weight, centers, labels, n_threads)

# ==================================================
# Occurrences: Lines 687-688 (2 instances)

weight_in_clusters = np.zeros(n_clusters, dtype=X.dtype)

# ==================================================
# Line: 712

inertia = _inertia(X, sample_weight, centers, labels, n_threads)

# ==================================================
# Line: 750

inertia = _inertia(X, sample_weight, centers, labels, n_threads)

# ==================================================
# Occurrences: Lines 1647-1650 (2 instances)

if to_reassign.sum() > 0.5 * X.shape[0]:

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cluster/_agglomerative.py
# Line: 353

coord_col = np.array(coord_col, dtype=np.intp, order="C")

# ==================================================
# Line: 360

inertia = np.empty(len(coord_row), dtype=np.float64, order="C")

# ==================================================
# Occurrences: Lines 400-403 (2 instances)

coord_col = np.array(coord_col, dtype=np.intp, order="C")

# ==================================================
# Line: 554

i, j = np.triu_indices(X.shape[0], k=1)

# ==================================================
# Line: 563

i, j = np.triu_indices(X.shape[0], k=1)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_base.py
# Line: 663

self.coef_ = np.vstack([out[0] for out in outs])

# ==================================================
# Line: 697

self.coef_ = np.vstack([out[0] for out in outs])

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_least_angle.py
# Line: 563

Gram = Gram.copy()

# ==================================================
# Line: 630

Gram_copy = Gram.copy()

# ==================================================
# Occurrences: Lines 687-687 (2 instances)

Cov[C_idx], Cov[0] = swap(Cov[C_idx], Cov[0])

# ==================================================
# Occurrences: Lines 737-737 (2 instances)

Cov[C_idx], Cov[0] = swap(Cov[C_idx], Cov[0])

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_glm/glm.py
# Line: 299

coef = sol.solve(X, y, sample_weight)

# ==================================================
# Line: 310

coef = sol.solve(X, y, sample_weight)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_coordinate_descent.py
# Occurrences: Lines 629-632 (2 instances)

elif len(alphas) > 1:

# ==================================================
# Line: 1668

X, y = validate_data(
    self, X, y, validate_separately=(check_X_params, check_y_params)
)

# ==================================================
# Line: 1693

X, y = validate_data(
    self, X, y, validate_separately=(check_X_params, check_y_params)
)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_bayes.py
# Occurrences: Lines 314-328 (2 instances)

coef_, sse_ = self._update_coef_(
    X, y, n_samples, n_features, XT_y, U, Vh, eigen_vals_, alpha_, lambda_
)

# ==================================================
# Occurrences: Lines 349-363 (2 instances)

self.coef_, sse_ = self._update_coef_(
    X, y, n_samples, n_features, XT_y, U, Vh, eigen_vals_, alpha_, lambda_
)

# ==================================================
# Occurrences: Lines 713-714 (2 instances)

sigma_ = update_sigma(X, alpha_, lambda_, keep_lambda)

# ==================================================
# Occurrences: Lines 754-755 (2 instances)

sigma_ = update_sigma(X, alpha_, lambda_, keep_lambda)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_stochastic_gradient.py
# Line: 199

coef_init = np.asarray(coef_init, dtype=input_dtype, order="C")

# ==================================================
# Line: 221

coef_init = np.asarray(coef_init, dtype=input_dtype, order="C")

# ==================================================
# Occurrences: Lines 235-246 (4 instances)

self.offset_ = intercept_init.reshape(
    1,
)

# ==================================================
# Occurrences: Lines 772-777 (2 instances)

self._standard_intercept = np.atleast_1d(intercept)

# ==================================================
# Line: 1332

binary = len(self.classes_) == 2

# ==================================================
# Line: 1356

prob_sum[all_zero] = len(self.classes_)

# ==================================================
# Occurrences: Lines 1758-1770 (5 instances)

self._average_intercept = np.atleast_1d(average_intercept)

# ==================================================
# Occurrences: Lines 2356-2368 (5 instances)

self._average_intercept = np.atleast_1d(average_intercept)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_sag.py
# Line: 267

coef_init = np.zeros((n_features, n_classes), dtype=X.dtype, order="C")

# ==================================================
# Occurrences: Lines 276-281 (2 instances)

intercept_init = np.zeros(n_classes, dtype=X.dtype)

# ==================================================
# Line: 292

sum_gradient_init = np.zeros((n_features, n_classes), dtype=X.dtype, order="C")

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_omp.py
# Occurrences: Lines 120-120 (2 instances)

Lkk = linalg.norm(X[:, lam]) ** 2 - v

# ==================================================
# Occurrences: Lines 126-126 (2 instances)

L[0, 0] = linalg.norm(X[:, lam])

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_ridge.py
# Occurrences: Lines 1889-1890 (2 instances)

X_mean = X_mean * n_samples / sqrt_sw.dot(sqrt_sw)

# ==================================================
# Occurrences: Lines 1927-1930 (4 instances)

X_batch[:, :-1] = X[batch].toarray() - X_mean * scale[batch][:, None]

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_logistic.py
# Occurrences: Lines 533-535 (4 instances)

w0 = np.concatenate([coef_.ravel(), intercept_])

# ==================================================
# Line: 1253

if self.multi_class == "multinomial" and len(self.classes_) == 2:

# ==================================================
# Occurrences: Lines 1284-1287 (2 instances)

multi_class = _check_multi_class(multi_class, solver, len(self.classes_))

# ==================================================
# Line: 1324

n_classes = len(self.classes_)

# ==================================================
# Line: 1333

if len(self.classes_) == 2:

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/linear_model/_linear_loss.py
# Occurrences: Lines 623-623 (2 instances)

] = sandwich_dot(X, h)

# ==================================================
# Occurrences: Lines 636-636 (2 instances)

h.sum()

# ==================================================
# Occurrences: Lines 645-645 (2 instances)

] = sandwich_dot(X, h)

# ==================================================
# Occurrences: Lines 657-657 (2 instances)

h.sum()

# ==================================================
# Line: 773

grad = np.empty((n_classes, n_dof), dtype=weights.dtype, order="F")

# ==================================================
# Line: 813

hess_prod = np.empty((n_classes, n_dof), dtype=weights.dtype, order="F")

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/impute/_base.py
# Line: 903

imputer_mask = _get_mask(X, self.missing_values)

# ==================================================
# Line: 912

n_missing = imputer_mask.sum(axis=0)

# ==================================================
# Occurrences: Lines 920-925 (2 instances)

imputer_mask = _get_mask(X, self.missing_values)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/impute/_iterative.py
# Occurrences: Lines 659-661 (2 instances)

X_filled = self.initial_imputer_.fit_transform(X)

# ==================================================
# Occurrences: Lines 668-670 (2 instances)

X_filled = self.initial_imputer_.transform(X)

# ==================================================
# Occurrences: Lines 847-849 (2 instances)

start_t = time()

# ==================================================
# Line: 877

% (self.n_iter_, self.max_iter, time() - start_t)

# ==================================================
# Line: 892

Xt_previous = Xt.copy()

# ==================================================
# Line: 934

start_t = time()

# ==================================================
# Line: 949

% (i_rnd + 1, self.n_iter_, time() - start_t)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/gaussian_process/kernels.py
# Occurrences: Lines 633-638 (2 instances)

K_single, K_grad_single = kernel(X, Y, eval_gradient)

# ==================================================
# Line: 1557

K = np.exp(-0.5 * dists)

# ==================================================
# Line: 1565

K = np.exp(-0.5 * dists)

# ==================================================
# Line: 1930

length_scale_gradient = np.empty((K.shape[0], K.shape[1], 0))

# ==================================================
# Line: 1940

alpha_gradient = np.empty((K.shape[0], K.shape[1], 0))

# ==================================================
# Line: 2077

length_scale_gradient = np.empty((K.shape[0], K.shape[1], 0))

# ==================================================
# Line: 2085

periodicity_gradient = np.empty((K.shape[0], K.shape[1], 0))

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/cross_decomposition/_pls.py
# Occurrences: Lines 272-277 (6 instances)

self.x_weights_ = np.zeros((p, n_components))  # U

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/feature_extraction/_dict_vectorizer.py
# Line: 202

assert array("i").itemsize == 4, (

# ==================================================
# Line: 221

indices = array("i")

# ==================================================
# Line: 257

vocab[feature_name] = len(feature_names)

# ==================================================
# Line: 279

map_index = np.empty(len(feature_names), dtype=np.int32)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/feature_extraction/text.py
# Line: 387

if id(self.stop_words) == getattr(self, "_stop_words_id", None):

# ==================================================
# Line: 399

self._stop_words_id = id(self.stop_words)

# ==================================================
# Line: 412

self._stop_words_id = id(self.stop_words)

# ==================================================
# Occurrences: Lines 1388-1393 (2 instances)

X = self._sort_features(X, vocabulary)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/naive_bayes.py
# Occurrences: Lines 440-442 (3 instances)

n_classes = len(self.classes_)

# ==================================================
# Line: 462

self.class_prior_ = np.zeros(len(self.classes_), dtype=np.float64)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/covariance/_graph_lasso.py
# Occurrences: Lines 564-568 (2 instances)

self.location_ = np.zeros(X.shape[1])

# ==================================================
# Line: 1008

t0 = time.time()

# ==================================================
# Line: 1083

% (i + 1, n_refinements, time.time() - t0)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/covariance/_robust_covariance.py
# Line: 132

precision = linalg.pinvh(covariance)

# ==================================================
# Occurrences: Lines 140-147 (3 instances)

covariance = cov_computation_method(X_support)

# ==================================================
# Line: 157

precision = linalg.pinvh(covariance)

# ==================================================
# Occurrences: Lines 164-165 (2 instances)

covariance = cov_computation_method(X_support)

# ==================================================
# Line: 454

support = np.zeros(n_samples, dtype=bool)

# ==================================================
# Occurrences: Lines 460-461 (2 instances)

precision = linalg.pinvh(covariance)

# ==================================================
# Occurrences: Lines 468-469 (2 instances)

precision = linalg.pinvh(covariance)

# ==================================================
# Line: 476

samples_shuffle = random_state.permutation(n_samples)

# ==================================================
# Occurrences: Lines 486-491 (2 instances)

all_best_covariances = np.zeros((n_best_tot, n_features, n_features))

# ==================================================
# Line: 518

selection = random_state.permutation(n_samples)[:n_samples_merged]

# ==================================================
# Line: 532

support = np.zeros(n_samples, dtype=bool)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/covariance/_shrunk_covariance.py
# Occurrences: Lines 371-379 (6 instances)

rows = slice(block_size * i, block_size * (i + 1))

# ==================================================
