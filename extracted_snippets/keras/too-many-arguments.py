# too-many-arguments snippets for keras

# File: /root/ecooptimizer/keras/keras/src/visualization/plot_image_gallery.py
# Line: 45

def plot_image_gallery(
    images,
    y_true=None,
    y_pred=None,
    label_map=None,
    rows=None,
    cols=None,
    value_range=(0, 255),
    scale=2,
    path=None,
    show=None,
    transparent=True,
    dpi=60,
    legend_handles=None,
    data_format=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/visualization/draw_bounding_boxes.py
# Line: 17

def draw_bounding_boxes(
    images,
    bounding_boxes,
    bounding_box_format,
    class_mapping=None,
    color=(128, 128, 128),
    line_thickness=2,
    text_thickness=1,
    font_scale=1.0,
    data_format=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/visualization/draw_segmentation_masks.py
# Line: 9

def draw_segmentation_masks(
    images,
    segmentation_masks,
    num_classes=None,
    color_mapping=None,
    alpha=0.8,
    blend=True,
    ignore_index=-1,
    data_format=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/visualization/plot_segmentation_mask_gallery.py
# Line: 15

def plot_segmentation_mask_gallery(
    images,
    num_classes,
    value_range=(0, 255),
    y_true=None,
    y_pred=None,
    color_mapping=None,
    blend=True,
    alpha=0.8,
    ignore_index=-1,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/visualization/plot_bounding_box_gallery.py
# Line: 18

def plot_bounding_box_gallery(
    images,
    bounding_box_format,
    y_true=None,
    y_pred=None,
    value_range=(0, 255),
    true_color=(0, 188, 212),
    pred_color=(255, 235, 59),
    line_thickness=2,
    font_scale=1.0,
    text_thickness=None,
    class_mapping=None,
    ground_truth_mapping=None,
    prediction_mapping=None,
    legend=False,
    legend_handles=None,
    rows=None,
    cols=None,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/lambda_callback.py
# Line: 64

def __init__(
    self,
    on_epoch_begin=None,
    on_epoch_end=None,
    on_train_begin=None,
    on_train_end=None,
    on_train_batch_begin=None,
    on_train_batch_end=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/model_checkpoint.py
# Line: 127

def __init__(
    self,
    filepath,
    monitor="val_loss",
    verbose=0,
    save_best_only=False,
    save_weights_only=False,
    mode="auto",
    save_freq="epoch",
    initial_value_threshold=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/early_stopping.py
# Line: 66

def __init__(
    self,
    monitor="val_loss",
    min_delta=0,
    patience=0,
    verbose=0,
    mode="auto",
    baseline=None,
    restore_best_weights=False,
    start_from_epoch=0,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/tensorboard.py
# Line: 156

def __init__(
    self,
    log_dir="logs",
    histogram_freq=0,
    write_graph=True,
    write_images=False,
    write_steps_per_second=False,
    update_freq="epoch",
    profile_batch=0,
    embeddings_freq=0,
    embeddings_metadata=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/callbacks/reduce_lr_on_plateau.py
# Line: 48

def __init__(
    self,
    monitor="val_loss",
    factor=0.1,
    patience=10,
    verbose=0,
    mode="auto",
    min_delta=1e-4,
    cooldown=0,
    min_lr=0.0,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/losses/losses.py
# Line: 668

def __init__(
    self,
    from_logits=False,
    label_smoothing=0.0,
    axis=-1,
    reduction="sum_over_batch_size",
    name="binary_crossentropy",
    dtype=None,

# ==================================================
# Line: 844

def __init__(
    self,
    apply_class_balancing=False,
    alpha=0.25,
    gamma=2.0,
    from_logits=False,
    label_smoothing=0.0,
    axis=-1,
    reduction="sum_over_batch_size",
    name="binary_focal_crossentropy",
    dtype=None,

# ==================================================
# Line: 960

def __init__(
    self,
    from_logits=False,
    label_smoothing=0.0,
    axis=-1,
    reduction="sum_over_batch_size",
    name="categorical_crossentropy",
    dtype=None,

# ==================================================
# Line: 1105

def __init__(
    self,
    alpha=0.25,
    gamma=2.0,
    from_logits=False,
    label_smoothing=0.0,
    axis=-1,
    reduction="sum_over_batch_size",
    name="categorical_focal_crossentropy",
    dtype=None,

# ==================================================
# Line: 1217

def __init__(
    self,
    from_logits=False,
    ignore_class=None,
    reduction="sum_over_batch_size",
    axis=-1,
    name="sparse_categorical_crossentropy",
    dtype=None,

# ==================================================
# Line: 1389

def __init__(
    self,
    alpha=0.5,
    beta=0.5,
    reduction="sum_over_batch_size",
    name="tversky",
    axis=None,
    dtype=None,

# ==================================================
# Line: 1477

def __init__(
    self,
    gamma=80.0,
    margin=0.4,
    remove_diagonal=True,
    reduction="sum_over_batch_size",
    name="circle",
    dtype=None,

# ==================================================
# Line: 2192

def categorical_focal_crossentropy(
    y_true,
    y_pred,
    alpha=0.25,
    gamma=2.0,
    from_logits=False,
    label_smoothing=0.0,
    axis=-1,

# ==================================================
# Line: 2397

def binary_focal_crossentropy(
    y_true,
    y_pred,
    apply_class_balancing=False,
    alpha=0.25,
    gamma=2.0,
    from_logits=False,
    label_smoothing=0.0,
    axis=-1,

# ==================================================
# Line: 2629

def circle(
    y_true,
    y_pred,
    ref_labels=None,
    ref_embeddings=None,
    remove_diagonal=True,
    gamma=80,
    margin=0.4,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/saving_lib.py
# Line: 769

def _load_state(
    saveable,
    weights_store,
    assets_store,
    inner_path,
    skip_mismatch=False,
    visited_saveables=None,
    failed_saveables=None,
    error_msgs=None,

# ==================================================
# Line: 897

def _load_container_state(
    container,
    weights_store,
    assets_store,
    inner_path,
    skip_mismatch,
    visited_saveables,
    failed_saveables,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/file_editor.py
# Line: 134

def _compare(
    target,
    ref_spec,
    inner_path,
    target_name,
    ref_name,
    error_count,
    match_count,
    checked_paths,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/datasets/reuters.py
# Line: 13

def load_data(
    path="reuters.npz",
    num_words=None,
    skip_top=0,
    maxlen=None,
    test_split=0.2,
    seed=113,
    start_char=1,
    oov_char=2,
    index_from=3,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/datasets/imdb.py
# Line: 13

def load_data(
    path="imdb.npz",
    num_words=None,
    skip_top=0,
    maxlen=None,
    seed=113,
    start_char=1,
    oov_char=2,
    index_from=3,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/compile_utils.py
# Line: 216

def _build_metrics_set(
    self, metrics, num_outputs, output_names, y_true, y_pred, argument_name

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/epoch_iterator.py
# Line: 50

def __init__(
    self,
    x,
    y=None,
    sample_weight=None,
    batch_size=None,
    steps_per_epoch=None,
    shuffle=False,
    class_weight=None,
    steps_per_execution=1,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/__init__.py
# Line: 18

def get_data_adapter(
    x,
    y=None,
    sample_weight=None,
    batch_size=None,
    steps_per_epoch=None,
    shuffle=False,
    class_weight=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/array_data_adapter.py
# Line: 15

def __init__(
    self,
    x,
    y=None,
    sample_weight=None,
    batch_size=None,
    steps=None,
    shuffle=False,
    class_weight=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/data_adapters/py_dataset_adapter_test.py
# Line: 19

def __init__(
    self,
    x_set,
    y_set,
    sample_weight=None,
    batch_size=32,
    delay=0,
    infinite=False,
    **kwargs,

# ==================================================
# Line: 136

def test_basic_flow(
    self,
    shuffle,
    dataset_type,
    infinite,
    workers=0,
    use_multiprocessing=False,
    max_queue_size=0,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/trainer.py
# Line: 41

def compile(
    self,
    optimizer="rmsprop",
    loss=None,
    loss_weights=None,
    metrics=None,
    weighted_metrics=None,
    run_eagerly=False,
    steps_per_execution=1,
    jit_compile="auto",
    auto_scale_loss=True,

# ==================================================
# Line: 403

def stateless_compute_loss(
    self,
    trainable_variables,
    non_trainable_variables,
    metrics_variables,
    x=None,
    y=None,
    y_pred=None,
    sample_weight=None,
    training=True,

# ==================================================
# Line: 512

def fit(
    self,
    x=None,
    y=None,
    batch_size=None,
    epochs=1,
    verbose="auto",
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0,
    steps_per_epoch=None,
    validation_steps=None,
    validation_batch_size=None,
    validation_freq=1,

# ==================================================
# Line: 714

def evaluate(
    self,
    x=None,
    y=None,
    batch_size=None,
    verbose="auto",
    sample_weight=None,
    steps=None,
    callbacks=None,
    return_dict=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/image.py
# Line: 221

def __init__(
    self,
    size,
    interpolation="bilinear",
    antialias=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    data_format=None,

# ==================================================
# Line: 273

def resize(
    images,
    size,
    interpolation="bilinear",
    antialias=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    data_format=None,

# ==================================================
# Line: 378

def _resize(
    images,
    size,
    interpolation="bilinear",
    antialias=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    data_format=None,

# ==================================================
# Line: 797

def __init__(
    self,
    top_padding=None,
    left_padding=None,
    bottom_padding=None,
    right_padding=None,
    target_height=None,
    target_width=None,
    data_format=None,

# ==================================================
# Line: 851

def pad_images(
    images,
    top_padding=None,
    left_padding=None,
    bottom_padding=None,
    right_padding=None,
    target_height=None,
    target_width=None,
    data_format=None,

# ==================================================
# Line: 921

def _pad_images(
    images,
    top_padding,
    left_padding,
    bottom_padding,
    right_padding,
    target_height,
    target_width,
    data_format=None,

# ==================================================
# Line: 1008

def __init__(
    self,
    top_cropping=None,
    left_cropping=None,
    bottom_cropping=None,
    right_cropping=None,
    target_height=None,
    target_width=None,
    data_format=None,

# ==================================================
# Line: 1076

def crop_images(
    images,
    top_cropping=None,
    left_cropping=None,
    bottom_cropping=None,
    right_cropping=None,
    target_height=None,
    target_width=None,
    data_format=None,

# ==================================================
# Line: 1142

def _crop_images(
    images,
    top_cropping,
    left_cropping,
    bottom_cropping,
    right_cropping,
    target_height,
    target_width,
    data_format=None,

# ==================================================
# Line: 1464

def __init__(
    self,
    alpha=20.0,
    sigma=5.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    seed=None,
    data_format=None,

# ==================================================
# Line: 1506

def elastic_transform(
    images,
    alpha=20.0,
    sigma=5.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    seed=None,
    data_format=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/nn_test.py
# Line: 39

def _dot_product_attention(
    query, key, value, bias=None, mask=None, scale=None, is_causal=False

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/numpy_test.py
# Line: 5290

def test_other_unary_symbolic_static_shape(
    self, op_function, op_class, np_op, init_kwargs, op_kwargs, input_shape

# ==================================================
# Line: 5307

def test_other_unary_symbolic_dynamic_shape(
    self, op_function, op_class, np_op, init_kwargs, op_kwargs, input_shape

# ==================================================
# Line: 5379

def test_other_unary_sparse_correctness(
    self, op_function, op_class, np_op, init_kwargs, op_kwargs, input_shape

# ==================================================
# Line: 5412

def test_binary_symbolic_static_shape(
    self, x_sparse, y_sparse, op_function, op_class, np_op, op_sparseness

# ==================================================
# Line: 5427

def test_binary_symbolic_dynamic_shape(
    self, x_sparse, y_sparse, op_function, op_class, np_op, op_sparseness

# ==================================================
# Line: 5444

def test_binary_correctness_sparse_tensor(
    self, x, y, op_function, op_class, np_op, op_sparseness, dtype

# ==================================================
# Line: 5465

def test_binary_correctness_indexed_slices(
    self, x, y, op_function, op_class, np_op, op_sparseness, dtype

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/nn.py
# Line: 1500

def separable_conv(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 1622

def conv_transpose(
    inputs,
    kernel,
    strides=1,
    padding="valid",
    output_padding=None,
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 2205

def batch_normalization(
    x, mean, variance, axis, offset=None, scale=None, epsilon=1e-3

# ==================================================
# Line: 2369

def ctc_decode(
    inputs,
    sequence_lengths,
    strategy="greedy",
    beam_width=100,
    top_paths=1,
    merge_repeated=True,
    mask_index=0,

# ==================================================
# Line: 2587

def call(
    self,
    query,
    key,
    value,
    bias=None,
    mask=None,
    scale=None,
    flash_attention=None,
    attn_logits_soft_cap=None,

# ==================================================
# Line: 2610

def compute_output_spec(
    self,
    query,
    key,
    value,
    bias=None,
    mask=None,
    scale=None,
    flash_attention=None,
    attn_logits_soft_cap=None,

# ==================================================
# Line: 2627

def dot_product_attention(
    query,
    key,
    value,
    bias=None,
    mask=None,
    scale=None,
    is_causal=False,
    flash_attention=None,
    attn_logits_soft_cap=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/math_test.py
# Line: 57

def _istft(
    x,
    sequence_length,
    sequence_stride,
    fft_length,
    length=None,
    window="hann",
    center=True,

# ==================================================
# Line: 438

def run_segment_reduce_test(
    self,
    segment_reduce_op,
    element_wise_reduce_method,
    num_indices,
    indices_high,
    data_dims=tuple(),
    num_segments=None,
    add_neg1_to_indices=False,
    sorted_indices=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/image_test.py
# Line: 697

def elastic_transform_np(
    images,
    alpha=20.0,
    sigma=5.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    seed=None,
    data_format=None,

# ==================================================
# Line: 1565

def test_pad_images(
    self,
    top_padding,
    left_padding,
    target_height,
    target_width,
    bottom_padding,
    right_padding,

# ==================================================
# Line: 1647

def test_crop_images(
    self,
    top_cropping,
    left_cropping,
    target_height,
    target_width,
    bottom_cropping,
    right_cropping,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/math.py
# Line: 804

def __init__(
    self,
    sequence_length,
    sequence_stride,
    fft_length,
    length=None,
    window="hann",
    center=True,

# ==================================================
# Line: 867

def istft(
    x,
    sequence_length,
    sequence_stride,
    fft_length,
    length=None,
    window="hann",
    center=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/operation_utils.py
# Line: 167

def compute_conv_output_shape(
    input_shape,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format="channels_last",
    dilation_rate=1,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/numpy.py
# Line: 3665

def linspace(
    start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0

# ==================================================
# Line: 4007

def logspace(start, stop, num=50, endpoint=True, base=10, dtype=None, axis=0):
    """Returns numbers spaced evenly on a log scale.

    In linear space, the sequence starts at `base ** start` and ends with
    `base ** stop` (see `endpoint` below).

    Args:
        start: The starting value of the sequence.
        stop: The final value of the sequence, unless `endpoint` is `False`.
            In that case, `num + 1` values are spaced over the interval in
            log-space, of which all but the last (a sequence of length `num`)
            are returned.
        num: Number of samples to generate. Defaults to `50`.
        endpoint: If `True`, `stop` is the last sample. Otherwise, it is not
            included. Defaults to `True`.
        base: The base of the log space. Defaults to `10`.
        dtype: The type of the output tensor.
        axis: The axis in the result to store the samples. Relevant only
            if start or stop are array-like.

    Note:
        Torch backend does not support `axis` argument.

    Returns:
        A tensor of evenly spaced samples on a log scale.
    """
    if any_symbolic_tensors((start, stop)):
        return Logspace(num, endpoint, base, dtype, axis)(start, stop)
    return backend.numpy.logspace(
        start,
        stop,
        num=num,
        endpoint=endpoint,
        base=base,
        dtype=dtype,
        axis=axis,
    )



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/models/model.py
# Line: 219

def summary(
    self,
    line_length=None,
    positions=None,
    print_fn=None,
    expand_nested=False,
    show_trainable=False,
    layer_range=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/jax_layer_test.py
# Line: 186

def _test_layer(
    self,
    model_name,
    layer_class,
    layer_init_kwargs,
    trainable_weights,
    trainable_params,
    non_trainable_weights,
    non_trainable_params,

# ==================================================
# Line: 452

def test_flax_layer(
    self,
    flax_model_class,
    flax_model_method,
    init_kwargs,
    trainable_weights,
    trainable_params,
    non_trainable_weights,
    non_trainable_params,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/dataset_utils.py
# Line: 483

def index_directory(
    directory,
    labels,
    formats,
    class_names=None,
    shuffle=True,
    seed=None,
    follow_links=False,
    verbose=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/summary_utils.py
# Line: 121

def print_summary(
    model,
    line_length=None,
    positions=None,
    print_fn=None,
    expand_nested=False,
    show_trainable=False,
    layer_range=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/numerical_utils.py
# Line: 104

def encode_categorical_inputs(
    inputs,
    output_mode,
    depth,
    dtype,
    sparse=False,
    count_weights=None,
    backend_module=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/timeseries_dataset_utils.py
# Line: 13

def timeseries_dataset_from_array(
    data,
    targets,
    sequence_length,
    sequence_stride=1,
    sampling_rate=1,
    batch_size=128,
    shuffle=False,
    seed=None,
    start_index=None,
    end_index=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/file_utils.py
# Line: 132

def get_file(
    fname=None,
    origin=None,
    untar=False,
    md5_hash=None,
    file_hash=None,
    cache_subdir="datasets",
    hash_algorithm="auto",
    extract=False,
    archive_format="auto",
    cache_dir=None,
    force_download=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/image_dataset_utils.py
# Line: 18

def image_dataset_from_directory(
    directory,
    labels="inferred",
    label_mode="int",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(256, 256),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    data_format=None,
    verbose=True,

# ==================================================
# Line: 363

def paths_and_labels_to_dataset(
    image_paths,
    image_size,
    num_channels,
    labels,
    label_mode,
    num_classes,
    interpolation,
    data_format,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    shuffle=False,
    shuffle_buffer_size=None,
    seed=None,

# ==================================================
# Line: 411

def load_image(
    path,
    image_size,
    num_channels,
    interpolation,
    data_format,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/audio_dataset_utils.py
# Line: 12

def audio_dataset_from_directory(
    directory,
    labels="inferred",
    label_mode="int",
    class_names=None,
    batch_size=32,
    sampling_rate=None,
    output_sequence_length=None,
    ragged=False,
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    follow_links=False,
    verbose=True,

# ==================================================
# Line: 278

def get_training_and_validation_dataset(
    file_paths,
    labels,
    validation_split,
    directory,
    label_mode,
    class_names,
    sampling_rate,
    output_sequence_length,
    ragged,
    shuffle=False,
    shuffle_buffer_size=None,
    seed=None,

# ==================================================
# Line: 340

def get_dataset(
    file_paths,
    labels,
    directory,
    validation_split,
    subset,
    label_mode,
    class_names,
    sampling_rate,
    output_sequence_length,
    ragged,
    shuffle=False,
    shuffle_buffer_size=None,
    seed=None,

# ==================================================
# Line: 399

def paths_and_labels_to_dataset(
    file_paths,
    labels,
    label_mode,
    num_classes,
    sampling_rate,
    output_sequence_length,
    ragged,
    shuffle=False,
    shuffle_buffer_size=None,
    seed=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/model_visualization.py
# Line: 195

def model_to_dot(
    model,
    show_shapes=False,
    show_dtype=False,
    show_layer_names=True,
    rankdir="TB",
    expand_nested=False,
    dpi=200,
    subgraph=False,
    show_layer_activations=False,
    show_trainable=False,
    **kwargs,

# ==================================================
# Line: 406

def plot_model(
    model,
    to_file="model.png",
    show_shapes=False,
    show_dtype=False,
    show_layer_names=False,
    rankdir="TB",
    expand_nested=False,
    dpi=200,
    show_layer_activations=False,
    show_trainable=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/text_dataset_utils.py
# Line: 14

def text_dataset_from_directory(
    directory,
    labels="inferred",
    label_mode="int",
    class_names=None,
    batch_size=32,
    max_length=None,
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    follow_links=False,
    verbose=True,

# ==================================================
# Line: 251

def paths_and_labels_to_dataset(
    file_paths,
    labels,
    label_mode,
    num_classes,
    max_length,
    shuffle=False,
    shuffle_buffer_size=None,
    seed=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/tf_utils.py
# Line: 95

def tf_encode_categorical_inputs(
    inputs,
    output_mode,
    depth,
    dtype="float32",
    sparse=False,
    count_weights=None,
    idf_weights=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/progbar.py
# Line: 26

def __init__(
    self,
    target,
    width=20,
    verbose=1,
    interval=0.05,
    stateful_metrics=None,
    unit_name="step",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/iou_metrics.py
# Line: 50

def __init__(
    self,
    num_classes,
    name=None,
    dtype=None,
    ignore_class=None,
    sparse_y_true=True,
    sparse_y_pred=True,
    axis=-1,

# ==================================================
# Line: 235

def __init__(
    self,
    num_classes,
    target_class_ids,
    name=None,
    dtype=None,
    ignore_class=None,
    sparse_y_true=True,
    sparse_y_pred=True,
    axis=-1,

# ==================================================
# Line: 504

def __init__(
    self,
    num_classes,
    name=None,
    dtype=None,
    ignore_class=None,
    sparse_y_true=True,
    sparse_y_pred=True,
    axis=-1,

# ==================================================
# Line: 621

def __init__(
    self,
    num_classes,
    target_class_ids,
    name=None,
    dtype=None,
    ignore_class=None,
    sparse_y_pred=False,
    axis=-1,

# ==================================================
# Line: 732

def __init__(
    self,
    num_classes,
    name=None,
    dtype=None,
    ignore_class=None,
    sparse_y_pred=False,
    axis=-1,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/f_score_metrics_test.py
# Line: 9

def _run_test(
    self,
    y_true,
    y_pred,
    sample_weights,
    average,
    beta,
    threshold,
    reference_result,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/regression_metrics_test.py
# Line: 303

def _run_test(
    self,
    y_true,
    y_pred,
    sample_weights,
    class_aggregation,
    num_regressors,
    reference_result,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/confusion_metrics.py
# Line: 1188

def __init__(
    self,
    num_thresholds=200,
    curve="ROC",
    summation_method="interpolation",
    name=None,
    dtype=None,
    thresholds=None,
    multi_label=False,
    num_labels=None,
    label_weights=None,
    from_logits=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/metrics/metrics_utils.py
# Line: 97

def _update_confusion_matrix_variables_optimized(
    variables_to_update,
    y_true,
    y_pred,
    thresholds,
    multi_label=False,
    sample_weights=None,
    label_weights=None,
    thresholds_with_epsilon=False,

# ==================================================
# Line: 341

def update_confusion_matrix_variables(
    variables_to_update,
    y_true,
    y_pred,
    thresholds,
    top_k=None,
    class_id=None,
    sample_weight=None,
    multi_label=False,
    label_weights=None,
    thresholds_distributed_evenly=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/adagrad.py
# Line: 35

def __init__(
    self,
    learning_rate=0.001,
    initial_accumulator_value=0.1,
    epsilon=1e-7,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="adagrad",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/adadelta.py
# Line: 40

def __init__(
    self,
    learning_rate=0.001,
    rho=0.95,
    epsilon=1e-7,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="adadelta",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/adafactor.py
# Line: 44

def __init__(
    self,
    learning_rate=0.001,
    beta_2_decay=-0.8,
    epsilon_1=1e-30,
    epsilon_2=1e-3,
    clip_threshold=1.0,
    relative_step=True,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="adafactor",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/ftrl.py
# Line: 78

def __init__(
    self,
    learning_rate=0.001,
    learning_rate_power=-0.5,
    initial_accumulator_value=0.1,
    l1_regularization_strength=0.0,
    l2_regularization_strength=0.0,
    l2_shrinkage_regularization_strength=0.0,
    beta=0.0,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="ftrl",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/adamw.py
# Line: 53

def __init__(
    self,
    learning_rate=0.001,
    weight_decay=0.004,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-7,
    amsgrad=False,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="adamw",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/nadam.py
# Line: 39

def __init__(
    self,
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-7,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="nadam",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/adamax.py
# Line: 53

def __init__(
    self,
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-7,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="adamax",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/adam.py
# Line: 43

def __init__(
    self,
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-7,
    amsgrad=False,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="adam",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/sgd.py
# Line: 43

def __init__(
    self,
    learning_rate=0.01,
    momentum=0.0,
    nesterov=False,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="SGD",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/lamb.py
# Line: 38

def __init__(
    self,
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-7,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="lamb",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/rmsprop.py
# Line: 53

def __init__(
    self,
    learning_rate=0.001,
    rho=0.9,
    momentum=0.0,
    epsilon=1e-7,
    centered=False,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="rmsprop",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/lion.py
# Line: 44

def __init__(
    self,
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.99,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="lion",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/muon.py
# Line: 77

def __init__(
    self,
    learning_rate=0.001,
    adam_beta_1=0.9,
    adam_beta_2=0.999,
    epsilon=1e-7,
    weight_decay=0.1,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="muon",
    exclude_layers=None,
    exclude_embeddings=True,
    muon_a=3.4445,
    muon_b=-4.7750,
    muon_c=2.0315,
    adam_lr_ratio=0.1,
    momentum=0.95,
    ns_steps=6,
    nesterov=True,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/base_optimizer.py
# Line: 68

def __init__(
    self,
    learning_rate,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name=None,
    **kwargs,

# ==================================================
# Line: 241

def add_variable(
    self,
    shape,
    initializer="zeros",
    dtype=None,
    aggregation="none",
    layout=None,
    name=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/schedules/learning_rate_schedule.py
# Line: 387

def __init__(
    self,
    initial_learning_rate,
    decay_steps,
    end_learning_rate=0.0001,
    power=1.0,
    cycle=False,
    name="PolynomialDecay",

# ==================================================
# Line: 669

def __init__(
    self,
    initial_learning_rate,
    decay_steps,
    alpha=0.0,
    name="CosineDecay",
    warmup_target=None,
    warmup_steps=0,

# ==================================================
# Line: 817

def __init__(
    self,
    initial_learning_rate,
    first_decay_steps,
    t_mul=2.0,
    m_mul=1.0,
    alpha=0.0,
    name="SGDRDecay",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/preprocessing/sequence.py
# Line: 55

def __init__(
    self,
    data,
    targets,
    length,
    sampling_rate=1,
    stride=1,
    start_index=0,
    end_index=None,
    shuffle=False,
    reverse=False,
    batch_size=128,

# ==================================================
# Line: 222

def skipgrams(
    sequence,
    vocabulary_size,
    window_size=4,
    negative_samples=1.0,
    shuffle=True,
    categorical=False,
    sampling_table=None,
    seed=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/preprocessing/image.py
# Line: 210

def set_processing_attrs(
    self,
    image_data_generator,
    target_size,
    color_mode,
    data_format,
    save_to_dir,
    save_prefix,
    save_format,
    subset,
    interpolation,
    keep_aspect_ratio,

# ==================================================
# Line: 401

def __init__(
    self,
    directory,
    image_data_generator,
    target_size=(256, 256),
    color_mode="rgb",
    classes=None,
    class_mode="categorical",
    batch_size=32,
    shuffle=True,
    seed=None,
    data_format=None,
    save_to_dir=None,
    save_prefix="",
    save_format="png",
    follow_links=False,
    subset=None,
    interpolation="nearest",
    keep_aspect_ratio=False,
    dtype=None,

# ==================================================
# Line: 522

def __init__(
    self,
    x,
    y,
    image_data_generator,
    batch_size=32,
    shuffle=False,
    sample_weight=None,
    seed=None,
    data_format=None,
    save_to_dir=None,
    save_prefix="",
    save_format="png",
    subset=None,
    ignore_class_split=False,
    dtype=None,

# ==================================================
# Line: 709

def __init__(
    self,
    dataframe,
    directory=None,
    image_data_generator=None,
    x_col="filename",
    y_col="class",
    weight_col=None,
    target_size=(256, 256),
    color_mode="rgb",
    classes=None,
    class_mode="categorical",
    batch_size=32,
    shuffle=True,
    seed=None,
    data_format="channels_last",
    save_to_dir=None,
    save_prefix="",
    save_format="png",
    subset=None,
    interpolation="nearest",
    keep_aspect_ratio=False,
    dtype="float32",
    validate_filenames=True,

# ==================================================
# Line: 953

def __init__(
    self,
    featurewise_center=False,
    samplewise_center=False,
    featurewise_std_normalization=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    zca_epsilon=1e-6,
    rotation_range=0,
    width_shift_range=0.0,
    height_shift_range=0.0,
    brightness_range=None,
    shear_range=0.0,
    zoom_range=0.0,
    channel_shift_range=0.0,
    fill_mode="nearest",
    cval=0.0,
    horizontal_flip=False,
    vertical_flip=False,
    rescale=None,
    preprocessing_function=None,
    data_format=None,
    validation_split=0.0,
    interpolation_order=1,
    dtype=None,

# ==================================================
# Line: 1089

def flow(
    self,
    x,
    y=None,
    batch_size=32,
    shuffle=True,
    sample_weight=None,
    seed=None,
    save_to_dir=None,
    save_prefix="",
    save_format="png",
    ignore_class_split=False,
    subset=None,

# ==================================================
# Line: 1120

def flow_from_directory(
    self,
    directory,
    target_size=(256, 256),
    color_mode="rgb",
    classes=None,
    class_mode="categorical",
    batch_size=32,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix="",
    save_format="png",
    follow_links=False,
    subset=None,
    interpolation="nearest",
    keep_aspect_ratio=False,

# ==================================================
# Line: 1159

def flow_from_dataframe(
    self,
    dataframe,
    directory=None,
    x_col="filename",
    y_col="class",
    weight_col=None,
    target_size=(256, 256),
    color_mode="rgb",
    classes=None,
    class_mode="categorical",
    batch_size=32,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix="",
    save_format="png",
    subset=None,
    interpolation="nearest",
    validate_filenames=True,
    **kwargs,

# ==================================================
# Line: 1551

def random_rotation(
    x,
    rg,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode="nearest",
    cval=0.0,
    interpolation_order=1,

# ==================================================
# Line: 1577

def random_shift(
    x,
    wrg,
    hrg,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode="nearest",
    cval=0.0,
    interpolation_order=1,

# ==================================================
# Line: 1607

def random_shear(
    x,
    intensity,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode="nearest",
    cval=0.0,
    interpolation_order=1,

# ==================================================
# Line: 1633

def random_zoom(
    x,
    zoom_range,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode="nearest",
    cval=0.0,
    interpolation_order=1,

# ==================================================
# Line: 1779

def apply_affine_transform(
    x,
    theta=0,
    tx=0,
    ty=0,
    shear=0,
    zx=1,
    zy=1,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode="nearest",
    cval=0.0,
    order=1,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/preprocessing/text.py
# Line: 54

def hashing_trick(
    text,
    n,
    hash_function=None,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=" ",
    analyzer=None,

# ==================================================
# Line: 85

def __init__(
    self,
    num_words=None,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=" ",
    char_level=False,
    oov_token=None,
    analyzer=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/legacy/backend.py
# Line: 243

def batch_normalization(x, mean, var, beta, gamma, axis=-1, epsilon=1e-3):
    """DEPRECATED."""
    return tf.nn.batch_normalization(x, mean, var, beta, gamma, epsilon)



# ==================================================
# Line: 542

def conv2d_transpose(
    x,
    kernel,
    output_shape,
    strides=(1, 1),
    padding="valid",
    data_format=None,
    dilation_rate=(1, 1),

# ==================================================
# Line: 1428

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,

# ==================================================
# Line: 1842

def separable_conv2d(
    x,
    depthwise_kernel,
    pointwise_kernel,
    strides=(1, 1),
    padding="valid",
    data_format=None,
    dilation_rate=(1, 1),

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/vgg16.py
# Line: 21

def VGG16(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="vgg16",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/resnet.py
# Line: 48

def ResNet(
    stack_fn,
    preact,
    use_bias,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="resnet",
    weights_name=None,

# ==================================================
# Line: 391

def ResNet50(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="resnet50",

# ==================================================
# Line: 431

def ResNet101(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="resnet101",

# ==================================================
# Line: 471

def ResNet152(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="resnet152",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/mobilenet_v3.py
# Line: 151

def MobileNetV3(
    stack_fn,
    last_point_ch,
    input_shape=None,
    alpha=1.0,
    model_type="large",
    minimalistic=False,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    classes=1000,
    pooling=None,
    dropout_rate=0.2,
    classifier_activation="softmax",
    include_preprocessing=True,
    name=None,

# ==================================================
# Line: 405

def MobileNetV3Small(
    input_shape=None,
    alpha=1.0,
    minimalistic=False,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    classes=1000,
    pooling=None,
    dropout_rate=0.2,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="MobileNetV3Small",

# ==================================================
# Line: 472

def MobileNetV3Large(
    input_shape=None,
    alpha=1.0,
    minimalistic=False,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    classes=1000,
    pooling=None,
    dropout_rate=0.2,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="MobileNetV3Large",

# ==================================================
# Line: 591

def _inverted_res_block(
    x, expansion, filters, kernel_size, stride, se_ratio, activation, block_id

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/densenet.py
# Line: 107

def DenseNet(
    blocks,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="densenet",

# ==================================================
# Line: 331

def DenseNet121(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="densenet121",

# ==================================================
# Line: 361

def DenseNet169(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="densenet169",

# ==================================================
# Line: 391

def DenseNet201(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="densenet201",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/inception_v3.py
# Line: 25

def InceptionV3(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="inception_v3",

# ==================================================
# Line: 383

def conv2d_bn(
    x, filters, num_row, num_col, padding="same", strides=(1, 1), name=None

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/efficientnet_v2.py
# Line: 605

def MBConvBlock(
    input_filters,
    output_filters,
    expand_ratio=1,
    kernel_size=3,
    strides=1,
    se_ratio=0.0,
    bn_momentum=0.9,
    activation="swish",
    survival_probability=0.8,
    name=None,

# ==================================================
# Line: 721

def FusedMBConvBlock(
    input_filters,
    output_filters,
    expand_ratio=1,
    kernel_size=3,
    strides=1,
    se_ratio=0.0,
    bn_momentum=0.9,
    activation="swish",
    survival_probability=0.8,
    name=None,

# ==================================================
# Line: 823

def EfficientNetV2(
    width_coefficient,
    depth_coefficient,
    default_size,
    dropout_rate=0.2,
    drop_connect_rate=0.2,
    depth_divisor=8,
    min_depth=8,
    bn_momentum=0.9,
    activation="swish",
    blocks_args="default",
    name="efficientnetv2",
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    weights_name=None,

# ==================================================
# Line: 1100

def EfficientNetV2B0(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-b0",

# ==================================================
# Line: 1134

def EfficientNetV2B1(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-b1",

# ==================================================
# Line: 1168

def EfficientNetV2B2(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-b2",

# ==================================================
# Line: 1202

def EfficientNetV2B3(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-b3",

# ==================================================
# Line: 1236

def EfficientNetV2S(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-s",

# ==================================================
# Line: 1270

def EfficientNetV2M(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-m",

# ==================================================
# Line: 1304

def EfficientNetV2L(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    include_preprocessing=True,
    name="efficientnetv2-l",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/vgg19.py
# Line: 21

def VGG19(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="vgg19",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/convnext.py
# Line: 331

def ConvNeXt(
    depths,
    projection_dims,
    drop_path_rate=0.0,
    layer_scale_init_value=1e-6,
    default_size=224,
    name="convnext",
    include_preprocessing=True,
    include_top=True,
    weights=None,
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    weights_name=None,

# ==================================================
# Line: 581

def ConvNeXtTiny(
    include_top=True,
    include_preprocessing=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="convnext_tiny",

# ==================================================
# Line: 617

def ConvNeXtSmall(
    include_top=True,
    include_preprocessing=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="convnext_small",

# ==================================================
# Line: 653

def ConvNeXtBase(
    include_top=True,
    include_preprocessing=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="convnext_base",

# ==================================================
# Line: 689

def ConvNeXtLarge(
    include_top=True,
    include_preprocessing=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="convnext_large",

# ==================================================
# Line: 725

def ConvNeXtXLarge(
    include_top=True,
    include_preprocessing=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="convnext_xlarge",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/mobilenet_v2.py
# Line: 22

def MobileNetV2(
    input_shape=None,
    alpha=1.0,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/xception.py
# Line: 25

def Xception(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="xception",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/inception_resnet_v2.py
# Line: 22

def InceptionResNetV2(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="inception_resnet_v2",

# ==================================================
# Line: 248

def conv2d_bn(
    x,
    filters,
    kernel_size,
    strides=1,
    padding="same",
    activation="relu",
    use_bias=False,
    name=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/nasnet.py
# Line: 20

def NASNet(
    input_shape=None,
    penultimate_filters=4032,
    num_blocks=6,
    stem_block_filters=96,
    skip_reduction=True,
    filter_multiplier=2,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    pooling=None,
    classes=1000,
    default_size=None,
    classifier_activation="softmax",
    name="NASNet",

# ==================================================
# Line: 321

def NASNetMobile(
    input_shape=None,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="nasnet_mobile",

# ==================================================
# Line: 417

def NASNetLarge(
    input_shape=None,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="nasnet_large",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/efficientnet.py
# Line: 208

def EfficientNet(
    width_coefficient,
    depth_coefficient,
    default_size,
    dropout_rate=0.2,
    drop_connect_rate=0.2,
    depth_divisor=8,
    activation="swish",
    blocks_args="default",
    name="efficientnet",
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    weights_name=None,

# ==================================================
# Line: 440

def block(
    inputs,
    activation="swish",
    drop_rate=0.0,
    name="",
    filters_in=32,
    filters_out=16,
    kernel_size=3,
    strides=1,
    expand_ratio=1,
    se_ratio=0.0,
    id_skip=True,

# ==================================================
# Line: 561

def EfficientNetB0(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="efficientnetb0",

# ==================================================
# Line: 594

def EfficientNetB1(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="efficientnetb1",

# ==================================================
# Line: 627

def EfficientNetB2(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="efficientnetb2",

# ==================================================
# Line: 660

def EfficientNetB3(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="efficientnetb3",

# ==================================================
# Line: 693

def EfficientNetB4(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="efficientnetb4",

# ==================================================
# Line: 726

def EfficientNetB5(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="efficientnetb5",

# ==================================================
# Line: 759

def EfficientNetB6(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="efficientnetb6",

# ==================================================
# Line: 792

def EfficientNetB7(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="efficientnetb7",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/mobilenet.py
# Line: 22

def MobileNet(
    input_shape=None,
    alpha=1.0,
    depth_multiplier=1,
    dropout=1e-3,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/applications/resnet_v2.py
# Line: 12

def ResNet50V2(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="resnet50v2",

# ==================================================
# Line: 54

def ResNet101V2(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="resnet101v2",

# ==================================================
# Line: 96

def ResNet152V2(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="resnet152v2",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/image.py
# Line: 7

def resize(
    image,
    size,
    interpolation="bilinear",
    antialias=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    data_format="channels_last",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/rnn.py
# Line: 1

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/nn.py
# Line: 348

def separable_conv(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 362

def conv_transpose(
    inputs,
    kernel,
    strides=1,
    padding="valid",
    output_padding=None,
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 424

def batch_normalization(
    x, mean, variance, axis, offset=None, scale=None, epsilon=1e-3

# ==================================================
# Line: 473

def ctc_decode(
    inputs,
    sequence_lengths,
    strategy="greedy",
    beam_width=100,
    top_paths=1,
    merge_repeated=True,
    mask_index=0,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/trainer.py
# Line: 149

def fit(
    self,
    x=None,
    y=None,
    batch_size=None,
    epochs=1,
    verbose="auto",
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0,
    steps_per_epoch=None,
    validation_steps=None,
    validation_batch_size=None,
    validation_freq=1,

# ==================================================
# Line: 227

def evaluate(
    self,
    x=None,
    y=None,
    batch_size=None,
    verbose="auto",
    sample_weight=None,
    steps=None,
    callbacks=None,
    return_dict=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/math.py
# Line: 83

def istft(
    x,
    sequence_length,
    sequence_stride,
    fft_length,
    length=None,
    window="hann",
    center=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/openvino/numpy.py
# Line: 950

def linspace(
    start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0

# ==================================================
# Line: 1035

def logspace(start, stop, num=50, endpoint=True, base=10, dtype=None, axis=0):
    raise NotImplementedError(
        "`logspace` is not supported with openvino backend"
    )



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/image.py
# Line: 130

def resize(
    images,
    size,
    interpolation="bilinear",
    antialias=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    data_format=None,

# ==================================================
# Line: 476

def _scale_and_translate(
    x, output_shape, spatial_dims, scale, translation, kernel, antialias

# ==================================================
# Line: 1016

def elastic_transform(
    images,
    alpha=20.0,
    sigma=5.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    seed=None,
    data_format=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/rnn.py
# Line: 6

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/nn.py
# Line: 466

def separable_conv(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 494

def conv_transpose(
    inputs,
    kernel,
    strides=1,
    padding="valid",
    output_padding=None,
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 693

def batch_normalization(
    x, mean, variance, axis, offset=None, scale=None, epsilon=1e-3

# ==================================================
# Line: 1035

def ctc_decode(
    inputs,
    sequence_lengths,
    strategy="greedy",
    beam_width=100,
    top_paths=1,
    merge_repeated=True,
    mask_index=0,

# ==================================================
# Line: 1109

def _dot_product_attention_xla(query, key, value, bias, mask, is_causal, scale):
    original_dtype = key.dtype
    logits_dtype = np.promote_types(query.dtype, np.float32)
    if backend.standardize_dtype(key.dtype) == "bfloat16":
        # `np.einsum` doesn't support bfloat16
        key = key.astype("float32")
        value = value.astype("float32")
    logits = np.einsum("BTNH,BSNH->BNTS", query, key)
    logits = logits.astype(logits_dtype)
    logits *= np.array(scale, dtype=logits.dtype)

    if bias is not None:
        logits = (logits + bias).astype(logits.dtype)

    padded_logits = _apply_masks(logits, mask, is_causal)

    # Softmax and it is always carried out in fp32.
    padded_logits = padded_logits.astype(np.float32)
    probs = softmax(padded_logits, axis=-1).astype(original_dtype)
    encoded_dtype = probs.dtype
    if backend.standardize_dtype(probs.dtype) == "bfloat16":
        # `np.einsum` doesn't support bfloat16
        probs = probs.astype("float32")
        value = value.astype("float32")
    encoded = np.einsum("BNTS,BSNH->BTNH", probs, value)
    encoded = encoded.astype(encoded_dtype)
    return encoded



# ==================================================
# Line: 1138

def dot_product_attention(
    query,
    key,
    value,
    bias=None,
    mask=None,
    scale=None,
    is_causal=False,
    flash_attention=None,
    attn_logits_soft_cap=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/trainer.py
# Line: 150

def fit(
    self,
    x=None,
    y=None,
    batch_size=None,
    epochs=1,
    verbose="auto",
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0,
    steps_per_epoch=None,
    validation_steps=None,
    validation_batch_size=None,
    validation_freq=1,

# ==================================================
# Line: 225

def evaluate(
    self,
    x=None,
    y=None,
    batch_size=None,
    verbose="auto",
    sample_weight=None,
    steps=None,
    callbacks=None,
    return_dict=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/math.py
# Line: 232

def istft(
    x,
    sequence_length,
    sequence_stride,
    fft_length,
    length=None,
    window="hann",
    center=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/numpy/numpy.py
# Line: 663

def linspace(
    start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0

# ==================================================
# Line: 746

def logspace(start, stop, num=50, endpoint=True, base=10, dtype=None, axis=0):
    if dtype is None:
        dtypes_to_resolve = [
            getattr(start, "dtype", type(start)),
            getattr(stop, "dtype", type(stop)),
            float,
        ]
        dtype = dtypes.result_type(*dtypes_to_resolve)
    return np.logspace(
        start,
        stop,
        num=num,
        endpoint=endpoint,
        base=base,
        dtype=dtype,
        axis=axis,
    )



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/image.py
# Line: 103

def resize(
    images,
    size,
    interpolation="bilinear",
    antialias=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    data_format=None,

# ==================================================
# Line: 782

def elastic_transform(
    images,
    alpha=20.0,
    sigma=5.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    seed=None,
    data_format=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/rnn.py
# Line: 6

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,

# ==================================================
# Line: 449

def gru(
    inputs,
    initial_state,
    mask,
    kernel,
    recurrent_kernel,
    bias,
    activation,
    recurrent_activation,
    return_sequences=False,
    go_backwards=False,
    unroll=False,
    time_major=False,
    reset_after=True,

# ==================================================
# Line: 669

def _cudnn_gru(
    inputs,
    initial_state,
    kernel,
    recurrent_kernel,
    bias,
    mask,
    time_major,
    go_backwards,
    return_sequences,

# ==================================================
# Line: 810

def lstm(
    inputs,
    initial_state_h,
    initial_state_c,
    mask,
    kernel,
    recurrent_kernel,
    bias,
    activation,
    recurrent_activation,
    return_sequences=False,
    go_backwards=False,
    unroll=False,
    time_major=False,

# ==================================================
# Line: 861

def _cudnn_lstm(
    inputs,
    initial_state_h,
    initial_state_c,
    kernel,
    recurrent_kernel,
    bias,
    mask,
    time_major,
    go_backwards,
    return_sequences,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/nn.py
# Line: 405

def separable_conv(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 468

def conv_transpose(
    inputs,
    kernel,
    strides=1,
    padding="valid",
    output_padding=None,
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 866

def batch_normalization(
    x, mean, variance, axis, offset=None, scale=None, epsilon=1e-3

# ==================================================
# Line: 912

def ctc_decode(
    inputs,
    sequence_lengths,
    strategy="greedy",
    beam_width=100,
    top_paths=1,
    merge_repeated=True,
    mask_index=0,

# ==================================================
# Line: 1019

def _dot_product_attention_xla(query, key, value, bias, mask, is_causal, scale):
    logits_dtype = backend.result_type(query.dtype, "float32")
    logits = tf.einsum("BTNH,BSNH->BNTS", query, key, optimize="optimal")
    logits = tf.cast(logits, logits_dtype)
    logits = tf.multiply(logits, tf.cast(scale, logits.dtype))

    if bias is not None:
        logits = tf.add(logits, tf.cast(bias, logits.dtype))

    padded_logits = _apply_masks(logits, mask, is_causal)

    # Softmax is always carried out in high precision.
    probs_dtype = backend.result_type(padded_logits.dtype, "float32")
    probs = tf.cast(
        tf.nn.softmax(tf.cast(padded_logits, probs_dtype), axis=-1), key.dtype
    )
    return tf.einsum("BNTS,BSNH->BTNH", probs, value, optimize="optimal")



# ==================================================
# Line: 1038

def dot_product_attention(
    query,
    key,
    value,
    bias=None,
    mask=None,
    scale=None,
    is_causal=False,
    flash_attention=None,
    attn_logits_soft_cap=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/trainer.py
# Line: 293

def fit(
    self,
    x=None,
    y=None,
    batch_size=None,
    epochs=1,
    verbose="auto",
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0,
    steps_per_epoch=None,
    validation_steps=None,
    validation_batch_size=None,
    validation_freq=1,

# ==================================================
# Line: 434

def evaluate(
    self,
    x=None,
    y=None,
    batch_size=None,
    verbose="auto",
    sample_weight=None,
    steps=None,
    callbacks=None,
    return_dict=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/math.py
# Line: 204

def istft(
    x,
    sequence_length,
    sequence_stride,
    fft_length,
    length=None,
    window="hann",
    center=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/numpy.py
# Line: 1575

def linspace(
    start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0

# ==================================================
# Line: 1697

def logspace(start, stop, num=50, endpoint=True, base=10, dtype=None, axis=0):
    result = linspace(
        start=start,
        stop=stop,
        num=num,
        endpoint=endpoint,
        dtype=dtype,
        axis=axis,
    )
    return tf.pow(tf.cast(base, result.dtype), result)



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/keras_tensor.py
# Line: 30

def __init__(
    self,
    shape,
    dtype="float32",
    sparse=False,
    ragged=False,
    record_history=True,
    name=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/backend_utils.py
# Line: 215

def compute_conv_transpose_output_shape(
    input_shape,
    kernel_size,
    filters,
    strides,
    padding,
    output_padding=None,
    data_format="channels_last",
    dilation_rate=1,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/common/variables.py
# Line: 92

def __init__(
    self,
    initializer,
    shape=None,
    dtype=None,
    trainable=True,
    autocast=True,
    aggregation="none",
    synchronization="auto",
    name=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/image.py
# Line: 133

def resize(
    images,
    size,
    interpolation="bilinear",
    antialias=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    data_format=None,

# ==================================================
# Line: 735

def elastic_transform(
    images,
    alpha=20.0,
    sigma=5.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    seed=None,
    data_format=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/rnn.py
# Line: 10

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/nn.py
# Line: 412

def separable_conv(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 440

def conv_transpose(
    inputs,
    kernel,
    strides=1,
    padding="valid",
    output_padding=None,
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 648

def batch_normalization(
    x, mean, variance, axis, offset=None, scale=None, epsilon=1e-3

# ==================================================
# Line: 977

def ctc_decode(
    inputs,
    sequence_lengths,
    strategy="greedy",
    beam_width=100,
    top_paths=1,
    merge_repeated=True,
    mask_index=0,

# ==================================================
# Line: 1104

def _dot_product_attention_core(
    query, key, value, bias, mask, is_causal, scale

# ==================================================
# Line: 1124

def wrap_flash_attention(
    query,
    key,
    value,
    decoder_segment_ids,
    custom_mask=None,
    attn_logits_soft_cap=None,
    head_shards=1,
    q_seq_shards=1,

# ==================================================
# Line: 1191

def dot_product_attention(
    query,
    key,
    value,
    bias=None,
    mask=None,
    scale=None,
    is_causal=False,
    flash_attention=None,
    attn_logits_soft_cap=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/trainer.py
# Line: 31

def compute_loss_and_updates(
    self,
    trainable_variables,
    non_trainable_variables,
    metrics_variables,
    x,
    y,
    sample_weight,
    training=False,
    optimizer_variables=None,

# ==================================================
# Line: 90

def _update_metrics_variables(
    self, metrics_variables, unscaled_loss, x, y, y_pred, sample_weight

# ==================================================
# Line: 326

def fit(
    self,
    x=None,
    y=None,
    batch_size=None,
    epochs=1,
    verbose="auto",
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0,
    steps_per_epoch=None,
    validation_steps=None,
    validation_batch_size=None,
    validation_freq=1,

# ==================================================
# Line: 516

def evaluate(
    self,
    x=None,
    y=None,
    batch_size=None,
    verbose="auto",
    sample_weight=None,
    steps=None,
    callbacks=None,
    return_dict=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/math.py
# Line: 201

def istft(
    x,
    sequence_length,
    sequence_stride,
    fft_length,
    length=None,
    window="hann",
    center=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/jax/numpy.py
# Line: 780

def linspace(
    start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0

# ==================================================
# Line: 852

def logspace(start, stop, num=50, endpoint=True, base=10, dtype=None, axis=0):
    return jnp.logspace(
        start,
        stop,
        num=num,
        endpoint=endpoint,
        base=base,
        dtype=dtype,
        axis=axis,
    )



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/image.py
# Line: 177

def resize(
    images,
    size,
    interpolation="bilinear",
    antialias=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    data_format=None,

# ==================================================
# Line: 901

def elastic_transform(
    images,
    alpha=20.0,
    sigma=5.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    seed=None,
    data_format=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/rnn.py
# Line: 9

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,

# ==================================================
# Line: 548

def lstm(
    inputs,
    initial_state_h,
    initial_state_c,
    mask,
    kernel,
    recurrent_kernel,
    bias,
    activation,
    recurrent_activation,
    return_sequences=False,
    go_backwards=False,
    unroll=False,
    batch_first=True,

# ==================================================
# Line: 624

def _cudnn_lstm(
    inputs,
    initial_state_h,
    initial_state_c,
    kernel,
    recurrent_kernel,
    bias,
    mask,
    batch_first,
    go_backwards,
    return_sequences,
    device,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/nn.py
# Line: 560

def separable_conv(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 587

def conv_transpose(
    inputs,
    kernel,
    strides=1,
    padding="valid",
    output_padding=None,
    data_format=None,
    dilation_rate=1,

# ==================================================
# Line: 821

def batch_normalization(
    x, mean, variance, axis, offset=None, scale=None, epsilon=1e-3

# ==================================================
# Line: 920

def ctc_decode(
    inputs,
    sequence_lengths,
    strategy="greedy",
    beam_width=100,
    top_paths=1,
    merge_repeated=True,
    mask_index=0,

# ==================================================
# Line: 1022

def dot_product_attention(
    query,
    key,
    value,
    bias=None,
    mask=None,
    scale=None,
    is_causal=False,
    flash_attention=None,
    attn_logits_soft_cap=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/trainer.py
# Line: 168

def fit(
    self,
    x=None,
    y=None,
    batch_size=None,
    epochs=1,
    verbose="auto",
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0,
    steps_per_epoch=None,
    validation_steps=None,
    validation_batch_size=None,
    validation_freq=1,

# ==================================================
# Line: 324

def evaluate(
    self,
    x=None,
    y=None,
    batch_size=None,
    verbose="auto",
    sample_weight=None,
    steps=None,
    callbacks=None,
    return_dict=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/math.py
# Line: 287

def istft(
    x,
    sequence_length,
    sequence_stride,
    fft_length,
    length=None,
    window="hann",
    center=True,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/numpy.py
# Line: 872

def linspace(
    start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0

# ==================================================
# Line: 973

def logspace(start, stop, num=50, endpoint=True, base=10, dtype=None, axis=0):
    if axis != 0:
        raise ValueError(
            "torch.logspace does not support an `axis` argument. "
            f"Received axis={axis}"
        )
    if dtype is None:
        dtypes_to_resolve = [
            getattr(start, "dtype", type(start)),
            getattr(stop, "dtype", type(stop)),
            float,
        ]
        dtype = dtypes.result_type(*dtypes_to_resolve)
    dtype = to_torch_dtype(dtype)

    if endpoint is False:
        stop = stop - ((stop - start) / num)
    if hasattr(start, "__len__") and hasattr(stop, "__len__"):
        start = convert_to_tensor(start, dtype=dtype)
        stop = convert_to_tensor(stop, dtype=dtype)
        steps = torch.arange(num, dtype=dtype, device=get_device()) / (num - 1)

        # reshape `steps` to allow for broadcasting
        for i in range(start.ndim):
            steps = steps.unsqueeze(-1)

        # increments from `start` to `stop` in each dimension
        linspace = start[None] + steps * (stop - start)[None]
        logspace = base**linspace
    else:
        compute_dtype = dtype
        # TODO: torch.logspace doesn't support float16 with cpu
        if get_device() == "cpu" and dtype == torch.float16:
            compute_dtype = torch.float32
        logspace = cast(
            torch.logspace(
                start=start,
                end=stop,
                steps=num,
                base=base,
                dtype=compute_dtype,
                device=get_device(),
            ),
            dtype,
        )
    return logspace



# ==================================================
# File: /root/ecooptimizer/keras/keras/src/export/tfsm_layer.py
# Line: 48

def __init__(
    self,
    filepath,
    call_endpoint="serve",
    call_training_endpoint=None,
    trainable=True,
    name=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/conv_lstm2d.py
# Line: 123

def __init__(
    self,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    activation="tanh",
    recurrent_activation="sigmoid",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    unit_forget_bias=True,
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/conv_lstm3d.py
# Line: 122

def __init__(
    self,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    activation="tanh",
    recurrent_activation="sigmoid",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    unit_forget_bias=True,
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/simple_rnn.py
# Line: 79

def __init__(
    self,
    units,
    activation="tanh",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    **kwargs,

# ==================================================
# Line: 296

def __init__(
    self,
    units,
    activation="tanh",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    unroll=False,
    seed=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/rnn.py
# Line: 174

def __init__(
    self,
    cell,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    unroll=False,
    zero_output_for_mask=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/lstm.py
# Line: 88

def __init__(
    self,
    units,
    activation="tanh",
    recurrent_activation="sigmoid",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    unit_forget_bias=True,
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    **kwargs,

# ==================================================
# Line: 448

def __init__(
    self,
    units,
    activation="tanh",
    recurrent_activation="sigmoid",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    unit_forget_bias=True,
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    unroll=False,
    use_cudnn="auto",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/conv_lstm.py
# Line: 85

def __init__(
    self,
    rank,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    activation="tanh",
    recurrent_activation="sigmoid",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    unit_forget_bias=True,
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    **kwargs,

# ==================================================
# Line: 464

def __init__(
    self,
    rank,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    activation="tanh",
    recurrent_activation="sigmoid",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    unit_forget_bias=True,
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/gru.py
# Line: 86

def __init__(
    self,
    units,
    activation="tanh",
    recurrent_activation="sigmoid",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    reset_after=True,
    seed=None,
    **kwargs,

# ==================================================
# Line: 465

def __init__(
    self,
    units,
    activation="tanh",
    recurrent_activation="sigmoid",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    unroll=False,
    reset_after=True,
    use_cudnn="auto",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/conv_lstm1d.py
# Line: 123

def __init__(
    self,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    activation="tanh",
    recurrent_activation="sigmoid",
    use_bias=True,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="orthogonal",
    bias_initializer="zeros",
    unit_forget_bias=True,
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/merging/merging_test.py
# Line: 104

def test_correctness_static(
    self,
    layer_class,
    np_op,
    init_kwargs={},
    input_shape=(2, 4, 5),
    expected_output_shape=(2, 4, 5),
    skip_mask_test=False,

# ==================================================
# Line: 142

def test_correctness_dynamic(
    self,
    layer_class,
    np_op,
    init_kwargs={},
    input_shape=(2, 4, 5),
    expected_output_shape=(2, 4, 5),
    skip_mask_test=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv3d.py
# Line: 95

def __init__(
    self,
    filters,
    kernel_size,
    strides=(1, 1, 1),
    padding="valid",
    data_format=None,
    dilation_rate=(1, 1, 1),
    groups=1,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv1d_transpose.py
# Line: 94

def __init__(
    self,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/separable_conv2d.py
# Line: 99

def __init__(
    self,
    filters,
    kernel_size,
    strides=(1, 1),
    padding="valid",
    data_format=None,
    dilation_rate=(1, 1),
    depth_multiplier=1,
    activation=None,
    use_bias=True,
    depthwise_initializer="glorot_uniform",
    pointwise_initializer="glorot_uniform",
    bias_initializer="zeros",
    depthwise_regularizer=None,
    pointwise_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    depthwise_constraint=None,
    pointwise_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/depthwise_conv_test.py
# Line: 18

def np_depthwise_conv1d(
    x,
    kernel_weights,
    bias_weights,
    strides,
    padding,
    data_format,
    dilation_rate,

# ==================================================
# Line: 89

def np_depthwise_conv2d(
    x,
    kernel_weights,
    bias_weights,
    strides,
    padding,
    data_format,
    dilation_rate,

# ==================================================
# Line: 203

def test_depthwise_conv1d_basic(
    self,
    depth_multiplier,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    input_shape,
    output_shape,

# ==================================================
# Line: 265

def test_depthwise_conv2d_basic(
    self,
    depth_multiplier,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    input_shape,
    output_shape,

# ==================================================
# Line: 366

def test_depthwise_conv1d(
    self,
    depth_multiplier,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,

# ==================================================
# Line: 431

def test_depthwise_conv2d(
    self,
    depth_multiplier,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/separable_conv_test.py
# Line: 54

def test_separable_conv1d_basic(
    self,
    depth_multiplier,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    input_shape,
    output_shape,

# ==================================================
# Line: 121

def test_separable_conv2d_basic(
    self,
    depth_multiplier,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    input_shape,
    output_shape,

# ==================================================
# Line: 241

def test_separable_conv1d(
    self,
    depth_multiplier,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,

# ==================================================
# Line: 328

def test_separable_conv2d(
    self,
    depth_multiplier,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv_test.py
# Line: 25

def np_conv1d(
    x,
    kernel_weights,
    bias_weights,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,

# ==================================================
# Line: 98

def np_conv2d(
    x,
    kernel_weights,
    bias_weights,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,

# ==================================================
# Line: 179

def np_conv3d(
    x,
    kernel_weights,
    bias_weights,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,

# ==================================================
# Line: 328

def test_conv1d_basic(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,
    input_shape,
    output_shape,

# ==================================================
# Line: 395

def test_conv2d_basic(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,
    input_shape,
    output_shape,

# ==================================================
# Line: 462

def test_conv3d_basic(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,
    input_shape,
    output_shape,

# ==================================================
# Line: 628

def test_enable_lora(
    self,
    conv_cls,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,
    input_shape,
    output_shape,

# ==================================================
# Line: 854

def test_conv1d(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,

# ==================================================
# Line: 952

def test_conv2d(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,

# ==================================================
# Line: 1041

def test_conv3d(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    data_format,
    dilation_rate,
    groups,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/depthwise_conv1d.py
# Line: 100

def __init__(
    self,
    kernel_size,
    strides=1,
    padding="valid",
    depth_multiplier=1,
    data_format=None,
    dilation_rate=1,
    activation=None,
    use_bias=True,
    depthwise_initializer="glorot_uniform",
    bias_initializer="zeros",
    depthwise_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    depthwise_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv1d.py
# Line: 95

def __init__(
    self,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    groups=1,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv2d.py
# Line: 98

def __init__(
    self,
    filters,
    kernel_size,
    strides=(1, 1),
    padding="valid",
    data_format=None,
    dilation_rate=(1, 1),
    groups=1,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/base_separable_conv.py
# Line: 78

def __init__(
    self,
    rank,
    depth_multiplier,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    activation=None,
    use_bias=True,
    depthwise_initializer="glorot_uniform",
    pointwise_initializer="glorot_uniform",
    bias_initializer="zeros",
    depthwise_regularizer=None,
    pointwise_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    depthwise_constraint=None,
    pointwise_constraint=None,
    bias_constraint=None,
    trainable=True,
    name=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/base_depthwise_conv.py
# Line: 84

def __init__(
    self,
    rank,
    depth_multiplier,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    activation=None,
    use_bias=True,
    depthwise_initializer="glorot_uniform",
    bias_initializer="zeros",
    depthwise_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    depthwise_constraint=None,
    bias_constraint=None,
    trainable=True,
    name=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/separable_conv1d.py
# Line: 98

def __init__(
    self,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    depth_multiplier=1,
    activation=None,
    use_bias=True,
    depthwise_initializer="glorot_uniform",
    pointwise_initializer="glorot_uniform",
    bias_initializer="zeros",
    depthwise_regularizer=None,
    pointwise_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    depthwise_constraint=None,
    pointwise_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv_transpose_test.py
# Line: 19

def np_conv1d_transpose(
    x,
    kernel_weights,
    bias_weights,
    strides,
    padding,
    output_padding,
    data_format,
    dilation_rate,

# ==================================================
# Line: 92

def np_conv2d_transpose(
    x,
    kernel_weights,
    bias_weights,
    strides,
    padding,
    output_padding,
    data_format,
    dilation_rate,

# ==================================================
# Line: 181

def np_conv3d_transpose(
    x,
    kernel_weights,
    bias_weights,
    strides,
    padding,
    output_padding,
    data_format,
    dilation_rate,

# ==================================================
# Line: 326

def test_conv1d_transpose_basic(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    output_padding,
    data_format,
    dilation_rate,
    input_shape,
    output_shape,

# ==================================================
# Line: 404

def test_conv2d_transpose_basic(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    output_padding,
    data_format,
    dilation_rate,
    input_shape,
    output_shape,

# ==================================================
# Line: 477

def test_conv3d_transpose_basic(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    output_padding,
    data_format,
    dilation_rate,
    input_shape,
    output_shape,

# ==================================================
# Line: 579

def test_conv1d_transpose(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    output_padding,
    data_format,
    dilation_rate,

# ==================================================
# Line: 659

def test_conv2d_transpose(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    output_padding,
    data_format,
    dilation_rate,

# ==================================================
# Line: 730

def test_conv3d_transpose(
    self,
    filters,
    kernel_size,
    strides,
    padding,
    output_padding,
    data_format,
    dilation_rate,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv3d_transpose.py
# Line: 101

def __init__(
    self,
    filters,
    kernel_size,
    strides=(1, 1, 1),
    padding="valid",
    data_format=None,
    dilation_rate=(1, 1, 1),
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/depthwise_conv2d.py
# Line: 101

def __init__(
    self,
    kernel_size,
    strides=(1, 1),
    padding="valid",
    depth_multiplier=1,
    data_format=None,
    dilation_rate=(1, 1),
    activation=None,
    use_bias=True,
    depthwise_initializer="glorot_uniform",
    bias_initializer="zeros",
    depthwise_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    depthwise_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/conv2d_transpose.py
# Line: 96

def __init__(
    self,
    filters,
    kernel_size,
    strides=(1, 1),
    padding="valid",
    data_format=None,
    dilation_rate=(1, 1),
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/base_conv.py
# Line: 90

def __init__(
    self,
    rank,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
    groups=1,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    lora_rank=None,
    lora_alpha=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/convolutional/base_conv_transpose.py
# Line: 71

def __init__(
    self,
    rank,
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    output_padding=None,
    data_format=None,
    dilation_rate=1,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    trainable=True,
    name=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/pooling/max_pooling_test.py
# Line: 143

def test_max_pooling1d(
    self,
    pool_size,
    strides,
    padding,
    data_format,
    input_shape,
    output_shape,

# ==================================================
# Line: 174

def test_max_pooling2d(
    self,
    pool_size,
    strides,
    padding,
    data_format,
    input_shape,
    output_shape,

# ==================================================
# Line: 212

def test_max_pooling3d(
    self,
    pool_size,
    strides,
    padding,
    data_format,
    input_shape,
    output_shape,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/pooling/average_pooling_test.py
# Line: 144

def test_average_pooling1d(
    self,
    pool_size,
    strides,
    padding,
    data_format,
    input_shape,
    output_shape,

# ==================================================
# Line: 179

def test_average_pooling2d(
    self,
    pool_size,
    strides,
    padding,
    data_format,
    input_shape,
    output_shape,

# ==================================================
# Line: 217

def test_average_pooling3d(
    self,
    pool_size,
    strides,
    padding,
    data_format,
    input_shape,
    output_shape,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/pooling/base_pooling.py
# Line: 12

def __init__(
    self,
    pool_size,
    strides,
    pool_dimensions,
    pool_mode="max",
    padding="valid",
    data_format=None,
    name=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/multi_head_attention.py
# Line: 103

def __init__(
    self,
    num_heads,
    key_dim,
    value_dim=None,
    dropout=0.0,
    use_bias=True,
    output_shape=None,
    attention_axes=None,
    flash_attention=None,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    seed=None,
    **kwargs,

# ==================================================
# Line: 413

def _compute_attention(
    self,
    query,
    key,
    value,
    attention_mask=None,
    training=None,
    return_attention_scores=False,

# ==================================================
# Line: 514

def call(
    self,
    query,
    value,
    key=None,
    query_mask=None,
    value_mask=None,
    key_mask=None,
    attention_mask=None,
    return_attention_scores=False,
    training=None,
    use_causal_mask=False,

# ==================================================
# Line: 575

def _compute_attention_mask(
    self,
    query,
    value,
    query_mask=None,
    value_mask=None,
    key_mask=None,
    attention_mask=None,
    use_causal_mask=False,

# ==================================================
# Line: 698

def compute_output_spec(
    self,
    query,
    value,
    key=None,
    query_mask=None,
    value_mask=None,
    key_mask=None,
    attention_mask=None,
    return_attention_scores=False,
    training=None,
    use_causal_mask=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/attention/grouped_query_attention.py
# Line: 90

def __init__(
    self,
    head_dim,
    num_query_heads,
    num_key_value_heads,
    dropout=0.0,
    use_bias=True,
    flash_attention=None,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    seed=None,
    **kwargs,

# ==================================================
# Line: 224

def call(
    self,
    query,
    value,
    key=None,
    query_mask=None,
    value_mask=None,
    key_mask=None,
    attention_mask=None,
    return_attention_scores=False,
    training=None,
    use_causal_mask=False,

# ==================================================
# Line: 278

def _compute_attention_mask(
    self,
    query,
    value,
    query_mask=None,
    value_mask=None,
    key_mask=None,
    attention_mask=None,
    use_causal_mask=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/normalization/batch_normalization.py
# Line: 124

def __init__(
    self,
    axis=-1,
    momentum=0.99,
    epsilon=1e-3,
    center=True,
    scale=True,
    beta_initializer="zeros",
    gamma_initializer="ones",
    moving_mean_initializer="zeros",
    moving_variance_initializer="ones",
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None,
    synchronized=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/normalization/group_normalization.py
# Line: 67

def __init__(
    self,
    groups=32,
    axis=-1,
    epsilon=1e-3,
    center=True,
    scale=True,
    beta_initializer="zeros",
    gamma_initializer="ones",
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/normalization/layer_normalization.py
# Line: 109

def __init__(
    self,
    axis=-1,
    epsilon=1e-3,
    center=True,
    scale=True,
    rms_scaling=False,
    beta_initializer="zeros",
    gamma_initializer="ones",
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/index_lookup.py
# Line: 90

def __init__(
    self,
    max_tokens,
    num_oov_indices,
    mask_token,
    oov_token,
    vocabulary_dtype,
    vocabulary=None,
    idf_weights=None,
    invert=False,
    output_mode="int",
    sparse=False,
    pad_to_max_tokens=False,
    name=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/stft_spectrogram_test.py
# Line: 17

def _calc_spectrograms(
    x, mode, scaling, window, periodic, frame_length, frame_step, fft_length

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/mel_spectrogram.py
# Line: 83

def __init__(
    self,
    fft_length=2048,
    sequence_stride=512,
    sequence_length=None,
    window="hann",
    sampling_rate=16000,
    num_mel_bins=128,
    min_freq=20.0,
    max_freq=None,
    power_to_db=True,
    top_db=80.0,
    mag_exp=2.0,
    min_power=1e-10,
    ref_power=1.0,
    **kwargs,

# ==================================================
# Line: 192

def linear_to_mel_weight_matrix(
    self,
    num_mel_bins=20,
    num_spectrogram_bins=129,
    sampling_rate=8000,
    lower_edge_hertz=125.0,
    upper_edge_hertz=3800.0,
    dtype="float32",

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/integer_lookup.py
# Line: 297

def __init__(
    self,
    max_tokens=None,
    num_oov_indices=1,
    mask_token=None,
    oov_token=-1,
    vocabulary=None,
    vocabulary_dtype="int64",
    idf_weights=None,
    invert=False,
    output_mode="int",
    sparse=False,
    pad_to_max_tokens=False,
    name=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/string_lookup.py
# Line: 294

def __init__(
    self,
    max_tokens=None,
    num_oov_indices=1,
    mask_token=None,
    oov_token="[UNK]",
    vocabulary=None,
    idf_weights=None,
    invert=False,
    output_mode="int",
    pad_to_max_tokens=False,
    sparse=False,
    encoding="utf-8",
    name=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/stft_spectrogram.py
# Line: 134

def __init__(
    self,
    mode="log",
    frame_length=256,
    frame_step=None,
    fft_length=None,
    window="hann",
    periodic=False,
    scaling="density",
    padding="valid",
    expand_dims=False,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/feature_space.py
# Line: 377

def __init__(
    self,
    features,
    output_mode="concat",
    crosses=None,
    crossing_dim=32,
    hashing_dim=32,
    num_discretization_bins=32,
    name=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/mel_spectrogram_test.py
# Line: 58

def test_output_shape(
    self,
    input_shape,
    num_mel_bins,
    sequence_stride,
    fft_length,
    sampling_rate,
    all_zero,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/aug_mix.py
# Line: 76

def __init__(
    self,
    value_range=(0, 255),
    num_chains=3,
    chain_depth=3,
    factor=0.3,
    alpha=1.0,
    all_ops=True,
    interpolation="bilinear",
    seed=None,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur.py
# Line: 40

def __init__(
    self,
    factor=1.0,
    kernel_size=3,
    sigma=1.0,
    value_range=(0, 255),
    data_format=None,
    seed=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_rotation.py
# Line: 83

def __init__(
    self,
    factor,
    fill_mode="reflect",
    interpolation="bilinear",
    seed=None,
    fill_value=0.0,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_erasing.py
# Line: 46

def __init__(
    self,
    factor=1.0,
    scale=(0.02, 0.33),
    fill_value=None,
    value_range=(0, 255),
    seed=None,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/bounding_box.py
# Line: 22

def convert_format(
    self,
    boxes,
    source,
    target,
    height=None,
    width=None,
    dtype="float32",

# ==================================================
# Line: 155

def affine(
    self,
    boxes,
    angle,
    translate_x,
    translate_y,
    scale,
    shear_x,
    shear_y,
    height,
    width,
    center_x=None,
    center_y=None,

# ==================================================
# Line: 400

def _compute_inverse_affine_matrix(
    self,
    center_x,
    center_y,
    angle,
    translate_x,
    translate_y,
    scale,
    shear_x,
    shear_y,
    height,
    width,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/converters.py
# Line: 117

def affine_transform(
    boxes,
    angle,
    translate_x,
    translate_y,
    scale,
    shear_x,
    shear_y,
    height,
    width,
    center_x=None,
    center_y=None,
    bounding_box_format="xyxy",

# ==================================================
# Line: 256

def encode_box_to_deltas(
    anchors,
    boxes,
    anchor_format,
    box_format,
    encoding_format="center_yxhw",
    variance=None,
    image_shape=None,

# ==================================================
# Line: 348

def decode_deltas_to_boxes(
    anchors,
    boxes_delta,
    anchor_format,
    box_format,
    encoded_format="center_yxhw",
    variance=None,
    image_shape=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/rand_augment.py
# Line: 54

def __init__(
    self,
    value_range=(0, 255),
    num_ops=2,
    factor=0.5,
    interpolation="bilinear",
    seed=None,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/resizing.py
# Line: 73

def __init__(
    self,
    height,
    width,
    interpolation="bilinear",
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    fill_mode="constant",
    fill_value=0.0,
    antialias=False,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py
# Line: 108

def __init__(
    self,
    height_factor,
    width_factor=None,
    fill_mode="reflect",
    interpolation="bilinear",
    seed=None,
    fill_value=0.0,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_translation.py
# Line: 100

def __init__(
    self,
    height_factor,
    width_factor,
    fill_mode="reflect",
    interpolation="bilinear",
    seed=None,
    fill_value=0.0,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py
# Line: 320

def _compute_affine_matrix(
    self,
    center_x,
    center_y,
    angle,
    translate_x,
    translate_y,
    scale,
    shear_x,
    shear_y,
    height,
    width,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_shear.py
# Line: 72

def __init__(
    self,
    x_factor=0.0,
    y_factor=0.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    data_format=None,
    seed=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_color_jitter.py
# Line: 62

def __init__(
    self,
    value_range=(0, 255),
    brightness_factor=None,
    contrast_factor=None,
    saturation_factor=None,
    hue_factor=None,
    seed=None,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_elastic_transform.py
# Line: 75

def __init__(
    self,
    factor=1.0,
    scale=1.0,
    interpolation="bilinear",
    fill_mode="reflect",
    fill_value=0.0,
    value_range=(0, 255),
    seed=None,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_perspective.py
# Line: 49

def __init__(
    self,
    factor=1.0,
    scale=1.0,
    interpolation="bilinear",
    fill_value=0.0,
    seed=None,
    data_format=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/text_vectorization.py
# Line: 205

def __init__(
    self,
    max_tokens=None,
    standardize="lower_and_strip_punctuation",
    split="whitespace",
    ngrams=None,
    output_mode="int",
    output_sequence_length=None,
    pad_to_max_tokens=False,
    vocabulary=None,
    idf_weights=None,
    sparse=False,
    ragged=False,
    encoding="utf-8",
    name=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/discretization.py
# Line: 88

def __init__(
    self,
    bin_boundaries=None,
    num_bins=None,
    epsilon=0.01,
    output_mode="int",
    sparse=False,
    dtype=None,
    name=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/reshaping/cropping3d_test.py
# Line: 34

def test_cropping_3d(
    self,
    dim1_cropping,
    dim2_cropping,
    dim3_cropping,
    data_format,
    dim1_expected,
    dim2_expected,
    dim3_expected,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/layer.py
# Line: 489

def add_variable(
    self,
    shape,
    initializer,
    dtype=None,
    trainable=True,
    autocast=True,
    regularizer=None,
    constraint=None,
    name=None,

# ==================================================
# Line: 515

def add_weight(
    self,
    shape=None,
    initializer=None,
    dtype=None,
    trainable=True,
    autocast=True,
    regularizer=None,
    constraint=None,
    aggregation="none",
    overwrite_with_gradient=False,
    name=None,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/input_spec.py
# Line: 51

def __init__(
    self,
    dtype=None,
    shape=None,
    ndim=None,
    max_ndim=None,
    min_ndim=None,
    axes=None,
    allow_last_axis_squeeze=False,
    name=None,
    optional=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/dense.py
# Line: 77

def __init__(
    self,
    units,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    lora_rank=None,
    lora_alpha=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/input_layer.py
# Line: 11

def __init__(
    self,
    shape=None,
    batch_size=None,
    dtype=None,
    sparse=None,
    ragged=None,
    batch_shape=None,
    input_tensor=None,
    optional=False,
    name=None,
    **kwargs,

# ==================================================
# Line: 145

def Input(
    shape=None,
    batch_size=None,
    dtype=None,
    sparse=None,
    ragged=None,
    batch_shape=None,
    name=None,
    tensor=None,
    optional=False,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/embedding.py
# Line: 82

def __init__(
    self,
    input_dim,
    output_dim,
    embeddings_initializer="uniform",
    embeddings_regularizer=None,
    embeddings_constraint=None,
    mask_zero=False,
    weights=None,
    lora_rank=None,
    lora_alpha=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/einsum_dense_test.py
# Line: 243

def test_einsum_dense_basics(
    self,
    equation,
    bias_axes,
    input_shape,
    output_shape,
    expected_kernel_shape,
    expected_bias_shape,
    expected_output_shape,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/core/einsum_dense.py
# Line: 120

def __init__(
    self,
    equation,
    output_shape,
    activation=None,
    bias_axes=None,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    lora_rank=None,
    lora_alpha=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/quantizers/quantizers_test.py
# Line: 355

def test_fake_quant_with_min_max_vars(
    self,
    input_mins,
    input_maxs,
    num_bits,
    narrow_range,
    axis,
    expected_nudged_input_mins,
    expected_nudged_input_maxs,
    expected_steps,

# ==================================================
