# cached-repeated-calls snippets for keras

# File: /root/ecooptimizer/keras/integration_tests/model_visualization_test.py
# Occurrences: Lines 28-31 (2 instances)

attributes = node.get_attributes()

# ==================================================
# File: /root/ecooptimizer/keras/integration_tests/tf_distribute_training_test.py
# Occurrences: Lines 29-30 (2 instances)

x = layers.Dense(256, activation="relu")(x)

# ==================================================
# File: /root/ecooptimizer/keras/integration_tests/dataset_tests/boston_housing_test.py
# Occurrences: Lines 13-14 (2 instances)

first_load = boston_housing.load_data(seed=seed)

# ==================================================
# File: /root/ecooptimizer/keras/integration_tests/dataset_tests/california_housing_test.py
# Occurrences: Lines 29-30 (2 instances)

first_load = california_housing.load_data(version="large", seed=seed)

# ==================================================
# File: /root/ecooptimizer/keras/integration_tests/basic_full_flow.py
# Occurrences: Lines 17-18 (2 instances)

self.dense1 = layers.Dense(hidden_dim, activation="relu")

# ==================================================
# Occurrences: Lines 32-33 (2 instances)

x = np.random.random((128, 4))

# ==================================================
# Occurrences: Lines 42-46 (2 instances)

output_before_fit = model(x)

# ==================================================
# File: /root/ecooptimizer/keras/api_gen.py
# Line: 45

init_file = f.read()

# ==================================================
# Occurrences: Lines 95-95 (3 instances)

legacy_contents = f.read()

# ==================================================
# Occurrences: Lines 101-101 (3 instances)

core_api_contents = f.read()

# ==================================================
# Line: 149

build_api_dir = os.path.join(build_dir, PACKAGE)

# ==================================================
# Line: 168

create_legacy_directory(package_dir=os.path.join(build_dir, PACKAGE))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/callback_test.py
# Occurrences: Lines 29-30 (2 instances)

x = np.random.random((8, 1))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/tensorboard_test.py
# Line: 755

callbacks.TensorBoard(
    logdir, histogram_freq=1, profile_batch=1, write_graph=False
)

# ==================================================
# Line: 763

