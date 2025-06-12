# no-self-use snippets for keras

# File: /root/ecooptimizer/keras/integration_tests/model_visualization_test.py
# Line: 13

def call(self, x):
    return x



# ==================================================
# Occurrences: Lines 267-271 (2 instances)

def call(self, x):
    return list(keras.ops.split(x, 2, axis=1))


# ==================================================
# File: /root/ecooptimizer/keras/integration_tests/basic_full_flow.py
# Line: 50

def test_basic_fit_no_training(self):
    model = MyModel(hidden_dim=2, output_dim=1)
    x = np.random.random((128, 4))
    model.predict(x)
    model(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/backup_and_restore_test.py
# Line: 44

def make_model(self):
    model = Sequential(
        [
            layers.Input((3,)),
            CanaryLayer(),
            layers.Dense(1),
        ]
    )
    model.compile(
        loss="mse",
        optimizer="sgd",
        metrics=["mse"],
    )
    return model


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/tensorboard_test.py
# Line: 135

def _get_model(self, compile_model=True):
    model = models.Sequential(
        [
            layers.Input((10, 10, 1)),
            layers.Flatten(),
            layers.Dense(1),
        ]
    )
    if compile_model:
        model.compile("sgd", "mse")
    return model


# ==================================================
# Line: 544

def _strip_to_only_final_name(self, summaries):
    """Removes all leading names in a summary

    Args:
        summaries: A `set` of `_ObservedSummary` values.

    Returns:
        A new `set` of `_ObservedSummary` values striped of all
        name except for the terminal one.

    """
    result = set()
    for s in summaries:
        if "/" not in s.tag:
            result.add(s)
        else:
            new_tag = s.tag.split("/")[-1]
            result.add(s._replace(tag=new_tag))
    return result


# ==================================================
# Line: 564

def _strip_layer_names(self, summaries, model_type):
    """Deduplicate summary names modulo layer prefix.

    This removes the first slash-component of each tag name: for
    instance, "foo/bar/baz" becomes "bar/baz".

    Args:
        summaries: A `set` of `_ObservedSummary` values.
        model_type: The model type currently being tested.

    Returns:
        A new `set` of `_ObservedSummary` values with layer prefixes
        removed.
    """
    result = set()
    for s in summaries:
        if "/" not in s.tag:
            raise ValueError(f"tag has no layer name: {s.tag!r}")
        start_from = 2 if "subclass" in model_type else 1
        new_tag = "/".join(s.tag.split("/")[start_from:])
        result.add(s._replace(tag=new_tag))
    return result


# ==================================================
# Line: 587

def _strip_variable_names(self, summaries):
    """Remove `variable_n` from summary tag

    `variable_n` tag names are added with random numbers. Removing them
    ensures deterministic tag names.

    Args:
        summaries: A `set` of `_ObservedSummary` values.

    Returns:
        A new `set` of `_ObservedSummary` values with layer prefixes
        removed.
    """
    result = set()
    for s in summaries:
        if "/" not in s.tag:
            result.add(s)
        else:
            split_tag = s.tag.split("/")
            if "variable" in split_tag[0]:
                result.add(s._replace(tag=split_tag[-1]))
            else:
                result.add(s)
    return result


# ==================================================
# Line: 654

def _count_xplane_file(self, logdir):
    profile_dir = os.path.join(logdir, "plugins", "profile")
    count = 0
    for dirpath, dirnames, filenames in os.walk(profile_dir):
        del dirpath  # unused
        del dirnames  # unused
        for filename in filenames:
            if filename.endswith(".xplane.pb"):
                count += 1
    return count


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/early_stopping_test.py
# Line: 130

def test_early_stopping_with_baseline(self):
    baseline = 0.6
    x_train = np.random.random((10, 5))
    y_train = np.random.random((10, 1))
    model = models.Sequential(
        (
            layers.Dense(1, activation="relu"),
            layers.Dense(1, activation="relu"),
        )
    )
    model.compile(optimizer="sgd", loss="mae", metrics=["mse"])

    patience = 3
    stopper = callbacks.EarlyStopping(
        monitor="mse", patience=patience, baseline=baseline
    )
    hist = model.fit(
        x_train, y_train, callbacks=[stopper], verbose=0, epochs=20
    )
    assert len(hist.epoch) >= patience


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/model_checkpoint.py
# Occurrences: Lines 325-329 (2 instances)

def _checkpoint_exists(self, filepath):
    """Returns whether the checkpoint `filepath` refers to exists."""
    return file_utils.exists(filepath)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/swap_ema_weights_test.py
# Line: 34

def _get_compiled_model(
    self, use_ema=True, jit_compile=True, loss_scale=False

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/losses/losses_test.py
# Line: 513

def l2_norm(self, x, axis):
    epsilon = 1e-12
    square_sum = np.sum(np.square(x), axis=axis, keepdims=True)
    x_inv_norm = 1 / np.sqrt(np.maximum(square_sum, epsilon))
    return np.multiply(x, x_inv_norm)


# ==================================================
# Line: 601

def huber_loss(self, y_true, y_pred, delta=1.0):
    error = y_pred - y_true
    abs_error = np.abs(error)

    quadratic = np.minimum(abs_error, delta)
    linear = np.subtract(abs_error, quadratic)
    return np.add(
        np.multiply(0.5, np.multiply(quadratic, quadratic)),
        np.multiply(delta, linear),
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/saving_api_test.py
# Line: 17

def get_model(self):
    return Sequential(
        [
            layers.Dense(5, input_shape=(3,)),
            layers.Softmax(),
        ]
    )


# ==================================================
# Line: 108

def get_model(self, dtype=None):
    return Sequential(
        [
            layers.Dense(5, input_shape=(3,), dtype=dtype),
            layers.Softmax(),
        ]
    )


# ==================================================
# Line: 196

def get_model(self, dtype=None):
    return Sequential(
        [
            layers.Dense(5, input_shape=(3,), dtype=dtype),
            layers.Softmax(),
        ]
    )


# ==================================================
# Line: 257

def get_model(self):
    return Sequential(
        [
            layers.Dense(5, input_shape=(3,)),
            layers.Softmax(),
        ]
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/saving_lib_test.py
# Line: 57

def two(self):
    return 2



# ==================================================
# Line: 99

def one(self):
    return 1



# ==================================================
# Line: 664

def save_own_variables(self, store):
    raise ValueError


# ==================================================
# Line: 699

def load_own_variables(self, store):
    raise ValueError


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/serialization_lib_test.py
# Line: 59

def roundtrip(self, obj, custom_objects=None, safe_mode=True):
    serialized = serialization_lib.serialize_keras_object(obj)
    json_data = json.dumps(serialized)
    json_data = json.loads(json_data)
    deserialized = serialization_lib.deserialize_keras_object(
        json_data, custom_objects=custom_objects, safe_mode=safe_mode
    )
    reserialized = serialization_lib.serialize_keras_object(deserialized)
    return serialized, deserialized, reserialized


# ==================================================
# Line: 308

def get_config(self):
    return {}


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/trainer_test.py
# Line: 623

def test_fit_with_data_adapter(
    self, dataset_type, dataset_kwargs={}, fit_kwargs={}

# ==================================================
# Line: 828

def test_evaluate_sparse(self, generator_type, mode):
    model = ExampleModel(units=3)
    model.compile(
        optimizer=optimizers.Adagrad(),
        loss=losses.MeanSquaredError(),
        metrics=[metrics.MeanSquaredError()],
        run_eagerly=(mode == "eager"),
        jit_compile=False,
    )
    dataset = sparse_generator(generator_type)
    model.evaluate(dataset)


# ==================================================
# Line: 1928

def test_for_eval_epoch_iterator(self):
    model = ExampleModel(units=3)
    model.compile(
        optimizer="adam", loss="mse", metrics=["mean_absolute_error"]
    )
    x = np.ones((16, 4))
    y = np.zeros((16, 3))
    x_test = np.ones((16, 4))
    y_test = np.zeros((16, 3))
    model.fit(
        x,
        y,
        batch_size=4,
        validation_data=(x_test, y_test),
    )
    assert getattr(model, "_eval_epoch_iterator", None) is None

    # Try model.fit with reshaped validation_data
    # This will throw an exception which is intended
    try:
        model.fit(
            x,
            y,
            batch_size=4,
            validation_data=(
                x_test.reshape((-1, 16, 4)),
                y_test.reshape((-1, 16, 3)),
            ),
        )
    except:
        pass

    # Try model.fit with correct validation_data this should work.
    # After successful training `_eval_epoch_iterator` should be None
    model.fit(
        x,
        y,
        batch_size=4,
        validation_data=(x_test, y_test),
    )
    assert getattr(model, "_eval_epoch_iterator", None) is None


# ==================================================
# Line: 1971

def test_callback_methods_keys(self):
    class CustomCallback(Callback):
        def on_train_begin(self, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == []

        def on_train_end(self, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == [
                "loss",
                "mean_absolute_error",
                "val_loss",
                "val_mean_absolute_error",
            ]

        def on_epoch_begin(self, epoch, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == []

        def on_epoch_end(self, epoch, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == [
                "loss",
                "mean_absolute_error",
                "val_loss",
                "val_mean_absolute_error",
            ]

        def on_test_begin(self, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == []

        def on_test_end(self, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == ["loss", "mean_absolute_error"]

        def on_predict_begin(self, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == []

        def on_predict_end(self, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == []

        def on_train_batch_begin(self, batch, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == []

        def on_train_batch_end(self, batch, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == ["loss", "mean_absolute_error"]

        def on_test_batch_begin(self, batch, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == []

        def on_test_batch_end(self, batch, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == ["loss", "mean_absolute_error"]

        def on_predict_batch_begin(self, batch, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == []

        def on_predict_batch_end(self, batch, logs=None):
            keys = sorted(list(logs.keys()))
            assert keys == ["outputs"]

    model = ExampleModel(units=3)
    model.compile(
        optimizer="adam", loss="mse", metrics=["mean_absolute_error"]
    )
    x = np.ones((16, 4))
    y = np.zeros((16, 3))
    x_test = np.ones((16, 4))
    y_test = np.zeros((16, 3))
    model.fit(
        x,
        y,
        callbacks=[CustomCallback()],
        batch_size=4,
        validation_data=(x_test, y_test),
    )
    model.evaluate(x_test, y_test, batch_size=4)
    model.predict(x_test, batch_size=4)


# ==================================================
# Line: 2076

def get_layer(self):
    class ExampleLayer(keras.Layer):
        def call(self, x):
            return x * 2

    return ExampleLayer


# ==================================================
# Line: 2083

def get_model(self):
    class ExampleModel(keras.Model):
        def call(self, x):
            return x * 2

    return ExampleModel


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/compile_utils.py
# Line: 216

def _build_metrics_set(
    self, metrics, num_outputs, output_names, y_true, y_pred, argument_name

# ==================================================
# Line: 675

def _get_y_pred_output_names(self, y_pred):
    flat_y_pred = tree.flatten(y_pred)
    if all((isinstance(x, KerasTensor) for x in flat_y_pred)):
        output_names = []
        for tensor in flat_y_pred:
            if hasattr(tensor, "_keras_history"):
                output_names.append(tensor._keras_history.operation.name)
            else:
                output_names.append(tensor.name)
    else:
        output_names = [None] * len(flat_y_pred)
    return output_names


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/compile_utils_test.py
# Line: 518

def test_different_container_types(self):
    y1, y2, y3 = np.array([[1]]), np.array([[2]]), np.array([[3]])
    y_true = ([{"a": y1}, {"b": ([y2], y3)}],)
    y_pred = [({"a": y1}, {"b": [(y2,), y3]})]
    loss = "mse"
    compile_loss = CompileLoss(loss=loss, output_names=["a", "b", "c"])
    y_true_symb = tree.map_structure(
        lambda _: backend.KerasTensor((1, 1)), y_true
    )
    y_pred_symb = tree.map_structure(
        lambda _: backend.KerasTensor((1, 1)), y_pred
    )
    compile_loss.build(y_true_symb, y_pred_symb)
    compile_loss(y_true, y_pred)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/epoch_iterator.py
# Line: 88

def _interrupted_warning(self):
    warnings.warn(
        "Your input ran out of data; interrupting training. "
        "Make sure that your dataset or generator can generate "
        "at least `steps_per_epoch * epochs` batches. "
        "You may need to use the `.repeat()` "
        "function when building your dataset.",
        stacklevel=2,
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/array_data_adapter_test.py
# Line: 17

def make_array(self, array_type, shape, dtype):
    x = np.array([[i] * shape[1] for i in range(shape[0])], dtype=dtype)
    if array_type == "np":
        return x
    elif array_type == "tf":
        return tf.constant(x)
    elif array_type == "tf_ragged":
        return tf.RaggedTensor.from_tensor(x)
    elif array_type == "tf_sparse":
        return tf.sparse.from_dense(x)
    elif array_type == "jax":
        return jax.numpy.array(x)
    elif array_type == "jax_sparse":
        return jax_sparse.BCOO.fromdense(x)
    elif array_type == "torch":
        return torch.as_tensor(x)
    elif array_type == "pandas_data_frame":
        return pandas.DataFrame(x)
    elif array_type == "pandas_series":
        return pandas.Series(x[:, 0])
    elif array_type == "scipy_sparse":
        return scipy.sparse.coo_matrix(x)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/py_dataset_adapter_test.py
# Line: 435

def test_iterate_infinite_with_none_num_batches(self):
    py_dataset = ExamplePyDataset(
        np.ones((6, 11), dtype="int32"),
        np.zeros((6, 11), dtype="int32"),
        batch_size=2,
        infinite=True,
    )
    for index, _ in enumerate(py_dataset):
        if index >= 10:
            break


# ==================================================
# Line: 446

def test_iterate_infinite_with_no_len(self):
    class NoLenDataset(py_dataset_adapter.PyDataset):
        def __getitem__(self, idx):
            yield np.ones((2, 11), dtype="int32")

    for index, _ in enumerate(NoLenDataset()):
        if index >= 10:
            break

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/trainer.py
# Line: 389

def _aggregate_additional_loss(self, loss):
    """Aggregates losses from `add_loss`, regularizers and sublayers.

    Args:
        loss: A tensor representing the additional loss to aggregate.

    Returns:
        A tensor representing the summed loss, cast to the `floatx()` if
        necessary.
    """
    if not backend.is_float_dtype(loss.dtype):
        loss = ops.cast(loss, dtype=backend.floatx())
    return ops.sum(loss)


# ==================================================
# Line: 978

def _should_eval(self, epoch, validation_freq):
    epoch = epoch + 1  # one-index the user-facing epoch.
    if isinstance(validation_freq, int):
        return epoch % validation_freq == 0
    elif isinstance(validation_freq, list):
        return epoch in validation_freq
    else:
        raise ValueError(
            "Expected `validation_freq` to be a list or int. "
            f"Received: validation_freq={validation_freq} of the "
            f"type {type(validation_freq)}."
        )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/core_test.py
# Occurrences: Lines 759-761 (2 instances)

def test_cond_raw_bool_compile(self):
    class ExampleLayer(layers.Layer):
        def call(self, x, training=False):
            return ops.cond(training, lambda: x, lambda: x * 2.0)

    model = models.Sequential([ExampleLayer()])
    model.compile(
        optimizer=optimizers.SGD(), loss=losses.MeanSquaredError()
    )
    x = np.ones((2, 4), dtype=np.float32)
    y = np.zeros((2, 4), dtype=np.float32)
    model.evaluate(x, y, batch_size=2)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/nn.py
# Line: 2180

def _check_shape(self, name, shape, expected_shape):
    if shape != expected_shape:
        raise ValueError(
            f"Arguments `{name}` must be a vector of length "
            f"`x.shape[axis]`. Expected: `{expected_shape}`. "
            f"Received: `{shape}."
        )


# ==================================================
# Line: 2268

def _check_shape_first_dim(self, name1, shape1, name2, shape2):
    if shape1[0] != shape2[0]:
        raise ValueError(
            f"Arguments `{name1}` and `{name2}` must have the same "
            "first dimension. "
            f"Received shapes: `{shape1}` and `{shape2}`."
        )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/einops.py
# Occurrences: Lines 90-93 (2 instances)

def call(self, tensor, pattern, **axes_lengths):
    return rearrange(tensor, pattern, **axes_lengths)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/math_test.py
# Line: 1049

def calculate_expected_shape(
    self, input_shape, sequence_length, sequence_stride

# ==================================================
# Line: 1169

def test_fft2_correct_input(self):
    fft2_op = kmath.FFT2()
    real_part = np.random.rand(2, 3, 4)
    imag_part = np.random.rand(2, 3, 4)
    # This should not raise any errors
    fft2_op.compute_output_spec((real_part, imag_part))


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/operation.py
# Line: 316

def _setattr_hook(self, name, value):
    """Can be overridden for per backend post build actions."""
    return name, value


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/image_test.py
# Line: 304

def test_map_coordinates_uint8(self):
    image_uint8 = tf.ones((1, 1, 3), dtype=tf.uint8)
    coordinates = tf.convert_to_tensor([-1.0, 0.0, 0.0])[..., None, None]

    if backend.backend() != "tensorflow":
        pytest.skip("Skipping test because the backend is not TensorFlow.")

    out = kimage.map_coordinates(
        image_uint8, coordinates, order=1, fill_mode="constant"
    )
    assert out.shape == coordinates.shape[1:]


# ==================================================
# Line: 316

def test_map_coordinates_float32(self):
    image_float32 = tf.ones((1, 1, 3), dtype=tf.float32)
    coordinates = tf.convert_to_tensor([-1.0, 0.0, 0.0])[..., None, None]

    if backend.backend() != "tensorflow":
        pytest.skip("Skipping test because the backend is not TensorFlow.")

    out = kimage.map_coordinates(
        image_float32, coordinates, order=1, fill_mode="constant"
    )
    assert out.shape == coordinates.shape[1:]


# ==================================================
# Line: 328

def test_map_coordinates_nearest(self):
    image_uint8 = tf.ones((1, 1, 3), dtype=tf.uint8)
    coordinates = tf.convert_to_tensor([-1.0, 0.0, 0.0])[..., None, None]

    if backend.backend() != "tensorflow":
        pytest.skip("Skipping test because the backend is not TensorFlow.")

    out = kimage.map_coordinates(
        image_uint8, coordinates, order=1, fill_mode="nearest"
    )
    assert out.shape == coordinates.shape[1:]


# ==================================================
# Line: 340

def test_map_coordinates_manual_cast(self):
    image_uint8 = tf.ones((1, 1, 3), dtype=tf.uint8)
    coordinates = tf.convert_to_tensor([-1.0, 0.0, 0.0])[..., None, None]
    image_uint8_casted = tf.cast(image_uint8, dtype=tf.float32)

    if backend.backend() != "tensorflow":
        pytest.skip("Skipping test because the backend is not TensorFlow.")

    out = tf.cast(
        kimage.map_coordinates(
            image_uint8_casted, coordinates, order=1, fill_mode="constant"
        ),
        dtype=tf.uint8,
    )
    assert out.shape == coordinates.shape[1:]


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/numpy.py
# Line: 4701

def _process_pad_width(self, pad_width):
    if isinstance(pad_width, int):
        return ((pad_width, pad_width),)
    if isinstance(pad_width, (tuple, list)) and isinstance(
        pad_width[0], int
    ):
        return (pad_width,)
    first_len = len(pad_width[0])
    for i, pw in enumerate(pad_width):
        if len(pw) != first_len:
            raise ValueError(
                "`pad_width` should be a list of tuples of length "
                f"1 or 2. Received: pad_width={pad_width}"
            )
        if len(pw) == 1:
            pad_width[i] = (pw[0], pw[0])
    return pad_width


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/core.py
# Occurrences: Lines 18-21 (2 instances)

def call(self, f, xs):
    return backend.core.map(f, xs)


# ==================================================
# Line: 91

def compute_output_spec(self, f, init, xs=None, length=None):
    if xs is None:
        n = int(length)
        x = None
    else:
        n = (
            int(length)
            if length is not None
            else tree.flatten(xs)[0].shape[0]
        )
        x = xs[0]

    carry, y = backend.compute_output_spec(f, init, x)
    y = KerasTensor(shape=(n,) + y.shape, dtype=y.dtype, sparse=y.sparse)
    return carry, y



# ==================================================
# Occurrences: Lines 286-289 (2 instances)

def call(self, indices, values, shape):
    return backend.core.scatter(indices, values, shape)


# ==================================================
# Occurrences: Lines 325-328 (2 instances)

def call(self, inputs, indices, updates):
    return backend.core.scatter_update(inputs, indices, updates)


# ==================================================
# Occurrences: Lines 385-388 (2 instances)

def call(self, inputs, start_indices, shape):
    return backend.core.slice(inputs, start_indices, shape)


# ==================================================
# Occurrences: Lines 424-427 (2 instances)

def call(self, inputs, start_indices, updates):
    return backend.core.slice_update(inputs, start_indices, updates)


# ==================================================
# Occurrences: Lines 468-471 (2 instances)

def call(self, index, branches, *operands):
    return backend.core.switch(index, branches, *operands)


# ==================================================
# Line: 533

def compute_output_spec(self, loop_vars):
    return [KerasTensor(v.shape, dtype=v.dtype) for v in loop_vars]



# ==================================================
# Occurrences: Lines 591-594 (2 instances)

def call(self, variable):
    return backend.core.stop_gradient(variable)


# ==================================================
# Line: 637

def compute_output_spec(self, init_val):
    return KerasTensor(init_val.shape, dtype=init_val.dtype)



# ==================================================
# Line: 1010

def call(self, pred, true_fn, false_fn):
    return backend.core.cond(pred, true_fn, false_fn)


# ==================================================
# Line: 1024

def _check_output_spec(self, true_fn_spec, false_fn_spec):
    try:
        tree.assert_same_structure(true_fn_spec, false_fn_spec)
    except:
        return False

    def check_leaf(t_spec, f_spec):
        if t_spec is None or f_spec is None:
            return t_spec is None and f_spec is None
        return t_spec.shape == f_spec.shape and t_spec.dtype == f_spec.dtype

    same = tree.map_structure(check_leaf, true_fn_spec, false_fn_spec)
    return all(tree.flatten(same))



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/functional_test.py
# Line: 64

def test_mutable_state(self):
    inputs = Input(shape=(3,), batch_size=2, name="input")
    x = layers.Dense(5)(inputs)
    outputs = layers.Dense(5)(x)
    model = Functional(inputs, outputs)
    # Allow attaching state to a model that isn't directly part of the DAG.
    # Most useful for functional subclasses.
    model.extra_layer = layers.Dense(5)


# ==================================================
# Line: 318

def test_training_arg(self):
    class Canary(layers.Layer):
        def call(self, x, training=False):
            assert training
            return x

        def compute_output_spec(self, x, training=False):
            return backend.KerasTensor(x.shape, dtype=x.dtype)

    inputs = Input(shape=(3,), batch_size=2)
    outputs = Canary()(inputs)
    model = Functional(inputs, outputs)
    model(np.random.random((2, 3)), training=True)


# ==================================================
# Line: 627

def test_for_functional_in_sequential(self):
    # Test for a v3.4.1 regression.
    if backend.image_data_format() == "channels_first":
        image_size = (3, 100, 100)
    else:
        image_size = (100, 100, 3)
    base_model = applications.mobilenet.MobileNet(
        include_top=False, weights=None
    )
    model = Sequential()
    model.add(layers.Input(shape=image_size))
    model.add(base_model)
    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dense(7, activation="softmax"))
    config = model.get_config()
    model = Sequential.from_config(config)


# ==================================================
# Line: 658

def test_dict_input_to_list_model(self):
    vocabulary_size = 100
    num_tags = 10
    num_departments = 3
    num_samples = 128

    title = layers.Input(shape=(vocabulary_size,), name="title")
    text_body = layers.Input(shape=(vocabulary_size,), name="text_body")
    tags = layers.Input(shape=(num_tags,), name="tags")
    features = layers.Concatenate()([title, text_body, tags])
    features = layers.Dense(64, activation="relu")(features)
    priority = layers.Dense(1, activation="sigmoid", name="priority")(
        features
    )
    department = layers.Dense(
        num_departments, activation="softmax", name="department"
    )(features)
    model = Functional(
        inputs=[title, text_body, tags], outputs=[priority, department]
    )

    title_data = np.random.randint(
        0, 2, size=(num_samples, vocabulary_size)
    )
    text_body_data = np.random.randint(
        0, 2, size=(num_samples, vocabulary_size)
    )
    tags_data = np.random.randint(0, 2, size=(num_samples, num_tags))
    priority_data = np.random.random(size=(num_samples, 1))
    department_data = np.random.randint(
        0, 2, size=(num_samples, num_departments)
    )

    # List style fit
    model.compile(
        optimizer="adam",
        loss=["mean_squared_error", "categorical_crossentropy"],
        metrics=[["mean_absolute_error"], ["accuracy"]],
    )
    model.fit(
        [title_data, text_body_data, tags_data],
        [priority_data, department_data],
        epochs=1,
    )
    model.evaluate(
        [title_data, text_body_data, tags_data],
        [priority_data, department_data],
    )
    priority_preds, department_preds = model.predict(
        [title_data, text_body_data, tags_data]
    )

    # Dict style fit
    model.compile(
        optimizer="adam",
        loss={
            "priority": "mean_squared_error",
            "department": "categorical_crossentropy",
        },
        metrics={
            "priority": ["mean_absolute_error"],
            "department": ["accuracy"],
        },
    )
    model.fit(
        {
            "title": title_data,
            "text_body": text_body_data,
            "tags": tags_data,
        },
        {"priority": priority_data, "department": department_data},
        epochs=1,
    )
    model.evaluate(
        {
            "title": title_data,
            "text_body": text_body_data,
            "tags": tags_data,
        },
        {"priority": priority_data, "department": department_data},
    )
    priority_preds, department_preds = model.predict(
        {
            "title": title_data,
            "text_body": text_body_data,
            "tags": tags_data,
        }
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/cloning_test.py
# Line: 144

def test_input_tensors(self, model_fn):
    ref_input = np.random.random((2, 7, 3))
    model = model_fn()
    model(ref_input)  # Maybe needed to get model inputs if no Input layer
    input_tensor = model.inputs[0]
    new_model = clone_model(model, input_tensors=input_tensor)
    tree.assert_same_structure(model.inputs, new_model.inputs)
    tree.assert_same_structure(model.outputs, new_model.outputs)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/model.py
# Line: 171

def layers(self, _):
    raise AttributeError(
        "`Model.layers` attribute is reserved and should not be used. "
        "Please use another name."
    )


# ==================================================
# Line: 764

def _create_nested_dict(self, variables, value_format):
    flat_dict = {}
    for v in variables:
        if v.path in flat_dict:
            raise ValueError(
                "The following variable path is found twice in the model: "
                f"'{v.path}'. `get_state_tree()` can only be called when "
                "all variable paths are unique. Make sure to give unique "
                "names to your layers (and other objects)."
            )
        if value_format == "backend_tensor":
            flat_dict[v.path] = v.value
        elif value_format == "numpy_array":
            flat_dict[v.path] = v.numpy()
        else:
            raise ValueError(
                "Invalid `value_format` argument. Expected one of "
                "{'numpy_array', 'backend_tensor'}. Received: "
                f"value_format={value_format}"
            )

    nested_dict = {}
    for path, value in flat_dict.items():
        parts = path.split("/")
        current_dict = nested_dict
        for part in parts[:-1]:
            if part not in current_dict:
                current_dict[part] = {}
            current_dict = current_dict[part]
        current_dict[parts[-1]] = value

    return nested_dict


# ==================================================
# Line: 833

def _assign_variable_values(self, variables, path_value_dict):
    for path, value in path_value_dict.items():
        for variable in variables:
            if variable.path == path:
                variable.assign(value)


# ==================================================
# Line: 839

def _flatten_nested_dict(self, nested_dict):
    flat_dict = {}

    def _flatten(current_dict, prefix=""):
        for key, value in current_dict.items():
            if isinstance(value, dict):
                _flatten(value, prefix + key + "/")
            else:
                flat_dict[prefix + key] = value

    _flatten(nested_dict)
    return flat_dict



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/sequential_test.py
# Line: 230

def test_nested_sequential(self):
    # https://github.com/keras-team/keras/issues/20203
    model = Sequential()
    model.add(Input(shape=(16,)))
    Sequential([model])


# ==================================================
# Line: 340

def test_pickleable(self):
    model = Sequential(name="seq")
    model.add(layers.Dense(4))

    result = pickle.loads(pickle.dumps(model))
    assert len(result.layers) == 1


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/audio_dataset_utils_test.py
# Line: 11

def _get_audio_samples(self, count=16, different_sequence_lengths=False):
    sequence_length = 30
    num_channels = 1
    audio_samples = []
    for _ in range(count):
        if different_sequence_lengths:
            random_sequence_length = np.random.randint(
                10, sequence_length + 1
            )
            audio = np.random.random((random_sequence_length, num_channels))
        else:
            audio = np.random.random((sequence_length, num_channels))
        audio_samples.append(tf.audio.encode_wav(audio, 1000))
    return audio_samples


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/jax_layer_test.py
# Line: 77

def forward(self, inputs):
    x = inputs
    x = flax.linen.Conv(features=32, kernel_size=(3, 3))(x)
    x = flax.linen.relu(x)
    x = flax.linen.avg_pool(x, window_shape=(2, 2), strides=(2, 2))
    x = flax.linen.Conv(features=64, kernel_size=(3, 3))(x)
    x = flax.linen.relu(x)
    x = flax.linen.avg_pool(x, window_shape=(2, 2), strides=(2, 2))
    x = x.reshape((x.shape[0], -1))  # flatten
    x = flax.linen.Dense(features=200)(x)
    x = flax.linen.relu(x)
    x = flax.linen.Dense(features=10)(x)
    x = flax.linen.softmax(x)
    return x


# ==================================================
# Line: 92

def get_config(self):
    return {}


# ==================================================
# Line: 102

def my_apply(self, inputs, training):
    x = inputs
    x = flax.linen.Conv(features=32, kernel_size=(3, 3))(x)
    x = flax.linen.relu(x)
    x = flax.linen.avg_pool(x, window_shape=(2, 2), strides=(2, 2))
    x = flax.linen.Conv(features=64, kernel_size=(3, 3))(x)
    x = flax.linen.relu(x)
    x = flax.linen.avg_pool(x, window_shape=(2, 2), strides=(2, 2))
    x = x.reshape((x.shape[0], -1))  # flatten
    x = flax.linen.Dense(features=200)(x)
    x = flax.linen.Dropout(rate=0.3, deterministic=not training)(x)
    x = flax.linen.relu(x)
    x = flax.linen.Dense(features=10)(x)
    x = flax.linen.softmax(x)
    return x


# ==================================================
# Line: 118

def get_config(self):
    return {}


# ==================================================
# Line: 166

def get_config(self):
    return {}


# ==================================================
# Line: 500

def test_with_training_in_call_fn_but_not_init_fn(self):
    def jax_call_fn(params, state, rng, inputs, training):
        return inputs, {}

    def jax_init_fn(rng, inputs):
        return {}, {}

    layer = JaxLayer(jax_call_fn, jax_init_fn)
    layer(np.ones((1,)))


# ==================================================
# Line: 510

def test_with_different_argument_order(self):
    def jax_call_fn(training, inputs, rng, state, params):
        return inputs, {}

    def jax_init_fn(training, inputs, rng):
        return {}, {}

    layer = JaxLayer(jax_call_fn, jax_init_fn)
    layer(np.ones((1,)))


# ==================================================
# Line: 520

def test_with_minimal_arguments(self):
    def jax_call_fn(inputs):
        return inputs

    def jax_init_fn(inputs):
        return {}

    layer = JaxLayer(jax_call_fn, jax_init_fn)
    layer(np.ones((1,)))


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/file_utils_test.py
# Line: 64

def _cleanup(self, base_dir):
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)


# ==================================================
# Line: 454

def _create_tar_file(self, directory):
    """Helper function to create a tar file."""
    text_file_path = os.path.join(directory, "test.txt")
    tar_file_path = os.path.join(directory, "test.tar.gz")
    with open(text_file_path, "w") as text_file:
        text_file.write("Float like a butterfly, sting like a bee.")

    with tarfile.open(tar_file_path, "w:gz") as tar_file:
        tar_file.add(text_file_path, arcname="test.txt")

    return text_file_path, tar_file_path


# ==================================================
# Line: 466

def _create_zip_file(self, directory):
    """Helper function to create a zip file."""
    text_file_path = os.path.join(directory, "test.txt")
    zip_file_path = os.path.join(directory, "test.zip")
    with open(text_file_path, "w") as text_file:
        text_file.write("Float like a butterfly, sting like a bee.")

    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        zip_file.write(text_file_path, arcname="test.txt")

    return text_file_path, zip_file_path


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/jax_layer.py
# Line: 255

def _validate_signature(self, fn, fn_name, allowed, required):
    fn_parameters = inspect.signature(fn).parameters
    for parameter_name in required:
        if parameter_name not in fn_parameters:
            raise ValueError(
                f"Missing required argument in `{fn_name}`: "
                f"`{parameter_name}`"
            )

    parameter_names = []
    for parameter in fn_parameters.values():
        if parameter.name not in allowed:
            raise ValueError(
                f"Unsupported argument in `{fn_name}`: `{parameter.name}`, "
                f"supported arguments are `{'`, `'.join(allowed)}`"
            )
        parameter_names.append(parameter.name)

    return parameter_names


# ==================================================
# Line: 626

def _params_and_state_to_variables(self, params, state):
    if params:
        if state:
            return {**params, **state}
        else:
            return params
    elif state:
        return state
    return {}


# ==================================================
# Line: 636

def _variables_to_params_and_state(self, variables):
    # neither params nor state
    if variables is None:
        return None, None
    # state only
    if "params" not in variables:
        return {}, variables
    # params only
    if len(variables) == 1:
        return variables, {}
    # both, we need to split
    params = {"params": variables["params"]}
    state = {k: v for k, v in variables.items() if k != "params"}
    return params, state


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/image_dataset_utils_test.py
# Line: 13

def _get_images(self, count=16, color_mode="rgb"):
    width = height = 24
    imgs = []
    for _ in range(count):
        if color_mode == "grayscale":
            img = np.random.randint(0, 256, size=(height, width, 1))
        elif color_mode == "rgba":
            img = np.random.randint(0, 256, size=(height, width, 4))
        else:
            img = np.random.randint(0, 256, size=(height, width, 3))
        if backend.config.image_data_format() == "channels_first":
            img = np.transpose(img, (2, 0, 1))
        img = image_utils.array_to_img(img)
        imgs.append(img)
    return imgs


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/progbar.py
# Line: 216

def _format_time(self, time_per_unit, unit_name):
    """format a given duration to display to the user.

    Given the duration, this function formats it in either milliseconds
    or seconds and displays the unit (i.e. ms/step or s/epoch).

    Args:
        time_per_unit: the duration to display
        unit_name: the name of the unit to display

    Returns:
        A string with the correctly formatted duration and units
    """
    formatted = ""
    if time_per_unit >= 1 or time_per_unit == 0:
        formatted += f" {time_per_unit:.0f}s/{unit_name}"
    elif time_per_unit >= 1e-3:
        formatted += f" {time_per_unit * 1000.0:.0f}ms/{unit_name}"
    else:
        formatted += f" {time_per_unit * 1000000.0:.0f}us/{unit_name}"
    return formatted


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/io_utils_test.py
# Line: 18

def test_set_logging_verbosity_valid(self):
    valid_levels = ["FATAL", "ERROR", "WARNING", "INFO", "DEBUG"]
    for level in valid_levels:
        io_utils.set_logging_verbosity(level)


# ==================================================
# Line: 36

def test_print_msg_interactive_with_line_break(self, mock_write):
    io_utils.enable_interactive_logging()
    io_utils.print_msg("Hello", line_break=True)
    mock_write.assert_called_once_with("Hello\n")


# ==================================================
# Line: 42

def test_print_msg_interactive_without_line_break(self, mock_write):
    io_utils.enable_interactive_logging()
    io_utils.print_msg("Hello", line_break=False)
    mock_write.assert_called_once_with("Hello")


# ==================================================
# Line: 48

def test_print_msg_non_interactive(self, mock_logging):
    io_utils.disable_interactive_logging()
    io_utils.print_msg("Hello")
    mock_logging.assert_called_once_with("Hello")


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/confusion_metrics_test.py
# Line: 1113

def test_end_to_end(self):
    # Test for https://github.com/keras-team/keras/issues/718
    model = models.Sequential(
        [
            layers.Input((1,)),
            layers.Dense(1),
        ]
    )
    model.compile(
        optimizer="rmsprop", loss="mse", metrics=[metrics.Precision()]
    )
    model.fit(np.ones((5, 1)), np.ones((5, 1)))



# ==================================================
# Line: 1747

def test_keras_model_compiles(self):
    inputs = layers.Input(shape=(10,), batch_size=1)
    output = layers.Dense(3, activation="sigmoid")(inputs)
    model = models.Model(inputs=inputs, outputs=output)
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=[metrics.AUC(multi_label=True)],
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/regression_metrics_test.py
# Line: 40

def l2_norm(self, x, axis):
    epsilon = 1e-12
    square_sum = np.sum(np.square(x), axis=axis, keepdims=True)
    x_inv_norm = 1 / np.sqrt(np.maximum(square_sum, epsilon))
    return np.multiply(x, x_inv_norm)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/correlation_metrics_test.py
# Line: 11

def _get_data(self):
    # Sample data for testing
    y_true = np.array(
        [[0, 1, 0.5], [1, 1, 0.2], [1, 1, 0.1], [0.1, 0.7, 0.0]],
        dtype="float32",
    )
    y_pred = np.array(
        [[0.1, 0.9, 0.5], [1, 0.9, 0.2], [0.2, 0.8, 0], [0.3, 0.3, 0.9]],
        dtype="float32",
    )

    ccc_expected = np.array(
        [0.97560976, 0.98765432, 0.46511628, -0.46376812]
    )
    # pcc_expected = np.array([1, 0.99339927, 0.69337525, -0.60999428])
    pcc_expected = np.array(
        [pearsonr(yt, yp).statistic for yt, yp in zip(y_true, y_pred)]
    )
    return y_true, y_pred, ccc_expected, pcc_expected


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/reduction_metrics_test.py
# Line: 181

def test_binary_accuracy_with_boolean_inputs(self):
    inp = layers.Input(shape=(1,))
    out = inp > 0.5
    model = models.Model(inputs=inp, outputs=out)

    x = np.random.rand(32, 1)
    y = x > 0.5

    res = model.predict(x)
    metric = metrics.BinaryAccuracy()
    metric.update_state(y, res)
    result = metric.result()
    assert result == 1.0

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/iou_metrics_test.py
# Line: 101

def test_compilation(self):
    m_obj = metrics.MeanIoU(num_classes=2, ignore_class=0)
    model = models.Sequential(
        [
            layers.Dense(2, activation="softmax"),
        ]
    )
    model.compile(optimizer="rmsprop", loss="mse", metrics=[m_obj])
    model.fit(np.array([[1.0, 1.0]]), np.array([[1.0, 0.0]]))



# ==================================================
# Line: 460

def test_user_warning_float_weight(self):
    y_pred = [0, 1, 1, 1]
    y_true = [0, 1, 1, 0]
    m_obj = metrics.MeanIoU(num_classes=3)
    with pytest.warns(Warning, match=r"weight.*float.*int.*casting"):
        m_obj(y_true, y_pred, sample_weight=np.array([0.2, 0.3, 0.4, 0.1]))



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/adafactor.py
# Line: 140

def _rms(self, x):
    return ops.sqrt(ops.mean(ops.square(x)))


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/adam_test.py
# Line: 80

def test_ema(self):
    # TODO: test correctness
    model = keras.Sequential([keras.layers.Dense(10)])
    model.compile(optimizer=Adam(use_ema=True), loss="mse")
    x = keras.ops.zeros((1, 5))
    y = keras.ops.zeros((1, 10))
    model.fit(x, y)


# ==================================================
# Line: 92

def test_clipnorm_indexed_slices(self):
    # https://github.com/keras-team/keras/issues/18985
    model = keras.Sequential(
        [
            keras.layers.Embedding(10, 4),
            keras.layers.Flatten(),
            keras.layers.Dense(2),
        ]
    )
    model.compile(optimizer=Adam(clipnorm=100), loss="mse")
    x = keras.ops.ones((8, 5))
    y = keras.ops.zeros((8, 2))
    model.fit(x, y, verbose=0)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/loss_scale_optimizer.py
# Line: 262

def check_finite(self, grads):
    tensor_grads = [g for g in grads if g is not None]
    finite_grads = [ops.all(ops.isfinite(g)) for g in tensor_grads]
    return ops.all(ops.convert_to_tensor(finite_grads))


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/lion_test.py
# Line: 99

def test_ema(self):
    # TODO: test correctness
    model = keras.Sequential([keras.layers.Dense(10)])
    model.compile(optimizer=Lion(use_ema=True), loss="mse")
    x = keras.ops.zeros((1, 5))
    y = keras.ops.zeros((1, 10))
    model.fit(x, y)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/muon.py
# Line: 234

def transpose_last_axis(self, X):
    shape = ops.shape(X)
    temp_order = list(range(len(shape)))
    temp_order[-2] = temp_order[-1]
    temp_order[-1] = len(shape) - 2
    X = ops.transpose(X, temp_order)
    return X


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/base_optimizer.py
# Line: 207

def _overwrite_variable_with_gradient(self, variable):
    return getattr(variable, "overwrite_with_gradient", False)


# ==================================================
# Line: 230

def _var_key(self, variable):
    # Helper function to get a stable ID and the variable instance mapping.
    return id(variable)


# ==================================================
# Line: 416

def assign(self, variable, value):
    """Assign a value to a variable.

    This should be used in optimizers instead of `variable.assign(value)` to
    support backend specific optimizations.
    Note that the variable can be a model variable or an optimizer variable;
    it can be a backend native variable or a Keras variable.

    Args:
        variable: The variable to update.
        value: The value to add to the variable.
    """
    variable.assign(value)


# ==================================================
# Line: 430

def assign_add(self, variable, value):
    """Add a value to a variable.

    This should be used in optimizers instead of
    `variable.assign_add(value)` to support backend specific optimizations.
    Note that the variable can be a model variable or an optimizer variable;
    it can be a backend native variable or a Keras variable.

    Args:
        variable: The variable to update.
        value: The value to add to the variable.
    """
    variable.assign_add(value)


# ==================================================
# Line: 444

def assign_sub(self, variable, value):
    """Subtract a value from a variable.

    This should be used in optimizers instead of
    `variable.assign_sub(value)` to support backend specific optimizations.
    Note that the variable can be a model variable or an optimizer variable;
    it can be a backend native variable or a Keras variable.

    Args:
        variable: The variable to update.
        value: The value to add to the variable.
    """
    variable.assign_sub(value)


# ==================================================
# Line: 629

def _backend_increment_gradient_accumulators(self, grads, acc_grads):
    new_g_accs = [(g + acc_g) for g, acc_g in zip(grads, acc_grads)]
    for n_g_acc, g_acc in zip(new_g_accs, acc_grads):
        g_acc.assign(n_g_acc)


# ==================================================
# Line: 836

def _filter_empty_gradients(self, grads, vars):
    filtered_grads = list(grads)
    filtered_vars = list(vars)
    missing_grad_vars = []

    # Iterate from right to left for safe popping
    for i in range(len(filtered_grads) - 1, -1, -1):
        if filtered_grads[i] is None:
            filtered_grads.pop(i)
            v = filtered_vars.pop(i)
            try:
                missing_grad_vars.append(v.path)
            except AttributeError:
                # `tf.Variable` doesn't have `path` attr.
                missing_grad_vars.append(v.name)

    if not filtered_grads:
        raise ValueError("No gradients provided for any variable.")
    if missing_grad_vars:
        warnings.warn(
            "Gradients do not exist for variables "
            f"{list(reversed(missing_grad_vars))} when minimizing the loss."
            " If using `model.compile()`, did you forget to provide a "
            "`loss` argument?"
        )
    return filtered_grads, filtered_vars


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/schedules/learning_rate_schedule_test.py
# Line: 302

def np_cosine_decay(self, step, decay_steps, alpha=0.0):
    step = min(step, decay_steps)
    completed_fraction = step / decay_steps
    decay = 0.5 * (1.0 + math.cos(math.pi * completed_fraction))
    return (1.0 - alpha) * decay + alpha


# ==================================================
# Line: 316

def linear_warmup(self, step, warmup_steps, initial_lr, target_lr):
    completed_fraction = step / warmup_steps
    total_delta = target_lr - initial_lr
    return completed_fraction * total_delta


# ==================================================
# Line: 392

def np_cosine_decay_restarts(
    self, step, decay_steps, t_mul=2.0, m_mul=1.0, alpha=0.0

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/saving/serialization.py
# Line: 79

def get(self, unused_object_id):
    return None


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/tree/tree_test.py
# Line: 96

def is_dmtree(self, tree_impl):
    if dmtree.available:
        from keras.src.tree import dmtree_impl

        return tree_impl is dmtree_impl
    return False


# ==================================================
# Line: 1618

def test_assert_same_paths_tf_wrappers(self, t):
    from tensorflow.python.trackable.data_structures import ListWrapper
    from tensorflow.python.trackable.data_structures import _DictWrapper

    t.assert_same_paths(ListWrapper([]), ListWrapper([]))
    t.assert_same_paths(ListWrapper([1]), ListWrapper([10]))
    t.assert_same_paths(ListWrapper([1, 2]), ListWrapper([10, 20]))
    t.assert_same_paths(_DictWrapper(), _DictWrapper())
    t.assert_same_paths(_DictWrapper({"a": 1}), _DictWrapper({"a": 11}))
    t.assert_same_paths(
        _DictWrapper({"b": 2, "a": 1}), _DictWrapper({"a": 11, "b": 12})
    )

    # Tensorflow wrappers are equivalent to the raw structures.
    t.assert_same_paths(ListWrapper([1, 2]), list([10, 20]))
    t.assert_same_paths(list([1, 2]), ListWrapper([10, 20]))
    t.assert_same_paths(_DictWrapper({"b": 2, "a": 1}), {"a": 10, "b": 20})
    t.assert_same_paths({"b": 2, "a": 1}, _DictWrapper({"a": 10, "b": 20}))


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/dtype_policies/dtype_policy.py
# Line: 68

def _parse_name(self, name):
    """Parses a `DTypePolicy` name into a compute and variable dtype.

    Args:
        name: The name of the policy.

    Returns:
        The `(compute_dtype, variable_dtype)` pair.
    """
    if not isinstance(name, str):
        raise TypeError(
            "'name' must be a string, such as 'mixed_float16'. "
            f"Received: name={name} (of type {type(name)})"
        )
    if name == "mixed_float16":
        return "float16", "float32"
    elif name == "mixed_bfloat16":
        return "bfloat16", "float32"
    try:
        dtype = backend.standardize_dtype(name)
        return dtype, dtype
    except ValueError:
        raise ValueError(
            f"Cannot convert '{name}' to a mixed precision "
            "DTypePolicy. Valid policies include 'mixed_float16', "
            "'mixed_bfloat16', and the name of any float dtype such as "
            "'float32'."
        )


# ==================================================
# Line: 199

def _should_cast(self, x, autocast, dtype):
    x_dtype = backend.standardize_dtype(x.dtype)
    if autocast and backend.is_float_dtype(x_dtype) and x_dtype != dtype:
        return True
    else:
        return False



# ==================================================
# Line: 245

def _check_quantization_mode(self, mode, compute_dtype):
    if mode not in QUANTIZATION_MODES:
        raise ValueError(
            "Invalid quantization mode. "
            f"Expected one of {QUANTIZATION_MODES}. "
            f"Received: mode={mode}"
        )
    if compute_dtype == "float16" and mode == "int8":
        raise ValueError(
            f"Quantization mode='{mode}' doesn't work well with "
            "compute_dtype='float16'."
        )



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/imagenet_utils_test.py
# Line: 150

def test_preprocess_input_symbolic_mixed_precision(self, mode):
    set_dtype_policy("mixed_float16")
    shape = (20, 20, 3)
    inputs = keras.layers.Input(shape=shape)
    try:
        keras.layers.Lambda(
            lambda x: utils.preprocess_input(x, mode=mode),
            output_shape=shape,
        )(inputs)
    finally:
        set_dtype_policy("float32")


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/trainer.py
# Line: 27

def _unpack_singleton(self, x):
    if isinstance(x, (list, tuple)) and len(x) == 1:
        return x[0]
    return x


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/export.py
# Line: 15

def add_endpoint(self, name, fn, input_signature=None, **kwargs):
    decorated_fn = tf.function(
        fn, input_signature=input_signature, autograph=False
    )
    return decorated_fn

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/saved_model_test.py
# Line: 32

def one(self):
    return 1



# ==================================================
# Line: 333

def concat(self, x):
    return x + x


# ==================================================
# Line: 346

def concat(self, x):
    return x + x


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/trainer.py
# Line: 645

def update_state(_, y, y_pred, sample_weight=None):
    return self._compiled_metrics_update_state(
        y, y_pred, sample_weight=sample_weight
    )


# ==================================================
# Line: 736

def tf_sync(self):
    tf_context.async_wait()


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/optimizer.py
# Line: 141

def _all_reduce_sum_gradients(self, grads_and_vars):
    """Returns all-reduced gradients aggregated via summation.

    Args:
        grads_and_vars: List of (gradient, variable) pairs.

    Returns:
        List of (gradient, variable) pairs
        where gradients have been all-reduced.
    """
    replica_context = tf.distribute.get_replica_context()
    if not replica_context:
        return grads_and_vars

    grads_and_vars = list(grads_and_vars)
    filtered_grads_and_vars = filter_empty_gradients(grads_and_vars)
    if filtered_grads_and_vars:
        grads = [pair[0] for pair in filtered_grads_and_vars]
        reduced = tf.distribute.get_replica_context().all_reduce(
            tf.distribute.ReduceOp.SUM, grads
        )
    else:
        reduced = []
    # Copy 'reduced' but add None gradients back in
    reduced_with_nones = []
    reduced_pos = 0
    for g, v in grads_and_vars:
        if g is None:
            reduced_with_nones.append((None, v))
        else:
            reduced_with_nones.append((reduced[reduced_pos], v))
            reduced_pos += 1
    assert reduced_pos == len(reduced), "Failed to add all gradients"
    return reduced_with_nones


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/core.py
# Line: 120

def _map_aggregation(self, aggregation):
    mapping = {
        "none": tf.VariableAggregation.NONE,
        "sum": tf.VariableAggregation.SUM,
        "mean": tf.VariableAggregation.MEAN,
        "only_first_replica": tf.VariableAggregation.ONLY_FIRST_REPLICA,
    }
    return mapping[aggregation]


# ==================================================
# Line: 129

def _map_synchronization(self, synchronization):
    mapping = {
        "none": tf.VariableSynchronization.NONE,
        "on_read": tf.VariableSynchronization.ON_READ,
        "on_write": tf.VariableSynchronization.ON_WRITE,
        "auto": tf.VariableSynchronization.AUTO,
    }
    return mapping[synchronization]



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/keras_tensor.py
# Line: 58

def shape(self, value):
    raise AttributeError(
        "The `shape` attribute of KerasTensor is immutable. One should "
        "create a new instance of KerasTensor for this."
    )


# ==================================================
# Line: 69

def dtype(self, value):
    raise AttributeError(
        "The `dtype` attribute of KerasTensor is immutable. One should "
        "create a new instance of KerasTensor for this."
    )


# ==================================================
# Line: 80

def sparse(self, value):
    raise AttributeError(
        "The `sparse` attribute of KerasTensor is immutable. One should "
        "create a new instance of KerasTensor for this."
    )


# ==================================================
# Line: 91

def ragged(self, value):
    raise AttributeError(
        "The `ragged` attribute of KerasTensor is immutable. One should "
        "create a new instance of KerasTensor for this."
    )


# ==================================================
# Line: 125

def __array__(self):
    raise ValueError(
        "A KerasTensor is symbolic: it's a placeholder for a shape "
        "an a dtype. It doesn't have any actual numerical value. "
        "You cannot convert it to a NumPy array."
    )


# ==================================================
# Line: 132

def __jax_array__(self):
    raise ValueError(
        "A KerasTensor cannot be used as input to a JAX function. "
        "A KerasTensor is a symbolic placeholder for a shape and dtype, "
        "used when constructing Keras Functional models "
        "or Keras Functions. You can only use it as input to a Keras layer "
        "or a Keras operation (from the namespaces `keras.layers` "
        "and `keras.ops`). "
        "You are likely doing something like:\n\n"
        "```\n"
        "x = Input(...)\n"
        "...\n"
        "jax_fn(x)  # Invalid.\n"
        "```\n\n"
        "What you should do instead is wrap `jax_fn` in a layer:\n\n"
        "```\n"
        "class MyLayer(Layer):\n"
        "    def call(self, x):\n"
        "        return jax_fn(x)\n\n"
        "x = MyLayer()(x)\n"
        "```\n"
    )


# ==================================================
# Line: 155

def __tf_tensor__(self, dtype=None, name=None):
    raise ValueError(
        "A KerasTensor cannot be used as input to a TensorFlow function. "
        "A KerasTensor is a symbolic placeholder for a shape and dtype, "
        "used when constructing Keras Functional models "
        "or Keras Functions. You can only use it as input to a Keras layer "
        "or a Keras operation (from the namespaces `keras.layers` "
        "and `keras.ops`). "
        "You are likely doing something like:\n\n"
        "```\n"
        "x = Input(...)\n"
        "...\n"
        "tf_fn(x)  # Invalid.\n"
        "```\n\n"
        "What you should do instead is wrap `tf_fn` in a layer:\n\n"
        "```\n"
        "class MyLayer(Layer):\n"
        "    def call(self, x):\n"
        "        return tf_fn(x)\n\n"
        "x = MyLayer()(x)\n"
        "```\n"
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/thread_safe_test.py
# Line: 11

def test_is_thread_safe(self):
    if backend.IS_THREAD_SAFE:
        executor = concurrent.futures.ThreadPoolExecutor()

        def sum(x, axis):
            return ops.sum(x, axis=axis)

        futures = []

        for i in range(10000):
            futures.clear()
            x = ops.convert_to_tensor(np.random.rand(100, 100))
            futures.append(executor.submit(sum, x, 1))
            x = ops.convert_to_tensor(np.random.rand(100))
            futures.append(executor.submit(sum, x, 0))
            concurrent.futures.wait(
                futures, return_when=concurrent.futures.ALL_COMPLETED
            )
            [future.result() for future in futures]

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/variables_test.py
# Line: 263

def test_standardize_dtype_with_torch_dtype(self):
    """Tests dtype standardization with PyTorch dtypes."""
    import torch

    x = torch.randn(4, 4)
    backend.standardize_dtype(x.dtype)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/export.py
# Line: 137

def _to_polymorphic_shape(self, struct, allow_none=True):
    if allow_none:
        # Generates unique names: a, b, ... z, aa, ab, ... az, ba, ... zz
        # for unknown non-batch dims. Defined here to be scope per endpoint.
        dim_names = itertools.chain(
            string.ascii_lowercase,
            itertools.starmap(
                lambda a, b: a + b,
                itertools.product(string.ascii_lowercase, repeat=2),
            ),
        )

    def convert_shape(x):
        poly_shape = []
        for index, dim in enumerate(list(x.shape)):
            if dim is not None:
                poly_shape.append(str(dim))
            elif not allow_none:
                raise ValueError(
                    f"Illegal None dimension in {x} with shape {x.shape}"
                )
            elif index == 0:
                poly_shape.append("batch")
            else:
                poly_shape.append(next(dim_names))
        return "(" + ", ".join(poly_shape) + ")"

    return tree.map_structure(convert_shape, struct)


# ==================================================
# Line: 166

def _check_device_compatible(self):
    from jax import default_backend as jax_device

    if (
        jax_device() == "gpu"
        and len(tf.config.list_physical_devices("GPU")) == 0
    ):
        warnings.warn(
            "JAX backend is using GPU for export, but installed "
            "TF package cannot access GPU, so reloading the model with "
            "the TF runtime in the same environment will not work. "
            "To use JAX-native serialization for high-performance export "
            "and serving, please install `tensorflow-gpu` and ensure "
            "CUDA version compatibility between your JAX and TF "
            "installations."
        )
        return False
    else:
        return True

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/trainer.py
# Line: 1045

def _prefetch_numpy_iterator(self, numpy_iterator):
    """Shard and prefetch batches on device.

    Most of the implementation has been borrowed from
    `flax.jax_utils.prefetch_to_device`

    This utility takes an iterator and returns a new iterator which fills an
    on device prefetch buffer. Eager prefetching can improve the performance
    of training loops significantly by overlapping compute and data
    transfer.
    """
    queue = collections.deque()

    # If you're training on GPUs, 2 is generally the best choice because
    # this guarantees that you can overlap a training step on GPU with a
    # data prefetch step on CPU.
    def enqueue(n=2):
        for data in itertools.islice(numpy_iterator, n):
            queue.append(_distribute_data(data))

    enqueue(n=2)  # TODO: should we make `n` configurable?
    while queue:
        yield queue.popleft()
        enqueue(1)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/distribution_lib_test.py
# Line: 51

def test_initialize_with_all_job_addresses(self, mock_jax_initialize):
    backend_dlib.initialize("10.0.0.1:1234,10.0.0.2:2345", 2, 0)
    mock_jax_initialize.assert_called_once_with(
        coordinator_address="10.0.0.1:1234", num_processes=2, process_id=0
    )


# ==================================================
# Line: 64

def test_initialize_with_coordinator_address(self, mock_jax_initialize):
    backend_dlib.initialize("10.0.0.1:1234", 2, 0)
    mock_jax_initialize.assert_called_once_with(
        coordinator_address="10.0.0.1:1234", num_processes=2, process_id=0
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/optimizers/torch_parallel_optimizer.py
# Line: 24

def _backend_increment_gradient_accumulators(self, grads, acc_grads):
    acc_list = [v.value for v in acc_grads]
    torch._foreach_add_(acc_list, grads, alpha=1.0)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/activations/activations.py
# Line: 72

def compute_output_spec(self, x):
    return backend.KerasTensor(x.shape, x.dtype)


# ==================================================
# Line: 616

def compute_output_spec(self, x):
    return backend.KerasTensor(x.shape, x.dtype)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/initializers/initializer.py
# Line: 55

def get_config(self):
    """Returns the initializer's configuration as a JSON-serializable dict.

    Returns:
        A JSON-serializable Python dict.
    """
    return {}


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/distribution/distribution_lib_test.py
# Line: 30

def test_initialize_with_explicit_param(self, mock_backend_initialize):
    job_addresses = "10.0.0.1:1234,10.0.0.2:2345"
    num_processes = 2
    current_process_id = 0

    distribution_lib.initialize(
        job_addresses, num_processes, current_process_id
    )

    mock_backend_initialize.assert_called_once_with(
        job_addresses, num_processes, current_process_id
    )


# ==================================================
# Line: 43

def test_initialize_with_env_vars(self, mock_backend_initialize):
    job_addresses = "10.0.0.1:1234,10.0.0.2:2345"
    num_processes = 2
    current_process_id = 0
    os.environ["KERAS_DISTRIBUTION_JOB_ADDRESSES"] = job_addresses
    os.environ["KERAS_DISTRIBUTION_NUM_PROCESSES"] = str(num_processes)
    os.environ["KERAS_DISTRIBUTION_PROCESS_ID"] = str(current_process_id)

    distribution_lib.initialize()
    mock_backend_initialize.assert_called_once_with(
        job_addresses, num_processes, current_process_id
    )


# ==================================================
# Line: 56

def test_init_with_nones(self, mock_backend_initialize):
    # This is also valid case for Cloud TPU on JAX
    distribution_lib.initialize()
    mock_backend_initialize.assert_called_once_with(None, None, None)



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/export/saved_model.py
# Line: 542

def _convert_to_tf_variable(self, backend_variable):
    if not isinstance(backend_variable, backend.Variable):
        raise TypeError(
            "`backend_variable` must be a `backend.Variable`. "
            f"Recevied: backend_variable={backend_variable} of type "
            f"({type(backend_variable)})"
        )
    return tf.Variable(
        backend_variable.value,
        dtype=backend_variable.dtype,
        trainable=backend_variable.trainable,
        name=backend_variable.name,
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/time_distributed.py
# Line: 56

def _get_child_input_shape(self, input_shape):
    if not isinstance(input_shape, (tuple, list)) or len(input_shape) < 3:
        raise ValueError(
            "`TimeDistributed` Layer should be passed an `input_shape` "
            f"with at least 3 dimensions, received: {input_shape}"
        )
    return (input_shape[0], *input_shape[2:])


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/time_distributed_test.py
# Line: 83

def test_with_mask_zero(self):
    model = Sequential(
        [
            layers.Input(shape=(20,)),
            layers.Embedding(input_dim=10, output_dim=5, mask_zero=True),
            layers.TimeDistributed(
                layers.Dense(units=5, activation="softmax")
            ),
        ]
    )
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    X_train = np.random.uniform(1, 10, size=(22, 20))
    Y_train = np.random.randint(1, 2, size=(22, 20))

    model.fit(X_train, Y_train, epochs=1, batch_size=16)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/merging/dot.py
# Line: 346

def compute_mask(self, inputs, mask=None):
    return None


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/merging/subtract.py
# Line: 42

def _merge_function(self, inputs):
    if len(inputs) != 2:
        raise ValueError(
            "A `Subtract` layer should be called on exactly 2 inputs. "
            f"Received: inputs={inputs}"
        )
    return ops.subtract(inputs[0], inputs[1])



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/merging/multiply.py
# Line: 34

def _merge_function(self, inputs):
    masks = [backend.get_keras_mask(x) for x in inputs]
    has_output_mask = all(mask is not None for mask in masks)
    output = None
    output_mask = None

    for x, mask in zip(inputs, masks):
        if mask is not None:
            mask = ops.broadcast_to(ops.expand_dims(mask, -1), ops.shape(x))
            # Replace 0s with 1s outside of mask.
            x = ops.where(mask, x, ops.cast(1, x.dtype))
            if has_output_mask:
                output_mask = (
                    mask
                    if output_mask is None
                    else ops.logical_or(output_mask, mask)
                )
        output = x if output is None else ops.multiply(output, x)

    if has_output_mask:
        # Replace 1s with 0s outside of mask per standard masking rules.
        output = ops.where(output_mask, output, ops.cast(0, output.dtype))
        output_mask = ops.any(output_mask, axis=-1, keepdims=False)
        backend.set_keras_mask(output, output_mask)
    return output



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/merging/base_merge.py
# Line: 23

def _apply_merge_op_and_or_mask(self, op_fn, inputs):
    """Merge a set of inputs by applying `op_fn` and ORing the masks.

    We use this for `Minimum` and `Maximum` as it handles the fact that
    there is no identity element. If applicable, the mask obtained by ORing
    all masks is set on the output.

    Args:
        op_fn: binary operation to apply to tensor pair.
        inputs: array of tensors to apply operation on.
    """
    output = None
    output_mask = None

    for x in inputs:
        mask = backend.get_keras_mask(x)
        if mask is not None:
            mask = ops.broadcast_to(ops.expand_dims(mask, -1), ops.shape(x))
        if output is None:
            output = x
            output_mask = mask
            continue
        if mask is not None:
            x = ops.where(mask, x, output)
        if output_mask is not None:
            output = ops.where(output_mask, output, x)
        if mask is not None and output_mask is not None:
            output_mask = ops.logical_or(output_mask, mask)
        else:
            output_mask = None
        output = op_fn(output, x)

    if output_mask is not None:
        output_mask = ops.any(output_mask, axis=-1, keepdims=False)
        backend.set_keras_mask(output, output_mask)
    return output


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/regularization/alpha_dropout.py
# Line: 80

def _get_concrete_noise_shape(self, inputs, noise_shape):
    if noise_shape is None:
        return ops.shape(inputs)

    concrete_inputs_shape = ops.shape(inputs)
    concrete_noise_shape = []
    for i, value in enumerate(noise_shape):
        concrete_noise_shape.append(
            concrete_inputs_shape[i] if value is None else value
        )
    return concrete_noise_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/regularization/gaussian_noise.py
# Line: 55

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/regularization/spatial_dropout_test.py
# Line: 64

def test_spatial_dropout_1D_dynamic(self):
    inputs = layers.Input((3, 2))
    layer = layers.SpatialDropout1D(0.5)
    layer(inputs, training=True)


# ==================================================
# Line: 75

def test_spatial_dropout_2D_dynamic(self):
    inputs = layers.Input((3, 2, 4))
    layer = layers.SpatialDropout2D(0.5)
    layer(inputs, training=True)


# ==================================================
# Line: 92

def test_spatial_dropout_3D_dynamic(self):
    inputs = layers.Input((3, 2, 4, 2))
    layer = layers.SpatialDropout3D(0.5)
    layer(inputs, training=True)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/regularization/spatial_dropout.py
# Line: 66

def _get_noise_shape(self, inputs):
    input_shape = ops.shape(inputs)
    return (input_shape[0], 1, input_shape[2])



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/pooling/global_average_pooling1d.py
# Line: 85

def compute_mask(self, inputs, mask=None):
    return None

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/attention.py
# Line: 190

def _calculate_score_mask(self, scores, v_mask, use_causal_mask):
    if use_causal_mask:
        # Creates a lower triangular mask, so position i cannot attend to
        # positions j > i. This prevents the flow of information from the
        # future into the past.
        score_shape = ops.shape(scores)
        # causal_mask_shape = [1, Tq, Tv].
        mask_shape = (1, score_shape[-2], score_shape[-1])
        ones_mask = ops.ones(shape=mask_shape, dtype="int32")
        row_index = ops.cumsum(ones_mask, axis=-2)
        col_index = ops.cumsum(ones_mask, axis=-1)
        causal_mask = ops.greater_equal(row_index, col_index)

        if v_mask is not None:
            # Mask of shape [batch_size, 1, Tv].
            v_mask = ops.expand_dims(v_mask, axis=-2)
            return ops.logical_and(v_mask, causal_mask)
        return causal_mask
    else:
        # If not using causal mask, return the value mask as is,
        # or None if the value mask is not provided.
        return v_mask


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/multi_head_attention.py
# Line: 646

def _compute_causal_mask(self, query, value=None):
    """Computes a causal mask (e.g., for masked self-attention layers).

    For example, if query and value both contain sequences of length 4,
    this function returns a boolean tensor equal to:

    ```
    [[[True,  False, False, False],
      [True,  True,  False, False],
      [True,  True,  True,  False],
      [True,  True,  True,  True]]]
    ```

    Args:
        query: query tensor of shape `(B, T, ...)`.
        value: value tensor of shape `(B, S, ...)` (optional, defaults to
            query).

    Returns:
        mask: a boolean tensor of shape `(1, T, S)` containing a lower
            triangular matrix of shape `(T, S)`.
    """
    q_seq_length = ops.shape(query)[1]
    v_seq_length = q_seq_length if value is None else ops.shape(value)[1]
    ones_mask = ops.ones((1, q_seq_length, v_seq_length), dtype="int32")
    row_index = ops.cumsum(ones_mask, axis=-2)
    col_index = ops.cumsum(ones_mask, axis=-1)
    return ops.greater_equal(row_index, col_index)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/grouped_query_attention.py
# Line: 346

def _compute_causal_mask(self, query, value=None):
    """Computes a causal mask (e.g., for masked self-attention layers).

    For example, if query and value both contain sequences of length 4,
    this function returns a boolean tensor equal to:

    ```
    [[[True,  False, False, False],
      [True,  True,  False, False],
      [True,  True,  True,  False],
      [True,  True,  True,  True]]]
    ```

    Args:
        query: query tensor of shape `(B, T, ...)`.
        value: value tensor of shape `(B, S, ...)` (optional, defaults to
            query).

    Returns:
        mask: a boolean tensor of shape `(1, T, S)` containing a lower
            triangular matrix of shape `(T, S)`.
    """
    q_seq_length = ops.shape(query)[1]
    v_seq_length = q_seq_length if value is None else ops.shape(value)[1]
    ones_mask = ops.ones((1, q_seq_length, v_seq_length), dtype="int32")
    row_index = ops.cumsum(ones_mask, axis=-2)
    col_index = ops.cumsum(ones_mask, axis=-1)
    return ops.greater_equal(row_index, col_index)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/multi_head_attention_test.py
# Line: 639

def test_multi_head_attention_output_shape_as_int(self):
    """Test MultiHeadAttention with output_shape as an int."""
    mha = layers.MultiHeadAttention(num_heads=2, key_dim=16, output_shape=8)
    query = random.uniform((2, 4, 16))
    value = random.uniform((2, 4, 16))
    output = mha(query=query, value=value)

    assert output.shape == (
        2,
        4,
        8,
    ), f"Expected shape (2, 4, 8), got {output.shape}"


# ==================================================
# Line: 652

def test_multi_head_attention_output_shape_as_tuple(self):
    """Test MultiHeadAttention with output_shape as a tuple."""
    mha = layers.MultiHeadAttention(
        num_heads=2, key_dim=16, output_shape=(8, 8)
    )
    query = random.uniform((2, 4, 16))
    value = random.uniform((2, 4, 16))
    output = mha(query=query, value=value)

    assert output.shape == (
        2,
        4,
        8,
        8,
    ), f"Expected shape (2, 4, 8, 8), got {output.shape}"


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/normalization/spectral_normalization_test.py
# Line: 86

def test_end_to_end(self):
    sn_wrapper = layers.SpectralNormalization(
        layers.Conv2D(
            3, (2, 2), padding="same", data_format="channels_last"
        ),
        power_iterations=2,
    )
    model = models.Sequential([sn_wrapper])
    model.compile("rmsprop", loss="mse")
    x = np.random.random((4, 8, 8, 3))
    y = np.random.random((4, 8, 8, 3))
    model.fit(x, y)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/feature_space_test.py
# Line: 16

def _get_train_data_dict(
    self,
    as_dataset=False,
    as_tensors=False,
    as_labeled_dataset=False,
    include_strings=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/pipeline_test.py
# Occurrences: Lines 22-25 (2 instances)

def compute_mask(self, x, mask=None):
    return x


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/index_lookup.py
# Occurrences: Lines 881-884 (2 instances)

def _convert_to_ndarray(self, x):
    return np.array(x) if isinstance(x, (list, tuple)) else x


# ==================================================
# Line: 931

def _find_repeated_tokens(self, vocabulary):
    """Return all repeated tokens in a vocabulary."""
    vocabulary_set = set(vocabulary)
    if len(vocabulary) != len(vocabulary_set):
        return [
            item
            for item, count in collections.Counter(vocabulary).items()
            if count > 1
        ]
    else:
        return []


# ==================================================
# Line: 943

def _num_tokens(self, data):
    """Count the number of tokens in a ragged, sparse or dense tensor."""
    if isinstance(data, tf.SparseTensor):
        flat_values = data.values
    elif isinstance(data, tf.RaggedTensor):
        flat_values = data.flat_values
    else:
        flat_values = tf.reshape(data, [-1])
    tokens, _, counts = tf.unique_with_counts(flat_values, out_idx="int64")
    return tokens, counts


# ==================================================
# Line: 954

def _inverse_document_frequency(self, token_document_counts, num_documents):
    """Computes the inverse-document-frequency (IDF) component of "tf_idf".
    Args:
        token_document_counts: An array of the # of documents each token
            appears in.
        num_documents: An int representing the total number of documents

    Returns:
        An array of "inverse document frequency" weights.
    """
    return tf.math.log(1 + num_documents / (1 + token_document_counts))


# ==================================================
# Line: 967

def _tensor_vocab_to_numpy(self, vocabulary):
    """Converts a tensor vocabulary to a numpy vocabulary."""
    return vocabulary.numpy()



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/stft_spectrogram_test.py
# Line: 280

def test_spectrogram_dynamic_shape(self):
    model = Sequential(
        [
            Input(shape=(None, 1), dtype=TestSpectrogram.DTYPE),
            layers.STFTSpectrogram(
                frame_length=500,
                frame_step=25,
                fft_length=1024,
                mode="stft",
                data_format="channels_last",
            ),
        ]
    )

    def generator():
        yield (np.random.random((2, 16000, 1)),)
        yield (np.random.random((3, 8000, 1)),)

    model.predict(generator())


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/rescaling.py
# Line: 55

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/normalization_test.py
# Line: 100

def test_call_on_meta_device_after_built(self):
    layer = layers.Normalization()
    data = np.random.random((32, 4))
    layer.adapt(data)
    with backend.device("meta"):
        layer(data)


# ==================================================
# Line: 148

def test_tf_data_compatibility(self):
    x = np.random.random((32, 3))
    ds = tf_data.Dataset.from_tensor_slices(x).batch(1)

    # With built-in values
    layer = layers.Normalization(
        mean=[0.1, 0.2, 0.3], variance=[0.1, 0.2, 0.3], axis=-1
    )
    layer.build((None, 3))
    for output in ds.map(layer).take(1):
        output.numpy()

    # With adapt flow
    layer = layers.Normalization(axis=-1)
    layer.adapt(
        np.random.random((32, 3)),
    )
    for output in ds.map(layer).take(1):
        output.numpy()


# ==================================================
# Line: 168

def test_normalization_with_scalar_mean_var(self):
    input_data = np.array([[1, 2, 3]], dtype="float32")
    layer = layers.Normalization(mean=3.0, variance=2.0)
    layer(input_data)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/text_vectorization_test.py
# Line: 148

def test_tf_as_first_sequential_layer(self):
    layer = layers.TextVectorization(
        max_tokens=10,
        output_mode="int",
        output_sequence_length=3,
    )
    layer.set_vocabulary(["baz", "bar", "foo"])
    model = models.Sequential(
        [
            layer,
            layers.Embedding(5, 4),
        ]
    )
    model(backend.convert_to_tensor([["foo qux bar"], ["qux baz"]]))


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/feature_space.py
# Line: 450

def _feature_to_input(self, name, feature):
    return layers.Input(shape=(1,), dtype=feature.dtype, name=name)


# ==================================================
# Line: 481

def _cross_to_crosser(self, cross):
    return layers.HashedCrossing(cross.crossing_dim, name=cross.name)


# ==================================================
# Line: 692

def _convert_input(self, x):
    if not isinstance(x, (tf.Tensor, tf.SparseTensor, tf.RaggedTensor)):
        if not isinstance(x, (list, tuple, int, float)):
            x = backend.convert_to_numpy(x)
        x = tf.convert_to_tensor(x)
    return x


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/hashed_crossing.py
# Line: 187

def _check_at_least_two_inputs(self, inputs):
    if not isinstance(inputs, (list, tuple)):
        raise ValueError(
            "`HashedCrossing` should be called on a list or tuple of "
            f"inputs. Received: inputs={inputs}"
        )
    if len(inputs) < 2:
        raise ValueError(
            "`HashedCrossing` should be called on at least two inputs. "
            f"Received: inputs={inputs}"
        )


# ==================================================
# Line: 199

def _check_input_shape_and_type(self, inputs):
    first_shape = tuple(inputs[0].shape)
    rank = len(first_shape)
    if rank > 2 or (rank == 2 and first_shape[-1] != 1):
        raise ValueError(
            "All `HashedCrossing` inputs should have shape `()`, "
            "`(batch_size)` or `(batch_size, 1)`. "
            f"Received: inputs={inputs}"
        )
    if not all(tuple(x.shape) == first_shape for x in inputs[1:]):
        raise ValueError(
            "All `HashedCrossing` inputs should have equal shape. "
            f"Received: inputs={inputs}"
        )
    if any(
        isinstance(x, (tf.RaggedTensor, tf.SparseTensor)) for x in inputs
    ):
        raise ValueError(
            "All `HashedCrossing` inputs should be dense tensors. "
            f"Received: inputs={inputs}"
        )
    if not all(
        tf.as_dtype(x.dtype).is_integer or x.dtype == tf.string
        for x in inputs
    ):
        raise ValueError(
            "All `HashedCrossing` inputs should have an integer or "
            f"string dtype. Received: inputs={inputs}"
        )

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_flip.py
# Line: 224

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_erasing_test.py
# Line: 81

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomErasing(data_format=data_format)

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/auto_contrast.py
# Occurrences: Lines 87-90 (2 instances)

def transform_labels(self, labels, transformation, training=True):
    return labels


# ==================================================
# Line: 98

def transform_segmentation_masks(
    self, segmentation_masks, transformation, training=True

# ==================================================
# Line: 108

def compute_output_shape(self, input_shape):
    return input_shape

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_sharpness_test.py
# Line: 53

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomSharpness(
        factor=0.5, data_format=data_format, seed=1337
    )

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_zoom_test.py
# Line: 126

def test_dynamic_shape(self):
    inputs = layers.Input((None, None, 3))
    outputs = layers.RandomZoom(
        height_factor=(0.5, 0.5),
        width_factor=(0.8, 0.8),
        interpolation="nearest",
        fill_mode="constant",
    )(inputs)
    model = models.Model(inputs, outputs)
    model.predict(np.random.random((1, 6, 6, 3)))


# ==================================================
# Line: 141

def test_connect_with_flatten(self):
    model = models.Sequential(
        [
            layers.RandomZoom((-0.5, 0.0), (-0.5, 0.0)),
            layers.Flatten(),
            layers.Dense(1, activation="relu"),
        ],
    )

    model.compile(loss="mse")
    model.fit(np.random.random((2, 2, 2, 1)), y=np.random.random((2,)))


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_shear_test.py
# Line: 68

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomShear(1, 1)

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/center_crop.py
# Line: 70

def transform_labels(self, labels, transformation, training=True):
    return labels


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_contrast_test.py
# Line: 101

def test_tf_data_compatibility(self):
    layer = layers.RandomContrast(factor=0.5, seed=1337)
    input_data = np.random.random((2, 8, 8, 3))
    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    next(iter(ds)).numpy()


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_color_jitter_test.py
# Line: 119

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomColorJitter(
        value_range=(0, 1),
        brightness_factor=0.1,
        contrast_factor=0.2,
        saturation_factor=0.9,
        hue_factor=0.1,
    )

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur.py
# Line: 58

def _set_kernel_size(self, factor, name):
    error_msg = f"{name} must be an odd number. Received: {name}={factor}"
    if isinstance(factor, (tuple, list)):
        if len(factor) != 2:
            error_msg = (
                f"The `{name}` argument should be a number "
                "(or a list of two numbers) "
                f"Received: {name}={factor}"
            )
            raise ValueError(error_msg)
        if (factor[0] % 2 == 0) or (factor[1] % 2 == 0):
            raise ValueError(error_msg)
        lower, upper = factor
    elif isinstance(factor, (int, float)):
        if factor % 2 == 0:
            raise ValueError(error_msg)
        lower, upper = factor, factor
    else:
        raise ValueError(error_msg)

    return lower, upper


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_rotation.py
# Line: 125

def transform_labels(self, labels, transformation, training=True):
    return labels


# ==================================================
# Line: 236

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_hue.py
# Occurrences: Lines 143-151 (3 instances)

def transform_labels(self, labels, transformation, training=True):
    return labels


# ==================================================
# Line: 167

def compute_output_shape(self, input_shape):
    return input_shape

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_saturation_test.py
# Line: 85

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomSaturation(
        factor=0.5, data_format=data_format, seed=1337
    )

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_elastic_transform_test.py
# Line: 77

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomElasticTransform(data_format=data_format)

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        print("Output shape:", output.shape)  # Debugging line
        output_numpy = output.numpy()
        print("Output numpy shape:", output_numpy.shape)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur_test.py
# Line: 81

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomGaussianBlur(data_format=data_format)

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/bounding_box.py
# Line: 250

def _xyxy_to_xyxy(self, boxes, height=None, width=None):
    return boxes


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/cut_mix_test.py
# Line: 75

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.CutMix(data_format=data_format)

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_brightness_test.py
# Line: 55

def test_tf_data_compatibility(self):
    layer = layers.RandomBrightness(factor=0.5, seed=1337)
    input_data = np.random.random((2, 8, 8, 3))
    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/mix_up.py
# Line: 171

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/resizing.py
# Line: 127

def transform_labels(self, labels, transformation=None, training=True):
    return labels


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/center_crop_test.py
# Line: 12

def np_center_crop(self, img, h_new, w_new, data_format="channels_last"):
    img = np.array(img)
    if img.ndim == 4:
        if data_format == "channels_last":
            _, h, w = img.shape[:3]
        else:
            _, h, w = img.shape[1:]
    else:
        if data_format == "channels_last":
            h, w = img.shape[:2]
        else:
            h, w = img.shape[1:]
    h_start = (h - h_new) // 2
    w_start = (w - w_new) // 2
    if data_format == "channels_last":
        return img[
            ..., h_start : h_start + h_new, w_start : w_start + w_new, :
        ]
    else:
        return img[
            ..., h_start : h_start + h_new, w_start : w_start + w_new
        ]


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/rand_augment_test.py
# Line: 75

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandAugment(data_format=data_format)

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()


# ==================================================
# Line: 87

def test_rand_augment_tf_data_bounding_boxes(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        image_shape = (1, 10, 8, 3)
    else:
        image_shape = (1, 3, 10, 8)
    input_image = np.random.random(image_shape)
    bounding_boxes = {
        "boxes": np.array(
            [
                [
                    [2, 1, 4, 3],
                    [6, 4, 8, 6],
                ]
            ]
        ),
        "labels": np.array([[1, 2]]),
    }

    input_data = {"images": input_image, "bounding_boxes": bounding_boxes}

    ds = tf_data.Dataset.from_tensor_slices(input_data)
    layer = layers.RandAugment(
        data_format=data_format,
        seed=42,
        bounding_box_format="xyxy",
    )
    ds.map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/solarization.py
# Occurrences: Lines 190-198 (3 instances)

def transform_labels(self, labels, transformation, training=True):
    return labels


# ==================================================
# Line: 213

def compute_output_shape(self, input_shape):
    return input_shape

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py
# Line: 182

def transform_labels(self, labels, transformation, training=True):
    return labels


# ==================================================
# Line: 416

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/max_num_bounding_box.py
# Occurrences: Lines 22-25 (2 instances)

def transform_images(self, images, transformation=None, training=True):
    return images


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/mix_up_test.py
# Line: 70

def test_tf_data_compatibility(self):
    layer = layers.MixUp()
    input_data = np.random.random((2, 8, 8, 3))
    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py
# Line: 58

def get_random_transformation(self, data, training=True, seed=None):
    return None


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/aug_mix_test.py
# Line: 56

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.AugMix(data_format=data_format)

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_shear.py
# Line: 238

def transform_labels(self, labels, transformation, training=True):
    return labels


# ==================================================
# Line: 400

def compute_output_shape(self, input_shape):
    return input_shape

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_grayscale.py
# Occurrences: Lines 95-109 (5 instances)

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_translation_test.py
# Line: 327

def test_tf_data_compatibility(self):
    layer = layers.RandomTranslation(0.2, 0.1)
    input_data = np.random.random((1, 4, 4, 3))
    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(1).map(layer)
    next(iter(ds)).numpy()


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_invert_test.py
# Line: 56

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomInvert(
        factor=0.5, value_range=[0, 1], data_format=data_format, seed=1337
    )

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_color_degeneration_test.py
# Line: 65

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomColorDegeneration(
        factor=0.5, data_format=data_format, seed=1337
    )

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_hue_test.py
# Line: 71

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomHue(
        factor=0.5, value_range=[0, 1], data_format=data_format, seed=1337
    )

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/equalization.py
# Line: 118

def _scale_values(self, values, source_range, target_range):
    source_min, source_max = source_range
    target_min, target_max = target_range
    scale = (target_max - target_min) / (source_max - source_min)
    offset = target_min - source_min * scale
    return values * scale + offset


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_posterization_test.py
# Line: 75

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomPosterization(1, [0, 255])

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_perspective_test.py
# Line: 86

def test_tf_data_compatibility(self):
    data_format = backend.config.image_data_format()
    if data_format == "channels_last":
        input_data = np.random.random((2, 8, 8, 3))
    else:
        input_data = np.random.random((2, 3, 8, 8))
    layer = layers.RandomPerspective(data_format=data_format)

    ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)
    for output in ds.take(1):
        output.numpy()


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_elastic_transform.py
# Line: 197

def get_elastic_transform_params(self, height, width, factor):
    alpha_scale = 0.1 * factor
    sigma_scale = 0.05 * factor

    alpha = max(height, width) * alpha_scale
    sigma = min(height, width) * sigma_scale

    return alpha, sigma


# ==================================================
# Line: 252

def transform_labels(self, labels, transformation, training=True):
    return labels


# ==================================================
# Line: 262

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_perspective.py
# Line: 314

def transform_labels(self, labels, transformation, training=True):
    return labels


# ==================================================
# Line: 324

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/rescaling_test.py
# Line: 71

def test_tf_data_compatibility(self):
    layer = layers.Rescaling(scale=1.0 / 255, offset=0.5)
    x = np.random.random((3, 10, 10, 3)) * 255
    ds = tf_data.Dataset.from_tensor_slices(x).batch(3).map(layer)
    next(iter(ds)).numpy()


# ==================================================
# Line: 77

def test_rescaling_with_channels_first_and_vector_scale(self):
    config = backend.image_data_format()
    backend.set_image_data_format("channels_first")
    layer = layers.Rescaling(
        scale=[1.0 / 255, 1.5 / 255, 2.0 / 255], offset=0.5
    )
    x = np.random.random((2, 3, 10, 10)) * 255
    layer(x)
    backend.set_image_data_format(config)


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/reshaping/up_sampling2d_test.py
# Line: 128

def test_upsampling_2d_various_interpolation_methods(self):
    input_shape = (2, 2, 1, 3)
    x = np.arange(np.prod(input_shape)).reshape(input_shape)
    for interpolation in ["nearest", "bilinear", "bicubic"]:
        layers.UpSampling2D(size=(1, 2), interpolation=interpolation)(x)


# ==================================================
# Line: 137

def test_upsampling_2d_lanczos_interpolation_methods(self):
    input_shape = (2, 2, 1, 3)
    x = np.arange(np.prod(input_shape)).reshape(input_shape)
    for interpolation in ["lanczos3", "lanczos5"]:
        layers.UpSampling2D(size=(1, 2), interpolation=interpolation)(x)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/reshaping/up_sampling3d.py
# Line: 108

def _resize_volumes(
    self, x, depth_factor, height_factor, width_factor, data_format

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/reshaping/up_sampling2d.py
# Line: 122

def _resize_images(
    self,
    x,
    height_factor,
    width_factor,
    data_format,
    interpolation="nearest",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/activations/prelu.py
# Line: 97

def compute_output_shape(self, input_shape):
    return input_shape

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/activations/relu.py
# Line: 86

def compute_output_shape(self, input_shape):
    return input_shape

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/layer.py
# Line: 810

def compute_mask(self, inputs, previous_mask):
    return previous_mask


# ==================================================
# Line: 1337

def _quantization_mode_error(self, mode):
    return NotImplementedError(
        "Invalid quantization mode. Expected one of "
        f"{dtype_policies.QUANTIZATION_MODES}. "
        f"Received: quantization_mode={mode}"
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/layer_test.py
# Occurrences: Lines 44-47 (2 instances)

def call(self, x):
    assert False  # Should never be called.


# ==================================================
# Occurrences: Lines 57-60 (2 instances)

def call(self, x):
    assert False  # Should never be called.


# ==================================================
# Occurrences: Lines 72-75 (2 instances)

def call(self, x):
    assert False  # Should never be called.


# ==================================================
# Occurrences: Lines 87-90 (2 instances)

def call(self, x):
    assert False  # Should never be called.


# ==================================================
# Occurrences: Lines 102-105 (2 instances)

def call(self, x):
    assert False  # Should never be called.


# ==================================================
# Occurrences: Lines 128-131 (2 instances)

def call(self, x):
    assert False  # Should never be called.


# ==================================================
# Line: 149

def call(self, x, bool_arg):
    if bool_arg:
        return x
    return x + 1


# ==================================================
# Line: 197

def call(self, x):
    return x + 1


# ==================================================
# Occurrences: Lines 278-282 (2 instances)

def call(self, x):
    return x + 1


# ==================================================
# Occurrences: Lines 309-312 (2 instances)

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# Occurrences: Lines 335-338 (2 instances)

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# Line: 521

def call(self, x):
    return x


# ==================================================
# Line: 623

def call(self, x, training=False):
    raise RuntimeError("oops!")


# ==================================================
# Line: 749

def call(self, x):
    # Here are the assertions.
    assertDType(x[0], "float32")  # Cast to compute_dtype
    assertDType(x[1], "int32")  # Untouched


# ==================================================
# Line: 783

def call(self, x, mask=None):
    assert mask is not None
    return x


# ==================================================
# Line: 800

def call(self, x, mask=None):
    assert isinstance(x, list)
    assert len(x) == 2
    assert isinstance(mask, list)
    assert len(mask) == 2
    return x


# ==================================================
# Line: 826

def call(self, x1, x2, x1_mask=None, x2_mask=None):
    assert x1_mask is not None
    assert x2_mask is not None
    return x1 + x2


# ==================================================
# Line: 840

def call(self, x1, x2, x1_mask=None, x2_mask=None):
    assert isinstance(x1, tuple)
    assert x1_mask is not None
    assert x2_mask is not None
    assert isinstance(x1_mask, tuple)
    return x1[0] + x1[1] + x2


# ==================================================
# Line: 865

def call(self, x, mask=None):
    assert mask is not None
    backend.set_keras_mask(x, None)  # Unset mask
    return x


# ==================================================
# Line: 962

def call(self, inputs):
    return inputs


# ==================================================
# Line: 980

def call(self, inputs):
    return inputs


# ==================================================
# Line: 1024

def call(self, foo, bar):
    return foo + bar


# ==================================================
# Line: 1031

def call(self, foo, bar):
    return foo[:, 0] + bar[:, 0]


# ==================================================
# Line: 1039

def call(self, foo, bar):
    return foo[:, 0] + bar[:, 0]


# ==================================================
# Line: 1047

def call(self, foo, bar=None, baz=None):
    return foo[:, 0] + bar[:, 0] + baz[:, 0]


# ==================================================
# Line: 1054

def call(self, foo, bar):
    return foo[:, 0] + bar[:, 0]


# ==================================================
# Line: 1554

def call(self, x, foo_mode=None):
    return x + (1 if foo_mode else 0)


# ==================================================
# Line: 1576

def call(self, x):
    return x


# ==================================================
# Line: 1592

def call(self, x):
    return x


# ==================================================
# Line: 1614

def call(self, x, foo_mode=None):
    return x + (1 if foo_mode else 0)


# ==================================================
# Line: 1648

def call(self, x, foo_mode=None):
    return x + (1 if foo_mode else 0)


# ==================================================
# Line: 1678

def call(self, x, foo_mode=False):
    # If foo_mode=True add 1, otherwise add 0
    add_val = ops.where(foo_mode, 1.0, 0.0)
    return x + add_val


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/input_layer.py
# Line: 123

def call(self):
    return


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/lambda_layer.py
# Line: 151

def _serialize_function_to_config(self, fn):
    if isinstance(fn, types.LambdaType) and fn.__name__ == "<lambda>":
        code, defaults, closure = python_utils.func_dump(fn)
        return {
            "class_name": "__lambda__",
            "config": {
                "code": code,
                "defaults": defaults,
                "closure": closure,
            },
        }
    elif callable(fn):
        return serialization_lib.serialize_keras_object(fn)
    raise ValueError(
        "Invalid input type for serialization. "
        f"Received: {fn} of type {type(fn)}."
    )


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/masking_test.py
# Occurrences: Lines 49-52 (2 instances)

def compute_output_shape(self, input_shape):
    return input_shape


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/input_layer_test.py
# Line: 140

def test_numpy_shape(self):
    # non-python int type shapes should be ok
    InputLayer(shape=(np.int64(32),))


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/constraints/constraints.py
# Line: 48

def get_config(self):
    """Returns a Python dict of the object config.

    A constraint config is a Python dictionary (JSON-serializable) that can
    be used to reinstantiate the same object.

    Returns:
        Python dict containing the configuration of the constraint object.
    """
    return {}


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/wrappers/utils.py
# Line: 54

def transform(self, y):
    """Makes 1D y 2D.

    Args:
        y : np.ndarray
            Target y to be transformed.

    Returns:
        np.ndarray
            A numpy array, of dimension at least 2.
    """
    if y.ndim == 1:
        return y.reshape(-1, 1)
    return y


# ==================================================
# File: /root/ecooptimizer/keras/keras/src/wrappers/sklearn_wrapper.py
# Line: 87

def _more_tags(self):
    return {"non_deterministic": True}


# ==================================================
