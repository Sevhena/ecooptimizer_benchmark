# no-self-use snippets for tensorflow

# File: /root/ecooptimizer/tensorflow/tensorflow/lite/schema/upgrade_schema.py
# Line: 177

def _Upgrade0To1(self, data):
  """Upgrade data from Version 0 to Version 1.

  Changes: Added subgraphs (which contains a subset of formally global
  entries).

  Args:
    data: Dictionary representing the TensorFlow lite data to be upgraded.
      This will be modified in-place to be an upgraded version.
  """
  subgraph = {}
  for key_to_promote in ["tensors", "operators", "inputs", "outputs"]:
    subgraph[key_to_promote] = data[key_to_promote]
    del data[key_to_promote]
  data["subgraphs"] = [subgraph]


# ==================================================
# Line: 193

def _Upgrade1To2(self, data):
  """Upgrade data from Version 1 to Version 2.

  Changes: Rename operators to Conform to NN API.

  Args:
    data: Dictionary representing the TensorFlow lite data to be upgraded.
      This will be modified in-place to be an upgraded version.
  Raises:
    ValueError: Throws when model builtins are numeric rather than symbols.
  """

  def RemapOperator(opcode_name):
    """Go from old schema op name to new schema op name.

    Args:
      opcode_name: String representing the ops (see :schema.fbs).
    Returns:
      Converted opcode_name from V1 to V2.
    """
    old_name_to_new_name = {
        "CONVOLUTION": "CONV_2D",
        "DEPTHWISE_CONVOLUTION": "DEPTHWISE_CONV_2D",
        "AVERAGE_POOL": "AVERAGE_POOL_2D",
        "MAX_POOL": "MAX_POOL_2D",
        "L2_POOL": "L2_POOL_2D",
        "SIGMOID": "LOGISTIC",
        "L2NORM": "L2_NORMALIZATION",
        "LOCAL_RESPONSE_NORM": "LOCAL_RESPONSE_NORMALIZATION",
        "Basic_RNN": "RNN",
    }

    return (old_name_to_new_name[opcode_name]
            if opcode_name in old_name_to_new_name else opcode_name)

  def RemapOperatorType(operator_type):
    """Remap operator structs from old names to new names.

    Args:
      operator_type: String representing the builtin operator data type
        string. (see :schema.fbs).
    Raises:
      ValueError: When the model has consistency problems.
    Returns:
      Upgraded builtin operator data type as a string.
    """
    old_to_new = {
        "PoolOptions": "Pool2DOptions",
        "DepthwiseConvolutionOptions": "DepthwiseConv2DOptions",
        "ConvolutionOptions": "Conv2DOptions",
        "LocalResponseNormOptions": "LocalResponseNormalizationOptions",
        "BasicRNNOptions": "RNNOptions",
    }
    return (old_to_new[operator_type]
            if operator_type in old_to_new else operator_type)

  for subgraph in data["subgraphs"]:
    for ops in subgraph["operators"]:
      ops["builtin_options_type"] = RemapOperatorType(
          ops["builtin_options_type"])

  # Upgrade the operator codes
  for operator_code in data["operator_codes"]:
    # Check if builtin_code is the appropriate string type
    # use type("") instead of str or unicode. for py2and3
    if not isinstance(operator_code["builtin_code"], type(u"")):
      raise ValueError("builtin_code %r is non-string. this usually means "
                       "your model has consistency problems." %
                       (operator_code["builtin_code"]))
    operator_code["builtin_code"] = (RemapOperator(
        operator_code["builtin_code"]))


# ==================================================
# Line: 265

def _Upgrade2To3(self, data):
  """Upgrade data from Version 2 to Version 3.

  Changed actual read-only tensor data to be in a buffers table instead
  of inline with the tensor.

  Args:
    data: Dictionary representing the TensorFlow lite data to be upgraded.
      This will be modified in-place to be an upgraded version.
  """
  buffers = [{"data": []}]  # Start with 1 empty buffer
  for subgraph in data["subgraphs"]:
    if "tensors" not in subgraph:
      continue
    for tensor in subgraph["tensors"]:
      if "data_buffer" not in tensor:
        tensor["buffer"] = 0
      else:
        if tensor["data_buffer"]:
          tensor[u"buffer"] = len(buffers)
          buffers.append({"data": tensor["data_buffer"]})
        else:
          tensor["buffer"] = 0
        del tensor["data_buffer"]
  data["buffers"] = buffers


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/authoring/authoring.py
# Line: 139

def _get_location_string(self, location):
  """Dump location of ConveterError.errors.location."""
  callstack = []
  for single_call in reversed(location.call):
    if (location.type ==
        converter_error_data_pb2.ConverterErrorData.CALLSITELOC):
      callstack.append(
          f"  - {single_call.source.filename}:{single_call.source.line}")
    else:
      callstack.append(str(single_call))
  callstack_dump = "\n".join(callstack)
  return callstack_dump


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
# Line: 146

def eval(self, x):
  return tf.cosh(x)


# ==================================================
# Line: 185

def eval(self, x):
  return tf.cos(x)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/op_hint.py
# Line: 347

def _validate_children_inputs_mappings(self, children_inputs_mappings):
  """Validate children inputs mappings is in the right format.

  Args:
    children_inputs_mappings: the Children ophint inputs/outputs mapping.
  """
  assert isinstance(children_inputs_mappings, dict)
  assert "parent_first_child_input" in children_inputs_mappings
  assert "parent_last_child_output" in children_inputs_mappings
  assert "internal_children_input_output" in children_inputs_mappings

  # validate parent_first_child_input.

  def assert_dictlist_has_keys(dictlist, keys):
    for dikt in dictlist:
      assert isinstance(dikt, dict)
      for key in keys:
        assert key in dikt

  assert_dictlist_has_keys(
      children_inputs_mappings["parent_first_child_input"],
      ["parent_ophint_input_index", "first_child_ophint_input_index"])
  assert_dictlist_has_keys(
      children_inputs_mappings["parent_last_child_output"],
      ["parent_output_index", "child_output_index"])
  assert_dictlist_has_keys(
      children_inputs_mappings["internal_children_input_output"],
      ["child_input_index", "child_output_index"])


# ==================================================
# Line: 376

def _setattr(self, dest_op, name, value):
  tensor_value = _ops.convert_to_tensor(value)
  # pylint: disable=protected-access
  dest_op.op._set_attr(name, _attr_value_pb2.AttrValue(
      tensor=tensor_value.op.node_def.attr["value"].tensor))
  # pylint: enable=protected-access


# ==================================================
# Line: 479

def aggregate_and_return_name_for_input(self, out_graphdef):
  """This adds the node(s) to out_graphdef and returns the input node name.

  Args:
    out_graphdef: A graphdef that is ready to have this input added.

  Returns:
    The output that the stub should use as an input for this operand.

  Raises:
    RuntimeError: if the method is not implemented.
  """
  del out_graphdef
  raise RuntimeError("Unimplemented abstract method.")


# ==================================================
# Line: 494

def aggregate_and_return_name_for_output(self, fused_op_name, output_index,
                                         out_graphdef):
  """Add node(s) to graph representing output operands and returns type.

  Args:
    fused_op_name: name of the fused op stub name.
    output_index: Output index that we are currently processing from stub.
    out_graphdef: The destination graphdef we are currently building up.

  Returns:
    The datatype of this identity.

  Raises:
    RuntimeError: if the method is not implemented.
  """
  del fused_op_name, output_index, out_graphdef
  raise RuntimeError("Unimplemented abstract method.")



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite.py
# Line: 942

def _contains_function_with_implements_attr(self, saved_model_proto):
  meta_graph = saved_model_proto.meta_graphs[0]
  for function in meta_graph.graph_def.library.function:
    if function.attr.get("_implements", None) or function.attr.get(
        "api_implements", None
    ):
      return True
  return False


# ==================================================
# Line: 1010

def _get_original_model_type(self):
  """One-time getter to return original model type and set it to NONE."""
  model_type = TFLiteConverterBase._original_model_type
  TFLiteConverterBase._original_model_type = (
      conversion_metadata_fb.ModelType.NONE
  )
  return model_type


# ==================================================
# Line: 1298

def _load_saved_model(self, saved_model_dir, saved_model_tags):
  """Load graph_def from saved model with the default serving signature key.

  Args:
    saved_model_dir: Directory of the SavedModel.
    saved_model_tags: Set of tags identifying the MetaGraphDef within the
      SavedModel to analyze.

  Returns:
    graph_def: The loaded GraphDef.
    input_tensors: List of input tensors.
    output_tensors: List of output tensors.
  """
  graph = _ops.Graph()
  saved_model = _loader_impl.SavedModelLoader(saved_model_dir)
  saved_model.load_graph(graph, tags=saved_model_tags)
  meta_graph = saved_model.get_meta_graph_def_from_tags(saved_model_tags)
  graph_def = meta_graph.graph_def
  signature_def = meta_graph.signature_def[
      _signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
  ]
  input_tensors = [
      graph.get_tensor_by_name(signature_def.inputs[key].name)
      for key in signature_def.inputs
  ]
  output_tensors = [
      graph.get_tensor_by_name(signature_def.outputs[key].name)
      for key in signature_def.outputs
  ]
  return graph_def, input_tensors, output_tensors


# ==================================================
# Line: 2430

def _validate_quantized_input_stats(self, converter_kwargs, quant_mode):
  """Ensure the `quantized_input_stats` flag is provided if required."""

  quantized_types = frozenset({_dtypes.int8, _dtypes.uint8})

  requires_quantized_input_stats = (
      converter_kwargs["inference_type"] in quantized_types
      or converter_kwargs["inference_input_type"] in quantized_types
  ) and not quant_mode.is_post_training_integer_quantization()

  if (
      requires_quantized_input_stats
      and not converter_kwargs["quantized_input_stats"]
  ):
    raise ValueError(
        "The `quantized_input_stats` flag must be defined when either "
        "`inference_type` flag or `inference_input_type` flag is set to "
        "tf.int8 or tf.uint8. Currently, `inference_type={}` and "
        "`inference_input_type={}`.".format(
            _get_tf_type_name(converter_kwargs["inference_type"]),
            _get_tf_type_name(converter_kwargs["inference_input_type"]),
        )
    )


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/convert_test.py
# Line: 248

def _getGraphOpTypes(self, graphdef, output_nodes):
  """Returns used op types in `graphdef` reachable from `output_nodes`.

  This is used to check that after the stub transformation the expected
  nodes are there.

  NOTE: this is not a exact test that the graph is the correct output, but
    it balances compact expressibility of test with sanity checking.

  Args:
    graphdef: TensorFlow proto graphdef.
    output_nodes: A list of output node names that we need to reach.

  Returns:
    A set of node types reachable from `output_nodes`.
  """
  name_to_input_name, name_to_node, _ = _extract_graph_summary(graphdef)
  # Find all nodes that are needed by the outputs
  used_node_names = _bfs_for_reachable_nodes(output_nodes, name_to_input_name)
  return set([name_to_node[node_name].op for node_name in used_node_names])


# ==================================================
# Line: 269

def _countIdentities(self, nodes):
  """Count the number of "Identity" op types in the list of proto nodes.

  Args:
    nodes: NodeDefs of the graph.

  Returns:
    The number of nodes with op type "Identity" found.
  """
  return len([x for x in nodes if x.op == "Identity"])


# ==================================================
# Occurrences: Lines 379-385 (3 instances)

def _get_input_index(self, x):
  return x.op.node_def.attr[op_hint.OpHint.FUNCTION_INPUT_INDEX_ATTR].i


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable.py
# Occurrences: Lines 79-94 (6 instances)

def increase_counter_debugger_creation(self):
  _counter_debugger_creation.get_cell().increase_by(1)


# ==================================================
# Line: 105

def set_converter_latency(self, value):
  _gauge_conversion_latency.get_cell().set(value)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/metrics/metrics_portable_test.py
# Occurrences: Lines 23-42 (6 instances)

def test_TFLiteMetrics_creation_success(self):
  metrics.TFLiteMetrics()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
# Occurrences: Lines 53-56 (2 instances)

def test_TFLiteMetrics_creation_no_arg_success(self):
  metrics.TFLiteMetrics()


# ==================================================
# Line: 130

def _constructGraphDef(self):
  with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[None, 16, 16, 3], dtype=dtypes.float32, name='in_tensor')
    math_ops.add(in_tensor, in_tensor, name='add')
    sess = session.Session()

  return (
      convert_to_constants.convert_variables_to_constants_from_session_graph(
          sess, sess.graph_def, ['add']))


# ==================================================
# Line: 181

def _getIntegerQuantizeModel(self):
  np.random.seed(0)

  root = autotrackable.AutoTrackable()

  @tf.function(
      input_signature=[tf.TensorSpec(shape=[1, 5, 5, 3], dtype=tf.float32)])
  def func(inp):
    conv = tf.nn.conv2d(
        inp, tf.ones([3, 3, 3, 16]), strides=[1, 1, 1, 1], padding='SAME')
    output = tf.nn.relu(conv, name='output')
    return output

  def calibration_gen():
    for _ in range(5):
      yield [np.random.uniform(-1, 1, size=(1, 5, 5, 3)).astype(np.float32)]

  root.f = func
  to_save = root.f.get_concrete_function()
  return (root, to_save, calibration_gen)


# ==================================================
# Line: 224

def test_conversion_from_keras_v2(self):
  x = [-1, 0, 1, 2, 3, 4]
  y = [-3, -1, 1, 3, 5, 7]
  model = tf.keras.models.Sequential(
      [tf.keras.layers.Dense(units=1, input_shape=[1])])
  model.compile(optimizer='sgd', loss='mean_squared_error')
  model.fit(x, y, epochs=1)
  converter = lite.TFLiteConverterV2.from_keras_model(model)
  mock_metrics = mock.create_autospec(
      metrics.TFLiteConverterMetrics, instance=True)
  converter._tflite_metrics = mock_metrics
  converter.convert()
  mock_metrics.assert_has_calls([
      mock.call.increase_counter_converter_attempt(),
      mock.call.increase_counter_converter_success(),
      mock.call.export_metrics(),
      mock.call.set_converter_param('inference_type', 'tf.float32'),
      mock.call.set_converter_param('target_ops', 'TFLITE_BUILTINS'),
      mock.call.set_converter_param('optimization_default', 'False'),
  ], any_order=True)  # pyformat: disable


# ==================================================
# Line: 279

def disable_converter_counter_metrics(self, tflite_metrics):

  def empty_func():
    pass

  tflite_metrics.increase_counter_converter_attempt = empty_func
  tflite_metrics.increase_counter_converter_success = empty_func


# ==================================================
# Line: 401

def call(self, input_tensor, **kwargs):
  return mock_ngrams(input_tensor, width=2, axis=-1, string_separator=' ')


# ==================================================
# Line: 526

def serving_default(self, a, b):
  return tf.add(a, b, name='add')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite_test.py
# Line: 844

def _getIntegerQuantizeModel(self, num_filters=16):
  np.random.seed(0)
  inp = array_ops.placeholder(
      dtype=dtypes.float32, shape=(1, 5, 5, 3), name='input')
  conv = nn_ops.conv2d(
      inp,
      filter=array_ops.ones([3, 3, 3, num_filters]),
      strides=[1, 1, 1, 1],
      padding='SAME')
  output = nn_ops.relu(conv, name='output')

  def calibration_gen():
    for _ in range(5):
      yield [np.random.uniform(-1, 1, size=(1, 5, 5, 3)).astype(np.float32)]

  return (inp, output, calibration_gen)


# ==================================================
# Line: 1510

def testResizingIntermediateDynamicTensor(self):
  # This is a regression test for the case where shape of dynamic output
  # tensors changes between invocations.
  # See also https://github.com/tensorflow/tensorflow/issues/26549
  with ops.Graph().as_default():
    input_tensor = array_ops.placeholder(shape=[1, 1], dtype=dtypes.float32)
    input2_tensor = array_ops.placeholder(shape=[1], dtype=dtypes.float32)

    # The bug is triggered only when dynamic tensor is intermediate. Putting
    # some other ops around it.
    neg = math_ops.negative(input2_tensor)
    padding = array_ops.placeholder(shape=[2, 2], dtype=dtypes.int32)
    output_tensor = array_ops.pad(input_tensor, padding) + neg

    sess = session.Session()

  converter = lite.TFLiteConverter.from_session(
      sess, [input_tensor, padding, input2_tensor], [output_tensor])
  tflite_model = converter.convert()

  interpreter = Interpreter(model_content=tflite_model)
  interpreter.allocate_tensors()

  input_details = interpreter.get_input_details()
  interpreter.set_tensor(input_details[1]['index'],
                         np.array([[1, 1], [1, 1]], dtype=np.int32))
  interpreter.invoke()

  # Without the fix, invocation will fail when changing the shape of
  # intermediate dynamic tensors.
  interpreter.set_tensor(input_details[1]['index'],
                         np.array([[2, 2], [2, 2]], dtype=np.int32))
  interpreter.invoke()


# ==================================================
# Line: 2681

def _getSparsificableModel(self, matrix_b_values):
  with ops.Graph().as_default():
    in_tensor_1 = array_ops.placeholder(
        shape=[16, 4], dtype=dtypes.float32, name='input1')
    in_tensor_2 = constant_op.constant(
        matrix_b_values, shape=[4, 8], dtype=dtypes.float32)
    out_tensor = math_ops.matmul(in_tensor_1, in_tensor_2)
    sess = session.Session()

  return (sess, [in_tensor_1], [out_tensor])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
# Line: 71

def _evaluateTFLiteModelUsingSignatureDef(self, tflite_model, signature_key,
                                          inputs):
  """Evaluates the model on the `inputs`.

  Args:
    tflite_model: TensorFlow Lite model.
    signature_key: Signature key.
    inputs: Map from input tensor names in the SignatureDef to tensor value.

  Returns:
    Dictionary of outputs.
    Key is the output name in the SignatureDef 'signature_key'
    Value is the output value
  """
  interpreter = Interpreter(model_content=tflite_model)
  signature_runner = interpreter.get_signature_runner(signature_key)
  return signature_runner(**inputs)


# ==================================================
# Line: 89

def _getSimpleVariableModel(self):
  root = autotrackable.AutoTrackable()
  root.v1 = variables.Variable(3.)
  root.v2 = variables.Variable(2.)
  root.f = def_function.function(lambda x: root.v1 * root.v2 * x)
  return root


# ==================================================
# Line: 184

def _getSqrtModel(self):
  """Returns a model with only one sqrt op, to test non-quantizable op."""

  @def_function.function(input_signature=[
      tensor_spec.TensorSpec(shape=(1, 10), dtype=dtypes.float32)
  ])
  def sqrt(x):
    return math_ops.sqrt(x)

  def calibration_gen():
    for _ in range(5):
      yield [np.random.uniform(0, 16, size=(1, 10)).astype(np.float32)]

  return sqrt, calibration_gen


# ==================================================
# Line: 291

def _getInfFloatModel(self):
  root = autotrackable.AutoTrackable()
  root.v = constant_op.constant([np.inf], shape=(), dtype=dtypes.float32)
  root.f = def_function.function(lambda x: root.v)
  return root

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/interpreter_test.py
# Line: 100

def testPathLikeModel(self):
  interpreter = interpreter_wrapper.Interpreter(
      model_path=pathlib.Path(
          resource_loader.get_path_to_datafile(
              'testdata/permute_float.tflite'
          )
      ),
  )
  interpreter.allocate_tensors()


# ==================================================
# Line: 330

def testCreationCounter(self, increase_call):
  interpreter_wrapper.Interpreter(
      model_path=resource_loader.get_path_to_datafile(
          'testdata/permute_float.tflite'))
  increase_call.assert_called_once()



# ==================================================
# Line: 379

def testEmptyInputTensor(self):

  class TestModel(tf.keras.models.Model):

    @tf.function(
        input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
    def TestSum(self, x):
      return tf.raw_ops.Sum(input=x, axis=[0])

  test_model = TestModel()
  converter = lite.TFLiteConverterV2.from_concrete_functions([
      test_model.TestSum.get_concrete_function(
          tf.TensorSpec([None], tf.float32))
  ], test_model)
  model = converter.convert()
  interpreter = lite.Interpreter(model_content=model)
  # Make sure that passing empty tensor doesn't cause any errors.
  interpreter.get_signature_runner()(x=tf.zeros([0], tf.float32))



# ==================================================
# Line: 385

def TestSum(self, x):
  return tf.raw_ops.Sum(input=x, axis=[0])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite_v2_test.py
# Line: 277

def _getIntegerQuantizeModel(self, num_filters=16):
  np.random.seed(0)

  root = autotrackable.AutoTrackable()

  @tf.function(
      input_signature=[tf.TensorSpec(shape=[1, 5, 5, 3], dtype=tf.float32)]
  )
  def func(inp):
    conv = tf.nn.conv2d(
        inp,
        tf.ones([3, 3, 3, num_filters]),
        strides=[1, 1, 1, 1],
        padding='SAME',
    )
    output = tf.nn.relu(conv, name='output')
    return output

  def calibration_gen():
    for _ in range(5):
      yield [np.random.uniform(-1, 1, size=(1, 5, 5, 3)).astype(np.float32)]

  root.f = func
  to_save = root.f.get_concrete_function()
  return (root, to_save, calibration_gen)


# ==================================================
# Line: 390

def _createV2QATSavedModelWithFloatOpsAtEnd(self):
  """Create a simple QAT SavedModel that includes float ops at the end."""
  saved_model_dir = os.path.join(self.get_temp_dir(), 'qat_float_ops_at_end')
  input_tensor = tf.keras.layers.Input((32, 32, 128))

  class _FakeQuantArgsLayer(tf.keras.layers.Layer):
    """A fake quantization layer with fake_quant_with_min_max_args.

    Keras 3 requires wrapping the tf function inside Keras layer.
    """

    def call(self, x):
      return tf.quantization.fake_quant_with_min_max_args(x, -3.0, 3.0)

  x = _FakeQuantArgsLayer()(input_tensor)
  x = tf.keras.layers.Conv2D(1, (3, 3), bias_initializer='ones')(x)
  x = _FakeQuantArgsLayer()(x)
  # Exclude the quantization of the following Dense layer by not putting
  # fake quant layer after the dense layer.
  output_tensor = tf.keras.layers.Dense(
      1, activation='sigmoid', bias_initializer='ones'
  )(x)
  model = tf.keras.Model(input_tensor, output_tensor)
  model.save(saved_model_dir)
  return saved_model_dir


# ==================================================
# Line: 401

def call(self, x):
  return tf.quantization.fake_quant_with_min_max_args(x, -3.0, 3.0)


# ==================================================
# Line: 813

def func(self, input_tensor):
  x = tf.quantization.fake_quant_with_min_max_args(
      input_tensor, -3.0, 3.0
  )
  x = tf.gather_nd(x, [[0, 0], [1, 1]])
  return tf.quantization.fake_quant_with_min_max_args(x, -3.0, 3.0)


# ==================================================
# Line: 891

def _getIntegerQuantizationModelWithFlexOp(self):
  np.random.seed(0)

  root = autotrackable.AutoTrackable()

  @tf.function(
      input_signature=[tf.TensorSpec(shape=[3, 3, 3, 3, 3], dtype=tf.float32)]
  )
  def func(inp):
    tanh = tf.math.tanh(inp)
    # Flex delegate will merge the consecutive conv3d and erf ops into one
    # Delegate node.
    conv3d = tf.nn.conv3d(
        tanh,
        tf.ones([3, 3, 3, 3, 3]),
        strides=[1, 1, 1, 1, 1],
        padding='SAME',
    )
    erf = tf.math.erf(conv3d)
    output = tf.math.tanh(erf)
    return output

  def calibration_gen():
    for _ in range(5):
      yield [
          np.random.uniform(-1, 1, size=(3, 3, 3, 3, 3)).astype(np.float32)
      ]

  root.f = func
  return (root, root.f.get_concrete_function(), calibration_gen)


# ==================================================
# Line: 997

def _getIntegerQuantizationModelWithUnsupportedOps(self):
  np.random.seed(0)

  root = autotrackable.AutoTrackable()

  @tf.function(
      input_signature=[
          tf.TensorSpec(shape=[3], dtype=tf.float32),
          tf.TensorSpec(shape=[3], dtype=tf.float32),
      ]
  )
  def func(a, b):
    # ceil kernel does not support int8 nor int16 types neither.
    left = tf.math.ceil(a)
    right = tf.nn.tanh(b)
    add = tf.math.add(left, right)
    # ceil kernel does not support int8 nor int16 types neither.
    output = tf.math.ceil(add)
    return (output, right)

  def calibration_gen():
    for _ in range(5):
      yield [
          np.random.uniform(-1, 1, size=(3)).astype(np.float32),
          np.random.uniform(-1, 1, size=(3)).astype(np.float32),
      ]

  root.f = func
  return (root, root.f.get_concrete_function(), calibration_gen)


# ==================================================
# Line: 1099

def _getIntegerQuantizationModelWithControlFlow(self):
  def true_fn(x):
    return x

  def false_fn(x):
    return x

  @tf.function(
      input_signature=[
          tf.TensorSpec(shape=[1, 2], dtype=tf.float32),
          tf.TensorSpec(shape=(), dtype=tf.bool),
      ]
  )
  def model(x, b):
    x = x + x
    x = tf.cond(b, true_fn=lambda: true_fn(x), false_fn=lambda: false_fn(x))
    return x + x

  def calibration_gen():
    for _ in range(5):
      yield [
          np.random.uniform(
              -1,
              1,
              size=(
                  1,
                  2,
              ),
          ).astype(np.float32),
          tf.constant(True),
      ]
    for _ in range(5):
      yield [
          np.random.uniform(
              -1,
              1,
              size=(
                  1,
                  2,
              ),
          ).astype(np.float32),
          tf.constant(False),
      ]

  return (model, model.get_concrete_function(), calibration_gen)


# ==================================================
# Line: 1391

def _getIntegerQuantizeDenseModel(self, num_filters=32):
  np.random.seed(0)

  root = autotrackable.AutoTrackable()

  @tf.function(
      input_signature=[tf.TensorSpec(shape=[1, 16], dtype=tf.float32)]
  )
  def func(inp):
    dense = tf.matmul(a=inp, b=tf.ones([16, num_filters]))
    output = tf.nn.relu(dense, name='output')
    return output

  def calibration_gen():
    for _ in range(5):
      yield [np.random.uniform(-1, 1, size=(1, 16)).astype(np.float32)]

  root.f = func
  to_save = root.f.get_concrete_function()
  return (root, to_save, calibration_gen)


# ==================================================
# Line: 1634

def _createV2QATSavedModel(self, shape):
  """Create a simple QAT SavedModel in TF 2."""
  saved_model_dir = os.path.join(self.get_temp_dir(), 'saved_model')
  input_name = 'input'
  output_name = 'scores'

  class _FakeQuantArgsLayer(tf.keras.layers.Layer):
    """A fake quantization layer with fake_quant_with_min_max_args.

    Keras 3 requires wrapping the tf function inside Keras layer.
    """

    def call(self, x):
      return tf.quantization.fake_quant_with_min_max_args(x, -3.0, 3.0)

  input_tensor = tf.keras.layers.Input((32, 32, 128), name=input_name)
  x = _FakeQuantArgsLayer()(input_tensor)
  x = tf.keras.layers.Conv2D(1, (3, 3))(x)
  x = _FakeQuantArgsLayer()(x)
  scores = tf.keras.layers.Reshape((-1,), name=output_name)(x)
  model = tf.keras.Model(input_tensor, scores)
  model.save(saved_model_dir)
  return saved_model_dir, input_name, output_name


# ==================================================
# Line: 1646

def call(self, x):
  return tf.quantization.fake_quant_with_min_max_args(x, -3.0, 3.0)


# ==================================================
# Line: 2731

def call(self, x):
  return tf.quantization.fake_quant_with_min_max_args(x, -3.0, 3.0)


# ==================================================
# Line: 2797

def call(self, x):
  return tf.quantization.fake_quant_with_min_max_vars(
      x, -3.0, 3.0, narrow_range=True)


# ==================================================
# Line: 3583

def call(self, x):
  return tf.quantization.fake_quant_with_min_max_vars(
      x, -3.0, 3.0, narrow_range=True)


# ==================================================
# Line: 4357

def _getIntegerQuantizeModelWithUnknownShapes(self):
  np.random.seed(0)

  @tf.function(
      input_signature=[tf.TensorSpec(shape=[None, 33], dtype=tf.float32)]
  )
  def model(input_tensor):
    """Define a model with tf.MatMul and unknown shapes."""
    # We need the tensor to have more than 1024 elements for quantize_weights
    # to kick in. Thus, the [33, 33] shape.
    const_tensor = tf.constant(
        np.random.uniform(low=-10.0, high=10.0, size=[33, 33]),
        shape=[33, 33],
        dtype=tf.float32,
        name='inputB',
    )

    shape = tf.shape(input_tensor)
    fill = tf.transpose(tf.fill(shape, 1.0))
    mult = tf.matmul(fill, input_tensor)
    return tf.matmul(mult, const_tensor)

  root = autotrackable.AutoTrackable()
  root.f = model
  concrete_func = root.f.get_concrete_function()

  def calibration_gen():
    for batch in range(5, 20, 5):
      for _ in range(5):
        yield [np.random.uniform(-1, 1, size=(batch, 33)).astype(np.float32)]

  return root, concrete_func, calibration_gen


# ==================================================
# Line: 5159

def _run(self, experimental_preserve_all_tensors):
  @tf.function
  def f(x):
    y = tf.add(x, x, name='y')
    z = tf.add(y, y, name='z')
    w = tf.add(z, z, name='w')
    return w

  # NOTE this is exactly representable as a float as are the intermediates of
  # f. So direct comparison is ok below.

  input_data = np.array(2.0, np.float32)
  concrete_func = f.get_concrete_function(input_data)
  converter = lite.TFLiteConverterV2.from_concrete_functions(
      [concrete_func], f
  )
  tflite_model = converter.convert()
  interp = interpreter.Interpreter(
      model_content=tflite_model,
      experimental_preserve_all_tensors=experimental_preserve_all_tensors,
  )
  interp.allocate_tensors()
  interp.set_tensor(interp.get_input_details()[0]['index'], input_data)
  interp.invoke()
  out = interp.get_tensor(interp.get_output_details()[0]['index'])
  tensors = {}
  for t in interp.get_tensor_details():
    # With Tensorflow Lite default delegate applied to the model graph, the
    # access to original tensors of a delegated op could cause a ValueError
    # (i.e. 'Tensor data is null. Run allocate_tensors() first') to be thrown
    # out because the tensor memory isn't allocated at all.
    val = None
    try:
      val = interp.get_tensor(t['index'])
    except ValueError:
      pass
    tensors.update({t['name']: val})
  return (tensors, out)


# ==================================================
# Line: 5249

def _getSparsificableModel(self, matrix_b_values):
  np.random.seed(0)
  root = autotrackable.AutoTrackable()

  @tf.function(
      input_signature=[tf.TensorSpec(shape=[16, 4], dtype=tf.float32)]
  )
  def func(inp):
    matrix_b = tf.constant(matrix_b_values, dtype=tf.float32)
    matrix_b = tf.reshape(matrix_b, [4, 8])
    matmul = tf.matmul(inp, matrix_b, transpose_a=False, transpose_b=False)
    output = tf.nn.relu(matmul, name='output')
    return output

  root.f = func
  to_save = root.f.get_concrete_function()
  return (root, to_save)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
# Occurrences: Lines 63-66 (2 instances)

def _getArrayNames(self, tensors):
  return [tensor.name for tensor in tensors]


# ==================================================
# Line: 78

def _convertSavedModel(self,
                       saved_model_dir,
                       input_arrays=None,
                       input_shapes=None,
                       output_arrays=None,
                       tag_set=None,
                       signature_key=None):
  if tag_set is None:
    tag_set = set([tag_constants.SERVING])
  if signature_key is None:
    signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
  graph_def, in_tensors, out_tensors, _ = (
      convert_saved_model.freeze_saved_model(
          saved_model_dir=saved_model_dir,
          input_arrays=input_arrays,
          input_shapes=input_shapes,
          output_arrays=output_arrays,
          tag_set=tag_set,
          signature_key=signature_key))
  return graph_def, in_tensors, out_tensors


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/lite_flex_test.py
# Line: 206

def _createGraphWithCustomOp(self, opname='CustomAdd'):
  custom_opdefs_str = (
      'name: \'' + opname + '\' input_arg: {name: \'Input1\' type: DT_FLOAT} '
      'input_arg: {name: \'Input2\' type: DT_FLOAT} output_arg: {name: '
      '\'Output\' type: DT_FLOAT}')

  # Create a graph that has one add op.
  new_graph = graph_pb2.GraphDef()
  with ops.Graph().as_default():
    with session.Session() as sess:
      in_tensor = array_ops.placeholder(
          shape=[1, 16, 16, 3], dtype=dtypes.float32, name='input')
      out_tensor = in_tensor + in_tensor
      inputs = {'x': in_tensor}
      outputs = {'z': out_tensor}

      new_graph.CopyFrom(sess.graph_def)

  # Rename Add op name to opname.
  for node in new_graph.node:
    if node.op.startswith('Add'):
      node.op = opname
      del node.attr['T']

  # Register custom op defs to import modified graph def.
  register_custom_opdefs([custom_opdefs_str])

  return (new_graph, inputs, outputs)


# ==================================================
# Line: 401

def conv_func(self, in_tensor, filter_tensor):
  bias = constant_op.constant(3., shape=[1])
  conv_tensor = tf.nn.conv2d(
      in_tensor,
      filter_tensor,
      strides=[1, 1, 1, 1],
      dilations=[1, 1, 1, 1],
      padding='VALID',
      data_format='NHWC')
  conv_tensor = conv_tensor + bias
  return tf.nn.relu(conv_tensor)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/kernels/variants/py/end_to_end_test.py
# Line: 36

def _get_interpreter_from_c_func(self, func):
  concrete_function_list = [func.get_concrete_function()]

  converter = lite.TFLiteConverterV2.from_concrete_functions(
      concrete_function_list
  )
  # Don't allow flex ops.
  converter.target_spec.supported_ops = [
      lite.OpsSet.TFLITE_BUILTINS,
  ]
  converter.allow_custom_ops = True
  converter.legalize_custom_tensor_list_ops = True
  converter._experimental_lower_tensor_list_ops = False

  tfl_model = converter.convert()

  # Instantiate interpreter with custom tensor list ops.
  interpreter = _interpreter.InterpreterWithCustomOps(
      model_content=tfl_model,
      custom_op_registerers=[register_list_ops_py.TFLRegisterListOps],
  )
  return interpreter


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/c/experimental/saved_model/internal/testdata/gen_saved_models.py
# Line: 79

def compute(self, value):
  acc, _ = while_loop.while_loop(
      cond=lambda acc, i: i > 0,
      body=lambda acc, i: (acc + i, i - 1),
      loop_vars=(constant_op.constant(0.0), value))
  return acc


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/concurrency_test.py
# Line: 57

def add(self, x, y):
  res = math_ops.add(x, y)
  return {'output': res}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
# Line: 75

def _get_dir_size(self, path: str = '.'):
  """Get the total size of files and sub-directories under the path.

  Args:
    path: Path of a directory or a file to calculate the total size.

  Returns:
    Total size of the directory or a file.
  """
  total = 0
  for root, _, files in os.walk(path):
    for filename in files:
      total += os.path.getsize(os.path.join(root, filename))
  return total


# ==================================================
# Line: 90

def _any_log_contains(
    self, substring: str, log_record_list: List['logging.LogRecord']

# ==================================================
# Line: 111

def _is_quantized_function(self, func: function_pb2.FunctionDef) -> bool:
  """Determine whether a FunctionDef is quantized.

  Args:
    func: A FunctionDef object.

  Returns:
    True iff `func` is quantized.
  """
  return func.signature.name.startswith('quantized_')


# ==================================================
# Line: 122

def _is_composite_function(self, func: function_pb2.FunctionDef) -> bool:
  """Determine whether a FunctionDef is composite function.

  Args:
    func: A FunctionDef object.

  Returns:
    True iff `func` is composte function.
  """
  return func.signature.name.startswith('composite_')


# ==================================================
# Line: 133

def _contains_op_with_name_and_attribute(
    self,
    nodes: Iterable[node_def_pb2.NodeDef],
    op_name: str,
    attr_name: str,
    attr_val: _AttrValType,
    node_name: str = '',

# ==================================================
# Line: 285

def _count_op_with_name_and_attribute(
    self,
    nodes: Iterable[node_def_pb2.NodeDef],
    op_name: str,
    attr_name: str,
    attr_val: _AttrValType,
    get_op_name: bool = False,

# ==================================================
# Line: 326

def _create_simple_tf1_conv_model(
    self,
    input_shape: Sequence[int] = (1, 3, 4, 3),
    filter_shape: Sequence[int] = (2, 3, 3, 2),
    use_variable_for_filter=False,

# ==================================================
# Line: 365

def _create_simple_tf1_gather_model(
    self, input_type: dtypes.DType, use_variable_for_filter=False

# ==================================================
# Line: 854

def _create_data_generator(
    self,
    input_key: str,
    shape: Sequence[int],
    minval: float = -1.0,
    maxval: float = 1.0,
    dtype: dtypes.DType = dtypes.float32,
    num_examples: int = 8,

# ==================================================
# Line: 883

def _save_tf1_model(
    self,
    sess: session.Session,
    saved_model_path: str,
    signature_key: str,
    tags: Collection[str],
    inputs: Mapping[str, core.Tensor],
    outputs: Mapping[str, core.Tensor],
    init_op: Optional[ops.Operation] = None,
    assets_collection: Optional[Sequence[core.Symbol]] = None,

# ==================================================
# Line: 1342

def _prepare_sample_einsum_datashapes(
    self,
    equation: str,
    generate_unknown_shape_signature: bool = False,
    use_bias: bool = False,

# ==================================================
# Occurrences: Lines 1531-1535 (2 instances)

def condition(self, x, w):
  return math_ops.reduce_sum(x, keepdims=False) < 100


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
# Line: 229

def _simple_model_data_gen(self) -> repr_dataset.RepresentativeDataset:
  """Creates an interable of representative samples.

  Yields:
    Representative samples, which is basically a mapping of: input key ->
    input value.
  """
  for _ in range(8):
    yield {
        'input_tensor': ops.convert_to_tensor(
            np.random.uniform(low=0, high=150, size=(1, 4)).astype('f4')
        ),
    }


# ==================================================
# Line: 398

def multiple_output_ops(
    self, input_tensor: core.Tensor

# ==================================================
# Line: 413

def duplicate_outputs(
    self, input_tensor: core.Tensor

# ==================================================
# Line: 429

def return_higher_index_only(
    self, input_tensor: core.Tensor

# ==================================================
# Line: 6002

def _run_model_in_sess(self, model_dir, tags, signature_key, sample_inputs):
  with tensorflow.compat.v1.Session(graph=tensorflow.Graph()) as sess:
    meta_graph = saved_model_loader.load(sess, tags, export_dir=model_dir)
    signature_def = meta_graph.signature_def[signature_key]

    # DumpTensorOp only works in graph mode.
    # Execute the model using session to run DumpTensorOp.
    output_tensor_names = [
        output_tensor_info.name
        for output_tensor_info in signature_def.outputs.values()
    ]

    output_values = []
    for sample_input in sample_inputs:
      feed_dict = {}
      for input_key, input_value in sample_input.items():
        input_tensor_name = signature_def.inputs[input_key].name
        feed_dict[input_tensor_name] = input_value

      # Obtain the output of the model.
      output_values.append(
          sess.run(output_tensor_names, feed_dict=feed_dict)[0]
      )
  return output_values


# ==================================================
# Line: 6027

def _read_tensor_array_file(self, file_path):
  tensor_protos = []
  for raw_record in tf_record.tf_record_iterator(file_path, options='ZLIB'):
    tensor_protos.append(
        tensorflow.make_ndarray(tensor_pb2.TensorProto.FromString(raw_record))
    )
  return np.array(tensor_protos)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset.py
# Line: 277

def _load_tf_record(self, tf_record_path: str) -> RepresentativeDataset:
  """Loads TFRecord containing samples of type`RepresentativeDataSample`."""
  samples = []
  with context.eager_mode():
    for sample_bytes in readers.TFRecordDatasetV2(filenames=[tf_record_path]):
      sample_proto = _RepresentativeDataSample.FromString(
          sample_bytes.numpy()
      )
      sample = {}
      for input_key, tensor_proto in sample_proto.tensor_proto_inputs.items():
        sample[input_key] = tensor_util.MakeNdarray(tensor_proto)
      samples.append(sample)
  return samples


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/py_function_lib.py
# Line: 629

def save_exported_model(
    self,
    dst_saved_model_path: str,
    exported_model_serialized: bytes,
    src_saved_model_path: str,
    tags: set[str],
    serialized_signature_def_map: dict[str, bytes],

# ==================================================
# Line: 681

def run_calibration(
    self,
    saved_model_path: str,
    signature_keys: list[str],
    tags: set[str],
    force_graph_mode_calibration: bool,
    representative_dataset_file_map_serialized: dict[str, bytes],

# ==================================================
# Line: 734

def get_calibration_min_max_value(
    self,
    calibration_statistics_serialized: bytes,
    calibration_options_serialized: bytes,

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/stablehlo/python/integration_test/quantize_model_test_base.py
# Line: 62

def _extract_first_xla_call_module_op(
    self, output_saved_model_path: str

# ==================================================
# Line: 82

def _get_num_xla_call_module_op(self, output_saved_model_path: str) -> int:
  """Gets the number of XlaCallModule ops in the output saved model."""
  root = load.load(output_saved_model_path)
  tf_graph_def = root.signatures['serving_default'].graph.as_graph_def()
  count = 0
  for node_def in tf_graph_def.node:
    if node_def.op == 'XlaCallModule':
      count += 1
  for function in tf_graph_def.library.function:
    for node_def in function.node_def:
      if node_def.op == 'XlaCallModule':
        count += 1
  return count


# ==================================================
# Line: 96

def _get_function_aliases(
    self, output_saved_model_path: str, tags: List[str]

# ==================================================
# Line: 170

def _any_log_contains(
    self, substring: str, log_record_list: List['logging.LogRecord']

# ==================================================
# Line: 399

def _create_add_model(
    self,
    shape: Sequence[int],
    saved_model_path: str,

# ==================================================
# Line: 411

def add(self, input_tensor: core.Tensor) -> Mapping[str, core.Tensor]:
  """Performs an add operation.

  Args:
    input_tensor: Input tensor to perform add on.

  Returns:
    A map of: output key -> output result.
  """
  out = math_ops.add(input_tensor, input_tensor)
  return {'output': out}


# ==================================================
# Line: 442

def _prepare_sample_einsum_datashapes(
    self,
    equation: str,
    generate_unknown_shape_signature: bool = False,
    use_bias: bool = False,

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/stablehlo/python/integration_test/quantize_model_test.py
# Line: 853

def matmul(self, input_tensor: core.Tensor) -> Mapping[str, core.Tensor]:
  """Performs a matrix multiplication.

  Args:
    input_tensor: Input tensor to matmul with the filter.

  Returns:
    A 'output' -> output tensor mapping
  """
  out = math_ops.matmul(input_tensor, random_tensor_gen_fn((2, 3)))
  out = math_ops.matmul(out, random_tensor_gen_fn((3, 4)))
  return {'output': out}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/tensorflow_to_stablehlo/python/integration_test/tensorflow_to_stablehlo_test.py
# Line: 28

def call(self, x):
  return x + 1


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
# Line: 384

def res_name(self, ns, types_ns, name):
  name_str = str(name)
  if name_str in TFR_BUILTINS:
    return {TFRTypes.TFR_BUILTIN_FUNC}, name_str
  if name_str in ns:
    ns_val = ns[name_str]
    return {type(ns_val)}, ns_val
  if name_str in __builtins__:
    return {TFRTypes.PY_BUILTIN_FUNC}, __builtins__[name_str]
  # This name is not in the namespace because the autograph transformation
  # is not backloaded into Python.
  if name_str == 'ag__':
    return {type(AG_MODULE)}, AG_MODULE

  return None, None


# ==================================================
# Line: 400

def res_value(self, ns, value):
  # resolves the type of the symbol by the metadata in 'value'
  if value is None:
    return {TFRTypes.NONE}
  if value in (TFRTypes.SHAPE, TFRTypes.TF_TENSOR_SHAPE_FUNC):
    # See TFRTypes.__getattribute__.
    # TODO(mdan): Replacing the enum with classes would avoid this overlap.
    return {value}
  # TODO(mdan): Index more efficiently. Could do a name check instead.
  if any(v is value for v in AG_MODULE.__dict__.values()):
    return {TFRTypes.AG_BUILTIN_FUNC}
  if getattr(value, '__name__', None) == 'tensorflow.raw_ops':
    return {types.ModuleType}
  if hasattr(value, '__module__'):
    if isinstance(value, dtypes.DType):
      return {TFRTypes.ATTR}

    # All the imported operations, which are not autograph built-ins, are
    # considered to be TF raw ops.
    # TODO(fengliuai): refine the condition that we only match TensorFlow
    # ops here.
    return {TFRTypes.TF_RAW_OP}
  # TODO(mdan): Is ATTR equivalent to string?
  return {_PY_TYPE_TO_TFR.get(type(value), TFRTypes.ATTR)}


# ==================================================
# Line: 536

def res_slice(self, ns, types_ns, node_or_slice, value, slice_):
  if not value:
    return value

  if isinstance(value, set):
    type_tuple = value.pop()
    if isinstance(type_tuple, tuple):
      value = {type_tuple[node_or_slice]}
    else:
      value = {type_tuple}

  assert len(value) == 1
  value, = tuple(value)
  if value == TFRTypes.TF_TENSOR_SHAPE_LIST:
    # TODO(mdan): This is not entirely correct for multi-element slices.
    return {int}
  elif value in (TFRTypes.TENSOR_LIST, TFRTypes.TENSOR):
    # TODO(mdan): This is not entirely correct for multi-element slices.
    return {TFRTypes.TENSOR}
  else:
    return {value}


# ==================================================
# Occurrences: Lines 558-569 (4 instances)

def res_compare(self, ns, types_ns, node, left, right):
  # TODO(fengliuai): make sure left and right are compatible
  return {TFRTypes.I1}


# ==================================================
# Line: 648

def _create_mlir_loc(self, loc):
  """Creates mlir location from autograph ORIGIN value.

  Args:
    loc: OriginInfo

  Returns:
    A serialized mlir location string.
  """
  if loc is not None and loc.loc.filename:
    file_name = os.path.basename(loc.loc.filename)
    return 'loc("{}":{}:{})'.format(file_name, loc.loc.lineno,
                                    loc.loc.col_offset)
  else:
    return 'loc(unknown)'


# ==================================================
# Line: 739

def _op_def(self, op_name):
  return op_def_registry.get(op_name)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/tfr/python/op_reg_gen.py
# Occurrences: Lines 38-41 (2 instances)

def visit_Name(self, node):
  return node.id


# ==================================================
# Line: 120

def transform_ast(self, node, ctx):
  gen = OpRegGenImpl(ctx)
  gen.visit(node)
  return gen.code_buffer



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/dtensor/python/dtensor_device.py
# Line: 86

def _create_host_array(self, shape, host_id):
  """Returns ID and device lists that can be used to create a host mesh."""
  num_global_devices = np.prod(shape)
  global_device_ids = np.arange(num_global_devices).reshape(shape)
  local_device_list = [
      tf_device.DeviceSpec(
          job=config.full_job_name(), device_type="CPU", device_index=0)
  ]
  num_local_devices = len(local_device_list)
  local_device_ids = [
      x + host_id * num_local_devices for x in range(num_local_devices)
  ]
  return global_device_ids, local_device_ids, local_device_list


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/dtensor/python/input_util.py
# Line: 190

def _to_components(self, value):
  return (value._iterator_resource_dtensor,)  # pylint: disable=protected-access


# ==================================================
# Line: 621

def _repeat_batch(self, dataset, repeats):
  if repeats == 1:
    # Remove this shortcut if tf.data can optimize this away.
    return dataset

  def repeat(*x):
    return dataset_ops.DatasetV2.from_tensors(x).repeat(repeats)

  return dataset.flat_map(repeat)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/type_spec_test.py
# Line: 73

def _to_components(self, value):
  return (value.x, value.y)


# ==================================================
# Line: 139

def _to_components(self, value):
  return (value.x, value.y)


# ==================================================
# Line: 186

def _to_components(self, value):
  return nest.flatten(value)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
# Occurrences: Lines 50-54 (2 instances)

def makeTensorConverter(self):
  """Returns a new PythonTensorConverter with the current context."""
  return PythonTensorConverter(context.context())


# ==================================================
# Line: 60

def makeApiInfoFromParamSpecs(self,
                              api_name,
                              param_names,
                              input_specs,
                              attr_specs,
                              defaults=()):
  """Returns a PythonAPIParameterConverter built from the given specs."""
  api_info = _pywrap_python_api_info.PythonAPIInfo(api_name)
  api_info.InitializeFromParamSpecs(input_specs, attr_specs, param_names,
                                    defaults)
  return api_info


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/node_file_writer_test.py
# Line: 110

def _get_input_shapes(self, node_def):
  input_shapes = []
  for shape_attr in node_def.attr['_input_shapes'].list.shape:
    shape = tuple(a.size for a in shape_attr.dim)
    input_shapes.append(shape)
  return input_shapes


# ==================================================
# Line: 117

def _get_input_dtypes(self, node_def):
  input_dtypes = []
  for dtype_attr in node_def.attr['_input_dtypes'].list.type:
    input_dtypes.append(dtypes.as_dtype(dtype_attr))
  return input_dtypes


# ==================================================
# Line: 123

def _get_input_tensor(self, node_def, input_index):
  tensor_proto = node_def.attr.get(f'_input_tensor_{input_index}')
  if tensor_proto is None:
    return None
  return tensor_util.MakeNdarray(tensor_proto.tensor)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor.py
# Line: 302

def _disallow(self, task):
  raise errors.OperatorNotAllowedInGraphError(
      f"{task} is not allowed."
      " You can attempt the following resolutions to the problem:"
      " If you are running in Graph mode, use Eager execution mode"
      " or decorate this function with @tf.function."
      " If you are using AutoGraph, you can try decorating this function"
      " with @tf.function. If that does not work, then you may be using"
      " an unsupported feature or your source code may not be visible"
      " to AutoGraph. See"
      " https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/autograph/g3doc/reference/limitations.md#access-to-source-code"
      " for more information.")


# ==================================================
# Occurrences: Lines 1167-1171 (2 instances)

def _to_components(self, value):
  assert isinstance(value, core_tf_types.Tensor)
  return value


# ==================================================
# Occurrences: Lines 1227-1232 (2 instances)

def can_encode(self, pyobj):
  # BoundedTensorSpec has its own decoder.
  return (isinstance(pyobj, TensorSpec) and
          not isinstance(pyobj, BoundedTensorSpec))


# ==================================================
# Occurrences: Lines 1241-1244 (2 instances)

def can_decode(self, value):
  return value.HasField("tensor_spec_value")


# ==================================================
# Occurrences: Lines 1420-1423 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, BoundedTensorSpec)


# ==================================================
# Occurrences: Lines 1437-1440 (2 instances)

def can_decode(self, value):
  return value.HasField("bounded_tensor_spec_value")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
# Line: 167

def _freezeModel(self, func):
  """Freezes the function.

  Args:
    func: Function.

  Returns:
    root: AutoTrackable object with original ConcreteFunction.
    output_func: frozen ConcreteFunction.
  """
  root = autotrackable.AutoTrackable()
  root.f = func
  input_func = root.f.get_concrete_function()

  output_func = convert_to_constants.convert_variables_to_constants_v2(
      input_func, lower_control_flow=False)
  return root, output_func


# ==================================================
# Line: 536

def _freezeModel(self, func):
  """Freezes the function.

  Args:
    func: Function.

  Returns:
    root: AutoTrackable object with original ConcreteFunction.
    output_func: frozen ConcreteFunction.
  """
  root = autotrackable.AutoTrackable()
  root.f = func
  input_func = root.f.get_concrete_function()

  output_func = convert_to_constants.convert_var_to_const_function_in_v1(
      input_func, lower_control_flow=False)
  return root, output_func


# ==================================================
# Line: 1035

def _inline_functions(self, graph_def, arrays):
  meta_graph = export_meta_graph(graph_def=graph_def)
  fetch_collection = meta_graph_pb2.CollectionDef()
  for name in arrays:
    fetch_collection.node_list.value.append(name)
  meta_graph.collection_def["train_op"].CopyFrom(fetch_collection)

  # Initialize RewriterConfig with everything disabled except function
  # inlining.
  config = config_pb2.ConfigProto()
  rewrite_options = config.graph_options.rewrite_options
  rewrite_options.optimizers.append("function")
  return tf_optimizer.OptimizeGraph(config, meta_graph)


# ==================================================
# Line: 1572

def _addNoinlineAttributeToFunction(self, saved_model_dir, func_name):
  saved_model_proto = loader_impl.parse_saved_model(saved_model_dir)
  new_saved_model = saved_model_pb2.SavedModel()
  new_saved_model.CopyFrom(saved_model_proto)
  new_meta_graph_def = new_saved_model.meta_graphs[0]
  prefix_len = len("__inference_")
  for func_def in new_meta_graph_def.graph_def.library.function:
    func_name_without_prefix = func_def.signature.name[prefix_len:]
    if func_name_without_prefix.startswith(func_name):
      func_def.attr["_noinline"].CopyFrom(attr_value_pb2.AttrValue(b=True))
  old_saved_model_file = os.path.join(saved_model_dir,
                                      constants.SAVED_MODEL_FILENAME_PB)
  if os.path.exists(old_saved_model_file):
    os.remove(old_saved_model_file)
  path = os.path.join(
      compat.as_bytes(saved_model_dir),
      compat.as_bytes(constants.SAVED_MODEL_FILENAME_PB))
  file_io.write_string_to_file(
      path, new_saved_model.SerializeToString(deterministic=True))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_shape_test.py
# Line: 360

def testConcatenate(self, concatenate_fn):
  tensor_shape.TensorShape([1, 2, 3, 4]).assert_is_compatible_with(
      concatenate_fn(
          tensor_shape.TensorShape([1, 2]), tensor_shape.TensorShape([3, 4])))
  tensor_shape.TensorShape([1, 2, 3, 4]).assert_is_compatible_with(
      concatenate_fn(
          tensor_shape.TensorShape([1, 2]), tensor_shape.TensorShape(None)))
  tensor_shape.TensorShape([1, 2, 3, 4]).assert_is_compatible_with(
      concatenate_fn(
          tensor_shape.TensorShape(None), tensor_shape.TensorShape([3, 4])))
  tensor_shape.TensorShape([1, 2, 3, 4]).assert_is_compatible_with(
      concatenate_fn(
          tensor_shape.TensorShape(None), tensor_shape.TensorShape(None)))


# ==================================================
# Line: 377

def testConcatenateWithDimension(self, concatenate_fn):
  tensor_shape.TensorShape([1, 2, 3]).assert_is_compatible_with(
      concatenate_fn(
          tensor_shape.TensorShape([1, 2]), tensor_shape.Dimension(3)))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/meta_graph_test.py
# Line: 702

def _testScopedExportWithQueue(self, test_dir, exported_filename):
  graph = ops.Graph()
  with graph.as_default():
    with ops.name_scope("queue1"):
      input_queue = data_flow_ops.FIFOQueue(10, dtypes.float32)
      enqueue = input_queue.enqueue((9876), name="enqueue")
      close = input_queue.close(name="close")
      qr = queue_runner_impl.QueueRunner(input_queue, [enqueue], close)
      queue_runner_impl.add_queue_runner(qr)
      input_queue.dequeue(name="dequeue")

    orig_meta_graph, _ = meta_graph.export_scoped_meta_graph(
        filename=os.path.join(test_dir, exported_filename),
        graph=ops.get_default_graph(),
        export_scope="queue1")

  return orig_meta_graph


# ==================================================
# Line: 720

def _testScopedImportWithQueue(self, test_dir, exported_filename,
                               new_exported_filename):
  graph = ops.Graph()
  meta_graph.import_scoped_meta_graph(
      os.path.join(test_dir, exported_filename),
      graph=graph,
      import_scope="new_queue1")
  graph.as_graph_element("new_queue1/dequeue:0")
  graph.as_graph_element("new_queue1/close")
  with graph.as_default():
    new_meta_graph, _ = meta_graph.export_scoped_meta_graph(
        filename=os.path.join(test_dir, new_exported_filename),
        graph=graph,
        export_scope="new_queue1")

  return new_meta_graph


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/extension_type.py
# Line: 587

def can_encode(self, pyobj):
  """Returns true if `pyobj` can be encoded as an ExtensionTypeSpec."""
  if isinstance(pyobj, ExtensionTypeSpec):
    try:
      type_spec_registry.get_name(type(pyobj))
      return True
    except ValueError:
      return False
  return False


# ==================================================
# Line: 597

def do_encode(self, extension_type_spec_value, encode_fn):
  """Returns an encoded proto for the given `tf.ExtensionTypeSpec`."""
  type_spec_class_name = type_spec_registry.get_name(
      type(extension_type_spec_value)
  )

  type_state = extension_type_spec_value._serialize()  # pylint: disable=protected-access
  num_flat_components = len(
      nest.flatten(
          extension_type_spec_value._component_specs, expand_composites=True  # pylint: disable=protected-access
      )
  )
  encoded_type_spec = struct_pb2.StructuredValue()
  encoded_type_spec.type_spec_value.CopyFrom(
      struct_pb2.TypeSpecProto(
          type_spec_class=struct_pb2.TypeSpecProto.EXTENSION_TYPE_SPEC,
          type_state=encode_fn(type_state),
          type_spec_class_name=type_spec_class_name,
          num_flat_components=num_flat_components,
      )
  )
  return encoded_type_spec


# ==================================================
# Line: 620

def can_decode(self, value):
  """Returns true if `value` can be decoded into a `tf.ExtensionTypeSpec`."""
  if value.HasField('type_spec_value'):
    type_spec_class_enum = value.type_spec_value.type_spec_class
    return (
        type_spec_class_enum == struct_pb2.TypeSpecProto.EXTENSION_TYPE_SPEC
    )
  return False


# ==================================================
# Line: 629

def do_decode(self, value, decode_fn):
  """Returns the `tf.TypeSpec` encoded by the proto `value`."""
  type_spec_proto = value.type_spec_value
  class_name = type_spec_proto.type_spec_class_name

  try:
    type_spec_class = type_spec_registry.lookup(class_name)
  except ValueError:
    type_spec_class = AnonymousExtensionTypeSpec
    warnings.warn(
        f"The type '{class_name}' has not been registered. "
        'Falling back to using AnonymousExtensionTypeSpec '
        'instead.'
    )

  # pylint: disable=protected-access
  return type_spec_class._deserialize(decode_fn(type_spec_proto.type_state))



# ==================================================
# Line: 686

def batch(self, spec, batch_size):
  """Returns the TypeSpec representing a batch of values described by `spec`.

  The default definition returns a `TypeSpec` that is equal to `spec`, except
  that an outer axis with size `batch_size` is added to every nested
  `TypeSpec` and `TensorShape` field.  Subclasses may override this default
  definition, when necessary.

  Args:
    spec: The `TypeSpec` for an individual value.
    batch_size: An `int` indicating the number of values that are batched
      together, or `None` if the batch size is not known.

  Returns:
    A `TypeSpec` for a batch of values.
  """

  def batch_field(f):
    if isinstance(f, type_spec.BatchableTypeSpec):
      return f.__batch_encoder__.batch(f, batch_size)
    elif isinstance(f, tensor_shape.TensorShape):
      return [batch_size] + f
    else:
      return f

  fields = tuple(spec.__dict__.items())
  batched_fields = nest.map_structure(batch_field, fields)
  return _create_object_from_type_and_dict(type(spec), batched_fields)


# ==================================================
# Line: 715

def unbatch(self, spec):
  """Returns the TypeSpec for a single unbatched element in `spec`.

  The default definition returns a `TypeSpec` that is equal to `spec`, except
  that the outermost axis is removed from every nested `TypeSpec`, and
  `TensorShape` field.  Subclasses may override this default definition, when
  necessary.

  Args:
    spec: The `TypeSpec` for a batch of values.

  Returns:
    A `TypeSpec` for an individual value.
  """

  def unbatch_field(f):
    if isinstance(f, type_spec.BatchableTypeSpec):
      return f.__batch_encoder__.unbatch(f)
    elif isinstance(f, tensor_shape.TensorShape):
      return f[1:]
    else:
      return f

  fields = tuple(spec.__dict__.items())
  unbatched_fields = nest.map_structure(unbatch_field, fields)
  return _create_object_from_type_and_dict(type(spec), unbatched_fields)


# ==================================================
# Line: 742

def encode(self, spec, value, minimum_rank=0):
  """Encodes `value` as a nest of batchable Tensors or CompositeTensors.

  The default definition returns a flat tuple of all the `Tensor`s,
  `CompositeTensor`s, and `ExtensionType`s from a depth-first traversal of
  `value`'s fields. Subclasses may override this default definition, when
  necessary.

  Args:
    spec: The TypeSpec of the value to encode.
    value: A value compatible with `spec`.
    minimum_rank: The minimum rank for the returned Tensors, CompositeTensors,
      and ExtensionType values.  This can be used to ensure that the encoded
      values can be unbatched this number of times.   If `minimum_rank>0`,
      then `t.shape[:minimum_rank]` must be compatible for all values `t`
      returned by `encode`.

  Returns:
    A nest (as defined by `tf.nest`) of `tf.Tensor`s, batchable
    `tf.CompositeTensor`s, or `tf.ExtensionType`s.  Stacking, unstacking, or
    concatenating these encoded values and then decoding the result must be
    equivalent to stacking, unstacking, or concatenating the original values.
  """
  return spec._to_components(value)  # pylint: disable=protected-access


# ==================================================
# Line: 767

def decode(self, spec, encoded_value):
  """Decodes `value` from a batchable tensor encoding.

  See `encode` for a description of the default encoding.  Subclasses may
  override this default definition, when necessary.

  Args:
    spec: The TypeSpec for the result value.  If encoded values with spec `s`
      were batched, then `spec` should be `s.batch(batch_size)`; or if encoded
      values with spec `s` were unbatched, then `spec` should be
      `s.unbatch()`.
    encoded_value: A nest of values returned by `encode`; or a nest of values
      that was formed by stacking, unstacking, or concatenating the
      corresponding elements of values returned by `encode`.

  Returns:
    A value compatible with `type_spec`.
  """
  return spec._from_components(encoded_value)  # pylint: disable=protected-access


# ==================================================
# Line: 787

def encoding_specs(self, spec):
  """Returns a list of `TensorSpec`(s) describing the encoding for `spec`.

  See `encode` for a description of the default encoding.  Subclasses may
  override this default definition, when necessary.

  Args:
    spec: The TypeSpec whose encoding should be described.

  Returns:
    A nest (as defined by `tf.nest) of `tf.TypeSpec`, describing the values
    that are returned by `self.encode(spec, ...)`.  All TypeSpecs in this
    nest must be batchable.
  """
  return spec._component_specs  # pylint: disable=protected-access



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/combinations.py
# Line: 37

def context_managers(self, kwargs):
  mode = kwargs.pop("mode", None)
  if mode is None:
    return []
  elif mode == "eager":
    return [context.eager_mode()]
  elif mode == "graph":
    return [ops.Graph().as_default(), context.graph_mode()]
  else:
    raise ValueError(
        "Argument 'mode' must be either 'eager' or 'graph'. "
        f"Received: {mode}.")


# ==================================================
# Line: 50

def parameter_modifiers(self):
  return [test_combinations.OptionalParameter("mode")]



# ==================================================
# Line: 64

def should_execute_combination(self, kwargs):
  tf_api_version = kwargs.pop("tf_api_version", None)
  if tf_api_version == 1 and tf2.enabled():
    return (False, "Skipping a TF1.x test when TF2 is enabled.")
  elif tf_api_version == 2 and not tf2.enabled():
    return (False, "Skipping a TF2 test when TF2 is not enabled.")
  return (True, None)


# ==================================================
# Line: 72

def parameter_modifiers(self):
  return [test_combinations.OptionalParameter("tf_api_version")]



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/weak_tensor.py
# Occurrences: Lines 44-47 (2 instances)

def get_gradient_components(self, weak_tensor):
  return weak_tensor.tensor


# ==================================================
# Line: 92

def _disallow(self, task):
  raise errors.OperatorNotAllowedInGraphError(
      f"{task} is not allowed. You can attempt the following resolutions to"
      " the problem: If you are running in Graph mode, use Eager execution"
      " mode or decorate this function with @tf.function. If you are using"
      " AutoGraph, you can try decorating this function with @tf.function."
      " If that does not work, then you may be using an unsupported feature"
      " or your source code may not be visible to AutoGraph. See"
      " https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/autograph/g3doc/reference/limitations.md#access-to-source-code"
      " for more information."
  )


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/function_test.py
# Line: 167

def testFunctionWithNoOutput(self):

  @function.Defun(dtypes.float32, dtypes.float32)
  def APlus2B(a, b):
    c = a + b * 2  # Create some ops to have nodes in the body
    print(c)  # Using 'print' to make lint happy

  with ops.Graph().as_default():
    # Call function. There should be no exceptions.
    APlus2B([1.0], [2.0])


# ==================================================
# Line: 1172

def stripInternalFunctionDefAnnotations(self, f_def):
  result = function_pb2.FunctionDef()
  result.CopyFrom(f_def)
  result.attr.pop("_construction_context", None)
  return result


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/importer_test.py
# Line: 49

def _MakeGraphDef(self,
                  text,
                  producer=versions.GRAPH_DEF_VERSION,
                  min_consumer=versions.GRAPH_DEF_VERSION_MIN_CONSUMER):
  text = "versions: { producer: %d min_consumer: %d };\n%s" % (producer,
                                                               min_consumer,
                                                               text)
  ret = graph_pb2.GraphDef()
  text_format.Merge(text, ret)
  return ret


# ==================================================
# Line: 372

def testResources(self):
  # Produce GraphDef containing a ops producing and consuming resources.
  graph = ops.Graph()
  with graph.as_default():
    var = resource_variable_ops.ResourceVariable(1.0)
    var_assign = var.assign(2.0)
    # Use an op that requires handle shape to be set.
    var_shape = resource_variable_ops.variable_shape(var.handle)
    init = variables.global_variables_initializer()
  graph_def = graph.as_graph_def()

  # Import the GraphDef.
  with ops.Graph().as_default():
    # pylint: disable=unused-variable
    imported_var, imported_assign, imported_shape, imported_init = (
        importer.import_graph_def(
            graph_def,
            return_elements=[var.name, var_assign.name, var_shape.name,
                             init.name]))

    # Make sure the handle shape is set on the imported variable.
    new_var_shape = resource_variable_ops.variable_shape(imported_var)
    # pylint: enable=unused-variable

    # Run the imported graph.
    # TODO(b/76173421): make this work (currently DCHECKS)
    # with self.cached_session() as sess:
    #   self.evaluate(imported_init)
    #   self.assertEqual(self.evaluate(imported_var), 1.0)
    #   self.assertEqual(self.evaluate(imported_assign), 2.0)
    #   self.assertEqual(list(self.evaluate(imported_shape)), [])
    #   self.assertEqual(list(self.evaluate(new_var_shape)), [])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/convert_to_constants.py
# Line: 836

def _eval(self, tensor):
  """Returns the value in the tensor. Must be implemented in sub-classes."""
  raise errors.UnimplementedError(
      "The evaluation method should be implemented in sub-classes.")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/op_def_library_test.py
# Line: 38

def Tensor(self, t, name="in"):
  return op_def_library.apply_op("OutT", T=t, name=name)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/test_util_test.py
# Line: 159

def testIsGoogleCudaEnabled(self):
  # The test doesn't assert anything. It ensures the py wrapper
  # function is generated correctly.
  if test_util.IsGoogleCudaEnabled():
    print("GoogleCuda is enabled")
  else:
    print("GoogleCuda is disabled")


# ==================================================
# Line: 167

def testIsMklEnabled(self):
  # This test doesn't assert anything.
  # It ensures the py wrapper function is generated correctly.
  if test_util.IsMklEnabled():
    print("MKL is enabled")
  else:
    print("MKL is disabled")


# ==================================================
# Line: 1017

def testBody(self):
  modes.append("run_" + mode_name())


# ==================================================
# Line: 1047

def runTest(self):
  del self


# ==================================================
# Line: 1158

def test_no_variable_sharing(self):
  variable_scope.get_variable(
      name="step_size",
      initializer=np.array(1e-5, np.float32),
      use_resource=True,
      trainable=False)



# ==================================================
# Line: 1182

def test_has_no_leak(self):
  constant_op.constant([3.], name="no-leak")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/errors_test.py
# Line: 33

def _CountReferences(self, typeof):
  """Count number of references to objects of type |typeof|."""
  objs = gc.get_objects()
  ref_count = 0
  for o in objs:
    try:
      if isinstance(o, typeof):
        ref_count += 1
    # Certain versions of python keeps a weakref to deleted objects.
    except ReferenceError:
      pass
  return ref_count


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_util_test.py
# Line: 778

def __array__(self, dtype=None):
  del dtype
  return np.array([b"foo", b"bar", b"baz"])


# ==================================================
# Line: 1442

def disableSetStaticShape(self):
  flag_old = shape_util._ENABLE_MAYBE_SET_STATIC_SHAPE
  shape_util._ENABLE_MAYBE_SET_STATIC_SHAPE = False
  try:
    yield
  finally:
    shape_util._ENABLE_MAYBE_SET_STATIC_SHAPE = flag_old


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
# Line: 40

def makePythonTensorConverter(self):
  return _pywrap_python_tensor_converter.PythonTensorConverter(
      context.context())


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/subscribe.py
# Line: 72

def calc_control_outputs(self, graph):
  """Returns the map of control_outputs for a given graph.

  Args:
    graph: The graph to parse.

  Returns:
    A map of the control outputs.
  """
  control_outputs = {}
  for op in graph.get_operations():
    for control_input in op.control_inputs:
      if control_input not in control_outputs:
        control_outputs[control_input] = set()
      control_outputs[control_input].add(op)
  return control_outputs


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/tensor_shape.py
# Line: 536

def __rdiv__(self, other):
  """Use `__floordiv__` via `x // y` instead.

  This function exists only to have a better error message. Instead of:
  `TypeError: unsupported operand type(s) for /: 'int' and 'Dimension'`,
  this function will explicitly call for usage of `//` instead.

  Args:
    other: Another `Dimension`.

  Raises:
    TypeError.
  """
  raise TypeError("unsupported operand type(s) for /: '{}' and 'Dimension', "
                  "please use // instead".format(type(other).__name__))


# ==================================================
# Occurrences: Lines 1524-1527 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, TensorShape)


# ==================================================
# Occurrences: Lines 1534-1537 (2 instances)

def can_decode(self, value):
  return value.HasField("tensor_shape_value")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/test_util.py
# Line: 3166

def _NDArrayNear(self, ndarray1, ndarray2, err):
  return np.linalg.norm(ndarray1 - ndarray2) < err


# ==================================================
# Line: 3581

def _format_subscripts(self, subscripts, value, limit=10, indent=2):
  """Generate a summary of ndarray subscripts as a list of str.

  If limit == N, this method will print up to the first N subscripts on
  separate
  lines. A line of ellipses (...) will be appended at the end if the number of
  subscripts exceeds N.

  Args:
    subscripts: The tensor (np.ndarray) subscripts, of the same format as
      np_where()'s return value, i.e., a tuple of arrays with each array
      corresponding to a dimension. E.g., (array([1, 1]), array([0, 1])).
    value: (np.ndarray) value of the tensor.
    limit: (int) The maximum number of indices to print.
    indent: (int) Number of characters to indent at the beginning of each
      line.

  Returns:
    (list of str) the multi-line representation of the subscripts and values,
      potentially with omission at the end.
  """
  lines = []
  subscripts = np.transpose(subscripts)
  prefix = " " * indent
  if np.ndim(value) == 0:
    return [prefix + "[0] : " + str(value)]
  for subscript in itertools.islice(subscripts, limit):
    lines.append(prefix + str(subscript) + " : " +
                 str(value[tuple(subscript)]))
  if len(subscripts) > limit:
    lines.append(prefix + "...")
  return lines


# ==================================================
# Line: 3895

def _constrain_devices_and_set_default(
    self, sess: s.Session, use_gpu: bool, force_gpu: bool,

# ==================================================
# Line: 3917

def _create_session(
    self,
    graph: Optional[ops.Graph],
    config: Optional[config_pb2.ConfigProto],
    force_gpu: bool,

# ==================================================
# Line: 4158

def gradient(self, y, x, grad_ys=None):
  result = gradients_impl.gradients(y, x, grad_ys)

  # Unlike `tape.gradient()`, `tf.gradients()` returns a list for a single
  # element. So unpack if needed to match `tape.gradient()` behavior.
  if not isinstance(x, (list, tuple)):
    assert len(result) == 1
    return result[0]

  return result


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/extension_type_field_test.py
# Line: 169

def testValidPytype(self, tp, allow_forward_references=False):
  extension_type_field.validate_field_value_type(
      tp, allow_forward_references=allow_forward_references)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/sparse_tensor.py
# Line: 419

def _to_components(self, value):
  if isinstance(value, SparseTensorValue):
    value = SparseTensor.from_value(value)
  return [value.indices, value.values, value.dense_shape]


# ==================================================
# Line: 446

def _to_tensor_list(self, value):
  value = SparseTensor.from_value(value)
  return [gen_sparse_ops.serialize_sparse(
      value.indices, value.values, value.dense_shape,
      out_type=dtypes.variant)]


# ==================================================
# Line: 501

def _to_legacy_output_classes(self):
  return SparseTensor


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/memory_checker_test.py
# Line: 26

def testNoLeakEmpty(self):
  with MemoryChecker() as memory_checker:
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()

  memory_checker.report()
  memory_checker.assert_no_leak_if_all_possibly_except_one()


# ==================================================
# Line: 36

def testNoLeak1(self):
  with MemoryChecker() as memory_checker:
    memory_checker.record_snapshot()
    x = constant_op.constant(1)  # pylint: disable=unused-variable
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()

  memory_checker.report()
  memory_checker.assert_no_leak_if_all_possibly_except_one()


# ==================================================
# Line: 47

def testNoLeak3(self):
  with MemoryChecker() as memory_checker:
    tensors = []
    for i in range(10):
      if i not in (5, 7):
        tensors.append(constant_op.constant(1))
      memory_checker.record_snapshot()

  memory_checker.report()
  memory_checker.assert_no_leak_if_all_possibly_except_one()


# ==================================================
# Line: 82

def testNoNewPythonObjectsEmpty(self):
  with MemoryChecker() as memory_checker:
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()

  memory_checker.assert_no_new_python_objects()


# ==================================================
# Line: 101

  def testNewPythonObjectBelowThreshold(self):

    class Foo(object):
      pass

    with MemoryChecker() as memory_checker:
      memory_checker.record_snapshot()
      foo = Foo()
      del foo
      memory_checker.record_snapshot()

    memory_checker.assert_no_new_python_objects()


if __name__ == '__main__':

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/extension_type_test.py
# Line: 921

def testCantUseReservedName(self):
  with self.assertRaisesRegex(
      ValueError,
      'The field annotations for MyType1 are invalid. '
      "Field '_to_components' is reserved",
  ):

    class MyType1(extension_type.ExtensionType):  # pylint: disable=unused-variable
      _to_components: int

  with self.assertRaisesRegex(
      ValueError,
      'The field annotations for MyType2 are invalid. '
      "Field '_tf_extension_type_foo' is reserved",
  ):

    class MyType2(extension_type.ExtensionType):  # pylint: disable=unused-variable
      _tf_extension_type_foo: int

  with self.assertRaisesRegex(
      ValueError,
      'The field annotations for MyType3 are invalid. '
      "Field 'is_compatible_with' is reserved",
  ):

    class MyType3(extension_type.ExtensionType):  # pylint: disable=unused-variable

      def is_compatible_with(self, other):
        return False


# ==================================================
# Line: 948

def is_compatible_with(self, other):
  return False


# ==================================================
# Line: 969

  def f(self, s):
    return s.x[0] + s.x[1] + s.y

s1 = self.ExtensionTypeWithName((1, 2), 3)
s2 = self.ExtensionTypeWithName((1.0, 2), [3.0, 4.0])


# ==================================================
# Line: 1355

def testConstruction(self, fields):
  if callable(fields):
    fields = fields()
  extension_type.AnonymousExtensionType(**fields)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/experimental/graph_building_test.py
# Line: 35

def _computeAddOpDuration(self, num_ops, num_iters):
  def add_op_to_graph(num_ops):
    with func_graph.FuncGraph("add").as_default():
      a = gen_array_ops.placeholder(dtypes.float32)
      b = gen_array_ops.placeholder(dtypes.float32)
      for _ in range(num_ops):
        gen_math_ops.add(a, b)

  runtimes = timeit.repeat(
      lambda: add_op_to_graph(num_ops), repeat=10, number=num_iters)
  return min(runtimes) / num_iters


# ==================================================
# Line: 47

def _computeReadVariableOpDuration(self, num_ops, num_iters):
  def add_op_to_graph(num_ops):
    with func_graph.FuncGraph("resource").as_default():
      handle = resource_variable_ops.var_handle_op(
          dtype=dtypes.int32, shape=[])
      resource_variable_ops.assign_variable_op(
          handle, constant_op.constant(1, dtype=dtypes.int32))
      for _ in range(num_ops):
        gen_resource_variable_ops.read_variable_op(handle, dtype=dtypes.int32)

  runtimes = timeit.repeat(
      lambda: add_op_to_graph(num_ops), repeat=10, number=num_iters)
  return min(runtimes) / num_iters


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
# Line: 401

def _computeMnistMlpGrads(self, math_ops_lib, nn_ops_lib, backprop_lib, cast,
                          num_iters, hidden_layers, hidden_size, batch_size):
  batch_size = 1
  image_size = 28 * 28
  num_classes = 10

  def model(x, hidden_weights, softmax_weight, labels):
    with backprop_lib.GradientTape() as tape:
      for weight in hidden_weights + [softmax_weight]:
        tape.watch(weight)
      for hidden_weight in hidden_weights:
        x = math_ops_lib.mat_mul(x, hidden_weight)
        x = nn_ops_lib.relu(x)
      logits = math_ops_lib.mat_mul(x, softmax_weight)
      loss = nn_ops_lib.sparse_softmax_cross_entropy_with_logits(
          logits=logits, labels=labels)

    grads = tape.gradient(loss, hidden_weights + [softmax_weight])
    return grads

  x = maybe_cast(array_ops.ones([batch_size, image_size]), cast)
  hidden_weights = []
  for i in range(hidden_layers):
    hidden_weights.append(
        maybe_cast(
            random_ops.random_uniform(
                [hidden_size if i else image_size, hidden_size]), cast))
  softmax_weight = maybe_cast(
      random_ops.random_uniform([hidden_size, num_classes]), cast)
  labels = maybe_cast(array_ops.zeros([batch_size], dtype=dtypes.int32), cast)

  with context_lib.set_default(get_immediate_execution_context()):
    # Warm up.
    for _ in range(10):
      model(x, hidden_weights, softmax_weight, labels)
    runtimes = timeit.repeat(
        lambda: model(x, hidden_weights, softmax_weight, labels),
        repeat=num_iters,
        number=10)
  return min(runtimes) / 10


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/python_op_gen_annotation_test.py
# Line: 26

def test_type_annotation_not_empty_for_internal_op(self):
  for internal_op in [
      data_flow_ops.dynamic_stitch,
      gen_nn_ops._fused_batch_norm,
      gen_math_ops.add,
  ]:
    sig = inspect.signature(internal_op)
    for key in sig.parameters:
      if key == "name":
        continue
      assert sig.parameters[key].annotation != inspect.Signature.empty


# ==================================================
# Line: 38

  def test_type_annotation_empty_for_imported_op(self):
    for imported_op in [
        data_flow_ops.DynamicStitch,
        gen_nn_ops.FusedBatchNorm,
        gen_math_ops.Add,
    ]:
      sig = inspect.signature(imported_op)
      for key in sig.parameters:
        if key == "name":
          continue
        assert sig.parameters[key].annotation == inspect.Signature.empty


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/composite_tensor_test.py
# Line: 212

def testNestAssertSameStructure(self, s1, s2, expand_composites=True):
  nest.assert_same_structure(s1, s2, expand_composites=expand_composites)
  nest.assert_shallow_structure(s1, s2, expand_composites=expand_composites)


# ==================================================
# Line: 249

def testNestAssertShallowStructure(self, s1, s2, expand_composites=True):
  nest.assert_shallow_structure(s1, s2, expand_composites=expand_composites)


# ==================================================
# Line: 413

def testAssertSameStructureWithValueAndTypeSpec(self, value_func):
  value = value_func()
  spec = nest.map_structure(type_spec.type_spec_from_value, value,
                            expand_composites=False)
  nest.assert_same_structure(value, spec, expand_composites=True)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/graph_util_test.py
# Line: 195

def create_node_def(self, op, name, inputs):
  new_node = node_def_pb2.NodeDef()
  new_node.op = op
  new_node.name = name
  new_node.input.extend(inputs)
  return new_node


# ==================================================
# Occurrences: Lines 213-217 (2 instances)

def set_attr_dtype(self, node, key, value):
  node.attr[key].CopyFrom(
      attr_value_pb2.AttrValue(type=value.as_datatype_enum))


# ==================================================
# Line: 224

def set_attr_tensor(self, node, key, value, dtype, shape=None):
  node.attr[key].CopyFrom(
      attr_value_pb2.AttrValue(
          tensor=tensor_util.make_tensor_proto(
              value, dtype=dtype, shape=shape)))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/constant_op.py
# Occurrences: Lines 397-400 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, tensor_lib.Tensor)


# ==================================================
# Occurrences: Lines 418-421 (2 instances)

def can_decode(self, value):
  return value.HasField("tensor_value")


# ==================================================
# Occurrences: Lines 435-438 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, np.ndarray)


# ==================================================
# Occurrences: Lines 447-450 (2 instances)

def can_decode(self, value):
  return value.HasField("numpy_value")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/ops_test.py
# Line: 920

  def __tf_tensor__(self, dtype=None, name=None):
    return constant_op.constant((1, 2, 3), dtype=dtype, name=name)

tc = TensorCompatible()


# ==================================================
# Line: 1548

def testBackslashAndDashRegex(self):
  # GitHub issue 39019, all should pass
  g = ops.Graph()
  with g.name_scope("n_CatCntc-campaign\\c_campaign"):
    pass
  with g.name_scope("foo"):
    with g.name_scope("n_CatCntc-campaign\\c_campaign"):
      pass
  with g.name_scope("n_CatCntc-campaign\\c_campaign"):
    with g.name_scope("foo"):
      pass


# ==================================================
# Line: 1920

def _overwritingDeviceFunction(self, unused_op):
  # This device function unconditionally overwrites the device of ops.
  #
  # NOTE(mrry): Writing device functions like this is not
  # recommended. Instead, in most cases you should use
  # `pydev.merge_device("/job:ps")` or simply `"/job:ps"` as the
  # argument to `tf.device()` and the device component will be merged in.
  return "/job:overwrite"


# ==================================================
# Line: 2394

def _as_graph_element(self):
  return a


# ==================================================
# Line: 3012

def _as_graph_element(self):
  return "FloatOutput:0"


# ==================================================
# Line: 3072

def _get_test_attrs(self):
  x = gen_control_flow_ops.no_op()
  try:
    a = compat.as_text(x.get_attr("_A"))
  except ValueError:
    a = None
  try:
    b = compat.as_text(x.get_attr("_B"))
  except ValueError:
    b = None
  return (a, b)


# ==================================================
# Line: 3438

def testColocateWithVariableInFunction(self):
  v = variables.Variable(1.)

  @def_function.function
  def f():
    with ops.colocate_with(v):
      return array_ops.ones([], name="output")

  f()
  graph_def = f.get_concrete_function().graph.as_graph_def()
  wrap_function.function_from_graph_def(graph_def, [], ["output"])



# ==================================================
# Line: 3479

def _error(self):
  return ((r"Op Old is not available in GraphDef version %d\. "
           r"It has been removed in version 8\. For reasons\.") %
          versions.GRAPH_DEF_VERSION)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/flexible_dtypes_test.py
# Line: 773

def testResultTypeSafeModeAllowedPromo(self, a_dtype, b_dtype):
  with DtypeConversionTestEnv('safe'):
    # Create Tensor of input dtypes.
    input_a = (
        constant_op.constant(1, dtype=a_dtype[0])
        if a_dtype[0] != dtypes.bool
        else constant_op.constant(True)
    )
    input_b = (
        constant_op.constant(2, dtype=b_dtype[0])
        if b_dtype[0] != dtypes.bool
        else constant_op.constant(False)
    )
    # Create WeakTensors if weak = True.
    if a_dtype[1]:
      input_a = weak_tensor.WeakTensor(input_a)
    if b_dtype[1]:
      input_b = weak_tensor.WeakTensor(input_b)
    flexible_dtypes.result_type(input_a, input_b)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/constant_op_test.py
# Line: 62

def _make_graph_def(self, text):
  ret = graph_pb2.GraphDef()
  text_format.Parse(text, ret)
  return ret


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
# Line: 36

def _build_function_def(self):
  with ops.Graph().as_default() as g:
    # Inputs
    x = array_ops.placeholder(dtypes.float32, name="x")
    y = array_ops.placeholder(dtypes.float32, name="y")

    # Outputs
    sum_squares = math_ops.add_n(
        [math_ops.pow(x, 2), math_ops.pow(y, 2)], name="sum_squares")
    sum_cubes = math_ops.add_n(
        [math_ops.pow(x, 3), math_ops.pow(y, 3)], name="sum_cubes")
  fdef = graph_to_function_def.graph_to_function_def(
      g,
      g.get_operations(),
      [x, y],  # Inputs
      [sum_squares, sum_cubes])  # Outputs.
  fdef.signature.name = "_whats_in_a_name"
  return fdef


# ==================================================
# Line: 193

def _build_function_def(self):
  with ops.Graph().as_default() as g:
    # Inputs:    x    y    z
    #            |\   |   /
    #            | \  |  /
    #            |  foo_1     list_output
    #            |   / \       /       \
    #            | d_1 e_1  a:1        a:0
    #            |  \   |   /           |
    #            |   \  |  /            |
    #            |    foo_2             |
    #            |     / \              |
    # Outputs:   x   d_2 e_2           a:0

    x = array_ops.placeholder(dtypes.float32, name="x")
    y = array_ops.placeholder(dtypes.int32, name="y")
    z = array_ops.placeholder(dtypes.int32, name="z")

    d_1, e_1 = op_def_library.apply_op("Foo1", name="foo_1", a=x, b=y, c=z)

    list_output0, list_output1 = test_ops.list_output(
        T=[dtypes.int32, dtypes.int32], name="list_output")

    d_2, e_2 = test_ops.foo1(a=d_1, b=e_1, c=list_output1, name="foo_2")

  fdef = graph_to_function_def.graph_to_function_def(
      g,
      g.get_operations(),
      [x, y, z],  # Inputs
      [x, d_2, e_2, list_output0])  # Outputs.

  # Assert that the FunctionDef was correctly built.
  assert len(fdef.node_def) == 3  # 2 Foo1 nodes and 1 ListOutput node.
  assert fdef.node_def[0].op == "Foo1"
  assert fdef.node_def[0].input == ["x", "y", "z"]
  assert fdef.node_def[1].op == "ListOutput"
  assert not fdef.node_def[1].input
  assert fdef.node_def[2].op == "Foo1"
  assert fdef.node_def[2].input == [
      "foo_1:d:0", "foo_1:e:0", "list_output:a:1"
  ]
  return fdef


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/test_combinations.py
# Line: 73

def should_execute_combination(self, kwargs):
  """Indicates whether the combination of test arguments should be executed.

  If the environment doesn't satisfy the dependencies of the test
  combination, then it can be skipped.

  Args:
    kwargs:  Arguments that are passed to the test combination.

  Returns:
    A tuple boolean and an optional string.  The boolean False indicates
  that the test should be skipped.  The string would indicate a textual
  description of the reason.  If the test is going to be executed, then
  this method returns `None` instead of the string.
  """
  del kwargs
  return (True, None)


# ==================================================
# Occurrences: Lines 91-95 (2 instances)

def parameter_modifiers(self):
  """Returns `ParameterModifier` instances that customize the arguments."""
  return []


# ==================================================
# Line: 148

def modified_arguments(self, kwargs, requested_parameters):
  """Replace user-provided arguments before they are passed to a test.

  This makes it possible to adjust user-provided arguments before passing
  them to the test method.

  Args:
    kwargs:  The combined arguments for the test.
    requested_parameters: The set of parameters that are defined in the
      signature of the test method.

  Returns:
    A dictionary with updates to `kwargs`.  Keys with values set to
    `ParameterModifier.DO_NOT_PASS_TO_THE_TEST` are going to be deleted and
    not passed to the test.
  """
  del kwargs, requested_parameters
  return {}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/function.py
# Line: 533

def _create_hash_str(self, input_arg, output_arg, node_def):
  """Creates an 8-character string unique to this input.

  Args:
    input_arg: the input_arg field of an OpDef
               (e.g. self._definition.signature.input_arg)
    output_arg: the output_arg field of an OpDef
               (e.g. self._definition.signature.output_arg)
    node_def: the node_def field of a FunctionDef
              (e.g. self._definition.node_def)

  Returns:
    The unique string for this input
  """
  hasher = hashlib.sha1()

  def update_num(n):
    hasher.update(compat.as_bytes("%x" % n))

  def update_str(s):
    update_num(len(s))
    hasher.update(compat.as_bytes(s))

  def update_strs(slist):
    update_num(len(slist))
    for s in slist:
      update_str(s)

  for adef in input_arg:
    update_str(adef.SerializeToString())

  for adef in output_arg:
    update_str(adef.SerializeToString())

  for n in sorted(node_def, key=lambda n: n.name):
    update_str(n.name)
    update_str(n.op)
    update_strs(n.input)
    update_num(len(n.attr))
    # NOTE: protobuf map serialization does not guarantee ordering.
    for k in sorted(n.attr):
      update_str(k)
      update_str(n.attr[k].SerializeToString())

  return hasher.hexdigest()[:8]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/python_api_info_test.py
# Line: 40

def makeConverterForGenOp(self, op_name):
  """Returns a PythonAPIInfo for the given gen_op."""
  api_info = _pywrap_python_api_info.PythonAPIInfo(op_name)
  api_info.InitializeFromRegisteredOp(op_name)
  return api_info


# ==================================================
# Line: 46

def makeConverterFromParamSpecs(self,
                                api_name,
                                param_names,
                                input_specs,
                                attr_specs,
                                defaults=()):
  """Returns a PythonAPIInfo built from the given specs."""
  api_info = _pywrap_python_api_info.PythonAPIInfo(api_name)
  api_info.InitializeFromParamSpecs(input_specs, attr_specs, param_names,
                                    defaults)
  return api_info


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
# Line: 309

def _supported_signatures(self):
  """Returns a tuple of supported signatures."""
  return TT_SUMMARY_SIGNATURES


# ==================================================
# Line: 339

def get_signature_to_agg_fn_map(self):
  """Returns a map that contains the aggregate function for each signature."""
  # TODO(b/199284834): Aggregations are not accurate for mean and sparsity if
  # cores have a different number of elements. Variance uses the maximal core
  # variance.
  return {TRACE_MODE_NORM: linalg_ops.norm,
          TRACE_MODE_HISTORY: math_ops.reduce_max,
          TRACE_MODE_MAX_ABS: math_ops.reduce_max,
          TRACE_MODE_NAN_INF: math_ops.reduce_max,
          TT_SUMMARY_NORM: linalg_ops.norm,
          TT_SUMMARY_MAX: math_ops.reduce_max,
          TT_SUMMARY_MAX_ABS:
              lambda t, axis=0: math_ops.reduce_max(math_ops.abs(t),  # pylint: disable=g-long-lambda
                                                    axis=axis),
          TT_SUMMARY_MIN: math_ops.reduce_min,
          # Exact if each part has the same number of values.
          TT_SUMMARY_SPARSITY: math_ops.reduce_mean,
          TT_SUMMARY_MEAN: math_ops.reduce_mean,
          TT_SUMMARY_VAR: math_ops.reduce_max,  # Simply reduce max variance.
          TT_SUMMARY_SIZE: math_ops.reduce_sum}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
# Line: 295

def report_proto_path(self, trace_dir, summary_tag_name):
  """Returns the path where report proto should be written.

  Args:
    trace_dir: String denoting the trace directory.
    summary_tag_name: Name of the unique tag that relates to
                      the report.
  Returns:
    A string denoting the path to the report proto.
  """
  filename = _TT_REPORT_PROTO + '.' + summary_tag_name.replace('/', '_')
  return os.path.join(trace_dir, filename)


# ==================================================
# Line: 308

def write_report_proto(self, report_path, report_proto, tt_parameters):
  """Writes the given report proto under trace_dir."""
  gfile.MakeDirs(tt_parameters.trace_dir)
  with gfile.GFile(report_path, 'wb') as f:
    f.write(report_proto.SerializeToString())


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_optimizer.py
# Line: 70

def _verify_and_get_subgroup_size(self, group_assignment, num_shards):
  """Verify group_assignment and get the subgroup size".

  Args:
    group_assignment: list of group ids for applying the optimizer
      to subgroups.
    num_shards: The number of TPU shards.

  Returns:
    The size of one subgroup in group_assignment.

  Raises:
    ValueError: If group_assignment is invalid.
  """
  if not group_assignment:
    return None
  if not (isinstance(group_assignment, list) and
          all(isinstance(i, list) for i in group_assignment)):
    raise ValueError(
        f"Argument `group_assignment` must be a list of lists. "
        f"Received: {group_assignment}")

  replica_ids = set()
  for g in group_assignment:
    for i in g:
      replica_ids.add(i)

  if set(range(num_shards)) != replica_ids:
    raise ValueError(
        f"Argument `group_assignment` must be a permutation of "
        f"range({num_shards}). Received: {group_assignment}")

  subgroup_size_list = [len(group) for group in group_assignment]
  if all(subgroup_size_list[0] == size for size in subgroup_size_list):
    return subgroup_size_list[0]
  else:
    raise ValueError("The size of each subgroup in `group_assignment` must "
                     f"be equal. Received: {group_assignment}")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3.py
# Line: 1218

def _raise_error_for_incorrect_control_flow_context(self):
  """Raises an error if we are not in the TPUReplicateContext."""
  # Do not allow any XLA control flow (i.e. control flow in between a
  # TPUStrategy's run call and the call to this function), as we can't
  # extract the enqueue from the head when in XLA control flow.
  graph = ops.get_default_graph()
  in_tpu_ctx = False
  while graph is not None:
    ctx = graph._get_control_flow_context()  # pylint: disable=protected-access
    while ctx is not None:
      if isinstance(ctx, tpu_replication.TPUReplicateContext):
        in_tpu_ctx = True
        break
      ctx = ctx.outer_context
    if in_tpu_ctx:
      break
    graph = getattr(graph, "outer_graph", None)
  if graph != ops.get_default_graph() and in_tpu_ctx:
    raise RuntimeError(
        "Current graph {} does not match graph which contains "
        "TPUReplicateContext {}. This is most likely due to the fact that "
        "enqueueing embedding data is called inside control flow or a "
        "tf.function inside `strategy.run`. This is not supported because "
        "outside compilation fails to extract the enqueue ops as the head of "
        "a computation.".format(ops.get_default_graph(), graph)
    )
  return in_tpu_ctx


# ==================================================
# Line: 1418

def _copy_tensors_to_device(
    self,
    partitioned_tensors: Dict[str, Any],

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
# Line: 83

def get_sum_combiner(self):

  @def_function.function
  def sum_combiner(valency, vectors):
    max_valency = vectors.shape[0]
    valid_mask = array_ops.range(max_valency) < valency
    vectors_masked = array_ops.where(
        array_ops.expand_dims(valid_mask, axis=-1),
        vectors,
        array_ops.zeros_like(vectors),
    )
    return math_ops.reduce_sum(vectors_masked, axis=0)

  return sum_combiner


# ==================================================
# Line: 98

def get_positional_weight_combiner(self):

  @def_function.function
  def positional_weight_combiner(valency, vectors, weights):
    max_valency = vectors.shape[0]
    valid_mask = array_ops.range(max_valency) < valency
    vectors_masked = array_ops.where(
        array_ops.expand_dims(valid_mask, axis=-1),
        vectors,
        array_ops.zeros_like(vectors),
    )
    return math_ops.matvec(vectors_masked, weights, transpose_a=True)

  return positional_weight_combiner


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_test.py
# Line: 54

def testHandlesNameCollision(self):
  """Test AddValue handles name collisions for ops from different graphs."""
  with ops.Graph().as_default():
    z = array_ops.zeros([2, 3], name="a")
    assert z.name == "a:0", "Expected: a:0, Found: %s" % z.name

    @def_function.function
    def f():
      pivot = control_flow_ops.no_op()
      context = tpu_replication.TPUReplicateContext(
          b"context", 1, pivot=pivot)
      context.Enter()
      array_ops.identity(z)  # Capture z.
      z1 = array_ops.zeros([3, 2], name="a")
      assert z1.name == "a:0", "Expected: a:0, Found: %s" % z1.name
      z2 = array_ops.zeros([3, 2], name="a")
      # Prior to fixing b/166794533 this would fail with a shape mismatch
      # because context.AddValue would have cached `z` by its name which
      # collides with z1's name.
      result = z1 + z2
      context.Exit()
      return result

    f.get_concrete_function()



# ==================================================
# Line: 82

def testUsingInfeedQueueWithRegularizer(self):
  """Test that Layer regularizers can reference data created in loops."""

  with ops.Graph().as_default():

    def make_regularizer(scale):
      def regularizer(inputs):
        return scale * math_ops.reduce_sum(math_ops.square(inputs))
      return regularizer

    def training_step(inputs, scale):
      outputs = convolutional.conv2d(
          inputs,
          filters=16,
          kernel_size=(3, 3),
          data_format="channels_first",
          kernel_regularizer=make_regularizer(scale))
      loss = math_ops.reduce_mean(math_ops.square(outputs))
      return loss.op

    inputs = array_ops.zeros(shape=(128, 32, 32, 16))
    scale = array_ops.ones(shape=())
    infeed = tpu_feed.InfeedQueue(
        tuple_types=[dtypes.float32, dtypes.float32],
        tuple_shapes=[inputs.shape, scale.shape])

    def loop():
      return training_loop.repeat(5, training_step, infeed_queue=infeed)

    # This should not throw an error.
    tpu.rewrite(loop)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_feed.py
# Occurrences: Lines 637-640 (2 instances)

def _default_placement_function(self, index):
  return "/task:%d/device:CPU:0" % (index / 8)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
# Line: 243

def _numpy_sequence_lookup(self, table, indices, values, batch_size,
                           max_sequence_length, dim):
  # First we truncate to max_sequence_length.
  valid_entries = np.nonzero(indices[:, 1] < max_sequence_length)[0]
  indices = indices[valid_entries]
  values = values[valid_entries]
  # Then we gather the values
  lookup = table[values]
  # Then we scatter them into the result array.
  scatter_result = np.zeros([batch_size, max_sequence_length, dim])
  for i, index in enumerate(indices):
    scatter_result[index[0], index[1], :] = lookup[i]
  return scatter_result


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/client/client.py
# Line: 185

def _symptom_msg(self, msg):
  """Return the structured Symptom message."""
  return 'Symptom: ' + msg


# ==================================================
# Line: 357

def get_local_ip(self):
  """Return the local ip address of the Google Cloud VM the workload is running on."""
  return _request_compute_metadata('instance/network-interfaces/0/ip')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/client/client_test.py
# Line: 94

def mock_service_client(self, tpu_map=None):
  if tpu_map is None:
    tpu_map = {}

  mock_locations = mock.MagicMock()
  mock_locations.nodes.return_value = MockNodeClass(tpu_map)

  mock_project = mock.MagicMock()
  mock_project.locations.return_value = mock_locations

  mock_client = mock.MagicMock()
  mock_client.projects.return_value = mock_project
  return mock_client


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
# Line: 896

def _add_data_for_tensor(self, tensor, weight, indices, values, weights,
                         int_zeros, float_zeros, path):
  if weight is not None:
    raise ValueError(
        "Weight specified for dense input {}, which is not allowed. "
        "Weight will always be 1 in this case.".format(path))
  # For tensors, there are no indices and no weights.
  indices.append(int_zeros)
  values.append(math_ops.cast(array_ops.reshape(tensor, [-1]), dtypes.int64))
  weights.append(float_zeros)


# ==================================================
# Line: 907

def _add_data_for_sparse_tensor(self, tensor, weight, indices, values,
                                weights, int_zeros, float_zeros, path,
                                feature):
  sample_indices = math_ops.cast(tensor.indices, dtypes.int32)
  if tensor.shape.rank == 2:
    if not feature.output_shape and feature.max_sequence_length > 0:
      # Add one dimension to the last axis.
      sample_indices = array_ops.pad(
          sample_indices, paddings=[[0, 0], [0, 1]])
  else:
    if feature.max_sequence_length > 0:
      logging.warning(
          (
              "Input tensor is rank %d which is above 2, the"
              " max_sequence_length setting will be ignored."
          ),
          tensor.shape.rank,
      )
  indices.append(sample_indices)
  values.append(math_ops.cast(tensor.values, dtypes.int64))
  # If we have weights they must be a SparseTensor.
  if weight is not None:
    if not isinstance(weight, sparse_tensor.SparseTensor):
      raise ValueError("Weight for {} is type {} which does not match "
                       "type input which is SparseTensor.".format(
                           path, type(weight)))
    weights.append(math_ops.cast(weight.values, dtypes.float32))
  else:
    weights.append(float_zeros)


# ==================================================
# Line: 937

def _add_data_for_ragged_tensor(self, tensor, weight, row_splits, values,
                                weights, int_zeros, float_zeros, path,
                                feature):
  row_splits.append(math_ops.cast(tensor.row_splits, dtypes.int32))
  values.append(math_ops.cast(tensor.values, dtypes.int64))
  # If we have weights they must be a RaggedTensor.
  if weight is not None:
    if not isinstance(weight, ragged_tensor.RaggedTensor):
      raise ValueError("Weight for {} is type {} which does not match "
                       "type input which is RaggedTensor.".format(
                           path, type(weight)))
    weights.append(math_ops.cast(weight.values, dtypes.float32))
  else:
    weights.append(float_zeros)


# ==================================================
# Line: 1020

def _raise_error_for_incorrect_control_flow_context(self):
  """Raises an error if we are not in the TPUReplicateContext."""
  # Do not allow any XLA control flow (i.e. control flow in between a
  # TPUStrategy's run call and the call to this function), as we can't
  # extract the enqueue from the head when in XLA control flow.
  graph = ops.get_default_graph()
  in_tpu_ctx = False
  while graph is not None:
    ctx = graph._get_control_flow_context()  # pylint: disable=protected-access
    while ctx is not None:
      if isinstance(ctx, tpu_replication.TPUReplicateContext):
        in_tpu_ctx = True
        break
      ctx = ctx.outer_context
    if in_tpu_ctx:
      break
    graph = getattr(graph, "outer_graph", None)
  if graph != ops.get_default_graph() and in_tpu_ctx:
    raise RuntimeError(
        "Current graph {} does not match graph which contains "
        "TPUReplicateContext {}. This is most likely due to the fact that "
        "enqueueing embedding data is called inside control flow or a "
        "tf.function inside `strategy.run`. This is not supported because "
        "outside compilation fails to extract the enqueue ops as the head of "
        "a computation.".format(ops.get_default_graph(), graph))
  return in_tpu_ctx


# ==================================================
# Line: 1047

def _raise_error_for_non_direct_inputs(self, features):
  """Checks all tensors in features to see if they are a direct input."""

  # expand_composites here is important: as composite tensors pass through
  # tpu.replicate, they get 'flattened' into their component tensors and then
  # repacked before being passed to the tpu function. In means that it is the
  # component tensors which are produced by an op with the
  # "_tpu_input_identity" attribute.
  for path, input_tensor in nest.flatten_with_joined_string_paths(
      features, expand_composites=True):
    if input_tensor.op.type == "Placeholder":
      continue
    try:
      is_input = input_tensor.op.get_attr("_tpu_input_identity")
    except ValueError:
      is_input = False
    if not is_input:
      raise ValueError(
          "Received input tensor {} which is the output of op {} (type {}) "
          "which does not have the `_tpu_input_identity` attr. Please "
          "ensure that the inputs to this layer are taken directly from "
          "the arguments of the function called by "
          "strategy.run. Two possible causes are: dynamic batch size "
          "support or you are using a keras layer and are not passing "
          "tensors which match the dtype of the `tf.keras.Input`s."
          "If you are triggering dynamic batch size support, you can "
          "disable it by passing tf.distribute.RunOptions("
          "experimental_enable_dynamic_batch_size=False) to the options "
          "argument of strategy.run().".format(path,
                                               input_tensor.op.name,
                                               input_tensor.op.type))


# ==================================================
# Line: 1079

def _raise_error_for_inputs_not_on_cpu(self, flat_inputs, flat_paths):
  """Checks all tensors in features to see are placed on the CPU."""

  def check_device(path, device_string):
    spec = tf_device.DeviceSpec.from_string(device_string)
    if spec.device_type == "TPU":
      raise ValueError(
          "Received input tensor {} which is on a TPU input device {}. Input "
          "tensors for TPU embeddings must be placed on the CPU. Please "
          "ensure that your dataset is prefetching tensors to the host by "
          "setting the 'experimental_fetch_to_device' option of the "
          "dataset distribution function. See the documentation of the "
          "enqueue method for an example.".format(path, device_string))

  # expand_composites here is important, we need to check the device of each
  # underlying tensor.
  for input_tensor, input_path in zip(flat_inputs, flat_paths):
    if nest.is_nested_or_composite(input_tensor):
      input_tensors = nest.flatten(input_tensor, expand_composites=True)
    else:
      input_tensors = [input_tensor]
    for t in input_tensors:
      if (t.op.type == "Identity" and
          t.op.inputs[0].op.type == "TPUReplicatedInput"):
        for tensor in t.op.inputs[0].op.inputs:
          check_device(input_path, tensor.device)
      else:
        check_device(input_path, t.device)


# ==================================================
# Line: 1455

def _get_input_shape_for_ragged_tensor(
    self, tensor, feature, per_replica, path

# ==================================================
# Line: 1530

def _is_tensor_shape_match(self, shape_a: TensorShape,
                           shape_b: TensorShape) -> bool:
  """Check if shape b matches with shape a."""
  for s_a, s_b in zip(shape_a.as_list(), shape_b.as_list()):
    if s_a and s_b and s_a != s_b:
      return False
  return True


# ==================================================
# Line: 1549

def _create_copy_for_async_checkpoint(
    self, feature_config, optimizer, pipeline_execution_with_tensor_core):
  """Create a TPUEmbedding copy for checkpoint/async_checkpoint_helper.py."""
  return TPUEmbedding(
      feature_config=feature_config,
      optimizer=optimizer,
      pipeline_execution_with_tensor_core=pipeline_execution_with_tensor_core)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
# Line: 160

def test_run_user_main_test(self):
  test_module = _write_and_load_module("""

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tensor_tracer.py
# Line: 605

def _escape_namescopes(self, variable_name):
  return variable_name.replace('/', '_').replace(':', '_')


# ==================================================
# Line: 1101

def _is_in_control_flow(self, op):
  """Returns true if the given op is inside a tf.cond or in tf.while_loop.

  Args:
    op: A tensorflow op that should be checked whether in control flow or not.
  Returns:
    A boolean value whether the op is in control flow or not.
  """
  return control_flow_util.IsInCond(op)


# ==================================================
# Line: 1290

def _filter_execution_path_operations(self, operations, fetches):
  """Returns the set of ops in the execution path to compute given fetches."""

  # If no fetch provided, then return all operations.
  if fetches is None:
    return set(operations)
  # Convert to list, if a single element is provided.
  if not isinstance(fetches, (list, tuple)):
    fetches = [fetches]
  # If a tensor is given as fetch, convert it to op.
  op_fetches = []
  for fetch in fetches:
    if isinstance(fetch, ops.Operation):
      op_fetches.append(fetch)
    elif isinstance(fetch, tensor_lib.Tensor):
      op_fetches.append(fetch.op)
    else:
      raise RuntimeError('Given fetch:%s is neither a tensor nor an op.'
                         %fetch)

  execution_path_operations = set(op_fetches)
  traverse_stack = list(op_fetches)
  while True:
    if not traverse_stack:
      break
    head_op = traverse_stack.pop()
    input_ops = [tensor_input.op for tensor_input in head_op.inputs]
    input_ops.extend(head_op.control_inputs)

    for input_op in input_ops:
      if input_op not in execution_path_operations:
        # Filter out loop condition operations, tracing them causes a cycle.
        # Trace only the loop-body.
        if TensorTracer.loop_cond_op(input_op):
          continue
        execution_path_operations.add(input_op)
        traverse_stack.append(input_op)
  return execution_path_operations


# ==================================================
# Line: 1732

def _process_tensor_fetches(self, tensor_fetches):
  """Check that tensor_fetches is not empty and have valid tensors."""
  # If none or empty list.
  if tensor_fetches is None:
    raise RuntimeError('tensor_fetches provided to tensor_tracer cannot be '
                       'None.')
  if not isinstance(tensor_fetches, (list, tuple)):
    tensor_fetches = [tensor_fetches]
  elif not tensor_fetches:
    raise RuntimeError('tensor_fetches provided to tensor_tracer cannot be '
                       'empty list.')
  fetches = []
  for fetch in tensor_fetches:
    if isinstance(fetch, tensor_lib.Tensor):
      fetches.append(fetch)
    else:
      raise RuntimeError('Given tensor_fetch:%s is not a tensor.' % fetch)
  return fetches


# ==================================================
# Line: 1751

def _process_op_fetches(self, op_fetches):
  """Check that op_fetches have valid ops."""
  if op_fetches is None:
    return []

  if not isinstance(op_fetches, (list, tuple)):
    op_fetches = [op_fetches]

  fetches = []
  for fetch in op_fetches:
    if isinstance(fetch, ops.Operation):
      fetches.append(fetch)
    elif isinstance(fetch, tensor_lib.Tensor):
      fetches.append(fetch.op)
    else:
      logging.warning('Ignoring the given op_fetch:%s, which is not an op.' %
                      fetch)
  return fetches


# ==================================================
# Line: 1770

def _convert_fetches_to_input_format(self, input_fetches, current_fetches):
  """Changes current_fetches' format, so that it matches input_fetches."""
  if isinstance(input_fetches, tensor_lib.Tensor):
    if len(current_fetches) != 1:
      raise RuntimeError('Tensor tracer input/output fetches do not match.')
    return current_fetches[0]
  else:
    if len(current_fetches) != len(current_fetches):
      raise RuntimeError('Tensor tracer input/output fetches do not match.')
    elif isinstance(input_fetches, tuple):
      return tuple(current_fetches)
    else:
      return current_fetches


# ==================================================
# Line: 1784

def _get_op_control_flow_context(self, op):
  """Returns the control flow of the given op.

  Args:
    op: tf.Operation for which the control flow context is requested.
  Returns:
    op_control_flow_context: which the is control flow context of the given
    op. If the operation type is LoopExit, returns the outer control flow
    context.
  """
  # pylint: disable=protected-access
  op_control_flow_context = op._control_flow_context
  # pylint: enable=protected-access
  if control_flow_util.IsLoopExit(op):
    op_control_flow_context = op_control_flow_context.outer_context
  return op_control_flow_context


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/profiler/profiler_analysis_pb2_grpc.py
# Line: 69

def NewSession(self, request, context):
  """Starts a profiling session, blocks until it completes.

  TPUProfileAnalysis service delegate this to TPUProfiler service.
  Populate the profiled data in repository, then return status to caller.
  """
  context.set_code(grpc.StatusCode.UNIMPLEMENTED)
  context.set_details('Method not implemented!')
  raise NotImplementedError('Method not implemented!')


# ==================================================
# Line: 79

def EnumSessions(self, request, context):
  """Enumerate existing sessions and return available profile tools."""
  context.set_code(grpc.StatusCode.UNIMPLEMENTED)
  context.set_details('Method not implemented!')
  raise NotImplementedError('Method not implemented!')


# ==================================================
# Line: 85

def GetSessionToolData(self, request, context):
  """Retrieve specific tool's data for specific session."""
  context.set_code(grpc.StatusCode.UNIMPLEMENTED)
  context.set_details('Method not implemented!')
  raise NotImplementedError('Method not implemented!')



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
# Line: 181

def _apply_combiner_to_embeddings(
    self,
    embeddings: tensor.Tensor,
    weight: tensor.Tensor,
    combiner: Optional[Text] = None) -> tensor.Tensor:
  """Apply the combiner to the embedding look up result on second to last axis.

  Args:
    embeddings: A Tensor of the embedding lookup result.
    weight: A Tensor of weight which has the same shape of the embeddings.
    combiner: One of "mean", "sum", "sqrtn". Defaults to "mean".

  Raises:
    ValueError: If the combiner is not one of 'mean', 'sqrtn' or 'sum'.
  Returns:
    A Tensor.
  """
  if combiner is None:
    combiner = "mean"
  if combiner == "sum":
    embeddings = math_ops.reduce_sum(embeddings, axis=-2)
  elif combiner == "mean":
    embeddings = math_ops.reduce_sum(embeddings, axis=-2)
    weight_sum = math_ops.reduce_sum(weight, axis=-2)
    embeddings = math_ops.div_no_nan(embeddings, weight_sum)
  elif combiner == "sqrtn":
    embeddings = math_ops.reduce_sum(embeddings, axis=-2)
    weight_squared = math_ops.pow(weight, 2)
    weight_sum = math_ops.reduce_sum(weight_squared, axis=-2)
    weight_sum_sqrt = math_ops.sqrt(weight_sum)
    embeddings = math_ops.div_no_nan(embeddings, weight_sum_sqrt)
  else:
    raise ValueError(
        f"combiner must be one of 'mean', 'sqrtn' or 'sum', got {combiner}")
  return embeddings


# ==================================================
# Line: 217

def _pad_or_truncate_with_sequence_length(
    self, embeddings: tensor.Tensor, sequence_length: int

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3_checkpoint_test.py
# Line: 107

  def _get_tmpdir(self, name, subdir=""):
    segments = [os.environ.get("TEST_TMPDIR", "/tmp"), name] + (
        [subdir] if subdir else []
    )
    return os.path.join(*segments)


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/stateful_random_ops.py
# Line: 472

def _create_variable(self, *args, **kwargs):
  """Creates a variable.

  Args:
    *args: positional arguments passed along to `variables.Variable.
    **kwargs: keyword arguments passed along to `variables.Variable.

  Returns:
    The created variable.
  """
  with ops.name_scope("random_generator"):
    # Make sure we don't change this name since Keras was using this name
    # to filter out the state variable.
    kwargs["name"] = "StateVar"
    v = variables.Variable(*args, **kwargs)
  if isinstance(v, sharded_variable.ShardedVariable):
    # RNG state is an atomic entity representing a 128-bit or
    # 192-bit value, so it mustn't be sharded.
    raise ValueError(
        "tf.random.Generator state is sharded, which is not allowed. When "
        "creating a tf.distribute.experimental.ParameterServerStrategy, "
        "please make sure that the `variable_partitioner` "
        "argument won't shard a "
        "small variable of shape [2] or [3]. Ways to avoid sharding small "
        "variables include setting `variable_partitioner` to None or to "
        "tf.distribute.experimental.partitioners.MinSizePartitioner with a "
        "large enough `min_shard_bytes`.")
  return v


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
# Line: 78

def _StripNode(self, nd):
  snode = node_def_pb2.NodeDef(name=nd.name, op=nd.op, input=nd.input)
  if nd.device:
    snode.device = nd.device
  return snode


# ==================================================
# Line: 475

def _makeGradient(self, use_case=False):
  inputs = [variables.Variable(2.0), variables.Variable(5.0)]
  with backprop.GradientTape() as tape:
    for x in inputs:
      tape.watch(x)
    f1 = lambda: math_ops.multiply(inputs[0], 17)
    f2 = lambda: math_ops.add(inputs[1], 23)
    if use_case:
      z = cond_v2.indexed_case(variables.Variable(1), [f1, f2])
    else:
      z = cond_v2.cond_v2(math_ops.less(inputs[0], inputs[1]), f1, f2)
  return tape.gradient(z, inputs)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/init_ops_test.py
# Line: 176

def testVariablePlacementWithOrthogonalInitializer(self):
  with ops.Graph().as_default() as g:
    with ops.device('gpu:0'):
      variable_scope.get_variable(
          name='v', shape=[8, 2], initializer=init_ops.Orthogonal)
      variable_scope.get_variable(
          name='w', shape=[8, 2], initializer=init_ops.RandomNormal)
    run_metadata = config_pb2.RunMetadata()
    run_options = config_pb2.RunOptions(
        trace_level=config_pb2.RunOptions.FULL_TRACE)
    config = config_pb2.ConfigProto(
        allow_soft_placement=False, log_device_placement=True)

    # Note: allow_soft_placement=False will fail whenever we cannot satisfy
    # the colocation constraints.
    with session.Session(config=config, graph=g) as sess:
      sess.run(
          variables.global_variables_initializer(),
          options=run_options,
          run_metadata=run_metadata)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
# Line: 87

def _QuantizedOutputToFloat(self, quantized, quantized_min, quantized_max):
  number_of_bits = 32
  number_of_steps = 1 << number_of_bits
  range_adjust = (number_of_steps / (number_of_steps - np.float64(1.0)))
  quantized_range = ((quantized_max - quantized_min) * range_adjust)
  range_scale = (quantized_range / number_of_steps)
  lowest_quantized = -(1 << (number_of_bits - 1))
  result = np.array([(quantized_min +
                      ((float(x) - lowest_quantized) * range_scale))
                     for x in quantized.flatten()], dtype=np.float64)
  return result


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/split_benchmark.py
# Line: 54

def _run_graph(self, device, output_shape, variable, num_outputs, axis):
  """Run the graph and print its execution time.

  Args:
    device: string, the device to run on.
    output_shape: shape of each output tensors.
    variable: whether or not the output shape should be fixed
    num_outputs: the number of outputs to split the input into
    axis: axis to be split

  Returns:
    The duration of the run in seconds.
  """
  graph = ops.Graph()
  with graph.as_default():
    if not variable:
      if axis == 0:
        input_shape = [output_shape[0] * num_outputs, output_shape[1]]
        sizes = [output_shape[0] for _ in range(num_outputs)]
      else:
        input_shape = [output_shape[0], output_shape[1] * num_outputs]
        sizes = [output_shape[1] for _ in range(num_outputs)]
    else:
      sizes = np.random.randint(
          low=max(1, output_shape[axis] - 2),
          high=output_shape[axis] + 2,
          size=num_outputs)
      total_size = np.sum(sizes)
      if axis == 0:
        input_shape = [total_size, output_shape[1]]
      else:
        input_shape = [output_shape[0], total_size]

    outputs = build_graph(device, input_shape, sizes, axis)
  config = config_pb2.ConfigProto(graph_options=config_pb2.GraphOptions(
      optimizer_options=config_pb2.OptimizerOptions(
          opt_level=config_pb2.OptimizerOptions.L0)))
  with session_lib.Session(graph=graph, config=config) as session:
    logging.set_verbosity("info")
    variables.global_variables_initializer().run()
    bench = benchmark.TensorFlowBenchmark()
    bench.run_op_benchmark(
        session,
        outputs,
        mbs=input_shape[0] * input_shape[1] * 4 * 2 * 100 / 1e6,
        extras={
            "input_shape": input_shape,
            "variable": variable,
            "axis": axis
        })


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/variable_scope.py
# Line: 947

def _get_default_initializer(self, name, shape=None, dtype=dtypes.float32):
  """Provide a default initializer and a corresponding value.

  Args:
    name: see get_variable.
    shape: see get_variable.
    dtype: see get_variable.

  Returns:
    initializer and initializing_from_value. See get_variable above.

  Raises:
    ValueError: When giving unsupported dtype.
  """
  del shape
  # If dtype is DT_FLOAT, provide a uniform unit scaling initializer
  if dtype.is_floating:
    initializer = init_ops.glorot_uniform_initializer()
    initializing_from_value = False
  # If dtype is DT_INT/DT_UINT, provide a default value `zero`
  # If dtype is DT_BOOL, provide a default value `FALSE`
  elif (dtype.is_integer or dtype.is_unsigned or dtype.is_bool or
        dtype == dtypes.string):
    initializer = init_ops.zeros_initializer()
    initializing_from_value = False
  # NOTES:Do we need to support for handling DT_STRING and DT_COMPLEX here?
  else:
    raise ValueError("An initializer for variable %s of %s is required" %
                     (name, dtype.base_dtype))

  return initializer, initializing_from_value



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
# Line: 248

  def _lambda_for_fields(self):
    return lambda: {
        'a':
            np.ones([1, 2, 3, 1]),
        'b':
            np.ones([1, 2, 3, 1, 5]),
        'c':
            ragged_factory_ops.constant(
                np.zeros([1, 2, 3, 1], dtype=np.uint8), dtype=dtypes.uint8),
        'd':
            ragged_factory_ops.constant(
                np.zeros([1, 2, 3, 1, 3]).tolist(), ragged_rank=1),
        'e':
            ragged_factory_ops.constant(
                np.zeros([1, 2, 3, 1, 2, 2]).tolist(), ragged_rank=2),
        'f':
            ragged_factory_ops.constant(
                np.zeros([1, 2, 3, 1, 3]), dtype=dtypes.float32),
        'g':
            StructuredTensor.from_pyval([[
                [  # pylint: disable=g-complex-comprehension
                    [{
                        'x': j,
                        'y': k
                    }] for k in range(3)
                ] for j in range(2)
            ]]),
        'h':
            StructuredTensor.from_pyval([[
                [  # pylint: disable=g-complex-comprehension
                    [[
                        {
                            'x': j,
                            'y': k,
                            'z': z
                        } for z in range(j)
                    ]] for k in range(3)
                ] for j in range(2)
            ]]),
    }


if __name__ == '__main__':

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
# Line: 99

def _randomNDArray(self, shape):
  return 2 * np.random.random_sample(shape) - 1


# ==================================================
# Line: 201

def _genParams(self, dtype=dtypes.float32):
  batch_size = 1
  image_height = 10
  image_width = 10
  channels = 1
  image_shape = (batch_size, image_height, image_width, channels)
  num_boxes = 3
  boxes_shape = (num_boxes, 4)
  random_seed.set_seed(123)
  image = random_ops.random_normal(shape=image_shape, dtype=dtype)
  boxes = random_ops.random_uniform(shape=boxes_shape, dtype=dtypes.float32)
  box_indices = random_ops.random_uniform(
      shape=(num_boxes,), minval=0, maxval=batch_size, dtype=dtypes.int32)
  crop_size = constant_op.constant([3, 3], dtype=dtypes.int32)
  return image, boxes, box_indices, crop_size


# ==================================================
# Line: 252

def _randomFloats(self, shape, low=0.0, high=1.0, dtype=dtypes.float32):
  """Generate a tensor of random floating-point values.

  Values will be continuously distributed in the range [low, high).

  Note that we use numpy to generate random numbers and then feed the result
  through a constant op to avoid the re-rolling of TensorFlow random ops on
  each run in graph mode.

  Args:
    shape: The output shape.
    low: Lower bound of random numbers generated, inclusive.
    high: Upper bound of random numbers generated, exclusive.
    dtype: The output dtype.

  Returns:
    A random tensor
  """
  val = np.random.random_sample(
      shape)  # float64 continuous uniform [0.0, 1.0)
  diff = high - low
  val *= diff
  val += low
  return constant_op.constant(val, dtype=dtype)


# ==================================================
# Line: 277

def _randomInts(self, shape, low, high):
  """Generate a tensor of random 32-bit integer values.

  Note that we use numpy to generate random numbers and then feed the result
  through a constant op to avoid the re-rolling of TensorFlow random ops on
  each run in graph mode.

  Args:
    shape: The output shape.
    low: Lower bound of random numbers generated, inclusive.
    high: Upper bound of random numbers generated, exclusive.

  Returns:
    A random tensor
  """
  val = np.random.randint(low=low, high=high, size=shape)
  return constant_op.constant(val, dtype=dtypes.int32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_constant_op_test.py
# Line: 232

def _make_graph_def(self, text):
  ret = graph_pb2.GraphDef()
  text_format.Parse(text, ret)
  return ret


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/while_v2.py
# Line: 1067

def _get_optimized_reduction_ops_cache_key(
    self,
    op_type,
    inputs,
    dtypes=None,  # pylint: disable=redefined-outer-name
    input_types=None,
    name=None,
    attrs=None,
    op_def=None,
    compute_device=True):
  # We need all elements of CacheKey to be hashable.
  inputs = tuple(map(lambda t: t.ref(), inputs))

  if dtypes is not None:
    dtypes = tuple(dtypes)

  if input_types is not None:
    input_types = tuple(input_types)

  if attrs is not None:
    hashable_attrs = []
    for attr_name, attr_value in sorted(attrs.items()):
      hashable_attrs.append((attr_name, attr_value.SerializeToString()))
    attrs = tuple(hashable_attrs)

  if op_def is not None:
    op_def = op_def.SerializeToString()

  return OptimizedReductionOpsCacheKey(op_type, inputs, dtypes, input_types,
                                       name, attrs, op_def, compute_device)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_ops.py
# Line: 413

def _conv1d(self, input, filter, strides, padding, data_format, name):
  return conv1d(
      value=input,
      filters=filter,
      stride=strides,
      padding=padding,
      data_format=data_format,
      name=name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_ops_test.py
# Line: 180

def _RGBToGrayscale(self, images):
  is_batch = True
  if len(images.shape) == 3:
    is_batch = False
    images = np.expand_dims(images, axis=0)
  out_shape = images.shape[0:3] + (1,)
  out = np.zeros(shape=out_shape, dtype=np.uint8)
  for batch in range(images.shape[0]):
    for y in range(images.shape[1]):
      for x in range(images.shape[2]):
        red = images[batch, y, x, 0]
        green = images[batch, y, x, 1]
        blue = images[batch, y, x, 2]
        gray = 0.2989 * red + 0.5870 * green + 0.1140 * blue
        out[batch, y, x, 0] = int(gray)
  if not is_batch:
    out = np.squeeze(out, axis=0)
  return out


# ==================================================
# Line: 1588

def _adjustContrastNp(self, x_np, contrast_factor):
  mean = np.mean(x_np, (1, 2), keepdims=True)
  y_np = mean + contrast_factor * (x_np - mean)
  return y_np


# ==================================================
# Line: 1715

def _NumpyPerImageWhitening(self, x):
  num_pixels = np.prod(x.shape)
  mn = np.mean(x)
  std = np.std(x)
  stddev = max(std, 1.0 / math.sqrt(num_pixels))

  y = x.astype(np.float32)
  y -= mn
  y /= stddev
  return y


# ==================================================
# Line: 2912

def shouldRunOnGPU(self, method, nptype):
  if (method == image_ops.ResizeMethod.NEAREST_NEIGHBOR and
      nptype in [np.float32, np.float64]):
    return True
  else:
    return False


# ==================================================
# Line: 3467

def shouldRunOnGPU(self, method, nptype):
  if (method == image_ops.ResizeMethodV1.NEAREST_NEIGHBOR and
      nptype in [np.float32, np.float64]):
    return True
  else:
    return False


# ==================================================
# Line: 4903

def _path(self, name):
  base = "tensorflow/core/lib/webp/testdata/"
  return os.path.join(base, name)


# ==================================================
# Line: 5097

def _total_variation_np(self, x_np):
  """Calculate the total variation of x_np using numpy.
  This implements the same function as TensorFlow but
  using numpy instead.

  Args:
      x_np: Numpy array with 3 or 4 dimensions.
  """

  dim = len(x_np.shape)

  if dim == 3:
    # Calculate differences for neighboring pixel-values using slices.
    dif1 = x_np[1:, :, :] - x_np[:-1, :, :]
    dif2 = x_np[:, 1:, :] - x_np[:, :-1, :]

    # Sum for all axis.
    sum_axis = None
  elif dim == 4:
    # Calculate differences for neighboring pixel-values using slices.
    dif1 = x_np[:, 1:, :, :] - x_np[:, :-1, :, :]
    dif2 = x_np[:, :, 1:, :] - x_np[:, :, :-1, :]

    # Only sum for the last 3 axis.
    sum_axis = (1, 2, 3)
  else:
    # This should not occur in this test-code.
    pass

  tot_var = np.sum(np.abs(dif1), axis=sum_axis) + \
            np.sum(np.abs(dif2), axis=sum_axis)

  return tot_var


# ==================================================
# Line: 5143

def _generateArray(self, shape):
  """Generate an array of the given shape for use in testing.
  The numbers are calculated as the cumulative sum, which
  causes the difference between neighboring numbers to vary."""

  # Flattened length of the array.
  flat_len = np.prod(shape)

  a = np.array(range(flat_len), dtype=int)
  a = np.cumsum(a)
  a = a.reshape(shape)

  return a


# ==================================================
# Occurrences: Lines 5808-5813 (2 instances)

def _PSNR_NumPy(self, orig, target, max_value):
  """Numpy implementation of PSNR."""
  mse = ((orig - target) ** 2).mean(axis=(-3, -2, -1))
  return 20 * np.log10(max_value) - 10 * np.log10(mse)


# ==================================================
# Line: 5912

def _RandomImage(self, shape, max_val):
  """Returns an image or image batch with given shape."""
  return np.random.rand(*shape).astype(np.float32) * max_val


# ==================================================
# Line: 6068

def _RandomImage(self, shape, max_val):
  """Returns an image or image batch with given shape."""
  return np.random.rand(*shape).astype(np.float32) * max_val


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/init_ops_v2.py
# Line: 68

def get_config(self):
  """Returns the configuration of the initializer as a JSON-serializable dict.

  Returns:
    A JSON-serializable Python dict.
  """
  return {}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_grad_test_base.py
# Line: 117

def _itGen(self, smaller_shape, larger_shape):
  up_sample = (smaller_shape, larger_shape)
  down_sample = (larger_shape, smaller_shape)
  pass_through = (larger_shape, larger_shape)
  shape_pairs = (up_sample, down_sample, pass_through)
  # Align corners is deprecated in TF2.0, but align_corners==False is not
  # supported by XLA.
  options = [(True, False)]
  if not test_util.is_xla_enabled():
    options += [(False, True), (False, False)]
  for align_corners, half_pixel_centers in options:
    for in_shape, out_shape in shape_pairs:
      yield in_shape, out_shape, align_corners, half_pixel_centers


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
# Line: 36

def _AccumulateNTemplate(self, inputs, init, shape, validate_shape):
  var = gen_state_ops.temporary_variable(
      shape=shape, dtype=inputs[0].dtype.base_dtype)
  ref = state_ops.assign(var, init, validate_shape=validate_shape)
  update_ops = [
      state_ops.assign_add(
          ref, tensor, use_locking=True).op for tensor in inputs
  ]
  with ops.control_dependencies(update_ops):
    return gen_state_ops.destroy_temporary_variable(ref, var_name=var.op.name)


# ==================================================
# Line: 69

def _GenerateUnorderedInputs(self, size, n):
  inputs = [random_ops.random_uniform(shape=[size]) for _ in range(n)]
  random.shuffle(inputs)
  return inputs


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
# Line: 280

def _BuildAndTestMiniMNIST(self, param_index, tag):
  # Fix seed to avoid occasional flakiness
  np.random.seed(6)

  # Hyperparameters
  batch = 3
  inputs = 16
  features = 32
  classes = 10

  # Define the parameters
  inp_data = np.random.random_sample(inputs * batch)
  hidden_weight_data = np.random.randn(inputs * features) / np.sqrt(inputs)
  hidden_bias_data = np.random.random_sample(features)
  sm_weight_data = np.random.randn(features * classes) / np.sqrt(features)
  sm_bias_data = np.random.random_sample(classes)

  # special care for labels since they need to be normalized per batch
  label_data = np.random.random(batch * classes).reshape((batch, classes))
  s = label_data.sum(axis=1)
  label_data /= s[:, None]

  # We treat the inputs as "parameters" here
  inp = constant_op.constant(
      inp_data.tolist(),
      shape=[batch, inputs],
      dtype=dtypes.float64,
      name="inp")
  hidden_weight = constant_op.constant(
      hidden_weight_data.tolist(),
      shape=[inputs, features],
      dtype=dtypes.float64,
      name="hidden_weight")
  hidden_bias = constant_op.constant(
      hidden_bias_data.tolist(),
      shape=[features],
      dtype=dtypes.float64,
      name="hidden_bias")
  softmax_weight = constant_op.constant(
      sm_weight_data.tolist(),
      shape=[features, classes],
      dtype=dtypes.float64,
      name="softmax_weight")
  softmax_bias = constant_op.constant(
      sm_bias_data.tolist(),
      shape=[classes],
      dtype=dtypes.float64,
      name="softmax_bias")

  # List all the parameter so that we can test them one at a time
  all_params = [inp, hidden_weight, hidden_bias, softmax_weight, softmax_bias]

  # Now, Building MNIST
  def f(inp, hidden_weight, hidden_bias, softmax_weight, softmax_bias):
    features = nn_ops.relu(
        nn_ops.xw_plus_b(inp, hidden_weight, hidden_bias), name="features")
    logits = nn_ops.xw_plus_b(
        features, softmax_weight, softmax_bias, name="logits")
    labels = constant_op.constant(
        label_data.tolist(),
        shape=[batch, classes],
        dtype=dtypes.float64,
        name="labels")
    cost = nn_ops.softmax_cross_entropy_with_logits(
        labels=labels, logits=logits, name="cost")
    return cost

  def f_restricted(x):
    xs = all_params
    i = param_index
    # use x for the i-th parameter
    xs = xs[0:i] + [x] + xs[i + 1:]
    return f(*xs)

  # Test the gradients.
  err = gradient_checker.max_error(*gradient_checker.compute_gradient(
      f_restricted, [all_params[param_index]], delta=1e-5))

  tf_logging.info("Mini MNIST: %s gradient error = %g", tag, err)
  return err


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/numpy_ops/np_utils_test.py
# Line: 162

def testSigMismatchIsNotError(self):
  """Tests that signature mismatch is not an error (when configured so)."""
  np_utils.set_is_sig_mismatch_an_error(False)

  def np_fun(x, y=1, **kwargs):
    return

  # The following functions all have signature mismatches, but they shouldn't
  # throw errors when is_sig_mismatch_an_error() is False.

  @np_utils.np_doc(None, np_fun=np_fun)
  def f1(a):
    return

  def f2(x, kwargs):
    return

  @np_utils.np_doc(None, np_fun=np_fun)
  def f3(x, y):
    return


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_test.py
# Line: 51

def _ZeroFraction(self, x):
  assert x.shape
  total_elements = np.prod(x.shape)
  nonzeros = np.count_nonzero(x.flatten())
  return 1.0 - nonzeros / total_elements


# ==================================================
# Line: 101

def _softmax(self, x):
  assert len(x.shape) == 2
  if x.shape[1] == 0:
    return x
  m = x.max(1)[:, np.newaxis]
  u = np.exp(x - m)
  z = u.sum(1)[:, np.newaxis]
  return u / z


# ==================================================
# Line: 159

def _log_poisson_loss(self, x, z, compute_full_loss=False):
  lpl = np.exp(x) - z * x
  if compute_full_loss:
    stirling_approx = z * np.log(z) - z + 0.5 * np.log(2. * np.pi * z)
    lpl += np.ma.masked_array(stirling_approx, mask=(z <= 1)).filled(0.)
  return lpl


# ==================================================
# Line: 195

def _log_softmax(self, x):
  assert len(x.shape) == 2
  m = x.max(1)[:, np.newaxis]
  u = x - m
  return u - np.log(np.sum(np.exp(u), 1, keepdims=True))


# ==================================================
# Line: 262

def _l2Normalize(self, x, dim):
  if isinstance(dim, list):
    norm = np.linalg.norm(x, axis=tuple(dim))
    for d in dim:
      norm = np.expand_dims(norm, d)
    return x / norm
  else:
    norm = np.apply_along_axis(np.linalg.norm, dim, x)
    return x / np.expand_dims(norm, dim)


# ==================================================
# Line: 478

def testLargeRate(self, dropout_fn):
  x_dim = 40
  y_dim = 30
  t = constant_op.constant(1.0, shape=[x_dim, y_dim], dtype=dtypes.float32)
  _ = dropout_fn(t, rate=0.9)


# ==================================================
# Line: 487

def testVariableRef(self, dropout_fn):
  x = variable_scope.get_variable("x", shape=[10, 10], dtype=dtypes.float32)
  _ = dropout_fn(x, rate=0.1)


# ==================================================
# Line: 540

def _GenerateTestData(self, num_classes, dim, batch_size, num_true, labels,
                      sampled, subtract_log_q):
  """Randomly generates input/output data for a single test case.

  This function returns numpy constants for use in a test case.

  Args:
    num_classes: An int. The number of embedding classes in the test case.
    dim: An int. The dimension of the embedding.
    batch_size: An int. The batch size.
    num_true: An int. The number of target classes per training example.
    labels: A list of batch_size * num_true ints. The target classes.
    sampled: A list of indices in [0, num_classes).
    subtract_log_q: A bool corresponding to the parameter in
      _compute_sampled_logits().

  Returns:
    weights: Embedding weights to use as test input. It is a numpy array
        of shape [num_classes, dim]
    biases: Embedding biases to use as test input. It is a numpy array
        of shape [num_classes].
    hidden_acts: Forward activations of the network to use as test input.
        It is a numpy array of shape [batch_size, dim].
    sampled_vals: A tuple based on `sampled` to use as test input in the
        format returned by a *_candidate_sampler function.
    exp_logits: The output logits expected from _compute_sampled_logits().
        It is a numpy array of shape [batch_size, num_true + len(sampled)].
    exp_labels: The output labels expected from _compute_sampled_logits().
        It is a numpy array of shape [batch_size, num_true + len(sampled)].
  """
  weights = np.random.randn(num_classes, dim).astype(np.float32)
  biases = np.random.randn(num_classes).astype(np.float32)
  hidden_acts = np.random.randn(batch_size, dim).astype(np.float32)

  true_exp = np.full([batch_size, 1], fill_value=0.5, dtype=np.float32)
  sampled_exp = np.full([len(sampled)], fill_value=0.5, dtype=np.float32)
  sampled_vals = (sampled, true_exp, sampled_exp)

  sampled_w, sampled_b = weights[sampled], biases[sampled]
  true_w, true_b = weights[labels], biases[labels]

  true_logits = np.sum(
      hidden_acts.reshape((batch_size, 1, dim)) * true_w.reshape(
          (batch_size, num_true, dim)),
      axis=2)
  true_b = true_b.reshape((batch_size, num_true))
  true_logits += true_b
  sampled_logits = np.dot(hidden_acts, sampled_w.T) + sampled_b

  if subtract_log_q:
    true_logits -= np.log(true_exp)
    sampled_logits -= np.log(sampled_exp[np.newaxis, :])

  exp_logits = np.concatenate([true_logits, sampled_logits], axis=1)
  exp_labels = np.hstack(
      (np.ones_like(true_logits) / num_true, np.zeros_like(sampled_logits)))

  return weights, biases, hidden_acts, sampled_vals, exp_logits, exp_labels


# ==================================================
# Line: 1779

def testUnknownSize(self):
  x = tensor_spec.TensorSpec(None, dtypes.float32, name="x")
  k = np.ones([3, 6, 6, 5], dtype=np.float32)

  @def_function.function
  def F(value):
    return nn_ops.convolution(value, k, "SAME")

  F.get_concrete_function(x)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/math_ops_test.py
# Line: 386

def sampledADDMMRef(
    self,
    indices,
    values,
    dense_shape,
    mat1,
    mat2,
    beta=1.0,
    alpha=1.0,
    output_type=dtypes.float32,

# ==================================================
# Occurrences: Lines 727-737 (3 instances)

def intTestData(self):
  nums = np.arange(-10, 10, 1).reshape(20, 1)
  divs = np.arange(-3, 4, 2).reshape(1, 4)
  return nums, divs


# ==================================================
# Line: 844

def testComplexDiv(self):
  foo = array_ops.constant([1. + 3.j])
  _ = math_ops.divide(foo, 1.)
  _ = math_ops.div(foo, 2.)


# ==================================================
# Line: 906

def intEdgeTestData(self, dtype):
  """Edge-case test data for integer types."""
  # INT_MIN/-1 will produce signed-integer overflow, so we instead test
  # (INT_MIN + 1) / -1.
  nums = np.array(
      [
          [np.iinfo(dtype).min, -1, 1, np.iinfo(dtype).max],
          [np.iinfo(dtype).min + 1, -1, 1, np.iinfo(dtype).max],
          [np.iinfo(dtype).min, -1, 1, np.iinfo(dtype).max],
          [np.iinfo(dtype).min, -1, 1, np.iinfo(dtype).max],
      ],
      dtype=dtype,
  )
  divs = np.array(
      [
          [
              np.iinfo(dtype).min,
              np.iinfo(dtype).min,
              np.iinfo(dtype).min,
              np.iinfo(dtype).min,
          ],
          [-1, -1, -1, -1],
          [1, 1, 1, 1],
          [
              np.iinfo(dtype).max,
              np.iinfo(dtype).max,
              np.iinfo(dtype).max,
              np.iinfo(dtype).max,
          ],
      ],
      dtype=dtype,
  )
  return nums, divs


# ==================================================
# Line: 1384

def _generateRandomTensor(self, dtype, shape):
  if dtype.is_integer:
    array = np.random.default_rng().integers(
        low=dtype.min, high=dtype.max, size=shape, endpoint=True)
    return constant_op.constant(array, dtype=dtype)
  else:
    array = np.random.default_rng().uniform(low=-1.0, high=1.0, size=shape)
    return constant_op.constant(array, dtype=dtype)


# ==================================================
# Line: 1393

def _getValidDtypes(self):
  return (dtypes.bfloat16, dtypes.float16, dtypes.float32, dtypes.float64,
          dtypes.int32, dtypes.int64)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
# Line: 35

def _npBatchNorm(self, x, m, v, beta, gamma, epsilon,
                 scale_after_normalization, shift_after_normalization):
  y = (x - m) / np.sqrt(v + epsilon)
  y = y * gamma if scale_after_normalization else y
  return y + beta if shift_after_normalization else y


# ==================================================
# Line: 41

def _opsBatchNorm(self, x, m, v, beta, gamma, epsilon,
                  scale_after_normalization, shift_after_normalization):
  y = (x - m) * math_ops.rsqrt(v + epsilon)
  if scale_after_normalization:
    y = gamma * y
  return y + beta if shift_after_normalization else y


# ==================================================
# Line: 48

def _tfBatchNormV1(self, x, m, v, beta, gamma, epsilon,
                   scale_after_normalization):
  """Original implementation."""
  test_util.set_producer_version(ops.get_default_graph(), 8)
  return gen_nn_ops._batch_norm_with_global_normalization(
      x, m, v, beta, gamma, epsilon, scale_after_normalization)


# ==================================================
# Line: 55

def _tfBatchNormV1BW(self, x, m, v, beta, gamma, epsilon,
                     scale_after_normalization):
  """Re-implementation of the original kernel for backward compatibility."""
  return nn_impl.batch_norm_with_global_normalization(
      x, m, v, beta, gamma, epsilon, scale_after_normalization)


# ==================================================
# Line: 61

def _tfBatchNormV2(self, x, m, v, beta, gamma, epsilon,
                   scale_after_normalization, shift_after_normalization):
  """New implementation."""
  return nn_impl.batch_normalization(x, m, v, beta if
                                     shift_after_normalization else None,
                                     gamma if scale_after_normalization else
                                     None, epsilon)


# ==================================================
# Line: 349

def _npSuffStats(self, x, axes, shift, keep_dims):
  axis = tuple(axes)
  if shift is not None:
    m_ss = np.sum(x - shift, axis=axis, keepdims=keep_dims)
    v_ss = np.sum((x - shift) * (x - shift), axis=axis, keepdims=keep_dims)
  else:
    m_ss = np.sum(x, axis=axis, keepdims=keep_dims)
    v_ss = np.sum(x * x, axis=axis, keepdims=keep_dims)
  count = 1.0
  for d in range(x.ndim):
    if d in set(axes):
      count *= x.shape[d]
  if not keep_dims:
    shift = np.asarray(shift)
  return count, m_ss, v_ss, shift


# ==================================================
# Line: 365

def _opSuffStats(self, x, axes, shift, keep_dims):
  return nn_impl.sufficient_statistics(x, axes, shift, keep_dims)


# ==================================================
# Line: 409

def _npNormalizeMoments(self, counts, mean_ss, variance_ss, shift):
  mean = mean_ss / counts
  variance = variance_ss / counts - mean * mean
  if shift is not None:
    mean += shift
  return mean, variance


# ==================================================
# Line: 416

def _opNormalizeMoments(self, counts, mean_ss, variance_ss, shift):
  return nn_impl.normalize_moments(counts, mean_ss, variance_ss, shift)


# ==================================================
# Line: 452

def _unweighted_moments(self, x, axes, keep_dims=False, extra_out_grads=None):
  # Method to compute moments of `x` wrt `axes`.
  #
  # This is exposed so WeightedMomentsTest can inherit the tests and
  # assertions from MomentsTest; the extra_out_grads argument allows
  # its inherited gradient tests to assert gradients against the
  # weights as well as the input values.

  return nn_impl.moments(x, axes, keep_dims=keep_dims)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_nn_test.py
# Line: 39

def _log_softmax(self, x):
  assert len(x.shape) == 2
  m = x.max(1)[:, np.newaxis]
  u = x - m
  return u - np.log(np.sum(np.exp(u), 1, keepdims=True))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
# Occurrences: Lines 263-273 (3 instances)

def _assert_non_singular(self):
  raise errors.InvalidArgumentError(
      node_def=None, op=None, message="Zero operators are always "
      "non-invertible.")


# ==================================================
# Line: 335

def _linop_matmul(
    self,
    left_operator: "LinearOperatorZeros",
    right_operator: linear_operator.LinearOperator
  ) -> linear_operator.LinearOperator:
  if not left_operator.is_square or not right_operator.is_square:
    raise ValueError("Matmul with non-square `LinearOperator`s or non-square "
                     "`LinearOperatorZeros` not supported at this time.")
  return left_operator


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
# Line: 340

def _linop_matmul(
    self,
    left_operator: "LinearOperatorIdentity",
    right_operator: linear_operator.LinearOperator,
  ) -> "LinearOperatorIdentity":
  del left_operator
  return right_operator


# ==================================================
# Line: 348

def _linop_solve(
    self,
    left_operator: "LinearOperatorIdentity",
    right_operator: linear_operator.LinearOperator,

# ==================================================
# Occurrences: Lines 356-362 (3 instances)

def _assert_non_singular(self):
  return control_flow_ops.no_op("assert_non_singular")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_permutation.py
# Line: 177

def _check_perm(self, perm):
  """Static check of perm."""
  if (perm.shape.ndims is not None and perm.shape.ndims < 1):
    raise ValueError(f"Argument `perm` must have at least 1 dimension. "
                     f"Received: {perm}.")
  if not perm.dtype.is_integer:
    raise TypeError(f"Argument `perm` must be integer dtype. "
                    f"Received: {perm}.")
  # Check that the permutation satisfies the uniqueness constraint.
  static_perm = tensor_util.constant_value(perm)
  if static_perm is not None:
    sorted_perm = np.sort(static_perm, axis=-1)
    if np.any(sorted_perm != np.arange(0, static_perm.shape[-1])):
      raise ValueError(
          f"Argument `perm` must be a vector of unique integers from "
          f"0 to {static_perm.shape[-1] - 1}.")


# ==================================================
# Line: 203

def _assert_non_singular(self):
  return control_flow_ops.no_op("assert_non_singular")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_full_matrix.py
# Line: 157

def _check_matrix(self, matrix):
  """Static check of the `matrix` argument."""
  allowed_dtypes = [
      dtypes.float16,
      dtypes.float32,
      dtypes.float64,
      dtypes.complex64,
      dtypes.complex128,
  ]

  matrix = tensor_conversion.convert_to_tensor_v2_with_dispatch(
      matrix, name="matrix"
  )

  dtype = matrix.dtype
  if dtype not in allowed_dtypes:
    raise TypeError(f"Argument `matrix` must have dtype in {allowed_dtypes}. "
                    f"Received: {dtype}.")

  if matrix.shape.ndims is not None and matrix.shape.ndims < 2:
    raise ValueError(f"Argument `matrix` must have at least 2 dimensions. "
                     f"Received: {matrix}.")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
# Line: 164

def _check_reflection_axis(self, reflection_axis):
  """Static check of reflection_axis."""
  if (reflection_axis.shape.ndims is not None and
      reflection_axis.shape.ndims < 1):
    raise ValueError(
        "Argument reflection_axis must have at least 1 dimension.  "
        "Found: %s" % reflection_axis)


# ==================================================
# Occurrences: Lines 182-190 (3 instances)

def _assert_non_singular(self):
  return control_flow_ops.no_op("assert_non_singular")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
# Line: 167

def _check_row_col(self, row, col):
  """Static check of row and column."""
  for name, tensor in [["row", row], ["col", col]]:
    if tensor.shape.ndims is not None and tensor.shape.ndims < 1:
      raise ValueError("Argument {} must have at least 1 dimension.  "
                       "Found: {}".format(name, tensor))

  if row.shape[-1] is not None and col.shape[-1] is not None:
    if row.shape[-1] != col.shape[-1]:
      raise ValueError(
          "Expected square matrix, got row and col with mismatched "
          "dimensions.")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_lower_triangular.py
# Line: 171

def _check_tril(self, tril):
  """Static check of the `tril` argument."""

  if tril.shape.ndims is not None and tril.shape.ndims < 2:
    raise ValueError(
        "Argument tril must have at least 2 dimensions.  Found: %s"
        % tril)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
# Line: 176

def _check_diag(self, diag):
  """Static check of diag."""
  if diag.shape.ndims is not None and diag.shape.ndims < 1:
    raise ValueError("Argument diag must have at least 1 dimension.  "
                     "Found: %s" % diag)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_inversion.py
# Line: 184

def _linop_solve(
    self,
    left_operator: "LinearOperatorInversion",
    right_operator: linear_operator.LinearOperator,

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
# Occurrences: Lines 60-63 (2 instances)

def get_gradient_components(self, value):
  return value._type_spec._to_components(value)


# ==================================================
# Line: 738

def _linop_matmul(
    self, left_operator: "LinearOperator", right_operator: "LinearOperator"

# ==================================================
# Line: 981

def _linop_solve(
    self, left_operator: "LinearOperator", right_operator: "LinearOperator"
  ) -> "LinearOperator":
  # instance of linear_operator_identity.LinearOperatorIdentity
  if hasattr(right_operator, "_ones_diag") and not hasattr(
      right_operator, "multiplier"
  ):
    return left_operator.inverse()

  # Generic solve of two `LinearOperator`s.
  is_square = property_hint_util.is_square(left_operator, right_operator)
  is_non_singular = None
  is_self_adjoint = None
  is_positive_definite = None

  if is_square:
    is_non_singular = property_hint_util.combined_non_singular_hint(
        left_operator, right_operator
    )
  elif is_square is False:  # pylint:disable=g-bool-id-comparison
    is_non_singular = False
    is_self_adjoint = False
    is_positive_definite = False

  # LinearOperator outputs a LinearOperatorComposition instance that contains
  # a LinearOperatorInversion instance, both of which
  # inherit from LinearOperator. The inline import is necessary to avoid
  # errors due to this cyclic dependency.
  from tensorflow.python.ops.linalg import linear_operator_composition  # pylint: disable=g-import-not-at-top
  from tensorflow.python.ops.linalg import linear_operator_inversion  # pylint: disable=g-import-not-at-top

  return linear_operator_composition.LinearOperatorComposition(
      operators=[
          linear_operator_inversion.LinearOperatorInversion(left_operator),
          right_operator,
      ],
      is_non_singular=is_non_singular,
      is_self_adjoint=is_self_adjoint,
      is_positive_definite=is_positive_definite,
      is_square=is_square,
  )


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
# Line: 1075

def _get_num_systems(self, operator):
  """Get some number, either 1 or 2, depending on operator."""
  if operator.tensor_rank is None or operator.tensor_rank % 2:
    return 1
  else:
    return 2



# ==================================================
# Line: 1152

def _get_num_systems(self, operator):
  """Get some number, either 1 or 2, depending on operator."""
  if operator.tensor_rank is None or operator.tensor_rank % 2:
    return 1
  else:
    return 2



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/clustering_ops.py
# Line: 439

def _mini_batch_training_op(self, inputs, cluster_idx_list, cluster_centers,
                            total_counts):
  """Creates an op for training for mini batch case.

  Args:
    inputs: list of input Tensors.
    cluster_idx_list: A vector (or list of vectors). Each element in the
      vector corresponds to an input row in 'inp' and specifies the cluster id
      corresponding to the input.
    cluster_centers: Tensor Ref of cluster centers.
    total_counts: Tensor Ref of cluster counts.

  Returns:
    An op for doing an update of mini-batch k-means.
  """
  update_ops = []
  for inp, cluster_idx in zip(inputs, cluster_idx_list):
    with ops.colocate_with(inp, ignore_existing=True):
      assert total_counts is not None
      cluster_idx = array_ops.reshape(cluster_idx, [-1])
      # Dedupe the unique ids of cluster_centers being updated so that updates
      # can be locally aggregated.
      unique_ids, unique_idx = array_ops.unique(cluster_idx)
      num_unique_cluster_idx = array_ops.size(unique_ids)
      # Fetch the old values of counts and cluster_centers.
      with ops.colocate_with(total_counts, ignore_existing=True):
        old_counts = array_ops.gather(total_counts, unique_ids)
      # TODO(agarwal): This colocation seems to run into problems. Fix it.
      with ops.colocate_with(cluster_centers, ignore_existing=True):
        old_cluster_centers = array_ops.gather(cluster_centers, unique_ids)
      # Locally aggregate the increment to counts.
      count_updates = math_ops.unsorted_segment_sum(
          array_ops.ones_like(unique_idx, dtype=total_counts.dtype),
          unique_idx, num_unique_cluster_idx)
      # Locally compute the sum of inputs mapped to each id.
      # For a cluster with old cluster value x, old count n, and with data
      # d_1,...d_k newly assigned to it, we recompute the new value as
      # \\(x += (sum_i(d_i) - k * x) / (n + k)\\).
      # Compute \\(sum_i(d_i)\\), see comment above.
      cluster_center_updates = math_ops.unsorted_segment_sum(
          inp, unique_idx, num_unique_cluster_idx)
      # Shape to enable broadcasting count_updates and learning_rate to inp.
      # It extends the shape with 1's to match the rank of inp.
      broadcast_shape = array_ops.concat([
          array_ops.reshape(num_unique_cluster_idx, [1]),
          array_ops.ones(
              array_ops.reshape(array_ops.rank(inp) - 1, [1]),
              dtype=dtypes.int32)
      ], 0)
      # Subtract k * x, see comment above.
      cluster_center_updates -= math_ops.cast(
          array_ops.reshape(count_updates, broadcast_shape),
          inp.dtype) * old_cluster_centers
      learning_rate = math_ops.reciprocal(
          math_ops.cast(old_counts + count_updates, inp.dtype))
      learning_rate = array_ops.reshape(learning_rate, broadcast_shape)
      # scale by 1 / (n + k), see comment above.
      cluster_center_updates *= learning_rate
      # Apply the updates.
    update_counts = state_ops.scatter_add(total_counts, unique_ids,
                                          count_updates)
    update_cluster_centers = state_ops.scatter_add(cluster_centers,
                                                   unique_ids,
                                                   cluster_center_updates)
    update_ops.extend([update_counts, update_cluster_centers])
  return control_flow_ops.group(*update_ops)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_d9m_test.py
# Line: 48

def _genParams(self, data_format, x_dtype, large_batch):
  if large_batch:
    batch_size = 5000
    height = width = 4
  else:
    batch_size = 10
    height = 5
    width = 5000
  channel_count = 3
  if data_format == 'NHWC':
    x_shape = (batch_size, height, width, channel_count)
  else:  # 'NCHW'
    x_shape = (batch_size, channel_count, height, width)
  # Using random_ops.random_normal would produce different values on each run
  x = constant_op.constant(np.random.normal(size=x_shape), dtype=x_dtype)
  scale_shape = (channel_count,)
  scale = constant_op.constant(
      np.random.normal(size=scale_shape), dtype=dtypes.float32)
  offset = constant_op.constant(
      np.random.normal(size=scale_shape), dtype=dtypes.float32)
  mean = np.random.normal(size=scale_shape)
  variance = np.random.normal(size=scale_shape)
  y_shape = x_shape
  y_dtype = x_dtype
  upstream_gradients = constant_op.constant(
      np.random.normal(size=y_shape), dtype=y_dtype)
  return x, scale, offset, mean, variance, upstream_gradients


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/memory_tests/custom_gradient_memory_test.py
# Line: 38

def _get_device_type(self):
  for accelerator in ["GPU", "TPU"]:
    if config.list_physical_devices(accelerator):
      return accelerator
  return "CPU"


# ==================================================
# Line: 44

def _grad(self, test_func, argnums=0):

  def _f(*params):
    with backprop.GradientTape() as tape:
      tape.watch(params)
      output = test_func(*params)
    return tape.gradient(output, params[argnums])

  return _f


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/critical_section_ops.py
# Line: 337

def _add_control_dependencies_to_lock(self, created_ops, lock_op):
  """To avoid deadlocks, all args must be executed before lock_op."""
  # Get all arguments (explicit and captured) of all ops created by fn().
  all_args = set([input_.op for op in created_ops for input_ in op.inputs])
  all_args.update(
      input_op for op in created_ops for input_op in op.control_inputs)
  # Unfortunately, we can't use sets throughout because TF seems to
  # create new Operation objects for the same op sometimes; and we
  # can't rely on id(op).

  # pylint: disable=protected-access
  all_args_dict = dict((op._id, op) for op in all_args)

  # Remove ops created within fn, or that lock_op already has a
  # control dependency on.  Also remove a possible self-loop.
  for op in created_ops:
    all_args_dict.pop(op._id, None)
  for op in lock_op.control_inputs:
    all_args_dict.pop(op._id, None)
  for input_ in lock_op.inputs:
    all_args_dict.pop(input_.op._id, None)
  all_args_dict.pop(lock_op._id, None)

  all_args = all_args_dict.values()

  if not all_args:
    # No control dependencies to add; return early.
    return

  # This group is important: it ensures that any ops in all_args
  # outside the control context of the lock_op (and this fn, which
  # runs in the same context) are added to this context before
  # being added to the control dependencies of lock_op.
  all_args = control_flow_ops.group(*all_args)

  lock_op._add_control_input(all_args)
  # pylint: enable=protected-access


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/sort_ops_test.py
# Line: 33

def random_array(self, shape, dtype):
  if np.issubdtype(dtype, np.integer):
    imin = np.iinfo(dtype).min
    imax = np.iinfo(dtype).max
    return np.random.randint(imin, imax, shape, dtype)
  else:
    return np.random.random(shape).astype(dtype)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/normal.py
# Occurrences: Lines 184-187 (2 instances)

def _event_shape_tensor(self):
  return constant_op.constant([], dtype=dtypes.int32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/distribution.py
# Line: 649

def _batch_shape(self):
  return tensor_shape.TensorShape(None)


# ==================================================
# Line: 686

def _event_shape(self):
  return tensor_shape.TensorShape(None)


# ==================================================
# Line: 1232

def _expand_sample_shape_to_vector(self, x, name):
  """Helper to `sample` which ensures input is 1D."""
  x_static_val = tensor_util.constant_value(x)
  if x_static_val is None:
    prod = math_ops.reduce_prod(x)
  else:
    prod = np.prod(x_static_val, dtype=x.dtype.as_numpy_dtype())

  ndims = x.get_shape().ndims  # != sample_ndims
  if ndims is None:
    # Maybe expand_dims.
    ndims = array_ops.rank(x)
    expanded_shape = util.pick_vector(
        math_ops.equal(ndims, 0),
        np.array([1], dtype=np.int32), array_ops.shape(x))
    x = array_ops.reshape(x, expanded_shape)
  elif ndims == 0:
    # Definitely expand_dims.
    if x_static_val is not None:
      x = ops.convert_to_tensor(
          np.array([x_static_val], dtype=x.dtype.as_numpy_dtype()),
          name=name)
    else:
      x = array_ops.reshape(x, [1])
  elif ndims != 1:
    raise ValueError("Input is neither scalar nor vector.")

  return x, prod


# ==================================================
# Line: 1305

def _is_scalar_helper(self, static_shape, dynamic_shape_fn):
  """Implementation for `is_scalar_batch` and `is_scalar_event`."""
  if static_shape.ndims is not None:
    return static_shape.ndims == 0
  shape = dynamic_shape_fn()
  if (shape.get_shape().ndims is not None and
      shape.get_shape().dims[0].value is not None):
    # If the static_shape is correctly written then we should never execute
    # this branch. We keep it just in case there's some unimagined corner
    # case.
    return shape.get_shape().as_list() == [0]
  return math_ops.equal(array_ops.shape(shape)[0], 0)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
# Line: 307

def _maybe_assert_valid_concentration(self, concentration, validate_args):
  """Checks the validity of the concentration parameter."""
  if not validate_args:
    return concentration
  return control_flow_ops.with_dependencies([
      check_ops.assert_positive(
          concentration,
          message="Concentration parameter must be positive."),
      check_ops.assert_rank_at_least(
          concentration, 1,
          message="Concentration parameter must have >=1 dimensions."),
      check_ops.assert_less(
          1, array_ops.shape(concentration)[-1],
          message="Concentration parameter must have event_size >= 2."),
  ], concentration)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/uniform.py
# Occurrences: Lines 160-163 (2 instances)

def _event_shape_tensor(self):
  return constant_op.constant([], dtype=dtypes.int32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
# Line: 103

def _merge_dicts(self, old=None, new=None):
  """Helper to merge two dictionaries."""
  old = {} if old is None else old
  new = {} if new is None else new
  for k, v in new.items():
    val = old.get(k, None)
    if val is not None and val is not v:
      raise ValueError("Found different value for existing key "
                       "(key:{} old_value:{} new_value:{}".format(
                           k, old[k], v))
    old[k] = v
  return old


# ==================================================
# Line: 116

def _merge(self, old, new):
  """Helper to merge which handles merging one value."""
  if old is None:
    return new
  elif new is not None and old is not new:
    raise ValueError("Incompatible values: %s != %s" % (old, new))
  return old


# ==================================================
# Line: 642

def _forward_event_shape_tensor(self, input_shape):
  """Subclass implementation for `forward_event_shape_tensor` function."""
  # By default, we assume event_shape is unchanged.
  return input_shape


# ==================================================
# Line: 666

def _forward_event_shape(self, input_shape):
  """Subclass implementation for `forward_event_shape` public function."""
  # By default, we assume event_shape is unchanged.
  return input_shape


# ==================================================
# Line: 686

def _inverse_event_shape_tensor(self, output_shape):
  """Subclass implementation for `inverse_event_shape_tensor` function."""
  # By default, we assume event_shape is unchanged.
  return output_shape


# ==================================================
# Line: 710

def _inverse_event_shape(self, output_shape):
  """Subclass implementation for `inverse_event_shape` public function."""
  # By default, we assume event_shape is unchanged.
  return tensor_shape.TensorShape(output_shape)


# ==================================================
# Line: 1099

def _maybe_get_static_event_ndims(self, event_ndims):
  """Helper which returns tries to return an integer static value."""
  event_ndims_ = distribution_util.maybe_get_static_value(event_ndims)

  if isinstance(event_ndims_, (np.generic, np.ndarray)):
    if event_ndims_.dtype not in (np.int32, np.int64):
      raise ValueError("Expected integer dtype, got dtype {}".format(
          event_ndims_.dtype))

    if isinstance(event_ndims_, np.ndarray) and len(event_ndims_.shape):
      raise ValueError("Expected a scalar integer, got {}".format(
          event_ndims_))
    event_ndims_ = int(event_ndims_)

  return event_ndims_

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/student_t.py
# Occurrences: Lines 239-242 (2 instances)

def _event_shape_tensor(self):
  return constant_op.constant([], dtype=math_ops.int32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/beta.py
# Occurrences: Lines 237-240 (2 instances)

def _event_shape_tensor(self):
  return constant_op.constant([], dtype=dtypes.int32)


# ==================================================
# Line: 327

def _maybe_assert_valid_concentration(self, concentration, validate_args):
  """Checks the validity of a concentration parameter."""
  if not validate_args:
    return concentration
  return control_flow_ops.with_dependencies([
      check_ops.assert_positive(
          concentration,
          message="Concentration parameter must be positive."),
  ], concentration)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/categorical.py
# Occurrences: Lines 261-264 (2 instances)

def _event_shape_tensor(self):
  return constant_op.constant([], dtype=dtypes.int32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
# Line: 332

def _maybe_assert_valid_concentration(self, concentration, validate_args):
  """Checks the validity of the concentration parameter."""
  if not validate_args:
    return concentration
  concentration = distribution_util.embed_check_categorical_event_shape(
      concentration)
  return control_flow_ops.with_dependencies([
      check_ops.assert_positive(
          concentration,
          message="Concentration parameter must be positive."),
  ], concentration)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/laplace.py
# Occurrences: Lines 148-151 (2 instances)

def _event_shape_tensor(self):
  return constant_op.constant([], dtype=dtypes.int32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/identity_bijector.py
# Occurrences: Lines 58-67 (4 instances)

def _forward(self, x):
  return x


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/gamma.py
# Occurrences: Lines 208-211 (2 instances)

def _event_shape_tensor(self):
  return constant_op.constant([], dtype=dtypes.int32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/distributions/bernoulli.py
# Occurrences: Lines 115-118 (2 instances)

def _event_shape_tensor(self):
  return array_ops.constant([], dtype=dtypes.int32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/init_ops.py
# Line: 67

def get_config(self):
  """Returns the configuration of the initializer as a JSON-serializable dict.

  Returns:
    A JSON-serializable Python dict.
  """
  return {}


# ==================================================
# Line: 1145

def _dict_to_tensor(self, x, k1, k2):
  """Convert a dictionary to a tensor.

  Args:
    x: A k1 * k2 dictionary.
    k1: First dimension of x.
    k2: Second dimension of x.

  Returns:
    A k1 * k2 tensor.
  """

  return array_ops_stack.stack([
      array_ops_stack.stack([x[i, j] for j in range(k2)]) for i in range(k1)])


# ==================================================
# Line: 1292

def _dict_to_tensor(self, x, k):
  """Convert a dictionary to a tensor.

  Args:
    x: A dictionary of length k.
    k: Dimension of x.

  Returns:
    A tensor with the same dimension.
  """

  return array_ops_stack.stack([x[i] for i in range(k)])


# ==================================================
# Line: 1426

def _dict_to_tensor(self, x, k1, k2, k3):
  """Convert a dictionary to a tensor.

  Args:
    x: A k1 * k2 dictionary.
    k1: First dimension of x.
    k2: Second dimension of x.
    k3: Third dimension of x.

  Returns:
    A k1 * k2 * k3 tensor.
  """

  return array_ops_stack.stack([array_ops_stack.stack(
      [array_ops_stack.stack([x[i, j, k] for k in range(k3)])
       for j in range(k2)]) for i in range(k1)])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
# Line: 77

def call_op(self, op, *args, **kwargs):
  return op(*args, **kwargs)


# ==================================================
# Line: 102

def is_wrapped_tensor_arg(self, value):
  if isinstance(value, WrappedTensor):
    return True
  if isinstance(value, (list, tuple)):
    if any(isinstance(x, WrappedTensor) for x in value):
      return True
  return False



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_resize_image_op_test.py
# Line: 35

def make_image_batch(self, sizes, channels):
  if not sizes:
    return ragged_tensor.RaggedTensor.from_tensor(
        array_ops.zeros([0, 5, 5, channels]), ragged_rank=2)
  images = [
      array_ops.reshape(
          math_ops.range(w * h * channels * 1.0), [w, h, channels])
      for (w, h) in sizes
  ]
  return ragged_concat_ops.stack(images)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops_test.py
# Line: 47

def _softmax(self, x):
  assert len(x.shape) == 2
  if x.shape[1] == 0:
    return x
  m = x.max(1)[:, np.newaxis]
  u = np.exp(x - m)
  z = u.sum(1)[:, np.newaxis]
  return u / z


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
# Line: 2511

def _to_components(self, value):
  if is_ragged(value):
    return [value.flat_values] + list(value.nested_row_splits)
  else:
    return [value]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
# Line: 49

def batch(self, spec: "DynamicRaggedShape.Spec",
          batch_size) -> "DynamicRaggedShape.Spec":
  if spec.num_row_partitions:
    new_head = _batch_rp_spec_head(spec._row_partitions[0], batch_size)  # pylint:disable=protected-access
    new_tail = [_batch_rp_spec(rp, batch_size) for rp in spec._row_partitions]  # pylint:disable=protected-access
    new_rp = [new_head] + new_tail
    new_static_inner_shape = _batch_static_inner_shape(
        spec._static_inner_shape, batch_size)  # pylint:disable=protected-access

    return DynamicRaggedShape.Spec(
        row_partitions=new_rp,
        static_inner_shape=new_static_inner_shape,
        dtype=spec.dtype)
  elif batch_size is None:
    if spec.inner_rank == 0:
      return DynamicRaggedShape.Spec._from_tensor_shape(  # pylint:disable=protected-access
          [None],
          0,
          dtype=spec.dtype)
    else:
      # Might be None
      new_head = RowPartitionSpec(
          uniform_row_length=spec._dimension(0),  # pylint:disable=protected-access
          dtype=spec.dtype)
      new_static_inner_shape = _batch_static_inner_shape(
          spec._static_inner_shape, batch_size)  # pylint:disable=protected-access
      return DynamicRaggedShape.Spec(
          row_partitions=[new_head],
          static_inner_shape=new_static_inner_shape,
          dtype=spec.dtype)
  else:

    return DynamicRaggedShape.Spec(
        row_partitions=[],
        static_inner_shape=_batch_tensor_shape(
            spec._static_inner_shape,  # pylint:disable=protected-access
            batch_size),
        dtype=spec.dtype)


# ==================================================
# Line: 88

def unbatch(self,
            spec: "DynamicRaggedShape.Spec") -> "DynamicRaggedShape.Spec":
  if spec.num_row_partitions:
    result = []
    head = spec._row_partitions[0]  # pylint:disable=protected-access
    scale = None if head.uniform_row_length is None else head.nrows

    for rp in spec._row_partitions[1:]:  # pylint:disable=protected-access
      if scale is None:
        result.append(
            RowPartitionSpec(
                nrows=None,
                nvals=None,
                uniform_row_length=rp.uniform_row_length,
                dtype=spec.dtype))
      else:
        nrows = None if rp.nrows is None else rp.nrows // scale
        if rp.uniform_row_length is None:
          scale = None
          result.append(
              RowPartitionSpec(
                  nrows=nrows,
                  nvals=None,
                  uniform_row_length=None,
                  dtype=spec.dtype))
        else:
          result.append(
              RowPartitionSpec(
                  nrows=nrows,
                  nvals=rp.nvals // scale,
                  uniform_row_length=rp.uniform_row_length,
                  dtype=spec.dtype))
    return DynamicRaggedShape.Spec(
        row_partitions=result,
        static_inner_shape=_unbatch_static_inner_shape(
            spec._static_inner_shape, scale),  # pylint:disable=protected-access
        dtype=spec.dtype)
  else:  # spec.num_row_partitions == 0
    return DynamicRaggedShape.Spec(
        row_partitions=[],
        static_inner_shape=spec._static_inner_shape[1:],  # pylint:disable=protected-access
        dtype=spec.dtype)


# ==================================================
# Occurrences: Lines 131-135 (2 instances)

def decode(self, spec: "DynamicRaggedShape.Spec",
           encoding) -> "DynamicRaggedShape":
  return DynamicRaggedShape.from_tensor(encoding, dtype=spec.dtype)


# ==================================================
# Line: 142

def encoding_specs(
    self, spec: "DynamicRaggedShape.Spec"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
# Line: 1995

def testRaggedTensorSetShapeUniformRowLength(self):
  rt = [[[1], [2], [3]], [[4], [5], [6]]]

  rt1 = RaggedTensor.from_tensor(rt, ragged_rank=1)
  rt1._set_shape([2, 3, 1])

  rt2 = nest.map_structure(
      lambda x: array_ops.placeholder_with_default(x, None),
      rt1,
      expand_composites=True)
  rt2._set_shape([2, 3, 1])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/row_partition.py
# Occurrences: Lines 1322-1325 (2 instances)

def _to_components(self, value):
  return value.row_splits()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Line: 1553

def testBroadcastDynamicShapeNextLayer(self):
  a_1 = RowPartition.from_uniform_row_length(
      1, nvals=1, nrows=1, dtype_hint=dtypes.int64)
  b_1 = RowPartition.from_row_lengths([2, 1, 3], dtype_hint=dtypes.int64)
  ac_0 = _LayerBroadcaster.from_gather_index(
      constant_op.constant([0, 0, 0], dtype=dtypes.int64))
  bc_0 = _LayerBroadcaster.from_gather_index(
      constant_op.constant([0, 1, 2], dtype=dtypes.int64))
  dynamic_ragged_shape._broadcast_dynamic_shape_next_layer_half_ragged(
      ac_0, bc_0, a_1, b_1)


# ==================================================
# Occurrences: Lines 2756-2764 (3 instances)

def test_dataset_only_dense(self):
  ragged = DynamicRaggedShape.from_lengths([4, 5, 2, 3])
  dataset_ops.DatasetV2.from_tensors(ragged)


# ==================================================
# Line: 2774

def test_dataset_only_simple_ragged(self):
  ragged = DynamicRaggedShape.from_lengths([4, (3, 0, 4, 5)])
  dataset_ops.DatasetV2.from_tensors(ragged)


# ==================================================
# Line: 2832

def test_unbatch_ragged(self):
  ragged = DynamicRaggedShape.from_lengths([4, (3, 0, 4, 5), 2, 3])
  ds = dataset_ops.DatasetV2.from_tensors(ragged)
  dsu = ds.unbatch()
  if context.executing_eagerly():
    dsu.__iter__()


# ==================================================
# Line: 3067

def testHashingWithMask(self):
  inp_data = ragged_factory_ops.constant(
      [['omar', 'stringer', 'marlo', 'wire'], ['marlo', 'skywalker', 'wire']],
      dtype=dtypes.string)
  mask = math_ops.equal(inp_data, '')
  values = string_ops.string_to_hash_bucket_strong(
      inp_data, 3, name='hash', key=[0xDECAFCAFFE, 0xDECAFCAFFE])
  values = math_ops.add(values, array_ops.ones_like(values))
  local_zeros = array_ops.zeros_like(values)
  values = array_ops.where(mask, local_zeros, values)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_cross_op_test.py
# Line: 423

def _ragged_to_sparse(self, t):
  if ragged_tensor.is_ragged(t):
    return ragged_tensor.convert_to_tensor_or_ragged_tensor(t).to_sparse()
  elif sparse_tensor.is_sparse(t):
    return sparse_tensor.SparseTensor.from_value(t)
  else:
    return ops.convert_to_tensor(t)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_concat_op_test.py
# Line: 34

def _rt_inputs_to_tensors(self, rt_inputs, ragged_ranks=None):
  if ragged_ranks is None:
    ragged_ranks = [None] * len(rt_inputs)
  return [  # pylint: disable=g-long-ternary
      ragged_factory_ops.constant(rt_input, ragged_rank=rrank)
      if rrank != 0 else constant_op.constant(rt_input)
      for (rt_input, rrank) in zip(rt_inputs, ragged_ranks)
  ]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/ragged_from_sparse_op_test.py
# Line: 66

def testGoodPartialSparseTensorRank(self):
  if not context.executing_eagerly():
    st1 = sparse_tensor.SparseTensor(
        indices=[[0, 0]],
        values=[0],
        dense_shape=array_ops.placeholder(dtypes.int64))
    st2 = sparse_tensor.SparseTensor(
        indices=array_ops.placeholder(dtypes.int64),
        values=[0],
        dense_shape=[4, 3])

    # Shouldn't throw ValueError
    RaggedTensor.from_sparse(st1)
    RaggedTensor.from_sparse(st2)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/variables.py
# Line: 872

def sparse_read(self, indices, name=None):
  r"""Gather slices from params axis axis according to indices.

  This function supports a subset of tf.gather, see tf.gather for details on
  usage.

  Args:
    indices: The index `Tensor`.  Must be one of the following types: `int32`,
      `int64`. Must be in range `[0, params.shape[axis])`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `params`.
  """
  raise AttributeError


# ==================================================
# Line: 888

def gather_nd(self, indices, name=None):
  r"""Gather slices from `params` into a Tensor with shape specified by `indices`.

  See tf.gather_nd for details.

  Args:
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Index tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `params`.
  """
  raise AttributeError


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nccl_ops_test.py
# Line: 183

def _Combined(self, tensors, devices):
  all_reduce_tensors = _NcclAllReduce(nccl_ops.all_sum, tensors, devices)
  single_reduce_tensors = _NcclReduce(nccl_ops.reduce_sum, tensors, devices)
  broadcast_tensors = _NcclBroadcast(single_reduce_tensors, devices)
  return all_reduce_tensors + broadcast_tensors


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/data_flow_ops.py
# Line: 298

def _scope_vals(self, vals):
  """Return a list of values to pass to `name_scope()`.

  Args:
    vals: A tensor, a list or tuple of tensors, or a dictionary.

  Returns:
    The values in vals as a list.
  """
  if isinstance(vals, (list, tuple)):
    return vals
  elif isinstance(vals, dict):
    return vals.values()
  else:
    return [vals]


# ==================================================
# Line: 1868

def _scope_vals(self, vals):
  """Return a list of values to pass to `name_scope()`.

  Args:
    vals: A tensor, a list or tuple of tensors, or a dictionary.

  Returns:
    The values in vals as a list.
  """
  if isinstance(vals, (list, tuple)):
    return vals
  elif isinstance(vals, dict):
    return vals.values()
  else:
    return [vals]



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/tensor_array_ops.py
# Line: 667

def close(self, name=None):
  """See TensorArray."""
  return gen_control_flow_ops.no_op(name=name)



# ==================================================
# Line: 1444

def _to_components(self, value):
  if not isinstance(value, TensorArray):
    raise TypeError("Expected value to be a TensorArray, but got: `{}`".format(
        type(value)))
  if value.flow is not None and value.flow.dtype == dtypes.variant:
    return [value.flow]
  else:
    # Convert to a TF2-style TensorArray.
    # TODO(ebrevdo): Add an "_as_variant" method to TensorArray class, or
    # "implementation / as_variant" arg to TensorArray constructor.
    with ops.name_scope("convert_tensor_array"):
      flow = list_ops.tensor_list_from_tensor(
          tensor=value.stack(), element_shape=value.element_shape)
    return [flow]


# ==================================================
# Line: 1490

def _to_legacy_output_classes(self):
  return TensorArray



# ==================================================
# Occurrences: Lines 1517-1520 (2 instances)

def flatten(self):
  return [tensor_lib.TensorSpec([], dtypes.variant)]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/array_ops_test.py
# Line: 32

def testGatherGradHasPartialStaticShape(self):
  # Create a tensor with an unknown dim 1.
  x = random_ops.random_normal([4, 10, 10])
  x = array_ops.gather(
      x, array_ops.reshape(array_ops.where_v2(x[0, :, 0] > 0.5), [-1]), axis=1
  )
  x.shape.assert_is_compatible_with([4, None, 10])

  with backprop.GradientTape() as tape:
    tape.watch(x)
    a = array_ops.gather(array_ops.gather(x, [0, 1]), [0, 1])
  grad_a = tape.gradient(a, x)
  with backprop.GradientTape() as tape:
    tape.watch(x)
    b = array_ops.gather(array_ops.gather(x, [2, 3], axis=2), [0, 1])
  grad_b = tape.gradient(b, x)

  # We make sure that the representation of the shapes are correct; the shape
  # equality check will always eval to false due to the shapes being partial.
  grad_a.shape.assert_is_compatible_with([None, None, 10])
  grad_b.shape.assert_is_compatible_with([4, None, 10])


# ==================================================
# Line: 54

def testReshapeShapeInference(self):
  # Create a tensor with an unknown dim 1.
  x = random_ops.random_normal([4, 10, 10])
  x = array_ops.gather(
      x, array_ops.reshape(array_ops.where_v2(x[0, :, 0] > 0.5), [-1]), axis=1
  )
  x.shape.assert_is_compatible_with([4, None, 10])
  a = array_ops.reshape(x, array_ops.shape(x))
  a.shape.assert_is_compatible_with([4, None, 10])
  b = array_ops.reshape(x, math_ops.cast(array_ops.shape(x), dtypes.int64))
  b.shape.assert_is_compatible_with([4, None, 10])

  # We do not shape-infer across a tf.cast into anything that's not tf.int32
  # or tf.int64, since they might end up mangling the shape.
  c = array_ops.reshape(
      x,
      math_ops.cast(
          math_ops.cast(array_ops.shape(x), dtypes.float32), dtypes.int32
      ),
  )
  c.shape.assert_is_compatible_with([None, None, None])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/gradients_test.py
# Line: 726

def testStopGradient(self):
  with ops.Graph().as_default():
    inp = constant(1.0, shape=[100, 32], name="in")
    out = array_ops.stop_gradient(inp)
    igrad = gradients.gradients(out, inp)[0]
  assert igrad is None



# ==================================================
# Line: 1163

def Multiply(self, x1, x2):
  result = x1 * x2
  grad = lambda dy: (dy * x1, dy * x2)
  return result, grad


# ==================================================
# Line: 1455

def testWithNumpyInputs(self):
  with context.eager_mode():

    @custom_gradient.custom_gradient
    def F(x):
      out = x

      def Grad(_):
        return (None, None)

      return out, Grad

    x = np.ones((3, 2), dtype=np.float32)
    # Smoke test to ensure numpy inputs are accepted
    F(x)


# ==================================================
# Line: 1584

def _TestFnVariablesGradient(self, inputs, test_fn, vars_to_grad):
  """Returns gradients of `test_model` with respect to `vars_to_grad`."""

  test_fn_re = custom_gradient.recompute_grad(test_fn)

  with backprop.GradientTape(persistent=True) as tape:
    tape.watch(vars_to_grad)
    out_re = test_fn_re(inputs, vars_to_grad)
    out = test_fn(inputs, vars_to_grad)

  grads_re = tape.gradient(out_re, vars_to_grad)
  grads = tape.gradient(out, vars_to_grad)

  return grads_re, grads


# ==================================================
# Line: 1599

def _grad(self, f, argnums=0):
  """Return a function which computes the gradient of `f`."""

  def F(*params):
    with backprop.GradientTape() as tape:
      tape.watch(params)
      outputs = f(*params)
    return tape.gradient(
        outputs,
        params[argnums],
        unconnected_gradients=unconnected_gradients.UnconnectedGradients.ZERO)

  return F


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
# Line: 37

def _batch_norm(self, x, mean, var, offset, scale, epsilon):
  # We compute the batch norm manually in this function because
  # nn_impl.batch_normalization does not support float16 yet.
  # TODO(reedwm): Add float16 support to nn_impl.batch_normalization.
  inv = math_ops.rsqrt(var + epsilon) * scale
  y = math_ops.cast(x, scale.dtype) * inv + (offset - mean * inv)
  return math_ops.cast(y, x.dtype)


# ==================================================
# Line: 102

def _running_mean(self, old_mean, new_val, factor):
  if factor == 1.0:
    return new_val
  else:
    return (1.0 - factor) * old_mean + factor * new_val


# ==================================================
# Line: 190

def _compute_gradient_error_float16(self, x, x32, x_shape, y, y32, y_shape,
                                    x_dtype):
  """Computes the gradient error for float16 inputs and/or outputs.

  This returns the same value as gradient_checker.compute_gradient_error. The
  difference is that gradient_checker.compute_gradient_error does not
  numerically compute the gradients in a numerically stable way for float16
  tensors. To fix this, this function requires float32 versions of x and y to
  numerically compute the gradients, to compare with the float16 symbolically
  computed gradients.

  Args:
    x: The input tensor.
    x32: A float32 version of x.
    x_shape: The shape of x.
    y: The output tensor.
    y32: A float32 version of y. Must be calculated based on x32, not x.
    y_shape: The shape of y.
    x_dtype: The type of x, float16 or bfloat16.

  Returns:
    The maximum error in between the two Jacobians, as in
    gradient_checker.compute_gradient_error.
  """
  x_init_val = np.random.random_sample(x_shape).astype(x_dtype)
  x32_init_val = x_init_val.astype(np.float32)

  # TODO(reedwm): Do not perform the unnecessary computations in
  # compute_gradient, since they double the computation time of this function.
  theoretical_grad, _ = gradient_checker.compute_gradient(
      x, x_shape, y, y_shape, delta=1e-3, x_init_value=x_init_val)
  _, numerical_grad = gradient_checker.compute_gradient(
      x32, x_shape, y32, y_shape, delta=1e-3, x_init_value=x32_init_val)

  # If grad is empty, no error.
  if theoretical_grad.size == 0 and numerical_grad.size == 0:
    return 0
  return np.fabs(theoretical_grad - numerical_grad).max()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/weak_tensor_math_ops_test.py
# Line: 374

def _generateRandomWeakTensor(self, dtype, shape):
  if dtype.is_integer:
    array = np.random.default_rng().integers(
        low=dtype.min, high=dtype.max, size=shape, endpoint=True)
    return _get_weak_tensor(array, dtype=dtype)
  else:
    array = np.random.default_rng().uniform(low=-1.0, high=1.0, size=shape)
    return _get_weak_tensor(array, dtype=dtype)


# ==================================================
# Line: 383

def _getValidDtypes(self):
  return (dtypes.float32, dtypes.float64, dtypes.int32, dtypes.int64)


# ==================================================
# Line: 817

def numpySafeFloorDivInt(self, x, y):
  z = x // y
  # Numpy produces 0 for INT_MIN/-1, but we expect an overflow to INT_MIN
  # so that (INT_MIN/-1) + (INT_MIN % -1) = INT_MIN + 0 = INT_MIN.
  z[(x == np.iinfo(x.dtype).min) & (y == -1)] = np.iinfo(x.dtype).min
  return z


# ==================================================
# Line: 840

def intEdgeTestData(self, dtype):
  """Edge-case test data for integer types."""
  # INT_MIN/-1 will produce signed-integer overflow, so we instead test
  # (INT_MIN + 1) / -1.
  nums = np.array(
      [
          [np.iinfo(dtype).min, -1, 1, np.iinfo(dtype).max],
          [np.iinfo(dtype).min + 1, -1, 1, np.iinfo(dtype).max],
          [np.iinfo(dtype).min, -1, 1, np.iinfo(dtype).max],
          [np.iinfo(dtype).min, -1, 1, np.iinfo(dtype).max],
      ],
      dtype=dtype,
  )
  divs = np.array(
      [
          [
              np.iinfo(dtype).min,
              np.iinfo(dtype).min,
              np.iinfo(dtype).min,
              np.iinfo(dtype).min,
          ],
          [-1, -1, -1, -1],
          [1, 1, 1, 1],
          [
              np.iinfo(dtype).max,
              np.iinfo(dtype).max,
              np.iinfo(dtype).max,
              np.iinfo(dtype).max,
          ],
      ],
      dtype=dtype,
  )
  return nums, divs


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/nn_xent_test.py
# Line: 36

def _SigmoidCrossEntropyWithLogits(self, logits, targets):
  assert len(logits) == len(targets)
  pred = [1 / (1 + exp(-x)) for x in logits]
  eps = 0.0001
  pred = [min(max(p, eps), 1 - eps) for p in pred]
  return [-z * log(y) - (1 - z) * log(1 - y) for y, z in zip(pred, targets)]


# ==================================================
# Line: 112

def _WeightedCrossEntropy(self, logits, targets, pos_coeff):
  assert len(logits) == len(targets)
  pred = [1 / (1 + exp(-x)) for x in logits]
  eps = 0.0001
  pred = [min(max(p, eps), 1 - eps) for p in pred]
  return [
      -z * pos_coeff * log(y) - (1 - z) * log(1 - y)
      for y, z in zip(pred, targets)
  ]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/rnn_grad_test.py
# Line: 119

def _lstm_block(self, op, w, b, x, cs_prev, h_prev):
  w_peephole = array_ops.zeros(cs_prev.shape[1:], dtype=w.dtype)
  _, all_cs, _, _, _, _, all_h = op(
      seq_len_max=math_ops.cast(array_ops.shape(x)[0], dtypes.int64),
      x=x,
      cs_prev=cs_prev,
      h_prev=h_prev,
      w=w,
      wci=w_peephole,
      wcf=w_peephole,
      wco=w_peephole,
      b=b,
      use_peephole=False)
  return all_cs, all_h



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/math_grad_test.py
# Line: 92

def _biasedRandN(self, shape, bias=0.1, sigma=1.0):
  """Returns samples from a normal distribution shifted `bias` away from 0."""
  value = np.random.randn(*shape) * sigma
  return value + np.sign(value) * bias


# ==================================================
# Line: 674

def _nextafter_gradient(self, x1, x2):
  with backprop.GradientTape() as tape:
    tape.watch(x1)
    tape.watch(x2)
    y = math_ops.nextafter(x1, x2)
    return tape.gradient(y, [x1, x2])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/control_flow_ops.py
# Occurrences: Lines 628-638 (4 instances)

def GetControlPivot(self):
  """Returns the pivot node for this context, or None."""
  return None


# ==================================================
# Occurrences: Lines 2199-2202 (2 instances)

def AddValue(self, x):
  return x


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/resource_variable_ops.py
# Line: 1644

def __idiv__(self, unused_other):
  raise RuntimeError("`var /= value` with `tf.Variable`s is not "
                     "supported. Use `var.assign(var / value)` to modify "
                     "the variable, or `out = var / value` if you "
                     "need to get a new output Tensor.")


# ==================================================
# Line: 1656

def __irealdiv__(self, unused_other):
  raise RuntimeError("`var /= value` with `tf.Variable`s is not "
                     "supported. Use `var.assign(var / value)` to modify "
                     "the variable, or `out = var / value` if you "
                     "need to get a new output Tensor.")


# ==================================================
# Line: 1674

def get_gradient_components(self, value):
  """Returns the components of `value` that should be included in gradients.

  For a ResourceVariable, its gradient component is its handle tensor.
  For now, we return the ResourceVariable because the gradient infrastructure
  has special logic to handle ResourceVariables. We should remove the special
  logic and return the handle tensor.

  Args:
    value: A `ResourceVariable`.

  Returns:
    `value` itself.
  """
  return value


# ==================================================
# Line: 1690

def replace_gradient_components(self, value, component_grads):
  """Replaces the gradient components in `value` with `component_grads`.

  The gradient of a ResourceVariable is either None or a Tensor. So we don't
  need `value`'s TypeSpec or non-gradient components in this method.

  Args:
    value: A `ResourceVariable` with its gradient components compatible with
      `component_grads`.
    component_grads: A `Tensor` or None as the gradient result.

  Returns:
    The `component_grads`, which is either a `Tensor` or None.
  """
  return component_grads



# ==================================================
# Line: 2697

def _to_components(self, value):
  return [value.handle]


# ==================================================
# Occurrences: Lines 2797-2806 (3 instances)

def to_tensors(self, value):
  assert isinstance(value, BaseResourceVariable)
  variable_accessed(value)
  return [value.handle]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/lookup_ops.py
# Line: 396

def _serialize_to_proto(self, **unused_kwargs):
  return None


# ==================================================
# Line: 1121

def _get_string_to_hash_bucket_fn(self, hasher_spec):
  """Returns the string_to_hash_bucket op to use based on `hasher_spec`."""
  if not isinstance(hasher_spec, HasherSpec):
    raise TypeError("`hasher_spec` must be of type HasherSpec, got "
                    f"{type(hasher_spec)}.")
  if hasher_spec.hasher == "fasthash":
    return string_ops.string_to_hash_bucket_fast
  if hasher_spec.hasher == "legacy":
    return string_ops.string_to_hash_bucket
  if hasher_spec.hasher == "stronghash":
    return functools.partial(
        string_ops.string_to_hash_bucket_strong, key=hasher_spec.key)
  raise ValueError(
      f"Found unknown hasher {hasher_spec.hasher} in `hasher_spec`")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# Line: 981

def test_assert(self):

  def loop_fn(i):
    return control_flow_assert.Assert(i < 10, [i, [10], [i + 1]])

  # TODO(agarwal): make this work with for_loop.
  with session.Session() as sess:
    sess.run(pfor_control_flow_ops.pfor(loop_fn, 3))
    sess.run(pfor_control_flow_ops.pfor(
        lambda i, pfor_config: loop_fn(i), 3))



# ==================================================
# Line: 1138

def _make_graph_def(self, text):
  ret = graph_pb2.GraphDef()
  text_format.Parse(text, ret)
  return ret


# ==================================================
# Line: 2103

def _cond(self, f=None, split=0):
  if f is None:
    f = lambda x, y: (x, y)

  def _f(x, y):
    return cond.cond(y > split, lambda: f(x, y), lambda:
                     (x + 1., y))

  return _f


# ==================================================
# Line: 2113

def _while(self, f=None):
  if f is None:
    f = lambda x, y: (x, y)

  def _f(x, y):
    return while_loop.while_loop(
        lambda j, _: j < y, lambda j, t:
        (j + 1, t + array_ops.gather(f(x, y)[0], j)), [0, x])[1], y

  return _f


# ==================================================
# Occurrences: Lines 2508-2511 (2 instances)

def _to_components(self, value):
  return (value.mass, value.velocity)


# ==================================================
# Line: 2813

def test_create_variable_once(self):
  x = array_ops.ones(shape=(3, 2, 2), dtype=dtypes.float32)
  y = array_ops.ones(shape=(2, 3), dtype=dtypes.float32)
  a_var = []

  def f(z):
    if not a_var:
      a_var.append(variables.Variable(lambda: y, name="a"))
    return math_ops.matmul(z, a_var[0] / 16)

  pfor_control_flow_ops.vectorized_map(f, x)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Line: 480

def _convert_enter(self, parent_pfor: "PFor", enter):
  """Converts an Enter node."""
  inp, stacked, _ = parent_pfor._convert_helper(enter.op.inputs[0])
  control_inputs = []
  for x in enter.op.control_inputs:
    converted = parent_pfor._convert_helper(x)
    if not isinstance(converted, ops.Operation):
      converted = converted.t
    control_inputs.append(converted)
  if control_inputs:
    with ops.control_dependencies(control_inputs):
      inp = array_ops.identity(inp)
  return inp, stacked


# ==================================================
# Line: 605

def _process_cond_unstacked(self, conditions, indices, inputs, output_tas):
  """Handles case when condition is unstacked.

  Note that all iterations end together. So we don't need to partition the
  inputs. When all iterations are done, we write the inputs to the
  TensorArrays. Note that we only write to index 0 of output_tas. Since all
  iterations end together, they can all be output together.
  """
  not_all_done = array_ops.reshape(conditions, [])
  new_output_tas = []
  # pylint: disable=cell-var-from-loop
  for i, out_ta in enumerate(output_tas):
    inp = inputs[i]
    new_output_tas.append(
        tf_cond.cond(not_all_done, lambda: out_ta,
                     lambda: out_ta.write(0, inp)))
  # pylint: enable=cell-var-from-loop
  return not_all_done, indices, inputs, new_output_tas


# ==================================================
# Line: 1442

def _restack_sparse_tensor_logically(self, indices, values, shape):
  sparse_tensor_rank = indices.get_shape().dims[-1].value
  if sparse_tensor_rank is not None:
    sparse_tensor_rank += 1

  def fn(args):
    res = gen_sparse_ops.serialize_sparse(
        args[0], args[1], args[2], out_type=dtypes.variant)
    return res

  # Applies a map function to the component tensors to serialize each
  # sparse tensor element and batch them all, then deserializes the batch.
  # TODO(rachelim): Try to do this without map_fn -- add the right offsets
  # to shape and indices tensors instead.
  result = map_fn.map_fn(fn, [indices, values, shape], dtype=dtypes.variant)
  return sparse_ops.deserialize_sparse(
      result, dtype=values.dtype, rank=sparse_tensor_rank)


# ==================================================
# Line: 4872

def _process_cond_unstacked(self, conditions, indices, inputs, output_tas):
  """Handles case when condition is pfor loop invariant."""
  # Note that all iterations end together. So we don't need to partition the
  # inputs.
  not_all_done = array_ops.reshape(conditions, [])
  return not_all_done, indices, inputs, output_tas


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
# Occurrences: Lines 455-462 (3 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, MyObject)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
# Line: 62

def _create_resource(self):
  # Return a constant here so that when re-saved, the traced `create_resource`
  # has valid returns.
  return constant_op.constant(1.0)


# ==================================================
# Line: 93

def load_graph(self, returns, meta_graph_def):
  """Called from wrap_function to import `meta_graph_def`."""
  # pylint: disable=protected-access
  saver, _ = tf_saver._import_meta_graph_with_return_elements(meta_graph_def)
  # pylint: enable=protected-access
  returns[0] = saver


# ==================================================
# Line: 100

def _extract_saver_restore(self, wrapped, saver):
  if saver is None:
    return None
  saver_def = saver.saver_def
  filename_tensor = wrapped.graph.as_graph_element(
      saver_def.filename_tensor_name
  )
  # We both feed and fetch filename_tensor so we have an operation to use to
  # feed into variable initializers (only relevant for v1 graph building).
  return wrapped.prune(
      feeds=[filename_tensor],
      fetches=[
          filename_tensor,
          wrapped.graph.as_graph_element(saver_def.restore_op_name),
      ],
  )


# ==================================================
# Line: 145

def _extract_signatures(self, wrapped, meta_graph_def):
  """Creates ConcreteFunctions for signatures in `meta_graph_def`."""
  signature_functions = {}
  for signature_key, signature_def in meta_graph_def.signature_def.items():
    if signature_def.inputs:
      input_items = sorted(
          signature_def.inputs.items(), key=lambda item: item[0]
      )
      original_input_names, input_specs = zip(*input_items)
    else:
      original_input_names = []
      input_specs = []

    # TODO(b/205015292): Support optional arguments
    feeds = [
        wrap_function._get_element_from_tensor_info(input_spec, wrapped.graph)  # pylint: disable=protected-access
        for input_spec in input_specs
    ]
    input_names = []
    input_tensors = []
    for original_input_name, feed in zip(original_input_names, feeds):
      if isinstance(feed, sparse_tensor.SparseTensor):
        # We have to give explicit name for SparseTensor arguments, because
        # these are not present in the TensorInfo.
        indices_name = "%s_indices" % original_input_name
        values_name = "%s_values" % original_input_name
        dense_shape_name = "%s_dense_shape" % original_input_name
        input_names.extend([indices_name, values_name, dense_shape_name])
        input_tensors.extend([feed.indices, feed.values, feed.dense_shape])
      elif isinstance(feed, composite_tensor.CompositeTensor):
        component_tensors = nest.flatten(feed, expand_composites=True)
        input_names.extend(
            "%s_component_%d" % (original_input_name, n)
            for n in range(len(component_tensors))
        )
        input_tensors.extend(component_tensors)
      else:
        input_names.append(original_input_name)
        input_tensors.append(feed)
    fetches = {name: out for name, out in signature_def.outputs.items()}
    input_signature = (
        (),
        func_graph.convert_structure_to_signature(
            dict(zip(input_names, input_tensors))
        ),
    )
    try:
      signature_fn = wrapped.prune(
          feeds=feeds,
          fetches=fetches,
          input_signature=input_signature,
          are_keyword_args_also_positional=True,
      )
    except lift_to_graph.UnliftableError as ex:
      # Mutate the exception to add a bit more detail.
      args = ex.args
      if not args:
        message = ""
      else:
        message = args[0]
      message = (
          "A SavedModel signature needs an input for each placeholder the "
          "signature's outputs use. An output for signature '{}' depends on "
          "a placeholder which is not an input (i.e. the placeholder is not "
          "fed a value).\n\n"
      ).format(signature_key) + message
      ex.args = (message,) + args[1:]
      raise

    # pylint: disable=protected-access
    signature_fn._arg_keywords = input_names

    if len(input_names) == 1:
      # Allowing positional arguments does not create any ambiguity if there's
      # only one.
      signature_fn._num_positional_args = 1
    else:
      signature_fn._num_positional_args = 0
    # pylint: enable=protected-access
    signature_functions[signature_key] = signature_fn
  return signature_functions


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/save_test.py
# Line: 433

def test_nested_inputs(self):
  root = autotrackable.AutoTrackable()
  root.f = def_function.function(
      lambda x: 2. * x[0],
      input_signature=([
          tensor_spec.TensorSpec(None, dtypes.float32),
          tensor_spec.TensorSpec(None, dtypes.float32)
      ],))
  root.f([constant_op.constant(1.), constant_op.constant(1.)])


# ==================================================
# Occurrences: Lines 495-499 (2 instances)

def foo(self, a):
  return a


# ==================================================
# Line: 521

def _default_save_signature(self, x):
  return x + x + 1


# ==================================================
# Line: 537

def add(self, x):
  return x + x + 1.


# ==================================================
# Line: 1005

def _deserialization_dependencies(self, children):
  return children


# ==================================================
# Line: 1018

def _deserialization_dependencies(self, children):
  del children  # Unused.
  return {"untracked": untracked}

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/load.py
# Line: 708

def _recreate_base_user_object(self, proto=None, node_id=None):
  del proto, node_id
  # Note: each user object has its own class. This allows making each one
  # individually callable by adding a `__call__` method to the classes of
  # the objects instances that have a `__call__` property.

  class _UserObject(autotrackable.AutoTrackable):
    pass

  return _UserObject(), setattr


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/load_test.py
# Line: 323

def test_cond_prune(self, cycles, use_cpp_bindings):
  # TODO(b/264869228) Fix LoadTest
  if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
  x_in = []
  x_out = []

  def f(x, y):
    x_in.append(x)
    xx = cond_v2.cond_v2(
        math_ops.less(1, 2),
        lambda: x + 1,
        lambda: x + 2,
    )
    x_out.append(xx)
    return xx, 2 * y

  f_wrapped = wrap_function.wrap_function(
      f, [tensor_spec.TensorSpec((), dtypes.float32)] * 2
  )
  f_pruned = f_wrapped.prune(x_in[0], [x_out[0]])

  class Adder(module.Module):

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32)
        ]
    )
    def add(self, x):
      return f_pruned(x)

  root = Adder()
  root.add(constant_op.constant(1.0))
  root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
  root.add(constant_op.constant(1.0))


# ==================================================
# Line: 352

def add(self, x):
  return f_pruned(x)


# ==================================================
# Line: 1855

def foo(self, a, b, c, d=10, **options):
  del options
  return a + b + c + d


# ==================================================
# Line: 1886

def do(self, x, y):
  return x + y


# ==================================================
# Line: 2457

def _create_resource(self):
  return get_handle()


# ==================================================
# Line: 2465

def _destroy_resource(self):
  handle = get_handle()
  resource_variable_ops.destroy_resource_op(
      handle, ignore_lookup_error=True
  )


# ==================================================
# Line: 3055

def foo(self, a):
  return a


# ==================================================
# Line: 3074

def test_restored_function_execute_eagerly(self, use_cpp_bindings):
  # TODO(b/264869753) Fix SingleCycleTest
  if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
  try:
    def_function.run_functions_eagerly(True)

    class MyModel(module.Module):

      @def_function.function
      def __call__(self, inputs, training=False):
        return math_ops.multiply(0.5, inputs)

    model = MyModel()
    model.__call__.get_concrete_function(
        tensor_spec.TensorSpec([None], dtypes.float32)
    )
    loaded = cycle(model, 1, use_cpp_bindings=use_cpp_bindings)

    # Calling the function should not throw an exception.
    loaded(constant_op.constant([1.0]))

  finally:
    def_function.run_functions_eagerly(False)


# ==================================================
# Line: 3409

def call(self):
  if callable(initial_value):
    return initial_value()
  return initial_value


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
# Occurrences: Lines 128-131 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, list)


# ==================================================
# Occurrences: Lines 138-141 (2 instances)

def can_decode(self, value):
  return value.HasField("list_value")


# ==================================================
# Occurrences: Lines 168-171 (2 instances)

def can_encode(self, pyobj):
  return _is_tuple(pyobj)


# ==================================================
# Occurrences: Lines 178-181 (2 instances)

def can_decode(self, value):
  return value.HasField("tuple_value")


# ==================================================
# Occurrences: Lines 188-191 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, collections_abc.Mapping)


# ==================================================
# Occurrences: Lines 198-201 (2 instances)

def can_decode(self, value):
  return value.HasField("dict_value")


# ==================================================
# Occurrences: Lines 212-215 (2 instances)

def can_encode(self, pyobj):
  return _is_named_tuple(pyobj)


# ==================================================
# Occurrences: Lines 226-229 (2 instances)

def can_decode(self, value):
  return value.HasField("named_tuple_value")


# ==================================================
# Occurrences: Lines 240-243 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, float)


# ==================================================
# Occurrences: Lines 249-252 (2 instances)

def can_decode(self, value):
  return value.HasField("float64_value")


# ==================================================
# Occurrences: Lines 260-263 (2 instances)

def can_encode(self, pyobj):
  return not isinstance(pyobj, bool) and isinstance(pyobj, int)


# ==================================================
# Occurrences: Lines 269-272 (2 instances)

def can_decode(self, value):
  return value.HasField("int64_value")


# ==================================================
# Occurrences: Lines 284-287 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, str)


# ==================================================
# Occurrences: Lines 293-296 (2 instances)

def can_decode(self, value):
  return value.HasField("string_value")


# ==================================================
# Occurrences: Lines 304-307 (2 instances)

def can_encode(self, pyobj):
  return pyobj is None


# ==================================================
# Occurrences: Lines 313-316 (2 instances)

def can_decode(self, value):
  return value.HasField("none_value")


# ==================================================
# Occurrences: Lines 324-327 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, bool)


# ==================================================
# Occurrences: Lines 333-336 (2 instances)

def can_decode(self, value):
  return value.HasField("bool_value")


# ==================================================
# Occurrences: Lines 344-347 (2 instances)

def can_encode(self, pyobj):
  return isinstance(pyobj, dtypes.DType)


# ==================================================
# Occurrences: Lines 353-356 (2 instances)

def can_decode(self, value):
  return value.HasField("tensor_dtype_value")


# ==================================================
# Line: 440

def can_encode(self, pyobj):
  """Returns true if `pyobj` can be encoded as a TypeSpec."""
  # Check if it's a registered type.
  if isinstance(pyobj, internal.TypeSpec):
    try:
      type_spec_registry.get_name(type(pyobj))
      return True
    except ValueError:
      return False

  return False


# ==================================================
# Line: 452

def do_encode(self, type_spec_value, encode_fn):
  """Returns an encoded proto for the given `tf.TypeSpec`."""
  type_spec_class_name = type_spec_registry.get_name(type(type_spec_value))
  type_spec_class = struct_pb2.TypeSpecProto.REGISTERED_TYPE_SPEC
  # Support for saving registered TypeSpecs is currently experimental.
  # Issue a warning to indicate the limitations.
  warnings.warn("Encoding a StructuredValue with type %s; loading this "
                "StructuredValue will require that this type be "
                "imported and registered." % type_spec_class_name)

  type_state = type_spec_value._serialize()  # pylint: disable=protected-access
  num_flat_components = len(
      nest.flatten(type_spec_value._component_specs, expand_composites=True))  # pylint: disable=protected-access
  encoded_type_spec = struct_pb2.StructuredValue()
  encoded_type_spec.type_spec_value.CopyFrom(
      struct_pb2.TypeSpecProto(
          type_spec_class=type_spec_class,
          type_state=encode_fn(type_state),
          type_spec_class_name=type_spec_class_name,
          num_flat_components=num_flat_components))
  return encoded_type_spec


# ==================================================
# Occurrences: Lines 474-478 (2 instances)

def can_decode(self, value):
  """Returns true if `value` can be decoded into a `tf.TypeSpec`."""
  return value.HasField("type_spec_value")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/builder_impl.py
# Line: 222

def _maybe_create_saver(self, saver=None):
  """Creates a sharded saver if one does not already exist."""
  if not saver:
    # Initialize a saver to generate a sharded output for all saveables in the
    # current scope.
    saver = tf_saver.Saver(
        variables._all_saveable_objects(),  # pylint: disable=protected-access
        sharded=True,
        write_version=saver_pb2.SaverDef.V2,
        allow_empty=True)
  return saver


# ==================================================
# Line: 511

def _maybe_add_main_op(self, main_op):
  """Adds main op to the SavedModel.

  Args:
    main_op: Main op to run as part of graph initialization. If None, no main
      op will be added to the graph.

  Raises:
    TypeError: If the main op is provided but is not of type `Operation`.
    ValueError: if the Graph already contains an init op.
  """
  if main_op is None:
    return

  if not isinstance(main_op, ops.Operation):
    raise TypeError(f"Expected {main_op} to be an Operation but got type "
                    f"{type(main_op)} instead.")

  # Validate that no other init ops have been added to this graph already.
  # We check main_op and legacy_init_op for thoroughness and explicitness.
  for init_op_key in (constants.MAIN_OP_KEY, constants.LEGACY_INIT_OP_KEY):
    if ops.get_collection(init_op_key):
      raise ValueError(
          "Graph already contains one or more main ops under the "
          f"collection {init_op_key}.")

  ops.add_to_collection(constants.MAIN_OP_KEY, main_op)


# ==================================================
# Line: 539

def _add_train_op(self, train_op):
  """Add train op to the SavedModel.

  Note that this functionality is in development, and liable to be
  moved elsewhere.

  Args:
    train_op: Op or group of ops that are used for training. These are stored
      as a collection with key TRAIN_OP_KEY, but not executed.

  Raises:
    TypeError if Train op is not of type `Operation`.
  """
  if train_op is not None:
    if (not isinstance(train_op, tensor.Tensor) and
        not isinstance(train_op, ops.Operation)):
      raise TypeError(f"`train_op` {train_op} needs to be a Tensor or Op.")
    ops.add_to_collection(constants.TRAIN_OP_KEY, train_op)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/saved_model_test.py
# Line: 61

def _get_export_dir(self, label):
  return os.path.join(test.get_temp_dir(), label)


# ==================================================
# Line: 69

def _build_asset_collection(self, asset_file_name, asset_file_contents,
                            asset_file_tensor_name, asset_subdir=""):
  parent_dir = os.path.join(
      compat.as_bytes(test.get_temp_dir()), compat.as_bytes(asset_subdir))
  file_io.recursive_create_dir(parent_dir)
  asset_filepath = os.path.join(
      compat.as_bytes(parent_dir), compat.as_bytes(asset_file_name))
  file_io.write_string_to_file(asset_filepath, asset_file_contents)
  asset_file_tensor = constant_op.constant(
      asset_filepath, name=asset_file_tensor_name)
  ops.add_to_collection(ops.GraphKeys.ASSET_FILEPATHS, asset_file_tensor)
  asset_collection = ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS)
  return asset_collection


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
# Occurrences: Lines 49-54 (2 instances)

def _create_model_with_function(self):
  root = autotrackable.AutoTrackable()
  root.f = def_function.function(lambda x: 2. * x)
  return root


# ==================================================
# Line: 61

def _create_model_with_data(self):
  root = autotrackable.AutoTrackable()
  root.x = constant_op.constant(1.0, dtype=dtypes.float32)
  root.f = def_function.function(
      lambda x: root.x * x,
      input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
  return root


# ==================================================
# Line: 69

def _read_fingerprint(self, filename):
  fingerprint_def = fingerprint_pb2.FingerprintDef()
  with file_io.FileIO(filename, "rb") as f:
    fingerprint_def.ParseFromString(f.read())
  return fingerprint_def


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/model_utils/mode_keys.py
# Line: 89

def _get_internal_key(self, key):
  """Return keys used for the internal dictionary."""
  if is_train(key):
    return KerasModeKeys.TRAIN
  if is_eval(key):
    return KerasModeKeys.TEST
  if is_predict(key):
    return KerasModeKeys.PREDICT
  raise ValueError('Invalid mode key: {}.'.format(key))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
# Line: 205

def test_predict_outputs_valid(self):
  """Tests that no errors are raised when provided outputs are valid."""
  outputs = {
      'output0': constant_op.constant([0]),
      u'output1': constant_op.constant(['foo']),
  }
  export_output_lib.PredictOutput(outputs)

  # Single Tensor is OK too
  export_output_lib.PredictOutput(constant_op.constant([0]))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
# Occurrences: Lines 28-33 (2 instances)

def _get_histogram_proto(self, proto_bytes):
  histogram_proto = summary_pb2.HistogramProto()
  histogram_proto.ParseFromString(proto_bytes)
  return histogram_proto


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/tf_should_use_test.py
# Line: 74

def _testAddShouldUseWarningWhenUsed(self, fn, name):
  c = constant_op.constant(0, name=name)
  with reroute_error() as error:
    h = tf_should_use._add_should_use_warning(c, warn_in_eager=True)
    fn(h)
    del h
  error.assert_not_called()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/nest_test.py
# Line: 675

def testDataclassListToTuple(self):
  mt = MaskedTensor(mask=True, value=constant_op.constant([1]))
  nmt = NestedMaskedTensor.nested_masked_tensor_with_opposite_masks(
      mask=True, inner_value=constant_op.constant([2])
  )
  input_sequence = [mt, (nmt, {"a": [mt, nmt, (mt,)]}, None, nmt, [[[mt]]])]

  mt2 = MaskedTensor(mask=True, value=constant_op.constant([3]))
  nmt2 = NestedMaskedTensor.nested_masked_tensor_with_opposite_masks(
      mask=False, inner_value=constant_op.constant([2])
  )
  results = nest.list_to_tuple(input_sequence)
  expected = (
      mt2,
      (nmt2, {"a": (mt2, nmt2, (mt2,))}, None, nmt2, (((mt2,),),)),
  )
  nest.assert_same_structure(results, expected)


# ==================================================
# Line: 1052

def testHeterogeneousComparison(self):
  nest.assert_same_structure({"a": 4}, _CustomMapping(a=3))
  nest.assert_same_structure(_CustomMapping(b=3), {"b": 4})


# ==================================================
# Line: 1844

def testListToTuple(self):
  input_sequence = [1, (2, {3: [4, 5, (6,)]}, None, 7, [[[8]]])]
  expected = (1, (2, {3: (4, 5, (6,))}, None, 7, (((8,),),)))
  nest.assert_same_structure(
      nest.list_to_tuple(input_sequence),
      expected,
  )


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/decorator_utils_test.py
# Line: 97

def test_function(self):
  decorator_utils.validate_callable(_test_function, "test")


# ==================================================
# Line: 103

def test_callable(self):

  class TestClass(object):

    def __call__(self):
      pass

  decorator_utils.validate_callable(TestClass(), "test")


# ==================================================
# Line: 112

def test_partial(self):
  partial = functools.partial(_test_function, unused_arg=7)
  decorator_utils.validate_callable(partial, "test")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/protobuf/compare_test.py
# Line: 306

def testNormalizesMaps(self):
  pb = compare_test_pb2.WithMap()
  pb.value_message[4].strings.extend(['a', 'b', 'c'])
  pb.value_string['d'] = 'e'
  compare.NormalizeNumberFields(pb)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/tf_inspect_test.py
# Line: 66

def two(self):
  return 2



# ==================================================
# Line: 806

def bound(self, a, b=2, c='Hello'):
  return (a, b, c)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/example_parser_configuration_test.py
# Line: 71

def getExpectedConfig(self, op_type):
  expected = example_parser_configuration_pb2.ExampleParserConfiguration()
  if op_type == 'ParseExampleV2':
    text_format.Parse(EXPECTED_CONFIG_V2, expected)
  else:
    text_format.Parse(EXPECTED_CONFIG_V1, expected)
  return expected


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/dispatch_test.py
# Line: 130

def _flatten_with_slice_flattening(self, x):
  flat = []
  for val in nest.flatten(x):
    if isinstance(val, slice):
      flat.extend((val.start, val.stop, val.step))
    else:
      flat.append(val)
  return flat


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
# Line: 84

  def testKwargNotInterned(self):
    func = (
        _function_parameter_canonicalizer_binding_for_test
        .FunctionParameterCanonicalizer(['long_parameter_name'], ()))
    kwargs = dict([('_'.join(['long', 'parameter', 'name']), 5)])
    func.canonicalize(**kwargs)


if __name__ == '__main__':

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/tf_decorator_test.py
# Occurrences: Lines 92-96 (2 instances)

def two_func(self):
  return 2


# ==================================================
# Line: 275

def testCompatibleWithNamelessCallables(self):

  class Callable(object):

    def __call__(self):
      pass

  callable_object = Callable()
  # Smoke test: This should not raise an exception, even though
  # `callable_object` does not have a `__name__` attribute.
  _ = tf_decorator.make_decorator(callable_object, test_wrapper)

  partial = functools.partial(test_function, x=1)
  # Smoke test: This should not raise an exception, even though `partial` does
  # not have `__name__`, `__module__`, and `__doc__` attributes.
  _ = tf_decorator.make_decorator(partial, test_wrapper)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/object_identity.py
# Line: 40

def _assert_type(self, other):
  if not isinstance(other, _ObjectIdentityWrapper):
    raise TypeError("Cannot compare wrapped object with unwrapped object")


# ==================================================
# Line: 132

def _wrap_key(self, key):
  return _ObjectIdentityWrapper(key)


# ==================================================
# Line: 211

def _wrap_key(self, key):
  return _ObjectIdentityWrapper(key)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/fast_module_type_test.py
# Occurrences: Lines 24-30 (3 instances)

def _getattribute1(self, name):  # pylint: disable=unused-argument
  return 2


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/function_utils_test.py
# Line: 53

def bar(self, a, b):
  return a + b


# ==================================================
# Line: 171

def fn(self, **x):
  del x

# ==================================================
# Line: 177

def fn(self, x):
  del x

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/vlog_test.py
# Line: 32

  def test_simple_conv(self):
    height, width = 7, 9
    images = random_ops.random_uniform((5, height, width, 3))
    w = random_ops.random_normal([5, 5, 3, 32], mean=0, stddev=1)
    nn_ops.conv2d(images, w, strides=[1, 1, 1, 1], padding="SAME")


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/tf_export.py
# Line: 328

def set_attr(
    self, func: Any, api_names_attr: str, names: Sequence[str]

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/util/deprecation_test.py
# Line: 363

def _fn(self, arg0, arg1):
  """fn doc.

  Args:
    arg0: Arg 0.
    arg1: Arg 1.

  Returns:
    Sum of args.
  """
  return arg0 + arg1


# ==================================================
# Line: 408

def _fn(self, arg0, arg1):
  """fn doc."""
  return arg0 + arg1


# ==================================================
# Line: 438

def _fn(self, arg0, arg1):
  return arg0 + arg1


# ==================================================
# Line: 457

def test_prop_wrong_order(self):
  with self.assertRaisesRegex(
      ValueError,
      "make sure @property appears before @deprecated in your source code"):
    # pylint: disable=unused-variable

    class _Object(object):

      def __init(self):
        pass

      @deprecation.deprecated("2016-07-04", "Instructions.")
      @property
      def _prop(self):
        return "prop_wrong_order"


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
# Line: 290

def _create_tuple_proto(self, num_outputs):
  shardings = [
      xla_data_pb2.OpSharding(type=xla_data_pb2.OpSharding.REPLICATED)
  ] * num_outputs
  return xla_data_pb2.OpSharding(
      type=xla_data_pb2.OpSharding.TUPLE, tuple_shardings=shardings)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py
# Line: 75

def _graph_has_xla_sharding_op(self, graph):
  for node in graph.node:
    if node.op == 'XlaSharding' and any(
        'ReadVariableOp' in input for input in node.input
    ):
      return True

  return False


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
# Occurrences: Lines 79-83 (2 instances)

def testTRTEngineInstanceAvailable(self):
  # test if we can access the TRTEngineInstance protobuf
  assert hasattr(TRTEngineInstance(), "serialized_engine")


# ==================================================
# Line: 102

def _GetShapeOpModel(self):

  class ShapeOpModel(autotrackable.AutoTrackable):

    def __init__(self):
      self.v = None

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=[None, None], dtype=dtypes.float32)
    ])
    def run(self, x):
      q = x + 1
      q_shape = array_ops.shape(q)
      # Add an OP that is not supported by TF-TRT. This allows TF-TRT to build
      # two engines. The first engine produces an int32 output and the second
      # engines has an int32 input and an int32 output.
      q = math_ops.cumsum(q_shape)
      q = q * 2
      return array_ops.identity(q, name="output")

  return ShapeOpModel()


# ==================================================
# Line: 112

def run(self, x):
  q = x + 1
  q_shape = array_ops.shape(q)
  # Add an OP that is not supported by TF-TRT. This allows TF-TRT to build
  # two engines. The first engine produces an int32 output and the second
  # engines has an int32 input and an int32 output.
  q = math_ops.cumsum(q_shape)
  q = q * 2
  return array_ops.identity(q, name="output")


# ==================================================
# Line: 142

def _GetGraphForV1(self, device):

  def _GraphFn():
    inp1 = array_ops.placeholder(
        dtype=dtypes.float32, shape=[None, 1, 1], name="input1")
    inp2 = array_ops.placeholder(
        dtype=dtypes.float32, shape=[None, 1, 1], name="input2")
    var = variables.Variable([[[1.0]]], dtype=dtypes.float32, name="v1")
    out = TrtConvertTest._GetGraph(inp1, inp2, var)
    return g, var, inp1, inp2, out

  g = ops.Graph()
  with g.as_default():
    if device:
      with g.device(device):
        return _GraphFn()
    return _GraphFn()


# ==================================================
# Line: 259

def _MayRemoveGraphSequenceNumber(self, name):
  prefix = re.search(r"TRTEngineOp_\d{3,}_", name)
  if prefix and name.startswith(prefix.group(0)):
    parts = name.split("_", maxsplit=2)
    assert len(parts) == 3
    return parts[0] + "_" + parts[2]
  return name


# ==================================================
# Line: 268

def _GetUniqueTRTEngineOp(self, graph_def):
  trt_engine_nodes = [
      node for node in graph_def.node if node.op == "TRTEngineOp"
  ]
  assert len(trt_engine_nodes) == 1
  return trt_engine_nodes[0]


# ==================================================
# Line: 397

def _CreateConverterV2(
    self,
    input_saved_model_dir,
    input_saved_model_signature_key=_SAVED_MODEL_SIGNATURE_KEY,
    max_workspace_size_bytes=10 << 20,  # Use a smaller workspace.
    precision_mode=trt_convert.TrtPrecisionMode.FP32,
    maximum_cached_engines=2,
    allow_build_at_runtime=True):
  return trt_convert.TrtGraphConverterV2(
      input_saved_model_dir=input_saved_model_dir,
      input_saved_model_signature_key=input_saved_model_signature_key,
      max_workspace_size_bytes=max_workspace_size_bytes,
      precision_mode=precision_mode,
      maximum_cached_engines=maximum_cached_engines,
      allow_build_at_runtime=allow_build_at_runtime)


# ==================================================
# Occurrences: Lines 429-434 (2 instances)

def _RandomInput(self, shape, dtype=np.float32):
  inp1 = np.random.random_sample(shape).astype(dtype)
  inp2 = np.random.random_sample(shape).astype(dtype)
  return inp1, inp2


# ==================================================
# Line: 851

def run(self):
  return array_ops.constant(1.0)


# ==================================================
# Line: 864

def run(self, inp):
  return inp + inp * inp


# ==================================================
# Line: 878

def run(self, inp1, inp2):
  return inp1 + inp2 * inp2


# ==================================================
# Line: 889

def run(self):
  return {"my_output": array_ops.constant(1.0)}


# ==================================================
# Line: 902

def run(self, inp):
  # Here the keys are not ordered lexicographically on purpose.
  return {
      "output_b": array_ops.constant(1.0),
      "output_a": inp + inp * inp
  }


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
# Line: 582

def _collections_to_keep(self, collection_keys):
  # TODO(laigd): currently we use the collection key to filter out
  # collections that depend on variable ops, but this may miss some
  # other user-defined collections. A better way would be to use
  # CollectionDef::NodeList for the filtering.
  collections_to_remove = (
      ops.GraphKeys._VARIABLE_COLLECTIONS + [
          ops.GraphKeys.TRAIN_OP, ops.GraphKeys.WHILE_CONTEXT,
          ops.GraphKeys.COND_CONTEXT
      ])
  return [key for key in collection_keys if key not in collections_to_remove]


# ==================================================
# Line: 1180

def _verify_profile_strategy(self, strategy):
  supported_strategies = [s.lower() for s in supported_profile_strategies()]
  if strategy.lower() not in supported_strategies:
    raise ValueError(
        ("profile_strategy '{}' is not supported. It should be one of {}"
        ).format(strategy, supported_profile_strategies()))
  if strategy == "ImplicitBatchModeCompatible":
    logging.warn(
        "ImplicitBatchModeCompatible strategy is deprecated, and"
        " using it may result in errors during engine building. Please"
        " consider using a different profile strategy.")


# ==================================================
# Line: 1335

def _for_each_trt_node(self, graph_def, fn):
  """Helper method to manipulate all TRTEngineOps in a GraphDef."""
  for node in graph_def.node:
    if node.op == _TRT_ENGINE_OP_NAME:
      fn(node)
  for func in graph_def.library.function:
    for node in func.node_def:
      if node.op == _TRT_ENGINE_OP_NAME:
        fn(node)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/collective_ops_multi_worker_test.py
# Line: 65

def testCheckHealth(self):

  def worker_fn():
    enable_collective_ops(cluster_resolver_lib.TFConfigClusterResolver())
    # There may be some delays before the server startup. Check health should
    # eventually be OK.
    while True:
      try:
        for task in [
            "/job:worker/replica:0/task:0",
            "/job:worker/replica:0/task:1",
        ]:
          context.context().check_collective_ops_peer_health(
              task, timeout_in_ms=1000)
      except (errors.UnavailableError, errors.DeadlineExceededError):
        continue
      break
    multi_process_runner.get_barrier().wait()

  cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
  mpr = multi_process_runner.MultiProcessRunner(worker_fn, cluster_spec)
  mpr.start()
  mpr.join()


# ==================================================
# Line: 103

def testCheckHealthPeerRestart(self):

  def worker_fn():
    cluster_resolver = cluster_resolver_lib.TFConfigClusterResolver()
    enable_collective_ops(cluster_resolver)

    collective_ops.all_reduce(
        constant_op.constant(1.),
        group_size=2,
        group_key=100,
        instance_key=100,
        merge_op="Add",
        final_op="Id",
        communication_hint="ring")

    if cluster_resolver.task_type == "worker":
      # MultiProcessRunner will auto restart worker-0.
      os._exit(1)  # pylint: disable=protected-access
    else:
      # chief should eventually gets FailedPreconditionError after worker-0
      # has restarted.
      while True:
        time.sleep(1)
        try:
          context.context().check_collective_ops_peer_health(
              "/job:worker/replica:0/task:0", timeout_in_ms=1000)
        except errors.UnavailableError:
          pass
        except errors.FailedPreconditionError:
          break

  cluster_spec = multi_worker_test_base.create_cluster_spec(
      has_chief=True, num_workers=1)
  mpr = multi_process_runner.MultiProcessRunner(
      worker_fn, cluster_spec, auto_restart=True)
  mpr.start()
  mpr.join()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
# Line: 105

def testEagerNoMemoryLeaked(self):
  # This is a somewhat convoluted way of testing that nothing gets added to
  # a global collection.
  predictions = constant_op.constant([4, 8, 12, 8, 1, 3], shape=(2, 3))
  labels = constant_op.constant([1, 9, 2, -5, -2, 6], shape=(2, 3))
  losses.absolute_difference(labels, predictions)



# ==================================================
# Line: 248

def testEagerNoMemoryLeaked(self):
  logits = constant_op.constant([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0],
                                 [0.0, 0.0, 10.0]])
  labels = constant_op.constant([[0], [1], [2]], dtype=dtypes.int32)
  losses.sparse_softmax_cross_entropy(labels, logits)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
# Line: 202

def _DtypesToTest(self, use_gpu):
  if test_util.IsMklEnabled():
    return [dtypes.float32]

  if use_gpu:
    # It is important that float32 comes first, since we are using its
    # gradients as a reference for fp16 gradients.
    out = [dtypes.float32, dtypes.bfloat16]
    if test_util.GpuSupportsHalfMatMulAndConv():
      out.append(dtypes.float16)
    if not test.is_built_with_rocm():
      out.extend([dtypes.float64])
    return out

  return [dtypes.float32, dtypes.float64, dtypes.float16, dtypes.bfloat16]


# ==================================================
# Line: 218

def _CreateNumpyTensor(self, shape):
  total_size = 1
  for s in shape:
    total_size *= s
  return np.arange(1, total_size + 1, dtype=np.float32).reshape(shape)


# ==================================================
# Line: 3299

def _InitValues(self, sizes):
  """Initializes values for input tensors.

  Args:
    sizes: Tensor dimensions.

  Returns:
    Tensor initialized to values.
  """
  total_size = 1
  for s in sizes:
    total_size *= s
  x = [f * 0.5 for f in range(1, total_size + 1)]
  return constant_op.constant(x, shape=sizes)


# ==================================================
# Occurrences: Lines 3818-3822 (2 instances)

def _CreateNumpyTensor(self, shape):
  total_size = np.prod(shape)
  return np.arange(1, total_size + 1, dtype=np.float32).reshape(shape)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
# Line: 39

def _AvgPoolAlongRows(self, input_matrix, row_seq, overlapping):
  """Perform average pool along row of a 2-D matrix based on row_seq.

  Args:
    input_matrix: A 2-D matrix.
    row_seq: Cumulative pooling sequence along row.
    overlapping: Whether or not use overlapping when pooling.

  Returns:
    A 2-D matrix, with
      * num_rows = len(row_seq)-1
      * num_cols = input_matrix.num_cols.
  """
  output_image = np.zeros(input_matrix.shape[1])
  row_max = row_seq[-1]
  for i in range(row_seq.shape[0] - 1):
    row_start = row_seq[i]
    row_end = row_seq[i + 1] + 1 if overlapping else row_seq[i + 1]
    row_end = min(row_end, row_max)
    output_image = np.vstack((output_image, np.mean(
        input_matrix[row_start:row_end, :], axis=0)))  # axis 0 is along row
  # remove the sentinel row
  return output_image[1:, :]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
# Line: 315

def _CreateNumpyTensor(self, sizes):
  return np.asarray([f * 1.0 for f in range(1,
                                            np.prod(sizes) + 1)],
                    dtype=np.float32).reshape(sizes)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_d9m_test.py
# Line: 36

def _genParams(self,
               use_cudnn=False,
               data_format="NHWC",
               dtype=dtypes.float32,
               seed=123):
  random_seed.set_seed(seed)
  batch_size = 2  # no interaction over batch, so make small
  if use_cudnn:
    # When op-determinism is not enabled, one input channel, plus a
    # cuDNN-supported filter size and number of output channels will result
    # in cuDNN being used for both backprop-to-input and backprop-to-filter on
    # cuDNN 7.6.3 and higher. When op-determnism is enabled, cuDNN is always
    # used for backprop-to-filter.
    input_channels = 1
  else:
    input_channels = 2  # no interaction over channels, so make small
  input_height = 500
  input_width = 1000
  if data_format == "NHWC":
    input_shape = (batch_size, input_height, input_width, input_channels)
  else:  # "NCHW"
    input_shape = (batch_size, input_channels, input_height, input_width)
  input_data = random_ops.random_normal(input_shape, dtype=dtype)
  # The following filter size results in nondeterminism being exercised in
  # cuDNN backprop (when determinism is not enabled) to both input and filter
  # as well as in the specialized (non-cuDNN) depthwise backprop to filter.
  filter_height = 7
  filter_width = 7
  channel_multiplier = 10
  filter_shape = (filter_height, filter_width, input_channels,
                  channel_multiplier)
  filter_data = random_ops.random_normal(filter_shape, dtype=dtype)
  strides = [1, 1, 1, 1]
  padding = "SAME"
  output_height = input_height  # because same padding
  output_width = input_width  # because same padding
  output_channels = input_channels * channel_multiplier
  if data_format == "NHWC":
    output_shape = (batch_size, output_height, output_width, output_channels)
  else:  # "NCHW"
    output_shape = (batch_size, output_channels, output_height, output_width)
  return input_data, filter_data, strides, padding, output_shape


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
# Line: 71

def _random_data_op(self, shape):
  # np.random.random_sample can properly interpret either tf.TensorShape or
  # namedtuple as a list.
  return constant_op.constant(
      2 * np.random.random_sample(shape) - 1, dtype=dtypes.float32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
# Line: 34

def _npSoftmax(self, features, dim=-1, log=False):
  if dim == -1:
    dim = len(features.shape) - 1
  one_only_on_dim = list(features.shape)
  one_only_on_dim[dim] = 1
  is_fp16 = features.dtype == np.float16
  if is_fp16:
    # Do the compute in fp32 and cast the input back to fp32.
    features = features.astype(np.float32)
  e = np.exp(features - np.reshape(
      np.amax(
          features, axis=dim), one_only_on_dim))
  softmax = e / np.reshape(np.sum(e, axis=dim), one_only_on_dim)
  if log:
    res = np.log(softmax)
  else:
    res = softmax
  if is_fp16:
    res = res.astype(np.float16)
  return res


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
# Line: 945

def testDynamicRNNAllowsUnknownTimeDimension(self):
  inputs = array_ops.placeholder(dtypes.float32, shape=[1, None, 20])
  cell = rnn_cell.GRUCell(30)
  # Smoke test, this should not raise an error
  rnn.dynamic_rnn(cell, inputs, dtype=dtypes.float32)


# ==================================================
# Line: 2568

def _retrieve_cpu_gpu_stats(self, run_metadata):
  cpu_stats = None
  gpu_stats = None
  step_stats = run_metadata.step_stats
  for ds in step_stats.dev_stats:
    if "cpu:0" in ds.device[-5:].lower():
      cpu_stats = ds.node_stats
    if "gpu:0" == ds.device[-5:].lower():
      gpu_stats = ds.node_stats
  return cpu_stats, gpu_stats


# ==================================================
# Line: 3027

def _retrieve_cpu_gpu_stats(self, run_metadata):
  cpu_stats = None
  gpu_stats = None
  step_stats = run_metadata.step_stats
  for ds in step_stats.dev_stats:
    if "cpu:0" in ds.device[-5:].lower():
      cpu_stats = ds.node_stats
    if "gpu:0" == ds.device[-5:].lower():
      gpu_stats = ds.node_stats
  return cpu_stats, gpu_stats


# ==================================================
# Line: 3288

def zero_state(self, batch_size=None, dtype=None):
  return "wrapped_cell_zero_state"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
# Line: 59

def call(self, input_, state, scope=None):
  return (input_ + 1, state + 1)



# ==================================================
# Occurrences: Lines 74-77 (2 instances)

def zero_state(self, batch_size, dtype):
  return array_ops.zeros([], dtype=dtypes.int32)


# ==================================================
# Occurrences: Lines 92-95 (2 instances)

def zero_state(self, batch_size, dtype):
  return array_ops.zeros([], dtype=dtypes.int32)


# ==================================================
# Occurrences: Lines 111-116 (2 instances)

def zero_state(self, batch_size, dtype):
  return (array_ops.zeros([], dtype=dtypes.int32),
          tensor_array_ops.TensorArray(
              dtype=dtype, size=0, dynamic_size=True))


# ==================================================
# Line: 244

def testEagerMemory(self):
  with context.eager_mode():
    cell = TensorArrayStateRNNCell()
    inputs = np.array([[[1], [2], [3], [4]]], dtype=np.float32)
    rnn.dynamic_rnn(cell, inputs, dtype=dtypes.float32, sequence_length=[4])


# ==================================================
# Line: 828

  def _benchmarkDynamicLSTMMemorySwapLongSeq(self):
    """The memory swapping test for the SOSP submission."""
    print("Calculation: Long LSTM Sequence")
    print("batch \t len \t units \t dynamic \t elapsed_t \t elapsed_t/len")
    batch_size = 512
    seqlen = 800
    num_units = 512
    dynamic = True
    swap_memory = True
    # Some warming up.
    if swap_memory:
      rnn_long_sequence_benchmark(batch_size, seqlen, num_units,
                                  dynamic, swap_memory, 2)
    # Measure the performance.
    for slen in range(100, 1100, 100):
      rnn_long_sequence_benchmark(batch_size, slen, num_units, dynamic,
                                  swap_memory, 3)

if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
# Line: 533

def testConstructionNonSharded(self):
  with ops.Graph().as_default():
    p = variables.Variable(
        array_ops.zeros(shape=[100, 100], dtype=dtypes.float32))
    ids = constant_op.constant([0, 1, 1, 7], dtype=dtypes.int32)
    embedding_ops.embedding_lookup([p], ids)


# ==================================================
# Line: 540

def testConstructionSharded(self):
  with ops.Graph().as_default():
    p = []
    for _ in range(2):
      p += [
          variables.Variable(
              array_ops.zeros(shape=[100, 100], dtype=dtypes.float32))
      ]
      ids = constant_op.constant([0, 1, 1, 17], dtype=dtypes.int32)
    embedding_ops.embedding_lookup(p, ids)


# ==================================================
# Line: 659

def _RandomIdsAndWeights(self, batch_size, vocab_size, ragged=False):
  max_val_per_entry = 6
  vals_per_batch_entry = np.random.randint(
      1, max_val_per_entry, size=batch_size)
  num_vals = np.sum(vals_per_batch_entry)

  ids = np.random.randint(vocab_size, size=num_vals)
  weights = 1 + np.random.rand(num_vals)

  indices = []
  for batch_entry, num_val in enumerate(vals_per_batch_entry):
    for val_index in range(num_val):
      indices.append([batch_entry, val_index])

  shape = [batch_size, max_val_per_entry]

  sp_ids = sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64),
      constant_op.constant(ids, dtypes.int32),
      constant_op.constant(shape, dtypes.int64))
  sp_weights = sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64),
      constant_op.constant(weights, dtypes.float32),
      constant_op.constant(shape, dtypes.int64))

  if ragged:
    sp_ids = ragged_tensor.RaggedTensor.from_sparse(sp_ids)
    sp_weights = ragged_tensor.RaggedTensor.from_sparse(sp_weights)

  return sp_ids, sp_weights, ids, weights, vals_per_batch_entry


# ==================================================
# Line: 690

def _GroupByBatchEntry(self, vals, vals_per_batch_entry):
  grouped_vals = []
  index = 0
  for num_val in vals_per_batch_entry:
    grouped_vals.append(list(vals[index:(index + num_val)]))
    index += num_val
  return grouped_vals


# ==================================================
# Line: 916

def _SortByKey(self, keys, vals):
  perm = sort_ops.argsort(keys)
  return array_ops.gather(keys, perm), array_ops.gather(vals, perm)


# ==================================================
# Line: 1035

def _ids_and_weights_2d(self, ragged):
  # Each row demonstrates a test case:
  #   Row 0: multiple valid ids, 1 invalid id, weighted mean
  #   Row 1: all ids are invalid (leaving no valid ids after pruning)
  #   Row 2: no ids to begin with
  #   Row 3: single id
  #   Row 4: all ids have <=0 weight
  indices = [[0, 0], [0, 1], [0, 2], [1, 0], [3, 0], [4, 0], [4, 1]]
  ids = [0, 1, -1, -1, 2, 0, 1]
  weights = [1.0, 2.0, 1.0, 1.0, 3.0, 0.0, -0.5]
  shape = [5, 4]

  sparse_ids = sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64),
      constant_op.constant(ids, dtypes.int64),
      constant_op.constant(shape, dtypes.int64))

  sparse_weights = sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64),
      constant_op.constant(weights, dtypes.float32),
      constant_op.constant(shape, dtypes.int64))

  if ragged:
    sparse_ids = ragged_tensor.RaggedTensor.from_sparse(sparse_ids)
    sparse_weights = ragged_tensor.RaggedTensor.from_sparse(sparse_weights)

  return sparse_ids, sparse_weights


# ==================================================
# Line: 1063

def _ids_and_weights_3d(self):
  # Each (2-D) index demonstrates a test case:
  #   Index 0, 0: multiple valid ids, 1 invalid id, weighted mean
  #   Index 0, 1: all ids are invalid (leaving no valid ids after pruning)
  #   Index 0, 2: no ids to begin with
  #   Index 1, 0: single id
  #   Index 1, 1: all ids have <=0 weight
  #   Index 1, 2: no ids to begin with
  indices = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [1, 0, 0], [1, 1, 0],
             [1, 1, 1]]
  ids = [0, 1, -1, -1, 2, 0, 1]
  weights = [1.0, 2.0, 1.0, 1.0, 3.0, 0.0, -0.5]
  shape = [2, 3, 4]

  sparse_ids = sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64),
      constant_op.constant(ids, dtypes.int64),
      constant_op.constant(shape, dtypes.int64))

  sparse_weights = sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64),
      constant_op.constant(weights, dtypes.float32),
      constant_op.constant(shape, dtypes.int64))

  return sparse_ids, sparse_weights


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_d9m_test.py
# Line: 37

def _makeShapeTuple(self, batch_size, channel_count, data_rank, data_dim,
                    data_layout):
  data_dims = data_rank * (data_dim,)
  if data_layout == 'channels_first':
    shape = (batch_size,) + (channel_count,) + data_dims
  elif data_layout == 'channels_last':
    shape = (batch_size,) + data_dims + (channel_count,)
  else:
    raise ValueError('Unknown data format')
  return shape


# ==================================================
# Line: 48

def _dataFormatFromDataLayout(self, data_layout=None):
  if data_layout == 'channels_first':
    return 'NCHW'
  elif data_layout == 'channels_last':
    return 'NHWC'
  else:
    raise ValueError('Unknown data_layout')


# ==================================================
# Line: 56

def _randomNDArray(self, shape):
  return 2 * np.random.random_sample(shape) - 1


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
# Line: 42

def _npRelu(self, np_features):
  return np.maximum(np_features, np.zeros(np_features.shape))


# ==================================================
# Line: 213

def _npRelu6(self, np_features):
  sixes = np.copy(np_features)
  sixes.fill(6.0)
  return np.minimum(
      np.maximum(np_features, np.zeros(np_features.shape)), sixes)


# ==================================================
# Line: 285

def _npLeakyRelu(self, np_features, alpha=0.1):
  return np.maximum(np_features, alpha * np_features)


# ==================================================
# Line: 419

def _npElu(self, np_features):
  return np.where(np_features < 0, np.exp(np_features) - 1, np_features)


# ==================================================
# Line: 531

def _npSelu(self, np_features):
  scale = 1.0507009873554804934193349852946
  scale_alpha = 1.7580993408473768599402175208123
  return np.where(np_features < 0, scale_alpha * (np.exp(np_features) - 1),
                  scale * np_features)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# Line: 187

def _isMaxPool(self, func):
  return func in (nn_ops.max_pool, nn_ops.max_pool_v2)


# ==================================================
# Line: 1599

def _MaxPoolGrad(self, orig_input, orig_output, grad, window_rows,
                 window_cols, row_stride, col_stride, padding, v2):
  """Max Pooling Gradient.

  Args:
    orig_input: A float Tensor. The original input tensor.
    orig_output: A float Tensor. The original output tensor.
    grad: A float Tensor.
      The 4D (batch x rows x cols x depth) output backprop.
    window_rows: integer. Kernel size along rows dimension.
    window_cols: integer. Kernel size along cols dimension.
    row_stride: integer. Stride along rows dimension
    col_stride: integer. Stride along cols dimension
    padding: PoolingOpDef.Padding.  Padding type.

  Returns:
    A Tensor.
  """
  pool_func = gen_nn_ops.max_pool_grad_v2 if v2 else gen_nn_ops.max_pool_grad
  if v2:
    return pool_func(orig_input, orig_output, grad,
                     [1, window_rows, window_cols, 1],
                     [1, row_stride, col_stride, 1], padding)
  else:
    padding, explicit_paddings = nn_ops.convert_padding(padding)
    return pool_func(orig_input, orig_output, grad,
                     [1, window_rows, window_cols, 1],
                     [1, row_stride, col_stride, 1], padding,
                     explicit_paddings)


# ==================================================
# Line: 2185

def _MaxPoolGradGrad(self, orig_input, orig_output, grad, window_rows,
                     window_cols, row_stride, col_stride, padding):
  """Max Pooling Second-Order Gradient.

  Args:
    orig_input: A float Tensor. The original input tensor.
    orig_output: A float Tensor. The original output tensor.
    grad: A float Tensor.
      The 4D (batch x out_rows x out_cols x depth) output backprop.
    window_rows: integer. Kernel size along rows dimension.
    window_cols: integer. Kernel size along cols dimension.
    row_stride: integer. Stride along rows dimension
    col_stride: integer. Stride along cols dimension
    padding: PoolingOpDef.Padding.  Padding type.

  Returns:
    A Tensor.
  """
  return gen_nn_ops.max_pool_grad_grad(
      orig_input, orig_output, grad, [1, window_rows, window_cols, 1],
      [1, row_stride, col_stride, 1], padding)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
# Line: 38

def _npBias(self, inputs, bias):
  assert len(bias.shape) == 1
  assert inputs.shape[-1] == bias.shape[0]
  return inputs + bias.reshape(([1] *
                                (len(inputs.shape) - 1)) + [bias.shape[0]])


# ==================================================
# Line: 56

def _AtLeast3d(self, np_value):
  # fill the input value to at least 3-dimension
  if np_value.ndim < 3:
    return np.reshape(np_value, (1,) * (3 - np_value.ndim) + np_value.shape)
  return np_value


# ==================================================
# Line: 70

def _NCHWToNHWC(self, np_value):
  assert len(np_value.shape) >= 3
  np_dim = list(range(np_value.ndim))
  # move the second dimension to the last
  np_dim_new = list(np_dim[0:1]) + list(np_dim[2:]) + list(np_dim[1:2])
  return np.transpose(np_value, np_dim_new)


# ==================================================
# Line: 93

def _expectedException(self):
  if context.executing_eagerly():
    return errors_impl.InvalidArgumentError
  else:
    return ValueError


# ==================================================
# Line: 151

def _random_tensor(self, shape, dtype):
  return constant_op.constant(2 * np.random.rand(*shape) - 1, dtype=dtype)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
# Line: 37

def _opFwdBwd(self, labels, logits, axis=-1):
  """ Runs the op-under-test both forwards and backwards."""
  logits = ops.convert_to_tensor(logits)  # needed for the gradient tape
  with backprop.GradientTape() as tape:
    tape.watch(logits)
    loss = nn_ops.softmax_cross_entropy_with_logits(
        labels=labels, logits=logits, dim=axis)
  return loss, tape.gradient(loss, logits)


# ==================================================
# Line: 46

def _npXent(self, labels, logits, dim=-1):
  if dim == -1:
    dim = len(logits.shape) - 1
  one_only_on_dim = list(logits.shape)
  one_only_on_dim[dim] = 1
  e = np.exp(logits - np.reshape(np.amax(logits, axis=dim), one_only_on_dim))
  probs = e / np.reshape(np.sum(e, axis=dim), one_only_on_dim)
  bp = (probs - labels)
  l = -np.sum(labels * np.log(probs + 1.0e-20), axis=dim)
  return l, bp


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/softsign_op_test.py
# Line: 30

def _npSoftsign(self, np_features):
  return np_features / (1 + np.abs(np_features))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
# Line: 39

def _MaxPoolAlongRows(self, input_matrix, row_seq, overlapping):
  """Perform max pool along row of a 2-D matrix based on row_seq.

  Args:
    input_matrix: A 2-D matrix.
    row_seq: Cumulative pooling sequence along row.
    overlapping: Whether or not use overlapping when pooling.

  Returns:
    A 2-D matrix, with
      * num_rows = len(row_seq)-1
      * num_cols = input_matrix.num_cols.
  """
  output_image = np.zeros(input_matrix.shape[1])
  row_max = row_seq[-1]
  for i in range(row_seq.shape[0] - 1):
    row_start = row_seq[i]
    row_end = row_seq[i + 1] + 1 if overlapping else row_seq[i + 1]
    row_end = min(row_end, row_max)
    output_image = np.vstack((output_image, np.amax(
        input_matrix[row_start:row_end, :], axis=0)))  # axis 0 is along row
  # remove the sentinel row
  return output_image[1:, :]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
# Line: 637

def testCtcLossDenseWithUndefinedStaticDimensions(self, unique, blank_index):
  random_seed.set_random_seed(5)

  # Trace without a batch size and number of frames
  batch_size = None
  num_labels = 6
  label_length = 5
  num_frames = None

  @def_function.function
  def func(labels, logits, label_lengths, logit_lengths):
    unique_labels = ctc_ops.ctc_unique_labels(labels) if unique else None
    return ctc_ops.ctc_loss_dense(
        labels=labels,
        logits=logits,
        label_length=label_lengths,
        logit_length=logit_lengths,
        unique=unique_labels,
        blank_index=blank_index)

  labels_spec = tensor_spec.TensorSpec([batch_size, label_length],
                                       dtypes.int64)
  logits_spec = tensor_spec.TensorSpec([num_frames, batch_size, num_labels],
                                       dtypes.float32)
  label_lengths_spec = tensor_spec.TensorSpec([batch_size], dtypes.int64)
  logit_lengths_spec = tensor_spec.TensorSpec([batch_size], dtypes.int64)

  f = func.get_concrete_function(
      labels_spec, logits_spec, label_lengths_spec, logit_lengths_spec)

  # Execute with a defined batch size and number of frames
  batch_size = 8
  num_frames = 12

  logits = random_ops.random_uniform([num_frames, batch_size, num_labels])
  labels = random_ops.random_uniform(
      [batch_size, label_length], minval=1, maxval=num_labels,
      dtype=dtypes.int64)

  label_lengths = random_ops.random_uniform(
      [batch_size], minval=2, maxval=label_length, dtype=dtypes.int64)
  label_mask = array_ops.sequence_mask(
      label_lengths, maxlen=label_length, dtype=label_lengths.dtype)
  labels *= label_mask

  logit_lengths = constant_op.constant(
      [num_frames] * batch_size, dtype=dtypes.int64)

  f(labels, logits, label_lengths, logit_lengths)


# ==================================================
# Line: 1166

def _randomFloats(self, shape):
  x = (2 * np.random.random_sample(shape) - 1)
  return constant_op.constant(x, dtype=dtypes.float32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv3d_transpose_test.py
# Line: 119

def testConv3DTransposeShapeMismatch(self):
  # Test case for GitHub issue 18460
  x_shape = [2, 2, 3, 4, 3]
  f_shape = [3, 3, 3, 2, 2]
  y_shape = [2, 2, 6, 8, 6]
  strides = [1, 1, 2, 2, 2]
  np.random.seed(1)
  x_value = np.random.random_sample(x_shape).astype(np.float64)
  f_value = np.random.random_sample(f_shape).astype(np.float64)
  nn_ops.conv3d_transpose(
      x_value, f_value, y_shape, strides, data_format="NCDHW")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
# Line: 74

def _randomFloats(self, shape, dtype, normalized_rows=False):
  a = (2 * np.random.random_sample(shape) - 1).astype(dtype)

  if normalized_rows:

    def normalize(row):
      return row / row.sum()

    a = np.apply_along_axis(normalize, 1, a)

  return constant_op.constant(a)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/softplus_op_test.py
# Line: 31

def _npSoftplus(self, np_features):
  np_features = np.asarray(np_features)
  zero = np.asarray(0).astype(np_features.dtype)
  return np.logaddexp(zero, np_features)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/nn_ops/lrn_op_test.py
# Line: 36

def _LRN(self, input_image, lrn_depth_radius=5, bias=1.0, alpha=1.0,
         beta=0.5):
  """Compute expected result."""
  output = copy.deepcopy(input_image)
  batch_size = input_image.shape[0]
  rows = input_image.shape[1]
  cols = input_image.shape[2]
  depth = input_image.shape[3]
  for b in range(batch_size):
    for r in range(rows):
      for c in range(cols):
        for d in range(depth):
          begin = max(0, d - lrn_depth_radius)
          end = min(depth, d + lrn_depth_radius + 1)
          patch = input_image[b, r, c, begin:end]
          output[b, r, c, d] /= (
              np.power(bias + alpha * np.sum(patch * patch), beta))
  return output


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test_big.py
# Occurrences: Lines 36-45 (4 instances)

def _tf_reduce_max(self, x, reduction_axes, keepdims):
  return math_ops.reduce_max(x, reduction_axes, keepdims)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
# Line: 162

def _inv(self, x):
  return 1.0 / x


# ==================================================
# Line: 168

def _sigmoid(self, x):
  return 1.0 / (1.0 + np.exp(-x))


# ==================================================
# Line: 174

def _replace_domain_error_with_inf(self, fn):

  def func(x):
    try:
      return fn(x)
    except ValueError as e:
      if "domain error" in str(e):
        return np.inf * np.ones_like(x)
      else:
        raise e

  return func


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Line: 39

def _input(self, input_shape, dtype=dtypes_lib.int32):
  num_elem = 1
  for x in input_shape:
    num_elem *= x
  values = np.arange(1, num_elem + 1)
  np_values = values.reshape(input_shape).astype(dtype.as_numpy_dtype)
  if dtype == dtypes_lib.bfloat16:
    # Large numbers from arange lead to high absolute diff with bfloat16, so
    # scale down.
    np_values *= np.array(0.00001, dtype=dtype.as_numpy_dtype)
  # Add a non-zero imaginary component to complex types.
  if dtype.is_complex:
    np_values -= 1j * np_values
  return constant_op.constant(
      np_values, shape=input_shape, dtype=dtype), np_values


# ==================================================
# Line: 55

def _segmentReduce(
    self,
    indices,
    x,
    op1,
    op2=None,
    num_segments=None,
    initial_value=0,
    empty_value=0,

# ==================================================
# Occurrences: Lines 89-95 (3 instances)

def _mean_cum_op(self, x, y):
  return (x[0] + y, x[1] + 1) if isinstance(x, tuple) else (x + y, 2)


# ==================================================
# Line: 628

def _sparseSegmentReduceGradWeights(self, ygrad, segment_ids, mode):
  assert mode in ("sum", "mean", "sqrtn")
  if mode == "sum":
    weights = np.ones(ygrad.shape[0], ygrad.dtype)
  else:
    weights = np.zeros(ygrad.shape[0], ygrad.dtype)
    for segment in segment_ids:
      weights[segment] += 1
    weights = 1. / weights if mode == "mean" else 1. / np.sqrt(weights)
  return weights


# ==================================================
# Line: 1381

def _npTypeToStr(self, t):
  if t == np.float32:
    return "fp32"
  if t == np.float64:
    return "fp64"


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
# Line: 36

def _computeLogSumExp(self, x, **kwargs):
  result_naive = math_ops.cumsum(math_ops.exp(x), **kwargs)
  result_fused = math_ops.exp(math_ops.cumulative_logsumexp(x, **kwargs))
  return result_naive, result_fused


# ==================================================
# Line: 99

def _logSumExpMap(self, x):
  return map_fn.map_fn(
      lambda i: math_ops.reduce_logsumexp(x[:i + 1]),
      math_ops.range(array_ops.shape(x)[0]),
      dtype=x.dtype)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
# Line: 46

def _npBatchMatmul(self, x, y, adjoint_a, adjoint_b):
  # output's shape depends on adj[0] and adj[1]
  if adjoint_a:
    x = np.conjugate(np.swapaxes(x, -1, -2))
  if adjoint_b:
    y = np.conjugate(np.swapaxes(y, -1, -2))
  return np.matmul(x, y)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
# Line: 97

def _inv(self, x):
  return 1.0 / x


# ==================================================
# Line: 202

def _run_session(self, session, results):
  n_iterations = 500
  with session as s:
    data = variables.Variable(1.0)
    with ops.device('/device:GPU:0'):
      random_seed.set_random_seed(1)
      matrix1 = variables.Variable(
          random_ops.truncated_normal([1024, 1]), name='matrix1')
      matrix2 = variables.Variable(
          random_ops.truncated_normal([1, 1024]), name='matrix2')
      x1 = math_ops.multiply(data, matrix1, name='x1')
      x3 = math_ops.matmul(x1, math_ops.matmul(matrix2, matrix1))
      x4 = math_ops.matmul(array_ops.transpose(x3), x3, name='x4')
      s.run(variables.global_variables_initializer())

      for _ in range(n_iterations):
        value = s.run(x4)
        results.add(value.flat[0])
        if len(results) != 1:
          break


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Line: 142

def _makeIncremental(self, shape, dtype):
  data = np.arange(np.prod(shape)).reshape(shape).astype(dtype.as_numpy_dtype)
  if dtype.is_complex:
    data -= 2j * data
  return data


# ==================================================
# Line: 148

def _makeRandom(self, shape, dtype):
  data = np.random.rand(*shape).astype(dtype.as_numpy_dtype)
  if dtype.is_complex:
    data -= 2j * data
  return data


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/aggregate_ops_test.py
# Line: 37

def _supported_types(self):
  if test.is_gpu_available():
    return [
        dtypes.float16, dtypes.bfloat16, dtypes.float32, dtypes.float64,
        dtypes.complex64, dtypes.complex128, dtypes.int64
    ]
  return [
      dtypes.int8,
      dtypes.int16,
      dtypes.int32,
      dtypes.int64,
      dtypes.bfloat16,
      dtypes.float16,
      dtypes.float32,
      dtypes.float64,
      dtypes.complex64,
      dtypes.complex128,
  ]


# ==================================================
# Line: 56

def _buildData(self, shape, dtype):
  data = np.random.randn(*shape).astype(dtype.as_numpy_dtype)
  # For complex types, add an index-dependent imaginary component so we can
  # tell we got the right value.
  if dtype.is_complex:
    return data + 10j * data
  return data


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
# Line: 35

def _np_transpose(self, x, perm):
  ret = np.copy(x)
  ret = ret.transpose(perm)
  return ret


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_d9m_test.py
# Line: 42

def _input(self, data_type, segment_ids_type):
  data = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=data_type)
  segment_ids = constant_op.constant([0, 1], dtype=segment_ids_type)
  num_segments = 2
  return data, segment_ids, num_segments


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
# Line: 171

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 351

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 552

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 749

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 948

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 1082

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 1354

def np_auc(self, predictions, labels, weights):
  """Computes the AUC explicitly using Numpy.

  Args:
    predictions: an ndarray with shape [N].
    labels: an ndarray with shape [N].
    weights: an ndarray with shape [N].

  Returns:
    the area under the ROC curve.
  """
  if weights is None:
    weights = np.ones(np.size(predictions))
  is_positive = labels > 0
  num_positives = np.sum(weights[is_positive])
  num_negatives = np.sum(weights[~is_positive])

  # Sort descending:
  inds = np.argsort(-predictions)

  sorted_labels = labels[inds]
  sorted_weights = weights[inds]
  is_positive = sorted_labels > 0

  tp = np.cumsum(sorted_weights * is_positive) / num_positives
  return np.sum((sorted_weights * tp)[~is_positive]) / num_negatives


# ==================================================
# Line: 1434

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 1581

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 1709

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 2959

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 3023

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 3114

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 3300

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 3400

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 3550

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 3624

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 3943

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 4180

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 4233

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 4285

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 4338

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 4392

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 4445

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 4497

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# Line: 4550

def setUp(self):
  np.random.seed(1)
  ops.reset_default_graph()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_ops_test.py
# Line: 33

def _AsSummary(self, s):
  summ = summary_pb2.Summary()
  summ.ParseFromString(s)
  return summ


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_image_op_test.py
# Line: 31

def _AsSummary(self, s):
  summ = summary_pb2.Summary()
  summ.ParseFromString(s)
  return summ


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_audio_op_test.py
# Line: 27

def _AsSummary(self, s):
  summ = summary_pb2.Summary()
  summ.ParseFromString(s)
  return summ


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
# Line: 1257

def create_run_metadata(self):
  step_stats = step_stats_pb2.StepStats(dev_stats=[
      step_stats_pb2.DeviceStepStats(
          device='cpu:0',
          node_stats=[step_stats_pb2.NodeExecStats(node_name='hello')])
  ])
  return config_pb2.RunMetadata(
      function_graphs=[
          config_pb2.RunMetadata.FunctionGraphs(
              pre_optimization_graph=graph_pb2.GraphDef(
                  node=[node_def_pb2.NodeDef(name='foo')]))
      ],
      step_stats=step_stats)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
# Line: 204

def test_with_dynamic_dimensions(self, dct_type, norm, shape, dtype):
  # "ortho" normalization is not implemented for type I.
  if dct_type == 1 and norm == "ortho":
    return
  signals = np.random.rand(*shape).astype(dtype)
  n = np.random.randint(1, 2 * shape[-1])
  n = np.random.choice([None, n])

  @def_function.function
  def func(signals):
    return dct_ops.dct(signals, n=n, type=dct_type, norm=norm)

  # Trace with all undefined dimensions
  signals_spec = tensor_spec.TensorSpec([None] * len(shape), dtype)
  f = func.get_concrete_function(signals_spec)
  # Run with actual shape
  f(signals)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
# Line: 175

def _np_fft(self, x, rank, fft_length=None):
  if rank == 1:
    return np.fft.fft2(x, s=fft_length, axes=(-1,))
  elif rank == 2:
    return np.fft.fft2(x, s=fft_length, axes=(-2, -1))
  elif rank == 3:
    return np.fft.fft2(x, s=fft_length, axes=(-3, -2, -1))
  else:
    raise ValueError("invalid rank")


# ==================================================
# Line: 185

def _np_ifft(self, x, rank, fft_length=None):
  if rank == 1:
    return np.fft.ifft2(x, s=fft_length, axes=(-1,))
  elif rank == 2:
    return np.fft.ifft2(x, s=fft_length, axes=(-2, -1))
  elif rank == 3:
    return np.fft.ifft2(x, s=fft_length, axes=(-3, -2, -1))
  else:
    raise ValueError("invalid rank")


# ==================================================
# Occurrences: Lines 209-215 (3 instances)

def _np_fftn(self, x, fft_length=None, axes=None, norm=None):
  return np.fft.fftn(x, s=fft_length, axes=axes, norm=norm)


# ==================================================
# Line: 225

def _tf_ifft_for_rank(self, rank):
  if rank == 1:
    return fft_ops.ifft
  elif rank == 2:
    return fft_ops.ifft2d
  elif rank == 3:
    return fft_ops.ifft3d
  else:
    raise ValueError("invalid rank")


# ==================================================
# Occurrences: Lines 501-507 (3 instances)

def _np_fftn(self, x, fft_length=None, axes=None, norm=None):
  return np.fft.rfftn(x, s=fft_length, axes=axes, norm=norm)


# ==================================================
# Line: 517

def _np_ifft(self, x, rank, fft_length=None):
  if rank == 1:
    return np.fft.irfft2(x, s=fft_length, axes=(-1,))
  elif rank == 2:
    return np.fft.irfft2(x, s=fft_length, axes=(-2, -1))
  elif rank == 3:
    return np.fft.irfft2(x, s=fft_length, axes=(-3, -2, -1))
  else:
    raise ValueError("invalid rank")


# ==================================================
# Line: 527

def _tf_fft_for_rank(self, rank):
  if rank == 1:
    return fft_ops.rfft
  elif rank == 2:
    return fft_ops.rfft2d
  elif rank == 3:
    return fft_ops.rfft3d
  else:
    raise ValueError("invalid rank")


# ==================================================
# Line: 537

def _tf_ifft_for_rank(self, rank):
  if rank == 1:
    return fft_ops.irfft
  elif rank == 2:
    return fft_ops.irfft2d
  elif rank == 3:
    return fft_ops.irfft3d
  else:
    raise ValueError("invalid rank")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
# Line: 139

def test_list_does_not_raise(self):
  list_of_stuff = [
      constant_op.constant([11, 22]), constant_op.constant([1, 2])
  ]
  check_ops.assert_proper_iterable(list_of_stuff)


# ==================================================
# Line: 146

def test_generator_does_not_raise(self):
  generator_of_stuff = (constant_op.constant([11, 22]), constant_op.constant(
      [1, 2]))
  check_ops.assert_proper_iterable(generator_of_stuff)



# ==================================================
# Line: 168

def test_returns_none_with_eager(self):
  with context.eager_mode():
    small = constant_op.constant([1, 2], name="small")
    x = check_ops.assert_equal(small, small)
    assert x is None


# ==================================================
# Line: 368

def test_returns_none_with_eager(self):
  with context.eager_mode():
    t1 = constant_op.constant([1, 2])
    t2 = constant_op.constant([3, 4])
    x = check_ops.assert_none_equal(t1, t2)
    assert x is None


# ==================================================
# Line: 512

def test_returns_none_with_eager(self):
  with context.eager_mode():
    t1 = constant_op.constant([1., 2.])
    t2 = constant_op.constant([1., 2.])
    x = check_ops.assert_near(t1, t2)
    assert x is None


# ==================================================
# Line: 593

def test_returns_none_with_eager(self):
  with context.eager_mode():
    t1 = constant_op.constant([1, 2])
    t2 = constant_op.constant([3, 4])
    x = check_ops.assert_less(t1, t2)
    assert x is None


# ==================================================
# Line: 1018

def _grappler_all_off_config(self):
  config = config_pb2.ConfigProto()
  off = rewriter_config_pb2.RewriterConfig.OFF
  config.graph_options.optimizer_options.opt_level = -1
  config.graph_options.rewrite_options.disable_model_pruning = 1
  config.graph_options.rewrite_options.constant_folding = off
  config.graph_options.rewrite_options.layout_optimizer = off
  config.graph_options.rewrite_options.arithmetic_optimization = off
  config.graph_options.rewrite_options.dependency_optimization = off
  return config


# ==================================================
# Line: 1065

def _apply_n_times(self, op, target, n=1000):
  for _ in range(n):
    target = op(target)
  return target


# ==================================================
# Line: 1617

def test_rank_zero_rank_one_size_one_equivalence(self):
  rank_one_size_one = array_ops.ones([1], name="rank_one_size_one")
  rank_zero = array_ops.constant(5, name="rank_zero")
  check_ops.assert_shapes([
      (rank_one_size_one, ()),
      (rank_zero, ()),
  ])
  check_ops.assert_shapes([
      (rank_one_size_one, (1,)),
      (rank_zero, (1,)),
  ])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/benchmark_test.py
# Occurrences: Lines 39-48 (4 instances)

def _dontRunThisBenchmark(self):
  _ran_somebenchmark_but_shouldnt[0] = True


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
# Line: 36

def _Sampler(
    self, num, counts, probs, dtype, gen=None, sample_shape=None, seed=None):
  def func():
    shape = [10 * num] if sample_shape is None else sample_shape
    generator = gen if gen is not None else (
        stateful_random_ops.Generator.from_seed(seed))
    return generator.binomial(
        shape=shape, counts=counts, probs=probs, dtype=dtype)

  return func


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
# Line: 145

def _make_ops(self, num_samples, seed=None, dtype=dtypes.float32):
  prob_dist = constant_op.constant([[0.15, 0.5, 0.3, 0.05]], dtype=dtype)
  logits = math_ops.log(prob_dist)
  # Two independent sets of samples from the same distribution
  sample_op1 = random_ops.multinomial(logits, num_samples, seed)
  sample_op2 = random_ops.multinomial(logits, num_samples, seed)
  return (sample_op1, sample_op2)


# ==================================================
# Line: 153

def _normalize(self, vec):
  batched = (len(vec.shape) == 2)
  return vec / vec.sum(axis=1, keepdims=True) if batched else vec / vec.sum()


# ==================================================
# Line: 189

def _chi2(self, expected, actual):
  actual = np.asarray(actual)
  expected = np.asarray(expected)
  diff = actual - expected
  chi2 = np.sum(diff * diff / expected, axis=0)
  return chi2


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
# Line: 37

def setUp(self):
  np.random.seed(137)
  random_seed.set_random_seed(137)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
# Line: 146

def testSplitInFunction(self, alg):
  g = random.Generator.from_seed(1, alg=alg)
  if alg == random_ops_util.Algorithm.THREEFRY:
    # We don't have CPU/GPU kernels for ThreeFry yet.
    return
  new_g = [None]  # using list as mutable cells
  @def_function.function
  def f():
    if new_g[0] is None:  # avoid creating variable in 2nd trace
      new_g[0] = g.split(2)
    return [new_g[0][i].normal([]) for i in range(2)]
  f()


# ==================================================
# Line: 223

def testCreateGeneratorFromSymbolic(self):
  g = [None, None, None]  # using list as mutable cells
  @def_function.function
  def f(scalar, vector2, vector3):
    if g[0] is None:  # avoid creating variable in 2nd trace
      g[0] = random.Generator.from_seed(scalar)
      g[0].reset_from_seed(scalar)  # also test reset
      g[1] = random.Generator.from_state(vector3, random.RNG_ALG_PHILOX)
      g[1].reset(vector3)
      g[2] = random.Generator.from_key_counter(
          scalar, vector2, random.RNG_ALG_PHILOX)
      g[2].reset_from_key_counter(scalar, vector2)
    return [g[i].normal([]) for i in range(3)]
  args = (1, [2, 2], [3, 3, 3])
  args = [constant_op.constant(v) for v in args]
  f(*args)


# ==================================================
# Line: 352

def testEagerAndDefun(self):
  """A simple test to make sure the op works in eager and defunned mode."""
  random.get_global_generator().normal((3,))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
# Line: 71

def _generateMatrix(self, m, n):
  matrix = (np.random.normal(-5, 5,
                             m * n).astype(np.complex128).reshape([m, n]))
  matrix.imag = (np.random.normal(-5, 5, m * n).astype(np.complex128).reshape(
      [m, n]))
  return matrix


# ==================================================
# Line: 163

def _GenerateTestData(self, matrix_shape, num_rhs):
  batch_shape = matrix_shape[:-2]
  matrix_shape = matrix_shape[-2:]
  assert matrix_shape[0] == matrix_shape[1]
  n = matrix_shape[0]
  matrix = (np.ones(matrix_shape).astype(np.float32) /
            (2.0 * n) + np.diag(np.ones(n).astype(np.float32)))
  rhs = np.ones([n, num_rhs]).astype(np.float32)
  matrix = variables.Variable(
      np.tile(matrix, batch_shape + (1, 1)), trainable=False)
  rhs = variables.Variable(
      np.tile(rhs, batch_shape + (1, 1)), trainable=False)
  return matrix, rhs


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
# Line: 256

def _GenerateMatrix(self, shape):
  batch_shape = shape[:-2]
  shape = shape[-2:]
  assert shape[0] == shape[1]
  n = shape[0]
  matrix = np.ones(shape).astype(np.float32) / (2.0 * n) + np.diag(
      np.ones(n).astype(np.float32))
  return np.tile(matrix, batch_shape + (1, 1))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
# Line: 62

def _gen_positive_diag(self, dtype, diag_shape):
  if dtype.is_complex:
    diag = linear_operator_test_util.random_uniform(
        diag_shape, minval=1e-4, maxval=1., dtype=dtypes.float32)
    return math_ops.cast(diag, dtype=dtype)

  return linear_operator_test_util.random_uniform(
      diag_shape, minval=1e-4, maxval=1., dtype=dtype)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_tridiag_test.py
# Line: 31

def build_operator_and_matrix(
    self, build_info, dtype, use_placeholder,
    ensure_self_adjoint_and_pd=False,
    diagonals_format='sequence'):
  shape = list(build_info.shape)

  # Ensure that diagonal has large enough values. If we generate a
  # self adjoint PD matrix, then the diagonal will be dominant guaranteeing
  # positive definitess.
  diag = linear_operator_test_util.random_sign_uniform(
      shape[:-1], minval=4., maxval=6., dtype=dtype)
  # We'll truncate these depending on the format
  subdiag = linear_operator_test_util.random_sign_uniform(
      shape[:-1], minval=1., maxval=2., dtype=dtype)
  if ensure_self_adjoint_and_pd:
    # Abs on complex64 will result in a float32, so we cast back up.
    diag = math_ops.cast(math_ops.abs(diag), dtype=dtype)
    # The first element of subdiag is ignored. We'll add a dummy element
    # to superdiag to pad it.
    superdiag = math_ops.conj(subdiag)
    superdiag = manip_ops.roll(superdiag, shift=-1, axis=-1)
  else:
    superdiag = linear_operator_test_util.random_sign_uniform(
        shape[:-1], minval=1., maxval=2., dtype=dtype)

  matrix_diagonals = array_ops_stack.stack(
      [superdiag, diag, subdiag], axis=-2)
  matrix = gen_array_ops.matrix_diag_v3(
      matrix_diagonals,
      k=(-1, 1),
      num_rows=-1,
      num_cols=-1,
      align='LEFT_RIGHT',
      padding_value=0.)

  if diagonals_format == 'sequence':
    diagonals = [superdiag, diag, subdiag]
  elif diagonals_format == 'compact':
    diagonals = array_ops_stack.stack([superdiag, diag, subdiag], axis=-2)
  elif diagonals_format == 'matrix':
    diagonals = matrix

  lin_op_diagonals = diagonals

  if use_placeholder:
    if diagonals_format == 'sequence':
      lin_op_diagonals = [array_ops.placeholder_with_default(
          d, shape=None) for d in lin_op_diagonals]
    else:
      lin_op_diagonals = array_ops.placeholder_with_default(
          lin_op_diagonals, shape=None)

  operator = linalg_lib.LinearOperatorTridiag(
      diagonals=lin_op_diagonals,
      diagonals_format=diagonals_format,
      is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
      is_positive_definite=True if ensure_self_adjoint_and_pd else None)
  return operator, matrix


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
# Line: 496

  def operator_and_matrix(
      self, shape_info, dtype, use_placeholder,
      ensure_self_adjoint_and_pd=False):
    del ensure_self_adjoint_and_pd
    shape = list(shape_info.shape)
    expected_blocks = (
        shape_info.__dict__["blocks"] if "blocks" in shape_info.__dict__
        else [shape])
    matrices = [
        linear_operator_test_util.random_normal(block_shape, dtype=dtype)
        for block_shape in expected_blocks
    ]

    lin_op_matrices = matrices

    if use_placeholder:
      lin_op_matrices = [
          array_ops.placeholder_with_default(
              matrix, shape=None) for matrix in matrices]

    blocks = []
    for l in lin_op_matrices:
      blocks.append(
          linalg.LinearOperatorFullMatrix(
              l,
              is_square=False,
              is_self_adjoint=False,
              is_positive_definite=False))
    operator = block_diag.LinearOperatorBlockDiag(blocks)

    # Broadcast the shapes.
    expected_shape = list(shape_info.shape)

    matrices = linear_operator_util.broadcast_matrix_batch_dims(matrices)

    block_diag_dense = _block_diag_dense(expected_shape, matrices)

    if not use_placeholder:
      block_diag_dense.set_shape(expected_shape)

    return operator, block_diag_dense


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
# Line: 73

def _makeBatch(self, matrix1, matrix2):
  matrix_batch = np.concatenate(
      [np.expand_dims(matrix1, 0),
       np.expand_dims(matrix2, 0)])
  matrix_batch = np.tile(matrix_batch, [2, 3, 1, 1])
  return matrix_batch


# ==================================================
# Line: 182

def _GenerateMatrix(self, shape):
  batch_shape = shape[:-2]
  shape = shape[-2:]
  assert shape[0] == shape[1]
  n = shape[0]
  matrix = np.ones(shape).astype(np.float32) / (2.0 * n) + np.diag(
      np.ones(n).astype(np.float32))
  return variables.Variable(np.tile(matrix, batch_shape + (1, 1)))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
# Line: 329

def expected_pinv(self, a, rcond):
  """Calls `np.linalg.pinv` but corrects its broken batch semantics."""
  if a.ndim < 3:
    return np.linalg.pinv(a, rcond)
  if rcond is None:
    rcond = 10. * max(a.shape[-2], a.shape[-1]) * np.finfo(a.dtype).eps
  s = np.concatenate([a.shape[:-2], [a.shape[-1], a.shape[-2]]])
  a_pinv = np.zeros(s, dtype=a.dtype)
  for i in np.ndindex(a.shape[:(a.ndim - 2)]):
    a_pinv[i] = np.linalg.pinv(
        a[i], rcond=rcond if isinstance(rcond.tolist(), float) else rcond[i])
  return a_pinv


# ==================================================
# Line: 657

def test_extreme_eigenvalues_test(self, dtype):
  huge = 0.33 * np.finfo(dtype).max
  tiny = 3 * np.finfo(dtype).tiny
  for (a, b) in [(tiny, tiny), (huge, np.sqrt(huge))]:
    alpha = np.array([-a, -np.sqrt(a), np.sqrt(a), a]).astype(dtype)

    beta = b * np.ones([3], dtype=dtype)
    if np.issubdtype(alpha.dtype, np.complexfloating):
      beta += 1j * beta


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
# Line: 47

def _makeBatch(self, matrix1, matrix2):
  matrix_batch = np.concatenate(
      [np.expand_dims(matrix1, 0),
       np.expand_dims(matrix2, 0)])
  matrix_batch = np.tile(matrix_batch, [2, 3, 1, 1])
  return matrix_batch


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
# Line: 50

def _makeBatch(self, matrix1, matrix2):
  matrix_batch = np.concatenate(
      [np.expand_dims(matrix1, 0),
       np.expand_dims(matrix2, 0)])
  matrix_batch = np.tile(matrix_batch, [2, 3, 1, 1])
  return matrix_batch


# ==================================================
# Line: 160

def _GenerateMatrix(self, shape):
  batch_shape = shape[:-2]
  shape = shape[-2:]
  assert shape[0] == shape[1]
  n = shape[0]
  matrix = np.ones(shape).astype(np.complex64) / (2.0 * n) + np.diag(
      np.ones(n).astype(np.complex64))
  return variables.Variable(np.tile(matrix, batch_shape + (1, 1)))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
# Line: 47

def operator_and_matrix(self,
                        build_info,
                        dtype,
                        use_placeholder,
                        ensure_self_adjoint_and_pd=False):
  shape = list(build_info.shape)

  if ensure_self_adjoint_and_pd:
    matrix = linear_operator_test_util.random_positive_definite_matrix(
        shape, dtype, force_well_conditioned=True)
  else:
    matrix = linear_operator_test_util.random_tril_matrix(
        shape, dtype, force_well_conditioned=True, remove_upper=True)

  lin_op_matrix = matrix

  if use_placeholder:
    lin_op_matrix = array_ops.placeholder_with_default(matrix, shape=None)

  if ensure_self_adjoint_and_pd:
    operator = LinearOperatorAdjoint(
        linalg.LinearOperatorFullMatrix(
            lin_op_matrix, is_positive_definite=True, is_self_adjoint=True))
  else:
    operator = LinearOperatorAdjoint(
        linalg.LinearOperatorLowerTriangular(lin_op_matrix))

  return operator, linalg.adjoint(matrix)


# ==================================================
# Line: 265

  def operator_and_matrix(self, build_info, dtype, use_placeholder):
    shape_before_adjoint = list(build_info.shape)
    # We need to swap the last two dimensions because we are taking the adjoint
    # of this operator
    shape_before_adjoint[-1], shape_before_adjoint[-2] = (
        shape_before_adjoint[-2], shape_before_adjoint[-1])
    matrix = linear_operator_test_util.random_normal(
        shape_before_adjoint, dtype=dtype)

    lin_op_matrix = matrix

    if use_placeholder:
      lin_op_matrix = array_ops.placeholder_with_default(matrix, shape=None)

    operator = LinearOperatorAdjoint(
        linalg.LinearOperatorFullMatrix(lin_op_matrix))

    return operator, linalg.adjoint(matrix)


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
# Line: 35

def _high_precision_matmul(self, a, b, adjoint_b):
  """Do a higher-precision matmul, casting either to float32 or float64."""
  if a.dtype == dtypes.float16:
    a = math_ops.cast(a, dtypes.float32)
    b = math_ops.cast(b, dtypes.float32)

  ret = test_util.matmul_without_tf32(a, b, adjoint_b=adjoint_b)
  return math_ops.cast(ret, a.dtype)


# ==================================================
# Line: 69

def _makeBatch(self, matrix1, matrix2):
  matrix_batch = np.concatenate(
      [np.expand_dims(matrix1, 0),
       np.expand_dims(matrix2, 0)])
  matrix_batch = np.tile(matrix_batch, [2, 3, 1, 1])
  return matrix_batch


# ==================================================
# Line: 179

def _GenerateMatrix(self, shape):
  batch_shape = shape[:-2]
  shape = shape[-2:]
  assert shape[0] == shape[1]
  n = shape[0]
  matrix = np.ones(shape).astype(np.float32) / (
      2.0 * n) + np.diag(np.ones(n).astype(np.float32))
  return variables.Variable(np.tile(matrix, batch_shape + (1, 1)))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
# Line: 225

def _GenerateMatrix(self, shape):
  batch_shape = shape[:-2]
  shape = shape[-2:]
  assert shape[0] == shape[1]
  n = shape[0]
  matrix = np.ones(shape).astype(np.float32) / (
      2.0 * n) + np.diag(np.ones(n).astype(np.float32))
  return variables.Variable(np.tile(matrix, batch_shape + (1, 1)))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
# Line: 52

def operator_and_matrix(self, build_info, dtype, use_placeholder,
                        ensure_self_adjoint_and_pd=False):
  shape = list(build_info.shape)

  # Either 1 or 2 matrices, depending.
  num_operators = rng.randint(low=1, high=3)
  if ensure_self_adjoint_and_pd:
    # The random PD matrices are also symmetric. Here we are computing
    # A @ A ... @ A. Since A is symmetric and PD, so are any powers of it.
    matrices = [
        linear_operator_test_util.random_positive_definite_matrix(
            shape, dtype, force_well_conditioned=True)] * num_operators
  else:
    matrices = [
        linear_operator_test_util.random_positive_definite_matrix(
            shape, dtype, force_well_conditioned=True)
        for _ in range(num_operators)
    ]

  lin_op_matrices = matrices

  if use_placeholder:
    lin_op_matrices = [
        array_ops.placeholder_with_default(
            matrix, shape=None) for matrix in matrices]

  operator = linalg.LinearOperatorComposition(
      [linalg.LinearOperatorFullMatrix(l) for l in lin_op_matrices],
      is_positive_definite=True if ensure_self_adjoint_and_pd else None,
      is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
      is_square=True)

  matmul_order_list = list(reversed(matrices))
  mat = matmul_order_list[0]
  for other_mat in matmul_order_list[1:]:
    mat = math_ops.matmul(other_mat, mat)

  return operator, mat


# ==================================================
# Line: 186

def operator_and_matrix(
    self, build_info, dtype, use_placeholder,
    ensure_self_adjoint_and_pd=False):
  del ensure_self_adjoint_and_pd
  shape = list(build_info.shape)

  # Create 2 matrices/operators, A1, A2, which becomes A = A1 A2.
  # Use inner dimension of 2.
  k = 2
  batch_shape = shape[:-2]
  shape_1 = batch_shape + [shape[-2], k]
  shape_2 = batch_shape + [k, shape[-1]]

  # Ensure that the matrices are well-conditioned by generating
  # random matrices whose singular values are close to 1.
  # The reason to do this is because cond(AB) <= cond(A) * cond(B).
  # By ensuring that each factor has condition number close to 1, we ensure
  # that the condition number of the product isn't too far away from 1.
  def generate_well_conditioned(shape, dtype):
    m, n = shape[-2], shape[-1]
    min_dim = min(m, n)
    # Generate singular values that are close to 1.
    d = linear_operator_test_util.random_normal(
        shape[:-2] + [min_dim],
        mean=1.,
        stddev=0.1,
        dtype=dtype)
    zeros = array_ops.zeros(shape=shape[:-2] + [m, n], dtype=dtype)
    d = linalg_lib.set_diag(zeros, d)
    u, _ = linalg_lib.qr(linear_operator_test_util.random_normal(
        shape[:-2] + [m, m], dtype=dtype))

    v, _ = linalg_lib.qr(linear_operator_test_util.random_normal(
        shape[:-2] + [n, n], dtype=dtype))
    return math_ops.matmul(u, math_ops.matmul(d, v))

  matrices = [
      generate_well_conditioned(shape_1, dtype=dtype),
      generate_well_conditioned(shape_2, dtype=dtype),
  ]

  lin_op_matrices = matrices

  if use_placeholder:
    lin_op_matrices = [
        array_ops.placeholder_with_default(
            matrix, shape=None) for matrix in matrices]

  operator = linalg.LinearOperatorComposition(
      [linalg.LinearOperatorFullMatrix(l) for l in lin_op_matrices])

  matmul_order_list = list(reversed(matrices))
  mat = matmul_order_list[0]
  for other_mat in matmul_order_list[1:]:
    mat = math_ops.matmul(other_mat, mat)

  return operator, mat


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
# Line: 446

def _makeDataForGradientWithBatching(self):
  y = np.array([1, 3, 2, 4])
  grad_diags = np.array([[-5, 0, 4, 0], [9, 0, -4, -16], [0, 0, 5, 16]])
  grad_rhs = np.array([1, 0, -1, 4])

  diags_batched = np.array(
      [[_sample_diags, 2 * _sample_diags, 3 * _sample_diags],
       [4 * _sample_diags, 5 * _sample_diags, 6 * _sample_diags]])
  rhs_batched = np.array([[_sample_rhs, -_sample_rhs, _sample_rhs],
                          [-_sample_rhs, _sample_rhs, -_sample_rhs]])
  y_batched = np.array([[y, y, y], [y, y, y]])
  expected_grad_diags_batched = np.array(
      [[grad_diags, -grad_diags / 4, grad_diags / 9],
       [-grad_diags / 16, grad_diags / 25, -grad_diags / 36]])
  expected_grad_rhs_batched = np.array(
      [[grad_rhs, grad_rhs / 2, grad_rhs / 3],
       [grad_rhs / 4, grad_rhs / 5, grad_rhs / 6]])

  return (y_batched, diags_batched, rhs_batched, expected_grad_diags_batched,
          expected_grad_rhs_batched)


# ==================================================
# Line: 663

def _generateData(self, matrix_size, batch_size, num_rhs, seed=42):
  np.random.seed(seed)
  data = np.random.normal(size=(batch_size, matrix_size, 3 + num_rhs))
  diags = np.stack([data[:, :, 0], data[:, :, 1], data[:, :, 2]], axis=-2)
  rhs = data[:, :, 3:]
  return (variables.Variable(diags, dtype=dtypes.float64),
          variables.Variable(rhs, dtype=dtypes.float64))


# ==================================================
# Line: 671

def _generateMatrixData(self, matrix_size, batch_size, num_rhs, seed=42):
  np.random.seed(seed)
  import scipy.sparse as sparse  # pylint:disable=g-import-not-at-top
  # By being strictly diagonally dominant, we guarantee invertibility.d
  diag = 2 * np.abs(np.random.randn(matrix_size)) + 4.1
  subdiag = 2 * np.abs(np.random.randn(matrix_size - 1))
  superdiag = 2 * np.abs(np.random.randn(matrix_size - 1))
  matrix = sparse.diags([superdiag, diag, subdiag], [1, 0, -1]).toarray()
  vector = np.random.randn(batch_size, matrix_size, num_rhs)
  return (variables.Variable(np.tile(matrix, (batch_size, 1, 1))),
          variables.Variable(vector))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
# Line: 98

def _makeTridiagonalMatrix(self, superdiag, maindiag, subdiag):
  super_pad = [[0, 0], [0, 1], [1, 0]]
  sub_pad = [[0, 0], [1, 0], [0, 1]]

  super_part = array_ops.pad(array_ops.matrix_diag(superdiag), super_pad)
  main_part = array_ops.matrix_diag(maindiag)
  sub_part = array_ops.pad(array_ops.matrix_diag(subdiag), sub_pad)
  return super_part + main_part + sub_part


# ==================================================
# Line: 107

def _randomComplexArray(self, shape):
  np.random.seed(43)
  return (np.random.uniform(-10, 10, shape) +
          np.random.uniform(-10, 10, shape) * 1j)


# ==================================================
# Line: 225

def baseline(self, upper, diag, lower, vec):
  diag_part = array_ops.expand_dims(diag, -1) * vec
  lower_part = array_ops.pad(
      array_ops.expand_dims(lower[:, 1:], -1) * vec[:, :-1, :],
      [[0, 0], [1, 0], [0, 0]])
  upper_part = array_ops.pad(
      array_ops.expand_dims(upper[:, :-1], -1) * vec[:, 1:, :],
      [[0, 0], [0, 1], [0, 0]])
  return lower_part + diag_part + upper_part


# ==================================================
# Line: 235

def _generateData(self, batch_size, m, n, seed=42):
  np.random.seed(seed)
  data = np.random.normal(size=(batch_size, m, 3 + n))
  return (variables.Variable(data[:, :, 0], dtype=dtypes.float64),
          variables.Variable(data[:, :, 1], dtype=dtypes.float64),
          variables.Variable(data[:, :, 2], dtype=dtypes.float64),
          variables.Variable(data[:, :, 3:], dtype=dtypes.float64))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
# Line: 195

def getShapes(self, shapeList):
  return ((elem, int(np.floor(1.2 * elem))) for elem in shapeList)


# ==================================================
# Line: 312

def _GenerateMatrix(self, shape):
  batch_shape = shape[:-2]
  shape = shape[-2:]
  assert shape[0] == shape[1]
  n = shape[0]
  matrix = np.ones(shape).astype(np.float32) / (
      2.0 * n) + np.diag(np.ones(n).astype(np.float32))
  return np.tile(matrix, batch_shape + (1, 1))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
# Line: 37

def operator_and_matrix(
    self, build_info, dtype, use_placeholder,
    ensure_self_adjoint_and_pd=False):
  shape = list(build_info.shape)

  matrix = linear_operator_test_util.random_positive_definite_matrix(
      shape, dtype)

  lin_op_matrix = matrix

  if use_placeholder:
    lin_op_matrix = array_ops.placeholder_with_default(matrix, shape=None)

  # Set the hints to none to test non-symmetric PD code paths.
  operator = linalg.LinearOperatorFullMatrix(
      lin_op_matrix,
      is_square=True,
      is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
      is_positive_definite=True if ensure_self_adjoint_and_pd else None)

  return operator, matrix


# ==================================================
# Line: 148

def operator_and_matrix(
    self, build_info, dtype, use_placeholder,
    ensure_self_adjoint_and_pd=False):

  # Matrix is always symmetric and positive definite in this class.
  del ensure_self_adjoint_and_pd

  shape = list(build_info.shape)

  matrix = linear_operator_test_util.random_positive_definite_matrix(
      shape, dtype, force_well_conditioned=True)

  lin_op_matrix = matrix

  if use_placeholder:
    lin_op_matrix = array_ops.placeholder_with_default(matrix, shape=None)

  operator = linalg.LinearOperatorFullMatrix(
      lin_op_matrix,
      is_square=True,
      is_self_adjoint=True,
      is_positive_definite=True)

  return operator, matrix


# ==================================================
# Line: 229

def operator_and_matrix(
    self, build_info, dtype, use_placeholder,
    ensure_self_adjoint_and_pd=False):
  del ensure_self_adjoint_and_pd
  shape = list(build_info.shape)
  matrix = linear_operator_test_util.random_normal(shape, dtype=dtype)

  lin_op_matrix = matrix

  if use_placeholder:
    lin_op_matrix = array_ops.placeholder_with_default(matrix, shape=None)

  operator = linalg.LinearOperatorFullMatrix(lin_op_matrix, is_square=True)

  return operator, matrix


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
# Line: 232

def _shape_to_spectrum_shape(self, shape):
  # If spectrum.shape = batch_shape + [N],
  # this creates an operator of shape batch_shape + [N, N]
  return shape[:-1]


# ==================================================
# Line: 656

def _shape_to_spectrum_shape(self, shape):
  """Get a spectrum shape that will make an operator of desired shape."""
  # This 2D block circulant operator takes a spectrum of shape
  # batch_shape + [N0, N1],
  # and creates and operator of shape
  # batch_shape + [N0*N1, N0*N1]
  if shape == (0, 0):
    return (0, 0)
  elif shape == (1, 1):
    return (1, 1)
  elif shape == (1, 6, 6):
    return (1, 2, 3)
  elif shape == (3, 4, 4):
    return (3, 2, 2)
  elif shape == (2, 1, 3, 3):
    return (2, 1, 3, 1)
  else:
    raise ValueError("Unhandled shape: %s" % shape)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/base64_ops_test.py
# Line: 40

def _RemovePad(self, msg, base64_msg):
  if len(msg) % 3 == 1:
    return base64_msg[:-2]
  if len(msg) % 3 == 2:
    return base64_msg[:-1]
  return base64_msg


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_script_op_test.py
# Line: 60

def _generateBenchmarkInput(self, size):
  chars = []
  i = 0
  offset = 0
  continuity_size = 20
  while i < size:
    chars.append(ord("a") + offset)
    i += 1
    offset += 1
    if i % continuity_size == 0:
      offset += 100
      if offset > 0x1F940:
        offset = 0

  return chars


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/io_ops/io_ops_test.py
# Line: 74

def _subset(self, files, indices):
  return set(
      compat.as_bytes(files[i].name) for i in range(len(files))
      if i in indices)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
# Line: 1435

def testCreateSequenceExample(self):
  value = sequence_example(
      context=features({
          "global_feature": float_feature([1, 2, 3]),
      }),
      feature_lists=feature_lists({
          "repeated_feature_2_frames":
              feature_list([
                  bytes_feature([b"a", b"b", b"c"]),
                  bytes_feature([b"a", b"d", b"e"])
              ]),
          "repeated_feature_3_frames":
              feature_list([
                  int64_feature([3, 4, 5, 6, 7]),
                  int64_feature([-1, 0, 0, 0, 0]),
                  int64_feature([1, 2, 3, 4, 5])
              ])
      }))
  value.SerializeToString()  # Smoke test


# ==================================================
# Line: 2328

def _ordinalize(self, words, fixed_length=None):
  outputs = []
  if fixed_length is None:
    fixed_length = len(words[0])

  for word in words:
    output = []
    for i in range(fixed_length):
      if i < len(word):
        output.append(ord(word[i]))
      else:
        output.append(0)
    outputs.append(output)
  return np.array(outputs)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
# Line: 78

def _Record(self, f, r):
  return compat.as_bytes("Record %d of file %d" % (r, f))


# ==================================================
# Line: 344

def _LineText(self, f, l):
  return compat.as_bytes("%d: %d" % (f, l))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
# Line: 551

def _gpu_modes(self):
  if test.is_gpu_available():
    return [False, True]
  else:
    return [False]


# ==================================================
# Line: 621

def _gpu_modes(self):
  if test.is_gpu_available():
    return [False, True]
  else:
    return [False]


# ==================================================
# Line: 722

def create_nd_inputs_and_expected_output(self, axis):
  a = np.arange(2, dtype=np.float32)
  b = a * 5
  num = 5

  res = np.array([[0., 0., 0., 0., 0.], [1., 2., 3., 4., 5.]])
  expected = res if axis != 0 else res.T
  return a, b, expected, num


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
# Line: 62

def _buildParams(self, data, dtype):
  data = data.astype(dtype.as_numpy_dtype)
  # For complex types, add an index-dependent imaginary component so we can
  # tell we got the right value.
  if dtype.is_complex:
    return data + 10j * data
  return data


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
# Line: 212

def spaceToDepthUsingTranspose(self, tensor, block_size, data_format):
  block_size_sq = block_size * block_size

  dtype = tensor.dtype
  if dtype == dtypes.qint8:
    tensor = array_ops.bitcast(tensor, dtypes.int8)

  if data_format == "NHWC":
    b, ih, iw, ic = tensor.shape.as_list()
    assert ih % block_size == 0, (ih, block_size)
    assert iw % block_size == 0, (iw, block_size)
    ow, oh, oc = iw // block_size, ih // block_size, ic * block_size_sq
    tensor = array_ops.reshape(tensor,
                               [b, oh, block_size, ow, block_size, ic])
    tensor = array_ops.transpose(tensor, [0, 1, 3, 2, 4, 5])
    tensor = array_ops.reshape(tensor, [b, oh, ow, oc])
  elif data_format == "NCHW":
    b, ic, ih, iw = tensor.shape.as_list()
    assert ih % block_size == 0, (ih, block_size)
    assert iw % block_size == 0, (iw, block_size)
    ow, oh, oc = iw // block_size, ih // block_size, ic * block_size_sq
    tensor = array_ops.reshape(tensor,
                               [b, ic, oh, block_size, ow, block_size])
    tensor = array_ops.transpose(tensor, [0, 3, 5, 1, 2, 4])
    tensor = array_ops.reshape(tensor, [b, oc, oh, ow])

  if dtype == dtypes.qint8:
    tensor = array_ops.bitcast(tensor, dtype)
  return tensor


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
# Line: 38

def _npPad(self, inp, paddings, mode, constant_values=0):
  mode = mode.lower()
  if mode == "constant":
    return np.pad(inp, paddings, mode=mode, constant_values=constant_values)
  else:
    return np.pad(inp, paddings, mode=mode)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/weights_broadcast_test.py
# Line: 34

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# Line: 162

def setUp(self):
  ops.reset_default_graph()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
# Line: 35

def _toDataType(self, dtype):
  """Returns TensorFlow data type for numpy type."""
  if dtype == np.float32:
    return dtypes.float32
  elif dtype == np.float64:
    return dtypes.float64
  elif dtype == np.int32:
    return dtypes.int32
  elif dtype == np.int64:
    return dtypes.int64
  elif dtype == np.bool_:
    return dtypes.bool
  elif dtype == np.complex64:
    return dtypes.complex64
  elif dtype == np.complex128:
    return dtypes.complex128
  else:
    return None


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
# Line: 323

def _moreCases(self, align=None):
  # Diagonal bands.
  # pyformat: disable
  vecs = np.array([[[1, 2, 3, 4],  # Input shape: (2, 3, 4)
                    [5, 6, 7, 8],
                    [9, 8, 7, 6]],
                   [[5, 4, 3, 2],
                    [1, 2, 3, 4],
                    [5, 6, 7, 8]]])
  tests = dict()
  tests[-3, -1] = (vecs,
                   np.array([[[0, 0, 0, 0, 0],
                              [1, 0, 0, 0, 0],
                              [5, 2, 0, 0, 0],
                              [9, 6, 3, 0, 0],
                              [0, 8, 7, 4, 0]],
                             [[0, 0, 0, 0, 0],
                              [5, 0, 0, 0, 0],
                              [1, 4, 0, 0, 0],
                              [5, 2, 3, 0, 0],
                              [0, 6, 3, 2, 0]]]))
  tests[-1, 1] = (vecs,
                  np.array([[[5, 1, 0, 0],
                             [9, 6, 2, 0],
                             [0, 8, 7, 3],
                             [0, 0, 7, 8]],
                            [[1, 5, 0, 0],
                             [5, 2, 4, 0],
                             [0, 6, 3, 3],
                             [0, 0, 7, 4]]]))
  tests[2, 4] = (vecs,
                 np.array([[[0, 0, 9, 5, 1, 0],
                            [0, 0, 0, 8, 6, 2],
                            [0, 0, 0, 0, 7, 7],
                            [0, 0, 0, 0, 0, 6],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]],
                           [[0, 0, 5, 1, 5, 0],
                            [0, 0, 0, 6, 2, 4],
                            [0, 0, 0, 0, 7, 3],
                            [0, 0, 0, 0, 0, 8],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]]))
  # pyformat: enable
  return (None, repack_diagonals_in_tests(tests, align))


# ==================================================
# Line: 1079

def setUp(self):
  np.random.seed(0)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
# Line: 263

def depthToSpaceUsingTranspose(self, tensor, block_size, data_format):
  block_size_sq = block_size * block_size
  if data_format == "NHWC":
    b, ih, iw, ic = tensor.shape.as_list()
    assert ic % block_size_sq == 0, (ic, block_size_sq)
    ow, oh, oc = iw * block_size, ih * block_size, ic // block_size_sq
    tensor = array_ops.reshape(tensor,
                               [b, ih, iw, block_size, block_size, oc])
    tensor = array_ops.transpose(tensor, [0, 1, 3, 2, 4, 5])
    tensor = array_ops.reshape(tensor, [b, oh, ow, oc])
  elif data_format == "NCHW":
    b, ic, ih, iw = tensor.shape.as_list()
    assert ic % block_size_sq == 0, (ic, block_size_sq)
    ow, oh, oc = iw * block_size, ih * block_size, ic // block_size_sq
    tensor = array_ops.reshape(tensor,
                               [b, block_size, block_size, oc, ih, iw])
    tensor = array_ops.transpose(tensor, [0, 3, 4, 1, 5, 2])
    tensor = array_ops.reshape(tensor, [b, oc, oh, ow])
  return tensor


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
# Line: 40

def randn(self, shape, dtype):
  data = np.random.randn(*shape)
  if dtype == np.bool_:
    return data < 0  # Naive casting yields True with P(1)!
  else:
    return data.astype(dtype)


# ==================================================
# Line: 47

def unstackReference(self, data, axis):
  """Use numpy primitives to implement unstack equivalent."""
  result = []
  rank = len(data.shape)
  axis = axis + rank if axis < 0 else axis
  for k in range(data.shape[axis]):
    axis = rank + axis if axis < 0 else axis
    # Slice in axis dimension of k'th slice.
    # e.g. if rank=4 k=2, axis=2 then equivalent of data[:,:,2,:]
    # Give error with loop context
    slice_spec = tuple(
        slice(None) if i != axis else k for i in range(rank))
    result.append(data.__getitem__(slice_spec))
  return result


# ==================================================
# Line: 160

def testUnknownShapeOkWithNum(self):
  # Testing unknown shape in graph mode.
  with ops.Graph().as_default():
    x = array_ops.placeholder(np.float32)
    array_ops_stack.unstack(x, num=2)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
# Line: 495

def scatter_nd(self, indices, updates, shape, input_=None):
  del input_  # input_ is not used in scatter_nd
  return array_ops.scatter_nd(indices, updates, shape)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_gather_op_test.py
# Line: 33

def _buildParams(self, data, dtype):
  data = data.astype(dtype.as_numpy_dtype)
  # For complex types, add an index-dependent imaginary component so we can
  # tell we got the right value.
  if dtype.is_complex:
    return data + 10j * data
  return data


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/bitcast_op_test.py
# Line: 84

def testUnknownShape(self):
  # Need to use placeholder for unknown shape
  with ops.Graph().as_default():
    x = array_ops.placeholder(dtypes.float32)
    datatype = dtypes.int8
    array_ops.bitcast(x, datatype, None)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
# Line: 693

def testTensorSliceEagerMemory(self):
  with context.eager_mode():
    inputs = constant_op.constant([[[1], [2], [3], [4]]],
                                  dtype=dtypes.float32)
    # Tests that slicing an EagerTensor doesn't leak memory
    inputs[0]  # pylint: disable=pointless-statement


# ==================================================
# Line: 702

def testVariableSliceEagerMemory(self):
  with context.eager_mode():
    v = variables.Variable([1., 2.])
    v[0]  # pylint: disable=pointless-statement


# ==================================================
# Line: 1213

def make_variable(self):
  n = 256
  shape = (n, n, n)
  items = n**3
  var = variables.Variable(
      array_ops.reshape(math_ops.linspace(1., float(items), items), shape),
      dtype=dtypes.float32)
  return var


# ==================================================
# Line: 1792

def _scale_per_slice(self, shape, axis, values):
  # Note: repeats the values if the shape is larger than values.
  out = np.take(values, np.remainder(np.arange(np.prod(shape)),
                                     len(values))).reshape(shape)
  if axis is not None:
    scale_shape = [1] * len(shape)
    scale_shape[axis] = shape[axis]
    out *= np.arange(1, shape[axis] + 1).reshape(scale_shape)
  return out


# ==================================================
# Line: 2180

def testInt64(self):

  @def_function.function
  def g():
    x = random_ops.random_normal(shape=[int(1e10)])
    y = array_ops.ones(shape=[int(1e10)])
    return array_ops.searchsorted(x, y, out_type=dtypes.int64)

  _ = g.get_concrete_function()


# ==================================================
# Line: 2190

def testInt64UnspecifiedOutType(self):

  @def_function.function
  def g():
    x = random_ops.random_normal(shape=[int(1e10)])
    y = array_ops.ones(shape=[int(1e10)])
    return array_ops.searchsorted(x, y)

  _ = g.get_concrete_function()


# ==================================================
# Line: 2321

def _map_fn_body(self, elems):
  return gen_array_ops.gather_nd(elems[0], elems[1])


# ==================================================
# Line: 2456

def make_variable(self, shape, dtype=dtypes.float32):
  items = 1
  for dim in shape:
    items *= dim
  var = variables.Variable(
      array_ops.reshape(math_ops.linspace(1., float(items), items), shape),
      dtype=dtype)
  return var


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
# Line: 46

def randn(self, shape, dtype):
  data = np.random.randn(*shape)
  if dtype == np.bool_:
    return data < 0  # Naive casting yields True with P(1)!
  else:
    return data.astype(dtype)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
# Line: 212

def testEagerMemory(self):
  """Tests PyObject refs are managed correctly when executing eagerly."""
  constant_op.constant([[1.]])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
# Line: 47

def _makeData(self, shape, dtype):
  data = np.random.rand(*shape).astype(dtype.as_numpy_dtype)
  if dtype.is_complex:
    data -= 1j * data
  return data


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/garbage_collection_test.py
# Line: 31

def testEagerResourceVariables(self):
  with context.eager_mode():
    resource_variable_ops.ResourceVariable(1.0, name="a")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
# Line: 484

def _np_rotate_transpose(self, x, shift):
  if not isinstance(x, np.ndarray):
    x = np.array(x)
  return np.transpose(x, np.roll(np.arange(len(x.shape)), shift))


# ==================================================
# Line: 681

def _fill_triangular(self, x, upper=False):
  """Numpy implementation of `fill_triangular`."""
  x = np.asarray(x)
  # Formula derived by solving for n: m = n(n+1)/2.
  m = np.int32(x.shape[-1])
  n = np.sqrt(0.25 + 2. * m) - 0.5
  if n != np.floor(n):
    raise ValueError("Invalid shape.")
  n = np.int32(n)
  # We can't do: `x[..., -(n**2-m):]` because this doesn't correctly handle
  # `m == n == 1`. Hence, we do absolute indexing.
  x_tail = x[..., (m - (n * n - m)):]
  y = np.concatenate(
      [x, x_tail[..., ::-1]] if upper else [x_tail, x[..., ::-1]],
      axis=-1)
  y = y.reshape(np.concatenate([
      np.int32(x.shape[:-1]),
      np.int32([n, n]),
  ], axis=0))
  return np.triu(y) if upper else np.tril(y)


# ==================================================
# Line: 808

def _reduce_weighted_logsumexp(self, logx, w, axis, keep_dims=False):
  m = np.max(logx, axis=axis, keepdims=True)
  sum_ = np.sum(w * np.exp(logx - m), axis=axis, keepdims=keep_dims)
  sgn = np.sign(sum_)
  if not keep_dims:
    m = np.squeeze(m, axis=axis)
  return m + np.log(sgn * sum_), sgn


# ==================================================
# Line: 915

def _npSoftplus(self, np_features):
  np_features = np.asarray(np_features)
  zero = np.asarray(0).astype(np_features.dtype)
  return np.logaddexp(zero, np_features)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
# Line: 300

def _kstest(self, alpha, beta, samples):
  # Uses the Kolmogorov-Smirnov test for goodness of fit.
  if not stats:
    return True  # If we can't test, return that the test passes.
  ks, _ = stats.kstest(samples, stats.gamma(alpha, scale=1 / beta).cdf)
  # Return True when the test passes.
  return ks < 0.02


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
# Line: 285

def _kstest(self, loc, scale, samples):
  # Uses the Kolmogorov-Smirnov test for goodness of fit.
  if not stats:
    return True  # If scipy isn't available, return "True" for passing
  ks, _ = stats.kstest(samples, stats.laplace(loc, scale=scale).cdf)
  # Return True when the test passes.
  return ks < 0.02


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
# Line: 61

def getHashTable(self):
  if tf2.enabled():
    return lookup_ops.StaticHashTable
  else:
    return lookup_ops.StaticHashTableV1


# ==================================================
# Line: 67

def getVocabularyTable(self):
  if tf2.enabled():
    return lookup_ops.StaticVocabularyTable
  else:
    return lookup_ops.StaticVocabularyTableV1


# ==================================================
# Line: 4231

def _create_table(self):
  return lookup_ops.MutableHashTable(dtypes.int64, dtypes.float32, 0.0)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
# Line: 1741

def _build_graph(self):
  """Builds a graph that enqueues and dequeues a single float.

  Returns:
    A tuple with the graph init tensor and graph output tensor.
  """
  q = data_flow_ops.FIFOQueue(1, "float")
  init = q.enqueue(1.0)
  x = q.dequeue()
  q_inc = q.enqueue(x + 1)
  return init, q_inc


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
# Line: 1153

def _grad_source_for_name(self, name):
  return tensor_array_grad._GetGradSource(constant_op.constant(0, name=name))


# ==================================================
# Line: 1870

def _tensorArrayWriteInWhile(self):
  size = 10000
  ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=size)
  (_, ta) = while_loop.while_loop(
      lambda i, _: i < size,
      lambda i, ta: (i + 1, ta.write(i, 0.)), [0, ta],
      parallel_iterations=1)
  return ta.stack()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
# Occurrences: Lines 49-54 (2 instances)

def _randomTensor(self, size, np_dtype, sparse=True):
  n, m = size
  x = np.random.randn(n, m).astype(np_dtype)
  return _sparsify(x) if sparse else x


# ==================================================
# Line: 72

def _SparseTensor_3x3_v2(self):
  # [           1]
  # [-1.9        ]
  # [   3    -4.2]
  ind = np.array([[0, 1], [1, 0], [2, 0], [2, 1]])
  val = np.array([1, -1.9, 3, -4.2])
  shape = np.array([3, 3])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtypes.float32),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 273

  def benchmarkSparseAddDense(self):

    print("SparseAddDense: add with sparse_to_dense vs. sparse_add")
    print("%nnz \t n \t m \t millis(s2d) \t millis(sparse_add) \t speedup")

    for sparsity in [0.99, 0.5, 0.01]:
      for n in [1, 256, 50000]:
        for m in [100, 1000]:
          s2d_dt, sa_dt = _s2d_add_vs_sparse_add(sparsity, n, m)
          print("%.2f \t %d \t %d \t %.4f \t %.4f \t %.2f" % (sparsity, n, m,
                                                              s2d_dt, sa_dt,
                                                              s2d_dt / sa_dt))


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
# Line: 55

def _SparseTensor_5x6(self, dtype):
  ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2], [3, 3]])
  val = np.array([0, 10, 13, 14, 32, 33])
  shape = np.array([5, 6])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtype),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 64

def _SparseTensor_2x3x4(self, dtype):
  # Includes two entries with the form [1, 1, x] : 150.
  ind = np.array([[0, 0, 1], [0, 1, 0], [0, 1, 2], [1, 0, 3], [1, 1, 0],
                  [1, 1, 1], [1, 1, 2], [1, 2, 2]])
  val = np.array([1, 10, 12, 103, 150, 149, 150, 122])
  shape = np.array([2, 3, 4])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtype),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 115

def _SparseTensorValue_3x50(self, indices_dtype, values_dtype):
  # NOTE: This input is intentionally not sorted to validate the
  # already_sorted flag below.
  ind = np.array([[0, 0], [1, 0], [1, 2], [2, 0], [2, 1], [1, 1]])
  # NB: these are not sorted
  indices = np.array([0, 13, 10, 33, 32, 14])
  values = np.array([-3, 4, 1, 9, 5, 1])
  shape = np.array([3, 3])
  indices = sparse_tensor.SparseTensorValue(
      np.array(ind, np.int64),
      np.array(indices, indices_dtype), np.array(shape, np.int64))
  values = sparse_tensor.SparseTensorValue(
      np.array(ind, np.int64),
      np.array(values, values_dtype), np.array(shape, np.int64))
  return indices, values


# ==================================================
# Line: 229

def _SparseTensor_3x50(self, indices_dtype, values_dtype):
  # NOTE: This input is intentionally not sorted to validate the
  # already_sorted flag below.
  ind = np.array([[0, 0], [1, 0], [1, 2], [2, 0], [2, 1], [1, 1]])
  # NB: these are not sorted
  indices0 = np.array([0, 13, 10, 33, 32, 14])
  indices1 = np.array([12, 4, 0, 0, 1, 30])
  values = np.array([-3, 4, 1, 9, 5, 1])
  shape = np.array([3, 3])
  indices0 = sparse_tensor.SparseTensorValue(
      np.array(ind, np.int64),
      np.array(indices0, indices_dtype), np.array(shape, np.int64))
  indices1 = sparse_tensor.SparseTensorValue(
      np.array(ind, np.int64),
      np.array(indices1, indices_dtype), np.array(shape, np.int64))
  values = sparse_tensor.SparseTensorValue(
      np.array(ind, np.int64),
      np.array(values, values_dtype), np.array(shape, np.int64))
  return ([sparse_tensor.SparseTensor.from_value(indices0),
           sparse_tensor.SparseTensor.from_value(indices1)],
          sparse_tensor.SparseTensor.from_value(values))


# ==================================================
# Line: 289

def _SparseTensorValue_5x6(self):
  ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2], [3, 3]])
  val = np.array([0, 10, 13, 14, 32, 33])
  shape = np.array([5, 6])
  return sparse_tensor.SparseTensorValue(
      np.array(ind, np.int64),
      np.array(val, np.int32), np.array(shape, np.int64))


# ==================================================
# Line: 551

def _SparseTensorValue_5x6(self, dtype=np.int32):
  ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2], [3, 3]])
  val = np.array([0, 10, 13, 14, 32, 33])
  shape = np.array([5, 6])
  return sparse_tensor.SparseTensorValue(
      np.array(ind, np.int64), np.array(val, dtype), np.array(
          shape, np.int64))


# ==================================================
# Line: 562

def _SparseTensor_String5x6(self):
  ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2], [3, 3]])
  val = np.array(["a", "b", "c", "d", "e", "f"])
  shape = np.array([5, 6])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtypes.string),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 571

def _SparseTensor_2x6(self):
  ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4]])
  val = np.array([0, 10, 13, 14])
  shape = np.array([2, 6])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtypes.int32),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensors_map_ops_test.py
# Line: 42

def _SparseTensorPlaceholder(self, dtype=None):
  if dtype is None:
    dtype = dtypes.int32
  return sparse_tensor_lib.SparseTensor(
      array_ops.placeholder(dtypes.int64),
      array_ops.placeholder(dtype), array_ops.placeholder(dtypes.int64))


# ==================================================
# Line: 49

def _SparseTensorValue_5x6(self, permutation):
  ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2],
                  [3, 3]]).astype(np.int64)
  val = np.array([0, 10, 13, 14, 32, 33]).astype(np.int32)

  ind = ind[permutation]
  val = val[permutation]

  shape = np.array([5, 6]).astype(np.int64)
  return sparse_tensor_lib.SparseTensorValue(ind, val, shape)


# ==================================================
# Line: 60

def _SparseTensorValue_3x4(self, permutation):
  ind = np.array([[0, 0], [1, 0], [1, 2], [1, 3], [2, 2],
                  [2, 3]]).astype(np.int64)
  val = np.array([0, 10, 13, 14, 32, 33]).astype(np.int32)

  ind = ind[permutation]
  val = val[permutation]

  shape = np.array([3, 4]).astype(np.int64)
  return sparse_tensor_lib.SparseTensorValue(ind, val, shape)


# ==================================================
# Line: 71

def _SparseTensorValue_1x1x1(self):
  ind = np.array([[0, 0, 0]]).astype(np.int64)
  val = np.array([0]).astype(np.int32)
  shape = np.array([3, 4, 5]).astype(np.int64)
  return sparse_tensor_lib.SparseTensorValue(ind, val, shape)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
# Line: 31

def _SparseTensor_4x6(self, val_dtype=np.int64):
  # [0 |  |2 |  |4 |5 ]
  # [  |11|  |13|14|  ]
  # [20|  |  |23|  |25]
  # [30|  |32|33|  |35]
  ind = np.array([[0, 0], [0, 2], [0, 4], [0, 5], [1, 1], [1, 3], [1,
                                                                   4], [2, 0],
                  [2, 3], [2, 5], [3, 0], [3, 2], [3, 3], [3, 5]]).astype(
                      np.int64)
  val = np.array([0, 2, 4, 5, 11, 13, 14, 20, 23, 25, 30, 32, 33, 35]).astype(
      val_dtype)
  shape = np.array([4, 6]).astype(np.int64)
  return sparse_tensor.SparseTensor(ind, val, shape)


# ==================================================
# Line: 45

def _SparseTensor_5x7(self):
  # [0 |  |2 |  |4 |5 |  ]
  # [  |11|  |13|14|  |16]
  # [20|  |  |23|  |25|  ]
  # [30|  |32|33|  |35|  ]
  # [  |41|  |  |44|  |46]
  ind = np.array([[0, 0], [0, 2], [0, 4], [0, 5], [1, 1], [1, 3], [1, 4],
                  [1, 6], [2, 0], [2, 3], [2, 5], [3, 0], [3, 2], [3, 3],
                  [3, 5], [4, 1], [4, 4], [4, 6]]).astype(np.int64)
  val = np.array(
      [0, 2, 4, 5, 11, 13, 14, 16, 20, 23, 25, 30, 32, 33, 35, 41, 44,
       46]).astype(np.int64)
  shape = np.array([5, 7]).astype(np.int64)
  return sparse_tensor.SparseTensor(ind, val, shape)


# ==================================================
# Line: 60

def _SparseTensorValue_3x4x2(self):
  #  slice(:,:, 0)
  #  ['a0'|    |'b0'|    ]
  #  [    |'c0'|    |'d0']
  #  [    |    |'e0'|    ]
  #  slice(:,:, 1)
  #  ['a1'|    |'b1'|    ]
  #  [    |'c1'|    |'d1']
  #  [    |    |'e1'|    ]
  ind = np.array([[0, 0, 0], [0, 0, 1], [0, 2, 0], [0, 2, 1], [1, 1, 0],
                  [1, 1, 1], [1, 3, 0], [1, 3, 1], [2, 2, 0], [2, 2,
                                                               1]]).astype(
                                                                   np.int64)
  val = np.array(['a0', 'a1', 'b0', 'b1', 'c0', 'c1', 'd0', 'd1', 'e0', 'e1'])
  shape = np.array([3, 4, 2]).astype(np.int64)
  return sparse_tensor.SparseTensorValue(ind, val, shape)


# ==================================================
# Line: 81

def _SparseTensor_4x6_empty(self, val_dtype=np.int64):
  ind = np.empty(shape=(0, 2), dtype=np.int64)
  val = np.array([]).astype(val_dtype)
  shape = np.array([4, 6]).astype(np.int64)
  return sparse_tensor.SparseTensor(ind, val, shape)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
# Line: 33

def _sparse_tensor(self, data, batch_size=-1):
  """Generates a SparseTensor.

  Args:
    data: Should be a list of list of strings or int64. Each item of the outer
      list represents a batch. Each item of the batch is a feature of a
      specific feature column.
    batch_size: optional batch size, especially for cases when data has no
      entry for some batches.

  Returns:
   A SparseTensor.
  """
  indices = []
  values = []
  max_col_count = 0
  for batch, batch_ix in zip(data, range(len(data))):
    for column, column_ix in zip(batch, range(len(batch))):
      indices.append([batch_ix, column_ix])
      values.append(column)
      max_col_count = max(max_col_count, column_ix + 1)
  shape = [batch_size if batch_size != -1 else len(data), max_col_count]
  value_type = (
      dtypes.string
      if not values or isinstance(values[0], str) else dtypes.int64)
  return sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64, [len(indices), 2]),
      constant_op.constant(values, value_type, [len(indices)]),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 427

def _sparse_tensor(self, data, batch_size=-1):
  """Generates a SparseTensor.

  Args:
    data: Should be a list of list of strings or int64. Each item of the outer
        list represents a batch. Each item of the batch is a feature of a
        specific feature column.
    batch_size: optional batch size, especially for cases when data has no
        entry for some batches.

  Returns:
   A SparseTensor.
  """
  indices = []
  values = []
  max_col_count = 0
  for batch, batch_ix in zip(data, range(len(data))):
    for column, column_ix in zip(batch, range(len(batch))):
      indices.append([batch_ix, column_ix])
      values.append(column)
      max_col_count = max(max_col_count, column_ix + 1)
  shape = [batch_size if batch_size != -1 else len(data), max_col_count]
  value_type = (dtypes.string if not values or isinstance(values[0], str) else
                dtypes.int64)
  return sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64, [len(indices), 2]),
      constant_op.constant(values, value_type, [len(indices)]),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
# Line: 29

def _SparseTensor_4x6(self):
  # [0 |  |2 |  |4 |5 ]
  # [  |11|  |13|14|  ]
  # [20|  |  |23|  |25]
  # [30|  |32|33|  |35]
  ind = np.array([[0, 0], [0, 2], [0, 4], [0, 5], [1, 1], [1, 3], [1, 4],
                  [2, 0], [2, 3], [2, 5], [3, 0], [3, 2], [3, 3],
                  [3, 5]]).astype(np.int64)
  val = np.array(
      [0, 2, 4, 5, 11, 13, 14, 20, 23, 25, 30, 32, 33, 35]).astype(np.int64)
  shape = np.array([4, 6]).astype(np.int64)
  return sparse_tensor.SparseTensor(ind, val, shape)


# ==================================================
# Line: 42

def _SparseTensor_5x7(self):
  # [0 |  |2 |  |4 |5 |  ]
  # [  |11|  |13|14|  |16]
  # [20|  |  |23|  |25|  ]
  # [30|  |32|33|  |35|  ]
  # [  |41|  |  |44|  |46]
  ind = np.array([[0, 0], [0, 2], [0, 4], [0, 5], [1, 1], [1, 3], [1, 4],
                  [1, 6], [2, 0], [2, 3], [2, 5], [3, 0], [3, 2], [3, 3],
                  [3, 5], [4, 1], [4, 4], [4, 6]]).astype(np.int64)
  val = np.array(
      [0, 2, 4, 5, 11, 13, 14, 16, 20, 23, 25, 30, 32, 33, 35, 41, 44,
       46]).astype(np.int64)
  shape = np.array([5, 7]).astype(np.int64)
  return sparse_tensor.SparseTensor(ind, val, shape)


# ==================================================
# Line: 57

def _SparseTensorValue_3x4x2(self):
  #  slice(:,:, 0)
  #  ['a0'|    |'b0'|    ]
  #  [    |'c0'|    |'d0']
  #  [    |    |'e0'|    ]
  #  slice(:,:, 1)
  #  ['a1'|    |'b1'|    ]
  #  [    |'c1'|    |'d1']
  #  [    |    |'e1'|    ]
  ind = np.array([[0, 0, 0], [0, 0, 1], [0, 2, 0], [0, 2, 1], [1, 1, 0],
                  [1, 1, 1], [1, 3, 0], [1, 3, 1], [2, 2, 0],
                  [2, 2, 1]]).astype(np.int64)
  val = np.array(['a0', 'a1', 'b0', 'b1', 'c0', 'c1', 'd0', 'd1', 'e0', 'e1'])
  shape = np.array([3, 4, 2]).astype(np.int64)
  return sparse_tensor.SparseTensorValue(ind, val, shape)


# ==================================================
# Line: 77

def _SparseTensor_4x6_empty(self, val_dtype=np.int64):
  ind = np.empty(shape=(0, 2), dtype=np.int64)
  val = np.array([]).astype(val_dtype)
  shape = np.array([4, 6]).astype(np.int64)
  return sparse_tensor.SparseTensor(ind, val, shape)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_d9m_test.py
# Occurrences: Lines 78-82 (2 instances)

def _randomInts(self, shape, high, dtype):
  return constant_op.constant(
      np.random.randint(low=0, high=high, size=shape).astype(dtype))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_grad_test.py
# Line: 30

def _sparsify(self, x, indices_dtype=np.int64):
  x[x < 0.5] = 0

  non_zero = np.where(x)
  x_indices = np.vstack(non_zero).astype(indices_dtype).T
  x_values = x[non_zero]
  x_shape = x.shape

  return sparse_tensor.SparseTensor(
      indices=x_indices, values=x_values, dense_shape=x_shape), len(x_values)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
# Line: 30

def _SparseTensor_UnknownShape(self,
                               ind_shape=None,
                               val_shape=None,
                               shape_shape=None):
  return sparse_tensor.SparseTensor(
      array_ops.placeholder(
          dtypes.int64, shape=ind_shape),
      array_ops.placeholder(
          dtypes.float32, shape=val_shape),
      array_ops.placeholder(
          dtypes.int64, shape=shape_shape))


# ==================================================
# Line: 42

def _SparseTensorValue_3x3(self):
  # [    1]
  # [2    ]
  # [3   4]
  ind = np.array([[0, 2], [1, 0], [2, 0], [2, 2]])
  val = np.array([1, 2, 3, 4])
  shape = np.array([3, 3])
  return sparse_tensor.SparseTensorValue(
      np.array(ind, np.int64),
      np.array(val, np.float32), np.array(shape, np.int64))


# ==================================================
# Line: 56

def _SparseTensorValue_3x5(self):
  # [         ]
  # [  1      ]
  # [2     1 0]
  ind = np.array([[1, 1], [2, 0], [2, 3], [2, 4]])
  val = np.array([1, 2, 1, 0])
  shape = np.array([3, 5])
  return sparse_tensor.SparseTensorValue(
      np.array(ind, np.int64),
      np.array(val, np.float32), np.array(shape, np.int64))


# ==================================================
# Line: 70

def _SparseTensor_3x2(self):
  # [   ]
  # [1  ]
  # [2  ]
  ind = np.array([[1, 0], [2, 0]])
  val = np.array([1, 2])
  shape = np.array([3, 2])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtypes.float32),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 82

def _SparseTensor_2x3(self):
  # [  1  ]
  # [1   2]
  ind = np.array([[0, 1], [1, 0], [1, 2]])
  val = np.array([1, 1, 2])
  shape = np.array([2, 3])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtypes.float32),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 93

def _SparseTensor_2x3x4(self):
  ind = np.array([
      [0, 0, 1],
      [0, 1, 0], [0, 1, 2],
      [1, 0, 3],
      [1, 1, 1], [1, 1, 3],
      [1, 2, 2]])
  val = np.array([1, 10, 12, 103, 111, 113, 122])
  shape = np.array([2, 3, 4])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtypes.float32),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 107

def _SparseTensor_NoNonZeros(self, dense_shape):
  ind = np.empty(shape=(0, len(dense_shape)))
  val = np.array([])
  shape = np.array(dense_shape)
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtypes.float32),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 116

def _SparseTensor_String3x3(self):
  # [    a]
  # [b    ]
  # [c   d]
  ind = np.array([[0, 2], [1, 0], [2, 0], [2, 2]])
  val = np.array(["a", "b", "c", "d"])
  shape = np.array([3, 3])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtypes.string),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# Line: 128

def _SparseTensor_String3x5(self):
  # [         ]
  # [  e      ]
  # [f     g h]
  ind = np.array([[1, 1], [2, 0], [2, 3], [2, 4]])
  val = np.array(["e", "f", "g", "h"])
  shape = np.array([3, 5])
  return sparse_tensor.SparseTensor(
      constant_op.constant(ind, dtypes.int64),
      constant_op.constant(val, dtypes.string),
      constant_op.constant(shape, dtypes.int64))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
# Line: 32

def _SparseTensorPlaceholder(self, dtype=None):
  if dtype is None:
    dtype = dtypes.int32
  return sparse_tensor_lib.SparseTensor(
      array_ops.placeholder(dtypes.int64),
      array_ops.placeholder(dtype), array_ops.placeholder(dtypes.int64))


# ==================================================
# Line: 39

def _SparseTensorValue_5x6(self, permutation):
  ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2],
                  [3, 3]]).astype(np.int64)
  val = np.array([0, 10, 13, 14, 32, 33]).astype(np.int32)

  ind = ind[permutation]
  val = val[permutation]

  shape = np.array([5, 6]).astype(np.int64)
  return sparse_tensor_lib.SparseTensorValue(ind, val, shape)


# ==================================================
# Line: 50

def _SparseTensorValue_3x4(self, permutation):
  ind = np.array([[0, 0], [1, 0], [1, 2], [1, 3], [2, 2],
                  [2, 3]]).astype(np.int64)
  val = np.array([0, 10, 13, 14, 32, 33]).astype(np.int32)

  ind = ind[permutation]
  val = val[permutation]

  shape = np.array([3, 4]).astype(np.int64)
  return sparse_tensor_lib.SparseTensorValue(ind, val, shape)


# ==================================================
# Line: 61

def _SparseTensorValue_1x1x1(self):
  ind = np.array([[0, 0, 0]]).astype(np.int64)
  val = np.array([0]).astype(np.int32)
  shape = np.array([3, 4, 5]).astype(np.int64)
  return sparse_tensor_lib.SparseTensorValue(ind, val, shape)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
# Line: 32

def _SparseTensorPlaceholder(self):
  return sparse_tensor.SparseTensor(
      array_ops.placeholder(dtypes.int64),
      array_ops.placeholder(dtypes.float64),
      array_ops.placeholder(dtypes.int64))


# ==================================================
# Line: 38

def _SparseTensorValue_5x6(self):
  ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2],
                  [3, 3]]).astype(np.int64)
  val = np.array([0, 10, 13, 14, 32, 33]).astype(np.float64)
  shape = np.array([5, 6]).astype(np.int64)
  return sparse_tensor.SparseTensorValue(ind, val, shape)


# ==================================================
# Line: 45

def _SparseTensorValue_2x3x4(self):
  ind = np.array([[0, 0, 1], [0, 1, 0], [0, 1, 2], [1, 0, 3], [1, 1, 1],
                  [1, 1, 3], [1, 2, 2]])
  val = np.array([1, 10, 12, 103, 111, 113, 122])
  shape = np.array([2, 3, 4])
  return sparse_tensor.SparseTensorValue(ind, val, shape)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reorder_op_test.py
# Line: 36

def _SparseTensorPlaceholder(self):
  return sparse_tensor.SparseTensor(
      array_ops.placeholder(dtypes.int64),
      array_ops.placeholder(dtypes.float64),
      array_ops.placeholder(dtypes.int64))


# ==================================================
# Line: 42

def _SparseTensorValue_5x6(self, permutation, dtype=dtypes.float64):
  ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2],
                  [3, 3]]).astype(np.int64)
  val = np.array([0, 10, 13, 14, 32, 33]).astype(dtype.as_numpy_dtype)

  ind = ind[permutation]
  val = val[permutation]

  shape = np.array([5, 6]).astype(np.int64)
  return sparse_tensor.SparseTensorValue(ind, val, shape)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
# Line: 36

def _opFwdBwd(self, labels, logits):
  """Runs the op-under-test both forwards and backwards"""
  logits = ops_lib.convert_to_tensor(logits)  # needed for the gradient tape
  with backprop_lib.GradientTape() as tape:
    tape.watch(logits)
    loss = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
        labels=labels, logits=logits)
  return loss, tape.gradient(loss, logits)


# ==================================================
# Line: 45

def _npXent(self, labels, logits):
  logits = np.reshape(logits, [-1, logits.shape[-1]])
  labels = np.reshape(labels, [-1])
  batch_dim = 0
  class_dim = 1
  batch_size = logits.shape[batch_dim]
  e = np.exp(logits -
             np.reshape(np.amax(logits, axis=class_dim), [batch_size, 1]))
  probs = e / np.reshape(np.sum(e, axis=class_dim), [batch_size, 1])
  labels_mat = np.zeros_like(probs).astype(probs.dtype)
  labels_mat[np.arange(batch_size), labels] = 1.0
  gradient = (probs - labels_mat)
  loss = -np.sum(labels_mat * np.log(probs + 1.0e-20), axis=1)
  return loss, gradient


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/image_ops/draw_bounding_box_op_test.py
# Line: 33

def _fillBorder(self, image, color):
  """Fill the border of the image.

  Args:
    image: Numpy array of shape [height, width, depth].
    color: Numpy color of shape [depth] and either contents RGB/RGBA.

  Returns:
    image of original shape with border filled with "color".

  Raises:
    ValueError: Depths of image and color don"t match.
  """
  height, width, depth = image.shape
  if depth != color.shape[0]:
    raise ValueError("Image (%d) and color (%d) depths must match." %
                     (depth, color.shape[0]))
  image[0:height, 0, 0:depth] = color
  image[0:height, width - 1, 0:depth] = color
  image[0, 0:width, 0:depth] = color
  image[height - 1, 0:width, 0:depth] = color
  return image


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_compressed_op_test.py
# Line: 32

def _compress(self, bytes_in, compression_type):
  if not compression_type:
    return bytes_in
  elif compression_type == "ZLIB":
    return zlib.compress(bytes_in)
  elif compression_type == "ZSTD":
    return zstd.compress(bytes_in)
  else:
    out = io.BytesIO()
    with gzip.GzipFile(fileobj=out, mode="wb") as f:
      f.write(bytes_in)
    return out.getvalue()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# Line: 937

def _npMLP(self, xval, wsval, bsval):
  for i in range(wsval.shape[0]):
    xval = np.tanh(np.dot(xval, wsval[i, :]) + bsval[i, :])
  return xval


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
# Line: 1202

def testRandomOpsShape(self, random_fn, expected_shape):
  shape = constant_op.constant([3])

  def Body(i, u):
    shape_extended = array_ops.concat([[5], shape], axis=0)
    u = random_fn(shape_extended)
    assert u.shape.as_list() == expected_shape, str(u.shape.as_list())
    return i + 1, u

  _, _ = while_loop_v2(
      cond=lambda i, _: i < 3,
      body=Body,
      loop_vars=[
          0,
          array_ops.zeros(expected_shape, dtype=dtypes.float32),
      ])


# ==================================================
# Line: 1220

def testReshapeShape(self):
  shape = constant_op.constant([3, 4])

  def Body(i, u):
    shape_extended = array_ops.concat([[5], shape], axis=0)
    u = array_ops.reshape(u, [-1])
    assert u.shape.as_list() == [60], str(u.shape.as_list())
    u = array_ops.reshape(u, shape_extended)
    assert u.shape.as_list() == [5, 3, 4], str(u.shape.as_list())
    return i + 1, u

  _, _ = while_loop_v2(
      cond=lambda i, _: i < 3,
      body=Body,
      loop_vars=[
          0,
          array_ops.zeros([5, 3, 4], dtype=dtypes.float32),
      ])


# ==================================================
# Line: 1245

def testFillOpsShape(self, fill_fn):
  shape = constant_op.constant([3, 4])

  def Body(i, u):
    shape_extended = array_ops.concat([[5], shape], axis=0)
    u = fill_fn(shape_extended)
    assert u.shape.as_list() == [5, 3, 4], str(u.shape.as_list())
    return i + 1, u

  _, _ = while_loop_v2(
      cond=lambda i, _: i < 3,
      body=Body,
      loop_vars=[
          0,
          array_ops.zeros([5, 3, 4], dtype=dtypes.float32),
      ])


# ==================================================
# Line: 1298

def testDoNotAccumulateForwardTensorsForReductionOps(self):

  @def_function.function
  def Fn():
    with backprop.GradientTape() as tape:
      x = constant_op.constant(2.)
      tape.watch(x)

      def Body(i, x):
        forward_graph = ops.get_default_graph()

        @custom_gradient.custom_gradient
        def SquaredWithZeroGrad(x):

          def Grad(unused_g, variables=None):  # pylint: disable=redefined-outer-name
            del variables
            gradient_graph = ops.get_default_graph()
            shape = gen_array_ops.shape(x)
            assert shape.graph is forward_graph
            rank = gen_array_ops.rank(x)
            assert rank.graph is forward_graph
            size = gen_array_ops.size(x)
            assert size.graph is forward_graph
            zeros = array_ops.zeros(shape)
            assert zeros.graph is gradient_graph
            return zeros

          return x * 2, Grad

        return i + 1, SquaredWithZeroGrad(x)

      _, result = while_loop_v2(lambda i, _: i < 2, Body, [0, x])
    grad = tape.gradient(result, x)
    return grad

  Fn()


# ==================================================
# Line: 1335

def testDoNotAccumulateForwardTensorsForTensorListReductionOps(self):

  @def_function.function
  def Fn():
    with backprop.GradientTape() as tape:
      e = constant_op.constant(2.)
      x = list_ops.empty_tensor_list(
          element_dtype=dtypes.float32, element_shape=e.shape)
      x = list_ops.tensor_list_push_back(x, e)
      tape.watch(x)

      def Body(i, x):
        forward_graph = ops.get_default_graph()

        @custom_gradient.custom_gradient
        def IdentityWithZeroGrad(x):

          def Grad(unused_g, variables=None):  # pylint: disable=redefined-outer-name
            del variables
            gradient_graph = ops.get_default_graph()
            shape = gen_list_ops.tensor_list_element_shape(
                x, shape_type=dtypes.int32)
            assert shape.graph is forward_graph
            size = gen_list_ops.tensor_list_length(x)
            assert size.graph is forward_graph
            zeros = gen_list_ops.tensor_list_reserve(shape, size,
                                                     dtypes.float32)
            assert zeros.graph is gradient_graph
            return zeros

          return x, Grad

        return i + 1, IdentityWithZeroGrad(x)

      _, result = while_loop_v2(lambda i, _: i < 2, Body, [0, x])
    ones_like = list_ops.tensor_list_from_tensor(
        array_ops.ones_like(
            list_ops.tensor_list_stack(result, element_dtype=dtypes.float32)),
        element_shape=tensor_shape.TensorShape([]))
    grad = tape.gradient(result, x, output_gradients=[ones_like])
    return grad

  Fn()


# ==================================================
# Line: 1380

def testInheritParentNameScope(self):

  @def_function.function
  def F():
    with ops.name_scope("foo"):

      def Cond(unused_i):
        with ops.name_scope("cond"):
          actual_name_scope = ops.get_name_scope()
          expected_name_scope = "foo/while/cond"
          assert actual_name_scope == expected_name_scope, (
              "%s does not match %s" %
              (actual_name_scope, expected_name_scope))
        return False

      def Body(i):
        with ops.name_scope("body"):
          actual_name_scope = ops.get_name_scope()
          expected_name_scope = "foo/while/body"
          assert actual_name_scope == expected_name_scope, (
              "%s does not match %s" %
              (actual_name_scope, expected_name_scope))
        return i

      return while_v2.while_loop(Cond, Body, [0.])

  F()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py
# Line: 75

def build_test_graph(self) -> ops.Graph:
  g = ops.Graph()
  with g.as_default():

    def while_loop(x):

      def b(x):
        with ops.name_scope("NestedCond"):
          return cond.cond(
              math_ops.less(x, 100), lambda: math_ops.add(x, 1),
              lambda: math_ops.add(x, 2))

      c = lambda x: math_ops.less(x, 10000)
      with ops.name_scope("OuterWhile"):
        return while_loop_tf.while_loop(c, b, [x])

    x = array_ops.placeholder(dtypes.int32)
    with ops.name_scope("OuterCond"):
      cond.cond(
          math_ops.less(x, 1000), lambda: while_loop(x),
          lambda: math_ops.add(x, 2))
  return g


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Line: 1398

def testCondTensorDeps(self):
  t = array_ops.identity(1.)

  @eager_def_function.function
  def f():
    with ops.control_dependencies([t]):
      return array_ops.identity(2.)

  f.get_concrete_function()


# ==================================================
# Line: 2324

def testWhileShapeInvariantTensorSpec(self):
  i = constant_op.constant(0)
  x = constant_op.constant([1])
  c = lambda i, _: i < 10
  b = lambda i, x: (i + 1, array_ops_stack.stack([x, x]))
  shape_invariants = [
      tensor_lib.TensorSpec([], dtype=dtypes.int32),
      tensor_lib.TensorSpec(None, dtype=dtypes.int32)]
  while_loop_tf.while_loop(c, b, [i, x], shape_invariants)


# ==================================================
# Line: 4681

def _buildWhileWithShapeInvariants(self, shape_invariants):
  r = constant_op.constant([1, 2])

  def cond(_):
    return False

  def body(_):
    return constant_op.constant([1])

  return while_loop_tf.while_loop(
      cond, body, [r], shape_invariants=shape_invariants)


# ==================================================
# Line: 4721

def _getWhileTensor(self):
  """Creates and returns a tensor from a while context."""
  tensor = []

  def body(i):
    if not tensor:
      tensor.append(constant_op.constant(1))
    return i + tensor[0]

  while_loop_tf.while_loop(lambda i: i < 10, body, [0])
  return tensor[0]


# ==================================================
# Line: 4733

def _getCondTensor(self):
  cond_tensor = []

  def true_fn():
    if not cond_tensor:
      cond_tensor.append(constant_op.constant(1))
    return cond_tensor[0]

  tf_cond.cond(
      math_ops.less(1, 2), true_fn, lambda: constant_op.constant(0))
  return cond_tensor[0]


# ==================================================
# Line: 4791

def testValidCondContextBranches(self):
  # Accessing a tensor from a cond context from the other branch's cond
  # context is OK (although dangerous).
  cond_tensor = []

  def branch_fn():
    if not cond_tensor:
      cond_tensor.append(constant_op.constant(1))
    return cond_tensor[0]

  tf_cond.cond(math_ops.less(1, 2), branch_fn, branch_fn)


# ==================================================
# Line: 4804

def testValidWhileContext(self):
  # Accessing a tensor in a nested while is OK.
  def body(_):
    c = constant_op.constant(1)
    return while_loop_tf.while_loop(lambda i: i < 3, lambda i: i + c, [0])

  while_loop_tf.while_loop(lambda i: i < 5, body, [0])


# ==================================================
# Line: 4979

def _getInitVariables(self):
  batch_size = 10
  image_size = 256
  kernel_size = 3
  depth = 16

  init_step = constant_op.constant(-1)
  image = variable_scope.get_variable(
      "image",
      initializer=random_ops.random_normal(
          [batch_size, image_size, image_size, depth],
          dtype=dtypes.float32,
          stddev=1e-1))
  kernel = variable_scope.get_variable(
      "weights",
      initializer=random_ops.truncated_normal(
          [kernel_size, kernel_size, depth, depth],
          dtype=dtypes.float32,
          stddev=1e-1))
  return init_step, image, kernel


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
# Line: 1458

def testNCCLFallbackOnCPU(self, collective_op):
  # communication_hint=NCCL should work for CPU by falling back to RING. The
  # test doesn't actually require GPU, only GPU builds. We specify
  # required_gpus=1 so that it's tested with GPU builds.
  dev0 = '/device:CPU:0'
  dev1 = '/device:CPU:1'
  group_key = 20
  instance_key = 30
  input_data = constant_op.constant([1., 2., 3., 4.])

  tokens = {}
  for device in [dev0, dev1]:
    with ops.device(device):
      tokens[device] = create_ordering_token()

  @def_function.function
  def run():
    for device in [dev0, dev1]:
      with ops.device(device):
        collective_op(
            input_data,
            group_size=2,
            group_key=group_key,
            instance_key=instance_key,
            ordering_token=tokens[device],
            communication_hint='NCCL')

  run()



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/proto/descriptor_source_test_base.py
# Line: 50

def _createDescriptorProto(self):
  proto = FileDescriptorSet()

  file_proto = proto.file.add(
      name='types.proto', package='tensorflow', syntax='proto3')
  enum_proto = file_proto.enum_type.add(name='DataType')
  enum_proto.value.add(name='DT_DOUBLE', number=0)
  enum_proto.value.add(name='DT_BOOL', number=1)

  file_proto = proto.file.add(
      name='test_example.proto',
      package='tensorflow.contrib.proto',
      dependency=['types.proto'])
  message_proto = file_proto.message_type.add(name='TestCase')
  message_proto.field.add(
      name='values',
      number=1,
      type=FieldDescriptorProto.TYPE_MESSAGE,
      type_name='.tensorflow.contrib.proto.TestValue',
      label=FieldDescriptorProto.LABEL_REPEATED)
  message_proto.field.add(
      name='shapes',
      number=2,
      type=FieldDescriptorProto.TYPE_INT32,
      label=FieldDescriptorProto.LABEL_REPEATED)
  message_proto.field.add(
      name='sizes',
      number=3,
      type=FieldDescriptorProto.TYPE_INT32,
      label=FieldDescriptorProto.LABEL_REPEATED)
  message_proto.field.add(
      name='fields',
      number=4,
      type=FieldDescriptorProto.TYPE_MESSAGE,
      type_name='.tensorflow.contrib.proto.FieldSpec',
      label=FieldDescriptorProto.LABEL_REPEATED)

  message_proto = file_proto.message_type.add(
      name='TestValue')
  message_proto.field.add(
      name='double_value',
      number=1,
      type=FieldDescriptorProto.TYPE_DOUBLE,
      label=FieldDescriptorProto.LABEL_REPEATED)
  message_proto.field.add(
      name='bool_value',
      number=2,
      type=FieldDescriptorProto.TYPE_BOOL,
      label=FieldDescriptorProto.LABEL_REPEATED)

  message_proto = file_proto.message_type.add(
      name='FieldSpec')
  message_proto.field.add(
      name='name',
      number=1,
      type=FieldDescriptorProto.TYPE_STRING,
      label=FieldDescriptorProto.LABEL_OPTIONAL)
  message_proto.field.add(
      name='dtype',
      number=2,
      type=FieldDescriptorProto.TYPE_ENUM,
      type_name='.tensorflow.DataType',
      label=FieldDescriptorProto.LABEL_OPTIONAL)
  message_proto.field.add(
      name='value',
      number=3,
      type=FieldDescriptorProto.TYPE_MESSAGE,
      type_name='.tensorflow.contrib.proto.TestValue',
      label=FieldDescriptorProto.LABEL_OPTIONAL)

  return proto


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
# Line: 1308

def testGetVariableWithRefDtype(self):
  v = variable_scope.get_variable("v", shape=[3, 4], dtype=dtypes.float32)
  # Ensure it is possible to do get_variable with a _ref dtype passed in.
  _ = variable_scope.get_variable("w", shape=[5, 6], dtype=v.dtype)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
# Occurrences: Lines 73-76 (2 instances)

def get_gradient_components(self, value):
  return value._type_spec._to_components(value)


# ==================================================
# Line: 308

def testDifferentAssignGraph(self):
  with ops.Graph().as_default():
    v = resource_variable_ops.ResourceVariable(1.0)
  ops.reset_default_graph()
  v.assign(2.0)  # Note: this fails if we run convert_to_tensor on not the
  # variable graph.


# ==================================================
# Line: 1563

def create_variant_shape_and_type_data(self):
  variant_shape_and_type_data = (
      cpp_shape_inference_pb2.CppShapeInferenceResult.HandleData())
  variant_shape_and_type_data.is_set = True
  stored_shape = tensor_shape.TensorShape([None, 4]).as_proto()
  stored_dtype = dtypes.float32.as_datatype_enum
  # NOTE(ebrevdo): shape_and_type lacks append() in some versions of protobuf.
  variant_shape_and_type_data.shape_and_type.extend([
      cpp_shape_inference_pb2.CppShapeInferenceResult.HandleShapeAndType(
          shape=stored_shape,
          dtype=stored_dtype,
          type=full_type_pb2.FullTypeDef())
  ])
  return variant_shape_and_type_data


# ==================================================
# Line: 1579

def create_constant_variant(self, value):
  value = constant_op.constant(
      tensor_pb2.TensorProto(
          dtype=dtypes.variant.as_datatype_enum,
          tensor_shape=tensor_shape.TensorShape([]).as_proto(),
          variant_val=[
              tensor_pb2.VariantTensorDataProto(
                  # Match registration in variant_op_registry.cc
                  type_name=b"int",
                  metadata=np.array(value, dtype=np.int32).tobytes())
          ]))
  return value


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/types/trace.py
# Line: 200

def to_tensors(self, value: Any) -> List[core.Tensor]:
  """Breaks down a value of this type into Tensors.

  For a TraceType instance, the number of tensors generated for corresponding
  value should be constant.

  Args:
    value: A value belonging to this TraceType

  Returns:
    List of Tensors.
  """
  del value
  return []


# ==================================================
# Line: 229

def flatten(self) -> List["TraceType"]:
  """Returns a list of TensorSpecs corresponding to `to_tensors` values."""
  return []


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/timeline.py
# Line: 67

def _create_event(
    self,
    ph: str,
    category: str,
    name: str,
    pid: int,
    tid: int,
    timestamp: int,

# ==================================================
# Line: 454

def _parse_op_label(
    self, label: str

# ==================================================
# Line: 469

def _parse_kernel_label(self, label, node_name):
  """Parses the fields in a node timeline label."""
  # Expects labels of the form: retval (arg) detail @@annotation
  start = label.find('@@')
  end = label.find('#')
  if start >= 0 and end >= 0 and start + 2 < end:
    node_name = label[start + 2 : end]
  # Node names should always have the form 'name:op'.
  fields = node_name.split(':') + ['unknown']
  name, op = fields[:2]
  return name, op


# ==================================================
# Line: 570

def _is_gputrace_device(self, device_name: str) -> bool:
  """Returns true if this device is part of the GPUTracer logging."""
  return '/stream:' in device_name or '/memcpy' in device_name


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/session.py
# Line: 517

def _assert_fetchable(self, graph, op):
  if not graph.is_fetchable(op):
    raise errors.InaccessibleTensorError(
        f'Operation {op.name} has been marked as not fetchable. Typically '
        'this happens when it is defined in another function or code block. '
        'Use return values, explicit Python locals or TensorFlow collections '
        'to access it.')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/virtual_gpu_test.py
# Line: 111

def _LogMatrix(self, mat, dim):
  logging.info('---- printing the first 10*10 submatrix ----')
  for i in range(min(10, dim)):
    row = ''
    for j in range(min(10, dim)):
      row += ' ' + str(mat[i][j])
    logging.info(row)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/session_test.py
# Line: 1830

def testInteractiveSessionNesting(self):
  sess1 = session.InteractiveSession()
  sess2 = session.InteractiveSession()
  del sess1
  del sess2


# ==================================================
# Occurrences: Lines 2089-2094 (2 instances)

def testOpenAndCloseGrpcSession(self):
  server = server_lib.Server.create_local_server()
  with session.Session(server.target):
    pass


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/map_op.py
# Line: 182

def _transformation_name(self):
  return "Dataset.map()"



# ==================================================
# Line: 237

def _transformation_name(self):
  return "Dataset.map()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# Line: 270

def _variant_tensor(self, _):
  raise ValueError("The `_variant_tensor` property cannot be modified.")


# ==================================================
# Occurrences: Lines 425-430 (2 instances)

def _graph(self, _):
  raise ValueError("The `_graph` property cannot be modified.")


# ==================================================
# Line: 845

def _normalize_id(self, iterator_id):
  # In debug mode, iterator ids may be eagerly-generated np.arrays instead
  # of Tensors. We convert them to scalars to make them hashable.
  if isinstance(iterator_id, np.ndarray):
    return iterator_id.item()
  return iterator_id


# ==================================================
# Line: 4697

def _to_components(self, value):
  return value._variant_tensor  # pylint: disable=protected-access


# ==================================================
# Line: 4707

def _to_tensor_list(self, value):
  return [
      ops.convert_to_tensor(
          tf_nest.map_structure(lambda x: x._variant_tensor, value))  # pylint: disable=protected-access
  ]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/flat_map_op.py
# Line: 56

def _transformation_name(self):
  return "Dataset.flat_map()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/interleave_op.py
# Line: 99

def _transformation_name(self):
  return "Dataset.interleave()"



# ==================================================
# Line: 169

def _transformation_name(self):
  return "Dataset.interleave()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/iterator_ops.py
# Line: 967

def _to_components(self, value):
  return (value._iterator_resource,)  # pylint: disable=protected-access


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/optional_ops.py
# Line: 246

def _to_components(self, value):
  return [value._variant_tensor]  # pylint: disable=protected-access


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
# Line: 158

def _inputs(self):
  # TODO(b/116506223): Determine which datasets should be used as inputs here.
  return []


# ==================================================
# Line: 202

def _inputs(self):
  # TODO(b/116506223): Determine which datasets should be used as inputs here.
  return []


# ==================================================
# Line: 402

def _to_components(self, value):
  # pylint: disable=protected-access
  c = [value._multi_device_iterator_resource]
  c.extend(value._device_iterators)
  return c


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/readers.py
# Line: 386

def _transformation_name(self):
  return "tf.data.experimental.parallel_interleave()"



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/snapshot_op.py
# Line: 118

def _transformation_name(self):
  return "Dataset.snapshot()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/scan_op.py
# Line: 159

def _transformation_name(self):
  return "Dataset.scan()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/range_op.py
# Line: 65

def _build_tensor(self, int64_value, name):
  return ops.convert_to_tensor(int64_value, dtype=dtypes.int64, name=name)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/filter_op.py
# Line: 60

def _transformation_name(self):
  return "Dataset.filter()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/from_generator_op.py
# Line: 399

def _transformation_name(self):
  return "Dataset.from_generator()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/group_by_window_op.py
# Line: 131

def _transformation_name(self):
  return "Dataset.group_by_window()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/ops/take_while_op.py
# Line: 57

def _transformation_name(self):
  return "Dataset.take_while()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/nest_test.py
# Line: 45

def __tf_unflatten__(self, metadata, components):
  mask = metadata[0]
  value = components[0]
  return MaskedTensor(mask=mask, value=value)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/util/structure_test.py
# Line: 506

def __tf_unflatten__(self, metadata, components):
  mask = metadata[0]
  value = components[0]
  return MaskedTensor(mask=mask, value=value)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
# Line: 537

def _build_shuffle_dataset(
    self,
    range_limit=10,
    num_repeats=5,
    buffer_size=5,
    seed=None,
    reshuffle_each_iteration=None,
    symbolic_checkpoint=None,

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py
# Line: 167

def _build_ds(self):
  components = np.array([1., 2., 3., np.nan, 5.]).astype(np.float32)

  dataset = dataset_ops.Dataset.from_tensor_slices(components)
  dataset = dataset.map(lambda x: array_ops.check_numerics(x, "message"))
  dataset = dataset.ignore_errors()
  options = options_lib.Options()
  options.experimental_external_state_policy = (
      options_lib.ExternalStatePolicy.IGNORE)
  return dataset.with_options(options)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
# Line: 59

def __tf_unflatten__(self, metadata, components):
  mask = metadata[0]
  value1, value2 = components
  return MaskedNdarrayPair(mask=mask, value1=value1, value2=value2)



# ==================================================
# Line: 214

def _build_dataset(self, arr, options=None):
  components = [
      np.tile(np.array([[1], [2], [3], [4]]), 20),
      np.tile(np.array([[12], [13], [14], [15]]), 22),
      np.array(arr)
  ]
  datasets = [
      dataset_ops.Dataset.from_tensor_slices(component)
      for component in components
  ]
  dataset = dataset_ops.Dataset.zip((datasets[0], (datasets[1], datasets[2])))
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/skip_test.py
# Line: 58

def _build_skip_dataset(self, count, options=None):
  dataset = dataset_ops.Dataset.range(100).skip(count)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
# Line: 61

def __tf_unflatten__(self, metadata, components):
  mask = metadata[0]
  value = components[0]
  return MaskedTensor(mask=mask, value=value)



# ==================================================
# Line: 330

def _build_tensor_dataset(self, variable_array, options=None):
  components = (variable_array, np.array([1, 2, 3]), np.array(37.0))
  dataset = dataset_ops.Dataset.from_tensors(components)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/choose_from_datasets_test.py
# Line: 141

def _build_dataset(self,
                   num_datasets,
                   num_elements_per_dataset,
                   options=None):
  datasets = [
      dataset_ops.Dataset.range(num_elements_per_dataset)
      for _ in range(num_datasets)
  ]
  indices = []
  for i in range(num_datasets):
    indices = indices + ([i] * num_elements_per_dataset)
  shuffled_indices = stateless_random_ops.stateless_shuffle(
      np.int64(indices), seed=[1, 2])
  choice_dataset = dataset_ops.Dataset.from_tensor_slices(shuffled_indices)
  dataset = dataset_ops.Dataset.choose_from_datasets(datasets, choice_dataset)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
# Line: 84

def _build_repeat_dataset(self,
                          num_elements,
                          num_epochs,
                          num_outputs=None,
                          options=None):
  dataset = dataset_ops.Dataset.range(num_elements).repeat(num_epochs)
  if num_outputs:
    range_dataset = dataset_ops.Dataset.range(num_outputs)
    dataset = dataset_ops.Dataset.zip((dataset, range_dataset))
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
# Line: 40

def _dynamicPad(self, bucket, window, window_size):
  # TODO(mrry): To match `tf.contrib.training.bucket()`, implement a
  # generic form of padded_batch that pads every component
  # dynamically and does not rely on static shape information about
  # the arguments.
  return dataset_ops.Dataset.zip(
      (dataset_ops.Dataset.from_tensors(bucket),
       window.padded_batch(
           32, (tensor_shape.TensorShape([]), tensor_shape.TensorShape(
               [None]), tensor_shape.TensorShape([3])))))


# ==================================================
# Line: 357

def _build_dataset(self, components):
  dataset = dataset_ops.Dataset.from_tensor_slices(components).repeat(-1)
  dataset = dataset.group_by_window(
      key_func=lambda x: x % 3,
      reduce_func=lambda _, xs: xs.batch(4),
      window_size=4)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
# Line: 184

def _build_filter_range_dataset(self, div, options=None):
  dataset = dataset_ops.Dataset.range(100).filter(
      lambda x: math_ops.not_equal(math_ops.mod(x, div), 2))
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# Line: 204

def _build_filter_dict_dataset(self):
  return dataset_ops.Dataset.range(10).map(lambda x: {
      "foo": x * 2,
      "bar": x**2
  }).filter(lambda d: math_ops.equal(d["bar"] % 2, 0)).map(
      lambda d: d["foo"] + d["bar"])


# ==================================================
# Line: 218

def _build_sparse_filter_dataset(self):

  def _map_fn(i):
    return sparse_tensor.SparseTensor(
        indices=[[0, 0]], values=(i * [1]), dense_shape=[1, 1]), i

  def _filter_fn(_, i):
    return math_ops.equal(i % 2, 0)

  return dataset_ops.Dataset.range(10).map(_map_fn).filter(_filter_fn).map(
      lambda x, i: x)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
# Line: 258

def _build_dataset(self):
  dataset = dataset_ops.Dataset.range(42).window(6).interleave(
      lambda x: x, cycle_length=2, num_parallel_calls=2)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/range_test.py
# Line: 153

def _build_range_dataset(self, start, stop, options=None):
  dataset = dataset_ops.Dataset.range(start, stop)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
# Line: 374

def _build_tensor_slices_dataset(self, components, options=None):
  dataset = dataset_ops.Dataset.from_tensor_slices(components)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py
# Line: 131

def _build_dataset(self, num_elements, upper_bound, options=None):
  dataset = dataset_ops.Dataset.range(num_elements)
  dataset = dataset.take_while(predicate=lambda x: x < upper_bound)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
# Line: 92

def _get_keywords(self, f, r):
  num_keywords = 1 + (f + r) % 2
  keywords = []
  for index in range(num_keywords):
    keywords.append(compat.as_bytes("keyword%d" % index))
  return keywords


# ==================================================
# Line: 137

def _interleave(self, iterators, cycle_length):
  pending_iterators = iterators
  open_iterators = []
  num_open = 0
  for i in range(cycle_length):
    if pending_iterators:
      open_iterators.append(pending_iterators.pop(0))
      num_open += 1

  while num_open:
    for i in range(min(cycle_length, len(open_iterators))):
      if open_iterators[i] is None:
        continue
      try:
        yield next(open_iterators[i])
      except StopIteration:
        if pending_iterators:
          open_iterators[i] = pending_iterators.pop(0)
        else:
          open_iterators[i] = None
          num_open -= 1


# ==================================================
# Line: 247

def _interleave(self, iterators, cycle_length):
  pending_iterators = iterators
  open_iterators = []
  num_open = 0
  for i in range(cycle_length):
    if pending_iterators:
      open_iterators.append(pending_iterators.pop(0))
      num_open += 1

  while num_open:
    for i in range(min(cycle_length, len(open_iterators))):
      if open_iterators[i] is None:
        continue
      try:
        yield next(open_iterators[i])
      except StopIteration:
        if pending_iterators:
          open_iterators[i] = pending_iterators.pop(0)
        else:
          open_iterators[i] = None
          num_open -= 1


# ==================================================
# Line: 317

def _record(self, f, r):
  return compat.as_bytes("Record %d of file %d" % (r, f))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/dataset_spec_test.py
# Line: 33

def testInputSignature(self):
  dataset = dataset_ops.Dataset.from_tensor_slices(
      np.arange(10).astype(np.int32)).batch(5)

  @def_function.function(input_signature=[
      dataset_ops.DatasetSpec(
          tensor_spec.TensorSpec(
              shape=(None,), dtype=dtypes.int32, name=None),
          tensor_shape.TensorShape([]))
  ])
  def fn(_):
    pass

  fn(dataset)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
# Line: 234

def build_dataset(self,
                  multiplier=15.0,
                  tensor_slice_len=2,
                  batch_size=2,
                  options=None):
  components = (np.arange(tensor_slice_len), np.array([[1, 2, 3]]) *
                np.arange(tensor_slice_len)[:, np.newaxis],
                np.array(multiplier) * np.arange(tensor_slice_len))

  dataset = dataset_ops.Dataset.from_tensor_slices(components).batch(
      batch_size).unbatch()
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
# Line: 335

def testNoneDataset(self):
  # Some datasets, e.g. datasets with None tensors, have components without
  # output shapes. Test that this doesn't break rebatching shape inference
  # logic.
  dataset = dataset_ops.Dataset.range(4)
  dataset = dataset.map(lambda x: (x, None))
  dataset = dataset.batch(4, drop_remainder=True)
  _ = dataset.rebatch(batch_size=[2, 2])



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
# Line: 342

def keyValueTensorInitializer(self, vals):
  keys_tensor = constant_op.constant(
      list(range(len(vals))), dtype=dtypes.int64)
  vals_tensor = constant_op.constant(vals)
  return lookup_ops.KeyValueTensorInitializer(keys_tensor, vals_tensor)


# ==================================================
# Line: 348

def datasetInitializer(self, vals):
  keys = dataset_ops.Dataset.range(len(vals))
  values = dataset_ops.Dataset.from_tensor_slices(vals)
  ds = dataset_ops.Dataset.zip((keys, values))
  return data_lookup_ops.DatasetInitializer(ds)


# ==================================================
# Line: 371

def graphRoundTrip(self, dataset, allow_stateful=False):
  """Converts a dataset to a graph and back."""
  graph = gen_dataset_ops.dataset_to_graph(
      dataset._variant_tensor, allow_stateful=allow_stateful)  # pylint: disable=protected-access
  return dataset_ops.from_variant(
      gen_experimental_dataset_ops.dataset_from_graph(graph),
      dataset.element_spec)


# ==================================================
# Line: 424

def configureDevicesForMultiDeviceTest(self, num_devices):
  """Configures number of logical devices for multi-device tests.

  It returns a list of device names. If invoked in GPU-enabled runtime, the
  last device name will be for a GPU device. Otherwise, all device names will
  be for a CPU device.

  Args:
    num_devices: The number of devices to configure.

  Returns:
    A list of device names to use for a multi-device test.
  """
  cpus = config.list_physical_devices("CPU")
  gpus = config.list_physical_devices("GPU")
  config.set_logical_device_configuration(cpus[0], [
      context.LogicalDeviceConfiguration() for _ in range(num_devices)
  ])
  devices = ["/device:CPU:" + str(i) for i in range(num_devices - 1)]
  if gpus:
    devices.append("/device:GPU:0")
  else:
    devices.append("/device:CPU:" + str(num_devices - 1))
  return devices

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
# Line: 568

def gen_break_points(self, num_outputs, num_samples=10):
  """Generates `num_samples` unique break points in [0, num_outputs]."""
  return np.unique(np.linspace(0, num_outputs, num_samples, dtype=int))


# ==================================================
# Occurrences: Lines 633-643 (3 instances)

def _get_output_types(self, ds_fn):
  assert not context.executing_eagerly()
  with ops.Graph().as_default():
    return dataset_ops.get_legacy_output_types(ds_fn())


# ==================================================
# Line: 661

def _initialize(self, init_op, sess):
  sess.run(variables.global_variables_initializer())
  sess.run(lookup_ops.tables_initializer())
  sess.run(init_op)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
# Line: 37

def _dataset_factory(self,
                     filenames,
                     compression_type="",
                     num_epochs=1,
                     batch_size=None):

  repeat_dataset = readers.TFRecordDataset(
      filenames, compression_type).repeat(num_epochs)
  if batch_size:
    return repeat_dataset.batch(batch_size)
  return repeat_dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py
# Line: 117

def build_dataset(self, options=None):
  dataset = dataset_ops.Dataset.range(100).prefetch(10)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
# Line: 135

def testId(self):
  # Ideally, placer should know that Identity(dataset) should be on the same
  # device as the dataset.
  @def_function.function
  def f():
    dataset = dataset_ops.Dataset.range(10)
    dataset = array_ops.identity(dataset)
    return dataset
  f()


# ==================================================
# Line: 191

def testCreateIteratorInFuncOnGpu(self):

  @def_function.function
  def create_iter():
    return gen_dataset_ops.anonymous_iterator_v2(
        output_types=[dtypes.float32], output_shapes=[[]])

  create_iter()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/take_test.py
# Line: 57

def _build_take_dataset(self, count, options=None):
  dataset = dataset_ops.Dataset.range(100).take(count)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/enumerate_test.py
# Line: 53

def _build_enumerate_dataset(self, start, stop, options=None):
  dataset = dataset_ops.Dataset.range(start, stop).enumerate()
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
# Line: 168

def _build_concatenate_dataset(self, var_array, options=None):
  input_components = (np.tile(np.array([[1], [2], [3], [4]]), 20),
                      np.tile(np.array([[12], [13], [14], [15]]), 4))
  to_concatenate_components = (np.tile(
      np.array([[5], [6], [7], [8], [9]]), 20), var_array)

  dataset = dataset_ops.Dataset.from_tensor_slices(
      input_components).concatenate(
          dataset_ops.Dataset.from_tensor_slices(to_concatenate_components))
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
# Line: 147

def _build_random_dataset(
    self,
    num_elements=10,
    seed=None,
    rerandomize_each_iteration=None):
  dataset = dataset_ops.Dataset.random(
      seed=seed, rerandomize_each_iteration=rerandomize_each_iteration)
  # Checkpoint tests need the test dataset to be finite whereas `random` is
  # infinite. Use `take` to limit the number of elements.
  return dataset.take(num_elements)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
# Line: 556

def testWithInputThatPurgeCheckpoint(self):
  """Tests underlying `expired_prefixes` are handled correctly.

  Explanation:
      The input for `interleave` looks like (created by `.repeat`):
      [0, |1, |2]
          ^   ^
          |   |
          |   expired_prefixes=["FiniteRepeat[1]"]
          expired_prefixes=["FiniteRepeat[0]"]

      [0]   [1]
       0     1    <--- expired_prefixes=["...FiniteRepeat[0]"]
      EOF   EOF
       2 <----- Tests the previous checkpoint stored at this index
                should not have an effect on the new checkpoint.

      EOF
  """
  options = options_lib.Options()
  options.experimental_symbolic_checkpoint = True
  options.experimental_optimization.inject_prefetch = False
  options.experimental_optimization.apply_default_optimizations = False

  def carefully_designed_map(x):
    if x == 0:
      return dataset_ops.Dataset.from_tensor_slices([0])
    elif x == 1:
      return dataset_ops.Dataset.from_tensor_slices([1])
    else:
      return dataset_ops.Dataset.from_tensor_slices([2])

  def _build_dataset():
    dataset = dataset_ops.Dataset.from_tensor_slices(["does not matter"])

    # Create [0, 1, 2] using repeat+enumerate+map
    dataset = dataset.repeat(3)
    dataset = dataset.enumerate()
    dataset = dataset.map(lambda idx, x: idx)

    dataset = dataset.interleave(
        carefully_designed_map,
        cycle_length=2,
        block_length=1,
        num_parallel_calls=None,
    )
    dataset = dataset.with_options(options)
    return dataset

  dataset = _build_dataset().with_options(options)

  it = dataset.as_numpy_iterator()

  try:
    for _ in range(4):
      next(it)
  except StopIteration:
    pass

  # should not crash
  it.save().numpy()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/counter_test.py
# Line: 48

def _build_counter_dataset(self, start, step, num_outputs, options=None):
  counter_dataset = dataset_ops.Dataset.counter(start, step)
  range_dataset = dataset_ops.Dataset.range(num_outputs)
  dataset = dataset_ops.Dataset.zip((counter_dataset, range_dataset))
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
# Line: 151

  def testImplicitDisposeParallelMapDataset(self):
    # Tests whether a parallel map dataset will be cleaned up correctly when
    # the pipeline does not run it until exhaustion.
    # The pipeline is TensorSliceDataset -> MapDataset(square_3) ->
    # RepeatDataset(None) -> PrefetchDataset(100).
    worker, _ = test_util.create_local_cluster(1, 1)

    components = (np.arange(1000),
                  np.array([[1, 2, 3]]) * np.arange(1000)[:, np.newaxis],
                  np.array(37.0) * np.arange(1000))

    def _map_fn(x, y, z):
      return math_ops.square(x), math_ops.square(y), math_ops.square(z)

    dataset = (
        dataset_ops.Dataset.from_tensor_slices(components).map(_map_fn)
        .repeat(None).prefetch(10000))

    iterator = dataset_ops.make_initializable_iterator(dataset)
    init_op = iterator.initializer
    get_next = iterator.get_next()

    with session.Session(worker[0].target) as sess:
      sess.run(init_op)
      for _ in range(3):
        sess.run(get_next)


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
# Line: 349

def __next__(self):
  return 42


# ==================================================
# Line: 516

  def testName(self):

    def generator():
      yield 42

    dataset_ops.Dataset.from_generator(
        generator,
        output_types=(dtypes.int64),
        output_shapes=[1],
        name="from_generator")


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/shard_test.py
# Line: 108

def _build_dataset(self, num_elements, num_shards, index, options=None):
  dataset = dataset_ops.Dataset.range(num_elements).shard(num_shards, index)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py
# Line: 46

def assertMemoryNotIncreasing(self, f, num_iters, max_increase_mb):
  """Assert memory usage doesn't increase beyond given threshold for f."""

  # Warm up.
  f()
  # Wait for background threads to start up and allocate memory.
  time.sleep(4)
  initial = memory_profiler.memory_usage(-1)[0]
  for _ in range(num_iters):
    f()
  increase = memory_profiler.memory_usage(-1)[0] - initial
  logging.info("Memory increase observed: %f MB" % increase)
  assert increase < max_increase_mb, (
      "Increase is too high. Initial memory usage: %f MB. Increase: %f MB. "
      "Maximum allowed increase: %f") % (initial, increase, max_increase_mb)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
# Line: 44

def _lineText(self, f, l):
  return compat.as_bytes("%d: %d" % (f, l))


# ==================================================
# Line: 237

def _build_iterator_graph(
    self, test_filenames, symbolic_checkpoint, compression_type=None

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
# Line: 46

def _counting_dataset(self, start, scan_fn):
  return dataset_ops.Dataset.from_tensors(0).repeat().scan(
      initial_state=start, scan_func=scan_fn)


# ==================================================
# Line: 305

def _build_dataset(self, num_elements, symbolic_checkpoint):
  dataset = dataset_ops.Dataset.from_tensors(1).repeat(num_elements)
  dataset = dataset.scan(
      initial_state=[0, 1],
      scan_func=lambda a, _: ([a[1], a[0] + a[1]], a[1]))
  options = options_lib.Options()
  options.experimental_symbolic_checkpoint = symbolic_checkpoint
  return dataset.with_options(options)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/sparse_batch_test.py
# Line: 108

def _build_dataset(self, components):
  return dataset_ops.Dataset.from_tensor_slices(components).map(
      lambda x: array_ops.fill([x], x)).sparse_batch(4, [12])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/from_sparse_tensor_slices_test.py
# Line: 165

def _build_sparse_tensor_slice_dataset(self, slices):
  # pylint: disable=g-complex-comprehension
  indices = np.array(
      [[i, j] for i in range(len(slices)) for j in range(len(slices[i]))],
      dtype=np.int64)
  values = np.array([val for s in slices for val in s], dtype=np.float64)
  # pylint: enable=g-complex-comprehension
  dense_shape = np.array(
      [len(slices), max(len(s) for s in slices) + 1], dtype=np.int64)
  sparse_components = sparse_tensor.SparseTensor(indices, values, dense_shape)
  return dataset_ops.Dataset.from_sparse_tensor_slices(sparse_components)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
# Occurrences: Lines 46-49 (2 instances)

def _normalize(self, vec):
  return vec / vec.sum()


# ==================================================
# Line: 301

def _build_dataset(self, probs, num_samples, options=None):
  datasets = [
      dataset_ops.Dataset.from_tensors(i).repeat(None)
      for i in range(len(probs))
  ]
  dataset = dataset_ops.Dataset.sample_from_datasets(
      datasets, probs, seed=1813)
  dataset = dataset.take(num_samples)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
# Line: 305

def _build_dataset(self,
                   multiplier=15.0,
                   tensor_slice_len=2,
                   batch_size=2,
                   num_parallel_calls=None,
                   options=None):
  components = (np.arange(tensor_slice_len), np.array([[1, 2, 3]]) *
                np.arange(tensor_slice_len)[:, np.newaxis],
                np.array(multiplier) * np.arange(tensor_slice_len))

  dataset = dataset_ops.Dataset.from_tensor_slices(components)
  dataset = dataset.batch(batch_size, num_parallel_calls=num_parallel_calls)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# Line: 344

def _sparse(self, i):
  return sparse_tensor.SparseTensorValue(
      indices=[[0]], values=(i * [1]), dense_shape=[1])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/ops/grouping.py
# Line: 384

def _transformation_name(self):
  return "tf.data.experimental.group_by_reducer()"



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/ops/weighted_flat_map_op.py
# Line: 161

def _transformation_name(self):
  return "Dataset.weighted_flat_map()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/ops/index_flat_map_op.py
# Line: 143

def _transformation_name(self) -> str:
  return "Dataset.index_flat_map()"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
# Line: 262

def _transformation_name(self):
  return "map_on_gpu()"



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
# Line: 58

def testStartDispatcher(self):
  dispatcher = server_lib.DispatchServer(start=False)
  dispatcher.start()


# ==================================================
# Line: 68

def testStartDispatcherWithWorkDirConfig(self):
  temp_dir = tempfile.mkdtemp()
  config = server_lib.DispatcherConfig(work_dir=temp_dir)
  dispatcher = server_lib.DispatchServer(  # pylint: disable=unused-variable
      config=config, start=True)


# ==================================================
# Line: 74

def testStartDispatcherWithFaultTolerantConfig(self):
  temp_dir = tempfile.mkdtemp()
  config = server_lib.DispatcherConfig(
      work_dir=temp_dir, fault_tolerant_mode=True)
  dispatcher = server_lib.DispatchServer(  # pylint: disable=unused-variable
      config=config, start=True)


# ==================================================
# Occurrences: Lines 88-92 (2 instances)

def testMultipleStartDispatcher(self):
  dispatcher = server_lib.DispatchServer(start=True)
  dispatcher.start()


# ==================================================
# Line: 105

def testMultipleStartWorker(self):
  dispatcher = server_lib.DispatchServer()
  worker = server_lib.WorkerServer(
      server_lib.WorkerConfig(dispatcher._address), start=True)
  worker.start()


# ==================================================
# Occurrences: Lines 111-116 (2 instances)

def testStopDispatcher(self):
  dispatcher = server_lib.DispatchServer()
  dispatcher.stop()
  dispatcher.stop()


# ==================================================
# Occurrences: Lines 139-144 (2 instances)

def testJoinDispatcher(self):
  dispatcher = server_lib.DispatchServer()
  dispatcher.stop()
  dispatcher.join()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
# Line: 34

def getHashTable(self):
  if tf2.enabled():
    return core_lookup_ops.StaticHashTable
  else:
    return core_lookup_ops.StaticHashTableV1


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
# Line: 199

def _build_dataset(self, components):
  reducer = grouping.Reducer(
      init_func=lambda _: np.int64(0),
      reduce_func=lambda x, y: x + y,
      finalize_func=lambda x: x)

  return dataset_ops.Dataset.from_tensor_slices(components).apply(
      grouping.group_by_reducer(lambda x: x % 5, reducer))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
# Line: 593

def _build_dataset(self, num_repeats):
  data_source_name = os.path.join(test.get_temp_dir(), "tftest.sqlite")
  driver_name = array_ops.placeholder_with_default(
      array_ops.constant("sqlite", dtypes.string), shape=[])
  query = ("SELECT first_name, last_name, motto FROM students ORDER BY "
           "first_name DESC")
  output_types = (dtypes.string, dtypes.string, dtypes.string)
  return readers.SqlDataset(driver_name, data_source_name, query,
                            output_types).repeat(num_repeats)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
# Line: 46

def _record(self, i):
  return compat.as_bytes("Record %d" % (i))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
# Line: 84

def _interleave(self, lists, cycle_length, block_length):
  """Python implementation of interleave used for testing."""
  num_open = 0

  # `all_iterators` acts as a queue of iterators over each element of `lists`.
  all_iterators = [iter(l) for l in lists]

  # `open_iterators` are the iterators whose elements are currently being
  # interleaved.
  open_iterators = []
  for i in range(cycle_length):
    if all_iterators:
      open_iterators.append(all_iterators.pop(0))
      num_open += 1
    else:
      open_iterators.append(None)

  while num_open or all_iterators:
    for i in range(cycle_length):
      if open_iterators[i] is None:
        if all_iterators:
          open_iterators[i] = all_iterators.pop(0)
          num_open += 1
        else:
          continue
      for _ in range(block_length):
        try:
          yield next(open_iterators[i])
        except StopIteration:
          open_iterators[i] = None
          num_open -= 1
          break


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
# Line: 59

def enableFilterParallelization(self, dataset):
  options = options_lib.Options()
  options.experimental_optimization.filter_parallelization = True
  return dataset.with_options(options)


# ==================================================
# Line: 229

def enableFilterParallelization(self, dataset):
  options = options_lib.Options()
  options.experimental_optimization.filter_parallelization = True
  return dataset.with_options(options)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
# Line: 47

def _set_seed(self):
  # Set the seed, since in graph mode some non-random dataset ops call
  # tf.compat.v1.get_seed to copy the seed to a Defun. Calling get_seed raises
  # an error with determinism if no seed is set.
  # TODO(reedwm): Ensure such dataset ops do not raise an error when no seed
  # is set.
  random_seed.set_random_seed(1)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_ft_test.py
# Line: 81

  def _create_cluster(self,
                      num_workers,
                      cross_trainer_cache_size_bytes=10 * (2**30)):
    cluster = data_service_test_base.TestCluster(num_workers=0)
    for _ in range(num_workers):
      worker = data_service_test_base.TestWorker(
          dispatcher_address=cluster.dispatcher_address(),
          shutdown_quiet_period_ms=0,
          cross_trainer_cache_size_bytes=cross_trainer_cache_size_bytes)
      worker.start()
      cluster.workers.append(worker)
    return cluster


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/distributed_save_ft_test.py
# Line: 509

def _get_dataset(self, dataset_range=10, num_sources=1):
  dataset = dataset_ops.Dataset.range(dataset_range)
  if num_sources > 1:
    dataset = dataset_ops.Dataset.zip((dataset,) * num_sources)
  return dataset


# ==================================================
# Line: 526

  def _make_stream_dir(self, snapshot_path, stream_name, worker=0):
    stream_dir = os.path.join(snapshot_path, "streams", stream_name)
    os.makedirs(stream_dir)
    pathlib.Path(os.path.join(stream_dir, "owner_worker")).write_text(
        f"{worker}")


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
# Line: 467

  def _create_cluster(self,
                      num_workers,
                      cross_trainer_cache_size_bytes=10 * (2**30)):
    cluster = data_service_test_base.TestCluster(num_workers=0)
    for _ in range(num_workers):
      worker = data_service_test_base.TestWorker(
          dispatcher_address=cluster.dispatcher_address(),
          shutdown_quiet_period_ms=0,
          cross_trainer_cache_size_bytes=cross_trainer_cache_size_bytes)
      worker.start()
      cluster.workers.append(worker)
    return cluster


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/dense_to_sparse_batch_test.py
# Line: 112

def _build_dataset(self, components):
  return dataset_ops.Dataset.from_tensor_slices(components).map(
      lambda x: array_ops.fill([x], x)).apply(
          batching.dense_to_sparse_batch(4, [12]))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
# Line: 32

def _build_dataset(self,
                   seed=None,
                   reshuffle_each_iteration=None,
                   num_elements=10):
  file_infos = []
  for _ in range(5):
    file_infos.append({"path": "unused", "num_elements": num_elements})

  def reader_factory(files):
    return dataset_ops.Dataset.range(
        num_elements * array_ops.shape(files, out_type=dtypes.int64)[0])

  return shuffle_ops.index_shuffle(
      file_infos,
      reader_factory,
      seed=seed,
      reshuffle_each_iteration=reshuffle_each_iteration)


# ==================================================
# Line: 172

def _build_dataset(
    self,
    num_elements_per_file,
    num_files,
    num_epochs,
    seed=None,
    reshuffle_each_iteration=None,
    symbolic_checkpoint=None,

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
# Line: 321

def testNoneDataset(self):
  # Some datasets, e.g. datasets with None tensors, have components without
  # output shapes. Test that this doesn't break rebatching shape inference
  # logic.
  dataset = dataset_ops.Dataset.range(4)
  dataset = dataset.map(lambda x: (x, None))
  dataset = dataset.batch(4, drop_remainder=True)
  _ = distribute._LegacyRebatchDataset(dataset, num_replicas=2)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
# Line: 190

def _build_list_dataset(self, elements, options=None):
  dataset = from_list.from_list(elements)
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/matching_files_dataset_test.py
# Line: 159

def _build_iterator_graph(self, test_patterns):
  return matching_files.MatchingFilesDataset(test_patterns)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
# Line: 31

def _build_ds(self, seed, count=5, num_elements=20):
  return dataset_ops.Dataset.range(num_elements).apply(
      shuffle_ops.shuffle_and_repeat(buffer_size=5, count=count, seed=seed))


# ==================================================
# Line: 155

def _build_ds(self, seed):
  return dataset_ops.Dataset.range(20).apply(
      shuffle_ops.shuffle_and_repeat(buffer_size=5, count=5, seed=seed))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_cardinality_test.py
# Line: 136

def build_dataset(self, num_elements, options=None):
  dataset = dataset_ops.Dataset.range(num_elements).apply(
      cardinality.assert_cardinality(num_elements))
  if options:
    dataset = dataset.with_options(options)
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
# Line: 36

def _make_csv_dataset(self, filenames, batch_size, num_epochs=1, **kwargs):
  return readers.make_csv_dataset(
      filenames, batch_size=batch_size, num_epochs=num_epochs, **kwargs)


# ==================================================
# Line: 64

def _next_expected_batch(self, expected_output, expected_keys, batch_size,
                         num_epochs):
  features = {k: [] for k in expected_keys}
  for _ in range(num_epochs):
    for values in expected_output:
      for n, key in enumerate(expected_keys):
        features[key].append(values[n])
      if len(features[expected_keys[0]]) == batch_size:
        yield features
        features = {k: [] for k in expected_keys}
  if features[expected_keys[0]]:  # Leftover from the last batch
    yield features


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_saveable_from_iterator_test.py
# Line: 31

def _build_input_pipeline(self, name, num_outputs):
  with ops.name_scope(name):
    ds = dataset_ops.Dataset.range(num_outputs).shuffle(
        10, reshuffle_each_iteration=False).prefetch(10)
    iterator = ds.make_initializable_iterator()
    saveable = contrib_iterator_ops.make_saveable_from_iterator(iterator)
    ops.add_to_collection(ops.GraphKeys.SAVEABLE_OBJECTS, saveable)
    return iterator.initializer, iterator.get_next()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/summary/writer/writer_test.py
# Line: 49

def _FileWriter(self, *args, **kwargs):
  return writer.FileWriter(*args, **kwargs)


# ==================================================
# Line: 444

def assets(self):
  return {"foo.txt": "foo!", "bar.txt": "bar!"}


# ==================================================
# Line: 557

def _createTaggedSummary(self, tag):
  summary = summary_pb2.Summary()
  summary.value.add(tag=tag)
  return summary


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/summary/summary_test.py
# Line: 149

def testHistogramSummaryTypes(self):
  for dtype in (dtypes.int8, dtypes.uint8, dtypes.int16, dtypes.int32,
                dtypes.float32, dtypes.float64):
    const = constant_op.constant(10, dtype=dtype)
    summary_lib.histogram('h', const)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/platform/stacktrace_handler_test.py
# Line: 36

def testChildProcessKillsItself(self):
  if FLAGS.child:
    os.kill(os.getpid(), signal.SIGABRT)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/platform/benchmark.py
# Line: 218

def _get_name(self, overwrite_name=None):
  """Returns full name of class and method calling report_benchmark."""

  # Find the caller method (outermost Benchmark class)
  stack = tf_inspect.stack()
  calling_class = None
  name = None
  for frame in stack[::-1]:
    f_locals = frame[0].f_locals
    f_self = f_locals.get("self", None)
    if isinstance(f_self, Benchmark):
      calling_class = f_self  # Get the outermost stack Benchmark call
      name = frame[3]  # Get the method name
      break
  if calling_class is None:
    raise ValueError("Unable to determine calling Benchmark class.")

  # Use the method name, or overwrite_name is provided.
  name = overwrite_name or name
  # Prefix the name with the class name.
  class_name = type(calling_class).__name__
  name = "%s.%s" % (class_name, name)
  return name


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/platform/logging_test.py
# Line: 22

  def test_log(self):
    # Just check that logging works without raising an exception.
    logging.error("test log message")


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/feature_column/feature_column_test.py
# Line: 1819

def test_runtime_batch_size_matches(self):
  price1 = fc._numeric_column('price1')
  price2 = fc._numeric_column('price2')
  with ops.Graph().as_default():
    features = {
        'price1': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
        'price2': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
    }
    predictions = fc.linear_model(features, [price1, price2])
    with _initialized_session() as sess:
      sess.run(
          predictions,
          feed_dict={
              features['price1']: [[1.], [5.]],
              features['price2']: [[1.], [5.]],
          })


# ==================================================
# Line: 2460

def test_runtime_batch_size_matches(self):
  price1 = fc._numeric_column('price1')
  price2 = fc._numeric_column('price2')
  with ops.Graph().as_default():
    features = {
        'price1': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
        'price2': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
    }
    predictions = get_keras_linear_model_predictions(features,
                                                     [price1, price2])
    with _initialized_session() as sess:
      sess.run(
          predictions,
          feed_dict={
              features['price1']: [[1.], [5.]],
              features['price2']: [[1.], [5.]],
          })


# ==================================================
# Line: 2969

def test_runtime_batch_size_matches(self):
  price1 = fc._numeric_column('price1')
  price2 = fc._numeric_column('price2')
  with ops.Graph().as_default():
    features = {
        'price1': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
        'price2': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
    }
    net = fc.input_layer(features, [price1, price2])
    with _initialized_session() as sess:
      sess.run(
          net,
          feed_dict={
              features['price1']: [[1.], [5.]],
              features['price2']: [[1.], [5.]],
          })


# ==================================================
# Line: 5663

def test_weighted_categorical_column_ok(self):
  with ops.Graph().as_default():
    categorical_column_a = fc._categorical_column_with_identity(
        key='aaa', num_buckets=3)
    weighted_categorical_column_a = fc._weighted_categorical_column(
        categorical_column_a, weight_feature_key='aaa_weights')
    categorical_column_b = fc._categorical_column_with_identity(
        key='bbb', num_buckets=3)
    weighted_categorical_column_b = fc._weighted_categorical_column(
        categorical_column_b, weight_feature_key='bbb_weights')
    fc_new.shared_embedding_columns(
        [weighted_categorical_column_a, categorical_column_b], dimension=2)
    fc_new.shared_embedding_columns(
        [categorical_column_a, weighted_categorical_column_b], dimension=2)
    fc_new.shared_embedding_columns(
        [weighted_categorical_column_a, weighted_categorical_column_b],
        dimension=2)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
# Line: 101

def create_variable(self,
                    feature_column,
                    name,
                    shape,
                    dtype=None,
                    trainable=True,
                    use_resource=True,
                    initializer=None):
  """Creates a new variable.

  Args:
    feature_column: A `FeatureColumn` object this variable corresponds to.
    name: variable name.
    shape: variable shape.
    dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
    trainable: Whether this variable is trainable or not.
    use_resource: If true, we use resource variables. Otherwise we use
      RefVariable.
    initializer: initializer instance (callable).

  Returns:
    The created variable.
  """
  del feature_column, name, shape, dtype, trainable, use_resource, initializer
  raise NotImplementedError('StateManager.create_variable')


# ==================================================
# Line: 127

def add_variable(self, feature_column, var):
  """Adds an existing variable to the state.

  Args:
    feature_column: A `FeatureColumn` object to associate this variable with.
    var: The variable.
  """
  del feature_column, var
  raise NotImplementedError('StateManager.add_variable')


# ==================================================
# Line: 137

def get_variable(self, feature_column, name):
  """Returns an existing variable.

  Args:
    feature_column: A `FeatureColumn` object this variable corresponds to.
    name: variable name.
  """
  del feature_column, name
  raise NotImplementedError('StateManager.get_var')


# ==================================================
# Line: 147

def add_resource(self, feature_column, name, resource):
  """Creates a new resource.

  Resources can be things such as tables, variables, trackables, etc.

  Args:
    feature_column: A `FeatureColumn` object this resource corresponds to.
    name: Name of the resource.
    resource: The resource.

  Returns:
    The created resource.
  """
  del feature_column, name, resource
  raise NotImplementedError('StateManager.add_resource')


# ==================================================
# Line: 163

def has_resource(self, feature_column, name):
  """Returns true iff a resource with same name exists.

  Resources can be things such as tables, variables, trackables, etc.

  Args:
    feature_column: A `FeatureColumn` object this variable corresponds to.
    name: Name of the resource.
  """
  del feature_column, name
  raise NotImplementedError('StateManager.has_resource')


# ==================================================
# Line: 175

def get_resource(self, feature_column, name):
  """Returns an already created resource.

  Resources can be things such as tables, variables, trackables, etc.

  Args:
    feature_column: A `FeatureColumn` object this variable corresponds to.
    name: Name of the resource.
  """
  del feature_column, name
  raise NotImplementedError('StateManager.get_resource')



# ==================================================
# Line: 3821

def _transform_id_weight_pair(self, id_weight_pair, size):
  id_tensor = id_weight_pair.id_tensor
  weight_tensor = id_weight_pair.weight_tensor

  # If the underlying column is weighted, return the input as a dense tensor.
  if weight_tensor is not None:
    weighted_column = sparse_ops.sparse_merge(
        sp_ids=id_tensor, sp_values=weight_tensor, vocab_size=int(size))
    # Remove (?, -1) index.
    weighted_column = sparse_ops.sparse_slice(weighted_column, [0, 0],
                                              weighted_column.dense_shape)
    # Use scatter_nd to merge duplicated indices if existed,
    # instead of sparse_tensor_to_dense.
    return array_ops.scatter_nd(weighted_column.indices,
                                weighted_column.values,
                                weighted_column.dense_shape)

  dense_id_tensor = sparse_ops.sparse_tensor_to_dense(
      id_tensor, default_value=-1)

  # One hot must be float for tf.concat reasons since all other inputs to
  # input_layer are float32.
  one_hot_id_tensor = array_ops.one_hot(
      dense_id_tensor, depth=size, on_value=1.0, off_value=0.0)

  # Reduce to get a multi-hot per example.
  return math_ops.reduce_sum(one_hot_id_tensor, axis=[-2])


# ==================================================
# Line: 4103

def _get_sparse_tensors_helper(self, sparse_tensors):
  id_tensor = sparse_tensors.id_tensor
  weight_tensor = sparse_tensors.weight_tensor
  # Expands third dimension, if necessary so that embeddings are not
  # combined during embedding lookup. If the tensor is already 3D, leave
  # as-is.
  shape = array_ops.shape(id_tensor)
  # Compute the third dimension explicitly instead of setting it to -1, as
  # that doesn't work for dynamically shaped tensors with 0-length at runtime.
  # This happens for empty sequences.
  target_shape = [shape[0], shape[1], math_ops.reduce_prod(shape[2:])]
  id_tensor = sparse_ops.sparse_reshape(id_tensor, target_shape)
  if weight_tensor is not None:
    weight_tensor = sparse_ops.sparse_reshape(weight_tensor, target_shape)
  return CategoricalColumn.IdWeightPair(id_tensor, weight_tensor)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# Line: 81

def get_config(self):
  raise ValueError('Should not use this method.')



# ==================================================
# Line: 156

def transform_feature(self, transformation_cache, state_manager):
  return 'Output'


# ==================================================
# Line: 181

def transform_feature(self, transformation_cache, state_manager):
  return 'Output'


# ==================================================
# Line: 1288

def transform_feature(self, transformation_cache, state_manager):
  raise ValueError('Should not be called.')


# ==================================================
# Line: 1295

def get_sparse_tensors(self, transformation_cache, state_manager):
  raise ValueError('Should not be called.')


# ==================================================
# Line: 1538

def transform_feature(self, transformation_cache, state_manager):
  raise ValueError('Should not use this method.')


# ==================================================
# Occurrences: Lines 1552-1555 (2 instances)

def get_dense_tensor(self, transformation_cache, state_manager):
  raise ValueError('Should not use this method.')


# ==================================================
# Occurrences: Lines 1566-1569 (2 instances)

def get_sparse_tensors(self, transformation_cache, state_manager):
  raise ValueError('Should not use this method.')


# ==================================================
# Line: 1982

def test_runtime_batch_size_matches(self):
  price1 = fc.numeric_column('price1')
  price2 = fc.numeric_column('price2')
  with ops.Graph().as_default():
    features = {
        'price1': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
        'price2': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
    }
    predictions = fc_old.linear_model(features, [price1, price2])
    with _initialized_session() as sess:
      sess.run(
          predictions,
          feed_dict={
              features['price1']: [[1.], [5.]],
              features['price2']: [[1.], [5.]],
          })


# ==================================================
# Line: 2686

def test_runtime_batch_size_matches(self):
  price1 = fc.numeric_column('price1')
  price2 = fc.numeric_column('price2')
  with ops.Graph().as_default():
    features = {
        'price1': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
        'price2': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
    }
    net = fc_old.input_layer(features, [price1, price2])
    with _initialized_session() as sess:
      sess.run(
          net,
          feed_dict={
              features['price1']: [[1.], [5.]],
              features['price2']: [[1.], [5.]],
          })


# ==================================================
# Line: 5627

def test_weighted_categorical_column_ok(self):
  # SharedEmbeddingColumns are graph-only
  with ops.Graph().as_default():
    categorical_column_a = fc.categorical_column_with_identity(
        key='aaa', num_buckets=3)
    weighted_categorical_column_a = fc.weighted_categorical_column(
        categorical_column_a, weight_feature_key='aaa_weights')
    categorical_column_b = fc.categorical_column_with_identity(
        key='bbb', num_buckets=3)
    weighted_categorical_column_b = fc.weighted_categorical_column(
        categorical_column_b, weight_feature_key='bbb_weights')
    fc.shared_embedding_columns_v2(
        [weighted_categorical_column_a, categorical_column_b], dimension=2)
    fc.shared_embedding_columns_v2(
        [categorical_column_a, weighted_categorical_column_b], dimension=2)
    fc.shared_embedding_columns_v2(
        [weighted_categorical_column_a, weighted_categorical_column_b],
        dimension=2)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_with_v1_optimizers_test.py
# Line: 255

def _build(self):
  return variable_scope.get_variable(name="in_manual_scope", shape=[])



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/benchmarks_test.py
# Occurrences: Lines 32-35 (2 instances)

def _serialize_to_tensors(self):
  return {base.VARIABLE_VALUE_KEY: array_ops.ones([])}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/functional_saver_test.py
# Line: 56

def _get_tensors_by_task(self, root):
  serialized_tensors, _, _, _ = (
      checkpoint.TrackableSaver(graph_view.ObjectGraphView(root))
      ._gather_serialized_tensors(None))

  tensors_by_task = {}
  for tensor_dict in serialized_tensors.values():
    for checkpoint_key, maybe_tensor in tensor_dict.items():
      if not isinstance(maybe_tensor, dict):
        maybe_tensor = {"": maybe_tensor}
      for slice_spec, tensor in maybe_tensor.items():
        tensor_task = saveable_object_util.set_cpu0(tensor.device)
        (tensors_by_task
         .setdefault(tensor_task, {})
         .setdefault(checkpoint_key, {})[slice_spec]) = tensor
  return tensors_by_task


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/restore_test.py
# Line: 78

def _serialize_to_tensors(self):
  return {"a": variables.Variable(5.0)}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_adapter.py
# Line: 30

def object_name(self) -> str:
  """Returns the local name of the object being restored.

  Override this method when the local name of object is different than in the
  checkpoint.
  """
  return None


# ==================================================
# Line: 38

def reshard(
    self,
    checkpoint_values: List[tensor.Tensor],
    shape_and_slice_spec: List[str],

# ==================================================
# Line: 60

def update_restore_inputs(
    self, checkpoint_key, shape_and_slice_spec

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_metrics_test.py
# Line: 30

def _get_write_histogram_proto(self, api_label):
  proto_bytes = metrics.GetCheckpointWriteDurations(api_label=api_label)
  histogram_proto = summary_pb2.HistogramProto()
  histogram_proto.ParseFromString(proto_bytes)
  return histogram_proto


# ==================================================
# Line: 36

def _get_read_histogram_proto(self, api_label):
  proto_bytes = metrics.GetCheckpointReadDurations(api_label=api_label)
  histogram_proto = summary_pb2.HistogramProto()
  histogram_proto.ParseFromString(proto_bytes)
  return histogram_proto


# ==================================================
# Occurrences: Lines 42-45 (2 instances)

def _get_time_saved(self, api_label):
  return metrics.GetTrainingTimeSaved(api_label=api_label)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Line: 130

def testInitNotCalled(self):

  class NoInit(autotrackable.AutoTrackable):

    def __init__(self):
      pass

  # __init__ for Trackable will be called implicitly.
  trackable_utils.add_variable(NoInit(), "var", shape=[])


# ==================================================
# Line: 423

def _get_checkpoint_name(self, name):
  root = autotrackable.AutoTrackable()
  trackable_utils.add_variable(
      root, name=name, shape=[1, 2], dtype=dtypes.float64)
  checkpoint_key = _get_all_checkpoint_names(root)[0]
  with ops.name_scope("root/" + checkpoint_key):
    pass  # Make sure we can use this as an op name if we prefix it.
  return checkpoint_key


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/sharding/sharding_util_test.py
# Line: 41

def _get_shardable_tensors_by_task(self, root):
  serialized_tensors, _, _, _ = (
      checkpoint.TrackableSaver(graph_view.ObjectGraphView(root))
      ._gather_serialized_tensors(None))

  shardable_tensors_by_task = {}
  for obj, tensor_dict in serialized_tensors.items():
    for checkpoint_key, tensor_slice_dict in tensor_dict.items():
      if not isinstance(tensor_slice_dict, dict):
        # Make sure that maybe_tensor is structured as {slice_spec -> tensor}.
        tensor_slice_dict = {"": tensor_slice_dict}
      for slice_spec, tensor_save_spec in tensor_slice_dict.items():
        if not isinstance(tensor_save_spec, saveable_object.SaveSpec):
          tensor_save_spec = saveable_object.SaveSpec(
              tensor=tensor_save_spec,
              slice_spec=slice_spec,
              name=checkpoint_key,
              dtype=tensor_save_spec.dtype,
              device=tensor_save_spec.device)
        save_spec_tensor = tensor_save_spec.tensor
        device = (device_lib.DeviceSpec.from_string(tensor_save_spec.device)
                  if isinstance(tensor_save_spec.device, str)
                  else tensor_save_spec.device)
        task = device_lib.DeviceSpec.from_string(
            saveable_object_util.set_cpu0(device.to_string()))
        shardable_tensors_by_task.setdefault(task, []).append(
            sharding_util.ShardableTensor(
                _tensor_save_spec=tensor_save_spec,
                tensor=save_spec_tensor,
                dtype=tensor_save_spec.dtype,
                device=device,
                name=tensor_save_spec.name,
                shape=save_spec_tensor.shape,
                slice_spec=slice_spec.strip(),
                checkpoint_key=checkpoint_key,
                trackable=obj))
  return shardable_tensors_by_task.values()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/sharding/sharding_policies_test.py
# Line: 47

def _get_shardable_tensors_by_task(self, root):
  serialized_tensors, _, _, _ = (
      checkpoint.TrackableSaver(graph_view.ObjectGraphView(root))
      ._gather_serialized_tensors(None))

  shardable_tensors_by_task = {}
  for obj, tensor_dict in serialized_tensors.items():
    # Divide tensor_dict by device.
    for checkpoint_key, tensor_slice_dict in tensor_dict.items():
      if not isinstance(tensor_slice_dict, dict):
        # Make sure that maybe_tensor is structured as {slice_spec -> tensor}.
        tensor_slice_dict = {"": tensor_slice_dict}
      for slice_spec, tensor_save_spec in tensor_slice_dict.items():
        if not isinstance(tensor_save_spec, saveable_object.SaveSpec):
          tensor_save_spec = saveable_object.SaveSpec(
              tensor=tensor_save_spec,
              slice_spec=slice_spec,
              name=checkpoint_key,
              dtype=tensor_save_spec.dtype,
              device=tensor_save_spec.device)
        save_spec_tensor = tensor_save_spec.tensor
        device = (device_lib.DeviceSpec.from_string(tensor_save_spec.device)
                  if isinstance(tensor_save_spec.device, str)
                  else tensor_save_spec.device)
        task = device_lib.DeviceSpec.from_string(
            saveable_object_util.set_cpu0(device.to_string()))
        shardable_tensors_by_task.setdefault(task, []).append(
            sharding_util.ShardableTensor(
                _tensor_save_spec=tensor_save_spec,
                tensor=save_spec_tensor,
                dtype=tensor_save_spec.dtype,
                device=device,
                name=tensor_save_spec.name,
                shape=save_spec_tensor.shape,
                slice_spec=slice_spec,
                checkpoint_key=checkpoint_key,
                trackable=obj))
  return shardable_tensors_by_task.values()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/base.py
# Line: 384

def _no_dependency(self, value):
  """If automatic dependency tracking is enabled, ignores `value`."""
  return value


# ==================================================
# Line: 753

def _serialize_to_proto(self, object_proto=None, **kwargs):
  """Returns a proto of any type to be saved into the SavedModel.

  Trackable classes decorated with `register_serializable` should overwrite
  this method to save metadata for this object to the SavedModel. The proto
  returned by this function will be passed to `_deserialize_from_proto` in the
  form of a `google.protobuf.Any` proto.

  This data is only saved and used by the Python API. Existing C++ loading
  APIs such as `tensorflow::LoadSavedModel` will not read this field at all.

  Args:
    object_proto: A `SavedObject` proto that may be filled by this function.
      Only the core serializable types (Variable, Function, Constant, Asset)
      should modify this argument.
    **kwargs: Future keyword arguments passed to the object during saving.

  Returns:
    A proto that serializes this class's type.
  """
  del object_proto, kwargs  # Unused.

  return None


# ==================================================
# Line: 888

def _deserialization_dependencies(self, children):
  """Returns a dictionary containing `Trackables` that this object depends on.

  Dependencies define the order to serialize and deserialize objects in the
  SavedModel. For example:

  class A(Trackable):
    b = B()
    def _deserialization_dependencies(self, children):
      return {'b': self.b}

  class B(Trackable):
    pass

  We say that object `a=A()` depends on `a.b`.

  Dependencies are guaranteed to be serialized and deserialized before the
  object depending on them. The following methods use dependencies:
    - `_deserialize_from_proto` [loading]

  SavedModel loads with the bottom-up approach, by first creating all objects
  in the order defined by the dependencies, then connecting the children.

  Unlike `_trackable_children`, this function does not define the
  `SavedObjectGraph`. It only changes the order in which things are
  saved/loaded. Therefore, if there are dependencies that are not in the
  `SavedObjectGraph`, saving will fail.

  Args:
    children: Dict returned from `_trackable_children`.

  Returns:
    A dictionary mapping names to `Trackable`.
  """
  del children  # Unused.
  return {}


# ==================================================
# Line: 1030

def _export_to_saved_model_graph(self,
                                 object_map,
                                 tensor_map,
                                 options,
                                 **kwargs):
  """Creates a copy of this object's tensors onto SavedModel graph.

  Needs to be overridden if the class contains tensors that must be saved
  into the graph. This method should update the `object_map` and `tensor_map`
  dictionaries.

  This method is called on all nodes in the Trackable Graph (generated by
  `_trackable_children`). The nodes are traversed in the order defined by
  `_deserialization_dependencies`

  All usages of _map_resources should be migrated to this method.

  Args:
    object_map: A dictionary that maps original Trackables to the copied
      Trackables. This only needs to be updated if the object is a
      tf.function, or if the copied tensors are necessary for checkpointing
      this object.
    tensor_map: Dictionary mapping original tensors to copied tensors.
    options: A `tf.saved_model.SaveOptions` object.
    **kwargs: Additional kwargs that may be added at a later time.

  Returns:
    Flat list of original tensors that have been copied.
  """
  _, _, _ = object_map, tensor_map, options
  del kwargs
  return []


# ==================================================
# Line: 1063

def _copy_trackable_to_cpu(self, object_map):
  """Creates a copy of this object onto CPU, also copies values over.

  Needs to be overridden if the `Trackable` requires AsyncCheckpoint support.
  The method first checks whether a copy of `self` is already created in
  `object_map`, and creates one if not already created. Then the method copies
  the **values** of itself over to its copy mapped by `object_map`.

  Args:
    object_map: A dictionary that maps original Trackables to the copied
      Trackables, which reside in the CPU.
  """
  del object_map  # Unused
  raise NotImplementedError("Need to implement _copy_trackable_to_cpu() if "
                            "the Trackable requires AsyncCheckpoint support.")


# ==================================================
# Line: 1079

def _checkpoint_adapter(self, path: str):
  """Returns a checkpoint adapter for this object.

  Needs to be overridden if the `Trackable` requires adapter at restore.
  Override this method to define callbacks for checkpoint positions to be
  applied at restore time.

  Args:
    path: Checkpoint path.
  Returns:
    A subclass of AbstractCheckpointAdapter that defines callbacks at restore
    for this trackable.
  """
  del path
  return None

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/data_structures.py
# Occurrences: Lines 380-384 (2 instances)

def _make_storage(self, *args, **kwargs):
  """Determines the backing storage (overridden in subclasses)."""
  return list(*args, **kwargs)


# ==================================================
# Line: 737

def _make_storage(self, *args, **kwargs):
  return dict(*args, **kwargs)


# ==================================================
# Line: 749

def _name_element(self, key):
  if not isinstance(key, str):
    raise TypeError(
        f"Mapping accepts only string keys, but got a key {repr(key)}.")
  return str(key)


# ==================================================
# Line: 928

def _name_element(self, key):
  """Tells TrackableDataStructure to use keys as names as-is."""
  return key


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/base_test.py
# Line: 72

def get_config(self):
  return NotSerializable()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/trackable/data_structures_test.py
# Line: 42

def testJSONSerialization(self):
  obj = autotrackable.AutoTrackable()
  obj.l = [1]
  json.dumps(obj.l, default=serialization.get_json_type)


# ==================================================
# Line: 184

def testSameStructure(self):
  l = [1]
  nest.assert_same_structure(l, data_structures.ListWrapper(copy.copy(l)))


# ==================================================
# Line: 341

def testJSONSerialization(self):
  obj = autotrackable.AutoTrackable()
  obj.d = {"a": 2}
  json.dumps(obj.d, default=serialization.get_json_type)


# ==================================================
# Line: 506

def testSameStructure(self):
  d = {1: "a"}
  nest.assert_same_structure(d, data_structures._DictWrapper(d.copy()))


# ==================================================
# Line: 523

def testJSONSerialization(self):
  obj = autotrackable.AutoTrackable()
  obj.l = (1,)
  json.dumps(obj.l, default=serialization.get_json_type)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/module/module_test.py
# Occurrences: Lines 274-277 (2 instances)

def _to_components(self, value):
  return value._variables


# ==================================================
# Line: 410

def alternative_forward(self):
  return get_name_scope()


# ==================================================
# Line: 421

def alternative_alternative_forward(self):
  return get_name_scope()



# ==================================================
# Occurrences: Lines 443-448 (2 instances)

def forward(self):
  return get_name_scope()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
# Line: 493

def _get_variable_creator_initial_value(self,
                                        replica_id,
                                        device,
                                        primary_var,
                                        **kwargs):
  """Return the initial value for variables on a replica."""
  if replica_id == 0:
    return kwargs["initial_value"]
  else:
    assert primary_var is not None
    assert device is not None
    assert kwargs is not None

    def initial_value_fn():
      if context.executing_eagerly() or ops.inside_function():
        init_value = primary_var.value()
        return array_ops.identity(init_value)
      else:
        with ops.device(device):
          init_value = primary_var.initial_value
          return array_ops.identity(init_value)

    return initial_value_fn


# ==================================================
# Occurrences: Lines 937-940 (2 instances)

def _get_local_replica_id(self, replica_id_in_sync_group):
  return replica_id_in_sync_group


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# Line: 403

def _initialize_local_devices(self, cluster_resolver, worker_device):
  # TODO(b/126786766): TFConfigClusterResolver returns wrong number of GPUs in
  # some cases.
  if isinstance(
      cluster_resolver, tfconfig_cluster_resolver.TFConfigClusterResolver
  ):
    num_gpus = context.num_gpus()
    num_tpus = 0
  else:
    num_gpus = cluster_resolver.num_accelerators().get("GPU", 0)
    num_tpus = cluster_resolver.num_accelerators().get("TPU", 0)

  if num_gpus:
    local_device_type = "GPU"
    num_local_devices = num_gpus
  elif num_tpus:
    local_device_type = "TPU"
    num_local_devices = num_tpus
  else:
    local_device_type = "CPU"
    num_local_devices = 1
  local_devices = tuple(
      f"{worker_device}/device:{local_device_type}:{i}"
      for i in range(num_local_devices)
  )
  return local_devices, local_device_type


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/moving_averages_test.py
# Line: 235

def _ema_replica_fn_graph(self):
  w = variables.Variable([1.0],
                         name="w",
                         aggregation=variables.VariableAggregation.MEAN)
  ema = moving_averages.ExponentialMovingAverage(0.8)
  w_apply = ema.apply([w])
  w_assign = w.assign_sub([0.5])
  return w_assign, w_apply, ema.average(w)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cross_device_utils.py
# Occurrences: Lines 300-305 (2 instances)

def _use_unique_instance_key(self):
  if not ops.executing_eagerly_outside_functions():
    return False
  return CollectiveReplicaLauncher._prefer_unique_instance_key


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
# Line: 161

def testGetNextAsOptionalExampleUsage(self, distribution):
  global_batch_size = 2
  steps_per_loop = 6
  dataset = dataset_ops.Dataset.range(
      8, output_type=dtypes.int32).batch(global_batch_size)
  distributed_iterator = iter(
      distribution.experimental_distribute_dataset(dataset))

  @def_function.function
  def train_fn(distributed_iterator):

    def step_fn(x):
      return x

    for _ in math_ops.range(steps_per_loop):
      optional_data = distributed_iterator.get_next_as_optional()
      if not optional_data.has_value():
        break
      distribution.run(step_fn, args=(optional_data.get_value(),))

  train_fn(distributed_iterator)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/values.py
# Line: 449

def _is_mirrored(self):
  return True



# ==================================================
# Line: 1611

def assign_sub(self,
               var,
               value,
               use_locking=False,
               name=None,
               read_value=True):
  """Subtracts a value from this variable."""
  with distribute_lib.enter_or_assert_strategy(var.distribute_strategy):
    if (distribute_lib.in_cross_replica_context() and
        not values_util.in_replica_update_context()):
      values_util.mark_as_unsaveable()
      return values_util.on_read_assign_sub_cross_replica(
          var, value, read_value=read_value)
    else:
      return values_util.on_write_assign_sub(
          var,
          value,
          use_locking=use_locking,
          name=name,
          read_value=read_value)


# ==================================================
# Line: 1632

def assign_add(self,
               var,
               value,
               use_locking=False,
               name=None,
               read_value=True):
  """Adds a value to this variable."""
  with distribute_lib.enter_or_assert_strategy(var.distribute_strategy):
    if (distribute_lib.in_cross_replica_context() and
        not values_util.in_replica_update_context()):
      values_util.mark_as_unsaveable()
      return values_util.on_read_assign_add_cross_replica(
          var, value, read_value=read_value)
    else:
      return values_util.on_write_assign_add(
          var,
          value,
          use_locking=use_locking,
          name=name,
          read_value=read_value)


# ==================================================
# Line: 1653

def assign(self, var, value, use_locking=False, name=None, read_value=True):
  with distribute_lib.enter_or_assert_strategy(var.distribute_strategy):
    if (distribute_lib.in_cross_replica_context() and
        not values_util.in_replica_update_context()):
      values_util.mark_as_unsaveable()
      return values_util.on_read_assign_cross_replica(
          var, value, read_value=read_value)
    else:
      return values_util.on_write_assign(
          var,
          value,
          use_locking=use_locking,
          name=name,
          read_value=read_value)


# ==================================================
# Line: 1696

def get_saveable(self, var, primary_var, name):
  """Create a saveable object for the given variable."""
  return values_util.get_on_read_saveable(var, primary_var, name)


# ==================================================
# Occurrences: Lines 1733-1737 (2 instances)

def assign(self, var, value, use_locking=False, name=None, read_value=True):
  return values_util.on_write_assign(
      var, value, use_locking=use_locking, name=name, read_value=read_value)


# ==================================================
# Line: 1746

def assign_sub(self,
               var,
               value,
               use_locking=False,
               name=None,
               read_value=True):
  return values_util.on_write_assign_sub(
      var, value, use_locking=use_locking, name=name, read_value=read_value)


# ==================================================
# Occurrences: Lines 1755-1767 (4 instances)

def scatter_sub(self, var, sparse_delta, use_locking=False, name=None):
  return values_util.scatter_sub(
      var, sparse_delta, use_locking=use_locking, name=name)


# ==================================================
# Occurrences: Lines 1798-1802 (2 instances)

def get_saveable(self, var, primary_var, name):
  """Saveable ops for AUTO variables."""
  return values_util.get_on_write_saveable(var, primary_var, name)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/step_fn.py
# Line: 31

def initialize(self):
  return []


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/v1/input_lib.py
# Line: 401

def initialize(self):
  # TODO(petebu) Should this throw an exception instead?
  return []



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
# Line: 85

def _buildInput(self, num_workers, num_gpus):
  t8 = constant_op.constant(
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      types_pb2.DT_FLOAT)
  input_tensors = []
  device_names = []
  for w in range(0, num_workers):
    for d in range(0, num_gpus):
      dn = "/replica:0/task:%d/device:GPU:%d" % (w, d % num_gpus)
      device_names.append(dn)
      with ops.device(dn):
        input_tensors.append(array_ops.identity(t8))
  return input_tensors, device_names


# ==================================================
# Line: 123

def _buildInitialVars(self, shape, dev_list):
  values = []
  num_devices = len(dev_list)
  dim = np.prod(shape, dtype=int) if shape else 1
  for d in range(0, num_devices):
    with ops.device(dev_list[d]):
      npt = np.zeros(shape).astype(np.float32)
      alias = np.frombuffer(npt.data, dtype=np.float32)
      for i in range(0, dim):
        alias[i] = i + 0.01 * d
      var = state_ops.variable_op(shape, types_pb2.DT_FLOAT)
      state_ops.init_variable(var, npt).op.run()
      values.append(var)
  return values


# ==================================================
# Line: 140

def _buildRing(self, num_workers, num_gpus, subdiv):
  gpu_perm = range(0, num_gpus)
  return lambda x, un_op: ar.build_ring_all_reduce(
      x, num_workers, subdiv, gpu_perm, math_ops.add, un_op)


# ==================================================
# Line: 185

def _buildShuffle(self, num_workers, num_gpus, num_shards):
  # Use local CPU for all shuffle shards
  gather_devices = ["/replica:0/task:0/device:CPU:0"
                    for _ in range(num_shards)]
  return lambda x, un_op: ar.build_shuffle_all_reduce(
      x, gather_devices, math_ops.add_n, un_op)


# ==================================================
# Line: 212

def _buildRecursiveHD(self, num_workers, num_gpus):
  return lambda x, un_op: ar.build_recursive_hd_all_reduce(
      x, math_ops.add, un_op)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
# Line: 638

def _get_indexed_slices(self,
                        devices,
                        start_i,
                        variable_length,
                        as_per_replica=True):
  dense_shape = [10, 2]
  values = ([[1., 2.]], [[3., 4.]], [[2., 1.]], [[0., 0.]], [[3., 1.]],
            [[2., 1.]])
  indices = ([1], [2], [3], [4], [5], [6])

  # values and indices that have variable lengths.
  vl_values = ([[1., 2.], [3., 4.]], [[3., 4.]], [[2., 1.]], [[0., 0.]],
               [[3., 1.], [2., 1.]], [[2., 1.]])
  vl_indices = ([1, 2], [2], [3], [4], [5, 6], [6])

  indexed_slices = []
  for i, d in enumerate(devices):
    idx = i + start_i
    indexed_slices.append(
        _make_indexed_slices(
            vl_values[idx] if variable_length else values[idx],
            vl_indices[idx] if variable_length else indices[idx], dense_shape,
            d))
  if as_per_replica:
    per_replica = value_lib.PerReplica(indexed_slices)
    return per_replica
  else:
    return indexed_slices


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/multi_process_runner.py
# Line: 459

def _queue_to_list(self, queue_to_convert):
  """Convert `queue.Queue` to `list`."""
  list_to_return = []
  # Calling `queue.empty()` is not reliable.
  while True:
    try:
      list_to_return.append(queue_to_convert.get(block=False))
    except Queue.Empty:
      break
  return list_to_return


# ==================================================
# Line: 762

def _runtime_mode(self, executing_eagerly):
  if executing_eagerly:
    with context.eager_mode():
      yield
  else:
    with context.graph_mode():
      yield


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/packed_distributed_variable_test.py
# Line: 159

  def testNoGarbage(self):
    device0 = device_util.canonicalize('/cpu:0')
    device1 = device_util.canonicalize('/cpu:1')

    with ops.device(device0):
      v0 = resource_variable_ops.ResourceVariable(1.0)
    with ops.device(device1):
      v1 = resource_variable_ops.ResourceVariable(2.0)

    packed_var = packed_distributed_variable.PackedDistributedVariable([v0, v1])
    # This needs a workaround to avoid creating reference cycles if the
    # attribute doesn't exist.
    hasattr(packed_var.on_device('/cpu:0'), 'nonexist')


if __name__ == '__main__':

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_lib.py
# Line: 172

def deserialize(self, serialized):
  return InputWorkers(serialized)



# ==================================================
# Line: 924

def _make_rebatch_fn(self, dataset, num_workers, num_replicas_in_sync):
  """Returns a callable that rebatches the input dataset.

  Args:
    dataset: A `tf.data.Dataset` representing the dataset to be distributed.
    num_workers: An integer representing the number of workers to distribute
      `dataset` among.
    num_replicas_in_sync: An integer representing the number of replicas in
      sync across all workers.
  """
  if num_replicas_in_sync % num_workers:
    raise ValueError(
        "tf.distribute expects every worker to have the same number of "
        "replicas. However, encountered `num_replicas_in_sync` ({}) that "
        "cannot be divided by `num_workers` ({})".format(
            num_replicas_in_sync, num_workers))

  num_replicas_per_worker = num_replicas_in_sync // num_workers
  with ops.colocate_with(dataset._variant_tensor):  # pylint: disable=protected-access
    batch_size = distribute.compute_batch_size(dataset)

  def rebatch_fn(dataset, worker_index):
    try:

      def apply_rebatch():
        batch_sizes = distribute.batch_sizes_for_worker(
            batch_size, num_workers, num_replicas_per_worker, worker_index)
        return dataset.rebatch(batch_sizes).prefetch(num_replicas_per_worker)

      # pylint: disable=protected-access
      def apply_legacy_rebatch():
        return distribute._LegacyRebatchDataset(
            dataset, num_replicas_in_sync).prefetch(num_replicas_per_worker)

      with ops.colocate_with(dataset._variant_tensor):
        return tf_cond.cond(
            math_ops.not_equal(batch_size, -1),
            true_fn=apply_rebatch,
            false_fn=apply_legacy_rebatch)
    except errors.InvalidArgumentError as e:
      if "without encountering a batch" in str(e):
        six.reraise(
            ValueError,
            ValueError(
                "Call the `batch` method on the input Dataset in order to be "
                "able to split your input across {} replicas.\n Please see "
                "the tf.distribute.Strategy guide. {}".format(
                    num_replicas_in_sync, e)),
            sys.exc_info()[2])
      else:
        raise

  return rebatch_fn


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# Line: 572

def load_and_run_v1(self,
                    model_dir,
                    inputs,
                    signature_key=tf1.saved_model.signature_constants
                    .DEFAULT_SERVING_SIGNATURE_DEF_KEY):
  """Load a SavedModel into a TF 1.x-style graph and run `signature_key`."""
  graph = tf.Graph()
  with graph.as_default(), tf1.Session() as session:
    meta_graph_def = tf1.saved_model.load(
        session, [tf1.saved_model.tag_constants.SERVING], model_dir)
    signature = meta_graph_def.signature_def[signature_key]
    feed_dict = {}
    for arg_name in inputs.keys():
      input_tensor = session.graph.get_tensor_by_name(
          signature.inputs[arg_name].name)
      feed_dict[input_tensor] = inputs[arg_name]
    output_dict = {}
    for output_name, output_tensor_info in signature.outputs.items():
      output_dict[output_name] = session.graph.get_tensor_by_name(
          output_tensor_info.name)
    return session.run(output_dict, feed_dict)["output_0"]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
# Line: 185

  def test_quick_recover(self):
    # This test simulates the case when a worker fails but recovers quickly
    # before the next collective.
    #
    # It's not guaranteed that the cluster only restarts once when one worker
    # fails. The external job management system is expected to keep restarting
    # failed workers.

    def worker_fn(attempts):
      # Set a long check alive interval to better simulate the case when a
      # worker fails and recovers during a check alive interval.
      mwms_lib.CollectiveAllReduceExtended._check_alive_interval = 30
      mwms_lib.CollectiveAllReduceExtended._check_alive_initial_timeout = 30

      strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
      task_id, attempt = get_attempt(strategy, attempts)

      @tf.function
      def replica_fn():
        ctx = tf.distribute.get_replica_context()
        # Use a large tensor because small tensor may hang regardless when the
        # worker recovers.
        value = tf.ones((64, 64))
        ctx.all_reduce(tf.distribute.ReduceOp.SUM, [value, value])

      strategy.run(replica_fn)
      # worker-1 dies here.
      if attempt == 1 and task_id == 1:
        quick_exit(1)
      strategy.run(replica_fn)

    cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
    attempts = multi_process_runner.manager().dict()
    mpr = multi_process_runner.MultiProcessRunner(
        worker_fn,
        cluster_spec,
        rpc_layer=RPC_PROTOCOL,
        args=(attempts,),
        auto_restart=True)
    mpr.start()
    mpr.join(timeout=90)


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_ops_test.py
# Line: 43

def _getNext(self, dataset):
  if context.executing_eagerly():
    iterator = iter(dataset)
    return iterator._next_internal  # pylint: disable=protected-access
  else:
    iterator = dataset_ops.make_one_shot_iterator(dataset)
    get_next = iterator.get_next()
    return lambda: get_next


# ==================================================
# Occurrences: Lines 52-55 (2 instances)

def _record(self, r, f):
  return compat.as_bytes("Record %d of file %d" % (r, f))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_lib_test.py
# Line: 105

def _wrap_dataset(self,
                  input_type,
                  dataset,
                  input_workers,
                  num_replicas_in_sync,
                  strategy,
                  input_context=None):
  if input_type == "dataset":
    if tf2.enabled():
      return input_lib.DistributedDataset(
          input_workers,
          strategy,
          dataset,
          num_replicas_in_sync=num_replicas_in_sync,
          input_context=input_context)
    else:
      return input_lib_v1.DistributedDatasetV1(
          dataset,
          input_workers,
          strategy,
          num_replicas_in_sync=num_replicas_in_sync,
          input_context=input_context)
  else:
    return strategy.distribute_datasets_from_function(dataset)


# ==================================================
# Line: 276

def _create_dataset_or_input_fn(self, input_type, input_fn):
  if input_type == "input_fn":
    return input_fn
  else:
    return input_fn(distribute_lib.InputContext())



# ==================================================
# Line: 1625

def testDevicePlacementForPerWorkerValuesWithPrefetch(self, distribution,
                                                      input_options):

  def dataset_fn(input_context):  # pylint: disable=[unused-argument]
    return dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4])

  ds = distribution.experimental_distribute_datasets_from_function(
      dataset_fn, input_options)

  for x in ds:
    assert x.values[0].device == distribution.extended.worker_devices[0]
    assert x.values[0].backing_device == distribution.extended.worker_devices[
        0]
    assert x.values[1].device == distribution.extended.worker_devices[1]
    assert x.values[1].backing_device == distribution.extended.worker_devices[
        1]


# ==================================================
# Line: 1660

def testDevicePlacementForPerWorkerValuesWithoutPrefetch(
    self, distribution, input_options):

  def dataset_fn(input_context):
    return dataset_ops.Dataset.from_tensor_slices(
        np.full(4, input_context.input_pipeline_id))

  ds = distribution.experimental_distribute_datasets_from_function(
      dataset_fn, input_options)

  for x in ds:
    x = distribution.run(lambda inputs: inputs, args=(x,))
    assert x.values[
        0].device == "/job:localhost/replica:0/task:0/device:CPU:0"
    assert x.values[
        0].backing_device == "/job:localhost/replica:0/task:0/device:CPU:0"
    assert x.values[
        1].device == "/job:localhost/replica:0/task:0/device:CPU:0"
    assert x.values[
        1].backing_device == "/job:localhost/replica:0/task:0/device:CPU:0"


# ==================================================
# Line: 1734

def testPrefetchBufferSizeInputOptions(self, distribution, input_options):

  def dataset_fn(input_context):
    return dataset_ops.Dataset.from_tensor_slices(
        np.arange(1, 11).reshape(
            (2, 5)) * (input_context.input_pipeline_id + 1))

  ds = distribution.experimental_distribute_datasets_from_function(
      dataset_fn, input_options)

  # validating the values
  x = next(iter(ds))
  assert np.array_equal(x.values[0].numpy(), np.array([1, 2, 3, 4, 5]))
  assert np.array_equal(x.values[1].numpy(), np.array([6, 7, 8, 9, 10]))


# ==================================================
# Line: 1771

def testOutputValuesForPerWorkerInputOptions(self, distribution,
                                             input_options):

  def dataset_fn(input_context):
    return dataset_ops.Dataset.from_tensor_slices(
        np.arange(1, 11).reshape(
            (2, 5)) * (input_context.input_pipeline_id + 1))

  ds = distribution.experimental_distribute_datasets_from_function(
      dataset_fn, input_options)

  # validating the values
  x = next(iter(ds))
  assert np.array_equal(x.values[0].numpy(), np.array([1, 2, 3, 4, 5]))
  assert np.array_equal(x.values[1].numpy(), np.array([6, 7, 8, 9, 10]))


# ==================================================
# Line: 1814

def testOutputValuesForPerReplicaInputOptions(self, distribution,
                                              input_options):

  def dataset_fn(input_context):
    return dataset_ops.Dataset.from_tensor_slices(
        np.arange(1, 10) * (input_context.input_pipeline_id + 1))

  ds = distribution.experimental_distribute_datasets_from_function(
      dataset_fn, input_options)
  expected = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
  for i, x in enumerate(ds):
    # validating the values
    assert x.values[0].numpy() == expected[i]
    assert x.values[1].numpy() == expected[i] * 2
    loop_num = i
  assert loop_num == len(expected) - 1



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
# Line: 179

def _test_session(self, target):
  config = config_pb2.ConfigProto(allow_soft_placement=True)
  config.graph_options.optimizer_options.opt_level = -1
  with session.Session(graph=None, config=config, target=target) as sess:
    yield sess


# ==================================================
# Line: 186

def _create_cluster_spec(self,
                         has_chief=False,
                         num_workers=1,
                         num_ps=0,
                         has_eval=False):
  cluster_spec = {}
  if has_chief:
    cluster_spec[CHIEF] = ["localhost:%s" % test_util.pick_unused_port()]
  if num_workers:
    cluster_spec[WORKER] = [
        "localhost:%s" % test_util.pick_unused_port()
        for _ in range(num_workers)
    ]
  if num_ps:
    cluster_spec[PS] = [
        "localhost:%s" % test_util.pick_unused_port() for _ in range(num_ps)
    ]
  if has_eval:
    cluster_spec[EVALUATOR] = ["localhost:%s" % test_util.pick_unused_port()]
  return cluster_spec


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distributed_table_test.py
# Line: 91

def makeDatasetFromTensorWithoutUsingResource(self, input_context, tensor):
  """Returns a dataset made from `tensor`. To be called in a dataset_fn."""
  global_batch_size = 24
  batch_size = input_context.get_per_replica_batch_size(global_batch_size)
  dataset = dataset_ops.DatasetV2.from_tensors(tensor).repeat().batch(
      batch_size, drop_remainder=True)
  dataset = dataset.shard(input_context.num_input_pipelines,
                          input_context.input_pipeline_id)
  dataset = dataset.prefetch(2)  # This prefetches 2 batches per device.
  return dataset


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/remote_mirrored_strategy_eager_test.py
# Line: 48

def _get_num_gpus(self):
  return len(get_gpus())


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distribute_lib.py
# Line: 2468

def _resource_creator_scope(self):
  """Returns one or a list of ops.resource_creator_scope for some Strategy."""
  return None


# ==================================================
# Line: 2563

def _allow_variable_partition(self):
  return False


# ==================================================
# Line: 3084

def _configure(self,
               session_config=None,
               cluster_spec=None,
               task_type=None,
               task_id=None):
  """Configures the strategy class."""
  del session_config, cluster_spec, task_type, task_id


# ==================================================
# Line: 3092

def _update_config_proto(self, config_proto):
  return copy.deepcopy(config_proto)


# ==================================================
# Line: 3334

def _use_merge_call(self):
  """Whether to use merge-calls inside the distributed strategy."""
  return True


# ==================================================
# Occurrences: Lines 4126-4129 (2 instances)

def _get_local_replica_id(self, replica_id_in_sync_group):
  return replica_id_in_sync_group


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
# Line: 253

def test_control_dep_on_assign(self):
  v0 = variables_lib.Variable([[0, 0]])
  v1 = variables_lib.Variable([[1, 1], [2, 2]])
  v2 = variables_lib.Variable([[3, 3]])
  s = sharded_variable.ShardedVariable([v0, v1, v2])

  @def_function.function
  def func():
    ret = s.assign([[4, 4], [5, 5], [6, 6], [7, 7]])
    with ops.control_dependencies([ret]):
      a = array_ops.ones((1, 1))
    with ops.control_dependencies([control_flow_ops.group(ret)]):
      b = array_ops.ones((1, 1))
    return a, b

  func()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
# Line: 161

def make_collective(self, num_processes, gpu_per_process):
  """Returns collectives and other info to be used in tests.

  Args:
    num_processes: an integer indicating the number of processes that
      participate in the collective.
    gpu_per_process: number of GPUs (0 if no GPUs) used by each process.

  Returns:
   A tuple of (collective, devices, pid) where collective is a instance
   of `CollectiveAllReduce`, devices are a list of local devices (str)
   attached to the current process, and pid is the id of this process among
   all participant processes.
  """

  cluster_resolver = cluster_resolver_lib.TFConfigClusterResolver()
  devices = [
      "/job:worker/replica:0/task:%d/device:CPU:0" % cluster_resolver.task_id
  ]
  if gpu_per_process > 0:
    devices = [
        "/job:worker/replica:0/task:%d/device:GPU:%d" %
        (cluster_resolver.task_id, i) for i in range(gpu_per_process)
    ]
  group_size = num_processes * len(devices)
  collective = cross_device_ops_lib.CollectiveAllReduce(
      devices=devices,
      group_size=group_size,
      options=collective_util.Options())
  return collective, devices, cluster_resolver.task_id


# ==================================================
# Line: 192

def as_list(self, value):
  """An utility to convert a `Mirrored`, `Tensor` or `IndexedSlices` to a list.

  The reason it exists is to provide a uniformed view of returned value of
  "reduce" calls, especially across tf.function boundaries. Returning
  `Mirrored` from a tf.function will only evaluate the primary value, which
  makes collective ops of non-primary device being pruned, and will eventually
  cause hanging.

  Args:
    value: the value to convert, can be one of `Mirrored`, `Tensor` and
      `IndexedSlices`.

  Returns:
    A list of `Tensor` or `IndexedSlices`.
  """
  if isinstance(value, tensor_lib.Tensor):
    return [value]
  elif isinstance(value, IndexedSlices):
    return [value]
  elif isinstance(value, value_lib.Mirrored):
    return value.values
  else:
    raise ValueError("unwrap: unsupported input type: %s" % type(value))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
# Line: 417

def start(self):
  # A tensorflow server starts when a remote session is created.
  logging.info(
      "Creating a remote session to start a TensorFlow server, "
      "target = %r, session_config=%r", target, session_config)
  session.Session(target=target, config=session_config)


# ==================================================
# Line: 424

  def join(self):
    while True:
      time.sleep(5)

if environment == "google":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_strategy.py
# Line: 617

def experimental_replicate_to_logical_devices(self, tensor):
  """Adds annotation that `tensor` will be replicated to all logical devices.

  This adds an annotation to tensor `tensor` specifying that operations on
  `tensor` will be invoked on all logical devices.

  ```python
  # Initializing TPU system with 2 logical devices and 4 replicas.
  resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
  tf.config.experimental_connect_to_cluster(resolver)
  topology = tf.tpu.experimental.initialize_tpu_system(resolver)
  device_assignment = tf.tpu.experimental.DeviceAssignment.build(
      topology,
      computation_shape=[1, 1, 1, 2],
      num_replicas=4)
  strategy = tf.distribute.TPUStrategy(
      resolver, experimental_device_assignment=device_assignment)

  iterator = iter(inputs)

  @tf.function()
  def step_fn(inputs):
    images, labels = inputs
    images = strategy.experimental_split_to_logical_devices(
      inputs, [1, 2, 4, 1])

    # model() function will be executed on 8 logical devices with `inputs`
    # split 2 * 4  ways.
    output = model(inputs)

    # For loss calculation, all logical devices share the same logits
    # and labels.
    labels = strategy.experimental_replicate_to_logical_devices(labels)
    output = strategy.experimental_replicate_to_logical_devices(output)
    loss = loss_fn(labels, output)

    return loss

  strategy.run(step_fn, args=(next(iterator),))
  ```
  Args:
    tensor: Input tensor to annotate.

  Returns:
    Annotated tensor with identical value as `tensor`.
  """
  return xla_sharding.replicate(tensor, use_sharding_op=True)



# ==================================================
# Line: 1047

def _check_spec(self, element_spec):
  if isinstance(element_spec, values.PerReplicaSpec):
    element_spec = element_spec._component_specs  # pylint: disable=protected-access
  specs = nest.flatten_with_joined_string_paths(element_spec)
  for path, spec in specs:
    if isinstance(spec, (sparse_tensor.SparseTensorSpec,
                         ragged_tensor.RaggedTensorSpec)):
      raise ValueError(
          "Found tensor {} with spec {}. TPUStrategy does not support "
          "distributed datasets with device prefetch when using sparse or "
          "ragged tensors. If you intend to use sparse or ragged tensors, "
          "please pass a tf.distribute.InputOptions object with "
          "experimental_fetch_to_device set to False to your dataset "
          "distribution function.".format(path, type(spec)))


# ==================================================
# Occurrences: Lines 1652-1657 (2 instances)

def read_var(self, var):
  assert isinstance(var, tpu_values.TPUVariableMixin) or isinstance(
      var, resource_variable_ops.BaseResourceVariable)
  return var.read_value()


# ==================================================
# Line: 1874

def _in_multi_worker_mode(self):
  """Whether this strategy indicates working in multi-worker settings."""
  # TPUStrategy has different distributed training structure that the whole
  # cluster should be treated as single worker from higher-level (e.g. Keras)
  # library's point of view.
  # TODO(rchao): Revisit this as we design a fault-tolerance solution for
  # TPUStrategy.
  return False


# ==================================================
# Line: 1883

def _get_local_replica_id(self, replica_id_in_sync_group):
  return replica_id_in_sync_group



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
# Line: 41

def merge_call(self, fn, *args, **kwargs):
  return kwargs["test_arg"]



# ==================================================
# Line: 76

def _create_variable(self, next_creator, **kwargs):
  return _get_test_variable(kwargs["name"], kwargs["synchronization"],
                            kwargs["aggregation"])


# ==================================================
# Occurrences: Lines 88-98 (4 instances)

def _distribute_datasets_from_function(self, dataset_fn, options):
  return dataset_fn(distribute_lib.InputContext())


# ==================================================
# Line: 119

def _get_local_replica_id(self, replica_id_in_sync_group):
  return replica_id_in_sync_group



# ==================================================
# Line: 523

def testExperimentalRunV2(self):
  default_strategy = distribute_lib._get_default_strategy()
  dataset = dataset_ops.Dataset.range(10).batch(2)
  iterator = default_strategy.extended._make_dataset_iterator(dataset)
  next_val = iterator.get_next()

  def train_step(input_data):
    return input_data

  for _ in range(2):
    default_strategy.run(train_step, args=(next_val,))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
# Occurrences: Lines 273-281 (3 instances)

def _resolve_own_rank(self):
  """Returns the rank of the current task in range [0, num_tasks)."""
  return int(_get_slurm_var('PROCID'))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
# Line: 123

def mock_service_client(self, tpu_map=None):

  if tpu_map is None:
    tpu_map = {}

  mock_locations = mock.MagicMock()
  mock_locations.nodes.return_value = MockNodeClass(tpu_map)

  mock_project = mock.MagicMock()
  mock_project.locations.return_value = mock_locations

  mock_client = mock.MagicMock()
  mock_client.projects.return_value = mock_project

  return mock_client


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
# Line: 47

def api_available(self):
  return False



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
# Line: 39

def standard_mock_instance_groups(self, instance_map=None):
  if instance_map is None:
    instance_map = [
        {'instance': 'https://gce.example.com/res/gce-instance-1'}
    ]

  mock_instance_group_request = mock.MagicMock()
  mock_instance_group_request.execute.return_value = {
      'items': instance_map
  }

  service_attrs = {
      'listInstances.return_value': mock_instance_group_request,
      'listInstances_next.return_value': None,
  }
  mock_instance_groups = mock.Mock(**service_attrs)
  return mock_instance_groups


# ==================================================
# Line: 57

def standard_mock_instances(self, instance_to_ip_map=None):
  if instance_to_ip_map is None:
    instance_to_ip_map = {
        'gce-instance-1': '10.123.45.67'
    }

  mock_get_request = mock.MagicMock()
  mock_get_request.execute.return_value = {
      'networkInterfaces': [
          {'networkIP': '10.123.45.67'}
      ]
  }

  def get_side_effect(project, zone, instance):
    del project, zone  # Unused

    if instance in instance_to_ip_map:
      mock_get_request = mock.MagicMock()
      mock_get_request.execute.return_value = {
          'networkInterfaces': [
              {'networkIP': instance_to_ip_map[instance]}
          ]
      }
      return mock_get_request
    else:
      raise RuntimeError('Instance %s not found!' % instance)

  service_attrs = {
      'get.side_effect': get_side_effect,
  }
  mock_instances = mock.MagicMock(**service_attrs)
  return mock_instances


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
# Line: 112

def _maybe_trigger_a_preemption(self, training_started_event,
                                trigger_it=False):
  if not training_started_event:
    return
  clear_events = [
      event for event in training_started_event if not event.is_set()
  ]
  if clear_events:
    if trigger_it:
      logging.info('Set preemption signal')
      clear_events[0].set()
    elif random.randrange(0, 9) > 6:
      clear_events[0].set()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
# Line: 897

def _run_for_tpu(self, distributed_train_function, *args, **kwargs):
  """PreemptionCheckpointHandler.run implementation for TPUStrategy."""
  gen_check_preemption_op.check_preemption(preemption_key=PREEMPTION_KEY)
  return distributed_train_function(*args, **kwargs)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
# Line: 502

def _configure_coordination_service(self, cluster_spec: base_cluster_resolver.ClusterSpec):
  if context.context().coordination_service is None:
    coordinated_jobs = ["worker", "ps"]
    coordinated_job_config = []
    for job in coordinated_jobs:
      if job in cluster_spec.jobs:
        coordinated_job_config.append(
            coordination_config_pb2.CoordinatedJob(
                name=job,
                num_tasks=cluster_spec.num_tasks(job)))
    context.context().configure_coordination_service(
        service_type="standalone",
        service_leader=multi_worker_util.coordination_leader(
            cluster_spec),
        heartbeat_timeout_in_ms=_HEARTBEAT_TIMEOUT_SECS * 1000,
        allow_new_incarnation_to_reconnect=True)


# ==================================================
# Line: 565

def _verify_args_and_config(self, cluster_resolver: base_cluster_resolver.ClusterResolver):
  if not cluster_resolver.cluster_spec():
    raise ValueError("Cluster spec must be non-empty in "
                     "`tf.distribute.cluster_resolver.ClusterResolver`.")
  cluster_spec = cluster_resolver.cluster_spec()

  # The following checks if the task types are allowed (chief, ps, worker).
  multi_worker_util._validate_cluster_spec(  # pylint: disable=protected-access
      cluster_spec, cluster_resolver.task_type, cluster_resolver.task_id)

  if multi_worker_util.task_count(cluster_spec, "ps") < 1:
    raise ValueError("There must be at least one ps.")

  if multi_worker_util.task_count(cluster_spec, "worker") < 1:
    raise ValueError("There must be at least one worker.")



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_values.py
# Line: 442

def assign_sub(self,
               var,
               value,
               use_locking=False,
               name=None,
               read_value=True):
  if (tpu_util.enclosing_tpu_context() and
      var.aggregation == variable_scope.VariableAggregation.NONE):
    return tpu_util.make_raw_assign_fn(
        gen_resource_variable_ops.assign_sub_variable_op)(
            var,
            value=value,
            use_locking=use_locking,
            name=name,
            read_value=read_value)
  return assign_sub(
      var, value, use_locking=use_locking, name=name, read_value=read_value)


# ==================================================
# Line: 460

def assign_add(self,
               var,
               value,
               use_locking=False,
               name=None,
               read_value=True):
  if (tpu_util.enclosing_tpu_context() and
      var.aggregation == variable_scope.VariableAggregation.NONE):
    return tpu_util.make_raw_assign_fn(
        gen_resource_variable_ops.assign_add_variable_op)(
            var,
            value=value,
            use_locking=use_locking,
            name=name,
            read_value=read_value)
  return assign_add(
      var, value, use_locking=use_locking, name=name, read_value=read_value)


# ==================================================
# Line: 478

def assign(self, var, value, use_locking=False, name=None, read_value=True):
  if (tpu_util.enclosing_tpu_context() and
      var.aggregation == variable_scope.VariableAggregation.NONE):
    return tpu_util.make_raw_assign_fn(
        gen_resource_variable_ops.assign_variable_op)(
            var,
            value=value,
            use_locking=use_locking,
            name=name,
            read_value=read_value)
  return assign(
      var, value, use_locking=use_locking, name=name, read_value=read_value)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
# Line: 160

def set_v2_tensorshape(self, v2):
  if v2:
    tensor_shape.enable_v2_tensorshape()
  else:
    tensor_shape.disable_v2_tensorshape()


# ==================================================
# Line: 1280

def _configure_distribution_strategy(self, distribution):
  cluster_spec = server_lib.ClusterSpec({
      "worker": ["/job:worker/task:0", "/job:worker/task:1"]
  })
  distribution.configure(cluster_spec=cluster_spec)


# ==================================================
# Line: 1409

def _make_cross_device_ops(self):
  return cross_device_ops_lib.ReductionToOneDevice()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
# Line: 498

def _create_config(self, config):
  if config is None:
    config = config_pb2.ConfigProto(allow_soft_placement=True)
  else:
    config = copy.deepcopy(config)
  # Don't perform optimizations for tests so we don't inadvertently run
  # gpu ops on cpu
  config.graph_options.optimizer_options.opt_level = -1
  config.graph_options.rewrite_options.constant_folding = (
      rewriter_config_pb2.RewriterConfig.OFF)

  return config


# ==================================================
# Line: 734

def _run_task_in_process(self, cmd_args, cluster_spec, task_type, task_id):
  env = os.environ.copy()
  env['TF_CONFIG'] = json.dumps({
      'cluster': cluster_spec,
      'task': {
          'type': task_type,
          'index': task_id
      }
  })
  return subprocess.Popen(
      cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)


# ==================================================
# Line: 784

def stream_stderr(self, processes, print_only_first=False):
  """Consume stderr of all processes and print to stdout.

  To reduce the amount of logging, caller can set print_only_first to True.
  In that case, this function only prints stderr from the first process of
  each type.

  Args:
    processes: A dictionary from process type string -> list of processes.
    print_only_first: If true, only print output from first process of each
      type.
  """

  def _stream_stderr_single_process(process, type_string, index,
                                    print_to_stdout):
    """Consume a single process's stderr and optionally print to stdout."""
    while True:
      output = process.stderr.readline()
      if not output and process.poll() is not None:
        break
      if output and print_to_stdout:
        print('{}{} {}'.format(type_string, index, output.strip()))
        sys.stdout.flush()

  stream_threads = []
  for process_type, process_list in six.iteritems(processes):
    for i in range(len(process_list)):
      print_to_stdout = (not print_only_first) or (i == 0)
      thread = threading.Thread(
          target=_stream_stderr_single_process,
          args=(process_list[i], process_type, i, print_to_stdout))
      thread.start()
      stream_threads.append(thread)
  for thread in stream_threads:
    thread.join()



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
# Line: 152

def _raise_pss_error_if_eager(self):
  if context.executing_eagerly():
    raise NotImplementedError(
        "`tf.compat.v1.distribute.experimental.ParameterServerStrategy` "
        "currently only works with the tf.Estimator API")



# ==================================================
# Line: 534

def _select_single_value(self, structured):
  """Select any single value in `structured`."""

  def _select_fn(x):  # pylint: disable=g-missing-docstring
    if isinstance(x, values.Mirrored) or isinstance(x, values.PerReplica):
      return x._primary  # pylint: disable=protected-access
    else:
      return x

  return nest.map_structure(_select_fn, structured)


# ==================================================
# Occurrences: Lines 689-692 (2 instances)

def _get_local_replica_id(self, replica_id_in_sync_group):
  return replica_id_in_sync_group


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/shared_variable_creator_test.py
# Line: 26

def _canonicalize(self, name):
  return shared_variable_creator._canonicalize_variable_name(name)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/experimental/dtensor_strategy_extended.py
# Line: 88

def value_container(self, value):
  return value


# ==================================================
# Occurrences: Lines 103-106 (2 instances)

def _in_multi_worker_mode(self):
  return d_config.num_clients() > 1


# ==================================================
# Line: 263

def _gather_to_implementation(self, value, destinations, axis, options):
  if isinstance(value, dtensor_util.DTensorDistributedValue):
    value = value.get_dtensor()
  if not d_api.is_dtensor(value):
    # This is the current behavior for mirrored strategy, should we raise an
    # error for unsupported types?
    return value

  # Unpack the dtensor components and gather the tensors on the axis
  components = d_api.unpack(value)
  return array_ops.concat(components, axis=axis)


# ==================================================
# Line: 275

def _use_merge_call(self):
  # This is method for V1 StrategyExtended by still used by
  # tf.__internal__.distribute.strategy_supports_no_merge_call
  return False

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/sharded_variable.py
# Line: 265

def _cast(self, value, _):
  return value



# ==================================================
# Line: 916

def __tf_experimental_restore_capture__(
    self, concrete_function, internal_capture

# ==================================================
# Line: 925

def _should_act_as_resource_variable(self):
  """Pass resource_variable_ops.is_resource_variable check."""
  return True


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
# Line: 212

def _assert_eager(self):
  """Verifies that tracing is not active."""
  if not context.executing_eagerly():
    raise NotImplementedError(
        "ParallelDevice is currently not supported inside `tf.function`. It "
        "can however run calls to a `tf.function` in parallel:\n\n"
        "with ParallelDevice() as p:\n  f()")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/one_device_strategy.py
# Line: 479

def _get_local_replica_id(self, replica_id_in_sync_group):
  return replica_id_in_sync_group



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
# Line: 208

def testInputSignatureForNestedPerReplicaValues(self, distribution):
  a = np.ones((10, 2)) * 5
  b = np.ones((10, 3)) * 6
  dataset = dataset_ops.DatasetV2.from_tensor_slices((a, b)).batch(2)

  dist_dataset = distribution.experimental_distribute_dataset(dataset)

  @def_function.function(input_signature=[dist_dataset.element_spec])
  def process_inputs(inputs):
    distribution.run(lambda inputs: inputs, args=(inputs,))

  for x in dist_dataset:
    process_inputs(x)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
# Line: 623

def test_two_clusters_with_same_fn(self, enable_packed_var):
  strategy = get_tpu_strategy(enable_packed_var)

  @def_function.function
  def foo(x):
    return strategy.run(lambda x: x + 1, (x,))

  @def_function.function
  def bar(x):
    foo(x)
    return foo(x)

  bar(1)


# ==================================================
# Line: 755

def method(self, arg_1):
  del arg_1


# ==================================================
# Line: 1213

def _test_replica_order(self, create_dist_dataset_fn):
  tf2.enable()

  resolver = get_tpu_cluster_resolver()
  remote.connect_to_cluster(resolver)
  topology = tpu_cluster_resolver.initialize_tpu_system(resolver)
  device_assignment = device_assignment_lib.DeviceAssignment(
      topology, core_assignment=[[[0, 0, 0, 1]], [[0, 0, 0, 0]]]
  )
  strategy = tpu_lib.TPUStrategyV2(
      resolver, experimental_device_assignment=device_assignment
  )
  strategy.extended._enable_data_reorder = True

  dist_dataset = create_dist_dataset_fn(strategy)
  iterator = iter(dist_dataset)

  @def_function.function
  def test_iterators_order(iterator):
    return next(iterator)

  return test_iterators_order(iterator)



# ==================================================
# Line: 1337

def test_create_iterator_on_device(self):

  @def_function.function
  def create_iter():
    with ops.device("/device:TPU:0"):
      return gen_dataset_ops.anonymous_iterator_v3(
          output_types=[dtypes.float32], output_shapes=[[]])

  create_iter()



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
# Line: 84

def _worker_idx(self):
  config_task = json.loads(os.environ['TF_CONFIG'])['task']
  return config_task['index']


# ==================================================
# Line: 298

def test_barrier(self):
  multi_process_runner.run(
      fn_with_barrier,
      cluster_spec=multi_worker_test_base.create_cluster_spec(
          has_chief=True, num_workers=1),
  )


# ==================================================
# Line: 459

def test_auto_restart_failure_immediate_after_restart(self):
  # Test the case when worker-0 fails immediately after worker-1 restarts.

  def fn():
    time.sleep(5)

  mpr = multi_process_runner.MultiProcessRunner(
      fn,
      multi_worker_test_base.create_cluster_spec(
          has_chief=False, num_workers=2),
      auto_restart=True)
  mpr.start()
  pid = mpr.get_process_id('worker', 1)
  mpr.terminate('worker', 1)
  while mpr.get_process_id('worker', 1) == pid:
    time.sleep(0.1)
  mpr.terminate('worker', 0)
  mpr.join(timeout=20)


# ==================================================
# Line: 583

def test_exception_in_main_process(self):
  # When there's an exception in the main process, __del__() is not called.
  # This test is to verify MultiProcessPoolRunner can cope with __del__() not
  # being called.
  cluster_spec = multi_worker_test_base.create_cluster_spec(
      has_chief=True, num_workers=2)
  runner = multi_process_runner.MultiProcessPoolRunner(cluster_spec)
  runner.run(fn_that_returns_pid)
  raise ValueError('failure')


# ==================================================
# Occurrences: Lines 600-603 (2 instances)

def test_global_pool(self):
  _global_pool.run(fn_that_does_nothing)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/strategy_common_test.py
# Line: 49

def testCaptureReplicaId(self, strategy):
  m = {}

  @def_function.function
  def f():
    return distribute_lib.get_replica_context().replica_id_in_sync_group

  @def_function.function
  def g():
    # Make g() a stateful function so it's traced twice.
    if m.get('v', None) is None:
      m['v'] = variables.Variable(0.)
    return strategy.run(f)

  g()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
# Line: 239

def testEvaluatorNotInCluster(self):
  cluster_spec = {
      "chief": ["127.0.0.1:1234"],
      "worker": ["127.0.0.1:8964", "127.0.0.1:2333"],
      "ps": ["127.0.0.1:1926", "127.0.0.1:3141"]
  }
  multi_worker_util._validate_cluster_spec(cluster_spec, "chief", 0)
  multi_worker_util._validate_cluster_spec(cluster_spec, "worker", 0)
  multi_worker_util._validate_cluster_spec(cluster_spec, "ps", 0)
  multi_worker_util._validate_cluster_spec(cluster_spec, "evaluator", 0)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/values.py
# Line: 214

def _from_components(self, value):
  return value



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/coordinator_context.py
# Line: 61

def maybe_get_remote_value(self, ret):
  return maybe_get_remote_value(ret)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
# Line: 133

def testNotifyBeforeWait(self):
  closure_queue = coordinator_lib._CoordinatedClosureQueue()

  def func():
    logging.info('func running')

  coord = coordinator.Coordinator(clean_stop_exception_types=[])

  def process_queue():
    with coord.stop_on_exception():
      closure_queue.get()
      closure_queue.mark_finished()

  closure_queue.put(ClosureWithOutput(func, closure_queue._cancellation_mgr))
  t = threading.Thread(target=process_queue)
  t.start()
  coord.join([t])

  # This test asserts that waiting at the time the function has been processed
  # doesn't time out.
  closure_queue.wait()


# ==================================================
# Line: 177

def _run_two_fns_in_parallel(self, first_fn, second_fn):
  coord = coordinator.Coordinator(clean_stop_exception_types=[])

  def wrapped_first_fn():
    with coord.stop_on_exception():
      first_fn()

  t = threading.Thread(target=wrapped_first_fn)
  t.start()

  second_fn()
  coord.join([t])


# ==================================================
# Line: 219

def _create_closure(self, cancellation_mgr):

  @def_function.function()
  def some_function():
    return 1.0

  return ClosureWithOutput(some_function, cancellation_mgr)


# ==================================================
# Line: 297

def _set_error(self, closure_queue, closure, error):
  try:
    raise error
  except Exception as e:  # pylint: disable=broad-except
    closure.output_remote_value._set_error(e)
    closure_queue.mark_failed(e)


# ==================================================
# Line: 1003

def _long_function(self):
  x = random_ops.random_uniform((1000, 1000))
  for _ in math_ops.range(10000):
    a = random_ops.random_uniform((1000, 1000))
    b = random_ops.random_uniform((1000, 1000))
    x += math_ops.matmul(a, b)
  return x


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
# Line: 1695

def fetch(self, val):
  """Blocking call to fetch results from the remote values.

  This is a wrapper around
  `tf.distribute.experimental.coordinator.RemoteValue.fetch` for a
  `RemoteValue` structure; it returns the execution results of
  `RemoteValue`s. If not ready, wait for them while blocking the caller.

  Example:
  ```python
  strategy = ...
  coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
      strategy)

  def dataset_fn():
    return tf.data.Dataset.from_tensor_slices([1, 1, 1])

  with strategy.scope():
    v = tf.Variable(initial_value=0)

  @tf.function
  def worker_fn(iterator):
    def replica_fn(x):
      v.assign_add(x)
      return v.read_value()
    return strategy.run(replica_fn, args=(next(iterator),))

  distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn)
  distributed_iterator = iter(distributed_dataset)
  result = coordinator.schedule(worker_fn, args=(distributed_iterator,))
  assert coordinator.fetch(result) == 1
  ```

  Args:
    val: The value to fetch the results from. If this is structure of
      `tf.distribute.experimental.coordinator.RemoteValue`, `fetch()` will be
      called on the individual
      `tf.distribute.experimental.coordinator.RemoteValue` to get the result.

  Returns:
    If `val` is a `tf.distribute.experimental.coordinator.RemoteValue` or a
    structure of `tf.distribute.experimental.coordinator.RemoteValue`s,
    return the fetched `tf.distribute.experimental.coordinator.RemoteValue`
    values immediately if they are available, or block the call until they are
    available, and return the fetched
    `tf.distribute.experimental.coordinator.RemoteValue` values with the same
    structure. If `val` is other types, return it as-is.
  """

  def _maybe_fetch(val):
    if isinstance(val, RemoteValue):
      return val.fetch()
    else:
      return val

  # TODO(yuefengz): we should fetch values in a batch.
  return nest.map_structure(_maybe_fetch, val)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/coordinator/metric_utils_test.py
# Line: 47

def get_rpc_layer(self):
  return 'grpc'


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/combinations_test.py
# Line: 199

def testSysArgvClearedIsFine(self):
  original_argv = list(sys.argv)
  sys.argv.clear()
  importlib.reload(combinations)
  sys.argv = original_argv



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_run.py
# Line: 433

def _merge_call(self, fn, args, kwargs):
  """`merge_call()` implementation for synchronized replica.

  This pauses the current replica thread and passes `fn` and its arguments to
  the main thread. The main thread will wait until all replicas pause, then
  invoke `fn` with grouped arguments. The current replica thread will continue
  after `fn` completes.

  See `_call_for_each_replica` for the logic in the main thread.

  Args:
    fn: a function that is called in cross replica context with grouped
      arguments from each replica. `fn` should returns grouped values.
    args: positional arguments to `fn`.
    kwargs: keyword arguments to `fn`.

  Returns:
    Return value of `fn` for the current replica.

  Raises:
    RuntimeError: when merge_call happens in a different graph, e.g. in a
      different tf.function, which is not supported now.
    _RequestedStop: when stop is requested.
  """
  t = threading.current_thread()
  assert isinstance(t, _MirroredReplicaThread)
  t.merge_fn = fn
  t.merge_args = args
  t.merge_kwargs = kwargs
  t.captured_name_scope = t.graph.get_name_scope()
  # Adding a "/" at end lets us re-enter this scope later.
  if t.captured_name_scope:
    t.captured_name_scope += "/"

  t.captured_var_scope = variable_scope.get_variable_scope()
  t.captured_control_deps = t.graph._current_control_dependencies()  # pylint: disable=protected-access

  t.merge_call_entered_in_eager = context.context().executing_eagerly()

  # It is problematic if `merge_call` is called under a different graph other
  # than the one that `_call_for_each_replica` is called under, there are
  # 3 cases this can happen:
  #
  #   1. The `fn` passed to `_call_for_each_replica` is decorated with
  #   `tf.function` and there is a `merge_call` in `fn`. Since
  #   MirroredStrategy traces a separate function per thread (per device),
  #   and each trace takes a shared lock, the lock is never released by the
  #   first thread and subsequent replica threads cannot proceed to trace
  #   their own functions. This issue is addressed by always converting
  #   `_call_for_each_replica(tf.function(f))` to
  #   ``tf.function(_call_for_each_replica(f))`.` in
  #   `MirroredStrategy._call_for_each_replica`.
  #
  #   2. The `fn` passed to `_call_for_each_replica` contains a nested
  #   `tf.function`, and there is a `merge_call` in the nested `tf.function`.
  #   In this case each thread can successfully trace its own function, but
  #   since the `merge_fn` passed to `merge_call` is executed in the main
  #   thread (where `_call_for_each_replica` is executed), it can't access
  #   the tensors that come from different graphs.
  #
  #   3. The `fn` passed to `_call_for_each_replica` contains a control-flow
  #   statement, and there is a `merge_call` inside the control-flow body,
  #   `fn` or `_call_for_each_replica` is decorated with `tf.function`.
  #   Control flow statement creates a separate graph for its body, similar
  #   to #2, `merge_fn` executed in the main thread can't access the
  #   tensors that come from different graphs.
  #
  #   We raise an error for #2 and #3.
  if ops.get_default_graph() != t.graph:
    raise RuntimeError(
        "`merge_call` called while defining a new graph or a tf.function."
        " This can often happen if the function `fn` passed to"
        " `strategy.run()` contains a nested `@tf.function`, and the nested "
        "`@tf.function` contains a synchronization point, such as aggregating"
        " gradients (e.g, optimizer.apply_gradients), or if the function `fn`"
        " uses a control flow statement which contains a synchronization"
        " point in the body. Such behaviors are not yet supported. Instead,"
        " please avoid nested `tf.function`s or control flow statements that"
        " may potentially cross a synchronization boundary, for example,"
        " wrap the `fn` passed to `strategy.run` or the entire `strategy.run`"
        " inside a `tf.function` or move the control flow out of `fn`. If"
        " you are subclassing a `tf.keras.Model`, please avoid decorating"
        " overridden methods `test_step` and `train_step` in `tf.function`.")

  t.has_paused.set()
  t.should_run.wait()
  t.should_run.clear()
  if t.coord.should_stop():
    raise _RequestedStop()
  t.merge_call_entered_in_eager = None
  return t.merge_result


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/values_v2_test.py
# Line: 389

def create_variable(self, strategy, initial_value, enable_packed_handle,
                    **kwargs):
  variables = []
  for device in strategy.extended.parameter_devices:
    with ops.device(device):
      variables.append(variables_lib.Variable(initial_value, **kwargs))
  return values_v2.DistributedVariable(
      variables, enable_packed_handle=enable_packed_handle)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
# Line: 109

def _findFirst(self, lines, string):
  """Find first occurrence of a string in a list of strings."""
  for i, line in enumerate(lines):
    find_index = line.find(string)
    if find_index >= 0:
      return i, find_index


# ==================================================
# Line: 116

def _extractBoldNumbers(self, out, start_line):
  """Extract all numbers that have the bold font attribute.

  Args:
    out: An instance of RichTextLines.
    start_line: 0-based index to start from.

  Returns:
    A list of floats.
  """
  floats = []
  for i in range(start_line, len(out.lines)):
    if i not in out.font_attr_segs:
      continue
    line_attrs = out.font_attr_segs[i]
    for begin, end, attr_value in line_attrs:
      if attr_value == "bold":
        floats.append(float(out.lines[i][begin:end]))
  return floats


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
# Line: 80

def testSingleDevice(self):
  node1 = step_stats_pb2.NodeExecStats(
      node_name="Add/123",
      op_start_rel_micros=3,
      op_end_rel_micros=5,
      all_end_rel_micros=4)

  node2 = step_stats_pb2.NodeExecStats(
      node_name="Mul/456",
      op_start_rel_micros=1,
      op_end_rel_micros=2,
      all_end_rel_micros=3)

  run_metadata = config_pb2.RunMetadata()
  device1 = run_metadata.step_stats.dev_stats.add()
  device1.device = "deviceA"
  device1.node_stats.extend([node1, node2])

  graph = test.mock.MagicMock()
  op1 = test.mock.MagicMock()
  op1.name = "Add/123"
  op1.traceback = [("a/b/file1", 10, "some_var")]
  op1.type = "add"
  op2 = test.mock.MagicMock()
  op2.name = "Mul/456"
  op2.traceback = [("a/b/file1", 11, "some_var")]
  op2.type = "mul"
  graph.get_operations.return_value = [op1, op2]

  prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(graph, run_metadata)
  prof_output = prof_analyzer.list_profile([]).lines

  _assert_at_least_one_line_matches(r"Device 1 of 1: deviceA", prof_output)
  _assert_at_least_one_line_matches(r"^Add/123.*add.*2us.*4us", prof_output)
  _assert_at_least_one_line_matches(r"^Mul/456.*mul.*1us.*3us", prof_output)


# ==================================================
# Line: 116

def testMultipleDevices(self):
  node1 = step_stats_pb2.NodeExecStats(
      node_name="Add/123",
      op_start_rel_micros=3,
      op_end_rel_micros=5,
      all_end_rel_micros=3)

  run_metadata = config_pb2.RunMetadata()
  device1 = run_metadata.step_stats.dev_stats.add()
  device1.device = "deviceA"
  device1.node_stats.extend([node1])

  device2 = run_metadata.step_stats.dev_stats.add()
  device2.device = "deviceB"
  device2.node_stats.extend([node1])

  graph = test.mock.MagicMock()
  op = test.mock.MagicMock()
  op.name = "Add/123"
  op.traceback = [("a/b/file1", 10, "some_var")]
  op.type = "abc"
  graph.get_operations.return_value = [op]

  prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(graph, run_metadata)
  prof_output = prof_analyzer.list_profile([]).lines

  _assert_at_least_one_line_matches(r"Device 1 of 2: deviceA", prof_output)
  _assert_at_least_one_line_matches(r"Device 2 of 2: deviceB", prof_output)

  # Try filtering by device.
  prof_output = prof_analyzer.list_profile(["-d", "deviceB"]).lines
  _assert_at_least_one_line_matches(r"Device 2 of 2: deviceB", prof_output)
  _assert_no_lines_match(r"Device 1 of 2: deviceA", prof_output)


# ==================================================
# Line: 150

def testWithSession(self):
  options = config_pb2.RunOptions()
  options.trace_level = config_pb2.RunOptions.FULL_TRACE
  run_metadata = config_pb2.RunMetadata()

  with session.Session(config=no_rewrite_session_config()) as sess:
    a = constant_op.constant([1, 2, 3])
    b = constant_op.constant([2, 2, 1])
    result = math_ops.add(a, b)

    sess.run(result, options=options, run_metadata=run_metadata)

    prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(
        sess.graph, run_metadata)
    prof_output = prof_analyzer.list_profile([]).lines

    _assert_at_least_one_line_matches("Device 1 of", prof_output)
    expected_headers = [
        "Node", r"Start Time \(us\)", r"Op Time \(.*\)", r"Exec Time \(.*\)",
        r"Filename:Lineno\(function\)"]
    _assert_at_least_one_line_matches(
        ".*".join(expected_headers), prof_output)
    _assert_at_least_one_line_matches(r"^Add/", prof_output)
    _assert_at_least_one_line_matches(r"Device Total", prof_output)


# ==================================================
# Line: 227

def testFiltering(self):
  node1 = step_stats_pb2.NodeExecStats(
      node_name="Add/123",
      all_start_micros=123,
      op_start_rel_micros=3,
      op_end_rel_micros=5,
      all_end_rel_micros=4)

  node2 = step_stats_pb2.NodeExecStats(
      node_name="Mul/456",
      all_start_micros=122,
      op_start_rel_micros=1,
      op_end_rel_micros=2,
      all_end_rel_micros=5)

  run_metadata = config_pb2.RunMetadata()
  device1 = run_metadata.step_stats.dev_stats.add()
  device1.device = "deviceA"
  device1.node_stats.extend([node1, node2])

  graph = test.mock.MagicMock()
  op1 = test.mock.MagicMock()
  op1.name = "Add/123"
  op1.traceback = [("a/b/file2", 10, "some_var")]
  op1.type = "add"
  op2 = test.mock.MagicMock()
  op2.name = "Mul/456"
  op2.traceback = [("a/b/file1", 11, "some_var")]
  op2.type = "mul"
  graph.get_operations.return_value = [op1, op2]

  prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(graph, run_metadata)

  # Filter by name
  prof_output = prof_analyzer.list_profile(["-n", "Add"]).lines
  _assert_at_least_one_line_matches(r"Add/123", prof_output)
  _assert_no_lines_match(r"Mul/456", prof_output)
  # Filter by op_type
  prof_output = prof_analyzer.list_profile(["-t", "mul"]).lines
  _assert_at_least_one_line_matches(r"Mul/456", prof_output)
  _assert_no_lines_match(r"Add/123", prof_output)
  # Filter by file name.
  prof_output = prof_analyzer.list_profile(["-f", ".*file2"]).lines
  _assert_at_least_one_line_matches(r"Add/123", prof_output)
  _assert_no_lines_match(r"Mul/456", prof_output)
  # Filter by execution time.
  prof_output = prof_analyzer.list_profile(["-e", "[5, 10]"]).lines
  _assert_at_least_one_line_matches(r"Mul/456", prof_output)
  _assert_no_lines_match(r"Add/123", prof_output)
  # Filter by op time.
  prof_output = prof_analyzer.list_profile(["-o", ">=2"]).lines
  _assert_at_least_one_line_matches(r"Add/123", prof_output)
  _assert_no_lines_match(r"Mul/456", prof_output)


# ==================================================
# Line: 281

def testSpecifyingTimeUnit(self):
  node1 = step_stats_pb2.NodeExecStats(
      node_name="Add/123",
      all_start_micros=123,
      op_start_rel_micros=3,
      op_end_rel_micros=5,
      all_end_rel_micros=4)

  node2 = step_stats_pb2.NodeExecStats(
      node_name="Mul/456",
      all_start_micros=122,
      op_start_rel_micros=1,
      op_end_rel_micros=2,
      all_end_rel_micros=5)

  run_metadata = config_pb2.RunMetadata()
  device1 = run_metadata.step_stats.dev_stats.add()
  device1.device = "deviceA"
  device1.node_stats.extend([node1, node2])

  graph = test.mock.MagicMock()
  op1 = test.mock.MagicMock()
  op1.name = "Add/123"
  op1.traceback = [("a/b/file2", 10, "some_var")]
  op1.type = "add"
  op2 = test.mock.MagicMock()
  op2.name = "Mul/456"
  op2.traceback = [("a/b/file1", 11, "some_var")]
  op2.type = "mul"
  graph.get_operations.return_value = [op1, op2]

  prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(graph, run_metadata)

  # Force time unit.
  prof_output = prof_analyzer.list_profile(["--time_unit", "ms"]).lines
  _assert_at_least_one_line_matches(r"Add/123.*add.*0\.002ms", prof_output)
  _assert_at_least_one_line_matches(r"Mul/456.*mul.*0\.005ms", prof_output)
  _assert_at_least_one_line_matches(r"Device Total.*0\.009ms", prof_output)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
# Line: 115

def tearDown(self):
  ops.reset_default_graph()


# ==================================================
# Line: 324

def tearDown(self):
  ops.reset_default_graph()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
# Line: 1387

def _findSourceLine(self, annotated_source, line_number):
  """Find line of given line number in annotated source.

  Args:
    annotated_source: (debugger_cli_common.RichTextLines) the annotated source
    line_number: (int) 1-based line number

  Returns:
    (int) If line_number is found, 0-based line index in
      annotated_source.lines. Otherwise, None.
  """

  index = None
  for i, line in enumerate(annotated_source.lines):
    if line.startswith("L%d " % line_number):
      index = i
      break
  return index


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
# Line: 66

def _babble(self, args, screen_info=None):
  ap = argparse.ArgumentParser(
      description="Do babble.", usage=argparse.SUPPRESS)
  ap.add_argument(
      "-n",
      "--num_times",
      dest="num_times",
      type=int,
      default=60,
      help="How many times to babble")

  parsed = ap.parse_args(args)

  lines = ["bar"] * parsed.num_times
  return debugger_cli_common.RichTextLines(lines)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
# Line: 472

def _get_list_profile_lines(
    self, device_name, device_index, device_count,
    profile_datum_list, sort_by, sort_reverse, time_unit,
    device_name_filter=None, node_name_filter=None, op_type_filter=None,
    screen_cols=80):
  """Get `RichTextLines` object for list_profile command for a given device.

  Args:
    device_name: (string) Device name.
    device_index: (int) Device index.
    device_count: (int) Number of devices.
    profile_datum_list: List of `ProfileDatum` objects.
    sort_by: (string) Identifier of column to sort. Sort identifier
        must match value of SORT_OPS_BY_OP_NAME, SORT_OPS_BY_OP_TYPE,
        SORT_OPS_BY_EXEC_TIME, SORT_OPS_BY_MEMORY or SORT_OPS_BY_LINE.
    sort_reverse: (bool) Whether to sort in descending instead of default
        (ascending) order.
    time_unit: time unit, must be in cli_shared.TIME_UNITS.
    device_name_filter: Regular expression to filter by device name.
    node_name_filter: Regular expression to filter by node name.
    op_type_filter: Regular expression to filter by op type.
    screen_cols: (int) Number of columns available on the screen (i.e.,
      available screen width).

  Returns:
    `RichTextLines` object containing a table that displays profiling
    information for each op.
  """
  profile_data = ProfileDataTableView(profile_datum_list, time_unit=time_unit)

  # Calculate total time early to calculate column widths.
  total_op_time = sum(datum.op_time for datum in profile_datum_list)
  total_exec_time = sum(datum.node_exec_stats.all_end_rel_micros
                        for datum in profile_datum_list)
  device_total_row = [
      "Device Total", "",
      cli_shared.time_to_readable_str(total_op_time,
                                      force_time_unit=time_unit),
      cli_shared.time_to_readable_str(total_exec_time,
                                      force_time_unit=time_unit)]

  # Calculate column widths.
  column_widths = [
      len(column_name) for column_name in profile_data.column_names()]
  for col in range(len(device_total_row)):
    column_widths[col] = max(column_widths[col], len(device_total_row[col]))
  for col in range(len(column_widths)):
    for row in range(profile_data.row_count()):
      column_widths[col] = max(
          column_widths[col], len(profile_data.value(
              row,
              col,
              device_name_filter=device_name_filter,
              node_name_filter=node_name_filter,
              op_type_filter=op_type_filter)))
    column_widths[col] += 2  # add margin between columns

  # Add device name.
  output = [RL("-" * screen_cols)]
  device_row = "Device %d of %d: %s" % (
      device_index + 1, device_count, device_name)
  output.append(RL(device_row))
  output.append(RL())

  # Add headers.
  base_command = "list_profile"
  row = RL()
  for col in range(profile_data.column_count()):
    column_name = profile_data.column_names()[col]
    sort_id = profile_data.column_sort_id(col)
    command = "%s -s %s" % (base_command, sort_id)
    if sort_by == sort_id and not sort_reverse:
      command += " -r"
    head_menu_item = debugger_cli_common.MenuItem(None, command)
    row += RL(column_name, font_attr=[head_menu_item, "bold"])
    row += RL(" " * (column_widths[col] - len(column_name)))

  output.append(row)

  # Add data rows.
  for row in range(profile_data.row_count()):
    new_row = RL()
    for col in range(profile_data.column_count()):
      new_cell = profile_data.value(
          row,
          col,
          device_name_filter=device_name_filter,
          node_name_filter=node_name_filter,
          op_type_filter=op_type_filter)
      new_row += new_cell
      new_row += RL(" " * (column_widths[col] - len(new_cell)))
    output.append(new_row)

  # Add stat totals.
  row_str = ""
  for width, row in zip(column_widths, device_total_row):
    row_str += ("{:<%d}" % width).format(row)
  output.append(RL())
  output.append(RL(row_str))
  return debugger_cli_common.rich_text_lines_from_rich_line_list(output)


# ==================================================
# Line: 573

def _measure_list_profile_column_widths(self, profile_data):
  """Determine the maximum column widths for each data list.

  Args:
    profile_data: list of ProfileDatum objects.

  Returns:
    List of column widths in the same order as columns in data.
  """
  num_columns = len(profile_data.column_names())
  widths = [len(column_name) for column_name in profile_data.column_names()]
  for row in range(profile_data.row_count()):
    for col in range(num_columns):
      widths[col] = max(
          widths[col], len(str(profile_data.row_values(row)[col])) + 2)
  return widths


# ==================================================
# Line: 732

def _get_total_cost(self, aggregated_profile, cost_type):
  if cost_type == "exec_time":
    return aggregated_profile.total_exec_time
  elif cost_type == "op_time":
    return aggregated_profile.total_op_time
  else:
    raise ValueError("Unsupported cost type: %s" % cost_type)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/base_ui.py
# Line: 130

def _parse_command(self, command):
  """Parse a command string into prefix and arguments.

  Args:
    command: (str) Command string to be parsed.

  Returns:
    prefix: (str) The command prefix.
    args: (list of str) The command arguments (i.e., not including the
      prefix).
    output_file_path: (str or None) The path to save the screen output
      to (if any).
  """
  command = command.strip()
  if not command:
    return "", [], None

  command_items = command_parser.parse_command(command)
  command_items, output_file_path = command_parser.extract_output_file_path(
      command_items)

  return command_items[0], command_items[1:], output_file_path


# ==================================================
# Line: 153

def _analyze_tab_complete_input(self, text):
  """Analyze raw input to tab-completer.

  Args:
    text: (str) the full, raw input text to be tab-completed.

  Returns:
    context: (str) the context str. For example,
      If text == "print_tensor softmax", returns "print_tensor".
      If text == "print", returns "".
      If text == "", returns "".
    prefix: (str) the prefix to be tab-completed, from the last word.
      For example, if text == "print_tensor softmax", returns "softmax".
      If text == "print", returns "print".
      If text == "", returns "".
    except_last_word: (str) the input text, except the last word.
      For example, if text == "print_tensor softmax", returns "print_tensor".
      If text == "print_tensor -a softmax", returns "print_tensor -a".
      If text == "print", returns "".
      If text == "", returns "".
  """
  text = text.lstrip()
  if not text:
    # Empty (top-level) context.
    context = ""
    prefix = ""
    except_last_word = ""
  else:
    items = text.split(" ")
    if len(items) == 1:
      # Single word: top-level context.
      context = ""
      prefix = items[0]
      except_last_word = ""
    else:
      # Multiple words.
      context = items[0]
      prefix = items[-1]
      except_last_word = " ".join(items[:-1]) + " "

  return context, prefix, except_last_word


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/readline_ui.py
# Line: 119

def _display_output(self, screen_output):
  for line in screen_output.lines:
    print(line)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
# Line: 1099

def _reconstruct_print_source_command(self,
                                      parsed,
                                      line_begin,
                                      max_elements_per_line_increase=0):
  return "ps %s %s -b %d -m %d" % (
      parsed.source_file_path, "-t" if parsed.tensors else "", line_begin,
      parsed.max_elements_per_line + max_elements_per_line_increase)


# ==================================================
# Line: 1166

def _make_source_table(self, source_list, is_tf_py_library):
  """Make a table summarizing the source files that create nodes and tensors.

  Args:
    source_list: List of source files and related information as a list of
      tuples (file_path, is_tf_library, num_nodes, num_tensors, num_dumps,
      first_line).
    is_tf_py_library: (`bool`) whether this table is for files that belong
      to the TensorFlow Python library.

  Returns:
    The table as a `debugger_cli_common.RichTextLines` object.
  """
  path_head = "Source file path"
  num_nodes_head = "#(nodes)"
  num_tensors_head = "#(tensors)"
  num_dumps_head = "#(tensor dumps)"

  if is_tf_py_library:
    # Use color to mark files that are guessed to belong to TensorFlow Python
    # library.
    color = cli_shared.COLOR_GRAY
    lines = [RL("TensorFlow Python library file(s):", color)]
  else:
    color = cli_shared.COLOR_WHITE
    lines = [RL("File(s) outside TensorFlow Python library:", color)]

  if not source_list:
    lines.append(RL("[No files.]"))
    lines.append(RL())
    return debugger_cli_common.rich_text_lines_from_rich_line_list(lines)

  path_column_width = max(
      max(len(item[0]) for item in source_list), len(path_head)) + 1
  num_nodes_column_width = max(
      max(len(str(item[2])) for item in source_list),
      len(num_nodes_head)) + 1
  num_tensors_column_width = max(
      max(len(str(item[3])) for item in source_list),
      len(num_tensors_head)) + 1

  head = RL(path_head + " " * (path_column_width - len(path_head)), color)
  head += RL(num_nodes_head + " " * (
      num_nodes_column_width - len(num_nodes_head)), color)
  head += RL(num_tensors_head + " " * (
      num_tensors_column_width - len(num_tensors_head)), color)
  head += RL(num_dumps_head, color)

  lines.append(head)

  for (file_path, _, num_nodes, num_tensors, num_dumps,
       first_line_num) in source_list:
    path_attributes = [color]
    if source_utils.is_extension_uncompiled_python_source(file_path):
      path_attributes.append(
          debugger_cli_common.MenuItem(None, "ps %s -b %d" %
                                       (file_path, first_line_num)))

    line = RL(file_path, path_attributes)
    line += " " * (path_column_width - len(line))
    line += RL(
        str(num_nodes) + " " * (num_nodes_column_width - len(str(num_nodes))),
        color)
    line += RL(
        str(num_tensors) + " " *
        (num_tensors_column_width - len(str(num_tensors))), color)
    line += RL(str(num_dumps), color)
    lines.append(line)
  lines.append(RL())

  return debugger_cli_common.rich_text_lines_from_rich_line_list(lines)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
# Line: 288

def _noop_handler(self, argv, screen_info=None):
  # A handler that does nothing other than returning "Done."
  return debugger_cli_common.RichTextLines(["Done."])


# ==================================================
# Occurrences: Lines 296-306 (3 instances)

def _handler_returning_wrong_type(self, argv, screen_info=None):
  # A handler that returns a wrong type, instead of the correct type
  # (RichTextLines).
  return "Hello"


# ==================================================
# Line: 940

def _restoreFileReadWritePermissions(self, file_path):
  os.chmod(file_path,
           (stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | stat.S_IWUSR |
            stat.S_IWGRP | stat.S_IWOTH))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
# Line: 786

def _version_handler(self, args, screen_info=None):
  del args  # Unused currently.
  del screen_info  # Unused currently.
  return get_tensorflow_version_lines(include_dependency_versions=True)


# ==================================================
# Line: 976

def _common_prefix(self, m):
  """Given a list of str, returns the longest common prefix.

  Args:
    m: (list of str) A list of strings.

  Returns:
    (str) The longest common prefix.
  """
  if not m:
    return ""

  s1 = min(m)
  s2 = max(m)
  for i, c in enumerate(s1):
    if c != s2[i]:
      return s1[:i]

  return s1



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
# Line: 73

def _findFirstTraceInsideTensorFlowPyLibrary(self, op):
  """Find the first trace of an op that belongs to the TF Python library."""
  for trace in op.traceback:
    if source_utils.guess_is_tensorflow_py_library(trace.filename):
      return trace


# ==================================================
# Line: 179

  def testGRPCServerMessageSizeLimit(self):
    """Assert gRPC debug server is started with unlimited message size."""
    with test.mock.patch.object(
        grpc, "server", wraps=grpc.server) as mock_grpc_server:
      (_, _, _, server_thread,
       server) = grpc_debug_test_server.start_server_on_separate_thread(
           poll_server=True)
      mock_grpc_server.assert_called_with(
          test.mock.ANY,
          options=[("grpc.max_receive_message_length", -1),
                   ("grpc.max_send_message_length", -1)])
    server.stop_server().wait()
    server_thread.join()


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
# Line: 307

def _get_ref_args(self, node):
  """Determine whether an input of an op is ref-type.

  Args:
    node: A `NodeDef`.

  Returns:
    A list of the arg names (as strs) that are ref-type.
  """
  op_def = op_def_registry.get(node.op)
  if op_def is None:
    return []

  ref_args = []
  for i, output_arg in enumerate(op_def.output_arg):
    if output_arg.is_ref:
      arg_name = node.name if i == 0 else ("%s:%d" % (node.name, i))
      ref_args.append(arg_name)
  return ref_args


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
# Line: 225

def _process_tensor_event_in_chunks(self, event, tensor_chunks):
  """Possibly reassemble event chunks.

  Due to gRPC's message size limit, a large tensor can be encapsulated in
  multiple Event proto chunks to be sent through the debugger stream. This
  method keeps track of the chunks that have arrived, reassemble all chunks
  corresponding to a tensor when they have arrived and return the reassembled
  Event proto.

  Args:
    event: The single Event proto that has arrived.
    tensor_chunks: A dict used to keep track of the Event protos that have
      arrived but haven't been reassembled.

  Returns:
    If all Event protos corresponding to a tensor have arrived, returns the
    reassembled Event proto. Otherwise, return None.
  """

  value = event.summary.value[0]
  debugger_plugin_metadata = json.loads(
      compat.as_text(value.metadata.plugin_data.content))
  device_name = debugger_plugin_metadata["device"]
  num_chunks = debugger_plugin_metadata["numChunks"]
  chunk_index = debugger_plugin_metadata["chunkIndex"]

  if num_chunks <= 1:
    return event

  debug_node_name = value.node_name
  timestamp = int(event.wall_time)
  tensor_key = "%s_%s_%d" % (device_name, debug_node_name, timestamp)

  if tensor_key not in tensor_chunks:
    tensor_chunks[tensor_key] = [None] * num_chunks

  chunks = tensor_chunks[tensor_key]
  if value.tensor.tensor_content:
    chunks[chunk_index] = value.tensor
  elif value.tensor.string_val:
    chunks[chunk_index] = event

  if None not in chunks:
    if value.tensor.tensor_content:
      event.summary.value[0].tensor.tensor_content = b"".join(
          chunk.tensor_content for chunk in chunks)
      del tensor_chunks[tensor_key]
      return event
    elif value.tensor.string_val:
      merged_event = chunks[0]
      for chunk in chunks[1:]:
        merged_event.summary.value[0].tensor.string_val.extend(
            list(chunk.summary.value[0].tensor.string_val))
      return merged_event


# ==================================================
# Line: 461

def SendTracebacks(self, request, context):
  """Base implementation of the handling of SendTracebacks calls.

  The base implementation does nothing with the incoming request.
  Override in an implementation of the server if necessary.

  Args:
    request: A `CallTraceback` proto, containing information about the
      type (e.g., graph vs. eager execution) and source-code traceback of the
      call and (any) associated `tf.Graph`s.
    context: Server context.

  Returns:
    A `EventReply` proto.
  """
  return debug_service_pb2.EventReply()


# ==================================================
# Line: 478

def SendSourceFiles(self, request, context):
  """Base implementation of the handling of SendSourceFiles calls.

  The base implementation does nothing with the incoming request.
  Override in an implementation of the server if necessary.

  Args:
    request: A `DebuggedSourceFiles` proto, containing the path, content, size
      and last-modified timestamp of source files.
    context: Server context.

  Returns:
    A `EventReply` proto.
  """
  return debug_service_pb2.EventReply()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
# Line: 335

def _get_tensor_name(self, tensor):
  if isinstance(tensor, (tensor_lib.Tensor, variables.Variable)):
    return tensor.name
  elif isinstance(tensor, str):
    return tensor
  else:
    raise TypeError(
        "x_tensor must be a str or tf.Tensor or tf.Variable, "
        "but instead has type %s" % type(tensor))



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_events_writer.py
# Line: 156

def _EnsureTimestampAdded(self, debug_event):
  if debug_event.wall_time == 0:
    debug_event.wall_time = time.time()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
# Line: 41

def _no_rewrite_session_config(self):
  rewriter_config = rewriter_config_pb2.RewriterConfig(
      dependency_optimization=rewriter_config_pb2.RewriterConfig.OFF,
      pin_to_host_optimization=rewriter_config_pb2.RewriterConfig.OFF,
      min_graph_nodes=-1)
  graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
  return config_pb2.ConfigProto(graph_options=graph_options)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_data.py
# Line: 796

def _find_partition_graph(self, partition_graphs, device_name):
  if partition_graphs is None:
    return None
  else:
    for graph_def in partition_graphs:
      for node_def in graph_def.node:
        if node_def.device == device_name:
          return graph_def
    return None


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_service_pb2_grpc.py
# Line: 59

def SendEvents(self, request_iterator, context):
  """Client(s) can use this RPC method to send the EventListener Event protos.
  The Event protos can hold information such as:
  1) intermediate tensors from a debugged graph being executed, which can
  be sent from DebugIdentity ops configured with grpc URLs.
  2) GraphDefs of partition graphs, which can be sent from special debug
  ops that get executed immediately after the beginning of the graph
  execution.
  """
  context.set_code(grpc.StatusCode.UNIMPLEMENTED)
  context.set_details('Method not implemented!')
  raise NotImplementedError('Method not implemented!')


# ==================================================
# Line: 72

def SendTracebacks(self, request, context):
  """Send the tracebacks of ops in a Python graph definition.
  """
  context.set_code(grpc.StatusCode.UNIMPLEMENTED)
  context.set_details('Method not implemented!')
  raise NotImplementedError('Method not implemented!')


# ==================================================
# Line: 79

def SendSourceFiles(self, request, context):
  """Send a collection of source code files being debugged.
  """
  context.set_code(grpc.StatusCode.UNIMPLEMENTED)
  context.set_details('Method not implemented!')
  raise NotImplementedError('Method not implemented!')



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
# Line: 75

def _expectedDefaultDeviceName(self):
  gpu_name = test_util.gpu_device_name()
  if gpu_name:
    return "/job:localhost/replica:0/task:0" + gpu_name
  else:
    return "/job:localhost/replica:0/task:0/device:CPU:0"


# ==================================================
# Line: 110

def testDisablingTracingCallbackWithoutEnablingFirstIsTolerated(self):
  dumping_callback.disable_dump_debug_info()


# ==================================================
# Line: 767

def ceil_times_two(self, x):
  return math_ops.ceil(x) * 2.0


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
# Line: 162

def _try_makedirs(self, dir_path):
  if not os.path.isdir(dir_path):
    try:
      os.makedirs(dir_path)
    except OSError as error:
      if error.errno != errno.EEXIST:
        raise


# ==================================================
# Line: 358

def _code_def_to_traceback(self, code_def, id_to_string):
  return [(id_to_string[trace.file_id],
           trace.lineno,
           id_to_string[trace.function_id]) for trace in code_def.traces]



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
# Line: 72

def testCallingDisableCheckNumericsWithoutEnablingFirstIsTolerated(self):
  check_numerics_callback.disable_check_numerics()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
# Line: 51

def tearDown(self):
  ops.reset_default_graph()
  debug_gradients.clear_gradient_debuggers()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
# Line: 136

def on_run_end(self, request):
  return framework.OnRunEndResponse()



# ==================================================
# Line: 143

def _no_rewrite_session_config(self):
  rewriter_config = rewriter_config_pb2.RewriterConfig(
      disable_model_pruning=True)
  graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
  return config_pb2.ConfigProto(graph_options=graph_options)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/wrappers/framework.py
# Line: 685

def _is_disk_usage_reset_each_run(self):
  """Indicates whether disk usage is reset after each Session.run.

  Subclasses that clean up the disk usage after every run should
  override this protected method.

  Returns:
    (`bool`) Whether the disk usage amount is reset to zero after
      each Session.run.
  """
  return False


# ==================================================
# Line: 738

def _decorate_run_options_for_profile(self, run_options):
  """Modify a RunOptions object for profiling TensorFlow graph execution.

  Args:
    run_options: (RunOptions) the modified RunOptions object.
  """

  run_options.trace_level = config_pb2.RunOptions.FULL_TRACE


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/wrappers/grpc_wrapper.py
# Line: 126

def _normalize_grpc_url(self, address):
  return (common.GRPC_URL_PREFIX + address
          if not address.startswith(common.GRPC_URL_PREFIX) else address)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
# Line: 174

def testConstructWrapper(self):
  local_cli_wrapper.LocalCLIDebugWrapperSession(session.Session())


# ==================================================
# Occurrences: Lines 823-828 (2 instances)

def before_run(self, _):
  return session_run_hook.SessionRunArgs(fetches=c)


# ==================================================
# Line: 836

def create_session(self):
  return sess


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
# Line: 122

def _is_disk_usage_reset_each_run(self):
  # The dumped tensors are all cleaned up after every Session.run
  # in a command-line wrapper.
  return True


# ==================================================
# Line: 209

def on_session_init(self, request):
  """Overrides on-session-init callback.

  Args:
    request: An instance of `OnSessionInitRequest`.

  Returns:
    An instance of `OnSessionInitResponse`.
  """

  return framework.OnSessionInitResponse(
      framework.OnSessionInitAction.PROCEED)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/profiler_wrapper_test.py
# Occurrences: Lines 24-28 (2 instances)

def test_xspace_to_tools_data_default_options(self):
  # filenames only used for `hlo_proto` tool.
  profiler_wrapper_plugin.xspace_to_tools_data([], 'trace_viewer')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
# Line: 49

def _no_rewrite_session_config(self):
  rewriter_config = rewriter_config_pb2.RewriterConfig(
      pin_to_host_optimization=rewriter_config_pb2.RewriterConfig.OFF)
  graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
  return config_pb2.ConfigProto(graph_options=graph_options)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
# Line: 68

def test_single_worker_no_profiling(self):
  """Test single worker without profiling."""

  _, steps, train_ds, model = _model_setup()

  model.fit(x=train_ds, epochs=2, steps_per_epoch=steps)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/tfprof_logger_test.py
# Line: 25

def _BuildSmallPlaceholderlModel(self):
  a = array_ops.placeholder(dtypes.int32, [2, 2])
  b = array_ops.placeholder(dtypes.int32, [2, 2])
  y = math_ops.matmul(a, b)
  return a, b, y


# ==================================================
# Line: 31

def _BuildSmallModel(self):
  a = constant_op.constant([[1, 2], [3, 4]])
  b = constant_op.constant([[1, 2], [3, 4]])
  return math_ops.matmul(a, b)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/model_analyzer.py
# Line: 201

def profile_python(self, options):
  """Profile the statistics of the Python codes.

    By default, it shows the call stack from root. To avoid
    redundant output, you may use options to filter as below
      options['show_name_regexes'] = ['.*my_code.py.*']

  Args:
    options: A dict of options. See core/profiler/g3doc/options.md.

  Returns:
    a MultiGraphNodeProto that records the results.
  """
  opts = _build_options(options)
  tfprof_node = tfprof_output_pb2.MultiGraphNodeProto()
  try:
    tfprof_node.ParseFromString(
        print_mdl.Profile('code'.encode('utf-8'), opts.SerializeToString()))
  except message.DecodeError as e:
    sys.stderr.write('Cannot parse returned proto: %s.\n' % e)
  return tfprof_node


# ==================================================
# Line: 223

def profile_operations(self, options):
  """Profile the statistics of the Operation types (e.g.

  MatMul, Conv2D).

  Args:
    options: A dict of options. See core/profiler/g3doc/options.md.

  Returns:
    a MultiGraphNodeProto that records the results.
  """
  opts = _build_options(options)
  tfprof_node = tfprof_output_pb2.MultiGraphNodeProto()
  try:
    tfprof_node.ParseFromString(
        print_mdl.Profile('op'.encode('utf-8'), opts.SerializeToString()))
  except message.DecodeError as e:
    sys.stderr.write('Cannot parse returned proto: %s.\n' % e)
  return tfprof_node


# ==================================================
# Line: 243

def profile_name_scope(self, options):
  """Profile the statistics of graph nodes, organized by name scope.

  Args:
    options: A dict of options. See core/profiler/g3doc/options.md.

  Returns:
    a GraphNodeProto that records the results.
  """
  opts = _build_options(options)
  tfprof_node = tfprof_output_pb2.GraphNodeProto()
  try:
    tfprof_node.ParseFromString(
        print_mdl.Profile('scope'.encode('utf-8'), opts.SerializeToString()))
  except message.DecodeError as e:
    sys.stderr.write('Cannot parse returned proto: %s.\n' % e)
  return tfprof_node


# ==================================================
# Line: 261

def profile_graph(self, options):
  """Profile the statistics of graph nodes, organized by dataflow graph.

  Args:
    options: A dict of options. See core/profiler/g3doc/options.md.

  Returns:
    a GraphNodeProto that records the results.
  """
  opts = _build_options(options)
  tfprof_node = tfprof_output_pb2.GraphNodeProto()
  try:
    tfprof_node.ParseFromString(
        print_mdl.Profile('graph'.encode('utf-8'), opts.SerializeToString()))
  except message.DecodeError as e:
    sys.stderr.write('Cannot parse returned proto: %s.\n' % e)
  return tfprof_node


# ==================================================
# Line: 279

def advise(self, options):
  """Automatically detect problems and generate reports.

  Args:
    options: A dict of options. See ALL_ADVICE example above.

  Returns:
    An Advise proto that contains the reports from all checkers.
  """
  advise_pb = tfprof_output_pb2.AdviceProto()
  opts = _build_advisor_options(options)
  advise_pb.ParseFromString(
      print_mdl.Profile('advise'.encode('utf-8'), opts.SerializeToString()))
  return advise_pb


# ==================================================
# Line: 294

def serialize_to_string(self):
  """Serialize the ProfileProto to a binary string.

    Users can write it to file for offline analysis by tfprof commandline
    or graphical interface.

  Returns:
    ProfileProto binary string.
  """
  return print_mdl.SerializeToString()


# ==================================================
# Line: 305

def _write_profile(self, filename):
  """Writes the profile to a file."""
  print_mdl.WriteProfile(filename)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/profiler/internal/print_model_analysis_test.py
# Line: 50

  def _BuildSmallModel(self):
    image = array_ops.zeros([2, 6, 6, 3])
    kernel = variable_scope.get_variable(
        'DW', [6, 6, 3, 6],
        dtypes.float32,
        initializer=init_ops.random_normal_initializer(stddev=0.001))
    x = nn_ops.conv2d(image, kernel, [1, 2, 2, 1], padding='SAME')
    return x


if __name__ == '__main__':

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/tensor_test.py
# Line: 359

def testConvertToTensorAllowsOverflow(self):
  _ = ops.convert_to_tensor(123456789, dtype=dtypes.uint8)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/benchmarks_test.py
# Line: 125

def _get_benchmark_name(self):
  """Mostly copied from benchmark.py _get_name()."""
  stack = tf_inspect.stack()
  name = None
  for frame in stack[::-1]:
    f_locals = frame[0].f_locals
    f_self = f_locals.get("self", None)
    if isinstance(f_self, test.Benchmark):
      name = frame[3]  # Get the method name
      # This is a hack to get around the fact that some methods might have a
      # disable_tfrt decorator around them. In that case a function called
      # 'decorated' wraps the real called function underneath and so we
      # peek one deeper into the stack to get the real name.
      if name == "decorated":
        continue
      else:
        break
  if name is None:
    raise ValueError("Unable to determine calling Benchmark function.")
  if context.is_tfrt_enabled():
    name = name + "_tfrt"
  return name


# ==================================================
# Occurrences: Lines 1492-1496 (2 instances)

def _boolean_mask_input(self):
  n = 3000
  return (array_ops.ones([n, n]), array_ops.fill([n, n], True))


# ==================================================
# Line: 1690

def _RandomIdsAndWeights(self, batch_size, vocab_size, max_val_per_entry):
  vals_per_batch_entry = np.random.randint(
      1, max_val_per_entry, size=batch_size
  )
  num_vals = np.sum(vals_per_batch_entry)

  ids = np.random.randint(vocab_size, size=num_vals)
  weights = 1 + np.random.rand(num_vals)

  indices = []
  for batch_entry, num_val in enumerate(vals_per_batch_entry):
    for val_index in range(num_val):
      indices.append([batch_entry, val_index])

  shape = [batch_size, max_val_per_entry]

  sp_ids = sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64),
      constant_op.constant(ids, dtypes.int32),
      constant_op.constant(shape, dtypes.int64),
  )
  sp_weights = sparse_tensor.SparseTensor(
      constant_op.constant(indices, dtypes.int64),
      constant_op.constant(weights, dtypes.float32),
      constant_op.constant(shape, dtypes.int64),
  )
  return sp_ids, sp_weights


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/core_test.py
# Line: 438

def _runInThread(self, target, args):
  t = threading.Thread(target=target, args=args)
  try:
    t.start()
    t.join()
  except Exception as e:
    raise e


# ==================================================
# Line: 775

def testExecuteShapeAttr(self):
  execute(
      b'VarHandleOp',
      num_outputs=1,
      inputs=[],
      attrs=('shape', [1, 2], 'dtype', dtypes.int32.as_datatype_enum,
             'container', '', 'shared_name', ''))


# ==================================================
# Line: 794

def testExecuteListStringAttr(self):
  execute(
      b'TensorSummary',
      num_outputs=1,
      inputs=[constant_op.constant(3.0)],
      attrs=('T', dtypes.float32.as_datatype_enum, 'description',
             'tensor_summary', 'labels', ['3',
                                          'summary'], 'display_name', 'test'))


# ==================================================
# Line: 873

def testExecuteListTypeListShapeAttr(self):
  execute(
      b'Barrier',
      num_outputs=1,
      inputs=[],
      attrs=('component_types', [dtypes.float64.as_datatype_enum], 'shapes',
             [[1, 2]], 'capacity', -1, 'container', '', 'shared_name', ''))


# ==================================================
# Line: 965

def testOperationWithNoInputsRunsOnDevice(self):
  shape = constant_op.constant([], dtype=dtypes.int32)

  # x: Run the "TruncatedNormal" op CPU and copy result to GPU.
  x = truncated_normal(shape).gpu()
  # y: Explicitly run the "TruncatedNormal" op on GPU.
  with context.device('gpu:0'):
    y = truncated_normal(shape)
  # Add would fail if x and y were not on the same device.
  execute(
      b'Add', 1, inputs=[x, y], attrs=('T', x.dtype.as_datatype_enum))


# ==================================================
# Line: 1074

def _send(self, tensor, tensor_name, to_device):
  return execute(
      b'_Send', num_outputs=0, inputs=[tensor],
      attrs=('T', tensor.dtype.as_datatype_enum,
             'tensor_name', tensor_name,
             'send_device', tensor.device,
             'send_device_incarnation', 0,
             'recv_device', to_device,
             'client_terminated', True))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/pywrap_tensor_test.py
# Line: 51

def test_no_leak_cycles(self):
  for i in range(int(1e2)):
    # use multiply to avoid cached tensors.
    x = 1.0 * constant_op.constant([1.0, 1, 1, i])
    y = 1.0 * constant_op.constant([1.0, 1, 2, i])
    x.self_ref = lambda x: x
    x.y = y
    y.x = x


# ==================================================
# Line: 61

def test_no_leak_shape(self):
  for i in range(int(1e2)):
    # use multiply to avoid cached tensors.
    x = 1.0 * constant_op.constant([3.0, 1, 1, i])
    x.shape.x = x


# ==================================================
# Line: 68

  def test_no_leak_handle_data(self):
    for i in range(int(1e2)):
      # use multiply to avoid cached tensors.
      x = 1.0 * constant_op.constant([4.0, 1, 1, i])
      x._handle_data = x


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/benchmarks_test_base.py
# Line: 36

def run_with_xprof(self, enable_python_trace, run_benchmark, func,
                   num_iters_xprof, execution_mode, suid):
  if enable_python_trace:
    options = profiler.ProfilerOptions(python_tracer_level=1)
    logdir = os.path.join(flags.FLAGS.logdir, suid + "_with_python")
  else:
    options = profiler.ProfilerOptions(python_tracer_level=0)
    logdir = os.path.join(flags.FLAGS.logdir, suid)
  with profiler.Profile(logdir, options):
    total_time = run_benchmark(func, num_iters_xprof, execution_mode)
  us_per_example = float("{0:.3f}".format(total_time * 1e6 / num_iters_xprof))
  return logdir, us_per_example


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/backprop_test.py
# Line: 1714

def _jacobian(self, experimental_use_pfor):
  persistent = context.executing_eagerly and not experimental_use_pfor
  with backprop.GradientTape(persistent=persistent) as g:
    x = constant_op.constant([1., 2.])
    y = constant_op.constant([3., 4.])
    g.watch(x)
    g.watch(y)
    z = x * x * y
  jacobian = g.jacobian(
      z, [x, y], experimental_use_pfor=experimental_use_pfor)
  answer = [array_ops.diag(2 * x * y), array_ops.diag(x * x)]
  return jacobian, answer


# ==================================================
# Line: 1944

def _batch_jacobian(self, experimental_use_pfor):
  persistent = context.executing_eagerly and not experimental_use_pfor
  with backprop.GradientTape(persistent=persistent) as g:
    x = constant_op.constant([[1., 2.], [3., 4.]])
    y = constant_op.constant([[3., 4.], [5., 6.]])
    g.watch(x)
    z = x * x * y
  batch_jacobian = g.batch_jacobian(
      z, x, experimental_use_pfor=experimental_use_pfor)
  answer = array_ops_stack.stack(
      [array_ops.diag(2 * x[0] * y[0]),
       array_ops.diag(2 * x[1] * y[1])])
  return batch_jacobian, answer


# ==================================================
# Line: 2064

def test_strided_slice(self):
  x = array_ops.ones([2, 4, 2])
  length = constant_op.constant([2, 3, 4, 4], dtype=dtypes.int64)
  with backprop.GradientTape() as tape:
    tape.watch(x)
    y = array_ops.repeat(x, [2], axis=1)
    y = y[:, :math_ops.reduce_max(length), :]
  tape.batch_jacobian(y, x)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
# Line: 70

def _get_benchmark_name(self):
  """Copied from benchmarks_test.py."""
  stack = tf_inspect.stack()
  name = None
  for frame in stack[::-1]:
    f_locals = frame[0].f_locals
    f_self = f_locals.get("self", None)
    if isinstance(f_self, test.Benchmark):
      name = frame[3]  # Get the method name
      # This is a hack to get around the fact that some methods might have a
      # disable_tfrt decorator around them. In that case a function called
      # 'decorated' wraps the real called function underneath and so we
      # peek one deeper into the stack to get the real name.
      if name == "decorated":
        continue
      else:
        break
  if name is None:
    raise ValueError("Unable to determine calling Benchmark function.")
  if context.is_tfrt_enabled():
    name = name + "_tfrt"
  if context.run_eager_op_as_function_enabled():
    name = name + "_eager_op_as_function"
  return name


# ==================================================
# Line: 176

def testDefaultAttrValues(self):
  ragged_map_ops.map_fn(
      fn=lambda x: x,
      elems=ragged_factory_ops.constant([[7]]),
      dtype=ragged_tensor.RaggedTensorType(dtype=dtypes.int32, ragged_rank=1))


# ==================================================
# Occurrences: Lines 182-186 (2 instances)

def testArrayFill(self):
  array_ops.fill(
      constant_op.constant([2], dtype=dtypes.int64), constant_op.constant(1))


# ==================================================
# Line: 203

def testMixedTypeListInputEagerFallback(self):
  array_ops.identity_n([1, 1])


# ==================================================
# Line: 211

def testMixedTypeListInputEagerFallbackDifferentArity(self):
  array_ops.identity_n([1, 1])
  array_ops.identity_n([1, 1, 1])


# ==================================================
# Line: 218

def testSingleTypeListEagerFallback(self):
  array_ops.concat([[1], [2]], axis=-1)


# ==================================================
# Occurrences: Lines 225-229 (2 instances)

def testSingleTypeListEagerFallbackDifferentArity(self):
  array_ops.concat([[1], [2]], axis=-1)
  array_ops.concat([[1], [2], [3]], axis=-1)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
# Line: 373

  def testIntAttrThatDoesNotFitIn32Bits(self):
    # Tests bug where int attributes >= 2**31 raised an exception on platforms
    # where sizeof(long) = 32 bits.
    ctx = context.context()
    ctx.ensure_initialized()
    shape = constant_op.constant([10])
    minval = constant_op.constant(0)
    maxval = constant_op.constant(10)
    seed = 2**50
    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "RandomUniformInt", None,
                                      shape, minval, maxval,
                                      "seed", seed)


if __name__ == "__main__":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/remote_test.py
# Line: 116

def testStreaming(self):
  """A mini stress test for streaming - issuing many RPCs back to back."""
  with ops.device('job:worker/replica:0/task:0/device:CPU:0'):
    x = array_ops.ones([2, 2])
    y = array_ops.zeros([2, 2])
    num_iters = 200
    for _ in range(num_iters):
      y = x + y
      # Ask for y's shape after every 10 additions on average.
      # This exercises waiting for remote shape logic in TensorHandle.
      if random.randint(1, 10) == 1:
        _ = y.shape
  np.testing.assert_array_equal(
      [[num_iters, num_iters], [num_iters, num_iters]], y.numpy())


# ==================================================
# Line: 672

def testResetClusterWithDifferentJobNames(self):
  addr = 'localhost:%s' % portpicker.pick_unused_port()
  cluster = server_lib.ClusterSpec({'localhost': [addr]})
  remote.connect_to_cluster(cluster, job_name='localhost')
  with ops.device('/job:localhost/task:0/device:CPU:0'):
    v1 = variables.Variable(initial_value=0)
    v1.assign_add(1)

  # Replace job name from 'localhost' to 'worker' in the cluster.
  addr = 'localhost:%s' % portpicker.pick_unused_port()
  cluster = server_lib.ClusterSpec({'worker': [addr]})
  remote.connect_to_cluster(cluster, job_name='worker')

  with ops.device('/job:worker/task:0/device:CPU:0'):
    v2 = variables.Variable(initial_value=0)
    v2.assign_add(1)


# ==================================================
# Line: 767

def testConnectToClusterWithLocalMaster(self):
  local_resolver = SimpleClusterResolver(ClusterSpec({}), master='local')
  remote.connect_to_cluster(local_resolver)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/monitoring_test.py
# Line: 42

def test_same_counter(self):
  counter1 = monitoring.Counter('test/same_counter', 'test counter')  # pylint: disable=unused-variable
  counter2 = monitoring.Counter('test/same_counter', 'test counter')  # pylint: disable=unused-variable


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/context_test.py
# Line: 34

def testSetGlobalSeed(self):
  c = context.Context()
  c._set_global_seed(123)
  for t in [np.int32, np.int64, np.uint32, np.uint64]:
    c._set_global_seed(t(123))
    c._set_global_seed(np.array(123, dtype=t))
    c._set_global_seed(ops.convert_to_tensor(123, dtype=t))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compilation_test.py
# Line: 389

def testCallOptionsMemory(self):
  @compiled_fn
  def model(x):
    return x + constant_op.constant(1.0)

  # This happens with a lot of option toggles, e.g. soft device placement
  context.context().function_call_options = None
  model(constant_op.constant(2.0))


# ==================================================
# Line: 2090

def method(self, x):
  return x


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/concrete_function.py
# Line: 1722

def _deserialization_dependencies(self, children):
  return children


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# Line: 136

def f(self, x):
  return x * 3.



# ==================================================
# Line: 544

def func(self, a):
  if a._shape_tuple()[0] is None:
    unknown_dim[0] = True
  return a + 1


# ==================================================
# Line: 831

def testGetConcreteFunctionThreadSafetyWithArgs(self):

  @polymorphic_function.function
  def add_100(*args):
    return math_ops.add_n(args)

  p = multiprocessing.pool.ThreadPool(2)
  args = (constant_op.constant(1.),) * 100
  f1, f2 = p.map(add_100.get_concrete_function, [args] * 2)
  # I see about len(args) + max(0, len(args) - 3) arguments expected.
  f1(*args)
  del f2


# ==================================================
# Line: 1343

def testNestedDefunWithNoOutputAndTapedInput(self):
  three = resource_variable_ops.ResourceVariable(3.0, name='v')

  @polymorphic_function.function
  def f(x):
    # This function intentionally takes a taped variable as input,
    # but does not return any values
    math_ops.add(x, three)

  @polymorphic_function.function
  def g(x):
    y = math_ops.add(x, three)
    f(y)

  g(three)


# ==================================================
# Line: 1518

def testFunctionHandlesInputsPlacedOnTheWrongDeviceGracefully(self):
  # The Reshape op requires the shape tensor to be placed in host memory.
  reshape = polymorphic_function.function(array_ops.reshape)
  value = constant_op.constant([1., 2.])
  shape = constant_op.constant([2, 1]).gpu()
  reshape(value, shape)  # No error is raised


# ==================================================
# Line: 1851

def one(self, tensor):
  return tensor


# ==================================================
# Line: 1871

def func(self, other=integer):
  return other


# ==================================================
# Line: 2031

def _total_function_cache_def_func(self, defined):
  return defined._list_all_concrete_functions()  # pylint: disable=protected-access


# ==================================================
# Line: 2544

def testConcreteFunctionMethodWithVarargs(self):
  float32_scalar = tensor_lib.TensorSpec(shape=(), dtype=dtypes.float32)

  class MyModel(module.Module):

    @polymorphic_function.function(
        input_signature=[float32_scalar, float32_scalar])
    def add(self, *arg):
      return math_ops.add(*arg)

  m = MyModel()
  cf = m.add.get_concrete_function()
  cf(-12.0, 3.0)


# ==================================================
# Line: 2551

def add(self, *arg):
  return math_ops.add(*arg)


# ==================================================
# Occurrences: Lines 2599-2607 (3 instances)

def bar_none(self):
  return 1


# ==================================================
# Line: 2978

def testIndexedSlicesAsGradientsForConcreteFunctions(self):

  @polymorphic_function.function
  def summing_rnn(inputs):
    return math_ops.reduce_sum(inputs, axis=1)

  @polymorphic_function.function
  def gradients(inputs):
    with backprop.GradientTape() as tape:
      tape.watch(inputs)
      hidden = summing_rnn(inputs)
      hidden = array_ops.gather(hidden, constant_op.constant([0]))
      loss = math_ops.reduce_mean(hidden)
    return tape.gradient(loss, inputs)

  gradients(constant_op.constant([[[1.0], [2.0]]]))  # No error is raised


# ==================================================
# Occurrences: Lines 3090-3094 (2 instances)

def func(self, position_arg1, position_arg2):
  return position_arg1, position_arg2


# ==================================================
# Line: 3238

def testControlDependencyAfterInline(self):
  v = variables.Variable(0.)

  @polymorphic_function.function
  def assign():
    return v.assign(1.)

  @polymorphic_function.function
  def assign_add():
    return v.assign_add(1.)

  @polymorphic_function.function
  def f():
    check_ops.assert_equal_v2(assign(), 1.)
    check_ops.assert_equal_v2(assign_add(), 2.)

  # We don't have a way to inspect the inlined graph in Python, so we run it
  # multiple times to have more confidence the dependency is correct.
  for _ in range(30):
    f()


# ==================================================
# Line: 3587

def f6(self, arg1, arg4=4, **kwargs):
  return arg1 + arg4


# ==================================================
# Line: 3680

def f(self, arg1, arg2, arg3, arg4=4):
  return arg1 + arg2 + arg3 + arg4

# ==================================================
# Line: 4261

def f(self, x):
  return x


# ==================================================
# Line: 4422

def testDouble(self, a):
  return a + a


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
# Line: 608

def _create_implements_attribute(self, implements_arg):
  """Creates the attribute value corresponding to attribute_lib.IMPLEMENTS."""
  attributes = {}
  if isinstance(implements_arg, str):
    # First check if the attribute_lib.IMPLEMENTS is specified as a
    # NameAttrList. This is used when apart from the function name being
    # implemented, a list of attributes is also being specified.
    # The attributes are specified as key-value pairs in the NameAttrList
    # of the corresponding AttrValue. The function name will be in the
    # 'name' field of the NameAttrList. Else, it is just a string
    # corresponding to the function name.
    try:
      attr_value = attr_value_pb2.AttrValue()
      nameattrlist = attr_value_pb2.NameAttrList()
      _text_format.Merge(implements_arg, nameattrlist)
      attr_value.func.CopyFrom(nameattrlist)
      attributes[attributes_lib.IMPLEMENTS] = attr_value
    except (_text_format.ParseError, DecodeError):
      attributes[attributes_lib.IMPLEMENTS] = implements_arg
  return attributes


# ==================================================
# Line: 1075

def _initialize_uninitialized_variables(self, initializers):
  """Make and call a `ConcreteFunction` which initializes variables."""

  if not initializers:
    return

  var_is_initialized = _evaluate_var_is_initialized(
      [v for v, _ in initializers])

  def initialize_variables():
    op_map = object_identity.ObjectIdentityDictionary()

    inits = []
    for (v, init), is_initialized in zip(initializers, var_is_initialized):
      with ops.init_scope():
        if is_initialized:
          continue
      inits.append(init)

    if inits:
      op_map = lift_to_graph.lift_to_graph(
          inits, ops.get_default_graph(), op_map=op_map)
    for (v, init), is_initialized in zip(initializers, var_is_initialized):
      with ops.init_scope():
        if is_initialized:
          continue
      v.assign(op_map[init], read_value=False)

  with ops.init_scope():
    # Note: using tracing compilation here avoids an infinite recursion.
    # Most of the code in this function runs eagerly with init_scope, where
    # autograph is not necessary.
    options = tracing_compilation.TracingOptions(
        initialize_variables, "initialize_variables", autograph=False
    )
    return tracing_compilation.call_function(tracing_options=options)


# ==================================================
# Line: 1201

def _deserialization_dependencies(self, children):
  """Returns concrete functions which must be loaded before this object."""
  return children


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
# Line: 483

def f1(self, x, a):
  return x + a


# ==================================================
# Line: 496

def f1(self, x):
  return string_ops.string_length(
      string_ops.string_format('{}', x))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec_test.py
# Line: 357

def test_method_bound_internal(
    self, input_signature, type_constraint, decorator

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/concrete_function_test.py
# Line: 33

def concrete_function_with_attrs(self, attrs):
  func_graph = func_graph_module.FuncGraph("f")
  return cf.ConcreteFunction.from_func_graph(func_graph, None, attrs=attrs)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/argument_naming_test.py
# Line: 126

def method(self, x):
  return x


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/context.py
# Line: 2136

def enable_xla_devices(self):
  """Enables XLA:CPU and XLA:GPU devices registration."""
  pywrap_tfe.TF_EnableXlaDevices()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/forwardprop_test.py
# Line: 691

def testHVPMemory(self):

  def fun(x):
    return math_ops.reduce_prod(math_ops.tanh(x)**2)

  primals = constant_op.constant([1., 2., 3.])
  tangents = constant_op.constant([3., 4., 5.])
  _hvp(fun, (primals,), (tangents,))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/remote_execution_test.py
# Line: 94

def testGpuToRemoteCopy(self):
  """Tests that the remote copy happens satisfactorily."""
  x1 = array_ops.ones([2, 2]).gpu()
  with ops.device("/job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    x2 = x1._copy()  # pylint: disable=protected-access

  np.testing.assert_array_equal(x1.numpy(), x2.numpy())


# ==================================================
# Line: 104

def testGpuToRemoteOp(self):
  with ops.device("gpu:0"):
    x = array_ops.ones([2, 2])
  with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    y = math_ops.matmul(x, x)

  np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())


# ==================================================
# Line: 113

def testDefunMatmul(self):
  """Basic remote eager execution with defun."""

  mm_defun = def_function.function(math_ops.matmul)
  with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    x1 = array_ops.ones([2, 2])
  with ops.device("job:%s/replica:0/task:2/device:CPU:0" % JOB_NAME):
    x2 = array_ops.ones([2, 2])
    y = mm_defun(x1, x2)
  np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())


# ==================================================
# Line: 125

def testSimpleMatmul(self):
  """Basic remote eager execution."""

  with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    x1 = array_ops.ones([2, 2])
  with ops.device("job:%s/replica:0/task:2/device:CPU:0" % JOB_NAME):
    x2 = array_ops.ones([2, 2])
    y = math_ops.matmul(x1, x2)
  np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())


# ==================================================
# Line: 152

def testSimpleWeightRead(self):
  """Basic remote eager weight read."""

  with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    w = resource_variable_ops.ResourceVariable([[2.0]])
    loss = w * w
  np.testing.assert_array_equal([[4.0]], loss.numpy())


# ==================================================
# Line: 161

def testTapeWeightRead(self):
  """Remote eager weight read in a tape."""

  with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    w = resource_variable_ops.ResourceVariable([[3.0]])
    with backprop.GradientTape() as tape:
      loss = w * w

    grad = tape.gradient(loss, w)
  np.testing.assert_array_equal([[9.0]], loss.numpy())
  np.testing.assert_array_equal([[6.0]], grad.numpy())


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/remote_cluster_test.py
# Line: 244

def testFunctionRunsAtMostOnceInvokedOnce(self):
  """Run a function decorated with `function_runs_at_most_once`."""
  @def_function.function(
      experimental_attributes={"function_runs_at_most_once": True}
  )
  def worker_fn(i):
    return math_ops.matmul(i, i)

  x = array_ops.ones([2, 2])
  y = worker_fn(x)
  np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
  # The kernel will be destroyed at this point. The purpose of this test is
  # to ensure it tears down cleanly because we have already released the
  # function handle.


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/dlpack/dlpack_test.py
# Line: 104

def testDLPackFromWithoutContextInitialization(self):
  tf_tensor = constant_op.constant(1)
  dlcapsule = dlpack.to_dlpack(tf_tensor)
  # Resetting the context doesn't cause an error.
  context._reset_context()
  _ = dlpack.from_dlpack(dlcapsule)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
# Line: 559

def _revive_metric_from_config(self, metadata):
  """Revives a metric object using the config saved in the metadata."""
  class_name = compat.as_str(metadata['class_name'])
  config = metadata.get('config')

  if not generic_utils.validate_config(config):
    return None

  try:
    obj = metrics.deserialize(
        generic_utils.serialize_keras_class_and_config(class_name, config))
  except ValueError:
    return None

  build_input_shape = metadata.get('build_input_shape')
  if build_input_shape is not None and hasattr(obj, '_build'):
    obj._build(build_input_shape)  # pylint: disable=protected-access

  return obj


# ==================================================
# Line: 790

def _config_node_setter(self, setter):
  """Creates edges for nodes that are recreated from config."""
  def setattr_wrapper(obj, name, value):
    # Avoid overwriting attributes of objects recreated from the config.
    if obj._lookup_dependency(name) is None:  # pylint: disable=protected-access
      setter(obj, name, value)
  return setattr_wrapper



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
# Line: 420

def _generate_input_signature(self, layer):
  """Inspects layer object and returns the inferred input signature.

  Args:
    layer: Layer object.

  Returns:
    List of possibly nested TensorSpecs of the layer call function inputs.
    The list does not contain the `training` argument.
  """
  if (isinstance(layer.call, def_function.Function) and
      layer.call.input_signature is not None):
    return layer.call.input_signature
  elif isinstance(layer, training_lib.Model):
    return saving_utils.model_input_signature(layer)
  elif (layer.input_spec is not None and
        layer._use_input_spec_as_call_signature):  # pylint: disable=protected-access

    def to_tensor_spec_or_none(x):
      spec = input_spec.to_tensor_spec(x, layer._compute_dtype)  # pylint: disable=protected-access
      # If the shape is too general (e.g. multiple dimensions are allowed),
      # return None so that separate functions can be generated for each
      # inferred input signature.
      # TODO(b/134962016): currently partial signatures are not supported.
      if spec.shape == tensor_shape.TensorShape(None):
        return None
      return spec
    input_signature = [nest.map_structure(
        to_tensor_spec_or_none, layer.input_spec)]

    return input_signature
  else:
    return None


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/saving/saved_model/layer_serialization.py
# Occurrences: Lines 135-138 (2 instances)

def objects_to_serialize(self, serialization_cache):
  return {}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/saving/utils_v1/mode_keys.py
# Line: 69

def _get_internal_key(self, key):
  """Return keys used for the internal dictionary."""
  if is_train(key):
    return KerasModeKeys.TRAIN
  if is_eval(key):
    return KerasModeKeys.TEST
  if is_predict(key):
    return KerasModeKeys.PREDICT
  raise ValueError('Invalid mode key: {}.'.format(key))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/object_identity.py
# Line: 40

def _assert_type(self, other):
  if not isinstance(other, _ObjectIdentityWrapper):
    raise TypeError("Cannot compare wrapped object with unwrapped object")


# ==================================================
# Line: 132

def _wrap_key(self, key):
  return _ObjectIdentityWrapper(key)


# ==================================================
# Line: 211

def _wrap_key(self, key):
  return _ObjectIdentityWrapper(key)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/generic_utils.py
# Line: 168

def get(self, unused_object_id):
  return None


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/callbacks.py
# Line: 1487

def _checkpoint_exists(self, filepath):
  """Returns whether the checkpoint `filepath` refers to exists."""
  if filepath.endswith('.h5'):
    return file_io.file_exists_v2(filepath)
  tf_saved_model_exists = file_io.file_exists_v2(filepath)
  tf_weights_only_checkpoint_exists = file_io.file_exists_v2(
      filepath + '.index')
  return tf_saved_model_exists or tf_weights_only_checkpoint_exists


# ==================================================
# Line: 1496

def _get_most_recently_modified_file_matching_pattern(self, pattern):
  """Returns the most recently modified filepath matching pattern.

  Pattern may contain python formatting placeholder. If
  `tf.train.latest_checkpoint()` does not return None, use that; otherwise,
  check for most recently modified one that matches the pattern.

  In the rare case where there are more than one pattern-matching file having
  the same modified time that is most recent among all, return the filepath
  that is largest (by `>` operator, lexicographically using the numeric
  equivalents). This provides a tie-breaker when multiple files are most
  recent. Note that a larger `filepath` can sometimes indicate a later time of
  modification (for instance, when epoch/batch is used as formatting option),
  but not necessarily (when accuracy or loss is used). The tie-breaker is
  put in the logic as best effort to return the most recent, and to avoid
  undeterministic result.

  Modified time of a file is obtained with `os.path.getmtime()`.

  This utility function is best demonstrated via an example:

  ```python
  file_pattern = 'f.batch{batch:02d}epoch{epoch:02d}.h5'
  test_dir = self.get_temp_dir()
  path_pattern = os.path.join(test_dir, file_pattern)
  file_paths = [
      os.path.join(test_dir, file_name) for file_name in
      ['f.batch03epoch02.h5', 'f.batch02epoch02.h5', 'f.batch01epoch01.h5']
  ]
  for file_path in file_paths:
    # Write something to each of the files
  self.assertEqual(
      _get_most_recently_modified_file_matching_pattern(path_pattern),
      file_paths[-1])
  ```

  Args:
      pattern: The file pattern that may optionally contain python placeholder
          such as `{epoch:02d}`.

  Returns:
      The most recently modified file's full filepath matching `pattern`. If
      `pattern` does not contain any placeholder, this returns the filepath
      that
      exactly matches `pattern`. Returns `None` if no match is found.
  """
  dir_name = os.path.dirname(pattern)
  base_name = os.path.basename(pattern)
  base_name_regex = '^' + re.sub(r'{.*}', r'.*', base_name) + '$'

  # If tf.train.latest_checkpoint tells us there exists a latest checkpoint,
  # use that as it is more robust than `os.path.getmtime()`.
  latest_tf_checkpoint = checkpoint_management.latest_checkpoint(dir_name)
  if latest_tf_checkpoint is not None and re.match(
      base_name_regex, os.path.basename(latest_tf_checkpoint)):
    return latest_tf_checkpoint

  latest_mod_time = 0
  file_path_with_latest_mod_time = None
  n_file_with_latest_mod_time = 0
  file_path_with_largest_file_name = None

  if file_io.file_exists_v2(dir_name):
    for file_name in os.listdir(dir_name):
      # Only consider if `file_name` matches the pattern.
      if re.match(base_name_regex, file_name):
        file_path = os.path.join(dir_name, file_name)
        mod_time = os.path.getmtime(file_path)
        if (file_path_with_largest_file_name is None or
            file_path > file_path_with_largest_file_name):
          file_path_with_largest_file_name = file_path
        if mod_time > latest_mod_time:
          latest_mod_time = mod_time
          file_path_with_latest_mod_time = file_path
          # In the case a file with later modified time is found, reset
          # the counter for the number of files with latest modified time.
          n_file_with_latest_mod_time = 1
        elif mod_time == latest_mod_time:
          # In the case a file has modified time tied with the most recent,
          # increment the counter for the number of files with latest modified
          # time by 1.
          n_file_with_latest_mod_time += 1

  if n_file_with_latest_mod_time == 1:
    # Return the sole file that has most recent modified time.
    return file_path_with_latest_mod_time
  else:
    # If there are more than one file having latest modified time, return
    # the file path with the largest file name.
    return file_path_with_largest_file_name



# ==================================================
# Line: 2182

def _validate_kwargs(self, kwargs):
  """Handle arguments were supported in V1."""
  if kwargs.get('write_grads', False):
    logging.warning('`write_grads` will be ignored in TensorFlow 2.0 '
                    'for the `TensorBoard` Callback.')
  if kwargs.get('batch_size', False):
    logging.warning('`batch_size` is no longer needed in the '
                    '`TensorBoard` Callback and will be ignored '
                    'in TensorFlow 2.0.')
  if kwargs.get('embeddings_layer_names', False):
    logging.warning('`embeddings_layer_names` is not supported in '
                    'TensorFlow 2.0. Instead, all `Embedding` layers '
                    'will be visualized.')
  if kwargs.get('embeddings_data', False):
    logging.warning('`embeddings_data` is not supported in TensorFlow '
                    '2.0. Instead, all `Embedding` variables will be '
                    'visualized.')

  unrecognized_kwargs = set(kwargs.keys()) - {
      'write_grads', 'embeddings_layer_names', 'embeddings_data', 'batch_size'
  }

  # Only allow kwargs that were supported in V1.
  if unrecognized_kwargs:
    raise ValueError('Unrecognized arguments in `TensorBoard` '
                     'Callback: ' + str(unrecognized_kwargs))


# ==================================================
# Line: 2524

def _log_weight_as_image(self, weight, weight_name, epoch):
  """Logs a weight as a TensorBoard image."""
  w_img = array_ops.squeeze(weight)
  shape = backend.int_shape(w_img)
  if len(shape) == 1:  # Bias case
    w_img = array_ops.reshape(w_img, [1, shape[0], 1, 1])
  elif len(shape) == 2:  # Dense layer kernel case
    if shape[0] > shape[1]:
      w_img = array_ops.transpose(w_img)
      shape = backend.int_shape(w_img)
    w_img = array_ops.reshape(w_img, [1, shape[0], shape[1], 1])
  elif len(shape) == 3:  # ConvNet case
    if backend.image_data_format() == 'channels_last':
      # Switch to channels_first to display every kernel as a separate
      # image.
      w_img = array_ops.transpose(w_img, perm=[2, 0, 1])
      shape = backend.int_shape(w_img)
    w_img = array_ops.reshape(w_img, [shape[0], shape[1], shape[2], 1])

  shape = backend.int_shape(w_img)
  # Not possible to handle 3D convnets etc.
  if len(shape) == 4 and shape[-1] in [1, 3, 4]:
    summary_ops_v2.image(weight_name, w_img, step=epoch)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/constraints.py
# Line: 69

def get_config(self):
  """Returns a Python dict of the object config.

  A constraint config is a Python dictionary (JSON-serializable) that can
  be used to reinstantiate the same object.

  Returns:
    Python dict containing the configuration of the constraint object.
  """
  return {}



# ==================================================
# Line: 269

def _kernel_constraint(self, kernel):
  """Radially constraints a kernel with shape (height, width, channels)."""
  padding = backend.constant([[1, 1], [1, 1]], dtype='int32')

  kernel_shape = backend.shape(kernel)[0]
  start = backend.cast(kernel_shape / 2, 'int32')

  kernel_new = backend.switch(
      backend.cast(math_ops.floormod(kernel_shape, 2), 'bool'),
      lambda: kernel[start - 1:start, start - 1:start],
      lambda: kernel[start - 1:start, start - 1:start] + backend.zeros(  # pylint: disable=g-long-lambda
          (2, 2), dtype=kernel.dtype))
  index = backend.switch(
      backend.cast(math_ops.floormod(kernel_shape, 2), 'bool'),
      lambda: backend.constant(0, dtype='int32'),
      lambda: backend.constant(1, dtype='int32'))
  while_condition = lambda index, *args: backend.less(index, start)

  def body_fn(i, array):
    return i + 1, array_ops.pad(
        array,
        padding,
        constant_values=kernel[start + i, start + i])

  _, kernel_new = while_loop.while_loop(
      while_condition,
      body_fn, [index, kernel_new],
      shape_invariants=[
          index.get_shape(),
          tensor_shape.TensorShape([None, None])
      ])
  return kernel_new



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
# Line: 523

def _get_default_initializer(self, name, shape=None, dtype=dtypes.float32):
  """Provide a default initializer and a corresponding value.

  Args:
    name: see get_variable.
    shape: see get_variable.
    dtype: see get_variable.

  Returns:
    initializer and initializing_from_value. See get_variable above.

  Raises:
    ValueError: When giving unsupported dtype.
  """
  del shape
  # If dtype is DT_FLOAT, provide a uniform unit scaling initializer
  if dtype.is_floating:
    initializer = init_ops.glorot_uniform_initializer()
    initializing_from_value = False
  # If dtype is DT_INT/DT_UINT, provide a default value `zero`
  # If dtype is DT_BOOL, provide a default value `FALSE`
  elif (dtype.is_integer or dtype.is_unsigned or dtype.is_bool or
        dtype == dtypes.string):
    initializer = init_ops.zeros_initializer()
    initializing_from_value = False
  # NOTES:Do we need to support for handling DT_STRING and DT_COMPLEX here?
  else:
    raise ValueError("An initializer for variable %s of %s is required" %
                     (name, dtype.base_dtype))

  return initializer, initializing_from_value



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
# Line: 724

def _raise_if_strategy_unsupported(self):
  if not strategy_supports_loss_scaling():
    strategy = distribute_lib.get_strategy()
    if isinstance(strategy,
                  (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV1,
                   tpu_strategy.TPUStrategyV2)):
      raise ValueError(
          'Loss scaling is not supported with TPUStrategy. Loss scaling is '
          'unnecessary with TPUs, since they support bfloat16 instead of '
          'float16 and bfloat16 does not require loss scaling. You should '
          'remove the use of the LossScaleOptimizer when TPUs are used.')
    else:
      raise ValueError('Loss scaling is not supported with the '
                       'tf.distribute.Strategy: %s. Try using a different '
                       'Strategy, e.g. a MirroredStrategy' %
                       strategy.__class__.__name__)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
# Line: 196

def _parse_name(self, name):
  """Parses a Policy name into a compute and variable dtype.

  Args:
    name: The name of the policy:

  Returns:
    The (compute_dtype, variable_dtype) pair.
  """
  if name.endswith('_float32_vars'):
    error_msg = ('Policies ending in \'_float32_vars\' have been removed '
                 'from TensorFlow.')
    if name in ('infer_float32_vars', 'infer_with_float32_vars'):
      error_msg += (' Please use the \'mixed_float16\' or \'mixed_bfloat16\' '
                    'policy instead.')
    elif name == 'float16_with_float32_vars':
      error_msg += (' Please use the \'mixed_float16\' policy instead.')
    elif name == 'bfloat16_with_float32_vars':
      error_msg += (' Please use the \'mixed_bfloat16\' policy instead.')
    error_msg += ' Got policy name: \'%s\'' % name
    raise ValueError(error_msg)

  if name == 'mixed_float16':
    return 'float16', 'float32'
  elif name == 'mixed_bfloat16':
    return 'bfloat16', 'float32'
  elif name == '_infer':
    # The "_infer" policy exists only for compatibility with TF 1, where
    # "_infer" is the default. The behavior matches the behavior of TF 1's
    # behavior before policies were introduced. With "_infer", the computation
    # and variable dtype are inferred from the first input the first time the
    # layer is called. Once the layer is called for the first time, the
    # layer's policy will change to the dtype of the first input, and it will
    # no longer have the "_infer" policy.
    #
    # The infer policy should be considered an implementation detail and may
    # be removed in the future.
    return None, None

  try:
    dtype = dtypes.as_dtype(name).name
  except TypeError:
    error = ("Cannot convert value %s to a mixed precision Policy. "
             "Valid policies include 'mixed_float16', 'mixed_bfloat16', "
             "and the name of any dtype such as 'float32'." % (name,))
    raise ValueError(error)
  return dtype, dtype


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
# Line: 85

def get_config(self):
  """Returns the configuration of the initializer as a JSON-serializable dict.

  Returns:
    A JSON-serializable Python dict.
  """
  return {}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/optimizer_v1.py
# Line: 777

def _clip_gradients(self, grads):
  """Clip gradients according to the clipnorm and clipvalue attributes."""
  # TFOptimizer wrapper has no gradient clipping options.
  return grads


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/compile_utils.py
# Line: 261

def _get_loss_object(self, loss):
  """Returns a `Loss` object.

  Converts the user-supplied loss to a `Loss` object. Also allows
  `SUM_OVER_BATCH_SIZE` reduction to be used for this loss.

  Args:
    loss: A string, function, or `Loss` object.

  Returns:
    A `Loss` object.
  """
  if loss is None:
    return None  # Ok to have no loss for an output.

  loss = losses_mod.get(loss)
  if not isinstance(loss, losses_mod.Loss):
    loss_name = get_custom_object_name(loss)
    if loss_name is None:
      raise ValueError('Loss should be a callable, found: {}'.format(loss))
    loss = losses_mod.LossFunctionWrapper(loss, name=loss_name)
  loss._allow_sum_over_batch_size = True  # pylint: disable=protected-access
  return loss


# ==================================================
# Line: 487

def _get_metric_object(self, metric, y_t, y_p):
  """Converts user-supplied metric to a `Metric` object.

  Args:
    metric: A string, function, or `Metric` object.
    y_t: Sample of label.
    y_p: Sample of output.

  Returns:
    A `Metric` object.
  """
  if metric is None:
    return None  # Ok to have no metric for an output.

  # Convenience feature for selecting b/t binary, categorical,
  # and sparse categorical.
  if str(metric).lower() not in ['accuracy', 'acc', 'crossentropy', 'ce']:
    metric_obj = metrics_mod.get(metric)
  else:
    y_t_rank = len(y_t.shape.as_list())
    y_p_rank = len(y_p.shape.as_list())
    y_t_last_dim = y_t.shape.as_list()[-1]
    y_p_last_dim = y_p.shape.as_list()[-1]

    is_binary = y_p_last_dim == 1
    is_sparse_categorical = (
        y_t_rank < y_p_rank or y_t_last_dim == 1 and y_p_last_dim > 1)

    if str(metric).lower() in ['accuracy', 'acc']:
      if is_binary:
        metric_obj = metrics_mod.binary_accuracy
      elif is_sparse_categorical:
        metric_obj = metrics_mod.sparse_categorical_accuracy
      else:
        metric_obj = metrics_mod.categorical_accuracy
    else:
      if is_binary:
        metric_obj = metrics_mod.binary_crossentropy
      elif is_sparse_categorical:
        metric_obj = metrics_mod.sparse_categorical_crossentropy
      else:
        metric_obj = metrics_mod.categorical_crossentropy

  if isinstance(metric_obj, losses_mod.Loss):
    metric_obj._allow_sum_over_batch_size = True  # pylint: disable=protected-access

  if not isinstance(metric_obj, metrics_mod.Metric):
    if isinstance(metric, str):
      metric_name = metric
    else:
      metric_name = get_custom_object_name(metric)
      if metric_name is None:
        raise ValueError(
            'Metric should be a callable, found: {}'.format(metric))

    metric_obj = metrics_mod.MeanMetricWrapper(metric_obj, name=metric_name)

  return metric_obj


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# Line: 848

def _standardize_batch(self, data):
  """Standardizes a batch output by a generator."""
  # Removes `None`s.
  x, y, sample_weight = unpack_x_y_sample_weight(data)
  data = pack_x_y_sample_weight(x, y, sample_weight)

  data = nest.list_to_tuple(data)

  def _convert_dtype(t):
    if (isinstance(t, np.ndarray) and issubclass(t.dtype.type, np.floating)):
      return np.array(t, dtype=backend.floatx())
    return t

  data = nest.map_structure(_convert_dtype, data)
  return data


# ==================================================
# Line: 869

def _handle_multiprocessing(self, x, workers, use_multiprocessing,
                            max_queue_size):
  """Create a callable, possibly including an Enqueuer."""
  if workers > 1 or (workers > 0 and use_multiprocessing):
    def generator_fn():
      enqueuer = data_utils.GeneratorEnqueuer(
          x, use_multiprocessing=use_multiprocessing)
      enqueuer.start(workers=workers, max_queue_size=max_queue_size)
      return enqueuer.get()
  else:
    generator_fn = lambda: x
  return generator_fn


# ==================================================
# Line: 1221

def sync(self):
  context.async_wait()


# ==================================================
# Line: 1299

def _log_indefinite_training_warning(self):
  logging.warning("The training loop will run indefinitely since you have "
                  "set `steps_per_epoch=-1`. Please use batch-level "
                  "callbacks to save checkpoints or log training progress, "
                  "etc")


# ==================================================
# Line: 1352

def _convert_to_dataset_creator(self, x, y, **kwargs):
  """Converts non-tf.data.Dataset to `DatasetCreator` instances."""

  def _dataset_fn(input_context):
    del input_context
    data_adapter_cls = select_data_adapter(x, y)
    return data_adapter_cls(x=x, y=y, **kwargs).get_dataset()

  # This check is needed because types like `tf.data.Dataset` don't work with
  # PSS yet. So only apply this logic to the types we can support.
  if (isinstance(x, _get_tensor_types()) and
      isinstance(y, _get_tensor_types())):
    return dataset_creator.DatasetCreator(_dataset_fn)
  else:
    raise NotImplementedError(
        "Only `tf.keras.utils.experimental.DatasetCreator`, `tf.Tensor`, "
        "numpy arrays and pandas dataframes are supported types at this "
        "time.")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
# Line: 252

def __array__(self):
  raise TypeError(
      'Cannot convert a symbolic Keras input/output to a numpy array. '
      'This error may indicate that you\'re trying to pass a symbolic value '
      'to a NumPy call, which is not supported. Or, '
      'you may be trying to pass Keras symbolic inputs/outputs '
      'to a TF API that does not register dispatching, '
      'preventing Keras from automatically '
      'converting the API call to a lambda layer '
      'in the Functional Model.')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
# Line: 282

def call(self, inputs, **kwargs):  # pylint: disable=unused-argument
  """This is where the layer's logic lives.

  Args:
      inputs: Input tensor, or list/tuple of input tensors.
      **kwargs: Additional keyword arguments.

  Returns:
      A tensor or list/tuple of tensors.
  """
  return inputs


# ==================================================
# Line: 2275

def _is_layer(self):
  return True


# ==================================================
# Line: 2329

def _dedup_weights(self, weights):
  """Dedupe weights while maintaining order as much as possible."""
  output, seen_ids = [], set()
  for w in weights:
    if id(w) not in seen_ids:
      output.append(w)
      # Track the Variable's identity to avoid __eq__ issues.
      seen_ids.add(id(w))

  return output


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/partial_batch_padding_handler.py
# Line: 34

def get_real_batch_size(self, dataset_batch):
  """Returns the number of elements in a potentially partial batch."""
  if isinstance(dataset_batch, (tuple, list)):
    dataset_batch = dataset_batch[0]

  assert nest.flatten(dataset_batch)

  def _find_any_tensor(batch_features):
    tensors = [
        x for x in nest.flatten(batch_features) if tensor_util.is_tf_type(x)
    ]
    if not tensors:
      raise ValueError('Cannot find any Tensor in features dict.')
    return tensors[0]

  return backend.cast(backend.shape(_find_any_tensor(dataset_batch))[0],
                      dtype='int64')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/functional.py
# Line: 604

def _conform_to_reference_input(self, tensor, ref_input):
  """Set shape and dtype based on `keras.Input`s."""
  if isinstance(tensor, tensor_lib.Tensor):
    # Allow (None,) and (None, 1) Tensors to be passed interchangeably. Use
    # the shape specified by the `keras.Input`.
    t_shape = tensor.shape
    t_rank = t_shape.rank
    ref_shape = ref_input.shape
    ref_rank = ref_shape.rank
    keras_history = getattr(tensor, '_keras_history', None)
    if t_rank is not None and ref_rank is not None:
      # Should squeeze last dimension.
      # True if tensor is (BATCH, ..., 1) and reference is (BATCH, ...).
      if (t_rank == ref_rank + 1 and t_shape[-1] == 1):
        tensor = array_ops.squeeze_v2(tensor, axis=-1)
      # Should expand last_dimension.
      # True if tensor is (BATCH, ...) and reference is (BATCH, ..., 1).
      elif (t_rank == ref_rank - 1 and ref_shape[-1] == 1):
        tensor = array_ops.expand_dims_v2(tensor, axis=-1)
    if keras_history is not None:  # Restore keras history.
      tensor._keras_history = keras_history

    # Add shape hints to Tensors that may have None shape dims but have shapes
    # defined by the `keras.Input` (not applicable in eager mode).
    if not context.executing_eagerly():
      try:
        tensor.set_shape(tensor.shape.merge_with(ref_input.shape))
      except ValueError:
        logging.warning(
            'Model was constructed with shape {} for input {}, but it was '
            'called on an input with incompatible shape {}.'.format(
                ref_input.shape, ref_input, tensor.shape))

    # Dtype casting.
    tensor = math_ops.cast(tensor, dtype=ref_input.dtype)
  elif tf_utils.is_extension_type(tensor):
    # Dtype casting (If the extension type has a non-variant dtype and
    # supports being cast)
    ref_input_dtype = getattr(ref_input, 'dtype', None)
    if ref_input_dtype is not None and ref_input_dtype != dtypes.variant:
      tensor = math_ops.cast(tensor, dtype=ref_input_dtype)

  return tensor


# ==================================================
# Line: 843

def _assert_weights_created(self):
  # Override the implementation in Model.
  # The Functional model should always have weight created already.
  return


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/training.py
# Line: 2408

def to_yaml(self, **kwargs):
  """Returns a yaml string containing the network configuration.

  Note: Since TF 2.6, this method is no longer supported and will raise a
  RuntimeError.

  To load a network from a yaml save file, use
  `keras.models.model_from_yaml(yaml_string, custom_objects={})`.

  `custom_objects` should be a dictionary mapping
  the names of custom losses / layers / etc to the corresponding
  functions / classes.

  Args:
      **kwargs: Additional keyword arguments
          to be passed to `yaml.dump()`.

  Returns:
      A YAML string.

  Raises:
      RuntimeError: announces that the method poses a security risk
  """
  raise RuntimeError(
      'Method `model.to_yaml()` has been removed due to security risk of '
      'arbitrary code execution. Please use `model.to_json()` instead.'
  )


# ==================================================
# Line: 2756

def _should_eval(self, epoch, validation_freq):
  epoch = epoch + 1  # one-index the user-facing epoch.
  if isinstance(validation_freq, int):
    return epoch % validation_freq == 0
  elif isinstance(validation_freq, list):
    return epoch in validation_freq
  else:
    raise ValueError('Expected `validation_freq` to be a list or int.')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Line: 465

def call(self, inputs, *args, **kwargs):  # pylint: disable=unused-argument
  """This is where the layer's logic lives.

  Note here that `call()` method in `tf.keras` is little bit different
  from `keras` API. In `keras` API, you can pass support masking for
  layers as additional arguments. Whereas `tf.keras` has `compute_mask()`
  method to support masking.

  Args:
    inputs: Input tensor, or dict/list/tuple of input tensors.
      The first positional `inputs` argument is subject to special rules:
      - `inputs` must be explicitly passed. A layer cannot have zero
        arguments, and `inputs` cannot be provided via the default value
        of a keyword argument.
      - NumPy array or Python scalar values in `inputs` get cast as tensors.
      - Keras mask metadata is only collected from `inputs`.
      - Layers are built (`build(input_shape)` method)
        using shape info from `inputs` only.
      - `input_spec` compatibility is only checked against `inputs`.
      - Mixed precision input casting is only applied to `inputs`.
        If a layer has tensor arguments in `*args` or `**kwargs`, their
        casting behavior in mixed precision should be handled manually.
      - The SavedModel input specification is generated using `inputs` only.
      - Integration with various ecosystem packages like TFMOT, TFLite,
        TF.js, etc is only supported for `inputs` and not for tensors in
        positional and keyword arguments.
    *args: Additional positional arguments. May contain tensors, although
      this is not recommended, for the reasons above.
    **kwargs: Additional keyword arguments. May contain tensors, although
      this is not recommended, for the reasons above.
      The following optional keyword arguments are reserved:
      - `training`: Boolean scalar tensor of Python boolean indicating
        whether the `call` is meant for training or inference.
      - `mask`: Boolean input mask. If the layer's `call()` method takes a
        `mask` argument, its default value will be set to the mask generated
        for `inputs` by the previous layer (if `input` did come from a layer
        that generated a corresponding mask, i.e. if it came from a Keras
        layer with masking support).

  Returns:
    A tensor or list/tuple of tensors.
  """
  return inputs


# ==================================================
# Line: 1688

def add_update(self, updates, inputs=None):
  """Add update op(s), potentially dependent on layer inputs.

  Weight updates (for instance, the updates of the moving mean and variance
  in a BatchNormalization layer) may be dependent on the inputs passed
  when calling a layer. Hence, when reusing the same layer on
  different inputs `a` and `b`, some entries in `layer.updates` may be
  dependent on `a` and some on `b`. This method automatically keeps track
  of dependencies.

  This call is ignored when eager execution is enabled (in that case, variable
  updates are run on the fly and thus do not need to be tracked for later
  execution).

  Args:
    updates: Update op, or list/tuple of update ops, or zero-arg callable
      that returns an update op. A zero-arg callable should be passed in
      order to disable running the updates by setting `trainable=False`
      on this Layer, when executing in Eager mode.
    inputs: Deprecated, will be automatically inferred.
  """
  if inputs is not None:
    tf_logging.warning(
        '`add_update` `inputs` kwarg has been deprecated. You no longer need '
        'to pass a value to `inputs` as it is being automatically inferred.')
  call_context = base_layer_utils.call_context()
  # No need to run updates during Functional API construction.
  if call_context.in_keras_graph:
    return

  # Callable updates are disabled by setting `trainable=False`.
  if not call_context.frozen:
    for update in nest.flatten(updates):
      if callable(update):
        update()  # pylint: disable=not-callable


# ==================================================
# Line: 2501

def _set_mask_keras_history_checked(self, flat_outputs):
  for output in flat_outputs:
    if getattr(output, '_keras_mask', None) is not None:
      # Do not track masks for `TensorFlowOpLayer` construction.
      output._keras_mask._keras_history_checked = True


# ==================================================
# Line: 2901

def _is_layer(self):
  return True


# ==================================================
# Line: 2985

def _dedup_weights(self, weights):
  """Dedupe weights while maintaining order as much as possible."""
  output, seen_ids = [], set()
  for w in weights:
    if id(w) not in seen_ids:
      output.append(w)
      # Track the Variable's identity to avoid __eq__ issues.
      seen_ids.add(id(w))

  return output


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/training_v1.py
# Line: 1900

def _handle_per_output_metrics(self,
                               metrics_dict,
                               y_true,
                               y_pred,
                               mask,
                               weights=None):
  """Calls metric functions for a single output.

  Args:
    metrics_dict: A dict with metric names as keys and metric fns as values.
    y_true: Target output.
    y_pred: Predicted output.
    mask: Computed mask value for the current output.
    weights: Weights to be applied on the current output.

  Returns:
    A list of metric result tensors.
  """
  metric_results = []
  for metric_name, metric_fn in metrics_dict.items():
    with backend.name_scope(metric_name):
      metric_result = training_utils_v1.call_metric_function(
          metric_fn, y_true, y_pred, weights=weights, mask=mask)
      metric_results.append(metric_result)
  return metric_results


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
# Occurrences: Lines 460-469 (3 instances)

def _transform_loss(self, loss):
  """Called in `.minimize` to transform loss before computing gradients."""
  return loss


# ==================================================
# Line: 1225

def _valid_dtypes(self):
  """Valid types for loss, variables and gradients.

  Subclasses should override to allow other float types.

  Returns:
    Valid types for loss, variables and gradients.
  """
  return _DEFAULT_VALID_DTYPES


# ==================================================
# Line: 1235

def _call_if_callable(self, param):
  """Call the function if param is callable."""
  return param() if callable(param) else param


# ==================================================
# Line: 1302

def _resource_scatter_add(self, x, i, v):
  with ops.control_dependencies([
      gen_resource_variable_ops.ResourceScatterAdd(
          resource=x.handle, indices=i, updates=v)
  ]):
    return x.value()


# ==================================================
# Line: 1309

def _resource_scatter_update(self, x, i, v):
  with ops.control_dependencies(
      [gen_resource_variable_ops.ResourceScatterUpdate(
          resource=x.handle, indices=i, updates=v)]):
    return x.value()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/distribute/distribute_coordinator_utils.py
# Line: 381

def start(self):
  # A tensorflow server starts when a remote session is created.
  logging.info(
      "Creating a remote session to start a TensorFlow server, "
      "target = %r, session_config=%r", target, session_config)
  session.Session(target=target, config=session_config)


# ==================================================
# Line: 388

  def join(self):
    while True:
      time.sleep(5)

if environment == "google":

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/recurrent.py
# Line: 888

def _maybe_reset_cell_dropout_mask(self, cell):
  if isinstance(cell, DropoutRNNCellMixin):
    cell.reset_dropout_mask()
    cell.reset_recurrent_dropout_mask()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/convolutional.py
# Line: 308

def _recreate_conv_op(self, inputs):  # pylint: disable=unused-argument
  return False


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/pooling.py
# Line: 977

def compute_mask(self, inputs, mask=None):
  return None



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/dense_attention.py
# Line: 82

def _calculate_scores(self, query, key):
  """Calculates attention scores.

  Args:
    query: Query tensor of shape `[batch_size, Tq, dim]`.
    key: Key tensor of shape `[batch_size, Tv, dim]`.

  Returns:
    Tensor of shape `[batch_size, Tq, Tv]`.
  """
  return NotImplementedError


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/merge.py
# Line: 200

def compute_mask(self, inputs, mask=None):
  if mask is None:
    return None
  if not isinstance(mask, (tuple, list)):
    raise ValueError('`mask` should be a list.')
  if not isinstance(inputs, (tuple, list)):
    raise ValueError('`inputs` should be a list.')
  if len(mask) != len(inputs):
    raise ValueError('The lists `inputs` and `mask` '
                     'should have the same length.')
  if all(m is None for m in mask):
    return None
  masks = [array_ops.expand_dims(m, axis=0) for m in mask if m is not None]
  return backend.all(
      backend.concatenate(masks, axis=0), axis=0, keepdims=False)



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
# Line: 202

def _variational_recurrent_dropout_value(
    self, unused_index, value, noise, keep_prob):
  """Performs dropout given the pre-calculated noise tensor."""
  # uniform [keep_prob, 1.0 + keep_prob)
  random_tensor = keep_prob + noise

  # 0. if [keep_prob, 1.0) and 1. if [1.0, 1.0 + keep_prob)
  binary_tensor = math_ops.floor(random_tensor)
  ret = math_ops.divide(value, keep_prob) * binary_tensor
  ret.set_shape(value.get_shape())
  return ret


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/layers/core.py
# Line: 126

def compute_output_shape(self, input_shape):
  return input_shape


# ==================================================
# Line: 224

def compute_output_shape(self, input_shape):
  return input_shape


# ==================================================
# Line: 428

def compute_output_shape(self, input_shape):
  return input_shape


# ==================================================
# Line: 480

def _fix_unknown_dimension(self, input_shape, output_shape):
  """Find and replace a missing dimension in an output shape.

  This is a near direct port of the internal Numpy function
  `_fix_unknown_dimension` in `numpy/core/src/multiarray/shape.c`

  Args:
    input_shape: Shape of array being reshaped
    output_shape: Desired shape of the array with at most
      a single -1 which indicates a dimension that should be
      derived from the input shape.

  Returns:
    The new output shape with a -1 replaced with its computed value.

  Raises:
    ValueError: If the total array size of the output_shape is
    different than the input_shape, or more than one unknown dimension
    is specified.
  """
  output_shape = list(output_shape)
  msg = ('total size of new array must be unchanged, '
         'input_shape = {}, output_shape = {}'
         .format(input_shape, output_shape))

  known, unknown = 1, None
  for index, dim in enumerate(output_shape):
    if dim < 0:
      if unknown is None:
        unknown = index
      else:
        raise ValueError('Can only specify one unknown dimension.')
    else:
      known *= dim

  original = np.prod(input_shape, dtype=int)
  if unknown is not None:
    if known == 0 or original % known != 0:
      raise ValueError(msg)
    output_shape[unknown] = original // known
  elif original != known:
    raise ValueError(msg)
  return output_shape


# ==================================================
# Line: 677

def compute_output_shape(self, input_shape):
  input_shape = tensor_shape.TensorShape(input_shape).as_list()
  if not input_shape:
    output_shape = tensor_shape.TensorShape([1])
  else:
    output_shape = [input_shape[0]]
  if np.all(input_shape[1:]):
    output_shape += [np.prod(input_shape[1:], dtype=int)]
  else:
    output_shape += [None]
  return tensor_shape.TensorShape(output_shape)


# ==================================================
# Line: 946

def _warn(self, msg):
  # This method will be overridden in a unit test to raise an error, because
  # self.assertWarns is not universally implemented.
  return tf_logging.warning(msg)


# ==================================================
# Line: 980

def _serialize_function_to_config(self, inputs, allow_raw=False):
  if isinstance(inputs, python_types.LambdaType):
    output = generic_utils.func_dump(inputs)
    output_type = 'lambda'
    module = inputs.__module__
  elif callable(inputs):
    output = inputs.__name__
    output_type = 'function'
    module = inputs.__module__
  elif allow_raw:
    output = inputs
    output_type = 'raw'
    module = None
  else:
    raise ValueError(
        'Invalid input for serialization, type: %s ' % type(inputs))

  return output, output_type, module


# ==================================================
# Line: 1292

def compute_output_shape(self, input_shape):
  return input_shape


# ==================================================
# Line: 1421

def _warn(self, msg):
  # This method will be overridden in a unit test to raise an error, because
  # self.assertWarns is not universally implemented.
  return tf_logging.warning(msg)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/backend.py
# Line: 6434

def _key(self):
  if context.executing_eagerly():
    return _DUMMY_EAGER_GRAPH.key
  else:
    return ops.get_default_graph()


# ==================================================
# Line: 6440

def _get_parent_graph(self, graph):
  """Returns the parent graph or dummy eager object."""
  # TODO(b/149317164): Currently FuncGraphs use ops.get_default_graph() as the
  # outer graph. This results in outer_graph always being a Graph,
  # even in eager mode (get_default_graph will create a new Graph if there
  # isn't a default graph). Because of this bug, we have to specially set the
  # key when eager execution is enabled.
  parent_graph = graph.outer_graph
  if (not isinstance(parent_graph, func_graph.FuncGraph) and
      ops.executing_eagerly_outside_functions()):
    return _DUMMY_EAGER_GRAPH.key
  return parent_graph


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/testing_utils.py
# Line: 538

def _layer_name_for_i(self, i):
  return 'layer{}'.format(i)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/lib/io/tf_record_test.py
# Line: 71

def _Record(self, f, r):
  return compat.as_bytes("Record %d of file %d" % (r, f))


# ==================================================
# Line: 583

def _Record(self, r):
  return compat.as_bytes("Record %d" % r)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/lib/io/file_io_test.py
# Line: 324

def _setupWalkDirectories(self, dir_path):
  # Creating a file structure as follows
  # test_dir -> file: file1.txt; dirs: subdir1_1, subdir1_2, subdir1_3
  # subdir1_1 -> file: file3.txt
  # subdir1_2 -> dir: subdir2
  file_io.create_dir(dir_path)
  file_io.FileIO(
      file_io.join(dir_path, "file1.txt"), mode="w").write("testing")
  sub_dirs1 = ["subdir1_1", "subdir1_2", "subdir1_3"]
  for name in sub_dirs1:
    file_io.create_dir(file_io.join(dir_path, name))
  file_io.FileIO(
      file_io.join(dir_path, "subdir1_1/file2.txt"),
      mode="w").write("testing")
  file_io.create_dir(file_io.join(dir_path, "subdir1_2/subdir2"))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/lib/io/file_io.py
# Line: 244

def seekable(self):
  """Returns True as FileIO supports random access ops of seek()/tell()"""
  return True



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compat/compat_test.py
# Occurrences: Lines 25-29 (2 instances)

def _compatibility_date(self):
  date = compat._FORWARD_COMPATIBILITY_HORIZON  # pylint: disable=protected-access
  return (date.year, date.month, date.day)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/moving_averages_test.py
# Line: 94

def testAssignMovingAverageNewNamingMultipleCallsWithReuse(self):
  with variable_scope.variable_scope("scope1") as vs1:
    var = variable_scope.get_variable("Var", shape=[])
    moving_averages.assign_moving_average(var, 0.0, 0.99)
    moving_averages.assign_moving_average(var, 0.0, 0.99)
  with variable_scope.variable_scope(vs1, reuse=True):
    var = variable_scope.get_variable("Var", shape=[])
    moving_averages.assign_moving_average(var, 0.0, 0.99)
    moving_averages.assign_moving_average(var, 0.0, 0.99)


# ==================================================
# Line: 550

def _ExportAndImportGraph(self, graph):
  """Export and import graph into a new graph."""
  meta_graph = saver_lib.export_meta_graph(
      graph=graph, collection_list=graph.get_all_collection_keys())
  graph_copy = ops.Graph()
  with graph_copy.as_default():
    _ = saver_lib.import_meta_graph(meta_graph)
  return graph_copy


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Line: 88

def _create_dummy_inputs(self):
  return {
      "sc_int": array_ops.sparse_placeholder(dtypes.int32),
      "sc_hash": array_ops.sparse_placeholder(dtypes.string),
      "sc_keys": array_ops.sparse_placeholder(dtypes.string),
      "sc_vocab": array_ops.sparse_placeholder(dtypes.string),
      "real": array_ops.placeholder(dtypes.float32)
  }


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/saving/saveable_object.py
# Line: 78

def restore(self, restored_tensors, restored_shapes):
  """Restores this object from 'restored_tensors'.

  Args:
    restored_tensors: the tensors that were loaded from a checkpoint
    restored_shapes: the shapes this object should conform to after
      restore, or None.

  Returns:
    An operation that restores the state of the object.

  Raises:
    ValueError: If the object cannot be restored using the provided
      parameters.
  """
  # pylint: disable=unused-argument
  raise ValueError("Calling an abstract method.")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
# Line: 133

def _create_resource(self):
  return gen_resource_variable_ops.var_handle_op(
      shape=[],
      dtype=dtypes.float32,
      shared_name=context.anonymous_name(),
      name="StateVar",
      container="")


# ==================================================
# Line: 228

def _serialize_to_tensors(self):
  return {}


# ==================================================
# Line: 235

def _gather_saveables_for_checkpoint(self):
  return {}


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/adam_test.py
# Line: 356

def testTwoSessions(self):
  optimizer = adam.AdamOptimizer()

  with context.eager_mode():
    var0 = variables.Variable(np.array([1.0, 2.0]), name="v0")
    grads0 = constant_op.constant(np.array([0.1, 0.1]))
    optimizer.apply_gradients([(grads0, var0)])

  g = ops.Graph()
  with g.as_default():
    with session.Session():
      var0 = variables.Variable(np.array([1.0, 2.0]), name="v0")
      grads0 = constant_op.constant(np.array([0.1, 0.1]))
      optimizer.apply_gradients([(grads0, var0)])

  gg = ops.Graph()
  with gg.as_default():
    with session.Session():
      var0 = variables.Variable(np.array([1.0, 2.0]), name="v0")
      grads0 = constant_op.constant(np.array([0.1, 0.1]))

      # If the optimizer saves any state not keyed by graph the following line
      # fails.
      optimizer.apply_gradients([(grads0, var0)])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/supervisor_test.py
# Line: 254

def _csv_data(self, logdir):
  # Create a small data file with 3 CSV records.
  data_path = os.path.join(logdir, "data.csv")
  with open(data_path, "w") as f:
    f.write("1,2,3\n")
    f.write("4,5,6\n")
    f.write("7,8,9\n")
  return data_path


# ==================================================
# Line: 490

def testNoLogdirSucceeds(self):
  with ops.Graph().as_default():
    variable_v1.VariableV1([1.0, 2.0, 3.0])
    sv = supervisor.Supervisor(logdir="", summary_op=None)
    sess = sv.prepare_or_wait_for_session("")
    sess.close()
    sv.stop()


# ==================================================
# Line: 498

def testUseSessionManager(self):
  with ops.Graph().as_default():
    variable_v1.VariableV1([1.0, 2.0, 3.0])
    sm = session_manager_lib.SessionManager()
    # Pass in session_manager. The additional init_op is ignored.
    sv = supervisor.Supervisor(logdir="", session_manager=sm)
    sv.prepare_or_wait_for_session("")


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/coordinator_test.py
# Line: 160

def testJoinWithoutGraceExpires(self):
  coord = coordinator.Coordinator()
  wait_for_stop_ev = threading.Event()
  has_stopped_ev = threading.Event()
  threads = [
      threading.Thread(
          target=StopOnEvent, args=(coord, wait_for_stop_ev, has_stopped_ev)),
      threading.Thread(target=SleepABit, args=(10.0,))
  ]
  for t in threads:
    t.daemon = True
    t.start()
  wait_for_stop_ev.set()
  has_stopped_ev.wait()
  coord.join(threads, stop_grace_period_secs=1., ignore_live_threads=True)


# ==================================================
# Line: 215

def testJoinIgnoresOutOfRange(self):
  coord = coordinator.Coordinator()
  ev_1 = threading.Event()
  threads = [
      threading.Thread(
          target=RaiseOnEvent,
          args=(coord, ev_1, None,
                errors_impl.OutOfRangeError(None, None, "First"), True))
  ]
  for t in threads:
    t.start()

  ev_1.set()
  coord.join(threads)


# ==================================================
# Line: 230

def testJoinIgnoresMyExceptionType(self):
  coord = coordinator.Coordinator(clean_stop_exception_types=(ValueError,))
  ev_1 = threading.Event()
  threads = [
      threading.Thread(
          target=RaiseOnEvent,
          args=(coord, ev_1, None, ValueError("Clean stop"), True))
  ]
  for t in threads:
    t.start()

  ev_1.set()
  coord.join(threads)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/supervisor.py
# Line: 367

def _get_first_op_from_collection(self, key):
  """Returns the first `Operation` from a collection.

  Args:
    key: A string collection key.

  Returns:
    The first Op found in a collection, or `None` if the collection is empty.
  """
  try:
    op_list = ops.get_collection(key)
    if len(op_list) > 1:
      logging.info("Found %d %s operations. Returning the first one.",
                   len(op_list), key)
    if op_list:
      return op_list[0]
  except LookupError:
    pass

  return None


# ==================================================
# Line: 900

def _default_global_step_tensor(self):
  """Returns the global_step from the default graph.

  Returns:
    The global step `Tensor` or `None`.
  """
  try:
    gs = ops.get_default_graph().get_tensor_by_name("global_step:0")
    if gs.dtype.base_dtype in [dtypes.int32, dtypes.int64]:
      return gs
    else:
      logging.warning("Found 'global_step' is not an int type: %s", gs.dtype)
      return None
  except KeyError:
    return None


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/sync_replicas_optimizer_test.py
# Line: 86

def _run(self, train_op, sess):
  sess.run(train_op)


# ==================================================
# Line: 273

def testCanCreatedBeforeMinimizeCalled(self):
  opt = training.SyncReplicasOptimizer(
      opt=gradient_descent.GradientDescentOptimizer(1.0),
      replicas_to_aggregate=1,
      total_num_replicas=1)
  hook = opt.make_session_run_hook(True)
  v = variable_v1.VariableV1([0.])
  global_step = variable_v1.VariableV1(0, name="global_step", trainable=False)
  opt.minimize(v, global_step=global_step)
  hook.begin()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/server_lib_test.py
# Line: 108

def _useRPCConfig(self):
  """Return a `tf.compat.v1.ConfigProto` that ensures we use the RPC stack for tests.

  This configuration ensures that we continue to exercise the gRPC
  stack when testing, rather than using the in-process optimization,
  which avoids using gRPC as the transport between a client and
  master in the same process.

  Returns:
    A `tf.compat.v1.ConfigProto`.
  """
  return config_pb2.ConfigProto(
      rpc_options=rpc_options_pb2.RPCOptions(
          use_rpc_for_inprocess_master=True
      )
  )


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/adam.py
# Line: 287

def _resource_scatter_add(self, x, i, v):
  with ops.control_dependencies(
      [resource_variable_ops.resource_scatter_add(x.handle, i, v)]):
    return x.value()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/rmsprop_test.py
# Line: 57

def _rmsprop_update_numpy(self, var, g, mg, rms, mom, lr, decay, momentum,
                          epsilon, centered):
  rms_t = rms * decay + (1 - decay) * g * g
  denom_t = rms_t + epsilon
  if centered:
    mg_t = mg * decay + (1 - decay) * g
    denom_t -= mg_t * mg_t
  else:
    mg_t = mg
  mom_t = momentum * mom + lr * g / np.sqrt(denom_t, dtype=denom_t.dtype)
  var_t = var - mom_t
  return var_t, mg_t, rms_t, mom_t


# ==================================================
# Line: 70

def _sparse_rmsprop_update_numpy(self, var, gindexs, gvalues, mg, rms, mom,
                                 lr, decay, momentum, epsilon, centered):
  mg_t = copy.deepcopy(mg)
  rms_t = copy.deepcopy(rms)
  mom_t = copy.deepcopy(mom)
  var_t = copy.deepcopy(var)
  for i in range(len(gindexs)):
    gindex = gindexs[i]
    gvalue = gvalues[i]
    rms_t[gindex] = rms[gindex] * decay + (1 - decay) * gvalue * gvalue
    denom_t = rms_t[gindex] + epsilon
    if centered:
      mg_t[gindex] = mg_t[gindex] * decay + (1 - decay) * gvalue
      denom_t -= mg_t[gindex] * mg_t[gindex]
    mom_t[gindex] = momentum * mom[gindex] + lr * gvalue / np.sqrt(denom_t)
    var_t[gindex] = var[gindex] - mom_t[gindex]
  return var_t, mg_t, rms_t, mom_t


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
# Line: 146

def _scale_grad(self, grad, loss_scale_reciprocal):
  if isinstance(grad, indexed_slices.IndexedSlices):
    grad_vals = grad.values * loss_scale_reciprocal
    return indexed_slices.IndexedSlices(grad_vals, grad.indices,
                                        grad.dense_shape)
  return grad * loss_scale_reciprocal


# ==================================================
# Occurrences: Lines 232-244 (4 instances)

def _apply_sparse(self, grad, var):
  """This function should never be called."""
  raise RuntimeError('This function should never be called')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
# Line: 121

def _run_fn_with_grad_check(self, strategy, var, opt, expected_grad):
  grad_check_fn = create_identity_with_grad_check_fn(
      expected_grad)
  loss = lambda: grad_check_fn(var) / strategy.num_replicas_in_sync
  return lambda: opt.minimize(loss, var_list=[var])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
# Line: 175

def test_warn_if_session_already_exists(self, mock_warn):
  # Set this to False, so Sessions created in previous tests do not trigger
  # the warning.
  mixed_precision_global_state.set_non_mixed_precision_session_created(False)

  with session.Session():
    mixed_precision.enable_mixed_precision_graph_rewrite_v1(
        gradient_descent_v1.GradientDescentOptimizer(1.0))
    mock_warn.assert_any_call(
        'You already have existing Sessions that do not use mixed precision. '
        'enable_mixed_precision_graph_rewrite() will not affect these '
        'Sessions.')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
# Line: 105

def _get_tensor(self, is_finite):
  tensor = cond.cond(is_finite, lambda: 1., lambda: float('NaN'))

  if not distribute_lib.has_strategy():
    return tensor

  def get():
    rep_id = (
        distribute_lib.get_replica_context()
        .replica_id_in_sync_group)
    return cond.cond(
        math_ops.equal(rep_id, 0), lambda: tensor, lambda: 1.)

  distribution = distribute_lib.get_strategy()
  return distribution.extended.call_for_each_replica(get)


# ==================================================
# Line: 290

def test_update_with_none_gradients(self):
  loss_scale = loss_scale_module.DynamicLossScale()
  loss_scale.update([None])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/saver.py
# Line: 181

def restore_op(self, filename_tensor, saveable, preferred_shard):
  """Create ops to restore 'saveable'.

  This is intended to be overridden by subclasses that want to generate
  different Ops.

  Args:
    filename_tensor: String Tensor.
    saveable: A BaseSaverBuilder.SaveableObject object.
    preferred_shard: Int.  Shard to open first when loading a sharded file.

  Returns:
    A list of Tensors resulting from reading 'saveable' from
      'filename'.
  """
  # pylint: disable=protected-access
  tensors = []
  for spec in saveable.specs:
    tensors.append(
        io_ops.restore_v2(filename_tensor, [spec.name], [spec.slice_spec],
                          [spec.dtype])[0])

  return tensors


# ==================================================
# Line: 207

def sharded_filename(self, filename_tensor, shard, num_shards):
  """Append sharding information to a filename.

  Args:
    filename_tensor: A string tensor.
    shard: Integer.  The shard for the filename.
    num_shards: An int Tensor for the number of shards.

  Returns:
    A string tensor.
  """
  return gen_io_ops.sharded_filename(filename_tensor, shard, num_shards)


# ==================================================
# Line: 417

def _GroupByDevices(self, saveables):
  """Group Variable tensor slices per device.

  TODO(touts): Make sure that all the devices found are on different
  job/replica/task/cpu|gpu.  It would be bad if 2 were on the same device.
  It can happen if the devices are unspecified.

  Args:
    saveables: A list of BaseSaverBuilder.SaveableObject objects.

  Returns:
    A list of tuples: (device_name, BaseSaverBuilder.SaveableObject) tuples.
    The list is sorted by ascending device_name.

  Raises:
    ValueError: If the tensors of a saveable are on different devices.
  """
  per_device = collections.defaultdict(lambda: [])
  for saveable in saveables:
    canonical_device = set(
        pydev.canonical_name(spec.device) for spec in saveable.specs)
    if len(canonical_device) != 1:
      raise ValueError("All tensors of a saveable object must be "
                       "on the same device: %s" % saveable.name)
    per_device[canonical_device.pop()].append(saveable)
  return sorted(per_device.items(), key=lambda t: t[0])


# ==================================================
# Line: 1015

def _CheckpointFilename(self, p):
  """Returns the checkpoint filename given a `(filename, time)` pair.

  Args:
    p: (filename, time) pair.

  Returns:
    Checkpoint file name.
  """
  name, _ = p
  return name


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/training_ops_test.py
# Line: 39

def _toType(self, dtype):
  if dtype == np.float16:
    return dtypes.float16
  elif dtype == np.float32:
    return dtypes.float32
  elif dtype == np.float64:
    return dtypes.float64
  elif dtype == np.int32:
    return dtypes.int32
  elif dtype == np.int64:
    return dtypes.int64
  else:
    assert False, (dtype)


# ==================================================
# Line: 450

def _adamUpdateNumpy(self, param, g_t, t, m, v, alpha, beta1, beta2, epsilon):
  alpha_t = alpha * np.sqrt(1 - beta2**t) / (1 - beta1**t)

  m_t = beta1 * m + (1 - beta1) * g_t
  v_t = beta2 * v + (1 - beta2) * g_t * g_t

  param_t = param - alpha_t * m_t / (np.sqrt(v_t) + epsilon)
  return param_t, m_t, v_t


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/monitored_session_test.py
# Line: 1174

def create_raw_session_with_failing_coordinator(self, session_creator, hook):
  """Return MonitoredSession that triggers coordinator failures."""
  session = monitored_session.MonitoredSession(session_creator, [hook])
  # We would like to test a situation where during fetches through the
  # raw session, the coordinator fails with an exception.  To do that, we
  # are going to use (raw_session + StopCoordinatorWithException) hook
  # combination that is stored in
  # `MonitoredSession._RecoverableSession._CoordinatedSession._sess`
  # at this point:
  session._tf_sess = lambda: session._sess._sess._sess
  # `run()` on such a session is equivalent to `run()` on the raw session
  # with separate coordinator threads independently stopping with an
  # exception.
  return session


# ==================================================
# Line: 2029

def step_fn(self, step_context):
  return step_context.run_with_hooks(fetches=v, feed_dict={c: 3.2})


# ==================================================
# Line: 2041

def step_fn(self, step_context, extra_foo):
  del step_context, extra_foo


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/session_manager.py
# Line: 480

def _safe_close(self, sess: session.Session):
  """Closes a session without raising an exception.

  Just like sess.close() but ignores exceptions.

  Args:
    sess: A `Session`.
  """
  # pylint: disable=broad-except
  try:
    sess.close()
  except Exception:
    # Intentionally not logging to avoid user complaints that
    # they get cryptic errors.  We really do not care that Close
    # fails.
    pass
  # pylint: enable=broad-except


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/momentum_test.py
# Line: 36

def _update_nesterov_momentum_numpy(self, var, accum, g, lr, momentum):
  var = var + accum * lr * momentum
  accum = accum * momentum + g
  var = var - lr * accum
  var = var - accum * lr * momentum
  return var, accum


# ==================================================
# Line: 345

def _dbParamsMom01(self):
  """Return dist-belief momentum values.

  Return values been generated from the dist-belief momentum unittest,
  running with a learning rate of 0.1 and a momentum of 0.1.

  These values record how a parameter vector of size 10, initialized with 0.0,
  gets updated with 10 consecutive momentum steps.  It uses random gradients.

  Returns:
    db_grad: The gradients to apply
    db_out: The parameters after the momentum update.
  """
  db_grad = [[]] * 10
  db_out = [[]] * 10
  # pylint: disable=line-too-long
  db_grad[0] = [
      0.00096264342, 0.17914793, 0.93945462, 0.41396621, 0.53037018,
      0.93197989, 0.78648776, 0.50036013, 0.55345792, 0.96722615
  ]
  db_out[0] = [
      -9.6264346e-05, -0.017914793, -0.093945466, -0.041396622, -0.053037018,
      -0.093197994, -0.078648776, -0.050036013, -0.055345792, -0.096722618
  ]
  db_grad[1] = [
      0.17075552, 0.88821375, 0.20873757, 0.25236958, 0.57578111, 0.15312378,
      0.5513742, 0.94687688, 0.16012503, 0.22159521
  ]
  db_out[1] = [
      -0.017181443, -0.10852765, -0.12421377, -0.070773244, -0.11591884,
      -0.11783017, -0.14165108, -0.14972731, -0.076892875, -0.1285544
  ]
  db_grad[2] = [
      0.35077485, 0.47304362, 0.44412705, 0.44368884, 0.078527533, 0.81223965,
      0.31168157, 0.43203235, 0.16792089, 0.24644311
  ]
  db_out[2] = [
      -0.053967446, -0.1648933, -0.1716533, -0.1180798, -0.13005978,
      -0.20151734, -0.17911947, -0.20289968, -0.095839672, -0.15638189
  ]
  db_grad[3] = [
      0.9694621, 0.75035888, 0.28171822, 0.83813518, 0.53807181, 0.3728098,
      0.81454384, 0.03848977, 0.89759839, 0.93665648
  ]
  db_out[3] = [
      -0.15459226, -0.24556576, -0.20456907, -0.20662397, -0.18528105,
      -0.24716705, -0.2643207, -0.21206589, -0.18749419, -0.2528303
  ]
  db_grad[4] = [
      0.38578293, 0.8536852, 0.88722926, 0.66276771, 0.13678469, 0.94036359,
      0.69107032, 0.81897682, 0.5433259, 0.67860287
  ]
  db_out[4] = [
      -0.20323303, -0.33900154, -0.29658359, -0.28175515, -0.20448165,
      -0.34576839, -0.34194785, -0.29488021, -0.25099224, -0.33033544
  ]
  db_grad[5] = [
      0.27885768, 0.76100707, 0.24625534, 0.81354135, 0.18959245, 0.48038563,
      0.84163809, 0.41172323, 0.83259648, 0.44941229
  ]
  db_out[5] = [
      -0.23598288, -0.42444581, -0.33041057, -0.3706224, -0.22536094,
      -0.40366709, -0.43387437, -0.34433398, -0.34060168, -0.38302717
  ]
  db_grad[6] = [
      0.27233034, 0.056316052, 0.5039115, 0.24105175, 0.35697976, 0.75913221,
      0.73577434, 0.16014607, 0.57500273, 0.071136251
  ]
  db_out[6] = [
      -0.26649091, -0.43862185, -0.38418442, -0.40361428, -0.26314685,
      -0.48537019, -0.51664448, -0.36529395, -0.40706289, -0.39540997
  ]
  db_grad[7] = [
      0.58697265, 0.2494842, 0.08106143, 0.39954534, 0.15892942, 0.12683646,
      0.74053431, 0.16033, 0.66625422, 0.73515922
  ]
  db_out[7] = [
      -0.32823896, -0.46498787, -0.39766794, -0.446868, -0.28281838,
      -0.50622416, -0.59897494, -0.38342294, -0.48033443, -0.47016418
  ]
  db_grad[8] = [
      0.8215279, 0.41994119, 0.95172721, 0.68000203, 0.79439718, 0.43384039,
      0.55561525, 0.22567581, 0.93331909, 0.29438227
  ]
  db_out[8] = [
      -0.41656655, -0.50961858, -0.49418902, -0.51919359, -0.36422527,
      -0.55169362, -0.6627695, -0.40780342, -0.58099347, -0.50707781
  ]
  db_grad[9] = [
      0.68297005, 0.67758518, 0.1748755, 0.13266537, 0.70697063, 0.055731893,
      0.68593478, 0.50580865, 0.12602448, 0.093537711
  ]
  db_out[9] = [
      -0.49369633, -0.58184016, -0.52132869, -0.5396927, -0.44306302,
      -0.56181377, -0.73774242, -0.46082234, -0.60366184, -0.52012295
  ]
  # pylint: enable=line-too-long
  return db_grad, db_out


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/queue_runner_impl.py
# Line: 282

def _close_on_stop(self, sess, cancel_op, coord):
  """Close the queue when the Coordinator requests stop.

  Args:
    sess: A Session.
    cancel_op: The Operation to run.
    coord: Coordinator.
  """
  coord.wait_for_stop()
  try:
    sess.run(cancel_op)
  except Exception as e:
    # Intentionally ignore errors from cancel_op.
    logging.vlog(1, "Ignored exception: %s", str(e))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/monitored_session.py
# Line: 867

def request_stop(self):
  """Exit the training loop by causing `should_stop()` to return `True`.

     Causes `step_fn` to exit by raising an exception.

  Raises:
    StopIteration
  """
  raise StopIteration('step_fn has requested the iterations to stop.')


# ==================================================
# Line: 1207

def _check_stop(self):
  """Hook for subclasses to provide their own stop condition.

  Returns:
    True if the session should stop, False otherwise.
  """
  return False


# ==================================================
# Occurrences: Lines 1510-1515 (2 instances)

def _raise_if_feeds_intersects(self, feeds1, feeds2, message):
  intersection = set(feeds1.keys()) & set(feeds2.keys())
  if intersection:
    raise RuntimeError(message + ' Conflict(s): ' + str(list(intersection)))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/session_run_hook.py
# Line: 125

def before_run(self, run_context):  # pylint: disable=unused-argument
  """Called before each call to run().

  You can return from this call a `SessionRunArgs` object indicating ops or
  tensors to add to the upcoming `run()` call.  These ops/tensors will be run
  together with the ops/tensors originally passed to the original run() call.
  The run args you return can also contain feeds to be added to the run()
  call.

  The `run_context` argument is a `SessionRunContext` that provides
  information about the upcoming `run()` call: the originally requested
  op/tensors, the TensorFlow Session.

  At this point graph is finalized and you can not add ops.

  Args:
    run_context: A `SessionRunContext` object.

  Returns:
    None or a `SessionRunArgs` object.
  """
  return None


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/optimizer.py
# Line: 1061

def _valid_dtypes(self):
  """Valid types for loss, variables and gradients.

  Subclasses should override to allow other float types.

  Returns:
    Valid types for loss, variables and gradients.
  """
  return set(
      [dtypes.float16, dtypes.bfloat16, dtypes.float32, dtypes.float64])


# ==================================================
# Line: 1214

def _finish(self, update_ops, name_scope):
  """Do what is needed to finish the update.

  This is called with the `name_scope` using the "name" that
  users have chosen for the application of gradients.

  Args:
    update_ops: List of `Operation` objects to update variables.  This list
      contains the values returned by the `_apply_dense()` and
      `_apply_sparse()` calls.
    name_scope: String.  Name to use for the returned operation.

  Returns:
    The operation to apply updates.
  """
  return control_flow_ops.group(*update_ops, name=name_scope)


# ==================================================
# Line: 1404

def _call_if_callable(self, param):
  """Call the function if param is callable."""
  return param() if callable(param) else param

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
# Line: 1329

def test_not_wait_for_step_zero(self):
  with ops.Graph().as_default():
    training_util.get_or_create_global_step()
    hook = basic_session_run_hooks.GlobalStepWaiterHook(wait_until_step=0)
    hook.begin()
    with session_lib.Session() as sess:
      # Before run should return without waiting gstep increment.
      hook.before_run(
          session_run_hook.SessionRunContext(
              original_args=None, session=sess))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/datasets_test.py
# Line: 230

def as_tensor_shape(self, proto_with_symbolic_values):
  for i in range(len(proto_with_symbolic_values.dim)):
    if proto_with_symbolic_values.dim[i].size < -1:
      proto_with_symbolic_values.dim[i].size = -1
  return tensor_shape.TensorShape(proto_with_symbolic_values)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
# Line: 355

def _lower_precision_dtype(self, mode):
  return dtypes.float16 if mode == 'cuda' else dtypes.bfloat16


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/cluster.py
# Line: 74

def ListAvailableOps(self):
  """Returns a list of all available operations (sorted alphabetically)."""
  return tf_cluster.TF_ListAvailableOps()


# ==================================================
# Line: 81

def EstimatePerformance(self, device):
  return tf_cluster.TF_EstimatePerformance(device.SerializeToString())


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
# Line: 110

def _GetMetaGraph(self, batch_size=14, image_dim=12, optimizer_scope_name=''):
  """A simple layered graph with conv, an intermediate op, and a ReLU."""
  graph = ops.Graph()
  with graph.as_default():
    random_seed.set_random_seed(1)
    current_activation = variable_scope.get_variable(
        name='start', shape=[batch_size, image_dim, image_dim, 5])
    conv_filter = variable_scope.get_variable(
        name='filter', shape=[5, 5, 5, 5])
    for layer_number in range(10):
      with variable_scope.variable_scope('layer_{}'.format(layer_number)):
        after_conv = nn.conv2d(current_activation, conv_filter, [1, 1, 1, 1],
                               'SAME')
        current_activation = 2. * after_conv
        current_activation = nn.relu(current_activation)
    loss = math_ops.reduce_mean(current_activation)
    with ops.name_scope(optimizer_scope_name):
      optimizer = train.AdamOptimizer(0.001)
      train_op = optimizer.minimize(loss)
    init_op = variables.global_variables_initializer()
    metagraph = train.export_meta_graph()
  return (metagraph, init_op.name, train_op.name, loss.name)


# ==================================================
# Line: 220

def _GetMemoryOptimizerSessionConfig(self):
  rewrite_options = rewriter_config_pb2.RewriterConfig(
      disable_model_pruning=True,
      memory_optimization=rewriter_config_pb2.RewriterConfig.HEURISTICS)
  graph_options = config_pb2.GraphOptions(rewrite_options=rewrite_options)
  return config_pb2.ConfigProto(graph_options=graph_options)


# ==================================================
# Line: 259

def _annotated_graph(self):
  graph = ops.Graph()
  with graph.as_default():
    random_seed.set_random_seed(2)
    current_activation = variable_scope.get_variable(
        name='start', shape=[1, 2, 2, 5])
    conv_filter = variable_scope.get_variable(
        name='filter', shape=[5, 5, 5, 5])
    for layer_number in range(3):
      with variable_scope.variable_scope('layer_{}'.format(layer_number)):
        after_conv = nn.conv2d(current_activation, conv_filter, [1, 1, 1, 1],
                               'SAME')
        current_activation = 2. * after_conv
        current_activation.op._set_attr(
            '_recompute_hint',
            # The value of the attribute does not matter; just that the key
            # exists in the op's attributes.
            attr_value_pb2.AttrValue(i=1))
        current_activation += 5.
        current_activation.op._set_attr(
            '_recompute_hint', attr_value_pb2.AttrValue(i=0))
        current_activation = nn.relu(current_activation)
        current_activation.op._set_attr(
            '_recompute_hint', attr_value_pb2.AttrValue(i=1))
    loss = math_ops.reduce_mean(current_activation)
    optimizer = train.AdamOptimizer(0.001)
    train_op = optimizer.minimize(loss)
    init_op = variables.global_variables_initializer()
  return graph, init_op, train_op


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py
# Line: 232

def other_method(self, x):
  return x + 20


# ==================================================
# Line: 248

def other_method(self, x):
  return x + 20


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/conditional_expressions.py
# Line: 27

def visit_IfExp(self, node):
  template = '''
      ag__.if_exp(
          test,
          lambda: true_expr,
          lambda: false_expr,
          expr_repr)
  '''
  expr_repr = parser.unparse(node.test, include_encoding_marker=False).strip()
  return templates.replace_as_expression(
      template,
      test=node.test,
      true_expr=node.body,
      false_expr=node.orelse,
      expr_repr=gast.Constant(expr_repr, kind=None))



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/functions_test.py
# Line: 100

  def f(self, l):

    def inner_fn(i):
      return i + 1

    l += 1
    return l, inner_fn(l)

tr = self.transform(TestClass.f, (functions, return_statements))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/control_flow.py
# Line: 67

def _create_state_functions(
    self, block_vars, nonlocal_declarations, getter_name, setter_name):
  if not block_vars:
    template = """
      def getter_name():
        return ()
      def setter_name(block_vars):
        pass
    """
    return templates.replace(
        template, getter_name=getter_name, setter_name=setter_name)

  guarded_block_vars = []
  for v in block_vars:
    if v.is_simple():
      guarded_block_vars.append(v)
    else:
      guarded_block_vars.append(
          templates.replace_as_expression(
              'ag__.ldu(lambda: var_, name)',
              var_=v,
              name=gast.Constant(str(v), kind=None)))

  template = """
    def getter_name():
      return guarded_state_vars,
    def setter_name(vars_):
      nonlocal_declarations
      state_vars, = vars_
  """
  return templates.replace(
      template,
      nonlocal_declarations=nonlocal_declarations,
      getter_name=getter_name,
      guarded_state_vars=guarded_block_vars,
      setter_name=setter_name,
      state_vars=tuple(block_vars))


# ==================================================
# Line: 105

def _create_loop_options(self, node):
  if not anno.hasanno(node, anno.Basic.DIRECTIVES):
    return gast.Dict([], [])

  loop_directives = anno.getanno(node, anno.Basic.DIRECTIVES)
  if directives.set_loop_options not in loop_directives:
    return gast.Dict([], [])

  opts_dict = loop_directives[directives.set_loop_options]
  str_keys, values = zip(*opts_dict.items())
  keys = [gast.Constant(s, kind=None) for s in str_keys]
  values = list(values)  # ast and gast don't play well with tuples.
  return gast.Dict(keys, values)


# ==================================================
# Line: 119

def _create_undefined_assigns(self, undefined_symbols):
  assignments = []
  for s in undefined_symbols:
    template = '''
      var = ag__.Undefined(symbol_name)
    '''
    assignments += templates.replace(
        template,
        var=s,
        symbol_name=gast.Constant(s.ssf(), kind=None))
  return assignments


# ==================================================
# Line: 145

def _get_block_composite_vars(self, modified, live_in):
  # The scope variables corresponding to composite symbols (e.g. `self.x`).
  composite_scope_vars = []
  for s in modified:
    if not s.is_composite():
      continue
    # Mutations made to objects created inside the scope will appear as writes
    # to composite symbols. Because these mutations appear as modifications
    # made to composite symbols, we check whether the composite's parent is
    # actually live into the scope.
    # Example:
    #   while cond:
    #     x = Foo()
    #     x.foo = 2 * x.foo  # x.foo is live into the scope, but x is not.
    #
    # Note that some parents might not be symbols - for example, in x['foo'],
    # 'foo' is a parent, but it's a literal, not a symbol. We don't check the
    # liveness of literals.
    support_set_symbols = tuple(
        sss for sss in s.support_set if sss.is_symbol())
    if not all(sss in live_in for sss in support_set_symbols):
      continue
    composite_scope_vars.append(s)
  return frozenset(composite_scope_vars)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/slices.py
# Line: 32

def _process_single_assignment(self, target, value):
  if not isinstance(target, gast.Subscript):
    return None
  s = target.slice
  if isinstance(s, (gast.Tuple, gast.Slice)):
    return None

  template = """
    target = ag__.set_item(target, key, item)
  """
  return templates.replace(
      template, target=target.value, key=target.slice, item=value)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/variables.py
# Line: 51

def visit_Name(self, node):
  # Only the loads which existed in the original code are overloaded.
  if not anno.hasanno(node, anno.Static.ORIG_DEFINITIONS):
    return node
  if isinstance(node.ctx, gast.Load):
    node = templates.replace_as_expression('ag__.ld(var_)', var_=node)
  return node


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/break_statements.py
# Line: 48

def _guard_if_present(self, block, var_name):
  """Prevents the block from executing if var_name is set."""
  if not block:
    return block

  template = """
      if not var_name:
        block
    """
  node = templates.replace(
      template,
      var_name=var_name,
      block=block)
  return node


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/lists.py
# Line: 57

def _replace_append_call(self, node):
  assert len(node.args) == 1
  assert isinstance(node.func, gast.Attribute)
  template = """
    target = ag__.list_append(target, element)
  """
  return templates.replace(
      template,
      target=node.func.value,
      element=node.args[0])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/call_trees.py
# Line: 127

def _args_to_tuple(self, node):
  """Ties together all positional and *arg arguments in a single tuple."""
  # TODO(mdan): We could rewrite this to just a call to tuple(). Maybe better?
  # For example for
  #   f(a, b, *args)
  # instead of writing:
  #   (a, b) + args
  # just write this?
  #   tuple(a, b, *args)
  builder = _ArgTemplateBuilder()
  for a in node.args:
    if isinstance(a, gast.Starred):
      builder.add_stararg(a.value)
    else:
      builder.add_arg(a)
  builder.finalize()
  return builder.to_ast()


# ==================================================
# Line: 145

def _kwargs_to_dict(self, node):
  """Ties together all keyword and **kwarg arguments in a single dict."""
  if node.keywords:
    return gast.Call(
        gast.Name(
            'dict', ctx=gast.Load(), annotation=None, type_comment=None),
        args=(),
        keywords=node.keywords)
  else:
    return parser.parse_expression('None')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/directives.py
# Line: 89

def _process_symbol_directive(self, call_node, directive):
  if len(call_node.args) < 1:
    raise ValueError('"%s" requires a positional first argument'
                     ' as the target' % directive.__name__)
  target = call_node.args[0]
  defs = anno.getanno(target, anno.Static.ORIG_DEFINITIONS)
  for def_ in defs:
    def_.directives[directive] = _map_args(call_node, directive)
  return call_node


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
# Occurrences: Lines 57-60 (2 instances)

def _as_lambda(self, expr):
  return templates.replace_as_expression('lambda: expr', expr=expr)


# ==================================================
# Line: 67

def _as_binary_operation(self, op, arg1, arg2):
  template = templates.replace_as_expression(
      'arg1 is arg2',  # Note: `is` will be replaced with `op` below.
      arg1=arg1,
      arg2=arg2)
  template.ops[0] = op
  return template


# ==================================================
# Line: 75

def _as_unary_function(self, func_name, arg):
  return templates.replace_as_expression(
      'func_name(arg)', func_name=parser.parse_expression(func_name), arg=arg)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/utils/tensors_test.py
# Occurrences: Lines 28-35 (3 instances)

def _simple_tensor_array(self):
  return tensor_array_ops.TensorArray(dtypes.int32, size=3)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/utils/context_managers_test.py
# Line: 26

  def test_control_dependency_on_returns(self):
    # Just dry run them.
    with context_managers.control_dependency_on_returns(None):
      pass
    with context_managers.control_dependency_on_returns(
        constant_op.constant(1)):
      pass
    with context_managers.control_dependency_on_returns(
        tensor_array_ops.TensorArray(dtypes.int32, size=1)):
      pass
    with context_managers.control_dependency_on_returns(
        [constant_op.constant(1),
         constant_op.constant(2)]):
      pass


if __name__ == '__main__':

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/utils/tensor_list_test.py
# Line: 30

def _shape(self, shape_tuple):
  return constant(shape_tuple, dtypes.int32)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
# Line: 574

def _basic_loop(self, init_value, body_fn):
  def body(i):
    nonlocal s
    s = body_fn(i, s)

  def set_state(loop_vars):
    nonlocal s
    s, = loop_vars

  s = init_value
  control_flow.for_stmt(
      constant_op.constant([1, 2, 3, 4]),
      extra_test=lambda: True,
      body=body,
      get_state=lambda: (s,),
      set_state=set_state,
      symbol_names=('s',),
      opts={})
  return s


# ==================================================
# Line: 1000

def _basic_loop(self, init_value, body_fn):

  def body():
    nonlocal i, s
    s = body_fn(i, s)
    i += 1

  def set_state(loop_vars):
    nonlocal i, s
    i, s = loop_vars

  i = 0
  n = constant_op.constant(5)
  s = init_value
  control_flow.while_stmt(
      test=lambda: i < n,
      body=body,
      get_state=lambda: (i, s),
      set_state=set_state,
      symbol_names=('i', 's'),
      opts={})
  return s


# ==================================================
# Line: 1041

def _fixed_while_loop(self, cond_fn):
  def test_():
    return cond_fn(s)

  def body():
    nonlocal s
    s += 1

  def set_state(loop_vars):
    nonlocal s
    s, = loop_vars

  s = constant_op.constant(0)
  control_flow.while_stmt(
      test=test_,
      body=body,
      get_state=lambda: (s,),
      set_state=set_state,
      symbol_names=('s',),
      opts={})
  return s


# ==================================================
# Line: 1244

def _basic_cond(self, body_fn, else_fn):
  def body():
    nonlocal x
    x = body_fn()

  def orelse():
    nonlocal x
    x = else_fn()

  def set_state(cond_vars):
    nonlocal x
    x, = cond_vars

  x = 0
  control_flow.if_stmt(
      cond=constant_op.constant(True),
      body=body,
      orelse=orelse,
      get_state=lambda: (x,),
      set_state=set_state,
      symbol_names=('x',),
      nouts=1)
  return x


# ==================================================
# Line: 1289

def _fixed_cond(self, cond_val):
  def body():
    nonlocal x
    x = 1

  def orelse():
    nonlocal x
    x = -1

  def set_state(cond_vars):
    nonlocal x
    x, = cond_vars

  x = 0
  control_flow.if_stmt(
      cond=cond_val,
      body=body,
      orelse=orelse,
      get_state=lambda: (x,),
      set_state=set_state,
      symbol_names=('x',),
      nouts=1)
  return x


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/control_flow.py
# Line: 774

def _get_ops(self):
  return set(ops.get_default_graph().get_operations())


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/logical_test.py
# Occurrences: Lines 28-31 (2 instances)

def _tf_true(self):
  return constant_op.constant(True)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
# Line: 39

def overridden_method(self, x):
  return x + 20



# ==================================================
# Line: 414

def _basic_function_scope(self):
  return function_wrappers.FunctionScope(
      'test_function_name',
      'test_scope',  # Note: this must match the name in the `with` statement.
      converter.ConversionOptions())


# ==================================================
# Line: 543

  def test_method(self):
    with test_case_self._basic_function_scope() as test_scope:
      b = py_builtins.super_in_original_context(super, (), test_scope)
      return b.overridden_method(1)

tc = TestSubclass()

# ==================================================
# Line: 559

  def test_method(self, x):
    y = 7
    with test_case_self._basic_function_scope() as test_scope:
      z = 7
      return py_builtins.super_in_original_context(
          super, (), test_scope).overridden_method(x + y - z)

tc = TestSubclass()

# ==================================================
# Line: 577

  def test_method(self, x):
    with test_case_self._basic_function_scope() as test_scope:
      # Oddly, it's sufficient to use `self` in an inner function
      # to gain access to __class__ in this scope.
      # TODO(mdan): Is this true across implementations?
      # Note: normally, it's illegal to use super() in inner functions (it
      # throws an error), but the generated code may create them.
      def inner_fn():
        return py_builtins.super_in_original_context(
            super, (), test_scope).overridden_method(x)

      return inner_fn()

tc = TestSubclass()

# ==================================================
# Line: 601

  def test_method(self, x):
    with test_case_self._basic_function_scope() as test_scope:
      # Oddly, it's sufficient to use `self` in an inner function
      # to gain access to __class__ in this scope.
      # TODO(mdan): Is this true across implementations?
      # Note: normally, it's illegal to use super() in inner functions (it
      # throws an error), but the generated code may create them.
      l = lambda: py_builtins.super_in_original_context(  # pylint:disable=g-long-lambda
          super, (), test_scope).overridden_method(x)
      return l()

tc = TestSubclass()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
# Line: 284

def test_function_call_in_list(self):
  template = """
      foo(bar)
  """
  source = parser.parse_expression('[a(b(1))]')
  templates.replace_as_expression(template, bar=source)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
# Line: 258

def _node_sets_self_attribute(self, node):
  if anno.hasanno(node, anno.Basic.QN):
    qn = anno.getanno(node, anno.Basic.QN)
    # TODO(mdan): The 'self' argument is not guaranteed to be called 'self'.
    if qn.has_attr and qn.parent.qn == ('self',):
      return True
  return False


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
# Line: 46

def lamba_check(self, fn_ast_node):
  if isinstance(fn_ast_node, gast.Lambda):
    # Exception: lambda functions are assumed to be used only in the
    # place where they are defined, and not later.
    return True
  return False


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_fndefs_test.py
# Line: 31

def _parse_and_analyze(self, test_fn):
  # TODO(mdan): Use a custom FunctionTransformer here.
  node, source = parser.parse_entity(test_fn, future_features=())
  entity_info = transformer.EntityInfo(
      name=test_fn.__name__,
      source_code=source,
      source_file=None,
      future_features=(),
      namespace={})
  node = qual_names.resolve(node)
  namer = naming.Namer({})
  ctx = transformer.Context(entity_info, namer, None)
  node = activity.resolve(node, ctx)
  graphs = cfg.build(node)
  node = reaching_definitions.resolve(node, ctx, graphs)
  node = reaching_fndefs.resolve(node, ctx, graphs)
  return node


# ==================================================
# Line: 49

  def assertHasFnDefs(self, node):
    anno.getanno(node, anno.Static.DEFINED_FNS_IN)


if __name__ == '__main__':

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
# Line: 35

def _parse_and_analyze(self, test_fn):
  # TODO(mdan): Use a custom FunctionTransformer here.
  node, source = parser.parse_entity(test_fn, future_features=())
  entity_info = transformer.EntityInfo(
      name=test_fn.__name__,
      source_code=source,
      source_file=None,
      future_features=(),
      namespace={})
  node = qual_names.resolve(node)
  namer = naming.Namer({})
  ctx = transformer.Context(entity_info, namer, None)
  node = activity.resolve(node, ctx)
  graphs = cfg.build(node)
  node = reaching_fndefs.resolve(node, ctx, graphs)
  node = liveness.resolve(node, ctx, graphs)
  return node


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
# Line: 34

def _parse_and_analyze(self, test_fn):
  # TODO(mdan): Use a custom FunctionTransformer here.
  node, source = parser.parse_entity(test_fn, future_features=())
  entity_info = transformer.EntityInfo(
      name=test_fn.__name__,
      source_code=source,
      source_file=None,
      future_features=(),
      namespace={})
  node = qual_names.resolve(node)
  namer = naming.Namer({})
  ctx = transformer.Context(entity_info, namer, None)
  node = activity.resolve(node, ctx)
  graphs = cfg.build(node)
  node = reaching_definitions.resolve(node, ctx, graphs,
                                      reaching_definitions.Definition)
  return node


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
# Line: 125

def _parse_and_analyze(self, test_fn):
  # TODO(mdan): Use a custom FunctionTransformer here.
  node, source = parser.parse_entity(test_fn, future_features=())
  entity_info = transformer.EntityInfo(
      name=test_fn.__name__,
      source_code=source,
      source_file=None,
      future_features=(),
      namespace={})
  node = qual_names.resolve(node)
  namer = naming.Namer({})
  ctx = transformer.Context(entity_info, namer, None)
  node = activity.resolve(node, ctx)
  return node, entity_info


# ==================================================
# Line: 856

def e(self):
  f = c + 1
  return f

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
# Line: 382

def _resolve_typed_callable(self, f_types, arg_types, keyword_types):
  ret_types = set()
  for t in f_types:

    if isinstance(t, Callable):
      # Note: these are undocumented - may be version-specific!
      # Callable[[x], y]: __args__ are (x, y)
      args = t.__args__
      if args:
        ret_types.add(args[-1])
      else:
        ret_types.add(Any)
    else:
      raise NotImplementedError('callable type {}'.format(type(t)))

  # Side effects can not be inferred based on type alone.
  side_effects = None
  return ret_types, side_effects


# ==================================================
# Occurrences: Lines 540-543 (2 instances)

def init_state(self, _):
  return _TypeMap()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_fndefs.py
# Line: 81

def init_state(self, _):
  return _NodeState()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
# Line: 164

def is_wildcard(self, p):
  if isinstance(p, (list, tuple)) and len(p) == 1:
    p, = p
  if isinstance(p, gast.Name) and p.id == '_':
    return True
  if p == '_':
    return True
  return False


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
# Line: 247

def get_transformed_name(self, node):
  """Returns a name for the output function. Subclasses may override this."""
  if isinstance(node, gast.Lambda):
    return 'lam'
  elif isinstance(node, gast.FunctionDef):
    return node.name
  raise ValueError('Unknown node type {}'.format(node))


# ==================================================
# Line: 286

def _erase_arg_defaults(self, node):
  """Erase arg default expressions, which would otherwise be unbound."""
  args = node.args
  for i in range(len(args.defaults)):
    args.defaults[i] = parser.parse_expression('None')
  for i, d in enumerate(args.kw_defaults):
    if d is not None:
      args.kw_defaults[i] = parser.parse_expression('None')
  return node


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
# Line: 29

def _simple_context(self):
  entity_info = transformer.EntityInfo(
      name='Test_fn',
      source_code=None,
      source_file=None,
      future_features=(),
      namespace=None)
  return transformer.Context(entity_info, None, None)


# ==================================================
# Line: 155

def _process_body_item(self, node):
  if isinstance(node, gast.Assign) and (node.value.id == 'y'):
    if_node = gast.If(
        gast.Name(
            'x', ctx=gast.Load(), annotation=None, type_comment=None),
        [node], [])
    return if_node, if_node.body
  return node, None


# ==================================================
# Line: 227

def visit_If(self, node):
  node.body = NotANode()
  raise ValueError('I blew up')


# ==================================================
# Line: 250

  def visit_If(self, node):
    return gast.Pass()

tr = TestTransformer(self._simple_context())


# ==================================================
# Line: 274

  def visit_If(self, node):
    return node.body

tr = TestTransformer(self._simple_context())


# ==================================================
# Line: 301

def _simple_context(self):
  entity_info = transformer.EntityInfo(
      name='test_fn',
      source_code=None,
      source_file=None,
      future_features=(),
      namespace=None)
  return transformer.Context(entity_info, None, None)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py
# Line: 54

def _create_source_map(self, test_fn):
  node, source = parser.parse_entity(test_fn, ())
  origin_info.resolve_entity(node, source, test_fn)
  # Creating a source map with the source code as output will create
  # an identity map.
  return origin_info.create_source_map(node, source, 'test_filename')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/parser_test.py
# Line: 244

def _eval_code(self, code, name):
  globs = {}
  exec(code, globs)  # pylint:disable=exec-used
  return globs[name]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/cfg.py
# Line: 206

def can_ignore(self, node):
  """Returns True if the node can safely be assumed not to touch variables."""
  ast_node = node.ast_node
  if anno.hasanno(ast_node, anno.Basic.SKIP_PROCESSING):
    return True
  return isinstance(ast_node,
                    (gast.Break, gast.Continue, gast.Raise, gast.Pass))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/transformer.py
# Line: 266

def debug_print(self, node):
  """Helper method useful for debugging. Prints the AST."""
  if __debug__:
    print(pretty_printer.fmt(node))
  return node


# ==================================================
# Line: 272

def debug_print_src(self, node):
  """Helper method useful for debugging. Prints the AST as code."""
  if __debug__:
    print(parser.unparse(node))
  return node


# ==================================================
# Line: 363

def create_assignment(self, target, expression):
  template = """
    target = expression
  """
  return templates.replace(template, target=target, expression=expression)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/loader_test.py
# Line: 115

  def test_cleanup(self):
    test_source = textwrap.dedent('')
    _, filename = loader.load_source(test_source, delete_on_exit=True)
    # Clean up the file before loader.py tries to remove it, to check that the
    # latter can deal with that situation.
    os.unlink(filename)

if __name__ == '__main__':

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
# Line: 144

def _match(self, pattern, parent, field, child):
  if pattern is ANY:
    return True
  else:
    return pattern.matches(parent, field, child)


# ==================================================
# Line: 394

def visit_ListComp(self, node):
  msg = ('ListComp nodes not supported '
         '(need to convert to a form that tolerates '
         'assignment statements in clause bodies).')
  raise ValueError(msg)


# ==================================================
# Line: 400

def visit_SetComp(self, node):
  msg = ('SetComp nodes not supported '
         '(need to convert to a form that tolerates '
         'assignment statements in clause bodies).')
  raise ValueError(msg)


# ==================================================
# Line: 406

def visit_DictComp(self, node):
  msg = ('DictComp nodes not supported '
         '(need to convert to a form that tolerates '
         'assignment statements in clause bodies).')
  raise ValueError(msg)


# ==================================================
# Line: 412

def visit_GeneratorExp(self, node):
  msg = ('GeneratorExp nodes not supported '
         '(need to convert to a form that tolerates '
         'assignment statements in clause bodies).')
  raise ValueError(msg)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
# Line: 47

def _simple_context(self):
  entity_info = transformer.EntityInfo(
      name='test_fn',
      source_code=None,
      source_file=None,
      future_features=(),
      namespace=None)
  return transformer.Context(entity_info, None, None)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
# Line: 228

  def global_var_for_test_namespace_collisions(self):
    return global_var_for_test_namespace_collisions

tr = TestTranspiler()

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
# Line: 40

def _build_cfg(self, fn):
  node, _ = parser.parse_entity(fn, future_features=())
  cfgs = cfg.build(node)
  return cfgs, node


# ==================================================
# Occurrences: Lines 91-99 (3 instances)

def _build_cfg(self, fn):
  node, _ = parser.parse_entity(fn, future_features=())
  cfgs = cfg.build(node)
  return cfgs


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/impl/api_test.py
# Line: 102

def plus_three(self, x):
  return x + 3


# ==================================================
# Line: 139

def called_member(self, a):
  if a < 0:
    a = -a
  return a


# ==================================================
# Line: 161

def called_member(self, a):
  return math_ops.negative(a)


# ==================================================
# Line: 182

def called_member(self, a):
  return math_ops.negative(a)


# ==================================================
# Line: 203

def called_member(self, a):
  if a < 0:
    a = -a
  return a


# ==================================================
# Line: 224

def test_method(self, a):
  if a < 0:
    a = -a
  return a


# ==================================================
# Line: 240

def test_method(self, x, y):
  z = x + y
  return z


# ==================================================
# Line: 268

def called_member(self, a):
  if a < 0:
    a = -a
  return a


# ==================================================
# Line: 504

def test_converted_call_callable_abc(self):

  test_self = self

  class TestBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __call__(self):
      test_self.fail('This should not be called')

  class TestSubclass(TestBase):

    def __init__(self):
      test_self.assertFalse(converter_testing.is_inside_generated_code())

    def __call__(self, expected):
      test_self.assertTrue(expected)
      test_self.assertTrue(converter_testing.is_inside_generated_code())

  tc = api.converted_call(TestSubclass, (), None, options=DEFAULT_RECURSIVE)
  api.converted_call(tc, (True,), None, options=DEFAULT_RECURSIVE)


# ==================================================
# Line: 651

def method(self):
  return converter_testing.is_inside_generated_code()


# ==================================================
# Line: 664

def method(self):
  return converter_testing.is_inside_generated_code()


# ==================================================
# Line: 781

def method(self):
  return 1


# ==================================================
# Line: 804

def __array__(self):
  raise ValueError('fault')


# ==================================================
# Line: 1144

def method(self):
  return converter_testing.is_inside_generated_code()


# ==================================================
# Line: 1199

def method(self):
  return converter_testing.is_inside_generated_code()


# ==================================================
# Line: 1217

def plus_three(self, x):
  return x + 3


# ==================================================
# Line: 1239

def plus_three(self, x):
  return x + 3


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/impl/api.py
# Occurrences: Lines 219-222 (2 instances)

def get_caching_key(self, ctx):
  return ctx.options


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/impl/conversion_test.py
# Line: 34

def _simple_program_ctx(self):
  return converter.ProgramContext(
      options=converter.ConversionOptions(recursive=True),
      autograph_module=api)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/core/converter.py
# Line: 257

def get_definition_directive(self, node, directive, arg, default):
  """Returns the unique directive argument for a symbol.

  See lang/directives.py for details on directives.

  Example:
     # Given a directive in the code:
     ag.foo_directive(bar, baz=1)

     # One can write for an AST node Name(id='bar'):
     get_definition_directive(node, ag.foo_directive, 'baz')

  Args:
    node: ast.AST, the node representing the symbol for which the directive
      argument is needed.
    directive: Callable[..., Any], the directive to search.
    arg: str, the directive argument to return.
    default: Any

  Raises:
    ValueError: if conflicting annotations have been found
  """
  defs = anno.getanno(node, anno.Static.ORIG_DEFINITIONS, ())
  if not defs:
    return default

  arg_values_found = []
  for def_ in defs:
    if (directive in def_.directives and arg in def_.directives[directive]):
      arg_values_found.append(def_.directives[directive][arg])

  if not arg_values_found:
    return default

  if len(arg_values_found) == 1:
    return arg_values_found[0]

  # If multiple annotations reach the symbol, they must all match. If they do,
  # return any of them.
  first_value = arg_values_found[0]
  for other_value in arg_values_found[1:]:
    if not ast_util.matches(first_value, other_value):
      qn = anno.getanno(node, anno.Basic.QN)
      raise ValueError(
          '%s has ambiguous annotations for %s(%s): %s, %s' %
          (qn, directive.__name__, arg, parser.unparse(other_value).strip(),
           parser.unparse(first_value).strip()))
  return first_value


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/core/function_wrappers.py
# Line: 63

def _sanitize(self, name):
  """See https://www.tensorflow.org/api_docs/python/tf/Graph#name_scope."""
  # TensorFlow doesn't like leading underscores at the top level.
  if name and name.startswith('_'):
    name = 'fn' + name
  return name


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/core/converter_testing.py
# Line: 114

def transform(
    self, f, converter_module, include_ast=False, ag_overrides=None):
  program_ctx = converter.ProgramContext(
      options=converter.ConversionOptions(recursive=True),
      autograph_module=api)

  tr = TestingTranspiler(converter_module, ag_overrides)
  transformed, _, _ = tr.transform_function(f, program_ctx)

  if include_ast:
    return transformed, tr.transformed_ast, tr.transform_ctx

  return transformed

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/core/unsupported_features_checker.py
# Occurrences: Lines 49-52 (2 instances)

def visit_Yield(self, node):
  raise errors.UnsupportedLanguageElementError('generators are not supported')


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
# Line: 273

def __tf_tracing_type__(self, _):
  return 1


# ==================================================
# Occurrences: Lines 443-465 (6 instances)

def testGeneric(self):
  trace_type.from_value(1)
  trace_type.from_value(DummyGenericClass())


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
# Line: 214

def experimental_as_proto(self):
  return serialization_test_pb2.MyCustomRepresentation()


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
# Line: 230

def f(self):
  return x


# ==================================================
# Line: 248

def g(self):
  return [x]


# ==================================================
# Line: 321

def baz_str(self):
  return "Baz"


# ==================================================
# Line: 329

def bar_str(self):
  return x + "Bar"


# ==================================================
# Line: 370

def g(self):
  return x


# ==================================================
# Line: 393

def g(self):
  return glob


# ==================================================
# Line: 466

def test_decorated_method_w_self_no_exception(self):
  """Test this pattern does not raise any exceptions."""

  def dummy_tf_function(func):

    func_map = free_vars_detect._detect_function_free_vars(func)
    self.assertLen(func_map, 1)
    self.assertIn("foo", func_map.keys())
    free_vars = get_var_name(func_map["foo"])
    self.assertSequenceEqual(free_vars, ["dummy_tf_function"])

    def wrapper(*args, **kwargs):
      return func(*args, **kwargs)

    return wrapper

  glob = 1

  # This pattern is not fully supported yet in the sense that `self.bar()` is
  # not inspected so `glob` cannot be detected.
  # The reason is the neither `self` nor `self.bar` is accessible from the
  # perspective of dummy_tf_function decorator.
  # One possible solution is parsing the source code of the whole module,
  # instead of single function. And probably get the source of `self.bar`
  # from the AST of the module where `Foo` is defined. One potentail challenge
  # of this approach is how to locate the decorated function in the AST.
  class Foo():

    @dummy_tf_function
    def foo(self):
      return self.bar()

    def bar(self):
      return glob

  _ = Foo()


# ==================================================
# Line: 498

def bar(self):
  return glob


# ==================================================
# Line: 539

def test_global_var_from_arg_func(self):
  x = 1

  def g():
    return x + 1

  def f(h):
    return h()

  _ = f(g)



# ==================================================
# Line: 567

def bar(self):
  return x


# ==================================================
# Line: 625

def g(self):
  return [x]


# ==================================================
# Line: 657

def g(self):
  return [x]


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/capture/capture_container_test.py
# Line: 27

def _prepare_dict(self):
  d = {"a": 1, "b": 2, "c": 3}
  mutation_d = capture_container.MutationAwareDict(copy.copy(d))
  return d, mutation_d


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/runtime_client/runtime_client_test.py
# Line: 35

def test_create_nullary(self):
  fndef = text_format.Parse(
      """
          signature {
             name: 'NullaryFunction'
             output_arg { name: 'o' type: DT_INT32 }
           }
           node_def {
             name: 'retval'
             op: 'Const'
             attr {
               key: 'dtype'
               value { type: DT_INT32 }
             }
             attr {
               key: 'value'
               value {
                 tensor {
                   dtype: DT_INT32
                   tensor_shape {}
                   int_val: 1
                 }
               }
             }
           }
           ret { key: 'o' value: 'retval:output' }
       """,
      function_pb2.FunctionDef(),
  )

  ctx = runtime_client.GlobalEagerContext()
  rt = runtime_client.Runtime(ctx)
  rt.CreateFunction(fndef)


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/transform/transform_test.py
# Line: 51

def f(self, x, y, add_2):
  r = math_ops.add(x, y, name="x_plus_y")
  if add_2:
    return r + 2
  else:
    return r



# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
# Line: 38

def most_specific_common_supertype(self, others):
  return None


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
# Line: 582

def is_subtype_of(self, other: trace.TraceType) -> bool:
  return False


# ==================================================
# Occurrences: Lines 601-604 (2 instances)

def is_subtype_of(self, other) -> bool:
  return True


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/platform/ram_file_system_test.py
# Line: 33

def test_create_and_delete_directory(self):
  file_io.create_dir_v2('ram://testdirectory')
  file_io.delete_recursively_v2('ram://testdirectory')


# ==================================================
# Line: 110

def foo(self):
  return constant_op.constant([1])


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/tfrt/saved_model/python/saved_model_load_and_run_test.py
# Line: 26

  def test_give_me_a_name(self):
    with context.eager_mode(), ops.device("CPU"):
      inputs = [
          constant_op.constant([0, 1, 2, 3, 4, 5, 6, 7]),
          constant_op.constant([1, 5, 8, 9, 21, 54, 67]),
          constant_op.constant([90, 81, 32, 13, 24, 55, 46, 67]),
      ]
    cpp_tensor = _pywrap_saved_model.RunConvertor(inputs)
    return cpp_tensor


if __name__ == "__main__":

# ==================================================