tb_cbk = callbacks.TensorBoard(
    logdir, histogram_freq=1, profile_batch=1, write_graph=False
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/csv_logger_test.py
# Line: 52

model = make_model()

# ==================================================
# Line: 72

model = make_model()

# ==================================================
# Line: 106

model = make_model()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/model_checkpoint_test.py
# Line: 55

temp_dir = self.get_temp_dir()

# ==================================================
# Line: 197

temp_dir = self.get_temp_dir()

# ==================================================
# Line: 233

temp_dir = self.get_temp_dir()

# ==================================================
# Line: 291

temp_dir = self.get_temp_dir()

# ==================================================
# Line: 319

temp_dir = self.get_temp_dir()

# ==================================================
# Occurrences: Lines 518-519 (2 instances)

model = get_model()

# ==================================================
# Occurrences: Lines 542-545 (2 instances)

ref_weights = model.get_weights()

# ==================================================
# Occurrences: Lines 551-552 (2 instances)

model = get_model()

# ==================================================
# Occurrences: Lines 576-580 (3 instances)

ref_weights = model.get_weights()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/monitor_callback_test.py
# Occurrences: Lines 15-18 (4 instances)

x_train = np.random.random((10, 5))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/early_stopping_test.py
# Occurrences: Lines 15-18 (4 instances)

x_train = np.random.random((10, 5))

# ==================================================
# Occurrences: Lines 119-126 (2 instances)

history1 = model.fit(
    data, labels, callbacks=[stopper], verbose=0, epochs=20
)

# ==================================================
# Line: 187

early_stop = callbacks.EarlyStopping(
    monitor="val_loss",
    patience=5,
    baseline=0.5,
    restore_best_weights=True,
)

# ==================================================
# Line: 211

early_stop = callbacks.EarlyStopping(
    monitor="val_loss",
    patience=5,
    baseline=0.5,
    restore_best_weights=True,
)

# ==================================================
# Occurrences: Lines 248-255 (2 instances)

stopper = callbacks.EarlyStopping(
    monitor="mse",
    patience=patience,
    start_from_epoch=start_from_epoch,
)

# ==================================================
# Occurrences: Lines 262-269 (2 instances)

stopper = callbacks.EarlyStopping(
    monitor="mse",
    patience=patience,
    start_from_epoch=start_from_epoch,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/early_stopping.py
# Line: 106

self.best_weights = self.model.get_weights()

# ==================================================
# Line: 114

self.best_weights = self.model.get_weights()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/swap_ema_weights_test.py
# Line: 69

model = self._get_compiled_model()

# ==================================================
# Line: 76

logs = model.evaluate(self.x_train, self.y_train, return_dict=True)

# ==================================================
# Line: 84

model = self._get_compiled_model()

# ==================================================
# Line: 92

logs = model.evaluate(self.x_train, self.y_train, return_dict=True)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/reduce_lr_on_plateau.py
# Line: 88

logs["learning_rate"] = float(
    backend.convert_to_numpy(self.model.optimizer.learning_rate)
)

# ==================================================
# Line: 111

old_lr = float(
    backend.convert_to_numpy(
        self.model.optimizer.learning_rate
    )
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/losses/losses_test.py
# Occurrences: Lines 336-346 (3 instances)

loss = hinge_obj(y_true, y_pred)

# ==================================================
# Occurrences: Lines 360-370 (3 instances)

loss = hinge_obj(y_true, y_pred, sample_weight=sample_weight)

# ==================================================
# Occurrences: Lines 397-407 (3 instances)

loss = hinge_obj(y_true, y_pred)

# ==================================================
# Occurrences: Lines 421-431 (3 instances)

loss = hinge_obj(y_true, y_pred, sample_weight=sample_weight)

# ==================================================
# Occurrences: Lines 458-468 (3 instances)

loss = hinge_obj(y_true, y_pred)

# ==================================================
# Occurrences: Lines 482-492 (3 instances)

loss = hinge_obj(y_true, y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 648

loss = h_obj(self.y_true, self.y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 655

loss_2 = h_obj(self.y_true, self.y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 744

loss = logcosh_obj(
    self.y_true, self.y_pred, sample_weight=sample_weight
)

# ==================================================
# Line: 753

loss_2 = logcosh_obj(
    self.y_true, self.y_pred, sample_weight=sample_weight
)

# ==================================================
# Line: 841

loss = k_obj(self.y_true, self.y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 848

loss_2 = k_obj(self.y_true, self.y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 927

loss = poisson_obj(
    self.y_true, self.y_pred, sample_weight=sample_weight
)

# ==================================================
# Line: 937

loss_2 = poisson_obj(
    self.y_true, self.y_pred, sample_weight=sample_weight
)

# ==================================================
# Occurrences: Lines 1018-1025 (4 instances)

bce_obj = losses.BinaryCrossentropy()

# ==================================================
# Occurrences: Lines 1315-1333 (7 instances)

logits = np.array([[[0.854, 0.698, 0.598], [0.088, 0.86, 0.018]]])

# ==================================================
# Occurrences: Lines 1342-1347 (2 instances)

output = losses.SparseCategoricalCrossentropy()(y_true, y_pred)

# ==================================================
# Occurrences: Lines 1357-1363 (2 instances)

output = losses.SparseCategoricalCrossentropy()(y_true, y_pred)

# ==================================================
# Occurrences: Lines 1372-1382 (3 instances)

y_pred_reshaped = np.moveaxis(y_pred, source=2, destination=0)

# ==================================================
# Occurrences: Lines 1390-1405 (4 instances)

escaped_message = re.escape(expected_message)

# ==================================================
# Occurrences: Lines 1414-1418 (2 instances)

y_pred_reshaped = np.moveaxis(y_pred, source=2, destination=0)

# ==================================================
# Line: 1431

y_true = np.array(
    [[0, 1, 2, 0], [1, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1]]
)

# ==================================================
# Occurrences: Lines 1462-1467 (2 instances)

output = losses.SparseCategoricalCrossentropy()(y_true, y_pred)

# ==================================================
# Occurrences: Lines 1503-1509 (2 instances)

output = losses.SparseCategoricalCrossentropy()(y_true, y_pred)

# ==================================================
# Occurrences: Lines 1538-1548 (3 instances)

y_pred_reshaped = np.moveaxis(y_pred, source=2, destination=0)

# ==================================================
# Occurrences: Lines 1556-1571 (4 instances)

escaped_message = re.escape(expected_message)

# ==================================================
# Occurrences: Lines 1607-1610 (2 instances)

y_pred_reshaped = np.moveaxis(y_pred, source=2, destination=0)

# ==================================================
# Occurrences: Lines 1997-2001 (2 instances)

loss = circle_loss(self.y_true, self.y_pred)

# ==================================================
# Line: 2139

y_true = np.array(
    [[0, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1]]
)

# ==================================================
# Occurrences: Lines 2150-2157 (2 instances)

output = losses.CategoricalGeneralizedCrossEntropy(q=0.5)(
    y_true, y_pred
)

# ==================================================
# Occurrences: Lines 2172-2180 (2 instances)

output = losses.CategoricalGeneralizedCrossEntropy(q=0.5)(
    y_true, y_pred
)

# ==================================================
# Occurrences: Lines 2209-2216 (2 instances)

output = losses.CategoricalGeneralizedCrossEntropy(q=0.5)(
    y_true, y_pred
)

# ==================================================
# Line: 2252

output = losses.CategoricalGeneralizedCrossEntropy(q=0.5)(
    y_true, y_pred
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/losses/loss_test.py
# Occurrences: Lines 32-52 (12 instances)

x1 = ops.ones((3,))

# ==================================================
# Line: 62

loss = loss_fn(y_true, y_pred)

# ==================================================
# Line: 68

loss = loss_fn(y_true, y_pred)

# ==================================================
# Line: 74

loss = loss_fn(y_true, y_pred)

# ==================================================
# Line: 100

loss = loss_fn(y_true, y_pred)

# ==================================================
# Line: 109

loss = loss_fn(y_true, y_pred)

# ==================================================
# Line: 119

loss = loss_fn(y_true, y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 127

loss = loss_fn(y_true, y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 176

rank1_loss = loss_fn(y_true, y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 184

rank2_loss = loss_fn(y_true, y_pred, sample_weight=sample_weight)

# ==================================================
# Occurrences: Lines 264-269 (2 instances)

loss = loss_fn(y_true, y_pred)

# ==================================================
# Occurrences: Lines 283-288 (2 instances)

loss = loss_fn(y_true, y_pred)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/saving_api_test.py
# Line: 242

src_model = self.get_model()

# ==================================================
# Line: 249

dest_model = self.get_model()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/file_editor_test.py
# Occurrences: Lines 42-47 (2 instances)

out = editor.compare(target_model)  # Fails

# ==================================================
# Line: 54

out = editor.compare(target_model)  # Succeeds

# ==================================================
# Occurrences: Lines 60-65 (2 instances)

out = editor.compare(target_model)  # Fails

# ==================================================
# Occurrences: Lines 75-84 (3 instances)

out = editor.compare(target_model)  # Succeeds

# ==================================================
# Line: 90

out = editor.compare(target_model)  # Succeeds

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/saving_lib_test.py
# Occurrences: Lines 460-470 (6 instances)

model = _get_basic_functional_model()

# ==================================================
# Line: 486

model = _get_subclassed_model()

# ==================================================
# Line: 492

new_model = _get_subclassed_model()

# ==================================================
# Occurrences: Lines 502-512 (6 instances)

model = _get_basic_functional_model()

# ==================================================
# Occurrences: Lines 520-532 (5 instances)

model = _get_basic_functional_model()

# ==================================================
# Line: 583

new_layer_kernel_value = np.array(new_model.layers[1].kernel)

# ==================================================
# Line: 595

np.array(new_model.layers[1].kernel), new_layer_kernel_value

# ==================================================
# Line: 607

new_layer_kernel_value = np.array(new_model.layers[2].kernel)

# ==================================================
# Line: 620

np.array(new_model.layers[2].kernel), new_layer_kernel_value

# ==================================================
# Line: 633

model = saving_lib.load_model(out)

# ==================================================
# Line: 641

new_model = saving_lib.load_model(out)

# ==================================================
# Occurrences: Lines 756-758 (2 instances)

reused_layer = keras.layers.Dense(4)

# ==================================================
# Occurrences: Lines 783-785 (2 instances)

model = model_fn(weights=None, input_shape=shape)

# ==================================================
# Occurrences: Lines 805-807 (2 instances)

model = model_fn(weights=None, input_shape=shape)

# ==================================================
# Occurrences: Lines 834-838 (2 instances)

_ = saving_api.load_model(temp_filepath)

# ==================================================
# Occurrences: Lines 844-847 (2 instances)

ref_output = model.predict(ref_input)

# ==================================================
# Occurrences: Lines 853-856 (2 instances)

ref_output = model.predict(ref_input)

# ==================================================
# Occurrences: Lines 898-901 (3 instances)

ref_out = model(data)

# ==================================================
# Occurrences: Lines 914-917 (3 instances)

ref_out = model(data)

# ==================================================
# Line: 1011

self.dense = keras.layers.Dense(3)

# ==================================================
# Line: 1022

self.a_dense = keras.layers.Dense(3)

# ==================================================
# Line: 1187

layer = keras.layers.Dense(units=16)

# ==================================================
# Line: 1204

revived_layer = keras.layers.Dense(units=16)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/saving_lib.py
# Line: 339

elif str(filepath).startswith("hf://"):

# ==================================================
# Line: 356

filepath = str(filepath)

# ==================================================
# Line: 822

currently_failed = len(failed_saveables)

# ==================================================
# Line: 856

newly_failed = len(failed_saveables) - currently_failed

# ==================================================
# Occurrences: Lines 949-954 (2 instances)

self.tmp_dir = get_temp_dir()

# ==================================================
# Occurrences: Lines 961-964 (2 instances)

self.tmp_dir = get_temp_dir()

# ==================================================
# Occurrences: Lines 1390-1395 (2 instances)

total_len = self._h5_entry_group.__len__()

# ==================================================
# Line: 1429

return super().__getitem__(key)

# ==================================================
# Line: 1436

item = super().__getitem__(key)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/object_registration_test.py
# Occurrences: Lines 19-21 (4 instances)

actual_custom_fn = keras.activations.get("custom_fn")

# ==================================================
# Occurrences: Lines 27-29 (4 instances)

actual_custom_fn = keras.activations.get("custom_fn")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/serialization_lib_test.py
# Occurrences: Lines 118-122 (2 instances)

_, new_obj, _ = self.roundtrip(obj)

# ==================================================
# Occurrences: Lines 140-157 (7 instances)

_ = new_dense(x)

# ==================================================
# Occurrences: Lines 165-167 (2 instances)

_ = new_layer(x)

# ==================================================
# Occurrences: Lines 216-221 (2 instances)

original_output = model(
    {"foo": np.zeros((2, 2)), "bar": np.zeros((2, 2))}
)

# ==================================================
# Occurrences: Lines 228-229 (2 instances)

input_1 = keras.Input((2,))

# ==================================================
# Occurrences: Lines 247-251 (3 instances)

inputs = keras.Input((2,), batch_size=3)

# ==================================================
# Line: 257

y2 = new_model(x)

# ==================================================
# Line: 263

inputs = keras.Input((2,), batch_size=3)

# ==================================================
# Occurrences: Lines 272-273 (2 instances)

x = ops.random.normal((2, 2))

# ==================================================
# Line: 281

y2 = new_model(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/file_editor.py
# Occurrences: Lines 84-86 (2 instances)

config_json = f.read()

# ==================================================
# Occurrences: Lines 520-520 (2 instances)

bold_key = summary_utils.bold_text(key)

# ==================================================
# Occurrences: Lines 542-542 (2 instances)

bold_key = summary_utils.bold_text(key)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/datasets/fashion_mnist.py
# Line: 81

y_train = np.frombuffer(lbpath.read(), np.uint8, offset=8)

# ==================================================
# Line: 89

y_test = np.frombuffer(lbpath.read(), np.uint8, offset=8)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/datasets/cifar100.py
# Occurrences: Lines 74-77 (2 instances)

x_train, y_train = load_batch(fpath, label_key=label_mode + "_labels")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/datasets/cifar10.py
# Occurrences: Lines 86-89 (2 instances)

) = load_batch(fpath)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/datasets/imdb.py
# Line: 91

indices = np.arange(len(x_train))

# ==================================================
# Line: 137

idx = len(x_train)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/trainer_test.py
# Occurrences: Lines 80-89 (2 instances)

self.dense_1 = layers.Dense(
    units,
    use_bias=False,
    kernel_initializer=initializers.Ones(),
)

# ==================================================
# Occurrences: Lines 102-111 (2 instances)

self.dense_1 = layers.Dense(
    units,
    use_bias=False,
    kernel_initializer=initializers.Ones(),
)

# ==================================================
# Occurrences: Lines 122-131 (2 instances)

self.dense_1 = layers.Dense(
    units,
    use_bias=False,
    kernel_initializer=initializers.Ones(),
)

# ==================================================
# Line: 679

history = model.fit(
    x,
    y,
    batch_size=batch_size,
    steps_per_epoch=steps_per_epoch if use_steps_per_epoch else None,
    epochs=epochs,
    validation_split=0.2,
)

# ==================================================
# Line: 694

history = model.fit(
    x,
    y,
    batch_size=batch_size,
    steps_per_epoch=steps_per_epoch if use_steps_per_epoch else None,
    epochs=epochs,
    validation_split=0.2,
)

# ==================================================
# Occurrences: Lines 900-902 (2 instances)

dataset = sparse_generator(generator_type)

# ==================================================
# Occurrences: Lines 1737-1738 (2 instances)

x = np.ones((128, 1))

# ==================================================
# Occurrences: Lines 1744-1745 (2 instances)

x = np.ones((128, 1))

# ==================================================
# Occurrences: Lines 1751-1752 (2 instances)

x = np.ones((128, 1))

# ==================================================
# Line: 1786

optimizer = optimizers.SGD(learning_rate=1e9)

# ==================================================
# Line: 1795

optimizer = optimizers.SGD(learning_rate=1e9)

# ==================================================
# Line: 1808

y = np.zeros((128, 1))

# ==================================================
# Line: 1814

self.assertAllClose(preds, np.zeros((128, 1)))

# ==================================================
# Line: 1857

output = model.predict_on_batch(x)

# ==================================================
# Line: 1866

output = model.predict_on_batch(x)

# ==================================================
# Line: 1914

x1, x2 = np.random.rand(2, 3, 4)

# ==================================================
# Line: 1923

x1, x2 = np.random.rand(2, 3, 4)

# ==================================================
# Occurrences: Lines 1933-1936 (4 instances)

x = np.ones((16, 4))

# ==================================================
# Occurrences: Lines 1974-1978 (2 instances)

keys = sorted(list(logs.keys()))

# ==================================================
# Occurrences: Lines 1987-1991 (2 instances)

keys = sorted(list(logs.keys()))

# ==================================================
# Occurrences: Lines 2000-2036 (10 instances)

keys = sorted(list(logs.keys()))

# ==================================================
# Occurrences: Lines 2043-2046 (4 instances)

x = np.ones((16, 4))

# ==================================================
# Line: 2139

y = model.predict(x)

# ==================================================
# Line: 2146

y = model.predict(x)

# ==================================================
# Occurrences: Lines 2159-2160 (2 instances)

out2 = model.predict_on_batch(np.ones((2, 20)))

# ==================================================
# Occurrences: Lines 2170-2179 (2 instances)

eval_out_1 = model.evaluate(
    np.ones((3, 2)), np.ones((3, 3)), return_dict=True
)

# ==================================================
# Line: 2204

eval_out = model.evaluate(np.ones((3, 2)), np.ones((3, 3)))

# ==================================================
# Line: 2212

eval_out = model.evaluate(np.ones((3, 2)), np.ones((3, 3)))

# ==================================================
# Occurrences: Lines 2350-2351 (2 instances)

out_1 = model.predict(x)

# ==================================================
# Occurrences: Lines 2359-2370 (6 instances)

self.train_counter = self.add_weight(
    shape=(),
    initializer="zeros",
)

# ==================================================
# Occurrences: Lines 2577-2578 (2 instances)

x = np.ones((dataset_size, 4))

# ==================================================
# Occurrences: Lines 2607-2610 (4 instances)

x1 = np.ones((dataset_size, 4))

# ==================================================
# Occurrences: Lines 2633-2635 (3 instances)

x = np.ones((dataset_size, 4))

# ==================================================
# Occurrences: Lines 2654-2656 (2 instances)

partial_model = keras.Model(inputs, [x, x, x])

# ==================================================
# Line: 2693

ref_weights = model.get_weights()

# ==================================================
# Line: 2703

weights = model.get_weights()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/compile_utils.py
# Occurrences: Lines 373-373 (3 instances)

results[name] = m.result()

# ==================================================
# Occurrences: Lines 379-379 (3 instances)

results[name] = m.result()

# ==================================================
# Occurrences: Lines 389-389 (3 instances)

results[name] = m.result()

# ==================================================
# Occurrences: Lines 401-401 (3 instances)

results[name] = m.result()

# ==================================================
# Occurrences: Lines 729-733 (2 instances)

y_true = tree.pack_sequence_as(y_pred, tree.flatten(y_true))

# ==================================================
# Line: 773

self._y_true_build_structure, tree.flatten(y_true)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/compile_utils_test.py
# Occurrences: Lines 23-24 (2 instances)

y_true = backend.KerasTensor((3, 4))

# ==================================================
# Line: 40

result = compile_metrics.result()

# ==================================================
# Line: 47

result = compile_metrics.result()

# ==================================================
# Line: 106

result = compile_metrics.result()

# ==================================================
# Line: 113

result = compile_metrics.result()

# ==================================================
# Line: 175

result = compile_metrics.result()

# ==================================================
# Line: 197

result = compile_metrics.result()

# ==================================================
# Occurrences: Lines 245-246 (2 instances)

y_true = backend.KerasTensor((3, 4))

# ==================================================
# Occurrences: Lines 259-260 (2 instances)

y_true = backend.KerasTensor((3, 4))

# ==================================================
# Occurrences: Lines 560-562 (2 instances)

ones = np.ones((320, 3))

# ==================================================
# Occurrences: Lines 568-570 (2 instances)

compile_loss(y_true, y_pred)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/epoch_iterator.py
# Line: 111

self._current_iterator = iter(self._get_iterator())

# ==================================================
# Occurrences: Lines 121-124 (2 instances)

self._current_iterator = iter(self._get_iterator())

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/array_slicing.py
# Occurrences: Lines 396-396 (2 instances)

x = np.asarray(x)

# ==================================================
# Occurrences: Lines 407-407 (2 instances)

x = np.asarray(x)

# ==================================================
# Occurrences: Lines 423-423 (2 instances)

and not backend.standardize_dtype(dtype) == backend.floatx()

# ==================================================
# Occurrences: Lines 429-432 (4 instances)

cast_dtype = backend.floatx()

# ==================================================
# Occurrences: Lines 453-453 (2 instances)

x = np.asarray(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/array_data_adapter.py
# Line: 220

options = tf.data.Options()

# ==================================================
# Line: 228

dataset = dataset.with_options(options)

# ==================================================
# Occurrences: Lines 237-241 (2 instances)

options = tf.data.Options()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/tf_dataset_adapter_test.py
# Occurrences: Lines 88-106 (8 instances)

dataset = tf.data.Dataset.range(42)

# ==================================================
# Occurrences: Lines 139-142 (2 instances)

adapter = tf_dataset_adapter.TFDatasetAdapter(
    base_ds, class_weight=class_weight
)

# ==================================================
# Occurrences: Lines 149-152 (2 instances)

adapter = tf_dataset_adapter.TFDatasetAdapter(
    base_ds, class_weight=class_weight
)

# ==================================================
# Occurrences: Lines 161-162 (2 instances)

y1 = np.array([0, 1, 2, 3], dtype="int64")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/data_adapter_utils.py
# Occurrences: Lines 148-152 (4 instances)

rank = len(x.shape)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/py_dataset_adapter_test.py
# Occurrences: Lines 267-271 (3 instances)

gen = adapter.get_numpy_iterator()

# ==================================================
# Occurrences: Lines 287-291 (3 instances)

gen = adapter.get_numpy_iterator()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/trainer.py
# Line: 433

new_v = scope.get_current_value(v)

# ==================================================
# Line: 439

new_v = scope.get_current_value(v)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/epoch_iterator_test.py
# Occurrences: Lines 122-127 (2 instances)

np.random.random((100, 16)), np.random.random((100, 4))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/operation_test.py
# Line: 74

out = op(x, y=y, z=z)

# ==================================================
# Line: 83

out = op(x, y=y, z=z)

# ==================================================
# Occurrences: Lines 102-104 (3 instances)

x = knp.ones((2, 3))

# ==================================================
# Occurrences: Lines 150-151 (2 instances)

x = np.ones((2,))

# ==================================================
# Line: 158

self.assertAllClose(out, 6 * np.ones((2,)))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/function_test.py
# Occurrences: Lines 17-18 (2 instances)

x1 = keras_tensor.KerasTensor((2, 3))

# ==================================================
# Line: 28

y_val = fn([np.ones((2, 3)), np.ones((2, 3))])

# ==================================================
# Occurrences: Lines 34-35 (2 instances)

x1_alt = keras_tensor.KerasTensor((2, 3))

# ==================================================
# Line: 44

y_val = fn([np.ones((2, 3)), np.ones((2, 3))])

# ==================================================
# Occurrences: Lines 70-71 (2 instances)

x1 = keras_tensor.KerasTensor((2, 3))

# ==================================================
# Occurrences: Lines 86-87 (2 instances)

x1_alt = keras_tensor.KerasTensor((2, 3))

# ==================================================
# Occurrences: Lines 95-96 (2 instances)

x1 = keras_tensor.KerasTensor((2, 3))

# ==================================================
# Occurrences: Lines 126-130 (2 instances)

config = model.get_config()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/core_test.py
# Line: 130

out = core.unstack(x, axis=axis)

# ==================================================
# Occurrences: Lines 145-149 (2 instances)

core.unstack(x, axis=axis)

# ==================================================
# Occurrences: Lines 157-164 (3 instances)

out = core.convert_to_tensor(x, sparse=True)

# ==================================================
# Line: 230

init = np.array(0, dtype="float32")

# ==================================================
# Line: 251

init = (np.array(0, dtype="float32"), np.array(1, dtype="float32"))

# ==================================================
# Line: 279

init = np.array(0, dtype="float32")

# ==================================================
# Occurrences: Lines 324-325 (2 instances)

DB = np.random.rand(b, l, d, n)

# ==================================================
# Line: 390

core.scatter_update(inputs, indices, updates),

# ==================================================
# Line: 399

core.scatter_update(inputs, indices, updates),

# ==================================================
# Line: 407

outputs = core.scatter_update(inputs, indices, updates)

# ==================================================
# Occurrences: Lines 414-435 (6 instances)

inputs = np.arange(10)

# ==================================================
# Line: 458

core.slice_update(inputs, start_indices, updates),

# ==================================================
# Line: 467

core.slice_update(inputs, start_indices, updates),

# ==================================================
# Occurrences: Lines 474-476 (3 instances)

updates = np.zeros([2, 2, 2, 2])

# ==================================================
# Occurrences: Lines 485-486 (2 instances)

x = np.random.rand(2, 3, 4).astype("float32")

# ==================================================
# Occurrences: Lines 588-589 (4 instances)

self.w = self.add_weight(shape=(1,), initializer="zeros")

# ==================================================
# Line: 662

x = ops.convert_to_numpy(x)

# ==================================================
# Line: 668

np_x = ops.convert_to_numpy(x)

# ==================================================
# Occurrences: Lines 786-790 (2 instances)

y = ops.cast(x, "float16")

# ==================================================
# Occurrences: Lines 801-811 (4 instances)

y = ops.cast(x, float8_dtype)

# ==================================================
# Occurrences: Lines 818-822 (2 instances)

y = ops.saturate_cast(x, "float16")

# ==================================================
# Line: 831

output = ops.vectorized_map(fn, ops.zeros((2, 3), dtype="float32"))

# ==================================================
# Line: 837

output = ops.vectorized_map(fn, ops.zeros((2, 3), dtype="float32"))

# ==================================================
# Line: 868

e = ops.exp(x)

# ==================================================
# Line: 878

return ops.log(1 + ops.exp(x))

# ==================================================
# Line: 886

y = log1pexp(x)

# ==================================================
# Line: 904

z = log1pexp(x)

# ==================================================
# Occurrences: Lines 1091-1100 (4 instances)

x = np.random.rand(2, 3, 4).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/operation_utils_test.py
# Occurrences: Lines 10-11 (2 instances)

x1 = backend.KerasTensor(shape=(2,))

# ==================================================
# Line: 24

output_shape = operation_utils.compute_expand_dims_output_shape(
    input_shape, axis
)

# ==================================================
# Line: 32

output_shape = operation_utils.compute_expand_dims_output_shape(
    input_shape, axis
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/nn_test.py
# Occurrences: Lines 64-68 (4 instances)

combined_mask = np.logical_and(combined_mask, mask)

# ==================================================
# Line: 1621

x = np.arange(540, dtype=float).reshape(input_shape)

# ==================================================
# Line: 1631

x = np.arange(540, dtype=float).reshape(input_shape)

# ==================================================
# Occurrences: Lines 1918-1921 (2 instances)

output_1d = knn.one_hot(indices_1d, 4, sparse=sparse)

# ==================================================
# Occurrences: Lines 1927-1930 (2 instances)

output_1d = knn.one_hot(indices_1d, 4, sparse=sparse)

# ==================================================
# Occurrences: Lines 1950-1953 (2 instances)

output_1d = knn.one_hot(indices_1d, 4, sparse=sparse)

# ==================================================
# Line: 1959

output_1d = knn.one_hot(indices_1d, 4, sparse=sparse)

# ==================================================
# Occurrences: Lines 1976-1977 (2 instances)

target = np.array([[0.1], [0.9], [0.2], [1.0]])

# ==================================================
# Occurrences: Lines 1985-1987 (3 instances)

target = np.array([[0.1], [0.9], [0.2], [1.0]])

# ==================================================
# Occurrences: Lines 1994-1996 (2 instances)

target = np.array([[0.1], [0.9], [0.2], [1.0]])

# ==================================================
# Line: 2031

result = knn.categorical_crossentropy(
    target, output, from_logits=True, axis=-1
)

# ==================================================
# Line: 2043

result = knn.categorical_crossentropy(
    target, output, from_logits=True, axis=-1
)

# ==================================================
# Line: 2075

output_1d = knn.multi_hot(indices_1d, 4, sparse=sparse)

# ==================================================
# Line: 2089

output_1d = knn.multi_hot(indices_1d, 4, sparse=sparse)

# ==================================================
# Occurrences: Lines 2096-2107 (4 instances)

mean, variance = knn.moments(x, axes=[0])

# ==================================================
# Line: 2115

x = np.random.uniform(size=(2, 28, 28, 3)).astype(np.float32)

# ==================================================
# Line: 2127

mean, variance = knn.moments(x, axes=[0])

# ==================================================
# Line: 2141

x = np.random.uniform(size=(2, 28, 28, 3)).astype(np.float32)

# ==================================================
# Line: 2147

x = np.random.uniform(size=(2, 28, 28, 3)).astype(np.float32)

# ==================================================
# Line: 2155

x = np.random.uniform(size=(2, 28, 28, 3)).astype(np.float32)

# ==================================================
# Occurrences: Lines 2254-2255 (2 instances)

label_length = np.array([3, 2])

# ==================================================
# Line: 2375

x1 = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])

# ==================================================
# Occurrences: Lines 2384-2385 (2 instances)

x3 = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])

# ==================================================
# Occurrences: Lines 2411-2412 (2 instances)

key = np.arange(math.prod(key_shape), dtype=float).reshape(key_shape)

# ==================================================
# Occurrences: Lines 3012-3013 (2 instances)

label_length = knp.array([3])

# ==================================================
# Occurrences: Lines 3072-3074 (3 instances)

query = knp.ones((2, 3, 3, 8), dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/numpy_test.py
# Occurrences: Lines 540-550 (3 instances)

result = knp.matmul(x, y)

# ==================================================
# Line: 1288

result = knp.concatenate([x, y], axis=1)

# ==================================================
# Line: 1294

result = knp.concatenate([x, y], axis=1)

# ==================================================
# Line: 1300

result = knp.concatenate([x, y], axis=1)

# ==================================================
# Occurrences: Lines 2528-2530 (2 instances)

x1 = np.ones([2, 1, 4, 3])

# ==================================================
# Line: 2595

y = np.arange(3).reshape([3]).astype("float32")

# ==================================================
# Occurrences: Lines 2601-2602 (2 instances)

x = np.arange(6).reshape([2, 3]).astype("float32")

# ==================================================
# Line: 2608

x = np.arange(6).reshape([2, 3]).astype("float32")

# ==================================================
# Line: 2615

x = np.arange(6).reshape([2, 3]).astype("float32")

# ==================================================
# Line: 2622

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Occurrences: Lines 2629-2630 (2 instances)

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Line: 2636

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Line: 2643

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Line: 2650

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Line: 2657

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Line: 2664

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Line: 2671

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Line: 2678

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Occurrences: Lines 2685-2686 (2 instances)

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Occurrences: Lines 2692-2693 (2 instances)

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Occurrences: Lines 2699-2700 (2 instances)

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Line: 2706

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Line: 2713

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Line: 2720

x = np.arange(720).reshape([2, 3, 4, 5, 6]).astype("float32")

# ==================================================
# Line: 2727

x = np.arange(720).reshape([2, 3, 4, 5, 6]).astype("float32")

# ==================================================
# Line: 3055

x = rng.standard_normal((2, 3, 4, 5))

# ==================================================
# Line: 3074

x = rng.standard_normal((2, 3, 4, 5))

# ==================================================
# Line: 3167

indices = np.ones([1, 4, 1, 1], dtype=np.int32)

# ==================================================
# Occurrences: Lines 3177-3178 (2 instances)

x = np.arange(12).reshape([1, 1, 3, 4])

# ==================================================
# Line: 3189

x = np.arange(12).reshape([1, 1, 3, 4])

# ==================================================
# Line: 3201

x = np.arange(12).reshape([1, 1, 3, 4])

# ==================================================
# Occurrences: Lines 3671-3680 (2 instances)

output = knp.bincount(
    x, weights=weights, minlength=minlength, sparse=sparse_arg
)

# ==================================================
# Occurrences: Lines 3690-3697 (2 instances)

output = knp.bincount(
    x, weights=weights, minlength=minlength, sparse=sparse_arg
)

# ==================================================
# Line: 3925

x = np.array([1, 2, 3])

# ==================================================
# Line: 3946

x = np.array([1, 2, 3])

# ==================================================
# Line: 3980

x = np.array([1, 2, 4, 7, 0])

# ==================================================
# Line: 3992

x = np.array([1, 2, 4, 7, 0])

# ==================================================
# Occurrences: Lines 4120-4121 (2 instances)

x = np.array([[1, 2, 3], [3, 2, 1]])

# ==================================================
# Line: 4320

x = np.ones([2, 3, 4, 5, 6], dtype=dtype)

# ==================================================
# Line: 4337

x = np.ones([2, 3, 4, 5, 6], dtype=dtype)

# ==================================================
# Line: 4487

x = np.array([[1, 2, 3], [3, 2, 1]])

# ==================================================
# Line: 4512

x_np = np.array([[1, 2, 3], [3, 2, 1]])

# ==================================================
# Line: 4826

y = knp.select(condlist, choicelist, 42)

# ==================================================
# Line: 4832

y = knp.select(condlist, choicelist, 42)

# ==================================================
# Occurrences: Lines 4839-4854 (4 instances)

y = knp.select(condlist, choicelist, 42)

# ==================================================
# Line: 4889

out = vfunc(np.eye(4))

# ==================================================
# Line: 4895

out = vfunc(np.eye(4))

# ==================================================
# Line: 5581

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 5595

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Occurrences: Lines 5672-5675 (4 instances)

x = knp.ones((), dtype=dtype)

# ==================================================
# Line: 5790

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 5804

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 5885

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 5899

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 6488

dtype = backend.floatx()

# ==================================================
# Line: 6500

expected_dtype = backend.floatx()

# ==================================================
# Occurrences: Lines 6755-6758 (4 instances)

x = knp.ones((1,), dtype=dtype)

# ==================================================
# Line: 6815

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 6829

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 7178

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 7194

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 7707

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 7721

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 7836

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 7850

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 8050

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 8064

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Occurrences: Lines 8118-8122 (4 instances)

a = knp.ones((3,), dtype=dtype)

# ==================================================
# Line: 8847

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# Line: 8864

expected_dtype = expected_dtype.replace("64", "32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/nn.py
# Line: 2922

inv = backend.math.rsqrt(variance + epsilon)

# ==================================================
# Line: 2935

inv = backend.math.rsqrt(variance + epsilon)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/math_test.py
# Line: 154

outputs = segment_reduce_op(data, segment_ids)

# ==================================================
# Line: 167

outputs = segment_reduce_op(data, segment_ids)

# ==================================================
# Line: 193

outputs = kmath.extract_sequences(x, sequence_length, sequence_stride)

# ==================================================
# Line: 201

outputs = kmath.extract_sequences(x, sequence_length, sequence_stride)

# ==================================================
# Occurrences: Lines 303-308 (2 instances)

outputs = segment_reduce_op(data, segment_ids)

# ==================================================
# Line: 316

outputs = segment_reduce_op(data, segment_ids, num_segments=5)

# ==================================================
# Line: 324

outputs = segment_reduce_op(data, segment_ids, num_segments=5)

# ==================================================
# Occurrences: Lines 429-433 (2 instances)

out = kmath.logdet(x)

# ==================================================
# Occurrences: Lines 602-607 (3 instances)

x = np.array([0, 4, 2, 1, 3, -1], dtype=np.float32)

# ==================================================
# Line: 614

outputs = kmath.top_k(x, k=2)

# ==================================================
# Line: 628

targets = np.array([1, 0, 2])

# ==================================================
# Line: 647

targets = np.array([1, 0, 2])

# ==================================================
# Line: 688

output = kmath.extract_sequences(x, sequence_length, sequence_stride)

# ==================================================
# Line: 702

output = kmath.extract_sequences(x, sequence_length, sequence_stride)

# ==================================================
# Occurrences: Lines 713-714 (2 instances)

real = np.random.random((2, 4, 3))

# ==================================================
# Occurrences: Lines 725-726 (2 instances)

real = np.random.random((2, 4, 3))

# ==================================================
# Occurrences: Lines 737-738 (2 instances)

real = np.random.random((2, 4, 3)).astype(np.float32)

# ==================================================
# Occurrences: Lines 752-755 (4 instances)

real_output, imag_output = kmath.rfft(x, fft_length=n)

# ==================================================
# Occurrences: Lines 761-764 (4 instances)

real_output, imag_output = kmath.rfft(x, fft_length=n)

# ==================================================
# Occurrences: Lines 771-783 (8 instances)

real = np.random.random((10,))

# ==================================================
# Occurrences: Lines 802-807 (2 instances)

real_output, imag_output = kmath.stft(
    x, sequence_length, sequence_stride, fft_length, window, center
)

# ==================================================
# Occurrences: Lines 813-818 (2 instances)

real_output, imag_output = kmath.stft(
    x, sequence_length, sequence_stride, fft_length, window, center
)

# ==================================================
# Occurrences: Lines 840-862 (4 instances)

real_x, imag_x = _stft(
    x, sequence_length, sequence_stride, fft_length, window, center
)

# ==================================================
# Occurrences: Lines 869-891 (4 instances)

real_x, imag_x = _stft(
    x, sequence_length, sequence_stride, fft_length, window, center
)

# ==================================================
# Occurrences: Lines 1153-1154 (2 instances)

real = np.array(1)

# ==================================================
# Occurrences: Lines 1171-1172 (2 instances)

real_part = np.random.rand(2, 3, 4)

# ==================================================
# Occurrences: Lines 1220-1225 (2 instances)

input_tensor = np.random.rand(3, 8)

# ==================================================
# Occurrences: Lines 1231-1236 (2 instances)

input_tensor = np.random.rand(3, 8)

# ==================================================
# Occurrences: Lines 1325-1326 (2 instances)

real_part = np.array(1)

# ==================================================
# Occurrences: Lines 1335-1336 (2 instances)

real_part = np.random.rand(4, 8)

# ==================================================
# Occurrences: Lines 1348-1349 (2 instances)

real_part = np.random.rand(4, 8)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/operation.py
# Occurrences: Lines 39-47 (2 instances)

call_fn = self.rematerialized_call(
    self.quantized_call,
    *args,
    **kwargs,
)

# ==================================================
# Occurrences: Lines 64-68 (2 instances)

return self.rematerialized_call(
    self.quantized_call, *args, **kwargs
)(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/image_test.py
# Line: 30

out = kimage.rgb_to_grayscale(x)

# ==================================================
# Line: 36

out = kimage.rgb_to_grayscale(x)

# ==================================================
# Line: 42

out = kimage.rgb_to_hsv(x)

# ==================================================
# Line: 48

out = kimage.rgb_to_hsv(x)

# ==================================================
# Line: 54

out = kimage.hsv_to_rgb(x)

# ==================================================
# Line: 60

out = kimage.hsv_to_rgb(x)

# ==================================================
# Occurrences: Lines 66-70 (2 instances)

out = kimage.resize(x, size=(15, 15))

# ==================================================
# Occurrences: Lines 76-80 (2 instances)

out = kimage.resize(x, size=(15, 15))

# ==================================================
# Line: 87

out = kimage.affine_transform(x, transform)

# ==================================================
# Line: 94

out = kimage.affine_transform(x, transform)

# ==================================================
# Occurrences: Lines 101-103 (2 instances)

out = kimage.extract_patches(x, (p_h, p_w))

# ==================================================
# Occurrences: Lines 110-112 (2 instances)

out = kimage.extract_patches(x, (p_h, p_w))

# ==================================================
# Occurrences: Lines 124-128 (2 instances)

out = kimage.pad_images(x, 2, 3, target_height=20, target_width=30)

# ==================================================
# Occurrences: Lines 139-143 (2 instances)

out = kimage.pad_images(x, 2, 3, target_height=20, target_width=30)

# ==================================================
# Occurrences: Lines 149-153 (2 instances)

out = kimage.crop_images(x, 2, 3, target_height=10, target_width=20)

# ==================================================
# Occurrences: Lines 159-163 (2 instances)

out = kimage.crop_images(x, 2, 3, target_height=10, target_width=20)

# ==================================================
# Line: 171

out = kimage.perspective_transform(x, start_points, end_points)

# ==================================================
# Line: 179

out = kimage.perspective_transform(x, start_points, end_points)

# ==================================================
# Line: 185

out = kimage.gaussian_blur(x)

# ==================================================
# Line: 191

out = kimage.gaussian_blur(x)

# ==================================================
# Line: 197

out = kimage.elastic_transform(x)

# ==================================================
# Line: 203

out = kimage.elastic_transform(x)

# ==================================================
# Line: 221

out = kimage.rgb_to_grayscale(x)

# ==================================================
# Line: 227

out = kimage.rgb_to_grayscale(x)

# ==================================================
# Line: 233

out = kimage.rgb_to_hsv(x)

# ==================================================
# Line: 239

out = kimage.rgb_to_hsv(x)

# ==================================================
# Line: 245

out = kimage.hsv_to_rgb(x)

# ==================================================
# Line: 251

out = kimage.hsv_to_rgb(x)

# ==================================================
# Line: 257

out = kimage.resize(x, size=(15, 15))

# ==================================================
# Line: 263

out = kimage.resize(x, size=(15, 15))

# ==================================================
# Line: 270

out = kimage.affine_transform(x, transform)

# ==================================================
# Line: 277

out = kimage.affine_transform(x, transform)

# ==================================================
# Occurrences: Lines 284-286 (2 instances)

out = kimage.extract_patches(x, (p_h, p_w))

# ==================================================
# Occurrences: Lines 293-295 (2 instances)

out = kimage.extract_patches(x, (p_h, p_w))

# ==================================================
# Occurrences: Lines 359-365 (2 instances)

out = kimage.pad_images(x, 2, 3, target_height=20, target_width=30)

# ==================================================
# Occurrences: Lines 371-377 (2 instances)

out = kimage.pad_images(x, 2, 3, target_height=20, target_width=30)

# ==================================================
# Occurrences: Lines 383-389 (2 instances)

out = kimage.crop_images(x, 2, 3, target_height=10, target_width=20)

# ==================================================
# Occurrences: Lines 395-402 (2 instances)

out = kimage.crop_images(x, 2, 3, target_height=10, target_width=20)

# ==================================================
# Line: 410

out = kimage.perspective_transform(x, start_points, end_points)

# ==================================================
# Line: 418

out = kimage.perspective_transform(x, start_points, end_points)

# ==================================================
# Line: 434

out = kimage.gaussian_blur(x, kernel_size, sigma)

# ==================================================
# Line: 450

out = kimage.gaussian_blur(x, kernel_size, sigma)

# ==================================================
# Line: 456

out = kimage.elastic_transform(x)

# ==================================================
# Line: 462

out = kimage.elastic_transform(x)

# ==================================================
# Occurrences: Lines 959-966 (4 instances)

out = kimage.rgb_to_grayscale(x)

# ==================================================
# Line: 973

out = kimage.rgb_to_grayscale(x)

# ==================================================
# Line: 980

out = kimage.rgb_to_grayscale(x)

# ==================================================
# Occurrences: Lines 993-1000 (4 instances)

out = kimage.rgb_to_hsv(x)

# ==================================================
# Line: 1007

out = kimage.rgb_to_hsv(x)

# ==================================================
# Line: 1014

out = kimage.rgb_to_hsv(x)

# ==================================================
# Occurrences: Lines 1027-1034 (4 instances)

out = kimage.hsv_to_rgb(x)

# ==================================================
# Line: 1041

out = kimage.hsv_to_rgb(x)

# ==================================================
# Line: 1048

out = kimage.hsv_to_rgb(x)

# ==================================================
# Occurrences: Lines 1088-1115 (4 instances)

out = kimage.resize(
    x,
    size=(15, 15),
    interpolation=interpolation,
    antialias=antialias,
)

# ==================================================
# Line: 1122

out = kimage.resize(
    x,
    size=(15, 15),
    interpolation=interpolation,
    antialias=antialias,
)

# ==================================================
# Line: 1139

out = kimage.resize(
    x,
    size=(15, 15),
    interpolation=interpolation,
    antialias=antialias,
)

# ==================================================
# Occurrences: Lines 1246-1250 (2 instances)

out = kimage.resize(x, size=(25, 25), crop_to_aspect_ratio=True)

# ==================================================
# Occurrences: Lines 1256-1260 (2 instances)

out = kimage.resize(x, size=(25, 25), crop_to_aspect_ratio=True)

# ==================================================
# Occurrences: Lines 1267-1278 (2 instances)

out = kimage.resize(
    x,
    size=(25, 25),
    pad_to_aspect_ratio=True,
    fill_value=fill_value,
)

# ==================================================
# Occurrences: Lines 1284-1305 (4 instances)

out = kimage.resize(
    x, size=(25, 25), pad_to_aspect_ratio=True, fill_value=fill_value
)

# ==================================================
# Occurrences: Lines 1351-1356 (4 instances)

transform = np.random.uniform(size=(6)).astype("float32")

# ==================================================
# Occurrences: Lines 1367-1375 (4 instances)

transform = np.random.uniform(size=(2, 6)).astype("float32")

# ==================================================
# Occurrences: Lines 1394-1398 (3 instances)

transform = np.random.uniform(size=(6)).astype("float32")

# ==================================================
# Occurrences: Lines 1413-1420 (3 instances)

transform = np.random.uniform(size=(2, 6)).astype("float32")

# ==================================================
# Line: 1470

patches_out = kimage.extract_patches(
    image,
    size=size,
    strides=strides,
    dilation_rate=dilation_rate,
    padding=padding,
)

# ==================================================
# Line: 1494

patches_out = kimage.extract_patches(
    image,
    size=size,
    strides=strides,
    dilation_rate=dilation_rate,
    padding=padding,
)

# ==================================================
# Line: 1582

padded_image = kimage.pad_images(
    image,
    top_padding,
    left_padding,
    bottom_padding,
    right_padding,
    target_height,
    target_width,
)

# ==================================================
# Line: 1602

padded_image = kimage.pad_images(
    image,
    top_padding,
    left_padding,
    bottom_padding,
    right_padding,
    target_height,
    target_width,
)

# ==================================================
# Line: 1664

cropped_image = kimage.crop_images(
    image,
    top_cropping,
    left_cropping,
    bottom_cropping,
    right_cropping,
    target_height,
    target_width,
)

# ==================================================
# Line: 1684

cropped_image = kimage.crop_images(
    image,
    top_cropping,
    left_cropping,
    bottom_cropping,
    right_cropping,
    target_height,
    target_width,
)

# ==================================================
# Occurrences: Lines 1726-1731 (3 instances)

start_points = np.random.uniform(size=(1, 4, 2)).astype("float32")

# ==================================================
# Occurrences: Lines 1743-1748 (3 instances)

start_points = np.random.uniform(size=(1, 4, 2)).astype("float32")

# ==================================================
# Occurrences: Lines 1766-1767 (2 instances)

kernel_size = np.array([3, 3])

# ==================================================
# Occurrences: Lines 1789-1790 (2 instances)

kernel_size = np.array([3, 3])

# ==================================================
# Line: 1832

out = backend.convert_to_numpy(out)

# ==================================================
# Line: 1860

out = backend.convert_to_numpy(out)

# ==================================================
# Line: 2015

transform = np.random.uniform(size=(6,))

# ==================================================
# Line: 2027

transform = np.random.uniform(size=(6,))

# ==================================================
# Occurrences: Lines 2129-2130 (2 instances)

start_points = np.random.uniform(size=(6,))

# ==================================================
# Occurrences: Lines 2146-2147 (2 instances)

start_points = np.random.uniform(size=(6,))

# ==================================================
# Line: 2164

end_points = np.random.uniform(size=(6,))

# ==================================================
# Occurrences: Lines 2175-2176 (2 instances)

start_points = np.random.uniform(size=(2, 2, 4, 2))

# ==================================================
# Occurrences: Lines 2187-2188 (2 instances)

start_points = np.random.uniform(size=())

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/operation_utils.py
# Occurrences: Lines 67-69 (2 instances)

axis = len(input_shape)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/linalg_test.py
# Occurrences: Lines 15-37 (6 instances)

out = linalg.cholesky(x)

# ==================================================
# Occurrences: Lines 53-62 (3 instances)

out = linalg.inv(x)

# ==================================================
# Occurrences: Lines 69-74 (2 instances)

lu, p = linalg.lu_factor(x)

# ==================================================
# Occurrences: Lines 116-121 (2 instances)

out = linalg.solve(a, b)

# ==================================================
# Occurrences: Lines 127-137 (3 instances)

linalg.solve(a, b)

# ==================================================
# Occurrences: Lines 145-160 (4 instances)

out = linalg.solve_triangular(a, b)

# ==================================================
# Occurrences: Lines 166-171 (2 instances)

linalg.solve_triangular(a, b)

# ==================================================
# Occurrences: Lines 192-210 (5 instances)

out = linalg.cholesky(x)

# ==================================================
# Occurrences: Lines 216-220 (2 instances)

linalg.eig(x)

# ==================================================
# Occurrences: Lines 226-235 (3 instances)

linalg.eigh(x)

# ==================================================
# Occurrences: Lines 242-247 (2 instances)

lu, p = linalg.lu_factor(x)

# ==================================================
# Occurrences: Lines 279-284 (2 instances)

out = linalg.solve(a, b)

# ==================================================
# Occurrences: Lines 290-295 (2 instances)

linalg.solve(a, b)

# ==================================================
# Occurrences: Lines 303-308 (2 instances)

out = linalg.solve_triangular(a, b)

# ==================================================
# Line: 314

linalg.solve_triangular(a, b)

# ==================================================
# Occurrences: Lines 343-348 (2 instances)

out = linalg.det(x)

# ==================================================
# Occurrences: Lines 401-413 (6 instances)

x = np.random.rand(m, n)

# ==================================================
# Line: 423

lu, pivots = map(ops.convert_to_numpy, linalg.lu_factor(x))

# ==================================================
# Occurrences: Lines 470-472 (2 instances)

linalg.norm(x, ord=ord, axis=axis, keepdims=keepdims)

# ==================================================
# Line: 504

output = linalg.solve_triangular(x1, x2, lower=True)

# ==================================================
# Line: 515

output = linalg.solve_triangular(x1, x2, lower=True)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/numpy.py
# Occurrences: Lines 336-338 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 666-668 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 702-704 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 735-737 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 770-772 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 804-806 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 901-903 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 1986-1988 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 2014-2016 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 2775-2775 (2 instances)

if len(x_shape) != len(split_spec[0]):

# ==================================================
# Occurrences: Lines 2789-2789 (2 instances)

for i in range(len(split_spec[0])):

# ==================================================
# Occurrences: Lines 2799-2799 (2 instances)

wildcard_shape_start_index = len(split_spec[0])

# ==================================================
# Line: 5085

output_shape = [int(np.sum(repeats))]

# ==================================================
# Line: 5102

output_shape[self.axis] = int(np.sum(repeats))

# ==================================================
# Occurrences: Lines 5320-5322 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 5349-5351 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 5708-5710 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# Occurrences: Lines 5737-5739 (2 instances)

dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/function.py
# Occurrences: Lines 280-285 (2 instances)

nodes_by_depth = collections.defaultdict(list)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/core.py
# Occurrences: Lines 93-97 (2 instances)

n = int(length)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/cloning.py
# Line: 143

clone_function = _wrap_clone_function(
    clone_function,
    call_function=call_function,
    recursive=recursive,
    cache=cache,
)

# ==================================================
# Line: 166

clone_function = _wrap_clone_function(
    clone_function,
    call_function=call_function,
    recursive=recursive,
    cache=cache,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/functional_test.py
# Line: 41

out_val = model(in_val)

# ==================================================
# Line: 48

out_val = model(in_val)

# ==================================================
# Occurrences: Lines 66-71 (3 instances)

x = layers.Dense(5)(inputs)

# ==================================================
# Line: 118

out_val = model(in_val)

# ==================================================
# Line: 125

out_val = model(in_val)

# ==================================================
# Occurrences: Lines 146-152 (3 instances)

x = layers.Dense(5)(input_a)

# ==================================================
# Line: 158

out_val = model(in_val)

# ==================================================
# Occurrences: Lines 165-173 (3 instances)

a = layers.Dense(5)(input_a)

# ==================================================
# Line: 180

out_val = model(in_val)

# ==================================================
# Line: 189

out_val = model(in_val)

# ==================================================
# Line: 196

out_val = model(in_val)

# ==================================================
# Line: 205

out_val = model(in_val)

# ==================================================
# Line: 212

out_val = model(in_val)

# ==================================================
# Line: 221

out_val = model(in_val)

# ==================================================
# Line: 237

out_val = model(in_val)

# ==================================================
# Line: 244

out_val = model(in_val)

# ==================================================
# Line: 350

out_val = model(in_val)

# ==================================================
# Line: 357

out_val = model(in_val)

# ==================================================
# Line: 364

outputs = layers.Dense(3)(inputs)

# ==================================================
# Line: 371

outputs = layers.Dense(3)(inputs)

# ==================================================
# Occurrences: Lines 679-684 (2 instances)

title_data = np.random.randint(
    0, 2, size=(num_samples, vocabulary_size)
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/cloning_test.py
# Occurrences: Lines 18-19 (2 instances)

x = layer(x)

# ==================================================
# Occurrences: Lines 48-49 (2 instances)

x = layer(x)

# ==================================================
# Occurrences: Lines 77-78 (4 instances)

self.d1 = layers.Dense(2)

# ==================================================
# Occurrences: Lines 159-160 (2 instances)

x = layers.Input((3,))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/functional.py
# Line: 414

node_key = make_node_key(operation, original_node_index)

# ==================================================
# Line: 427

node_key = make_node_key(operation, original_node_index)

# ==================================================
# Occurrences: Lines 549-552 (2 instances)

functional_config[key] = config.pop(key)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/variable_mapping_test.py
# Line: 11

variable_map = model._get_variable_map()

# ==================================================
# Line: 20

variable_map = model._get_variable_map()

# ==================================================
# Line: 27

variable_map = model._get_variable_map()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/model_test.py
# Occurrences: Lines 145-146 (4 instances)

self.dense1 = layers.Dense(4, activation="relu", name="layer1")

# ==================================================
# Occurrences: Lines 783-784 (2 instances)

x1 = np.random.rand(2, 3)

# ==================================================
# Line: 845

self.dense = layers.Dense(units)

# ==================================================
# Line: 856

self.dense = layers.Dense(units)

# ==================================================
# Occurrences: Lines 1021-1022 (2 instances)

y1 = np.random.rand(8, 1)

# ==================================================
# Line: 1050

model.fit(x, y, batch_size=2, epochs=1, verbose=0)

# ==================================================
# Line: 1056

hist = model.fit(
    x,
    y,
    batch_size=2,
    epochs=1,
    verbose=0,
)

# ==================================================
# Occurrences: Lines 1079-1080 (2 instances)

y1 = np.random.rand(8, 1)

# ==================================================
# Occurrences: Lines 1127-1128 (2 instances)

y1 = np.random.rand(8, 1)

# ==================================================
# Occurrences: Lines 1168-1170 (3 instances)

y1 = np.random.rand(8, 1)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/sequential_test.py
# Occurrences: Lines 30-31 (2 instances)

x = np.random.random((3, 2))

# ==================================================
# Line: 38

y = model(x)

# ==================================================
# Occurrences: Lines 53-54 (2 instances)

x = np.random.random((3, 2))

# ==================================================
# Occurrences: Lines 63-64 (2 instances)

x = np.random.random((3, 2))

# ==================================================
# Occurrences: Lines 106-107 (2 instances)

x = np.random.random((3, 2))

# ==================================================
# Line: 116

y = model(x)

# ==================================================
# Occurrences: Lines 126-127 (2 instances)

x = np.random.random((3, 2))

# ==================================================
# Occurrences: Lines 136-137 (2 instances)

x = np.random.random((3, 2))

# ==================================================
# Line: 171

y = model(x)

# ==================================================
# Line: 177

y = model(x)

# ==================================================
# Line: 197

y = model(x)

# ==================================================
# Line: 203

y = model(x)

# ==================================================
# Occurrences: Lines 285-290 (2 instances)

revived = self.run_class_serialization_test(model)

# ==================================================
# Line: 299

revived = self.run_class_serialization_test(model)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/random/seed_generator_test.py
# Occurrences: Lines 26-37 (6 instances)

seed1 = ops.convert_to_numpy(gen.next())

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/random/random_test.py
# Occurrences: Lines 127-128 (4 instances)

x = random.normal((), seed=None)

# ==================================================
# Occurrences: Lines 137-149 (7 instances)

seed0 = ops.convert_to_numpy(seed)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/backend_utils_test.py
# Occurrences: Lines 27-29 (2 instances)

y = dynamic_backend.numpy.log10(x)

# ==================================================
# Line: 35

y = dynamic_backend.numpy.log10(x)

# ==================================================
# Line: 41

y = dynamic_backend.numpy.log10(x)

# ==================================================
# Line: 47

y = dynamic_backend.numpy.log10(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/audio_dataset_utils_test.py
# Line: 99

batch = next(iter(dataset))

# ==================================================
# Line: 112

batch = next(iter(dataset))

# ==================================================
# Line: 125

batch = next(iter(dataset))

# ==================================================
# Occurrences: Lines 159-169 (5 instances)

dataset = audio_dataset_utils.audio_dataset_from_directory(
    directory, batch_size=8, output_sequence_length=30, label_mode=None
)

# ==================================================
# Occurrences: Lines 177-177 (2 instances)

batch = next(iter(dataset))

# ==================================================
# Occurrences: Lines 190-190 (2 instances)

batch = next(iter(dataset))

# ==================================================
# Line: 207

batch = next(iter(dataset))

# ==================================================
# Line: 218

batch = next(iter(dataset))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/jax_layer_test.py
# Occurrences: Lines 39-40 (4 instances)

rng, w_rng = jax.random.split(rng)

# ==================================================
# Occurrences: Lines 80-87 (5 instances)

x = flax.linen.relu(x)

# ==================================================
# Occurrences: Lines 105-113 (5 instances)

x = flax.linen.relu(x)

# ==================================================
# Occurrences: Lines 138-161 (7 instances)

x = flax.linen.BatchNorm(use_running_average=ura, use_scale=False)(
    x
)

# ==================================================
# Line: 224

layer1 = layer_class(**layer_init_kwargs)

# ==================================================
# Occurrences: Lines 240-252 (4 instances)

tw1_before_fit = tree.map_structure(
    backend.convert_to_numpy, layer1.trainable_weights
)

# ==================================================
# Occurrences: Lines 267-272 (2 instances)

tw1_after_call = tree.map_structure(
    backend.convert_to_numpy, layer1.trainable_weights
)

# ==================================================
# Line: 345

layer5 = layer_class(**layer_init_kwargs)

# ==================================================
# Occurrences: Lines 478-481 (4 instances)

flax_model = flax_model_class()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/file_utils_test.py
# Occurrences: Lines 320-321 (2 instances)

dest_dir = self.get_temp_dir()

# ==================================================
# Occurrences: Lines 329-330 (2 instances)

dest_dir = self.get_temp_dir()

# ==================================================
# Occurrences: Lines 338-339 (2 instances)

dest_dir = self.get_temp_dir()

# ==================================================
# Occurrences: Lines 383-387 (3 instances)

cache_dir = self.get_temp_dir()

# ==================================================
# Line: 399

new_hash = file_utils.hash_file(src_path)

# ==================================================
# Occurrences: Lines 411-427 (6 instances)

cache_dir = self.get_temp_dir()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/jax_layer.py
# Line: 433

predictions, new_state = self.call_fn(*call_args)

# ==================================================
# Line: 439

return self.call_fn(*call_args)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/traceback_utils.py
# Occurrences: Lines 98-103 (2 instances)

last_tb = types.TracebackType(last_tb, f, f.f_lasti, line_no)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/dataset_utils.py
# Occurrences: Lines 617-620 (2 instances)

rng = np.random.RandomState(seed)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/summary_utils.py
# Line: 174

nodes_by_depth = model._nodes_by_depth.values()

# ==================================================
# Line: 213

for v in model._nodes_by_depth.values():

# ==================================================
# Occurrences: Lines 277-279 (4 instances)

params = highlight_number(0)

# ==================================================
# Occurrences: Lines 441-443 (4 instances)

if min(lower_index) > max(upper_index):

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/timeseries_dataset_utils_test.py
# Line: 74

dataset = timeseries_dataset_utils.timeseries_dataset_from_array(
    data,
    targets,
    sequence_length=5,
    batch_size=1,
    shuffle=True,
    seed=123,
)

# ==================================================
# Line: 92

dataset = timeseries_dataset_utils.timeseries_dataset_from_array(
    data,
    targets,
    sequence_length=5,
    batch_size=1,
    shuffle=True,
    seed=123,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/image_utils.py
# Line: 90

x_max = np.max(x)

# ==================================================
# Line: 102

if np.max(x) > 255:

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/image_dataset_utils_test.py
# Line: 109

batch = next(iter(dataset))

# ==================================================
# Line: 119

batch = next(iter(dataset))

# ==================================================
# Line: 132

batch = next(iter(dataset))

# ==================================================
# Occurrences: Lines 170-184 (5 instances)

dataset = image_dataset_utils.image_dataset_from_directory(
    directory, batch_size=8, image_size=(18, 18), label_mode=None
)

# ==================================================
# Occurrences: Lines 192-192 (2 instances)

batch = next(iter(dataset))

# ==================================================
# Occurrences: Lines 205-205 (2 instances)

batch = next(iter(dataset))

# ==================================================
# Line: 221

batch = next(iter(dataset))

# ==================================================
# Line: 236

batch = next(iter(dataset))

# ==================================================
# Line: 251

batch = next(iter(dataset))

# ==================================================
# Line: 268

batch = next(iter(dataset))

# ==================================================
# Line: 292

directory = self._prepare_directory(num_classes=1, count=4)

# ==================================================
# Line: 303

directory = self._prepare_directory(num_classes=1, count=4)

# ==================================================
# Line: 316

batch = next(iter(dataset))

# ==================================================
# Line: 331

batch = next(iter(dataset))

# ==================================================
# Occurrences: Lines 494-528 (6 instances)

batches_1 = np.concatenate(batches_1, axis=0)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/backend_utils.py
# Occurrences: Lines 136-137 (4 instances)

if str(value).startswith("<module 'keras."):

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/tracking_test.py
# Line: 21

lst = tracking.TrackedList([], tracker)

# ==================================================
# Line: 39

lst2 = tracking.TrackedList([], tracker)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/tracking.py
# Occurrences: Lines 87-92 (2 instances)

wrapped_attr[name] = self.track(e)

# ==================================================
# Occurrences: Lines 217-222 (2 instances)

value = super().pop(key, default)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/numerical_utils.py
# Line: 170

return backend_module.nn.one_hot(
    inputs, depth, dtype=dtype, sparse=sparse
)

# ==================================================
# Line: 183

one_hot_encoding = backend_module.nn.one_hot(
    inputs, depth, dtype=dtype, sparse=sparse
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/timeseries_dataset_utils.py
# Occurrences: Lines 142-146 (2 instances)

if start_index >= len(data):

# ==================================================
# Occurrences: Lines 155-159 (2 instances)

if end_index >= len(data):

# ==================================================
# Occurrences: Lines 173-177 (2 instances)

if sampling_rate >= len(data):

# ==================================================
# Occurrences: Lines 184-188 (2 instances)

if sequence_stride >= len(data):

# ==================================================
# Line: 194

end_index = len(data)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/text_dataset_utils_test.py
# Line: 78

batch = next(iter(dataset))

# ==================================================
# Line: 89

batch = next(iter(dataset))

# ==================================================
# Line: 99

batch = next(iter(dataset))

# ==================================================
# Occurrences: Lines 119-129 (5 instances)

dataset = text_dataset_utils.text_dataset_from_directory(
    directory, batch_size=8, label_mode=None
)

# ==================================================
# Occurrences: Lines 137-137 (2 instances)

batch = next(iter(dataset))

# ==================================================
# Occurrences: Lines 147-147 (2 instances)

batch = next(iter(dataset))

# ==================================================
# Line: 163

batch = next(iter(dataset))

# ==================================================
# Line: 173

batch = next(iter(dataset))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/file_utils.py
# Occurrences: Lines 250-260 (6 instances)

download_target = os.path.join(datadir, fname)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/image_dataset_utils.py
# Line: 436

img = tf.transpose(img, (2, 0, 1))

# ==================================================
# Occurrences: Lines 449-453 (2 instances)

img = tf.transpose(img, (2, 0, 1))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/rng_utils_test.py
# Occurrences: Lines 30-32 (2 instances)

y1 = get_model_output()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/torch_utils_test.py
# Occurrences: Lines 97-106 (3 instances)

ref_weights = model.get_weights()

# ==================================================
# Line: 113

running_mean = backend.convert_to_numpy(
    model.torch_wrappers[0].module[-1].running_mean
    if cls is Classifier
    else model.bn1.module.running_mean
)

# ==================================================
# Line: 123

running_mean = backend.convert_to_numpy(
    model.torch_wrappers[0].module[-1].running_mean
    if cls is Classifier
    else model.bn1.module.running_mean
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/numerical_utils_test.py
# Occurrences: Lines 85-86 (2 instances)

positive_mask = backend.convert_to_numpy(positive_mask)

# ==================================================
# Occurrences: Lines 113-117 (3 instances)

positive_mask, negative_mask = numerical_utils.build_pos_neg_masks(
    query_labels, key_labels, remove_diagonal=True
)

# ==================================================
# Occurrences: Lines 141-145 (3 instances)

positive_mask, negative_mask = numerical_utils.build_pos_neg_masks(
    query_labels, key_labels, remove_diagonal=True
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/tf_utils.py
# Occurrences: Lines 115-119 (2 instances)

inputs = expand_dims(inputs, -1)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/python_utils.py
# Occurrences: Lines 47-51 (4 instances)

raw_code = marshal.dumps(func.__code__).replace(b"\\", b"/")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/progbar.py
# Line: 165

avg = backend.convert_to_numpy(
    backend.numpy.mean(
        self._values[k][0] / max(1, self._values[k][1])
    )
)

# ==================================================
# Line: 197

avg = backend.convert_to_numpy(
    backend.numpy.mean(
        self._values[k][0] / max(1, self._values[k][1])
    )
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/dtype_utils.py
# Occurrences: Lines 43-45 (4 instances)

if highest_float is None or dtype_size(dtype) > highest_float_size:

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/naming_test.py
# Occurrences: Lines 23-24 (2 instances)

naming.uniquify(name)

# ==================================================
# Occurrences: Lines 34-41 (4 instances)

naming.get_uid(prefix)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/iou_metrics.py
# Occurrences: Lines 255-257 (2 instances)

if max(target_class_ids) >= num_classes:

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/confusion_metrics_test.py
# Occurrences: Lines 431-432 (2 instances)

y_pred = np.array([0, 0, 0, 0])

# ==================================================
# Occurrences: Lines 595-596 (2 instances)

y_pred = np.array([0, 0, 0, 0])

# ==================================================
# Occurrences: Lines 1184-1189 (2 instances)

old_config = auc_obj.get_config()

# ==================================================
# Occurrences: Lines 1223-1227 (2 instances)

old_config = auc_obj.get_config()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/accuracy_metrics_test.py
# Occurrences: Lines 93-109 (6 instances)

bin_acc_obj = accuracy_metrics.BinaryAccuracy(
    name="binary_accuracy", dtype="float32"
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/metric_test.py
# Occurrences: Lines 63-64 (2 instances)

y_true = np.random.random((num_samples, 3))

# ==================================================
# Occurrences: Lines 72-77 (2 instances)

result = metric.result()

# ==================================================
# Occurrences: Lines 88-89 (2 instances)

y_true = np.random.random((num_samples, 3))

# ==================================================
# Line: 95

metric_variables = metric.stateless_update_state(
    metric_variables, y_true_batch, y_pred_batch
)

# ==================================================
# Line: 115

metric_variables = metric.stateless_update_state(
    metric_variables, y_true_batch, y_pred_batch
)

# ==================================================
# Occurrences: Lines 129-130 (2 instances)

y_true = np.random.random((num_samples, 3))

# ==================================================
# Occurrences: Lines 217-220 (3 instances)

y_true = np.random.random((num_samples, 3))

# ==================================================
# Line: 232

result = metric.result()

# ==================================================
# Occurrences: Lines 243-244 (2 instances)

y_true = np.random.random((10, 3))

# ==================================================
# Line: 250

result = metric.result()

# ==================================================
# Line: 256

result = metric.result()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/accuracy_metrics.py
# Occurrences: Lines 137-138 (2 instances)

y_pred_rank = len(y_pred.shape)

# ==================================================
# Occurrences: Lines 144-144 (2 instances)

and (len(y_true.shape) == len(y_pred.shape))

# ==================================================
# Occurrences: Lines 221-223 (3 instances)

y_true_org_shape = ops.shape(y_true)

# ==================================================
# Occurrences: Lines 229-230 (3 instances)

and (len(y_true.shape) == len(y_pred.shape))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/metrics_utils.py
# Line: 496

pred_shape = ops.shape(y_pred)

# ==================================================
# Line: 506

pred_shape = ops.shape(y_pred)

# ==================================================
# Line: 548

ops.cast(sample_weight, dtype=y_pred.dtype), ops.shape(y_pred)

# ==================================================
# Line: 558

label_weights = ops.broadcast_to(label_weights, ops.shape(y_pred))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/reduction_metrics.py
# Line: 27

values_ndim = len(values.shape)

# ==================================================
# Line: 41

values_ndim = len(values.shape)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/iou_metrics_test.py
# Line: 143

result = obj(y_true, y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 159

result = obj(y_true, y_pred, sample_weight=sample_weight)

# ==================================================
# Line: 173

result = obj(y_true, y_pred)

# ==================================================
# Line: 183

result = obj(y_true, y_pred)

# ==================================================
# Line: 429

conf_matrix_from_keras = np.array(mean_iou_metric_all.total_cm)

# ==================================================
# Line: 449

conf_matrix_from_keras = np.array(mean_iou_metric_all.total_cm)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/__init__.py
# Occurrences: Lines 63-64 (2 instances)

if config["class_name"].lower() in ALL_OBJECTS_DICT:

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/adafactor.py
# Line: 152

lr = ops.minimum(lr, 1 / ops.sqrt(local_step))

# ==================================================
# Line: 158

rho_t = ops.minimum(lr, 1 / ops.sqrt(local_step))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/optimizer_test.py
# Occurrences: Lines 29-31 (2 instances)

v = backend.Variable([[3.0, 4.0], [5.0, 6.0]])

# ==================================================
# Occurrences: Lines 38-40 (2 instances)

v2 = backend.Variable([[3.0, 4.0], [5.0, 6.0]])

# ==================================================
# Occurrences: Lines 177-180 (2 instances)

optimizer_1 = optimizers.Adam()

# ==================================================
# Line: 244

ref_pred = model.predict(x)

# ==================================================
# Occurrences: Lines 253-258 (2 instances)

pred = model.predict(x)

# ==================================================
# Occurrences: Lines 271-275 (4 instances)

v = backend.Variable([[1.0, 2.0], [3.0, 4.0]])

# ==================================================
# Occurrences: Lines 285-287 (2 instances)

v = backend.Variable([[1.0, 2.0], [3.0, 4.0]])

# ==================================================
# Occurrences: Lines 361-362 (2 instances)

variable1 = backend.Variable([[0.9], [0.5]])

# ==================================================
# Occurrences: Lines 413-415 (2 instances)

grads = backend.convert_to_tensor([[1.0, 1.0], [1.0, 1.0]])

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/muon.py
# Line: 257

x = self.transpose_last_axis(x)

# ==================================================
# Occurrences: Lines 263-268 (2 instances)

temp_a = x @ self.transpose_last_axis(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/base_optimizer.py
# Line: 572

grads = self._clip_gradients(grads)

# ==================================================
# Line: 589

grads = self._clip_gradients(grads)

# ==================================================
# Line: 672

new_v = scope.get_current_value(v)

# ==================================================
# Line: 679

new_v = scope.get_current_value(v)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/schedules/learning_rate_schedule_test.py
# Occurrences: Lines 35-36 (2 instances)

x = np.arange(32).reshape((16, 2))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/muon_test.py
# Line: 35

vars = backend.Variable([[1.0, 2.0], [3.0, 4.0]])

# ==================================================
# Line: 47

vars = backend.Variable([[1.0, 2.0], [3.0, 4.0]])

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/optimizer_sparse_test.py
# Occurrences: Lines 256-259 (4 instances)

optimizer_sparse = optimizer_class(**init_kwargs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/saving/legacy_h5_format_test.py
# Occurrences: Lines 89-93 (2 instances)

output = model(ref_input)

# ==================================================
# Occurrences: Lines 147-148 (2 instances)

mean = ops.random.uniform((4, 2, 3))

# ==================================================
# Occurrences: Lines 341-342 (2 instances)

mean = np.random.random((4, 2, 3))

# ==================================================
# Line: 411

outputs = MyDense(1)(inputs)

# ==================================================
# Line: 421

outputs = MyDense(1)(inputs)

# ==================================================
# Occurrences: Lines 436-440 (2 instances)

prev_input = layer(prev_input)

# ==================================================
# Occurrences: Lines 482-486 (2 instances)

prev_input = layer(prev_input)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/saving/serialization.py
# Line: 292

name = object_registration.get_registered_name(instance.__class__)

# ==================================================
# Line: 319

name = object_registration.get_registered_name(instance.__class__)

# ==================================================
# Occurrences: Lines 389-389 (2 instances)

object_registration.get_registered_object(item, custom_objects)

# ==================================================
# Occurrences: Lines 401-401 (2 instances)

object_registration.get_registered_object(item, custom_objects)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/saving/legacy_h5_format.py
# Occurrences: Lines 304-309 (2 instances)

chunked_data = np.array_split(data_npy, num_chunks)

# ==================================================
# Line: 344

weights = _legacy_weights(layer)

# ==================================================
# Line: 366

symbolic_weights = _legacy_weights(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/saving/json_utils_test.py
# Line: 61

loaded = json_utils.decode(string)

# ==================================================
# Line: 73

loaded = json_utils.decode(string)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/preprocessing/image.py
# Line: 182

_iter_valid_files(directory, white_list_formats, follow_links)

# ==================================================
# Line: 188

valid_files = _iter_valid_files(
    directory, white_list_formats, follow_links
)

# ==================================================
# Occurrences: Lines 456-457 (2 instances)

self.num_classes = len(classes)

# ==================================================
# Occurrences: Lines 487-488 (2 instances)

self.classes[i : i + len(classes)] = classes

# ==================================================
# Line: 566

f"y.shape = {np.asarray(y).shape}"

# ==================================================
# Line: 573

f"sample_weight.shape = {np.asarray(sample_weight).shape}"

# ==================================================
# Occurrences: Lines 633-637 (2 instances)

self.y = np.asarray(y)

# ==================================================
# Occurrences: Lines 758-760 (2 instances)

num_classes = len(classes)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/preprocessing/text.py
# Line: 108

self.word_docs = collections.defaultdict(int)

# ==================================================
# Line: 116

self.index_docs = collections.defaultdict(int)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/backend.py
# Line: 1320

x_shape = x.shape.as_list()

# ==================================================
# Line: 1350

x_shape = x.shape.as_list()

# ==================================================
# Occurrences: Lines 1529-1533 (2 instances)

inp = _get_input_tensor(i)

# ==================================================
# Occurrences: Lines 1543-1544 (2 instances)

flat_states = tf.nest.flatten(states)

# ==================================================
# Line: 1564

outputs = tf.stack(successive_outputs)

# ==================================================
# Occurrences: Lines 1580-1583 (2 instances)

inp = _get_input_tensor(i)

# ==================================================
# Line: 1592

outputs = tf.stack(successive_outputs)

# ==================================================
# Occurrences: Lines 1718-1724 (3 instances)

current_input = tf.nest.pack_sequence_as(inputs, current_input)

# ==================================================
# Occurrences: Lines 1735-1736 (2 instances)

flat_state = tf.nest.flatten(states)

# ==================================================
# Occurrences: Lines 1778-1788 (5 instances)

current_input = tf.nest.pack_sequence_as(inputs, current_input)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/tree/tree_test.py
# Occurrences: Lines 1642-1697 (17 instances)

self.assertEqualStrict(v.visited(), [1])

# ==================================================
# Line: 1704

v.visited(), [OrderedDict([("b", 2), ("a", 1)]), 2, 1]

# ==================================================
# Line: 1711

self.assertEqualStrict(v.visited(), [defaultdict(default_value)])

# ==================================================
# Line: 1718

v.visited(), [defaultdict(default_value, [("a", 1)]), 1]

# ==================================================
# Line: 1726

v.visited(),

# ==================================================
# Occurrences: Lines 1732-1753 (6 instances)

self.assertEqualStrict(v.visited(), [TrackedList([])])

# ==================================================
# Line: 1761

self.assertEqualStrict(v.visited(), [TrackedDict()])

# ==================================================
# Line: 1767

self.assertEqualStrict(v.visited(), [TrackedDict({"a": 1}), 1])

# ==================================================
# Line: 1774

v.visited(), [TrackedDict({"a": 1, "b": 2}), 1, 2]

# ==================================================
# Line: 1798

v.visited(),

# ==================================================
# Line: 1838

v.visited(),

# ==================================================
# Line: 1855

v.visited(),

# ==================================================
# Line: 1872

v.visited(),

# ==================================================
# Occurrences: Lines 1928-1983 (17 instances)

self.assertEqualStrict(v.visited(), [1])

# ==================================================
# Line: 1990

v.visited(), [2, 1, OrderedDict([("b", 12), ("a", 11)])]

# ==================================================
# Line: 1997

self.assertEqualStrict(v.visited(), [defaultdict(default_value)])

# ==================================================
# Line: 2004

v.visited(), [1, defaultdict(default_value, [("a", 11)])]

# ==================================================
# Line: 2012

v.visited(),

# ==================================================
# Occurrences: Lines 2018-2039 (6 instances)

self.assertEqualStrict(v.visited(), [TrackedList([])])

# ==================================================
# Line: 2047

self.assertEqualStrict(v.visited(), [TrackedDict()])

# ==================================================
# Line: 2053

self.assertEqualStrict(v.visited(), [1, TrackedDict({"a": 11})])

# ==================================================
# Line: 2060

v.visited(), [1, 2, TrackedDict({"a": 11, "b": 12})]

# ==================================================
# Line: 2084

v.visited(),

# ==================================================
# Line: 2124

v.visited(),

# ==================================================
# Line: 2147

v.visited(),

# ==================================================
# Line: 2170

v.visited(),

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/tree/dmtree_impl.py
# Occurrences: Lines 109-112 (2 instances)

registration = REGISTERED_CLASSES.get(type(s), None)

# ==================================================
# Occurrences: Lines 120-122 (2 instances)

registration = REGISTERED_CLASSES.get(type(s), None)

# ==================================================
# Occurrences: Lines 129-132 (4 instances)

ret = dmtree._sequence_like(s, ret)

# ==================================================
# Line: 350

_, value = next(flat_sequence_it)

# ==================================================
# Line: 361

index, _ = next(flat_sequence_it)

# ==================================================
# Occurrences: Lines 387-391 (4 instances)

ret = func(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/tree/optree_impl.py
# Occurrences: Lines 67-69 (2 instances)

return traverse_children()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/dtype_policies/dtype_policy.py
# Line: 161

x = backend.cast(x, dtype=dtype)

# ==================================================
# Line: 173

x = backend.cast(x, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/dtype_policies/dtype_policy_map_test.py
# Occurrences: Lines 128-150 (6 instances)

dtype_policy_map["layer/dense_0"] = dtype_policies.DTypePolicy(
    "bfloat16"
)

# ==================================================
# Occurrences: Lines 165-166 (2 instances)

dtype_policy_map["dense"] = dtype_policies.DTypePolicy("float32")

# ==================================================
# Line: 174

dtype_policy_map["layer/dense_0"] = dtype_policies.DTypePolicy(
    "bfloat16"
)

# ==================================================
# Line: 183

dtype_policies.DTypePolicy("bfloat16"),

# ==================================================
# Occurrences: Lines 210-215 (2 instances)

dtype_policy_map["layer/dense_0"] = dtype_policies.DTypePolicy(
    "bfloat16"
)

# ==================================================
# Occurrences: Lines 230-231 (2 instances)

dtype_policies.DTypePolicy("bfloat16"),

# ==================================================
# Occurrences: Lines 251-265 (6 instances)

dtype_policy_map["layer/dense_0"] = dtype_policies.DTypePolicy(
    "mixed_bfloat16"
)

# ==================================================
# Occurrences: Lines 276-283 (4 instances)

dtype_policy_map["layer/dense_0"] = dtype_policies.DTypePolicy(
    "mixed_bfloat16"
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/dtype_policies/dtype_policy_test.py
# Line: 148

config = policy.get_config()

# ==================================================
# Line: 155

config = policy.get_config()

# ==================================================
# Occurrences: Lines 163-174 (6 instances)

config = serialize(policy)

# ==================================================
# Occurrences: Lines 186-196 (4 instances)

copied_policy = copy.deepcopy(policy)

# ==================================================
# Occurrences: Lines 203-213 (4 instances)

copied_policy = copy.deepcopy(policy)

# ==================================================
# Line: 393

config = policy.get_config()

# ==================================================
# Line: 404

config = policy.get_config()

# ==================================================
# Occurrences: Lines 419-422 (3 instances)

config = serialize(policy)

# ==================================================
# Occurrences: Lines 429-432 (3 instances)

config = serialize(policy)

# ==================================================
# Occurrences: Lines 683-687 (2 instances)

policy = dtype_policy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/applications_test.py
# Line: 168

model = app(weights=None, include_top=False, input_shape=input_shape)

# ==================================================
# Line: 177

model = app(weights=None, include_top=False, input_shape=input_shape)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/resnet.py
# Line: 172

x = layers.GlobalAveragePooling2D(name="avg_pool")(x)

# ==================================================
# Line: 182

x = layers.GlobalAveragePooling2D(name="avg_pool")(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/mobilenet_v3.py
# Occurrences: Lines 188-192 (2 instances)

is_input_t_tensor = backend.is_keras_tensor(input_tensor)

# ==================================================
# Line: 231

backend.is_keras_tensor(input_tensor)

# ==================================================
# Line: 241

if backend.is_keras_tensor(input_tensor):

# ==================================================
# Line: 293

if not backend.is_keras_tensor(input_tensor):

# ==================================================
# Line: 323

x = activation(x)

# ==================================================
# Line: 343

x = activation(x)

# ==================================================
# Line: 353

x = activation(x)

# ==================================================
# Line: 373

inputs = operation_utils.get_source_inputs(input_tensor)

# ==================================================
# Line: 614

x = activation(x)

# ==================================================
# Line: 634

x = activation(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/imagenet_utils.py
# Line: 254

ndim = len(x.shape)

# ==================================================
# Line: 267

if len(x.shape) == 3:

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/densenet.py
# Line: 246

x = layers.GlobalAveragePooling2D(name="avg_pool")(x)

# ==================================================
# Line: 254

x = layers.GlobalAveragePooling2D(name="avg_pool")(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/inception_v3.py
# Occurrences: Lines 142-160 (9 instances)

x = layers.MaxPooling2D((3, 3), strides=(2, 2))(x)

# ==================================================
# Occurrences: Lines 169-181 (8 instances)

branch1x1 = conv2d_bn(x, 64, 1, 1)

# ==================================================
# Occurrences: Lines 189-201 (8 instances)

branch1x1 = conv2d_bn(x, 64, 1, 1)

# ==================================================
# Occurrences: Lines 211-217 (3 instances)

branch3x3dbl = conv2d_bn(x, 64, 1, 1)

# ==================================================
# Occurrences: Lines 223-238 (9 instances)

branch1x1 = conv2d_bn(x, 192, 1, 1)

# ==================================================
# Occurrences: Lines 247-262 (13 instances)

branch1x1 = conv2d_bn(x, 192, 1, 1)

# ==================================================
# Occurrences: Lines 270-285 (10 instances)

branch1x1 = conv2d_bn(x, 192, 1, 1)

# ==================================================
# Occurrences: Lines 293-296 (2 instances)

branch3x3 = conv2d_bn(x, 192, 1, 1)

# ==================================================
# Line: 303

branch_pool = layers.MaxPooling2D((3, 3), strides=(2, 2))(x)

# ==================================================
# Occurrences: Lines 329-332 (2 instances)

branch_pool = layers.AveragePooling2D(
    (3, 3), strides=(1, 1), padding="same"
)(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/efficientnet_v2.py
# Line: 1045

x = layers.GlobalAveragePooling2D(name="avg_pool")(x)

# ==================================================
# Line: 1058

x = layers.GlobalAveragePooling2D(name="avg_pool")(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/mobilenet_v2.py
# Occurrences: Lines 131-135 (2 instances)

is_input_t_tensor = backend.is_keras_tensor(input_tensor)

# ==================================================
# Line: 170

backend.is_keras_tensor(input_tensor)

# ==================================================
# Occurrences: Lines 177-179 (2 instances)

if input_shape is None and not backend.is_keras_tensor(input_tensor):

# ==================================================
# Line: 248

if not backend.is_keras_tensor(input_tensor):

# ==================================================
# Line: 344

x = layers.GlobalAveragePooling2D()(x)

# ==================================================
# Line: 352

x = layers.GlobalAveragePooling2D()(x)

# ==================================================
# Line: 359

inputs = operation_utils.get_source_inputs(input_tensor)

# ==================================================
# Line: 379

weights_path = file_utils.get_file(
    model_name, weight_path, cache_subdir="models"
)

# ==================================================
# Line: 392

weights_path = file_utils.get_file(
    model_name, weight_path, cache_subdir="models"
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/xception.py
# Line: 142

residual = layers.BatchNormalization(axis=channel_axis)(residual)

# ==================================================
# Occurrences: Lines 161-166 (2 instances)

x = layers.add([x, residual])

# ==================================================
# Occurrences: Lines 186-191 (2 instances)

x = layers.add([x, residual])

# ==================================================
# Line: 211

x = layers.add([x, residual])

# ==================================================
# Occurrences: Lines 251-256 (2 instances)

x = layers.add([x, residual])

# ==================================================
# Line: 276

x = layers.add([x, residual])

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/inception_resnet_v2.py
# Occurrences: Lines 134-137 (2 instances)

x = layers.MaxPooling2D(3, strides=2)(x)

# ==================================================
# Occurrences: Lines 144-145 (2 instances)

branch_2 = conv2d_bn(branch_2, 96, 3)

# ==================================================
# Occurrences: Lines 160-163 (2 instances)

branch_1 = conv2d_bn(x, 256, 1)

# ==================================================
# Occurrences: Lines 174-181 (4 instances)

branch_0 = conv2d_bn(x, 256, 1)

# ==================================================
# Occurrences: Lines 333-341 (4 instances)

branch_0 = conv2d_bn(x, 32, 1)

# ==================================================
# Occurrences: Lines 347-348 (2 instances)

branch_0 = conv2d_bn(x, 192, 1)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/nasnet.py
# Line: 250

x = layers.GlobalAveragePooling2D()(x)

# ==================================================
# Line: 257

x = layers.GlobalAveragePooling2D()(x)

# ==================================================
# Line: 616

p = layers.BatchNormalization(
    axis=channel_dim,
    momentum=0.9997,
    epsilon=1e-3,
    name=f"adjust_bn_{block_id}",
)(p)

# ==================================================
# Line: 635

p = layers.BatchNormalization(
    axis=channel_dim,
    momentum=0.9997,
    epsilon=1e-3,
    name=f"adjust_bn_{block_id}",
)(p)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/imagenet_utils_test.py
# Occurrences: Lines 15-26 (5 instances)

x = np.random.uniform(0, 255, (10, 10, 3))

# ==================================================
# Occurrences: Lines 37-43 (4 instances)

x = np.random.uniform(0, 255, (10, 10, 3))

# ==================================================
# Occurrences: Lines 55-64 (5 instances)

x = np.random.uniform(0, 255, (2, 10, 10, 3))

# ==================================================
# Occurrences: Lines 84-101 (6 instances)

x = np.random.uniform(0, 255, (2, 10, 10, 3))

# ==================================================
# Line: 109

model2 = keras.Model(inputs2, outputs2)

# ==================================================
# Occurrences: Lines 115-131 (6 instances)

x = np.random.uniform(0, 255, (10, 10, 3))

# ==================================================
# Line: 139

model2 = keras.Model(inputs2, outputs2)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/efficientnet.py
# Line: 393

x = layers.GlobalAveragePooling2D(name="avg_pool")(x)

# ==================================================
# Line: 405

x = layers.GlobalAveragePooling2D(name="avg_pool")(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/mobilenet.py
# Occurrences: Lines 260-268 (2 instances)

weights_path = file_utils.get_file(
    model_name, weight_path, cache_subdir="models"
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/nn.py
# Occurrences: Lines 433-434 (2 instances)

mean_shape = ov_opset.shape_of(mean)

# ==================================================
# Occurrences: Lines 440-441 (2 instances)

mean_shape = ov_opset.shape_of(mean)

# ==================================================
# Line: 453

perm_vector = ov_opset.constant(perm_vector, Type.i32).output(0)

# ==================================================
# Line: 462

perm_vector = ov_opset.constant(perm_vector, Type.i32).output(0)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/random.py
# Occurrences: Lines 25-29 (2 instances)

seed = draw_seed(seed)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/trainer.py
# Occurrences: Lines 72-77 (2 instances)

param_elem = self._parameterize_data(elem)

# ==================================================
# Line: 97

and get_device() == self.ov_device

# ==================================================
# Occurrences: Lines 118-119 (2 instances)

self.ov_compiled_model = ov.compile_model(ov_model, get_device())

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/numpy.py
# Line: 290

x1_type = ov_to_keras_type(x1.get_element_type())

# ==================================================
# Line: 300

ov_type = x1.get_element_type()

# ==================================================
# Occurrences: Lines 349-353 (2 instances)

k = ov_opset.constant(1, Type.i32).output(0)

# ==================================================
# Occurrences: Lines 381-385 (2 instances)

k = ov_opset.constant(1, Type.i32).output(0)

# ==================================================
# Line: 410

x_shape_tensor = ov_opset.shape_of(x, Type.i32).output(0)

# ==================================================
# Line: 418

x_shape_tensor = ov_opset.shape_of(x, Type.i32).output(0)

# ==================================================
# Occurrences: Lines 657-660 (2 instances)

return OpenVINOKerasTensor(get_ov_output(a))

# ==================================================
# Occurrences: Lines 680-682 (2 instances)

end_upper = ov_opset.constant(
    np.array([0] * rank, dtype=np.int64), Type.i64
).output(0)

# ==================================================
# Occurrences: Lines 698-700 (2 instances)

begin_lower = ov_opset.constant(
    np.array([0] * rank, dtype=np.int64), Type.i64
).output(0)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/core.py
# Occurrences: Lines 102-113 (4 instances)

x = ov_opset.constant(x, ov_type).output(0)

# ==================================================
# Line: 134

x_shape = x.get_partial_shape()

# ==================================================
# Occurrences: Lines 149-150 (2 instances)

if x.get_partial_shape().rank.is_static:

# ==================================================
# Line: 473

dtype = standardize_dtype(dtype)

# ==================================================
# Line: 479

dtype = standardize_dtype(dtype)

# ==================================================
# Occurrences: Lines 487-499 (4 instances)

x = np.array(x, dtype=dtype)

# ==================================================
# Line: 505

return ov.Tensor(np.array(x, dtype=dtype))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/image.py
# Occurrences: Lines 187-189 (2 instances)

crop_height = int(float(width * target_height) / target_width)

# ==================================================
# Occurrences: Lines 228-230 (2 instances)

pad_height = int(float(width * target_height) / target_width)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/rnn.py
# Occurrences: Lines 92-96 (2 instances)

inp = _get_input_tensor(i)

# ==================================================
# Occurrences: Lines 127-134 (3 instances)

outputs = np.stack(successive_outputs)

# ==================================================
# Line: 143

outputs = np.stack(successive_outputs)

# ==================================================
# Line: 154

output_t, new_states = step_function(current_input, states)

# ==================================================
# Line: 180

output_t, new_states = step_function(current_input, states)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/nn.py
# Occurrences: Lines 949-955 (3 instances)

paths, unique_inverse = np.unique(paths, return_inverse=True, axis=0)

# ==================================================
# Occurrences: Lines 1005-1011 (3 instances)

paths, unique_inverse = np.unique(paths, return_inverse=True, axis=0)

# ==================================================
# Line: 1095

combined_mask = np.logical_and(combined_mask, mask)

# ==================================================
# Line: 1101

combined_mask = np.logical_and(combined_mask, mask)

# ==================================================
# Line: 1115

value = value.astype("float32")

# ==================================================
# Line: 1132

value = value.astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/numpy.py
# Occurrences: Lines 887-889 (2 instances)

x = x.astype(config.floatx())

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/core.py
# Occurrences: Lines 43-48 (2 instances)

dtype = standardize_dtype(dtype)

# ==================================================
# Occurrences: Lines 188-192 (2 instances)

n = int(length)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/image.py
# Occurrences: Lines 149-161 (3 instances)

shape = tf.shape(images)

# ==================================================
# Occurrences: Lines 185-197 (3 instances)

shape = tf.shape(images)

# ==================================================
# Occurrences: Lines 208-209 (2 instances)

batch_size = tf.shape(images)[0]

# ==================================================
# Line: 251

channels = tf.shape(images)[2]

# ==================================================
# Occurrences: Lines 669-672 (4 instances)

safe_coords = tf.clip_by_value(coords, 0, size - 1)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/sparse.py
# Occurrences: Lines 326-326 (3 instances)

x, func(x.values, *args, **kwargs)

# ==================================================
# Occurrences: Lines 333-333 (3 instances)

sparse_output_values = func(x.values, *args, **kwargs)

# ==================================================
# Occurrences: Lines 439-439 (3 instances)

output = sparse_op(x1, x2)

# ==================================================
# Occurrences: Lines 450-450 (3 instances)

return sparse_op(x1, x2)

# ==================================================
# Occurrences: Lines 459-459 (3 instances)

return sparse_op(x1, x2)

# ==================================================
# Occurrences: Lines 666-666 (2 instances)

x2 = sparse_to_dense(x2)

# ==================================================
# Occurrences: Lines 674-678 (4 instances)

x2_zeros_and_nans = tf.equal(x2, 0)

# ==================================================
# Occurrences: Lines 688-688 (2 instances)

x2_zeros_and_nan_indices = tf.where(x2_zeros_and_nans)

# ==================================================
# Occurrences: Lines 715-715 (2 instances)

x2 = sparse_to_dense(x2)

# ==================================================
# Occurrences: Lines 722-722 (2 instances)

x2 = tf.convert_to_tensor(x2)

# ==================================================
# Occurrences: Lines 732-736 (4 instances)

x2_zeros_and_nans = tf.equal(x2, 0)

# ==================================================
# Occurrences: Lines 751-751 (2 instances)

tf.where(x2_zeros_and_nans), axis=-1

# ==================================================
# Occurrences: Lines 778-778 (2 instances)

x2 = tf.convert_to_tensor(x2)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/rnn.py
# Occurrences: Lines 166-170 (2 instances)

inp = _get_input_tensor(i)

# ==================================================
# Occurrences: Lines 180-181 (2 instances)

flat_states = tree.flatten(states)

# ==================================================
# Line: 201

outputs = tf.stack(successive_outputs)

# ==================================================
# Occurrences: Lines 217-220 (2 instances)

inp = _get_input_tensor(i)

# ==================================================
# Line: 229

outputs = tf.stack(successive_outputs)

# ==================================================
# Occurrences: Lines 355-361 (3 instances)

current_input = tree.pack_sequence_as(inputs, current_input)

# ==================================================
# Occurrences: Lines 372-373 (2 instances)

flat_state = tree.flatten(states)

# ==================================================
# Occurrences: Lines 410-416 (4 instances)

current_input = tree.pack_sequence_as(inputs, current_input)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/nn.py
# Line: 379

outputs = tf.nn.depthwise_conv2d(
    inputs,
    kernel,
    strides,
    padding,
    data_format=tf_data_format,
    dilations=dilation_rate,
)

# ==================================================
# Line: 395

return tf.nn.depthwise_conv2d(
    inputs,
    kernel,
    strides,
    padding,
    data_format=tf_data_format,
    dilations=dilation_rate,
)

# ==================================================
# Line: 442

outputs = tf.nn.separable_conv2d(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides,
    padding,
    data_format=tf_data_format,
    dilations=dilation_rate,
)

# ==================================================
# Line: 457

return tf.nn.separable_conv2d(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides,
    padding,
    data_format=tf_data_format,
    dilations=dilation_rate,
)

# ==================================================
# Line: 553

outputs = tf.sparse.reduce_max(
    outputs, axis=reduction_axis, output_is_sparse=True
)

# ==================================================
# Line: 561

outputs = one_hot(x, num_classes, axis=axis, dtype=dtype)

# ==================================================
# Occurrences: Lines 570-574 (2 instances)

return tf.sparse.reduce_max(
    outputs, axis=reduction_axis, output_is_sparse=True
)

# ==================================================
# Line: 1004

combined_mask = tf.logical_and(combined_mask, mask)

# ==================================================
# Line: 1011

combined_mask = tf.logical_and(combined_mask, mask)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/saved_model_test.py
# Occurrences: Lines 25-26 (2 instances)

self.dense1 = layers.Dense(1)

# ==================================================
# Occurrences: Lines 200-205 (2 instances)

model = models.Model([input_1, input_2], [output_1, output_2])

# ==================================================
# Line: 355

_ = restored_model.concat("hello")

# ==================================================
# Line: 366

self.assertEqual(model.concat("hello"), restored_model.concat("hello"))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/random.py
# Occurrences: Lines 74-76 (2 instances)

return tf.shape(inputs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/trainer.py
# Occurrences: Lines 177-177 (2 instances)

lambda: iterator.get_next_as_optional(),

# ==================================================
# Occurrences: Lines 200-200 (2 instances)

next_optional_inputs = iterator.get_next_as_optional()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/distribute_test.py
# Occurrences: Lines 174-183 (4 instances)

inputs = layers.Input(shape=(1,))

# ==================================================
# Occurrences: Lines 189-198 (4 instances)

inputs = layers.Input(shape=(1,))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/numpy.py
# Occurrences: Lines 70-71 (2 instances)

array = tf.reverse(array, axis=[2])

# ==================================================
# Occurrences: Lines 81-82 (2 instances)

array = tf.reverse(array, axis=[2])

# ==================================================
# Occurrences: Lines 319-340 (20 instances)

return tf.matmul(x, y, output_type=output_type)

# ==================================================
# Occurrences: Lines 346-347 (4 instances)

y = tf.reshape(y, [c, -1])

# ==================================================
# Occurrences: Lines 354-378 (28 instances)

y = tf.reshape(y, [c, -1])

# ==================================================
# Occurrences: Lines 384-402 (18 instances)

x = tf.reshape(x, [-1, b, c * d])

# ==================================================
# Occurrences: Lines 408-409 (4 instances)

y = tf.transpose(y, [0, 2, 1, 3])  # abef

# ==================================================
# Occurrences: Lines 418-419 (4 instances)

y = tf.transpose(y, [0, 2, 3, 1])  # acef

# ==================================================
# Occurrences: Lines 441-452 (4 instances)

compute_dtype = config.floatx()

# ==================================================
# Occurrences: Lines 595-600 (2 instances)

output = tf.cast(output, result_dtype)

# ==================================================
# Occurrences: Lines 606-607 (2 instances)

output = tf.matmul(x1, x2, output_type=output_type)

# ==================================================
# Occurrences: Lines 709-713 (2 instances)

x = tf.reduce_any(x, axis=axis, keepdims=keepdims)

# ==================================================
# Occurrences: Lines 727-729 (2 instances)

return tf.reduce_any(x, axis=axis, keepdims=keepdims)

# ==================================================
# Occurrences: Lines 903-910 (4 instances)

dtype = standardize_dtype(x.dtype)

# ==================================================
# Occurrences: Lines 919-926 (4 instances)

is_negative_zero, -np.finfo(standardize_dtype(x.dtype)).tiny, x

# ==================================================
# Occurrences: Lines 934-941 (4 instances)

dtype = standardize_dtype(x.dtype)

# ==================================================
# Occurrences: Lines 950-957 (4 instances)

is_negative_zero, -np.finfo(standardize_dtype(x.dtype)).tiny, x

# ==================================================
# Occurrences: Lines 985-990 (2 instances)

x = tf.cast(x, dtype)

# ==================================================
# Occurrences: Lines 1003-1006 (2 instances)

avg = _rank_equal_case()

# ==================================================
# Line: 1210

x1_dim = shape_op(x1)[-1]

# ==================================================
# Line: 1217

shape = shape_op(x1)

# ==================================================
# Line: 1296

x = _zeros()

# ==================================================
# Line: 1303

lambda: _zeros(),

# ==================================================
# Line: 1595

result = tf.linspace(start, stop, num, axis=axis)

# ==================================================
# Line: 1607

result = tf.linspace(start, stop, num, axis=axis)

# ==================================================
# Occurrences: Lines 1739-1743 (2 instances)

x = tf.reduce_all(x, axis=axis, keepdims=keepdims)

# ==================================================
# Occurrences: Lines 1757-1759 (2 instances)

return tf.reduce_all(x, axis=axis, keepdims=keepdims)

# ==================================================
# Occurrences: Lines 1952-1955 (2 instances)

+ tf.gather(sorted_y, _get_indices("higher"), axis=-1)

# ==================================================
# Line: 2258

indices = convert_to_tensor(indices, sparse=False)

# ==================================================
# Line: 2265

indices = convert_to_tensor(indices, sparse=False)

# ==================================================
# Line: 2405

return tf.round(x)

# ==================================================
# Line: 2418

x = tf.round(x)

# ==================================================
# Line: 2443

dtype = standardize_dtype(x.dtype)

# ==================================================
# Line: 2455

if standardize_dtype(x.dtype) == "bool":

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/optimizer.py
# Line: 151

replica_context = tf.distribute.get_replica_context()

# ==================================================
# Line: 159

reduced = tf.distribute.get_replica_context().all_reduce(

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/core.py
# Occurrences: Lines 152-157 (2 instances)

return tf.cast(x, dtype)

# ==================================================
# Occurrences: Lines 306-311 (2 instances)

n = int(length)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/stateless_scope_test.py
# Occurrences: Lines 11-16 (5 instances)

var1 = backend.Variable(np.zeros((2,)))

# ==================================================
# Occurrences: Lines 31-35 (2 instances)

var_out_value = scope.get_current_value(var_out)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/global_state_test.py
# Occurrences: Lines 8-13 (3 instances)

name0 = auto_name("somename")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/variables_test.py
# Occurrences: Lines 642-643 (2 instances)

v1 = backend.Variable(initializer=np.array([1.0, 2.0, 3.0]))

# ==================================================
# Occurrences: Lines 654-655 (2 instances)

v1 = backend.Variable(initializer=np.array([1.0, 2.0, 3.0]))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/symbolic_scope_test.py
# Occurrences: Lines 18-24 (4 instances)

y = ops.ones(shape=(2,))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/variables.py
# Occurrences: Lines 143-145 (2 instances)

parent_path = current_path()

# ==================================================
# Line: 183

self._shape = self._validate_shape(shape)

# ==================================================
# Line: 205

self._shape = self._validate_shape(shape)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/global_state.py
# Occurrences: Lines 76-77 (2 instances)

GLOBAL_STATE_TRACKER = threading.local()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/remat_test.py
# Occurrences: Lines 55-75 (5 instances)

global_state.get_global_attribute("remat_scope_stack")

# ==================================================
# Occurrences: Lines 98-102 (2 instances)

output_with_remat = backend.core.remat(activations.ReLU())(x_train)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/keras_tensor_test.py
# Occurrences: Lines 408-409 (2 instances)

x = keras_tensor.KerasTensor(shape=(3, 4), dtype="float32")

# ==================================================
# Occurrences: Lines 420-421 (2 instances)

x = keras_tensor.KerasTensor(shape=(3, 4), dtype="float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/image.py
# Occurrences: Lines 191-193 (2 instances)

crop_height = int(float(width * target_height) / target_width)

# ==================================================
# Occurrences: Lines 232-234 (2 instances)

pad_height = int(float(width * target_height) / target_width)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/sparse.py
# Occurrences: Lines 289-289 (2 instances)

x2 = x2.todense()

# ==================================================
# Occurrences: Lines 325-325 (2 instances)

x2 = x2.todense()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/export.py
# Line: 67

jax_fn.__signature__ = inspect.Signature(
    parameters=fn_parameters[0 : len(input_signature)],
    return_annotation=fn_signature.return_annotation,
)

# ==================================================
# Line: 115

stateful_fn.__signature__ = inspect.Signature(
    parameters=fn_parameters[0 : len(input_signature)],
    return_annotation=fn_signature.return_annotation,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/rnn.py
# Occurrences: Lines 96-100 (2 instances)

inp = _get_input_tensor(i)

# ==================================================
# Occurrences: Lines 131-138 (3 instances)

outputs = jnp.stack(successive_outputs)

# ==================================================
# Line: 147

outputs = jnp.stack(successive_outputs)

# ==================================================
# Line: 158

output_t, new_states = step_function(current_input, states)

# ==================================================
# Line: 184

output_t, new_states = step_function(current_input, states)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/nn.py
# Occurrences: Lines 889-897 (2 instances)

paths, unique_inverse = jnp.unique(
    paths,
    return_inverse=True,
    size=2 * num_classes * beam_width,
    axis=0,
    fill_value=_pad,
)

# ==================================================
# Occurrences: Lines 950-958 (2 instances)

paths, unique_inverse = jnp.unique(
    paths,
    return_inverse=True,
    size=2 * num_classes * beam_width,
    axis=0,
    fill_value=_pad,
)

# ==================================================
# Line: 1089

combined_mask = jnp.logical_and(combined_mask, mask)

# ==================================================
# Line: 1095

combined_mask = jnp.logical_and(combined_mask, mask)

# ==================================================
# Occurrences: Lines 1309-1315 (2 instances)

causal_mask = jnp.tril(
    jnp.ones((q_len, q_len), dtype=jnp.bool_)
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/trainer.py
# Occurrences: Lines 239-245 (8 instances)

data = next(iterator)

# ==================================================
# Occurrences: Lines 255-260 (8 instances)

data = next(iterator)

# ==================================================
# Line: 268

return step_function(state, next(iterator))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/distribution_lib_test.py
# Line: 82

return distribution_lib.distribute_tensor(inputs, target_layout)

# ==================================================
# Line: 91

result = distribution_lib.distribute_tensor(inputs, target_layout)

# ==================================================
# Line: 143

return distribution_lib.distribute_tensor(inputs, target_layout)

# ==================================================
# Line: 154

result = distribution_lib.distribute_tensor(inputs, target_layout)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/optimizer.py
# Line: 51

grads = self._clip_gradients(grads)

# ==================================================
# Line: 79

grads = self._clip_gradients(grads)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/core.py
# Line: 62

dtype = standardize_dtype(dtype)

# ==================================================
# Line: 84

if not is_tensor(x) and standardize_dtype(dtype) == "bfloat16":

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/image.py
# Occurrences: Lines 233-235 (2 instances)

crop_height = int(float(width * target_height) / target_width)

# ==================================================
# Occurrences: Lines 249-251 (2 instances)

pad_height = int(float(width * target_height) / target_width)

# ==================================================
# Occurrences: Lines 749-757 (3 instances)

if len(coordinate_arrs) != len(input_arr.shape):

# ==================================================
# Occurrences: Lines 893-896 (2 instances)

device = get_device()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/rnn.py
# Occurrences: Lines 95-104 (3 instances)

mask_list = torch.unbind(mask)

# ==================================================
# Occurrences: Lines 114-115 (2 instances)

flat_states = tree.flatten(states)

# ==================================================
# Line: 135

outputs = torch.stack(successive_outputs)

# ==================================================
# Occurrences: Lines 151-154 (2 instances)

inp = _get_input_tensor(i)

# ==================================================
# Line: 163

outputs = torch.stack(successive_outputs)

# ==================================================
# Line: 213

mask_ta = list(torch.unbind(mask))

# ==================================================
# Occurrences: Lines 271-277 (3 instances)

current_input = tree.pack_sequence_as(inputs, current_input)

# ==================================================
# Occurrences: Lines 288-289 (2 instances)

flat_state = tree.flatten(states)

# ==================================================
# Occurrences: Lines 331-337 (4 instances)

current_input = tree.pack_sequence_as(inputs, current_input)

# ==================================================
# Occurrences: Lines 492-493 (2 instances)

bias_ih_data = torch.zeros(4 * hidden_size, device=device)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/nn.py
# Occurrences: Lines 156-160 (2 instances)

dtype = backend.standardize_dtype(x.dtype)

# ==================================================
# Occurrences: Lines 176-180 (2 instances)

dtype = backend.standardize_dtype(x.dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/random.py
# Occurrences: Lines 19-23 (2 instances)

device = get_device()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/math.py
# Line: 89

x = convert_to_tensor(x)

# ==================================================
# Line: 96

x = convert_to_tensor(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/numpy.py
# Occurrences: Lines 113-114 (2 instances)

x1_dtype = standardize_dtype(x1.dtype)

# ==================================================
# Occurrences: Lines 133-134 (2 instances)

x1_dtype = standardize_dtype(x1.dtype)

# ==================================================
# Line: 143

compute_dtype = config.floatx()

# ==================================================
# Line: 149

compute_dtype = config.floatx()

# ==================================================
# Occurrences: Lines 552-555 (2 instances)

x = cast(x, config.floatx())

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/core.py
# Line: 200

device = get_device()

# ==================================================
# Occurrences: Lines 208-216 (4 instances)

return x.to(to_torch_dtype(dtype))

# ==================================================
# Occurrences: Lines 238-239 (2 instances)

dtype = to_torch_dtype(dtype)

# ==================================================
# Occurrences: Lines 328-331 (2 instances)

meta_args, meta_kwargs = tree.map_structure(
    lambda x: convert_keras_tensor_to_torch(x, fill_value),
    (args, kwargs),
)

# ==================================================
# Occurrences: Lines 338-341 (2 instances)

eager_args, eager_kwargs = tree.map_structure(
    lambda x: convert_keras_tensor_to_torch(x, fill_value),
    (args, kwargs),
)

# ==================================================
# Occurrences: Lines 416-420 (2 instances)

n = int(length)

# ==================================================
# Occurrences: Lines 714-716 (2 instances)

output, ctx.grad_fn = forward_fn(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/activations/activations_test.py
# Line: 529

expected = np.zeros((2, 5))

# ==================================================
# Line: 558

expected_large_negative = np.zeros((2, 5))

# ==================================================
# Line: 568

positive_values = np.random.random((2, 5))

# ==================================================
# Line: 576

negative_values = np.random.uniform(-1, 0, (2, 5))

# ==================================================
# Line: 585

positive_values = np.random.random((2, 5))

# ==================================================
# Line: 593

negative_values = np.random.uniform(-1, 0, (2, 5))

# ==================================================
# Occurrences: Lines 661-666 (2 instances)

x = np.random.random((2, 5))

# ==================================================
# Occurrences: Lines 677-682 (2 instances)

x = np.random.random((2, 5))

# ==================================================
# Occurrences: Lines 692-697 (2 instances)

x = np.random.random((2, 4))

# ==================================================
# Line: 789

expected = np.tanh(x)

# ==================================================
# Line: 795

expected = np.tanh(x)

# ==================================================
# Occurrences: Lines 838-843 (2 instances)

expected = np.exp(x)

# ==================================================
# Line: 939

x = np.random.uniform(-10, 10, (10, 5))

# ==================================================
# Line: 947

x_float32 = np.random.uniform(-10, 10, (10, 5)).astype(np.float32)

# ==================================================
# Line: 955

x_1d = np.linspace(1, 12, num=12)

# ==================================================
# Occurrences: Lines 961-974 (9 instances)

x_2d = np.linspace(1, 12, num=12).reshape(-1, 2)

# ==================================================
# Occurrences: Lines 981-981 (2 instances)

x_3d = np.linspace(1, 12, num=12).reshape(-1, 1, 3)

# ==================================================
# Occurrences: Lines 988-989 (3 instances)

x_3d = np.linspace(1, 12, num=12).reshape(-1, 1, 3)

# ==================================================
# Line: 996

x_4d = np.linspace(1, 12, num=12).reshape(-1, 1, 1, 2)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/initializers/constant_initializers_test.py
# Occurrences: Lines 104-105 (2 instances)

window = window.astype("float64").reshape((-1, 1, 1))

# ==================================================
# Occurrences: Lines 116-118 (2 instances)

window = window.astype("float64").reshape((-1, 1, 1))

# ==================================================
# Occurrences: Lines 128-130 (2 instances)

window = window.astype("float64").reshape((-1, 1, 1))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/initializers/random_initializers_test.py
# Line: 21

values = initializer(shape=shape)

# ==================================================
# Occurrences: Lines 33-52 (8 instances)

initializer = initializers.RandomNormal(
    mean=mean, stddev=stddev, seed=1337
)

# ==================================================
# Occurrences: Lines 58-73 (7 instances)

values = initializer(shape=shape)

# ==================================================
# Line: 103

values = initializer(shape=shape)

# ==================================================
# Line: 117

values = initializer(shape=shape)

# ==================================================
# Occurrences: Lines 175-182 (4 instances)

initializer = initializers.get(tensor)

# ==================================================
# Occurrences: Lines 221-233 (4 instances)

seed = random.SeedGenerator()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/initializers/random_initializers.py
# Occurrences: Lines 295-300 (2 instances)

stddev = math.sqrt(scale) / 0.87962566103423978

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/distribution/distribution_lib.py
# Line: 677

distributed_dataset = dataset.rebatch(per_process_batch_size)

# ==================================================
# Line: 694

distributed_dataset = dataset.rebatch(per_process_batch_size)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/distribution/distribution_lib_test.py
# Occurrences: Lines 152-153 (2 instances)

distribution_1 = distribution_lib.Distribution(self.device_mesh)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/export/export_utils.py
# Occurrences: Lines 75-79 (2 instances)

dtype = backend.standardize_dtype(x.dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/export/tf2onnx_lib.py
# Occurrences: Lines 82-82 (4 instances)

val = func(*inputs)

# ==================================================
# Occurrences: Lines 95-95 (4 instances)

val = func(*inputs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/export/saved_model_test.py
# Occurrences: Lines 113-114 (2 instances)

output1 = revived_model.serve(input)

# ==================================================
# Occurrences: Lines 149-152 (2 instances)

output1, counter1 = revived_model.serve(input)

# ==================================================
# Occurrences: Lines 251-252 (2 instances)

ref_input_x = np.random.normal(size=(batch_size, 10)).astype("float32")

# ==================================================
# Line: 364

export_archive = saved_model.ExportArchive()

# ==================================================
# Line: 370

export_archive = saved_model.ExportArchive()

# ==================================================
# Line: 511

export_archive = saved_model.ExportArchive()

# ==================================================
# Line: 521

export_archive = saved_model.ExportArchive()

# ==================================================
# Occurrences: Lines 637-638 (2 instances)

X = np.random.random((1024, window_size, 1))

# ==================================================
# Line: 680

ref_input = np.random.random((1024, window_size, 1))

# ==================================================
# Occurrences: Lines 722-723 (2 instances)

x1 = layers.Input((2,))

# ==================================================
# Occurrences: Lines 729-732 (2 instances)

ref_outputs = model(ref_inputs)

# ==================================================
# Occurrences: Lines 747-750 (2 instances)

ref_outputs = model(ref_inputs)

# ==================================================
# Occurrences: Lines 813-814 (2 instances)

x1 = tf.random.normal((3, 2, 2))

# ==================================================
# Occurrences: Lines 834-835 (2 instances)

x1 = tf.random.normal((3, 2, 2))

# ==================================================
# Line: 903

export_archive = saved_model.ExportArchive()

# ==================================================
# Line: 920

export_archive = saved_model.ExportArchive()

# ==================================================
# Occurrences: Lines 927-931 (2 instances)

export_archive = saved_model.ExportArchive()

# ==================================================
# Line: 939

export_archive = saved_model.ExportArchive()

# ==================================================
# Line: 946

export_archive = saved_model.ExportArchive()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/export/onnx_test.py
# Occurrences: Lines 189-190 (2 instances)

ref_input_x = np.random.normal(size=(batch_size, 10)).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/lstm_test.py
# Line: 60

output = layer(sequence)

# ==================================================
# Line: 80

output = layer(sequence)

# ==================================================
# Line: 100

output = layer(sequence)

# ==================================================
# Line: 120

output = layer(sequence)

# ==================================================
# Line: 140

output = layer(sequence)

# ==================================================
# Occurrences: Lines 161-162 (2 instances)

layer(sequence)

# ==================================================
# Occurrences: Lines 173-174 (2 instances)

layer(sequence)

# ==================================================
# Line: 197

output = layer(sequence, initial_state=initial_state)

# ==================================================
# Line: 210

output = layer(sequence, initial_state=initial_state)

# ==================================================
# Line: 226

output = layer(sequence, mask=mask)

# ==================================================
# Line: 239

output = layer(sequence, mask=mask)

# ==================================================
# Line: 271

output = layer(sequence, mask=mask)

# ==================================================
# Line: 302

output = layer(sequence, mask=mask)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/rnn_test.py
# Occurrences: Lines 159-163 (2 instances)

output_shape = layer.compute_output_shape(sequence.shape)

# ==================================================
# Line: 169

output_shape = layer.compute_output_shape(sequence.shape)

# ==================================================
# Line: 176

output_shape = layer.compute_output_shape(sequence.shape)

# ==================================================
# Occurrences: Lines 183-187 (2 instances)

output_shape = layer.compute_output_shape(sequence.shape)

# ==================================================
# Line: 193

output_shape = layer.compute_output_shape(sequence.shape)

# ==================================================
# Line: 201

output_shape = layer.compute_output_shape(sequence.shape)

# ==================================================
# Occurrences: Lines 209-213 (2 instances)

output_shape = layer.compute_output_shape(sequence_shape)

# ==================================================
# Line: 219

output_shape = layer.compute_output_shape(sequence_shape)

# ==================================================
# Occurrences: Lines 226-235 (3 instances)

output_shape = layer.compute_output_shape(sequence_shape)

# ==================================================
# Line: 241

output_shape = layer.compute_output_shape(sequence_shape)

# ==================================================
# Line: 249

output_shape = layer.compute_output_shape(sequence_shape)

# ==================================================
# Occurrences: Lines 257-261 (2 instances)

output = layer(sequence)

# ==================================================
# Line: 267

output, state = layer(sequence)

# ==================================================
# Line: 274

output, state = layer(sequence)

# ==================================================
# Occurrences: Lines 281-285 (2 instances)

output = layer(sequence)

# ==================================================
# Line: 291

output, state1, state2 = layer(sequence)

# ==================================================
# Line: 299

output, state1, state2 = layer(sequence)

# ==================================================
# Line: 308

output = layer(sequence, initial_state=state)

# ==================================================
# Line: 314

output, state = layer(sequence, initial_state=state)

# ==================================================
# Line: 322

output = layer(sequence, initial_state=state)

# ==================================================
# Line: 328

output, state_1, state_2 = layer(sequence, initial_state=state)

# ==================================================
# Occurrences: Lines 336-342 (4 instances)

layer(sequence)

# ==================================================
# Occurrences: Lines 349-350 (2 instances)

layer(sequence)

# ==================================================
# Occurrences: Lines 356-357 (2 instances)

layer(sequence)

# ==================================================
# Occurrences: Lines 365-371 (4 instances)

layer(sequence)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/bidirectional.py
# Occurrences: Lines 111-125 (4 instances)

config = serialization_lib.serialize_keras_object(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/lstm.py
# Line: 236

dp_mask = self.get_dropout_mask(inputs)

# ==================================================
# Line: 274

dp_mask = self.get_dropout_mask(inputs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/stacked_rnn_cells_test.py
# Line: 139

output = layer(sequence)

# ==================================================
# Line: 147

output = layer(sequence)

# ==================================================
# Line: 161

output, state_1, state_2 = layer(sequence)

# ==================================================
# Line: 177

output, state_1, state_2 = layer(sequence)

# ==================================================
# Line: 197

output = layer(sequence)

# ==================================================
# Line: 205

output = layer(sequence)

# ==================================================
# Line: 219

output, state_1, state_2 = layer(sequence)

# ==================================================
# Occurrences: Lines 242-243 (2 instances)

layer(sequence)

# ==================================================
# Occurrences: Lines 253-254 (2 instances)

layer(sequence)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/simple_rnn_test.py
# Line: 48

output = layer(sequence)

# ==================================================
# Line: 65

output = layer(sequence)

# ==================================================
# Line: 83

output = layer(sequence)

# ==================================================
# Line: 101

output = layer(sequence)

# ==================================================
# Occurrences: Lines 121-122 (2 instances)

layer(sequence)

# ==================================================
# Occurrences: Lines 133-134 (2 instances)

layer(sequence)

# ==================================================
# Line: 154

output = layer(sequence, initial_state=initial_state)

# ==================================================
# Line: 172

output = layer(sequence, initial_state=initial_state)

# ==================================================
# Line: 193

output = layer(sequence, mask=mask)

# ==================================================
# Line: 211

output = layer(sequence, mask=mask)

# ==================================================
# Line: 243

output = layer(sequence, mask=mask)

# ==================================================
# Line: 274

output = layer(sequence, mask=mask)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/bidirectional_test.py
# Line: 46

output = layer(sequence)

# ==================================================
# Line: 58

output = layer(sequence)

# ==================================================
# Line: 65

output1, output2 = layer(sequence)

# ==================================================
# Line: 85

output = layer(sequence)

# ==================================================
# Line: 99

output = layer(sequence)

# ==================================================
# Occurrences: Lines 128-129 (2 instances)

layer(sequence)

# ==================================================
# Occurrences: Lines 140-141 (2 instances)

layer(sequence)

# ==================================================
# Occurrences: Lines 243-260 (10 instances)

layer = layers.Bidirectional(sub_layer, merge_mode=merge_mode)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/stacked_rnn_cells.py
# Occurrences: Lines 91-92 (4 instances)

state_is_list = tree.is_nested(states)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/gru_test.py
# Line: 59

output = layer(sequence)

# ==================================================
# Line: 78

output = layer(sequence)

# ==================================================
# Line: 97

output = layer(sequence)

# ==================================================
# Line: 116

output = layer(sequence)

# ==================================================
# Line: 135

output = layer(sequence)

# ==================================================
# Occurrences: Lines 156-157 (2 instances)

layer(sequence)

# ==================================================
# Occurrences: Lines 168-169 (2 instances)

layer(sequence)

# ==================================================
# Line: 189

output = layer(sequence, initial_state=initial_state)

# ==================================================
# Line: 202

output = layer(sequence, initial_state=initial_state)

# ==================================================
# Line: 218

output = layer(sequence, mask=mask)

# ==================================================
# Line: 231

output = layer(sequence, mask=mask)

# ==================================================
# Line: 263

output = layer(sequence, mask=mask)

# ==================================================
# Line: 294

output = layer(sequence, mask=mask)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/gru.py
# Line: 198

dp_mask = self.get_dropout_mask(inputs)

# ==================================================
# Occurrences: Lines 238-239 (2 instances)

z = self.recurrent_activation(x_z + recurrent_z)

# ==================================================
# Occurrences: Lines 254-257 (2 instances)

hh = self.activation(x_h + recurrent_h)

# ==================================================
# Occurrences: Lines 283-284 (2 instances)

z = self.recurrent_activation(x_z + recurrent_z)

# ==================================================
# Line: 293

hh = self.activation(x_h + recurrent_h)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/merging/base_merge.py
# Occurrences: Lines 158-162 (2 instances)

x_ndim = ops.ndim(x)

# ==================================================
# Line: 169

x_ndim = ops.ndim(x)

# ==================================================
# Line: 201

y = self._merge_function(reshaped_inputs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/merging/merging_test.py
# Occurrences: Lines 115-120 (4 instances)

x1 = np.random.rand(*input_shape)

# ==================================================
# Occurrences: Lines 131-132 (2 instances)

mask1 = np.ones(input_shape[:-1], dtype=np.bool_)

# ==================================================
# Occurrences: Lines 152-157 (4 instances)

x1 = np.random.rand(*input_shape)

# ==================================================
# Occurrences: Lines 195-196 (2 instances)

input_1 = layers.Input(shape=shape, batch_size=batch_size)

# ==================================================
# Occurrences: Lines 212-214 (3 instances)

input_1 = layers.Input(shape=shape)

# ==================================================
# Occurrences: Lines 231-235 (2 instances)

c = layers.Dot(axes=(-2, -1))([a, b])

# ==================================================
# Occurrences: Lines 243-248 (2 instances)

output = layers.Add()([x1, x2])

# ==================================================
# Occurrences: Lines 257-262 (2 instances)

output = layers.Subtract()([x1, x2])

# ==================================================
# Occurrences: Lines 271-276 (2 instances)

output = layers.Average()([x1, x2])

# ==================================================
# Occurrences: Lines 285-290 (2 instances)

output = layers.Multiply()([x1, x2])

# ==================================================
# Occurrences: Lines 301-306 (2 instances)

output = layers.Maximum()([x1, x2])

# ==================================================
# Occurrences: Lines 315-320 (2 instances)

output = layers.Minimum()([x1, x2])

# ==================================================
# Occurrences: Lines 346-352 (3 instances)

x2 = np.ones((1, 1, 1, 1, 4))

# ==================================================
# Line: 360

out = layers.Concatenate(axis=-1)([x1, x2])

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv_test.py
# Line: 643

layer = conv_cls(
    filters=filters,
    kernel_size=kernel_size,
    strides=strides,
    padding=padding,
    data_format=data_format,
    dilation_rate=dilation_rate,
    groups=groups,
)

# ==================================================
# Occurrences: Lines 663-664 (2 instances)

init_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Occurrences: Lines 671-672 (2 instances)

final_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Line: 699

conv_cls(
    filters=filters,
    kernel_size=kernel_size,
    strides=strides,
    padding=padding,
    data_format=data_format,
    dilation_rate=dilation_rate,
    groups=groups,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv_transpose_test.py
# Line: 836

kc_res = kc_layer(input)

# ==================================================
# Occurrences: Lines 855-860 (2 instances)

kc_res = kc_layer(input)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/regularization/alpha_dropout.py
# Occurrences: Lines 82-84 (2 instances)

return ops.shape(inputs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/additive_attention_test.py
# Occurrences: Lines 63-64 (2 instances)

query_mask = np.array([[True, False]])

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/multi_head_attention.py
# Line: 804

char = _index_to_einsum_variable(i + letter_offset)

# ==================================================
# Line: 810

char = _index_to_einsum_variable(i + letter_offset)

# ==================================================
# Line: 816

char = _index_to_einsum_variable(i + letter_offset)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/grouped_query_attention_test.py
# Occurrences: Lines 302-303 (2 instances)

query = np.identity(head_dim)[np.newaxis, ...]

# ==================================================
# Line: 319

kernel = np.identity(head_dim)

# ==================================================
# Occurrences: Lines 390-391 (2 instances)

query = np.random.random((2, 4, 8))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/attention_test.py
# Line: 51

output, scores = layer(
    [query, value, key],
    return_attention_scores=True,
)

# ==================================================
# Line: 64

output, scores = layer(
    [query, value, key],
    return_attention_scores=True,
)

# ==================================================
# Occurrences: Lines 79-80 (2 instances)

query_mask = np.array([[True, False]])

# ==================================================
# Occurrences: Lines 237-241 (3 instances)

valid_mask = np.array([True, True, True])

# ==================================================
# Occurrences: Lines 252-256 (3 instances)

valid_mask = np.array([False, False, False])

# ==================================================
# Occurrences: Lines 347-352 (4 instances)

layer = layers.Attention()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/multi_head_attention_test.py
# Occurrences: Lines 367-373 (3 instances)

output_1 = layer(query=x, value=x, attention_mask=mask)

# ==================================================
# Occurrences: Lines 405-406 (2 instances)

query = np.identity(key_dim)[np.newaxis, ...]

# ==================================================
# Line: 419

kernel = np.identity(key_dim)

# ==================================================
# Line: 503

layer = layers.MultiHeadAttention(
    num_heads=3,
    key_dim=8,
    use_bias=False,
)

# ==================================================
# Line: 532

model = models.Model(inputs, outputs)

# ==================================================
# Occurrences: Lines 555-560 (2 instances)

outputs = layers.MultiHeadAttention(
    num_heads=3,
    key_dim=8,
    use_bias=False,
)(inputs["query"], inputs["key"], inputs["value"])

# ==================================================
# Occurrences: Lines 573-580 (6 instances)

x = layers.Input(batch_shape=shape)

# ==================================================
# Occurrences: Lines 629-630 (2 instances)

query = np.random.random((2, 4, 8))

# ==================================================
# Occurrences: Lines 642-643 (2 instances)

query = random.uniform((2, 4, 16))

# ==================================================
# Occurrences: Lines 657-658 (2 instances)

query = random.uniform((2, 4, 16))

# ==================================================
# Line: 682

output_float = layer(query, key, value)

# ==================================================
# Line: 696

output_quantized = layer(query, key, value)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/normalization/spectral_normalization_test.py
# Occurrences: Lines 95-96 (2 instances)

x = np.random.random((4, 8, 8, 3))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/normalization/batch_normalization_test.py
# Occurrences: Lines 112-131 (8 instances)

inference_out = layer(x, training=False)

# ==================================================
# Line: 194

out = layer(x, training=True)

# ==================================================
# Line: 203

out = layer(x, training=True)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/normalization/unit_normalization_test.py
# Line: 47

outputs = layer(inputs)

# ==================================================
# Line: 53

outputs = layer(inputs)

# ==================================================
# Line: 59

outputs = layer(inputs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/discretization_test.py
# Occurrences: Lines 119-121 (2 instances)

ds = tf_data.Dataset.from_tensor_slices(x).batch(1).map(layer)

# ==================================================
# Occurrences: Lines 130-132 (2 instances)

ds = tf_data.Dataset.from_tensor_slices(x).batch(1).map(layer)

# ==================================================
# Occurrences: Lines 138-157 (8 instances)

config = layer.get_config()

# ==================================================
# Occurrences: Lines 163-171 (3 instances)

model = models.Sequential(
    [
        layers.Input((2,)),
        layer,
    ]
)

# ==================================================
# Occurrences: Lines 181-191 (5 instances)

ref_output = layer(ref_input)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/feature_space_test.py
# Occurrences: Lines 99-106 (3 instances)

out = fs(data)

# ==================================================
# Line: 115

self._get_train_data_dict(as_tensors=True, include_strings=False)

# ==================================================
# Line: 228

out = fs(data)

# ==================================================
# Occurrences: Lines 234-236 (2 instances)

data = self._get_train_data_dict(as_tensors=True)

# ==================================================
# Line: 245

out = fs(self._get_train_data_dict(as_tensors=True))

# ==================================================
# Line: 356

fs.adapt(self._get_train_data_dict(as_dataset=True))

# ==================================================
# Line: 365

ds = self._get_train_data_dict(as_dataset=True)

# ==================================================
# Line: 383

self._get_train_data_dict(as_dataset=True, include_strings=False)

# ==================================================
# Occurrences: Lines 389-404 (8 instances)

ds = self._get_train_data_dict(
    as_labeled_dataset=True, include_strings=False
)

# ==================================================
# Line: 556

self._get_train_data_dict(as_dataset=True, include_strings=False)

# ==================================================
# Occurrences: Lines 564-568 (2 instances)

ref_out = fs(data)

# ==================================================
# Line: 575

out = fs(data)

# ==================================================
# Occurrences: Lines 581-587 (3 instances)

ds = self._get_train_data_dict(as_dataset=True, include_strings=False)

# ==================================================
# Occurrences: Lines 625-639 (2 instances)

fs = feature_space.FeatureSpace(
    features={
        "f1": "integer_categorical",
        "f2": "integer_categorical",
    }
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/index_lookup_test.py
# Line: 29

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Line: 38

output = layer(input_data)

# ==================================================
# Line: 57

output = layer(input_data)

# ==================================================
# Line: 74

output = layer(input_data)

# ==================================================
# Line: 80

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Line: 89

output = layer(input_data)

# ==================================================
# Line: 95

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Line: 104

output = layer(input_data)

# ==================================================
# Line: 120

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Line: 127

output = layer(input_data)

# ==================================================
# Line: 144

output = layer(input_data)

# ==================================================
# Line: 159

output = layer(input_data)

# ==================================================
# Line: 165

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Line: 172

output = layer(input_data)

# ==================================================
# Line: 178

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Line: 185

output = layer(input_data)

# ==================================================
# Occurrences: Lines 246-271 (11 instances)

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Occurrences: Lines 277-280 (3 instances)

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Occurrences: Lines 299-301 (2 instances)

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Occurrences: Lines 317-322 (2 instances)

layer = layers.IndexLookup(**kwargs)

# ==================================================
# Occurrences: Lines 372-400 (12 instances)

layer = layers.IndexLookup(**kwargs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/pipeline_test.py
# Occurrences: Lines 49-50 (2 instances)

x = np.array([0])

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/index_lookup.py
# Occurrences: Lines 259-270 (2 instances)

self.token_counts = tf.lookup.experimental.MutableHashTable(
    key_dtype=vocabulary_dtype,
    value_dtype="int64",
    default_value=0,
)

# ==================================================
# Occurrences: Lines 591-595 (2 instances)

data = tf.expand_dims(data, 0)

# ==================================================
# Line: 627

self.idf_weights_const = self.idf_weights.value()

# ==================================================
# Line: 679

self.idf_weights_const = self.idf_weights.value()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/stft_spectrogram_test.py
# Occurrences: Lines 325-335 (6 instances)

y_true, y = self._calc_spectrograms(x, **init_args)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/hashing_test.py
# Line: 37

output = layer(inp)

# ==================================================
# Line: 43

output = layer(inp)

# ==================================================
# Line: 49

output = layer(inp)

# ==================================================
# Line: 55

output = layer(inp)

# ==================================================
# Occurrences: Lines 112-117 (2 instances)

output = layer(inp)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/normalization_test.py
# Occurrences: Lines 65-67 (2 instances)

data = backend.convert_to_tensor(x)

# ==================================================
# Occurrences: Lines 74-75 (2 instances)

output = layer(x)

# ==================================================
# Occurrences: Lines 84-92 (4 instances)

data = backend.convert_to_tensor(x)

# ==================================================
# Line: 149

x = np.random.random((32, 3))

# ==================================================
# Line: 163

np.random.random((32, 3)),

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/text_vectorization_test.py
# Occurrences: Lines 82-86 (2 instances)

output = model(input_data)

# ==================================================
# Occurrences: Lines 98-99 (2 instances)

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# Occurrences: Lines 109-110 (2 instances)

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/tf_data_layer.py
# Line: 43

outputs = super().__call__(inputs, **kwargs)

# ==================================================
# Line: 49

return super().__call__(inputs, **kwargs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/integer_lookup_test.py
# Line: 31

output = layer(single_sample_input_data)

# ==================================================
# Line: 43

output = layer(single_sample_input_data)

# ==================================================
# Line: 54

output = layer(single_sample_input_data)

# ==================================================
# Line: 63

output = layer(single_sample_input_data)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/category_encoding_test.py
# Occurrences: Lines 132-135 (2 instances)

layer = layers.CategoryEncoding(
    num_tokens=num_tokens, output_mode="multi_hot", sparse=sparse
)

# ==================================================
# Occurrences: Lines 150-154 (2 instances)

layer = layers.CategoryEncoding(
    num_tokens=num_tokens, output_mode="multi_hot", sparse=sparse
)

# ==================================================
# Occurrences: Lines 173-176 (2 instances)

layer = layers.CategoryEncoding(
    num_tokens=num_tokens, output_mode="one_hot", sparse=sparse
)

# ==================================================
# Occurrences: Lines 190-194 (2 instances)

layer = layers.CategoryEncoding(
    num_tokens=num_tokens, output_mode="one_hot", sparse=sparse
)

# ==================================================
# Occurrences: Lines 200-213 (4 instances)

layer = layers.CategoryEncoding(
    num_tokens=num_tokens, output_mode="one_hot", sparse=sparse
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/stft_spectrogram.py
# Line: 241

outputs = ops.reshape(
    outputs,
    [batch_size, channels * freq_channels, time_seq],
)

# ==================================================
# Occurrences: Lines 252-264 (3 instances)

outputs = ops.reshape(
    outputs,
    [batch_size, channels * freq_channels, time_seq],
)

# ==================================================
# Occurrences: Lines 276-287 (4 instances)

_, time_seq, freq_channels = ops.shape(outputs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/feature_space.py
# Line: 592

feature = encoder(feature)

# ==================================================
# Line: 655

feature = encoder(feature)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_flip.py
# Line: 105

x1, x2, x3, x4 = self.backend.numpy.split(boxes, 4, axis=-1)

# ==================================================
# Line: 112

x1, x2, x3, x4 = self.backend.numpy.split(boxes, 4, axis=-1)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_erasing_test.py
# Occurrences: Lines 41-42 (2 instances)

inputs = np.random.randint(0, 255, size=(224, 224, 3))

# ==================================================
# Occurrences: Lines 48-49 (2 instances)

inputs = np.random.randint(0, 255, size=(224, 224, 3))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_flip_test.py
# Occurrences: Lines 138-149 (4 instances)

layer = layers.RandomFlip(
    "vertical", data_format="channels_last", seed=42
)

# ==================================================
# Occurrences: Lines 168-169 (2 instances)

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/auto_contrast_test.py
# Occurrences: Lines 24-25 (2 instances)

img = np.expand_dims(img, axis=-1)

# ==================================================
# Occurrences: Lines 36-37 (2 instances)

img = np.expand_dims(img, axis=-1)

# ==================================================
# Occurrences: Lines 74-75 (2 instances)

img = np.expand_dims(img, axis=-1)

# ==================================================
# Occurrences: Lines 86-87 (2 instances)

img = np.expand_dims(img, axis=-1)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/aug_mix.py
# Line: 213

augmentation_layer = getattr(self, layer_name)

# ==================================================
# Line: 235

augmentation_layer = getattr(self, layer_name)

# ==================================================
# Line: 261

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# Line: 289

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_zoom_test.py
# Occurrences: Lines 225-226 (2 instances)

data_format = backend.config.image_data_format()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_color_degeneration.py
# Line: 93

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# Line: 104

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_shear_test.py
# Occurrences: Lines 156-157 (2 instances)

data_format = backend.config.image_data_format()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_crop.py
# Line: 126

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# Line: 178

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/center_crop.py
# Line: 119

bounding_boxes = _get_clipped_bbox(
    bounding_boxes, h_end, h_start, w_end, w_start
)

# ==================================================
# Line: 140

bounding_boxes = _get_clipped_bbox(
    bounding_boxes, h_end, h_start, w_end, w_start
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_color_jitter_test.py
# Occurrences: Lines 56-59 (2 instances)

output = backend.convert_to_numpy(layer(inputs))

# ==================================================
# Occurrences: Lines 76-79 (2 instances)

output = layer(inputs)

# ==================================================
# Occurrences: Lines 94-97 (2 instances)

output = layer(inputs)

# ==================================================
# Occurrences: Lines 112-115 (2 instances)

output = layer(inputs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_hue.py
# Occurrences: Lines 96-96 (2 instances)

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# Occurrences: Lines 102-103 (4 instances)

adjust_factors = self.backend.numpy.expand_dims(adjust_factors, -1)

# ==================================================
# Occurrences: Lines 109-114 (4 instances)

h_channel = self.backend.numpy.where(
    h_channel > 1.0, h_channel - 1.0, h_channel
)

# ==================================================
# Occurrences: Lines 120-125 (4 instances)

h_channel = self.backend.numpy.where(
    h_channel > 1.0, h_channel - 1.0, h_channel
)

# ==================================================
# Occurrences: Lines 136-136 (2 instances)

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_elastic_transform_test.py
# Occurrences: Lines 44-45 (2 instances)

inputs = np.random.randint(0, 255, size=(224, 224, 3))

# ==================================================
# Occurrences: Lines 51-52 (2 instances)

inputs = np.random.randint(0, 255, size=(224, 224, 3))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_erasing.py
# Line: 277

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# Line: 294

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/bounding_box.py
# Occurrences: Lines 128-148 (10 instances)

x1, y1, x2, y2 = ops.numpy.split(boxes, 4, axis=-1)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/cut_mix_test.py
# Line: 40

inputs = np.asarray([image1, image2])

# ==================================================
# Line: 50

inputs = np.asarray([image1, image2])

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_brightness_test.py
# Occurrences: Lines 39-40 (2 instances)

inputs = np.random.randint(0, 255, size=(224, 224, 3))

# ==================================================
# Occurrences: Lines 49-50 (2 instances)

inputs = np.random.randint(0, 255, size=(224, 224, 3))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/rand_augment.py
# Line: 169

augmentation_layer = getattr(self, layer_name)

# ==================================================
# Line: 175

augmentation_layer = getattr(self, layer_name)

# ==================================================
# Line: 188

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# Line: 196

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/mix_up.py
# Occurrences: Lines 47-52 (2 instances)

images_shape = self.backend.shape(images)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/center_crop_test.py
# Line: 82

out = layers.CenterCrop(
    size[0],
    size[1],
    data_format=data_format,
)(img)

# ==================================================
# Line: 95

ref_out = self.np_center_crop(img, size[0], size[1])

# ==================================================
# Line: 103

out = layers.CenterCrop(
    size[0],
    size[1],
    data_format=data_format,
)(img)

# ==================================================
# Line: 119

ref_out = self.np_center_crop(
    img,
    size[0],
    size[1],
)

# ==================================================
# Occurrences: Lines 139-146 (2 instances)

out = layers.CenterCrop(
    size[0],
    size[1],
    data_format=data_format,
)(img)

# ==================================================
# Occurrences: Lines 154-161 (2 instances)

out = layers.CenterCrop(
    size[0],
    size[1],
    data_format=data_format,
)(img)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py
# Occurrences: Lines 364-368 (2 instances)

inputs_shape = self.backend.shape(inputs)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/mix_up_test.py
# Line: 38

output = mix_up_layer.transform_images(
    image, transformation=transformation
)[0]

# ==================================================
# Line: 46

output = mix_up_layer.transform_images(
    image, transformation=transformation
)

# ==================================================
# Line: 56

output = mix_up_layer.transform_images(
    image, transformation=transformation
)[0]

# ==================================================
# Line: 64

output = mix_up_layer.transform_images(
    image, transformation=transformation
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_translation.py
# Occurrences: Lines 287-290 (2 instances)

images_shape = self.backend.shape(images)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py
# Occurrences: Lines 222-228 (4 instances)

bounding_box[key] = self.backend.numpy.expand_dims(
    bounding_box[key], axis=0
)

# ==================================================
# Occurrences: Lines 235-241 (4 instances)

bounding_boxes[key] = self.backend.numpy.squeeze(
    bounding_boxes[key], axis=0
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_saturation.py
# Line: 118

s_channel = self.backend.numpy.clip(
    s_channel, self.value_range[0], self.value_range[1]
)

# ==================================================
# Line: 128

s_channel = self.backend.numpy.clip(
    s_channel, self.value_range[0], self.value_range[1]
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_translation_test.py
# Occurrences: Lines 399-400 (2 instances)

data_format = backend.config.image_data_format()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_sharpness.py
# Line: 100

images = self.backend.numpy.swapaxes(images, -3, -1)

# ==================================================
# Line: 139

images = self.backend.numpy.swapaxes(images, -3, -1)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/equalization.py
# Line: 181

equalized = self._equalize_channel(
    channel, self.value_range
)

# ==================================================
# Line: 190

equalized = self._equalize_channel(
    channel, self.value_range
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_perspective_test.py
# Occurrences: Lines 218-219 (2 instances)

data_format = backend.config.image_data_format()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_grayscale_test.py
# Occurrences: Lines 43-44 (2 instances)

layer = layers.RandomGrayscale(factor=1.0, data_format=data_format)

# ==================================================
# Occurrences: Lines 51-52 (2 instances)

layer = layers.RandomGrayscale(factor=1.0, data_format=data_format)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_color_jitter.py
# Line: 132

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# Line: 178

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_elastic_transform.py
# Line: 207

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# Line: 249

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_perspective.py
# Occurrences: Lines 161-164 (2 instances)

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/cut_mix.py
# Line: 176

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# Line: 186

images = self.backend.cast(images, self.compute_dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/normalization.py
# Occurrences: Lines 247-248 (2 instances)

total_mean = ops.zeros(self._mean_and_var_shape)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/text_vectorization.py
# Line: 588

shape = lookup_data.shape.as_list()

# ==================================================
# Line: 612

static_padded_shape = lookup_data.shape.as_list()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/discretization.py
# Occurrences: Lines 265-268 (2 instances)

discretization = cls(**config)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/hashed_crossing_test.py
# Occurrences: Lines 55-57 (3 instances)

feat1 = np.array(["A", "B", "A", "B", "A"])

# ==================================================
# Occurrences: Lines 63-65 (3 instances)

feat1 = np.array(["A", "B", "A", "B", "A"])

# ==================================================
# Occurrences: Lines 120-139 (4 instances)

output_dtype = backend.standardize_dtype(
    layer((input_1, input_2)).dtype
)

# ==================================================
# Occurrences: Lines 177-182 (3 instances)

outputs = layer((feat1, feat2))

# ==================================================
# Occurrences: Lines 193-199 (4 instances)

layer((feat1, feat2)),

# ==================================================
# Line: 207

original_outputs = layer((feat1, feat2))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/reshaping/cropping2d.py
# Occurrences: Lines 93-96 (2 instances)

and sum(self.cropping[0]) >= input_shape[2]

# ==================================================
# Occurrences: Lines 120-123 (2 instances)

and sum(self.cropping[0]) >= input_shape[1]

# ==================================================
# Occurrences: Lines 149-152 (2 instances)

and sum(self.cropping[0]) >= inputs.shape[2]

# ==================================================
# Occurrences: Lines 186-189 (2 instances)

and sum(self.cropping[0]) >= inputs.shape[1]

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/reshaping/zero_padding1d_test.py
# Occurrences: Lines 41-49 (2 instances)

padded = layers.ZeroPadding1D((1, 2), data_format="channels_last")(
    input_layer
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/reshaping/cropping3d_test.py
# Occurrences: Lines 187-190 (2 instances)

input_layer = layers.Input(batch_shape=shape)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/layer.py
# Occurrences: Lines 923-937 (6 instances)

new_scope = backend.AutocastScope(None)

# ==================================================
# Occurrences: Lines 999-1000 (2 instances)

elif call_context.get_value(arg_name) is not None:

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/layer_test.py
# Line: 52

layer.compute_output_spec(backend.KerasTensor((2, 3))).shape, (2, 3)

# ==================================================
# Line: 64

out = layer.compute_output_spec(backend.KerasTensor((2, 3)))

# ==================================================
# Line: 79

out = layer.compute_output_spec(backend.KerasTensor((2, 3)))

# ==================================================
# Line: 94

out = layer.compute_output_spec(backend.KerasTensor((2, 3)))

# ==================================================
# Line: 113

out = layer.compute_output_spec(backend.KerasTensor((2, 3)))

# ==================================================
# Line: 138

out = layer.compute_output_spec(backend.KerasTensor((2, 3)))

# ==================================================
# Occurrences: Lines 203-208 (2 instances)

output_no_remat = layer(input_tensor)

# ==================================================
# Occurrences: Lines 395-399 (6 instances)

self.dense1 = layers.Dense(units)

# ==================================================
# Line: 445

self.metric = metrics.MeanSquaredError(name="my_metric")

# ==================================================
# Line: 457

self.metric = metrics.MeanSquaredError(name="my_metric")

# ==================================================
# Line: 493

self.dense1 = layers.Dense(units)

# ==================================================
# Occurrences: Lines 505-506 (4 instances)

self.dense1 = layers.Dense(units)

# ==================================================
# Line: 576

self.dp = layers.Dropout(0.9)

# ==================================================
# Occurrences: Lines 582-585 (3 instances)

x = np.ones((4, 4))

# ==================================================
# Occurrences: Lines 598-601 (3 instances)

x = np.ones((4, 4))

# ==================================================
# Line: 610

self.dp = layers.Dropout(0.9)

# ==================================================
# Line: 616

x = np.ones((4, 4))

# ==================================================
# Occurrences: Lines 626-636 (3 instances)

x = np.ones((4, 4))

# ==================================================
# Line: 647

y = layer(x)

# ==================================================
# Line: 653

y = layer(x)

# ==================================================
# Line: 687

self.v = self.add_weight(
    shape=(),
    initializer="ones",
    trainable=True,
)

# ==================================================
# Line: 721

self.v = self.add_weight(
    shape=(),
    initializer="ones",
    trainable=True,
)

# ==================================================
# Occurrences: Lines 788-793 (5 instances)

x = backend.numpy.ones((4, 4))

# ==================================================
# Occurrences: Lines 808-818 (8 instances)

x1 = backend.numpy.ones((4, 4))

# ==================================================
# Occurrences: Lines 848-855 (6 instances)

x1_1 = backend.numpy.ones((4, 4))

# ==================================================
# Occurrences: Lines 871-874 (3 instances)

x = backend.numpy.ones((4, 4))

# ==================================================
# Occurrences: Lines 950-959 (2 instances)

self.w1 = self.add_weight(
    shape=(),
    initializer="ones",
    trainable=True,
)

# ==================================================
# Occurrences: Lines 967-976 (2 instances)

self.w1 = self.add_weight(
    shape=(),
    initializer="ones",
    trainable=True,
)

# ==================================================
# Occurrences: Lines 1170-1173 (2 instances)

self.w = self._untrack_variable(self.w)

# ==================================================
# Line: 1262

config = layer.get_config()

# ==================================================
# Line: 1272

config = layer.get_config()

# ==================================================
# Line: 1282

config = layer.get_config()

# ==================================================
# Line: 1290

config = layer.get_config()

# ==================================================
# Line: 1302

self.var = self.add_weight(
    shape=(1,),
    name="inner",
)

# ==================================================
# Line: 1311

self.var = self.add_weight(
    shape=(1,),
    name="inner",
)

# ==================================================
# Line: 1344

self.var = self.add_weight(
    shape=(1,),
    name="inner",
)

# ==================================================
# Line: 1357

self.var = self.add_weight(
    shape=(1,),
    name="inner",
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/embedding_test.py
# Line: 141

layer = layers.Embedding(10, 16)

# ==================================================
# Occurrences: Lines 153-154 (2 instances)

init_lora_a_embeddings_value = layer.lora_embeddings_a.numpy()

# ==================================================
# Occurrences: Lines 165-166 (2 instances)

final_lora_a_embeddings_value = layer.lora_embeddings_a.numpy()

# ==================================================
# Line: 194

layers.Embedding(10, 16),

# ==================================================
# Occurrences: Lines 271-274 (2 instances)

layer = layers.Embedding(10, 16)

# ==================================================
# Line: 287

y_quantized = layer(x)

# ==================================================
# Occurrences: Lines 307-311 (2 instances)

layer = layers.Embedding(10, 16)

# ==================================================
# Line: 431

layer = layers.Embedding(10, 16)

# ==================================================
# Occurrences: Lines 441-442 (2 instances)

init_lora_a_embeddings_value = layer.lora_embeddings_a.numpy()

# ==================================================
# Occurrences: Lines 449-450 (2 instances)

final_lora_a_embeddings_value = layer.lora_embeddings_a.numpy()

# ==================================================
# Line: 475

[layers.Input((3,), dtype="int32"), layers.Embedding(10, 16)]

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/dense_test.py
# Line: 69

inputs = np.array(
    [[-1.0, 2.0]],
)

# ==================================================
# Line: 82

inputs = np.array(
    [[-1.0, 2.0]],
)

# ==================================================
# Line: 133

outputs = layer(inputs)

# ==================================================
# Line: 149

outputs = layer(inputs)

# ==================================================
# Line: 210

layer = layers.Dense(units=16)

# ==================================================
# Occurrences: Lines 222-223 (2 instances)

init_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Occurrences: Lines 234-235 (2 instances)

final_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Line: 262

layers.Dense(units=16),

# ==================================================
# Occurrences: Lines 363-366 (3 instances)

layer = layers.Dense(units=16)

# ==================================================
# Line: 377

y_quantized = layer(x)

# ==================================================
# Occurrences: Lines 397-402 (3 instances)

layer = layers.Dense(units=16)

# ==================================================
# Line: 532

layer = layers.Dense(**config)

# ==================================================
# Occurrences: Lines 542-543 (2 instances)

init_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Occurrences: Lines 550-551 (2 instances)

final_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Line: 575

new_model = models.Sequential([layers.Dense(**config)])

# ==================================================
# Line: 632

loss = loss_fn(x, dy)

# ==================================================
# Line: 672

loss = loss_fn(x, dy)

# ==================================================
# Line: 727

layer = layers.Dense(**config)

# ==================================================
# Line: 753

new_model = models.Sequential([layers.Dense(**config)])

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/lambda_layer_test.py
# Line: 76

output = layer(2 * np.ones((2, 3)))

# ==================================================
# Occurrences: Lines 82-87 (2 instances)

output = layer(2 * np.ones((2, 3)))

# ==================================================
# Line: 93

output = layer(2 * np.ones((2, 3)))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/einsum_dense_test.py
# Line: 292

layer = layers.EinsumDense(
    equation="ab,bcd->acd",
    output_shape=(8, 32),
    bias_axes=None,
)

# ==================================================
# Occurrences: Lines 308-309 (2 instances)

init_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Occurrences: Lines 320-321 (2 instances)

final_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Line: 348

layers.EinsumDense(
    equation="ab,bcd->acd",
    output_shape=(8, 32),
    bias_axes=None,
),

# ==================================================
# Occurrences: Lines 429-436 (3 instances)

layer = layers.EinsumDense(
    equation="ab,bcd->acd",
    output_shape=(8, 32),
    bias_axes="d",
)

# ==================================================
# Line: 447

y_quantized = layer(x)

# ==================================================
# Occurrences: Lines 467-476 (3 instances)

layer = layers.EinsumDense(
    equation="ab,bcd->acd",
    output_shape=(8, 32),
    bias_axes="d",
)

# ==================================================
# Occurrences: Lines 522-525 (2 instances)

y_float = layer(x)

# ==================================================
# Line: 682

layer = layers.EinsumDense(**config)

# ==================================================
# Occurrences: Lines 692-693 (2 instances)

init_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Occurrences: Lines 700-701 (2 instances)

final_lora_a_kernel_value = layer.lora_kernel_a.numpy()

# ==================================================
# Line: 725

new_model = models.Sequential([layers.EinsumDense(**config)])

# ==================================================
# Line: 785

loss = loss_fn(x, dy)

# ==================================================
# Line: 825

loss = loss_fn(x, dy)

# ==================================================
# Line: 884

layer = layers.EinsumDense(**config)

# ==================================================
# Line: 910

new_model = models.Sequential([layers.EinsumDense(**config)])

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/einsum_dense.py
# Occurrences: Lines 873-875 (6 instances)

input_spec = split_string.group(1)

# ==================================================
# Occurrences: Lines 883-892 (8 instances)

input_spec = split_string.group(1)

# ==================================================
# Occurrences: Lines 904-913 (8 instances)

input_spec = split_string.group(1)

# ==================================================
# Occurrences: Lines 931-935 (2 instances)

index = output_spec.find(label)

# ==================================================
# Occurrences: Lines 943-944 (2 instances)

index_input = input_spec.find(label)

# ==================================================
# Occurrences: Lines 954-955 (2 instances)

index_input = input_spec.find(label)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/lambda_layer.py
# Occurrences: Lines 192-201 (2 instances)

fn = python_utils.func_load(
    inner_config["code"],
    defaults=inner_config["defaults"],
    closure=inner_config["closure"],
)

# ==================================================
# Occurrences: Lines 211-220 (2 instances)

fn = python_utils.func_load(
    inner_config["code"],
    defaults=inner_config["defaults"],
    closure=inner_config["closure"],
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/masking_test.py
# Line: 39

layer = layers.Masking(mask_value=0.0)

# ==================================================
# Line: 59

layers.Masking(mask_value=0.0),

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/quantizers/quantizers.py
# Line: 77

original_dtype = backend.standardize_dtype(inputs.dtype)

# ==================================================
# Line: 96

scale = ops.cast(scale, backend.standardize_dtype(inputs.dtype))

# ==================================================
# Line: 253

return ops.cast(outputs, dtype=dtype)

# ==================================================
# Line: 267

outputs = ops.cast(outputs, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/quantizers/quantizers_test.py
# Line: 29

quantized_values, scale = quantizer(values)

# ==================================================
# Occurrences: Lines 51-55 (2 instances)

quantized_values, scale = quantizer(values)

# ==================================================
# Line: 433

result = quantizers.fake_quant_with_min_max_vars(
    inputs,
    input_mins,
    input_maxs,
    num_bits,
    narrow_range,
    axis,
)

# ==================================================
# Line: 455

result = quantizers.fake_quant_with_min_max_vars(
    inputs, input_mins, input_maxs, num_bits, narrow_range, axis
)

# ==================================================
