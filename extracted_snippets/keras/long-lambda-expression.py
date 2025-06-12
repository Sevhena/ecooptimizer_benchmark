# long-lambda-expression snippets for keras

# File: /root/ecooptimizer/keras/keras/src/saving/serialization_lib.py
# Line: 228

lambda x: (
    x.as_list()
    if isinstance(x, tf.TensorShape)
    else (x.name if isinstance(x, tf.DType) else x)
),

# ==================================================
# Line: 663

lambda x: (
    tf.TensorShape(x)
    if isinstance(x, list)
    else (getattr(tf, x) if hasattr(tf.dtypes, str(x)) else x)
),

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/image.py
# Occurrences: Lines 212-247 (2 instances)

lambda: tf.concat(
    [
        tf.ones(
            (batch_size, img_box_hstart, width, channels),
            dtype=images.dtype,
        )
        * fill_value,
        images,
        tf.ones(
            (batch_size, img_box_hstart, width, channels),
            dtype=images.dtype,
        )
        * fill_value,
    ],
    axis=1,
),

# ==================================================
# Occurrences: Lines 254-289 (2 instances)

lambda: tf.concat(
    [
        tf.ones(
            (img_box_hstart, width, channels),
            dtype=images.dtype,
        )
        * fill_value,
        images,
        tf.ones(
            (img_box_hstart, width, channels),
            dtype=images.dtype,
        )
        * fill_value,
    ],
    axis=0,
),

# ==================================================
