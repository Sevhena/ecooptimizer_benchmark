# cached-repeated-calls snippets for tensorflow

# File: /root/ecooptimizer/tensorflow/tensorflow/lite/toco/logging/gen_html.py
# Occurrences: Lines 249-250 (2 instances)

toco_conversion_log_before = _toco_conversion_log_pb2.TocoConversionLog()

# ==================================================
# Occurrences: Lines 258-260 (2 instances)

dot_before = f.read().rstrip()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/toco/logging/gen_html_test.py
# Occurrences: Lines 31-32 (2 instances)

toco_conversion_log_before = _toco_conversion_log_pb2.TocoConversionLog()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/tutorials/dataset.py
# Occurrences: Lines 40-43 (4 instances)

magic = read32(f)

# ==================================================
# Occurrences: Lines 56-57 (2 instances)

magic = read32(f)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/experimental/acceleration/mini_benchmark/metrics/blazeface_metrics.py
# Occurrences: Lines 99-103 (4 instances)

expected_box_encodings = tf.placeholder(
    dtype=tf.float32, shape=[1, 564, 16])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/experimental/acceleration/mini_benchmark/metrics/mobilenet.py
# Occurrences: Lines 41-42 (2 instances)

expected_scores = tf.placeholder(dtype=tf.float32, shape=[1, 1001])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/op_hint.py
# Line: 252

global_index = self._get_new_global_index(index_override)

# ==================================================
# Line: 259

self._get_new_global_index(index_override))

# ==================================================
# Occurrences: Lines 600-601 (2 instances)

assert len(flattened) == 1

# ==================================================
# Line: 607

new_node.attr["N"].i = len(flattened)

# ==================================================
# Occurrences: Lines 634-635 (2 instances)

assert len(flattened) == 1

# ==================================================
# Line: 643

stack_node.attr["num"].i = len(flattened)

# ==================================================
# Occurrences: Lines 996-1001 (2 instances)

new_node = _node_def_pb2.NodeDef()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite.py
# Occurrences: Lines 1205-1207 (2 instances)

start_time = time.process_time()

# ==================================================
# Occurrences: Lines 1360-1360 (2 instances)

shape_list = tensor.shape.as_list()

# ==================================================
# Occurrences: Lines 1370-1370 (2 instances)

shape = tensor.shape.as_list()

# ==================================================
# Line: 2827

keras_model = keras_deps.get_load_model_function()(
    model_file, custom_objects
)

# ==================================================
# Line: 2846

keras_model = keras_deps.get_load_model_function()(
    model_file, custom_objects
)

# ==================================================
# Line: 3216

graph_def = _graph_pb2.GraphDef()

# ==================================================
# Line: 3224

graph_def = _graph_pb2.GraphDef()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/interpreter.py
# Occurrences: Lines 96-97 (2 instances)

options_keys = (ctypes.c_char_p * len(options))()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/util_test.py
# Line: 386

output_io_data = _run_tflite_inference(model_io, in_tftype, out_tftype)

# ==================================================
# Line: 393

output_io_data = _run_tflite_inference(model_io, in_tftype, out_tftype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/convert_test.py
# Occurrences: Lines 350-351 (2 instances)

a = array_ops.constant([1.0])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
# Occurrences: Lines 69-72 (2 instances)

stub = metrics.TFLiteMetrics()

# ==================================================
# Occurrences: Lines 355-359 (2 instances)

mock_attempt = mock.create_autospec(monitoring.Counter, instance=True)

# ==================================================
# Occurrences: Lines 548-551 (2 instances)

input_tensor1 = tf.keras.layers.Input(
    shape=[None, None, 2, 3, 3], dtype=tf.complex64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite_test.py
# Occurrences: Lines 326-327 (2 instances)

in_tensor_a = array_ops.placeholder(shape=[3], dtype=dtypes.float32)

# ==================================================
# Line: 594

input_details = interpreter.get_input_details()

# ==================================================
# Line: 617

input_details = interpreter.get_input_details()

# ==================================================
# Occurrences: Lines 804-811 (2 instances)

float_converter = lite.TFLiteConverter.from_session(sess, [in_tensor_1],
                                                    [out_tensor])

# ==================================================
# Line: 867

float_converter = lite.TFLiteConverter.from_session(sess, [inp], [output])

# ==================================================
# Line: 885

quantized_converter = lite.TFLiteConverter.from_session(
    sess, [inp], [output])

# ==================================================
# Line: 924

float_converter = lite.TFLiteConverter.from_session(sess, [inp], [output])

# ==================================================
# Line: 930

quantized_converter = lite.TFLiteConverter.from_session(
    sess, [inp], [output])

# ==================================================
# Occurrences: Lines 971-977 (2 instances)

float_converter = lite.TFLiteConverter.from_session(sess, [inp], [output])

# ==================================================
# Line: 1129

float_converter = lite.TFLiteConverter.from_session(sess, [inp], [output])

# ==================================================
# Line: 1140

quantized_converter = lite.TFLiteConverter.from_session(
    sess, [inp], [output])

# ==================================================
# Occurrences: Lines 1270-1274 (2 instances)

float_converter = lite.TFLiteConverter.from_session(sess, [inp], [output])

# ==================================================
# Line: 2170

_ = converter.convert()

# ==================================================
# Line: 2178

_ = converter.convert()

# ==================================================
# Occurrences: Lines 2406-2407 (2 instances)

x = np.random.random((1, 3))

# ==================================================
# Occurrences: Lines 2465-2468 (4 instances)

input_a_np = np.random.random((10, 3))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/tflite_convert.py
# Occurrences: Lines 650-659 (6 instances)

use_v2_converter = tf2.enabled()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
# Line: 52

input_details = interpreter.get_input_details()

# ==================================================
# Line: 62

input_details = interpreter.get_input_details()

# ==================================================
# Line: 130

self.z = variables.Variable(3.)

# ==================================================
# Line: 136

self.z = variables.Variable(3.)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/interpreter_test.py
# Occurrences: Lines 421-433 (7 instances)

array_initial_copy = self.interpreter.get_tensor(self.input0)

# ==================================================
# Occurrences: Lines 441-444 (2 instances)

in0 = self.interpreter.tensor(self.input0)()

# ==================================================
# Occurrences: Lines 450-451 (2 instances)

in0safe = self.interpreter.tensor(self.input0)

# ==================================================
# Line: 527

interpreter_a = interpreter_wrapper.Interpreter(
    model_path=self._model_file, experimental_delegates=[delegate])

# ==================================================
# Line: 534

interpreter_b = interpreter_wrapper.Interpreter(
    model_path=self._model_file, experimental_delegates=[delegate])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/util.py
# Occurrences: Lines 602-604 (2 instances)

if min(remove_tensors_idxs) == len(tensors) - len(remove_tensors_idxs):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite_v2_test.py
# Occurrences: Lines 311-320 (2 instances)

float_converter = lite.TFLiteConverterV2.from_concrete_functions(
    [func], root
)

# ==================================================
# Occurrences: Lines 371-378 (2 instances)

converter = lite.TFLiteConverterV2.from_concrete_functions([func], root)

# ==================================================
# Occurrences: Lines 477-484 (2 instances)

converter = lite.TFLiteConverterV2.from_concrete_functions([func], root)

# ==================================================
# Occurrences: Lines 561-567 (2 instances)

float_converter = lite.TFLiteConverterV2.from_concrete_functions(
    [func], root
)

# ==================================================
# Occurrences: Lines 741-745 (2 instances)

float_converter = lite.TFLiteConverterV2.from_keras_model(model)

# ==================================================
# Occurrences: Lines 1299-1302 (4 instances)

tensor_details = interp.get_tensor_details()

# ==================================================
# Occurrences: Lines 1938-1946 (3 instances)

actual_value = interp.get_tensor(output_details[0]['index'])

# ==================================================
# Line: 2186

converter = lite.TFLiteConverterV2.from_saved_model(tf_saved_model_dir)

# ==================================================
# Line: 2196

input_data = np.random.random(tflite_input_shape).astype(np.float32)

# ==================================================
# Line: 2203

converter = lite.TFLiteConverterV2.from_saved_model(tf_saved_model_dir)

# ==================================================
# Line: 2223

input_data = np.random.random(tflite_input_shape)

# ==================================================
# Occurrences: Lines 3252-3258 (5 instances)

left_input_data = tf.constant(1.0, shape=[1, 3])

# ==================================================
# Line: 3856

weights = np.random.random_sample((10, 10))

# ==================================================
# Line: 3867

input_data = np.random.random_sample((10, 10))

# ==================================================
# Occurrences: Lines 4393-4400 (2 instances)

float_converter = lite.TFLiteConverterV2.from_concrete_functions(
    [concrete_func], root
)

# ==================================================
# Occurrences: Lines 4420-4427 (2 instances)

float_converter = lite.TFLiteConverterV2.from_concrete_functions(
    [concrete_func], root
)

# ==================================================
# Occurrences: Lines 4444-4449 (2 instances)

input_data_1 = tf.constant(
    np.array(np.random.random_sample((1, 256, 256)), dtype=np.float32)
)

# ==================================================
# Occurrences: Lines 4626-4634 (3 instances)

actual_value = interp.get_tensor(output_details[0]['index'])

# ==================================================
# Occurrences: Lines 4686-4694 (3 instances)

actual_value = interp.get_tensor(output_details[0]['index'])

# ==================================================
# Occurrences: Lines 4745-4753 (3 instances)

actual_value = interp.get_tensor(output_details[0]['index'])

# ==================================================
# Occurrences: Lines 4801-4809 (3 instances)

actual_value = interp.get_tensor(output_details[0]['index'])

# ==================================================
# Line: 5019

converter.convert()

# ==================================================
# Line: 5031

tflite_model = converter.convert()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite_flex_test.py
# Occurrences: Lines 320-327 (2 instances)

outputs = signature_runner(
    x=np.array([[1.0, 2.0, 3.0, 4.0]], dtype=np.float32))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/kernels/variants/py/end_to_end_test.py
# Occurrences: Lines 354-355 (4 instances)

l = list_ops.tensor_list_from_tensor(x, element_shape[1:])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/security/fuzzing/raggedCountSparseOutput_fuzz.py
# Occurrences: Lines 28-30 (2 instances)

splits = fh.get_int_list()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/security/fuzzing/dataFormatVecPermute_fuzz.py
# Occurrences: Lines 35-36 (2 instances)

src_format_digits = str(fh.get_int(min_int=0, max_int=999999999))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/security/fuzzing/sparseCountSparseOutput_fuzz.py
# Occurrences: Lines 28-33 (5 instances)

shape1 = fh.get_int_list(min_length=0, max_length=8, min_int=0, max_int=8)

# ==================================================
# Occurrences: Lines 44-45 (2 instances)

minlength = fh.get_int()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/security/fuzzing/add_fuzz.py
# Occurrences: Lines 31-32 (2 instances)

input_tensor_x = fh.get_random_numeric_tensor()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/security/fuzzing/tf2migration_fuzz.py
# Occurrences: Lines 32-34 (2 instances)

input_shape = fh.get_int_list(
    min_length=0, max_length=6, min_int=0, max_int=10)

# ==================================================
# Occurrences: Lines 56-63 (4 instances)

x_shape = fh.get_int_list(min_length=0, max_length=6, min_int=0, max_int=10)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
# Occurrences: Lines 976-978 (2 instances)

out = array_ops.fake_quant_with_min_max_args(
    out, min=-0.1, max=0.2, num_bits=8, narrow_range=False
)

# ==================================================
# Occurrences: Lines 998-1000 (2 instances)

out = array_ops.fake_quant_with_min_max_args(
    out, min=-0.1, max=0.2, num_bits=8, narrow_range=False
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
# Occurrences: Lines 401-402 (2 instances)

k = array_ops.constant(4, dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 432-433 (2 instances)

k = array_ops.constant(4, dtype=dtypes.int32)

# ==================================================
# Line: 667

got_outputs = converted_model.signatures[signature_key](**model_inputs)

# ==================================================
# Line: 703

new_outputs = converted_model.signatures[signature_key](**model_inputs)

# ==================================================
# Occurrences: Lines 756-756 (2 instances)

array_ops.constant([0.5, 0.5], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 785-785 (2 instances)

out_max = array_ops.constant([0.5, 0.5], dtype=dtypes.float32)

# ==================================================
# Line: 821

got_outputs = converted_model.signatures[signature_key](
    input=ops.convert_to_tensor(input_data)
)

# ==================================================
# Line: 861

new_outputs = converted_model.signatures[signature_key](
    input=ops.convert_to_tensor(input_data)
)

# ==================================================
# Line: 944

got_outputs = converted_model.signatures[signature_key](**model_inputs)

# ==================================================
# Line: 980

new_outputs = converted_model.signatures[signature_key](**model_inputs)

# ==================================================
# Line: 2634

'x': ops.convert_to_tensor(
    np.random.uniform(low=0.0, high=1.0, size=x_signature).astype(
        'f4'
    )
),

# ==================================================
# Occurrences: Lines 2669-2675 (2 instances)

input_data = ops.convert_to_tensor(
    np.random.uniform(low=0.0, high=1.0, size=x_signature).astype('f4')
)

# ==================================================
# Line: 2706

new_outputs = converted_model.signatures['serving_default'](
    x=ops.convert_to_tensor(input_data)
)

# ==================================================
# Line: 2747

prev_log_level = logging.get_verbosity()

# ==================================================
# Line: 2783

prev_log_level = logging.get_verbosity()

# ==================================================
# Occurrences: Lines 3487-3499 (8 instances)

self.filters_0 = np.random.uniform(
    low=-1.0, high=1.0, size=(4, 3)
).astype('f4')

# ==================================================
# Occurrences: Lines 3942-3947 (2 instances)

in_placeholder_1, output_tensor_1 = self._create_simple_tf1_conv_model()

# ==================================================
# Line: 4417

np.random.uniform(
    low=-0.1, high=0.2, size=(1, 3, 4, 3, 3)
).astype('f4')

# ==================================================
# Occurrences: Lines 4447-4453 (2 instances)

input_data = np.random.uniform(
    low=-0.1, high=0.2, size=(1, 3, 4, 3, 3)
).astype('f4')

# ==================================================
# Line: 4490

new_outputs = converted_model.signatures[signature_key](
    input_tensor=ops.convert_to_tensor(input_data)
)

# ==================================================
# Occurrences: Lines 5796-5808 (2 instances)

converted_model = quantize_model.quantize(
    input_saved_model_path,
    output_directory,
    quantization_options,
)

# ==================================================
# Occurrences: Lines 5857-5868 (2 instances)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    self._output_saved_model_path,
    quantization_options,
)

# ==================================================
# Line: 6369

'input_tensor': ops.convert_to_tensor(
    np.random.uniform(low=0, high=10, size=(1, 3, 4, 3)).astype(
        'f4'
    )
),

# ==================================================
# Line: 6401

sample_input = ops.convert_to_tensor(
    np.random.uniform(low=0, high=10, size=(1, 3, 4, 3)).astype('f4')
)

# ==================================================
# Occurrences: Lines 6640-6650 (5 instances)

outlier = np.random.uniform(low=0, high=10, size=(1, 3, 4, 3)).astype(
    'f4'
)

# ==================================================
# Occurrences: Lines 6710-6711 (2 instances)

sample_input = ops.convert_to_tensor(
    np.random.uniform(low=0, high=10, size=(1, 3, 4, 3)).astype('f4')
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
# Line: 491

_QuantizationComponentSpec(
    quantization_component=_QuantizationComponent.COMPONENT_WEIGHT,
    tensor_type=_TensorType.TENSORTYPE_INT_8,
)

# ==================================================
# Line: 507

_QuantizationComponentSpec(
    quantization_component=_QuantizationComponent.COMPONENT_WEIGHT,
    tensor_type=_TensorType.TENSORTYPE_INT_8,
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/stablehlo/python/integration_test/quantize_model_test_base.py
# Occurrences: Lines 234-234 (2 instances)

ones = array_ops.ones_like(out)

# ==================================================
# Occurrences: Lines 252-252 (2 instances)

ones = array_ops.ones_like(out)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/stablehlo/python/integration_test/quantize_model_test.py
# Occurrences: Lines 676-684 (2 instances)

new_outputs_1 = root.signatures['serving_default'](
    x=ops.convert_to_tensor(input_data)
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
# Line: 465

op_def, _ = self._op_defs.lookup(op_name)

# ==================================================
# Line: 493

op_def, _ = self._op_defs.lookup(op_name)

# ==================================================
# Line: 770

value, _ = self.visit(node.value)

# ==================================================
# Line: 787

value, ty = self.visit(node.value)

# ==================================================
# Occurrences: Lines 902-905 (3 instances)

cond, _ = self.visit(node.args[0])

# ==================================================
# Occurrences: Lines 916-917 (2 instances)

body, _ = self.visit(node.args[2])

# ==================================================
# Occurrences: Lines 942-945 (2 instances)

arg, ty = self.visit(node.args[0])

# ==================================================
# Line: 954

size_value = self._ssa_name('len')

# ==================================================
# Occurrences: Lines 1007-1012 (2 instances)

cst_ty = self._get_inferred_type(node)

# ==================================================
# Occurrences: Lines 1161-1165 (2 instances)

begin = self._ssa_name('begin')

# ==================================================
# Occurrences: Lines 1179-1183 (2 instances)

step = self._ssa_name('step')

# ==================================================
# Line: 1299

value, ty = self.visit(arg)

# ==================================================
# Line: 1315

value, (ssa_name, ty) = self.visit(arg)

# ==================================================
# Occurrences: Lines 1360-1364 (2 instances)

lookup_type = anno.getanno(node, anno.Static.TYPES, types.FunctionType)

# ==================================================
# Line: 1538

lib_path = os.path.join(lib_dir, lib_name)

# ==================================================
# Line: 1548

lib_path = os.path.join(lib_dir, lib_name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/tfr/python/op_reg_gen.py
# Occurrences: Lines 106-109 (2 instances)

py_str = attr.replace('"', "'")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
# Occurrences: Lines 69-72 (2 instances)

x, y = compiled_f()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/dtensor/python/layout.py
# Line: 132

flat_global_device_ids = global_device_ids.flatten()

# ==================================================
# Line: 164

global_device_ids_flatten = global_device_ids.flatten()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/dtensor/python/d_variable.py
# Occurrences: Lines 78-82 (6 instances)

api.unpack(dvariable.read_value()), host_layout)

# ==================================================
# Line: 228

initial_value = api.relayout(initial_value, layout)

# ==================================================
# Line: 243

initial_value = api.relayout(initial_value, layout)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/dtensor/python/accelerator_util.py
# Line: 210

if config.gpu_use_nccl_communication():

# ==================================================
# Line: 251

gpu_use_nccl_communication=config.gpu_use_nccl_communication(),

# ==================================================
# Line: 257

)._collective_use_nccl_communication = config.gpu_use_nccl_communication(
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/func_graph.py
# Occurrences: Lines 714-717 (2 instances)

return func()

# ==================================================
# Occurrences: Lines 1026-1033 (2 instances)

func_args_before = nest.pack_sequence_as(
    func_args,
    nest.flatten(func_args, expand_composites=True),
    expand_composites=True)

# ==================================================
# Occurrences: Lines 1070-1077 (2 instances)

func_args = nest.pack_sequence_as(
    func_args,
    nest.flatten(func_args, expand_composites=True),
    expand_composites=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/subscribe_test.py
# Occurrences: Lines 44-45 (2 instances)

a = constant_op.constant(1)

# ==================================================
# Occurrences: Lines 79-80 (2 instances)

a = constant_op.constant(1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/type_spec_test.py
# Line: 438

[trace_type.from_value(t) for t in spec.to_tensors(value)],

# ==================================================
# Line: 447

flat_original = spec.to_tensors(value)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/node_file_writer_test.py
# Line: 138

node_defs = self._get_new_node_defs()

# ==================================================
# Line: 159

node_defs = self._get_new_node_defs()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor.py
# Occurrences: Lines 1018-1020 (2 instances)

placeholder = self._graph_placeholder(context_graph, name=name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
# Occurrences: Lines 508-509 (2 instances)

w0 = variables.Variable(np.random.random_sample((3, 4)), dtype=np.float32)

# ==================================================
# Occurrences: Lines 885-888 (2 instances)

w0 = variables.Variable(
    np.random.random_sample((3, 4)), dtype=np.float32)

# ==================================================
# Line: 963

output = self.evaluate(output_node)

# ==================================================
# Line: 983

output = self.evaluate(output_node)

# ==================================================
# Line: 1000

output = self.evaluate(output_node)

# ==================================================
# Occurrences: Lines 1030-1032 (2 instances)

output = self.evaluate(output_node)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/config_test.py
# Occurrences: Lines 250-251 (2 instances)

a = constant_op.constant([2., 2.])

# ==================================================
# Occurrences: Lines 280-285 (2 instances)

options = config.get_optimizer_experimental_options()

# ==================================================
# Line: 291

self.assertDictEqual(config.get_optimizer_experimental_options(), options)

# ==================================================
# Occurrences: Lines 301-306 (2 instances)

options = config.get_optimizer_experimental_options()

# ==================================================
# Line: 312

self.assertDictEqual(config.get_optimizer_experimental_options(), options)

# ==================================================
# Line: 319

options = config.get_optimizer_experimental_options()

# ==================================================
# Line: 332

gpu = self.evaluate(fun())

# ==================================================
# Occurrences: Lines 338-343 (2 instances)

self.assertDictEqual(config.get_optimizer_experimental_options(), options)

# ==================================================
# Occurrences: Lines 349-354 (2 instances)

self.assertDictEqual(config.get_optimizer_experimental_options(), options)

# ==================================================
# Occurrences: Lines 384-390 (3 instances)

a = constant_op.constant(1.0)

# ==================================================
# Line: 400

d = constant_op.constant(1.0)

# ==================================================
# Line: 462

a = constant_op.constant(1.0)

# ==================================================
# Line: 468

a = constant_op.constant(1.0)

# ==================================================
# Line: 532

a = array_ops.identity(1.0)

# ==================================================
# Line: 538

a = array_ops.identity(1.0)

# ==================================================
# Line: 654

info1 = config.get_memory_info(device)

# ==================================================
# Line: 661

info2 = config.get_memory_info(device)

# ==================================================
# Occurrences: Lines 741-746 (2 instances)

gpus = config.list_logical_devices('GPU')

# ==================================================
# Line: 764

gpus = config.list_logical_devices('GPU')

# ==================================================
# Occurrences: Lines 799-803 (3 instances)

gpus = config.list_physical_devices('GPU')

# ==================================================
# Line: 810

gpus = config.list_physical_devices('GPU')

# ==================================================
# Line: 818

gpus = config.list_physical_devices('GPU')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_shape_test.py
# Occurrences: Lines 29-32 (2 instances)

dim = tensor_shape.Dimension(12)

# ==================================================
# Occurrences: Lines 51-61 (12 instances)

tensor_shape.Dimension(12), dim.merge_with(tensor_shape.Dimension(12)))

# ==================================================
# Occurrences: Lines 67-119 (44 instances)

dim = tensor_shape.Dimension(None)

# ==================================================
# Line: 257

s = tensor_shape.TensorShape(None)

# ==================================================
# Line: 270

for _ in tensor_shape.TensorShape(None):

# ==================================================
# Occurrences: Lines 476-485 (2 instances)

s1 = tensor_shape.TensorShape([
    tensor_shape.Dimension(3),
    tensor_shape.Dimension(4),
    tensor_shape.Dimension(7)
])

# ==================================================
# Line: 496

unk0 = tensor_shape.unknown_shape()

# ==================================================
# Line: 502

unk1 = tensor_shape.unknown_shape()

# ==================================================
# Occurrences: Lines 528-529 (2 instances)

type_1 = tensor_shape.TensorShape([1, 2, 3])

# ==================================================
# Occurrences: Lines 560-561 (2 instances)

type_1 = tensor_shape.TensorShape([1, 2, 3])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/meta_graph_test.py
# Line: 70

orig_graph = ops.Graph()

# ==================================================
# Line: 98

new_graph = ops.Graph()

# ==================================================
# Occurrences: Lines 131-138 (2 instances)

op_list = meta_graph.stripped_op_list_for_graph(ops.get_default_graph()
                                                .as_graph_def())

# ==================================================
# Occurrences: Lines 145-146 (2 instances)

a = graph.library.function.add()

# ==================================================
# Occurrences: Lines 163-164 (2 instances)

a = graph.library.function.add()

# ==================================================
# Occurrences: Lines 201-205 (2 instances)

meta_graph_def, _ = meta_graph.export_scoped_meta_graph(
    graph_def=ops.get_default_graph().as_graph_def(),
    strip_default_attrs=True)

# ==================================================
# Line: 214

node_def = test_util.get_node_def_from_graph("complex",
                                             meta_graph_def.graph_def)

# ==================================================
# Occurrences: Lines 227-231 (2 instances)

meta_graph_def, _ = meta_graph.export_scoped_meta_graph(
    graph_def=ops.get_default_graph().as_graph_def(),
    strip_default_attrs=True)

# ==================================================
# Occurrences: Lines 447-450 (2 instances)

self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))

# ==================================================
# Occurrences: Lines 462-465 (2 instances)

self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))

# ==================================================
# Occurrences: Lines 477-490 (4 instances)

self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))

# ==================================================
# Line: 496

self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))

# ==================================================
# Occurrences: Lines 538-542 (3 instances)

init_op = variables.global_variables_initializer()

# ==================================================
# Occurrences: Lines 562-568 (3 instances)

grad = gradients_impl.gradients([output], [var])

# ==================================================
# Occurrences: Lines 598-603 (2 instances)

graph = ops.Graph()

# ==================================================
# Occurrences: Lines 614-619 (2 instances)

graph = ops.Graph()

# ==================================================
# Line: 646

graph = ops.Graph()

# ==================================================
# Line: 662

newgraph = ops.Graph()

# ==================================================
# Line: 753

graph1 = ops.Graph()

# ==================================================
# Occurrences: Lines 759-766 (2 instances)

weights1 = variables.Variable(
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], name="weights")

# ==================================================
# Line: 780

graph2 = ops.Graph()

# ==================================================
# Line: 810

graph1 = ops.Graph()

# ==================================================
# Line: 823

graph2 = ops.Graph()

# ==================================================
# Line: 839

graph1 = ops.Graph()

# ==================================================
# Line: 862

graph2 = ops.Graph()

# ==================================================
# Line: 874

graph2 = ops.Graph()

# ==================================================
# Line: 886

graph2 = ops.Graph()

# ==================================================
# Line: 911

graph = ops.Graph()

# ==================================================
# Line: 923

initializer = variables.local_variables_initializer()

# ==================================================
# Occurrences: Lines 932-935 (2 instances)

graph = ops.Graph()

# ==================================================
# Line: 941

graph = ops.Graph()

# ==================================================
# Line: 951

initializer = variables.local_variables_initializer()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/extension_type.py
# Occurrences: Lines 973-974 (2 instances)

keyword_only_start = len(fields)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/device_test.py
# Occurrences: Lines 39-48 (4 instances)

var1 = variables.Variable(1.0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_test.py
# Line: 179

ops_before = g.get_operations()

# ==================================================
# Occurrences: Lines 186-195 (3 instances)

self.assertLen(g.get_operations(), len(ops_before))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/function_test.py
# Occurrences: Lines 275-282 (4 instances)

logits = array_ops.placeholder(dtype)

# ==================================================
# Occurrences: Lines 1041-1043 (4 instances)

val1, val2 = sess.run((result1, result2))

# ==================================================
# Line: 1324

library = function_pb2.FunctionDefLibrary()

# ==================================================
# Line: 1334

library = function_pb2.FunctionDefLibrary()

# ==================================================
# Occurrences: Lines 1358-1362 (2 instances)

gradient1 = function_pb2.GradientDef()

# ==================================================
# Occurrences: Lines 1532-1533 (4 instances)

m = array_ops.zeros_like(x[0])

# ==================================================
# Occurrences: Lines 1573-1574 (4 instances)

m = array_ops.zeros_like(x[0])

# ==================================================
# Occurrences: Lines 1587-1587 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 1593-1593 (2 instances)

finish = time.time()

# ==================================================
# Occurrences: Lines 1614-1614 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 1622-1622 (2 instances)

finish = time.time()

# ==================================================
# Line: 1740

return _Model(x)

# ==================================================
# Line: 1749

y = _Model(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/importer_test.py
# Line: 121

a, b = importer.import_graph_def(
    graph_def,
    return_elements=["A", "B"],
    name="")

# ==================================================
# Line: 130

a1, b1 = importer.import_graph_def(
    graph_def,
    return_elements=["A", "B"],
    name="")

# ==================================================
# Line: 139

a2, b2 = importer.import_graph_def(
    graph_def,
    return_elements=["A", "B"],
    name="")

# ==================================================
# Line: 158

a_a, a_b = importer.import_graph_def(
    graph_def,
    return_elements=["A", "B"],
    name="A/")

# ==================================================
# Line: 167

a_a1, a_b1 = importer.import_graph_def(
    graph_def,
    return_elements=["A", "B"],
    name="A/")

# ==================================================
# Line: 374

graph = ops.Graph()

# ==================================================
# Line: 384

with ops.Graph().as_default():

# ==================================================
# Line: 407

graph = ops.Graph()

# ==================================================
# Line: 415

with ops.Graph().as_default():

# ==================================================
# Line: 424

graph = ops.Graph()

# ==================================================
# Line: 430

with ops.Graph().as_default():

# ==================================================
# Line: 445

graph = ops.Graph()

# ==================================================
# Line: 451

with ops.Graph().as_default():

# ==================================================
# Line: 717

a, b = importer.import_graph_def(original_graph_def,
                                 return_elements=["A", "B"],
                                 name="")

# ==================================================
# Line: 737

a, b = importer.import_graph_def(original_graph_def,
                                 return_elements=["A", "B"],
                                 name="")

# ==================================================
# Line: 769

a, b = importer.import_graph_def(original_graph_def,
                                 return_elements=["A", "B"],
                                 name="imported_graph")

# ==================================================
# Line: 787

a, b = importer.import_graph_def(original_graph_def,
                                 return_elements=["A", "B"],
                                 name="imported_graph")

# ==================================================
# Line: 803

a, b = importer.import_graph_def(original_graph_def,
                                 return_elements=["A", "B"],
                                 name="imported_graph")

# ==================================================
# Occurrences: Lines 852-855 (2 instances)

a, b = importer.import_graph_def(
    original_graph_def, return_elements=["A", "B"], name="")

# ==================================================
# Line: 964

a2, b2, c2 = importer.import_graph_def(
    gdef, return_elements=["a", "b", "c"])

# ==================================================
# Line: 972

a3, b3, c3 = importer.import_graph_def(
    gdef, return_elements=["a", "b", "c"])

# ==================================================
# Line: 980

a4, b4, c4 = importer.import_graph_def(
    gdef, return_elements=["a", "b", "c"])

# ==================================================
# Line: 988

a5, b5, c5 = importer.import_graph_def(
    gdef, return_elements=["a", "b", "c"])

# ==================================================
# Occurrences: Lines 997-998 (2 instances)

v1 = constant_op.constant(1.0)

# ==================================================
# Occurrences: Lines 1190-1196 (3 instances)

p1, p2, a, b = importer.import_graph_def(
    gdef, return_elements=["p1:0", "p2:0", "f:0", "f:1"], name="")

# ==================================================
# Occurrences: Lines 1208-1216 (3 instances)

p1, p2, a, b = importer.import_graph_def(
    gdef, return_elements=["p1:0", "p2:0", "f:0", "f:1"], name="")

# ==================================================
# Occurrences: Lines 1265-1266 (2 instances)

x = random_ops.random_uniform(dtype=dtypes.float32, shape=())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/traceable_stack_test.py
# Occurrences: Lines 99-102 (4 instances)

obj_3 = t_stack.pop_obj()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/extension_type_field.py
# Line: 166

type_args = type_annotations.get_generic_type_args(value_type)

# ==================================================
# Occurrences: Lines 172-175 (2 instances)

for arg in type_annotations.get_generic_type_args(value_type):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/op_def_library_test.py
# Occurrences: Lines 1383-1384 (2 instances)

x = constant_op.constant(32, dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/test_util_test.py
# Occurrences: Lines 121-128 (3 instances)

def_empty = g.as_graph_def()

# ==================================================
# Occurrences: Lines 149-150 (2 instances)

def_1 = get_graph_def()

# ==================================================
# Occurrences: Lines 219-221 (2 instances)

meta_graph_def_outer = meta_graph_pb2.MetaGraphDef()

# ==================================================
# Occurrences: Lines 244-245 (2 instances)

pb1 = compare_test_pb2.Floats(float_=float("nan"))

# ==================================================
# Occurrences: Lines 257-258 (2 instances)

pb1 = compare_test_pb2.Floats(float_=float("inf"))

# ==================================================
# Occurrences: Lines 270-275 (2 instances)

pb1 = compare_test_pb2.Floats(
    float_=sys.float_info.min * sys.float_info.epsilon
)

# ==================================================
# Occurrences: Lines 295-296 (2 instances)

pb1 = compare_test_pb2.NestedFloats()

# ==================================================
# Occurrences: Lines 309-310 (2 instances)

pb1 = compare_test_pb2.MapFloats()

# ==================================================
# Occurrences: Lines 326-327 (2 instances)

a1 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# ==================================================
# Occurrences: Lines 835-836 (2 instances)

array_a = np.random.rand(3, 1)

# ==================================================
# Occurrences: Lines 844-845 (2 instances)

tensor_x = random_ops.random_uniform((5, 2, 1))

# ==================================================
# Occurrences: Lines 897-904 (6 instances)

a = random.randint(1, 1000)

# ==================================================
# Occurrences: Lines 1245-1257 (7 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 1266-1278 (7 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_util_test.py
# Occurrences: Lines 191-195 (2 instances)

a = tensor_util.MakeNdarray(t)

# ==================================================
# Line: 547

a = tensor_util.MakeNdarray(t)

# ==================================================
# Line: 554

a = tensor_util.MakeNdarray(t)

# ==================================================
# Line: 669

a = tensor_util.MakeNdarray(t)

# ==================================================
# Line: 679

a = tensor_util.MakeNdarray(t)

# ==================================================
# Line: 689

a = tensor_util.MakeNdarray(t)

# ==================================================
# Line: 706

a = tensor_util.MakeNdarray(t)

# ==================================================
# Line: 723

a = tensor_util.MakeNdarray(t)

# ==================================================
# Occurrences: Lines 1056-1060 (2 instances)

tf_val = constant_op.constant(np_val)

# ==================================================
# Line: 1100

c_val = tensor_util.constant_value(tf_val)

# ==================================================
# Line: 1111

c_val = tensor_util.constant_value(tf_val)

# ==================================================
# Occurrences: Lines 1120-1126 (4 instances)

tf_val = math_ops.cast(constant_op.constant(np_val), dtypes.float64)

# ==================================================
# Line: 1133

c_val = tensor_util.constant_value(tf_val)

# ==================================================
# Line: 1141

c_val = tensor_util.constant_value(tf_val)

# ==================================================
# Line: 1148

c_val = tensor_util.constant_value(tf_val)

# ==================================================
# Line: 1155

c_val = tensor_util.constant_value(tf_val)

# ==================================================
# Line: 1163

c_val = tensor_util.constant_value(tf_val)

# ==================================================
# Line: 1171

c_val = tensor_util.constant_value(tf_val)

# ==================================================
# Line: 1177

c_val = tensor_util.constant_value(tf_val)

# ==================================================
# Occurrences: Lines 1237-1245 (3 instances)

self.assertEqual(tensor_util.constant_value(tf_val), True)

# ==================================================
# Occurrences: Lines 1252-1261 (3 instances)

self.assertEqual(tensor_util.constant_value(tf_val), False)

# ==================================================
# Line: 1348

c_val = tensor_util.constant_value_as_shape(tf_val)

# ==================================================
# Line: 1354

c_val = tensor_util.constant_value_as_shape(tf_val)

# ==================================================
# Occurrences: Lines 1361-1366 (2 instances)

c_val = tensor_util.constant_value_as_shape(tf_val)

# ==================================================
# Line: 1372

c_val = tensor_util.constant_value_as_shape(tf_val)

# ==================================================
# Occurrences: Lines 1384-1424 (9 instances)

c_val = tensor_util.constant_value_as_shape(tf_val)

# ==================================================
# Line: 1430

c_val = tensor_util.constant_value_as_shape(tf_val)

# ==================================================
# Line: 1436

c_val = tensor_util.constant_value_as_shape(tf_val)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/dtypes_test.py
# Occurrences: Lines 59-59 (2 instances)

dtype = dtypes.as_dtype(datatype_enum)

# ==================================================
# Occurrences: Lines 65-65 (2 instances)

dtypes.as_dtype(datatype_enum).base_dtype,

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/importer.py
# Occurrences: Lines 227-227 (2 instances)

dst_op = input_dst._as_tf_output().oper  # pylint: disable=protected-access

# ==================================================
# Occurrences: Lines 233-233 (2 instances)

dst_output = input_dst._as_tf_output()  # pylint: disable=protected-access

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/op_callbacks_test.py
# Occurrences: Lines 162-163 (2 instances)

instrument_0 = _NumpyFunctionCallback()

# ==================================================
# Occurrences: Lines 183-186 (2 instances)

instrument_0 = _NumpyFunctionCallback()

# ==================================================
# Line: 195

x = constant_op.constant(4.0)

# ==================================================
# Line: 210

x = constant_op.constant(4.0)

# ==================================================
# Occurrences: Lines 255-258 (2 instances)

instrument_0 = _NumpyFunctionCallback()

# ==================================================
# Occurrences: Lines 295-301 (4 instances)

square_log(x_float32)

# ==================================================
# Occurrences: Lines 325-328 (2 instances)

instrument_0 = _NumpyFunctionCallback()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/auto_control_deps.py
# Occurrences: Lines 225-226 (2 instances)

values = array_ops.identity(tensor.values)

# ==================================================
# Occurrences: Lines 232-233 (2 instances)

values = array_ops.identity(tensor.values)

# ==================================================
# Occurrences: Lines 450-450 (2 instances)

input_id = ops.tensor_id(inp)

# ==================================================
# Occurrences: Lines 461-461 (2 instances)

input_id = ops.tensor_id(inp)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
# Occurrences: Lines 185-188 (2 instances)

gen_resource_variable_ops.assign_variable_op(v.handle, v + 1)

# ==================================================
# Occurrences: Lines 216-227 (4 instances)

assign_op1 = gen_resource_variable_ops.assign_variable_op(
    v.handle, v + 1)

# ==================================================
# Occurrences: Lines 707-708 (2 instances)

p = array_ops.placeholder(dtype=dtypes.bool)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/weak_tensor_test.py
# Line: 169

a = WeakTensor.from_tensor(constant_op.constant(1, dtypes.int32))

# ==================================================
# Line: 177

b = constant_op.constant(1, dtypes.int32)

# ==================================================
# Line: 185

t = constant_op.constant([1.0, 2.0], dtypes.float32)

# ==================================================
# Line: 200

t = constant_op.constant([1.0, 2.0], dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/test_util.py
# Occurrences: Lines 314-315 (4 instances)

a_proto = proto_type()

# ==================================================
# Occurrences: Lines 782-788 (6 instances)

registered_function_names = context.context().list_function_names()

# ==================================================
# Occurrences: Lines 822-828 (6 instances)

_get_object_count_by_type(
    exclude=gc.get_referents(test_errors, test_skipped)) -

# ==================================================
# Occurrences: Lines 887-889 (4 instances)

result = f(self, **kwargs)

# ==================================================
# Occurrences: Lines 946-959 (6 instances)

return "{}, {}".format(type(obj), id(obj))

# ==================================================
# Line: 981

obj_id = id(obj)

# ==================================================
# Occurrences: Lines 1045-1048 (4 instances)

previous_garbage = len(gc.garbage)

# ==================================================
# Occurrences: Lines 1063-1063 (2 instances)

len(gc.garbage) - previous_garbage)

# ==================================================
# Occurrences: Lines 1498-1498 (2 instances)

with ops.Graph().as_default():

# ==================================================
# Occurrences: Lines 1508-1508 (2 instances)

graph_for_eager_test = ops.Graph()

# ==================================================
# Occurrences: Lines 2459-2463 (6 instances)

result = func(*args, **kwargs)

# ==================================================
# Occurrences: Lines 2538-2546 (3 instances)

ret = math_ops.matmul(a, b, *args, **kwargs)

# ==================================================
# Occurrences: Lines 2870-2872 (2 instances)

flattened_results = sess.run(flattened_tensors)

# ==================================================
# Line: 3740

err_str = str(e)

# ==================================================
# Line: 3755

(str(type(e)), str(e)))

# ==================================================
# Occurrences: Lines 3840-3843 (2 instances)

a = cast(ragged_tensor_value.RaggedTensorValue, self.evaluate(a))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/memory_checker_test.py
# Occurrences: Lines 61-63 (2 instances)

x = constant_op.constant(1)  # pylint: disable=unused-variable

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_conversion_registry.py
# Occurrences: Lines 143-147 (2 instances)

conversion_funcs = _tensor_conversion_func_cache.get(query)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/extension_type_test.py
# Line: 1287

weight_dtype = property(lambda self: self.weight.dtype)

# ==================================================
# Line: 1303

weight_dtype = property(lambda self: self.weight.dtype)

# ==================================================
# Occurrences: Lines 1565-1568 (2 instances)

n = len(op._tf_fallback_dispatchers)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/experimental/graph_building_test.py
# Occurrences: Lines 38-39 (4 instances)

a = gen_array_ops.placeholder(dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/ops.py
# Line: 2043

self._graph_device_function_stack = traceable_stack.TraceableStack()

# ==================================================
# Line: 2078

self._graph_colocation_stack = traceable_stack.TraceableStack()

# ==================================================
# Line: 2406

graph = graph_pb2.GraphDef()

# ==================================================
# Line: 2413

graph = graph_pb2.GraphDef()

# ==================================================
# Line: 2993

op = self._get_operation_by_name(name)

# ==================================================
# Line: 3004

op = self._get_operation_by_name(name)

# ==================================================
# Occurrences: Lines 3574-3578 (2 instances)

self._device_function_stack = traceable_stack.TraceableStack()

# ==================================================
# Occurrences: Lines 3675-3679 (2 instances)

old_top_of_stack = self._device_function_stack.peek_top_obj()

# ==================================================
# Line: 4816

scope = get_default_graph().get_name_scope()

# ==================================================
# Line: 4838

outer_graph = get_default_graph()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/python_memory_checker.py
# Line: 50

result = collections.Counter()

# ==================================================
# Line: 56

result += collections.Counter()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/graph_building_benchmark.py
# Occurrences: Lines 41-44 (2 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/graph_util_test.py
# Occurrences: Lines 118-128 (6 instances)

const_0 = constant_op.constant(5.0)

# ==================================================
# Occurrences: Lines 141-151 (6 instances)

const_0 = constant_op.constant(5.0)

# ==================================================
# Occurrences: Lines 162-178 (5 instances)

n1 = graph_def.node.add()

# ==================================================
# Occurrences: Lines 241-243 (2 instances)

graph_def = graph_pb2.GraphDef()

# ==================================================
# Line: 251

b_constant = self.create_constant_node_def(
    b_constant_name, value=1, dtype=dtypes.float32, shape=[])

# ==================================================
# Occurrences: Lines 264-284 (6 instances)

c_constant = self.create_constant_node_def(
    c_constant_name, value=1, dtype=dtypes.float32, shape=[]
)

# ==================================================
# Occurrences: Lines 290-301 (3 instances)

c_constant = self.create_constant_node_def(
    c_constant_name, value=1, dtype=dtypes.float32, shape=[]
)

# ==================================================
# Line: 315

graph_def = graph_pb2.GraphDef()

# ==================================================
# Line: 323

expected_graph_def = graph_pb2.GraphDef()

# ==================================================
# Line: 345

graph_def1 = graph_pb2.GraphDef()

# ==================================================
# Line: 352

graph_def2 = graph_pb2.GraphDef()

# ==================================================
# Line: 362

graph_def1 = graph_pb2.GraphDef()

# ==================================================
# Line: 369

graph_def2 = graph_pb2.GraphDef()

# ==================================================
# Line: 379

graph_def1 = graph_pb2.GraphDef()

# ==================================================
# Line: 386

graph_def2 = graph_pb2.GraphDef()

# ==================================================
# Line: 395

graph_def1 = graph_pb2.GraphDef()

# ==================================================
# Line: 403

graph_def2 = graph_pb2.GraphDef()

# ==================================================
# Line: 413

graph_def1 = graph_pb2.GraphDef()

# ==================================================
# Line: 421

graph_def2 = graph_pb2.GraphDef()

# ==================================================
# Occurrences: Lines 441-444 (2 instances)

graph_def1 = graph_pb2.GraphDef()

# ==================================================
# Occurrences: Lines 461-469 (4 instances)

library = function_pb2.FunctionDefLibrary()

# ==================================================
# Occurrences: Lines 482-485 (2 instances)

library = function_pb2.FunctionDefLibrary()

# ==================================================
# Occurrences: Lines 493-495 (2 instances)

reversed_library = function_pb2.FunctionDefLibrary()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/meta_graph.py
# Occurrences: Lines 754-755 (2 instances)

kind = col_def.WhichOneof("kind")

# ==================================================
# Line: 821

kind = col_def.WhichOneof("kind")

# ==================================================
# Occurrences: Lines 840-840 (2 instances)

proto = proto_type()

# ==================================================
# Occurrences: Lines 850-862 (7 instances)

variable = from_proto(
    proto, import_scope=scope_to_prepend_to_names)

# ==================================================
# Line: 959

new_graph_def = graph_pb2.GraphDef()

# ==================================================
# Line: 974

graph_def = graph_pb2.GraphDef()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/ops_test.py
# Occurrences: Lines 175-176 (2 instances)

a = array_ops.placeholder(dtype=dtypes.float32, shape=[2, None, 3])

# ==================================================
# Occurrences: Lines 237-239 (2 instances)

x1 = constant_op.constant(3)

# ==================================================
# Occurrences: Lines 258-260 (2 instances)

x1 = constant_op.constant(3)

# ==================================================
# Occurrences: Lines 279-281 (2 instances)

x1 = constant_op.constant(3)

# ==================================================
# Occurrences: Lines 303-305 (2 instances)

x1 = constant_op.constant(3)

# ==================================================
# Occurrences: Lines 696-700 (2 instances)

self.assertEqual(2, len(op.values()))

# ==================================================
# Occurrences: Lines 735-740 (4 instances)

self.assertEqual(1, len(op1.values()))

# ==================================================
# Occurrences: Lines 848-850 (2 instances)

tensor = ops.convert_to_tensor(values)

# ==================================================
# Line: 879

tensor = ops.convert_to_tensor(values, preferred_dtype=dtypes.int64)

# ==================================================
# Line: 885

tensor = ops.convert_to_tensor(values, preferred_dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 1101-1102 (2 instances)

g_0 = ops.Graph()

# ==================================================
# Occurrences: Lines 1193-1194 (2 instances)

g_0 = ops.Graph()

# ==================================================
# Occurrences: Lines 1639-1643 (2 instances)

op1 = g.create_op("FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 1968-1971 (2 instances)

self.has_mutated_graph = threading.Event()

# ==================================================
# Occurrences: Lines 2143-2147 (4 instances)

op1 = g.create_op("FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2212-2213 (2 instances)

other_collection_snapshot = g.get_collection("other")

# ==================================================
# Occurrences: Lines 2219-2228 (5 instances)

self.assertEqual(["foo", "bar"], g.get_collection("other"))

# ==================================================
# Occurrences: Lines 2235-2236 (2 instances)

self.assertEqual(["something"], g.get_collection("empty"))

# ==================================================
# Occurrences: Lines 2353-2356 (3 instances)

a = constant_op.constant(1.0)

# ==================================================
# Occurrences: Lines 2373-2384 (4 instances)

a = constant_op.constant(1.0)

# ==================================================
# Line: 2390

a = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Line: 2398

c = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2404-2410 (5 instances)

a_1 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Line: 2416

b_2 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2424-2427 (4 instances)

a_1 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2435-2446 (6 instances)

b_3_4 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2466-2483 (9 instances)

a_1 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2489-2492 (2 instances)

b_3 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_3, a_4],
                [dtypes.float32])

# ==================================================
# Occurrences: Lines 2498-2501 (2 instances)

b_4 = _apply_op(g, "TwoFloatInputsFloatOutput", [a_3, a_4],
                [dtypes.float32])

# ==================================================
# Occurrences: Lines 2532-2534 (2 instances)

b = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2549-2555 (4 instances)

a = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2724-2727 (4 instances)

a_1 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2736-2747 (6 instances)

b_3_4 = _apply_op(g, "FloatOutput", [], [dtypes.float32])

# ==================================================
# Occurrences: Lines 2757-2760 (3 instances)

g0 = ops.Graph()

# ==================================================
# Occurrences: Lines 2774-2776 (2 instances)

g0 = ops.Graph()

# ==================================================
# Occurrences: Lines 2782-2800 (9 instances)

on_gpu = constant_op.constant(1.0)

# ==================================================
# Line: 2807

_ = constant_op.constant(1.0)

# ==================================================
# Line: 2815

_ = constant_op.constant(1.0)

# ==================================================
# Line: 2821

_ = constant_op.constant(1.0)

# ==================================================
# Occurrences: Lines 2884-2885 (2 instances)

with ops.Graph().as_default():

# ==================================================
# Line: 2978

g0 = ops.Graph()

# ==================================================
# Line: 2986

with ops.Graph().as_default() as g1:

# ==================================================
# Occurrences: Lines 3092-3108 (7 instances)

a1 = self._get_test_attrs()

# ==================================================
# Occurrences: Lines 3130-3140 (6 instances)

default_1 = test_ops.kernel_label()

# ==================================================
# Occurrences: Lines 3530-3531 (4 instances)

g1 = ops.Graph()

# ==================================================
# Occurrences: Lines 3548-3551 (2 instances)

c = config_pb2.ConfigProto()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_util.py
# Line: 614

if shape is not None and np.prod(shape, dtype=np.int64) == 0:

# ==================================================
# Line: 660

shape_size = np.prod(shape, dtype=np.int64)

# ==================================================
# Occurrences: Lines 814-817 (2 instances)

values = np.array([complex(x[0], x[1]) for x in zip(it, it)], dtype=dtype)

# ==================================================
# Line: 867

input_shape = tensor.op.inputs[0].get_shape()

# ==================================================
# Line: 875

input_shape = tensor.op.inputs[0].get_shape()

# ==================================================
# Line: 881

input_shape = tensor.op.inputs[0].get_shape()

# ==================================================
# Occurrences: Lines 890-893 (2 instances)

start = constant_value(tensor.op.inputs[0])

# ==================================================
# Line: 901

pre_cast = constant_value(tensor.op.inputs[0])

# ==================================================
# Occurrences: Lines 907-912 (2 instances)

dim = constant_value(tensor.op.inputs[0])

# ==================================================
# Line: 923

value = constant_value(x)

# ==================================================
# Occurrences: Lines 952-957 (2 instances)

value = constant_value(tensor.op.inputs[0], partial)

# ==================================================
# Line: 965

fill_value = constant_value(tensor.op.inputs[1])

# ==================================================
# Occurrences: Lines 971-989 (6 instances)

value1 = constant_value(tensor.op.inputs[0])

# ==================================================
# Line: 1096

value = constant_value(tensor)

# ==================================================
# Occurrences: Lines 1109-1111 (2 instances)

return tensor_shape.TensorShape([])

# ==================================================
# Line: 1117

return tensor_shape.unknown_shape(shape.dims[0].value)

# ==================================================
# Line: 1127

ret = tensor_shape.TensorShape([])  # Empty list.

# ==================================================
# Occurrences: Lines 1145-1149 (2 instances)

ret = tensor_shape.TensorShape([])  # Empty list.

# ==================================================
# Occurrences: Lines 1155-1159 (2 instances)

ret = tensor_shape.TensorShape([])  # Empty list.

# ==================================================
# Line: 1185

prev = constant_value_as_shape(tensor.op.inputs[0])

# ==================================================
# Occurrences: Lines 1207-1208 (2 instances)

ret = tensor_shape.unknown_shape(shape.dims[0].value)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/flexible_dtypes_test.py
# Line: 836

flexible_dtypes.result_type(d),

# ==================================================
# Occurrences: Lines 842-846 (2 instances)

_ = flexible_dtypes.result_type(d)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/graph_util_impl.py
# Occurrences: Lines 317-322 (2 instances)

new_node = node_def_pb2.NodeDef()

# ==================================================
# Occurrences: Lines 362-370 (7 instances)

new_node = node_def_pb2.NodeDef()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
# Line: 317

fdef.arg_attr[0].attr["_test_attr"].s = "value".encode("ascii")

# ==================================================
# Line: 324

"value".encode("ascii"))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/device_spec.py
# Occurrences: Lines 347-351 (4 instances)

elif ((ly == 1 or ly == 2) and (y[0].upper() in valid_device_types)):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
# Occurrences: Lines 54-58 (4 instances)

value = self.evaluate(sp)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/smart_cond_test.py
# Occurrences: Lines 64-68 (2 instances)

x = constant_op.constant(1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/auto_control_deps_utils.py
# Occurrences: Lines 96-97 (2 instances)

reads = object_identity.ObjectIdentitySet()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/op_def_library.py
# Occurrences: Lines 419-424 (4 instances)

values = keywords.pop(input_name)

# ==================================================
# Occurrences: Lines 601-614 (10 instances)

if len(values) != attrs[input_arg.number_attr]:

# ==================================================
# Occurrences: Lines 644-644 (2 instances)

type_attr = _Attr(op_def, input_arg.type_attr)

# ==================================================
# Occurrences: Lines 661-661 (2 instances)

_Attr(op_def, input_arg.type_attr),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
# Occurrences: Lines 153-156 (4 instances)

cache_idx = len(self.tensorname_to_cache_idx)

# ==================================================
# Occurrences: Lines 164-164 (2 instances)

len(self.tensorname_to_cache_idx),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/training_loop.py
# Line: 155

output_tensors = array_ops.constant(0)

# ==================================================
# Line: 177

inputs = [array_ops.constant(0)]

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/feature_column_v2.py
# Line: 963

sparse_tensor = transformation_cache.get(self.categorical_column.name,
                                         state_manager)

# ==================================================
# Line: 973

values = transformation_cache.get(self.categorical_column.name,
                                  state_manager)

# ==================================================
# Line: 1001

sparse_tensor = inputs.get(self.get_feature_key_name())

# ==================================================
# Line: 1010

values = inputs.get(self.get_feature_key_name())

# ==================================================
# Line: 1078

sparse_tensor = transformation_cache.get(self.categorical_column.name,
                                         state_manager)

# ==================================================
# Line: 1088

values = transformation_cache.get(self.categorical_column.name,
                                  state_manager)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3.py
# Line: 148

fullshape = variable.shape.as_list()

# ==================================================
# Line: 154

var_shape=variable.shape.as_list(),

# ==================================================
# Line: 1223

graph = ops.get_default_graph()

# ==================================================
# Line: 1235

if graph != ops.get_default_graph() and in_tpu_ctx:

# ==================================================
# Line: 1242

"a computation.".format(ops.get_default_graph(), graph)

# ==================================================
# Line: 1681

weight = array_ops.ones_like(input_feature.values, dtype=dtypes.float32)

# ==================================================
# Line: 1707

weight = array_ops.ones_like(input_feature.values, dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu.py
# Line: 408

input_shape = input_tensor.get_shape().as_list()

# ==================================================
# Line: 441

input_shape = input_tensor.get_shape().as_list()

# ==================================================
# Occurrences: Lines 486-489 (6 instances)

lambda: array_ops.pad(input_tensor, paddings),  # pylint: disable=cell-var-from-loop

# ==================================================
# Occurrences: Lines 636-637 (2 instances)

metadata_kwargs["allow_soft_placement"] = config.get_soft_device_placement()

# ==================================================
# Line: 755

graph = ops.get_default_graph()

# ==================================================
# Line: 775

attr_value_pb2.AttrValue(s=compat.as_bytes(cluster_name)))

# ==================================================
# Line: 888

output_tensors = tt.trace_tpu(ops.get_default_graph(),

# ==================================================
# Line: 907

attr_value = attr_value_pb2.AttrValue(s=compat.as_bytes(cluster_name))

# ==================================================
# Occurrences: Lines 1038-1038 (2 instances)

o = array_ops.identity(t)

# ==================================================
# Occurrences: Lines 1045-1045 (2 instances)

o = array_ops.identity(t)

# ==================================================
# Occurrences: Lines 1099-1110 (8 instances)

o = array_ops.identity(o)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_sharding_test.py
# Occurrences: Lines 28-33 (2 instances)

p1 = tpu_sharding.ShardingPolicy()

# ==================================================
# Occurrences: Lines 60-67 (3 instances)

p1 = tpu_sharding.ShardingPolicy()

# ==================================================
# Line: 79

p1 = tpu_sharding.ShardingPolicy()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
# Occurrences: Lines 72-73 (2 instances)

opt1 = optimizer(0.1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/datasets_test.py
# Occurrences: Lines 41-48 (4 instances)

self._coord = server_lib.Server.create_local_server()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/async_checkpoint_test.py
# Line: 79

loss = losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

# ==================================================
# Line: 100

loss = losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/datasets.py
# Occurrences: Lines 169-175 (2 instances)

h, dataset_ops.get_legacy_output_types(source_dataset),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3_cpu_ops_test.py
# Occurrences: Lines 100-101 (2 instances)

max_ids = np.zeros(num_sc_shards)

# ==================================================
# Occurrences: Lines 203-204 (2 instances)

sorted_sample_ids = np.full(max_ids_per_chip, 8, dtype=np.int32)

# ==================================================
# Occurrences: Lines 224-229 (4 instances)

round_up_to(row_pointers_index, padded_row_pointers_size),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_test.py
# Occurrences: Lines 44-49 (2 instances)

z1 = array_ops.identity(1)

# ==================================================
# Occurrences: Lines 67-69 (4 instances)

z1 = array_ops.zeros([3, 2], name="a")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
# Occurrences: Lines 366-367 (6 instances)

y = tpu_replication.outside_compilation(host_computation, x)

# ==================================================
# Occurrences: Lines 393-394 (6 instances)

y = tpu_replication.outside_compilation(host_computation, x)

# ==================================================
# Occurrences: Lines 429-430 (8 instances)

y = tpu_replication.outside_compilation(host_computation, x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_feed.py
# Occurrences: Lines 506-510 (2 instances)

dequeue_op = tpu_ops.infeed_dequeue_tuple(
    dtypes=self._tuple_types, shapes=sharded_shapes, name=full_name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3_test.py
# Occurrences: Lines 625-630 (2 instances)

random1 = np.random.uniform(size=(16, self.embedding_dim)).astype(
    np.float32
)

# ==================================================
# Occurrences: Lines 709-714 (2 instances)

random1 = np.random.uniform(size=(16, self.embedding_dim)).astype(
    np.float32
)

# ==================================================
# Line: 919

inner_result = array_ops.zeros(
    [16, self.embedding_dim], dtype=dtypes.float32
)

# ==================================================
# Line: 937

inner_result = array_ops.zeros(
    [16, self.embedding_dim], dtype=dtypes.float32
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
# Occurrences: Lines 352-355 (2 instances)

embedding_one = tpu_embedding_for_serving.TPUEmbeddingForServing(
    feature_config=feature_config, optimizer=optimizer)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/client/client_test.py
# Occurrences: Lines 98-104 (3 instances)

mock_locations = mock.MagicMock()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving.py
# Line: 572

ragged_output = _ragged_embedding_lookup_with_reduce(
    table, inp, weight, feature.table.combiner
)

# ==================================================
# Line: 582

ragged_output = embedding_ops.embedding_lookup_v2(table, inp)

# ==================================================
# Occurrences: Lines 604-611 (2 instances)

ragged_lookup = embedding_ops.embedding_lookup_v2(table, inp)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
# Occurrences: Lines 458-462 (2 instances)

nest.flatten(per_replica_input_shapes),

# ==================================================
# Occurrences: Lines 863-867 (4 instances)

variables[table.name] = create_variables(table)

# ==================================================
# Line: 1025

graph = ops.get_default_graph()

# ==================================================
# Line: 1037

if graph != ops.get_default_graph() and in_tpu_ctx:

# ==================================================
# Line: 1044

"a computation.".format(ops.get_default_graph(), graph))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3_checkpoint_adapter_test.py
# Occurrences: Lines 39-40 (2 instances)

) -> sparse_core_layout_pb2.SparseCoreTableLayout():

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_replication.py
# Occurrences: Lines 225-229 (2 instances)

outside_attr = op.get_attr(_OUTSIDE_COMPILATION_ATTR).decode("ascii")

# ==================================================
# Line: 238

outside_attr = op.get_attr(_OUTSIDE_COMPILATION_ATTR).decode("ascii")

# ==================================================
# Line: 265

parts = outside_attr.split(".")

# ==================================================
# Line: 608

return computation(*args, **kwargs)

# ==================================================
# Line: 622

retval = computation(*args, **kwargs)

# ==================================================
# Line: 628

initial_context = graph._get_control_flow_context()  # pylint: disable=protected-access

# ==================================================
# Occurrences: Lines 635-639 (2 instances)

retval = computation(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tensor_tracer.py
# Line: 808

for _, val in sorted(signatures.items(),

# ==================================================
# Line: 815

(_, val), = signatures.items()

# ==================================================
# Occurrences: Lines 900-907 (5 instances)

lambda: constant_op.constant([0.0]))

# ==================================================
# Line: 949

tensor = math_ops.cast(tensor, dtypes.float32)

# ==================================================
# Line: 982

tensor = math_ops.cast(tensor, dtypes.float32)

# ==================================================
# Occurrences: Lines 1564-1564 (2 instances)

old_value = state_ops.assign_add(snapshot_variable, 0.0)

# ==================================================
# Occurrences: Lines 1572-1572 (2 instances)

new_value_from_var = state_ops.assign_add(snapshot_variable, 0.0)

# ==================================================
# Occurrences: Lines 1688-1690 (2 instances)

array_ops.identity(training_util.get_or_create_global_step()))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/topology.py
# Occurrences: Lines 146-147 (2 instances)

tasks = np.full(list(self.mesh_shape), -1, dtype=np.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_sharding.py
# Occurrences: Lines 173-178 (2 instances)

dims = shape.as_list()

# ==================================================
# Occurrences: Lines 225-234 (4 instances)

f"Shape {shape.as_list()} does not contain shard_dimension "

# ==================================================
# Occurrences: Lines 261-264 (2 instances)

raise ValueError(f"Shape {shape.as_list()} does not contain "

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_system_metadata.py
# Line: 113

spec = tf_device.DeviceSpec.from_string(device.name)

# ==================================================
# Line: 142

spec = tf_device.DeviceSpec.from_string(device.name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/device_assignment.py
# Line: 402

computation_shape = np.array([1] * topology_rank, dtype=np.int32)

# ==================================================
# Line: 409

computation_stride = np.array([1] * topology_rank, dtype=np.int32)

# ==================================================
# Line: 516

for index in range(np.prod(computation_shape)):

# ==================================================
# Occurrences: Lines 558-563 (2 instances)

assert num_replicas * np.prod(
    computation_shape) <= topology.num_tasks * topology.num_tpus_per_task

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3_checkpoint_adapter.py
# Line: 362

stime = time.time()

# ==================================================
# Line: 376

etime = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
# Occurrences: Lines 201-207 (3 instances)

embeddings = math_ops.reduce_sum(embeddings, axis=-2)

# ==================================================
# Occurrences: Lines 390-395 (3 instances)

weight = array_ops.ones_like(inp, dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 411-411 (2 instances)

weight = array_ops.ones_like(inp, dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 435-444 (3 instances)

output_batch_size = math_ops.reduce_prod(feature.output_shape).numpy()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/async_checkpoint.py
# Line: 131

ops.get_default_graph().as_graph_def(add_shapes=True),

# ==================================================
# Line: 138

graph = ops.get_default_graph()

# ==================================================
# Occurrences: Lines 184-184 (2 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 200-200 (2 instances)

end_time = time.time()

# ==================================================
# Occurrences: Lines 223-225 (2 instances)

blocking_start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3_additional_test.py
# Occurrences: Lines 96-100 (2 instances)

tpu_cluster_resolver.initialize_tpu_system(resolver)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/concat_benchmark.py
# Occurrences: Lines 102-106 (4 instances)

_ = session.run(outputs)  # warm up.

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/control_flow_case.py
# Line: 381

pred_fn_pairs = pred_fn_pairs.items()

# ==================================================
# Occurrences: Lines 390-393 (2 instances)

pred_fn_pairs = list(pred_fn_pairs.items())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/sparse_ops_test.py
# Line: 216

result = sparse_ops.map_values(mapping, sp, sp_incomp, kwarg='kwarg')

# ==================================================
# Line: 222

result = sparse_ops.map_values(mapping, sp, sp_incomp, kwarg='kwarg')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_grad.py
# Line: 905

dx, dscale, doffset, _, _ = grad_fun(**args)

# ==================================================
# Line: 929

dx, dscale, doffset, _, _ = grad_fun(**args)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/metrics_impl.py
# Line: 114

predictions.get_shape().assert_is_compatible_with(labels.get_shape())

# ==================================================
# Occurrences: Lines 125-132 (3 instances)

predictions_shape = predictions.get_shape()

# ==================================================
# Line: 141

lambda: array_ops.expand_dims(weights, [-1]), lambda: weights)

# ==================================================
# Line: 148

maybe_squeeze_weights = lambda: array_ops.squeeze(weights, [-1])

# ==================================================
# Occurrences: Lines 299-306 (6 instances)

metric_value = metric_value_fn(distribution, *a)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/array_grad.py
# Line: 95

input_shape = array_ops.shape(x)

# ==================================================
# Line: 124

out_grads = array_ops.split(grad, sizes, non_neg_concat_dim)

# ==================================================
# Line: 136

value = tensor_util.constant_value(concat_dim)

# ==================================================
# Line: 155

out_grads = array_ops.split(grad, sizes, non_neg_concat_dim)

# ==================================================
# Line: 164

concat_dim_static = tensor_util.constant_value(concat_dim)

# ==================================================
# Line: 176

sizes = [array_ops.shape(x) for x in input_values]

# ==================================================
# Occurrences: Lines 607-612 (2 instances)

accum_dim_value = array_ops.ones((), dtype=indices_dtype)

# ==================================================
# Line: 665

params_shape = array_ops.shape(params)

# ==================================================
# Line: 691

values = array_ops.reshape(
    _IndexedSlicesToTensorNoWarning(grad), values_shape)

# ==================================================
# Line: 710

values = array_ops.reshape(
    _IndexedSlicesToTensorNoWarning(grad), values_shape)

# ==================================================
# Line: 736

array_ops.shape(params)

# ==================================================
# Line: 1068

_, ksize_r, ksize_c, _ = op.get_attr("ksizes")

# ==================================================
# Line: 1081

input_idx, op.get_attr("ksizes"), op.get_attr("strides"),

# ==================================================
# Line: 1124

input_idx, op.get_attr("ksizes"), op.get_attr("strides"),

# ==================================================
# Line: 1131

_, ksize_p, ksize_r, ksize_c, _ = op.get_attr("ksizes")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/summary_op_util.py
# Occurrences: Lines 96-99 (2 instances)

tag = scope.rstrip('/')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/batch_norm_benchmark.py
# Occurrences: Lines 97-99 (4 instances)

mean = array_ops.zeros(moment_shape)

# ==================================================
# Occurrences: Lines 145-149 (4 instances)

_ = session.run([out.op for out in outputs])  # warm up.

# ==================================================
# Occurrences: Lines 177-197 (12 instances)

t1 = self._run_graph("cpu", shape, axes, 10, "op", True, False, 5)

# ==================================================
# Occurrences: Lines 203-223 (12 instances)

t1 = self._run_graph("cpu", shape, axes, 10, "op", True, False, 5)

# ==================================================
# Occurrences: Lines 229-234 (4 instances)

t1 = self._run_graph("cpu", shape, axes, 10, "py", True, False, 5)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
# Occurrences: Lines 269-269 (2 instances)

embedding = embedding_ops.embedding_lookup(embedding_matrix, [0])

# ==================================================
# Occurrences: Lines 283-283 (2 instances)

embedding = embedding_ops.embedding_lookup(embedding_matrix, [0])

# ==================================================
# Line: 778

tensor = array_ops.placeholder(dtype=dtype, shape=None)

# ==================================================
# Line: 786

tensor = array_ops.placeholder(dtype=dtype, shape=None)

# ==================================================
# Occurrences: Lines 852-853 (4 instances)

fn_true, true_tensors = _build_branch(dtype, shape)

# ==================================================
# Occurrences: Lines 871-872 (2 instances)

ta1 = _create_tensor_array(4, element_shape)

# ==================================================
# Line: 1336

return flexible_fn(a)

# ==================================================
# Occurrences: Lines 1343-1348 (2 instances)

r = flexible_fn(a)

# ==================================================
# Line: 1355

r, result, grad = run_defun_and_tape(a)

# ==================================================
# Line: 1361

r, result, grad = run_defun_and_tape(a)

# ==================================================
# Occurrences: Lines 1407-1423 (6 instances)

return flexible_fn(a)

# ==================================================
# Occurrences: Lines 1494-1495 (2 instances)

x = constant_op.constant(2)

# ==================================================
# Occurrences: Lines 1637-1644 (6 instances)

i = constant_op.constant(0)

# ==================================================
# Occurrences: Lines 1652-1658 (6 instances)

t_acc = t_acc.write(i, ticker.read_value())

# ==================================================
# Line: 1684

self.evaluate(ticker.read_value()),

# ==================================================
# Occurrences: Lines 1752-1756 (2 instances)

c = control_flow_assert.Assert(i < 10, [i, [10], [i + 1]])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/script_ops_test.py
# Occurrences: Lines 149-150 (4 instances)

sum1 = numpy_func_stateless(a, b)

# ==================================================
# Occurrences: Lines 174-175 (4 instances)

sum1 = numpy_func_stateful(a, b)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/autograph_ops.py
# Line: 56

tensor_args_idx[i] = len(tensor_args)

# ==================================================
# Line: 76

tensor_args_idx[k] = len(tensor_args)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/matmul_benchmark.py
# Occurrences: Lines 92-95 (2 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/losses/util.py
# Occurrences: Lines 67-73 (2 instances)

y_true, y_pred = confusion_matrix.remove_squeezable_dimensions(
    y_true, y_pred)

# ==================================================
# Occurrences: Lines 91-93 (2 instances)

sample_weight = array_ops.squeeze(sample_weight, [-1])

# ==================================================
# Occurrences: Lines 99-102 (2 instances)

maybe_squeeze_weights = lambda: array_ops.squeeze(sample_weight, [-1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/losses/losses_impl.py
# Line: 1031

weights = array_ops.squeeze(weights, [-1])

# ==================================================
# Line: 1040

lambda: array_ops.squeeze(weights, [-1]),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
# Occurrences: Lines 212-229 (6 instances)

tin = math_ops.cast(
    constant_op.constant(1, shape=[1, 2, 3, 3]), dtype=dtypes.quint8)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/gradients_util.py
# Line: 547

src_graph = ops.get_default_graph()

# ==================================================
# Line: 571

gradient_uid = ops.get_default_graph().unique_name("uid")

# ==================================================
# Line: 702

ops.get_default_graph()._get_control_flow_context()):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/variable_scope.py
# Occurrences: Lines 2415-2418 (2 instances)

current_name_scope = ops.name_scope(name_scope, skip_on_eager=False)

# ==================================================
# Occurrences: Lines 2431-2434 (2 instances)

current_name_scope = current_name_scope or ops.name_scope(
    name_scope, skip_on_eager=False)

# ==================================================
# Line: 2456

entered_pure_variable_scope = pure_variable_scope.__enter__()

# ==================================================
# Line: 2477

entered_pure_variable_scope = pure_variable_scope.__enter__()

# ==================================================
# Line: 2490

current_name_scope_name = current_name_scope.__enter__()

# ==================================================
# Line: 2508

entered_pure_variable_scope = pure_variable_scope.__enter__()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_impl.py
# Occurrences: Lines 471-471 (2 instances)

sigmoid_features = math_ops.sigmoid(beta * features)

# ==================================================
# Occurrences: Lines 481-481 (2 instances)

return features * math_ops.sigmoid(beta * features), grad

# ==================================================
# Occurrences: Lines 590-595 (2 instances)

x_inv_norm = math_ops.rsqrt(math_ops.maximum(square_sum, epsilon))

# ==================================================
# Occurrences: Lines 1576-1578 (2 instances)

mean = constant_op.constant([])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
# Occurrences: Lines 994-1000 (3 instances)

nrows = len(pyval)

# ==================================================
# Occurrences: Lines 1394-1395 (2 instances)

row_partitions[1:], row_partitions[0].row_splits()[-1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
# Line: 1685

st = StructuredTensor.from_pyval(pyval)

# ==================================================
# Occurrences: Lines 1697-1701 (2 instances)

st = StructuredTensor.from_pyval(pyval)

# ==================================================
# Occurrences: Lines 1708-1710 (2 instances)

st = StructuredTensor.from_pyval(pyval)

# ==================================================
# Occurrences: Lines 1718-1720 (2 instances)

st = StructuredTensor.from_pyval(pyval)

# ==================================================
# Occurrences: Lines 1761-1766 (2 instances)

shape = tensor_shape.TensorShape((4,))

# ==================================================
# Line: 1773

shape = tensor_shape.TensorShape(())

# ==================================================
# Line: 1779

repr(rs._to_tensor_shape()), repr(tensor_shape.TensorShape(())))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
# Line: 401

nvals = st.nrows()

# ==================================================
# Occurrences: Lines 407-412 (2 instances)

st.row_partitions[axis - 2].nvals() if (axis - 2 >= 0) else st.nrows())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
# Line: 151

output_image = image_ops.resize_bilinear(
    input_image,
    output_shape[1:3],
    align_corners=align_corners,
    half_pixel_centers=half_pixel_centers)

# ==================================================
# Occurrences: Lines 161-171 (5 instances)

result_a = resize_bilinear_gradients(local_seed)

# ==================================================
# Occurrences: Lines 184-185 (4 instances)

result_a = resize_bilinear_gradients.eval(feed_dict=feed_dict)

# ==================================================
# Occurrences: Lines 328-332 (4 instances)

image_gradients_a, boxes_gradients_a = tape.gradient(
    upstream, [image, boxes])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_constant_op_test.py
# Line: 139

_ = constant_op.constant(a, dtypes.int32)

# ==================================================
# Line: 151

_ = constant_op.constant(a, dtypes.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/while_v2.py
# Line: 71

flat_orig_loop_vars = nest.flatten(orig_loop_vars, expand_composites=True)

# ==================================================
# Line: 238

num_flattened_outputs = len(nest.flatten(orig_loop_vars,
                                         expand_composites=True))

# ==================================================
# Occurrences: Lines 341-343 (2 instances)

num_original_outputs = len(while_op.outputs)

# ==================================================
# Line: 405

attr_value_pb2.AttrValue(i=len(while_op.outputs)))

# ==================================================
# Occurrences: Lines 472-473 (4 instances)

cond_graph.outer_graph = ops.get_default_graph()

# ==================================================
# Line: 1100

captured_tensor = self._indirect_captures.get(ops.tensor_id(tensor))

# ==================================================
# Line: 1106

captured_tensor = super(_WhileBodyGradFuncGraph, self)._capture_helper(
    tensor, name)

# ==================================================
# Line: 1121

captured_tensor = self._indirect_captures.get(ops.tensor_id(tensor))

# ==================================================
# Line: 1130

captured_tensor = super(_WhileBodyGradFuncGraph,
                        self)._capture_helper(tensor, name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_ops.py
# Occurrences: Lines 1286-1291 (2 instances)

dilations = _get_sequence(dilations, num_spatial_dims, channel_index,
                          "dilations")

# ==================================================
# Occurrences: Lines 1607-1611 (2 instances)

num_spatial_dims = len(window_shape)

# ==================================================
# Line: 3846

ndims = array_ops.rank(inputs)

# ==================================================
# Line: 3854

input_rank = array_ops.rank(inputs)

# ==================================================
# Line: 4354

labels_shape = array_ops.shape(labels)

# ==================================================
# Line: 4377

cost = _sparse_softmax_cross_entropy_with_rank_2_logits(
    precise_logits, labels, name=name)

# ==================================================
# Line: 4390

array_ops.shape(labels),

# ==================================================
# Line: 4397

cost = _sparse_softmax_cross_entropy_with_rank_2_logits(
    precise_logits, labels, name=name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/conv2d_benchmark.py
# Occurrences: Lines 69-85 (4 instances)

conv2d_op = nn_ops.conv2d(
    inp, filt, strides, padding, data_format=data_format)

# ==================================================
# Occurrences: Lines 143-145 (2 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_ops_test.py
# Occurrences: Lines 225-227 (3 instances)

x_tf = constant_op.constant(x_np, shape=x_np.shape)

# ==================================================
# Occurrences: Lines 235-237 (3 instances)

x_tf = constant_op.constant(x_np, shape=x_np.shape)

# ==================================================
# Line: 252

x_tf = constant_op.constant(x_np, shape=x_np.shape)

# ==================================================
# Line: 265

x_tf = constant_op.constant(x_np, shape=x_np.shape)

# ==================================================
# Occurrences: Lines 290-295 (2 instances)

rgb_tf_unknown = array_ops.placeholder(dtypes.uint8)

# ==================================================
# Occurrences: Lines 590-592 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 620-622 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 650-652 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 712-714 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 755-758 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 1964-1966 (3 instances)

x = constant_op.constant(x_np, shape=x_shape)

# ==================================================
# Occurrences: Lines 1980-1982 (3 instances)

x = constant_op.constant(x_np, shape=x_shape)

# ==================================================
# Occurrences: Lines 2537-2544 (3 instances)

y = array_ops.strided_slice(image_tf, begin, begin + size)

# ==================================================
# Occurrences: Lines 2558-2565 (3 instances)

y = array_ops.strided_slice(image_tf, begin, begin + size)

# ==================================================
# Occurrences: Lines 2905-2909 (2 instances)

y = image_ops.resize_images_v2(images, size)

# ==================================================
# Occurrences: Lines 2940-2940 (2 instances)

yshape = array_ops.shape(y)

# ==================================================
# Occurrences: Lines 2952-2952 (2 instances)

yshape = array_ops.shape(y)

# ==================================================
# Occurrences: Lines 2976-2977 (4 instances)

yshape = array_ops.shape(y)

# ==================================================
# Occurrences: Lines 2987-2988 (4 instances)

yshape = array_ops.shape(y)

# ==================================================
# Occurrences: Lines 2996-3007 (4 instances)

_ = resize_func(image, new_size, image_ops.ResizeMethod.BILINEAR)

# ==================================================
# Occurrences: Lines 3248-3258 (16 instances)

image = constant_op.constant(img_np, shape=input_shape)

# ==================================================
# Occurrences: Lines 3460-3464 (2 instances)

y = image_ops.resize_images(images, size)

# ==================================================
# Occurrences: Lines 3495-3495 (2 instances)

yshape = array_ops.shape(y)

# ==================================================
# Occurrences: Lines 3506-3506 (2 instances)

yshape = array_ops.shape(y)

# ==================================================
# Occurrences: Lines 3529-3530 (2 instances)

yshape = array_ops.shape(y)

# ==================================================
# Occurrences: Lines 3539-3540 (2 instances)

yshape = array_ops.shape(y)

# ==================================================
# Occurrences: Lines 3547-3558 (4 instances)

_ = resize_func(image, new_size, image_ops.ResizeMethodV1.BILINEAR)

# ==================================================
# Occurrences: Lines 3810-3826 (24 instances)

image = constant_op.constant(img_np, shape=input_shape)

# ==================================================
# Occurrences: Lines 5022-5023 (2 instances)

image_ops.convert_image_dtype(image, dtypes.uint8)

# ==================================================
# Line: 5387

scores = constant_op.constant([0.9])

# ==================================================
# Line: 5393

scores = constant_op.constant([0.9])

# ==================================================
# Occurrences: Lines 5400-5405 (2 instances)

scores = constant_op.constant([0.9])

# ==================================================
# Occurrences: Lines 5411-5418 (4 instances)

boxes = constant_op.constant([[0.0, 0.0, 1.0, 1.0]])

# ==================================================
# Occurrences: Lines 5459-5466 (5 instances)

boxes = constant_op.constant(boxes_np, dtype=input_dtype)

# ==================================================
# Occurrences: Lines 5474-5483 (6 instances)

boxes = constant_op.constant(boxes_np, dtype=input_dtype)

# ==================================================
# Occurrences: Lines 5489-5498 (6 instances)

boxes = constant_op.constant(boxes_np, dtype=input_dtype)

# ==================================================
# Line: 5506

max_output_size = constant_op.constant(max_output_size_np)

# ==================================================
# Line: 5513

selected_indices = self.evaluate(selected_indices)

# ==================================================
# Occurrences: Lines 5777-5778 (2 instances)

img1 = array_ops.placeholder(dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 5818-5819 (2 instances)

image1 = self._RandomImage((8, 8, 1), 1)

# ==================================================
# Occurrences: Lines 5831-5832 (2 instances)

image1 = self._RandomImage((10, 8, 8, 1), 1)

# ==================================================
# Occurrences: Lines 5876-5877 (2 instances)

img1 = self._RandomImage((10, 8, 8, 1), 255)

# ==================================================
# Occurrences: Lines 6009-6010 (2 instances)

img1 = self._RandomImage((1, 16, 16, 3), 255)

# ==================================================
# Occurrences: Lines 6024-6025 (2 instances)

img1 = self._RandomImage((1, 16, 16, 3), 255)

# ==================================================
# Occurrences: Lines 6204-6205 (2 instances)

img1 = self._RandomImage((1, 180, 240, 3), 255)

# ==================================================
# Line: 6505

op = image_ops_impl.crop_and_resize_v2(
    image=array_ops.zeros((2, 1, 1, 1)),
    boxes=[[1.0e+40, 0, 0, 0]],
    box_indices=[1],
    crop_size=[1, 1])

# ==================================================
# Line: 6515

op = image_ops_impl.crop_and_resize_v2(
    image=array_ops.zeros((2, 1, 1, 1)),
    boxes=[[1.0e+40, 0, 0, 0]],
    box_indices=[1],
    crop_size=[1, 1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parsing_config.py
# Line: 496

default_value = ops.convert_to_tensor(
    default_value, dtype=dtype, name=key_name)

# ==================================================
# Line: 504

default_value = ops.convert_to_tensor(
    default_value, dtype=dtype, name=key_name)

# ==================================================
# Line: 572

feature_tensor_shape = tensor_shape.as_shape(feature.shape)

# ==================================================
# Line: 583

self.dense_shapes.append(tensor_shape.as_shape(feature.shape))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/op_selector_test.py
# Occurrences: Lines 48-55 (6 instances)

g0 = ops_lib.Graph()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/signal/reconstruction_ops.py
# Line: 125

signal = array_ops.reshape(signal, shape)

# ==================================================
# Line: 140

signal = array_ops.reshape(signal, shape)

# ==================================================
# Line: 151

signal = array_ops.reshape(signal, shape)

# ==================================================
# Line: 158

signal = array_ops.reshape(signal, shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/signal/shape_ops.py
# Line: 134

array_ops.shape(signal))

# ==================================================
# Line: 174

signal_shape = array_ops.shape(signal)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/signal/dct_ops.py
# Line: 169

weights = _array_ops.pad(
    _array_ops.expand_dims(n1, 0), [[0, axis_dim - 1]],
    constant_values=n2)

# ==================================================
# Line: 181

weights = _array_ops.pad(
    _array_ops.expand_dims(n1, 0), [[0, axis_dim - 1]],
    constant_values=n2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/init_ops_v2.py
# Occurrences: Lines 604-607 (2 instances)

stddev = math.sqrt(scale) / .87962566103423978

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_grad_test_base.py
# Occurrences: Lines 103-110 (12 instances)

input_tensor = constant_op.constant(x, shape=in_shape)

# ==================================================
# Occurrences: Lines 628-632 (3 instances)

x_reds = np.ones((in_shape[0], in_shape[1], in_shape[2])).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
# Occurrences: Lines 108-111 (4 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
# Occurrences: Lines 38-40 (2 instances)

data = np.random.random_sample(shape).astype(dtype.as_numpy_dtype)

# ==================================================
# Occurrences: Lines 158-165 (4 instances)

x = constant_op.constant(_random_complex(x_shape, x_dtype))

# ==================================================
# Occurrences: Lines 175-182 (4 instances)

x = constant_op.constant(_random_complex(x_shape, x_dtype))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/np_config_test.py
# Line: 29

getattr(a, name)

# ==================================================
# Line: 35

_ = getattr(a, name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
# Occurrences: Lines 1190-1193 (9 instances)

arr = (np.asarray(state.randn(*shape) * 100, dtype=dtype) +

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
# Occurrences: Lines 444-447 (2 instances)

a = ravel(a)

# ==================================================
# Occurrences: Lines 808-810 (2 instances)

original_shape = (repeats_np.sum(),)

# ==================================================
# Line: 938

axis1, axis2 = adjust_axes((axis1, axis2), a_rank)

# ==================================================
# Line: 944

axis1, axis2 = adjust_axes((axis1, axis2), a_rank)

# ==================================================
# Line: 1594

return math_ops.sign(x)

# ==================================================
# Line: 1600

result = math_ops.sign(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
# Occurrences: Lines 303-303 (2 instances)

axis_a = np_utils.add(axis_a, array_ops.rank(a))

# ==================================================
# Occurrences: Lines 314-314 (2 instances)

math_ops.range(axis + 1, array_ops.rank(a)),

# ==================================================
# Occurrences: Lines 322-322 (2 instances)

axis == np_utils.subtract(array_ops.rank(a), 1),

# ==================================================
# Occurrences: Lines 338-338 (2 instances)

array_ops.zeros([array_ops.rank(a) - 1, 2], dtypes.int32),

# ==================================================
# Occurrences: Lines 356-356 (2 instances)

r = array_ops.rank(a)

# ==================================================
# Line: 1226

result = math_ops.linspace(start, stop, num, axis=axis)

# ==================================================
# Line: 1239

result = math_ops.linspace(start, stop, num, axis=axis)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
# Occurrences: Lines 56-59 (2 instances)

x = np.ones([1, 2])

# ==================================================
# Line: 261

dataset = tf.data.Dataset.from_tensor_slices(values_as_array)

# ==================================================
# Line: 278

dataset = tf.data.Dataset.from_tensor_slices(values_as_array).batch(2)

# ==================================================
# Occurrences: Lines 320-325 (2 instances)

[tf.keras.layers.Dense(100), ProjectionLayer(2)])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_test.py
# Occurrences: Lines 126-127 (2 instances)

y_pos_axis = nn_ops.softmax_v2(arr, axis=0)

# ==================================================
# Occurrences: Lines 214-215 (2 instances)

y_pos_axis = nn_ops.log_softmax_v2(arr, axis=0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/stateless_random_ops.py
# Line: 383

key, counter, alg = random_ops_util.get_key_counter_alg(seed, alg)

# ==================================================
# Line: 391

key, counter, alg = random_ops_util.get_key_counter_alg(seed, alg)

# ==================================================
# Line: 402

key, counter, alg = random_ops_util.get_key_counter_alg(seed, alg)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/batch_ops_test.py
# Occurrences: Lines 133-134 (2 instances)

inp0 = array_ops.placeholder(dtype=dtypes.int32, shape=[1])

# ==================================================
# Occurrences: Lines 244-247 (2 instances)

batched_index = constant_op.constant(
    value=np.random.randint(0, 100, size=(3, 3, 1)), dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 615-622 (4 instances)

original_input = random_ops.random_uniform(
    shape=(3, 1), dtype=dtypes.float64, maxval=None)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/while_v2_indexed_slices_rewriter.py
# Line: 187

values = array_ops.zeros(
    values_shape, dtype=values_out.dtype, name="values_init")

# ==================================================
# Line: 195

values = array_ops.zeros(
    values_shape, dtype=values_out.dtype, name="values_init")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/control_flow_ops_benchmark.py
# Line: 61

start_time = time.time()

# ==================================================
# Line: 67

wall_time=time.time() - start_time,

# ==================================================
# Line: 84

start_time = time.time()

# ==================================================
# Line: 90

wall_time=time.time() - start_time,

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/collective_ops_benchmark.py
# Occurrences: Lines 63-69 (15 instances)

overall_start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
# Occurrences: Lines 152-156 (4 instances)

t = constant_op.constant(tensor_value)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/math_ops_test.py
# Occurrences: Lines 551-565 (4 instances)

x = dtype(1)

# ==================================================
# Occurrences: Lines 622-624 (2 instances)

tensor = array_ops.ones([10, 10])

# ==================================================
# Occurrences: Lines 690-693 (4 instances)

addn = math_ops.add_n(input_vars)

# ==================================================
# Occurrences: Lines 1022-1024 (2 instances)

_ = math_ops.div_no_nan(x, y)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
# Occurrences: Lines 74-77 (4 instances)

m_val = np.random.random_sample(param_shape).astype(np.float32)

# ==================================================
# Occurrences: Lines 124-127 (4 instances)

m_val = np.random.random_sample(param_shape).astype(np.float64)

# ==================================================
# Occurrences: Lines 208-213 (6 instances)

x_val = np.random.random_sample(x_shape).astype(np.float32)

# ==================================================
# Occurrences: Lines 261-264 (4 instances)

m_val = np.random.random_sample(param_shape).astype(np.float32)

# ==================================================
# Occurrences: Lines 304-307 (4 instances)

m_val = np.random.random_sample(param_shape).astype(numpy_param_dtype)

# ==================================================
# Occurrences: Lines 376-376 (2 instances)

op_c, op_m, op_v, op_s = self._opSuffStats(x, axes, shift, keep_dims)

# ==================================================
# Occurrences: Lines 384-384 (2 instances)

op_c, op_m, op_v, op_s = self._opSuffStats(x, axes, shift, keep_dims)

# ==================================================
# Occurrences: Lines 421-425 (3 instances)

mean_ss = np.random.random_sample(shape).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_nn_test.py
# Occurrences: Lines 60-61 (2 instances)

y_pos_axis = nn_ops.log_softmax_v2(arr, axis=0)

# ==================================================
# Line: 167

z = self.evaluate(y_wt)

# ==================================================
# Line: 173

z = self.evaluate(y_wt)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
# Occurrences: Lines 49-50 (2 instances)

t1 = self.evaluate(init(shape, dtype))

# ==================================================
# Occurrences: Lines 207-208 (2 instances)

init1 = init_ops_v2.RandomUniform(0, 7, seed=1)

# ==================================================
# Occurrences: Lines 241-242 (2 instances)

init1 = init_ops_v2.RandomNormal(0, 7, seed=1)

# ==================================================
# Occurrences: Lines 279-280 (2 instances)

init1 = init_ops_v2.TruncatedNormal(0.0, 1.0, seed=1)

# ==================================================
# Occurrences: Lines 398-399 (2 instances)

init1 = init_ops_v2.Orthogonal(seed=1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/rnn.py
# Occurrences: Lines 245-251 (3 instances)

new_output, new_state = call_cell()

# ==================================================
# Occurrences: Lines 266-270 (3 instances)

new_output, new_state = call_cell()

# ==================================================
# Line: 1169

time = constant_op.constant(0, dtype=dtypes.int32)

# ==================================================
# Line: 1178

constant_op.constant(0, dtype=dtypes.int32))

# ==================================================
# Line: 1200

flat_emit_structure = nest.flatten(emit_structure)

# ==================================================
# Line: 1208

flat_emit_size = nest.flatten(emit_structure)

# ==================================================
# Occurrences: Lines 1421-1422 (2 instances)

if tensor_shape.dimension_value(fixed_batch_size):

# ==================================================
# Line: 1451

tensor_shape.dimension_value(fixed_batch_size),

# ==================================================
# Line: 1537

state_name_flat = nest.flatten(state_name)

# ==================================================
# Line: 1562

state_name = nest.flatten(state_name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_grad.py
# Occurrences: Lines 238-243 (3 instances)

grad = conj(grad)

# ==================================================
# Occurrences: Lines 266-271 (3 instances)

conj(a), grad, transpose_output=True, conjugate_output=True)

# ==================================================
# Line: 282

grad_a = matmul(b, conj(grad), adjoint_a=adj_b)

# ==================================================
# Line: 291

grad_a = matmul(b, conj(grad), transpose_a=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
# Line: 329

output = math_ops.conj(output)

# ==================================================
# Occurrences: Lines 339-342 (5 instances)

output_shape = _prefer_static_shape(output)

# ==================================================
# Line: 357

output = math_ops.conj(output)

# ==================================================
# Line: 377

_prefer_static_shape(output)[:-2], matrix_shape))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/slicing.py
# Line: 132

param_batch_rank = array_ops.size(param_batch_shape)

# ==================================================
# Line: 139

tensor_util.constant_value(array_ops.size(param_batch_shape)) == 0):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
# Line: 299

zeros = array_ops.zeros(shape=special_shape, dtype=self.dtype)

# ==================================================
# Line: 306

zeros = array_ops.zeros(shape=special_shape, dtype=self.dtype)

# ==================================================
# Occurrences: Lines 318-326 (6 instances)

array_ops.shape(x)[:-2],

# ==================================================
# Line: 332

zeros = array_ops.zeros(shape=output_shape, dtype=x.dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
# Line: 521

y_mat = self.matmul(x_mat, adjoint=adjoint)

# ==================================================
# Line: 530

y_mat = self.matmul(x_mat, adjoint=adjoint)

# ==================================================
# Line: 723

solution_mat = self.solve(rhs_mat, adjoint=adjoint)

# ==================================================
# Line: 734

solution_mat = self.solve(rhs_mat, adjoint=adjoint)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
# Line: 388

zeros = array_ops.zeros(shape=special_shape, dtype=self.dtype)

# ==================================================
# Line: 395

zeros = array_ops.zeros(shape=special_shape, dtype=self.dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
# Occurrences: Lines 295-296 (2 instances)

if tensor_shape.dimension_value(self.u.shape[-1]) is not None:

# ==================================================
# Line: 457

v, u = self._get_uv_as_tensors()

# ==================================================
# Line: 465

u, v = self._get_uv_as_tensors()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
# Occurrences: Lines 294-298 (3 instances)

squarings = math_ops.maximum(
    math_ops.floor(
        math_ops.log(l1_norm / maxnorm) / math_ops.log(const(2.0))), 0)

# ==================================================
# Occurrences: Lines 307-311 (3 instances)

squarings = math_ops.maximum(
    math_ops.floor(
        math_ops.log(l1_norm / maxnorm) / math_ops.log(const(2.0))), 0)

# ==================================================
# Line: 653

rhs = math_ops.conj(rhs)

# ==================================================
# Line: 663

rhs = math_ops.conj(rhs)

# ==================================================
# Line: 1355

alpha = math_ops.real(alpha)

# ==================================================
# Occurrences: Lines 1451-1451 (2 instances)

mid = midpoint(lower, upper)

# ==================================================
# Occurrences: Lines 1461-1461 (2 instances)

return midpoint(lower, upper)

# ==================================================
# Line: 1577

return math_ops.real(alpha)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
# Occurrences: Lines 397-400 (4 instances)

operator_a, mat_a = self.operator_and_matrix(
    shapes_info, dtype, use_placeholder=use_placeholder)

# ==================================================
# Occurrences: Lines 417-420 (4 instances)

operator_a, mat_a = self.operator_and_matrix(
    shapes_info, dtype, use_placeholder=use_placeholder)

# ==================================================
# Occurrences: Lines 1262-1268 (2 instances)

samples = random_ops.random_normal(
    shape, mean=mean, stddev=stddev, dtype=dtype.real_dtype, seed=seed)

# ==================================================
# Occurrences: Lines 1300-1310 (2 instances)

samples = random_ops.random_uniform(
    shape, dtype=dtype.real_dtype, minval=minval, maxval=maxval, seed=seed)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
# Line: 432

if len(self.operators) == 1:

# ==================================================
# Line: 441

blockwise_dim = len(self.operators)

# ==================================================
# Line: 659

y_mat = self.matmul(x_mat, adjoint=adjoint)

# ==================================================
# Line: 668

y_mat = self.matmul(x_mat, adjoint=adjoint)

# ==================================================
# Line: 913

solution_mat = self.solve(rhs_mat, adjoint=adjoint)

# ==================================================
# Line: 923

solution_mat = self.solve(rhs_mat, adjoint=adjoint)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/map_fn.py
# Occurrences: Lines 534-536 (2 instances)

spec = type_spec.type_spec_from_value(elem)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ref_variable.py
# Occurrences: Lines 398-411 (4 instances)

self._initial_value = ops.convert_to_tensor(
    initial_value, name="initial_value", dtype=dtype)

# ==================================================
# Occurrences: Lines 422-427 (2 instances)

self._initial_value.get_shape()

# ==================================================
# Line: 435

initial_value_shape = self._initial_value.get_shape()

# ==================================================
# Occurrences: Lines 454-457 (2 instances)

self._snapshot = array_ops.identity(self._variable, name="read")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_ops.py
# Occurrences: Lines 136-138 (2 instances)

x_arg_name = next(arg_names)

# ==================================================
# Occurrences: Lines 171-171 (2 instances)

bound_kwargs[y_arg_name] = _convert_or_cast(y, target_type, "y")

# ==================================================
# Occurrences: Lines 192-197 (6 instances)

bound_kwargs[x_arg_name] = _convert_or_cast(x, target_type, "x")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/array_grad_test.py
# Occurrences: Lines 142-143 (2 instances)

begin = constant_op.constant([1], dtype=dtypes.int64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/embedding_ops.py
# Line: 178

tensor_shape.dimension_value(params[p].get_shape()[0]))

# ==================================================
# Line: 184

param_p_dim = tensor_shape.dimension_value(params[p].get_shape()[0])

# ==================================================
# Line: 1085

segment_ids = math_ops.cast(segment_ids, dtypes.int32)

# ==================================================
# Occurrences: Lines 1121-1125 (2 instances)

embeddings = math_ops.segment_sum(embeddings, segment_ids)

# ==================================================
# Line: 1136

segment_ids = math_ops.cast(segment_ids, dtypes.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/collective_ops_xla_test.py
# Occurrences: Lines 59-60 (4 instances)

input_tensor1 = array_ops.identity(f(constant))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/template.py
# Occurrences: Lines 333-343 (4 instances)

ops.get_collection_ref(ops.GraphKeys.GLOBAL_VARIABLES))

# ==================================================
# Line: 356

variables = ops.get_collection_ref(ops.GraphKeys.GLOBAL_VARIABLES)

# ==================================================
# Line: 368

result = self._func(*args, **kwargs)

# ==================================================
# Occurrences: Lines 624-632 (4 instances)

vars_at_start = self._template_store.variables()

# ==================================================
# Line: 638

trainable_variables = self._template_store.trainable_variables()

# ==================================================
# Line: 652

variables = self._template_store.variables()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/check_ops.py
# Line: 468

test_op = op_func(x, y)

# ==================================================
# Line: 502

condition = math_ops.reduce_all(op_func(x, y))

# ==================================================
# Line: 1837

rank = len(sizes.symbolic_sizes)

# ==================================================
# Line: 1882

tensor_dim = i - len(sizes.symbolic_sizes)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg_grad.py
# Line: 593

l2_regularizer = math_ops.cast(op.inputs[2], a.dtype.base_dtype)

# ==================================================
# Line: 618

l2_regularizer = math_ops.cast(op.inputs[2], a.dtype.base_dtype)

# ==================================================
# Line: 656

num_bands = array_ops.shape(a)[-2]

# ==================================================
# Line: 676

a_shape = array_ops.shape(a)

# ==================================================
# Line: 741

vt = _linalg.adjoint(v)

# ==================================================
# Line: 754

mid = array_ops.matrix_diag(grad_e)

# ==================================================
# Line: 766

vt = _linalg.adjoint(v)

# ==================================================
# Line: 772

vt, math_ops.matmul(array_ops.matrix_diag(grad_e), vt))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/tensor_math_operator_overrides_test.py
# Occurrences: Lines 42-50 (6 instances)

x = constant_op.constant([1, 2, 3])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_d9m_test.py
# Occurrences: Lines 64-69 (6 instances)

scale = constant_op.constant(
    np.random.normal(size=scale_shape), dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 84-92 (4 instances)

op_output = nn_impl.fused_batch_norm(
    x,
    scale,
    offset,
    mean,
    variance,
    data_format=data_format,
    is_training=is_training,
    exponential_avg_factor=1.01)

# ==================================================
# Occurrences: Lines 99-107 (4 instances)

op_output_b = nn_impl.fused_batch_norm(
    x,
    scale,
    offset,
    mean,
    variance,
    data_format=data_format,
    is_training=is_training,
    exponential_avg_factor=1.01)

# ==================================================
# Occurrences: Lines 149-156 (12 instances)

grad = tape.gradient(gradient_injector_output, backprop_to)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# Occurrences: Lines 642-644 (4 instances)

arr = np.array(r.randn(*shape)).astype(dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/memory_tests/custom_gradient_memory_test.py
# Occurrences: Lines 94-99 (2 instances)

run(f_no_recompute)

# ==================================================
# Occurrences: Lines 110-111 (2 instances)

res_no_recompute = run(f_no_recompute)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/critical_section_ops.py
# Occurrences: Lines 271-281 (4 instances)

existing_ops = ops.get_default_graph().get_operations()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_np_array_ops_test.py
# Occurrences: Lines 408-409 (10 instances)

actual = np_array_ops.arange(start, stop, step)

# ==================================================
# Occurrences: Lines 427-428 (10 instances)

actual = np_array_ops.arange(start, stop, step)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/control_flow_state.py
# Line: 178

self._grad_context = control_flow_ops.WhileContext(
    maximum_iterations=forward_ctxt.maximum_iterations,
    parallel_iterations=forward_ctxt.parallel_iterations,
    back_prop=forward_ctxt.back_prop,
    swap_memory=forward_ctxt.swap_memory,
    name=forward_ctxt.name,
    grad_state=self)

# ==================================================
# Line: 192

self._grad_context = control_flow_ops.WhileContext(
    maximum_iterations=forward_ctxt.maximum_iterations,
    parallel_iterations=forward_ctxt.parallel_iterations,
    back_prop=forward_ctxt.back_prop,
    swap_memory=forward_ctxt.swap_memory,
    name=forward_ctxt.name,
    grad_state=self)

# ==================================================
# Line: 355

push = gen_data_flow_ops.stack_push_v2(
    enter_acc, value, swap_memory=swap_enabled)

# ==================================================
# Occurrences: Lines 368-375 (2 instances)

push = gen_data_flow_ops.stack_push_v2(
    enter_acc, value, swap_memory=swap_enabled)

# ==================================================
# Line: 617

result = array_ops.zeros(val_shape.dims, val.dtype)

# ==================================================
# Line: 638

result = array_ops.zeros(val_shape.dims, val.dtype)

# ==================================================
# Line: 693

zeros_shape = array_ops.shape_internal(val, optimize=False)

# ==================================================
# Line: 699

zeros_shape = array_ops.shape_internal(val, optimize=False)

# ==================================================
# Occurrences: Lines 736-736 (3 instances)

next_grad_val = control_flow_ops._NextIteration(grad_val)

# ==================================================
# Occurrences: Lines 751-751 (3 instances)

next_grad_val = control_flow_ops._NextIteration(grad_val)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/special_math.py
# Occurrences: Lines 384-385 (2 instances)

even_sum = array_ops.zeros_like(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
# Occurrences: Lines 827-834 (4 instances)

ildjs = self._inverse_log_det_jacobian(y, **kwargs)

# ==================================================
# Occurrences: Lines 846-853 (4 instances)

ildj = self._inverse_log_det_jacobian(y, **kwargs)

# ==================================================
# Line: 931

fldjs = self._forward_log_det_jacobian(x, **kwargs)  # No caching.

# ==================================================
# Occurrences: Lines 937-938 (2 instances)

y = self._forward(x, **kwargs)

# ==================================================
# Line: 949

ildj = -self._forward_log_det_jacobian(x, **kwargs)

# ==================================================
# Occurrences: Lines 955-956 (2 instances)

else self._forward(x, **kwargs))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
# Line: 289

_ndims_from_shape(self._override_event_shape), self._zero))

# ==================================================
# Line: 304

override_event_ndims = _ndims_from_shape(self._override_event_shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/util.py
# Occurrences: Lines 1249-1254 (2 instances)

grid = ops.convert_to_tensor(grid, name="grid", dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg_ops.py
# Line: 353

matrix_shape = matrix.get_shape()[-2:]

# ==================================================
# Line: 374

tensor_shape = matrix.get_shape()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/functional_ops.py
# Line: 331

a = nest.map_structure(lambda elem: elem.read(i), elems_ta)

# ==================================================
# Line: 338

elem = nest.map_structure(lambda elem: elem.read(i), elems_ta)

# ==================================================
# Line: 842

return gen_functional_ops._if(
    cond, inputs, tlist, then_branch, else_branch, name=name)

# ==================================================
# Line: 854

ret = gen_functional_ops._if(
    cond, inputs, tlist, then_branch, else_branch, name=name)

# ==================================================
# Occurrences: Lines 982-986 (2 instances)

input_attr = attr_value_pb2.AttrValue()

# ==================================================
# Occurrences: Lines 1112-1116 (2 instances)

input_attr = attr_value_pb2.AttrValue()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_ops_test.py
# Occurrences: Lines 238-242 (2 instances)

res = unary_api_specific_dtype(tensor_input)

# ==================================================
# Occurrences: Lines 1013-1019 (8 instances)

_ = math_ops.matmul(x, y)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/transpose_benchmark.py
# Occurrences: Lines 49-53 (2 instances)

transpose_op = array_ops.transpose(t, perm)

# ==================================================
# Occurrences: Lines 81-84 (2 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_ops_impl.py
# Occurrences: Lines 948-952 (2 instances)

img_w, dynamic_w = _get_dim(image, 1)

# ==================================================
# Occurrences: Lines 1122-1125 (2 instances)

image = array_ops.expand_dims(image, 0)

# ==================================================
# Occurrences: Lines 1228-1231 (2 instances)

image = array_ops.expand_dims(image, 0)

# ==================================================
# Occurrences: Lines 1350-1353 (2 instances)

image = array_ops.expand_dims(image, 0)

# ==================================================
# Line: 1520

images = array_ops.squeeze(images, axis=[0])

# ==================================================
# Line: 1530

images = array_ops.squeeze(images, axis=[0])

# ==================================================
# Occurrences: Lines 1808-1811 (2 instances)

image = array_ops.expand_dims(image, 0)

# ==================================================
# Line: 2540

cast = math_ops.cast(image, dtype)

# ==================================================
# Line: 2551

cast = math_ops.cast(image, dtype)

# ==================================================
# Occurrences: Lines 4297-4298 (2 instances)

g = array_ops.reshape(g, shape=[1, -1]) + array_ops.reshape(g, shape=[-1, 1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/init_ops.py
# Occurrences: Lines 874-878 (2 instances)

stddev = math.sqrt(scale) / .87962566103423978

# ==================================================
# Occurrences: Lines 1241-1245 (2 instances)

p = self._block_orth(
    self._symmetric_projection(cout), self._symmetric_projection(cout))

# ==================================================
# Occurrences: Lines 1373-1375 (2 instances)

p = self._block_orth(self._symmetric_projection(cout))

# ==================================================
# Occurrences: Lines 1539-1545 (2 instances)

p = self._block_orth(
    self._symmetric_projection(cout), self._symmetric_projection(cout),
    self._symmetric_projection(cout))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
# Line: 537

rt = RaggedTensor.from_row_splits(values, row_splits)

# ==================================================
# Line: 546

_ = rt.to_list()

# ==================================================
# Occurrences: Lines 556-557 (2 instances)

rt = RaggedTensor.from_row_splits(values, row_splits)

# ==================================================
# Occurrences: Lines 567-568 (2 instances)

rt = RaggedTensor.from_row_splits(values, row_splits)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
# Occurrences: Lines 670-674 (2 instances)

out = rt_val.to_tensor(default_val, shape=shape_val)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch.py
# Occurrences: Lines 38-39 (2 instances)

x_is_ragged = ragged_tensor.is_ragged(x)

# ==================================================
# Occurrences: Lines 70-75 (3 instances)

x_values = x.flat_values if ragged_tensor.is_ragged(x) else x

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
# Occurrences: Lines 1201-1208 (2 instances)

rt = ragged_tensor.RaggedTensor.from_uniform_row_length(
    ragged_factory_ops.constant([[1, 2], [3]]), uniform_row_length=2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
# Line: 147

masked_values = boolean_mask(data, mask)

# ==================================================
# Line: 173

return ragged_tensor.RaggedTensor.from_row_splits(
    masked_values, masked_splits, validate=False)

# ==================================================
# Line: 183

return boolean_mask(data, mask)

# ==================================================
# Line: 208

masked_values = ragged_tensor.RaggedTensor.from_row_splits(
    masked_values, masked_splits, validate=False)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# Occurrences: Lines 54-59 (2 instances)

rp = RowPartition.from_row_splits(row_splits=[0, 4, 4, 7, 8, 8])

# ==================================================
# Line: 70

inner_rt = RowPartition.from_row_splits(row_splits=[0, 4, 4, 7, 8, 8])

# ==================================================
# Line: 485

partition = factory(**kwargs)

# ==================================================
# Line: 500

partition = factory(**kwargs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_autograph.py
# Line: 25

init_vars = get_state()

# ==================================================
# Line: 37

return (iterate_index,) + get_state()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
# Occurrences: Lines 2748-2750 (2 instances)

value = components.pop()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
# Line: 55

new_static_inner_shape = _batch_static_inner_shape(
    spec._static_inner_shape, batch_size)  # pylint:disable=protected-access

# ==================================================
# Line: 73

new_static_inner_shape = _batch_static_inner_shape(
    spec._static_inner_shape, batch_size)  # pylint:disable=protected-access

# ==================================================
# Line: 767

first_dimension = self._num_slices_in_dimension(-new_inner_rank)

# ==================================================
# Line: 780

first_dimension = self._num_slices_in_dimension(-new_inner_rank)

# ==================================================
# Occurrences: Lines 973-978 (2 instances)

new_inner_shape = self._alt_inner_shape(rank - inner_axis)

# ==================================================
# Occurrences: Lines 1724-1725 (2 instances)

x_is_ragged = ragged_tensor.is_ragged(x)

# ==================================================
# Occurrences: Lines 1760-1765 (3 instances)

x_values = x.flat_values if ragged_tensor.is_ragged(x) else x

# ==================================================
# Occurrences: Lines 1791-1792 (2 instances)

x_is_ragged = ragged_tensor.is_ragged(x)

# ==================================================
# Occurrences: Lines 1823-1824 (2 instances)

x_values = x.flat_values if ragged_tensor.is_ragged(x) else x

# ==================================================
# Line: 2197

return array_ops.broadcast_to(rt, self._target_inner_shape_int32())

# ==================================================
# Line: 2208

rt = array_ops.broadcast_to(rt, self._target_inner_shape_int32())

# ==================================================
# Line: 2356

b_layer = math_ops.range(b_0)

# ==================================================
# Occurrences: Lines 2363-2369 (3 instances)

a_layer = _LayerBroadcaster.from_gather_index(a_gi)

# ==================================================
# Occurrences: Lines 2377-2384 (4 instances)

a_layer = _LayerBroadcaster.from_gather_index(a_gi)

# ==================================================
# Occurrences: Lines 2413-2414 (2 instances)

a_layer = _LayerBroadcaster.from_gather_index(a_gi)

# ==================================================
# Line: 2435

b_layer = math_ops.range(b_0)

# ==================================================
# Line: 2459

a_layer = math_ops.range(a_0)

# ==================================================
# Occurrences: Lines 2465-2466 (2 instances)

a_layer = math_ops.range(a_0)

# ==================================================
# Occurrences: Lines 2564-2567 (3 instances)

[bc_1, c_1b] = _broadcast_half(bc_0, b_1)

# ==================================================
# Line: 2574

[bc_1, c_1b] = _broadcast_half(bc_0, b_1)

# ==================================================
# Occurrences: Lines 2582-2583 (2 instances)

[bc_1, c_1b] = _broadcast_half(bc_0, b_1)

# ==================================================
# Line: 2597

ac_1 = _LayerBroadcaster.from_gather_index(ac_1_gather_index)

# ==================================================
# Occurrences: Lines 2645-2653 (4 instances)

[ac_1, _] = _broadcast_half(ac_0, a_1)

# ==================================================
# Occurrences: Lines 2659-2661 (2 instances)

[ac_1, c_1a] = _broadcast_half(ac_0, a_1)

# ==================================================
# Occurrences: Lines 2669-2675 (4 instances)

[ac_1, _] = _broadcast_half(ac_0, a_1)

# ==================================================
# Occurrences: Lines 2683-2684 (2 instances)

[ac_1, c_1a] = _broadcast_half(ac_0, a_1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_to_sparse_op_test.py
# Line: 118

st = rt.to_sparse()

# ==================================================
# Line: 125

st = rt.to_sparse()

# ==================================================
# Line: 131

st = rt.to_sparse()

# ==================================================
# Occurrences: Lines 148-153 (2 instances)

bad_rt2 = ragged_tensor.RaggedTensor.from_row_splits(
    row_splits=[0, 5], values=empty_vector, validate=False)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_util_test.py
# Occurrences: Lines 144-148 (4 instances)

data = constant_op.constant(data)

# ==================================================
# Occurrences: Lines 209-213 (4 instances)

data = constant_op.constant(data)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
# Line: 547

result = array_ops.expand_dims(result, axis=0)

# ==================================================
# Occurrences: Lines 589-592 (2 instances)

result = _ragged_segment_aggregate(unsorted_segment_op, rt_input.values,
                                   segment_ids, num_segments, separator)

# ==================================================
# Line: 599

result = _ragged_segment_aggregate(unsorted_segment_op, rt_input.values,
                                   segment_ids, num_segments, separator)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_bincount_ops.py
# Occurrences: Lines 171-175 (2 instances)

weights = validate_ragged_weights(arr, weights, dtype)

# ==================================================
# Occurrences: Lines 355-359 (2 instances)

weights = validate_ragged_weights(values, weights)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
# Line: 73

rt = RaggedTensor.from_row_splits(
    values=[3, 1, 4, 1, 5, 9, 2, 6], row_splits=[0, 4, 4, 7, 8, 8])

# ==================================================
# Line: 91

inner_rt = RaggedTensor.from_row_splits(
    values=[3, 1, 4, 1, 5, 9, 2, 6], row_splits=[0, 4, 4, 7, 8, 8])

# ==================================================
# Line: 125

rt_value = ragged_tensor_value.RaggedTensorValue(values, splits)

# ==================================================
# Line: 136

values=ragged_tensor_value.RaggedTensorValue(values, splits),

# ==================================================
# Occurrences: Lines 1506-1511 (2 instances)

unbatched_spec = batched_spec._unbatch()

# ==================================================
# Occurrences: Lines 1561-1564 (2 instances)

y = func(x)

# ==================================================
# Occurrences: Lines 1943-1948 (2 instances)

actual = rt.numpy()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/row_partition.py
# Line: 255

const_rowids = tensor_util.constant_value(value_rowids)

# ==================================================
# Line: 269

const_rowids = tensor_util.constant_value(value_rowids)

# ==================================================
# Line: 592

const_row_length = tensor_util.constant_value(uniform_row_length)

# ==================================================
# Line: 606

const_uniform_row_length = tensor_util.constant_value(uniform_row_length)

# ==================================================
# Line: 649

const_row_length = tensor_util.constant_value(uniform_row_length)

# ==================================================
# Line: 1259

self._nvals = tensor_shape.TensorShape([0])

# ==================================================
# Line: 1265

self._nvals = tensor_shape.TensorShape([0])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Occurrences: Lines 1702-1706 (2 instances)

nodes_at_a = len(g.as_graph_def().node)

# ==================================================
# Occurrences: Lines 1713-1715 (2 instances)

nodes_at_b = len(g.as_graph_def().node)

# ==================================================
# Line: 1793

nodes_at_a = len(g.as_graph_def().node)

# ==================================================
# Line: 1799

nodes_at_b = len(g.as_graph_def().node)

# ==================================================
# Occurrences: Lines 1807-1809 (2 instances)

nodes_at_b = len(g.as_graph_def().node)

# ==================================================
# Line: 1864

shape_e = tensor_shape.TensorShape(shape_e)

# ==================================================
# Line: 1872

shape_e = tensor_shape.TensorShape(shape_e)

# ==================================================
# Occurrences: Lines 2325-2327 (2 instances)

b = DynamicRaggedShape._from_inner_shape([3])

# ==================================================
# Occurrences: Lines 2335-2338 (2 instances)

a = DynamicRaggedShape._from_inner_shape([3])

# ==================================================
# Occurrences: Lines 2346-2349 (3 instances)

a = DynamicRaggedShape._from_inner_shape([3])

# ==================================================
# Occurrences: Lines 3048-3049 (4 instances)

rts_a = DynamicRaggedShape._from_inner_shape(x)

# ==================================================
# Occurrences: Lines 4143-4146 (2 instances)

static_inner_shape=tensor_shape.TensorShape([None]),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py
# Occurrences: Lines 139-142 (8 instances)

result0 = strategy.experimental_local_results(next(ds))

# ==================================================
# Occurrences: Lines 220-223 (8 instances)

result0 = strategy.experimental_local_results(next(ds))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
# Line: 437

expected=sum([1, 2, 3, 4, 5, 6, 7, 8, 9])),

# ==================================================
# Line: 479

expected=sum([1, 2, 3, 4, 5, 6, 7, 8, 9])),

# ==================================================
# Line: 492

expected=[[[sum([1, 2, 3, 4, 5, 6, 7, 8, 9])]]]),

# ==================================================
# Line: 535

expected=[[[sum([1, 2, 3, 4, 5, 6, 7, 8, 9])]]]),

# ==================================================
# Line: 613

expected=sum([1, 2, 3, 4, 5, 6, 7, 8, 9])),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
# Occurrences: Lines 331-346 (7 instances)

condition = math_ops.equal(lengths, 1)

# ==================================================
# Line: 575

dst_size = dst_shape.dimension_size(axis)

# ==================================================
# Line: 596

dst_size = dst_shape.dimension_size(axis)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
# Line: 203

params = ragged_tensor.RaggedTensor.from_tensor(
    params, ragged_rank=1, row_splits_dtype=indices.row_splits.dtype)

# ==================================================
# Line: 228

params = ragged_tensor.RaggedTensor.from_tensor(
    params, ragged_rank=1, row_splits_dtype=indices.row_splits.dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/lookup_ops_async_checkpoint_test.py
# Occurrences: Lines 131-139 (2 instances)

table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    name="t1",
    checkpoint=True,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 158

table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    name="t1",
    checkpoint=True,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 171

checkpoint = checkpoint_utils.Checkpoint(table=table, v0=v0, v1=v1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_special_math_ops_test.py
# Line: 108

y_wt = special_math_ops.expint(x_wt)

# ==================================================
# Line: 115

special.expi(x), self.evaluate(special_math_ops.expint(x_wt))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/gradient_checker_v2.py
# Line: 175

grad = _to_numpy(grad_fn(dy_data, *xs)[0])

# ==================================================
# Line: 191

grad = _to_numpy(grad_fn(dy_data, *xs)[0])

# ==================================================
# Occurrences: Lines 248-251 (4 instances)

y_pos = _to_numpy(f(*xs))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/sparse_ops.py
# Occurrences: Lines 444-449 (2 instances)

return sparse_tensor.SparseTensor(output_ind, output_val, output_shape)

# ==================================================
# Occurrences: Lines 866-870 (2 instances)

return sparse_tensor.SparseTensor(reordered_ind, reordered_val, dense_shape)

# ==================================================
# Occurrences: Lines 3182-3187 (2 instances)

weights = validate_sparse_weights(arr, weights, dtype)

# ==================================================
# Line: 3386

weights = validate_sparse_weights(values, weights)

# ==================================================
# Line: 3394

weights = validate_sparse_weights(values, weights)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/tensor_array_ops.py
# Occurrences: Lines 174-176 (2 instances)

self._handle, self._flow = create()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/script_ops.py
# Occurrences: Lines 142-145 (2 instances)

outputs = self._call(device, args)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ctc_ops.py
# Occurrences: Lines 1368-1373 (3 instances)

state_log_prob = array_ops.expand_dims(state_log_prob, axis=1)  # Broadcast.

# ==================================================
# Occurrences: Lines 1385-1390 (3 instances)

state_log_prob = array_ops.expand_dims(state_log_prob, axis=1)  # Broadcast.

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/variable_spec_test.py
# Occurrences: Lines 228-234 (4 instances)

spec = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, False)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/gradients_test.py
# Occurrences: Lines 89-90 (2 instances)

w = constant(1.0, shape=[2, 2])

# ==================================================
# Occurrences: Lines 110-111 (2 instances)

x = constant(1.0, shape=[1, 2])

# ==================================================
# Occurrences: Lines 127-128 (2 instances)

x = constant(1.0, shape=[1, 2])

# ==================================================
# Occurrences: Lines 147-148 (2 instances)

x = constant(1.0, shape=[1, 1])

# ==================================================
# Occurrences: Lines 264-267 (2 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 433-434 (2 instances)

x = constant(1.0)

# ==================================================
# Occurrences: Lines 452-453 (2 instances)

a = constant_op.constant(1.0)

# ==================================================
# Occurrences: Lines 473-474 (2 instances)

a = constant_op.constant(1.0)

# ==================================================
# Occurrences: Lines 510-511 (2 instances)

a = constant_op.constant(1.0)

# ==================================================
# Line: 604

g = ops.Graph()

# ==================================================
# Line: 612

f.add_to_graph(ops.Graph())

# ==================================================
# Occurrences: Lines 757-758 (2 instances)

v_value = rng.randn(m, 1).astype("float32")

# ==================================================
# Occurrences: Lines 1065-1067 (2 instances)

var._variable = array_ops.identity(var, name="a")

# ==================================================
# Occurrences: Lines 1352-1353 (2 instances)

c = core_layers.dense(b, 3, use_bias=False)

# ==================================================
# Line: 1494

grads = gradients.gradients(out, [x, variables[0]], grad_ys=out_grad)

# ==================================================
# Line: 1505

grads = gradients.gradients(out, [x, variables[0]], grad_ys=out_grad)

# ==================================================
# Occurrences: Lines 1565-1573 (2 instances)

tl = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32,
    element_shape=ops.convert_to_tensor([], dtype=dtypes.int32))

# ==================================================
# Occurrences: Lines 1706-1707 (2 instances)

grads_re = self.evaluate(grads_re)

# ==================================================
# Occurrences: Lines 1713-1714 (2 instances)

grads_re = self.evaluate(grads_re)

# ==================================================
# Occurrences: Lines 1721-1722 (2 instances)

grads_re = self.evaluate(grads_re)

# ==================================================
# Occurrences: Lines 1728-1729 (2 instances)

grads_re = self.evaluate(grads_re)

# ==================================================
# Occurrences: Lines 1782-1783 (2 instances)

grads_re = self.evaluate(grads_re)

# ==================================================
# Occurrences: Lines 1789-1790 (2 instances)

grads_re = self.evaluate(grads_re)

# ==================================================
# Line: 1808

grads = gradients.gradients(y, z)

# ==================================================
# Line: 1817

grads = gradients.gradients(y, z)

# ==================================================
# Line: 1836

grads = tape.gradient(y, z)

# ==================================================
# Line: 1845

grads = tape.gradient(y, z)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/summary_ops_v2.py
# Occurrences: Lines 325-329 (4 instances)

self._resource = create_fn()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/array_ops.py
# Line: 858

input = ops.convert_to_tensor(input)

# ==================================================
# Line: 868

input = ops.convert_to_tensor(input)

# ==================================================
# Line: 5124

accum_dim_value = ones((), dtype=indices_dtype)

# ==================================================
# Line: 5131

step = ones((), dtype=indices_dtype)

# ==================================================
# Line: 6540

expanded = expand_dims(data, axis + 1)

# ==================================================
# Line: 6581

expanded = expand_dims(data, axis + 1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
# Occurrences: Lines 70-73 (4 instances)

scale_val = np.random.random_sample(scale_shape).astype(scale_dtype)

# ==================================================
# Occurrences: Lines 152-159 (4 instances)

scale_val = np.random.random_sample(scale_shape).astype(scale_dtype)

# ==================================================
# Occurrences: Lines 240-241 (2 instances)

scale_val = np.random.random_sample(scale_shape).astype(scale_dtype)

# ==================================================
# Occurrences: Lines 251-252 (2 instances)

pop_mean = np.random.random_sample(scale_shape).astype(scale_dtype)

# ==================================================
# Occurrences: Lines 307-310 (4 instances)

x_val = np.random.random_sample(x_shape).astype(x_dtype)

# ==================================================
# Occurrences: Lines 321-322 (2 instances)

pop_mean = np.random.random_sample(scale_shape).astype(scale_dtype)

# ==================================================
# Occurrences: Lines 691-694 (4 instances)

scale = np.random.random_sample((3,)).astype(np.float32)

# ==================================================
# Occurrences: Lines 715-717 (3 instances)

x = array_ops.ones((2, 2, 2, 2))

# ==================================================
# Occurrences: Lines 723-725 (3 instances)

x = array_ops.ones((2, 2, 2, 2))

# ==================================================
# Occurrences: Lines 731-735 (5 instances)

x = array_ops.ones((2, 2, 2, 2))

# ==================================================
# Occurrences: Lines 742-746 (5 instances)

x = array_ops.ones((2, 2, 2, 2))

# ==================================================
# Occurrences: Lines 754-758 (5 instances)

x = array_ops.ones((2, 2, 2, 2))

# ==================================================
# Occurrences: Lines 771-775 (5 instances)

x = array_ops.ones((2, 2, 2, 2))

# ==================================================
# Occurrences: Lines 791-794 (4 instances)

x = array_ops.ones((2, 2, 2, 2))

# ==================================================
# Occurrences: Lines 800-804 (5 instances)

y_backprop = array_ops.ones((2, 2, 2, 2))

# ==================================================
# Occurrences: Lines 811-815 (5 instances)

y_backprop = array_ops.ones((2, 2, 2, 2))

# ==================================================
# Occurrences: Lines 822-826 (5 instances)

y_backprop = array_ops.ones((2, 2, 2, 2))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/clustering_ops_test.py
# Occurrences: Lines 64-67 (2 instances)

sampled_point = clustering_ops.kmc2_chain_initialization(distances, seed)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_math_ops_test.py
# Occurrences: Lines 102-111 (3 instances)

res = math_ops.reduce_sum(x, axis=axis)

# ==================================================
# Line: 158

self.assertAllClose(self.evaluate(math_ops.reduce_std(x)), 0)

# ==================================================
# Occurrences: Lines 164-167 (2 instances)

math_ops.reduce_std(x)

# ==================================================
# Occurrences: Lines 978-980 (2 instances)

_ = math_ops.div_no_nan(x, y)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/rnn_grad_test.py
# Occurrences: Lines 67-77 (6 instances)

batch_size = np.random.randint(1, 32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/special_math_ops.py
# Occurrences: Lines 1114-1116 (2 instances)

axis_order[ax] = len(axis_order)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/confusion_matrix.py
# Occurrences: Lines 69-72 (2 instances)

predictions = array_ops.squeeze(predictions, [-1])

# ==================================================
# Line: 81

lambda: array_ops.squeeze(predictions, [-1]),

# ==================================================
# Line: 87

lambda: array_ops.squeeze(labels, [-1]),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/math_grad_test.py
# Occurrences: Lines 263-263 (2 instances)

x = constant_op.constant([1.0, -0.0], dtype=dtype)

# ==================================================
# Occurrences: Lines 270-270 (2 instances)

dx_answer = constant_op.constant([1.0, -0.0], dtype=dtype)

# ==================================================
# Occurrences: Lines 545-546 (4 instances)

x = constant_op.constant(0., dtype=dtype)

# ==================================================
# Occurrences: Lines 643-644 (4 instances)

x = constant_op.constant(0., dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/cond_v2.py
# Occurrences: Lines 418-419 (4 instances)

true_graph.outer_graph = ops.get_default_graph()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/gradient_checker.py
# Line: 114

backprop = sess.run(
    dx, feed_dict=_extra_feeds(extra_feed_dict, {x: x_data, dy: dy_data}))

# ==================================================
# Line: 122

backprop = sess.run(
    dx, feed_dict=_extra_feeds(extra_feed_dict, {x: x_data, dy: dy_data}))

# ==================================================
# Occurrences: Lines 182-183 (4 instances)

x_pos = x_data.copy()

# ==================================================
# Occurrences: Lines 233-235 (2 instances)

x_data = np.random.random_sample(x_shape).astype(t.as_numpy_dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/control_flow_ops.py
# Line: 432

v = _NextIteration(v)

# ==================================================
# Line: 448

v = _NextIteration(v)

# ==================================================
# Occurrences: Lines 897-899 (2 instances)

pre_summaries = ops.get_collection(ops.GraphKeys._SUMMARY_COLLECTION)  # pylint: disable=protected-access

# ==================================================
# Line: 908

original_result = variable_utils.convert_variables_to_tensors(
    original_result)

# ==================================================
# Line: 915

original_result = variable_utils.convert_variables_to_tensors(
    original_result)

# ==================================================
# Line: 995

self._name = ops.get_default_graph().unique_name(name)

# ==================================================
# Line: 1011

self._graph = ops.get_default_graph()

# ==================================================
# Line: 1022

g = ops.get_default_graph()

# ==================================================
# Line: 1065

self._graph = ops.get_default_graph()

# ==================================================
# Line: 1270

control_inputs, external_inputs = self._RemoveExternalControlEdges(op)

# ==================================================
# Line: 1285

_, external_inputs = self._RemoveExternalControlEdges(op)

# ==================================================
# Line: 1408

one = constant_op.constant(1, name="b_count")

# ==================================================
# Line: 1424

one = constant_op.constant(1, name="b_count")

# ==================================================
# Line: 1489

zeros_shape = array_ops.shape_internal(value, optimize=False)

# ==================================================
# Line: 1502

zeros_shape = array_ops.shape_internal(value, optimize=False)

# ==================================================
# Occurrences: Lines 1727-1729 (2 instances)

pre_summaries = ops.get_collection(ops.GraphKeys._SUMMARY_COLLECTION)  # pylint: disable=protected-access

# ==================================================
# Line: 1787

flat_orig_loop_vars = nest.flatten(loop_vars, expand_composites=True)

# ==================================================
# Line: 1794

nest.flatten(loop_vars, expand_composites=True))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/math_grad.py
# Line: 184

input_shape = array_ops.shape(op.inputs[0])

# ==================================================
# Occurrences: Lines 217-220 (2 instances)

grad = array_ops.reshape(grad, output_shape_kept_dims)

# ==================================================
# Line: 228

grad = array_ops.reshape(grad, output_shape_kept_dims)

# ==================================================
# Line: 1411

return gen_math_ops.mul(grad, math_ops.conj(y)), None

# ==================================================
# Line: 1428

gx = gen_math_ops.mul(grad, math_ops.conj(y))

# ==================================================
# Occurrences: Lines 1446-1450 (4 instances)

return gen_math_ops.mul_no_nan(grad, y), gen_math_ops.mul_no_nan(x, grad)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_fused_batch_norm_grad.py
# Occurrences: Lines 69-74 (2 instances)

scale = array_ops.reshape(scale, shape)

# ==================================================
# Line: 91

grad_offset = math_ops.reduce_sum(grad_y, axis=reduce_axis)

# ==================================================
# Occurrences: Lines 101-111 (7 instances)

pop_mean = array_ops.reshape(pop_mean, shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/tensor_array_ops_test.py
# Occurrences: Lines 34-39 (2 instances)

a = array_ops.placeholder(dtypes.string, [
    None,
])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
# Line: 125

loss = distribution.reduce("SUM", per_replica_losses, axis=None)

# ==================================================
# Line: 134

loss = distribution.reduce("SUM", per_replica_losses, axis=None)

# ==================================================
# Line: 144

loss = distribution.reduce("SUM", per_replica_losses, axis=None)

# ==================================================
# Line: 164

loss = distribution.reduce("SUM", per_replica_losses, axis=None)

# ==================================================
# Line: 173

loss = distribution.reduce("SUM", per_replica_losses, axis=None)

# ==================================================
# Occurrences: Lines 209-214 (2 instances)

nn_impl_distribute.compute_average_loss(per_example_loss)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/resource_variable_ops.py
# Occurrences: Lines 770-772 (2 instances)

new_variable = copy_to_graph_uninitialized(self)

# ==================================================
# Occurrences: Lines 841-843 (2 instances)

result = read_and_set_handle(no_copy)

# ==================================================
# Line: 2081

handle._parent_trackable = weakref.ref(self)

# ==================================================
# Line: 2118

value = gen_resource_variable_ops.read_variable_op(handle, dtype)

# ==================================================
# Line: 2141

cached_value = gen_resource_variable_ops.read_variable_op(
    handle, dtype)

# ==================================================
# Line: 2150

cached_value._cached_variable = weakref.ref(self)  # pylint: disable=protected-access

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/collective_ops_test.py
# Line: 156

start_time = time.time()

# ==================================================
# Line: 163

elapsed = time.time() - start_time

# ==================================================
# Occurrences: Lines 305-309 (2 instances)

in0 = constant_op.constant(in_val)

# ==================================================
# Occurrences: Lines 423-427 (2 instances)

in0 = array_ops.placeholder(dtype=dtypes.int32, shape=[None])

# ==================================================
# Occurrences: Lines 553-554 (4 instances)

input_tensor1 = array_ops.identity(constant)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/math_ops.py
# Occurrences: Lines 1002-1005 (2 instances)

values_cast = cast(x.values, base_type, name=name)

# ==================================================
# Occurrences: Lines 3592-3598 (4 instances)

a = ops.convert_to_tensor(a, name="a")

# ==================================================
# Occurrences: Lines 3620-3623 (2 instances)

a = conj(a)

# ==================================================
# Occurrences: Lines 3651-3654 (2 instances)

a = conj(a)

# ==================================================
# Occurrences: Lines 5319-5320 (4 instances)

if a.get_shape().is_fully_defined() and isinstance(axes, (list, tuple)):

# ==================================================
# Occurrences: Lines 5329-5329 (2 instances)

a_trans = array_ops.transpose(a, perm)

# ==================================================
# Occurrences: Lines 5338-5339 (4 instances)

if a.get_shape().ndims is not None and isinstance(axes, (list, tuple)):

# ==================================================
# Occurrences: Lines 5345-5352 (9 instances)

axes = ops.convert_to_tensor(axes, dtype=dtypes.int32, name="axes")

# ==================================================
# Occurrences: Lines 5365-5370 (3 instances)

reshaped_a = array_ops.reshape(array_ops.transpose(a, perm), new_shape)

# ==================================================
# Line: 5382

rank = array_ops.rank(a)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/lookup_ops.py
# Occurrences: Lines 550-556 (4 instances)

self._keys = ops.convert_to_tensor(keys, dtype=key_dtype, name="keys")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# Occurrences: Lines 245-246 (2 instances)

x = random_ops.random_uniform([4, 3, 2])

# ==================================================
# Occurrences: Lines 732-737 (12 instances)

scale = random_ops.random_uniform([2])

# ==================================================
# Occurrences: Lines 757-763 (12 instances)

outputs[1] = constant_op.constant(0.)

# ==================================================
# Occurrences: Lines 792-794 (2 instances)

logits = random_ops.random_uniform([3, 2, 4])

# ==================================================
# Occurrences: Lines 1126-1127 (2 instances)

handle1 = list_ops.tensor_list_reserve([], 2, dtypes.int32)

# ==================================================
# Line: 1153

external_handle = list_ops.tensor_list_reserve([], 2, dtypes.int32)

# ==================================================
# Line: 1159

h1 = list_ops.tensor_list_reserve([], 2, dtypes.int32)

# ==================================================
# Occurrences: Lines 1181-1184 (4 instances)

h1 = list_ops.tensor_list_reserve([], 2, dtypes.int32)

# ==================================================
# Occurrences: Lines 1240-1241 (4 instances)

handle = list_ops.tensor_list_push_back(handle, [1, 2])

# ==================================================
# Occurrences: Lines 1299-1300 (4 instances)

handle = list_ops.tensor_list_scatter([[1, 2]], [1], input_handle=handle)

# ==================================================
# Occurrences: Lines 1467-1469 (4 instances)

l1 = list_ops.tensor_list_reserve([], 2, dtypes.int32)

# ==================================================
# Occurrences: Lines 1476-1480 (2 instances)

l1 = list_ops.tensor_list_reserve([], 2, dtypes.int32)

# ==================================================
# Occurrences: Lines 1603-1605 (4 instances)

e2 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)

# ==================================================
# Occurrences: Lines 1619-1621 (4 instances)

e2 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)

# ==================================================
# Occurrences: Lines 1636-1638 (4 instances)

e1 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)

# ==================================================
# Line: 1644

e3 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)

# ==================================================
# Occurrences: Lines 2251-2254 (2 instances)

begin = time.time()

# ==================================================
# Occurrences: Lines 2268-2269 (2 instances)

x = random_ops.random_normal([n, params])

# ==================================================
# Occurrences: Lines 2345-2346 (2 instances)

x = random_ops.random_uniform([n, n])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
# Occurrences: Lines 45-48 (4 instances)

x = random_ops.random_uniform([3, 5])

# ==================================================
# Occurrences: Lines 233-234 (2 instances)

x = random_ops.random_uniform([3, 5])

# ==================================================
# Occurrences: Lines 260-261 (2 instances)

y = random_ops.random_uniform([3, 5])

# ==================================================
# Occurrences: Lines 270-271 (2 instances)

x = random_ops.random_uniform([4, 2, 3])

# ==================================================
# Occurrences: Lines 609-610 (2 instances)

a = random_ops.random_uniform([2, 3, 5])

# ==================================================
# Occurrences: Lines 626-627 (2 instances)

a = random_ops.random_uniform([2, 3, 5])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
# Occurrences: Lines 163-165 (2 instances)

return f()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/gradients.py
# Line: 47

output_shape = array_ops.shape(output)

# ==================================================
# Line: 57

output_size = array_ops.shape(output)[0]

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
# Occurrences: Lines 252-254 (2 instances)

y = self.max_pool2d(y)

# ==================================================
# Occurrences: Lines 584-587 (2 instances)

begin = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
# Occurrences: Lines 310-315 (2 instances)

loop_fn_output_tensors = nest.map_structure(_composite_to_tensors,
                                            loop_fn_outputs)

# ==================================================
# Occurrences: Lines 324-326 (4 instances)

loop_fn_output = ops.convert_to_tensor(loop_fn_output)

# ==================================================
# Occurrences: Lines 353-354 (2 instances)

for loop_fn_output in nest.flatten(loop_fn_output_tensors):

# ==================================================
# Occurrences: Lines 369-371 (2 instances)

flattened_output_tensors = nest.flatten(loop_fn_output_tensors)

# ==================================================
# Line: 388

nest.map_structure(_composite_to_tensors, loop_fn_outputs))

# ==================================================
# Line: 415

nest.flatten(loop_fn_output_tensors)):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Line: 807

num_outputs = len(self._outputs)

# ==================================================
# Line: 814

output_tas = while_outputs[-len(self._outputs):]

# ==================================================
# Occurrences: Lines 1666-1668 (2 instances)

has_vectorized_variant_inputs = any(
    _is_variant_with_internal_stacking(x) for x in
    y_op.inputs)

# ==================================================
# Occurrences: Lines 1688-1690 (2 instances)

has_vectorized_variant_inputs = any(
    _is_variant_with_internal_stacking(x) for x in
    y_op.inputs)

# ==================================================
# Line: 1889

inp = array_ops.reshape(inp, new_shape)

# ==================================================
# Line: 1895

inp = array_ops.reshape(inp, new_shape)

# ==================================================
# Occurrences: Lines 1920-1925 (2 instances)

output = array_ops.reshape(output, new_shape)

# ==================================================
# Line: 1950

x_shape = array_ops.shape(x)

# ==================================================
# Line: 1962

reverse_shape = array_ops.shape(x)

# ==================================================
# Occurrences: Lines 2833-2843 (3 instances)

b = array_ops.transpose(b, perm)

# ==================================================
# Line: 2851

for i in array_ops.split(array_ops.shape(b), 3)

# ==================================================
# Line: 2947

t, t_stacked, _ = pfor_input.input(0)

# ==================================================
# Line: 2953

t, _, _ = pfor_input.input(0)

# ==================================================
# Line: 2985

num_segments = math_ops.cast(num_segments, dtypes.int64)

# ==================================================
# Line: 2996

num_segments = math_ops.cast(num_segments, dtypes.int64) * math_ops.cast(

# ==================================================
# Line: 3027

_, segment_ids_stacked, _ = pfor_input.input(2)

# ==================================================
# Line: 3040

segment_ids, _, _ = pfor_input.input(2)

# ==================================================
# Occurrences: Lines 3769-3772 (2 instances)

value = data_flow_ops.tensor_array_gather_v3(
    handle, index, flow, dtype=dtype)

# ==================================================
# Occurrences: Lines 3780-3783 (2 instances)

value = data_flow_ops.tensor_array_gather_v3(
    handle, index, flow, dtype=dtype)

# ==================================================
# Line: 3806

flow_out = data_flow_ops.tensor_array_write_v3(handle, index, value, flow)

# ==================================================
# Line: 3820

flow_out = data_flow_ops.tensor_array_write_v3(handle, index, value, flow)

# ==================================================
# Line: 3869

value = _unflatten_first_dim(value, n)

# ==================================================
# Line: 3883

value = _unflatten_first_dim(value, n)

# ==================================================
# Line: 3905

flow_out = data_flow_ops.tensor_array_scatter_v3(handle, indices, value,
                                                 flow)

# ==================================================
# Line: 3918

flow_out = data_flow_ops.tensor_array_scatter_v3(handle, indices, value,
                                                 flow)

# ==================================================
# Line: 3926

flow_out = data_flow_ops.tensor_array_scatter_v3(handle, indices, value, flow)

# ==================================================
# Line: 4273

output = list_ops.tensor_list_gather(
    handle,
    index,
    element_shape=element_shape,
    element_dtype=element_dtype)

# ==================================================
# Line: 4283

values = list_ops.tensor_list_gather(
    handle, index, element_shape=element_shape, element_dtype=element_dtype)

# ==================================================
# Occurrences: Lines 4896-4896 (2 instances)

user_list_len = list_ops.tensor_list_length(inp)

# ==================================================
# Occurrences: Lines 4913-4913 (2 instances)

length = list_ops.tensor_list_length(inp)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/control_flow_assert.py
# Line: 100

xs = ops.convert_n_to_tensor(data)

# ==================================================
# Line: 110

xs = ops.convert_n_to_tensor(data)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
# Occurrences: Lines 123-128 (2 instances)

key_value_pair = expected_named_tuple.values.add()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/save_context_test.py
# Occurrences: Lines 36-37 (2 instances)

entered_context_in_thread = threading.Event()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/function_deserialization.py
# Line: 401

graph = ops.get_default_graph()

# ==================================================
# Line: 494

func.add_to_graph(ops.get_default_graph())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/save_test.py
# Line: 979

loaded_root = load.load(save_dir)

# ==================================================
# Line: 991

loaded_root = load.load(save_dir)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/metrics_test.py
# Occurrences: Lines 60-103 (20 instances)

write_count = metrics.GetWrite(write_version="2")

# ==================================================
# Line: 109

read_count = metrics.GetRead(write_version="1")

# ==================================================
# Line: 116

self.assertEqual(metrics.GetRead(write_version="1"), read_count + 1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/load.py
# Occurrences: Lines 340-341 (4 instances)

node._serialize_to_tensors = self.get(save_fn_id)  # pylint: disable=protected-access

# ==================================================
# Occurrences: Lines 348-349 (4 instances)

saveable_fn_by_name[name] = (self.get(save_fn_id),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/load_test.py
# Occurrences: Lines 157-160 (4 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Line: 198

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

# ==================================================
# Line: 204

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

# ==================================================
# Line: 257

captured_constant = constant_op.constant(2.0)

# ==================================================
# Line: 263

self.assertEqual(4.0, self.evaluate(imported.f(constant_op.constant(2.0))))

# ==================================================
# Occurrences: Lines 409-410 (2 instances)

root.asset1 = asset.Asset(vocab)

# ==================================================
# Occurrences: Lines 1211-1213 (2 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 1239-1241 (3 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Line: 1289

root = autotrackable.AutoTrackable()

# ==================================================
# Line: 1302

closure = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 1452-1453 (4 instances)

self.v = variables.Variable(1.0)

# ==================================================
# Line: 1630

vsave = variables.Variable(1)

# ==================================================
# Line: 1642

vload = variables.Variable(1)

# ==================================================
# Occurrences: Lines 1963-1965 (2 instances)

original_collections = _gather_nonempty_collections()

# ==================================================
# Line: 2458

return get_handle()

# ==================================================
# Line: 2466

handle = get_handle()

# ==================================================
# Line: 2544

rt = ragged_factory_ops.constant([[1, 2], [3]])

# ==================================================
# Line: 2550

rt = ragged_factory_ops.constant([[1, 2], [3]])

# ==================================================
# Occurrences: Lines 2568-2570 (2 instances)

root.table = lookup_ops.MutableHashTable(dtypes.string, dtypes.float32, -1)

# ==================================================
# Line: 2674

expected_grads = tape.gradient(y, v)

# ==================================================
# Line: 2691

grads = tape.gradient(y, v)

# ==================================================
# Line: 2725

expected_grads = tape.gradient(y, params)

# ==================================================
# Line: 2741

grads = tape.gradient(y, params)

# ==================================================
# Line: 2775

expected_grads = tape.gradient(y, params)

# ==================================================
# Line: 2791

grads = tape.gradient(y, params)

# ==================================================
# Line: 2950

imported = test_load(save_dir)

# ==================================================
# Line: 2961

imported = test_load(save_dir)

# ==================================================
# Occurrences: Lines 2994-2995 (2 instances)

root = module.Module()

# ==================================================
# Occurrences: Lines 3028-3029 (2 instances)

root = module.Module()

# ==================================================
# Line: 3035

loaded = module.Module()

# ==================================================
# Line: 3169

file = os.path.join(temp_dir, file_name)

# ==================================================
# Line: 3193

file_io.delete_file(os.path.join(temp_dir, file_name))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/saved_model_test.py
# Line: 391

collection_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)

# ==================================================
# Line: 401

collection_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)

# ==================================================
# Occurrences: Lines 419-424 (2 instances)

constant_5_name = constant_op.constant(5.0).name

# ==================================================
# Line: 435

b = constant_op.constant(6.0)

# ==================================================
# Line: 444

b = constant_op.constant(5.0)

# ==================================================
# Occurrences: Lines 539-543 (2 instances)

collection_foo_vars = ops.get_collection("foo_vars")

# ==================================================
# Occurrences: Lines 552-556 (2 instances)

collection_bar_vars = ops.get_collection("bar_vars")

# ==================================================
# Occurrences: Lines 623-637 (4 instances)

tensor_without_encoding = meta_graph_pb2.TensorInfo()

# ==================================================
# Occurrences: Lines 653-657 (2 instances)

builder = saved_model_builder._SavedModelBuilder(export_dir)

# ==================================================
# Occurrences: Lines 668-672 (2 instances)

builder = saved_model_builder._SavedModelBuilder(export_dir)

# ==================================================
# Occurrences: Lines 682-687 (2 instances)

builder = saved_model_builder._SavedModelBuilder(export_dir)

# ==================================================
# Line: 850

idx = str(i)

# ==================================================
# Line: 866

idx = str(i)

# ==================================================
# Occurrences: Lines 1216-1219 (2 instances)

saver_1 = training.Saver()

# ==================================================
# Line: 1252

asset_file_path = asset_list[0].eval()

# ==================================================
# Line: 1273

self.assertEqual(asset_file_path, asset_list[0].eval())

# ==================================================
# Line: 1319

with session.Session(graph=ops.Graph()) as sess:

# ==================================================
# Line: 1347

sess = session.Session(graph=ops.Graph())

# ==================================================
# Line: 1371

sess = session.Session(graph=ops.Graph())

# ==================================================
# Occurrences: Lines 1502-1504 (3 instances)

with session.Session(graph=ops.Graph()) as sess:

# ==================================================
# Occurrences: Lines 1512-1514 (3 instances)

with session.Session(graph=ops.Graph()) as sess:

# ==================================================
# Line: 1524

sess = session.Session(graph=ops.Graph())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/save.py
# Occurrences: Lines 120-124 (2 instances)

self._children_cache = object_identity.ObjectIdentityDictionary()

# ==================================================
# Occurrences: Lines 156-159 (3 instances)

super(_AugmentedGraphView, self)._breadth_first_traversal())

# ==================================================
# Line: 183

return super(_AugmentedGraphView, self)._breadth_first_traversal()

# ==================================================
# Occurrences: Lines 340-343 (6 instances)

self.node_ids[save_fn] = len(self.nodes)

# ==================================================
# Occurrences: Lines 411-415 (3 instances)

object_map = object_identity.ObjectIdentityDictionary()

# ==================================================
# Occurrences: Lines 738-738 (2 instances)

outer_fn = func_graph_map.get(outer_fn.graph.outer_graph)

# ==================================================
# Occurrences: Lines 746-746 (2 instances)

outer_fn = func_graph_map.get(outer_fn.graph.outer_graph)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/model_utils/export_utils.py
# Line: 157

excluded_signatures[signature_name] = str(e)

# ==================================================
# Line: 175

excluded_signatures[signature_name] = str(e)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/model_utils/export_test.py
# Occurrences: Lines 219-226 (3 instances)

export_dir_1 = export_utils.get_timestamped_export_dir(
    export_dir_base)

# ==================================================
# Occurrences: Lines 242-247 (2 instances)

tmp_export_dir = export_utils.get_temp_export_dir(export_dir)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
# Occurrences: Lines 133-136 (2 instances)

self.assertEqual(metrics.GetReadFingerprint(), "")

# ==================================================
# Occurrences: Lines 144-147 (2 instances)

self.assertEqual(metrics.GetWriteFingerprint(), "")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
# Line: 69

distractor = ref_variable.RefVariable(-1.0, name="distractor")

# ==================================================
# Line: 77

distractor = ref_variable.RefVariable(-1.0, name="distractor")

# ==================================================
# Line: 321

second_path = os.path.join(
    self.get_temp_dir(), "saved_model", str(ops.uid())
)

# ==================================================
# Line: 334

third_path = os.path.join(
    self.get_temp_dir(), "saved_model", str(ops.uid())
)

# ==================================================
# Occurrences: Lines 577-580 (2 instances)

root = load.load(path)

# ==================================================
# Line: 605

root = load.load(path)

# ==================================================
# Line: 614

root = load.load(path)

# ==================================================
# Occurrences: Lines 943-948 (2 instances)

path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/utils_test.py
# Line: 146

unscoped = array_ops.placeholder(dtypes.float32, 1, name="x")

# ==================================================
# Line: 153

expected = array_ops.placeholder(dtypes.float32, 1, name="x")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/loader_test.py
# Line: 145

loader = loader_impl.SavedModelLoader(SAVED_MODEL_WITH_MAIN_OP)

# ==================================================
# Line: 167

loader = loader_impl.SavedModelLoader(SAVED_MODEL_WITH_MAIN_OP)

# ==================================================
# Occurrences: Lines 198-201 (2 instances)

with ops.Graph().as_default():

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/loader_impl.py
# Line: 106

file_content = f.read()

# ==================================================
# Line: 113

file_content = f.read()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
# Line: 376

tensor_names, shapes_and_slices, tensors, _ = _get_tensors(trackables)

# ==================================================
# Occurrences: Lines 382-386 (3 instances)

_get_tensors(trackables))

# ==================================================
# Occurrences: Lines 392-393 (2 instances)

restored_tensors = io_ops.restore_v2(merged_prefix, tensor_names,
                                     shapes_and_slices, dtypes)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/registration/registration_test.py
# Occurrences: Lines 201-205 (3 instances)

x = base.Trackable()

# ==================================================
# Line: 214

x2 = base.Trackable()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/nest_test.py
# Line: 733

nest.pack_sequence_as(structure, flat), (("a", "b"), "c",

# ==================================================
# Line: 739

restructured_from_flat = nest.pack_sequence_as(structure, flat)

# ==================================================
# Occurrences: Lines 1075-1079 (2 instances)

structure3 = collections.defaultdict(list)

# ==================================================
# Occurrences: Lines 1238-1239 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Line: 1246

input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)

# ==================================================
# Line: 1256

input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)

# ==================================================
# Line: 1265

input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)

# ==================================================
# Occurrences: Lines 1275-1280 (2 instances)

input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)

# ==================================================
# Line: 1286

input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)

# ==================================================
# Occurrences: Lines 1296-1297 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1303-1304 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1311-1312 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1318-1319 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1327-1328 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1335-1336 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1347-1348 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1354-1355 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1364-1365 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1371-1372 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1395-1397 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Line: 1409

input_tree_flattened_as_shallow_tree) = get_paths_and_values(shallow_tree,
                                                             input_tree)

# ==================================================
# Line: 1430

input_tree_flattened_as_shallow_tree) = get_paths_and_values(shallow_tree,
                                                             input_tree)

# ==================================================
# Line: 1442

input_tree_flattened_as_shallow_tree) = get_paths_and_values(shallow_tree,
                                                             input_tree)

# ==================================================
# Line: 1455

input_tree_flattened_as_shallow_tree) = get_paths_and_values(shallow_tree,
                                                             input_tree)

# ==================================================
# Line: 1466

input_tree_flattened_as_shallow_tree) = get_paths_and_values(shallow_tree,
                                                             input_tree)

# ==================================================
# Line: 1478

input_tree_flattened_as_shallow_tree) = get_paths_and_values(shallow_tree,
                                                             input_tree)

# ==================================================
# Occurrences: Lines 1491-1493 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1502-1504 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Line: 1520

get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1526-1528 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1537-1539 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1550-1552 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1562-1564 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1579-1581 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1592-1594 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1606-1608 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 1619-1621 (2 instances)

flattened_input_tree) = get_paths_and_values(shallow_tree, input_tree)

# ==================================================
# Line: 1647

out = nest.map_structure_up_to(
    inp_val,
    lambda val, ops: (val + ops["add"]) * ops["mul"], inp_val, inp_ops)

# ==================================================
# Occurrences: Lines 1659-1668 (2 instances)

nest.map_structure_up_to(
    inp_val,
    lambda val, ops: (val + ops["add"]) * ops["mul"], inp_val, inp_ops)

# ==================================================
# Line: 1678

nest.map_structure_up_to(
    inp_val,
    lambda val, ops: (val + ops["add"]) * ops["mul"], inp_val, inp_ops)

# ==================================================
# Occurrences: Lines 1903-1904 (2 instances)

Foo1 = collections.namedtuple("Foo", ["a", "b"])

# ==================================================
# Occurrences: Lines 1929-1932 (2 instances)

t0 = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/traceback_utils.py
# Occurrences: Lines 111-114 (2 instances)

new_tb = types.TracebackType(new_tb, f, f.f_lasti, line_no)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/tf_stack.py
# Occurrences: Lines 49-51 (2 instances)

self._thread_key = _get_thread_key()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/protobuf/compare_test.py
# Line: 342

b = copy.deepcopy(a)

# ==================================================
# Line: 359

b = copy.deepcopy(a)

# ==================================================
# Occurrences: Lines 378-379 (2 instances)

pb1 = compare_test_pb2.Large(int64_=4)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/module_wrapper.py
# Occurrences: Lines 146-151 (2 instances)

call_location = _call_location()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/example_parser_configuration.py
# Occurrences: Lines 145-146 (2 instances)

num_ragged = len(ragged_value_types)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/tf_stack_test.py
# Occurrences: Lines 24-25 (2 instances)

frames1 = tf_stack.extract_stack()

# ==================================================
# Line: 86

trace = func(5)

# ==================================================
# Line: 93

trace = list(func(5))

# ==================================================
# Occurrences: Lines 99-101 (3 instances)

stack1 = tf_stack.extract_stack()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/nest_util.py
# Line: 193

instance_type = type(instance)

# ==================================================
# Line: 203

instance_type = type(instance)

# ==================================================
# Line: 219

"addition to self. Cause: {}".format(type(instance), instance, err)

# ==================================================
# Line: 228

instance_type = type(instance)

# ==================================================
# Line: 243

return type(instance)(sequence_like(instance.__wrapped__, args))

# ==================================================
# Line: 249

return type(instance)(args)

# ==================================================
# Line: 1295

shallow_type = type(shallow_tree)

# ==================================================
# Line: 1306

input_type=type(input_tree), shallow_type=type(shallow_tree)

# ==================================================
# Line: 1326

input_type=type(input_tree), shallow_type=type(shallow_tree)

# ==================================================
# Line: 1339

input_type=type(input_tree), shallow_type=type(shallow_tree)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/dispatch_test.py
# Occurrences: Lines 836-837 (2 instances)

checker1 = dispatch.make_type_checker(int)

# ==================================================
# Occurrences: Lines 929-932 (2 instances)

some_op = dispatch.add_type_based_api_dispatcher(some_op)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/dispatch.py
# Line: 425

_make_signature_checker(api_signature, signature)

# ==================================================
# Line: 443

checker = _make_signature_checker(api_signature, signature)

# ==================================================
# Line: 735

type_args = type_annotations.get_generic_type_args(annotation)

# ==================================================
# Line: 754

type_args = type_annotations.get_generic_type_args(annotation)

# ==================================================
# Occurrences: Lines 1107-1110 (4 instances)

y = kwargs.pop(y_name, None)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/function_utils_test.py
# Line: 214

double_wrapped_fn = functools.partial(wrapped_fn, test_arg1=123)

# ==================================================
# Line: 226

double_wrapped_fn = functools.partial(wrapped_fn, test_arg1=123)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/tf_export.py
# Occurrences: Lines 123-128 (2 instances)

api_names = getattr(undecorated_symbol, api_names_attr)

# ==================================================
# Occurrences: Lines 134-135 (2 instances)

api_names = getattr(undecorated_symbol, api_names_attr)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/deprecation_test.py
# Occurrences: Lines 1150-1154 (2 instances)

result = deprecated_module.a()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/object_identity_test.py
# Occurrences: Lines 34-35 (2 instances)

wrap1 = object_identity._ObjectIdentityWrapper(o)

# ==================================================
# Occurrences: Lines 85-86 (2 instances)

a = object()

# ==================================================
# Occurrences: Lines 93-94 (2 instances)

a = object()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/xla/pjrt_compile_virtual_device_test.py
# Line: 55

x = variables.Variable([0.0, 1.0])

# ==================================================
# Line: 64

var_a = variables.Variable([0.0, 1.0])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
# Line: 236

proto = self._create_tuple_proto(num_outputs=1)

# ==================================================
# Line: 243

proto = self._create_tuple_proto(num_outputs=1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py
# Occurrences: Lines 96-97 (2 instances)

in_tensor = array_ops.ones([4, 5, 6], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 118-119 (2 instances)

in_tensor = array_ops.ones([4, 5, 6], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 139-140 (2 instances)

in_tensor = array_ops.ones([4, 5, 6], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 167-167 (2 instances)

tensor_src = array_ops.identity(tensor)

# ==================================================
# Occurrences: Lines 173-183 (8 instances)

tensor_dest = array_ops.identity(tensor)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
# Occurrences: Lines 430-431 (2 instances)

inp1 = np.random.random_sample(shape).astype(dtype)

# ==================================================
# Line: 443

input_saved_model_dir = self.mkdtemp()

# ==================================================
# Line: 457

output_saved_model_dir = self.mkdtemp()

# ==================================================
# Line: 464

input_saved_model_dir = self.mkdtemp()

# ==================================================
# Occurrences: Lines 485-488 (2 instances)

output_saved_model_dir = self.mkdtemp()

# ==================================================
# Occurrences: Lines 495-498 (2 instances)

output_saved_model_dir = self.mkdtemp()

# ==================================================
# Line: 682

output_with_trt = converted_signature(
    inp1=ops.convert_to_tensor(np_input1),
    inp2=ops.convert_to_tensor(np_input2))

# ==================================================
# Line: 698

converted_signature(
    inp1=ops.convert_to_tensor(np_input1),
    inp2=ops.convert_to_tensor(np_input2))

# ==================================================
# Line: 747

input_saved_model_dir = self.mkdtemp()

# ==================================================
# Line: 763

output_saved_model_dir = self.mkdtemp()

# ==================================================
# Line: 779

root = load.load(output_saved_model_dir)

# ==================================================
# Line: 787

root = load.load(output_saved_model_dir)

# ==================================================
# Occurrences: Lines 798-798 (2 instances)

input_saved_model_dir = self.mkdtemp()

# ==================================================
# Occurrences: Lines 805-805 (2 instances)

output_saved_model_dir = self.mkdtemp()

# ==================================================
# Occurrences: Lines 1044-1050 (3 instances)

input_saved_model_dir = self.mkdtemp()

# ==================================================
# Line: 1062

output_saved_model_dir = self.mkdtemp()

# ==================================================
# Occurrences: Lines 1102-1103 (2 instances)

np_input1 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))

# ==================================================
# Line: 1121

input_saved_model_dir = self.mkdtemp()

# ==================================================
# Line: 1144

output_saved_model_dir = self.mkdtemp()

# ==================================================
# Line: 1168

input_saved_model_dir = self.mkdtemp()

# ==================================================
# Line: 1181

output_saved_model_dir = self.mkdtemp()

# ==================================================
# Occurrences: Lines 1203-1204 (2 instances)

np_input1 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))

# ==================================================
# Occurrences: Lines 1241-1242 (2 instances)

np_input1 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
# Occurrences: Lines 316-321 (6 instances)

sess.run(fetches=output_tensor_names, feed_dict=inputs)

# ==================================================
# Occurrences: Lines 376-381 (6 instances)

self.graph_func(*inputs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
# Occurrences: Lines 335-339 (2 instances)

optimizer = rewriter_config_with_trt.custom_optimizers.add()

# ==================================================
# Occurrences: Lines 809-809 (3 instances)

name = ops.prepend_name_scope(value, scope)

# ==================================================
# Occurrences: Lines 826-826 (3 instances)

ops.prepend_name_scope(value, scope))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/numerics_test.py
# Occurrences: Lines 52-53 (2 instances)

t = constant_op.constant(x, shape=x_shape, dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 60-61 (2 instances)

t = constant_op.constant(x, shape=x_shape, dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 80-81 (2 instances)

t1 = constant_op.constant(0.0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
# Occurrences: Lines 510-511 (2 instances)

logits = array_ops.placeholder(dtypes.float32, shape=(None, 1))

# ==================================================
# Occurrences: Lines 527-528 (2 instances)

logits = array_ops.placeholder(dtypes.float32, shape=(None, 2))

# ==================================================
# Occurrences: Lines 1148-1150 (2 instances)

predictions_placeholder = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 1204-1212 (4 instances)

labels0 = random_ops.random_uniform(
    shape, minval=0, maxval=1, dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
# Occurrences: Lines 3067-3068 (2 instances)

input_val = np.ones([2, 4, 10, 10])

# ==================================================
# Occurrences: Lines 3074-3075 (2 instances)

input_val = np.ones([2, 4, 10, 10])

# ==================================================
# Line: 3121

out_backprop_val = np.ones([32, 3, 2, 2])

# ==================================================
# Line: 3133

out_backprop_val = np.ones([32, 3, 2, 2])

# ==================================================
# Occurrences: Lines 3147-3148 (2 instances)

input_val = np.ones([2, 4, 10, 10])

# ==================================================
# Occurrences: Lines 3158-3159 (2 instances)

input_val = np.ones([2, 4, 10, 10])

# ==================================================
# Occurrences: Lines 3506-3509 (2 instances)

values_expect = self.evaluate([conv])

# ==================================================
# Occurrences: Lines 3554-3556 (4 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 3702-3726 (5 instances)

output_explicit_pad = nn_ops.conv2d(
    output_explicit_pad,
    filter,
    strides,
    padding=padding,
    data_format="NCHW")

# ==================================================
# Occurrences: Lines 3732-3743 (3 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
# Occurrences: Lines 598-601 (2 instances)

row_pooling_sequence = constant_op.constant(
    1, shape=[4], dtype=dtypes.int64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/betainc_op_test.py
# Occurrences: Lines 101-103 (3 instances)

a_p = array_ops.placeholder(dtype)

# ==================================================
# Occurrences: Lines 114-115 (2 instances)

a_s = np.abs(np.random.randn(10, 10) * 30)  # in (0, infty)

# ==================================================
# Occurrences: Lines 121-122 (2 instances)

a_s = np.abs(np.random.randn(10, 10) * 30)  # in (0, infty)

# ==================================================
# Occurrences: Lines 128-129 (2 instances)

a_s = np.abs(np.random.randn(10, 10) * 1e15)  # in (0, infty)

# ==================================================
# Occurrences: Lines 136-137 (2 instances)

a_s = np.abs(np.random.randn(10, 10) * 1e-16)  # in (0, infty)

# ==================================================
# Occurrences: Lines 144-145 (2 instances)

a_s = np.abs(np.random.randn(10, 10) * 1e-8)  # in (0, infty)

# ==================================================
# Occurrences: Lines 175-181 (4 instances)

ga_s = np.abs(np.random.randn(2, 2) * 30)  # in (0, infty)

# ==================================================
# Occurrences: Lines 189-190 (2 instances)

tf_gx_s = constant_op.constant(gx_s, dtype=dtypes.float64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
# Line: 171

values = nn_ops.nth_element(inputs, 3)

# ==================================================
# Line: 179

values = nn_ops.nth_element(inputs, 3)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_d9m_test.py
# Occurrences: Lines 87-90 (4 instances)

result_a = nn_impl.depthwise_conv2d_v2(input_data, filter_data, strides,
                                       padding, data_format)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
# Occurrences: Lines 91-92 (2 instances)

result_1 = operation()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
# Occurrences: Lines 92-94 (3 instances)

self._output_size = tensor_shape.TensorShape(self._dims)

# ==================================================
# Occurrences: Lines 176-177 (2 instances)

self._num_state_calls = variable_v1.VariableV1(0)

# ==================================================
# Line: 373

input_tensor = array_ops.ones([10, 50])

# ==================================================
# Line: 380

input_tensor = array_ops.ones([10, 50])

# ==================================================
# Occurrences: Lines 883-885 (2 instances)

outputs0, _ = rnn.static_rnn(cell, inputs, dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 927-930 (2 instances)

outputs0, _ = rnn.static_rnn(cell, inputs, dtype=dtypes.float32)

# ==================================================
# Line: 970

np.random.randn(batch_size, input_size).astype(np.float32))

# ==================================================
# Line: 1003

input_value = np.random.randn(batch_size, input_size)

# ==================================================
# Line: 1050

np.random.randn(batch_size, input_size).astype(np.float32))

# ==================================================
# Line: 1093

input_value = np.random.randn(batch_size, input_size)

# ==================================================
# Occurrences: Lines 1104-1108 (2 instances)

nest.flatten(state_static), feed_dict={

# ==================================================
# Occurrences: Lines 1120-1121 (2 instances)

state_static = nest.flatten(state_static)

# ==================================================
# Occurrences: Lines 1145-1172 (6 instances)

initializer = init_ops.random_uniform_initializer(
    -0.01, 0.01, seed=self._seed)

# ==================================================
# Line: 1188

trainable_variables = ops.get_collection(
    ops.GraphKeys.TRAINABLE_VARIABLES)

# ==================================================
# Occurrences: Lines 1217-1232 (4 instances)

concat_inputs = array_ops.placeholder(
    dtypes.float32, shape=(time_steps, batch_size, input_size))

# ==================================================
# Line: 1260

trainable_variables = ops.get_collection(
    ops.GraphKeys.TRAINABLE_VARIABLES)

# ==================================================
# Occurrences: Lines 1340-1346 (2 instances)

h_prev = constant_op.constant(
    0.592631638, shape=[28, 17], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 1386-1409 (17 instances)

x = constant_op.constant(0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 1446-1452 (6 instances)

cs_prev = random_ops.random_uniform([3, 0], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 1488-1491 (2 instances)

cell_fw = rnn_cell.LSTMCell(
    num_units, input_size, initializer=initializer, state_is_tuple=False)

# ==================================================
# Occurrences: Lines 1612-1615 (2 instances)

cell_fw = rnn_cell.LSTMCell(
    num_units, initializer=initializer, state_is_tuple=use_state_tuple)

# ==================================================
# Occurrences: Lines 1828-1830 (2 instances)

self.assertEqual(out.get_shape().as_list(), inp.get_shape().as_list())

# ==================================================
# Occurrences: Lines 2548-2558 (2 instances)

outputs, _ = rnn.dynamic_rnn(
    gpu_cell,
    inputs,
    sequence_length=sequence_length,
    dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 2643-2644 (2 instances)

x = array_ops.zeros([1, 2])

# ==================================================
# Occurrences: Lines 2671-2672 (2 instances)

x = array_ops.zeros([1, 2])

# ==================================================
# Occurrences: Lines 2692-2694 (3 instances)

x = array_ops.zeros([1, 2])

# ==================================================
# Occurrences: Lines 2706-2707 (2 instances)

m = array_ops.zeros([1, 2])

# ==================================================
# Occurrences: Lines 2829-2831 (3 instances)

x = array_ops.zeros([1, 2])

# ==================================================
# Occurrences: Lines 2862-2863 (2 instances)

m0 = array_ops.zeros([1, 4])

# ==================================================
# Occurrences: Lines 3017-3018 (2 instances)

x = array_ops.zeros([1, 3])

# ==================================================
# Occurrences: Lines 3091-3093 (3 instances)

x = array_ops.zeros([1, 2])

# ==================================================
# Occurrences: Lines 3138-3155 (8 instances)

config = wrapper.get_config()

# ==================================================
# Occurrences: Lines 3163-3168 (4 instances)

config = wrapper.get_config()

# ==================================================
# Occurrences: Lines 3176-3191 (8 instances)

config = wrapper.get_config()

# ==================================================
# Occurrences: Lines 3199-3204 (4 instances)

config = wrapper.get_config()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
# Line: 174

outputs, state = rnn.dynamic_rnn(cell, inputs, dtype=dtypes.float32)

# ==================================================
# Line: 190

outputs, state = rnn.dynamic_rnn(cell, inputs, dtype=dtypes.float32)

# ==================================================
# Line: 340

save = saver.Saver()

# ==================================================
# Line: 351

save = saver.Saver()

# ==================================================
# Occurrences: Lines 444-447 (2 instances)

start = time.time()

# ==================================================
# Line: 474

delta_static = _timer(sess, ops)

# ==================================================
# Line: 482

delta_dynamic = _timer(sess, ops)

# ==================================================
# Line: 536

delta_half_seq_len = _timer(sess, ops)

# ==================================================
# Line: 548

delta_unroll_half = _timer(sess, ops)

# ==================================================
# Line: 604

delta_concat_state = _timer(sess, ops)

# ==================================================
# Line: 616

delta_tuple_state = _timer(sess, ops)

# ==================================================
# Occurrences: Lines 662-674 (4 instances)

inputs_t = variables_lib.Variable(inputs, trainable=False).value()

# ==================================================
# Occurrences: Lines 702-702 (2 instances)

elapsed = _timer(sess, ops)

# ==================================================
# Occurrences: Lines 712-712 (2 instances)

elapsed = _timer(sess, ops)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_decoder_ops_test.py
# Line: 64

outputs = sess.run(decoded_unwrapped + [log_probability])

# ==================================================
# Line: 91

sess.run(decoded_unwrapped + [log_probability])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_conv2d_test.py
# Occurrences: Lines 123-124 (10 instances)

y1 = nn_ops.atrous_conv2d(y1, f, rate, padding=padding)

# ==================================================
# Occurrences: Lines 130-132 (15 instances)

y2 = nn_ops.conv2d(y2, f, strides=[1, 1, 1, 1], padding=padding)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_d9m_test.py
# Line: 102

bias_add_output = nn_ops.bias_add(
    input_val, bias_val, data_format=data_format)

# ==================================================
# Occurrences: Lines 109-116 (5 instances)

result_a = bias_gradients(local_seed)

# ==================================================
# Occurrences: Lines 129-130 (4 instances)

result_a = bias_gradients.eval(feed_dict=feed_dict)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# Occurrences: Lines 266-267 (2 instances)

ksize_placeholder = array_ops.placeholder(dtypes.int32, shape=[4])

# ==================================================
# Occurrences: Lines 947-953 (8 instances)

t = constant_op.constant(tensor_input, shape=input_shape)

# ==================================================
# Occurrences: Lines 967-982 (14 instances)

t = constant_op.constant(tensor_input, shape=input_shape)

# ==================================================
# Occurrences: Lines 1004-1019 (14 instances)

t = constant_op.constant(tensor_input, shape=input_shape)

# ==================================================
# Occurrences: Lines 1133-1147 (4 instances)

orig_in = constant_op.constant(orig_input, shape=[2, 3, 3, 1])

# ==================================================
# Occurrences: Lines 1161-1172 (4 instances)

orig_in = constant_op.constant(orig_input, shape=[2, 3, 3, 1])

# ==================================================
# Occurrences: Lines 2516-2520 (3 instances)

orig_in = array_ops.ones((1, 1, 1, 1))

# ==================================================
# Occurrences: Lines 2535-2536 (2 instances)

orig_out = array_ops.ones((1, 1, 1, 1))

# ==================================================
# Line: 2552

inp = array_ops.ones((1, 1, 1, 1))

# ==================================================
# Line: 2573

grad = array_ops.ones((1, 1, 1, 1))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
# Line: 164

return nn_ops.bias_add(
    input_tensor, bias_tensor, data_format=data_format)

# ==================================================
# Occurrences: Lines 172-175 (2 instances)

return bias_add(input_tensor, bias_tensor)

# ==================================================
# Line: 186

bias_add_output = bias_add(input_tensor, bias_tensor)

# ==================================================
# Line: 194

output_tensor = nn_ops.bias_add(
    input_tensor, bias_tensor, data_format=data_format)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
# Occurrences: Lines 634-638 (3 instances)

orig_in = array_ops.ones((1, 1, 1, 1, 1))

# ==================================================
# Occurrences: Lines 655-656 (2 instances)

orig_out = array_ops.ones((1, 1, 1, 1, 1))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv3d_backprop_filter_v2_grad_test.py
# Occurrences: Lines 65-69 (2 instances)

tin = constant_op.constant(
    .5053710941, shape=[2, 2, 2, 2, 1], dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
# Occurrences: Lines 287-288 (2 instances)

labels = np.zeros([0, 2, 4]).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
# Line: 644

input_backprop_not_overlapping = self.evaluate(r)

# ==================================================
# Line: 654

input_backprop_overlapping = self.evaluate(r)

# ==================================================
# Occurrences: Lines 664-673 (5 instances)

orig_input = constant_op.constant(
    .453409232, shape=[1, 7, 13, 1], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 688-702 (5 instances)

orig_input = constant_op.constant(
    0.453409232, shape=[1, 7, 13, 1], dtype=dtypes.float32
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
# Occurrences: Lines 103-108 (2 instances)

(tf_loss, tf_grad) = self.evaluate([loss, grad])

# ==================================================
# Occurrences: Lines 661-662 (2 instances)

label_lengths_spec = tensor_spec.TensorSpec([batch_size], dtypes.int64)

# ==================================================
# Line: 762

new_dense = sparse_ops.sparse_tensor_to_dense(sparse)

# ==================================================
# Line: 771

padded_dense = sparse_ops.sparse_tensor_to_dense(sparse)

# ==================================================
# Occurrences: Lines 1229-1232 (4 instances)

loss_a, gradient_a = self._forwardAndBackward(sparse_labels,
                                              logits_time_major, seed)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
# Occurrences: Lines 110-113 (6 instances)

result_a = nn_ops.softmax_cross_entropy_with_logits(
    labels=labels, logits=logits)

# ==================================================
# Occurrences: Lines 137-138 (6 instances)

labels_grad_a, logits_grad_a = gradients(seed=seed)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/lrn_op_test.py
# Occurrences: Lines 122-133 (2 instances)

input_grads = random_ops.random_uniform(
    shape=[4, 4, 4, 4],
    minval=-10000,
    maxval=10000,
    dtype=dtypes.float32,
    seed=-2033)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
# Occurrences: Lines 472-477 (3 instances)

f = np.ones([1, 1, 1, 1], np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test.py
# Occurrences: Lines 50-58 (3 instances)

np_l = np.array([[0., 0., 0., 1.],
                 [0., .5, .5, 0.]]).astype(np.float32)

# ==================================================
# Line: 64

tf_loss, tf_gradient = gen_nn_ops.softmax_cross_entropy_with_logits(
    tf_f, tf_l)

# ==================================================
# Occurrences: Lines 92-93 (4 instances)

labels = array_ops.zeros([0, 2, 4], dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test_big.py
# Line: 87

col_sum = np.ones([size_y], dtype=np.float32) * size_x

# ==================================================
# Line: 109

sum_xz = np.ones([size_y], dtype=np.float32)

# ==================================================
# Line: 137

row_max = np.max(arr, axis=1)

# ==================================================
# Line: 143

tf_row_max = self._tf_reduce_max(arr_placeholder, 1, False)

# ==================================================
# Line: 158

sum_y = np.max(arr, axis=1)

# ==================================================
# Line: 165

tf_sum_y = self._tf_reduce_max(arr_placeholder, 1, False)

# ==================================================
# Line: 185

col_sum = np.ones([size_y], dtype=np.bool_)

# ==================================================
# Line: 192

tf_row_sum = self._tf_reduce_all(arr_placeholder, 1, False)

# ==================================================
# Line: 207

sum_xz = np.ones([size_y], dtype=np.bool_)

# ==================================================
# Line: 213

tf_sum_y = self._tf_reduce_all(arr_placeholder, 1, False)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/argmax_op_test.py
# Line: 40

tf_ans = self.evaluate(ans)

# ==================================================
# Line: 47

self.evaluate(ans)

# ==================================================
# Line: 108

tf_ans = self.evaluate(ans)

# ==================================================
# Line: 116

tf_ans = self.evaluate(ans)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
# Occurrences: Lines 76-78 (2 instances)

grad_rtol = _default_tolerance(x.dtype)

# ==================================================
# Occurrences: Lines 622-623 (6 instances)

x = constant_op.constant(rand(dtype, real_range))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
# Occurrences: Lines 55-56 (2 instances)

labels = np.arange(5, dtype=dtype)

# ==================================================
# Occurrences: Lines 78-80 (3 instances)

m_neg = array_ops.placeholder(dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 168-170 (3 instances)

labels = np.arange(5, dtype=np.int32)

# ==================================================
# Occurrences: Lines 224-225 (2 instances)

labels = np.arange(2)

# ==================================================
# Occurrences: Lines 233-234 (2 instances)

labels = np.arange(2)

# ==================================================
# Occurrences: Lines 252-253 (2 instances)

labels_placeholder = array_ops.placeholder(dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 278-279 (2 instances)

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 304-305 (2 instances)

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 330-331 (2 instances)

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 357-358 (2 instances)

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 384-385 (2 instances)

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 413-414 (2 instances)

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 439-440 (2 instances)

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 458-459 (2 instances)

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Occurrences: Lines 493-494 (2 instances)

gradients_indices = np.zeros((9, 3), dtype=np.float32)

# ==================================================
# Occurrences: Lines 563-566 (6 instances)

data = np.zeros((2, 0), dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
# Occurrences: Lines 130-131 (2 instances)

xt = x.astype(t)

# ==================================================
# Occurrences: Lines 141-143 (2 instances)

xt = x.astype(t)

# ==================================================
# Occurrences: Lines 260-261 (2 instances)

x = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 1286-1287 (2 instances)

x = np.random.rand(2, 2).astype(dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
# Occurrences: Lines 121-126 (4 instances)

res = math_ops.matmul(a, b, **kwargs_)

# ==================================================
# Occurrences: Lines 264-271 (20 instances)

a_np = np.random.normal(-5, 5, m * k).astype(dtype).reshape([m, k])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/tensordot_op_test.py
# Occurrences: Lines 56-57 (2 instances)

a_ph = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 82-83 (2 instances)

a_ph = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 115-134 (24 instances)

a = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 180-181 (6 instances)

a = array_ops.placeholder(dtype_)

# ==================================================
# Occurrences: Lines 209-212 (4 instances)

a_np = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape)).reshape(shape).astype(dtype_)

# ==================================================
# Occurrences: Lines 220-221 (6 instances)

a = array_ops.placeholder(dtype_)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
# Line: 380

self._set_intersection(sp_a, sp_b)

# ==================================================
# Line: 425

intersection = self._set_intersection(sp_a, sp_b)

# ==================================================
# Occurrences: Lines 498-511 (9 instances)

static_indices_shape = op.indices.get_shape()

# ==================================================
# Line: 524

for i in range(1, len(ops)):

# ==================================================
# Occurrences: Lines 870-872 (2 instances)

self._set_difference(sp_a, sp_b, False)

# ==================================================
# Line: 913

difference = self._set_difference(sp_a, sp_b, True)

# ==================================================
# Line: 966

difference = self._set_difference(sp_a, sp_b, False)

# ==================================================
# Line: 1166

self._set_union(sp_a, sp_b)

# ==================================================
# Line: 1220

intersection = self._set_union(sp_a, sp_b)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
# Occurrences: Lines 36-38 (2 instances)

vals = np.array(np.random.normal(loc, scale, np.prod(shape)), dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
# Occurrences: Lines 39-48 (8 instances)

inx = ops.convert_to_tensor(x)

# ==================================================
# Occurrences: Lines 134-137 (2 instances)

x = (1 + np.linspace(0, 5, np.prod([1, 3, 2]))).astype(np.float32).reshape(
    [1, 3, 2])

# ==================================================
# Occurrences: Lines 175-178 (2 instances)

x1 = (1 + np.linspace(0, 5, np.prod([1, 3, 2]))).astype(np.float32).reshape(
    [1, 3, 2])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
# Occurrences: Lines 128-130 (2 instances)

out = 1.1 * tf_func(inx, iny)

# ==================================================
# Occurrences: Lines 158-160 (2 instances)

out = 1.1 * tf_func(inx, iny)

# ==================================================
# Occurrences: Lines 215-216 (2 instances)

x1 = np.random.randn(5, 6).astype(np.float32)

# ==================================================
# Occurrences: Lines 270-272 (2 instances)

x = np.linspace(-20, 20, 10).reshape(1, 2, 5).astype(bfloat16)  # pylint: disable=too-many-function-args

# ==================================================
# Occurrences: Lines 292-293 (2 instances)

x1 = np.random.randn(7, 4).astype(np.float64)

# ==================================================
# Occurrences: Lines 856-856 (2 instances)

x = np.array([5, 2]).astype(dtype)

# ==================================================
# Occurrences: Lines 864-864 (2 instances)

x = np.array([5, 2]).astype(dtype)

# ==================================================
# Occurrences: Lines 872-872 (2 instances)

x = np.array([5, 2]).astype(dtype)

# ==================================================
# Occurrences: Lines 955-956 (2 instances)

xt = x.astype(t)

# ==================================================
# Occurrences: Lines 965-967 (2 instances)

xt = x.astype(t)

# ==================================================
# Occurrences: Lines 1057-1075 (12 instances)

x = np.asarray([0, 1, 2, 3, 4])

# ==================================================
# Occurrences: Lines 1089-1090 (2 instances)

x = np.asarray([0, 1, 2, 3, 4])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# Occurrences: Lines 257-261 (4 instances)

ans = clip_ops.clip_by_norm(x, clip_norm)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Occurrences: Lines 283-284 (4 instances)

size_x = int(2**np.random.uniform(0, 15))

# ==================================================
# Occurrences: Lines 291-294 (2 instances)

row_sum = np.sum(arr, axis=1)

# ==================================================
# Occurrences: Lines 304-309 (2 instances)

sum_y = np.sum(arr, axis=1)

# ==================================================
# Occurrences: Lines 323-324 (6 instances)

size_x = int(2 ** np.random.uniform(0, 7))

# ==================================================
# Occurrences: Lines 331-333 (4 instances)

row_sum = np.sum(arr, axis=1)

# ==================================================
# Occurrences: Lines 343-347 (4 instances)

sum_y = np.sum(arr, axis=1)

# ==================================================
# Occurrences: Lines 390-398 (3 instances)

c_unknown = array_ops.placeholder(dtypes.float32)

# ==================================================
# Line: 404

np_input = np.random.randn(3, 3, 3)

# ==================================================
# Occurrences: Lines 452-457 (2 instances)

data = np.random.randint(1024, size=shape)

# ==================================================
# Occurrences: Lines 769-781 (4 instances)

x1 = x.copy()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
# Occurrences: Lines 59-64 (2 instances)

jacob_t, jacob_n = gradient_checker_v2.compute_gradient(
    lambda x: array_ops.transpose(x, p, conjugate=conjugate), [inx])

# ==================================================
# Occurrences: Lines 89-94 (2 instances)

jacob_t, jacob_n = gradient_checker_v2.compute_gradient(
    lambda x: array_ops.transpose(x, p, conjugate=conjugate), [inx])

# ==================================================
# Occurrences: Lines 188-195 (6 instances)

total_size = np.prod(input_shape)

# ==================================================
# Occurrences: Lines 225-232 (6 instances)

total_size = np.prod(input_shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/reduce_benchmark_test.py
# Occurrences: Lines 39-42 (2 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
# Line: 497

values_queue = data_flow_ops.FIFOQueue(
    4, dtypes=dtypes_lib.float32, shapes=(1, 2))

# ==================================================
# Line: 506

weights_queue = data_flow_ops.FIFOQueue(
    4, dtypes=dtypes_lib.float32, shapes=(1, 2))

# ==================================================
# Line: 525

values_queue = data_flow_ops.FIFOQueue(
    4, dtypes=dtypes_lib.float32, shapes=(1, 2))

# ==================================================
# Line: 534

weights_queue = data_flow_ops.FIFOQueue(
    4, dtypes=dtypes_lib.float32, shapes=(1, 2))

# ==================================================
# Occurrences: Lines 591-592 (2 instances)

predictions = array_ops.ones((10, 3))

# ==================================================
# Occurrences: Lines 599-602 (2 instances)

predictions = random_ops.random_uniform(
    (10, 3), maxval=3, dtype=dtypes_lib.int64, seed=1)

# ==================================================
# Occurrences: Lines 613-615 (2 instances)

initial_accuracy = self.evaluate(accuracy)

# ==================================================
# Line: 621

preds_queue = data_flow_ops.FIFOQueue(
    4, dtypes=dtypes_lib.float32, shapes=(1, 1))

# ==================================================
# Line: 630

labels_queue = data_flow_ops.FIFOQueue(
    4, dtypes=dtypes_lib.float32, shapes=(1, 1))

# ==================================================
# Line: 712

preds_queue = data_flow_ops.FIFOQueue(
    4, dtypes=dtypes_lib.float32, shapes=(1, 1))

# ==================================================
# Line: 721

labels_queue = data_flow_ops.FIFOQueue(
    4, dtypes=dtypes_lib.float32, shapes=(1, 1))

# ==================================================
# Occurrences: Lines 780-783 (2 instances)

predictions = random_ops.random_uniform(
    (10, 3), maxval=1, dtype=dtypes_lib.int64, seed=1)

# ==================================================
# Occurrences: Lines 794-796 (2 instances)

initial_precision = self.evaluate(precision)

# ==================================================
# Occurrences: Lines 802-803 (2 instances)

predictions = constant_op.constant(inputs)

# ==================================================
# Occurrences: Lines 842-843 (2 instances)

predictions = array_ops.placeholder(dtype=dtypes_lib.float32)

# ==================================================
# Occurrences: Lines 862-863 (2 instances)

predictions = array_ops.placeholder(dtype=dtypes_lib.float32)

# ==================================================
# Occurrences: Lines 900-901 (2 instances)

predictions = array_ops.placeholder(dtype=dtypes_lib.float32)

# ==================================================
# Occurrences: Lines 936-937 (2 instances)

predictions = constant_op.constant([0, 0, 0, 0])

# ==================================================
# Occurrences: Lines 980-983 (2 instances)

predictions = random_ops.random_uniform(
    (10, 3), maxval=1, dtype=dtypes_lib.int64, seed=1)

# ==================================================
# Occurrences: Lines 994-996 (2 instances)

initial_recall = self.evaluate(recall)

# ==================================================
# Occurrences: Lines 1002-1003 (2 instances)

predictions = constant_op.constant(np_inputs)

# ==================================================
# Occurrences: Lines 1070-1071 (2 instances)

predictions = array_ops.zeros((1, 4))

# ==================================================
# Occurrences: Lines 1126-1128 (2 instances)

initial_auc = self.evaluate(auc)

# ==================================================
# Occurrences: Lines 1487-1489 (2 instances)

initial_specificity = self.evaluate(specificity)

# ==================================================
# Occurrences: Lines 1634-1636 (2 instances)

initial_sensitivity = self.evaluate(sensitivity)

# ==================================================
# Line: 1946

num_batches = int(num_samples / batch_size)

# ==================================================
# Occurrences: Lines 1984-1987 (2 instances)

predictions_queue = data_flow_ops.FIFOQueue(
    num_batches, dtypes=dtypes_lib.float32, shapes=(batch_size,))

# ==================================================
# Line: 2006

for _ in range(int(num_samples / batch_size)):

# ==================================================
# Occurrences: Lines 3001-3003 (2 instances)

initial_error = self.evaluate(error)

# ==================================================
# Occurrences: Lines 3071-3073 (2 instances)

initial_error = self.evaluate(error)

# ==================================================
# Occurrences: Lines 3156-3163 (4 instances)

initial_error = self.evaluate(error)

# ==================================================
# Line: 3205

preds_queue = data_flow_ops.FIFOQueue(
    2, dtypes=dtypes_lib.float32, shapes=(1, 3))

# ==================================================
# Line: 3212

labels_queue = data_flow_ops.FIFOQueue(
    2, dtypes=dtypes_lib.float32, shapes=(1, 3))

# ==================================================
# Line: 3230

preds_queue0 = data_flow_ops.FIFOQueue(
    2, dtypes=dtypes_lib.float32, shapes=(1, 3))

# ==================================================
# Line: 3237

preds_queue1 = data_flow_ops.FIFOQueue(
    2, dtypes=dtypes_lib.float32, shapes=(1, 3))

# ==================================================
# Line: 3244

labels_queue0 = data_flow_ops.FIFOQueue(
    2, dtypes=dtypes_lib.float32, shapes=(1, 3))

# ==================================================
# Line: 3251

labels_queue1 = data_flow_ops.FIFOQueue(
    2, dtypes=dtypes_lib.float32, shapes=(1, 3))

# ==================================================
# Line: 3274

preds_queue = data_flow_ops.FIFOQueue(
    2, dtypes=dtypes_lib.float32, shapes=(1, 3))

# ==================================================
# Line: 3281

labels_queue = data_flow_ops.FIFOQueue(
    2, dtypes=dtypes_lib.float32, shapes=(1, 3))

# ==================================================
# Occurrences: Lines 3343-3352 (4 instances)

initial_error = self.evaluate(error)

# ==================================================
# Occurrences: Lines 3448-3450 (2 instances)

initial_error = self.evaluate(error)

# ==================================================
# Occurrences: Lines 3456-3459 (2 instances)

predictions = constant_op.constant(
    np_labels, shape=(1, 3, 3), dtype=dtypes_lib.float32)

# ==================================================
# Occurrences: Lines 3665-3666 (2 instances)

predictions = array_ops.ones([10])

# ==================================================
# Occurrences: Lines 3674-3677 (2 instances)

predictions = random_ops.random_uniform(
    [10], maxval=num_classes, dtype=dtypes_lib.int64, seed=1)

# ==================================================
# Occurrences: Lines 3689-3691 (2 instances)

initial_mean_iou = self.evaluate(mean_iou)

# ==================================================
# Line: 3698

preds_queue = data_flow_ops.FIFOQueue(
    5, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Line: 3708

labels_queue = data_flow_ops.FIFOQueue(
    5, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Line: 3730

preds_queue = data_flow_ops.FIFOQueue(
    6, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Line: 3741

labels_queue = data_flow_ops.FIFOQueue(
    6, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Line: 3780

preds_queue = data_flow_ops.FIFOQueue(
    5, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Line: 3791

labels_queue = data_flow_ops.FIFOQueue(
    5, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Occurrences: Lines 3835-3836 (2 instances)

predictions = array_ops.zeros([40])

# ==================================================
# Occurrences: Lines 3911-3912 (2 instances)

labels = constant_op.constant([0])

# ==================================================
# Occurrences: Lines 3986-3987 (2 instances)

predictions = array_ops.ones([10])

# ==================================================
# Occurrences: Lines 3996-3999 (2 instances)

predictions = random_ops.random_uniform(
    [10], maxval=num_classes, dtype=dtypes_lib.int64, seed=1)

# ==================================================
# Occurrences: Lines 4011-4019 (3 instances)

initial_mean_accuracy = self.evaluate(mean_accuracy)

# ==================================================
# Line: 4028

labels_queue = data_flow_ops.FIFOQueue(
    5, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Line: 4044

self.assertAlmostEqual(desired_output, self.evaluate(mean_accuracy))

# ==================================================
# Line: 4051

preds_queue = data_flow_ops.FIFOQueue(
    6, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Line: 4062

labels_queue = data_flow_ops.FIFOQueue(
    6, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Line: 4101

preds_queue = data_flow_ops.FIFOQueue(
    5, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Line: 4112

labels_queue = data_flow_ops.FIFOQueue(
    5, dtypes=dtypes_lib.int32, shapes=(1, 1))

# ==================================================
# Occurrences: Lines 4132-4133 (2 instances)

predictions = array_ops.zeros([40])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
# Occurrences: Lines 523-528 (3 instances)

pb1 = summary_pb2.Summary()

# ==================================================
# Line: 540

expected_pb = summary_pb2.Summary()

# ==================================================
# Occurrences: Lines 669-674 (3 instances)

ops_without_writer = define_ops()

# ==================================================
# Occurrences: Lines 863-873 (4 instances)

writer1 = summary_ops.create_file_writer_v2(logdir)

# ==================================================
# Line: 900

f1.writer = summary_ops.create_file_writer_v2(logdir)

# ==================================================
# Occurrences: Lines 906-916 (3 instances)

f2.writer = summary_ops.create_file_writer_v2(logdir)

# ==================================================
# Line: 1075

pre_save_files = set(events_from_multifile_logdir(logdir))

# ==================================================
# Occurrences: Lines 1083-1090 (4 instances)

restored = saved_model_load.load(export_dir)

# ==================================================
# Line: 1126

pre_save_files = set(events_from_multifile_logdir(logdir))

# ==================================================
# Occurrences: Lines 1154-1158 (2 instances)

post_restore_files = set(events_from_multifile_logdir(logdir))

# ==================================================
# Occurrences: Lines 1496-1498 (2 instances)

logdir = self.get_temp_dir()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
# Occurrences: Lines 136-140 (2 instances)

a = constant_op.constant(10)

# ==================================================
# Occurrences: Lines 149-151 (2 instances)

a = constant_op.constant(10)

# ==================================================
# Occurrences: Lines 204-205 (2 instances)

one_handle = self.evaluate(session_ops.get_session_handle(one))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/array_ops_test.py
# Line: 33

axis_known_t = array_ops.placeholder(dtypes.int32, shape=[3])

# ==================================================
# Line: 43

axis_2d_t = array_ops.placeholder(dtypes.int32, shape=[3])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
# Occurrences: Lines 408-409 (4 instances)

re = np.random.uniform(size=n)

# ==================================================
# Occurrences: Lines 428-429 (4 instances)

re = np.random.uniform(size=n)

# ==================================================
# Occurrences: Lines 820-828 (7 instances)

n = np.prod(shape)

# ==================================================
# Occurrences: Lines 911-912 (2 instances)

re = np.ones(shape=(size,) * dims, dtype=np_rtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
# Occurrences: Lines 169-176 (4 instances)

expected = np.reshape(
    expected_inner_frames, (1,) * rank + expected_inner_frames.shape)

# ==================================================
# Occurrences: Lines 196-197 (2 instances)

expected = np.reshape(
    expected_inner_frames, (1,) * rank + expected_inner_frames.shape)

# ==================================================
# Occurrences: Lines 203-204 (2 instances)

expected = np.reshape(
    expected_inner_frames, (1,) * rank + expected_inner_frames.shape)

# ==================================================
# Occurrences: Lines 279-294 (4 instances)

result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=True, pad_value=99)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
# Occurrences: Lines 299-300 (2 instances)

larry = constant_op.constant([])

# ==================================================
# Occurrences: Lines 361-362 (2 instances)

larry = constant_op.constant([])

# ==================================================
# Occurrences: Lines 483-484 (2 instances)

larry = constant_op.constant([])

# ==================================================
# Occurrences: Lines 514-515 (2 instances)

t1 = constant_op.constant([1., 2.])

# ==================================================
# Occurrences: Lines 587-588 (2 instances)

larry = constant_op.constant([])

# ==================================================
# Occurrences: Lines 664-665 (2 instances)

larry = constant_op.constant([])

# ==================================================
# Occurrences: Lines 736-737 (2 instances)

larry = constant_op.constant([])

# ==================================================
# Occurrences: Lines 808-809 (2 instances)

larry = constant_op.constant([])

# ==================================================
# Occurrences: Lines 1037-1039 (4 instances)

start = time.time()

# ==================================================
# Line: 1751

out = array_ops.identity(x)

# ==================================================
# Line: 1762

out = array_ops.identity(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/benchmark_test.py
# Occurrences: Lines 165-169 (2 instances)

expected_1 = test_log_pb2.BenchmarkEntry()

# ==================================================
# Line: 175

expected_3 = test_log_pb2.BenchmarkEntry()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
# Line: 67

value = np.array(value, dtype=np.uint64)

# ==================================================
# Line: 87

return np.array(value, dtype=np.uint64)

# ==================================================
# Occurrences: Lines 256-259 (2 instances)

result_cpu = stateless_op(seed=seed)

# ==================================================
# Occurrences: Lines 267-269 (2 instances)

old = stateless_op(seed=seed)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
# Occurrences: Lines 77-86 (8 instances)

sx = self._Sampler(1000, counts=10., probs=0.4, dtype=dt, seed=345)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
# Occurrences: Lines 330-332 (2 instances)

stddev = variables.Variable(1.)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
# Occurrences: Lines 58-60 (3 instances)

y = self.evaluate(x)

# ==================================================
# Occurrences: Lines 89-90 (4 instances)

x = sampler()

# ==================================================
# Occurrences: Lines 119-120 (4 instances)

sx = self._Sampler(1000, 0.0, 1.0, dt, use_gpu=True, seed=345)

# ==================================================
# Occurrences: Lines 128-129 (4 instances)

rnd1 = random_ops.random_normal(shape, 0.0, 1.0, dtypes.float32)

# ==================================================
# Occurrences: Lines 191-192 (4 instances)

x = sampler()

# ==================================================
# Occurrences: Lines 227-228 (4 instances)

sx = self._Sampler(1000, 0.0, 1.0, dt, use_gpu=True, seed=345)

# ==================================================
# Occurrences: Lines 265-266 (2 instances)

rnd1 = random_ops.truncated_normal(shape, 0.0, 1.0, dtypes.float32)

# ==================================================
# Occurrences: Lines 273-278 (3 instances)

random_ops.random_normal([])

# ==================================================
# Occurrences: Lines 314-315 (4 instances)

x = sampler()

# ==================================================
# Occurrences: Lines 389-390 (6 instances)

sx = self._Sampler(1000, 0, 17, dtype=dt, use_gpu=True, seed=seed)

# ==================================================
# Occurrences: Lines 398-399 (4 instances)

rnd1 = random_ops.random_uniform(shape, 0, 17, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
# Occurrences: Lines 372-385 (4 instances)

float_val, int_val = self.evaluate(dequeued_t)

# ==================================================
# Line: 406

float_val, int_val = self.evaluate(dequeued_t)

# ==================================================
# Occurrences: Lines 412-420 (3 instances)

float_val, int_val = self.evaluate(dequeued_t)

# ==================================================
# Occurrences: Lines 1243-1249 (2 instances)

q_empty = data_flow_ops.RandomShuffleQueue(5, 0, dtypes_lib.float32, (
    (),))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/random_crop_test.py
# Occurrences: Lines 128-130 (2 instances)

counts = np.zeros(size, dtype=np.int32)

# ==================================================
# Occurrences: Lines 147-151 (2 instances)

counts = np.zeros(size, dtype=np.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
# Occurrences: Lines 71-72 (2 instances)

sample1a = self.evaluate(sample_op1)

# ==================================================
# Occurrences: Lines 149-150 (2 instances)

sample_op1 = random_ops.multinomial(logits, num_samples, seed)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
# Occurrences: Lines 98-99 (2 instances)

alpha = array_ops.placeholder(dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
# Occurrences: Lines 91-92 (4 instances)

sx = self._Sampler(1000, 1.0, dt, use_gpu=True, seed=345)

# ==================================================
# Occurrences: Lines 104-105 (4 instances)

rnd1 = random_ops.random_poisson(2.0, [24], dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
# Occurrences: Lines 140-141 (4 instances)

x = sampler()

# ==================================================
# Occurrences: Lines 163-164 (4 instances)

sx = self._Sampler(1000, 0.0, 1.0, dt, seed=345)

# ==================================================
# Occurrences: Lines 176-177 (4 instances)

rnd1 = random_ops.random_gamma([24], 2.0, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
# Occurrences: Lines 111-115 (4 instances)

keys1 = gen._make_int64_keys(shape=shape)

# ==================================================
# Line: 125

return gen.make_seeds(count=count)

# ==================================================
# Occurrences: Lines 179-183 (4 instances)

expected_normal = gen.normal(shape)

# ==================================================
# Occurrences: Lines 204-207 (6 instances)

gen = constructor()

# ==================================================
# Occurrences: Lines 215-215 (2 instances)

g_seeded = constructor()

# ==================================================
# Line: 307

g_copy = random.Generator(g)

# ==================================================
# Line: 319

g_seeded = random.Generator(g)

# ==================================================
# Occurrences: Lines 365-367 (2 instances)

a = random.get_global_generator().normal(shape)

# ==================================================
# Occurrences: Lines 373-378 (3 instances)

return random.get_global_generator().normal(shape)

# ==================================================
# Occurrences: Lines 529-533 (2 instances)

cpu = random.Generator.from_seed(seed).uniform_full_int(
    shape=shape, dtype=dtype)

# ==================================================
# Occurrences: Lines 681-689 (4 instances)

generator = random.get_global_generator()

# ==================================================
# Occurrences: Lines 701-705 (2 instances)

samples = f()

# ==================================================
# Occurrences: Lines 715-716 (2 instances)

g1 = random.Generator.from_seed(1)

# ==================================================
# Occurrences: Lines 728-730 (2 instances)

g = random.Generator.from_seed(1)

# ==================================================
# Occurrences: Lines 743-745 (4 instances)

r1 = g.uniform([], dtype=dtypes.uint32, minval=None)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Occurrences: Lines 104-106 (2 instances)

initial_test_loss = self.evaluate(test_loss)

# ==================================================
# Occurrences: Lines 143-145 (2 instances)

initial_test_loss = test_loss()

# ==================================================
# Occurrences: Lines 183-190 (4 instances)

store = variable_scope._VariableStore()

# ==================================================
# Occurrences: Lines 201-214 (6 instances)

second_store = variable_scope._VariableStore()

# ==================================================
# Occurrences: Lines 237-241 (4 instances)

tmpl1 = template.make_template("s1", variable_scoped_function)

# ==================================================
# Occurrences: Lines 250-254 (2 instances)

tmpl1 = template.make_template(
    "_", variable_scoped_function, unique_name_="s1")

# ==================================================
# Occurrences: Lines 269-276 (4 instances)

tmpl1 = template.make_template(
    "_", variable_scoped_function, unique_name_="s1")

# ==================================================
# Occurrences: Lines 285-294 (4 instances)

tmpl1 = template.make_template("s1", variable_scoped_function)

# ==================================================
# Occurrences: Lines 302-306 (4 instances)

tmpl1 = template.make_template("s1", internally_variable_scoped_function)

# ==================================================
# Occurrences: Lines 324-330 (4 instances)

tmpl1 = template.make_template(
    "s1", internally_variable_scoped_function, scope_name="test")

# ==================================================
# Occurrences: Lines 378-382 (4 instances)

tmpl1 = template.make_template("s1", nested)

# ==================================================
# Occurrences: Lines 393-394 (4 instances)

nested1 = template.make_template("nested", variable_scoped_function)

# ==================================================
# Occurrences: Lines 415-419 (4 instances)

tmpl1 = template.make_template("s1", nested_template)

# ==================================================
# Occurrences: Lines 471-474 (4 instances)

inner_imm_var = tmpl_immed()

# ==================================================
# Occurrences: Lines 490-491 (2 instances)

ta = template.make_template("bar", variable_scoped_function, True)

# ==================================================
# Occurrences: Lines 586-588 (3 instances)

linear1 = make_linear_module(output_size=2, name="foo")

# ==================================================
# Occurrences: Lines 601-603 (3 instances)

linear2 = make_linear_module(output_size=2, name="foo")

# ==================================================
# Occurrences: Lines 647-648 (2 instances)

ta = template.make_template("bar", variable_scoped_function, True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/norm_op_test.py
# Occurrences: Lines 70-76 (4 instances)

tf_norm = linalg_ops.norm(
    tf_matrix, ord=ord_, axis=axis_, keepdims=keep_dims_)

# ==================================================
# Occurrences: Lines 90-92 (4 instances)

matrix = np.random.randn(*shape_).astype(dtype_)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
# Occurrences: Lines 79-81 (2 instances)

s1, u1, v1 = self.evaluate(linalg_ops.svd(matrix))

# ==================================================
# Occurrences: Lines 107-120 (18 instances)

matrix1 = stateless_random_ops.stateless_random_normal(shape, seed)

# ==================================================
# Occurrences: Lines 193-198 (4 instances)

x_np = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape_)).reshape(shape_).astype(dtype_)

# ==================================================
# Occurrences: Lines 206-207 (2 instances)

s_tf, u_tf, v_tf = linalg_ops.svd(
    x_tf, compute_uv=compute_uv_, full_matrices=full_matrices_)

# ==================================================
# Occurrences: Lines 215-216 (2 instances)

s_tf = linalg_ops.svd(
    x_tf, compute_uv=compute_uv_, full_matrices=full_matrices_)

# ==================================================
# Occurrences: Lines 224-228 (4 instances)

u_np, s_np, v_np = np.linalg.svd(
    x_np, compute_uv=compute_uv_, full_matrices=full_matrices_)

# ==================================================
# Occurrences: Lines 235-237 (4 instances)

CompareSingularVectors(self, u_np, u_tf_val, min(shape_[-2:]), tol)

# ==================================================
# Occurrences: Lines 279-282 (6 instances)

a = np.random.uniform(low=-1.0, high=1.0, size=shape_).astype(dtype_)

# ==================================================
# Occurrences: Lines 321-324 (4 instances)

a = np.random.uniform(low=-1.0, high=1.0, size=shape_).astype(dtype_)

# ==================================================
# Occurrences: Lines 343-346 (4 instances)

x_init = np.random.uniform(low=-1.0, high=1.0, size=shape_).astype(dtype_)

# ==================================================
# Occurrences: Lines 387-390 (6 instances)

matrix_value = np.random.uniform(
    low=-1.0, high=1.0, size=shape_).astype(np.float32)

# ==================================================
# Occurrences: Lines 402-405 (6 instances)

matrix_value = np.random.uniform(
    low=-1.0, high=1.0, size=shape_).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
# Occurrences: Lines 59-60 (8 instances)

a_ph = array_ops.placeholder(dtypes.as_dtype(np_type))

# ==================================================
# Occurrences: Lines 72-75 (2 instances)

matrix = (np.random.normal(-5, 5,
                           m * n).astype(np.complex128).reshape([m, n]))

# ==================================================
# Occurrences: Lines 131-138 (8 instances)

lhs1 = stateless_random_ops.stateless_random_normal(
    matrix_shape, seed=seed)

# ==================================================
# Occurrences: Lines 186-187 (8 instances)

matrix, rhs = self._GenerateTestData(matrix_shape, num_rhs)

# ==================================================
# Occurrences: Lines 204-205 (8 instances)

matrix, rhs = self._GenerateTestData(matrix_shape, num_rhs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_grad_test.py
# Occurrences: Lines 113-114 (4 instances)

a_mats_val = sparsify(np.random.randn(*dense_shape))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
# Line: 181

csr = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
    indices=indices, values=values, dense_shape=dense_shape
)

# ==================================================
# Line: 191

csr = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
    indices=indices, values=values, dense_shape=dense_shape
)

# ==================================================
# Occurrences: Lines 201-207 (2 instances)

indices = constant_op.constant(0, shape=[5, 3], dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 214-220 (2 instances)

indices = constant_op.constant(0, shape=[5, 3], dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 255-260 (3 instances)

self.evaluate(a_rt)

# ==================================================
# Occurrences: Lines 529-530 (2 instances)

a_mats = sparsify(np.random.randn(*dense_shape)).astype(np.float32)

# ==================================================
# Occurrences: Lines 1024-1025 (2 instances)

softmax = sparsify(np.random.randn(*dense_shape))

# ==================================================
# Occurrences: Lines 1049-1050 (2 instances)

softmax = sparsify(np.random.randn(*dense_shape))

# ==================================================
# Occurrences: Lines 1542-1545 (8 instances)

x_mats = sparsify(
    random_ops.random_uniform(dense_shape, dtype=dtypes.float32))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
# Occurrences: Lines 151-152 (2 instances)

_, p = linalg_ops.lu(data)

# ==================================================
# Occurrences: Lines 162-163 (2 instances)

_, p = linalg_ops.lu(data)

# ==================================================
# Occurrences: Lines 196-202 (3 instances)

matrices = np.random.rand(batch_size, 5, 5)

# ==================================================
# Occurrences: Lines 209-214 (3 instances)

data = np.random.rand(n, n)

# ==================================================
# Occurrences: Lines 227-230 (2 instances)

matrix1 = stateless_random_ops.stateless_random_normal(
    shape=matrix_shape, seed=seed)

# ==================================================
# Occurrences: Lines 270-271 (4 instances)

matrix = variables.Variable(self._GenerateMatrix(shape))

# ==================================================
# Occurrences: Lines 283-284 (4 instances)

matrix = variables.Variable(self._GenerateMatrix(shape))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
# Occurrences: Lines 44-46 (4 instances)

arr = np.array(r.randn(*shape)).astype(dtype)

# ==================================================
# Occurrences: Lines 163-165 (6 instances)

arr = np.array(r.randn(*shape)).astype(dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
# Occurrences: Lines 65-68 (8 instances)

matrix1 = stateless_random_ops.stateless_random_normal(
    matrix_shape, seed)

# ==================================================
# Occurrences: Lines 128-133 (4 instances)

x_np = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape_)).reshape(shape_).astype(dtype_)

# ==================================================
# Occurrences: Lines 191-194 (4 instances)

a = np.random.uniform(low=-1.0, high=1.0, size=shape_).astype(dtype_)

# ==================================================
# Occurrences: Lines 250-253 (6 instances)

matrix_value = np.random.uniform(
    low=-1.0, high=1.0, size=shape_).astype(np.float32)

# ==================================================
# Occurrences: Lines 265-268 (6 instances)

matrix_value = np.random.uniform(
    low=-1.0, high=1.0, size=shape_).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
# Occurrences: Lines 86-92 (2 instances)

u = linear_operator_test_util.random_normal_correlated_columns(
    u_perturbation_shape, dtype=dtype)

# ==================================================
# Occurrences: Lines 333-342 (4 instances)

num_rows_ph = array_ops.placeholder(dtypes.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
# Occurrences: Lines 56-57 (4 instances)

matrix1 = random_ops.random_normal([5, 5], seed=42)

# ==================================================
# Occurrences: Lines 143-147 (4 instances)

a = np.random.uniform(
    low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)

# ==================================================
# Occurrences: Lines 190-194 (6 instances)

a = np.random.uniform(
    low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_tridiag_test.py
# Line: 43

subdiag = linear_operator_test_util.random_sign_uniform(
    shape[:-1], minval=1., maxval=2., dtype=dtype)

# ==================================================
# Occurrences: Lines 53-57 (2 instances)

superdiag = linear_operator_test_util.random_sign_uniform(
    shape[:-1], minval=1., maxval=2., dtype=dtype)

# ==================================================
# Line: 69

diagonals = array_ops_stack.stack([superdiag, diag, subdiag], axis=-2)

# ==================================================
# Line: 168

operator = linalg_lib.LinearOperatorTridiag(
    diagonals, diagonals_format='sequence')

# ==================================================
# Line: 179

operator = linalg_lib.LinearOperatorTridiag(
    diagonals, diagonals_format='sequence')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
# Occurrences: Lines 399-400 (2 instances)

operator_1 = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py
# Occurrences: Lines 58-59 (4 instances)

matrix1 = random_ops.random_normal([5, 5], seed=42)

# ==================================================
# Occurrences: Lines 162-166 (6 instances)

a = np.random.uniform(
    low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)

# ==================================================
# Occurrences: Lines 214-218 (6 instances)

a = np.random.uniform(
    low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
# Occurrences: Lines 158-159 (2 instances)

matrix1 = random_ops.random_normal([5, 5], seed=42)

# ==================================================
# Occurrences: Lines 196-197 (4 instances)

matrix = self._GenerateMatrix(shape)

# ==================================================
# Occurrences: Lines 209-210 (4 instances)

matrix = self._GenerateMatrix(shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
# Occurrences: Lines 38-40 (2 instances)

temp = rng.randn(n, n).astype(dtype)

# ==================================================
# Occurrences: Lines 621-623 (4 instances)

beta = np.random.uniform(size=(n - 1,)).astype(dtype)

# ==================================================
# Occurrences: Lines 676-678 (2 instances)

beta = np.random.uniform(size=(n - 1,)).astype(dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
# Occurrences: Lines 216-220 (2 instances)

matrix = array_ops.placeholder_with_default(input=(), shape=None)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
# Occurrences: Lines 113-116 (2 instances)

matrix1 = stateless_random_ops.stateless_random_normal(
    shape=matrix_shape, seed=seed)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_permutation_test.py
# Line: 63

perm = math_ops.range(0, shape[-1])

# ==================================================
# Line: 75

math_ops.range(0, shape[-1]),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
# Occurrences: Lines 131-136 (2 instances)

matrix1 = math_ops.cast(
    stateless_random_ops.stateless_random_normal(matrix_shape, seed=seed),
    dtypes.complex64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/normalize_op_test.py
# Occurrences: Lines 39-42 (2 instances)

norm = np.expand_dims(norm, d)

# ==================================================
# Occurrences: Lines 69-71 (4 instances)

matrix = np.random.randn(*shape_).astype(dtype_)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
# Occurrences: Lines 135-136 (2 instances)

matrix1 = np.random.randn(4, 4)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
# Line: 153

rhs = np.random.uniform(size=[10, 1])

# ==================================================
# Line: 160

rhs = np.random.uniform(size=[10, 1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py
# Occurrences: Lines 68-72 (2 instances)

return np.linalg.solve(gramian, rhs)

# ==================================================
# Occurrences: Lines 113-114 (2 instances)

a_ph = array_ops.placeholder(dtypes.as_dtype(dtype))

# ==================================================
# Line: 188

rhs = np.array([[1., 0., 1.], [0., 1., 1.]])

# ==================================================
# Line: 216

rhs = np.array([[1., 0., 1.], [0., 1., 1.]])

# ==================================================
# Occurrences: Lines 236-239 (2 instances)

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)

# ==================================================
# Occurrences: Lines 253-256 (2 instances)

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)

# ==================================================
# Occurrences: Lines 270-273 (2 instances)

matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)

# ==================================================
# Occurrences: Lines 333-334 (6 instances)

matrix, rhs = _GenerateTestData(matrix_shape, num_rhs)

# ==================================================
# Occurrences: Lines 348-349 (6 instances)

matrix, rhs = _GenerateTestData(matrix_shape, num_rhs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
# Occurrences: Lines 153-154 (4 instances)

matrix1 = random_ops.random_normal([5, 5], seed=42)

# ==================================================
# Occurrences: Lines 194-195 (6 instances)

matrix = self._GenerateMatrix(shape)

# ==================================================
# Occurrences: Lines 208-209 (6 instances)

matrix = self._GenerateMatrix(shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
# Occurrences: Lines 162-163 (2 instances)

operator_1 = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
# Occurrences: Lines 161-162 (2 instances)

matrix1 = random_ops.random_normal([5, 5], seed=42)

# ==================================================
# Occurrences: Lines 238-239 (4 instances)

matrix = self._GenerateMatrix(shape)

# ==================================================
# Occurrences: Lines 251-252 (4 instances)

matrix = self._GenerateMatrix(shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
# Occurrences: Lines 176-178 (3 instances)

diag1 = linalg.LinearOperatorDiag([1.])

# ==================================================
# Occurrences: Lines 190-191 (2 instances)

diag1 = linalg.LinearOperatorDiag([1.])

# ==================================================
# Occurrences: Lines 205-206 (2 instances)

diag1 = linalg.LinearOperatorDiag([1.])

# ==================================================
# Occurrences: Lines 247-248 (2 instances)

diag1 = linalg.LinearOperatorDiag([1.])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
# Occurrences: Lines 108-109 (2 instances)

operator_1 = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)

# ==================================================
# Occurrences: Lines 124-125 (2 instances)

x = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)

# ==================================================
# Occurrences: Lines 267-268 (2 instances)

mat_ph_1 = array_ops.placeholder(dtypes.float64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
# Occurrences: Lines 489-490 (2 instances)

rhs_placeholder = placeholder(rank=3)

# ==================================================
# Occurrences: Lines 635-638 (4 instances)

superdiag = array_ops.placeholder(dtypes.float64, shape=[None])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_toeplitz_test.py
# Occurrences: Lines 83-84 (2 instances)

row = np.random.uniform(low=1., high=5., size=shape[:-1])

# ==================================================
# Occurrences: Lines 139-140 (2 instances)

col = variables_module.Variable([1.])

# ==================================================
# Occurrences: Lines 158-159 (2 instances)

col = variables_module.Variable([1.])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
# Occurrences: Lines 149-151 (2 instances)

superdiag = self._randomComplexArray((b, m - 1))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
# Line: 129

matrices = np.random.rand(10, 5, 5)

# ==================================================
# Occurrences: Lines 136-136 (2 instances)

matrices = np.random.rand(10, 5, 5) + 1j * np.random.rand(10, 5, 5)

# ==================================================
# Occurrences: Lines 182-183 (2 instances)

matrix1 = stateless_random_ops.stateless_random_normal(matrix_shape, seed)

# ==================================================
# Occurrences: Lines 260-263 (4 instances)

a = np.random.randn(shape[0], shape[1]).astype(dtype.as_numpy_dtype)

# ==================================================
# Occurrences: Lines 326-327 (4 instances)

matrix = variables.Variable(self._GenerateMatrix(shape))

# ==================================================
# Occurrences: Lines 340-341 (4 instances)

matrix = variables.Variable(self._GenerateMatrix(shape))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
# Occurrences: Lines 232-234 (3 instances)

operator_1 = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
# Occurrences: Lines 49-50 (2 instances)

x = ops.convert_to_tensor([1., 2, 0])

# ==================================================
# Occurrences: Lines 83-84 (2 instances)

x = ops.convert_to_tensor([1., 2, 0])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/as_string_op_test.py
# Occurrences: Lines 106-110 (2 instances)

result = string_ops.as_string(inputs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
# Occurrences: Lines 201-204 (2 instances)

_input_array(num_dims=5).reshape([2] * i + [1] + [2] * (5 - i))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
# Line: 42

values = self.evaluate(outputs)

# ==================================================
# Line: 52

values = self.evaluate(outputs)

# ==================================================
# Line: 62

values = self.evaluate(outputs)

# ==================================================
# Line: 90

values = self.evaluate(outputs)

# ==================================================
# Line: 100

values = self.evaluate(outputs)

# ==================================================
# Line: 196

values = self.evaluate(outputs)

# ==================================================
# Line: 202

values = self.evaluate(outputs)

# ==================================================
# Occurrences: Lines 267-272 (2 instances)

values = self.evaluate(outputs)

# ==================================================
# Occurrences: Lines 281-294 (5 instances)

values = self.evaluate(outputs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/base64_ops_test.py
# Occurrences: Lines 82-87 (4 instances)

for _ in range(np.random.randint(10))]

# ==================================================
# Occurrences: Lines 105-111 (3 instances)

enc = base64.urlsafe_b64encode(msg)

# ==================================================
# Occurrences: Lines 123-124 (2 instances)

msg = np.random.bytes(34)

# ==================================================
# Occurrences: Lines 130-131 (2 instances)

msg = np.random.bytes(33)

# ==================================================
# Occurrences: Lines 141-142 (2 instances)

msg = np.random.bytes(33)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
# Occurrences: Lines 67-71 (3 instances)

position = np.array(0, dtype)

# ==================================================
# Occurrences: Lines 79-83 (4 instances)

position = np.array(0, dtype)

# ==================================================
# Occurrences: Lines 92-95 (3 instances)

length = np.array(5, dtype)

# ==================================================
# Occurrences: Lines 108-111 (3 instances)

length = np.array(5, dtype)

# ==================================================
# Occurrences: Lines 171-173 (2 instances)

substr_op = string_ops.substr(test_string, position, length, unit=unit)

# ==================================================
# Occurrences: Lines 186-188 (2 instances)

substr_op = string_ops.substr(test_string, position, length, unit=unit)

# ==================================================
# Occurrences: Lines 269-271 (2 instances)

substr_op = string_ops.substr(test_string, position, length, unit=unit)

# ==================================================
# Occurrences: Lines 292-294 (2 instances)

substr_op = string_ops.substr(test_string, position, length, unit=unit)

# ==================================================
# Occurrences: Lines 308-310 (2 instances)

substr_op = string_ops.substr(test_string, position, length, unit=unit)

# ==================================================
# Occurrences: Lines 398-399 (2 instances)

length = np.array([[3, 2, 1], [1, 2, 3], [2, 2, 2]], dtype)

# ==================================================
# Occurrences: Lines 406-407 (2 instances)

length = np.array([[3, 2, 1], [1, 2, 3], [2, 2, 2]], dtype)

# ==================================================
# Occurrences: Lines 429-430 (2 instances)

length = np.array([1, 2, 3], dtype)

# ==================================================
# Occurrences: Lines 437-438 (2 instances)

length = np.array([1, 2, 3], dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
# Occurrences: Lines 34-43 (4 instances)

tensor = math_ops.range(10)

# ==================================================
# Occurrences: Lines 104-127 (8 instances)

tensor = math_ops.range(6)

# ==================================================
# Line: 360

tensor = math_ops.range(10)

# ==================================================
# Line: 367

tensor = math_ops.range(10)

# ==================================================
# Line: 374

tensor = math_ops.range(10)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
# Occurrences: Lines 84-86 (2 instances)

test_value = np.array([ord('H'), ord('e'), 0x7FFFFFFF, -1, ord('o')],
                      np.int32)

# ==================================================
# Line: 92

test_value = np.array([ord('H'), ord('e'), 0x7FFFFFFF, -1, ord('o')],
                      np.int32)

# ==================================================
# Occurrences: Lines 100-102 (2 instances)

test_value = np.array([ord('H'), ord('e'), 0x7FFFFFFF, -1, ord('o')],
                      np.int32)

# ==================================================
# Occurrences: Lines 108-122 (5 instances)

expected_value = u"A".encode(encoding)

# ==================================================
# Occurrences: Lines 136-141 (2 instances)

unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)

# ==================================================
# Occurrences: Lines 147-152 (2 instances)

unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
# Line: 100

indices, values, shape = self.evaluate(tokens)

# ==================================================
# Line: 106

indices, values, shape = self.evaluate(tokens)

# ==================================================
# Line: 155

indices, values, shape = self.evaluate(tokens)

# ==================================================
# Line: 164

indices, values, shape = self.evaluate(tokens)

# ==================================================
# Occurrences: Lines 217-221 (2 instances)

ragged_string_ops.string_split(source, sep, skip_empty, delimiter,
                               result_type)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/unsorted_segment_join_op_test.py
# Line: 78

res = self.evaluate(
    string_ops.unsorted_segment_join(
        inputs=inputs,
        segment_ids=segment_ids,
        num_segments=num_segments,
        separator=separator))

# ==================================================
# Line: 89

res = self.evaluate(
    string_ops.unsorted_segment_join(
        inputs=inputs,
        segment_ids=segment_ids,
        num_segments=num_segments,
        separator=separator))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_number_op_test.py
# Line: 37

result, = output.eval(feed_dict={input_string: [instr]})

# ==================================================
# Line: 43

output.eval(feed_dict={input_string: [instr]})

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
# Occurrences: Lines 93-98 (2 instances)

out = parsing_ops.parse_single_example(**kwargs)

# ==================================================
# Occurrences: Lines 892-899 (4 instances)

out = parsing_ops.parse_single_example(**kwargs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
# Occurrences: Lines 30-31 (2 instances)

decode = parsing_ops.decode_csv(**args)

# ==================================================
# Occurrences: Lines 40-41 (2 instances)

decode = parsing_ops.decode_csv(**args)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
# Line: 149

remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=row_remapping,
    col_remapping=col_remapping,
    initializing_values=[],
    num_rows=len(row_remapping),
    num_cols=len(col_remapping))

# ==================================================
# Line: 164

remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=row_remapping,
    col_remapping=col_remapping,
    initializing_values=[],
    num_rows=len(row_remapping),
    num_cols=len(col_remapping))

# ==================================================
# Occurrences: Lines 231-238 (2 instances)

ckpt_path = constant_op.constant(
    '/tmp/warm_starting_util_test5kl2a3pc/tmpph76tep2/model-0',
    shape=[],
    dtype=dtypes.string)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
# Occurrences: Lines 87-93 (3 instances)

self.evaluate(parsing_ops.parse_example(**kwargs))

# ==================================================
# Occurrences: Lines 1200-1202 (2 instances)

self.evaluate(parsing_ops.parse_single_example(**kwargs))

# ==================================================
# Occurrences: Lines 1470-1479 (4 instances)

self.evaluate(parsing_ops.parse_sequence_example(**kwargs))

# ==================================================
# Line: 1544

new_values[k] = np.expand_dims(v, axis=0)

# ==================================================
# Occurrences: Lines 1559-1562 (4 instances)

new_values[k] = np.expand_dims(v, axis=0)

# ==================================================
# Occurrences: Lines 2431-2435 (2 instances)

output_example = example_pb2.Example()

# ==================================================
# Occurrences: Lines 2495-2497 (2 instances)

parsing_ops.decode_json_example(json_tensor)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
# Line: 370

k, v = self.evaluate([key, value])

# ==================================================
# Line: 376

k, v = self.evaluate([key, value])

# ==================================================
# Line: 397

k, v = self.evaluate([key, value])

# ==================================================
# Line: 403

k, v = self.evaluate([key, value])

# ==================================================
# Line: 533

k, v = self.evaluate([key, value])

# ==================================================
# Line: 539

k, v = self.evaluate([key, value])

# ==================================================
# Line: 559

k, v = self.evaluate([key, value])

# ==================================================
# Line: 565

k, v = self.evaluate([key, value])

# ==================================================
# Line: 631

k, v = self.evaluate([key, value])

# ==================================================
# Line: 637

k, v = self.evaluate([key, value])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
# Occurrences: Lines 55-63 (3 instances)

a = constant_op.constant([0, 1, 2], dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 69-79 (4 instances)

slice_val = self.evaluate(slice_t)

# ==================================================
# Line: 86

slice_val = self.evaluate(slice_t)

# ==================================================
# Occurrences: Lines 96-99 (2 instances)

slice_val = self.evaluate(slice_t)

# ==================================================
# Occurrences: Lines 105-112 (3 instances)

slice_val = self.evaluate(slice_t)

# ==================================================
# Occurrences: Lines 274-275 (2 instances)

x = np.random.randint(0, 9)

# ==================================================
# Line: 477

a = constant_op.constant([[1, 2, 3], [4, 5, 6]])

# ==================================================
# Line: 485

a = constant_op.constant([[1, 2, 3], [4, 5, 6]])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
# Occurrences: Lines 82-83 (2 instances)

t1 = init(shape).eval()

# ==================================================
# Occurrences: Lines 257-258 (4 instances)

init1 = init_ops.random_normal_initializer(0.0, 1.0, seed=1, dtype=dtype)

# ==================================================
# Occurrences: Lines 287-290 (4 instances)

init1 = init_ops.truncated_normal_initializer(
    0.0, 1.0, seed=1, dtype=dtype)

# ==================================================
# Occurrences: Lines 321-322 (4 instances)

init1 = init_ops.random_uniform_initializer(0, 7, seed=1, dtype=dtype)

# ==================================================
# Occurrences: Lines 343-349 (8 instances)

init1 = init_ops.uniform_unit_scaling_initializer(seed=1, dtype=dtype)

# ==================================================
# Occurrences: Lines 643-644 (2 instances)

start_t = array_ops.placeholder(dtypes.float32, shape=graph_shape)

# ==================================================
# Occurrences: Lines 784-785 (4 instances)

init1 = init_ops.orthogonal_initializer(seed=1, dtype=dtype)

# ==================================================
# Occurrences: Lines 845-846 (4 instances)

init1 = init_ops.convolutional_delta_orthogonal(seed=1, dtype=dtype)

# ==================================================
# Occurrences: Lines 918-919 (4 instances)

init1 = init_ops.convolutional_orthogonal_1d(seed=1, dtype=dtype)

# ==================================================
# Occurrences: Lines 987-988 (4 instances)

init1 = init_ops.convolutional_orthogonal_2d(seed=1, dtype=dtype)

# ==================================================
# Occurrences: Lines 1032-1033 (4 instances)

init1 = init_ops.convolutional_orthogonal_3d(seed=1, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
# Occurrences: Lines 317-324 (4 instances)

axis = array_ops.placeholder(dtypes.int32)

# ==================================================
# Line: 519

result = array_ops.gather(params, indices, axis=axis, batch_dims=batch_dims)

# ==================================================
# Line: 525

return array_ops.gather(params, indices, axis=axis, batch_dims=batch_dims)

# ==================================================
# Occurrences: Lines 536-539 (2 instances)

return array_ops.gather(params, indices, axis=axis, batch_dims=batch_dims)

# ==================================================
# Line: 545

gradient_checker_v2.compute_gradient(
    lambda p: gather_unknown_shapes(p, indices), [f64_params])

# ==================================================
# Line: 562

result = array_ops.gather(
    params, indices, axis=axis, batch_dims=batch_dims)

# ==================================================
# Line: 657

result = array_ops.gather(params, indices, axis=axis, batch_dims=batch_dims)

# ==================================================
# Line: 664

result = array_ops.gather(
    params, indices, axis=axis, batch_dims=batch_dims)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
# Occurrences: Lines 77-96 (10 instances)

indices_empty = np.empty((0, 2), dtype=np.int32)

# ==================================================
# Occurrences: Lines 320-323 (2 instances)

inputs = constant_op.constant([[1, 2], [3, 4]], dtype=dtypes.float64)

# ==================================================
# Occurrences: Lines 453-456 (2 instances)

t1 = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
# Line: 220

b, ih, iw, ic = tensor.shape.as_list()

# ==================================================
# Line: 229

b, ic, ih, iw = tensor.shape.as_list()

# ==================================================
# Occurrences: Lines 271-280 (4 instances)

actual = array_ops.bitcast(t, dtypes.int8)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
# Occurrences: Lines 40-41 (2 instances)

p1 = array_ops.placeholder(dtypes.float32, shape=[4, 4])

# ==================================================
# Occurrences: Lines 56-57 (2 instances)

p1 = array_ops.placeholder(dtypes.float32, shape=[4, 4])

# ==================================================
# Occurrences: Lines 87-88 (2 instances)

p1 = np.random.rand(2, 3).astype("i")

# ==================================================
# Occurrences: Lines 98-99 (2 instances)

p1 = np.random.rand(2, 3).astype(dtypes.bfloat16.as_numpy_dtype)

# ==================================================
# Occurrences: Lines 109-110 (2 instances)

p1 = np.random.rand(2, 3).astype(dtypes.float8_e5m2.as_numpy_dtype)

# ==================================================
# Occurrences: Lines 120-121 (2 instances)

p1 = np.random.rand(2, 3).astype(dtypes.float8_e4m3fn.as_numpy_dtype)

# ==================================================
# Occurrences: Lines 131-132 (2 instances)

p1 = np.random.rand(4, 4).astype("f")

# ==================================================
# Occurrences: Lines 360-361 (2 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 411-413 (2 instances)

p1 = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 533-535 (3 instances)

x_1 = array_ops.placeholder(dtypes.float64)

# ==================================================
# Occurrences: Lines 551-552 (2 instances)

c1 = np.random.rand(4, 4)

# ==================================================
# Line: 637

output = self.evaluate(c)

# ==================================================
# Line: 643

output = self.evaluate(c)

# ==================================================
# Occurrences: Lines 683-684 (2 instances)

x1_placeholder = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 782-794 (6 instances)

s0 = constant_op.constant([2, 3, 5], dtypes.int32)

# ==================================================
# Occurrences: Lines 809-810 (2 instances)

s3_1 = array_ops.slice(s2, [0, 4, 4, 0], [-1, 8178, 4082, 1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/inplace_ops_test.py
# Occurrences: Lines 77-77 (2 instances)

x = array_ops.ones([7, 3], dtype)

# ==================================================
# Occurrences: Lines 89-89 (2 instances)

x = inplace_ops.inplace_add(x, None, array_ops.ones([7, 3], dtype) * 99)

# ==================================================
# Occurrences: Lines 96-96 (2 instances)

x = array_ops.ones([7, 3], dtype)

# ==================================================
# Occurrences: Lines 108-108 (2 instances)

x = inplace_ops.inplace_sub(x, None, array_ops.ones([7, 3], dtype) * 99)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
# Occurrences: Lines 342-352 (4 instances)

padded = array_ops.pad(inp, array_ops.placeholder(dtypes.int32))

# ==================================================
# Occurrences: Lines 358-371 (4 instances)

unknown = array_ops.placeholder(dtypes.int32)

# ==================================================
# Line: 380

rank_known = array_ops.placeholder(dtypes.int32)

# ==================================================
# Line: 386

inp = constant_op.constant(0.0, shape=[4, 4])

# ==================================================
# Line: 392

inp = constant_op.constant(0.0, shape=[4, 4])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/weights_broadcast_test.py
# Occurrences: Lines 40-41 (2 instances)

weights_placeholder = array_ops.placeholder(dtypes_lib.float32)

# ==================================================
# Occurrences: Lines 104-105 (2 instances)

weights_placeholder = array_ops.placeholder(dtypes_lib.float32)

# ==================================================
# Occurrences: Lines 168-169 (2 instances)

weights_placeholder = array_ops.placeholder(dtypes_lib.float32)

# ==================================================
# Occurrences: Lines 246-247 (2 instances)

weights_placeholder = array_ops.placeholder(dtypes_lib.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/reverse_sequence_op_test.py
# Line: 45

tf_ans = self.evaluate(ans)

# ==================================================
# Line: 53

self.evaluate(ans)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
# Line: 67

tf_ans = constant_op.constant(orig)

# ==================================================
# Occurrences: Lines 73-78 (2 instances)

tf_ans = constant_op.constant(orig)

# ==================================================
# Line: 84

tf_ans = constant_op.constant(orig)

# ==================================================
# Occurrences: Lines 371-375 (2 instances)

self.assertAllEqual(z.numpy(), np.zeros([2, 3]))

# ==================================================
# Occurrences: Lines 388-388 (2 instances)

z_value = z.numpy()

# ==================================================
# Occurrences: Lines 394-394 (2 instances)

z_value = z.numpy()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
# Occurrences: Lines 108-111 (2 instances)

b = math_ops.cast(math_ops.cast(a, dtypes.bfloat16), dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
# Occurrences: Lines 550-555 (2 instances)

x = constant_op.constant(np.random.rand(*shape), np.float32)

# ==================================================
# Occurrences: Lines 564-570 (2 instances)

x = constant_op.constant(np.random.rand(*shape), np.float32)

# ==================================================
# Occurrences: Lines 602-612 (4 instances)

v = np.array([3.0, 4.0])

# ==================================================
# Line: 701

v = array_ops.placeholder(dtype=dtypes_lib.float32)

# ==================================================
# Line: 707

d = array_ops.placeholder(dtype=dtypes_lib.float32)

# ==================================================
# Occurrences: Lines 751-753 (3 instances)

v = array_ops.placeholder(dtype=dtypes_lib.float32)

# ==================================================
# Occurrences: Lines 799-802 (2 instances)

mat_diag = array_ops.matrix_diag_part(mat)

# ==================================================
# Line: 903

error = gradient_checker.compute_gradient_error(x,
                                                x.get_shape().as_list(),
                                                y,
                                                y.get_shape().as_list())

# ==================================================
# Line: 918

error = gradient_checker.compute_gradient_error(
    x,
    x.get_shape().as_list(), y,
    y.get_shape().as_list())

# ==================================================
# Occurrences: Lines 1124-1126 (3 instances)

i = np.arange(2)[:, None, None]

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/matrix_band_part_op_test.py
# Occurrences: Lines 114-115 (6 instances)

matrix = variables.Variable(array_ops.ones(shape_))

# ==================================================
# Occurrences: Lines 128-129 (6 instances)

matrix = variables.Variable(array_ops.ones(shape_))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
# Occurrences: Lines 42-50 (4 instances)

x_tf = array_ops.depth_to_space(input_nhwc, block_size)

# ==================================================
# Occurrences: Lines 59-65 (4 instances)

x_tf = array_ops.depth_to_space(input_nhwc, block_size)

# ==================================================
# Line: 125

x_tf = array_ops.depth_to_space(input_nhwc, block_size)

# ==================================================
# Line: 131

x_tf = array_ops.depth_to_space(input_nhwc, block_size)

# ==================================================
# Line: 266

b, ih, iw, ic = tensor.shape.as_list()

# ==================================================
# Line: 274

b, ic, ih, iw = tensor.shape.as_list()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
# Occurrences: Lines 41-45 (2 instances)

tf_ans = self.evaluate(ans)

# ==================================================
# Occurrences: Lines 249-250 (2 instances)

x = np.random.randn(3, 4)

# ==================================================
# Occurrences: Lines 301-302 (4 instances)

x_gen = random_ops.random_uniform([m, n], dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
# Occurrences: Lines 48-49 (2 instances)

num_block_dims = len(block_shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
# Occurrences: Lines 308-309 (2 instances)

indices = array_ops.zeros([2, 2, 2], dtypes.int32)

# ==================================================
# Line: 479

ref = variables.Variable(array_ops.zeros([1]))

# ==================================================
# Line: 485

ref2 = variables.Variable(array_ops.zeros([1]))

# ==================================================
# Occurrences: Lines 504-506 (3 instances)

expected = np.array([False, False, False, True, False, False, False, True])

# ==================================================
# Occurrences: Lines 512-514 (3 instances)

expected = np.array([False, False, False, True, False, False, False, True])

# ==================================================
# Occurrences: Lines 533-548 (6 instances)

scatter = self.scatter_nd(indices, updates, shape=(8,))

# ==================================================
# Occurrences: Lines 554-556 (2 instances)

scatter = self.scatter_nd(indices, updates, shape=(8,))

# ==================================================
# Occurrences: Lines 562-563 (2 instances)

indices = array_ops.zeros([2, 2, 2], dtypes.int32)

# ==================================================
# Occurrences: Lines 596-603 (4 instances)

indices = array_ops.placeholder(dtypes.int32, shape=[2, 2, 2])

# ==================================================
# Occurrences: Lines 613-614 (2 instances)

indices = array_ops.placeholder(dtypes.int32, shape=None)

# ==================================================
# Occurrences: Lines 627-628 (2 instances)

indices = array_ops.zeros([0], dtypes.int32)

# ==================================================
# Occurrences: Lines 681-681 (2 instances)

updates = constant_op.constant([[3, 4], [1, 2]], dtype=dtype)

# ==================================================
# Occurrences: Lines 688-688 (2 instances)

grad_vals = constant_op.constant([[3, 4], [1, 2]], dtype=dtype)

# ==================================================
# Occurrences: Lines 820-822 (2 instances)

val = self.evaluate(self.scatter_nd(indices, values, shape))

# ==================================================
# Occurrences: Lines 1012-1014 (2 instances)

val = self.evaluate(array_ops.tensor_scatter_update(a, indices, values))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/huge_slice_op_test.py
# Line: 32

slice_val = self.evaluate(slice_t)

# ==================================================
# Line: 38

slice_val = self.evaluate(slice_t)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
# Line: 37

out = self.evaluate(tf_ans)

# ==================================================
# Line: 44

out = self.evaluate(tf_ans)

# ==================================================
# Line: 51

out = self.evaluate(y)

# ==================================================
# Line: 57

out = self.evaluate(y)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
# Occurrences: Lines 143-147 (2 instances)

x_t = array_ops.placeholder(dtypes.int32, shape=None)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
# Occurrences: Lines 61-63 (4 instances)

sess.run(x, feed_dict=feed)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
# Line: 604

tensor = self.test.evaluate(op)

# ==================================================
# Line: 612

tensor = self.test.evaluate(op)

# ==================================================
# Occurrences: Lines 1205-1210 (4 instances)

_ = self.evaluate(slice_op)

# ==================================================
# Line: 1257

value = np.array(value).astype(self.tensor_type.as_numpy_dtype)

# ==================================================
# Line: 1274

valnp[index] = np.array(value)

# ==================================================
# Occurrences: Lines 1706-1711 (4 instances)

dims_1 = constant_op.constant([6, 7, 8, 9], dtype=dtype)

# ==================================================
# Occurrences: Lines 2449-2453 (4 instances)

_ = self.evaluate(op)

# ==================================================
# Occurrences: Lines 2511-2514 (2 instances)

tiled_tensor_0 = list_ops.tensor_list_stack(tiled_handles[0], t.dtype, 2,
                                            [3, 4])

# ==================================================
# Occurrences: Lines 2522-2525 (2 instances)

tiled_tensor_0 = list_ops.tensor_list_stack(tiled_handles[0], t.dtype, 2,
                                            [3, 4])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
# Occurrences: Lines 145-145 (2 instances)

data = self.randn(shape, np.float32)

# ==================================================
# Occurrences: Lines 151-151 (2 instances)

data = self.randn(shape, np.float32)

# ==================================================
# Occurrences: Lines 162-162 (2 instances)

data = self.randn(shape, np.float32)

# ==================================================
# Occurrences: Lines 168-168 (2 instances)

data = self.randn(shape, np.float32)

# ==================================================
# Occurrences: Lines 268-272 (8 instances)

actual_pack = array_ops_stack.stack(test_arrays, axis=axis)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
# Occurrences: Lines 283-284 (2 instances)

c = constant_op.constant(large_array)

# ==================================================
# Occurrences: Lines 461-461 (2 instances)

z_value = self.evaluate(z)

# ==================================================
# Occurrences: Lines 467-467 (2 instances)

z_value = self.evaluate(z)

# ==================================================
# Line: 520

np.ones((2, 3), dtype=numpy_dtype), dtype=dtype)

# ==================================================
# Line: 534

feed_dict[d] = np.ones((2, 3), dtype=numpy_dtype)

# ==================================================
# Occurrences: Lines 644-645 (2 instances)

h = array_ops.placeholder(dtypes_lib.int32, shape=[])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_scatter_ops_test.py
# Occurrences: Lines 59-62 (6 instances)

updates = _AsType(
    np.random.randn(*(indices_shape + extra_shape)), vtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
# Occurrences: Lines 390-397 (4 instances)

x = array_ops.placeholder(dtypes.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/edit_distance_op_test.py
# Occurrences: Lines 49-53 (2 instances)

output = self.evaluate(edit_distance)

# ==================================================
# Occurrences: Lines 197-200 (2 instances)

hypothesis_indices = np.empty((0, 2), dtype=np.int64)

# ==================================================
# Occurrences: Lines 212-217 (6 instances)

hypothesis_indices = np.full((3, 3), -1250999896764, dtype=np.int64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
# Line: 185

inp = array_ops.zeros([2**31])

# ==================================================
# Line: 193

inp = array_ops.zeros([2**31])

# ==================================================
# Occurrences: Lines 302-306 (2 instances)

tf_ans = self.evaluate(tensor)

# ==================================================
# Line: 561

input_shape = np.random.randint(1, 4, size=rank)

# ==================================================
# Line: 567

multiples = np.random.randint(1, 4, size=rank).astype(np.int32)

# ==================================================
# Occurrences: Lines 724-734 (4 instances)

tiled = array_ops.tile(inp, array_ops.placeholder(dtypes.int32))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
# Occurrences: Lines 38-42 (3 instances)

array_ops.one_hot(dtype=dtype, **inputs)

# ==================================================
# Line: 49

self.evaluate(ans)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/kullback_leibler_test.py
# Occurrences: Lines 67-71 (2 instances)

a.kl_divergence(a).eval()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
# Line: 83

dist = bernoulli.Bernoulli(probs=p, validate_args=True)

# ==================================================
# Line: 89

dist = bernoulli.Bernoulli(probs=p, validate_args=True)

# ==================================================
# Occurrences: Lines 216-219 (2 instances)

dist = bernoulli.Bernoulli(probs=0.5)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
# Occurrences: Lines 273-275 (2 instances)

xs = np.array([2., 3., 4.], dtype=np.float32)

# ==================================================
# Occurrences: Lines 286-288 (2 instances)

xs = np.array([2., 3., 4.], dtype=np.float32)

# ==================================================
# Occurrences: Lines 299-301 (2 instances)

xs = np.array([2., 3., 4.], dtype=np.float32)  # (3,)

# ==================================================
# Occurrences: Lines 409-412 (3 instances)

mean = student.mean()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
# Occurrences: Lines 61-66 (4 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 241-248 (2 instances)

du.get_logits_and_probs(
    probs=p, multidimensional=True, validate_args=True)

# ==================================================
# Occurrences: Lines 256-263 (2 instances)

du.get_logits_and_probs(
    logits=l, multidimensional=True, validate_args=True)

# ==================================================
# Occurrences: Lines 274-281 (2 instances)

checked_param = du.embed_check_categorical_event_shape(
    param)

# ==================================================
# Occurrences: Lines 289-296 (2 instances)

checked_param = du.embed_check_categorical_event_shape(
    param)

# ==================================================
# Occurrences: Lines 386-393 (4 instances)

vector1 = array_ops.placeholder(dtype=dtypes.float32, shape=[None])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
# Occurrences: Lines 49-50 (2 instances)

a = np.random.rand(3)

# ==================================================
# Occurrences: Lines 58-59 (2 instances)

a = np.random.rand(3, 2, 2)

# ==================================================
# Line: 214

dist = beta_lib.Beta(a, b, allow_nan_stats=False)

# ==================================================
# Line: 220

dist = beta_lib.Beta(a, b, allow_nan_stats=False)

# ==================================================
# Line: 227

dist = beta_lib.Beta(a, b, allow_nan_stats=True)

# ==================================================
# Line: 236

dist = beta_lib.Beta(a, b, allow_nan_stats=True)

# ==================================================
# Occurrences: Lines 307-308 (2 instances)

a = np.random.rand(3, 2, 2).astype(np.float32)

# ==================================================
# Occurrences: Lines 325-327 (6 instances)

a = 10. * np.random.random(shape).astype(dt)

# ==================================================
# Occurrences: Lines 338-340 (6 instances)

a = 10. * np.random.random(shape).astype(dt)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
# Line: 149

log_pdf_values = self.evaluate(log_pdf)

# ==================================================
# Occurrences: Lines 155-157 (2 instances)

self.evaluate(log_pdf).shape)

# ==================================================
# Occurrences: Lines 512-513 (2 instances)

mu = array_ops.placeholder(dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
# Occurrences: Lines 470-471 (6 instances)

a_logits = np.random.randn(batch_size, categories)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# Occurrences: Lines 209-211 (4 instances)

counts_one = np.zeros([3], dtype=np.float32)

# ==================================================
# Line: 378

pmf = dist.prob(counts)

# ==================================================
# Line: 386

pmf = dist.prob(counts)

# ==================================================
# Line: 394

pmf = dist.prob(counts)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
# Line: 89

log_prob = self.evaluate(dist.log_prob(x))

# ==================================================
# Line: 95

log_prob = self.evaluate(dist.log_prob(x))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
# Occurrences: Lines 347-354 (2 instances)

gamma = gamma_lib.Gamma(
    concentration=alpha_v, rate=beta_v, validate_args=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
# Occurrences: Lines 334-341 (2 instances)

laplace = laplace_lib.Laplace(
    loc=loc_v, scale=scale_v, validate_args=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
# Line: 126

run_concurrently = run_concurrently()

# ==================================================
# Line: 132

run_concurrently()

# ==================================================
# Occurrences: Lines 205-220 (6 instances)

to_capture_too = array_ops.identity(to_capture)

# ==================================================
# Line: 246

i_n = array_ops.identity(i_n)

# ==================================================
# Line: 272

i_n = array_ops.identity(i_n)

# ==================================================
# Line: 296

i_n = array_ops.identity(i_n)

# ==================================================
# Occurrences: Lines 313-314 (2 instances)

cs = critical_section_ops.CriticalSection(shared_name="cs")

# ==================================================
# Occurrences: Lines 326-327 (2 instances)

cs0 = critical_section_ops.CriticalSection()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
# Occurrences: Lines 187-198 (3 instances)

table1 = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(keys, values),
    default_val,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Occurrences: Lines 391-392 (2 instances)

session1 = session.Session(server.target)

# ==================================================
# Occurrences: Lines 498-514 (4 instances)

table = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(keys, values),
    -1,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 674

init1 = lookup_ops.KeyValueTensorInitializer(
    ("brain", "salad", "surgery"), (0, 1, 2), dtypes.string, dtypes.int64)

# ==================================================
# Line: 682

init2 = lookup_ops.KeyValueTensorInitializer(
    ("brain", "salad", "surgery"), (0, 1, 2), dtypes.string, dtypes.int64)

# ==================================================
# Occurrences: Lines 859-873 (3 instances)

init1 = lookup_ops.TextFileInitializer(
    vocabulary_file, dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
    dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER)

# ==================================================
# Line: 1240

table1 = self.getVocabularyTable()(
    lookup_ops.TextFileIdTableInitializer(
        vocab_file, vocab_size=vocab_size),
    oov_buckets,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 1262

table2 = self.getVocabularyTable()(
    lookup_ops.TextFileIdTableInitializer(
        vocab_file, vocab_size=vocab_size),
    oov_buckets,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 1866

save = saver.Saver()

# ==================================================
# Line: 1899

save = saver.Saver()

# ==================================================
# Line: 1935

save = saver.Saver([table])

# ==================================================
# Line: 1968

save = saver.Saver([table])

# ==================================================
# Occurrences: Lines 2108-2110 (3 instances)

empty_key = constant_op.constant([11, 13], dtypes.int64)

# ==================================================
# Line: 2126

save = saver.Saver()

# ==================================================
# Occurrences: Lines 2143-2145 (3 instances)

empty_key = constant_op.constant([11, 13], dtypes.int64)

# ==================================================
# Line: 2162

save = saver.Saver()

# ==================================================
# Occurrences: Lines 2184-2186 (3 instances)

empty_key = constant_op.constant([11, 13], dtypes.int64)

# ==================================================
# Line: 2201

save = saver.Saver()

# ==================================================
# Occurrences: Lines 2218-2220 (3 instances)

empty_key = constant_op.constant([11, 13], dtypes.int64)

# ==================================================
# Line: 2237

save = saver.Saver()

# ==================================================
# Line: 2313

values1 = constant_op.constant([0, 1], dtypes.int64)

# ==================================================
# Line: 2325

values2 = constant_op.constant([0, 1], dtypes.int64)

# ==================================================
# Occurrences: Lines 2336-2337 (2 instances)

keys = constant_op.constant([[11, 0], [12, 1]], dtypes.int64)

# ==================================================
# Occurrences: Lines 2393-2394 (2 instances)

v = variables.Variable(1.)

# ==================================================
# Occurrences: Lines 2685-2697 (4 instances)

table = lookup_ops.index_table_from_tensor(
    vocabulary_list=("brain", "salad", "surgery"), num_oov_buckets=1)

# ==================================================
# Line: 3072

table1 = lookup_ops.IdTableWithHashBuckets(
    lookup_ops.StaticHashTable(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size), default_value), oov_buckets)

# ==================================================
# Line: 3092

table2 = lookup_ops.IdTableWithHashBuckets(
    lookup_ops.StaticHashTable(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size), default_value), oov_buckets)

# ==================================================
# Occurrences: Lines 3411-3419 (2 instances)

table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    name="t1",
    checkpoint=True,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 3438

table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    name="t1",
    checkpoint=True,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 3451

save = saver.Saver()

# ==================================================
# Occurrences: Lines 3480-3488 (2 instances)

table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    name="t1",
    checkpoint=True,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 3505

table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    name="t1",
    checkpoint=True,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 3518

save = saver.Saver([table])

# ==================================================
# Occurrences: Lines 3544-3552 (2 instances)

table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    name="t1",
    checkpoint=True,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 3569

table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    name="t1",
    checkpoint=True,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 3582

checkpoint = trackable.Checkpoint(table=table, v0=v0, v1=v1)

# ==================================================
# Occurrences: Lines 3657-3658 (2 instances)

session1 = session.Session(server.target)

# ==================================================
# Line: 3728

table1 = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Line: 3747

table2 = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# Occurrences: Lines 4038-4052 (3 instances)

table1 = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
# Line: 198

t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)

# ==================================================
# Line: 206

t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)

# ==================================================
# Line: 220

t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)

# ==================================================
# Line: 229

t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)

# ==================================================
# Line: 241

t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)

# ==================================================
# Line: 252

t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)

# ==================================================
# Line: 262

t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)

# ==================================================
# Line: 394

t = list_ops.tensor_list_gather(l, [], element_dtype=dtypes.float32)

# ==================================================
# Line: 405

t = list_ops.tensor_list_gather(l, [], element_dtype=dtypes.float32)

# ==================================================
# Line: 416

t = list_ops.tensor_list_gather(l, [], element_dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 625-627 (2 instances)

l, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)

# ==================================================
# Line: 722

e1 = gen_list_ops.tensor_list_get_item(
    l, 1, element_shape=[2, 3], element_dtype=dtypes.float32)

# ==================================================
# Line: 731

e1 = gen_list_ops.tensor_list_get_item(
    l, 1, element_shape=[2, 3], element_dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 790-792 (2 instances)

l, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 1221-1227 (6 instances)

l = list_ops.tensor_list_push_back(l, sub_l)

# ==================================================
# Occurrences: Lines 1280-1281 (2 instances)

l_read1 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 1300-1303 (2 instances)

self.assertIs(fn(shape), shape)

# ==================================================
# Line: 1309

result = fn(shape)

# ==================================================
# Occurrences: Lines 1326-1331 (2 instances)

a = list_ops.empty_tensor_list(
    element_dtype=dtypes.variant, element_shape=[])

# ==================================================
# Occurrences: Lines 1360-1361 (2 instances)

l1_element_shape = array_ops.placeholder(dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 1426-1430 (2 instances)

t = list_ops.tensor_list_concat(l, element_dtype=dtypes.float32)

# ==================================================
# Line: 1471

t = list_ops.tensor_list_concat(l1, element_dtype=dtypes.float32)

# ==================================================
# Line: 1478

t = list_ops.tensor_list_concat(l1, element_dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 1761-1763 (4 instances)

outer_l = array_ops.identity(outer_l)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
# Occurrences: Lines 40-41 (2 instances)

pi = array_ops.placeholder(dtypes.int64)

# ==================================================
# Occurrences: Lines 62-63 (2 instances)

pi = array_ops.placeholder(dtypes.int64)

# ==================================================
# Occurrences: Lines 85-86 (2 instances)

pi = array_ops.placeholder(dtypes.int64)

# ==================================================
# Occurrences: Lines 134-135 (2 instances)

pi = array_ops.placeholder(dtypes.int64)

# ==================================================
# Occurrences: Lines 163-164 (2 instances)

pi = array_ops.placeholder(dtypes.int64)

# ==================================================
# Occurrences: Lines 349-353 (5 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 407-411 (5 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 451-456 (6 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 543-548 (6 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/priority_queue_test.py
# Occurrences: Lines 42-43 (2 instances)

side_value_0 = np.random.rand(100).astype(bytes)

# ==================================================
# Occurrences: Lines 76-77 (2 instances)

side_value_0 = np.random.rand(100).astype(bytes)

# ==================================================
# Occurrences: Lines 237-238 (2 instances)

side_value_0 = np.random.rand(100).astype(bytes)

# ==================================================
# Occurrences: Lines 286-287 (2 instances)

side_value_0 = np.random.rand(1000).astype(bytes)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
# Occurrences: Lines 160-164 (2 instances)

_, keys_val, values_0_val, values_1_val = sess.run(
    [index_t, key_t, value_list_t[0], value_list_t[1]])

# ==================================================
# Occurrences: Lines 174-178 (2 instances)

_, keys_val, values_0_val, values_1_val = sess.run(
    [index_t, key_t, value_list_t[0], value_list_t[1]])

# ==================================================
# Occurrences: Lines 623-635 (4 instances)

indices_val, unused_keys_val, unused_val_0, unused_val_1 = sess.run(
    [
        take_ops[i][0], take_ops[i][1], take_ops[i][2][0],
        take_ops[i][2][1]
    ])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
# Line: 398

float_val, int_val = self.evaluate(dequeued_t)

# ==================================================
# Line: 404

float_val, int_val = self.evaluate(dequeued_t)

# ==================================================
# Line: 429

float_val, int_val = self.evaluate(dequeued_t)

# ==================================================
# Line: 439

float_val, int_val = self.evaluate(dequeued_t)

# ==================================================
# Occurrences: Lines 1339-1344 (2 instances)

q1 = data_flow_ops.PaddingFIFOQueue(
    1, dtypes_lib.float32, ((),), shared_name="shared_queue")

# ==================================================
# Occurrences: Lines 1462-1466 (2 instances)

q_empty = data_flow_ops.PaddingFIFOQueue(5, dtypes_lib.float32, ((),))

# ==================================================
# Occurrences: Lines 1577-1579 (4 instances)

np_array = np.sqrt(np_array.astype(np_dtype))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
# Occurrences: Lines 132-134 (2 instances)

q = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])

# ==================================================
# Line: 144

self.q1 = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])

# ==================================================
# Line: 150

self.q2 = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])

# ==================================================
# Line: 312

dequeued_t = q.dequeue_many(4)

# ==================================================
# Line: 319

float_val, int_val = self.evaluate(q.dequeue_many(4))

# ==================================================
# Line: 341

dequeued_t = q.dequeue_up_to(4)

# ==================================================
# Line: 349

float_val, int_val = self.evaluate(q.dequeue_up_to(4))

# ==================================================
# Occurrences: Lines 491-496 (2 instances)

q1 = data_flow_ops.FIFOQueue(
    1, dtypes_lib.float32, shared_name="shared_queue")

# ==================================================
# Occurrences: Lines 601-603 (4 instances)

np_array = np.sqrt(np_array.astype(np_dtype))

# ==================================================
# Occurrences: Lines 654-656 (2 instances)

f = sess.run(dequeue_2["f"])

# ==================================================
# Occurrences: Lines 714-718 (2 instances)

i, f, s = sess.run([dequeue_2["i"], dequeue_2["f"], dequeue_2["s"]])

# ==================================================
# Occurrences: Lines 1771-1775 (4 instances)

_ = session.run(output)  # warm up.

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
# Occurrences: Lines 124-127 (2 instances)

h1 = gen_data_flow_ops.stack_v2(
    -1, elem_type=dtypes.float32, stack_name="foo")

# ==================================================
# Occurrences: Lines 261-263 (2 instances)

h1 = gen_data_flow_ops._stack(dtypes.float32, stack_name="foo")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/listdiff_op_test.py
# Occurrences: Lines 85-87 (4 instances)

x_size = np.random.randint(max_size + 1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
# Occurrences: Lines 87-94 (4 instances)

q_f32_0 = data_flow_ops.ConditionalAccumulator(
    dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))

# ==================================================
# Line: 236

val = self.evaluate(takeg_t)

# ==================================================
# Line: 245

val = self.evaluate(takeg_t)

# ==================================================
# Line: 264

val = self.evaluate(takeg_t)

# ==================================================
# Line: 273

val = self.evaluate(takeg_t)

# ==================================================
# Occurrences: Lines 308-326 (6 instances)

elems_ave = sum(elems) / len(elems)

# ==================================================
# Occurrences: Lines 341-346 (2 instances)

takeg_t = q.take_grad(1)

# ==================================================
# Occurrences: Lines 352-357 (2 instances)

takeg_t = q.take_grad(1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
# Occurrences: Lines 77-80 (2 instances)

s = map_ops.tensor_map_size(m)

# ==================================================
# Occurrences: Lines 94-95 (2 instances)

k2 = constant_op.constant(2.0)

# ==================================================
# Occurrences: Lines 105-106 (2 instances)

k2 = constant_op.constant(2.0)

# ==================================================
# Occurrences: Lines 117-118 (2 instances)

k2 = constant_op.constant(2.0)

# ==================================================
# Line: 143

keys = map_ops.tensor_map_stack_keys(m, k.dtype)

# ==================================================
# Line: 149

keys = map_ops.tensor_map_stack_keys(m, k.dtype)

# ==================================================
# Line: 390

s = map_ops.tensor_map_size(m)

# ==================================================
# Line: 404

s = map_ops.tensor_map_size(m)

# ==================================================
# Line: 439

s = map_ops.tensor_map_size(m)

# ==================================================
# Line: 445

s = map_ops.tensor_map_size(m)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
# Line: 155

w1 = w0.write(1, constant_op.constant([],
                                      shape=(0,),
                                      dtype=dtypes.int32))

# ==================================================
# Line: 164

w1 = w0.write(1, constant_op.constant([],
                                      shape=(0,),
                                      dtype=dtypes.int32))

# ==================================================
# Line: 272

d0, d1, d2 = self.evaluate([r0, r1, r2])

# ==================================================
# Line: 283

d0, d1, d2 = self.evaluate([r0, r1, r2])

# ==================================================
# Line: 294

d0, d1, d2 = self.evaluate([r0, r1, r2])

# ==================================================
# Occurrences: Lines 320-324 (4 instances)

r0 = w0.read(0)

# ==================================================
# Occurrences: Lines 330-336 (5 instances)

lengths = constant_op.constant([2, 0, 1])

# ==================================================
# Occurrences: Lines 342-349 (5 instances)

lengths = constant_op.constant([2, 0, 1])

# ==================================================
# Occurrences: Lines 469-470 (2 instances)

g_ta_0 = ta.grad("grad")

# ==================================================
# Line: 567

ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32,
    tensor_array_name="foo",
    size=3,
    infer_shape=False)

# ==================================================
# Line: 581

ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32,
    tensor_array_name="foo",
    size=3,
    infer_shape=False)

# ==================================================
# Occurrences: Lines 766-768 (2 instances)

r0 = w1.read(0)

# ==================================================
# Line: 849

r0_readonce = w_readonce.read(0)

# ==================================================
# Line: 855

self.evaluate(w_readonce.read(0))

# ==================================================
# Occurrences: Lines 863-865 (2 instances)

r0_readtwice = w_readtwice.read(0)

# ==================================================
# Occurrences: Lines 880-881 (2 instances)

r0 = w.read(0)

# ==================================================
# Line: 1201

ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=3)

# ==================================================
# Line: 1208

ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=3)

# ==================================================
# Line: 1217

ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=3)

# ==================================================
# Occurrences: Lines 1229-1234 (2 instances)

c0 = array_ops.placeholder(dtypes.float32, [None, None, None, 3])

# ==================================================
# Line: 1311

r0 = w0.read(0)

# ==================================================
# Line: 1321

r0 = w0.read(0)

# ==================================================
# Occurrences: Lines 1480-1482 (2 instances)

ta = ta.unstack(array_ops.zeros([0, 3, 5]))

# ==================================================
# Line: 1599

ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=2)

# ==================================================
# Line: 1621

ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/composite_tensor_ops_test.py
# Occurrences: Lines 133-136 (2 instances)

y = func(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
# Line: 90

tensor = math_ops.range(10)

# ==================================================
# Line: 98

tensor = math_ops.range(10)

# ==================================================
# Line: 106

tensor = math_ops.range(10)

# ==================================================
# Line: 114

tensor = math_ops.range(10)

# ==================================================
# Occurrences: Lines 284-287 (2 instances)

line_0 = f.readline()

# ==================================================
# Line: 350

x = f(tensor)

# ==================================================
# Line: 357

y = f(tensor)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
# Occurrences: Lines 86-89 (2 instances)

gradients = constant_op.constant(
    value=[[1.0], [2.0], [4.0]], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 115-118 (2 instances)

gradients = constant_op.constant(
    value=[[1.0], [2.0], [4.0]], dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_matmul_op_test.py
# Occurrences: Lines 89-90 (2 instances)

x = np.ones((0, 0)).astype(np.float32)

# ==================================================
# Occurrences: Lines 99-100 (2 instances)

r2 = np.random.randint(1, 10)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
# Occurrences: Lines 60-62 (2 instances)

val = np.array([1, 2, 3, 4])

# ==================================================
# Line: 123

sum_out = self.evaluate(sp_sum)

# ==================================================
# Line: 132

sum_out = self.evaluate(sp_sum)

# ==================================================
# Occurrences: Lines 145-146 (6 instances)

sp_a, nnz_a = self._randomTensor([n, m], np.float32)

# ==================================================
# Occurrences: Lines 160-161 (6 instances)

rand_vals_np = np.random.randn(n, m).astype(dtype)

# ==================================================
# Occurrences: Lines 180-181 (2 instances)

rand_vals_np = np.random.randn(n, m).astype(np.float32)

# ==================================================
# Occurrences: Lines 253-255 (2 instances)

sp_vals = np.random.rand(n, m).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
# Line: 609

grad, _ = self.evaluate(
    sparse_ops.sparse_fill_empty_rows_grad(
        reverse_index_map=[-1, 3], grad_values=[]
    )
)

# ==================================================
# Line: 620

self.evaluate(
    sparse_ops.sparse_fill_empty_rows_grad(
        reverse_index_map=[-1, 3], grad_values=[]
    )
)

# ==================================================
# Occurrences: Lines 903-912 (4 instances)

err = gradient_checker.compute_gradient_error(
    sp_t.values, (nnz,), reduced,
    self.evaluate(reduced).shape)

# ==================================================
# Line: 1185

sp_zero = sparse_tensor.SparseTensor([[0]], [0], [7])

# ==================================================
# Line: 1193

sp_zero = sparse_tensor.SparseTensor([[0]], [0], [7])

# ==================================================
# Occurrences: Lines 1219-1220 (6 instances)

a_np = np.random.randn(*shape).astype(dtype)

# ==================================================
# Occurrences: Lines 1243-1248 (2 instances)

sp_one = sparse_tensor.SparseTensor([[0]], [1], [2])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
# Occurrences: Lines 289-292 (2 instances)

sp_output = sparse_ops.sparse_slice(sp_input, start, size)

# ==================================================
# Occurrences: Lines 301-304 (2 instances)

sp_output = sparse_ops.sparse_slice(sp_input, start, size)

# ==================================================
# Occurrences: Lines 313-316 (2 instances)

sp_output = sparse_ops.sparse_slice(sp_input, start, size)

# ==================================================
# Occurrences: Lines 326-329 (2 instances)

sp_output = sparse_ops.sparse_slice(sp_input, start, size)

# ==================================================
# Occurrences: Lines 339-342 (2 instances)

sp_output = sparse_ops.sparse_slice(sp_input, start, size)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
# Occurrences: Lines 461-474 (6 instances)

st1 = sparse_tensor.SparseTensor([[0, 0]], [0], [2, 2])

# ==================================================
# Occurrences: Lines 861-863 (3 instances)

sp_inp_1 = self._sparse_tensor([])

# ==================================================
# Occurrences: Lines 1029-1049 (2 instances)

inds, vals, shapes = gen_sparse_ops.sparse_cross_hashed(
    indices=[sp_inp_1.indices, sp_inp_2.indices, sp_inp_3.indices],
    values=[sp_inp_1.values, sp_inp_2.values, sp_inp_3.values],
    shapes=[
        sp_inp_1.dense_shape, sp_inp_2.dense_shape, sp_inp_3.dense_shape
    ],
    dense_inputs=[],
    strong_hash=True,
    num_buckets=1000,
    salt=[137, 173])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
# Occurrences: Lines 237-237 (2 instances)

self._SparseTensor_3x4x2()):

# ==================================================
# Occurrences: Lines 243-243 (2 instances)

expected_output = self._SparseTensor_3x4x2()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_d9m_test.py
# Occurrences: Lines 121-125 (4 instances)

result_a = sparse_ops.sparse_tensor_dense_matmul(
    sparse_input, dense_input)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
# Occurrences: Lines 177-187 (4 instances)

output = sparse_ops.sparse_to_dense(indices, shape, 1, 0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
# Occurrences: Lines 138-140 (4 instances)

sum_elems = np.zeros([3, 3, 3]).astype(dtype.as_numpy_dtype)

# ==================================================
# Occurrences: Lines 153-160 (4 instances)

q_f32_0 = data_flow_ops.SparseConditionalAccumulator(
    dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([2, 2]))

# ==================================================
# Occurrences: Lines 172-174 (4 instances)

expected_tensor = _indexedslice(tensor_to_add)

# ==================================================
# Occurrences: Lines 245-246 (2 instances)

takeg_t = q.take_indexed_slices_grad(1)

# ==================================================
# Occurrences: Lines 262-263 (2 instances)

takeg_t = q.take_indexed_slices_grad(1)

# ==================================================
# Line: 654

val = self.evaluate(q.take_indexed_slices_grad(1))

# ==================================================
# Line: 666

val = self.evaluate(q.take_indexed_slices_grad(1))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test.py
# Occurrences: Lines 85-88 (4 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 96-99 (3 instances)

ops = _sparse_vs_dense_xent_benchmark_dense(labels, logits)

# ==================================================
# Occurrences: Lines 105-108 (3 instances)

ops = _sparse_vs_dense_xent_benchmark_sparse(labels, logits)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
# Occurrences: Lines 216-217 (2 instances)

r2 = np.random.randint(1, 10)

# ==================================================
# Occurrences: Lines 342-344 (4 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 355-365 (7 instances)

x_t = constant_op.constant(x)

# ==================================================
# Occurrences: Lines 371-385 (11 instances)

x_ind = constant_op.constant(np.vstack(np.where(x)).astype(np.int64).T)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_d9m_test.py
# Occurrences: Lines 107-110 (8 instances)

result_a = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
    labels=labels, logits=logits)

# ==================================================
# Occurrences: Lines 135-136 (8 instances)

result_a = gradients(seed=seed)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_grad_test.py
# Occurrences: Lines 48-50 (2 instances)

x = np.random.randn(n, m).astype(values_dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
# Occurrences: Lines 392-395 (2 instances)

x = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 1]], values=[1, 2], dense_shape=[2, 2])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
# Occurrences: Lines 169-170 (2 instances)

serialized = array_ops_stack.stack([serialized, serialized])

# ==================================================
# Occurrences: Lines 212-213 (2 instances)

sp_input0 = self._SparseTensorPlaceholder()

# ==================================================
# Occurrences: Lines 369-370 (2 instances)

sp_input0 = self._SparseTensorPlaceholder()

# ==================================================
# Occurrences: Lines 407-408 (2 instances)

sp_input0 = self._SparseTensorPlaceholder()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
# Occurrences: Lines 296-297 (2 instances)

sp_input = self._SparseTensorPlaceholder()

# ==================================================
# Occurrences: Lines 303-305 (2 instances)

sp_input = self._SparseTensorPlaceholder()

# ==================================================
# Line: 311

sp_input = self._SparseTensorPlaceholder()

# ==================================================
# Occurrences: Lines 325-328 (2 instances)

orig_rank = np.random.randint(2, 7)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
# Occurrences: Lines 280-287 (2 instances)

tf_loss = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
    labels=labels, logits=logits)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_jpeg_op_test.py
# Occurrences: Lines 90-90 (2 instances)

image = image_ops.decode_jpeg(image_content, channels=3)

# ==================================================
# Occurrences: Lines 97-97 (2 instances)

image = image_ops.decode_jpeg(image_content, channels=3)

# ==================================================
# Occurrences: Lines 112-115 (2 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_image_patches_op_test.py
# Occurrences: Lines 65-67 (2 instances)

image = np.reshape(range(120), [2, 3, 4, 5])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# Occurrences: Lines 378-379 (2 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
# Line: 752

x = constant_op.constant(0)

# ==================================================
# Line: 769

inner_x = constant_op.constant(0)

# ==================================================
# Occurrences: Lines 1022-1023 (2 instances)

x = array_ops.placeholder(dtype=dtypes.float32, shape=shape)

# ==================================================
# Line: 1069

while_op = self._createWhile(None)

# ==================================================
# Line: 1081

while2_op = self._createWhile(None)

# ==================================================
# Occurrences: Lines 1159-1160 (4 instances)

v = array_ops.identity(v)

# ==================================================
# Occurrences: Lines 1264-1265 (2 instances)

external_t = constant_op.constant(2.)

# ==================================================
# Occurrences: Lines 1307-1307 (3 instances)

forward_graph = ops.get_default_graph()

# ==================================================
# Occurrences: Lines 1314-1314 (3 instances)

gradient_graph = ops.get_default_graph()

# ==================================================
# Occurrences: Lines 1347-1347 (3 instances)

forward_graph = ops.get_default_graph()

# ==================================================
# Occurrences: Lines 1354-1354 (3 instances)

gradient_graph = ops.get_default_graph()

# ==================================================
# Occurrences: Lines 1388-1388 (2 instances)

actual_name_scope = ops.get_name_scope()

# ==================================================
# Occurrences: Lines 1397-1397 (2 instances)

actual_name_scope = ops.get_name_scope()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
# Line: 47

x = numpy_reverse(x, axis)

# ==================================================
# Line: 65

x = numpy_reverse(x, axis)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
# Line: 131

r = map_fn.map_fn(double_scoped, elems)

# ==================================================
# Line: 141

r = map_fn.map_fn(double_scoped, elems)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
# Line: 78

expected_val, actual_val, expected_grad_val, actual_grad_val = sess.run(
    (expected, actual, expected_grad, actual_grad), sess_run_args)

# ==================================================
# Line: 85

expected_val, actual_val, expected_grad_val, actual_grad_val = sess.run(
    (expected, actual, expected_grad, actual_grad), sess_run_args)

# ==================================================
# Line: 92

expected_val, actual_val, expected_grad_val, actual_grad_val = sess.run(
    (expected, actual, expected_grad, actual_grad), sess_run_args)

# ==================================================
# Line: 99

expected_val, actual_val, expected_grad_val, actual_grad_val = sess.run(
    (expected, actual, expected_grad, actual_grad), sess_run_args)

# ==================================================
# Line: 221

y = tape.gradient(f(x, cond), v)

# ==================================================
# Line: 228

y = tape.gradient(f(x, cond), v)

# ==================================================
# Line: 331

_, cond_op = self._createCond(None)

# ==================================================
# Line: 345

_, cond2_op = self._createCond(None)

# ==================================================
# Occurrences: Lines 361-361 (2 instances)

actual_name_scope = ops.get_name_scope()

# ==================================================
# Occurrences: Lines 368-368 (2 instances)

actual_name_scope = ops.get_name_scope()

# ==================================================
# Occurrences: Lines 551-561 (6 instances)

x, y, pred1, pred2, true_fn, false_fn = build_graph()

# ==================================================
# Occurrences: Lines 1519-1524 (2 instances)

z = math_ops.add(x, y)

# ==================================================
# Line: 1547

q0 = data_flow_ops.FIFOQueue(1, dtypes.float32)

# ==================================================
# Occurrences: Lines 1558-1566 (11 instances)

v1 = variables.Variable([1])

# ==================================================
# Occurrences: Lines 1580-1588 (11 instances)

v1 = variables.Variable([1])

# ==================================================
# Occurrences: Lines 1609-1611 (2 instances)

q4 = data_flow_ops.FIFOQueue(1, dtypes.float32)

# ==================================================
# Line: 1642

c = constant_op.constant(3.0)

# ==================================================
# Line: 1651

c = constant_op.constant(3.0)

# ==================================================
# Occurrences: Lines 1711-1714 (4 instances)

cpu_zero_op = test_ops.device_placement_op()

# ==================================================
# Line: 1732

return test_ops.device_placement_op()

# ==================================================
# Occurrences: Lines 1759-1761 (4 instances)

local_op = test_ops.device_placement_op()

# ==================================================
# Occurrences: Lines 1778-1780 (4 instances)

local_op = test_ops.device_placement_op()

# ==================================================
# Occurrences: Lines 1808-1810 (4 instances)

zero_expected = cond_v2.cond_v2(condition, _fn, _fn)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Occurrences: Lines 624-626 (3 instances)

v1 = variables.Variable(7)

# ==================================================
# Occurrences: Lines 1081-1082 (2 instances)

run_metadata_no_lowering = config_pb2.RunMetadata()

# ==================================================
# Occurrences: Lines 1237-1238 (2 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# Line: 1332

y2 = array_ops.gather(x1, [2]) * x2

# ==================================================
# Occurrences: Lines 1338-1339 (4 instances)

y2 = array_ops.gather(x1, [2]) * x2

# ==================================================
# Occurrences: Lines 1648-1649 (2 instances)

input1 = array_ops.placeholder(dtype=dtypes.float32, shape=[None, None])

# ==================================================
# Occurrences: Lines 1765-1773 (4 instances)

xla_context = control_flow_ops.XLAControlFlowContext()

# ==================================================
# Occurrences: Lines 1824-1832 (4 instances)

final_with_xla_context = create_while_loop()

# ==================================================
# Occurrences: Lines 1884-1887 (4 instances)

i = ops.convert_to_tensor(0)

# ==================================================
# Occurrences: Lines 1905-1908 (4 instances)

i = ops.convert_to_tensor(0)

# ==================================================
# Occurrences: Lines 1928-1929 (2 instances)

c = ops.convert_to_tensor([0])

# ==================================================
# Occurrences: Lines 2428-2429 (2 instances)

n = constant_op.constant(0)

# ==================================================
# Occurrences: Lines 2704-2705 (2 instances)

select1 = variables.Variable([3.0, 4.0, 5.0])

# ==================================================
# Line: 2877

i = constant_op.constant(0)

# ==================================================
# Line: 2890

x = constant_op.constant(0)

# ==================================================
# Occurrences: Lines 3281-3282 (2 instances)

x2_init = constant_op.constant(1.)

# ==================================================
# Occurrences: Lines 3640-3641 (2 instances)

_, r1 = while_loop_tf.while_loop(c, b, [i, x], parallel_iterations=1)

# ==================================================
# Line: 3697

z = constant_op.constant(0)

# ==================================================
# Line: 3703

z = constant_op.constant(0)

# ==================================================
# Line: 3721

z = constant_op.constant(0)

# ==================================================
# Line: 3727

z = constant_op.constant(0)

# ==================================================
# Occurrences: Lines 4040-4041 (2 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# Line: 4220

y = constant_op.constant(2)

# ==================================================
# Line: 4267

default=lambda: constant_op.constant(2))

# ==================================================
# Occurrences: Lines 4274-4276 (3 instances)

v0 = variables.Variable(-1)

# ==================================================
# Occurrences: Lines 4419-4424 (2 instances)

vd = variable_v1.VariableV1([0.0])

# ==================================================
# Occurrences: Lines 4467-4469 (3 instances)

p1 = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 4475-4515 (18 instances)

p1 = array_ops.placeholder(dtypes.float32, shape=[1, 2])

# ==================================================
# Occurrences: Lines 4524-4528 (4 instances)

p1 = array_ops.placeholder(dtypes.float32)

# ==================================================
# Occurrences: Lines 4535-4543 (5 instances)

v1 = variable_v1.VariableV1([[1, 2]])

# ==================================================
# Occurrences: Lines 4549-4550 (2 instances)

v2 = variable_v1.VariableV1(p2, validate_shape=False)

# ==================================================
# Occurrences: Lines 4948-4950 (2 instances)

guarded_metadata = config_pb2.RunMetadata()

# ==================================================
# Occurrences: Lines 5056-5059 (2 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
# Occurrences: Lines 73-76 (2 instances)

f = script_ops.eager_py_func(raise_exception, [], [])

# ==================================================
# Line: 188

x = constant_op.constant(0.0, dtypes.float64)

# ==================================================
# Line: 195

x = constant_op.constant(0.0, dtypes.float64)

# ==================================================
# Line: 485

initial_size = script_ops._py_funcs.size()

# ==================================================
# Line: 492

self.assertEqual(initial_size, script_ops._py_funcs.size())

# ==================================================
# Line: 644

old_cache_size = len(script_ops.tape_cache)

# ==================================================
# Occurrences: Lines 651-668 (6 instances)

y = script_ops.eager_py_func(f, inp=[x], Tout=dtypes.float32)

# ==================================================
# Line: 680

dy_dx = tape.gradient(y, x)

# ==================================================
# Line: 688

dy_dx = tape.gradient(y, x)

# ==================================================
# Occurrences: Lines 756-757 (2 instances)

x = array_ops.placeholder(dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
# Line: 149

in_value = constant_op.constant([1.])

# ==================================================
# Line: 163

in_value = constant_op.constant([1.])

# ==================================================
# Occurrences: Lines 199-204 (2 instances)

tokens[dev] = create_ordering_token()

# ==================================================
# Line: 218

in_value = constant_op.constant([1.])

# ==================================================
# Line: 246

cpu_tokens[i] = create_ordering_token()

# ==================================================
# Line: 506

dev = '/{}:{}'.format(device, device_idx)

# ==================================================
# Line: 516

dev = '/{}:{}'.format(device, device_idx)

# ==================================================
# Line: 564

in_value = constant_op.constant([1.])

# ==================================================
# Line: 588

in_value = constant_op.constant([1.])

# ==================================================
# Occurrences: Lines 752-756 (3 instances)

r1 = _collective_ops.all_reduce_v2([1.],
                                   group_size,
                                   group_key,
                                   instance_key,
                                   ordering_token=token)

# ==================================================
# Occurrences: Lines 762-766 (3 instances)

r2 = _collective_ops.all_reduce_v2([1.],
                                   group_size,
                                   group_key,
                                   instance_key,
                                   ordering_token=token)

# ==================================================
# Line: 1125

ret = collective_op(
    in_tensor,
    group_size,
    group_key,
    instance_key,
    ordering_token=tokens[dev0],
    communication_hint=communication)

# ==================================================
# Line: 1144

collective_op(
    in_tensor,
    group_size,
    group_key,
    instance_key,
    ordering_token=tokens[dev0],
    communication_hint=communication)

# ==================================================
# Occurrences: Lines 1241-1243 (3 instances)

in_tensor = constant_op.constant([1.])

# ==================================================
# Line: 1286

args=(dev0, constant_op.constant([1.]), t1_cancellation_manager,

# ==================================================
# Line: 1313

dev = '/{}:{}'.format(device, i)

# ==================================================
# Line: 1326

dev = '/{}:{}'.format(device, i)

# ==================================================
# Occurrences: Lines 1342-1346 (2 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 1513-1515 (2 instances)

token0 = create_ordering_token()

# ==================================================
# Line: 1543

ordering_token=create_ordering_token(),

# ==================================================
# Line: 1551

ordering_token=create_ordering_token(),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/proto/encode_proto_op_test_base.py
# Occurrences: Lines 98-99 (2 instances)

sizes = array_ops.placeholder(dtypes.int32)

# ==================================================
# Occurrences: Lines 121-122 (2 instances)

values1 = array_ops.placeholder(dtypes.float64)

# ==================================================
# Occurrences: Lines 157-160 (4 instances)

in_obj = test_example_pb2.TestValue()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
# Occurrences: Lines 86-86 (2 instances)

fd = test_example_pb2.PrimitiveValue()

# ==================================================
# Occurrences: Lines 99-99 (2 instances)

msg = test_example_pb2.PrimitiveValue()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/proto/proto_op_test_base.py
# Occurrences: Lines 56-131 (16 instances)

field = test_case.fields.add()

# ==================================================
# Line: 173

field = test_case.fields.add()

# ==================================================
# Line: 180

field = test_case.fields.add()

# ==================================================
# Line: 187

field = test_case.fields.add()

# ==================================================
# Line: 193

field = test_case.fields.add()

# ==================================================
# Line: 199

field = test_case.fields.add()

# ==================================================
# Line: 205

field = test_case.fields.add()

# ==================================================
# Line: 211

field = test_case.fields.add()

# ==================================================
# Line: 217

field = test_case.fields.add()

# ==================================================
# Line: 223

field = test_case.fields.add()

# ==================================================
# Line: 229

field = test_case.fields.add()

# ==================================================
# Line: 235

field = test_case.fields.add()

# ==================================================
# Line: 241

field = test_case.fields.add()

# ==================================================
# Line: 247

field = test_case.fields.add()

# ==================================================
# Line: 253

field = test_case.fields.add()

# ==================================================
# Occurrences: Lines 282-287 (2 instances)

field = test_case.fields.add()

# ==================================================
# Occurrences: Lines 304-324 (5 instances)

field = test_case.fields.add()

# ==================================================
# Occurrences: Lines 333-337 (2 instances)

value = test_case.values.add()

# ==================================================
# Line: 345

field = test_case.fields.add()

# ==================================================
# Line: 352

field = test_case.fields.add()

# ==================================================
# Occurrences: Lines 362-377 (6 instances)

value = test_case.values.add()

# ==================================================
# Line: 384

field = test_case.fields.add()

# ==================================================
# Line: 393

field = test_case.fields.add()

# ==================================================
# Occurrences: Lines 428-438 (3 instances)

field = test_case.fields.add()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
# Occurrences: Lines 365-367 (2 instances)

var_x = variable_v1.VariableV1(2.0)

# ==================================================
# Occurrences: Lines 500-509 (2 instances)

v = variables.Variable(
    lambda: constant_op.constant(1.),
    constraint=constraint)

# ==================================================
# Line: 549

v = variables.Variable(variable_def=v_def)

# ==================================================
# Line: 561

v = variables.Variable(variable_def=v_def)

# ==================================================
# Line: 796

v0 = variables.Variable([0])

# ==================================================
# Line: 806

v0 = variables.Variable([0])

# ==================================================
# Line: 822

v0 = variables.Variable([0])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
# Occurrences: Lines 212-218 (2 instances)

var1 = gen_state_ops.temporary_variable([1, 2],
                                        dtypes.float32,
                                        var_name="dup")

# ==================================================
# Occurrences: Lines 228-229 (2 instances)

val1 = gen_state_ops.destroy_temporary_variable(var, var_name="dup")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
# Occurrences: Lines 354-359 (3 instances)

rnd_par = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]])

# ==================================================
# Occurrences: Lines 371-379 (3 instances)

rnd_par = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]])

# ==================================================
# Occurrences: Lines 391-396 (3 instances)

rnd_par = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]])

# ==================================================
# Occurrences: Lines 505-506 (2 instances)

slice1 = _IotaInitializer([4, 5])

# ==================================================
# Occurrences: Lines 569-572 (2 instances)

ops_before_read = session.graph.get_operations()

# ==================================================
# Occurrences: Lines 592-595 (2 instances)

ops_before_concat = session.graph.get_operations()

# ==================================================
# Line: 610

save_graph = ops.Graph()

# ==================================================
# Line: 623

save_graph.get_collection_ref("partvar").append(v0)

# ==================================================
# Occurrences: Lines 630-635 (2 instances)

restore_graph = ops.Graph()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
# Occurrences: Lines 81-82 (2 instances)

v = vs.get_variable("v", [1])

# ==================================================
# Occurrences: Lines 97-98 (2 instances)

v = vs.get_variable("v", [1])

# ==================================================
# Occurrences: Lines 307-315 (3 instances)

v = variable_scope.get_variable("v", [])

# ==================================================
# Line: 322

v2_identity_device = variable_scope.get_variable("v", [])

# ==================================================
# Occurrences: Lines 328-331 (2 instances)

v_live = variable_scope.get_variable("v", [])

# ==================================================
# Occurrences: Lines 349-351 (2 instances)

v = variable_scope.get_variable("v", [])

# ==================================================
# Line: 367

losses = ops.get_collection(ops.GraphKeys.REGULARIZATION_LOSSES)

# ==================================================
# Occurrences: Lines 376-378 (2 instances)

v = variable_scope.get_variable("v",
                                [])  # "v" is already there, reused

# ==================================================
# Occurrences: Lines 639-643 (4 instances)

_ = state_ops.assign(variable_scope.get_variable("var", []), x)

# ==================================================
# Occurrences: Lines 757-781 (7 instances)

va = variable_scope.get_variable("v", [1])

# ==================================================
# Line: 787

variable_scope.get_variable("v", [1])

# ==================================================
# Occurrences: Lines 1147-1153 (4 instances)

_ = variable_scope.get_variable("testGetCollection_a", [])

# ==================================================
# Occurrences: Lines 1166-1168 (2 instances)

_ = variable_scope.get_variable("testGetCollection_a", [])

# ==================================================
# Occurrences: Lines 1340-1341 (4 instances)

g1 = ops.Graph()

# ==================================================
# Occurrences: Lines 1413-1415 (2 instances)

v_concat = variable_scope.get_variable("name0", shape=(3, 1, 1))

# ==================================================
# Occurrences: Lines 1432-1433 (2 instances)

v1 = variable_scope.get_variable("name0", shape=(3, 1, 1))

# ==================================================
# Occurrences: Lines 1519-1526 (4 instances)

v = variable_scope.get_variable("v", [1])

# ==================================================
# Occurrences: Lines 1573-1575 (2 instances)

v = variable_scope.get_variable("v", [1])

# ==================================================
# Occurrences: Lines 1705-1707 (2 instances)

scope = variable_scope.variable_creator_scope(creator)

# ==================================================
# Line: 1751

partition_info = variable_scope._PartitionInfo(
    full_shape=[9, 3], var_offset=[4, 0])

# ==================================================
# Line: 1772

partition_info = variable_scope._PartitionInfo(
    full_shape=[9, 3], var_offset=[4, 0])

# ==================================================
# Occurrences: Lines 1787-1787 (2 instances)

v = variable_scope.get_variable("v", [])

# ==================================================
# Occurrences: Lines 1793-1793 (2 instances)

variable_scope.get_variable("v", [])

# ==================================================
# Occurrences: Lines 1817-1817 (2 instances)

v = variable_scope.get_variable("v", [])

# ==================================================
# Occurrences: Lines 1823-1823 (2 instances)

variable_scope.get_variable("v", [])

# ==================================================
# Occurrences: Lines 1857-1862 (4 instances)

v = variable_scope.get_variable("v", [])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
# Line: 259

init_value = np.ones((4, 4, 4))

# ==================================================
# Line: 278

copied_variable.assign(4 * np.ones((4, 4, 4)))

# ==================================================
# Occurrences: Lines 399-406 (2 instances)

first_read = resource_variable_ops.read_variable_op(
    handle, dtype=dtypes.int32)

# ==================================================
# Occurrences: Lines 607-611 (2 instances)

meta_graph_def = saver.export_meta_graph(graph=graph)

# ==================================================
# Line: 1033

v = resource_variable_ops.ResourceVariable(variable_def=v_def)

# ==================================================
# Line: 1045

v = resource_variable_ops.ResourceVariable(variable_def=v_def)

# ==================================================
# Line: 1093

value = self.evaluate(value_op)

# ==================================================
# Line: 1099

value = self.evaluate(value_op)

# ==================================================
# Line: 1266

v = resource_variable_ops.ResourceVariable(
    2.0, caching_device="/job:localhost")

# ==================================================
# Line: 1273

w = resource_variable_ops.ResourceVariable(
    2.0, caching_device="/job:localhost")

# ==================================================
# Line: 1534

v = resource_variable_ops.ResourceVariable(array_ops.zeros([1024]))

# ==================================================
# Line: 1541

v2 = resource_variable_ops.ResourceVariable(array_ops.zeros([1024]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/timeline.py
# Occurrences: Lines 581-583 (2 instances)

device_pid = self._alloc_pid()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/timeline_test.py
# Occurrences: Lines 71-80 (4 instances)

tl = timeline.Timeline(step_stats)

# ==================================================
# Occurrences: Lines 104-113 (4 instances)

tl = timeline.Timeline(step_stats)

# ==================================================
# Occurrences: Lines 185-194 (4 instances)

tl = timeline.Timeline(step_stats)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/session.py
# Line: 1305

results = fetch_handler.build_results(self, results)

# ==================================================
# Line: 1348

return fetch_handler.build_results(self, results)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
# Occurrences: Lines 44-45 (2 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 59-60 (2 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 87-88 (2 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 103-104 (2 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 131-132 (2 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 174-175 (2 instances)

server1 = server_lib.Server.create_local_server(config=server_config)

# ==================================================
# Occurrences: Lines 205-206 (2 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 240-243 (4 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Line: 249

cluster_def2 = cluster_pb2.ClusterDef()

# ==================================================
# Line: 263

init1 = variables.global_variables_initializer()

# ==================================================
# Line: 270

init2 = variables.global_variables_initializer()

# ==================================================
# Occurrences: Lines 301-304 (4 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Line: 310

cluster_def2 = cluster_pb2.ClusterDef()

# ==================================================
# Occurrences: Lines 353-355 (3 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 367-378 (6 instances)

feed1 = array_ops.placeholder(dtypes.float32, shape=(2))

# ==================================================
# Occurrences: Lines 421-422 (2 instances)

sess1 = session.Session(server.target, config=config)

# ==================================================
# Line: 446

sess3 = session.Session(server.target, config=config)

# ==================================================
# Occurrences: Lines 468-469 (2 instances)

sess1 = session.Session(server.target, config=config)

# ==================================================
# Line: 487

sess3 = session.Session(server.target, config=config)

# ==================================================
# Line: 505

var1 = variables.Variable(array_ops.zeros([2]), name='var')

# ==================================================
# Line: 511

var2 = variables.Variable(array_ops.zeros([2]), name='var')

# ==================================================
# Occurrences: Lines 534-535 (2 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 545-548 (3 instances)

a = array_ops.placeholder(dtypes.float32, shape=[])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/session_partial_run_test.py
# Occurrences: Lines 32-38 (4 instances)

a = array_ops.placeholder(dtypes.float32, shape=[])

# ==================================================
# Line: 46

h2 = sess.partial_run_setup([r1, r2], [a, b, c])

# ==================================================
# Occurrences: Lines 54-56 (3 instances)

a = array_ops.placeholder(dtypes.float32, shape=[])

# ==================================================
# Occurrences: Lines 65-67 (3 instances)

a = array_ops.placeholder(dtypes.float32, shape=[])

# ==================================================
# Occurrences: Lines 121-123 (3 instances)

a = array_ops.placeholder(dtypes.float32, shape=[])

# ==================================================
# Occurrences: Lines 132-134 (3 instances)

a = array_ops.placeholder(dtypes.float32, shape=[])

# ==================================================
# Occurrences: Lines 144-146 (3 instances)

a = array_ops.placeholder(dtypes.float32, shape=[])

# ==================================================
# Occurrences: Lines 157-159 (3 instances)

a = array_ops.placeholder(dtypes.float32, shape=[])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/session_benchmark.py
# Occurrences: Lines 56-58 (4 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 84-86 (4 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 113-115 (4 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 139-141 (4 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 166-168 (4 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/session_test.py
# Occurrences: Lines 147-160 (5 instances)

pool = config_pb.session_inter_op_thread_pool.add()

# ==================================================
# Occurrences: Lines 185-186 (2 instances)

a = array_ops.placeholder(dtypes.float32, shape=[])

# ==================================================
# Occurrences: Lines 326-327 (2 instances)

field1 = attr.ib()

# ==================================================
# Occurrences: Lines 355-356 (2 instances)

field0 = attr.ib()

# ==================================================
# Line: 650

sp_out = s.run(sp)

# ==================================================
# Occurrences: Lines 656-671 (4 instances)

sp_out = s.run(sp)

# ==================================================
# Line: 691

sp_out = s.run([[[sp]], sp])

# ==================================================
# Line: 701

sp_out = s.run([[[sp]], sp])

# ==================================================
# Line: 858

ind_out = s.run(ind)

# ==================================================
# Occurrences: Lines 864-879 (4 instances)

ind_out = s.run(ind)

# ==================================================
# Line: 930

ind_out = s.run(ind)

# ==================================================
# Occurrences: Lines 936-951 (4 instances)

ind_out = s.run(ind)

# ==================================================
# Line: 1007

v_val = self.evaluate(v)

# ==================================================
# Occurrences: Lines 1015-1018 (2 instances)

v_val = self.evaluate(v)

# ==================================================
# Line: 1060

v_val = self.evaluate(v)

# ==================================================
# Occurrences: Lines 1066-1070 (2 instances)

v_val = self.evaluate(v)

# ==================================================
# Line: 1083

v_val = self.evaluate(v)

# ==================================================
# Occurrences: Lines 1090-1093 (2 instances)

v_val = self.evaluate(v)

# ==================================================
# Line: 1112

v_val = self.evaluate(v)

# ==================================================
# Occurrences: Lines 1119-1122 (2 instances)

v_val = self.evaluate(v)

# ==================================================
# Occurrences: Lines 1129-1130 (2 instances)

constructed_events = [threading.Event() for _ in range(10)]

# ==================================================
# Occurrences: Lines 1168-1170 (4 instances)

x = array_ops.placeholder(dtype=dtypes.float32)

# ==================================================
# Line: 1231

x = array_ops.zeros([2])

# ==================================================
# Occurrences: Lines 1243-1244 (3 instances)

z = (((array_ops.zeros([2]),),), array_ops.zeros([2]),

# ==================================================
# Occurrences: Lines 1310-1312 (2 instances)

c_1 = constant_op.constant(5.0)

# ==================================================
# Occurrences: Lines 1338-1350 (4 instances)

sess = session.InteractiveSession()

# ==================================================
# Occurrences: Lines 1377-1379 (2 instances)

a = constant_op.constant(1.0, shape=[1, 2])

# ==================================================
# Occurrences: Lines 1399-1401 (2 instances)

_ = constant_op.constant(1.0, shape=[1, 2])

# ==================================================
# Occurrences: Lines 1447-1451 (15 instances)

np_array = np.sqrt(np_array.astype(np_dtype))

# ==================================================
# Occurrences: Lines 1817-1821 (2 instances)

sess1 = session.Session()

# ==================================================
# Occurrences: Lines 1831-1832 (2 instances)

sess1 = session.InteractiveSession()

# ==================================================
# Occurrences: Lines 1839-1844 (2 instances)

sess = session.Session()

# ==================================================
# Occurrences: Lines 1949-1950 (2 instances)

a = constant_op.constant(1)

# ==================================================
# Occurrences: Lines 1960-1961 (2 instances)

a = constant_op.constant(1)

# ==================================================
# Occurrences: Lines 1990-1990 (2 instances)

c, d = self.evaluate(fn(constant_op.constant(1), constant_op.constant(2)))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/session_list_devices_test.py
# Occurrences: Lines 61-62 (2 instances)

server1 = server_lib.Server.create_local_server()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/structured_function.py
# Line: 157

nested_args = structure.from_compatible_tensor_list(
    self._input_structure, args)

# ==================================================
# Occurrences: Lines 178-179 (2 instances)

ret = wrapper_helper(*args)

# ==================================================
# Occurrences: Lines 186-187 (3 instances)

ret = wrapper_helper(*args)

# ==================================================
# Line: 204

nested_args = structure.from_compatible_tensor_list(
    self._input_structure, args)

# ==================================================
# Occurrences: Lines 211-211 (2 instances)

ret = structure.to_tensor_list(self._output_structure, ret)

# ==================================================
# Occurrences: Lines 231-232 (2 instances)

ret = wrapper_helper(*args)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/dataset_autograph.py
# Line: 62

init_vars = get_state()

# ==================================================
# Line: 87

new_loop_vars = get_state()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/iterator_ops.py
# Line: 767

ret = gen_dataset_ops.iterator_get_next(
    self._iterator_resource,
    output_types=self._flat_output_types,
    output_shapes=self._flat_output_shapes)

# ==================================================
# Line: 776

ret = gen_dataset_ops.iterator_get_next(
    self._iterator_resource,
    output_types=self._flat_output_types,
    output_shapes=self._flat_output_shapes)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/range_op.py
# Occurrences: Lines 47-54 (6 instances)

self._step = self._build_tensor(1, "step")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/nest_test.py
# Line: 59

nest.pack_sequence_as(structure, flat), (("a", "b"), "c",

# ==================================================
# Line: 65

restructured_from_flat = nest.pack_sequence_as(structure, flat)

# ==================================================
# Occurrences: Lines 432-433 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Line: 439

input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)

# ==================================================
# Occurrences: Lines 450-451 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 457-458 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 465-466 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 472-473 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 481-482 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 489-490 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 501-502 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 508-509 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 518-519 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 525-526 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# Occurrences: Lines 532-533 (2 instances)

flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/options_test.py
# Occurrences: Lines 68-73 (2 instances)

merged_options = options.merge_options(options1, options2)

# ==================================================
# Occurrences: Lines 80-90 (8 instances)

merged_options = options.merge_options(options1, options2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/traverse_test.py
# Occurrences: Lines 61-62 (2 instances)

ds1 = dataset_ops.Dataset.range(10)

# ==================================================
# Occurrences: Lines 71-72 (2 instances)

ds1 = dataset_ops.Dataset.range(10)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/structure.py
# Occurrences: Lines 219-221 (2 instances)

if sum(flat_spec_lengths) != len(tensor_list):

# ==================================================
# Occurrences: Lines 472-474 (2 instances)

ctor = lambda items: type(element)(element.default_factory, items)

# ==================================================
# Line: 484

element_type = type(element)

# ==================================================
# Line: 493

return type(element)(*[

# ==================================================
# Occurrences: Lines 512-516 (2 instances)

3, "Failed to convert %r to tensor: %s" % (type(element).__name__, e))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/options.py
# Line: 142

result_type = type(options_list[0])

# ==================================================
# Occurrences: Lines 153-156 (3 instances)

"option of type {} which does not.".format(type(options_list[0])))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/sparse_test.py
# Line: 317

classes = sparse.get_classes(test_case)

# ==================================================
# Line: 323

sparse.get_classes(test_case))

# ==================================================
# Line: 333

classes = sparse.get_classes(test_case)

# ==================================================
# Line: 339

sparse.get_classes(test_case))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
# Occurrences: Lines 58-65 (6 instances)

ping = data_flow_ops.FIFOQueue(capacity=2, dtypes=dtypes.int64)

# ==================================================
# Occurrences: Lines 160-164 (2 instances)

elem_on_1, elem_on_2 = multi_device_iterator.get_next()

# ==================================================
# Occurrences: Lines 176-181 (2 instances)

elem_on_0, elem_on_1, elem_on_2 = multi_device_iterator.get_next()

# ==================================================
# Occurrences: Lines 194-199 (2 instances)

elements = multi_device_iterator.get_next()

# ==================================================
# Line: 212

elem_on_1, elem_on_2 = multi_device_iterator.get_next()

# ==================================================
# Line: 218

elem_on_1, elem_on_2 = multi_device_iterator.get_next()

# ==================================================
# Occurrences: Lines 230-248 (10 instances)

elem_on_1, elem_on_2 = multi_device_iterator.get_next_as_optional()

# ==================================================
# Occurrences: Lines 271-272 (2 instances)

dataset1 = dataset_ops.Dataset.range(1000)

# ==================================================
# Occurrences: Lines 284-285 (2 instances)

dataset1 = dataset_ops.Dataset.range(1000)

# ==================================================
# Occurrences: Lines 311-315 (2 instances)

elem_on_1, elem_on_2 = multi_device_iterator.get_next()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
# Line: 90

get_next = self.getNext(dataset_fn(buffer_size=100, seed=37))

# ==================================================
# Occurrences: Lines 98-101 (3 instances)

self.assertAllEqual(sorted(unshuffled_elements), sorted(shuffled_elements))

# ==================================================
# Line: 120

sorted(shuffled_elements), sorted(reshuffled_elements_different_seed))

# ==================================================
# Line: 132

sorted(unshuffled_elements), sorted(reshuffled_elements_small_buffer))

# ==================================================
# Line: 145

get_next = iterator.get_next()

# ==================================================
# Line: 157

get_next = iterator.get_next()

# ==================================================
# Occurrences: Lines 273-279 (7 instances)

dataset = dataset_ops.Dataset.range(10).shuffle(10, seed=1)

# ==================================================
# Occurrences: Lines 399-400 (2 instances)

first_epoch = self.getDatasetOutput(dataset)

# ==================================================
# Occurrences: Lines 675-676 (2 instances)

shuffled_dataset = dataset.shuffle(buffer_size=100, seed=5)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py
# Line: 102

get_next = self.getNext(dataset)

# ==================================================
# Line: 115

get_next = self.getNext(dataset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
# Line: 372

next_elem = iterator_ops.get_next_as_optional(iterator)

# ==================================================
# Occurrences: Lines 378-389 (6 instances)

self.assertTrue(next_elem.has_value())

# ==================================================
# Occurrences: Lines 397-398 (2 instances)

elem_has_value_t = next_elem.has_value()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
# Occurrences: Lines 76-82 (3 instances)

results = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 89-95 (3 instances)

results = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 118-125 (3 instances)

result1, (result2, result3) = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 157-158 (2 instances)

x = attr.ib()

# ==================================================
# Occurrences: Lines 376-377 (2 instances)

x = attr.ib()

# ==================================================
# Occurrences: Lines 399-401 (2 instances)

first_dataset = dataset_ops.Dataset.range(dataset_range)

# ==================================================
# Occurrences: Lines 457-460 (3 instances)

expected = [(x * 2, x) for x in range(min(dataset_ranges))]

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/ragged_batch_test.py
# Line: 117

rows = [nest.map_structure(_to_list, self.evaluate(get_next()))

# ==================================================
# Line: 128

result = self.evaluate(get_next())

# ==================================================
# Line: 136

self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
# Occurrences: Lines 147-151 (4 instances)

batch, = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 188-199 (20 instances)

sorted(generated_batch_sizes[l]), sorted(expected_batch_sizes[l]),

# ==================================================
# Occurrences: Lines 243-246 (4 instances)

batch, = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 297-300 (2 instances)

batch, = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 338-341 (2 instances)

batch, = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
# Occurrences: Lines 166-167 (2 instances)

x = attr.ib()

# ==================================================
# Occurrences: Lines 219-220 (2 instances)

get_next = self.getNext(dataset)

# ==================================================
# Occurrences: Lines 232-233 (2 instances)

get_next = self.getNext(dataset)

# ==================================================
# Occurrences: Lines 307-312 (2 instances)

var_0 = resource_variable_ops.ResourceVariable(initial_value=1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
# Occurrences: Lines 101-110 (5 instances)

sess = random.choice([sess1, sess2])

# ==================================================
# Occurrences: Lines 491-495 (2 instances)

dataset = dataset.prefetch(buffer_size=dataset_ops.AUTOTUNE)

# ==================================================
# Occurrences: Lines 545-549 (4 instances)

dataset = dataset.prefetch(buffer_size=dataset_ops.AUTOTUNE)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
# Occurrences: Lines 101-102 (2 instances)

which_bucket_even, bucketed_values_even = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 167-168 (2 instances)

which_bucket0, bucketed_values_even0 = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
# Occurrences: Lines 83-87 (4 instances)

result = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
# Line: 77

result = self.evaluate(get_next())

# ==================================================
# Line: 86

result = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 95-97 (2 instances)

self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
# Occurrences: Lines 81-85 (2 instances)

elem = self.evaluate(next_fn())

# ==================================================
# Occurrences: Lines 107-107 (3 instances)

run_dirlist = sorted(os.listdir(run_dir))

# ==================================================
# Occurrences: Lines 116-116 (3 instances)

run_dirlist = sorted(os.listdir(run_dir))

# ==================================================
# Line: 139

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 149

dataset2 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Occurrences: Lines 163-168 (2 instances)

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 182

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 193

dataset2 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 208

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 224

dataset2 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Occurrences: Lines 254-255 (2 instances)

dataset = dataset_ops.Dataset.range(0)

# ==================================================
# Occurrences: Lines 263-264 (2 instances)

dataset2 = dataset_ops.Dataset.range(0)

# ==================================================
# Occurrences: Lines 296-299 (2 instances)

dataset1 = dataset_ops.Dataset.range(1000)

# ==================================================
# Line: 311

dataset1 = dataset_ops.Dataset.range(1000)

# ==================================================
# Line: 317

dataset2 = dataset_ops.Dataset.range(1000)

# ==================================================
# Occurrences: Lines 377-379 (2 instances)

dataset1 = make_dataset()

# ==================================================
# Occurrences: Lines 494-498 (2 instances)

dataset = dataset.apply(snapshot.legacy_snapshot(tmpdir))

# ==================================================
# Occurrences: Lines 507-511 (2 instances)

dataset1 = dataset_ops.Dataset.range(1000)

# ==================================================
# Line: 650

dataset = dataset_ops.Dataset.range(10)

# ==================================================
# Line: 663

dataset = dataset_ops.Dataset.range(10)

# ==================================================
# Line: 710

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 718

dataset2 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 735

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 743

dataset2 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 753

dataset3 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 771

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 779

dataset2 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 788

dataset3 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 821

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 835

dataset2 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 868

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 881

dataset2 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Occurrences: Lines 890-903 (8 instances)

dataset1 = dataset_ops.Dataset.range(0, 100)

# ==================================================
# Line: 912

dataset1 = dataset_ops.Dataset.range(1000)

# ==================================================
# Line: 928

dataset2 = dataset_ops.Dataset.range(1000)

# ==================================================
# Line: 941

dataset1 = dataset_ops.Dataset.range(1000)

# ==================================================
# Line: 951

dataset2 = dataset_ops.Dataset.range(1000)

# ==================================================
# Line: 998

dataset = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 1005

dataset2 = core_readers._TFRecordDataset(filenames)

# ==================================================
# Line: 1015

dataset3 = core_readers._TFRecordDataset(filenames)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
# Occurrences: Lines 63-67 (2 instances)

results = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 190-195 (2 instances)

results = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 211-215 (2 instances)

results = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 280-285 (2 instances)

results = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
# Line: 59

result = self.evaluate(get_next())

# ==================================================
# Line: 70

result = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 81-83 (2 instances)

self.evaluate(get_next())

# ==================================================
# Line: 172

result = self.evaluate(get_next())

# ==================================================
# Line: 191

self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
# Occurrences: Lines 59-61 (2 instances)

options1 = options_lib.Options()

# ==================================================
# Occurrences: Lines 73-75 (2 instances)

options1 = options_lib.Options()

# ==================================================
# Occurrences: Lines 84-86 (2 instances)

options1 = options_lib.Options()

# ==================================================
# Occurrences: Lines 97-99 (2 instances)

options1 = options_lib.Options()

# ==================================================
# Occurrences: Lines 110-111 (2 instances)

options1 = options_lib.Options()

# ==================================================
# Occurrences: Lines 122-124 (2 instances)

options1 = options_lib.Options()

# ==================================================
# Line: 144

options = options_lib.Options()

# ==================================================
# Line: 173

result = options_lib.Options()

# ==================================================
# Occurrences: Lines 180-182 (2 instances)

options = options_lib.Options()

# ==================================================
# Occurrences: Lines 188-192 (2 instances)

pb = dataset_options_pb2.Options()

# ==================================================
# Occurrences: Lines 215-220 (2 instances)

options = options_lib.Options()

# ==================================================
# Occurrences: Lines 227-231 (2 instances)

options = options_lib.Options()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
# Occurrences: Lines 120-122 (2 instances)

features, label = self.evaluate(outputs())

# ==================================================
# Line: 143

open_iterators.append(pending_iterators.pop(0))

# ==================================================
# Line: 154

open_iterators[i] = pending_iterators.pop(0)

# ==================================================
# Line: 253

open_iterators.append(pending_iterators.pop(0))

# ==================================================
# Line: 264

open_iterators[i] = pending_iterators.pop(0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/dataset_spec_test.py
# Occurrences: Lines 56-61 (2 instances)

trace_type_1 = dataset_ops.DatasetSpec(
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.int32),
    [5])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
# Occurrences: Lines 84-86 (2 instances)

data = data.unbatch()

# ==================================================
# Occurrences: Lines 101-103 (2 instances)

data = data.unbatch()

# ==================================================
# Occurrences: Lines 115-118 (2 instances)

data = data.unbatch()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
# Line: 214

get_next = self.getNext(
    dataset, requires_initialization=requires_initialization)

# ==================================================
# Line: 224

get_next = self.getNext(
    dataset, requires_initialization=requires_initialization)

# ==================================================
# Occurrences: Lines 259-261 (4 instances)

self.evaluate(next2())

# ==================================================
# Line: 407

actual = self.getDatasetOutput(dataset)

# ==================================================
# Line: 417

actual = self.getDatasetOutput(dataset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
# Occurrences: Lines 546-550 (4 instances)

for key1, key2 in zip(sorted(expected), sorted(actual)):

# ==================================================
# Occurrences: Lines 581-583 (2 instances)

get_next = sparse_tensor.SparseTensor(*iterator.get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
# Occurrences: Lines 37-43 (3 instances)

tmpdir = self.get_temp_dir()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/fingerprint_test.py
# Occurrences: Lines 93-94 (2 instances)

fingerprint1 = self.evaluate(dataset_fn().fingerprint())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
# Occurrences: Lines 213-229 (5 instances)

dataset_device = test_ops.device_placement_op()

# ==================================================
# Occurrences: Lines 242-258 (5 instances)

dataset_device = test_ops.device_placement_op()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
# Occurrences: Lines 115-119 (2 instances)

dataset_ops.Dataset.from_tensor_slices(components).cache(
    self.cache_prefix))

# ==================================================
# Occurrences: Lines 137-141 (2 instances)

dataset_ops.Dataset.from_tensor_slices(components).cache(
    self.cache_prefix))

# ==================================================
# Occurrences: Lines 193-194 (2 instances)

first_order = self.getDatasetOutput(dataset)

# ==================================================
# Occurrences: Lines 384-385 (2 instances)

it1 = iter(dataset)

# ==================================================
# Line: 399

it = iter(dataset)

# ==================================================
# Line: 405

it = iter(dataset)

# ==================================================
# Line: 607

outputs = self.gen_outputs(
    ds_fn, [], self.num_outputs, verify_exhausted=False)

# ==================================================
# Line: 615

outputs = self.gen_outputs(
    ds_fn, [], self.num_outputs, verify_exhausted=False)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
# Line: 57

result = self.evaluate(get_next())

# ==================================================
# Line: 66

self.evaluate(get_next())

# ==================================================
# Line: 88

result = self.evaluate(get_next())

# ==================================================
# Line: 97

self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 211-212 (2 instances)

input_dataset = dataset_ops.Dataset.from_tensor_slices([])

# ==================================================
# Occurrences: Lines 423-429 (9 instances)

dataset_ranges[0], sum(dataset_ranges[:2])

# ==================================================
# Line: 448

num_outputs=sum(dataset_ranges),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
# Occurrences: Lines 233-235 (2 instances)

input_dataset = dataset_ops.Dataset.range(0)

# ==================================================
# Line: 490

dataset_ops.get_legacy_output_shapes(dataset))

# ==================================================
# Line: 497

dataset_ops.get_legacy_output_shapes(dataset))

# ==================================================
# Line: 504

dataset_ops.get_legacy_output_shapes(dataset))

# ==================================================
# Line: 511

dataset_ops.get_legacy_output_shapes(dataset))

# ==================================================
# Line: 518

dataset_ops.get_legacy_output_shapes(dataset))

# ==================================================
# Line: 525

dataset_ops.get_legacy_output_shapes(dataset))

# ==================================================
# Line: 533

dataset_ops.get_legacy_output_shapes(dataset))

# ==================================================
# Line: 539

dataset_output_shapes = dataset_ops.get_legacy_output_shapes(dataset)

# ==================================================
# Line: 558

dataset_ops.get_legacy_output_shapes(dataset))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py
# Line: 55

dense_val, sparse_val = self.evaluate(dataset.get_single_element())

# ==================================================
# Line: 62

self.evaluate(dataset.get_single_element())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
# Occurrences: Lines 42-44 (2 instances)

output_1 = self.getDatasetOutput(ds, requires_initialization=True)

# ==================================================
# Occurrences: Lines 63-64 (2 instances)

first_epoch = self.getDatasetOutput(dataset, requires_initialization=True)

# ==================================================
# Occurrences: Lines 83-84 (2 instances)

first_epoch = self.getDatasetOutput(dataset)

# ==================================================
# Occurrences: Lines 127-128 (2 instances)

first_epoch = self.getDatasetOutput(dataset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
# Line: 76

open_iterators.append(all_iterators.pop(0))

# ==================================================
# Line: 85

open_iterators[i] = all_iterators.pop(0)

# ==================================================
# Occurrences: Lines 313-314 (2 instances)

dataset = dataset.interleave(interleave_fn, cycle_length=5)

# ==================================================
# Occurrences: Lines 539-548 (4 instances)

it = dataset.as_numpy_iterator()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
# Occurrences: Lines 101-105 (2 instances)

result = sess.run(get_next)

# ==================================================
# Occurrences: Lines 128-132 (2 instances)

result = sess.run(get_next)

# ==================================================
# Occurrences: Lines 165-169 (4 instances)

result = sess.run(get_next)

# ==================================================
# Occurrences: Lines 264-272 (3 instances)

get_next = iterator.get_next()

# ==================================================
# Occurrences: Lines 286-294 (3 instances)

get_next = iterator.get_next()

# ==================================================
# Line: 364

dataset_1 = dataset_ops.Dataset.from_generator(
    g, output_types=dtypes.int64)

# ==================================================
# Line: 372

dataset_2 = dataset_ops.Dataset.from_generator(
    g, output_types=dtypes.int64)

# ==================================================
# Occurrences: Lines 577-581 (2 instances)

handle_with_name = one_shot_iterator.string_handle(name="foo")

# ==================================================
# Line: 652

elem = sess.run(
    remote_op,
    feed_dict={
        target_placeholder: "/job:localhost/replica:0/task:0/cpu:1"
    })

# ==================================================
# Occurrences: Lines 665-695 (8 instances)

elem = sess.run(
    remote_op,
    feed_dict={
        target_placeholder: "/job:localhost/replica:0/task:0/cpu:1"
    })

# ==================================================
# Occurrences: Lines 770-793 (4 instances)

elem = sess.run(
    remote_op,
    feed_dict={
        target_placeholder: "/job:localhost/replica:0/task:0/cpu:0"
    })

# ==================================================
# Occurrences: Lines 1079-1081 (2 instances)

it = ds.as_numpy_iterator()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# Occurrences: Lines 224-228 (2 instances)

result = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 307-311 (2 instances)

result = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 518-521 (2 instances)

queue = data_flow_ops.FIFOQueue(
    200, dtypes.int64, shapes=[], shared_name="shared_queue")

# ==================================================
# Line: 544

get_next = self.getNext(dataset, requires_initialization=True)

# ==================================================
# Line: 552

get_next = self.getNext(dataset, requires_initialization=True)

# ==================================================
# Line: 568

random_values = self.evaluate(get_next())

# ==================================================
# Line: 574

if np.any(random_values != self.evaluate(get_next())):

# ==================================================
# Occurrences: Lines 771-772 (2 instances)

label = attr.ib()

# ==================================================
# Occurrences: Lines 784-788 (2 instances)

data = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
# Line: 85

elem = sess.run(remote_op, feed_dict={target_placeholder: device1})

# ==================================================
# Occurrences: Lines 92-95 (2 instances)

elem = sess.run(remote_op, feed_dict={target_placeholder: device1})

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
# Occurrences: Lines 142-146 (2 instances)

val0, val1 = self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 212-216 (4 instances)

next_val = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
# Line: 124

iterator = ds.as_numpy_iterator()

# ==================================================
# Line: 135

restore_iter = ds.as_numpy_iterator()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
# Occurrences: Lines 180-181 (2 instances)

len_dataset = self.evaluate(dataset.cardinality())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
# Occurrences: Lines 153-155 (2 instances)

first_iterator = iter(readers.TextLineDataset(filename))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
# Occurrences: Lines 216-220 (2 instances)

(longer_vector_val, larger_rank_val), _ = self.evaluate(next_element())

# ==================================================
# Occurrences: Lines 274-275 (2 instances)

weights = variables.Variable(initial_value=array_ops.zeros((1000, 1000)))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/sparse_batch_test.py
# Line: 38

results = self.evaluate(get_next())

# ==================================================
# Line: 50

self.evaluate(get_next())

# ==================================================
# Line: 61

results = self.evaluate(get_next())

# ==================================================
# Line: 77

self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/from_sparse_tensor_slices_test.py
# Line: 59

results = sess.run(get_next)

# ==================================================
# Line: 66

sess.run(get_next)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
# Occurrences: Lines 210-211 (2 instances)

first_epoch = self.getDatasetOutput(sample_dataset)

# ==================================================
# Occurrences: Lines 265-266 (2 instances)

first_epoch = self.getDatasetOutput(sample_dataset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
# Line: 94

result = self.evaluate(get_next())

# ==================================================
# Line: 100

result = self.evaluate(get_next())

# ==================================================
# Line: 107

result = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
# Line: 89

init_op, get_next, save_op, _ = _build_graph(start, stop)

# ==================================================
# Line: 98

init_op, get_next, _, restore_op = _build_graph(start, stop)

# ==================================================
# Line: 109

init_op, get_next, save_op, restore_op = _build_graph(start, stop)

# ==================================================
# Line: 143

init_op, get_next, save_op, _ = _build_graph(start, stop)

# ==================================================
# Line: 152

init_op, get_next, _, restore_op = _build_graph(start, stop)

# ==================================================
# Line: 179

init_op, get_next, save_op, _ = _build_graph(start, stop)

# ==================================================
# Line: 188

init_op, get_next, save_op, restore_op = _build_graph(start, stop)

# ==================================================
# Line: 198

init_op, get_next, save_op, restore_op = _build_graph(start, stop)

# ==================================================
# Line: 225

init_op, get_next, save_op, restore_op = _build_graph(
    start, stop, num_epochs)

# ==================================================
# Line: 243

init_op, get_next, _, restore_op = _build_graph(start, stop, num_epochs)

# ==================================================
# Line: 271

init_op, get_next, save_op, restore_op = _build_graph(
    start, stop, num_epochs)

# ==================================================
# Line: 289

init_op, get_next, _, restore_op = _build_graph(start, stop, num_epochs)

# ==================================================
# Occurrences: Lines 330-332 (2 instances)

iterator_1 = iter(dataset)

# ==================================================
# Occurrences: Lines 369-373 (2 instances)

save_path = checkpoint.save(checkpoint_prefix, options=ckpt_options)

# ==================================================
# Occurrences: Lines 419-422 (3 instances)

iterator = iter(dataset)

# ==================================================
# Occurrences: Lines 430-433 (3 instances)

iterator = iter(dataset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
# Occurrences: Lines 996-996 (2 instances)

dataset_id_val = tensor_util.constant_value(dataset_id)

# ==================================================
# Occurrences: Lines 1015-1015 (2 instances)

dataset_id_val = tensor_util.constant_value(dataset_id)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/ops/readers.py
# Line: 167

column_names = next(csv.reader(f, **csv_kwargs))

# ==================================================
# Line: 175

if next(csv.reader(f, **csv_kwargs)) != column_names:

# ==================================================
# Occurrences: Lines 315-319 (2 instances)

dataset = dataset.batch(batch_size, drop_remainder=drop_final_batch)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/ops/shuffle_ops.py
# Occurrences: Lines 153-155 (2 instances)

offsets = np.int64([])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
# Occurrences: Lines 154-158 (2 instances)

worker1 = server_lib.WorkerServer(  # pylint: disable=unused-variable
    server_lib.WorkerConfig(dispatcher._address))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
# Occurrences: Lines 51-52 (2 instances)

keys = dataset_ops.Dataset.range(100)

# ==================================================
# Occurrences: Lines 64-65 (2 instances)

keys = dataset_ops.Dataset.range(100)

# ==================================================
# Occurrences: Lines 119-120 (2 instances)

keys = dataset_ops.Dataset.range(100)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
# Occurrences: Lines 129-133 (4 instances)

x, y = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
# Occurrences: Lines 89-92 (2 instances)

dataset = readers.CsvDataset(filenames, **kwargs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
# Line: 96

open_iterators.append(all_iterators.pop(0))

# ==================================================
# Line: 105

open_iterators[i] = all_iterators.pop(0)

# ==================================================
# Occurrences: Lines 285-287 (4 instances)

self.evaluate(next_element())

# ==================================================
# Line: 293

self.evaluate(next_element())

# ==================================================
# Occurrences: Lines 329-331 (4 instances)

self.evaluate(next_element())

# ==================================================
# Line: 337

self.evaluate(next_element())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/global_shuffle_test.py
# Occurrences: Lines 133-134 (2 instances)

first_epoch = self.getDatasetOutput(dataset)

# ==================================================
# Occurrences: Lines 244-246 (4 instances)

expected = next(it)

# ==================================================
# Occurrences: Lines 291-296 (2 instances)

checkpoint = it.save()

# ==================================================
# Occurrences: Lines 304-307 (5 instances)

checkpoint = it.save()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/copy_to_device_test.py
# Occurrences: Lines 233-238 (2 instances)

actual = self.evaluate(next_element)

# ==================================================
# Occurrences: Lines 266-271 (2 instances)

actual = self.evaluate(next_element)

# ==================================================
# Occurrences: Lines 328-333 (2 instances)

x, y, z = self.evaluate(next_element)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_batched_features_dataset_test.py
# Occurrences: Lines 100-104 (2 instances)

actual_batch = self.evaluate(next_element())

# ==================================================
# Occurrences: Lines 114-127 (2 instances)

outputs1 = self.getNext(
    self.make_batch_feature(
        filenames=self._filenames[0],
        num_epochs=num_epochs,
        batch_size=batch_size,
        shuffle=True,
        shuffle_seed=5))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py
# Occurrences: Lines 156-157 (2 instances)

elems1 = array_ops.placeholder(dtypes.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
# Occurrences: Lines 90-94 (4 instances)

result = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_fusion_test.py
# Occurrences: Lines 163-167 (2 instances)

dataset = dataset.map(lambda x: 2 * x,
                      num_parallel_calls=dataset_ops.AUTOTUNE)

# ==================================================
# Occurrences: Lines 193-194 (2 instances)

dataset = dataset.map(f, num_parallel_calls=dataset_ops.AUTOTUNE)

# ==================================================
# Occurrences: Lines 218-220 (2 instances)

dataset = dataset.map(lambda x: x, num_parallel_calls=dataset_ops.AUTOTUNE)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/seq_interleave_prefetch_test.py
# Occurrences: Lines 50-51 (2 instances)

dataset1 = dataset_ops.Dataset.range(num_input_elements)

# ==================================================
# Line: 65

(lambda _: dataset_ops.Dataset.range(num_input_elements)),

# ==================================================
# Occurrences: Lines 74-75 (2 instances)

dataset2 = dataset_ops.Dataset.range(num_input_elements)

# ==================================================
# Line: 89

(lambda _: dataset_ops.Dataset.range(num_input_elements)),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
# Occurrences: Lines 265-266 (2 instances)

a = dataset_ops.Dataset.range(100)

# ==================================================
# Occurrences: Lines 378-379 (2 instances)

cluster_1 = data_service_test_base.TestCluster(num_workers=1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
# Occurrences: Lines 341-342 (2 instances)

ds1 = self.make_distributed_dataset(make_ds(), cluster, job_name="job_name")

# ==================================================
# Occurrences: Lines 370-375 (2 instances)

ds1 = self.make_distributed_range_dataset(
    num_elements, cluster, job_name="job_name"
)

# ==================================================
# Occurrences: Lines 388-394 (2 instances)

ds1 = self.make_distributed_range_dataset(
    num_elements, cluster, job_name="job_name"
)

# ==================================================
# Occurrences: Lines 412-422 (2 instances)

ds1 = ds.apply(
    data_service_ops.distribute(
        data_service_ops.ShardingPolicy.OFF,
        cluster.dispatcher_address(),
        job_name="shared_job"))

# ==================================================
# Occurrences: Lines 521-530 (2 instances)

it2 = iter(
    self.make_distributed_range_dataset(
        num_elements, cluster, job_name="test2"
    )
)

# ==================================================
# Occurrences: Lines 827-831 (2 instances)

ds1 = dataset_ops.Dataset.range(num_elements)

# ==================================================
# Occurrences: Lines 846-850 (2 instances)

ds1 = dataset_ops.Dataset.range(num_elements)

# ==================================================
# Occurrences: Lines 999-1001 (2 instances)

slow = dataset_ops.Dataset.range(1)

# ==================================================
# Occurrences: Lines 1062-1063 (2 instances)

dataset1 = dataset_ops.Dataset.range(10)

# ==================================================
# Occurrences: Lines 1099-1100 (2 instances)

dataset1 = dataset_ops.Dataset.range(10)

# ==================================================
# Occurrences: Lines 1198-1200 (4 instances)

element = self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_test.py
# Occurrences: Lines 50-54 (2 instances)

ds = self.make_coordinated_read_dataset(cluster, num_consumers)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_ft_test.py
# Line: 44

elements = self._get_next(get_next, 100)

# ==================================================
# Line: 53

elements = self._get_next(get_next, 100)

# ==================================================
# Line: 69

elements = self._get_next(get_next, 100)

# ==================================================
# Line: 75

elements = self._get_next(get_next, 100)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/distributed_save_load_test.py
# Occurrences: Lines 232-237 (2 instances)

os.path.join(snapshot_dir.full_path, f"dataset_{i}"),

# ==================================================
# Line: 320

dataset = dataset_ops.Dataset.load(snapshot_dir.full_path, wait=True)

# ==================================================
# Line: 328

dataset = dataset_ops.Dataset.load(snapshot_dir.full_path, wait=True)

# ==================================================
# Line: 344

dataset = dataset_ops.Dataset.load(snapshot_dir.full_path, wait=True)

# ==================================================
# Line: 354

dataset = dataset_ops.Dataset.load(snapshot_dir.full_path, wait=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_device_test.py
# Occurrences: Lines 67-79 (6 instances)

dataset = dataset_ops.Dataset.range(3)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
# Line: 269

self.assertEqual(i, next(iterator).numpy())

# ==================================================
# Line: 277

val = next(iterator).numpy()

# ==================================================
# Line: 285

val = next(iterator).numpy()

# ==================================================
# Line: 298

iterator = iter(ds)

# ==================================================
# Line: 310

next(iter(ds)).numpy()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
# Occurrences: Lines 401-406 (2 instances)

dataset = dataset.prefetch(buffer_size=dataset_ops.AUTOTUNE)

# ==================================================
# Occurrences: Lines 418-423 (2 instances)

dataset1 = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)

# ==================================================
# Occurrences: Lines 444-449 (2 instances)

dataset1 = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
# Occurrences: Lines 336-350 (6 instances)

dataset = self._make_distributed_infinite_range_dataset(
    cluster, job_name="shared_job_name")

# ==================================================
# Occurrences: Lines 362-365 (2 instances)

dataset = self._make_distributed_infinite_range_dataset(
    cluster, job_name="shared_job_name")

# ==================================================
# Occurrences: Lines 371-376 (2 instances)

dataset = self._make_distributed_infinite_range_dataset(
    cluster, job_name="shared_job_name")

# ==================================================
# Line: 392

get_next = self.getNext(dataset)

# ==================================================
# Line: 401

get_next = self.getNext(dataset)

# ==================================================
# Line: 417

get_next = self.getNext(dataset)

# ==================================================
# Line: 426

get_next = self.getNext(dataset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/distributed_save_ft_test.py
# Occurrences: Lines 269-275 (3 instances)

while len(get_streams()) != n:

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
# Line: 62

dataset_id1 = data_service_ops.register_dataset(
    cluster.dispatcher.target, dataset, dataset_id="dataset_id")

# ==================================================
# Line: 74

dataset_id2 = data_service_ops.register_dataset(
    cluster.dispatcher.target, dataset, dataset_id="dataset_id")

# ==================================================
# Occurrences: Lines 91-96 (2 instances)

dataset1 = self.make_distributed_dataset(dataset, cluster, job_name="job")

# ==================================================
# Occurrences: Lines 216-229 (2 instances)

dataset1 = self.make_distributed_dataset(
    dataset,
    cluster,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer ID"))

# ==================================================
# Occurrences: Lines 395-397 (3 instances)

output1 = self.getDatasetOutput(dataset1.take(10))

# ==================================================
# Occurrences: Lines 408-410 (3 instances)

output2 = self.getDatasetOutput(dataset2.take(10))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/dense_to_sparse_batch_test.py
# Line: 40

results = self.evaluate(get_next())

# ==================================================
# Line: 52

self.evaluate(get_next())

# ==================================================
# Line: 64

results = self.evaluate(get_next())

# ==================================================
# Line: 80

self.evaluate(get_next())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
# Line: 84

result = self.evaluate(get_next())

# ==================================================
# Line: 90

self.evaluate(get_next())

# ==================================================
# Line: 99

result = self.evaluate(get_next())

# ==================================================
# Line: 105

result = self.evaluate(get_next())

# ==================================================
# Line: 111

self.evaluate(get_next())

# ==================================================
# Line: 171

got = self.evaluate([element() for element in elements])

# ==================================================
# Line: 178

self.evaluate([element() for element in elements])

# ==================================================
# Line: 198

got = self.evaluate([element() for element in elements])

# ==================================================
# Line: 205

self.evaluate([element() for element in elements])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
# Occurrences: Lines 91-98 (4 instances)

shuffled_elements_1 = self.getDatasetOutput(
    self._build_dataset(), requires_initialization=True)

# ==================================================
# Occurrences: Lines 104-107 (2 instances)

shuffled_elements_1 = self.getDatasetOutput(
    self._build_dataset(seed=42), requires_initialization=True)

# ==================================================
# Occurrences: Lines 135-136 (2 instances)

shuffled_elements_1 = self.getDatasetOutput(dataset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
# Occurrences: Lines 36-43 (3 instances)

tmpdir = self.get_temp_dir()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
# Occurrences: Lines 194-195 (2 instances)

dataset = dataset.batch(10, drop_remainder=False)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/prefetch_to_device_test.py
# Occurrences: Lines 131-136 (2 instances)

actual = self.evaluate(next_element)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/prefetch_with_slack_test.py
# Occurrences: Lines 46-50 (2 instances)

elem_on_1, elem_on_2 = multi_device_iterator.get_next()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/non_serializable_test.py
# Occurrences: Lines 32-35 (2 instances)

dataset = dataset.skip(0)  # Should not be removed by noop elimination

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
# Occurrences: Lines 264-265 (2 instances)

self._cached_server1 = server_lib.Server.create_local_server()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/sleep_test.py
# Occurrences: Lines 37-40 (2 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 62-65 (2 instances)

ds = dataset_ops.Dataset.range(1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
# Occurrences: Lines 65-66 (2 instances)

output1 = self._gen_outputs(lambda: self._build_ds(10), 100)

# ==================================================
# Occurrences: Lines 144-146 (2 instances)

shuffle_1 = self.getDatasetOutput(ds)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
# Occurrences: Lines 74-96 (11 instances)

dataset = dataset_ops.Dataset.from_tensors(input_tensor).apply(
    contrib_parsing_ops.parse_example_dataset(feature_val))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
# Line: 94

actual_features = self.evaluate(get_next())

# ==================================================
# Line: 106

self.evaluate(get_next())

# ==================================================
# Occurrences: Lines 705-743 (14 instances)

dataset1 = self._make_csv_dataset(
    filenames,
    column_defaults=record_defaults,
    column_names=column_names,
    batch_size=batch_size,
    header=True,
    shuffle=True,
    shuffle_seed=5,
    num_epochs=2,
)

# ==================================================
# Occurrences: Lines 754-759 (8 instances)

next1 = self.getNext(dataset1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_saveable_from_iterator_test.py
# Occurrences: Lines 61-66 (2 instances)

init_ops, get_next_ops, saver = self._build_graph(num_pipelines,
                                                  num_outputs)

# ==================================================
# Occurrences: Lines 72-78 (2 instances)

init_ops, get_next_ops, saver = self._build_graph(num_pipelines,
                                                  num_outputs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
# Line: 75

elem = self.evaluate(next_fn())

# ==================================================
# Line: 83

self.evaluate(next_fn())

# ==================================================
# Occurrences: Lines 127-128 (2 instances)

dataset = dataset.prefetch(1)

# ==================================================
# Occurrences: Lines 144-149 (2 instances)

dataset1 = dataset_ops.Dataset.list_files(
    self._filenames, shuffle=False)

# ==================================================
# Occurrences: Lines 169-175 (2 instances)

dataset1 = dataset_ops.Dataset.list_files(
    self._filenames, shuffle=shuffle)

# ==================================================
# Occurrences: Lines 356-359 (2 instances)

ds1 = distribute._RemoteDataset(graph_def, "/device:CPU:0",
                                dataset.element_spec)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_tf_record_dataset_test.py
# Line: 93

next_element = self.getNext(dataset_fn())

# ==================================================
# Line: 101

next_element = self.getNext(dataset_fn())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/summary/writer/writer_test.py
# Occurrences: Lines 83-88 (2 instances)

ev = next(rr)

# ==================================================
# Line: 96

ev = next(rr)

# ==================================================
# Line: 104

self.assertRaises(StopIteration, lambda: next(rr))

# ==================================================
# Line: 126

run_metadata = config_pb2.RunMetadata()

# ==================================================
# Occurrences: Lines 134-139 (2 instances)

ev = next(rr)

# ==================================================
# Line: 145

ev = next(rr)

# ==================================================
# Line: 153

ev = next(rr)

# ==================================================
# Line: 161

ev = next(rr)

# ==================================================
# Occurrences: Lines 169-178 (3 instances)

ev = next(rr)

# ==================================================
# Occurrences: Lines 254-277 (6 instances)

ev = next(rr)

# ==================================================
# Line: 337

ev = next(rr)

# ==================================================
# Line: 343

ev = next(rr)

# ==================================================
# Line: 352

ev = next(rr)

# ==================================================
# Line: 361

self.assertRaises(StopIteration, lambda: next(rr))

# ==================================================
# Occurrences: Lines 372-378 (4 instances)

value = summary_pb2.Summary.Value(tag="foo", simple_value=10.0)

# ==================================================
# Occurrences: Lines 385-390 (2 instances)

ev = next(rr)

# ==================================================
# Line: 396

ev = next(rr)

# ==================================================
# Line: 412

ev = next(rr)

# ==================================================
# Line: 421

self.assertRaises(StopIteration, lambda: next(rr))

# ==================================================
# Occurrences: Lines 456-460 (2 instances)

content = f.read()

# ==================================================
# Occurrences: Lines 566-571 (2 instances)

writer1 = writer.FileWriter(session=sess, logdir=logdir)

# ==================================================
# Line: 588

writer5 = writer.FileWriter(session=sess, logdir=logdir)

# ==================================================
# Line: 595

events = summary_iterator.summary_iterator(next(event_paths))

# ==================================================
# Line: 603

events = summary_iterator.summary_iterator(next(event_paths))

# ==================================================
# Line: 623

writer2 = summary_ops_v2.create_file_writer(logdir=logdir)

# ==================================================
# Line: 642

writer4 = summary_ops_v2.create_file_writer(logdir=logdir)

# ==================================================
# Line: 656

writer6 = summary_ops_v2.create_file_writer(logdir=logdir)

# ==================================================
# Line: 666

events = summary_iterator.summary_iterator(next(event_paths))

# ==================================================
# Line: 674

events = summary_iterator.summary_iterator(next(event_paths))

# ==================================================
# Line: 680

events = summary_iterator.summary_iterator(next(event_paths))

# ==================================================
# Occurrences: Lines 724-726 (2 instances)

sw1 = writer_cache.FileWriterCache.get(dir1)

# ==================================================
# Occurrences: Lines 741-743 (2 instances)

sw1 = writer_cache.FileWriterCache.get(dir1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
# Occurrences: Lines 68-69 (2 instances)

self._flush_sentinel = object()

# ==================================================
# Occurrences: Lines 246-249 (2 instances)

self._not_empty = threading.Condition(self._mutex)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/summary/summary_test.py
# Occurrences: Lines 57-59 (2 instances)

im1 = summary_lib.scalar('inner', i, family='family')

# ==================================================
# Occurrences: Lines 241-244 (2 instances)

new_summ_pb = summary_pb2.Summary()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/summary/summary_iterator_test.py
# Occurrences: Lines 39-54 (5 instances)

ev = next(rr)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/summary/plugin_asset_test.py
# Occurrences: Lines 46-48 (2 instances)

epa = plugin_asset.get_plugin_asset(_ExamplePluginAsset)

# ==================================================
# Occurrences: Lines 68-69 (2 instances)

g1 = ops.Graph()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/platform/googletest.py
# Line: 184

orig_attr = getattr(obj, attr_name)

# ==================================================
# Line: 199

orig_attr = getattr(obj, attr_name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/platform/benchmark.py
# Occurrences: Lines 349-351 (4 instances)

start_time = time.time()

# ==================================================
# Line: 379

l = len(x)

# ==================================================
# Line: 386

l = len(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/feature_column/feature_column_test.py
# Line: 1755

my_vars = g.get_collection('my-vars')

# ==================================================
# Line: 1771

my_vars = g.get_collection('my-vars')

# ==================================================
# Line: 1935

fc.linear_model(features, [price])

# ==================================================
# Line: 1941

net = fc.linear_model(features, [price])

# ==================================================
# Line: 2395

my_vars = g.get_collection('my-vars')

# ==================================================
# Line: 2411

my_vars = g.get_collection('my-vars')

# ==================================================
# Line: 2582

get_keras_linear_model_predictions(features, [price])

# ==================================================
# Line: 2588

net = get_keras_linear_model_predictions(features, [price])

# ==================================================
# Line: 2633

inputs = input_layer(features)

# ==================================================
# Line: 2644

_ = input_layer(features)

# ==================================================
# Line: 3220

fc.input_layer(features, [price])

# ==================================================
# Line: 3226

net = fc.input_layer(features, [price])

# ==================================================
# Occurrences: Lines 4420-4422 (2 instances)

input_indices = array_ops.placeholder(dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 5137-5139 (3 instances)

input_indices = array_ops.placeholder(dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 5945-5948 (2 instances)

input_a_placeholder = array_ops.placeholder(
    dtype=dtypes.int64, shape=[None, 3])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
# Occurrences: Lines 209-210 (2 instances)

self._cols_to_vars_map = collections.defaultdict(lambda: {})

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# Line: 1918

my_vars = g.get_collection('my-vars')

# ==================================================
# Line: 1934

my_vars = g.get_collection('my-vars')

# ==================================================
# Line: 2099

fc_old.linear_model(features, [price])

# ==================================================
# Line: 2108

net = fc_old.linear_model(features, [price])

# ==================================================
# Line: 2331

inputs = input_layer(features)

# ==================================================
# Line: 2342

_ = input_layer(features)

# ==================================================
# Line: 2855

fc_old.input_layer(features, [price])

# ==================================================
# Line: 2864

net = fc_old.input_layer(features, [price])

# ==================================================
# Occurrences: Lines 4214-4216 (2 instances)

input_indices = array_ops.placeholder(dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 5061-5063 (3 instances)

input_indices = array_ops.placeholder(dtype=dtypes.int64)

# ==================================================
# Line: 5394

config = embedding_column.get_config()

# ==================================================
# Line: 5425

self.assertEqual(embedding_column.get_config(),

# ==================================================
# Line: 5437

self.assertEqual(embedding_column.get_config(),

# ==================================================
# Occurrences: Lines 5962-5965 (2 instances)

input_a_placeholder = array_ops.placeholder(
    dtype=dtypes.int64, shape=[None, 3])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/feature_column/serialization.py
# Occurrences: Lines 326-326 (2 instances)

tf_inspect.isfunction(_get_registered_object(item, custom_objects))):

# ==================================================
# Occurrences: Lines 335-335 (2 instances)

deserialized_objects[key] = _get_registered_object(item, custom_objects)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_with_v1_optimizers_test.py
# Occurrences: Lines 41-44 (2 instances)

root = trackable_utils.Checkpoint()

# ==================================================
# Line: 62

new_root = trackable_utils.Checkpoint()

# ==================================================
# Line: 74

new_root.optimizer = adam.AdamOptimizer(0.1)

# ==================================================
# Line: 106

root = create_trackable()

# ==================================================
# Line: 113

new_root = create_trackable()

# ==================================================
# Occurrences: Lines 166-168 (2 instances)

before_ops = graph.get_operations()

# ==================================================
# Occurrences: Lines 184-186 (2 instances)

before_ops = graph.get_operations()

# ==================================================
# Occurrences: Lines 194-197 (2 instances)

first_graph = ops.Graph()

# ==================================================
# Occurrences: Lines 207-213 (3 instances)

beta1_power, _ = optimizer._get_beta_accumulators()

# ==================================================
# Line: 222

beta1_power, _ = optimizer._get_beta_accumulators()

# ==================================================
# Line: 228

beta1_power, _ = optimizer._get_beta_accumulators()

# ==================================================
# Line: 235

beta1_power, _ = optimizer._get_beta_accumulators()

# ==================================================
# Line: 243

beta1_power, _ = optimizer._get_beta_accumulators()

# ==================================================
# Line: 282

optimizer = adam.AdamOptimizer(0.0)

# ==================================================
# Line: 295

load_optimizer = adam.AdamOptimizer(0.0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/saveable_compat_test.py
# Line: 78

table_module = generate_checkpoint.TableModule()

# ==================================================
# Line: 85

new_table_module = generate_checkpoint.TableModule()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_view_test.py
# Occurrences: Lines 28-29 (2 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 40-41 (2 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 51-56 (6 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 69-83 (11 instances)

root1 = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 94-102 (5 instances)

root1 = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 119-134 (12 instances)

root1 = autotrackable.AutoTrackable()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/benchmarks_test.py
# Occurrences: Lines 61-64 (2 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/restore.py
# Line: 592

serialized_tensors = object_identity.ObjectIdentityDictionary()

# ==================================================
# Occurrences: Lines 612-612 (2 instances)

object_names = object_identity.ObjectIdentityDictionary()

# ==================================================
# Occurrences: Lines 655-655 (2 instances)

serialized_tensors_renamed = object_identity.ObjectIdentityDictionary()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/functional_saver_test.py
# Occurrences: Lines 240-242 (6 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/restore_test.py
# Occurrences: Lines 41-48 (4 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 76-79 (2 instances)

self.a = variables.Variable(5.0)

# ==================================================
# Line: 138

self.a = variables.Variable(5.0)

# ==================================================
# Line: 149

self.a = variables.Variable(5.0)

# ==================================================
# Occurrences: Lines 162-164 (2 instances)

root_ckpt = trackable_utils.Checkpoint(root=root)

# ==================================================
# Occurrences: Lines 175-177 (2 instances)

root_ckpt = trackable_utils.Checkpoint(root=root)

# ==================================================
# Line: 256

self.a = variables.Variable(1.0)

# ==================================================
# Line: 264

self.a = variables.Variable(1.0)

# ==================================================
# Occurrences: Lines 273-275 (2 instances)

root_ckpt = trackable_utils.Checkpoint(root=root)

# ==================================================
# Occurrences: Lines 285-287 (2 instances)

root_ckpt = trackable_utils.Checkpoint(root=root)

# ==================================================
# Occurrences: Lines 297-299 (2 instances)

root_ckpt = trackable_utils.Checkpoint(root=root)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/save_util_v1_test.py
# Occurrences: Lines 55-59 (2 instances)

root.v = variables.Variable(1.0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/tensor_callable_test.py
# Occurrences: Lines 56-58 (2 instances)

save_path = ckpt.save(prefix)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
# Line: 89

saver = saver_module.Saver(sharded=True)

# ==================================================
# Line: 95

saver = saver_module.Saver(sharded=True)

# ==================================================
# Line: 120

save = saver_module.Saver({"v0": v0})

# ==================================================
# Line: 135

save = saver_module.Saver({"v0": v0})

# ==================================================
# Occurrences: Lines 342-345 (4 instances)

first_path = manager.save()

# ==================================================
# Occurrences: Lines 359-363 (4 instances)

manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=None)

# ==================================================
# Occurrences: Lines 371-373 (2 instances)

manager = checkpoint_management.CheckpointManager(
    checkpoint, directory, max_to_keep=None)

# ==================================================
# Line: 385

fifth_path = manager.save()

# ==================================================
# Occurrences: Lines 406-411 (2 instances)

state = checkpoint_management.get_checkpoint_state(directory)

# ==================================================
# Line: 418

second_manager = checkpoint_management.CheckpointManager(
    checkpoint, directory,
    max_to_keep=2, keep_checkpoint_every_n_hours=1.5)

# ==================================================
# Line: 431

state = checkpoint_management.get_checkpoint_state(directory)

# ==================================================
# Occurrences: Lines 447-457 (3 instances)

state = checkpoint_management.get_checkpoint_state(directory)

# ==================================================
# Occurrences: Lines 472-486 (7 instances)

checkpoint = util.Checkpoint()

# ==================================================
# Occurrences: Lines 503-512 (4 instances)

first_path = first_manager.save()

# ==================================================
# Line: 531

fourth_path = second_manager.save()

# ==================================================
# Occurrences: Lines 537-541 (2 instances)

fifth_path = second_manager.save()

# ==================================================
# Occurrences: Lines 577-581 (2 instances)

path = manager.save(checkpoint_number=5)

# ==================================================
# Occurrences: Lines 623-627 (2 instances)

expected = str(directory / "ckpt_name-1")

# ==================================================
# Occurrences: Lines 654-673 (5 instances)

path = manager.save(check_interval=True)

# ==================================================
# Occurrences: Lines 695-705 (3 instances)

path = manager.save(check_interval=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/trackable_view_test.py
# Occurrences: Lines 25-26 (2 instances)

root = base.Trackable()

# ==================================================
# Occurrences: Lines 34-35 (2 instances)

root = base.Trackable()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
# Occurrences: Lines 359-359 (2 instances)

async_save_start_time = time.time()

# ==================================================
# Occurrences: Lines 383-383 (2 instances)

async_save_end_time = time.time()

# ==================================================
# Line: 480

write_start_time = time.time()

# ==================================================
# Line: 510

write_end_time = time.time()

# ==================================================
# Line: 528

save_start_time = time.time()

# ==================================================
# Line: 575

save_end_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/save_util_v1.py
# Occurrences: Lines 263-266 (2 instances)

object_names = object_identity.ObjectIdentityDictionary()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_metrics_test.py
# Occurrences: Lines 54-68 (6 instances)

self.assertEqual(self._get_time_saved(api_label), 0.0)

# ==================================================
# Line: 74

self.assertEqual(self._get_time_saved(api_label), time_saved)

# ==================================================
# Occurrences: Lines 85-104 (7 instances)

self.assertEqual(self._get_time_saved(api_label), 0.0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/save_util.py
# Occurrences: Lines 89-92 (2 instances)

object_names = object_identity.ObjectIdentityDictionary()

# ==================================================
# Occurrences: Lines 182-184 (2 instances)

object_names = object_identity.ObjectIdentityDictionary()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/util.py
# Occurrences: Lines 161-168 (3 instances)

object_names = object_identity.ObjectIdentityDictionary()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint.py
# Occurrences: Lines 1220-1221 (2 instances)

self._cache = object_identity.ObjectIdentityWeakKeyDictionary()

# ==================================================
# Occurrences: Lines 1340-1343 (2 instances)

self._object_graph_feed_tensor = constant_op.constant(
    "", dtype=dtypes.string)

# ==================================================
# Occurrences: Lines 1819-1822 (2 instances)

start_time = time.time()

# ==================================================
# Line: 2045

start_time = time.time()

# ==================================================
# Line: 2056

microseconds=_get_duration_microseconds(start_time, time.time()))

# ==================================================
# Line: 2367

start_time = time.time()

# ==================================================
# Line: 2381

end_time = time.time()

# ==================================================
# Line: 2591

start_time = time.time()

# ==================================================
# Line: 2598

microseconds=_get_duration_microseconds(start_time, time.time()))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Occurrences: Lines 96-99 (2 instances)

duplicate = trackable_utils.add_variable(
    obj, name="duplicate", shape=[])

# ==================================================
# Line: 222

save_path = checkpoint.save(file_prefix=prefix, options=ckpt_options)

# ==================================================
# Line: 232

save_path = checkpoint.save(file_prefix=prefix, options=ckpt_options)

# ==================================================
# Occurrences: Lines 314-320 (3 instances)

v = resource_variable_ops.ResourceVariable(0, dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 331-333 (3 instances)

v = resource_variable_ops.ResourceVariable(0, dtype=dtypes.int64)

# ==================================================
# Line: 341

v = resource_variable_ops.ResourceVariable(0, dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 444-445 (2 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 453-454 (2 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 526-527 (2 instances)

save_root = trackable_utils.Checkpoint()

# ==================================================
# Occurrences: Lines 535-541 (6 instances)

first_root = trackable_utils.Checkpoint()

# ==================================================
# Occurrences: Lines 553-559 (6 instances)

first_root = trackable_utils.Checkpoint()

# ==================================================
# Occurrences: Lines 573-576 (4 instances)

save_root = trackable_utils.Checkpoint()

# ==================================================
# Occurrences: Lines 582-587 (5 instances)

load_root = trackable_utils.Checkpoint()

# ==================================================
# Occurrences: Lines 601-603 (3 instances)

save_root = trackable_utils.Checkpoint()

# ==================================================
# Occurrences: Lines 610-611 (2 instances)

load_root = trackable_utils.Checkpoint()

# ==================================================
# Occurrences: Lines 640-641 (2 instances)

first = trackable_utils.Checkpoint()

# ==================================================
# Line: 653

first_load = trackable_utils.Checkpoint()

# ==================================================
# Occurrences: Lines 683-693 (6 instances)

first = trackable_utils.Checkpoint()

# ==================================================
# Line: 770

checkpoint = trackable_utils.Checkpoint(model=model)

# ==================================================
# Line: 781

checkpoint = trackable_utils.Checkpoint(model=model)

# ==================================================
# Line: 801

status = load_checkpoint.read(checkpoint_prefix)

# ==================================================
# Line: 809

status = load_checkpoint.read(checkpoint_prefix)

# ==================================================
# Line: 834

status = load_checkpoint.read(checkpoint_prefix)

# ==================================================
# Line: 842

status = load_checkpoint.read(checkpoint_prefix)

# ==================================================
# Line: 904

model = self._create_trackable()

# ==================================================
# Line: 914

new_model = self._create_trackable()

# ==================================================
# Line: 923

model = self._create_trackable()

# ==================================================
# Line: 937

new_model = self._create_trackable()

# ==================================================
# Occurrences: Lines 949-950 (2 instances)

new_model.separate_variable = variables_lib.Variable(200.)

# ==================================================
# Occurrences: Lines 958-959 (2 instances)

separate_variable = variables_lib.Variable(200.)

# ==================================================
# Line: 968

model = self._create_trackable()

# ==================================================
# Line: 975

new_model = self._create_trackable()

# ==================================================
# Line: 1004

x = autotrackable.AutoTrackable()

# ==================================================
# Line: 1017

no_v = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 1028-1033 (5 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Line: 1039

new_root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 1046-1056 (4 instances)

new_root.branch_no_value = autotrackable.AutoTrackable()

# ==================================================
# Line: 1062

root2 = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 1151-1156 (2 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 1442-1443 (4 instances)

v2 = second_inner()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/functional_saver.py
# Occurrences: Lines 654-659 (2 instances)

restore_fn()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/python_state_test.py
# Occurrences: Lines 73-77 (2 instances)

value = getattr(arrays, name)

# ==================================================
# Occurrences: Lines 147-173 (13 instances)

save_state = _NumpyState()

# ==================================================
# Occurrences: Lines 184-204 (8 instances)

save_path = saver.save(prefix)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/autotrackable_test.py
# Occurrences: Lines 30-33 (3 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 44-45 (2 instances)

root = autotrackable.AutoTrackable()

# ==================================================
# Line: 53

root.a = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 59-62 (3 instances)

a = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 74-77 (3 instances)

a = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 85-89 (3 instances)

a = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 97-118 (9 instances)

a = autotrackable.AutoTrackable()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/resource_test.py
# Occurrences: Lines 82-86 (2 instances)

resource_tracker1 = resource.ResourceTracker()

# ==================================================
# Occurrences: Lines 96-102 (3 instances)

resource_tracker = resource.ResourceTracker()

# ==================================================
# Occurrences: Lines 145-147 (2 instances)

scope = ops.resource_creator_scope(creator, "_DummyResource")

# ==================================================
# Line: 158

instance = next_creator(*a, **kwargs)

# ==================================================
# Line: 164

return next_creator(*a, **kwargs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/base_test.py
# Occurrences: Lines 26-36 (5 instances)

root = base.Trackable()

# ==================================================
# Occurrences: Lines 58-62 (2 instances)

has_config = base.Trackable()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/data_structures_test.py
# Occurrences: Lines 102-104 (3 instances)

v1 = resource_variable_ops.ResourceVariable(1.)

# ==================================================
# Occurrences: Lines 113-116 (4 instances)

v1 = resource_variable_ops.ResourceVariable(1.)

# ==================================================
# Occurrences: Lines 208-209 (2 instances)

a = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 286-287 (2 instances)

v1 = resource_variable_ops.ResourceVariable(1.)

# ==================================================
# Occurrences: Lines 347-357 (5 instances)

mapping = data_structures.Mapping()

# ==================================================
# Line: 382

copied = copy.copy(root.a)

# ==================================================
# Line: 393

util.list_objects(copy.copy(root.a))

# ==================================================
# Line: 399

copied = copy.deepcopy(root.a)

# ==================================================
# Line: 410

util.list_objects(copy.deepcopy(root.a))

# ==================================================
# Line: 416

copied = copy.copy(root.a)

# ==================================================
# Line: 432

util.list_objects(copy.copy(root.a))

# ==================================================
# Line: 438

copied = copy.deepcopy(root.a)

# ==================================================
# Occurrences: Lines 449-453 (3 instances)

util.list_objects(copy.deepcopy(root.a))

# ==================================================
# Occurrences: Lines 466-467 (2 instances)

original = autotrackable.AutoTrackable()

# ==================================================
# Occurrences: Lines 537-538 (2 instances)

v1 = resource_variable_ops.ResourceVariable(1.)

# ==================================================
# Occurrences: Lines 551-554 (4 instances)

v1 = resource_variable_ops.ResourceVariable(1.)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/module/module_test.py
# Occurrences: Lines 304-306 (2 instances)

leaf1 = m.new_leaf()

# ==================================================
# Occurrences: Lines 522-524 (2 instances)

mod = module.Module()

# ==================================================
# Occurrences: Lines 539-541 (2 instances)

mod = module.Module()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
# Occurrences: Lines 168-171 (6 instances)

num_gpus = sum(1 for d in device_in_task if _is_gpu_device(d))

# ==================================================
# Line: 390

self._communication_options = collective_util.Options(
    implementation=collective_util.CommunicationImplementation.RING)

# ==================================================
# Line: 398

self._communication_options = collective_util.Options(
    implementation=collective_util.CommunicationImplementation.RING)

# ==================================================
# Line: 524

return next_creator(**kwargs)

# ==================================================
# Line: 548

v = next_creator(**kwargs)

# ==================================================
# Occurrences: Lines 795-796 (4 instances)

cross_device_ops = self._get_cross_device_ops(value)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# Line: 468

group_size=len(local_devices),

# ==================================================
# Line: 495

self._num_devices_per_worker = len(local_devices)

# ==================================================
# Line: 624

group_size=len(local_devices) * self._num_workers,

# ==================================================
# Line: 644

self._num_devices_per_worker = len(local_devices)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/random_generator_test.py
# Occurrences: Lines 110-111 (4 instances)

t1 = gen.uniform_full_int(shape=shape, dtype=dtype)

# ==================================================
# Occurrences: Lines 138-139 (4 instances)

t1 = gen.uniform_full_int(shape=shape, dtype=dtype)

# ==================================================
# Occurrences: Lines 158-161 (2 instances)

s1 = read_values(g.state)

# ==================================================
# Occurrences: Lines 194-195 (4 instances)

t1 = gen.uniform_full_int(shape=shape, dtype=dtype)

# ==================================================
# Occurrences: Lines 248-249 (4 instances)

t1 = gen.uniform_full_int(shape=shape, dtype=dtype)

# ==================================================
# Line: 343

state_before = m()

# ==================================================
# Occurrences: Lines 352-358 (3 instances)

state_before_2 = m()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
# Line: 361

local_results = self.evaluate(distribution.experimental_local_results(v0))

# ==================================================
# Line: 372

local_results1 = self.evaluate(
    distribution.experimental_local_results(v1))

# ==================================================
# Line: 392

local_results = self.evaluate(distribution.experimental_local_results(v0))

# ==================================================
# Line: 400

local_results1 = self.evaluate(
    distribution.experimental_local_results(v1))

# ==================================================
# Occurrences: Lines 554-555 (4 instances)

cell_fw = rnn_cell_impl.LSTMCell(300)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/moving_averages_test.py
# Occurrences: Lines 148-150 (3 instances)

var1 = variables.Variable([0.0, 0.0])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/warm_starting_util_test.py
# Occurrences: Lines 72-75 (2 instances)

_, prev_init_val = create_var(g)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
# Occurrences: Lines 101-113 (4 instances)

v0 = variables.Variable(initial_value=0.0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cross_device_utils.py
# Occurrences: Lines 115-117 (4 instances)

group_0_agg_grads_bcast = array_ops.identity(agg_total_grads)

# ==================================================
# Occurrences: Lines 335-341 (2 instances)

instance_key = self._collective_keys.get_instance_key(
    self._group_key, self._device)

# ==================================================
# Line: 570

max_length = math_ops.reduce_max(all_lengths)

# ==================================================
# Line: 582

math_ops.reduce_max(all_lengths),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
# Occurrences: Lines 976-984 (8 instances)

per_replica_outputs = distribution.run(
    func, (next(input_iterator),))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/values_test.py
# Line: 191

multiple_values = range(distribution.num_replicas_in_sync)

# ==================================================
# Line: 197

expected = range(distribution.num_replicas_in_sync)

# ==================================================
# Line: 212

multiple_values = range(distribution.num_replicas_in_sync)

# ==================================================
# Line: 228

expected = [i**2 for i in range(distribution.num_replicas_in_sync)]

# ==================================================
# Occurrences: Lines 538-545 (2 instances)

v1 = variables_lib.Variable(
    0.0,
    aggregation=variables_lib.VariableAggregation.SUM,
    synchronization=variables_lib.VariableSynchronization.ON_READ)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
# Occurrences: Lines 103-105 (2 instances)

self._init_condition = threading.Condition()

# ==================================================
# Occurrences: Lines 279-279 (2 instances)

replica_id = _get_replica_id_integer()

# ==================================================
# Occurrences: Lines 287-287 (2 instances)

replica_id = _get_replica_id_integer()

# ==================================================
# Occurrences: Lines 480-480 (3 instances)

fetched = d.extended.read_var(v)

# ==================================================
# Occurrences: Lines 488-488 (3 instances)

after_list.append(d.extended.read_var(v))

# ==================================================
# Occurrences: Lines 536-538 (2 instances)

next_element = iterator.get_next()

# ==================================================
# Occurrences: Lines 545-547 (2 instances)

next_element = iterator.get_next()

# ==================================================
# Occurrences: Lines 554-556 (2 instances)

next_element = iterator.get_next()

# ==================================================
# Occurrences: Lines 638-641 (2 instances)

fn = lambda: dataset_ops.Dataset.range(100)

# ==================================================
# Occurrences: Lines 668-672 (2 instances)

fn = lambda: dataset_ops.Dataset.range(100)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/shared_variable_creator.py
# Line: 64

canonical_name = _canonicalize_variable_name(kwargs.get("name"))

# ==================================================
# Line: 75

name = kwargs.get("name")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/values.py
# Occurrences: Lines 528-530 (4 instances)

v.handle._distributed_container = weakref.ref(self)  # pylint: disable=protected-access

# ==================================================
# Occurrences: Lines 621-624 (2 instances)

return self._primary.is_initialized()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
# Occurrences: Lines 162-165 (2 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 193-196 (2 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 219-222 (2 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
# Occurrences: Lines 175-176 (2 instances)

device_util.resolve(_cpu_device))

# ==================================================
# Line: 470

comm_options = collective_util.Options(implementation=communication)

# ==================================================
# Line: 496

comm_options = collective_util.Options(implementation=communication)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
# Occurrences: Lines 104-113 (4 instances)

extended_whole = array_ops.concat(
    [tensor, array_ops.zeros([pad_len], dtype=tensor.dtype)], 0)

# ==================================================
# Occurrences: Lines 545-549 (6 instances)

new_chunks[left_idx] = array_ops.concat([chunks[left_idx],
                                         chunks[right_idx]], 0)

# ==================================================
# Occurrences: Lines 665-666 (2 instances)

per_task_devices = collections.OrderedDict()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/multi_process_runner.py
# Occurrences: Lines 240-241 (2 instances)

self._process_status_queue = self._manager.Queue()

# ==================================================
# Line: 247

self._streaming_queue = self._manager.Queue()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/packed_distributed_variable_test.py
# Occurrences: Lines 74-79 (2 instances)

val0 = packed_var.assign(2.0).assign_add(1.0)

# ==================================================
# Occurrences: Lines 87-90 (4 instances)

read0 = packed_var.value()

# ==================================================
# Occurrences: Lines 106-111 (2 instances)

val0 = packed_var.assign(2.0).assign_add(1.0)

# ==================================================
# Occurrences: Lines 139-145 (2 instances)

packed_var0 = packed_distributed_variable.PackedVarAndDevice(
    packed_var, device0)

# ==================================================
# Occurrences: Lines 151-153 (2 instances)

var0 = packed_distributed_variable.PackedVarAndDevice(packed_var, device0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_lib.py
# Line: 665

optional_data = iterator.get_next_as_optional()

# ==================================================
# Line: 674

optional_data = iterator.get_next_as_optional()

# ==================================================
# Line: 833

distribute_start_time_ns = time.time_ns()

# ==================================================
# Line: 841

distribute_duration_ms = (time.time_ns() -

# ==================================================
# Line: 1163

distribute_start_time_ns = time.time_ns()

# ==================================================
# Line: 1170

distribute_duration_ms = (time.time_ns() -

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/vars_test.py
# Occurrences: Lines 444-444 (2 instances)

ckpt = trackable_utils.Checkpoint(var=v_on_write)

# ==================================================
# Occurrences: Lines 467-467 (2 instances)

ckpt_on_write = trackable_utils.Checkpoint(var=v_on_write)

# ==================================================
# Occurrences: Lines 1165-1167 (4 instances)

ckpt = trackable_utils.Checkpoint(var=v_on_read)

# ==================================================
# Occurrences: Lines 1183-1187 (4 instances)

manager = ckpt_manager.CheckpointManager(
    ckpt, "/tmp/ckpt_" + str(uuid.uuid4()), max_to_keep=None)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# Occurrences: Lines 252-257 (2 instances)

export_dir = self.get_temp_dir()

# ==================================================
# Occurrences: Lines 383-386 (2 instances)

loaded = tf.saved_model.load(export_dir2)

# ==================================================
# Line: 530

v1_export_dir = self.get_temp_dir()

# ==================================================
# Line: 544

v2_export_dir = self.get_temp_dir()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/integration_test/tpu_memory_test.py
# Occurrences: Lines 42-47 (2 instances)

dataset = dataset.repeat()

# ==================================================
# Occurrences: Lines 121-130 (2 instances)

y = tf.keras.layers.Dense(
    1024,
    activation="softmax",
    kernel_initializer=tf.random_normal_initializer(stddev=0.01))(
        y)

# ==================================================
# Line: 174

result = train_step(iterator)

# ==================================================
# Line: 181

_ = train_step(iterator)

# ==================================================
# Occurrences: Lines 190-196 (7 instances)

buffer_2g_1 = tf.random.uniform((2, 256, 1024, 1024), dtype=tf.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_ops_test.py
# Occurrences: Lines 303-304 (2 instances)

ds1 = dataset_ops.Dataset.range(10)

# ==================================================
# Occurrences: Lines 311-312 (2 instances)

ds1 = dataset_ops.Dataset.range(10)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_lib_test.py
# Line: 205

iterator = iter(dataset)

# ==================================================
# Line: 236

iterator = iter(dataset)

# ==================================================
# Line: 268

iterator = iter(dataset)

# ==================================================
# Occurrences: Lines 375-376 (2 instances)

local = distribution.experimental_local_results(element)

# ==================================================
# Occurrences: Lines 386-387 (2 instances)

local = distribution.experimental_local_results(element)

# ==================================================
# Occurrences: Lines 486-487 (4 instances)

dataset1 = dataset_ops.Dataset.range(10)

# ==================================================
# Occurrences: Lines 521-522 (4 instances)

dataset1 = dataset_ops.Dataset.range(10)

# ==================================================
# Line: 597

iterator = iter(dist_dataset)

# ==================================================
# Line: 622

iterator = iter(dist_dataset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distributed_table_test.py
# Occurrences: Lines 248-251 (2 instances)

dataset = dataset_ops.DatasetV2.from_tensors(
    constant_op.constant([0, 1, 3], dtype=dtypes.int64))

# ==================================================
# Occurrences: Lines 260-266 (2 instances)

dataset = dataset_ops.DatasetV2.from_tensors(
    constant_op.constant([0, 1, 3], dtype=dtypes.int64))

# ==================================================
# Occurrences: Lines 273-287 (6 instances)

per_worker_dataset = coordinator.create_per_worker_dataset(
    per_worker_dataset_fn())

# ==================================================
# Occurrences: Lines 338-347 (3 instances)

lookup_table = self.createStaticHashTable(
    init_source=source, vals=[0, 1, 2], default_value=-2)

# ==================================================
# Line: 363

lookup_table = self.createStaticHashTable(
    init_source=source, vals=[0, 1, 2], default_value=-2)

# ==================================================
# Occurrences: Lines 370-376 (2 instances)

dataset = dataset_ops.DatasetV2.from_tensors(
    constant_op.constant([0, 1, 3], dtype=dtypes.int64))

# ==================================================
# Occurrences: Lines 384-398 (6 instances)

per_worker_dataset = coordinator.create_per_worker_dataset(
    per_worker_dataset_fn())

# ==================================================
# Line: 584

replica_result = array_ops.zeros(shape=(), dtype=dtypes.int64)

# ==================================================
# Line: 592

step_result = array_ops.zeros(shape=(), dtype=dtypes.int64)

# ==================================================
# Occurrences: Lines 619-623 (2 instances)

file_path = os.path.join(self.get_temp_dir(), "text_file_initializer")

# ==================================================
# Occurrences: Lines 645-648 (2 instances)

file_path = os.path.join(self.get_temp_dir(), "text_file_initializer")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/ps_values_test.py
# Line: 39

save_path = checkpoint.save(prefix, options=ckpt_options)

# ==================================================
# Line: 51

save_path = checkpoint.save(prefix, options=ckpt_options)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distribute_lib.py
# Occurrences: Lines 3816-3821 (8 instances)

input_shape = array_ops.shape(xs[i])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
# Occurrences: Lines 94-113 (5 instances)

got = partitioner(tensor_shape.TensorShape([6, 1]), dtypes.float32)

# ==================================================
# Occurrences: Lines 168-169 (2 instances)

v0 = variables_lib.Variable(array_ops.zeros((11, 1)))

# ==================================================
# Occurrences: Lines 195-197 (3 instances)

v0 = variables_lib.Variable(array_ops.zeros((10, 1)))

# ==================================================
# Occurrences: Lines 218-219 (2 instances)

v0 = variables_lib.Variable(array_ops.zeros((11, 1)))

# ==================================================
# Occurrences: Lines 239-241 (3 instances)

v0 = variables_lib.Variable(array_ops.zeros((10, 1)))

# ==================================================
# Occurrences: Lines 263-265 (4 instances)

a = array_ops.ones((1, 1))

# ==================================================
# Line: 356

model = autotrackable.AutoTrackable()

# ==================================================
# Line: 367

model2 = autotrackable.AutoTrackable()

# ==================================================
# Line: 384

model = autotrackable.AutoTrackable()

# ==================================================
# Line: 395

model2 = autotrackable.AutoTrackable()

# ==================================================
# Line: 436

[variables_lib.Variable([0]), 'not-a-variable'])

# ==================================================
# Line: 454

v = variables_lib.Variable([0])

# ==================================================
# Occurrences: Lines 797-805 (4 instances)

loaded_layer = load.load(model_dir)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
# Occurrences: Lines 669-669 (2 instances)

value = constant_op.constant(1.0)

# ==================================================
# Occurrences: Lines 686-686 (2 instances)

value = (constant_op.constant(1.0), constant_op.constant(2.0))

# ==================================================
# Occurrences: Lines 1300-1305 (6 instances)

i = array_ops.identity(1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
# Line: 395

assert _thread_local.session_config_str == repr(session_config)

# ==================================================
# Line: 405

_thread_local.session_config_str = repr(session_config)

# ==================================================
# Line: 815

server = _run_std_server(
    cluster_spec=cluster_spec,
    task_type=task_type,
    task_id=task_id,
    session_config=session_config,
    rpc_layer=rpc_layer,
    environment=environment)

# ==================================================
# Line: 846

server = _run_std_server(
    cluster_spec=cluster_spec,
    task_type=task_type,
    task_id=task_id,
    session_config=session_config,
    rpc_layer=rpc_layer,
    environment=environment)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cross_device_ops.py
# Line: 304

options = collective_util.Options()

# ==================================================
# Line: 319

options = collective_util.Options()

# ==================================================
# Line: 423

options = collective_util.Options()

# ==================================================
# Line: 445

options = collective_util.Options()

# ==================================================
# Line: 1194

num_devices = len(self._devices)

# ==================================================
# Line: 1207

pool = multiprocessing.pool.ThreadPool(len(self._devices))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
# Line: 223

result = strategy.run(def_function.function(model), args=(5.0,))

# ==================================================
# Line: 232

result = strategy.run(def_function.function(model), args=(5.0,))

# ==================================================
# Occurrences: Lines 302-305 (2 instances)

x = random_ops.random_uniform((batch_size, num_feature_in),
                              dtype=dtypes.float32)

# ==================================================
# Line: 325

delta = random_ops.random_uniform((batch_size, num_feature_in),
                                  dtype=dtypes.float32)

# ==================================================
# Line: 332

delta = random_ops.random_uniform((batch_size, num_feature_in),
                                  dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 343-346 (2 instances)

x = random_ops.random_uniform((batch_size, num_feature_in),
                              dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 353-366 (5 instances)

result = w.numpy()

# ==================================================
# Occurrences: Lines 386-389 (2 instances)

w1 = random_ops.random_uniform((num_feature_in, num_feature_out),
                               dtype=dtypes.float32)

# ==================================================
# Line: 411

result = strategy.run(step_fn, args=(x,))

# ==================================================
# Line: 423

result = strategy.run(step_fn, args=(x,))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_strategy.py
# Occurrences: Lines 917-918 (2 instances)

self._device_input_worker_devices = collections.OrderedDict()

# ==================================================
# Line: 1259

return next_creator(**kwargs)

# ==================================================
# Line: 1272

return next_creator(**kwargs)

# ==================================================
# Line: 1296

initial_value = initial_value() if callable(

# ==================================================
# Line: 1309

v = next_creator(**kwargs)

# ==================================================
# Line: 1330

initial_value = initial_value() if callable(

# ==================================================
# Occurrences: Lines 1340-1344 (3 instances)

v = next_creator(**kwargs)

# ==================================================
# Occurrences: Lines 1371-1371 (2 instances)

if kwargs.get("initial_value", None) is None:

# ==================================================
# Occurrences: Lines 1380-1388 (4 instances)

initial_value = kwargs.get("initial_value", None)

# ==================================================
# Occurrences: Lines 1401-1408 (3 instances)

if kwargs.get("dtype", None) is None:

# ==================================================
# Occurrences: Lines 1425-1427 (3 instances)

dtype = kwargs.get("dtype", None)

# ==================================================
# Line: 1435

initial_value = initial_value()

# ==================================================
# Occurrences: Lines 1454-1459 (3 instances)

v = uninitialized_variable_creator(**kwargs)

# ==================================================
# Occurrences: Lines 1962-1966 (4 instances)

value_shape = array_ops.shape(value)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
# Occurrences: Lines 135-135 (2 instances)

dist = _TestStrategy()

# ==================================================
# Occurrences: Lines 144-144 (2 instances)

another_strategy = _TestStrategy()

# ==================================================
# Occurrences: Lines 258-259 (2 instances)

dist = _TestStrategy()

# ==================================================
# Occurrences: Lines 278-283 (2 instances)

dist = _TestStrategy()

# ==================================================
# Occurrences: Lines 296-300 (3 instances)

dist = _TestStrategy()

# ==================================================
# Line: 307

dist2 = _TestStrategy()

# ==================================================
# Occurrences: Lines 331-332 (4 instances)

x = constant_op.constant(1.)

# ==================================================
# Occurrences: Lines 379-380 (2 instances)

x = constant_op.constant(1.)

# ==================================================
# Line: 466

self.assertIs(None, distribute_lib.get_replica_context())

# ==================================================
# Line: 473

replica_ctx = distribute_lib.get_replica_context()

# ==================================================
# Occurrences: Lines 540-546 (2 instances)

dist_dataset = default_strategy.experimental_distribute_dataset(
    dataset_fn(distribute_lib.InputContext()))

# ==================================================
# Line: 558

default_strategy.distribute_datasets_from_function(
    dataset_fn)

# ==================================================
# Line: 565

default_strategy.distribute_datasets_from_function(
    dataset_fn)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
# Occurrences: Lines 269-271 (2 instances)

if sum(self._jobs.values()) != num_tasks:

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
# Occurrences: Lines 128-134 (3 instances)

mock_locations = mock.MagicMock()

# ==================================================
# Occurrences: Lines 700-703 (2 instances)

mock_list_devices.side_effect = errors.DeadlineExceededError(
    None, None, 'timeout')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver_test.py
# Occurrences: Lines 39-45 (3 instances)

mock_status = mock.Mock()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
# Line: 63

mock_get_request = mock.MagicMock()

# ==================================================
# Line: 74

mock_get_request = mock.MagicMock()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
# Occurrences: Lines 524-525 (2 instances)

cluster_spec = cluster_resolver.cluster_spec()

# ==================================================
# Occurrences: Lines 541-542 (2 instances)

cluster_spec = cluster_resolver.cluster_spec()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
# Occurrences: Lines 180-180 (3 instances)

fetched = distribution.extended.read_var(v)

# ==================================================
# Occurrences: Lines 189-189 (3 instances)

after_list.append(distribution.extended.read_var(v))

# ==================================================
# Occurrences: Lines 257-259 (2 instances)

next_element = iterator.get_next()

# ==================================================
# Occurrences: Lines 266-268 (2 instances)

next_element = iterator.get_next()

# ==================================================
# Occurrences: Lines 275-278 (2 instances)

next_element = iterator.get_next()

# ==================================================
# Occurrences: Lines 371-374 (4 instances)

fn = lambda: dataset_ops.Dataset.range(20)

# ==================================================
# Occurrences: Lines 516-519 (2 instances)

fn = lambda: dataset_ops.Dataset.range(5 * required_gpus)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
# Occurrences: Lines 282-284 (3 instances)

training_started_event = multi_process_runner.manager().Event()

# ==================================================
# Occurrences: Lines 320-322 (3 instances)

training_started_event = threading.Event()

# ==================================================
# Occurrences: Lines 412-420 (4 instances)

termination_config = failure_handling.TerminationConfig(
    grace_period=grace_period)

# ==================================================
# Occurrences: Lines 457-463 (4 instances)

termination_config = failure_handling.TerminationConfig(
    grace_period=grace_period)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/failure_handling/gce_failure_handler_test.py
# Occurrences: Lines 217-220 (2 instances)

max([int(ckpt_index) for ckpt_index in checkpoint_index]), 2)

# ==================================================
# Line: 226

max([int(ckpt_index) for ckpt_index in checkpoint_index]),

# ==================================================
# Line: 251

running_threads = test_util.get_running_threads()

# ==================================================
# Line: 263

running_threads = test_util.get_running_threads()

# ==================================================
# Occurrences: Lines 303-305 (3 instances)

maintenance_event = multi_process_runner.manager().Event()

# ==================================================
# Occurrences: Lines 333-335 (3 instances)

maintenance_event = threading.Event()

# ==================================================
# Occurrences: Lines 391-393 (3 instances)

maintenance_event = multi_process_runner.manager().Event()

# ==================================================
# Occurrences: Lines 430-432 (3 instances)

maintenance_event = threading.Event()

# ==================================================
# Line: 468

checkpoint_dir = os.path.join(self.get_temp_dir(), 'fh_ckpt/')

# ==================================================
# Occurrences: Lines 484-487 (4 instances)

checkpoint_dir = os.path.join(self.get_temp_dir(), 'fh_ckpt/')

# ==================================================
# Occurrences: Lines 530-532 (3 instances)

maintenance_event = threading.Event()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
# Occurrences: Lines 612-616 (2 instances)

self._received_own_sigterm = threading.Event()

# ==================================================
# Line: 703

self._received_own_sigterm_time = time.time()

# ==================================================
# Line: 712

self._received_own_sigterm_time = time.time()

# ==================================================
# Occurrences: Lines 908-910 (2 instances)

run_begin_time = time.time()

# ==================================================
# Line: 1068

start_time = time.monotonic()

# ==================================================
# Line: 1076

end_time = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
# Occurrences: Lines 189-189 (3 instances)

fetched = d.extended.read_var(v)

# ==================================================
# Occurrences: Lines 197-197 (3 instances)

after_list.append(d.extended.read_var(v))

# ==================================================
# Occurrences: Lines 246-246 (3 instances)

fetched = d.extended.read_var(v)

# ==================================================
# Occurrences: Lines 253-253 (3 instances)

after_list.append(d.extended.read_var(v))

# ==================================================
# Occurrences: Lines 363-367 (2 instances)

iterator = iter(iterable)

# ==================================================
# Occurrences: Lines 374-378 (2 instances)

iterator = iter(iterable)

# ==================================================
# Occurrences: Lines 397-400 (2 instances)

next_element = iterator.get_next()

# ==================================================
# Occurrences: Lines 407-410 (2 instances)

next_element = iterator.get_next()

# ==================================================
# Occurrences: Lines 417-421 (2 instances)

next_element = iterator.get_next()

# ==================================================
# Occurrences: Lines 478-485 (3 instances)

x_1, y_1 = run_and_concatenate(strategy, i)

# ==================================================
# Occurrences: Lines 759-761 (2 instances)

a = array_ops.identity(1.)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
# Occurrences: Lines 566-569 (2 instances)

if not cluster_resolver.cluster_spec():

# ==================================================
# Occurrences: Lines 654-655 (2 instances)

v = next_creator(**kwargs)

# ==================================================
# Occurrences: Lines 678-679 (2 instances)

v = next_creator(**kwargs)

# ==================================================
# Line: 768

initial_value = initial_value()

# ==================================================
# Line: 837

value = initial_value()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_values.py
# Line: 281

tpu_context = tpu_util.enclosing_tpu_context()

# ==================================================
# Line: 292

if (tpu_util.enclosing_tpu_context() and

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_replicated_variable_test.py
# Occurrences: Lines 52-53 (2 instances)

x = np.random.rand(batch_size, num_feature_in).astype(np.float32)

# ==================================================
# Occurrences: Lines 63-76 (5 instances)

result = self.evaluate(w.read_value())

# ==================================================
# Occurrences: Lines 95-96 (2 instances)

x = np.random.rand(batch_size, num_feature_in).astype(np.float32)

# ==================================================
# Line: 102

before_save = self.evaluate(w.read_value())

# ==================================================
# Occurrences: Lines 110-114 (2 instances)

save_path = ckpt.save(file_prefix=prefix, options=ckpt_options)

# ==================================================
# Line: 121

after_restore = self.evaluate(w.read_value())

# ==================================================
# Occurrences: Lines 127-143 (6 instances)

y = np.random.rand(batch_size, num_feature_in).astype(np.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
# Occurrences: Lines 600-606 (5 instances)

return ops.executing_eagerly_outside_functions()

# ==================================================
# Occurrences: Lines 612-614 (3 instances)

in_scope = ops.executing_eagerly_outside_functions()

# ==================================================
# Occurrences: Lines 939-944 (2 instances)

self.evaluate(distribution.experimental_local_results(
    distribution.extended.call_for_each_replica(model_fn)))

# ==================================================
# Occurrences: Lines 1300-1302 (2 instances)

a = constant_op.constant(1.)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
# Line: 131

worker_config = config_pb2.ConfigProto()

# ==================================================
# Occurrences: Lines 149-152 (2 instances)

ps_config = config_pb2.ConfigProto()

# ==================================================
# Line: 194

self._cluster_spec = cluster_resolver.cluster_spec().as_dict()

# ==================================================
# Line: 203

cluster_spec = cluster_resolver.cluster_spec()

# ==================================================
# Occurrences: Lines 318-319 (2 instances)

self._start_events[task_type][task_id] = self._mpr_manager.Event()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/shared_variable_creator_test.py
# Occurrences: Lines 57-63 (3 instances)

v0 = variable_v1.VariableV1(1.0, name="foo")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/experimental/multi_worker_mirrored_strategy_test.py
# Occurrences: Lines 141-149 (5 instances)

strategy1 = mwms.MultiWorkerMirroredStrategy()

# ==================================================
# Occurrences: Lines 266-273 (3 instances)

replica_context = distribute_lib.get_replica_context()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
# Occurrences: Lines 107-115 (5 instances)

strategy1 = mirrored_strategy.MirroredStrategy(mesh=self.mesh)

# ==================================================
# Occurrences: Lines 295-302 (3 instances)

replica_context = distribute_lib.get_replica_context()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
# Line: 416

server = rpc_ops.GrpcServer(address)

# ==================================================
# Line: 426

t = threading.Thread(target=start_server)

# ==================================================
# Line: 438

error_code, _ = result_or.get_error()

# ==================================================
# Line: 467

error_code, error_message = result_or.get_error()

# ==================================================
# Line: 476

error_code, _ = result_or.get_error()

# ==================================================
# Occurrences: Lines 482-483 (2 instances)

server = rpc_ops.GrpcServer(address)

# ==================================================
# Occurrences: Lines 592-599 (2 instances)

handle = client.call(
    "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])

# ==================================================
# Line: 616

handle = client.call(
    "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])

# ==================================================
# Line: 625

handle = client.call(
    "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])

# ==================================================
# Occurrences: Lines 724-728 (2 instances)

result_or = client.call("assign_add",
                        [variables.Variable(2, dtype=dtypes.int64)])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
# Occurrences: Lines 380-392 (2 instances)

status_or, deleter = gen_rpc_ops.rpc_call(
    client_handle,
    args=validate_and_get_flat_inputs(*args),
    method_name=method_name,
    timeout_in_ms=timeout_in_ms)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
# Line: 84

before_save = dvar_test.evaluate(v.read_value())

# ==================================================
# Occurrences: Lines 92-96 (2 instances)

save_path = checkpoint.save(file_prefix=prefix, options=ckpt_options)

# ==================================================
# Line: 102

after_restore = dvar_test.evaluate(v)

# ==================================================
# Occurrences: Lines 108-119 (4 instances)

before_save_1 = dvar_test.evaluate(v.read_value())

# ==================================================
# Occurrences: Lines 251-253 (2 instances)

in_dist_copy = copy.deepcopy(v)

# ==================================================
# Line: 629

val = v1._get()

# ==================================================
# Line: 635

val = v1._get()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
# Occurrences: Lines 339-344 (2 instances)

restore_on_create.v = variables.Variable(0.)

# ==================================================
# Occurrences: Lines 379-381 (2 instances)

x = self.device.pack(x_parts)

# ==================================================
# Occurrences: Lines 414-419 (2 instances)

single_device_loaded = load.load(saved_model_path)

# ==================================================
# Occurrences: Lines 428-429 (2 instances)

parallel_result = computation()

# ==================================================
# Line: 475

captured_value = constant_op.constant(2.)

# ==================================================
# Occurrences: Lines 489-493 (6 instances)

initial_value = constant_op.constant(2.)

# ==================================================
# Occurrences: Lines 525-526 (2 instances)

y = layer(x)

# ==================================================
# Occurrences: Lines 537-538 (2 instances)

y = layer(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
# Line: 103

return distribution.group(update)

# ==================================================
# Line: 117

update = distribution.group(update)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/per_replica_test.py
# Line: 88

f(per_replica)

# ==================================================
# Line: 98

output = f(per_replica)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
# Occurrences: Lines 134-142 (3 instances)

result = super(PackedDistributedVariable, self).is_initialized(name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
# Line: 304

iterator = iter(ds)

# ==================================================
# Occurrences: Lines 310-312 (2 instances)

_check_type_spec_structure(iter(ds))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
# Occurrences: Lines 819-822 (2 instances)

data = range(0, strategy.num_replicas_in_sync)

# ==================================================
# Occurrences: Lines 1143-1150 (5 instances)

x = random_ops.random_normal((10240, 10240))

# ==================================================
# Occurrences: Lines 1167-1171 (3 instances)

w = variables.Variable(array_ops.identity(x))

# ==================================================
# Occurrences: Lines 1577-1582 (2 instances)

tpu_variable = variables.Variable(1.0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mwms_pjrt_gpu_test.py
# Occurrences: Lines 83-84 (6 instances)

input_tensor1 = array_ops.identity(f(constant))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/zero_batch_test.py
# Occurrences: Lines 49-54 (4 instances)

inputs = np.random.random((0, 4, 4, 3)) + 100

# ==================================================
# Occurrences: Lines 79-84 (2 instances)

moving_mean, moving_var = self.evaluate(
    [bn.moving_mean, bn.moving_variance])

# ==================================================
# Occurrences: Lines 96-101 (2 instances)

moving_mean, moving_var = self.evaluate(
    [bn.moving_mean, bn.moving_variance])

# ==================================================
# Occurrences: Lines 119-120 (2 instances)

inputs = np.random.random((0, 4, 4, 3)).astype(np.float32) + 100

# ==================================================
# Occurrences: Lines 171-172 (2 instances)

inputs = np.random.random((11, 4, 4, 3)).astype(np.float32) + 100

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/numpy_dataset.py
# Occurrences: Lines 39-40 (2 instances)

start_placeholder = array_ops.placeholder(dtypes.int64, ())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
# Occurrences: Lines 471-473 (2 instances)

pid = mpr.get_process_id('worker', 1)

# ==================================================
# Occurrences: Lines 557-567 (4 instances)

pid = runner.run(fn_that_returns_pid)

# ==================================================
# Line: 617

num_gpus = len(context.context().list_physical_devices('GPU'))

# ==================================================
# Occurrences: Lines 631-645 (5 instances)

result = runner.join()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/strategy_common_test.py
# Line: 492

value = indexed_slices.IndexedSlices(
    values=array_ops.identity([[1.0]]),
    indices=array_ops.identity([0]),
    dense_shape=array_ops.identity([5, 1]))

# ==================================================
# Line: 506

expect = indexed_slices.IndexedSlices(
    values=array_ops.identity([[1.0]]),
    indices=array_ops.identity([0]),
    dense_shape=array_ops.identity([5, 1]))

# ==================================================
# Occurrences: Lines 657-660 (2 instances)

run(input_iterator)

# ==================================================
# Occurrences: Lines 685-687 (2 instances)

run(input_iterator)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
# Occurrences: Lines 41-50 (3 instances)

job = cluster_def.job.add()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/metric_utils.py
# Occurrences: Lines 96-99 (2 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test_base.py
# Occurrences: Lines 74-75 (2 instances)

data = random_ops.random_uniform((10, 10))

# ==================================================
# Occurrences: Lines 82-93 (6 instances)

self.iterator = iter(
    self.cluster_coord.create_per_worker_dataset(distribute_dataset_fn))

# ==================================================
# Line: 185

running_threads = test_util.get_running_threads()

# ==================================================
# Line: 204

running_threads = test_util.get_running_threads()

# ==================================================
# Occurrences: Lines 257-264 (4 instances)

x = random_ops.random_uniform((2, 10))

# ==================================================
# Occurrences: Lines 271-274 (8 instances)

x = random_ops.random_uniform((1000, 1000))

# ==================================================
# Occurrences: Lines 610-611 (4 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 625-630 (2 instances)

self.thread_coord = thread_coordinator.Coordinator(
    clean_stop_exception_types=[])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
# Occurrences: Lines 118-120 (2 instances)

t1 = threading.Thread(target=process_queue, daemon=True)

# ==================================================
# Occurrences: Lines 157-158 (2 instances)

first_fn_done = threading.Event()

# ==================================================
# Occurrences: Lines 229-232 (2 instances)

closure1 = self._create_closure(closure_queue._cancellation_mgr)

# ==================================================
# Line: 310

closure_queue.put(self._create_closure(closure_queue._cancellation_mgr))

# ==================================================
# Line: 325

closure3 = self._create_closure(closure_queue._cancellation_mgr)

# ==================================================
# Occurrences: Lines 422-424 (3 instances)

closure1 = self._create_closure(queue._cancellation_mgr)

# ==================================================
# Occurrences: Lines 614-620 (4 instances)

result = self.coordinator.schedule(
    worker_fn, args=(iter(distributed_dataset),))

# ==================================================
# Occurrences: Lines 798-798 (2 instances)

result_sum = sum(var.read_all()).numpy()

# ==================================================
# Occurrences: Lines 811-811 (2 instances)

result_sum = sum(var.read_all()).numpy()

# ==================================================
# Line: 883

per_worker_dataset1 = self.coordinator.create_per_worker_dataset(input_fn1)

# ==================================================
# Line: 896

per_worker_dataset3 = self.coordinator.create_per_worker_dataset(input_fn1)

# ==================================================
# Occurrences: Lines 908-909 (2 instances)

per_worker_dataset1 = self.coordinator.create_per_worker_dataset(input_fn)

# ==================================================
# Occurrences: Lines 918-922 (4 instances)

result = self.coordinator.schedule(
    worker_fn, args=(per_worker_iterator1, per_worker_iterator2))

# ==================================================
# Occurrences: Lines 1004-1007 (5 instances)

x = random_ops.random_uniform((1000, 1000))

# ==================================================
# Occurrences: Lines 1330-1337 (2 instances)

result = self.coordinator.schedule(
    worker_fn, args=(constant_op.constant(3.),))

# ==================================================
# Occurrences: Lines 1369-1376 (2 instances)

result = self.coordinator.schedule(
    worker_fn, args=(constant_op.constant(3.),))

# ==================================================
# Occurrences: Lines 1416-1418 (2 instances)

v.read_value()  # Reads value 1.0

# ==================================================
# Occurrences: Lines 1439-1441 (6 instances)

t = v.read_value()  # Reads value 1.0

# ==================================================
# Line: 1447

result = result.fetch()

# ==================================================
# Line: 1453

self.assertEqual(v.read_value(), 4.0)

# ==================================================
# Occurrences: Lines 1460-1462 (6 instances)

t = v.read_value()  # Reads value 2.0 ==> Should be cached

# ==================================================
# Line: 1469

result = result.fetch()

# ==================================================
# Line: 1477

v.read_value()

# ==================================================
# Occurrences: Lines 1484-1489 (2 instances)

dataset_fn = lambda _: dataset_ops.DatasetV2.range(1, 11).batch(4)

# ==================================================
# Occurrences: Lines 1511-1515 (2 instances)

dataset_fn = lambda _: dataset_ops.DatasetV2.range(1, 11).batch(4)

# ==================================================
# Occurrences: Lines 1645-1647 (2 instances)

lambda _: dataset_ops.DatasetV2.from_tensor_slices([1, 2]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
# Occurrences: Lines 335-342 (3 instances)

self._queue_lock = threading.Lock()

# ==================================================
# Occurrences: Lines 349-352 (2 instances)

self._queue_free_slot_condition = threading.Condition(self._queue_lock)

# ==================================================
# Line: 377

self._put_wait_lock = threading.Lock()

# ==================================================
# Line: 1289

self._potential_ps_failures_lock = threading.Lock()

# ==================================================
# Line: 1301

self._transient_timeouts_lock = threading.Lock()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/metric_utils_test.py
# Occurrences: Lines 37-40 (5 instances)

x = random_ops.random_uniform((1000, 1000))

# ==================================================
# Occurrences: Lines 105-106 (2 instances)

self.coordinator.schedule(func, args=None, kwargs=None)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distribute_utils.py
# Line: 132

if same_id and not always_wrap and value_container(v0) is v0:

# ==================================================
# Occurrences: Lines 143-147 (2 instances)

value_container(v0) is not v0):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_run.py
# Occurrences: Lines 332-333 (2 instances)

self.should_run = threading.Event()

# ==================================================
# Occurrences: Lines 344-347 (2 instances)

self.graph = ops.get_default_graph()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/values_v2_test.py
# Occurrences: Lines 209-210 (2 instances)

v = self.create_variable()

# ==================================================
# Occurrences: Lines 220-221 (2 instances)

v = self.create_variable()

# ==================================================
# Occurrences: Lines 227-229 (2 instances)

v = self.create_variable(1.)

# ==================================================
# Occurrences: Lines 236-237 (2 instances)

v = self.create_variable(1.)

# ==================================================
# Occurrences: Lines 343-344 (2 instances)

v = self.create_variable()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
# Line: 640

out = tensor_format.numeric_summary(x)

# ==================================================
# Line: 646

out = tensor_format.numeric_summary(x)

# ==================================================
# Line: 656

out = tensor_format.numeric_summary(x)

# ==================================================
# Line: 686

out = tensor_format.numeric_summary(x)

# ==================================================
# Occurrences: Lines 692-702 (3 instances)

out = tensor_format.numeric_summary(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
# Occurrences: Lines 98-103 (3 instances)

graph = test.mock.MagicMock()

# ==================================================
# Occurrences: Lines 124-133 (4 instances)

device1 = run_metadata.step_stats.dev_stats.add()

# ==================================================
# Occurrences: Lines 195-200 (3 instances)

graph = test.mock.MagicMock()

# ==================================================
# Occurrences: Lines 247-252 (3 instances)

graph = test.mock.MagicMock()

# ==================================================
# Occurrences: Lines 301-306 (3 instances)

graph = test.mock.MagicMock()

# ==================================================
# Occurrences: Lines 332-338 (4 instances)

self.loop_cond_lineno = _line_number_above()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
# Line: 157

num_dumped_tensors = int(next(line_iter).split(" ")[0])

# ==================================================
# Occurrences: Lines 163-175 (4 instances)

next(line_iter))

# ==================================================
# Occurrences: Lines 312-351 (16 instances)

tst.assertEqual("Node %s" % node_name, next(line_iter))

# ==================================================
# Occurrences: Lines 358-368 (4 instances)

tst.assertEqual("", next(line_iter))

# ==================================================
# Occurrences: Lines 375-396 (12 instances)

tst.assertEqual("", next(line_iter))

# ==================================================
# Occurrences: Lines 409-411 (3 instances)

tst.assertEqual("", next(line_iter))

# ==================================================
# Line: 417

line = next(line_iter)

# ==================================================
# Line: 434

next(line_iter))

# ==================================================
# Occurrences: Lines 593-594 (2 instances)

cls._dump_root = tempfile.mkdtemp()

# ==================================================
# Occurrences: Lines 616-626 (4 instances)

cls._u_line_number = line_number_above()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
# Line: 521

column_widths[col], len(profile_data.value(
    row,
    col,
    device_name_filter=device_name_filter,
    node_name_filter=node_name_filter,
    op_type_filter=op_type_filter)))

# ==================================================
# Line: 555

new_cell = profile_data.value(
    row,
    col,
    device_name_filter=device_name_filter,
    node_name_filter=node_name_filter,
    op_type_filter=op_type_filter)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/tensor_format.py
# Line: 127

lines.extend(repr(tensor).split("\n"))

# ==================================================
# Line: 151

array_lines = repr(tensor).split("\n")

# ==================================================
# Occurrences: Lines 240-245 (2 instances)

ndims = len(dims)

# ==================================================
# Occurrences: Lines 361-364 (2 instances)

num_matches = len(matching_indices_list)

# ==================================================
# Occurrences: Lines 383-386 (2 instances)

num_matches = len(matching_indices_list)

# ==================================================
# Occurrences: Lines 461-466 (4 instances)

if match.start() > ellipsis_index:

# ==================================================
# Occurrences: Lines 505-512 (8 instances)

count_val_str = str(count_val)

# ==================================================
# Line: 545

output = _counts_summary(counts, total_count=np.size(tensor))

# ==================================================
# Line: 561

return _counts_summary(counts, total_count=np.size(tensor))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/evaluator.py
# Line: 73

split_items = debug_tensor_name.split(":")

# ==================================================
# Occurrences: Lines 91-96 (3 instances)

output_slot = int(split_items[1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
# Occurrences: Lines 559-559 (2 instances)

op_type = self._debug_dump.node_op_type(dump.node_name)

# ==================================================
# Occurrences: Lines 566-566 (2 instances)

op_type = self._debug_dump.node_op_type(dump.node_name)

# ==================================================
# Occurrences: Lines 699-730 (11 instances)

(0, len(row), [debugger_cli_common.MenuItem(None, command), "bold"]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/cli_config_test.py
# Line: 48

config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)

# ==================================================
# Line: 56

config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)

# ==================================================
# Occurrences: Lines 79-82 (2 instances)

config = cli_config.CLIConfig(config_file_path=self._tmp_config_path)

# ==================================================
# Occurrences: Lines 112-117 (3 instances)

test_value["graph_recursion_depth"] = config.get("graph_recursion_depth")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
# Line: 634

rich_lines = debugger_cli_common.RichTextLines(["Violets are blue"])

# ==================================================
# Line: 641

rich_lines = debugger_cli_common.RichTextLines(["Violets are blue"])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
# Occurrences: Lines 467-467 (2 instances)

if len(line) <= cols:

# ==================================================
# Occurrences: Lines 483-485 (9 instances)

while idx < len(line):

# ==================================================
# Line: 744

lines = self._get_help_for_command_prefix(cmd_prefix)

# ==================================================
# Line: 751

return RichTextLines(self._get_help_for_command_prefix(cmd_prefix))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
# Line: 925

dump = debug_data.DebugDumpDir(
    self._dump_root, partition_graphs=run_metadata.partition_graphs)

# ==================================================
# Line: 955

dump = debug_data.DebugDumpDir(
    self._dump_root, partition_graphs=run_metadata.partition_graphs)

# ==================================================
# Line: 974

debug_data.DebugDumpDir(
    self._dump_root, partition_graphs=run_metadata.partition_graphs)

# ==================================================
# Line: 1328

run_options = config_pb2.RunOptions(output_partition_graphs=True)

# ==================================================
# Line: 1341

run_options = config_pb2.RunOptions(output_partition_graphs=True)

# ==================================================
# Line: 1354

run_options = config_pb2.RunOptions(output_partition_graphs=True)

# ==================================================
# Line: 1458

dump.node_traceback("traceback/w")

# ==================================================
# Line: 1470

traceback = dump.node_traceback("traceback/w")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
# Occurrences: Lines 83-90 (4 instances)

a_lineno = line_number_above()

# ==================================================
# Occurrences: Lines 123-130 (4 instances)

a_lineno = line_number_above()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/source_utils.py
# Occurrences: Lines 258-259 (2 instances)

path_to_node_names = collections.defaultdict(set)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
# Occurrences: Lines 111-114 (4 instances)

self._source_file_paths_lock = threading.Lock()

# ==================================================
# Occurrences: Lines 498-516 (8 instances)

tensor_proto = _concrete_tensor_to_proto(
    gen_debug_ops.debug_numeric_summary_v2(
        tensor,
        tensor_debug_mode=tensor_debug_mode,
        output_dtype=dtypes.float64))

# ==================================================
# Occurrences: Lines 565-570 (2 instances)

if outputs and compat.as_bytes(
    op_type) not in op_callbacks_common.OP_CALLBACK_SKIP_OPS:

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
# Occurrences: Lines 226-230 (2 instances)

self.assertFalse(reader.executions())

# ==================================================
# Occurrences: Lines 371-374 (2 instances)

lines[i] = reader.source_lines("localhost", "/tmp/file_%d.py" % i)

# ==================================================
# Occurrences: Lines 436-444 (4 instances)

execution_digests = reader.executions(digest=True)

# ==================================================
# Occurrences: Lines 522-528 (4 instances)

digests = reader.graph_execution_traces(digest=True)

# ==================================================
# Occurrences: Lines 615-620 (4 instances)

graph_op_creation = debug_event_pb2.GraphOpCreation(
    op_type="FooOp", op_name=op_name, graph_id="graph1")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
# Occurrences: Lines 199-209 (3 instances)

graph_cpu_0 = graph_pb2.GraphDef()

# ==================================================
# Occurrences: Lines 236-251 (5 instances)

graph_cpu_0 = graph_pb2.GraphDef()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
# Occurrences: Lines 85-87 (2 instances)

run_metadata = config_pb2.RunMetadata()

# ==================================================
# Occurrences: Lines 94-96 (2 instances)

run_metadata = config_pb2.RunMetadata()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
# Occurrences: Lines 155-168 (5 instances)

self.u_init_line_number = line_number_above()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
# Line: 145

self.assertFalse(reader.executions())

# ==================================================
# Line: 151

executions = reader.executions()

# ==================================================
# Line: 296

tensor_id = reader.graph_execution_trace_to_tensor_id(trace)

# ==================================================
# Line: 307

tensor_id = reader.graph_execution_trace_to_tensor_id(trace)

# ==================================================
# Line: 323

tensor_id = reader.graph_execution_trace_to_tensor_id(trace)

# ==================================================
# Line: 338

tensor_id = reader.graph_execution_trace_to_tensor_id(trace)

# ==================================================
# Occurrences: Lines 1050-1051 (2 instances)

dumping_callback.enable_dump_debug_info(self.dump_root)

# ==================================================
# Line: 1205

tensor_values = [reader.graph_execution_trace_to_tensor_value(trace)

# ==================================================
# Occurrences: Lines 1212-1217 (2 instances)

tensor_id = reader.graph_execution_trace_to_tensor_id(trace)

# ==================================================
# Line: 1224

tensor_id = reader.graph_execution_trace_to_tensor_id(trace)

# ==================================================
# Occurrences: Lines 1237-1238 (2 instances)

tensor_id = reader.graph_execution_trace_to_tensor_id(trace)

# ==================================================
# Line: 1246

reader.graph_execution_trace_to_tensor_value(trace)

# ==================================================
# Line: 1295

exec_digests = reader.executions(digest=True)

# ==================================================
# Line: 1308

exec_digests = reader.executions(digest=True)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
# Occurrences: Lines 118-118 (2 instances)

tensor_value = tensor_util.MakeNdarray(trace.tensor_proto)

# ==================================================
# Occurrences: Lines 129-129 (2 instances)

tensor_value = tensor_util.MakeNdarray(trace.tensor_proto)

# ==================================================
# Occurrences: Lines 406-417 (4 instances)

tensor, tensor_id = debug_summary(constant_op.constant(x))

# ==================================================
# Occurrences: Lines 433-435 (3 instances)

c = constant_op.constant(x)

# ==================================================
# Occurrences: Lines 441-449 (5 instances)

c = constant_op.constant(x)

# ==================================================
# Occurrences: Lines 527-538 (4 instances)

tensor, tensor_id = debug_summary(constant_op.constant(x))

# ==================================================
# Occurrences: Lines 557-564 (4 instances)

tensor_1, tensor_id_1 = debug_summary(c)

# ==================================================
# Line: 595

tensor, tensor_id = debug_summary(constant_op.constant(x))

# ==================================================
# Line: 601

tensor, tensor_id = debug_summary(constant_op.constant(x))

# ==================================================
# Line: 607

tensor, tensor_id = debug_summary(constant_op.constant(x))

# ==================================================
# Line: 710

tensor, tensor_id = debug_summary(constant_op.constant(x))

# ==================================================
# Occurrences: Lines 720-724 (2 instances)

tensor, tensor_id = debug_summary(constant_op.constant(x))

# ==================================================
# Line: 733

tensor, tensor_id = debug_summary(constant_op.constant(x))

# ==================================================
# Occurrences: Lines 754-756 (3 instances)

c = constant_op.constant(x)

# ==================================================
# Occurrences: Lines 764-766 (3 instances)

c = constant_op.constant(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
# Occurrences: Lines 210-211 (2 instances)

x = constant_op.constant(2.0, dtype=dtypes.float64)

# ==================================================
# Occurrences: Lines 412-413 (2 instances)

scale = constant_op.constant([1], dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
# Occurrences: Lines 76-81 (2 instances)

w_grad = grad_debugger.gradient_tensor(self.w.name)

# ==================================================
# Occurrences: Lines 107-112 (2 instances)

w_grad = grad_debugger.gradient_tensor(self.w.name)

# ==================================================
# Occurrences: Lines 124-125 (2 instances)

grad_debugger_1 = debug_gradients.GradientsDebugger()

# ==================================================
# Occurrences: Lines 152-153 (2 instances)

grad_debugger_1 = debug_gradients.GradientsDebugger()

# ==================================================
# Occurrences: Lines 311-315 (2 instances)

grad_debugger_1 = debug_gradients.GradientsDebugger()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/wrappers/framework.py
# Occurrences: Lines 455-465 (3 instances)

return callable_runner(*callable_runner_args)

# ==================================================
# Occurrences: Lines 485-497 (3 instances)

retvals = callable_runner(*callable_runner_args)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper.py
# Line: 106

fetches_event = event_pb2.Event()

# ==================================================
# Line: 114

feed_keys_event = event_pb2.Event()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
# Line: 232

run_info_output = wrapped_sess._run_info_handler([])

# ==================================================
# Line: 243

run_info_output = wrapped_sess._run_info_handler([])

# ==================================================
# Occurrences: Lines 390-391 (2 instances)

ph1 = array_ops.placeholder(dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/pprof_profiler_test.py
# Occurrences: Lines 47-48 (2 instances)

graph = test.mock.MagicMock()

# ==================================================
# Line: 62

run_metadata = config_pb2.RunMetadata()

# ==================================================
# Occurrences: Lines 70-76 (3 instances)

run_metadata = config_pb2.RunMetadata()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/profile_context_test.py
# Line: 44

profile_step100 = os.path.join(test.get_temp_dir(), "profile_100")

# ==================================================
# Occurrences: Lines 58-67 (3 instances)

profile_str = f.read()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
# Line: 100

dump_str = lib.CheckAndRemoveDoc(f.read())

# ==================================================
# Occurrences: Lines 109-109 (2 instances)

metrics = o[o.find('(') + 1:o.find(')')].split(',')

# ==================================================
# Occurrences: Lines 134-134 (2 instances)

metrics = o[o.find('(') + 1:o.find(')')].split(',')

# ==================================================
# Line: 146

self.assertEqual(dump_str, lib.CheckAndRemoveDoc(f.read()))

# ==================================================
# Occurrences: Lines 376-377 (4 instances)

self.assertLessEqual(len(tfprof_node.graph_nodes), last_occurrence)

# ==================================================
# Occurrences: Lines 495-532 (7 instances)

tfprof_node = model_analyzer.profile(
    sess.graph, run_meta=run_meta, options=opts)

# ==================================================
# Line: 560

_ = model_analyzer.profile(sess.graph, run_meta=run_meta, options=opts)

# ==================================================
# Line: 567

_ = model_analyzer.profile(sess.graph, run_meta=run_meta, options=opts)

# ==================================================
# Line: 574

_ = model_analyzer.profile(sess.graph, run_meta=run_meta, options=opts)

# ==================================================
# Occurrences: Lines 586-586 (2 instances)

ret = gfile.ListDirectory(time_dir)

# ==================================================
# Occurrences: Lines 593-595 (4 instances)

self.assertEqual(len(gfile.ListDirectory(time_dir)), 0)

# ==================================================
# Occurrences: Lines 602-604 (4 instances)

self.assertEqual(len(gfile.ListDirectory(memory_dir)), 0)

# ==================================================
# Occurrences: Lines 611-611 (2 instances)

self.assertEqual(len(gfile.ListDirectory(profile_dir)), 0)

# ==================================================
# Occurrences: Lines 708-709 (2 instances)

a = array_ops.constant(np.ones((100, 100)))

# ==================================================
# Line: 717

run_metadata = config_pb2.RunMetadata()

# ==================================================
# Occurrences: Lines 724-730 (3 instances)

ret = model_analyzer.profile(
    sess.graph, run_meta=run_metadata, cmd='scope', options=options)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/profiler_test.py
# Occurrences: Lines 61-96 (8 instances)

profiler_str = f.read()

# ==================================================
# Line: 102

pma_str = f.read()

# ==================================================
# Occurrences: Lines 114-116 (2 instances)

pb0 = profiler.profile_name_scope(opts)

# ==================================================
# Line: 122

pb1 = profiler.profile_name_scope(opts)

# ==================================================
# Line: 128

run_meta2 = config_pb2.RunMetadata()

# ==================================================
# Line: 134

pb2 = profiler.profile_name_scope(opts)

# ==================================================
# Line: 140

run_meta3 = config_pb2.RunMetadata()

# ==================================================
# Line: 146

pb3 = profiler.profile_name_scope(opts)

# ==================================================
# Line: 185

init_var_run_meta = config_pb2.RunMetadata()

# ==================================================
# Line: 191

train_run_meta = config_pb2.RunMetadata()

# ==================================================
# Line: 198

ret1 = profiler.profile_name_scope(opts)

# ==================================================
# Line: 209

ret2 = profiler.profile_name_scope(opts)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/tfprof_logger_test.py
# Occurrences: Lines 26-33 (4 instances)

a = array_ops.placeholder(dtypes.int32, [2, 2])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/model_analyzer.py
# Line: 360

ret = print_mdl.PrintModelAnalysis(graph_str, run_meta_str,
                                   op_log.SerializeToString(),
                                   cmd.encode('utf-8'),
                                   opts.SerializeToString())

# ==================================================
# Line: 371

ret = print_mdl.PrintModelAnalysis(graph_str, run_meta_str,
                                   op_log.SerializeToString(),
                                   cmd.encode('utf-8'),
                                   opts.SerializeToString())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/pprof_profiler.py
# Occurrences: Lines 236-239 (2 instances)

label = sample.label.add()

# ==================================================
# Occurrences: Lines 343-353 (8 instances)

sample_type = pprof_profile.sample_type.add()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/profile_context.py
# Line: 69

ret = self._profiler_run_internal(
    fetches, feed_dict, options, run_metadata)

# ==================================================
# Line: 104

return self._profiler_run_internal(
    fetches, feed_dict, options, run_metadata)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/tfprof_logger.py
# Line: 103

entry = tfprof_log_pb2.OpLogEntry()

# ==================================================
# Line: 128

entry = tfprof_log_pb2.OpLogEntry()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/profiler_v2_test.py
# Occurrences: Lines 61-63 (2 instances)

file_list = gfile.ListDirectory(logdir)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
# Occurrences: Lines 204-207 (4 instances)

if op.name.find('gradients/') > 0 and op.name.find('_grad/') > 0:

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/tensor_test.py
# Occurrences: Lines 123-136 (4 instances)

tensor = constant_op.constant(numpy_tensor)

# ==================================================
# Occurrences: Lines 143-147 (2 instances)

tensor = constant_op.constant(numpy_tensor)

# ==================================================
# Occurrences: Lines 227-229 (2 instances)

tensor_str = str(t)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/benchmarks_test.py
# Occurrences: Lines 96-101 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 823-824 (2 instances)

m = random_ops.random_uniform(shape).cpu()

# ==================================================
# Occurrences: Lines 845-846 (2 instances)

m = random_ops.random_uniform(shape).cpu()

# ==================================================
# Occurrences: Lines 864-865 (2 instances)

m = random_ops.random_uniform(shape).cpu()

# ==================================================
# Occurrences: Lines 875-876 (2 instances)

m = random_ops.random_uniform(shape).cpu()

# ==================================================
# Occurrences: Lines 969-970 (2 instances)

a = array_ops.ones((2, 2))

# ==================================================
# Occurrences: Lines 1471-1472 (2 instances)

inputs = array_ops.ones((1, 1, 1, 1))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/core_test.py
# Occurrences: Lines 114-115 (2 instances)

constant_a = constant_op.constant(1.0)

# ==================================================
# Occurrences: Lines 124-125 (2 instances)

variable_a = variables.Variable(1.0)

# ==================================================
# Occurrences: Lines 135-136 (2 instances)

numpy_a = np.array(1.0)

# ==================================================
# Occurrences: Lines 165-166 (2 instances)

constant_a = constant_op.constant(float('nan'))

# ==================================================
# Occurrences: Lines 175-176 (2 instances)

variable_a = variables.Variable(float('nan'))

# ==================================================
# Occurrences: Lines 185-186 (2 instances)

numpy_a = np.array(float('nan'))

# ==================================================
# Occurrences: Lines 199-203 (4 instances)

tf_a = constant_op.constant([1, 2])

# ==================================================
# Occurrences: Lines 278-284 (4 instances)

tf_a = constant_op.constant([1, 1])

# ==================================================
# Occurrences: Lines 537-540 (4 instances)

x = x.cpu()

# ==================================================
# Occurrences: Lines 550-553 (4 instances)

x = x.cpu()

# ==================================================
# Occurrences: Lines 599-605 (4 instances)

test_var = variables.Variable(2.)

# ==================================================
# Occurrences: Lines 969-972 (2 instances)

x = truncated_normal(shape).gpu()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/backprop.py
# Occurrences: Lines 569-569 (2 instances)

flat_result = nest.flatten(result)

# ==================================================
# Occurrences: Lines 578-578 (2 instances)

this_tape, nest.flatten(result), sources, output_gradients=dy)

# ==================================================
# Line: 1151

target_shape = array_ops.shape(target)

# ==================================================
# Line: 1166

target_size = array_ops.shape(target)[0]

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/pywrap_tensor_test.py
# Occurrences: Lines 45-47 (2 instances)

layer = my_layer(x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/wrap_function_test.py
# Occurrences: Lines 251-255 (2 instances)

x = constant_op.constant(1.)

# ==================================================
# Occurrences: Lines 264-268 (2 instances)

x = constant_op.constant(1.)

# ==================================================
# Occurrences: Lines 314-315 (2 instances)

v0 = variables.Variable(0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/remote_benchmarks_test.py
# Occurrences: Lines 47-52 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 77-79 (2 instances)

self._cached_server1 = server_lib.Server.create_local_server()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/backprop_test.py
# Line: 307

x = array_ops.ones((batch_size), dtypes.int64)

# ==================================================
# Line: 319

tf_x = array_ops.ones((batch_size), dtypes.int64)

# ==================================================
# Occurrences: Lines 451-456 (2 instances)

a_2_by_2 = constant_op.constant(2.0, shape=[2, 2])

# ==================================================
# Occurrences: Lines 542-547 (2 instances)

grad = t.gradient(loss, v1)

# ==================================================
# Occurrences: Lines 578-579 (2 instances)

x1 = resource_variable_ops.ResourceVariable(2.0, trainable=False)

# ==================================================
# Occurrences: Lines 1050-1051 (2 instances)

x = constant_op.constant(1.0)

# ==================================================
# Occurrences: Lines 1327-1332 (6 instances)

y = c(x)

# ==================================================
# Occurrences: Lines 1425-1426 (2 instances)

grad1 = get_grad()

# ==================================================
# Occurrences: Lines 1432-1433 (2 instances)

x1 = resource_variable_ops.ResourceVariable(1.0)

# ==================================================
# Occurrences: Lines 1451-1452 (2 instances)

x1 = constant_op.constant(3.0)

# ==================================================
# Occurrences: Lines 1633-1634 (4 instances)

a = math_ops.cos(x)

# ==================================================
# Line: 1838

def_function.function(_inner), [array_ops.ones([10, 4, 4, 1])])

# ==================================================
# Line: 1844

x = array_ops.ones([10, 4, 4, 1])

# ==================================================
# Occurrences: Lines 1863-1868 (2 instances)

x = array_ops.zeros([3])

# ==================================================
# Occurrences: Lines 1876-1881 (2 instances)

x = array_ops.zeros([3])

# ==================================================
# Occurrences: Lines 2048-2050 (4 instances)

x = constant_op.constant([[2.]], dtype=dtype)

# ==================================================
# Occurrences: Lines 2056-2058 (4 instances)

x = constant_op.constant([[2.]], dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/small_constants_optimizer_test.py
# Occurrences: Lines 44-47 (4 instances)

x = constant_op.constant(1)

# ==================================================
# Occurrences: Lines 54-63 (6 instances)

left = constant_op.constant(True)

# ==================================================
# Occurrences: Lines 76-79 (4 instances)

x = constant_op.constant(1)

# ==================================================
# Occurrences: Lines 140-143 (4 instances)

x = constant_op.constant(1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/graph_only_ops_test.py
# Occurrences: Lines 34-35 (2 instances)

x = np.array([42])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/lift_to_graph.py
# Line: 244

op_map = op_map or object_identity.ObjectIdentityDictionary()

# ==================================================
# Line: 301

inverse_captures = object_identity.ObjectIdentityDictionary()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/memory_tests/memory_test_util.py
# Line: 56

instance_count_by_class_before = _instance_count_by_class()

# ==================================================
# Line: 69

_instance_count_by_class() - instance_count_by_class_before)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
# Occurrences: Lines 40-43 (2 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
# Occurrences: Lines 47-51 (4 instances)

a_2_by_2 = random_ops.random_uniform((2, 2))

# ==================================================
# Occurrences: Lines 125-126 (2 instances)

a_2_by_2 = random_ops.random_uniform((2, 2))

# ==================================================
# Occurrences: Lines 140-141 (2 instances)

a_2_by_2 = random_ops.random_uniform((2, 2))

# ==================================================
# Occurrences: Lines 160-161 (2 instances)

a_2_by_2 = random_ops.random_uniform((2, 2))

# ==================================================
# Occurrences: Lines 175-176 (2 instances)

a_2_by_2 = random_ops.random_uniform((2, 2))

# ==================================================
# Line: 307

fastpath_dtype = test_ops.dtype_with_default_op(im).numpy()

# ==================================================
# Line: 314

graph_dtype_symbolic = test_ops.dtype_with_default_op(im)

# ==================================================
# Line: 325

return test_ops.dtype_with_default_op(im)

# ==================================================
# Line: 333

return test_ops.dtype_with_default_op(im)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/remote_test.py
# Occurrences: Lines 77-82 (2 instances)

b = constant_op.constant([1])

# ==================================================
# Occurrences: Lines 442-443 (2 instances)

unused_values.append(array_ops.zeros(shape))

# ==================================================
# Occurrences: Lines 475-479 (4 instances)

read0 = resource_variable_ops.read_variable_op(
    packed_var, dtype=dtypes.float32)

# ==================================================
# Line: 641

output = self.evaluate(func())

# ==================================================
# Line: 647

output = self.evaluate(func())

# ==================================================
# Line: 677

v1 = variables.Variable(initial_value=0)

# ==================================================
# Line: 686

v2 = variables.Variable(initial_value=0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/monitoring_test.py
# Occurrences: Lines 43-44 (2 instances)

counter1 = monitoring.Counter('test/same_counter', 'test counter')  # pylint: disable=unused-variable

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/context_test.py
# Occurrences: Lines 81-85 (2 instances)

return x + constant_op.constant(1.)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compilation_test.py
# Occurrences: Lines 116-118 (4 instances)

loss, count = forward_pass(x)

# ==================================================
# Line: 225

x = random_ops.random_uniform([2, 2]).numpy()

# ==================================================
# Line: 231

x = random_ops.random_uniform([2, 2]).numpy()

# ==================================================
# Line: 237

np_ones = numpy.ones([], numpy.float32)

# ==================================================
# Line: 251

mutable = numpy.ones([], numpy.float32)

# ==================================================
# Line: 284

x = random_ops.random_uniform([2, 2]).numpy()

# ==================================================
# Line: 290

x = random_ops.random_uniform([2, 2]).numpy()

# ==================================================
# Occurrences: Lines 307-312 (3 instances)

return array_ops.ones([10])

# ==================================================
# Line: 327

ones = array_ops.ones([10])

# ==================================================
# Occurrences: Lines 372-375 (2 instances)

v_cpu = resource_variable_ops.ResourceVariable([0.0, 1.0, 2.0])

# ==================================================
# Line: 561

self.assertAllEqual(a, defined(a))

# ==================================================
# Line: 580

out = defined(a)

# ==================================================
# Line: 644

b = array_ops.ones([1])

# ==================================================
# Occurrences: Lines 656-658 (2 instances)

c = array_ops.ones([1])

# ==================================================
# Line: 669

out = foo([a, b], c)

# ==================================================
# Line: 698

out = bar(inputs)

# ==================================================
# Line: 708

out = bar(inputs)

# ==================================================
# Line: 1006

with ops.get_default_graph().as_default():

# ==================================================
# Line: 1016

graph = ops.get_default_graph()

# ==================================================
# Occurrences: Lines 1097-1102 (2 instances)

with ops.get_default_graph().as_default():

# ==================================================
# Line: 1170

with ops.get_default_graph().as_default():

# ==================================================
# Line: 1176

graph = ops.get_default_graph()

# ==================================================
# Line: 1184

graph = ops.get_default_graph()

# ==================================================
# Line: 1196

with ops.get_default_graph().as_default():

# ==================================================
# Line: 1207

graph = ops.get_default_graph()

# ==================================================
# Line: 1219

v = resource_variable_ops.ResourceVariable(0.0)

# ==================================================
# Line: 1227

w = resource_variable_ops.ResourceVariable(0.0)

# ==================================================
# Line: 1366

add_cache = function_cache_lib.FunctionCache()

# ==================================================
# Line: 1372

maybe_add_cache = function_cache_lib.FunctionCache()

# ==================================================
# Line: 1382

x = constant_op.constant(11)

# ==================================================
# Line: 1392

x = constant_op.constant(11)

# ==================================================
# Line: 1398

function_cache = function_cache_lib.FunctionCache()

# ==================================================
# Line: 1409

function_cache = function_cache_lib.FunctionCache()

# ==================================================
# Occurrences: Lines 1453-1454 (2 instances)

a = attr.ib()

# ==================================================
# Occurrences: Lines 1492-1494 (3 instances)

x = resource_variable_ops.ResourceVariable(0.0)

# ==================================================
# Occurrences: Lines 1512-1514 (3 instances)

x = resource_variable_ops.ResourceVariable(0.0)

# ==================================================
# Occurrences: Lines 1542-1544 (3 instances)

x = resource_variable_ops.ResourceVariable(0.0)

# ==================================================
# Occurrences: Lines 1672-1674 (4 instances)

m1 = math_ops.matmul(a, b, transpose_a=transpose_a)

# ==================================================
# Line: 2095

class_op = compiled_method.get_concrete_function(
    tensor_lib.TensorSpec(shape=(), dtype=dtypes.float32)
)

# ==================================================
# Line: 2104

method_op = compiled_method.get_concrete_function(
    tensor_lib.TensorSpec(shape=(), dtype=dtypes.float32)
)

# ==================================================
# Line: 2140

method_op = compiled_method.get_concrete_function()

# ==================================================
# Line: 2146

method_op2 = compiled_method.get_concrete_function()

# ==================================================
# Occurrences: Lines 2227-2237 (9 instances)

s0 = test_ops.device_placement_op()

# ==================================================
# Line: 2244

outputs = self.evaluate(defined())

# ==================================================
# Line: 2253

outputs = self.evaluate(defined())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/concrete_function.py
# Occurrences: Lines 379-384 (2 instances)

self._num_outputs = len(func_graph.outputs)

# ==================================================
# Occurrences: Lines 606-606 (2 instances)

while num_processed_output_tangents != len(output_tangents):

# ==================================================
# Occurrences: Lines 613-613 (2 instances)

num_processed_output_tangents = len(output_tangents)

# ==================================================
# Occurrences: Lines 955-961 (2 instances)

self._build_functions_for_outputs(
    outputs, inference_args, input_tangents)

# ==================================================
# Occurrences: Lines 1329-1334 (2 instances)

flat_outputs = forward_function.call_flat(*args_with_tangents)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# Occurrences: Lines 159-162 (2 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 263-265 (2 instances)

v1 = variables.Variable(1.0)

# ==================================================
# Occurrences: Lines 317-326 (8 instances)

read0 = resource_variable_ops.read_variable_op(
    packed_var_0, dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 343-344 (2 instances)

a = array_ops.placeholder(dtypes.float32, ())

# ==================================================
# Occurrences: Lines 370-371 (2 instances)

a = array_ops.ones((1,))

# ==================================================
# Occurrences: Lines 395-396 (2 instances)

a = variables.Variable((1.0,))

# ==================================================
# Occurrences: Lines 459-460 (2 instances)

a = array_ops.placeholder(dtypes.float32, ())

# ==================================================
# Occurrences: Lines 523-532 (4 instances)

y = test_fn(v)

# ==================================================
# Line: 676

b = variables.Variable(1.0)

# ==================================================
# Line: 683

c = cc[0] = variables.Variable(1.)

# ==================================================
# Occurrences: Lines 855-859 (2 instances)

t1 = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])

# ==================================================
# Occurrences: Lines 1006-1009 (3 instances)

x = f()

# ==================================================
# Occurrences: Lines 1350-1354 (2 instances)

math_ops.add(x, three)

# ==================================================
# Line: 1690

cpu_graph_function = defined.get_concrete_function()

# ==================================================
# Line: 1702

default_graph_function = defined.get_concrete_function()

# ==================================================
# Occurrences: Lines 1714-1717 (2 instances)

x = array_ops.identity(1.0)

# ==================================================
# Occurrences: Lines 1897-1898 (2 instances)

v1 = variables.Variable(1.0)

# ==================================================
# Occurrences: Lines 1936-1941 (2 instances)

with ops.get_default_graph().as_default():

# ==================================================
# Line: 2003

expected_spec = resource_variable_ops.VariableSpec([], alias_id=0)

# ==================================================
# Line: 2010

expected_spec1 = resource_variable_ops.VariableSpec([], alias_id=0)

# ==================================================
# Occurrences: Lines 2041-2042 (2 instances)

x1 = resource_variable_ops.ResourceVariable(0.0)

# ==================================================
# Occurrences: Lines 2059-2072 (6 instances)

x1 = resource_variable_ops.ResourceVariable(0.0)

# ==================================================
# Occurrences: Lines 3719-3723 (2 instances)

self.x = variables.Variable(1., name='v')

# ==================================================
# Occurrences: Lines 4001-4004 (2 instances)

func_a = func.get_concrete_function(
    tensor_lib.TensorSpec([None], dtypes.int32))

# ==================================================
# Occurrences: Lines 4014-4015 (2 instances)

func_a = func.get_concrete_function(constant_op.constant(2.))

# ==================================================
# Occurrences: Lines 4022-4027 (2 instances)

func_c = func.get_concrete_function(constant_op.constant(2.))

# ==================================================
# Line: 4635

float_captured_tensor = constant_op.constant([3.], dtype=dtypes.float32)

# ==================================================
# Line: 4658

new_float_captured_tensor = constant_op.constant([3.], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 4910-4912 (2 instances)

_ = f()

# ==================================================
# Occurrences: Lines 4924-4926 (2 instances)

_ = f()

# ==================================================
# Line: 4950

graph_def = graph.as_graph_def()

# ==================================================
# Line: 4957

updated_graph_def = graph.as_graph_def()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/function_context.py
# Line: 45

executing_eagerly = ctx.executing_eagerly()

# ==================================================
# Occurrences: Lines 59-63 (3 instances)

executing_eagerly = ctx.executing_eagerly()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
# Occurrences: Lines 337-338 (2 instances)

outer_graph = ops.get_default_graph()

# ==================================================
# Line: 350

resource_variable_ops.var_is_initialized_op(self._handle))

# ==================================================
# Line: 381

graph = ops.get_default_graph()

# ==================================================
# Line: 387

resource_variable_ops.var_is_initialized_op(self._handle),

# ==================================================
# Line: 827

tracing_count = self.experimental_get_tracing_count()

# ==================================================
# Line: 835

new_tracing_count = self.experimental_get_tracing_count()

# ==================================================
# Occurrences: Lines 988-991 (2 instances)

concrete_fn = self.get_concrete_function(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
# Occurrences: Lines 82-84 (3 instances)

i1 = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# ==================================================
# Line: 375

x = ops.convert_to_tensor(x)

# ==================================================
# Line: 388

x = ops.convert_to_tensor(x)

# ==================================================
# Occurrences: Lines 745-746 (2 instances)

arg1 = random_ops.random_normal([2])

# ==================================================
# Occurrences: Lines 799-800 (2 instances)

a = random_ops.random_normal([10, 10])

# ==================================================
# Occurrences: Lines 841-842 (2 instances)

a = random_ops.random_normal([2])

# ==================================================
# Occurrences: Lines 951-952 (2 instances)

a = random_ops.random_normal([100, 100])

# ==================================================
# Occurrences: Lines 1081-1082 (2 instances)

orig_nojit = cell_nojit.value()

# ==================================================
# Occurrences: Lines 1089-1092 (3 instances)

self.assertEqual(cell_nojit.value(), orig_nojit + 1)

# ==================================================
# Occurrences: Lines 1098-1099 (2 instances)

self.assertEqual(cell_nojit.value(), orig_nojit + 1)

# ==================================================
# Occurrences: Lines 1111-1112 (2 instances)

self.assertEqual(cell_nojit.value(), orig_nojit + 2)

# ==================================================
# Occurrences: Lines 1124-1125 (2 instances)

self.assertEqual(cell_nojit.value(), orig_nojit + 2)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/saved_model_utils.py
# Occurrences: Lines 79-81 (2 instances)

imported_constant = constant_op.constant(ndarray)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
# Occurrences: Lines 141-146 (2 instances)

traced_f = polymorphic_function.function(f)

# ==================================================
# Line: 155

primal_out = f()

# ==================================================
# Line: 171

self.assertAllClose(expected(two), f())

# ==================================================
# Occurrences: Lines 522-536 (6 instances)

self.assertAllEqual(outer_fn(x), 5.0 * (5.0 + 3.0))

# ==================================================
# Line: 544

grad = tp.gradient(result, y)

# ==================================================
# Line: 551

grad = tp.gradient(result, y)

# ==================================================
# Occurrences: Lines 765-779 (6 instances)

self.assertAllEqual(outer_fn(x), 5.0 * (5.0 + 3.0))

# ==================================================
# Occurrences: Lines 786-787 (2 instances)

result = outer_fn(y)

# ==================================================
# Occurrences: Lines 794-795 (2 instances)

result = outer_fn(y)

# ==================================================
# Line: 802

grad = tp.gradient(result, y)

# ==================================================
# Line: 826

grad, = gradients_impl.gradients(outer_fn(x), x)

# ==================================================
# Occurrences: Lines 832-841 (3 instances)

grad, = gradients_impl.gradients(outer_fn(x), x)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/argument_naming_test.py
# Line: 177

method_op = has_method.method.get_concrete_function()

# ==================================================
# Line: 184

method_op2 = has_method.method.get_concrete_function()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir_test.py
# Occurrences: Lines 232-235 (2 instances)

hlo_1 = compiler_ir.from_concrete_function(concrete_fn, [x])(stage='hlo')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/ops_test.py
# Occurrences: Lines 503-507 (2 instances)

old_x = constant_op.constant(9.5)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/context.py
# Line: 578

self._initialize_lock = threading.Lock()

# ==================================================
# Line: 605

self._device_lock = threading.Lock()

# ==================================================
# Occurrences: Lines 642-645 (2 instances)

self._rng = random.Random(seed)

# ==================================================
# Line: 1330

toggle = self._optimizer_experimental_options.get(option, None)

# ==================================================
# Line: 1345

toggle = self._optimizer_experimental_options.get(option, None)

# ==================================================
# Occurrences: Lines 2182-2187 (2 instances)

attr = getattr(rewrite_options, option)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/forwardprop_test.py
# Line: 573

primal_out = f(primal)

# ==================================================
# Line: 585

self.assertAllClose(expected, f(primal))

# ==================================================
# Occurrences: Lines 610-615 (2 instances)

two = constant_op.constant(2.)

# ==================================================
# Occurrences: Lines 671-674 (3 instances)

m1 = random_ops.random_uniform((256, 2096))

# ==================================================
# Occurrences: Lines 752-757 (2 instances)

c_tangent = constant_op.constant(2.)

# ==================================================
# Occurrences: Lines 802-806 (4 instances)

forward_accumulator = forwardprop.ForwardAccumulator(c, .1)

# ==================================================
# Occurrences: Lines 833-837 (4 instances)

forward_accumulator = forwardprop.ForwardAccumulator(c, .1)

# ==================================================
# Line: 959

v = constant_op.constant(1.)

# ==================================================
# Line: 965

return constant_op.constant(1.)

# ==================================================
# Occurrences: Lines 1097-1107 (6 instances)

batch_acc = forwardprop.ForwardAccumulator._batch_accumulator(x, tangents)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/remote.py
# Line: 141

if cluster_spec_or_resolver.master() in _LOCAL_MASTERS:

# ==================================================
# Line: 194

is_uptc_sess = ".uptc-worker." in cluster_spec_or_resolver.master()

# ==================================================
# Occurrences: Lines 243-244 (2 instances)

cluster_resolver.ClusterResolver) and cluster_spec_or_resolver.master():

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/remote_execution_test.py
# Occurrences: Lines 66-67 (2 instances)

self._cached_server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 118-120 (2 instances)

x1 = array_ops.ones([2, 2])

# ==================================================
# Occurrences: Lines 129-131 (2 instances)

x1 = array_ops.ones([2, 2])

# ==================================================
# Occurrences: Lines 186-187 (2 instances)

x1 = array_ops.ones([2, 2])

# ==================================================
# Occurrences: Lines 201-202 (2 instances)

x1 = array_ops.ones([2, 2])

# ==================================================
# Occurrences: Lines 212-213 (2 instances)

x1 = array_ops.ones([2, 2])

# ==================================================
# Occurrences: Lines 222-223 (2 instances)

x1 = array_ops.ones([2, 2])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/wrap_function.py
# Line: 176

new_variable = _lift_single_variable(
    old_variable, graph, variable_holder)

# ==================================================
# Line: 183

new_variable = _lift_single_variable(
    old_variable, graph, variable_holder)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/summary_optimizer_test.py
# Occurrences: Lines 135-135 (2 instances)

return math_ops.add(step, 1)

# ==================================================
# Occurrences: Lines 148-148 (2 instances)

step = math_ops.add(step, 1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/remote_cluster_test.py
# Occurrences: Lines 68-71 (4 instances)

self._cached_server1 = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 166-179 (4 instances)

x1 = array_ops.ones([2, 2])

# ==================================================
# Occurrences: Lines 186-191 (3 instances)

x1 = array_ops.ones([2, 2])

# ==================================================
# Line: 202

y = math_ops.matmul(x1, x2)

# ==================================================
# Line: 223

x1 = array_ops.ones([2, 2])

# ==================================================
# Line: 238

x2 = array_ops.ones([2, 2])

# ==================================================
# Occurrences: Lines 269-274 (2 instances)

y = worker_fn(x)

# ==================================================
# Line: 295

y = worker_fn(x1)

# ==================================================
# Line: 301

y = worker_fn(x1)

# ==================================================
# Occurrences: Lines 322-332 (3 instances)

y = worker_fn(x1)

# ==================================================
# Occurrences: Lines 402-406 (2 instances)

ret[i] = worker_fn(x1)

# ==================================================
# Occurrences: Lines 533-538 (2 instances)

y = worker_fn(x1)

# ==================================================
# Line: 568

y = worker_fn(x1)

# ==================================================
# Line: 575

y = worker_fn(x1)

# ==================================================
# Occurrences: Lines 639-640 (2 instances)

executor_t3 = executor.new_executor(enable_async=False)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/dlpack/dlpack_test.py
# Occurrences: Lines 95-98 (2 instances)

_ = dlpack.from_dlpack(dlcapsule)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
# Line: 102

to_visit = list_all_layers(layer)

# ==================================================
# Line: 110

to_visit.extend(list_all_layers(layer))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
# Occurrences: Lines 392-400 (2 instances)

self.loaded_nodes[node_metadata.node_id] = self._load_layer(
    node_metadata.node_id, node_metadata.identifier,
    node_metadata.metadata)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
# Line: 292

status = clone.load_weights(checkpoint_path)

# ==================================================
# Line: 303

clone.load_weights(checkpoint_path)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/saving/utils_v1/export_utils.py
# Line: 103

excluded_signatures[signature_name] = str(e)

# ==================================================
# Line: 119

excluded_signatures[signature_name] = str(e)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
# Line: 278

return preprocess_weights_for_loading(
    layer.layer, weights, original_keras_version, original_backend)

# ==================================================
# Line: 330

weights = preprocess_weights_for_loading(
    layer.layer, weights, original_keras_version, original_backend)

# ==================================================
# Line: 341

weights[0] = np.transpose(weights[0], (2, 3, 1, 0))

# ==================================================
# Line: 348

weights[0] = np.transpose(weights[0], (2, 3, 1, 0))

# ==================================================
# Occurrences: Lines 378-393 (6 instances)

kernel = np.concatenate(
    [weights[0], weights[6], weights[3], weights[9]], axis=-1)

# ==================================================
# Occurrences: Lines 508-510 (2 instances)

kernels = transform_kernels(weights[0], transpose_input(from_cudnn),
                            n_gates)

# ==================================================
# Occurrences: Lines 544-546 (2 instances)

kernels = transform_kernels(weights[0], transpose_input(from_cudnn),
                            n_gates)

# ==================================================
# Line: 675

weights = _legacy_weights(layer)

# ==================================================
# Line: 683

weight_names = load_attributes_from_hdf5_group(g, 'weight_names')

# ==================================================
# Occurrences: Lines 698-701 (2 instances)

weight_names = load_attributes_from_hdf5_group(g, 'weight_names')

# ==================================================
# Occurrences: Lines 830-835 (2 instances)

chunked_data = np.array_split(data_npy, num_chunks)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/backend_config.py
# Occurrences: Lines 102-103 (2 instances)

raise ValueError('Unknown floatx type: ' + str(value))

# ==================================================
# Occurrences: Lines 139-140 (2 instances)

raise ValueError('Unknown data_format: ' + str(data_format))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/callbacks_v1.py
# Occurrences: Lines 182-190 (8 instances)

mapped_weight_name = weight.name.replace(':', '_')

# ==================================================
# Occurrences: Lines 197-197 (3 instances)

shape = K.int_shape(w_img)

# ==================================================
# Occurrences: Lines 206-206 (3 instances)

shape = K.int_shape(w_img)

# ==================================================
# Occurrences: Lines 212-212 (2 instances)

mapped_weight_name = weight.name.replace(':', '_')

# ==================================================
# Occurrences: Lines 262-263 (2 instances)

self.batch_id = batch_id = array_ops.placeholder(dtypes.int32)

# ==================================================
# Line: 330

value = value.item()

# ==================================================
# Line: 336

value = value.item()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/data_utils.py
# Occurrences: Lines 219-222 (2 instances)

untar_fpath = os.path.join(datadir, fname)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/losses_utils.py
# Occurrences: Lines 132-135 (2 instances)

predictions = array_ops.squeeze(predictions, [-1])

# ==================================================
# Line: 144

lambda: array_ops.squeeze(predictions, [-1]),

# ==================================================
# Line: 150

lambda: array_ops.squeeze(labels, [-1]),

# ==================================================
# Occurrences: Lines 192-198 (2 instances)

y_true, y_pred = remove_squeezable_dimensions(
    y_true, y_pred)

# ==================================================
# Occurrences: Lines 216-218 (2 instances)

sample_weight = array_ops.squeeze(sample_weight, [-1])

# ==================================================
# Occurrences: Lines 224-227 (2 instances)

maybe_squeeze_weights = lambda: array_ops.squeeze(sample_weight, [-1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
# Occurrences: Lines 153-153 (2 instances)

result_t = array_ops.identity(raw_result)

# ==================================================
# Occurrences: Lines 161-161 (2 instances)

result_t = array_ops.identity(raw_result)

# ==================================================
# Line: 636

sample_weight = math_ops.cast(sample_weight, dtype=variable_dtype)

# ==================================================
# Line: 702

math_ops.cast(sample_weight, dtype=variable_dtype), y_pred)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/generic_utils.py
# Line: 493

name = get_registered_name(instance.__class__)

# ==================================================
# Line: 517

name = get_registered_name(instance.__class__)

# ==================================================
# Occurrences: Lines 581-581 (2 instances)

tf_inspect.isfunction(get_registered_object(item, custom_objects))):

# ==================================================
# Occurrences: Lines 590-590 (2 instances)

deserialized_objects[key] = get_registered_object(item, custom_objects)

# ==================================================
# Occurrences: Lines 725-729 (4 instances)

raw_code = marshal.dumps(func.__code__).replace(b'\\', b'/')

# ==================================================
# Line: 947

avg = np.mean(self._values[k][0] / max(1, self._values[k][1]))

# ==================================================
# Line: 972

avg = np.mean(self._values[k][0] / max(1, self._values[k][1]))

# ==================================================
# Line: 1067

start = start.tolist()

# ==================================================
# Line: 1076

start = start.tolist()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/layer_utils.py
# Line: 130

nodes_by_depth = model._nodes_by_depth.values()

# ==================================================
# Line: 170

for v in model._nodes_by_depth.values():

# ==================================================
# Line: 207

params = layer.count_params()

# ==================================================
# Line: 239

layer.count_params(), first_connection

# ==================================================
# Occurrences: Lines 299-304 (4 instances)

ki = kernel[:, i].reshape(original_fm_shape)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/vis_utils.py
# Line: 142

layer_id = str(id(layer))

# ==================================================
# Line: 229

layer_id = str(id(layer))

# ==================================================
# Occurrences: Lines 253-253 (4 instances)

sub_n_first_node[layer.name].get_name())

# ==================================================
# Occurrences: Lines 263-263 (4 instances)

output_name = sub_n_first_node[layer.name].get_name()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/callbacks.py
# Line: 368

start_time = time.time()

# ==================================================
# Line: 378

self._hook_times[hook_name].append(time.time() - start_time)

# ==================================================
# Occurrences: Lines 1490-1491 (2 instances)

return file_io.file_exists_v2(filepath)

# ==================================================
# Line: 1808

self.best_weights = self.model.get_weights()

# ==================================================
# Line: 1814

self.best_weights = self.model.get_weights()

# ==================================================
# Line: 2527

shape = backend.int_shape(w_img)

# ==================================================
# Line: 2533

shape = backend.int_shape(w_img)

# ==================================================
# Occurrences: Lines 2540-2543 (2 instances)

shape = backend.int_shape(w_img)

# ==================================================
# Line: 2675

logs['lr'] = backend.get_value(self.model.optimizer.lr)

# ==================================================
# Line: 2693

old_lr = backend.get_value(self.model.optimizer.lr)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/optimizers.py
# Occurrences: Lines 89-90 (2 instances)

if config['class_name'].lower() in all_classes:

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/metrics.py
# Line: 168

control_status = ag_ctx.control_status_ctx()

# ==================================================
# Line: 183

control_status = ag_ctx.control_status_ctx()

# ==================================================
# Occurrences: Lines 426-429 (2 instances)

num_values = math_ops.cast(array_ops.size(values), self._dtype)

# ==================================================
# Line: 2370

riemann_terms = math_ops.multiply(x[:self.num_thresholds - 1] - x[1:],
                                  heights)

# ==================================================
# Line: 2387

math_ops.multiply(x[:self.num_thresholds - 1] - x[1:], heights),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
# Line: 415

default_graph = ops.get_default_graph()

# ==================================================
# Line: 423

init_graph = ops.get_default_graph()

# ==================================================
# Line: 517

return super(Layer, self).__call__(inputs, *args, **kwargs)

# ==================================================
# Line: 558

outputs = super(Layer, self).__call__(inputs, *args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
# Occurrences: Lines 645-650 (2 instances)

loss_scale_update_op, should_apply_grads = _if_should_apply_grads(grads)

# ==================================================
# Line: 657

loss_scale_update_op, should_apply_grads = _if_should_apply_grads(grads)

# ==================================================
# Line: 668

maybe_apply_op = smart_cond.smart_cond(should_apply_grads, apply_fn,
                                       do_not_apply_fn)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/initializers/__init__.py
# Line: 40

if LOCAL.ALL_OBJECTS and LOCAL.GENERATED_WITH_V2 == tf2.enabled():

# ==================================================
# Line: 46

LOCAL.GENERATED_WITH_V2 = tf2.enabled()

# ==================================================
# Line: 74

if tf2.enabled():

# ==================================================
# Line: 179

identifier = str(identifier)

# ==================================================
# Line: 187

str(identifier))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
# Occurrences: Lines 497-500 (2 instances)

stddev = math.sqrt(scale) / .87962566103423978

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/optimizer_v1.py
# Line: 818

grads = self.optimizer.compute_gradients(loss, params)

# ==================================================
# Line: 829

grads = self.optimizer.compute_gradients(loss, params)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# Occurrences: Lines 1164-1167 (2 instances)

distribution_strategy=distribute_lib.get_strategy(),

# ==================================================
# Occurrences: Lines 1195-1200 (2 instances)

data_iterator = iter(self._dataset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
# Occurrences: Lines 146-147 (2 instances)

name = getattr(tensor, 'name', None)

# ==================================================
# Occurrences: Lines 180-181 (2 instances)

name = getattr(tensor, 'name', None)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
# Occurrences: Lines 335-335 (2 instances)

batch_logs = cbks.make_logs(model, batch_logs, batch_outs, mode)

# ==================================================
# Occurrences: Lines 390-390 (2 instances)

batch_logs = cbks.make_logs(model, batch_logs, batch_outs, mode)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/node.py
# Occurrences: Lines 149-153 (2 instances)

return (tensor_dict[kt_id].pop(),), {}

# ==================================================
# Occurrences: Lines 175-176 (2 instances)

node_key = make_node_key(kh.layer.name, node_index)

# ==================================================
# Occurrences: Lines 204-205 (2 instances)

node_key = make_node_key(kh.layer.name, node_index)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
# Line: 684

input_list = nest.flatten(inputs)

# ==================================================
# Line: 701

input_list = nest.flatten(inputs)

# ==================================================
# Occurrences: Lines 730-735 (3 instances)

training_value = backend.learning_phase()

# ==================================================
# Occurrences: Lines 761-766 (2 instances)

graph = backend.get_graph()

# ==================================================
# Line: 827

cast_inputs = self._maybe_cast_inputs(inputs)

# ==================================================
# Line: 1036

loss = tensor_conversion.convert_to_tensor_v2_with_dispatch(
    loss, dtype=backend.floatx()
)

# ==================================================
# Line: 1053

loss = tensor_conversion.convert_to_tensor_v2_with_dispatch(
    loss, dtype=backend.floatx()
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
# Occurrences: Lines 417-419 (2 instances)

start_time = time.time()

# ==================================================
# Line: 573

data_len = len(data)

# ==================================================
# Line: 617

if len(data) != len(names):

# ==================================================
# Line: 624

'following list of ' + str(len(data)) + ' arrays: ' +

# ==================================================
# Line: 632

elif len(data) == 1 and not hasattr(data[0], 'shape'):

# ==================================================
# Line: 1120

metric = metrics_module.get(metric)

# ==================================================
# Line: 1130

metric_fn = metrics_module.get(metric)

# ==================================================
# Line: 1219

loss = losses.get(loss)

# ==================================================
# Line: 1227

loss_fn = losses.get(loss)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/functional.py
# Occurrences: Lines 125-132 (4 instances)

if isinstance(inputs, list) and len(nest.flatten(inputs)) == 1:

# ==================================================
# Line: 539

x_id = str(id(x))

# ==================================================
# Line: 564

x_id = str(id(x))

# ==================================================
# Occurrences: Lines 945-950 (2 instances)

nodes_by_depth = collections.defaultdict(list)

# ==================================================
# Line: 1170

new_node_index = get_node_index(layer, node_index)

# ==================================================
# Occurrences: Lines 1297-1300 (2 instances)

layer_name, node_index, tensor_index = layer_data.as_list()

# ==================================================
# Occurrences: Lines 1307-1310 (2 instances)

layer_name, node_index, tensor_index = layer_data.as_list()

# ==================================================
# Line: 1338

node_key = _make_node_key(layer.name, original_node_index)

# ==================================================
# Line: 1348

node_key = _make_node_key(layer.name, original_node_index)

# ==================================================
# Line: 1365

node_key = _make_node_key(layer.name, node_index)

# ==================================================
# Line: 1381

node_key = _make_node_key(layer.name, node_index)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/training.py
# Occurrences: Lines 322-325 (3 instances)

self._train_counter = variables.Variable(0, dtype='int64', aggregation=agg)

# ==================================================
# Line: 857

return step_function(self, iterator)

# ==================================================
# Line: 864

outputs = step_function(self, iterator)

# ==================================================
# Line: 1327

return step_function(self, iterator)

# ==================================================
# Line: 1334

outputs = step_function(self, iterator)

# ==================================================
# Line: 1577

return step_function(self, iterator)

# ==================================================
# Occurrences: Lines 1583-1583 (2 instances)

outputs = step_function(self, iterator)

# ==================================================
# Occurrences: Lines 1589-1589 (2 instances)

step_outputs = step_function(self, iterator)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Line: 974

input_list = nest.flatten(inputs)

# ==================================================
# Line: 992

input_list = nest.flatten(inputs)

# ==================================================
# Line: 1486

loss = tensor_conversion.convert_to_tensor_v2_with_dispatch(
    loss, dtype=backend.floatx()
)

# ==================================================
# Line: 1505

loss = tensor_conversion.convert_to_tensor_v2_with_dispatch(
    loss, dtype=backend.floatx()
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/training_v1.py
# Line: 146

if (ops.executing_eagerly_outside_functions() and

# ==================================================
# Line: 158

ops.executing_eagerly_outside_functions())

# ==================================================
# Line: 2390

flat_expected_inputs = nest.flatten(self.inputs, expand_composites=False)

# ==================================================
# Line: 2410

flat_expected_inputs = nest.flatten(self.inputs, expand_composites=False)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/optimizer_v2/adagrad.py
# Occurrences: Lines 75-80 (2 instances)

epsilon = backend_config.epsilon()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/optimizer_v2/nadam.py
# Line: 72

learning_rate = kwargs.get('lr', learning_rate)

# ==================================================
# Line: 79

self._set_hyper('learning_rate', kwargs.get('lr', learning_rate))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
# Occurrences: Lines 1008-1011 (2 instances)

local_step = math_ops.cast(self.iterations, var_dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/optimizer_v2/rmsprop.py
# Line: 186

mg = self.get_slot(var, "mg")

# ==================================================
# Line: 215

mg = self.get_slot(var, "mg")

# ==================================================
# Line: 232

mg = self.get_slot(var, "mg")

# ==================================================
# Line: 266

mg = self.get_slot(var, "mg")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
# Line: 896

distributed_model = get_distributed_model(model, mode)

# ==================================================
# Line: 912

distributed_model = get_distributed_model(model, mode)

# ==================================================
# Occurrences: Lines 1124-1127 (2 instances)

distributed_model = get_distributed_model(model, mode)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/distribute/distribute_coordinator_utils.py
# Line: 359

assert _thread_local.session_config_str == repr(session_config)

# ==================================================
# Line: 369

_thread_local.session_config_str = repr(session_config)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/losses.py
# Line: 1244

r = loss_fn(*inputs)

# ==================================================
# Line: 1259

return loss_fn(*inputs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/recurrent.py
# Line: 542

input_spec_shape = shape.as_list()

# ==================================================
# Line: 553

shape = tuple(shape.as_list())

# ==================================================
# Occurrences: Lines 569-578 (4 instances)

self.input_spec[0] = get_input_spec(input_shape)

# ==================================================
# Line: 932

if nest.flatten(self.states)[0] is None:

# ==================================================
# Line: 947

for state, size in zip(nest.flatten(self.states),

# ==================================================
# Line: 953

flat_states = nest.flatten(self.states)

# ==================================================
# Occurrences: Lines 1878-1879 (2 instances)

z = self.recurrent_activation(x_z + recurrent_z)

# ==================================================
# Line: 1893

hh = self.activation(x_h + recurrent_h)

# ==================================================
# Occurrences: Lines 1919-1920 (2 instances)

z = self.recurrent_activation(x_z + recurrent_z)

# ==================================================
# Line: 1928

hh = self.activation(x_h + recurrent_h)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/merge.py
# Occurrences: Lines 128-132 (2 instances)

x_ndim = backend.ndim(x)

# ==================================================
# Line: 138

x_ndim = backend.ndim(x)

# ==================================================
# Line: 160

y = self._merge_function(reshaped_inputs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/serialization.py
# Line: 56

if LOCAL.ALL_OBJECTS and LOCAL.GENERATED_WITH_V2 == tf2.enabled():

# ==================================================
# Line: 62

LOCAL.GENERATED_WITH_V2 = tf2.enabled()

# ==================================================
# Line: 71

if tf2.enabled():

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/models.py
# Line: 488

value = getattr(model, name)

# ==================================================
# Line: 549

attributes_cache[name] = getattr(model, name)

# ==================================================
# Occurrences: Lines 670-672 (2 instances)

clone = clone_model(model, input_tensors=input_tensors)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/backend.py
# Line: 527

previous_graph_value = _GRAPH_LEARNING_PHASES.get(get_graph(), None)

# ==================================================
# Line: 544

graph = get_graph()

# ==================================================
# Occurrences: Lines 867-871 (2 instances)

device_type = device_type.upper()

# ==================================================
# Line: 1316

spec = ragged_tensor.RaggedTensorSpec(
    shape=shape, dtype=dtype, ragged_rank=ragged_rank)

# ==================================================
# Line: 1331

type_spec = ragged_tensor.RaggedTensorSpec(
    shape=shape, dtype=dtype, ragged_rank=ragged_rank)

# ==================================================
# Line: 3190

x_shape = x.shape.as_list()

# ==================================================
# Line: 3222

x_shape = x.shape.as_list()

# ==================================================
# Line: 3700

x.assign(numpy_compat.np_asarray(value, dtype=dtype_numpy(x)))

# ==================================================
# Line: 3707

value = numpy_compat.np_asarray(value, dtype=dtype_numpy(x))

# ==================================================
# Occurrences: Lines 3761-3767 (2 instances)

op = logging_ops.print_v2(
    message, x, output_stream=sys.stdout, summarize=summarize)

# ==================================================
# Occurrences: Lines 4205-4208 (2 instances)

inp = _get_input_tensor(i)

# ==================================================
# Occurrences: Lines 4218-4219 (2 instances)

flat_states = nest.flatten(states)

# ==================================================
# Line: 4230

outputs = array_ops_stack.stack(successive_outputs)

# ==================================================
# Occurrences: Lines 4242-4248 (3 instances)

inp = _get_input_tensor(i)

# ==================================================
# Occurrences: Lines 4358-4363 (3 instances)

current_input = nest.pack_sequence_as(inputs, current_input)

# ==================================================
# Occurrences: Lines 4370-4371 (2 instances)

flat_state = nest.flatten(states)

# ==================================================
# Occurrences: Lines 4404-4413 (5 instances)

current_input = nest.pack_sequence_as(inputs, current_input)

# ==================================================
# Occurrences: Lines 4864-4868 (2 instances)

res = nn.sparse_softmax_cross_entropy_with_logits_v2(
    labels=target, logits=output)

# ==================================================
# Occurrences: Lines 6378-6381 (2 instances)

ragged = ragged_tensor.RaggedTensor.from_tensor(output, nested_row_lengths)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/testing_utils.py
# Line: 164

layer = layer_cls(**kwargs)

# ==================================================
# Line: 178

weights = layer.get_weights()

# ==================================================
# Occurrences: Lines 184-188 (3 instances)

layer = layer_cls(**kwargs)

# ==================================================
# Line: 225

actual_output = model.predict(input_data)

# ==================================================
# Occurrences: Lines 239-244 (3 instances)

model_config = model.get_config()

# ==================================================
# Occurrences: Lines 250-252 (2 instances)

layer_weights = layer.get_weights()  # Get the layer weights BEFORE training.

# ==================================================
# Occurrences: Lines 273-277 (2 instances)

model.add(layers.Input(shape=input_shape[1:], dtype=input_dtype))

# ==================================================
# Occurrences: Lines 296-301 (3 instances)

model_config = model.get_config()

# ==================================================
# Line: 597

inputs = layers.Input(
    shape=input_shape,
    dtype=input_dtype,
    ragged=input_ragged,
    sparse=input_sparse)

# ==================================================
# Line: 625

inputs = layers.Input(
    shape=input_shape,
    dtype=input_dtype,
    ragged=input_ragged,
    sparse=input_sparse)

# ==================================================
# Occurrences: Lines 701-707 (4 instances)

if self._shared_input_branch_func():

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/lib/io/tf_record_test.py
# Occurrences: Lines 377-380 (2 instances)

record = next(reader)

# ==================================================
# Occurrences: Lines 544-549 (2 instances)

record, offset = reader.read(offset)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/lib/io/file_io_test.py
# Occurrences: Lines 110-114 (2 instances)

file_contents = file_io.read_file_to_string(file_path)

# ==================================================
# Occurrences: Lines 189-191 (2 instances)

file_path = file_io.join(dir_path, name)

# ==================================================
# Occurrences: Lines 210-212 (2 instances)

file_path = file_io.join(dir_path, name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/lib/io/file_io.py
# Occurrences: Lines 973-976 (2 instances)

chunk = f.read(n=block_size)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compat/disable_v2_behavior_test.py
# Occurrences: Lines 27-34 (4 instances)

t = constant_op.constant([1, 2, 3])  # creates a hidden context

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/server_lib_same_variables_clear_container_test.py
# Occurrences: Lines 50-51 (2 instances)

sess_0 = session.Session(server0.target)

# ==================================================
# Line: 59

_ = session.Session(server0.target)

# ==================================================
# Occurrences: Lines 70-74 (2 instances)

_ = session.Session(server1.target)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/moving_averages_test.py
# Occurrences: Lines 43-50 (2 instances)

assign = moving_averages.assign_moving_average(
    var, val, decay, zero_debias=False)

# ==================================================
# Occurrences: Lines 65-70 (2 instances)

assign = moving_averages.assign_moving_average(var, val, decay)

# ==================================================
# Occurrences: Lines 96-100 (2 instances)

var = variable_scope.get_variable("Var", shape=[])

# ==================================================
# Occurrences: Lines 108-109 (2 instances)

weight = array_ops.placeholder(dtypes.float32, [])

# ==================================================
# Occurrences: Lines 134-135 (2 instances)

weight = array_ops.placeholder(dtypes.bfloat16, [])

# ==================================================
# Line: 370

op = ema.apply([v0, v1])

# ==================================================
# Line: 378

self.evaluate(ema.apply([v0, v1]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Line: 568

cols_to_vars = self._create_linear_model([sc_int], partitioner)

# ==================================================
# Line: 578

cols_to_vars = self._create_linear_model([sc_int], partitioner)

# ==================================================
# Line: 597

cols_to_vars = self._create_linear_model([sc_hash], partitioner)

# ==================================================
# Line: 607

cols_to_vars = self._create_linear_model([sc_hash], partitioner)

# ==================================================
# Line: 631

cols_to_vars = self._create_linear_model([sc_vocab], partitioner)

# ==================================================
# Line: 641

cols_to_vars = self._create_linear_model([sc_vocab], partitioner)

# ==================================================
# Line: 667

cols_to_vars = self._create_linear_model([sc_vocab], partitioner)

# ==================================================
# Line: 677

cols_to_vars = self._create_linear_model([sc_vocab], partitioner)

# ==================================================
# Line: 712

cols_to_vars = self._create_linear_model([sc_vocab], partitioner)

# ==================================================
# Line: 722

cols_to_vars = self._create_linear_model([sc_vocab], partitioner)

# ==================================================
# Line: 755

cols_to_vars = self._create_linear_model([real_bucket], partitioner)

# ==================================================
# Line: 765

cols_to_vars = self._create_linear_model([real_bucket], partitioner)

# ==================================================
# Line: 826

cols_to_vars = self._create_linear_model(all_linear_cols, partitioner)

# ==================================================
# Line: 842

cols_to_vars = self._create_linear_model(all_linear_cols, partitioner)

# ==================================================
# Line: 1211

x = variable_scope.get_variable(
    "x",
    shape=[4, 1],
    initializer=ones(),
    partitioner=lambda shape, dtype: [2, 1])

# ==================================================
# Line: 1224

x = variable_scope.get_variable(
    "x",
    shape=[4, 1],
    initializer=ones(),
    partitioner=lambda shape, dtype: [2, 1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/ftrl_test.py
# Occurrences: Lines 41-47 (8 instances)

var0 = resource_variable_ops.ResourceVariable([0.0, 0.0],
                                              dtype=dtype)

# ==================================================
# Occurrences: Lines 58-58 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 66-66 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 96-96 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 103-103 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 148-148 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 155-155 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 175-175 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 182-182 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 207-207 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 214-214 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 238-238 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 246-246 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 277-277 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 285-285 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 315-315 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 323-323 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 333-336 (8 instances)

var0 = variables.Variable([1.0, 2.0], dtype=dtype)

# ==================================================
# Occurrences: Lines 353-353 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 362-362 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 373-374 (2 instances)

var0 = variables.Variable([[0.0], [0.0]], dtype=dtype)

# ==================================================
# Occurrences: Lines 382-383 (2 instances)

var0 = variables.Variable([0.0, 0.0], dtype=dtype)

# ==================================================
# Line: 391

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 403

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
# Occurrences: Lines 592-595 (2 instances)

ops.get_default_graph().as_graph_def(add_shapes=True),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/slot_creator_test.py
# Occurrences: Lines 244-246 (2 instances)

xla_sharding.get_tensor_sharding(slot))

# ==================================================
# Occurrences: Lines 269-271 (2 instances)

xla_sharding.get_tensor_sharding(slot))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/proximal_gradient_descent_test.py
# Occurrences: Lines 38-42 (4 instances)

var0 = resource_variable_ops.ResourceVariable([0.0, 0.0])

# ==================================================
# Line: 50

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 58

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 80

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 88

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 123

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 131

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 158

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 170

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/queue_runner_test.py
# Occurrences: Lines 66-68 (2 instances)

var0 = variable_v1.VariableV1(zero64)

# ==================================================
# Occurrences: Lines 209-210 (2 instances)

threads.extend(qr.create_threads(sess, coord=coord))

# ==================================================
# Line: 223

threads = qr.create_threads(sess, start=True)

# ==================================================
# Line: 233

threads = qr.create_threads(sess, start=True)

# ==================================================
# Line: 328

qr0_recon = queue_runner_impl.QueueRunner.from_proto(qr0_proto)

# ==================================================
# Line: 341

qr0_legacy_recon = queue_runner_impl.QueueRunner.from_proto(qr0_proto)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/adagrad_test.py
# Occurrences: Lines 58-63 (4 instances)

ada_update = ada_opt.apply_gradients(
    zip([grads0, grads1], [var0, var1]))

# ==================================================
# Occurrences: Lines 72-75 (4 instances)

ada_opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

# ==================================================
# Occurrences: Lines 180-183 (4 instances)

repeated_index_update_var = variables.Variable(
    [[1.0], [2.0]], dtype=dtype)

# ==================================================
# Occurrences: Lines 211-216 (4 instances)

var_repeated = resource_variable_ops.ResourceVariable(
    [1.0, 2.0], dtype=dtype)

# ==================================================
# Occurrences: Lines 281-284 (4 instances)

ada_update1 = ada_opt.apply_gradients(
    zip([grads0, grads1], [var0, var1]))

# ==================================================
# Occurrences: Lines 320-325 (2 instances)

ada_update = ada_opt.apply_gradients(
    zip([grads0], [var0]))

# ==================================================
# Occurrences: Lines 333-336 (2 instances)

ada_opt.apply_gradients(zip([grads0], [var0]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/input_test.py
# Occurrences: Lines 45-48 (2 instances)

temp_dir = self.get_temp_dir()

# ==================================================
# Occurrences: Lines 55-57 (2 instances)

star = inp.match_filenames_once(os.path.join(self.get_temp_dir(), "*"))

# ==================================================
# Line: 478

results = self.evaluate(batched_fetch)

# ==================================================
# Line: 495

self.evaluate(batched_fetch)

# ==================================================
# Line: 546

results = self.evaluate(batched)

# ==================================================
# Line: 556

self.evaluate(batched)

# ==================================================
# Line: 579

results = self.evaluate(batched)

# ==================================================
# Line: 592

self.evaluate(batched)

# ==================================================
# Line: 619

results = self.evaluate(batched)

# ==================================================
# Line: 633

self.evaluate(batched)

# ==================================================
# Line: 660

results = self.evaluate(batched)

# ==================================================
# Line: 676

results = self.evaluate(batched)

# ==================================================
# Line: 690

self.evaluate(batched)

# ==================================================
# Line: 719

results = self.evaluate(batched)

# ==================================================
# Line: 731

results = self.evaluate(batched)

# ==================================================
# Line: 746

self.evaluate(batched)

# ==================================================
# Line: 843

results = self.evaluate(batched)

# ==================================================
# Line: 850

self.evaluate(batched)

# ==================================================
# Line: 1069

results = self.evaluate(batched_fetch)

# ==================================================
# Line: 1100

self.evaluate(batched_fetch)

# ==================================================
# Line: 1168

results = self.evaluate(batched)

# ==================================================
# Line: 1200

self.evaluate(batched)

# ==================================================
# Line: 1255

results = self.evaluate(batched)

# ==================================================
# Line: 1275

results = self.evaluate(batched)

# ==================================================
# Line: 1303

self.evaluate(batched)

# ==================================================
# Line: 1352

results = self.evaluate(batched)

# ==================================================
# Line: 1360

count_string_a.append(sum(x == b"a" for x in s))

# ==================================================
# Line: 1372

results = self.evaluate(batched)

# ==================================================
# Line: 1380

count_string_a.append(sum(x == b"a" for x in s))

# ==================================================
# Line: 1403

self.evaluate(batched)

# ==================================================
# Line: 1468

results = self.evaluate(batched)

# ==================================================
# Line: 1479

self.evaluate(batched)

# ==================================================
# Line: 1669

results = self.evaluate(batched_fetch)

# ==================================================
# Line: 1687

self.evaluate(batched_fetch)

# ==================================================
# Line: 1725

results = self.evaluate(batched_fetch)

# ==================================================
# Line: 1750

self.evaluate(batched_fetch)

# ==================================================
# Line: 1779

results = self.evaluate(batched)

# ==================================================
# Line: 1798

self.evaluate(batched)

# ==================================================
# Line: 1830

results = self.evaluate(batched)

# ==================================================
# Line: 1842

results = self.evaluate(batched)

# ==================================================
# Line: 1857

self.evaluate(batched)

# ==================================================
# Line: 1911

results = self.evaluate(batched)

# ==================================================
# Line: 1918

self.evaluate(batched)

# ==================================================
# Line: 2129

results = self.evaluate(batched_fetch)

# ==================================================
# Line: 2159

self.evaluate(batched_fetch)

# ==================================================
# Line: 2223

results = self.evaluate(batched)

# ==================================================
# Line: 2243

results = self.evaluate(batched)

# ==================================================
# Line: 2270

self.evaluate(batched)

# ==================================================
# Line: 2346

results = self.evaluate(batched)

# ==================================================
# Line: 2353

self.evaluate(batched)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
# Line: 524

saveable_factories = obj._gather_saveables_for_checkpoint()  # pylint: disable=protected-access

# ==================================================
# Line: 567

return obj._gather_saveables_for_checkpoint()  # pylint: disable=protected-access

# ==================================================
# Line: 595

return restore_fn(restored_tensor_dict)

# ==================================================
# Line: 602

ret = restore_fn(restored_tensor_dict)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/adadelta_test.py
# Occurrences: Lines 66-67 (4 instances)

adadelta_update = adadelta_opt.apply_gradients(
    zip([grads, grads], [var0, var1]))

# ==================================================
# Occurrences: Lines 111-111 (4 instances)

adadelta_opt.apply_gradients(zip([grads, grads], [var0, var1]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/warm_starting_util.py
# Occurrences: Lines 168-173 (2 instances)

current_var_name = _infer_var_name([var])

# ==================================================
# Occurrences: Lines 254-256 (2 instances)

total_v_first_axis = sum(v.get_shape().as_list()[0] for v in var)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/server_lib_same_variables_clear_test.py
# Occurrences: Lines 43-44 (2 instances)

sess_1 = session.Session(server.target)

# ==================================================
# Line: 56

sess_2 = session.Session(server.target)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/adam_test.py
# Occurrences: Lines 72-76 (4 instances)

grads0_np_indices = np.array([0, 1], dtype=np.int32)

# ==================================================
# Occurrences: Lines 144-147 (4 instances)

repeated_index_update_var = variables.Variable(
    [[1.0], [2.0]], dtype=dtype)

# ==================================================
# Occurrences: Lines 206-208 (6 instances)

update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

# ==================================================
# Occurrences: Lines 225-225 (2 instances)

self.assertEqual(0, len(opt.variables()))

# ==================================================
# Occurrences: Lines 231-231 (2 instances)

beta1_power, beta2_power = opt._get_beta_accumulators()

# ==================================================
# Occurrences: Lines 238-238 (2 instances)

opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

# ==================================================
# Occurrences: Lines 326-327 (4 instances)

update1 = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

# ==================================================
# Occurrences: Lines 360-375 (8 instances)

var0 = variables.Variable(np.array([1.0, 2.0]), name="v0")

# ==================================================
# Occurrences: Lines 385-386 (2 instances)

v1 = resource_variable_ops.ResourceVariable(1.)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/supervisor_test.py
# Occurrences: Lines 176-188 (8 instances)

ev = next(rr)

# ==================================================
# Occurrences: Lines 196-201 (4 instances)

ev = next(rr)

# ==================================================
# Occurrences: Lines 225-236 (4 instances)

ev = next(rr)

# ==================================================
# Line: 244

ev = next(rr)

# ==================================================
# Line: 252

self.assertRaises(StopIteration, lambda: next(rr))

# ==================================================
# Occurrences: Lines 358-362 (2 instances)

ev = next(rr)

# ==================================================
# Line: 368

ev = next(rr)

# ==================================================
# Line: 375

ev = next(rr)

# ==================================================
# Occurrences: Lines 383-387 (2 instances)

ev = next(rr)

# ==================================================
# Occurrences: Lines 393-394 (2 instances)

sv = supervisor.Supervisor(is_chief=False)

# ==================================================
# Occurrences: Lines 402-403 (2 instances)

sv = supervisor.Supervisor(is_chief=False)

# ==================================================
# Occurrences: Lines 458-462 (2 instances)

ev = next(rr)

# ==================================================
# Line: 468

ev = next(rr)

# ==================================================
# Line: 476

ev = next(rr)

# ==================================================
# Occurrences: Lines 484-488 (2 instances)

ev = next(rr)

# ==================================================
# Occurrences: Lines 595-600 (2 instances)

with ops.Graph().as_default():

# ==================================================
# Line: 610

g = ops.Graph()

# ==================================================
# Line: 629

sess = sv.prepare_or_wait_for_session(server.target)

# ==================================================
# Occurrences: Lines 776-778 (2 instances)

ev = next(rr)

# ==================================================
# Line: 784

ev = next(rr)

# ==================================================
# Occurrences: Lines 791-797 (3 instances)

ev = next(rr)

# ==================================================
# Occurrences: Lines 827-833 (3 instances)

ev = next(rr)

# ==================================================
# Occurrences: Lines 839-845 (3 instances)

ev = next(rr)

# ==================================================
# Occurrences: Lines 860-862 (2 instances)

ev = next(rr)

# ==================================================
# Line: 882

sess = sv.prepare_or_wait_for_session("")

# ==================================================
# Line: 889

sess2 = sv.prepare_or_wait_for_session("")

# ==================================================
# Line: 901

sess = sv.prepare_or_wait_for_session("")

# ==================================================
# Line: 908

sess2 = sv.prepare_or_wait_for_session("")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/coordinator_test.py
# Occurrences: Lines 82-83 (2 instances)

wait_for_stop_ev = threading.Event()

# ==================================================
# Occurrences: Lines 140-141 (4 instances)

wait_for_stop_ev = threading.Event()

# ==================================================
# Occurrences: Lines 162-163 (2 instances)

wait_for_stop_ev = threading.Event()

# ==================================================
# Occurrences: Lines 178-179 (2 instances)

ev_1 = threading.Event()

# ==================================================
# Occurrences: Lines 198-199 (2 instances)

ev_1 = threading.Event()

# ==================================================
# Occurrences: Lines 246-247 (2 instances)

ev_1 = threading.Event()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/coordinator.py
# Line: 208

_, ex_instance, _ = sys.exc_info()

# ==================================================
# Line: 221

self._exc_info_to_raise = sys.exc_info()

# ==================================================
# Line: 238

self._exc_info_to_raise = sys.exc_info()

# ==================================================
# Occurrences: Lines 490-491 (2 instances)

next_timer_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/quantize_training_test.py
# Line: 57

g = ops.Graph()

# ==================================================
# Occurrences: Lines 71-72 (2 instances)

with ops.Graph().as_default() as g, session.Session(graph=g) as sess:

# ==================================================
# Occurrences: Lines 83-84 (2 instances)

with ops.Graph().as_default() as g, session.Session(graph=g) as sess:

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/proximal_adagrad_test.py
# Occurrences: Lines 37-38 (2 instances)

var0 = variables.Variable([0.0, 0.0])

# ==================================================
# Line: 49

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 57

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 87

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 94

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 133

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 140

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 160

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 168

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 196

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Line: 208

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/server_lib_test.py
# Occurrences: Lines 64-65 (2 instances)

sess_1 = session.Session(server.target)

# ==================================================
# Line: 97

sess = session.Session(server.target)

# ==================================================
# Line: 104

sess = session.Session(server.target)

# ==================================================
# Occurrences: Lines 214-223 (6 instances)

master_old = server_lib.Server.create_local_server()

# ==================================================
# Occurrences: Lines 327-332 (4 instances)

sharing_sess_0 = session.Session(server.target, config=sharing_config)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/evaluation.py
# Line: 252

start = time.time()

# ==================================================
# Line: 269

logging.info('Inference Time : {:0.5f}s'.format(time.time() - start))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/rmsprop_test.py
# Occurrences: Lines 131-136 (12 instances)

mg0_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)

# ==================================================
# Occurrences: Lines 256-261 (12 instances)

mg0_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/localhost_cluster_performance_test.py
# Occurrences: Lines 62-64 (4 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/saver_test.py
# Line: 89

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Line: 118

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Line: 140

v2_2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Line: 227

graph_saver = saver_module.Saver([w1, w2])

# ==================================================
# Line: 238

graph_saver = saver_module.Saver([w1, w2])

# ==================================================
# Line: 253

graph_saver = saver_module.Saver([w3, w4])

# ==================================================
# Line: 260

graph_saver = saver_module.Saver([w3, w4])

# ==================================================
# Occurrences: Lines 276-279 (2 instances)

save = saver_module.Saver([v])

# ==================================================
# Line: 316

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Line: 356

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Occurrences: Lines 478-480 (2 instances)

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Occurrences: Lines 500-501 (2 instances)

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Line: 525

v2_2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Line: 546

save = saver_module.Saver({var_name: var})

# ==================================================
# Line: 553

save = saver_module.Saver({var_name: var})

# ==================================================
# Occurrences: Lines 570-574 (2 instances)

save = saver_module.Saver(allow_empty=True)

# ==================================================
# Occurrences: Lines 616-618 (2 instances)

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Occurrences: Lines 626-628 (2 instances)

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Line: 676

save = saver_module.Saver()

# ==================================================
# Occurrences: Lines 682-683 (2 instances)

var = variable_v1.VariableV1([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])

# ==================================================
# Line: 691

var = variable_v1.VariableV1([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])

# ==================================================
# Occurrences: Lines 832-845 (6 instances)

save_graph = ops_lib.Graph()

# ==================================================
# Line: 857

histogram_proto = summary_pb2.HistogramProto()

# ==================================================
# Line: 863

histogram_proto = summary_pb2.HistogramProto()

# ==================================================
# Line: 869

time_start = metrics.GetTrainingTimeSaved(api_label=api_label)

# ==================================================
# Line: 876

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Occurrences: Lines 887-893 (3 instances)

ckpt_prefix = save.save(sess, save_path)

# ==================================================
# Line: 899

v2 = saver_test_utils.CheckpointedOp(name="v2")

# ==================================================
# Occurrences: Lines 907-909 (2 instances)

metrics.GetTrainingTimeSaved(api_label=api_label),

# ==================================================
# Occurrences: Lines 915-918 (2 instances)

metrics.GetTrainingTimeSaved(api_label=api_label),

# ==================================================
# Line: 932

save_path = os.path.join(self.get_temp_dir(), "sharded_basics")

# ==================================================
# Occurrences: Lines 940-952 (3 instances)

t0 = saver_test_utils.CheckpointedOp(name="t0")

# ==================================================
# Occurrences: Lines 970-971 (2 instances)

v0 = variable_v1.VariableV1(111, name="v0")

# ==================================================
# Line: 995

t1 = saver_test_utils.CheckpointedOp(name="t1")

# ==================================================
# Occurrences: Lines 1018-1031 (4 instances)

v0 = variable_v1.VariableV1(111, name="v0")

# ==================================================
# Line: 1041

save_path = os.path.join(self.get_temp_dir(), "sharded_basics")

# ==================================================
# Line: 1060

os.path.join(self.get_temp_dir(), "sharded_basics"))

# ==================================================
# Occurrences: Lines 1158-1167 (4 instances)

restored_full = _restore(
    partitioner=partitioned_variables.fixed_size_partitioner(
        num_shards=3))

# ==================================================
# Occurrences: Lines 1188-1205 (9 instances)

ds0 = dataset_ops.Dataset.range(10)

# ==================================================
# Occurrences: Lines 1221-1238 (9 instances)

ds0 = dataset_ops.Dataset.range(10)

# ==================================================
# Occurrences: Lines 1253-1264 (8 instances)

ds0 = dataset_ops.Dataset.range(10)

# ==================================================
# Occurrences: Lines 1286-1297 (8 instances)

ds0 = dataset_ops.Dataset.range(10)

# ==================================================
# Occurrences: Lines 1331-1336 (2 instances)

save = saver_module.Saver({"v": v}, max_to_keep=2)

# ==================================================
# Line: 1344

s2 = save.save(None, os.path.join(save_dir, "s2"))

# ==================================================
# Line: 1364

save2 = saver_module.Saver({"v": v}, max_to_keep=2)

# ==================================================
# Line: 1370

s2 = save.save(None, os.path.join(save_dir, "s2"))

# ==================================================
# Line: 1381

s1 = save.save(None, os.path.join(save_dir, "s1"))

# ==================================================
# Line: 1407

s1 = save.save(sess, os.path.join(save_dir, "s1"))

# ==================================================
# Line: 1415

s2 = save.save(sess, os.path.join(save_dir, "s2"))

# ==================================================
# Occurrences: Lines 1435-1445 (3 instances)

save2 = saver_module.Saver(saver_def=save.as_saver_def())

# ==================================================
# Line: 1465

s1 = save.save(sess, os.path.join(save_dir, "s1"))

# ==================================================
# Line: 1697

save = saver_module.Saver({"v": v}, max_to_keep=10)

# ==================================================
# Line: 1714

save2 = saver_module.Saver({"v": v}, max_to_keep=10)

# ==================================================
# Line: 1727

save3 = saver_module.Saver({"v": v}, max_to_keep=10)

# ==================================================
# Line: 1807

save = saver_module.Saver({"save_prefix/v0": v0, "save_prefix/v1": v1})

# ==================================================
# Line: 1837

save = saver_module.Saver({"save_prefix/v0": v0, "save_prefix/v1": v1})

# ==================================================
# Line: 1858

save = saver_module.Saver({"save_prefix/v0": v0, "save_prefix/v1": v1})

# ==================================================
# Occurrences: Lines 1992-2003 (4 instances)

kind = collection_def.WhichOneof("kind")

# ==================================================
# Line: 2020

v1 = sess.graph.get_tensor_by_name("v1:0")

# ==================================================
# Line: 2031

v1 = sess.graph.get_tensor_by_name("v1:0")

# ==================================================
# Occurrences: Lines 2078-2091 (4 instances)

kind = collection_def.WhichOneof("kind")

# ==================================================
# Line: 2109

saver = saver_module.import_meta_graph(filename)

# ==================================================
# Line: 2115

saver_module.import_meta_graph(filename)

# ==================================================
# Occurrences: Lines 2124-2129 (2 instances)

saver_module.import_meta_graph(filename)

# ==================================================
# Line: 2301

init_op = variables.global_variables_initializer()

# ==================================================
# Line: 2313

grad = gradients_impl.gradients([output], [var])

# ==================================================
# Line: 2322

expected_grad_value = self.evaluate(grad)

# ==================================================
# Occurrences: Lines 2336-2342 (3 instances)

grad = gradients_impl.gradients([output], [var])

# ==================================================
# Occurrences: Lines 2436-2445 (4 instances)

real_num = variable_v1.VariableV1(1.0, dtype=dtypes.float32, name="real")

# ==================================================
# Occurrences: Lines 2453-2462 (4 instances)

real_num = variable_v1.VariableV1(1.0, dtype=dtypes.float32, name="real")

# ==================================================
# Line: 2471

with ops_lib.Graph().as_default():

# ==================================================
# Line: 2488

graph = ops_lib.Graph()

# ==================================================
# Line: 2503

graph_1 = ops_lib.Graph()

# ==================================================
# Line: 2511

graph_2 = ops_lib.Graph()

# ==================================================
# Line: 2544

with ops_lib.Graph().as_default():

# ==================================================
# Line: 2561

graph = ops_lib.Graph()

# ==================================================
# Line: 2913

graph1 = ops_lib.Graph()

# ==================================================
# Line: 2928

saver = saver_module.Saver(var_list=var_list_1, max_to_keep=1)

# ==================================================
# Line: 2946

saver1 = saver_module.Saver(var_list=var_list_1, max_to_keep=1)

# ==================================================
# Line: 2954

graph2 = ops_lib.Graph()

# ==================================================
# Line: 2970

graph1 = ops_lib.Graph()

# ==================================================
# Line: 2991

graph2 = ops_lib.Graph()

# ==================================================
# Line: 3008

graph = ops_lib.Graph()

# ==================================================
# Line: 3025

graph1 = ops_lib.Graph()

# ==================================================
# Line: 3041

graph2 = ops_lib.Graph()

# ==================================================
# Line: 3211

a_saver = saver_module.Saver([a])

# ==================================================
# Line: 3219

a_saver = saver_module.Saver([a])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/experimental/loss_scale.py
# Line: 380

is_finite = _is_all_finite(grads)

# ==================================================
# Line: 392

is_finite = _is_all_finite(grads)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
# Line: 182

run_op = strategy.experimental_run(run_fn)

# ==================================================
# Line: 193

run_op = strategy.experimental_run(run_fn)

# ==================================================
# Line: 213

run_op = strategy.experimental_run(run_fn)

# ==================================================
# Line: 224

run_op = strategy.experimental_run(run_fn)

# ==================================================
# Line: 247

run_op = strategy.experimental_run(run_fn)

# ==================================================
# Line: 257

run_op = strategy.experimental_run(run_fn)

# ==================================================
# Line: 285

opt_op = strategy.experimental_run(run_fn)

# ==================================================
# Line: 297

self.evaluate(strategy.experimental_run(run_fn))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
# Line: 149

self.assertAlmostEqual(overflow_in_float16().numpy(), 2 ** 20)

# ==================================================
# Line: 156

out = overflow_in_float16()

# ==================================================
# Line: 163

out = overflow_in_float16()

# ==================================================
# Line: 170

out = overflow_in_float16()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
# Occurrences: Lines 146-150 (2 instances)

update_op = update()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/saver.py
# Line: 896

_END_TIME_OF_LAST_WRITE = time.time()

# ==================================================
# Line: 932

time.time() + self._keep_checkpoint_every_n_hours * 3600)

# ==================================================
# Line: 1243

start_time = time.time()

# ==================================================
# Line: 1309

end_time = time.time()

# ==================================================
# Line: 1406

start_time = time.time()

# ==================================================
# Line: 1462

microseconds=_get_duration_microseconds(start_time, time.time()))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/checkpoint_utils.py
# Occurrences: Lines 229-232 (4 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/training_util_test.py
# Occurrences: Lines 102-103 (2 instances)

first = training_util._get_or_create_global_step_read()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/training_util.py
# Line: 387

global_step_read_tensor = _get_global_step_read(graph)

# ==================================================
# Line: 407

return _get_global_step_read(graph)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/training_ops_test.py
# Occurrences: Lines 69-71 (4 instances)

x = np.arange(100).astype(dtype)

# ==================================================
# Occurrences: Lines 194-197 (4 instances)

x = np.arange(100).astype(dtype)

# ==================================================
# Occurrences: Lines 204-204 (2 instances)

x = np.arange(100).astype(dtype)

# ==================================================
# Occurrences: Lines 210-210 (2 instances)

grad = np.arange(100).astype(dtype)

# ==================================================
# Occurrences: Lines 217-217 (2 instances)

x = np.arange(100).astype(dtype)

# ==================================================
# Occurrences: Lines 223-223 (2 instances)

grad = np.arange(100).astype(dtype)

# ==================================================
# Occurrences: Lines 412-415 (4 instances)

var = np.arange(100).astype(dtype)

# ==================================================
# Line: 479

ret = constant_op.constant(0, dtypes.int32)

# ==================================================
# Line: 489

ret = constant_op.constant(0, dtypes.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/monitored_session_test.py
# Occurrences: Lines 122-124 (2 instances)

scaffold1 = monitored_session.Scaffold()

# ==================================================
# Occurrences: Lines 369-372 (2 instances)

w1 = session.run(w_add)

# ==================================================
# Line: 379

w3 = session.run(w_add)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/session_manager.py
# Line: 243

ckpt = checkpoint_management.get_checkpoint_state(checkpoint_dir)

# ==================================================
# Line: 249

ckpt = checkpoint_management.get_checkpoint_state(checkpoint_dir)

# ==================================================
# Line: 420

self, master: str, config=None, max_wait_secs=float("Inf")

# ==================================================
# Line: 450

max_wait_secs = float("Inf")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/momentum_test.py
# Occurrences: Lines 64-64 (2 instances)

mom_update = mom_opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

# ==================================================
# Occurrences: Lines 99-99 (2 instances)

mom_opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

# ==================================================
# Line: 144

optimizer_variables = optimizer.variables()

# ==================================================
# Line: 158

optimizer_variables = optimizer.variables()

# ==================================================
# Occurrences: Lines 171-172 (4 instances)

accum0_np = np.array([0.0, 0.0], dtype=dtype.as_numpy_dtype)

# ==================================================
# Occurrences: Lines 193-207 (20 instances)

var0_np = np.array([1.0, 2.0], dtype=dtype.as_numpy_dtype)

# ==================================================
# Occurrences: Lines 222-225 (4 instances)

var0_np, accum0_np = self._update_nesterov_momentum_numpy(
    var0_np, accum0_np, var0_np * 10, 2.0, 0.9)

# ==================================================
# Occurrences: Lines 546-549 (4 instances)

mom_update1 = mom_opt.apply_gradients(
    zip([grads0, grads1], [var0, var1]))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/queue_runner_impl.py
# Line: 472

queue_runners = ops.get_collection(collection)

# ==================================================
# Line: 481

for qr in ops.get_collection(collection):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/optimizer.py
# Occurrences: Lines 193-195 (2 instances)

update_op = optimizer._resource_apply_dense(g, self._v)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/session_manager_test.py
# Occurrences: Lines 98-100 (2 instances)

sm = session_manager.SessionManager(
    ready_op=variables.report_uninitialized_variables())

# ==================================================
# Occurrences: Lines 118-141 (4 instances)

session_manager.SessionManager(
    ready_op=variables.report_uninitialized_variables())

# ==================================================
# Line: 238

saver = saver_lib.Saver({"v": v})

# ==================================================
# Line: 262

saver = saver_lib.Saver({"v": v})

# ==================================================
# Line: 296

saver = saver_lib.Saver({"v": v})

# ==================================================
# Line: 319

saver = saver_lib.Saver({"v": v})

# ==================================================
# Occurrences: Lines 725-727 (2 instances)

sm = session_manager.SessionManager(
    ready_op=variables.assert_variables_initialized())

# ==================================================
# Occurrences: Lines 745-768 (4 instances)

session_manager.SessionManager(
    ready_op=variables.assert_variables_initialized())

# ==================================================
# Occurrences: Lines 785-787 (2 instances)

sm = session_manager.SessionManager(
    ready_op=variables.assert_variables_initialized())

# ==================================================
# Occurrences: Lines 800-802 (2 instances)

sm2 = session_manager.SessionManager(
    ready_op=variables.assert_variables_initialized())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/adagrad_da_test.py
# Occurrences: Lines 38-42 (8 instances)

var0 = resource_variable_ops.ResourceVariable([0.0, 0.0], dtype=dtype)

# ==================================================
# Occurrences: Lines 55-55 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 62-62 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 121-121 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 128-128 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 153-153 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 160-160 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 185-185 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# Occurrences: Lines 192-192 (2 instances)

v0_val, v1_val = self.evaluate([var0, var1])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
# Line: 510

global_step = training_util.get_or_create_global_step()

# ==================================================
# Line: 533

global_step = training_util.get_or_create_global_step()

# ==================================================
# Line: 541

global_step = training_util.get_or_create_global_step()

# ==================================================
# Line: 567

global_step = training_util.get_or_create_global_step()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/moving_averages.py
# Occurrences: Lines 236-237 (2 instances)

biased_initializer = init_ops.zeros_initializer()

# ==================================================
# Occurrences: Lines 682-685 (5 instances)

name_map[self.average_name(v.deref())] = v.deref()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
# Occurrences: Lines 180-184 (2 instances)

before = my1.initialized_value()

# ==================================================
# Line: 192

self.assertAllEqual(session.run(my1.initialized_value()), v1)

# ==================================================
# Line: 292

my1_var_list = my1._get_variable_list()

# ==================================================
# Line: 309

my1_values = session.run(my1_var_list)

# ==================================================
# Line: 330

my1_var_list = my1._get_variable_list()

# ==================================================
# Line: 336

my1_values = session.run(my1_var_list)

# ==================================================
# Occurrences: Lines 416-419 (2 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/server_lib_multiple_containers_test.py
# Line: 40

sess = session.Session(server.target)

# ==================================================
# Line: 53

sess = session.Session(server.target)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/remapper_test.py
# Occurrences: Lines 109-113 (2 instances)

gdef_ref = tf_optimizer.OptimizeGraph(config, mg)

# ==================================================
# Occurrences: Lines 126-133 (2 instances)

output_ref = sess.run(
    model_fn, options=run_options, run_metadata=metadata)

# ==================================================
# Occurrences: Lines 326-330 (2 instances)

y = nn.bias_add(y, b, data_format=b_format)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/cluster_test.py
# Occurrences: Lines 32-33 (2 instances)

a = random_ops.random_uniform(shape=())

# ==================================================
# Occurrences: Lines 49-50 (2 instances)

a = random_ops.random_uniform(shape=())

# ==================================================
# Occurrences: Lines 67-68 (2 instances)

a = random_ops.random_uniform(shape=())

# ==================================================
# Occurrences: Lines 87-88 (2 instances)

a = random_ops.random_uniform(shape=[1024, 1024])

# ==================================================
# Occurrences: Lines 114-115 (2 instances)

a = random_ops.random_uniform(shape=())

# ==================================================
# Occurrences: Lines 138-139 (2 instances)

a = random_ops.random_uniform(shape=(2, 3))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/tf_optimizer_test.py
# Occurrences: Lines 103-104 (2 instances)

start = array_ops.placeholder(shape=[], dtype=dtypes.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
# Occurrences: Lines 97-98 (2 instances)

s = _weight([6])

# ==================================================
# Occurrences: Lines 109-110 (2 instances)

s = _weight([6])

# ==================================================
# Occurrences: Lines 450-451 (2 instances)

x = _conv_bn(x)

# ==================================================
# Occurrences: Lines 485-486 (2 instances)

x = _conv3d_bn(x)

# ==================================================
# Line: 518

output_val_ref, output_val, cost_graph = self._run(mode, output)

# ==================================================
# Line: 526

output_val_ref, output_val, cost_graph = self._run(mode, output)

# ==================================================
# Line: 548

output_val_ref, output_val, cost_graph = self._run(mode, output)

# ==================================================
# Line: 557

output_val_ref, output_val, cost_graph = self._run(mode, output)

# ==================================================
# Line: 615

output_val_ref, output_val, cost_graph = self._run(mode, output)

# ==================================================
# Line: 625

output_val_ref, output_val, cost_graph = self._run(mode, output)

# ==================================================
# Occurrences: Lines 716-717 (2 instances)

y1 = _matmul_act(x)

# ==================================================
# Occurrences: Lines 749-750 (2 instances)

init_c = _input([8, 4])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
# Occurrences: Lines 95-96 (2 instances)

w_conv1 = _weight([5, 5, 1, 32])

# ==================================================
# Occurrences: Lines 114-117 (4 instances)

x1 = random_ops.truncated_normal([1, 784], seed=0)

# ==================================================
# Occurrences: Lines 125-128 (4 instances)

x1 = random_ops.truncated_normal([1, 784], seed=0)

# ==================================================
# Occurrences: Lines 136-139 (4 instances)

x1 = random_ops.truncated_normal([1, 784], seed=0)

# ==================================================
# Occurrences: Lines 1306-1309 (4 instances)

mean = random_ops.truncated_normal([1, 1, 1, 1, 3], seed=0)

# ==================================================
# Occurrences: Lines 1384-1387 (4 instances)

scale = constant_op.constant(0.1, shape=[3])

# ==================================================
# Occurrences: Lines 1502-1503 (2 instances)

x = random_ops.truncated_normal([2, 2, 14, 14, 1], seed=0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/tf_optimizer.py
# Line: 61

out_graph = optimize_method(
    cluster.tf_cluster,
    config_proto.SerializeToString(),
    metagraph,
    verbose,
    graph_id,
    strip_default_attributes,
)

# ==================================================
# Line: 76

out_graph = optimize_method(
    cluster.tf_cluster,
    config_proto.SerializeToString(),
    metagraph,
    verbose,
    graph_id,
    strip_default_attributes,
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/constant_folding_test.py
# Line: 42

x = array_ops.zeros([10, 20, 30], dtype=dtypes.float32)

# ==================================================
# Line: 56

init_y = array_ops.zeros([10, 20, 30], dtype=dtypes.float32)

# ==================================================
# Occurrences: Lines 87-90 (2 instances)

x = resource_variable_ops.ResourceVariable(
    np.random.uniform(size=[2, 2]), dtype=dtypes.float32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/return_statements.py
# Occurrences: Lines 390-391 (2 instances)

node = qual_names.resolve(node)

# ==================================================
# Occurrences: Lines 397-398 (2 instances)

node = qual_names.resolve(node)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/utils/tensor_list_test.py
# Occurrences: Lines 35-49 (4 instances)

l = tl.dynamic_list_append(l, 1)

# ==================================================
# Occurrences: Lines 60-62 (2 instances)

_ = l.pop()

# ==================================================
# Occurrences: Lines 81-87 (6 instances)

c1 = l.count()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/lang/special_functions_test.py
# Line: 42

sl = list_ops.tensor_list_stack(l, element_dtype=dtypes.int32)

# ==================================================
# Line: 49

sl = list_ops.tensor_list_stack(l, element_dtype=dtypes.int32)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
# Line: 255

shape = array_ops.shape(s)

# ==================================================
# Line: 264

return array_ops.shape(s)[0]

# ==================================================
# Line: 276

return cond.cond(rank > 0, lambda: array_ops.shape(s)[0],

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
# Occurrences: Lines 362-363 (2 instances)

s = constant_op.constant(0, dtype=dtypes.int64)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/control_flow.py
# Line: 132

cond = array_ops.reshape(cond, ())

# ==================================================
# Line: 141

cond = array_ops.reshape(cond, ())

# ==================================================
# Line: 633

init_vars = aug_get_state()

# ==================================================
# Occurrences: Lines 641-645 (4 instances)

loop_vars = aug_get_state()  # updated by set_state() in _tf_while_loop.

# ==================================================
# Line: 689

init_vars = get_state()

# ==================================================
# Line: 699

new_loop_vars = get_state()

# ==================================================
# Line: 1077

init_vars = get_state()

# ==================================================
# Line: 1125

new_loop_vars = get_state()

# ==================================================
# Line: 1233

init_vars = get_state()

# ==================================================
# Line: 1242

new_body_vars = get_state()

# ==================================================
# Line: 1253

new_orelse_vars = get_state()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/variables_test.py
# Occurrences: Lines 24-25 (2 instances)

undefined_symbol = variables.Undefined('name')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/data_structures.py
# Occurrences: Lines 145-147 (2 instances)

inferred_shape = constant_op.constant(-1)  # unknown shape, by convention

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
# Line: 124

dataset = dataset_ops.DatasetV2.from_tensor_slices([3, 2, 1])

# ==================================================
# Line: 130

dataset = dataset_ops.DatasetV2.from_tensor_slices([3, 2, 1])

# ==================================================
# Line: 136

dataset = dataset_ops.DatasetV2.range(5).repeat().batch(2)

# ==================================================
# Line: 143

dataset = dataset_ops.DatasetV2.range(5).repeat().batch(2)

# ==================================================
# Line: 150

dataset = dataset_ops.DatasetV2.range(5).filter(lambda _: True).batch(2)

# ==================================================
# Line: 157

dataset = dataset_ops.DatasetV2.range(5).filter(lambda _: True).batch(2)

# ==================================================
# Occurrences: Lines 171-175 (2 instances)

t = py_builtins.len_(p)

# ==================================================
# Line: 634

dataset_1 = dataset_ops.DatasetV2.from_tensor_slices([False, True, False])

# ==================================================
# Line: 643

dataset_4 = dataset_ops.DatasetV2.from_tensor_slices([False, True, False])

# ==================================================
# Line: 657

dataset_1 = dataset_ops.DatasetV2.from_tensor_slices([False, True, False])

# ==================================================
# Line: 666

dataset_4 = dataset_ops.DatasetV2.from_tensor_slices([False, True, False])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
# Occurrences: Lines 477-482 (2 instances)

before_parent = Scope.copy_of(self.scope)

# ==================================================
# Occurrences: Lines 668-673 (2 instances)

node.target = self.visit(node.target)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
# Occurrences: Lines 138-143 (2 instances)

def_ = self._definition_factory()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
# Occurrences: Lines 55-57 (2 instances)

scope = activity.Scope(None)

# ==================================================
# Occurrences: Lines 68-69 (2 instances)

scope = activity.Scope(None)

# ==================================================
# Line: 192

print_args_scope = anno.getanno(print_node, NodeAnno.ARGS_SCOPE)

# ==================================================
# Line: 198

print_args_scope = anno.getanno(print_node, NodeAnno.ARGS_SCOPE)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
# Occurrences: Lines 183-183 (2 instances)

if hasattr(pattern, f) and getattr(pattern, f):

# ==================================================
# Occurrences: Lines 191-191 (2 instances)

p = getattr(pattern, f)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
# Occurrences: Lines 290-293 (2 instances)

args.defaults[i] = parser.parse_expression('None')

# ==================================================
# Line: 456

factory = self._cached_factory(fn, cache_subkey)

# ==================================================
# Line: 462

factory = self._cached_factory(fn, cache_subkey)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/parser.py
# Line: 85

block_level = len(block_indentation)

# ==================================================
# Line: 95

block_level = len(block_indentation)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/error_utils.py
# Occurrences: Lines 217-219 (2 instances)

to_ret = preferred_type(self.get_message())

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
# Line: 61

node = self.generic_visit(node)

# ==================================================
# Line: 67

node = self.generic_visit(node)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
# Occurrences: Lines 92-97 (2 instances)

orig_anno = anno.getanno(node, 'foo')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
# Occurrences: Lines 262-266 (2 instances)

ns = inspect_utils.getnamespace(test_fn)

# ==================================================
# Occurrences: Lines 304-307 (2 instances)

foo = object()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/transformer.py
# Line: 521

eof_before = len(self._output_code)

# ==================================================
# Line: 530

eof_after = len(self._output_code)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
# Occurrences: Lines 236-241 (2 instances)

k = len(self._pending_statements)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
# Line: 407

a = f(c)

# ==================================================
# Line: 418

a = f(c)

# ==================================================
# Occurrences: Lines 441-445 (2 instances)

orig_source = parser.unparse(node, indentation='  ')

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/anno_test.py
# Occurrences: Lines 52-55 (2 instances)

node_1 = ast.Name()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/impl/api_test.py
# Line: 904

cache_size_before = len(conversion._ALLOWLIST_CACHE)

# ==================================================
# Line: 913

self.assertEqual(len(conversion._ALLOWLIST_CACHE), cache_size_before + 1)

# ==================================================
# Line: 920

self.assertEqual(len(conversion._ALLOWLIST_CACHE), cache_size_before + 1)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/impl/api.py
# Line: 100

message = self.get_message()

# ==================================================
# Line: 111

return preferred_type(self.get_message())

# ==================================================
# Line: 122

return StagingError(self.get_message())

# ==================================================
# Occurrences: Lines 571-578 (2 instances)

wrapper_factory = convert(
    recursive=True, user_requested=user_requested, conversion_ctx=ctx)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
# Occurrences: Lines 108-110 (2 instances)

literal_a = default_types.Literal(1)

# ==================================================
# Occurrences: Lines 358-362 (4 instances)

list_a = default_types.List(literal(1), literal(2), literal(3))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
# Occurrences: Lines 98-107 (6 instances)

v1 = resource_variable_ops.ResourceVariable([1])

# ==================================================
# Occurrences: Lines 147-150 (2 instances)

spec_1 = tensor_spec.TensorSpec(
    None, dtype=dtypes.int32).__tf_tracing_type__(context)

# ==================================================
# Occurrences: Lines 163-166 (2 instances)

trace_a = trace_type.from_value((1, 2, 3, 4))

# ==================================================
# Occurrences: Lines 174-177 (2 instances)

trace_a = trace_type.from_value([1, 2, 3, 4])

# ==================================================
# Occurrences: Lines 197-198 (2 instances)

trace_a = trace_type.from_value(struct)

# ==================================================
# Occurrences: Lines 216-217 (2 instances)

trace_a_1 = trace_type.from_value(object_a)

# ==================================================
# Line: 541

array_ops.zeros([5, 13]),

# ==================================================
# Line: 549

lookup_call_arg = array_ops.zeros([5, 13])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
# Line: 166

named_tuple_type = type(value)

# ==================================================
# Line: 173

mapping_type = type(value)

# ==================================================
# Line: 179

type(value),

# ==================================================
# Line: 191

type(value), metadata, tuple(from_value(c, context) for c in components)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/capture/capture_container.py
# Occurrences: Lines 67-72 (4 instances)

self._by_ref_internal = py_collections.OrderedDict()

# ==================================================
# Line: 79

self._cached_capture_types = py_collections.OrderedDict()

# ==================================================
# Line: 129

graph_const = self._create_placeholder_helper(graph, tensor, name)

# ==================================================
# Line: 141

return self._create_placeholder_helper(graph, tensor, name)

# ==================================================
# Line: 228

value_nested = lam()

# ==================================================
# Line: 235

value = lam()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
# Occurrences: Lines 729-731 (2 instances)

logging_txt = free_vars_detect.generate_free_var_logging(f)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
# Occurrences: Lines 235-235 (2 instances)

signature = _make_callable_signature(obj)

# ==================================================
# Occurrences: Lines 245-245 (2 instances)

if _make_callable_signature(obj) not in fn_map:

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/capture/by_ref_capture_test.py
# Occurrences: Lines 52-52 (2 instances)

graph = ops.get_default_graph()

# ==================================================
# Occurrences: Lines 58-58 (2 instances)

graph = ops.get_default_graph()

# ==================================================
# Occurrences: Lines 90-91 (2 instances)

graph = ops.get_default_graph()

# ==================================================
# Occurrences: Lines 98-99 (2 instances)

graph = ops.get_default_graph()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
# Occurrences: Lines 96-99 (2 instances)

b = tf_f()

# ==================================================
# Occurrences: Lines 214-217 (2 instances)

_ = tf_f()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/runtime_client/runtime_client_test.py
# Line: 285

result = add(*inputs)

# ==================================================
# Line: 291

result = add(*inputs)

# ==================================================
# Line: 307

result = add(*inputs)

# ==================================================
# Line: 313

result = add(*inputs)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/transform/transform_test.py
# Line: 117

z = f(x, y)

# ==================================================
# Line: 124

z = f(x, y)

# ==================================================
# Line: 233

i = constant_op.constant(1.0)

# ==================================================
# Line: 242

one = constant_op.constant(1.0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/polymorphism/type_dispatch.py
# Occurrences: Lines 42-47 (2 instances)

self._dispatch_table = collections.OrderedDict()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
# Occurrences: Lines 318-325 (2 instances)

subtyping_time = timeit.timeit(
    lambda: cache.lookup(keys[-1]),
    number=iterations,
)

# ==================================================
# Occurrences: Lines 368-375 (2 instances)

subtyping_time = timeit.timeit(
    lambda: cache.lookup(keys[-1]),
    number=iterations,
)

# ==================================================
# Occurrences: Lines 415-420 (2 instances)

MockFunction(make_single_param_type(MockSubtypeOf2(2)), "testing"),

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
# Occurrences: Lines 257-267 (3 instances)

table_1 = type_dispatch.TypeDispatchTable()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/polymorphism/function_type.py
# Occurrences: Lines 726-728 (4 instances)

args_signature.append(to_signature(p.type_constraint))

# ==================================================
# File: /root/ecooptimizer/tensorflow/configure.py
# Occurrences: Lines 133-137 (2 instances)

output = subprocess.check_output(cmd, stderr=stderr)

# ==================================================
# Line: 1314

clang_version = retrieve_clang_version(clang_compiler_path)

# ==================================================
# Line: 1320

clang_version = retrieve_clang_version(clang_compiler_path)

# ==================================================
