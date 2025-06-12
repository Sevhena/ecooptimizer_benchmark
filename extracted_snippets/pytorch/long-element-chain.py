# long-element-chain snippets for pytorch

# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train_regression.py
# Line: 430

value = tree_.value[node][0][0]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/gradcheck.py
# Occurrences: Lines 595-597 (2 instances)

jacobians[i][index_o][lin_idx].zero_()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/comm_analysis.py
# Occurrences: Lines 245-246 (2 instances)

intraLat = hwLat[intraHw][nccl_algo][nccl_proto]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codecache.py
# Line: 326

timings[choice] = cache[op][inputs][precision][choice_hash]

# ==================================================
# Line: 353

local_cache[op][inputs][precision][choice.hash_key()] = timing

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/split_cat.py
# Line: 1802

) or getitem_idx != parent_to_indices[current_getitem_parent][-1][-1] + 1:

# ==================================================
# Occurrences: Lines 1837-1838 (2 instances)

cat_inputs_list.index(parent_to_getitems[parent][idx][0]),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/_memory_viz.py
# Line: 76

real_size = b["history"][0]["real_size"]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/_dynamism.py
# Line: 94

tracking[key_path][0][i].add(dim)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_numpy/_dtypes_impl.py
# Line: 56

return _cd._can_cast_dict[casting][from_torch_dtype][to_torch_dtype]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/output_graph.py
# Line: 2518

rv.node.meta["nn_module_stack"][target][1],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_tools/ilp_utils.py
# Occurrences: Lines 149-170 (7 instances)

"grad_total": mod_mem_stat.snapshots[_ModState.PRE_BW][-1][dev][
    _MemRefType.GRAD
],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_tools/sac_ilp.py
# Occurrences: Lines 182-183 (2 instances)

slope = graph.nodes[i]["slopes"][s]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_tools/mem_tracker.py
# Line: 514

mod_stats.snapshots[peak_state][-1][dev] = deepcopy(

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/debug/_comm_mode.py
# Line: 155

self.module_helper_dict[self.name]["parameters"][param_name] = str(

# ==================================================
# Line: 710

self.comm_module_counts[self.advanced_module_tracker.name][key][
    func_packet
] += 1

# ==================================================
# Line: 724

self.comm_module_counts[par][key][func_packet] += 1

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/_numeric_suite.py
# Occurrences: Lines 114-118 (2 instances)

quantized_dict[key].__getstate__()[0][4][0].__getstate__()[0][0]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/_numeric_suite_fx.py
# Line: 324

results[ref_name][res_type][model_name] = [extracted_weight]

# ==================================================
# Line: 605

results[key][mod.results_type][mod.model_name] = []

# ==================================================
# Occurrences: Lines 627-629 (2 instances)

results[key][mod.results_type][mod.model_name].append(data)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/fx/weight_utils.py
# Occurrences: Lines 46-47 (2 instances)

res.append(weight_value.param.__getstate__()[0][4][0].__getstate__()[0][0])

# ==================================================
# Occurrences: Lines 83-86 (2 instances)

weight_value.param.__getstate__()[0][4][0].__getstate__()[0][0]  # type: ignore[index]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/fx/n_shadows_utils.py
# Occurrences: Lines 1135-1138 (2 instances)

results["model"][NSSingleResultValuesType.WEIGHT.value][name_fp32] = [

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/activation_sparsifier/activation_sparsifier.py
# Line: 175

self.state[name]["mask"][feature_idx] = torch.ones_like(

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_equalize.py
# Occurrences: Lines 921-922 (2 instances)

layer = activation_comparison_dict[key]["node_output"]["int8"][0]["fqn"]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_model_report/model_report_visualizer.py
# Line: 276

feature_val = filtered_data[module_fqn][feature][channel]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/partitioners.py
# Line: 1919

weight = nx_graph[edge.get_source()][edge.get_destination()]["capacity"]

# ==================================================
