# long-message-chain snippets for keras

# File: /root/ecooptimizer/keras/keras/src/losses/losses_test.py
# Line: 1851

logits = (np.arange(24).reshape((2, 4, 3)).astype("float32") - 12) / 100

# ==================================================
# Line: 1857

logits = (np.arange(24).reshape((2, 4, 3)).astype("float32") - 12) / 100

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/saving/serialization_lib_test.py
# Line: 100

return str(x).replace("(", "[").replace(")", "]")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/trainers/trainer_test.py
# Line: 1828

sw = np.arange(100).reshape((100,)).astype("float32") / 50.0

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/ops/numpy_test.py
# Occurrences: Lines 2558-2559 (2 instances)

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Occurrences: Lines 2594-2595 (2 instances)

x = np.arange(2).reshape([2]).astype("float32")

# ==================================================
# Occurrences: Lines 2601-2602 (2 instances)

x = np.arange(6).reshape([2, 3]).astype("float32")

# ==================================================
# Occurrences: Lines 2608-2609 (2 instances)

x = np.arange(6).reshape([2, 3]).astype("float32")

# ==================================================
# Occurrences: Lines 2615-2616 (2 instances)

x = np.arange(6).reshape([2, 3]).astype("float32")

# ==================================================
# Occurrences: Lines 2622-2623 (2 instances)

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Occurrences: Lines 2629-2630 (2 instances)

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Occurrences: Lines 2636-2637 (2 instances)

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Occurrences: Lines 2643-2644 (2 instances)

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Occurrences: Lines 2650-2651 (2 instances)

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Occurrences: Lines 2657-2658 (2 instances)

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Occurrences: Lines 2664-2665 (2 instances)

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Occurrences: Lines 2671-2672 (2 instances)

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Occurrences: Lines 2678-2679 (2 instances)

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
# Occurrences: Lines 2706-2707 (2 instances)

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Occurrences: Lines 2713-2714 (2 instances)

x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")

# ==================================================
# Occurrences: Lines 2720-2721 (2 instances)

x = np.arange(720).reshape([2, 3, 4, 5, 6]).astype("float32")

# ==================================================
# Occurrences: Lines 2727-2728 (2 instances)

x = np.arange(720).reshape([2, 3, 4, 5, 6]).astype("float32")

# ==================================================
# Line: 3002

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# Occurrences: Lines 3213-3214 (2 instances)

x = np.arange(24).reshape([1, 2, 3, 4]).astype("float32")

# ==================================================
# Occurrences: Lines 3996-3997 (2 instances)

x = np.arange(24).reshape([2, 3, 4]).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/random/random_test.py
# Line: 354

ds = tf.data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/io_utils.py
# Occurrences: Lines 122-128 (2 instances)

input(f"[WARNING] {filepath} already exists - overwrite? [y/n]")
.strip()
.lower()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/utils/rng_utils_test.py
# Line: 26

ds = tf.data.Dataset.from_tensor_slices(x).shuffle(32).batch(16)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/optimizers/base_optimizer.py
# Line: 316

str(reference_variable.name).replace("/", "_").replace(":", "_")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/tensorflow/trainer.py
# Line: 961

if tf.math.reduce_all(constant_dims).numpy().item():

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/rnn.py
# Occurrences: Lines 698-700 (3 instances)

outputs = outputs.detach().clone().cpu()

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/nn.py
# Occurrences: Lines 845-846 (2 instances)

x.subtract(mean)
.mul_(variance.add(epsilon).rsqrt_().mul(scale))
.add_(offset)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/backend/torch/math.py
# Line: 21

segment_ids.repeat_interleave(num_repeats)
.view(*data.shape)
.type(torch.int64)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/lstm_test.py
# Line: 52

sequence = np.arange(72).reshape((3, 6, 4)).astype("float32")

# ==================================================
# Line: 153

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# Occurrences: Lines 186-189 (3 instances)

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# Line: 217

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/rnn_test.py
# Line: 363

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/conv_lstm2d_test.py
# Line: 61

np.arange(480).reshape((2, 3, 4, 4, 5)).astype("float32") / 100

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/stacked_rnn_cells_test.py
# Line: 137

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# Line: 195

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# Line: 238

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# Line: 249

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/simple_rnn_test.py
# Line: 41

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# Line: 113

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# Occurrences: Lines 146-147 (2 instances)

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# Line: 184

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/conv_lstm1d_test.py
# Line: 56

sequence = np.arange(120).reshape((2, 3, 4, 5)).astype("float32") / 10

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/conv_lstm_test.py
# Occurrences: Lines 12-14 (3 instances)

x = np.arange(150).reshape((2, 5, 5, 3)).astype("float32") / 10

# ==================================================
# Occurrences: Lines 39-41 (3 instances)

x = np.arange(450).reshape((2, 3, 5, 5, 3)).astype("float32") / 100

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/conv_lstm3d_test.py
# Line: 67

