# long-lambda-expr snippets for keras

# File: /root/ecooptimizer/keras/keras/src/utils/timeseries_dataset_utils.py
# Line: 223

lambda i, positions: tf.range(
    positions[i],
    positions[i] + sequence_length * sampling_rate,
    sampling_rate,
),

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/schedules/learning_rate_schedule.py
# Line: 738

lambda: self._warmup_function(
    global_step_recomp,
    warmup_steps,
    warmup_target,
    initial_learning_rate,
),

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/core.py
# Line: 468

lambda: tf.concat(
    [
        _interleave_with_b(
            slice_along_axis(a, None, -1, axis=axis)
        ),
        slice_along_axis(a, -1, None, axis=axis),
    ],
    axis=axis,
),

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_flip_test.py
# Line: 276

lambda x: random_flip_layer.transform_bounding_boxes(
    x["bounding_boxes"],
    transformation=transformation,
    training=True,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_zoom_test.py
# Line: 260

lambda x: random_zoom_layer.transform_bounding_boxes(
    x["bounding_boxes"],
    transformation=transformation,
    training=True,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_shear_test.py
# Line: 191

lambda x: layer.transform_bounding_boxes(
    x["bounding_boxes"],
    transformation=transformation,
    training=True,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/mix_up_test.py
# Line: 148

lambda x: layer.transform_bounding_boxes(
    x["bounding_boxes"],
    transformation=transformation,
    training=True,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_translation_test.py
# Line: 434

lambda x: random_translation_layer.transform_bounding_boxes(
    x["bounding_boxes"],
    transformation=transformation,
    training=True,
)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_perspective_test.py
# Line: 257

lambda x: layer.transform_bounding_boxes(
    x["bounding_boxes"],
    transformation=transformation,
    training=True,
)

# ==================================================
