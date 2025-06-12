# string-concat-loop snippets for tensorflow

# File: /root/ecooptimizer/tensorflow/tensorflow/lite/toco/logging/gen_html.py
# Occurrences: Lines 66-70 (4 instances)

for i in range(len(lst)):
  if i % 2 == 0:
    out_str += "shape:"
  else:
    out_str += "type:"
  out_str += lst[i]
  out_str += ","

# ==================================================
# Occurrences: Lines 165-178 (4 instances)

for i in range(len(toco_conversion_log_before.op_list)):
  # Append operator name column.
  pre_op_profile += "<tr><td>" + toco_conversion_log_before.op_list[
      i] + "</td>"
  # Append input type column.
  if i < len(toco_conversion_log_before.op_signatures):
    pre_op_profile += "<td>" + get_input_type_from_signature(
        toco_conversion_log_before.op_signatures[i]) + "</td></tr>"
  else:
    pre_op_profile += "<td></td></tr>"


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/lite/python/tflite_convert.py
# Occurrences: Lines 318-324 (5 instances)

for flag in unparsed:
  output += _get_message_unparsed(flag, "--input_file", "--graph_def_file")
  output += _get_message_unparsed(flag, "--savedmodel_directory",
                                  "--saved_model_dir")
  output += _get_message_unparsed(flag, "--std_value", "--std_dev_values")
  output += _get_message_unparsed(flag, "--batch_size", "--input_shapes")
  output += _get_message_unparsed(flag, "--dump_graphviz",
                                  "--dump_graphviz_dir")

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/gen_quantized_function_library.py
# Occurrences: Lines 55-57 (2 instances)

for arg_value in arg_values:
  arg_dict = {arg_name: arg_value}
  replacement_text += '\\n'
  replacement_text += _substitute_parameterization_template(
      loop_template.safe_substitute(arg_dict))

# ==================================================
# Occurrences: Lines 88-89 (2 instances)

for key, value in value_dict.items():
  # Replace single quote to double quote since single quote around a
  # string are not valid in the MLIR representation.
  value_dict[key] = str(value).replace("'", '"')

# ==================================================
# Line: 147

for quantized_op in quantized_ops[2:]:
  function_name += '_and_{}'.format(
      _format_snake_case_op_name(quantized_op))


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/framework/test_util.py
# Line: 3743

while op is not None:
  err_str += "\nCaused by: " + op.name
  op = op._original_op  # pylint: disable=protected-access

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
# Line: 384

for out_tensor in op.outputs:
  if out_tensor.name not in graph_order.tensor_to_idx:
    raise ValueError(
        'out_tensor is not in tensor_to_idx. out_tensor={}, '
        'tensor_to_idx={}'
        .format(out_tensor.name, graph_order.tensor_to_idx))
  line += ' %d'%graph_order.tensor_to_idx[out_tensor.name]

# ==================================================
# Line: 407

for consumer_op in consumers:
  if consumer_op.name not in graph_order.op_to_idx:
    raise ValueError(
        'consumer_op is not in op_to_idx.  '
        'got consumer_op={}, op_to_idx={}'
        .format(consumer_op.name, graph_order.op_to_idx))
  line += ' %d'%graph_order.op_to_idx[consumer_op.name]

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tensor_tracer.py
# Line: 220

for key, value in tensor_tracer_params.items():
  enable_flags += ' --%s=%s' % (key, value)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/image_ops_test.py
# Occurrences: Lines 1162-1166 (2 instances)

for seed in seeds_list:
  y_tf = func(x_tf, seed=seed)
  y_tf_eval = self.evaluate(y_tf)
  if y_tf_eval[0][0] == 1:
    self.assertAllEqual(y_tf_eval, x_np)
    count_unflipped += 1
    flip_seq += "U"
  else:
    self.assertAllEqual(y_tf_eval, y_np)
    count_flipped += 1
    flip_seq += "F"


# ==================================================
# Occurrences: Lines 1219-1223 (2 instances)

for j in range(batch_size):
  if y_tf_eval[j][0][0] == 1:
    self.assertAllEqual(y_tf_eval[j], x_np[j])
    count_unflipped += 1
    flip_seq += "U"
  else:
    self.assertAllEqual(y_tf_eval[j], y_np[j])
    count_flipped += 1
    flip_seq += "F"


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
# Line: 224

for operator in operators[1:]:
  name += "_x_" + operator.name

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/cond_v2.py
# Line: 1297

for branch_graph in branch_graphs:
  branch_graph.name += "_rewritten"


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
# Line: 155

for num, bin_start, bin_end in zip(hist, bin_edges, bin_edges[1:]):
  bar = "#" * int(MAX_WIDTH * float(num) / float(max_num_elems))
  ret += ("({:<{max_start_bin_width}}, {:<{max_end_bin_width}}) | {:10} | "
          "{:}\n").format(
      bin_start,
      bin_end,
      num,
      bar,
      max_start_bin_width=max_start_bin_width,
      max_end_bin_width=max_end_bin_width,
  )

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/client/virtual_gpu_test.py
# Line: 116