np.arange(1920).reshape((2, 3, 4, 4, 4, 5)).astype("float32") / 100

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/bidirectional_test.py
# Line: 36

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# Line: 119

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# Occurrences: Lines 153-158 (5 instances)

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# Line: 181

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# Line: 202

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/gru_test.py
# Line: 52

sequence = np.arange(72).reshape((3, 6, 4)).astype("float32")

# ==================================================
# Line: 148

sequence = np.arange(24).reshape((2, 3, 4)).astype("float32")

# ==================================================
# Occurrences: Lines 181-182 (2 instances)

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# Line: 209

sequence = np.arange(24).reshape((2, 4, 3)).astype("float32")

# ==================================================
# Line: 301

sequence = np.arange(72).reshape((3, 6, 4)).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/rnn/time_distributed_test.py
# Line: 38

sequence = np.arange(24).reshape((3, 2, 4)).astype("float32")

# ==================================================
# Line: 73

sequence = np.arange(24).reshape((3, 2, 4)).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/normalization/group_normalization_test.py
# Line: 164

x = np.arange(16).reshape((1, 4, 2, 2)).astype("float32")

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/discretization_test.py
# Line: 119

ds = tf_data.Dataset.from_tensor_slices(x).batch(1).map(layer)

# ==================================================
# Line: 130

ds = tf_data.Dataset.from_tensor_slices(x).batch(1).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/pipeline_test.py
# Line: 71

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/stft_spectrogram_test.py
# Line: 365

ds = tf.data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/hashing_test.py
# Line: 62

ds = tf.data.Dataset.from_tensor_slices(inp).batch(5).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/text_vectorization_test.py
# Line: 98

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# Line: 109

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# Line: 139

tf_data.Dataset.from_tensor_slices(input_data)
.batch(2)
.map(call_layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/integer_lookup_test.py
# Line: 104

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(4).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/category_encoding_test.py
# Line: 269

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(4).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/mel_spectrogram_test.py
# Line: 100

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_erasing_test.py
# Line: 89

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_flip_test.py
# Line: 143

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# Line: 168

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_sharpness_test.py
# Line: 63

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_zoom_test.py
# Line: 113

ds = tf_data.Dataset.from_tensor_slices(input_image).batch(1).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_shear_test.py
# Line: 76

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_contrast_test.py
# Line: 104

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_color_jitter_test.py
# Line: 133

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_saturation_test.py
# Line: 95

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_crop_test.py
# Line: 138

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_elastic_transform_test.py
# Line: 85

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur_test.py
# Line: 89

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/cut_mix_test.py
# Line: 83

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_brightness_test.py
# Line: 58

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/center_crop_test.py
# Line: 173

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/equalization_test.py
# Line: 132

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/rand_augment_test.py
# Line: 83

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/mix_up_test.py
# Line: 73

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/aug_mix_test.py
# Line: 64

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_translation_test.py
# Line: 330

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(1).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_invert_test.py
# Line: 66

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_color_degeneration_test.py
# Line: 75

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_hue_test.py
# Line: 81

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_posterization_test.py
# Line: 83

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_perspective_test.py
# Line: 94

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/random_grayscale_test.py
# Line: 73

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/image_preprocessing/resizing_test.py
# Line: 70

np.asarray([[5, 7], [13, 15]])
.astype(np.float32)
.reshape((1, 2, 2, 1))

# ==================================================
# Line: 90

np.asarray([[0, 0, 1, 1], [0, 0, 1, 1], [2, 2, 3, 3], [2, 2, 3, 3]])
.astype(np.float32)
.reshape((1, 4, 4, 1))

# ==================================================
# Line: 111

np.asarray(
    [
        [1, 2],
        [5, 6],
        [9, 10],
        [13, 14],
    ]
)
.astype("float32")
.reshape((1, 4, 2, 1))

# ==================================================
# Line: 135

np.asarray(
    [
        [5, 7],
        [13, 15],
    ]
)
.astype("float32")
.reshape((2, 2, 1))

# ==================================================
# Line: 157

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(2).map(layer)

# ==================================================
# Line: 177

tf_data.Dataset.from_tensor_slices(input_data)
.batch(2)
.map(Sequential([layer]))

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/rescaling_test.py
# Line: 74

ds = tf_data.Dataset.from_tensor_slices(x).batch(3).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/string_lookup_test.py
# Line: 79

ds = tf_data.Dataset.from_tensor_slices(input_data).batch(3).map(layer)

# ==================================================
# File: /root/ecooptimizer/keras/keras/src/layers/preprocessing/hashed_crossing_test.py
# Line: 85

tf.data.Dataset.from_tensor_slices((feat1, feat2))
.batch(5)
.map(lambda x1, x2: layer((x1, x2)))

# ==================================================
# Line: 103

tf.data.Dataset.from_tensor_slices((feat1, feat2))
.batch(5, drop_remainder=True)
.map(call_layer)

# ==================================================