for j in range(min(10, dim)):
  row += ' ' + str(mat[i][j])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/sharding/sharding_util.py
# Occurrences: Lines 281-283 (3 instances)

for ckpt_key, slice_spec in unseen_tensor_dict.items():
  tensors_info += "  tensor:\n"
  tensors_info += f"    checkpoint_key: {ckpt_key}\n"
  tensors_info += f"    slice_spec: {slice_spec}\n"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/cli_shared.py
# Line: 423

for key in feed_dict:
  description += "1 feed (%s)" % (
      key
      if isinstance(key, str) or not hasattr(key, "name") else key.name)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
# Line: 568

for width, row in zip(column_widths, device_total_row):
  row_str += ("{:<%d}" % width).format(row)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
# Occurrences: Lines 1424-1428 (3 instances)

for k in range(depth):
  if k < depth - 1:
    if k + 1 in unfinished:
      hang += HANG_UNFINISHED
    else:
      hang += HANG_FINISHED
  else:
    hang += HANG_SUFFIX


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/debug/lib/check_numerics_callback.py
# Line: 186

for slot, input_tensor in enumerate(inputs):
  message += "         %d: %s\n" % (
      slot, _maybe_lookup_original_input_tensor(graph, input_tensor))

# ==================================================
# Occurrences: Lines 208-212 (2 instances)

for filepath, lineno, function_name, source_line in traceback[
    -stack_height_limit:]:
  user_code_indicator = "    "
  if not source_utils.guess_is_tensorflow_py_library(filepath):
    user_code_indicator = " -> "

  message += "    + %s (L%d) %s\n" % (
      limit_string_length(filepath, path_length_limit), lineno,
      function_name)
  if source_line is not None:
    message += "%s|   %s\n" % (user_code_indicator, source_line)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/function_type_utils.py
# Line: 336

for name, value in self.default_values.items():
  summary += f"\n  {name}: {value!r}"

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/generic_utils.py
# Occurrences: Lines 945-953 (4 instances)

for k in self._values_order:
  info += ' - %s:' % k
  if isinstance(self._values[k], list):
    avg = np.mean(self._values[k][0] / max(1, self._values[k][1]))
    if abs(avg) > 1e-3:
      info += ' %.4f' % avg
    else:
      info += ' %.4e' % avg
  else:
    info += ' %s' % self._values[k]


# ==================================================
# Occurrences: Lines 971-976 (3 instances)

for k in self._values_order:
  info += ' - %s:' % k
  avg = np.mean(self._values[k][0] / max(1, self._values[k][1]))
  if avg > 1e-3:
    info += ' %.4f' % avg
  else:
    info += ' %.4e' % avg

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/utils/layer_utils.py
# Occurrences: Lines 178-180 (2 instances)

for i in range(len(fields)):
  if i > 0:
    line = line[:-1] + ' '
  line += str(fields[i])
  line = line[:positions[i]]
  line += ' ' * (positions[i] - len(line))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/mixed_precision/device_compatibility_check.py
# Line: 103

for device_str in _dedup_strings(supported_device_strs +
                                 unsupported_device_strs):
  warning_str += '  ' + device_str + '\n'

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# Line: 1660

for label, single_data in zip(["x", "y", "sample_weight"], data):
  msg += "  {} sizes: {}\n".format(
      label, ", ".join(str(i.shape[0]) for i in nest.flatten(single_data)))

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/grappler/cost_analyzer.py
# Line: 78

for tensor in live_tensors:
  op_name = tensor[0]
  output_id = tensor[1]
  mem_used = tensor[2]
  report += "  " + str(op_name) + ":" + str(output_id) + " uses " + str(
      mem_used) + " bytes\n"


# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
# Line: 150

for n, rn in zip(nodes, reparsed_nodes):
  nodes_str = pretty_printer.fmt(n, color=False, noanno=True)
  reparsed_nodes_str = pretty_printer.fmt(rn, color=False, noanno=True)
  diff = difflib.context_diff(
      nodes_str.split('\n'),
      reparsed_nodes_str.split('\n'),
      fromfile='Original nodes',
      tofile='Reparsed nodes',
      n=7)
  diff = '\n'.join(diff)
  new_msg += diff + '\n'

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/cfg.py
# Occurrences: Lines 131-134 (2 instances)

for node in self.index.values():
  result += '  %s [label="%s"];\n' % (id(node), node)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
# Line: 192

for i in range(0, len(self.qn) - 1):
  if self.has_subscript():
    delimiter = '_sub_'
  else:
    delimiter = '_'
  ssf_string += ssfs[i] + delimiter

# ==================================================
