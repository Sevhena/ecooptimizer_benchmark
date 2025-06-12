# cached-repeated-calls snippets for pytorch

# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/mixed_mm/gen_data_mixed_mm.py
# Occurrences: Lines 117-118 (4 instances)

k = self.get_random_dim()

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train_decision.py
# Line: 393

count = len(group)

# ==================================================
# Line: 436

assert len(group) >= 2, "Need at least 2 choices"

# ==================================================
# Occurrences: Lines 449-450 (2 instances)

assert len(unique_choices) == len(group), (

# ==================================================
# Occurrences: Lines 850-855 (2 instances)

num_wrong = len(wrong_probas)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/mm/gen_data_mm.py
# Occurrences: Lines 107-109 (6 instances)

m = self.get_random_dim()

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/pad_mm/gen_data_pad_mm.py
# Occurrences: Lines 38-39 (2 instances)

prepadded_left = self.prepadded()

# ==================================================
# Occurrences: Lines 122-128 (12 instances)

m = random.randint(1, 65536)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen.py
# Line: 535

return generate_static_dispatch_fallback_call(sig, f, backend_indices)

# ==================================================
# Line: 565

fallback = generate_static_dispatch_fallback_call(sig, f, backend_indices)

# ==================================================
# Occurrences: Lines 1576-1577 (2 instances)

ns_definitions: dict[str, list[str]] = defaultdict(list)

# ==================================================
# Line: 1622

registrations[kernel_namespace] = defaultdict(list)

# ==================================================
# Line: 1934

grouped_functions = grouped_functions_by_root_name.get(name, [])

# ==================================================
# Line: 1995

grouped_functions = grouped_functions_by_root_name.get(name, [])

# ==================================================
# Occurrences: Lines 2278-2278 (2 instances)

return sorted(set(headers))

# ==================================================
# Occurrences: Lines 2473-2473 (2 instances)

return "\n".join(sorted(set(headers)))

# ==================================================
# Occurrences: Lines 2974-2981 (4 instances)

cpu_fm = make_file_manager(options=options)

# ==================================================
# Occurrences: Lines 3019-3023 (2 instances)

backend_indices[DispatchKey.parse(key)]

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/api/translate.py
# Occurrences: Lines 282-282 (2 instances)

options = direct_solve(options_ctype)

# ==================================================
# Occurrences: Lines 303-332 (16 instances)

options = direct_solve(options_ctype)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/api/structured.py
# Line: 70

elem = argumenttype_type(t.elem, mutable=mutable, binds=binds)

# ==================================================
# Line: 84

elem = argumenttype_type(t.elem, mutable=mutable, binds=binds)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/api/cpp.py
# Line: 180

elem = argumenttype_type(t.elem, mutable=mutable, binds=binds, symint=symint)

# ==================================================
# Line: 213

elem = argumenttype_type(t.elem, mutable=mutable, binds=binds, symint=symint)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/api/lazy.py
# Line: 225

self.is_optional = isinstance(arg.type, OptionalType)

# ==================================================
# Line: 231

or (isinstance(arg.type, OptionalType) and isSymIntType(arg.type.elem))

# ==================================================
# Occurrences: Lines 357-360 (2 instances)

elif getattr(func.arguments, arg_field) is not None:

# ==================================================
# Line: 371

curr_args = getattr(func.arguments, arg_field)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/api/python.py
# Line: 707

elem = argument_type_str(t.elem, simple_type=simple_type, symint=symint)

# ==================================================
# Line: 734

elem = argument_type_str(t.elem, simple_type=simple_type, symint=symint)

# ==================================================
# Occurrences: Lines 988-991 (2 instances)

elem = argument_type_str_pyi(t.elem)

# ==================================================
# Line: 1008

inner = return_type_str_pyi(t.elem)

# ==================================================
# Line: 1020

inner = return_type_str_pyi(t.elem)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/static_runtime/generator.py
# Line: 262

maybe_method = ivalue_type_conversion_method(arg.type)

# ==================================================
# Line: 279

maybe_method = ivalue_type_conversion_method(arg.type)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_aoti_c_shim.py
# Line: 116

c_types, names, aten_types, callsite_exprs = convert_arg_type_and_name(
    typ.elem, name
)

# ==================================================
# Line: 159

c_types, names, aten_types, _ = convert_arg_type_and_name(typ.elem, name)

# ==================================================
# Occurrences: Lines 478-485 (2 instances)

declaration, _ = gen_declaration_and_definition(
    schema, device, backend_call, version_info
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/dest/register_dispatch_key.py
# Line: 330

name = sig.name()

# ==================================================
# Line: 357

wrapper_name = sig.name()

# ==================================================
# Occurrences: Lines 434-436 (2 instances)

name = sig.name()

# ==================================================
# Occurrences: Lines 455-455 (2 instances)

return {sig.name()}({", ".join(e.expr for e in translate(cpp_sig.arguments(), sig.arguments()))});

# ==================================================
# Line: 495

sig.arguments(), kernel_sig.arguments(), method=False

# ==================================================
# Line: 777

and f.func.kind() is SchemaKind.out

# ==================================================
# Line: 822

k = f.func.kind()

# ==================================================
# Line: 863

out_args_str = ", ".join(a.name for a in f.func.arguments.out)

# ==================================================
# Line: 987

refs = ", ".join(a.name for a in f.func.arguments.out)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/dest/lazy_ir.py
# Occurrences: Lines 250-253 (2 instances)

reuse_ctor_args = ", ".join(ctor_args)

# ==================================================
# File: /root/ecooptimizer/pytorch/setup.py
# Occurrences: Lines 423-427 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 565-570 (4 instances)

lib_name = otool_cmds[idx + 2].strip()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_fuser.py
# Occurrences: Lines 40-41 (2 instances)

old_profiling_executor = torch._C._jit_set_profiling_executor(True)

# ==================================================
# Occurrences: Lines 54-55 (2 instances)

old_profiling_executor = torch._C._jit_set_profiling_executor(True)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_script.py
# Occurrences: Lines 308-310 (4 instances)

num_methods = len(cls._methods)

# ==================================================
# Occurrences: Lines 1019-1024 (2 instances)

obj_id = id(obj)

# ==================================================
# Line: 1168

qualified_name = _qualified_name(obj)

# ==================================================
# Occurrences: Lines 1196-1200 (2 instances)

qualified_name = _qualified_name(obj)

# ==================================================
# Line: 1213

_rcb = _jit_internal.createResolutionCallbackFromClosure(obj)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/frontend.py
# Occurrences: Lines 455-463 (2 instances)

ctx_range = ctx.make_range(
    expr.lineno, expr.col_offset - 1, expr.col_offset + len(expr.arg)
)

# ==================================================
# Line: 981

err_range = ctx.make_raw_range(lhs.range().end, rhs.range().start)

# ==================================================
# Line: 990

err_range = ctx.make_raw_range(lhs.range().end, rhs.range().start)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_shape_functions.py
# Occurrences: Lines 105-107 (4 instances)

assert len(sizes) >= len(self)

# ==================================================
# Occurrences: Lines 637-638 (2 instances)

assert len(self) <= 2

# ==================================================
# Occurrences: Lines 974-975 (2 instances)

assert len(input) == len(dims)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/supported_ops.py
# Line: 89

attr = getattr(mod, elem)

# ==================================================
# Line: 115

builtin = _find_builtin(getattr(mod, elem))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/annotations.py
# Line: 403

ann_args = typing.get_args(ann)  # always returns a tuple!

# ==================================================
# Occurrences: Lines 415-421 (3 instances)

return TupleType([try_ann_to_type(a, loc) for a in ann_args])

# ==================================================
# Occurrences: Lines 450-453 (2 instances)

for a in typing.get_args(ann):

# ==================================================
# Occurrences: Lines 459-463 (3 instances)

return RRefType(try_ann_to_type(ann_args[0], loc))

# ==================================================
# Occurrences: Lines 493-494 (2 instances)

if _get_script_class(ann) is None:

# ==================================================
# Occurrences: Lines 500-504 (2 instances)

maybe_script_class = _get_script_class(ann)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_trace.py
# Occurrences: Lines 121-121 (2 instances)

trace_inputs = _unflatten(in_args, in_desc)

# ==================================================
# Occurrences: Lines 128-128 (2 instances)

inputs_states.append(_unflatten(in_args, in_desc))

# ==================================================
# Occurrences: Lines 188-189 (2 instances)

start = torch.cuda.Event(enable_timing=True)

# ==================================================
# Occurrences: Lines 413-413 (3 instances)

mod_stack = n_mod.sourceRange()

# ==================================================
# Occurrences: Lines 454-454 (3 instances)

compare_stack = n_mod.sourceRange()

# ==================================================
# Occurrences: Lines 479-479 (2 instances)

graph_diff_errors, tensor_compare_errors = graph_diagnostic_info()

# ==================================================
# Occurrences: Lines 588-588 (2 instances)

diag_info = graph_diagnostic_info()

# ==================================================
# Occurrences: Lines 1252-1255 (4 instances)

forward_method = getattr(mod, method_name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_recursive.py
# Occurrences: Lines 230-233 (4 instances)

attr_type = torch._C.InferredType(ann_to_type)

# ==================================================
# Line: 249

attr_type, _ = infer_type(name, item)

# ==================================================
# Line: 263

attr_type, _ = infer_type(name, item)

# ==================================================
# Line: 271

attr_type, _ = infer_type(name, item)

# ==================================================
# Occurrences: Lines 579-579 (2 instances)

orig_value = getattr(nn_module, name)

# ==================================================
# Occurrences: Lines 590-590 (2 instances)

orig_value = getattr(nn_module, name)

# ==================================================
# Occurrences: Lines 614-616 (3 instances)

item = getattr(nn_module, name, None)

# ==================================================
# Line: 706

item = getattr(nn_module, name, None)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/cond.py
# Line: 221

n_primals = len(args)

# ==================================================
# Line: 231

assert len(args) == len(grad_args)

# ==================================================
# Line: 461

merged_out = mode.shape_env.create_unbacked_symint()

# ==================================================
# Line: 520

new_size = mode.shape_env.create_unbacked_symint()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/effects.py
# Line: 260

token_tensor = new_token_tensor()

# ==================================================
# Line: 269

tokens[key] = new_token_tensor()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/triton_kernel_wrap.py
# Line: 194

triton_version = get_triton_attrs_descriptor_version()

# ==================================================
# Occurrences: Lines 209-210 (2 instances)

target = triton.runtime.driver.active.get_current_target()

# ==================================================
# Occurrences: Lines 255-260 (3 instances)

target = triton.runtime.driver.active.get_current_target()

# ==================================================
# Occurrences: Lines 376-378 (2 instances)

lambda: defaultdict(list)

# ==================================================
# Line: 429

fn_ops = defaultdict(list)

# ==================================================
# Line: 930

kwargs = kwargs.copy()

# ==================================================
# Line: 950

kwargs = kwargs.copy()

# ==================================================
# Line: 1504

new_configs = copy.deepcopy(variable.kernel.configs)

# ==================================================
# Line: 1547

new_var = type(variable)(new_kernel, None, variable.grid)

# ==================================================
# Line: 1570

new_configs = copy.deepcopy(variable.kernel.configs)

# ==================================================
# Line: 1591

new_var = type(variable)(new_kernel, None, variable.grid)

# ==================================================
# Line: 1609

new_configs = copy.deepcopy(variable.kernel.configs)

# ==================================================
# Line: 1629

new_var = type(variable)(new_kernel, None, variable.grid)

# ==================================================
# Line: 1689

new_var = type(variable)(new_kernel, None, variable.grid)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/while_loop.py
# Occurrences: Lines 136-140 (2 instances)

carried, additional = pytree.tree_unflatten(flat_args, in_spec)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/__init__.py
# Occurrences: Lines 271-271 (2 instances)

last_error = ctypes.get_last_error()

# ==================================================
# Occurrences: Lines 286-286 (2 instances)

err = ctypes.WinError(ctypes.get_last_error())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/xeon/run_cpu.py
# Occurrences: Lines 196-198 (6 instances)

self.physical_core_node_map[int(cpuinfo[1])] = int(node_id)

# ==================================================
# Line: 339

find_tc = self.add_lib_preload(lib_type="tcmalloc")

# ==================================================
# Line: 347

find_je = self.add_lib_preload(lib_type="jemalloc")

# ==================================================
# Occurrences: Lines 362-366 (2 instances)

find_tc = self.add_lib_preload(lib_type="tcmalloc")

# ==================================================
# Line: 447

and args.ncores_per_instance * args.ninstances < len(cores)

# ==================================================
# Occurrences: Lines 453-456 (2 instances)

len(cores),

# ==================================================
# Line: 471

cores = self.cpuinfo.get_all_physical_cores()

# ==================================================
# Line: 478

args.ncores_per_instance = len(cores)

# ==================================================
# Occurrences: Lines 486-495 (4 instances)

if args.ninstances > len(cores):

# ==================================================
# Line: 514

args.ninstances = len(cores) // args.ncores_per_instance

# ==================================================
# Line: 525

while ncore_per_node * i <= len(cores):

# ==================================================
# Occurrences: Lines 534-537 (3 instances)

assert len(cores) % args.ncores_per_instance == 0

# ==================================================
# Occurrences: Lines 547-548 (2 instances)

cores = self.cpuinfo.get_all_physical_cores()

# ==================================================
# Occurrences: Lines 556-557 (2 instances)

cores = self.cpuinfo.get_all_physical_cores()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/cudnn/rnn.py
# Line: 49

dropout_state[dropout_desc_name].get() is None

# ==================================================
# Line: 63

dropout_ts = dropout_state[dropout_desc_name].get()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/_nnapi/serializer.py
# Occurrences: Lines 384-389 (4 instances)

scale = tensor.q_scale()

# ==================================================
# Line: 735

retval_count = len(return_values)

# ==================================================
# Line: 742

assert len(return_shapes) == len(return_values)

# ==================================================
# Occurrences: Lines 1157-1159 (2 instances)

inputs[4] = self.add_immediate_int_scalar(0)  # begin mask

# ==================================================
# Occurrences: Lines 1190-1194 (4 instances)

out_shape = change_element(in_oper.shape, dim, -1)

# ==================================================
# Occurrences: Lines 1644-1649 (6 instances)

inputs[1] = self.add_immediate_int_scalar(0)

# ==================================================
# Occurrences: Lines 1666-1668 (2 instances)

image, size_jit, scale_jit = node.inputs()

# ==================================================
# Occurrences: Lines 2156-2160 (4 instances)

inputs[10] = self.add_immediate_int_scalar(fuse_code)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/sparse/__init__.py
# Occurrences: Lines 606-606 (4 instances)

obj.values().shape[batch_dim + 1 : batch_dim + 3]

# ==================================================
# Occurrences: Lines 628-628 (4 instances)

values = obj.values()

# ==================================================
# Occurrences: Lines 634-634 (4 instances)

values = obj.values()

# ==================================================
# Occurrences: Lines 647-649 (12 instances)

a = args.pop(0)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/sparse/_semi_structured_conversions.py
# Occurrences: Lines 89-93 (2 instances)

dense_4 = dense.view(-1, k // ksparse, ksparse)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/sparse/_triton_ops.py
# Line: 395

others = as1Dbatch(others)

# ==================================================
# Line: 405

accumulators = torch.zeros(
    (*others_shape[:-2], M, N), dtype=blocks.dtype, device=blocks.device
)

# ==================================================
# Line: 413

accumulators = as1Dbatch(accumulators)

# ==================================================
# Line: 445

others = as1Dbatch(others)

# ==================================================
# Line: 455

accumulators = torch.zeros(
    (*others_shape[:-2], M, N), dtype=blocks.dtype, device=blocks.device
)

# ==================================================
# Line: 463

accumulators = as1Dbatch(accumulators)

# ==================================================
# Occurrences: Lines 712-714 (2 instances)

num_warps = {16: 1, 32: 1, 64: 2}.get(Ms, 4)

# ==================================================
# Occurrences: Lines 930-931 (2 instances)

r0 = crow_indices[m].item()

# ==================================================
# Occurrences: Lines 938-945 (5 instances)

q_offsets = torch.cat(q_offsets_lst)

# ==================================================
# Occurrences: Lines 956-957 (2 instances)

r0 = crow_indices[m].item()

# ==================================================
# Occurrences: Lines 967-976 (5 instances)

q_offsets = torch.cat(q_offsets_lst)

# ==================================================
# Occurrences: Lines 991-992 (2 instances)

r0 = crow_indices[m].item()

# ==================================================
# Line: 1207

left_alpha = dense.new_empty(()).expand(
    *original_batch_dims_broadcasted, M, N
)  # not referenced

# ==================================================
# Line: 1217

right_alpha = dense.new_empty(()).expand(
    *original_batch_dims_broadcasted, M, N
)  # not referenced

# ==================================================
# Occurrences: Lines 1826-1836 (4 instances)

row_tile = tl.load(
    curr_row_values_ptrs + row_arange, mask=mask, other=-float("inf")
).to(tl.float32)

# ==================================================
# Occurrences: Lines 1842-1851 (5 instances)

num = tl.exp(row_tile - max_row_value)

# ==================================================
# Occurrences: Lines 1862-1865 (2 instances)

row_tile = tl.load(
    curr_row_values_ptrs + row_arange, mask=mask, other=-float("inf")
).to(tl.float32)

# ==================================================
# Occurrences: Lines 1878-1883 (3 instances)

if input._nnz() == 0 or input.numel() == 0:

# ==================================================
# Occurrences: Lines 1896-1900 (3 instances)

if input.values().transpose(-3, -2).is_contiguous():

# ==================================================
# Line: 1932

.reshape(*input.values().shape)

# ==================================================
# Occurrences: Lines 2196-2197 (2 instances)

q = tl.load(q_ptr)

# ==================================================
# Occurrences: Lines 2207-2208 (2 instances)

q = tl.load(q_ptr)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/sparse/_triton_ops_meta.py
# Line: 139

op_data = _operation_device_version_data.get((op, device_name, version))

# ==================================================
# Line: 150

op_data = _operation_device_version_data.get((op, device_name, version))

# ==================================================
# Occurrences: Lines 284-287 (2 instances)

return tuple(parameters[k] for k in sorted(parameters))

# ==================================================
# Line: 304

if verbose and "out of resource" not in str(msg):

# ==================================================
# Line: 321

if verbose and "out of resource" not in str(msg):

# ==================================================
# Occurrences: Lines 344-354 (9 instances)

next_parameters = parameters.copy()

# ==================================================
# Occurrences: Lines 360-361 (8 instances)

all_values[next_key] = str(msg)

# ==================================================
# Occurrences: Lines 404-410 (9 instances)

next_value = step_func(name, value, direction, parameters)

# ==================================================
# Line: 471

device_name = torch.cuda.get_device_name()

# ==================================================
# Line: 564

device_name = torch.cuda.get_device_name()

# ==================================================
# Occurrences: Lines 908-908 (3 instances)

(bench(meta), sparsity, tuple(meta[k] for k in sorted(meta)))

# ==================================================
# Occurrences: Lines 934-934 (3 instances)

tuple(meta[k] for k in sorted(meta)),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/__init__.py
# Occurrences: Lines 96-96 (2 instances)

out = cast(Union[torch.Tensor, graph.GradientEdge], out)

# ==================================================
# Occurrences: Lines 141-141 (2 instances)

out = cast(Union[torch.Tensor, graph.GradientEdge], out)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/_functions/tensor.py
# Occurrences: Lines 48-52 (2 instances)

"x".join(map(str, tensor.size())),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler_util.py
# Line: 148

if bw_parent(evt) is None and evt.stack is not None:

# ==================================================
# Line: 154

p = bw_parent(evt)

# ==================================================
# Occurrences: Lines 601-606 (2 instances)

return sum(kinfo.duration for kinfo in self.kernels) + sum(

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler_legacy.py
# Line: 196

name = record.name()

# ==================================================
# Line: 213

if _filter_name(record.name()) or record_key in filtered_handles:

# ==================================================
# Line: 222

prev_record.name() == record.name()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler.py
# Occurrences: Lines 361-363 (2 instances)

t0 = perf_counter_ns()

# ==================================================
# Occurrences: Lines 369-371 (2 instances)

t0 = perf_counter_ns()

# ==================================================
# Occurrences: Lines 388-391 (2 instances)

t0 = perf_counter_ns()

# ==================================================
# Occurrences: Lines 427-432 (3 instances)

t0 = perf_counter_ns()

# ==================================================
# Occurrences: Lines 440-443 (3 instances)

t0 = perf_counter_ns()

# ==================================================
# Occurrences: Lines 588-589 (4 instances)

rel_end_ns = kineto_event.end_ns() - trace_start_ns

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/functional.py
# Occurrences: Lines 452-460 (4 instances)

grad_res = _autograd_grad(
    grad_inputs, grad_outputs, v, create_graph=create_graph
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/gradcheck.py
# Occurrences: Lines 194-201 (3 instances)

x_values = x_tensor.values()

# ==================================================
# Occurrences: Lines 216-219 (3 instances)

x_values = x_block_values.flatten(0, 2)

# ==================================================
# Occurrences: Lines 234-235 (2 instances)

x_values = x_block_values.flatten(0, 2)

# ==================================================
# Occurrences: Lines 375-377 (2 instances)

outa = fn()

# ==================================================
# Occurrences: Lines 556-559 (3 instances)

raw_outputs = _as_tuple(fn(*dual_inputs))

# ==================================================
# Occurrences: Lines 581-584 (3 instances)

raw_outputs = _as_tuple(fn(*dual_inputs))

# ==================================================
# Occurrences: Lines 776-780 (4 instances)

vjps1 = _get_analytical_vjps_wrt_specific_output(vjp_fn, output.clone(), v)

# ==================================================
# Occurrences: Lines 858-859 (2 instances)

vjps1 = _compute_analytical_jacobian_rows(vjp_fn, output.clone())

# ==================================================
# Occurrences: Lines 1249-1249 (2 instances)

inp = fwAD.make_dual(inp.detach(), torch.zeros_like(inp))

# ==================================================
# Occurrences: Lines 1265-1272 (13 instances)

dual_inputs[idx] = fwAD.make_dual(inp.detach(), torch.zeros_like(inp))

# ==================================================
# Line: 1341

for o in _differentiable_outputs(func(*inputs))

# ==================================================
# Line: 1350

output_to_check = _differentiable_outputs(func(*inputs))

# ==================================================
# Line: 1465

imag_outputs = _differentiable_outputs(imag_func_out)

# ==================================================
# Line: 1481

real_outputs = _differentiable_outputs(real_func_out)

# ==================================================
# Line: 1523

diff_imag_func_out = _differentiable_outputs(imag_func_out)

# ==================================================
# Line: 1544

diff_real_func_out = _differentiable_outputs(real_func_out)

# ==================================================
# Line: 1674

torch.rand(x_values.numel(), generator=generator)
.to(dtype=dtype, device=x.device)
.view(x_values.shape)

# ==================================================
# Line: 1688

torch.rand(x_values.numel(), generator=generator)
.to(dtype=dtype, device=x.device)
.view(x_values.shape)

# ==================================================
# Occurrences: Lines 1811-1814 (4 instances)

ur = _vec_from_tensor_cpu(inp, g_cpu, True)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/graph.py
# Line: 511

id = torch._C._current_graph_task_id()

# ==================================================
# Line: 548

id = torch._C._current_graph_task_id()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/csrc/lazy/test_mnist.py
# Occurrences: Lines 32-39 (3 instances)

x = F.relu(x)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/non_strict_utils.py
# Line: 834

cur_mod = getattr(cur_mod, attr)

# ==================================================
# Occurrences: Lines 842-843 (2 instances)

cur_mod, attr = _leaf_mod_and_attr(mod, fqn)

# ==================================================
# Line: 857

cur_mod, attr = _leaf_mod_and_attr(mod, fqn)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/pass_base.py
# Line: 106

x = torch.dequantize(x)

# ==================================================
# Line: 117

fake_tensor = self.fake_tensor_mode.from_tensor(x)

# ==================================================
# Occurrences: Lines 139-143 (2 instances)

x = torch.dequantize(x)

# ==================================================
# Occurrences: Lines 430-431 (2 instances)

fake_tensor_mode = nullcontext()  # type: ignore[assignment]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/utils.py
# Occurrences: Lines 178-178 (2 instances)

submodule = _getattr(mod, target)

# ==================================================
# Occurrences: Lines 191-191 (2 instances)

submodule = _getattr(mod, target)

# ==================================================
# Line: 335

path = get_keystr(keypath)

# ==================================================
# Line: 351

path = get_keystr(keypath)

# ==================================================
# Line: 368

path = get_keystr(keypath)

# ==================================================
# Line: 376

path = get_keystr(keypath)

# ==================================================
# Line: 387

path = get_keystr(keypath)

# ==================================================
# Occurrences: Lines 1391-1395 (5 instances)

if ref is None or ref() is None:

# ==================================================
# Line: 1418

flattened, [flat_names, *args] = flatten_fn(obj)  # type: ignore[misc]

# ==================================================
# Line: 1449

flats, context = flatten_fn(obj)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/converter.py
# Line: 49

orig_state_dict_keys = torch.jit._unique_state_dict(model).keys()

# ==================================================
# Line: 65

if orig_state_dict_keys != torch.jit._unique_state_dict(model).keys():

# ==================================================
# Line: 154

sym_size_int = torch.ops.aten.sym_size.int(im, dim)

# ==================================================
# Line: 163

sym_size_int = torch.ops.aten.sym_size.int(im, dim)

# ==================================================
# Line: 371

schema_str = node.schema()

# ==================================================
# Line: 386

f"Unable to find operator {node.kind()} with schema {node.schema()}"

# ==================================================
# Occurrences: Lines 537-539 (4 instances)

kwargs[schema_arg.name] = self.get_fx_value_by_ir_value(input)

# ==================================================
# Occurrences: Lines 602-602 (2 instances)

normalized_name = normalize_name(name)

# ==================================================
# Occurrences: Lines 610-614 (4 instances)

fx_node = get_node_as_placeholder_or_get_attr(
    self.fx_graph, name, self.is_top_level_graph()
)

# ==================================================
# Occurrences: Lines 623-630 (4 instances)

fx_node = get_node_as_placeholder_or_get_attr(
    self.fx_graph, name, self.is_top_level_graph()
)

# ==================================================
# Occurrences: Lines 641-643 (2 instances)

fx_node = get_node_as_placeholder_or_get_attr(
    self.fx_graph, name, self.is_top_level_graph()
)

# ==================================================
# Line: 728

constant_kind = node.kindOf("value")

# ==================================================
# Line: 745

raise ValueError(f"Unsupported constant type: {node.kindOf('value')}")

# ==================================================
# Occurrences: Lines 850-852 (4 instances)

k = self.get_fx_value_by_ir_value(inp)

# ==================================================
# Occurrences: Lines 1593-1593 (3 instances)

output_name = node.output().debugName()

# ==================================================
# Occurrences: Lines 1599-1599 (3 instances)

output_name = node.output().debugName()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/serde/schema_check.py
# Occurrences: Lines 83-83 (3 instances)

args = typing.get_args(t)

# ==================================================
# Occurrences: Lines 96-96 (3 instances)

*[dump_type(x, level + 1) for x in typing.get_args(t)]

# ==================================================
# Line: 205

fields, cpp_fields, thrift_fields = _handle_aggregate(ty)

# ==================================================
# Line: 273

fields, cpp_fields, thrift_fields = _handle_aggregate(ty)

# ==================================================
# Line: 634

checksum_head = match.group(1)

# ==================================================
# Line: 642

thrift_checksum_head = match.group(1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/serde/serialize.py
# Line: 573

meta_val = node.meta.get("val", None)

# ==================================================
# Line: 606

meta_val = node.meta.get("val", None)

# ==================================================
# Line: 892

arg_name = arg.get_name()

# ==================================================
# Line: 899

arg_name = arg.get_name()

# ==================================================
# Occurrences: Lines 933-935 (2 instances)

arg_type = arg_type.getElementType()  # type: ignore[assignment]

# ==================================================
# Line: 1391

name = self._output_node_name_at_index(node, idx)

# ==================================================
# Occurrences: Lines 1418-1418 (2 instances)

name = self._output_node_name_at_index(node, idx)

# ==================================================
# Occurrences: Lines 1438-1438 (2 instances)

user_node_name = self._output_node_name_at_index(node, idx)

# ==================================================
# Occurrences: Lines 1911-1911 (2 instances)

placeholder_node = self.graph.placeholder(node_name)

# ==================================================
# Occurrences: Lines 1919-1919 (2 instances)

placeholder_node = self.graph.placeholder(node_name)

# ==================================================
# Occurrences: Lines 1936-1936 (2 instances)

placeholder_node = self.graph.placeholder(node_name)

# ==================================================
# Line: 2011

metadata = self.deserialize_metadata(serialized_node.metadata)

# ==================================================
# Line: 2034

fx_node = self.graph.create_node(
    "call_function", target, args, kwargs, name
)

# ==================================================
# Line: 2052

fx_node = self.graph.create_node(
    "call_function", target, args, kwargs, name
)

# ==================================================
# Line: 2072

fx_node.meta.update(self.deserialize_metadata(serialized_node.metadata))

# ==================================================
# Occurrences: Lines 2376-2378 (4 instances)

kwargs[input_.name] = self.deserialize_input(input_.arg)

# ==================================================
# Occurrences: Lines 2928-2931 (2 instances)

if typing.get_origin(cls) == typing.Union and type(None) in typing.get_args(cls):

# ==================================================
# Occurrences: Lines 2953-2956 (2 instances)

d_type = typing.get_args(cls)[0]

# ==================================================
# Occurrences: Lines 3086-3086 (2 instances)

if s := get_name(a):

# ==================================================
# Occurrences: Lines 3094-3094 (2 instances)

if s := get_name(a):

# ==================================================
# Occurrences: Lines 3106-3106 (2 instances)

if s := get_name(a):

# ==================================================
# Occurrences: Lines 3120-3125 (4 instances)

if s := get_name(a):

# ==================================================
# Occurrences: Lines 3202-3213 (8 instances)

a.name = name_table.get(a.name, a.name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/passes/constant_folding.py
# Line: 120

return super().run_node(node)

# ==================================================
# Line: 165

out = super().run_node(node)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/passes/replace_with_hop_pass_util.py
# Line: 31

call_func_node.meta["nn_module_stack"] = copy.copy(
    enter_block_node.meta.get("nn_module_stack", {})
)

# ==================================================
# Line: 45

get_attr_node.meta["nn_module_stack"] = copy.copy(
    enter_block_node.meta.get("nn_module_stack", {})
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/passes/lift_constants_pass.py
# Occurrences: Lines 258-267 (8 instances)

constant_fqn = _get_first_fqn(constant_attrs, constant_val)

# ==================================================
# Occurrences: Lines 282-291 (8 instances)

constant_fqn = _get_first_fqn(constant_attrs, constant_val)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/wrappers.py
# Line: 91

flat_args, in_spec = pytree.tree_flatten((args, kwargs))

# ==================================================
# Line: 98

_, in_spec = pytree.tree_flatten((args, kwargs))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/debug.py
# Line: 166

name = snode.get_name()

# ==================================================
# Line: 180

name = snode.get_name()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/sizevars.py
# Occurrences: Lines 94-101 (5 instances)

replacement_count = len(self.replacements)

# ==================================================
# Occurrences: Lines 118-125 (5 instances)

replacement_count = len(self.replacements)

# ==================================================
# Occurrences: Lines 195-198 (2 instances)

return FloorDiv(remove_zero_terms(base, divisor), divisor)

# ==================================================
# Occurrences: Lines 589-595 (5 instances)

prior_len = len(self.replacements)

# ==================================================
# Line: 926

m1 = term1.match(scale * ModularIndexing(base, divisor, mod1))

# ==================================================
# Line: 944

m1 = term1.match(scale * ModularIndexing(base, divisor, mod1))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/virtualized.py
# Occurrences: Lines 167-168 (2 instances)

self.removed_buffers = OrderedSet[Any]()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/jagged_lowerings.py
# Line: 147

offsets_dtype = offsets.get_dtype()

# ==================================================
# Line: 156

offsets_loader = offsets.make_loader()

# ==================================================
# Line: 212

offsets_dtype = offsets.get_dtype()

# ==================================================
# Line: 220

offsets_loader = offsets.make_loader()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codecache.py
# Line: 323

choice_hash = choice.hash_key()

# ==================================================
# Line: 353

local_cache[op][inputs][precision][choice.hash_key()] = timing

# ==================================================
# Line: 362

choice.hash_key(): timings[choice] for choice in choices

# ==================================================
# Occurrences: Lines 577-579 (2 instances)

start = time()

# ==================================================
# Line: 2346

result = cls._load_library_inner(path, key)

# ==================================================
# Line: 2354

result = cls._load_library_inner(path, key)

# ==================================================
# Occurrences: Lines 3332-3334 (2 instances)

paths = _cutlass_paths()

# ==================================================
# Line: 3659

start_time = time()

# ==================================================
# Line: 3691

end_time = time()

# ==================================================
# Line: 3791

start_time = time()

# ==================================================
# Line: 3803

end_time = time()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/standalone_compile.py
# Occurrences: Lines 130-132 (2 instances)

assert reader.read_bytes() == torch_key()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/utils.py
# Occurrences: Lines 200-201 (2 instances)

start_event = torch.cuda.Event(enable_timing=True)

# ==================================================
# Occurrences: Lines 218-219 (2 instances)

start_event = [torch.cuda.Event(enable_timing=True) for _ in range(n_repeat)]

# ==================================================
# Occurrences: Lines 273-274 (2 instances)

start_event = torch.cuda.Event(enable_timing=True)

# ==================================================
# Occurrences: Lines 541-545 (2 instances)

t0 = time.perf_counter()

# ==================================================
# Line: 684

sources = sorted(OrderedSet(sources))

# ==================================================
# Line: 695

sources = sorted(OrderedSet(sources))

# ==================================================
# Occurrences: Lines 713-714 (2 instances)

from_node_dict = collections.defaultdict(list)

# ==================================================
# Occurrences: Lines 2223-2231 (4 instances)

before_io = io.StringIO()

# ==================================================
# Line: 2764

context = torch._guards.TracingContext.try_get()

# ==================================================
# Line: 2774

if ctx := torch._guards.TracingContext.try_get():

# ==================================================
# Line: 3020

V.debug._inductor_triton_kernel_to_post_grad_node_info.setdefault(
    kernel_name, []
)

# ==================================================
# Line: 3034

curr_node_info = V.debug._inductor_triton_kernel_to_post_grad_node_info.setdefault(
    kernel_name, []
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fuzzer.py
# Occurrences: Lines 266-271 (2 instances)

map(type, next(iter(default.items())))

# ==================================================
# Line: 289

new_type = random.choice(type_hint.__args__)

# ==================================================
# Line: 321

return random.choice(type_hint.__args__)

# ==================================================
# Line: 763

test_model_fn = self.test_model_fn_factory()

# ==================================================
# Line: 773

test_model_fn2 = self.test_model_fn_factory()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/tiling_utils.py
# Occurrences: Lines 168-172 (3 instances)

zero_index = sympy_subs(index, variables)

# ==================================================
# Occurrences: Lines 180-180 (2 instances)

if (sympy_subs(index, variables) - new_val) == 1:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/flex_decoding.py
# Line: 370

Bq, Hq, seq_len_q, qk_head_dim = query.get_size()

# ==================================================
# Occurrences: Lines 456-467 (2 instances)

buf_M = empty_strided(
    buf_ML_shape,
    None,
    dtype=torch.float32,  # The rowmax is always stored in fp32 regardless of the input dtype
    device=query.get_device(),
)

# ==================================================
# Occurrences: Lines 540-543 (6 instances)

v = cur_kernel_options.pop(k)

# ==================================================
# Line: 578

call_sizes=query.get_size(),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/mm_common.py
# Occurrences: Lines 146-148 (2 instances)

*b2, n, k2 = mat2.get_size()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/flex_attention.py
# Line: 159

indices, tensor_indices = check_and_broadcast_indices(indices, grad.get_device())

# ==================================================
# Line: 176

device = grad.get_device()

# ==================================================
# Occurrences: Lines 1421-1426 (4 instances)

small_dqk = V.graph.sizevars.evaluate_expr(sympy.Lt(query.get_size()[-1], 16))

# ==================================================
# Line: 1482

sympy.Ne(query.get_size()[1], key.get_size()[1]),

# ==================================================
# Occurrences: Lines 1529-1530 (2 instances)

Bq, Hq, seq_len_q, qk_head_dim = query.get_size()

# ==================================================
# Occurrences: Lines 1632-1635 (6 instances)

v = cur_kernel_options.pop(k)

# ==================================================
# Line: 1688

call_sizes=query.get_size(),

# ==================================================
# Occurrences: Lines 2593-2595 (3 instances)

device = query.get_device()

# ==================================================
# Line: 2650

create_placeholder(name, dtype, query.get_device())

# ==================================================
# Occurrences: Lines 2690-2691 (2 instances)

dtype=query.get_dtype(),

# ==================================================
# Line: 2717

empty(0, device=query.get_device()) for _ in range(4)

# ==================================================
# Occurrences: Lines 2764-2767 (6 instances)

v = cur_kernel_options.pop(k)

# ==================================================
# Line: 2817

call_sizes=query.get_size() + key.get_size()[1:3],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/conv.py
# Line: 478

if len(x.get_size()) == 3 and len(kernel_shape) == 1 and device_type == "xpu":

# ==================================================
# Line: 496

ndim = len(kernel_shape)

# ==================================================
# Occurrences: Lines 506-509 (2 instances)

layout = conv_layout(x, weight, None, **kwargs)

# ==================================================
# Occurrences: Lines 546-551 (3 instances)

layout = conv_layout(x, weight, None, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/pattern_matcher.py
# Occurrences: Lines 299-302 (2 instances)

graph_with_eager_vals = trace_fn(replacement_fn, example_vals)

# ==================================================
# Occurrences: Lines 321-322 (2 instances)

example_vals = torch.fx.map_arg(args, lambda arg: arg.meta["val"])

# ==================================================
# Occurrences: Lines 654-654 (2 instances)

cls = type(x)

# ==================================================
# Occurrences: Lines 660-660 (2 instances)

is_leaf=lambda x: type(x) in type_mapping,

# ==================================================
# Line: 667

is_leaf=lambda x: type(x) in type_mapping,

# ==================================================
# Line: 1345

seen_patterns[pattern_repr].append(str(graph) if graph else None)

# ==================================================
# Line: 1356

new_graph_str = str(graph)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/ir.py
# Line: 1254

split = inner_reduction_splits(reduction_numel_hint, numel_hint)

# ==================================================
# Occurrences: Lines 1327-1335 (8 instances)

original_stride = getattr(buf.layout, "stride", None)

# ==================================================
# Line: 1357

return ReductionHint.INNER, inner_reduction_splits(
    reduction_numel_hint, numel_hint
)

# ==================================================
# Occurrences: Lines 2002-2004 (3 instances)

mean = const(0)

# ==================================================
# Line: 2024

return copy(inner_fns[0]), const(0), const(1)

# ==================================================
# Occurrences: Lines 2587-2603 (2 instances)

return as_storage_and_layout(
    x.data,
    freeze=freeze,
    want_contiguous=want_contiguous,
    stride_order=stride_order,
    allow_padding=allow_padding,
    exact_strides=exact_strides,
)

# ==================================================
# Occurrences: Lines 3084-3085 (4 instances)

size_old = stack_old.pop()

# ==================================================
# Occurrences: Lines 3096-3096 (2 instances)

var2, size_new2 = stack_new.pop()

# ==================================================
# Occurrences: Lines 3107-3107 (2 instances)

modulus = stack_old.pop()

# ==================================================
# Occurrences: Lines 3116-3121 (2 instances)

size_old = stack_old.pop()

# ==================================================
# Line: 4971

output_stride = make_channels_last_strides_for(new_size)

# ==================================================
# Line: 4985

output_stride = make_channels_last_strides_for(new_size)

# ==================================================
# Line: 5552

exact_strides, x.get_layout().stride, x.get_size()

# ==================================================
# Line: 5573

x.get_size(),

# ==================================================
# Line: 5585

exact_strides, x.get_layout().stride, x.get_size()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/compile_worker/subproc_pool.py
# Occurrences: Lines 117-118 (2 instances)

subproc_read_fd, write_fd = os.pipe()

# ==================================================
# Occurrences: Lines 158-161 (2 instances)

self.write_lock = threading.Lock()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/comm_lowering.py
# Line: 201

inp = clone(inp)

# ==================================================
# Line: 210

inp = ir.ExternKernel.require_contiguous(inp)

# ==================================================
# Line: 229

inp = ir.ExternKernel.require_contiguous(inp)

# ==================================================
# Line: 237

inputs = [clone(inp) for inp in inputs]

# ==================================================
# Line: 329

inp = clone(inp)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_utils.py
# Line: 518

input = input_loader(index)

# ==================================================
# Occurrences: Lines 527-535 (5 instances)

input = input_loader(index)

# ==================================================
# Occurrences: Lines 542-546 (4 instances)

input = input_loader(index)

# ==================================================
# Line: 558

result = ops.to_dtype(result, dtype)

# ==================================================
# Line: 564

input = input_loader(index)

# ==================================================
# Occurrences: Lines 571-581 (3 instances)

return ops.sigmoid(input_loader(index))

# ==================================================
# Occurrences: Lines 590-597 (3 instances)

input = input_loader(index)

# ==================================================
# Occurrences: Lines 606-614 (4 instances)

input = input_loader(index)

# ==================================================
# Occurrences: Lines 624-626 (2 instances)

input = input_loader(index)

# ==================================================
# Line: 632

result = ops.to_dtype(result, dtype)

# ==================================================
# Occurrences: Lines 641-648 (3 instances)

other_loader = other.make_loader()

# ==================================================
# Occurrences: Lines 657-661 (2 instances)

bias_loader = other.make_loader()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/triton_combo_kernel.py
# Occurrences: Lines 428-428 (2 instances)

code.writeline(f"{tree.prefix}numel = {int(simplified_tree_numel)}")

# ==================================================
# Occurrences: Lines 435-435 (2 instances)

grid.append(int(simplified_tree_numel))

# ==================================================
# Occurrences: Lines 441-441 (2 instances)

val = int(simplified_tree_numel)

# ==================================================
# Occurrences: Lines 468-468 (2 instances)

x_numels = int(simplified_tree_numel)

# ==================================================
# Occurrences: Lines 480-480 (2 instances)

x_numels = int(simplified_tree_numel)

# ==================================================
# Line: 832

device = V.graph.get_current_device_or_throw()

# ==================================================
# Line: 848

index = V.graph.get_current_device_or_throw().index

# ==================================================
# Occurrences: Lines 911-913 (2 instances)

modified_line = modified_line.replace(
    block, f"{block}_{num_kernel}"
)

# ==================================================
# Occurrences: Lines 920-922 (2 instances)

modified_line = modified_line.replace(
    block, f"{block}_{num_kernel}"
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_flex_attention_template.py
# Occurrences: Lines 795-797 (2 instances)

start_offset = getattr(self, len_attr)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cutlass_cache.py
# Line: 73

start_time = time.time()

# ==================================================
# Line: 104

log.info("Loaded ops from %s cache in %.3fs", filename, time.time() - start_time)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cutlass_lib_extensions/gemm_operation_extensions.py
# Line: 157

2 if "2sm" in operation.procedural_name() else 1

# ==================================================
# Line: 176

sizeof(typename {str(operation.procedural_name())}_epilogue::SharedStorage))>"

# ==================================================
# Line: 212

epilogue_functor = self.emit_block_scale_epilogue_functor(operation)

# ==================================================
# Line: 220

epilogue_functor = self.emit_block_scale_epilogue_functor(operation)

# ==================================================
# Line: 268

operation_name_str = operation.procedural_name()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cuda_cpp_scheduling.py
# Line: 215

scheduler_nodes_to_fuse = node_to_fuse.get_nodes()

# ==================================================
# Occurrences: Lines 229-233 (4 instances)

elif not node.get_computed_buffer_name():  # type: ignore[attr-defined]

# ==================================================
# Line: 273

existing_epilogue_nodes + list(node_to_fuse.get_nodes()),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/gemm_template.py
# Line: 953

start_time = time.time()

# ==================================================
# Line: 966

time.time() - start_time,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cutlass_utils.py
# Line: 282

start_time = time.time()

# ==================================================
# Line: 299

time.time() - start_time,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cuda_template.py
# Line: 87

kernel_name = str(Placeholder.KERNEL_NAME)

# ==================================================
# Occurrences: Lines 97-102 (2 instances)

_, call_args, _, _ = kernel.args.python_argdefs()

# ==================================================
# Line: 151

kernel_name=str(Placeholder.KERNEL_NAME),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_grouped_gemm_template.py
# Line: 223

new_inputs, new_layout = reorder_and_filter(input_nodes, layout)

# ==================================================
# Line: 304

new_input_nodes, _ = reorder_and_filter(input_nodes, layout)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_wrapper_cpu.py
# Occurrences: Lines 63-67 (4 instances)

self.kernel_callsite_id = count()

# ==================================================
# Occurrences: Lines 73-74 (2 instances)

self.cached_output_id = count()

# ==================================================
# Occurrences: Lines 296-296 (2 instances)

code.writeline(f"int64_t {sym_or_exp} = {name_fn(base_name)}[{dim}];")

# ==================================================
# Occurrences: Lines 311-311 (2 instances)

base_name = name_fn(base_name)

# ==================================================
# Occurrences: Lines 562-565 (2 instances)

num_args = len(V.graph.graph_inputs)

# ==================================================
# Line: 656

signature = kernel.get_signature()

# ==================================================
# Line: 673

for kernel in sorted(declare_kernel):

# ==================================================
# Line: 684

signature = kernel.get_signature().replace(name, kernel_ptr)

# ==================================================
# Line: 691

for name in sorted(declare_kernel):

# ==================================================
# Occurrences: Lines 750-755 (2 instances)

V.graph.get_original_value_of_constant(name).is_cuda

# ==================================================
# Line: 1784

conditional.predicate.codegen_reference(),

# ==================================================
# Line: 1790

predicate = conditional.predicate.codegen_reference()

# ==================================================
# Line: 2457

type_.getElementType(),

# ==================================================
# Occurrences: Lines 2480-2496 (5 instances)

element_type = type_.getElementType()

# ==================================================
# Line: 2509

element_type = type_.getElementType()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/rocm/rocm_template.py
# Occurrences: Lines 80-89 (3 instances)

runtime_arg_values=self.get_runtime_arg_values(**kwargs),

# ==================================================
# Line: 113

runtime_args = self.get_runtime_arg_values(**kwargs)

# ==================================================
# Line: 130

runtime_arg_values=self.get_runtime_arg_values(**kwargs),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/rocm/ck_universal_gemm_template.py
# Line: 679

bias_layout = torch_layout_to_ck_layout(Bias.get_layout())

# ==================================================
# Line: 847

bias_layout=torch_layout_to_ck_layout(Bias.get_layout())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/triton_utils.py
# Line: 47

tye = _type_of(arg.dtype)

# ==================================================
# Line: 91

return _type_of(arg.dtype)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp.py
# Occurrences: Lines 416-419 (4 instances)

result = sympy.Symbol(f"{var}_mod_c{mod_freevar_id}")

# ==================================================
# Line: 2172

assert self.reduction_depth == len(lengths)

# ==================================================
# Line: 2180

self.reduction_depth = len(lengths)

# ==================================================
# Line: 2227

kernel = _loop_nest.get_kernel()

# ==================================================
# Line: 2258

kernel = _loop_nest.get_kernel()

# ==================================================
# Line: 3599

tiling_factor = cpu_vec_isa.pick_vec_isa().nelements(dtype=dtype)

# ==================================================
# Line: 3727

factor_lowp = cpu_vec_isa.pick_vec_isa().nelements(dtype=dtype)

# ==================================================
# Occurrences: Lines 3761-3764 (3 instances)

contig_vars = OrderedSet[int]()

# ==================================================
# Occurrences: Lines 3889-3891 (3 instances)

to_type_node = sub_graph.call_method(
    "to_dtype", args=(ops, _node, torch.float)
)

# ==================================================
# Occurrences: Lines 3990-3992 (3 instances)

to_type_node = sub_graph.call_method(
    "to_dtype", args=(ops, _node, torch.float)
)

# ==================================================
# Occurrences: Lines 4163-4166 (2 instances)

loop = self.loop_nest.tile(tiling_indices[0], factor=tiling_factors[0])

# ==================================================
# Line: 4189

outer_loop = self.loop_nest.tile(
    tiling_indices[0], factor=tiling_factors[0]
)

# ==================================================
# Line: 4240

vec_kernel = codegen_kernel(
    CppVecKernel, tiling_factors[0], tiling_indices[0]
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/halide.py
# Occurrences: Lines 795-799 (6 instances)

while handled_count < len(nodes) and not eq(tree.numel, divisor):

# ==================================================
# Occurrences: Lines 819-819 (3 instances)

handled_count = len(nodes)

# ==================================================
# Occurrences: Lines 831-831 (4 instances)

prior_len = len(sizes_to_add)

# ==================================================
# Occurrences: Lines 837-837 (4 instances)

assert len(sizes_to_add) < prior_len or prior_len == 0

# ==================================================
# Line: 1298

result_var = self.newfunc(self.sort_used_dims(all_used_dims))

# ==================================================
# Line: 1352

unpack_vars = [self.newfunc(self.sort_used_dims(all_used_dims)) for _ in values]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/block_analysis.py
# Line: 79

match_expr = sympy_dot(strides, block_index_exprs)

# ==================================================
# Line: 141

matched_index = sympy_dot(strides, block_index_exprs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/simd.py
# Line: 839

index = self.simplify_indexing(index)

# ==================================================
# Line: 862

simp_index = self.simplify_indexing(index)

# ==================================================
# Line: 1501

index_vars = kernel.split_and_set_ranges(node.get_ranges())

# ==================================================
# Line: 1519

index_vars = kernel.split_and_set_ranges(node.get_ranges())

# ==================================================
# Line: 1828

pointwise_ranges, reduction_ranges = node.get_ranges()

# ==================================================
# Line: 1837

pointwise_ranges, reduction_ranges = node.get_ranges()

# ==================================================
# Occurrences: Lines 2098-2100 (3 instances)

prev_var_coalesced_score = coalesce_analysis.coalesced_by_var.get(
    v, 0
)

# ==================================================
# Occurrences: Lines 2114-2114 (3 instances)

split_scores.append(coalesce_analysis.coalesced_by_var.get(v, 0))

# ==================================================
# Occurrences: Lines 2123-2123 (3 instances)

split_scores.append(coalesce_analysis.coalesced_by_var.get(v, 0))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/wrapper.py
# Line: 471

kernel_name = node.get_kernel_name()

# ==================================================
# Line: 479

kernel_name = node.get_kernel_name()

# ==================================================
# Occurrences: Lines 730-731 (2 instances)

assert self.node.get_name() not in V.graph.removed_buffers

# ==================================================
# Occurrences: Lines 908-909 (2 instances)

self.allocated = OrderedSet[BufferName]()

# ==================================================
# Line: 2100

"device": DeviceProperties.create(V.graph.get_current_device_or_throw()),

# ==================================================
# Line: 2216

current_device = V.graph.get_current_device_or_throw()

# ==================================================
# Occurrences: Lines 2595-2602 (4 instances)

arg_str = self.generate_example_arg_value(
    arg, arg_type, raw_arg
)

# ==================================================
# Occurrences: Lines 2838-2840 (2 instances)

self.freed.add(input_buffer.get_name())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_wrapper_cpu_array_ref.py
# Occurrences: Lines 294-297 (2 instances)

num_args = len(V.graph.graph_inputs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_micro_gemm.py
# Line: 941

result = KernelTemplate._template_from_string(self.TEMPLATE_KERNEL).render(
    options
)

# ==================================================
# Line: 951

result += KernelTemplate._template_from_string(self.TEMPLATE_KERNEL).render(
    options
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/mps.py
# Line: 638

acc_buf = self._new_idxvar(src_dtype, acc_buf_size)

# ==================================================
# Line: 683

acc_buf = self._new_idxvar(src_dtype, acc_buf_size)

# ==================================================
# Line: 690

acc_buf = self._new_idxvar("float3", acc_buf_size)

# ==================================================
# Line: 703

acc_buf = self._new_idxvar("float3", acc_buf_size)

# ==================================================
# Occurrences: Lines 815-818 (2 instances)

dtype_str = self.dtype_to_str(V.graph.get_dtype(outer))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_template_kernel.py
# Occurrences: Lines 143-147 (2 instances)

outer_name = node.get_name()

# ==================================================
# Line: 443

and multi_output_buffers[gemm_idx].get_name()

# ==================================================
# Line: 450

and multi_output_buffers[gemm_idx].get_name()

# ==================================================
# Occurrences: Lines 482-485 (4 instances)

and multi_output_buffers[gemm_idx].get_name() in all_read_names

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/simd_kernel_features.py
# Occurrences: Lines 294-294 (2 instances)

dep = dep.simplify_with_ranges()

# ==================================================
# Occurrences: Lines 312-312 (2 instances)

dep = dep.simplify_with_ranges()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_gemm_template.py
# Occurrences: Lines 689-692 (2 instances)

blocking = get_blocking(
    m_factor, n_factor, 1, m_blocks, n_blocks, k_blocks
)

# ==================================================
# Line: 712

best_blocking = get_better_blocking(blocking, best_blocking)

# ==================================================
# Occurrences: Lines 718-721 (2 instances)

blocking = get_blocking(
    m_factor, n_factor, 1, m_blocks, n_blocks, k_blocks
)

# ==================================================
# Line: 931

new_inputs, new_layout = reorder_and_filter(input_nodes, layout)

# ==================================================
# Line: 1027

new_input_nodes, _ = reorder_and_filter(input_nodes, layout)

# ==================================================
# Occurrences: Lines 1158-1163 (2 instances)

BCompensate, x_w_scale = _get_compensation_node(
    W, use_int8_fast_compensation_path
)

# ==================================================
# Occurrences: Lines 1174-1179 (2 instances)

BCompensate, _ = _get_compensation_node(
    W, use_int8_fast_compensation_path
)

# ==================================================
# Line: 1426

gemm_output_name = f"{template_buffer.get_name()}_GemmOut"

# ==================================================
# Line: 1433

buffer_name = template_buffer.get_name()

# ==================================================
# Line: 1457

Y_aliases.add(template_buffer.get_name())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/triton.py
# Line: 1821

for tree in self.active_range_trees():

# ==================================================
# Line: 1851

index, range_tree.symbol()

# ==================================================
# Line: 1858

block_shape=[TritonSymbols.get_block_size(range_tree)],

# ==================================================
# Line: 1883

index_var = range_tree.symbol()

# ==================================================
# Line: 1938

linear_block_size = TritonSymbols.get_block_size(range_tree)

# ==================================================
# Line: 1981

range_trees = self.active_range_trees()

# ==================================================
# Line: 2284

result_var = self.cse.generate(load_buffer, line, dtype=dtype)

# ==================================================
# Line: 2296

result_var = self.cse.generate(load_buffer, line, dtype=dtype)

# ==================================================
# Line: 2473

dense_size_str = self.dense_size_str()

# ==================================================
# Line: 2497

value = self.reduction_collapse_dims(buffer, value, dtype)

# ==================================================
# Line: 2525

value = self.reduction_collapse_dims(buffer, value, dtype)

# ==================================================
# Line: 2539

torch_acc_type = upcast_acc_dtype(src_dtype)

# ==================================================
# Line: 2553

default = self._map_tuple_or_scalar(constant_repr, default)

# ==================================================
# Line: 2587

result_var = self.welford_reduce(
    result_var, reduction_type, value, where_cond, acc_type, dtype
)

# ==================================================
# Occurrences: Lines 2617-2628 (5 instances)

default = ir.Reduction.default_accumulator(reduction_type, src_dtype)

# ==================================================
# Line: 2646

result_var = self.welford_reduce(
    result_var, reduction_type, value, where_cond, acc_type, dtype
)

# ==================================================
# Occurrences: Lines 2655-2658 (2 instances)

f"{accumulator_max} = tl.full({self.dense_size_str()}, float('-inf'), {acc_type})"

# ==================================================
# Line: 2722

default = ir.Reduction.default_accumulator(reduction_type, src_dtype)

# ==================================================
# Line: 2736

index_dtype = self.features.select_index_dtype()

# ==================================================
# Occurrences: Lines 2745-2751 (3 instances)

result_mean, upcast_acc_dtype(src_dtype), default[0]

# ==================================================
# Occurrences: Lines 2767-2770 (2 instances)

result_max, upcast_acc_dtype(src_dtype), default[0]

# ==================================================
# Line: 2783

result_var, upcast_acc_dtype(src_dtype), default

# ==================================================
# Occurrences: Lines 2898-2899 (2 instances)

result_m2 = self.cse.newvar(dtype=dtype)

# ==================================================
# Line: 3087

combine_helper_fn = self._lift_helper(combine_fn, len(values), dtypes)

# ==================================================
# Line: 3122

n = len(values)

# ==================================================
# Line: 3389

device = V.graph.get_current_device_or_throw()

# ==================================================
# Line: 3403

current_device = V.graph.get_current_device_or_throw()

# ==================================================
# Occurrences: Lines 4214-4218 (2 instances)

path = cache_file_path()

# ==================================================
# Line: 4250

ms = float("inf")

# ==================================================
# Line: 4260

ms = float("inf")

# ==================================================
# Line: 4384

path = cache_file_path()

# ==================================================
# Line: 4391

path = cache_file_path()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/memory_planning.py
# Occurrences: Lines 646-650 (4 instances)

name = line.node.get_name()

# ==================================================
# Occurrences: Lines 697-702 (4 instances)

line = worklist.popleft()

# ==================================================
# Line: 755

seen = OrderedSet[AllocationPool]()

# ==================================================
# Line: 765

seen = OrderedSet[AllocationPool]()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/common.py
# Line: 1588

dtype = V.graph.get_dtype(outer)

# ==================================================
# Line: 1596

dtype = V.graph.get_dtype(outer)

# ==================================================
# Line: 1604

dtype = V.graph.get_dtype(outer)

# ==================================================
# Occurrences: Lines 2490-2491 (2 instances)

new_bounds = ValueRanges.unknown()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_template.py
# Occurrences: Lines 56-61 (2 instances)

_, call_args, _, _ = kernel.args.python_argdefs()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/compile_fx.py
# Line: 774

start = time.time()

# ==================================================
# Line: 828

start_time = time.time_ns()

# ==================================================
# Line: 867

mb_compiled_graph = fx_codegen_and_compile(
    gm, example_inputs, inputs_to_check, **graph_kwargs
)

# ==================================================
# Occurrences: Lines 878-882 (2 instances)

mb_compiled_graph = fx_codegen_and_compile(
    gm, example_inputs, inputs_to_check, **graph_kwargs
)

# ==================================================
# Line: 971

log.debug("FX codegen and compilation took %.3fs", time.time() - start)

# ==================================================
# Line: 1278

or isinstance(node.meta.get("val", None), FakeScriptObject)

# ==================================================
# Line: 1437

meta_val = node.meta.get("val", None)

# ==================================================
# Line: 1675

model(list(static_inputs))

# ==================================================
# Line: 1683

static_outputs = model(list(static_inputs))

# ==================================================
# Line: 2084

+ f"\n\n # graph id: {id(model_.graph)}",

# ==================================================
# Line: 2096

torch._inductor.debug._pre_grad_graph_id = id(model_.graph)

# ==================================================
# Line: 2108

+ f"\n\n # graph id: {id(model_.graph)}",

# ==================================================
# Occurrences: Lines 2158-2163 (3 instances)

model_outputs_node = output_node(gm)

# ==================================================
# Occurrences: Lines 2282-2284 (2 instances)

model_outputs_node = output_node(gm)

# ==================================================
# Line: 2315

torch._guards.TracingContext.try_get()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/triton_helpers.py
# Occurrences: Lines 551-552 (2 instances)

left_valid_mask = tl.full(x.shape, True, tl.int1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/triton_heuristics.py
# Line: 203

and (len(configs) > 1 or inductor_meta.get("coordinate_descent_tuning"))

# ==================================================
# Occurrences: Lines 219-231 (5 instances)

autotune_cache_info["num_configs"] = len(configs)

# ==================================================
# Occurrences: Lines 959-961 (2 instances)

start_time = time.time_ns()

# ==================================================
# Occurrences: Lines 1079-1083 (2 instances)

start_time = time.time_ns()

# ==================================================
# Occurrences: Lines 1128-1130 (2 instances)

start_time = time.time_ns()

# ==================================================
# Occurrences: Lines 1772-1774 (2 instances)

start_time = time.time_ns()

# ==================================================
# Line: 2005

target = conditional_product(x, y, z)

# ==================================================
# Line: 2019

x * maxGridSize[0] < size_hints["x"] or conditional_product(x, y, z) < target

# ==================================================
# Line: 2027

or conditional_product(x, y, z) < target

# ==================================================
# Line: 2036

or conditional_product(x, y, z) < target

# ==================================================
# Line: 2042

conditional_product(x, y, z) // num_elements_per_warp, min_num_warps=1

# ==================================================
# Line: 2050

if conditional_product(x, y, z) >= 128 and not torch.version.hip:

# ==================================================
# Occurrences: Lines 2058-2061 (2 instances)

conditional_product(x, y, z),

# ==================================================
# Occurrences: Lines 2136-2148 (5 instances)

target = total_numel()

# ==================================================
# Occurrences: Lines 2155-2156 (2 instances)

for prefix in sorted(rnumels):

# ==================================================
# Occurrences: Lines 2193-2207 (5 instances)

target = total_numel()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/benchmarking.py
# Occurrences: Lines 119-123 (8 instances)

run_start_t = time.perf_counter()

# ==================================================
# Line: 258

estimated_timing = self.get_event_pairs_min_timing(event_pairs)

# ==================================================
# Line: 277

benchmarked_timing = self.get_event_pairs_min_timing(event_pairs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/compile_tasks.py
# Occurrences: Lines 60-63 (2 instances)

start_ns = time.time_ns()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/constant_folding.py
# Line: 91

self.unknown_value = object()

# ==================================================
# Line: 98

self.deferred_value = object()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/select_algorithm.py
# Occurrences: Lines 411-413 (6 instances)

pre_state = self.input_dependent_preserved_state()

# ==================================================
# Line: 1874

out_new = algo(*args)

# ==================================================
# Line: 1880

return do_bench_using_profiling(lambda: algo(*args))

# ==================================================
# Line: 2195

return choices[0].output_node()

# ==================================================
# Occurrences: Lines 2228-2228 (2 instances)

precompile_start_ts = time.time()

# ==================================================
# Occurrences: Lines 2235-2240 (4 instances)

precompile_elapse = time.time() - precompile_start_ts

# ==================================================
# Occurrences: Lines 2248-2251 (4 instances)

prescreening_elapse = time.time() - prescreening_start_ts

# ==================================================
# Occurrences: Lines 2259-2259 (2 instances)

autotune_elapse = time.time() - autotune_start_ts

# ==================================================
# Line: 2314

timings = do_autotuning(choices, precompile_fn)

# ==================================================
# Line: 2349

timings = do_autotuning(choices, precompile_fn)

# ==================================================
# Line: 2360

node = choice.output_node()

# ==================================================
# Line: 2366

node = choices[0].output_node()

# ==================================================
# Line: 2375

node = choice.output_node()

# ==================================================
# Occurrences: Lines 2451-2454 (4 instances)

start_ns = time.time_ns()

# ==================================================
# Occurrences: Lines 2644-2647 (4 instances)

timing = float("inf")

# ==================================================
# Occurrences: Lines 2669-2669 (2 instances)

timing = float("inf")

# ==================================================
# Occurrences: Lines 2680-2680 (2 instances)

timing = float("inf")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/scheduler.py
# Occurrences: Lines 561-570 (9 instances)

V.kernel.args.make_inplace(input_buf.get_name(), buf.get_name())

# ==================================================
# Occurrences: Lines 855-859 (2 instances)

return self.get_read_write_buffers_sizes() / gpu_memory_bandwidth

# ==================================================
# Occurrences: Lines 955-960 (2 instances)

op_name = name_to_buf[dep.name].defining_op_name()

# ==================================================
# Occurrences: Lines 1567-1568 (2 instances)

producer = typing.cast(ForeachKernelSchedulerNode, producer)

# ==================================================
# Line: 1583

consumer = typing.cast(ForeachKernelSchedulerNode, consumer)

# ==================================================
# Line: 1598

producer = typing.cast(ForeachKernelSchedulerNode, producer)

# ==================================================
# Occurrences: Lines 1616-1620 (2 instances)

producer = typing.cast(ForeachKernelSchedulerNode, producer)

# ==================================================
# Occurrences: Lines 1627-1628 (2 instances)

producer = typing.cast(ForeachKernelSchedulerNode, producer)

# ==================================================
# Line: 1634

producer = typing.cast(ForeachKernelSchedulerNode, producer)

# ==================================================
# Line: 1648

consumer = typing.cast(ForeachKernelSchedulerNode, consumer)

# ==================================================
# Occurrences: Lines 2088-2099 (4 instances)

self.nodes = self.topological_sort_schedule(self.nodes)

# ==================================================
# Line: 2147

"num_nodes_after_fusion": len(self.nodes),

# ==================================================
# Occurrences: Lines 2345-2345 (2 instances)

unbacked_symbol_to_origin_node[s] = node.get_name()

# ==================================================
# Occurrences: Lines 2357-2357 (2 instances)

node.add_fake_dep(StarDep(buf.get_name()))

# ==================================================
# Occurrences: Lines 2373-2378 (4 instances)

alt_name = rename(alt_name)

# ==================================================
# Occurrences: Lines 2386-2386 (2 instances)

WeakDep(other_name, mutating_buf=buf.get_name())

# ==================================================
# Occurrences: Lines 2400-2402 (14 instances)

self.mutation_renames[rename(alt_name)] = buf.get_name()

# ==================================================
# Line: 2443

buf.set_users(name_to_users[buf.get_name()].items)

# ==================================================
# Occurrences: Lines 2617-2617 (2 instances)

old_len = len(nodes)

# ==================================================
# Occurrences: Lines 2624-2624 (2 instances)

new_len = len(nodes)

# ==================================================
# Line: 2939

future_choices.append((choice, *compile_kernel(node_list_fused)))

# ==================================================
# Line: 2989

future_and_mod_l1_fused = compile_kernel(node_list_fused)

# ==================================================
# Occurrences: Lines 3106-3111 (4 instances)

self.get_fused_node(node1) in pending_fusions

# ==================================================
# Occurrences: Lines 3132-3133 (2 instances)

node1 = self.get_fused_node(node1)

# ==================================================
# Line: 3175

num_nodes_orig = len(self.nodes)

# ==================================================
# Line: 3213

len(self.nodes),

# ==================================================
# Line: 3250

buffer_names_grouping = collections.defaultdict(list)

# ==================================================
# Line: 3260

group_grouping = collections.defaultdict(list)

# ==================================================
# Line: 3623

node1.get_device()

# ==================================================
# Line: 3721

device = node1.get_device()

# ==================================================
# Line: 3850

read_name = self.mutation_renames.get(read.name, read.name)

# ==================================================
# Line: 3872

read_name = self.mutation_renames.get(read.name, read.name)

# ==================================================
# Occurrences: Lines 3940-3941 (4 instances)

assert node1.get_device() == node2.get_device()

# ==================================================
# Occurrences: Lines 4709-4709 (2 instances)

if device := node.get_device():

# ==================================================
# Occurrences: Lines 4762-4762 (2 instances)

device = node.get_device()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/lowering.py
# Occurrences: Lines 602-606 (6 instances)

return override_fn_when_input_bool(*[load(index) for load in loaders])

# ==================================================
# Occurrences: Lines 624-625 (6 instances)

if is_gpu(i.get_device().type):

# ==================================================
# Occurrences: Lines 932-936 (2 instances)

broadcast_symbolic_shapes, [x.get_size() for x in inputs], []

# ==================================================
# Line: 1611

fusable_reduction = any(can_fuse_reduction(t) for t in inputs)

# ==================================================
# Line: 1678

) and not any(can_fuse_reduction(t) for t in inputs)

# ==================================================
# Line: 1688

num_dims = len(original_shape)

# ==================================================
# Line: 1723

original_idx = [0] * len(original_shape)

# ==================================================
# Line: 1734

assert cur_dim == len(original_shape) - 2

# ==================================================
# Line: 2301

val = values_loader(idx)

# ==================================================
# Line: 2315

val = values_loader(idx)

# ==================================================
# Occurrences: Lines 2541-2541 (2 instances)

and arg.maybe_get_stride() is not None

# ==================================================
# Occurrences: Lines 2554-2554 (2 instances)

maybe_stride = arg.maybe_get_stride()

# ==================================================
# Occurrences: Lines 2593-2593 (2 instances)

and arg.maybe_get_stride() is not None

# ==================================================
# Line: 3676

for _ in range(len(mask.get_size()), len(self.get_size())):

# ==================================================
# Occurrences: Lines 3682-3689 (3 instances)

return index_put_fallback(self, indices, values, accumulate)

# ==================================================
# Occurrences: Lines 3695-3698 (3 instances)

self = view(self, [1])

# ==================================================
# Line: 3709

return index_put_fallback(self, indices, values, accumulate)

# ==================================================
# Line: 3718

self = view(self, [1])

# ==================================================
# Line: 3755

self = view(self, [])

# ==================================================
# Occurrences: Lines 3778-3780 (4 instances)

mask_val = ops.to_dtype(mask_loader(idx), torch.bool)

# ==================================================
# Line: 3915

ndim = len(self.get_size())

# ==================================================
# Line: 3936

shape = self.get_size()

# ==================================================
# Line: 3974

buffer.name = V.graph.register_buffer(buffer)

# ==================================================
# Line: 3993

buffer.name = V.graph.register_buffer(buffer)

# ==================================================
# Line: 4632

assert len(x.get_size()) in (3, 4)

# ==================================================
# Occurrences: Lines 4663-4668 (2 instances)

*_batch, _height, width = x.get_size()

# ==================================================
# Line: 4899

if x.get_dtype() == torch.int64:

# ==================================================
# Line: 4919

return empty(o_size, dtype=x.get_dtype(), device=x.get_device())

# ==================================================
# Line: 4928

dtype = x.get_dtype()

# ==================================================
# Line: 4974

if x.get_dtype() == torch.int64:

# ==================================================
# Line: 4990

return empty(o_size, dtype=x.get_dtype(), device=x.get_device()), empty(

# ==================================================
# Line: 5002

dtype = x.get_dtype()

# ==================================================
# Occurrences: Lines 5400-5404 (2 instances)

assert len(x.get_size()) in (3, 4)

# ==================================================
# Line: 5416

new_size = list(x.get_size())

# ==================================================
# Occurrences: Lines 5571-5575 (2 instances)

assert len(x.get_size()) in (4, 5)

# ==================================================
# Line: 5591

new_size = list(x.get_size())

# ==================================================
# Occurrences: Lines 5857-5862 (2 instances)

output_dtype = x.get_dtype()

# ==================================================
# Occurrences: Lines 5923-5928 (2 instances)

dtype=x.get_dtype(),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/mock_cache.py
# Occurrences: Lines 78-84 (7 instances)

self.autotune_local = _GlobalItemStats()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/cpp_builder.py
# Occurrences: Lines 369-372 (4 instances)

file_path = os.path.join(root, name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/mkldnn_ir.py
# Occurrences: Lines 56-57 (4 instances)

assert len(output_size) == len(weight_size), "Expect input dim == weight dim"

# ==================================================
# Line: 120

dims = len(x_fake.size()) - 2

# ==================================================
# Line: 138

input_size = x_fake.size()

# ==================================================
# Line: 235

*m, _ = x.get_size()

# ==================================================
# Line: 241

req_stride_order = list(reversed(range(len(x.get_size()))))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autoheuristic/autoheuristic.py
# Line: 196

metadata = self.serialize_metadata()

# ==================================================
# Line: 203

lines.append(self.serialize_metadata())

# ==================================================
# Line: 289

current_inputs_key = create_inputs_key(input_nodes)

# ==================================================
# Line: 300

inputs_key = create_inputs_key(input_nodes)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/cudagraph_trees.py
# Occurrences: Lines 1531-1532 (2 instances)

live_storage_data_ptrs = OrderedSet[Any]()

# ==================================================
# Occurrences: Lines 1927-1928 (2 instances)

self.graph_counter = itertools.count(0)

# ==================================================
# Line: 2069

node_id = self._get_node_id()

# ==================================================
# Line: 2138

if self.non_cudagraph_managed_mutation_hint[self._get_node_id()][

# ==================================================
# Line: 2147

curr_node_id = self._get_node_id()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/graph.py
# Occurrences: Lines 1594-1597 (2 instances)

result = super().run_node(n)

# ==================================================
# Occurrences: Lines 1623-1626 (2 instances)

strides = n.meta["val"].stride()

# ==================================================
# Line: 1642

strides = n.meta["val"].stride()

# ==================================================
# Line: 1674

ir.get_stride_order(strides),

# ==================================================
# Line: 1734

ir.get_stride_order(n.meta["val"].stride()),

# ==================================================
# Line: 2039

visited_grids[val] = len(grid_inputs)

# ==================================================
# Occurrences: Lines 2058-2058 (3 instances)

new_kwargs[k] = len(kwargs_inputs)

# ==================================================
# Occurrences: Lines 2065-2065 (3 instances)

visited_kwargs[v] = len(kwargs_inputs)

# ==================================================
# Occurrences: Lines 2080-2081 (2 instances)

if len(grid_inputs) > 0:

# ==================================================
# Line: 2099

self.autotuning_inputs = returned_outputs[: len(kwargs_inputs)]

# ==================================================
# Line: 2189

real_inputs = extract_real_inputs()

# ==================================================
# Line: 2197

real_inputs = extract_real_inputs()

# ==================================================
# Occurrences: Lines 2382-2383 (2 instances)

shape_counter = itertools.count(0)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/comms.py
# Occurrences: Lines 181-184 (2 instances)

MOVE_LIMIT = len(snodes) * 100

# ==================================================
# Occurrences: Lines 307-309 (4 instances)

name_to_fused_node[snode.get_name()] = snode

# ==================================================
# Line: 317

scores_0[snode.get_name()] = comm_idx

# ==================================================
# Line: 323

scores_1[snode.get_name()] = 1

# ==================================================
# Occurrences: Lines 449-454 (2 instances)

snodes = snode.get_nodes()

# ==================================================
# Occurrences: Lines 527-529 (2 instances)

peak_memory, _ = estimate_peak_memory(
    snodes, get_freeable_input_buf(snodes, graph_inputs), graph_outputs
)

# ==================================================
# Occurrences: Lines 538-540 (4 instances)

t0 = time.time()

# ==================================================
# Occurrences: Lines 549-551 (2 instances)

peak_memory, _ = estimate_peak_memory(
    snodes, get_freeable_input_buf(snodes, graph_inputs), graph_outputs
)

# ==================================================
# Occurrences: Lines 573-574 (2 instances)

graph_input_to_resized_to_full_node_idxes = defaultdict(list)

# ==================================================
# Line: 627

unsharded_param_to_fsdp_copy_node_idxes = defaultdict(list)

# ==================================================
# Occurrences: Lines 948-950 (4 instances)

end_idx_of_current_ag_block = len(ag_related_snodes)

# ==================================================
# Occurrences: Lines 964-964 (2 instances)

for i in range(len(ag_related_snodes) - 1):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/post_grad.py
# Occurrences: Lines 297-307 (6 instances)

loop_idx, _, _, _ = pytree.tree_unflatten(
    flat_args,
    operands_and_additional_inputs_spec,
)

# ==================================================
# Occurrences: Lines 500-509 (6 instances)

loop_idx, _, _, _, _ = pytree.tree_unflatten(
    flat_args, operands_and_additional_inputs_spec
)  # type: ignore[has-type]

# ==================================================
# Occurrences: Lines 1016-1021 (3 instances)

input_storages = OrderedSet[Union[int, None]]()

# ==================================================
# Line: 1045

node_storage = get_node_storage(node)

# ==================================================
# Line: 1160

flat_args, spec = pytree.tree_flatten((args, kwargs))

# ==================================================
# Line: 1166

args, kwargs = pytree.tree_unflatten(flat_args, spec)

# ==================================================
# Line: 1186

flat_args, spec = pytree.tree_flatten((args, kwargs))

# ==================================================
# Line: 1195

const_attr = getattr(graph.owning_module, node.target)  # type: ignore[arg-type]

# ==================================================
# Line: 1208

args, kwargs = pytree.tree_unflatten(flat_args, spec)

# ==================================================
# Line: 1226

getattr(graph.owning_module, node.target), torch.fx.GraphModule

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/reinplace.py
# Line: 256

node_to_view_base[node] = node_to_view_base.get(inp, inp)  # type: ignore[arg-type]

# ==================================================
# Line: 281

inp_base = node_to_view_base.get(inp, inp)  # type: ignore[arg-type]

# ==================================================
# Line: 607

copy_node = copy_args_to_copy_nodes.get((mutated_arg, node))

# ==================================================
# Line: 648

copy_node = copy_args_to_copy_nodes.get((mutated_arg, node))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/freezing_patterns.py
# Line: 163

cat_t = torch.cat((w1, w2, w3), dim=1)

# ==================================================
# Line: 203

cat_w = torch.cat((w1, w2, w3), dim=1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/efficient_conv_bn_eval.py
# Line: 44

bias_on_the_fly = torch.zeros_like(bn.running_var)

# ==================================================
# Line: 54

bn_bias = torch.zeros_like(bn.running_var)

# ==================================================
# Line: 109

bias_on_the_fly = torch.zeros_like(bn_running_var)

# ==================================================
# Line: 119

bn_bias = torch.zeros_like(bn_running_var)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/b2b_gemm.py
# Occurrences: Lines 614-615 (4 instances)

while next(iter(f_node.users)) is not outer_mm:

# ==================================================
# Line: 698

new_input_node = new_graph.placeholder(name="subgraph_input")

# ==================================================
# Line: 708

new_input_node = new_graph.placeholder(name="subgraph_input")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/quantization.py
# Line: 1607

output_reshape_node = match.output_node()

# ==================================================
# Line: 1615

linear_node = match.output_node()

# ==================================================
# Line: 2165

linear_weight_prepack_cases = itertools.product(
    [torch.float32, torch.bfloat16], [True, False], [True, False]
)

# ==================================================
# Line: 2190

for dtype, with_bias, is_tensor_overload in itertools.product(
    [torch.float32, torch.bfloat16], [True, False], [True, False]
):

# ==================================================
# Occurrences: Lines 2270-2270 (2 instances)

relu_node = match.output_node()

# ==================================================
# Occurrences: Lines 2286-2286 (2 instances)

output_reshape_node = next(iter(linear_node.users))

# ==================================================
# Occurrences: Lines 2294-2294 (2 instances)

add_bias_node = next(iter(linear_node.users))

# ==================================================
# Occurrences: Lines 2341-2341 (2 instances)

out_node = match.output_node()

# ==================================================
# Occurrences: Lines 2642-2651 (6 instances)

new_out_node = match.graph.call_function(
    aten.reshape.default,
    args=(new_out_node, out_shape),  # type: ignore[possibly-undefined]
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/mkldnn_fusion.py
# Occurrences: Lines 359-362 (4 instances)

return L[computation_op](*computation_args)

# ==================================================
# Occurrences: Lines 409-411 (4 instances)

return L[computation_op](*computation_args)

# ==================================================
# Line: 893

reshape_2_node = match.output_node()

# ==================================================
# Line: 924

add_node = match.output_node()

# ==================================================
# Line: 962

add_node = match.output_node()

# ==================================================
# Line: 1180

conv_node = match.output_node()

# ==================================================
# Line: 1194

packed_weight_node = graph.create_node(
    "call_function", packed_weight_op, args=packed_weight_inputs
)

# ==================================================
# Line: 1226

lstm_node = match.output_node()

# ==================================================
# Line: 1290

linear_node = match.output_node()

# ==================================================
# Line: 1337

packed_weight_node = graph.create_node(
    "call_function", packed_weight_op, args=packed_weight_inputs
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/group_batch_fusion.py
# Line: 838

batch_layer_norm = graph.call_function(  # type: ignore[operator]
    torch.mul, args=(stack_weight, batch_layer_norm)
)

# ==================================================
# Line: 848

batch_layer_norm = graph.call_function(  # type: ignore[operator]
    torch.add, args=(stack_bias, batch_layer_norm)
)

# ==================================================
# Line: 859

batch_layer_norm = graph.call_function(
    torch.mul, args=(stack_weight, batch_layer_norm)
)

# ==================================================
# Line: 870

batch_layer_norm = graph.call_function(
    torch.add, args=(stack_bias, batch_layer_norm)
)

# ==================================================
# Occurrences: Lines 1231-1232 (4 instances)

visited_node_set = OrderedSet[torch.fx.Node]()

# ==================================================
# Line: 1258

subset_deps = OrderedSet[torch.fx.Node]()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/joint_graph.py
# Line: 311

out = super(ConstantFolder, self).run_node(node)

# ==================================================
# Line: 317

return super(ConstantFolder, self).run_node(node)

# ==================================================
# Line: 325

args, kwargs = self.fetch_args_kwargs_from_env(node)

# ==================================================
# Line: 334

return super(ConstantFolder, self).run_node(node)

# ==================================================
# Line: 356

args, kwargs = self.fetch_args_kwargs_from_env(node)

# ==================================================
# Occurrences: Lines 394-395 (2 instances)

zeros = OrderedSet[Any]()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/pad_mm.py
# Occurrences: Lines 423-432 (6 instances)

k_padded_length = get_padded_length(k, get_alignment_size(mat1))

# ==================================================
# Occurrences: Lines 867-871 (4 instances)

dim2a = functools.partial(torch.empty, (4, 4), device=device, requires_grad=True)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/numeric_utils.py
# Occurrences: Lines 144-144 (2 instances)

res = compare_parameters(model_base, model_control, precision)

# ==================================================
# Occurrences: Lines 171-171 (2 instances)

res = compare_parameters(model_base, model_control, precision)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/binary_folding.py
# Line: 194

weight_meta_value = conv_node.args[1].meta.get("val")

# ==================================================
# Line: 202

other_meta_value = other.meta.get("val")

# ==================================================
# Line: 248

weight_meta_value = weight_node.meta.get("val")

# ==================================================
# Line: 256

other_meta_value = other.meta.get("val")

# ==================================================
# Line: 282

binary_node = match.output_node()

# ==================================================
# Occurrences: Lines 321-326 (3 instances)

res = graph.create_node(
    "call_function",
    aten.expand.default,
    (res, shape),
)

# ==================================================
# Occurrences: Lines 333-337 (2 instances)

res = graph.create_node(
    "call_function",
    aten.expand.default,
    (res, shape),
)

# ==================================================
# Occurrences: Lines 349-355 (5 instances)

weight_meta_value = conv_node.args[1].meta.get("val")

# ==================================================
# Occurrences: Lines 367-373 (3 instances)

weight_broadcast_shape[0] = weight_meta_value.size(0)

# ==================================================
# Occurrences: Lines 380-383 (4 instances)

other_reshape = resize_scalar_or_tensor_to_shape(
    graph,
    other,
    (weight_meta_value.size(0),),
    weight_meta_value,
)

# ==================================================
# Occurrences: Lines 408-415 (3 instances)

weight_meta_value = weight_node.meta.get("val")

# ==================================================
# Line: 429

other_reshape1 = resize_scalar_or_tensor_to_shape(
    graph,
    other,
    tuple(weight_broadcast_shape),
    weight_meta_value,
)

# ==================================================
# Occurrences: Lines 440-445 (2 instances)

other_reshape = resize_scalar_or_tensor_to_shape(
    graph,
    other,
    (weight_meta_value.size(1),),
    weight_meta_value,
)

# ==================================================
# Line: 471

binary_node = match.output_node()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/micro_pipeline_tp.py
# Line: 101

zero_dim_all_gather_pattern = make_zero_dim_all_gather_pattern(KeywordArg("shard"))

# ==================================================
# Line: 131

make_zero_dim_all_gather_pattern(
    KeywordArg("shard"),
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/split_cat.py
# Occurrences: Lines 1015-1021 (4 instances)

stacked_input = graph.call_function(
    torch.stack, args=(to_stack,), kwargs={"dim": stack_dim}
)

# ==================================================
# Occurrences: Lines 1066-1072 (4 instances)

stacked_input = graph.call_function(
    torch.stack, args=(to_stack,), kwargs={"dim": stack_dim}
)

# ==================================================
# Occurrences: Lines 1154-1158 (2 instances)

if not is_sorted_and_consecutive(getitem_indices) or len(  # type: ignore[arg-type]
    getitem_indices
) != len(unbind_node.meta["example_value"]):

# ==================================================
# Occurrences: Lines 1789-1790 (4 instances)

parent_to_indices = defaultdict(list)  # type: ignore[var-annotated]

# ==================================================
# Occurrences: Lines 2816-2823 (4 instances)

decomposed_stack_node = graph.call_function(
    torch.stack,
    args=(stack_node_input,),
    kwargs={"dim": stack_dim},
)

# ==================================================
# Occurrences: Lines 2847-2854 (4 instances)

decomposed_stack_node = graph.call_function(
    torch.stack,
    args=(stack_node_input,),
    kwargs={"dim": stack_dim},
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/ddp_fusion.py
# Line: 206

args, kwargs = tree_unflatten(flatten_args, spec)

# ==================================================
# Line: 213

args, kwargs = tree_unflatten(flatten_args, spec)

# ==================================================
# Line: 255

args, kwargs = tree_unflatten(flatten_args, spec)

# ==================================================
# Line: 269

args, kwargs = tree_unflatten(flatten_args, spec)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/pre_grad.py
# Line: 233

pass_name, pass_func = _get_pass_name_func(p)

# ==================================================
# Line: 247

pass_name, pass_func = _get_pass_name_func(p)

# ==================================================
# Line: 290

gm_before_fx_passes = gm.__copy__()

# ==================================================
# Line: 351

gm_after_fx_passes = gm.__copy__()

# ==================================================
# Line: 484

hash_id = hash(node.args[0].target)

# ==================================================
# Line: 544

hash_id = hash(node.args[0].target)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/compiler_bisector.py
# Occurrences: Lines 247-249 (4 instances)

low = int(line.strip().split("=")[1])

# ==================================================
# Line: 327

counter = cls.get_system_counter(subsystem, increment=True)

# ==================================================
# Line: 340

cls.get_system_counter(subsystem, increment=True),

# ==================================================
# Occurrences: Lines 447-451 (4 instances)

_, high = cls.get_bisect_range(curr_backend, curr_subsystem.name)

# ==================================================
# Occurrences: Lines 464-464 (2 instances)

low, high = cls.get_bisect_range(curr_backend, curr_subsystem.name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/choices.py
# Occurrences: Lines 240-241 (2 instances)

divisors = sympy.divisors(reduction_numel_hint)

# ==================================================
# Occurrences: Lines 248-249 (2 instances)

divisors = sympy.divisors(reduction_numel_hint)

# ==================================================
# Occurrences: Lines 272-273 (2 instances)

divisors = sympy.divisors(reduction_numel_hint)

# ==================================================
# Occurrences: Lines 279-280 (2 instances)

divisors = sympy.divisors(reduction_numel_hint)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/mkldnn_lowerings.py
# Occurrences: Lines 58-70 (4 instances)

weight_compens_tensor = torch.sum(W_tensor.to(torch.float), dim=0)

# ==================================================
# Occurrences: Lines 337-346 (5 instances)

x_size = x.get_size()

# ==================================================
# Line: 390

result = view(result, (*x_size[:-1], result.get_size()[-1]))

# ==================================================
# Occurrences: Lines 397-408 (4 instances)

x_size = x.get_size()

# ==================================================
# Line: 452

result = view(result, (*x_size[:-1], result.get_size()[-1]))

# ==================================================
# Occurrences: Lines 548-554 (2 instances)

x_scale = V.graph.add_tensor_constant(
    torch.tensor(x_scale, dtype=torch.float32), name="x_scale"
)

# ==================================================
# Occurrences: Lines 610-616 (2 instances)

x_scale = V.graph.add_tensor_constant(
    torch.tensor(x_scale, dtype=torch.float32), name="x_scale"
)

# ==================================================
# Occurrences: Lines 676-684 (3 instances)

x_size = x.get_size()

# ==================================================
# Line: 691

x_scale = view(x_scale, [])

# ==================================================
# Occurrences: Lines 699-706 (2 instances)

x_zp = V.graph.add_tensor_constant(
    torch.tensor(0, dtype=torch.int32), name="x_zp"
)

# ==================================================
# Line: 719

w_zp = V.graph.add_tensor_constant(
    torch.tensor(0, dtype=torch.int32), name="w_zp"
)

# ==================================================
# Occurrences: Lines 729-732 (2 instances)

w_zp_tensor = V.graph.constants[w_zp.get_name()].to(torch.int32)

# ==================================================
# Line: 759

) = create_int8_compensation(
    W_tensor,
    packed_weight,
    x_scale,
    x_zp,
    w_scale,
)

# ==================================================
# Occurrences: Lines 775-794 (9 instances)

input_loader = input_buffer.make_loader()

# ==================================================
# Occurrences: Lines 801-835 (10 instances)

_x_scale = x_scale_loader(())

# ==================================================
# Occurrences: Lines 845-876 (13 instances)

output_cast_loader = output_buf.make_loader()

# ==================================================
# Line: 954

result = view(result, (*x_size[:-1], result.get_size()[-1]))

# ==================================================
# Occurrences: Lines 984-995 (3 instances)

x_size = x.get_size()

# ==================================================
# Occurrences: Lines 1002-1019 (4 instances)

x_scale = view(x_scale, [])

# ==================================================
# Occurrences: Lines 1032-1041 (6 instances)

w_zp_tensor = V.graph.constants[w_zp.get_name()].to(torch.int32)

# ==================================================
# Occurrences: Lines 1048-1051 (4 instances)

assert x2.get_dtype() == output_dtype, (

# ==================================================
# Line: 1082

) = create_int8_compensation(
    W_tensor,
    packed_weight,
    x_scale,
    x_zp,
    w_scale,
)

# ==================================================
# Occurrences: Lines 1099-1116 (8 instances)

input_loader = input_buffer.make_loader()

# ==================================================
# Occurrences: Lines 1123-1150 (10 instances)

_x_scale = x_scale_loader(())

# ==================================================
# Line: 1161

output_buf = ir.Pointwise(
    device=input_buffer.get_device(),
    dtype=torch.float32,  # Hardcode to FP32 for u8s8f32
    inner_fn=inner_fn,
    ranges=input_buffer.get_size(),
)

# ==================================================
# Occurrences: Lines 1179-1210 (13 instances)

output_cast_loader = output_buf.make_loader()

# ==================================================
# Line: 1282

result = view(result, (*x_size[:-1], result.get_size()[-1]))

# ==================================================
# Line: 1307

*_, layout, x, transposed_w = mm_args(
    x, transposed_w, layout=layout
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/async_compile.py
# Line: 319

return load_kernel()

# ==================================================
# Occurrences: Lines 397-399 (2 instances)

start_ns = time_ns()

# ==================================================
# Line: 405

elapsed_us = (time_ns() - start_ns) // 1000

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/package/package.py
# Line: 33

compile_flags = json.load(f)

# ==================================================
# Line: 48

linker_flags = json.load(f)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autotune_process.py
# Occurrences: Lines 111-112 (2 instances)

subproc_read_fd, write_fd = os.pipe()

# ==================================================
# Line: 455

start_ts = time.time()

# ==================================================
# Occurrences: Lines 464-465 (2 instances)

create_tensor_elapse = time.time() - start_ts  # type: ignore[possibly-undefined]

# ==================================================
# Occurrences: Lines 474-480 (3 instances)

load_elapse = time.time() - start_ts  # type: ignore[possibly-undefined]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_logging/_internal.py
# Line: 1007

log = logging.getLogger(log_qname)

# ==================================================
# Occurrences: Lines 1013-1018 (2 instances)

log = logging.getLogger(log_qname)

# ==================================================
# Line: 1254

start_time = time.time_ns()

# ==================================================
# Line: 1311

structured_logging_overhead_s = (time.time_ns() - start_time) / 1e9

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/__init__.py
# Line: 823

socket_handles = amdsmi.amdsmi_get_processor_handles()

# ==================================================
# Line: 831

handler = amdsmi.amdsmi_get_processor_handles()[idx]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/_memory_viz.py
# Occurrences: Lines 355-355 (3 instances)

n = _name()

# ==================================================
# Occurrences: Lines 367-372 (6 instances)

name, _, _ = allocation_addr_to_name.get(addr, (addr, None, None))

# ==================================================
# Occurrences: Lines 379-379 (3 instances)

name = _name()

# ==================================================
# Line: 506

device = to_device(tensor_key.device)

# ==================================================
# Occurrences: Lines 552-554 (2 instances)

free(kv_to_elem.pop((tensor_key, version)), to_device(tensor_key.device))

# ==================================================
# Line: 565

(to_device(tensor_key.device), event["addr"], event["size"], event["frames"])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/_utils.py
# Line: 211

log_size = ctypes.c_size_t()

# ==================================================
# Line: 218

ptx_size = ctypes.c_size_t()

# ==================================================
# Line: 374

module = ctypes.c_void_p()

# ==================================================
# Line: 386

func = ctypes.c_void_p()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/graphs.py
# Line: 323

outputs = torch.utils._pytree.tree_leaves(func(*args))

# ==================================================
# Line: 351

outputs = func(*args)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/tunable.py
# Line: 578

underscore_count = untuned_gemm[0].count("_")

# ==================================================
# Line: 588

[op_sig, data_type, layout] = untuned_gemm[0].split("_")

# ==================================================
# Occurrences: Lines 599-601 (2 instances)

count = untuned_gemm[0].count("_")

# ==================================================
# Line: 650

matA, matB = _create_matrices(
    m, n, k, lda, ldb, ldc, transA, transB, dtype, deviceid, subMatrix=subMatrix
)

# ==================================================
# Line: 757

X, matA = _create_matrices(
    m, n, k, lda, ldb, ldc, transA, transB, dtype, deviceid, subMatrix=subMatrix
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/hipify/hipify_python.py
# Occurrences: Lines 345-347 (6 instances)

while string.find("<<<", kernel_end) != -1:

# ==================================================
# Occurrences: Lines 868-873 (2 instances)

output_source = RE_PYTORCH_PREPROCESSOR.sub(pt_repl, output_source)

# ==================================================
# Occurrences: Lines 882-882 (3 instances)

f = m.group(1)

# ==================================================
# Occurrences: Lines 894-894 (3 instances)

return templ.format(get_hip_file_path(m.group(1), is_pytorch_extension))

# ==================================================
# Occurrences: Lines 901-902 (4 instances)

header_dir_to_check = os.path.dirname(fin_path)

# ==================================================
# Occurrences: Lines 910-910 (3 instances)

header_path_to_check = os.path.abspath(os.path.join(header_dir_to_check, f))

# ==================================================
# Line: 969

and os.path.dirname(fin_path) == os.path.dirname(fout_path)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/jit/log_extract.py
# Occurrences: Lines 68-71 (2 instances)

s = time.perf_counter()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/__init__.py
# Occurrences: Lines 75-75 (2 instances)

use_count = t._use_count()

# ==================================================
# Occurrences: Lines 84-84 (2 instances)

if t._use_count() == 2:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_sympy/printers.py
# Occurrences: Lines 68-69 (2 instances)

assert exp == int(exp), exp

# ==================================================
# Line: 375

base = self._print(base)

# ==================================================
# Line: 388

r = "1.0/" + self._print(base)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_sympy/interp.py
# Line: 148

return getattr(analysis, handler_name)(*args, index_dtype)

# ==================================================
# Line: 160

handler = getattr(analysis, handler_name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/viz/_cycles.py
# Occurrences: Lines 55-57 (6 instances)

before = torch.cuda.memory_allocated()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_pytree.py
# Occurrences: Lines 1127-1127 (2 instances)

children, context = flatten_fn(tree)

# ==================================================
# Occurrences: Lines 1179-1179 (2 instances)

children, context = flatten_fn(tree)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_content_store.py
# Occurrences: Lines 73-79 (2 instances)

a = torch.randint(
    -(2**31), 2**31, x.shape, device=x.device, dtype=torch.int32
).abs()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/tensorboard/_utils.py
# Line: 112

tensor_NCHW = tensor.transpose(index)

# ==================================================
# Line: 118

tensor_HWC = tensor.transpose(index)

# ==================================================
# Line: 125

tensor = tensor.transpose(index)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/file_baton.py
# Occurrences: Lines 48-53 (2 instances)

start_time = time.time()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/dataloader.py
# Line: 1134

self._worker_result_queue = multiprocessing_context.Queue()  # type: ignore[var-annotated]

# ==================================================
# Line: 1143

index_queue = multiprocessing_context.Queue()  # type: ignore[var-annotated]

# ==================================================
# Line: 1445

success, data = self._try_get_data()

# ==================================================
# Line: 1455

success, data = self._try_get_data()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/dataset.py
# Line: 265

items = dataset.__getitems__(indices)  # type: ignore[attr-defined]

# ==================================================
# Line: 282

items = dataset.__getitems__(indices)  # type: ignore[attr-defined]

# ==================================================
# Occurrences: Lines 452-452 (2 instances)

if math.isclose(sum(lengths), 1) and sum(lengths) <= 1:

# ==================================================
# Occurrences: Lines 475-480 (2 instances)

if sum(lengths) != len(dataset):  # type: ignore[arg-type]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/_utils/worker.py
# Line: 274

dataset = apply_random_seed(dataset, shared_rng)

# ==================================================
# Line: 289

fetcher = _DatasetKind.create_fetcher(
    dataset_kind, dataset, auto_collation, collate_fn, drop_last
)

# ==================================================
# Occurrences: Lines 326-331 (2 instances)

dataset = apply_random_seed(dataset, shared_rng)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/_utils/collate.py
# Line: 77

clone = copy.copy(data)

# ==================================================
# Occurrences: Lines 87-89 (2 instances)

return elem_type(*(default_convert(d) for d in data))

# ==================================================
# Occurrences: Lines 98-107 (4 instances)

clone = copy.copy(data)  # type: ignore[arg-type]

# ==================================================
# Line: 169

clone = copy.copy(elem)

# ==================================================
# Line: 198

collate(samples, collate_fn_map=collate_fn_map)

# ==================================================
# Line: 212

collate(samples, collate_fn_map=collate_fn_map)

# ==================================================
# Occurrences: Lines 221-228 (3 instances)

clone = copy.copy(elem)  # type: ignore[arg-type]

# ==================================================
# Line: 236

collate(samples, collate_fn_map=collate_fn_map)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/_utils/pin_memory.py
# Line: 75

clone = copy.copy(data)

# ==================================================
# Line: 98

clone = copy.copy(data)  # type: ignore[arg-type]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/_utils/fetch.py
# Line: 33

data.append(next(self.dataset_iter))

# ==================================================
# Line: 42

data = next(self.dataset_iter)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/iter/callable.py
# Occurrences: Lines 95-98 (2 instances)

return self.fn(data)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/iter/grouping.py
# Occurrences: Lines 234-235 (4 instances)

if len(self.buffer_elements[findkey]) > biggest_size:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/iter/combinatorics.py
# Line: 138

idx = self._rng.randint(0, len(self._buffer) - 1)

# ==================================================
# Line: 144

idx = self._rng.randint(0, len(self._buffer) - 1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/_hook_iterator.py
# Line: 148

self._profiler_enabled = torch.autograd._profiler_enabled()

# ==================================================
# Line: 184

gen = func(*args, **kwargs)

# ==================================================
# Occurrences: Lines 195-204 (6 instances)

iterator_id = _set_datapipe_valid_iterator_id(
    datapipe
)  # This ID is tied to each created iterator

# ==================================================
# Occurrences: Lines 213-216 (6 instances)

response = gen.send(request)

# ==================================================
# Occurrences: Lines 247-251 (5 instances)

if torch.autograd._profiler_enabled():

# ==================================================
# Line: 265

iter_ret = func(*args, **kwargs)

# ==================================================
# Line: 272

iterator_id = _set_datapipe_valid_iterator_id(
    datapipe
)  # This ID is tied to each created iterator

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/_decorator.py
# Occurrences: Lines 203-205 (4 instances)

yield from f(self)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/utils/decoder.py
# Line: 207

result = np.asarray(img)

# ==================================================
# Line: 216

result = np.asarray(img)

# ==================================================
# Occurrences: Lines 222-225 (2 instances)

result = np.array(result.transpose(2, 0, 1))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/utils/common.py
# Line: 194

path = os.path.abspath(path)

# ==================================================
# Line: 201

path = os.path.abspath(path)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/dataframe/datapipes.py
# Occurrences: Lines 70-72 (4 instances)

size = df_wrapper.get_len(df)

# ==================================================
# Occurrences: Lines 97-98 (4 instances)

size = len(df.index)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/fuzzer.py
# Occurrences: Lines 284-286 (2 instances)

order = np.arange(dim)

# ==================================================
# Occurrences: Lines 426-429 (6 instances)

candidate_params[p.name] = p.sample(state)

# ==================================================
# Line: 448

alias_count = sum(isinstance(v, ParameterAlias) for v in params.values())

# ==================================================
# Line: 456

alias_count_new = sum(isinstance(v, ParameterAlias) for v in params.values())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/sparse_fuzzer.py
# Occurrences: Lines 96-97 (2 instances)

nnz = math.ceil(sum(size) * density)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/compile.py
# Line: 95

running_time = bench_loop(opt_model, sample_input, num_iters, optimizer, loss_fn)

# ==================================================
# Line: 110

running_time = bench_loop(opt_model, sample_input, num_iters, optimizer, loss_fn)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py
# Occurrences: Lines 460-460 (2 instances)

path = os.path.join(self._data_dir, f"{name}.pt")

# ==================================================
# Occurrences: Lines 468-468 (2 instances)

path = os.path.join(self._data_dir, f"{name}.pt")

# ==================================================
# Line: 593

script_file = os.path.join(working_dir, "timer_callgrind.py")

# ==================================================
# Line: 610

return invocation, f.read()

# ==================================================
# Line: 622

script_file = os.path.join(working_dir, "timer_callgrind.py")

# ==================================================
# Line: 664

error_report = f.read()

# ==================================================
# Line: 736

callgrind_out_contents = f.read()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/cpp_extension.py
# Line: 618

extension = next(extension_iter, None)

# ==================================================
# Line: 633

extension = next(extension_iter, None)

# ==================================================
# Occurrences: Lines 728-732 (2 instances)

cflags = copy.deepcopy(extra_postargs)

# ==================================================
# Line: 771

output_dir = os.path.abspath(output_dir)

# ==================================================
# Occurrences: Lines 777-782 (2 instances)

self.compiler._setup_compile(output_dir, macros,
                             include_dirs, sources,
                             depends, extra_postargs)

# ==================================================
# Line: 880

self.cflags = copy.deepcopy(extra_postargs)

# ==================================================
# Line: 910

nvcc = _join_cuda_home('bin', 'nvcc')

# ==================================================
# Line: 957

output_dir = os.path.abspath(output_dir)

# ==================================================
# Line: 968

self.compiler._setup_compile(output_dir, macros,
                             include_dirs, sources,
                             depends, extra_postargs)

# ==================================================
# Line: 986

with_cuda = any(map(_is_cuda_file, sources))

# ==================================================
# Line: 1534

lib_dir = os.path.join('lib', 'x64')

# ==================================================
# Line: 1549

lib_dir = os.path.join('lib', 'x64')

# ==================================================
# Occurrences: Lines 2562-2564 (2 instances)

vc_env = {k.upper(): v for k, v in _get_vc_env(plat_spec).items()}

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/checkpoint.py
# Line: 1284

return func(*args, **kwargs)

# ==================================================
# Line: 1298

out = func(*args, **kwargs)

# ==================================================
# Line: 1321

return func(*args, **kwargs)

# ==================================================
# Line: 1342

out = func(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_strobelight/cli_function_profiler.py
# Line: 265

return work_function(*args, **kwargs)

# ==================================================
# Line: 274

result = work_function(*args, **kwargs)

# ==================================================
# Line: 280

result = work_function(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/backend_registration.py
# Line: 97

return _get_current_device_index()

# ==================================================
# Line: 108

device_idx = _get_current_device_index()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_device.py
# Occurrences: Lines 85-90 (2 instances)

mode = _pop_mode()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/model_dump/__init__.py
# Occurrences: Lines 134-139 (2 instances)

storage_info = get_storage_info(storage)

# ==================================================
# Line: 229

raw = torch.utils.show_pickle.DumpUnpickler(handle, catch_invalid_utf8=True).load()

# ==================================================
# Occurrences: Lines 252-254 (4 instances)

raw_code = handle.read()

# ==================================================
# Line: 324

obj = torch.utils.show_pickle.DumpUnpickler(handle, catch_invalid_utf8=True).load()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_backport_slots.py
# Occurrences: Lines 96-100 (4 instances)

fields = dataclasses.fields(self)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/multiprocessing/reductions.py
# Line: 355

tensor_offset = tensor.storage_offset()

# ==================================================
# Line: 386

tensor.storage_offset(),

# ==================================================
# Line: 395

tensor.storage_offset(),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_ops.py
# Line: 393

result = handler(mode, *args, **kwargs)

# ==================================================
# Line: 463

return handler(mode, *args, **kwargs)

# ==================================================
# Line: 592

current_mode_stack_pre_dispatch = mode_stack_state_for_pre_dispatch()

# ==================================================
# Occurrences: Lines 603-611 (4 instances)

mode_stack_state_for_pre_dispatch().set(0, None)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/quantization/_quantized_conversions.py
# Line: 104

tmp = outp.view(-1).view(torch.int32)

# ==================================================
# Line: 110

tmp = outp.view(-1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/node.py
# Line: 177

items = ", ".join(
    _format_arg(a) for idx, a in enumerate(arg) if idx < max_list_len
)

# ==================================================
# Line: 185

items = ", ".join(
    _format_arg(a) for idx, a in enumerate(arg) if idx < max_list_len
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/_compatibility.py
# Line: 16

docstring = textwrap.dedent(getattr(fn, "__doc__", None) or "")

# ==================================================
# Line: 30

docstring = textwrap.dedent(getattr(fn, "__doc__", None) or "")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/_graph_pickler.py
# Occurrences: Lines 419-422 (2 instances)

root, detail = name.split(".", 1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py
# Line: 268

dim, counter = gen_dvar(counter)

# ==================================================
# Line: 331

dim_var, counter = gen_dvar(counter)

# ==================================================
# Occurrences: Lines 1173-1174 (4 instances)

new_dims_rhs_1, counter = gen_tensor_dims(i, counter)

# ==================================================
# Occurrences: Lines 1209-1215 (6 instances)

dims1, counter = gen_tensor_dims(i, counter)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/migrate_gradual_types/transform_to_z3.py
# Line: 53

new_c, counter = transform_to_z3(c, counter, dimension_dict)

# ==================================================
# Line: 60

new_c, counter = transform_to_z3(c, counter, dimension_dict)

# ==================================================
# Occurrences: Lines 90-95 (2 instances)

lhs, counter = transform_dimension(
    constraint.lhs, counter, dimension_dict
)

# ==================================================
# Occurrences: Lines 101-106 (2 instances)

lhs, counter = transform_algebraic_expression(
    constraint.lhs, counter, dimension_dict
)

# ==================================================
# Occurrences: Lines 113-118 (2 instances)

lhs, counter = transform_dimension(
    constraint.lhs, counter, dimension_dict
)

# ==================================================
# Occurrences: Lines 172-197 (6 instances)

lhs, counter = transform_algebraic_expression(
    constraint.lhs, counter, dimension_dict
)

# ==================================================
# Occurrences: Lines 432-442 (4 instances)

s = z3.Solver()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/migrate_gradual_types/constraint_generator.py
# Occurrences: Lines 171-172 (2 instances)

dims_input1, counter = gen_tensor_dims(3, counter)

# ==================================================
# Occurrences: Lines 284-289 (2 instances)

expand, counter = gen_tvar(counter)

# ==================================================
# Line: 731

my_gt, counter = gen_bvar(counter)

# ==================================================
# Line: 743

my_gt, counter = gen_bvar(counter)

# ==================================================
# Line: 760

my_gt, counter = gen_bvar(counter)

# ==================================================
# Line: 789

my_eq, counter = gen_bvar(counter)

# ==================================================
# Line: 801

my_eq, counter = gen_bvar(counter)

# ==================================================
# Line: 841

my_ne, counter = gen_bvar(counter)

# ==================================================
# Line: 864

my_ne, counter = gen_bvar(counter)

# ==================================================
# Occurrences: Lines 875-878 (4 instances)

b1, counter = gen_dvar(counter)

# ==================================================
# Line: 888

my_ne, counter = gen_bvar(counter)

# ==================================================
# Line: 919

my_ne, counter = gen_bvar(counter)

# ==================================================
# Line: 950

my_lt, counter = gen_bvar(counter)

# ==================================================
# Line: 962

my_lt, counter = gen_bvar(counter)

# ==================================================
# Occurrences: Lines 1034-1035 (2 instances)

e11, counter = gen_tvar(counter)

# ==================================================
# Line: 1060

my_output, counter = gen_tvar(counter)

# ==================================================
# Occurrences: Lines 1071-1076 (2 instances)

my_output, counter = gen_tvar(counter)

# ==================================================
# Occurrences: Lines 1093-1098 (2 instances)

my_output, counter = gen_tvar(counter)

# ==================================================
# Occurrences: Lines 1282-1283 (4 instances)

new_dims_rhs_1, counter = gen_tensor_dims(i, counter)

# ==================================================
# Occurrences: Lines 1362-1365 (4 instances)

d1, counter = gen_dvar(counter)

# ==================================================
# Occurrences: Lines 1384-1387 (4 instances)

d1, counter = gen_dvar(counter)

# ==================================================
# Line: 1494

x, counter = gen_tvar(counter)

# ==================================================
# Line: 1549

output, counter = gen_tvar(counter)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/shape_inference/infer_symbol_values.py
# Line: 28

matches = re.findall(square_brackets_pattern, constraint)

# ==================================================
# Occurrences: Lines 35-36 (2 instances)

matches = re.findall(square_brackets_pattern, constraint)

# ==================================================
# Occurrences: Lines 48-49 (2 instances)

matches = re.findall(square_brackets_pattern, constraint)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/shape_inference/infer_shape.py
# Line: 29

dim_count += input_tensor.dim() - 1

# ==================================================
# Line: 49

curr_dim = input_tensor.dim()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/proxy_tensor.py
# Occurrences: Lines 502-504 (2 instances)

proxy.node.meta["tensor_meta"] = _extract_tensor_metadata(val)

# ==================================================
# Occurrences: Lines 850-854 (2 instances)

const_args, const_kwargs = pytree.tree_unflatten(
    const_flat_args_kwargs, spec
)

# ==================================================
# Occurrences: Lines 978-981 (2 instances)

const_args, const_kwargs = pytree.tree_unflatten(
    const_flat_args_kwargs, spec
)

# ==================================================
# Occurrences: Lines 1190-1190 (2 instances)

mode = _pop_mode()

# ==================================================
# Occurrences: Lines 1207-1207 (2 instances)

mode = _pop_mode()

# ==================================================
# Line: 2030

fake_tensor_mode = torch._dynamo.utils.detect_fake_mode(args)

# ==================================================
# Line: 2045

fake_tensor_mode = torch._dynamo.utils.detect_fake_mode(args)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/validator.py
# Occurrences: Lines 78-80 (2 instances)

decl = e.decl()

# ==================================================
# Line: 91

if not (z3.is_app(e) and e.decl().kind() == kind):

# ==================================================
# Line: 109

arg = e.arg(0)

# ==================================================
# Line: 126

argstr = z3str(e.arg(0))

# ==================================================
# Line: 137

return str(decl)

# ==================================================
# Line: 834

log.debug("bisecting at %s: %s", mid, get_node_event(node))

# ==================================================
# Line: 847

event = get_node_event(node)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/unify_refinements.py
# Occurrences: Lines 26-31 (2 instances)

mgu = unify_eq(r.constraints)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/schema_type_annotation.py
# Occurrences: Lines 64-69 (2 instances)

return super().call_function(target, args, kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/sym_node.py
# Occurrences: Lines 151-156 (2 instances)

computed_hint = compute_hint()

# ==================================================
# Line: 1340

op = method_to_operator(method)

# ==================================================
# Line: 1431

op = method_to_operator(method)

# ==================================================
# Line: 1753

self = promote(self)

# ==================================================
# Occurrences: Lines 1762-1769 (5 instances)

self = promote(self)

# ==================================================
# Occurrences: Lines 1778-1785 (5 instances)

self = promote(self)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/_dynamism.py
# Occurrences: Lines 34-36 (4 instances)

getattr(module, attr_name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/const_fold.py
# Line: 272

new_node.meta = node.meta.copy()

# ==================================================
# Line: 293

folded_attrs.meta = node.meta.copy()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/unification/multipledispatch/utils.py
# Occurrences: Lines 26-29 (2 instances)

rest = expand_tuples(L[1:])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/unification/multipledispatch/dispatcher.py
# Line: 82

sig = next(sigiter)

# ==================================================
# Occurrences: Lines 89-92 (4 instances)

sig = next(sigiter)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/unification/unification_tools.py
# Line: 298

rv = inner = factory()

# ==================================================
# Occurrences: Lines 304-307 (4 instances)

dtemp = factory()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/optimization.py
# Occurrences: Lines 254-257 (6 instances)

begin = time.time()

# ==================================================
# Occurrences: Lines 441-442 (4 instances)

assert get_color(node.args[0]) is not None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/symbolic_shapes.py
# Occurrences: Lines 276-276 (2 instances)

cur = wrapped_f.cache_info()

# ==================================================
# Occurrences: Lines 286-286 (2 instances)

cur = wrapped_f.cache_info()

# ==================================================
# Line: 767

return type(expr)(*map(canonicalize_bool_expr, expr.args))

# ==================================================
# Occurrences: Lines 773-777 (2 instances)

t = opposite[type(expr)]  # type: ignore[index]

# ==================================================
# Occurrences: Lines 2518-2526 (6 instances)

prior_key = self._get_key()

# ==================================================
# Occurrences: Lines 2972-2974 (2 instances)

old_n_congruences = len(self._congruences[s])

# ==================================================
# Line: 3060

solution = sympy.solvers.inequalities.reduce_inequalities(exprs, s)

# ==================================================
# Line: 3113

solution = sympy.solvers.inequalities.reduce_inequalities(exprs, s)

# ==================================================
# Occurrences: Lines 3240-3242 (3 instances)

(dim.min < 2 and c.get("min", 2) == 2) or dim.min == c.get("min", 2)  # type: ignore[attr-defined]

# ==================================================
# Occurrences: Lines 3258-3265 (3 instances)

root = next(iter(c["eq"].free_symbols))

# ==================================================
# Line: 3281

and str(symbol := next(iter(c["eq"].free_symbols))) == old_root

# ==================================================
# Line: 3299

root = next(iter(c["eq"].free_symbols))

# ==================================================
# Occurrences: Lines 3727-3728 (2 instances)

self.unbacked_symfloat_counter = itertools.count()

# ==================================================
# Occurrences: Lines 4529-4532 (2 instances)

if all(r == DimDynamic.STATIC for r in dynamic_sizes)

# ==================================================
# Occurrences: Lines 4677-4678 (2 instances)

assert int(sym) == hint

# ==================================================
# Occurrences: Lines 4715-4716 (2 instances)

assert float(sym) == hint

# ==================================================
# Line: 4915

f"for {source.name()}"

# ==================================================
# Line: 4928

source_name = source.name()

# ==================================================
# Line: 4972

out = sympy.Integer(val)

# ==================================================
# Line: 4999

symbol_id = self._generate_unique_id(source.name())

# ==================================================
# Line: 5011

self.var_to_val[sympy_expr] = sympy.Integer(val)

# ==================================================
# Line: 5102

source.name(),

# ==================================================
# Line: 5115

"source": source.name(),

# ==================================================
# Line: 5131

self.log.debug("create_symbol %s duck sized %s", r, source.name())

# ==================================================
# Line: 5259

_create_no_constraints_context(t) if isinstance(t, Tensorlike) else None

# ==================================================
# Line: 5267

input_contexts[i] = _create_no_constraints_context(t)

# ==================================================
# Occurrences: Lines 5449-5450 (4 instances)

if isinstance(val, SymInt) and val.node.maybe_as_int() is not None:

# ==================================================
# Occurrences: Lines 5484-5486 (2 instances)

var_with_range = self._render_range_for_constraint_violation(
    source, constraint
)

# ==================================================
# Occurrences: Lines 5515-5517 (2 instances)

var_with_range = self._render_range_for_constraint_violation(
    source, constraint
)

# ==================================================
# Occurrences: Lines 5537-5538 (4 instances)

if isinstance(val, SymFloat) and val.node.maybe_as_float() is not None:

# ==================================================
# Occurrences: Lines 5637-5637 (2 instances)

srcname = source.name()

# ==================================================
# Line: 5667

res = f"{printer.print_source(source)} == {printer.doprint(expr)}"

# ==================================================
# Line: 5691

symbol = next(iter(expr.free_symbols))

# ==================================================
# Occurrences: Lines 5700-5700 (2 instances)

f"The values of {self._debug_name(source)} = {source.name()} and "

# ==================================================
# Occurrences: Lines 5719-5719 (2 instances)

f"The values of {self._debug_name(source)} = {source.name()} must always be related to "

# ==================================================
# Occurrences: Lines 5754-5757 (2 instances)

is_trivial = self.dim_constraints.add(expr)

# ==================================================
# Line: 5766

symbol = next(iter(expr.free_symbols))

# ==================================================
# Line: 5776

f"satisfy the generated guard {py_printer.doprint(expr)}."

# ==================================================
# Line: 5815

self.dim_constraints.add(expr)

# ==================================================
# Line: 5868

guard_expr = py_printer.doprint(expr)

# ==================================================
# Line: 6329

expr = safe_expand(expr)

# ==================================================
# Occurrences: Lines 6379-6380 (2 instances)

expr = expr.xreplace(div_replacements)

# ==================================================
# Line: 6390

new_expr = expr.xreplace(div_replacements)

# ==================================================
# Line: 6570

sloc = self._get_sloc()

# ==================================================
# Line: 6578

sloc = self._get_sloc()

# ==================================================
# Line: 6626

tgt_bound = self.bound_sympy(tgt)

# ==================================================
# Line: 6656

tgt_bound = self.bound_sympy(tgt)

# ==================================================
# Line: 7129

"expr": str(g),

# ==================================================
# Line: 7145

"expr": str(g),

# ==================================================
# Line: 7153

str_g = str(g)

# ==================================================
# Line: 7398

concrete_val = compute_concrete_val()

# ==================================================
# Line: 7548

concrete_val = compute_concrete_val()

# ==================================================
# Line: 7556

expr = sympy.Not(expr)

# ==================================================
# Line: 7563

g = sympy.Not(expr)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/accelerator_partitioner.py
# Occurrences: Lines 441-450 (5 instances)

partition = self.create_partition()

# ==================================================
# Occurrences: Lines 473-477 (5 instances)

device = find_device_based_on_size(node)

# ==================================================
# Line: 704

partition = self.create_partition()

# ==================================================
# Line: 728

partition = self.create_partition()

# ==================================================
# Occurrences: Lines 737-745 (8 instances)

partition = reset_partition_in_sparse_nn(partition)

# ==================================================
# Occurrences: Lines 953-953 (2 instances)

cost = float("inf")

# ==================================================
# Occurrences: Lines 960-979 (8 instances)

partition_to_latency_mapping = get_partition_to_latency_mapping(
    self.partitions, node_to_latency_mapping
)

# ==================================================
# Line: 989

min_cost = float("inf")

# ==================================================
# Occurrences: Lines 1006-1012 (2 instances)

partition_to_latency_mapping = get_partition_to_latency_mapping(
    self.partitions, node_to_latency_mapping
)

# ==================================================
# Occurrences: Lines 1051-1054 (2 instances)

get_device_to_partitions_mapping(self.partitions, self.devices)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/graph.py
# Line: 168

match = _name_regex.match(candidate)

# ==================================================
# Line: 179

match = _name_regex.match(candidate)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/shape_prop.py
# Occurrences: Lines 177-180 (2 instances)

result = super().run_node(n)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/utils/matcher_utils.py
# Occurrences: Lines 402-404 (2 instances)

before = len(matches)

# ==================================================
# Occurrences: Lines 421-431 (6 instances)

if len(valid_matches) != len(matches):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/_tensorify_python_scalars.py
# Line: 228

val = node.meta.get("val")

# ==================================================
# Line: 300

metrics_context = get_metrics_context()

# ==================================================
# Line: 320

(val := node.meta.get("val")),

# ==================================================
# Line: 360

metrics_context = get_metrics_context()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/splitter_base.py
# Occurrences: Lines 471-472 (2 instances)

supported_node_types = defaultdict(set)

# ==================================================
# Line: 537

acc_subgraphs_num = len([g for g in subgraphs if g.is_acc])

# ==================================================
# Line: 543

acc_subgraphs_num = len([g for g in subgraphs if g.is_acc])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/param_fetch.py
# Line: 63

attrs_for_lowering["name"] = torch.typename(mod)

# ==================================================
# Line: 69

f"Fetcher version {version} try to fetch {torch.typename(mod)} version {mod._version}, "

# ==================================================
# Line: 77

f"{torch.typename(mod)} is not in the module_fetch_book yet, "

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/split_module.py
# Occurrences: Lines 187-192 (5 instances)

base_mod_env[node.name].meta = node.meta.copy()

# ==================================================
# Line: 251

partition_name = str(split_callback(node))

# ==================================================
# Occurrences: Lines 317-339 (7 instances)

grad_regions[active_grad] = set({split_callback(node)})

# ==================================================
# Line: 363

pid = split_callback(node)

# ==================================================
# Line: 414

node.meta.copy()

# ==================================================
# Occurrences: Lines 435-444 (6 instances)

placeholder = partition.graph.placeholder(
    inp,
    type_expr=orig_nodes[inp].type,
)

# ==================================================
# Line: 465

target_attr = _get_attr_from_qualname(m, node.target)

# ==================================================
# Line: 486

new_node.meta = node.meta.copy()

# ==================================================
# Line: 517

base_mod_env, base_mod_attrs = construct_graph(
    node, base_mod_env, base_mod_attrs
)

# ==================================================
# Occurrences: Lines 571-573 (2 instances)

base_mod_env, _based_mod_attrs = construct_graph(
    node, base_mod_env, base_mod_attrs
)

# ==================================================
# Occurrences: Lines 580-582 (2 instances)

base_mod_env, base_mod_attrs = construct_graph(
    node, base_mod_env, base_mod_attrs
)

# ==================================================
# Line: 610

base_mod_env, base_mod_attrs = construct_graph(
    node, base_mod_env, base_mod_attrs
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/pass_manager.py
# Occurrences: Lines 105-108 (4 instances)

output = base_pass(output)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/split_utils.py
# Line: 152

main_g = torch.fx.Graph()

# ==================================================
# Line: 162

comp = Component(torch.fx.Graph(), len(all_components), f"{tag}")

# ==================================================
# Occurrences: Lines 215-215 (3 instances)

comp.getattr_maps[x].meta = copy.copy(x.meta)

# ==================================================
# Occurrences: Lines 229-229 (3 instances)

placeholder.meta = copy.copy(x.meta)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/dialect/common/cse_pass.py
# Occurrences: Lines 111-111 (2 instances)

new_node = new_graph.node_copy(n, lambda x: env[x])

# ==================================================
# Occurrences: Lines 148-148 (2 instances)

new_node = new_graph.node_copy(n, lambda x: env[x])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_utils.py
# Occurrences: Lines 211-212 (2 instances)

device = torch.device(device)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/quasirandom.py
# Line: 102

result = self._first_point.to(dtype)

# ==================================================
# Line: 112

result = torch.cat((self._first_point.to(dtype), result), dim=-2)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_weights_only_unpickler.py
# Occurrences: Lines 230-231 (2 instances)

module = readline()[:-1].decode("utf-8")

# ==================================================
# Occurrences: Lines 276-276 (2 instances)

key = read(1)

# ==================================================
# Occurrences: Lines 294-298 (4 instances)

strlen = read(1)[0]

# ==================================================
# Occurrences: Lines 323-323 (2 instances)

key = read(1)

# ==================================================
# Occurrences: Lines 382-383 (4 instances)

args = self.stack.pop()

# ==================================================
# Occurrences: Lines 400-400 (2 instances)

args = self.stack.pop()

# ==================================================
# Occurrences: Lines 414-414 (2 instances)

state = self.stack.pop()

# ==================================================
# Occurrences: Lines 447-447 (2 instances)

item = self.stack.pop()

# ==================================================
# Occurrences: Lines 455-455 (2 instances)

items = self.pop_mark()

# ==================================================
# Occurrences: Lines 463-466 (6 instances)

(v, k) = (self.stack.pop(), self.stack.pop())

# ==================================================
# Occurrences: Lines 474-474 (2 instances)

items = self.pop_mark()

# ==================================================
# Occurrences: Lines 509-518 (8 instances)

strval = str(read(strlen), "utf-8", "surrogatepass")

# ==================================================
# Occurrences: Lines 534-547 (8 instances)

idx = (read(1) if key[0] == BINGET[0] else unpack("<I", read(4)))[0]

# ==================================================
# Occurrences: Lines 556-556 (2 instances)

rc = self.stack.pop()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_decomp/__init__.py
# Line: 102

sig = inspect.signature(f)

# ==================================================
# Line: 126

_fn.__signature__ = inspect.Signature(  # type: ignore[attr-defined]
    parameters=params,  # type: ignore[arg-type]
    return_annotation=sig.return_annotation,
)

# ==================================================
# Occurrences: Lines 159-166 (2 instances)

sig = inspect.signature(f)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_decomp/decompositions.py
# Occurrences: Lines 729-732 (2 instances)

ndim = self.dim()

# ==================================================
# Occurrences: Lines 1757-1761 (2 instances)

computation_dtype = utils.get_computation_dtype(input.dtype)

# ==================================================
# Occurrences: Lines 1799-1800 (2 instances)

save_mean = input.new_zeros((0,))

# ==================================================
# Occurrences: Lines 2133-2138 (2 instances)

x_tensor = torch._prims.convert_element_type(x_tensor, dtype)

# ==================================================
# Occurrences: Lines 2723-2724 (2 instances)

torch._check(len(sequences) > 0, lambda: "received an empty list of sequences")

# ==================================================
# Occurrences: Lines 4000-4002 (2 instances)

result = result.sum()

# ==================================================
# Occurrences: Lines 4269-4272 (4 instances)

ix = compute_source_index(x, iW)

# ==================================================
# Occurrences: Lines 4292-4293 (2 instances)

ix = compute_source_index(x, iW)

# ==================================================
# Occurrences: Lines 4303-4304 (2 instances)

ix_nw = ix.floor()

# ==================================================
# Occurrences: Lines 4944-4948 (2 instances)

z = z.sum(dim=(0, -1)).mean()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_decomp/decompositions_for_rng.py
# Occurrences: Lines 78-79 (2 instances)

self.seed = torch.tensor(())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_decomp/decompositions_for_jvp.py
# Line: 193

d_weight = torch.zeros(())  # should be None but doesn't work with vjp

# ==================================================
# Line: 203

d_bias = torch.zeros(())  # should be None but doesn't work with vjp

# ==================================================
# Line: 229

input_rank = input.dim()

# ==================================================
# Line: 241

reduciton_dims = [0] + list(range(2, input.dim()))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_helper.py
# Line: 60

node = value.node()

# ==================================================
# Line: 88

element_node = v.node()

# ==================================================
# Occurrences: Lines 97-97 (2 instances)

return [int(_node_get(v.node(), "value")) for v in value.node().inputs()]

# ==================================================
# Occurrences: Lines 519-521 (2 instances)

if not _is_tensor(x) or x.type() is None:

# ==================================================
# Occurrences: Lines 527-529 (2 instances)

if not _is_tensor(x) or x.type() is None:

# ==================================================
# Occurrences: Lines 968-970 (2 instances)

if not input.type().dim():

# ==================================================
# Occurrences: Lines 1051-1059 (8 instances)

empty_roi = _optional_input_placeholder_tensor(g)

# ==================================================
# Occurrences: Lines 1074-1078 (4 instances)

empty_roi = _optional_input_placeholder_tensor(g)

# ==================================================
# Line: 1138

rank = _get_tensor_rank(input)

# ==================================================
# Occurrences: Lines 1151-1157 (4 instances)

empty_roi = _optional_input_placeholder_tensor(g)

# ==================================================
# Occurrences: Lines 1171-1178 (3 instances)

rank = _get_tensor_rank(input)

# ==================================================
# Occurrences: Lines 1336-1338 (2 instances)

if self.type().dim() is None:

# ==================================================
# Occurrences: Lines 1788-1799 (10 instances)

dtype = _get_const(dtype, "i", "dtype")

# ==================================================
# Occurrences: Lines 1809-1820 (10 instances)

dtype = _get_const(dtype, "i", "dtype")

# ==================================================
# Occurrences: Lines 1877-1893 (7 instances)

mean = g.op("ReduceMean", input, keepdims_i=0)

# ==================================================
# Occurrences: Lines 1900-1927 (11 instances)

num_elements = g.op(
    "Cast", num_elements, to_i=_C_onnx.TensorProtoDataType.FLOAT
)

# ==================================================
# Occurrences: Lines 1937-1942 (4 instances)

num_elements = g.op(
    "Cast", num_elements, to_i=_C_onnx.TensorProtoDataType.FLOAT
)

# ==================================================
# Occurrences: Lines 1996-1997 (2 instances)

block_input_iter = utils._add_input_to_block(loop_block)

# ==================================================
# Line: 2026

axes = loop_context.op(
    "Constant", value_t=torch.tensor([0], dtype=torch.long)
)

# ==================================================
# Line: 2036

axes = loop_context.op(
    "Constant", value_t=torch.tensor([0], dtype=torch.long)
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset8.py
# Line: 305

old_type, input = _try_cast_integer_to_float(g, input)

# ==================================================
# Line: 313

old_type, input = _try_cast_integer_to_float(g, input)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/utils.py
# Line: 864

orig_state_dict_keys = torch.jit._unique_state_dict(model).keys()

# ==================================================
# Line: 882

if orig_state_dict_keys != torch.jit._unique_state_dict(model).keys():

# ==================================================
# Line: 1081

params_dict = _get_named_param_dict(graph, params)

# ==================================================
# Line: 1137

params_dict = _get_named_param_dict(graph, params)

# ==================================================
# Occurrences: Lines 1580-1582 (9 instances)

identity_node.output().setType(node.type())

# ==================================================
# Line: 1706

outputs = node.outputsSize()

# ==================================================
# Line: 1738

op_name, *inputs, **attrs, outputs=node.outputsSize()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/ops/_symbolic_impl.py
# Occurrences: Lines 107-117 (6 instances)

start_pos = len(encoded.attr_ints)

# ==================================================
# Occurrences: Lines 125-135 (6 instances)

start_pos = len(encoded.attr_floats)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/ops/_impl.py
# Occurrences: Lines 105-108 (2 instances)

x_rotate_concat = torch.cat((real, imag), dim=-1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset14.py
# Line: 188

mul_qk_add = g.op("Add", mul_qk, attn_mask)

# ==================================================
# Line: 194

mul_qk_add = g.op("Add", mul_qk, attn_mask)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/verification.py
# Line: 1464

new_input = graph.addInput()

# ==================================================
# Line: 1487

new_input = graph.addInput()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_onnx_supported_ops.py
# Occurrences: Lines 86-86 (2 instances)

symbolics_schema.arguments = _symbolic_argument_count(func)

# ==================================================
# Occurrences: Lines 93-93 (2 instances)

symbolics_schema.arguments = _symbolic_argument_count(func)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset11.py
# Line: 226

broadcast_index_shape = g.op("Shape", index)

# ==================================================
# Line: 276

rank = symbolic_helper._get_tensor_rank(values)

# ==================================================
# Line: 291

broadcast_index_shape = g.op("Shape", index)

# ==================================================
# Line: 298

rank = symbolic_helper._get_tensor_rank(values)

# ==================================================
# Line: 815

delta_default = g.op(
    "Constant",
    value_t=torch.tensor(1, dtype=type_.dtype()),
)

# ==================================================
# Line: 837

delta_default = g.op(
    "Constant",
    value_t=torch.tensor(1, dtype=type_.dtype()),
)

# ==================================================
# Occurrences: Lines 1390-1396 (4 instances)

new_tensor = symbolic_helper._unsqueeze_helper(
    g, new_tensor, axes_i=[-1]
)

# ==================================================
# Occurrences: Lines 1407-1409 (2 instances)

self = symbolic_helper._unsqueeze_helper(g, self, axes_i=[-1])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset9.py
# Line: 458

out = g.op("Cast", out, to_i=_C_onnx.TensorProtoDataType.FLOAT)

# ==================================================
# Line: 466

out = g.op("Cast", out, to_i=_C_onnx.TensorProtoDataType.FLOAT)

# ==================================================
# Occurrences: Lines 522-525 (2 instances)

scalar_type = torch.get_default_dtype()

# ==================================================
# Line: 554

tensors = symbolic_helper._unpack_list(tensor_list)

# ==================================================
# Line: 577

tensors = symbolic_helper._unpack_list(tensor_list)

# ==================================================
# Occurrences: Lines 640-641 (2 instances)

alpha = symbolic_helper._scalar(alpha)

# ==================================================
# Line: 652

symbolic_helper._scalar(beta), dtype=scalar_type.dtype()

# ==================================================
# Occurrences: Lines 664-665 (2 instances)

beta_f=symbolic_helper._scalar(beta),

# ==================================================
# Occurrences: Lines 1322-1327 (2 instances)

parsed_dtype = symbolic_helper._get_const(dtype, "i", "dtype")

# ==================================================
# Occurrences: Lines 1340-1343 (2 instances)

parsed_dtype = symbolic_helper._get_const(dtype, "i", "dtype")

# ==================================================
# Occurrences: Lines 3643-3645 (2 instances)

dim_size = symbolic_helper._unsqueeze_helper(g, n, [0])

# ==================================================
# Occurrences: Lines 3652-3656 (2 instances)

symbolic_helper._unsqueeze_helper(g, n, [0]),

# ==================================================
# Line: 3915

dtype = symbolic_helper._get_const(args[1], "i", "dtype")

# ==================================================
# Line: 3921

dtype = symbolic_helper._get_const(args[0], "i", "dtype")

# ==================================================
# Occurrences: Lines 3960-3970 (3 instances)

dtype = symbolic_helper._get_const(args[1], "i", "dtype")

# ==================================================
# Line: 4107

after_transpose = g.op("Transpose", after_view, perm_i=[0, 1, 4, 2, 5, 3])

# ==================================================
# Line: 4142

after_transpose = g.op("Transpose", after_view, perm_i=[0, 1, 4, 2, 5, 3])

# ==================================================
# Line: 4311

sequence_lens = unused(g) if batch_sizes is None else batch_sizes

# ==================================================
# Occurrences: Lines 4371-4371 (2 instances)

bias_concat = unused(g)

# ==================================================
# Occurrences: Lines 4382-4382 (2 instances)

bias_concat = unused(g)

# ==================================================
# Line: 4580

weight = symbolic_helper._unpack_list(weight_v)

# ==================================================
# Line: 4608

weight = symbolic_helper._unpack_list(weight_v)

# ==================================================
# Line: 5191

end = symbolic_helper._unsqueeze_helper(g, end, [0])

# ==================================================
# Occurrences: Lines 5210-5211 (2 instances)

end = symbolic_helper._unsqueeze_helper(g, end, [0])

# ==================================================
# Occurrences: Lines 5226-5227 (2 instances)

end = symbolic_helper._unsqueeze_helper(g, end, [0])

# ==================================================
# Occurrences: Lines 5334-5336 (2 instances)

if len(adv_idx_indices) == 0:

# ==================================================
# Line: 5357

adv_idx_count = len(adv_idx_indices)

# ==================================================
# Line: 5457

ord = g.op("Constant", value_t=torch.LongTensor([2]))

# ==================================================
# Line: 5464

ord_value = symbolic_helper._parse_arg(ord, "f")

# ==================================================
# Occurrences: Lines 5470-5471 (2 instances)

ord = g.op("Constant", value_t=torch.LongTensor([2]))

# ==================================================
# Line: 5657

half = torch.tensor(0.5, dtype=torch.double)

# ==================================================
# Line: 5671

g.op("Constant", value_t=torch.tensor(0.5, dtype=torch.double)),

# ==================================================
# Occurrences: Lines 5934-5935 (2 instances)

alpha = g.op("Constant", value_t=torch.tensor(1, dtype=torch.int64))

# ==================================================
# Occurrences: Lines 6012-6013 (2 instances)

src_dims = perm.copy()

# ==================================================
# Line: 6059

other_dim_rank = symbolic_helper._get_tensor_rank(other)

# ==================================================
# Line: 6072

g, other, [symbolic_helper._get_tensor_rank(other)]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset13.py
# Line: 150

start = g.op("Constant", value_t=torch.tensor([0], dtype=torch.long))

# ==================================================
# Occurrences: Lines 160-164 (3 instances)

res.append(g.op("Slice", self, start, end, axis))

# ==================================================
# Line: 203

padding_0 = g.op("Constant", value_t=torch.tensor([0], dtype=torch.long))

# ==================================================
# Occurrences: Lines 213-215 (3 instances)

block_input_iter = utils._add_input_to_block(loop_block)

# ==================================================
# Occurrences: Lines 243-250 (3 instances)

end = symbolic_helper._size_helper(g, self, axis)

# ==================================================
# Occurrences: Lines 416-427 (10 instances)

dtype = symbolic_helper._get_const(dtype, "i", "dtype")

# ==================================================
# Occurrences: Lines 434-445 (10 instances)

dtype = symbolic_helper._get_const(dtype, "i", "dtype")

# ==================================================
# Occurrences: Lines 691-693 (3 instances)

block_input_iter = utils._add_input_to_block(loop_block)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/onnx_proto_utils.py
# Occurrences: Lines 117-122 (2 instances)

inputs[tensor.name] = numpy_helper.to_array(tensor)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/fx/fx_onnx_interpreter.py
# Occurrences: Lines 226-233 (4 instances)

onnxscript_value.dtype = fx_type_utils.from_scalar_type_to_torch_dtype(
    type(expected_value)
)

# ==================================================
# Occurrences: Lines 244-244 (2 instances)

onnxscript_value.shape = torch.Size((*expected_value.size(), 2))

# ==================================================
# Occurrences: Lines 254-254 (2 instances)

onnxscript_value.shape = expected_value.size()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/fx/onnxfunction_dispatcher.py
# Line: 116

op_full_name = self._get_aten_name(node).qualified_name()

# ==================================================
# Line: 127

op_full_name = self._get_aten_name(node).qualified_name()

# ==================================================
# Line: 276

op_full_name = internal_opname.qualified_name()

# ==================================================
# Line: 283

op_full_name = internal_opname.qualified_name()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/fx/passes/modularization.py
# Occurrences: Lines 684-685 (2 instances)

ref_submodule_outputs = self.module_outputs()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_building.py
# Occurrences: Lines 83-83 (2 instances)

named_inputs[param.name] = reversed_args_stack.pop()  # type: ignore[assignment]

# ==================================================
# Occurrences: Lines 106-106 (2 instances)

attribute = reversed_args_stack.pop()  # type: ignore[assignment]

# ==================================================
# Occurrences: Lines 415-415 (2 instances)

dtype = _determine_input_dtype(param, arg, type_binding)

# ==================================================
# Occurrences: Lines 436-436 (2 instances)

dtype = _determine_input_dtype(param, arg, type_binding)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_core.py
# Occurrences: Lines 266-272 (3 instances)

value.shape = ir.Shape([])

# ==================================================
# Occurrences: Lines 321-323 (4 instances)

nn_module_name = _get_qualified_module_name(nn_module)

# ==================================================
# Line: 1346

profile_result = _maybe_stop_profiler_and_get_result(profiler)

# ==================================================
# Line: 1411

profile_result = _maybe_stop_profiler_and_get_result(profiler)

# ==================================================
# Line: 1422

f"{_format_exceptions_for_all_strategies(failed_results)}\n\n{_format_exception(e)}",

# ==================================================
# Line: 1471

profile_result = _maybe_stop_profiler_and_get_result(profiler)

# ==================================================
# Line: 1485

f"{_format_exceptions_for_all_strategies(failed_results)}\n\n{_format_exception(e)}",

# ==================================================
# Line: 1506

profile_result = _maybe_stop_profiler_and_get_result(profiler)

# ==================================================
# Line: 1559

f"{_format_exceptions_for_all_strategies(failed_results)}\n\n{_format_exception(e)}",

# ==================================================
# Line: 1591

onnx_runtime_error_message = _format_exception(e)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_schemas.py
# Line: 254

subtypes = typing.get_args(type_)

# ==================================================
# Line: 262

subtypes = typing.get_args(type_)

# ==================================================
# Line: 297

subtypes = typing.get_args(type_)

# ==================================================
# Line: 308

subtypes = typing.get_args(type_)

# ==================================================
# Line: 317

subtypes = typing.get_args(type_)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_dynamic_shapes.py
# Occurrences: Lines 262-262 (2 instances)

custom_name = _get_custom_axis_name(axis)

# ==================================================
# Occurrences: Lines 282-282 (3 instances)

custom_name = _get_custom_axis_name(axis)

# ==================================================
# Occurrences: Lines 291-291 (3 instances)

rename_mapping[input.shape[dim].value] = _get_custom_axis_name(axis)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset12.py
# Occurrences: Lines 263-266 (2 instances)

out = g.op("Celu", self, alpha_f=alpha)

# ==================================================
# Line: 318

low_start = g.op("Constant", value_t=torch.tensor(0))

# ==================================================
# Occurrences: Lines 325-328 (2 instances)

g, low_indices, g.op("Constant", value_t=torch.tensor(0))

# ==================================================
# Occurrences: Lines 348-349 (2 instances)

block_input_iter = utils._add_input_to_block(loop_block)

# ==================================================
# Occurrences: Lines 426-436 (3 instances)

output_a = opset9._reshape_from_tensor(g, new_input_a, shape_sizes)

# ==================================================
# Occurrences: Lines 449-459 (3 instances)

output_b = opset9._reshape_from_tensor(g, new_input_b, shape_sizes)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/schema_check_mode.py
# Occurrences: Lines 171-174 (4 instances)

if arguments.get(name) is not None:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/meta_utils.py
# Line: 282

is_view = t._is_view()

# ==================================================
# Line: 336

if t._is_view():

# ==================================================
# Line: 458

torch._C._autograd._get_creation_meta(t) if t._is_view() else None

# ==================================================
# Line: 469

if recurse and t._is_view() and t._base is not None

# ==================================================
# Line: 1182

(sizes, strides, storage_offset) = sym_sizes_strides_storage_offset(
    t, source
)

# ==================================================
# Line: 1247

fake_t: _TensorT = empty_create_subclass(
    t, outer_size=sizes, outer_stride=strides
)

# ==================================================
# Line: 1335

r.real_tensor = _safe_clone(t.data)

# ==================================================
# Occurrences: Lines 1388-1393 (2 instances)

r.real_tensor = _safe_clone(t.data)

# ==================================================
# Occurrences: Lines 1409-1416 (2 instances)

) = sym_sizes_strides_storage_offset(t, source)

# ==================================================
# Line: 1422

r.real_tensor = torch.empty_strided(
    t.size, t.stride, dtype=t.dtype, device=t.device
)

# ==================================================
# Line: 1431

r = self._backward_error(r)

# ==================================================
# Occurrences: Lines 1450-1450 (2 instances)

ft = _to_fake_tensor(t.unwrapped)

# ==================================================
# Occurrences: Lines 1468-1468 (2 instances)

ft = _to_fake_tensor(t.unwrapped)

# ==================================================
# Occurrences: Lines 1484-1498 (2 instances)

r = self._backward_error(r)

# ==================================================
# Occurrences: Lines 1508-1524 (2 instances)

r = callback(
    lambda: torch.empty_strided(
        sizes,
        strides,
        dtype=t.dtype,
        device="meta",
    ),
    # device="meta",
)

# ==================================================
# Line: 1534

unwrapped = self.meta_tensor(
    t.unwrapped,
    shape_env,
    callback,
    source,
    symbolic_context,
)

# ==================================================
# Line: 1631

r = view_from_base(base, t)

# ==================================================
# Line: 1638

r = view_from_base(base, t)

# ==================================================
# Occurrences: Lines 1685-1696 (2 instances)

r = empty_create_subclass(
    t, outer_size=sizes, outer_stride=strides
)

# ==================================================
# Line: 1702

r.real_tensor = torch.empty_strided(
    t.size, t.stride, dtype=t.dtype, device=t.device
)

# ==================================================
# Line: 1720

r = self._backward_error(r)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/fake_utils.py
# Occurrences: Lines 267-268 (2 instances)

r_flat = pytree.tree_leaves(r)

# ==================================================
# Occurrences: Lines 279-279 (2 instances)

zip(pytree.tree_leaves(r), pytree.tree_leaves(fake_r))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/functional_tensor.py
# Occurrences: Lines 473-478 (2 instances)

is_included = torch._C._dispatch_tls_is_dispatch_key_included(
    torch._C.DispatchKey.Functionalize
)

# ==================================================
# Line: 502

outs_wrapped = pytree.tree_map_only(
    torch.Tensor, wrap, outs_unwrapped
)

# ==================================================
# Occurrences: Lines 520-532 (3 instances)

outs_wrapped = pytree.tree_map_only(
    torch.Tensor, wrap, outs_unwrapped
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/fake_tensor.py
# Occurrences: Lines 906-909 (4 instances)

is_cpu_zero_dim = cpu_zero_dim(t)

# ==================================================
# Line: 1457

return self._dispatch_impl(func, types, args, kwargs)

# ==================================================
# Line: 1474

return self._dispatch_impl(func, types, args, kwargs)

# ==================================================
# Line: 1487

output = self._dispatch_impl(func, types, args, kwargs)

# ==================================================
# Occurrences: Lines 2313-2314 (2 instances)

const_args, const_kwargs = pytree.tree_unflatten(const_flat_args, args_spec)

# ==================================================
# Occurrences: Lines 2381-2386 (2 instances)

const_args, const_kwargs = pytree.tree_unflatten(const_flat_args, args_spec)

# ==================================================
# Line: 2466

is_builtin = library_utils.is_builtin(func)

# ==================================================
# Occurrences: Lines 2537-2552 (4 instances)

self._maybe_infer_fake_kernel_from_pytree_out(
    func,
    (args, kwargs),
    (real_args, real_kwargs),
    fake_out,
    real_out,
)

# ==================================================
# Occurrences: Lines 2634-2639 (2 instances)

and not library_utils.is_builtin(func)

# ==================================================
# Occurrences: Lines 2667-2670 (2 instances)

and not library_utils.is_builtin(func)

# ==================================================
# Occurrences: Lines 2778-2778 (2 instances)

args, kwargs = pytree.tree_unflatten(flat_args, args_spec)

# ==================================================
# Occurrences: Lines 2790-2790 (2 instances)

args, kwargs = pytree.tree_unflatten(flat_args, args_spec)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/compiler/_cache.py
# Occurrences: Lines 71-73 (2 instances)

artifact_type_key = artifact_cls.type()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/serialization.py
# Occurrences: Lines 1039-1039 (2 instances)

storage_numel = storage.nbytes()

# ==================================================
# Occurrences: Lines 1061-1061 (2 instances)

storage_key = str(storage._cdata)

# ==================================================
# Occurrences: Lines 1097-1097 (4 instances)

view_metadata = (str(storage._cdata), offset, storage.nbytes())

# ==================================================
# Line: 1179

storage_numel = storage.nbytes()

# ==================================================
# Line: 1238

num_bytes = storage.nbytes()

# ==================================================
# Occurrences: Lines 1665-1667 (4 instances)

num_storages = pickle_module.load(f, **pickle_load_args)

# ==================================================
# Occurrences: Lines 1673-1680 (4 instances)

obj = restore_location(obj, location)

# ==================================================
# Occurrences: Lines 1697-1699 (4 instances)

num_tensors = pickle_module.load(f, **pickle_load_args)

# ==================================================
# Occurrences: Lines 1705-1706 (6 instances)

numel = struct.unpack(f"<{ndim}q", f.read(8 * ndim))

# ==================================================
# Occurrences: Lines 1742-1752 (9 instances)

obj = cast(Storage, torch.UntypedStorage(nbytes))

# ==================================================
# Line: 1788

if f_should_read_directly and f.tell() == 0:

# ==================================================
# Occurrences: Lines 1802-1817 (5 instances)

magic_number = pickle_module.load(f, **pickle_load_args)

# ==================================================
# Line: 1828

offset = f.tell()

# ==================================================
# Line: 1854

return default_restore_location(storage, location)

# ==================================================
# Line: 1871

result = default_restore_location(storage, location)

# ==================================================
# Line: 1977

current_offset = zip_file.get_record_offset(name)

# ==================================================
# Occurrences: Lines 2007-2007 (2 instances)

storage._checkpoint_offset = zip_file.get_record_offset(name)

# ==================================================
# Occurrences: Lines 2013-2022 (8 instances)

storage_offset = _get_offset(key, name, numel)

# ==================================================
# Occurrences: Lines 2028-2033 (6 instances)

storage_offset = _get_offset(key, name, numel)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/functional.py
# Line: 114

s = len(shape)

# ==================================================
# Line: 128

for i in range(-1, -1 - len(shape), -1):

# ==================================================
# Occurrences: Lines 1084-1086 (2 instances)

return _unique_impl(input, sorted, return_inverse, return_counts, dim)

# ==================================================
# Occurrences: Lines 1100-1102 (2 instances)

return _unique_impl(input, sorted, return_inverse, return_counts, dim)

# ==================================================
# Occurrences: Lines 1116-1120 (2 instances)

return _unique_impl(input, sorted, return_inverse, return_counts, dim)

# ==================================================
# Occurrences: Lines 1168-1172 (2 instances)

return _unique_consecutive_impl(input, return_inverse, return_counts, dim)

# ==================================================
# Occurrences: Lines 1185-1187 (2 instances)

return _unique_consecutive_impl(input, return_inverse, return_counts, dim)

# ==================================================
# Occurrences: Lines 1200-1204 (2 instances)

return _unique_consecutive_impl(input, return_inverse, return_counts, dim)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/distribution.py
# Occurrences: Lines 297-303 (4 instances)

event_dim_start = len(value.size()) - len(self._event_shape)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/wishart.py
# Occurrences: Lines 119-123 (3 instances)

self.scale_tril = param.expand(batch_shape + (-1, -1))

# ==================================================
# Occurrences: Lines 259-274 (6 instances)

sample = self._bartlett_sampling(sample_shape)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/transforms.py
# Occurrences: Lines 161-165 (2 instances)

return self._call(x)

# ==================================================
# Occurrences: Lines 174-178 (2 instances)

return self._inverse(y)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/von_mises.py
# Occurrences: Lines 18-20 (2 instances)

result = coef.pop()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_jit_internal.py
# Line: 1411

arg_type = get_args(target_type)[0]

# ==================================================
# Occurrences: Lines 1425-1426 (2 instances)

key_type = get_args(target_type)[0]

# ==================================================
# Line: 1442

arg_types = get_args(target_type)

# ==================================================
# Line: 1458

inner_types = get_args(target_type)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_prims/__init__.py
# Line: 2448

dim = len(shape)

# ==================================================
# Line: 2457

strides = [0] * len(shape)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_prims/rng_prims.py
# Occurrences: Lines 136-137 (2 instances)

if kwargs.get("device"):

# ==================================================
# Occurrences: Lines 203-207 (2 instances)

return impl_backend_select(op, *args, **kwargs)

# ==================================================
# Line: 236

out = op(*args, **kwargs)

# ==================================================
# Line: 244

out = op(*args, **kwargs)

# ==================================================
# Line: 253

out = op(*args, **kwargs)

# ==================================================
# Line: 262

out = op(*args, **kwargs)

# ==================================================
# Line: 297

return op(*args, **kwargs)

# ==================================================
# Line: 338

out = op(*args, **kwargs)

# ==================================================
# Line: 353

return op(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/masked/_ops.py
# Occurrences: Lines 298-303 (2 instances)

example_input = example_input.to(dtype=torch.float32)

# ==================================================
# Line: 333

example_input = example_input.to(dtype=torch.float32)

# ==================================================
# Occurrences: Lines 551-562 (4 instances)

mask.values(), tuple(range(1, input.sparse_dim() + 1)), False

# ==================================================
# Line: 582

where_mask_values = mask.values()[w1]

# ==================================================
# Line: 686

return new_values.to(dtype=output_dtype).to_sparse()

# ==================================================
# Occurrences: Lines 719-728 (5 instances)

out = new_values.new_empty(out_shape)

# ==================================================
# Line: 928

mask.to_sparse(), input.shape

# ==================================================
# Line: 939

mask = mask.to_sparse()

# ==================================================
# Occurrences: Lines 984-989 (2 instances)

outmask = _input_mask(input, *args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/masked/maskedtensor/unary.py
# Occurrences: Lines 131-135 (3 instances)

data_args[0] = data_args[0].coalesce()

# ==================================================
# Occurrences: Lines 142-146 (2 instances)

v = fn(*data_args)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/masked/maskedtensor/_ops_refs.py
# Occurrences: Lines 502-504 (2 instances)

new_data = func(*new_args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/masked/maskedtensor/reductions.py
# Occurrences: Lines 100-105 (4 instances)

mask = self.get_mask()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/masked/maskedtensor/binary.py
# Occurrences: Lines 109-123 (7 instances)

if not _tensors_match(data_args[0].indices(), data_args[1].indices()):

# ==================================================
# Occurrences: Lines 129-131 (2 instances)

_tensors_match(data_args[0].crow_indices(), data_args[1].crow_indices())

# ==================================================
# Occurrences: Lines 138-148 (7 instances)

data_args[1] = data_args[1].values()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/masked/maskedtensor/core.py
# Occurrences: Lines 77-80 (4 instances)

a_impl, _ = _map_mt_args_kwargs(a, {}, map_fn)

# ==================================================
# Occurrences: Lines 89-92 (2 instances)

impl_args.append(_helper(a, map_fn))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/overrides.py
# Occurrences: Lines 1843-1848 (6 instances)

func = getattr(namespace, func_name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_tensor.py
# Occurrences: Lines 279-282 (2 instances)

return self._reduce_ex_internal(proto)

# ==================================================
# Line: 335

cpu_tensor = self.cpu()

# ==================================================
# Occurrences: Lines 360-362 (2 instances)

self.cpu().numpy()

# ==================================================
# Line: 417

torch.storage.TypedStorage(
    wrap_storage=self._typed_storage()._untyped_storage,
    dtype=self.dtype,
    _internal=True,
),

# ==================================================
# Line: 532

storage = torch.storage.TypedStorage(
    wrap_storage=self._typed_storage()._untyped_storage,
    dtype=self.dtype,
    _internal=True,
)  # type: ignore[assignment]

# ==================================================
# Occurrences: Lines 1723-1725 (2 instances)

stream = torch.cuda.default_stream()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/storage.py
# Line: 747

device=_get_device_from_module(cls.__module__),

# ==================================================
# Line: 765

cls_device = _get_device_from_module(cls.__module__)

# ==================================================
# Line: 1282

untyped_storage: torch.UntypedStorage = torch.UntypedStorage.from_buffer(
    *args, dtype=dtype, **kwargs
)

# ==================================================
# Line: 1299

untyped_storage = torch.UntypedStorage.from_buffer(
    *args, dtype=dtype, **kwargs
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_tensor_str.py
# Line: 190

value_str = f"{{:.{PRINT_OPTS.precision}e}}".format(value)

# ==================================================
# Line: 205

value_str = f"{{:.{PRINT_OPTS.precision}e}}".format(value)

# ==================================================
# Line: 400

dim = self.dim()

# ==================================================
# Line: 411

return self.new_empty([0] * self.dim())

# ==================================================
# Line: 497

values_str = _tensor_str(values, indent + len(values_prefix))

# ==================================================
# Line: 561

values_str = _tensor_str(values, indent + len(values_prefix))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nested/_internal/ops.py
# Line: 294

assert isinstance(a, NestedTensor) or isinstance(b, NestedTensor)

# ==================================================
# Line: 300

if isinstance(a, NestedTensor) and isinstance(b, NestedTensor):

# ==================================================
# Line: 309

a_is_nt = isinstance(a, NestedTensor)

# ==================================================
# Line: 390

inp = new_kwargs.pop("input")

# ==================================================
# Line: 426

inp = new_kwargs.pop("input")

# ==================================================
# Occurrences: Lines 1414-1417 (2 instances)

isinstance(new_kwargs["dim"], (tuple, list)) and len(new_kwargs["dim"]) == 0

# ==================================================
# Line: 1428

is_dimlist = isinstance(new_kwargs["dim"], (tuple, list))

# ==================================================
# Line: 1462

out = func(inp._values, **new_kwargs)

# ==================================================
# Line: 1493

out = func(inp._values, **new_kwargs)

# ==================================================
# Line: 1499

if isinstance(new_kwargs["dim"], (tuple, list))

# ==================================================
# Line: 1555

inp_kwargs = extract_kwargs(inp)

# ==================================================
# Line: 1572

return NestedTensor(func(inp._values, **new_kwargs), **extract_kwargs(inp))

# ==================================================
# Occurrences: Lines 1893-1896 (2 instances)

if inp.lengths() is None:

# ==================================================
# Occurrences: Lines 1914-1918 (2 instances)

inp._values = func(inp._values, func_indices, **new_kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nested/_internal/sdpa.py
# Line: 354

max_seqlen = qkv._get_max_seqlen()

# ==================================================
# Line: 361

max_seqlen = qkv._get_max_seqlen()

# ==================================================
# Line: 556

q_num_heads = query.size(1)

# ==================================================
# Line: 568

num_heads = query.size(1)

# ==================================================
# Occurrences: Lines 752-753 (2 instances)

query.offsets(),

# ==================================================
# Line: 808

attention = nested_view_from_values_offsets_lengths(
    attention,  # output from flash_attn is [total_q, num_heads, head_size_og]
    **output_nt_info,
).transpose(1, 2)

# ==================================================
# Line: 823

) = _sdpa_nested_preprocessing(query, key, value)

# ==================================================
# Line: 860

) = _sdpa_nested_preprocessing(query, key, value)

# ==================================================
# Occurrences: Lines 886-895 (3 instances)

return nested_view_from_values_offsets_lengths(
    attention,
    **output_nt_info,
).transpose(1, 2)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_numpy/_funcs_impl.py
# Occurrences: Lines 1605-1608 (4 instances)

slice1 = [slice(None)] * N

# ==================================================
# Occurrences: Lines 1631-1633 (4 instances)

slice1[axis] = slice(1, -1)

# ==================================================
# Occurrences: Lines 1714-1717 (8 instances)

slice1[axis] = slice(None)

# ==================================================
# Occurrences: Lines 1968-1970 (2 instances)

sample = normalize_array_like(sample).T

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_library/utils.py
# Line: 155

loc = next(iter(alias_set))

# ==================================================
# Line: 166

if loc != next(iter(alias_set)):

# ==================================================
# Occurrences: Lines 359-360 (4 instances)

key = id(tensor.untyped_storage())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_library/autograd.py
# Line: 40

result = op.redispatch(keyset & _C._after_autograd_keyset, *args, **kwargs)

# ==================================================
# Line: 50

result = op.redispatch(keyset & _C._after_autograd_keyset, *args, **kwargs)

# ==================================================
# Line: 145

metadata.result_is_tuple = isinstance(result, tuple)

# ==================================================
# Line: 210

assert isinstance(result, tuple)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_library/fake_profile.py
# Line: 157

if opdef := _maybe_get_opdef(op_str):

# ==================================================
# Line: 185

opdef = _maybe_get_opdef(op_str)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_library/infer_schema.py
# Occurrences: Lines 166-170 (4 instances)

default_repr = str(param.default)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/library.py
# Line: 174

getattr(torch.ops, self.ns), packet_name

# ==================================================
# Line: 184

ns = getattr(torch.ops, self.ns)

# ==================================================
# Occurrences: Lines 1444-1444 (2 instances)

cpp_filename = op._handle.debug()

# ==================================================
# Occurrences: Lines 1456-1456 (2 instances)

cpp_filename = op._handle.debug()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/pt2_archive/_package.py
# Line: 347

or (isinstance(f, (str, os.PathLike)) and os.fspath(f).endswith(".pt2"))

# ==================================================
# Line: 357

f = os.fspath(f)

# ==================================================
# Line: 515

or (isinstance(f, (str, os.PathLike)) and os.fspath(f).endswith(".pt2"))

# ==================================================
# Line: 525

f = os.fspath(f)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/dynamic_shapes.py
# Occurrences: Lines 548-551 (2 instances)

return _get_node_type(t) not in BUILTIN_TYPES

# ==================================================
# Line: 709

t_id = id(t)

# ==================================================
# Line: 716

self._shapes[id(t)] = shape

# ==================================================
# Line: 899

f"specified at `dynamic_shapes{keystr(path)}` "

# ==================================================
# Line: 908

f"Expected dynamic shape spec {shape} specified at `dynamic_shapes{keystr(path)}` "

# ==================================================
# Line: 922

f"specified at `dynamic_shapes{keystr(path)}` "

# ==================================================
# Line: 930

f"Unexpected input tensor shape {shape} specified at `dynamic_shapes{keystr(path)}` "

# ==================================================
# Line: 976

rendered_path = keystr(path)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/passes/__init__.py
# Occurrences: Lines 44-53 (5 instances)

v.to(_get_new_device(v.device, location)),

# ==================================================
# Line: 63

lambda v: v.to(_get_new_device(v.device, location))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/_trace.py
# Occurrences: Lines 1124-1126 (4 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 1212-1216 (2 instances)

dynamic_shapes = dynamic_shapes.dynamic_shapes(mod, args, kwargs)

# ==================================================
# Occurrences: Lines 1686-1686 (2 instances)

input_names = _graph_input_names(gm)

# ==================================================
# Occurrences: Lines 1729-1729 (2 instances)

input_names = _graph_input_names(gm)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/unflatten.py
# Line: 603

return_val = torch.fx.Interpreter(self, graph=self.graph).run(
    *flat_args, enable_io_processing=False
)

# ==================================================
# Line: 614

tree_out = torch.fx.Interpreter(self, graph=self.graph).run(
    *flat_args, enable_io_processing=False
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/profiler/_pattern_matcher.py
# Occurrences: Lines 564-567 (2 instances)

not_aligned_dim_timer = benchmark.Timer(
    stmt="torch.mm(matrixA, matrixB)",
    globals={"matrixA": matrixA, "matrixB": matrixB},
)

# ==================================================
# Occurrences: Lines 574-577 (2 instances)

aligned_dim_timer = benchmark.Timer(
    stmt="torch.mm(matrixA, matrixB)",
    globals={"matrixA": matrixA, "matrixB": matrixB},
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/profiler/_utils.py
# Line: 186

return event.start_ns()

# ==================================================
# Occurrences: Lines 202-203 (4 instances)

start_time = event.start_ns()

# ==================================================
# Occurrences: Lines 352-353 (2 instances)

if end is None or end >= len(seq):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/profiler/_memory_profiler.py
# Line: 460

key = TensorKey.from_allocation(i.typed[1])

# ==================================================
# Line: 470

edges[TensorKey.from_allocation(i.typed[1])].input_version = None

# ==================================================
# Occurrences: Lines 767-767 (2 instances)

start_size = len(depends_on_gradient)

# ==================================================
# Occurrences: Lines 786-786 (2 instances)

if len(depends_on_gradient) == start_size:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/contrib/_tensorboard_vis.py
# Occurrences: Lines 125-129 (2 instances)

op, name = name_for(node)

# ==================================================
# Line: 143

op, name = name_for(node)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/resume_execution.py
# Occurrences: Lines 221-223 (2 instances)

push_exc_info_inst = next(push_exc_info_gen, None)

# ==================================================
# Occurrences: Lines 253-257 (2 instances)

cur = next(it)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/backends/tvm.py
# Line: 108

lib = relay.build(mod, target=target, params=params)

# ==================================================
# Line: 142

lib = relay.build(mod, target=target, params=params)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/backends/cudagraphs.py
# Line: 153

interp = boxed_nop(aot_model, aot_inputs)

# ==================================================
# Line: 178

interp = boxed_nop(aot_model, aot_inputs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/backends/distributed.py
# Occurrences: Lines 268-270 (4 instances)

self.tc = torch._guards.TracingContext.try_get()

# ==================================================
# Line: 276

has_tracing_context = torch._guards.TracingContext.try_get() is not None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/graph_deduplication.py
# Line: 276

ready = OrderedSet[Node]()

# ==================================================
# Line: 283

outputs = OrderedSet[Node]()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/repro/after_dynamo.py
# Line: 113

compiled_gm = compiler_fn(copy.deepcopy(gm), example_inputs)

# ==================================================
# Line: 128

compiled_gm = compiler_fn(copy.deepcopy(gm), example_inputs)

# ==================================================
# Occurrences: Lines 232-233 (2 instances)

curdir = os.getcwd()

# ==================================================
# Line: 462

args = run_load_args(options, mod, load_args)

# ==================================================
# Occurrences: Lines 474-478 (2 instances)

args = run_load_args(options, mod, load_args)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/repro/after_aot.py
# Occurrences: Lines 155-155 (2 instances)

return inner_compiled_fn(real_inputs)

# ==================================================
# Occurrences: Lines 211-215 (6 instances)

return inner_compiled_fn(real_inputs)  # type: ignore[operator]

# ==================================================
# Line: 688

new_args = clone_inputs(args)

# ==================================================
# Line: 709

reason = compare_tuples(meta, meta2)

# ==================================================
# Line: 715

new_args = clone_inputs(args)

# ==================================================
# Line: 729

r = super().run_node(n)

# ==================================================
# Occurrences: Lines 739-739 (2 instances)

new_mod, new_args = cast_to_fp64(copy.deepcopy(mod), clone_inputs(args))

# ==================================================
# Occurrences: Lines 746-751 (2 instances)

r = super().run_node(n)

# ==================================================
# Occurrences: Lines 760-760 (2 instances)

new_mod, new_args = cast_to_fp64(copy.deepcopy(mod), clone_inputs(args))

# ==================================================
# Line: 769

r = super().run_node(n)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/utils.py
# Occurrences: Lines 395-400 (2 instances)

pt2_compile_substack = chromium_log.get_pt2_compile_substack()

# ==================================================
# Line: 689

start_ns = time.time_ns()

# ==================================================
# Line: 725

end_ns = time.time_ns()

# ==================================================
# Line: 1979

chromium_start_time = time.time_ns()

# ==================================================
# Line: 1991

time.time_ns(),

# ==================================================
# Occurrences: Lines 2054-2056 (2 instances)

y.grad = clone_input(x.grad, dtype=dtype)

# ==================================================
# Line: 2105

result.grad = clone_input(x.grad, dtype=dtype)

# ==================================================
# Line: 2112

result._dynamo_dynamic_indices = x._dynamo_dynamic_indices.copy()  # type: ignore[attr-defined]

# ==================================================
# Occurrences: Lines 2297-2301 (2 instances)

t0 = time.perf_counter()

# ==================================================
# Line: 3821

for s in x.size():

# ==================================================
# Line: 3827

for s in x.stride():

# ==================================================
# Occurrences: Lines 3833-3834 (2 instances)

size = x.size()

# ==================================================
# Line: 3968

lineno, col = next_valid_char(lineno, col)

# ==================================================
# Line: 3976

lineno, col = next_valid_char(lineno, col)

# ==================================================
# Occurrences: Lines 4023-4028 (3 instances)

left_lineno, left_col = next_valid_char(left_lineno, left_col)

# ==================================================
# Occurrences: Lines 4037-4042 (3 instances)

left_lineno, left_col = next_valid_char(left_lineno, left_col)

# ==================================================
# Line: 4078

linecache.getline(code.co_filename, lineno).rstrip()

# ==================================================
# Line: 4122

line = linecache.getline(code.co_filename, lineno).rstrip()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/test_minifier_common.py
# Line: 141

cwd = _as_posix_path(cwd)

# ==================================================
# Line: 169

cwd = _as_posix_path(cwd)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/debug_utils.py
# Occurrences: Lines 840-843 (2 instances)

data_type, shape_str = match.groups()

# ==================================================
# Occurrences: Lines 853-856 (2 instances)

attr_name, data_type, shape_str, _ = match.groups()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/graph_region_tracker.py
# Line: 377

current_node = region_wrappers[0].next_candidate()

# ==================================================
# Line: 431

current_node = region_wrappers[0].next_candidate()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/decorators.py
# Line: 86

fn = innermost_fn(fn)

# ==================================================
# Line: 93

fn = innermost_fn(fn)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/side_effects.py
# Occurrences: Lines 905-905 (2 instances)

varname_map[name] = cg.tx.output.new_var()

# ==================================================
# Occurrences: Lines 958-958 (2 instances)

varname_map[name] = cg.tx.output.new_var()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/guards.py
# Occurrences: Lines 892-900 (2 instances)

l2_guard_manager_enum = self.get_guard_manager_type(
    source, example_value
)

# ==================================================
# Line: 963

source_name = source.name()

# ==================================================
# Line: 1143

out = base_guard_manager.list_getitem_manager(
    key=source.index,
    source=source_name,
    example_value=example_value,
    guard_manager_enum=guard_manager_enum,
)

# ==================================================
# Line: 1155

out = base_guard_manager.list_getitem_manager(
    key=source.index,
    source=source_name,
    example_value=example_value,
    guard_manager_enum=guard_manager_enum,
)

# ==================================================
# Occurrences: Lines 1303-1306 (2 instances)

f"missing guard manager builder {source} - {source.name()}"

# ==================================================
# Line: 1392

val = hasattr(self.get(base), attr)

# ==================================================
# Line: 1399

guard, [code], provided_guarded_object=self.get(base)

# ==================================================
# Line: 1407

base_example_value = self.get(base)

# ==================================================
# Occurrences: Lines 1479-1480 (2 instances)

val = self.get(guard.name)

# ==================================================
# Line: 1633

guard_hooks_ids = hooks_ids_fn(get_hooks())

# ==================================================
# Line: 1641

return guard_hooks_ids == hooks_ids_fn(get_hooks())

# ==================================================
# Occurrences: Lines 1648-1649 (2 instances)

value = self.get(guard.name)

# ==================================================
# Line: 1741

get_verbose_code_parts(code, guard),

# ==================================================
# Line: 1754

get_verbose_code_parts(code, guard),

# ==================================================
# Line: 1766

verbose_code_parts = get_verbose_code_parts(code, guard)

# ==================================================
# Line: 1865

t = type(value)

# ==================================================
# Line: 1871

t = type(value)

# ==================================================
# Line: 1881

t = type(value)

# ==================================================
# Line: 1888

t = type(value)

# ==================================================
# Occurrences: Lines 2087-2094 (2 instances)

python_code_parts, verbose_code_parts = _get_code_parts(
    ("python", "verbose_python")
)

# ==================================================
# Line: 2311

guard_manager = self.get_guard_manager(guard)

# ==================================================
# Line: 2397

self.get_guard_manager(guard).add_dynamic_indices_guard(

# ==================================================
# Line: 2407

self.get_guard_manager(guard).add_no_hasattr_guard(

# ==================================================
# Line: 2524

node_ = super().visit(node)

# ==================================================
# Line: 2533

return super().visit(node)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/eval_frame.py
# Line: 343

self.forward = self.dynamo_ctx(self._orig_mod.__call__)

# ==================================================
# Line: 357

self.forward = self.dynamo_ctx(self._orig_mod.__call__)

# ==================================================
# Occurrences: Lines 667-667 (2 instances)

prior = set_eval_frame(None)

# ==================================================
# Occurrences: Lines 717-717 (2 instances)

set_eval_frame(None)

# ==================================================
# Occurrences: Lines 888-888 (2 instances)

prior = set_eval_frame(None)

# ==================================================
# Occurrences: Lines 897-897 (2 instances)

set_eval_frame(None)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/test_case.py
# Line: 182

search_path = inspect.getfile(cls)

# ==================================================
# Line: 195

f"Test requires a specific Python version but not found in path {inspect.getfile(cls)}"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/convert_frame.py
# Occurrences: Lines 248-248 (2 instances)

torch._C._is_default_mobile_cpu_allocator_set()

# ==================================================
# Occurrences: Lines 282-282 (2 instances)

torch._C._is_default_mobile_cpu_allocator_set()

# ==================================================
# Occurrences: Lines 415-417 (4 instances)

start_ts = time.time()

# ==================================================
# Occurrences: Lines 798-798 (2 instances)

last_attempt_start_time = start_time = time.time()

# ==================================================
# Occurrences: Lines 835-835 (2 instances)

last_attempt_start_time = time.time()

# ==================================================
# Line: 1089

start_time_ns = time.time_ns()

# ==================================================
# Line: 1116

fail_reason = str(e)

# ==================================================
# Line: 1150

f"{type(e).__qualname__}: {str(e)}"

# ==================================================
# Line: 1190

dynamo_time_before_restart = (time.time_ns() - start_time_ns) / 1e9

# ==================================================
# Line: 1412

is_skipfile = trace_rules.check(frame.f_code)

# ==================================================
# Line: 1430

elif trace_rules.check(frame.f_code):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/bytecode_transformation.py
# Occurrences: Lines 620-624 (2 instances)

b = next(bytes_iter)

# ==================================================
# Occurrences: Lines 651-655 (8 instances)

start = decode_exception_table_varint(exntab_iter) * 2

# ==================================================
# Occurrences: Lines 852-855 (2 instances)

entry, inst_entry = step()

# ==================================================
# Occurrences: Lines 1261-1263 (4 instances)

idx = names[name] = len(names)

# ==================================================
# Occurrences: Lines 1300-1304 (4 instances)

instructions[i].arg = (get_name_index(instructions[i].argval) << 1) + (

# ==================================================
# Occurrences: Lines 1310-1314 (4 instances)

instructions[i].arg = (get_name_index(instructions[i].argval) << 1) + (

# ==================================================
# Occurrences: Lines 1320-1320 (2 instances)

(get_name_index(instructions[i].argval) << 2)

# ==================================================
# Occurrences: Lines 1345-1345 (2 instances)

instructions[i].arg = get_name_index(instructions[i].argval)

# ==================================================
# Line: 1438

tmp_code = types.CodeType(*[code_options[k] for k in keys])

# ==================================================
# Line: 1466

return instructions, types.CodeType(*[code_options[k] for k in keys])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/codegen.py
# Line: 668

output = create_call_function(nargs, push_null)

# ==================================================
# Line: 674

output = create_call_function(nargs, push_null)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/symbolic_convert.py
# Occurrences: Lines 511-516 (2 instances)

stack_above_dynamo = get_stack_above_dynamo()

# ==================================================
# Occurrences: Lines 1480-1483 (2 instances)

return ConstantVariable.create(value=inst.argval)

# ==================================================
# Occurrences: Lines 1814-1815 (2 instances)

from_vt = self.pop()

# ==================================================
# Occurrences: Lines 1846-1849 (2 instances)

val = self.pop()

# ==================================================
# Occurrences: Lines 1856-1858 (3 instances)

_exc = self.pop()

# ==================================================
# Line: 1919

self.push(self.exn_vt_stack.get_current_exception())

# ==================================================
# Line: 1942

block_stack_entry = self.block_stack.pop()

# ==================================================
# Occurrences: Lines 1963-1965 (2 instances)

block_stack_entry = self.block_stack.pop()

# ==================================================
# Occurrences: Lines 2177-2180 (3 instances)

argsvars = self.pop()

# ==================================================
# Occurrences: Lines 2191-2197 (3 instances)

null = self.pop()

# ==================================================
# Occurrences: Lines 2225-2227 (2 instances)

argnames = self.pop()

# ==================================================
# Occurrences: Lines 2268-2270 (2 instances)

dummy = self.pop()

# ==================================================
# Occurrences: Lines 2483-2484 (2 instances)

fn_name = self.pop()

# ==================================================
# Occurrences: Lines 2498-2504 (4 instances)

closure = self.pop()

# ==================================================
# Occurrences: Lines 2578-2586 (5 instances)

a = self.pop()

# ==================================================
# Occurrences: Lines 2592-2595 (4 instances)

a = self.pop()

# ==================================================
# Occurrences: Lines 2607-2608 (2 instances)

a = self.pop()

# ==================================================
# Occurrences: Lines 3062-3063 (2 instances)

tos = self.pop()

# ==================================================
# Occurrences: Lines 3085-3087 (2 instances)

fn = self.pop()

# ==================================================
# Occurrences: Lines 3409-3412 (4 instances)

cell_var = side_effects.track_cell_new()

# ==================================================
# Line: 4125

val = self.pop()

# ==================================================
# Line: 4147

self.pop()

# ==================================================
# Line: 4163

val = self.pop()

# ==================================================
# Line: 4180

self.pop()  # Python 3.12 uses new opcode END_SEND

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/output_graph.py
# Line: 1999

binds_symbol = placeholder_binds_symbol(node) is not None

# ==================================================
# Line: 2038

symbol = placeholder_binds_symbol(node)

# ==================================================
# Line: 2465

rv.node.meta["nn_module_stack"] = nn_module_stack.copy()

# ==================================================
# Line: 2498

rv.node.meta["nn_module_stack"] = nn_module_stack.copy()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/trace_rules.py
# Occurrences: Lines 2930-2934 (2 instances)

obj = _load_obj_from_str(x[0])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/testing.py
# Line: 105

name = remove_optimized_module_prefix(name)

# ==================================================
# Line: 118

name = remove_optimized_module_prefix(name)

# ==================================================
# Occurrences: Lines 376-379 (4 instances)

val1a = opt_fn(*args1)

# ==================================================
# Occurrences: Lines 470-472 (4 instances)

fn = getattr(cls, name)

# ==================================================
# Occurrences: Lines 482-482 (2 instances)

setattr(DummyTestClass, name, getattr(cls, name))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/compiled_autograd.py
# Line: 417

psymints = [self.to_proxy(e) for e in ctx._get_compiled_autograd_symints()]

# ==================================================
# Line: 478

symints = ctx._get_compiled_autograd_symints()

# ==================================================
# Occurrences: Lines 506-506 (3 instances)

ph.name = make_unique(node.name)

# ==================================================
# Occurrences: Lines 519-524 (6 instances)

qualname = self.fx_tracer.get_fresh_qualname(name)

# ==================================================
# Occurrences: Lines 532-545 (12 instances)

result = self.fx_tracer.graph.node_copy(
    node, lambda n: value_remap[n]
)

# ==================================================
# Occurrences: Lines 899-901 (2 instances)

before = len(self.fx_tracer.graph.nodes)

# ==================================================
# Occurrences: Lines 910-911 (2 instances)

next(it)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/misc.py
# Line: 1135

key = args[0].as_python_constant()

# ==================================================
# Line: 1163

key = args[0].as_python_constant()

# ==================================================
# Line: 1859

return self.wrap_state(self.random.getstate())

# ==================================================
# Line: 1866

state = self.random.getstate()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/tensor.py
# Occurrences: Lines 838-843 (2 instances)

and fqn(type(dtype.as_python_constant())) == "torch.tensortype"

# ==================================================
# Occurrences: Lines 1477-1488 (2 instances)

tx.output.create_proxy(
    "call_function", numpy_attr_wrapper, (self.as_proxy(), name), {}
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/functions.py
# Line: 154

ba[name] = wrap_bound_arg(tx, rem_kw.pop(name))

# ==================================================
# Line: 176

ba[name] = wrap_bound_arg(tx, rem_kw.pop(name))

# ==================================================
# Occurrences: Lines 412-412 (2 instances)

contents_var = variables.DeletedVariable()

# ==================================================
# Occurrences: Lines 424-424 (2 instances)

contents_var = variables.DeletedVariable()

# ==================================================
# Line: 688

return self.next_variable(tx)

# ==================================================
# Occurrences: Lines 704-706 (2 instances)

tracer = self._get_inline_tracer(tx)

# ==================================================
# Line: 721

tracer = self._get_inline_tracer(tx)

# ==================================================
# Line: 761

if self.next_variable(tx):

# ==================================================
# Line: 781

tracer = self._get_inline_tracer(tx)

# ==================================================
# Line: 792

retval = self.next_variable(tx)

# ==================================================
# Line: 858

self.next_variable(tx)

# ==================================================
# Occurrences: Lines 922-925 (2 instances)

assert is_generator(self.vt.get_code())

# ==================================================
# Line: 1218

code = self.get_code()

# ==================================================
# Line: 1224

tuple(make_cell(None) for _ in range(len(self.get_code().co_freevars))),

# ==================================================
# Line: 1382

graph_break_msg = kwargs.get("msg", None)

# ==================================================
# Line: 1394

skip_frame_msg = kwargs.get("msg", None)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/ctx_manager.py
# Occurrences: Lines 488-489 (2 instances)

batch_size_value = batch_size.as_python_constant()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/nn_module.py
# Line: 369

out = VariableTracker.build(tx, subobj, NNModuleSource(source))

# ==================================================
# Line: 405

return VariableTracker.build(tx, subobj, NNModuleSource(source))

# ==================================================
# Line: 539

module = tx.output.get_submodule(key)

# ==================================================
# Line: 592

submod = tx.output.get_submodule(key)

# ==================================================
# Line: 601

fn = getattr(module, name)

# ==================================================
# Line: 619

fn = getattr(module, name)

# ==================================================
# Line: 732

args[0].as_python_constant() in module._modules

# ==================================================
# Occurrences: Lines 746-748 (2 instances)

key = args[0].as_python_constant()

# ==================================================
# Occurrences: Lines 769-770 (2 instances)

keys = list(range(len(module)))[args[0].as_python_constant()]

# ==================================================
# Occurrences: Lines 781-786 (2 instances)

new_module = module[args[0].as_python_constant()]

# ==================================================
# Line: 800

key = args[0].as_python_constant()

# ==================================================
# Line: 829

fn = getattr(module, name).__func__

# ==================================================
# Line: 868

if type(value) is torch.jit._script.RecursiveScriptModule:

# ==================================================
# Occurrences: Lines 875-880 (2 instances)

if type(value) is lazy_value_to_become:

# ==================================================
# Occurrences: Lines 955-958 (2 instances)

fn = getattr(self.value_type, name)

# ==================================================
# Line: 1120

hooks_dict = getattr(self.value, name)

# ==================================================
# Line: 1145

hooks_dict = getattr(self.value, name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/builder.py
# Line: 713

base = self.get_source()

# ==================================================
# Occurrences: Lines 719-721 (2 instances)

key = LazyVariableTracker.create(k, source_key)

# ==================================================
# Occurrences: Lines 793-797 (2 instances)

func_src = AttrSource(self.get_source(), "func")

# ==================================================
# Line: 804

keywords_source = AttrSource(self.get_source(), "keywords")

# ==================================================
# Line: 818

self.get_source().make_guard(GuardBuilder.TYPE_MATCH),

# ==================================================
# Occurrences: Lines 1356-1359 (2 instances)

key = LazyVariableTracker.create(k, source_key)

# ==================================================
# Line: 1832

return ConstantVariable.create(value=value, source=self.source)

# ==================================================
# Line: 1839

result = ConstantVariable.create(value=value, source=self.source)

# ==================================================
# Line: 1932

if type(value) in (

# ==================================================
# Line: 1957

subclass_type = type(value)

# ==================================================
# Line: 2022

type(value),

# ==================================================
# Line: 2208

name = self.source.name()

# ==================================================
# Line: 2221

normalized_source_name = normalize_source_name(self.source.name())

# ==================================================
# Line: 3073

name = source.name()

# ==================================================
# Line: 3113

record_automatic_dynamic(tx, name, e)

# ==================================================
# Line: 3143

frame_state_entry = record_automatic_dynamic(tx, name, e)

# ==================================================
# Line: 3197

normalized_source_name = normalize_source_name(source.name())

# ==================================================
# Line: 3448

value_type = type(value)

# ==================================================
# Occurrences: Lines 3512-3514 (2 instances)

for name in namedtuple_fields(type(value))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/base.py
# Occurrences: Lines 281-283 (2 instances)

value = value.unwrap()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/builtin.py
# Occurrences: Lines 442-445 (2 instances)

return TupleVariable([*a.items, *b.unpack_var_sequence(tx)])

# ==================================================
# Line: 494

[*a.items, *b.unpack_var_sequence(tx)],

# ==================================================
# Line: 515

seq = b.unpack_var_sequence(tx)

# ==================================================
# Occurrences: Lines 896-896 (2 instances)

has_constant_handler = obj.has_constant_handler(args, kwargs)

# ==================================================
# Occurrences: Lines 912-912 (2 instances)

has_constant_handler = obj.has_constant_handler(args, kwargs)

# ==================================================
# Line: 1267

resolved_fn = getattr(self.fn, name)

# ==================================================
# Line: 1275

resolved_fn = getattr(self.fn, name)

# ==================================================
# Line: 1444

raw_b = b.as_python_constant()

# ==================================================
# Line: 1472

b.as_python_constant(),

# ==================================================
# Line: 1801

arg_type = arg.python_type()

# ==================================================
# Line: 1827

return issubclass(arg.python_type(), ty)

# ==================================================
# Line: 2076

member = getattr(obj.value, name)

# ==================================================
# Line: 2086

member = getattr(obj.value, name)

# ==================================================
# Line: 2127

name = name_var.as_python_constant()

# ==================================================
# Line: 2234

getattr_var = obj.var_getattr(tx, name_var.as_python_constant())

# ==================================================
# Line: 2332

constant_result = id(args[0].value)

# ==================================================
# Line: 2340

return variables.ConstantVariable.create(id(args[0].value))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/user_defined.py
# Occurrences: Lines 460-462 (2 instances)

items = args[0].force_unpack_var_sequence(tx)

# ==================================================
# Line: 471

items = args[0].force_unpack_var_sequence(tx)

# ==================================================
# Line: 550

cm_obj = tx.output.side_effects.track_new_user_defined_object(
    variables.BuiltinVariable(object),
    self,
    args,
)

# ==================================================
# Line: 563

items = args[0].force_unpack_var_sequence(tx)

# ==================================================
# Line: 622

var = tx.output.side_effects.track_new_user_defined_object(
    variables.BuiltinVariable(object), self, args
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/lists.py
# Line: 638

return ConstantVariable.create(None)

# ==================================================
# Occurrences: Lines 659-660 (2 instances)

slice_within_maxlen = slice(None, maxlen)

# ==================================================
# Occurrences: Lines 671-672 (2 instances)

slice_within_maxlen = slice(None, maxlen)

# ==================================================
# Occurrences: Lines 680-682 (2 instances)

result = super().call_method(tx, name, args, kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/dicts.py
# Line: 440

return ConstantVariable.create(None)

# ==================================================
# Line: 481

return ConstantVariable.create(None)

# ==================================================
# Line: 487

return ConstantVariable.create(None)

# ==================================================
# Line: 505

return ConstantVariable.create(None)

# ==================================================
# Line: 530

return ConstantVariable.create(None)

# ==================================================
# Line: 552

x = ConstantVariable.create(None)

# ==================================================
# Line: 566

return ConstantVariable.create(None)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/higher_order_ops.py
# Occurrences: Lines 305-310 (4 instances)

state = _CacheKeyState(fake_mode.shape_env)

# ==================================================
# Occurrences: Lines 323-324 (4 instances)

a_flat, _ = pytree.tree_flatten((a_node.args, a_node.kwargs))

# ==================================================
# Occurrences: Lines 335-336 (4 instances)

a_flat, _ = pytree.tree_flatten((a_node.args, a_node.kwargs))

# ==================================================
# Occurrences: Lines 345-346 (4 instances)

a_flat, _ = pytree.tree_flatten((a_node.args, a_node.kwargs))

# ==================================================
# Occurrences: Lines 421-423 (6 instances)

tracer.create_graph_input(arg_name, a.python_type(), example_value)

# ==================================================
# Occurrences: Lines 430-432 (2 instances)

new_proxy = tracer.create_graph_input(
    arg_name, a.python_type(), example_value
)

# ==================================================
# Occurrences: Lines 438-443 (2 instances)

a = wrap_fx_proxy_cls(
    target_cls=type(a),
    tx=tx,
    proxy=new_proxy,
    example_value=example_value,
)

# ==================================================
# Occurrences: Lines 470-487 (10 instances)

tracer.create_graph_input(arg_name, a.python_type(), example_value)

# ==================================================
# Line: 702

prev_side_effects = tx.output.side_effects.clone()

# ==================================================
# Line: 708

new_side_effects = tx.output.side_effects.clone()

# ==================================================
# Occurrences: Lines 1021-1023 (2 instances)

return true_fn.call_function(tx, operands.unpack_var_sequence(tx), {})

# ==================================================
# Line: 1039

operands_seq = operands.unpack_var_sequence(tx)

# ==================================================
# Line: 3000

bwd_tracer = torch._dynamo.output_graph.SubgraphTracer(
    tx.output,
    parent=fwd_tracer,
    source_target="autograd.Function",
)

# ==================================================
# Line: 3039

(bwd_out, _), bwd_graph, bwd_freevars = speculate_subgraph(
    tx,
    bwd_fn,
    bwd_args,
    kwargs,
    "autograd.Function",
    enable_grad=False,
    set_subgraph_inputs="manual",
    restore_side_effects=False,
    tracer=bwd_tracer,
)

# ==================================================
# Line: 3056

bwd_tracer = torch._dynamo.output_graph.SubgraphTracer(
    tx.output,
    parent=fwd_tracer,
    source_target="autograd.Function",
)

# ==================================================
# Line: 3083

(bwd_out, _), bwd_graph, bwd_freevars = speculate_subgraph(
    tx,
    bwd_fn,
    bwd_args,
    kwargs,
    "autograd.Function",
    enable_grad=False,
    set_subgraph_inputs="manual",
    restore_side_effects=False,
    tracer=bwd_tracer,
)

# ==================================================
# Line: 3152

fwd_nn_modules = tx.output.tracing_context.module_context.copy_graphstate()

# ==================================================
# Line: 3217

bwd_nn_modules = tx.output.tracing_context.module_context.copy_graphstate()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/torch_function.py
# Occurrences: Lines 154-157 (4 instances)

inp0 = torch.ones(1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/constant.py
# Line: 169

method = getattr(self.value, name)

# ==================================================
# Line: 176

return ConstantVariable.create(getattr(self.value, name)())

# ==================================================
# Line: 200

method = getattr(self.value, name)

# ==================================================
# Occurrences: Lines 207-211 (2 instances)

round(self.value, args[0].as_python_constant())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/distributed.py
# Occurrences: Lines 227-229 (2 instances)

method(self.value, *args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/iter.py
# Line: 88

seq = args[0].unpack_var_sequence(tx)

# ==================================================
# Line: 153

iterable = args[0].unpack_var_sequence(tx)

# ==================================================
# Line: 188

seq = args[0].unpack_var_sequence(tx)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/torch.py
# Occurrences: Lines 304-314 (4 instances)

ctx = GradModeVariable.create(tx, False)

# ==================================================
# Line: 1049

ind = args[0].as_python_constant()

# ==================================================
# Line: 1065

if args[0].is_python_constant() and args[0].as_python_constant() is None:

# ==================================================
# Occurrences: Lines 1112-1114 (4 instances)

arg_type = flat_arg_vt.python_type()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/polyfills/pytree.py
# Line: 139

assert len(self._children) == 0

# ==================================================
# Line: 150

num_children = len(self._children)

# ==================================================
# Occurrences: Lines 228-232 (2 instances)

children, metadata, *_ = optree.tree_flatten_one_level(
    node,
    none_is_leaf=True,
    namespace="torch",
)

# ==================================================
# Occurrences: Lines 277-281 (2 instances)

children, metadata, *_ = optree.tree_flatten_one_level(
    node,
    none_is_leaf=True,
    namespace="torch",
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/amp/autocast_mode.py
# Occurrences: Lines 516-519 (4 instances)

args[0]._fwd_used_autocast = torch.is_autocast_enabled(device_type)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_meta_registrations.py
# Line: 234

signal_ndim = len(dim)

# ==================================================
# Line: 267

for i in range(len(dim)):

# ==================================================
# Line: 335

output = self.new_empty(
    out_sizes, dtype=utils.corresponding_complex_dtype(self.dtype)
)

# ==================================================
# Line: 347

working_tensor = self.new_empty(
    out_sizes, dtype=utils.corresponding_complex_dtype(self.dtype)
)

# ==================================================
# Occurrences: Lines 375-382 (2 instances)

out = self.new_empty(
    out_sizes, dtype=utils.corresponding_complex_dtype(self.dtype)
)

# ==================================================
# Occurrences: Lines 464-469 (2 instances)

output = self.new_empty(out_sizes, dtype=toRealValueType(self.dtype))

# ==================================================
# Line: 479

temp = self.clone(memory_format=torch.contiguous_format)

# ==================================================
# Line: 491

out = self.new_empty(out_sizes, dtype=toRealValueType(self.dtype))

# ==================================================
# Occurrences: Lines 548-550 (2 instances)

assert weight.size(0) == bias.size(0), "output size mismatch"

# ==================================================
# Occurrences: Lines 1239-1248 (3 instances)

P = A.new_empty(sizes)

# ==================================================
# Occurrences: Lines 1279-1283 (2 instances)

pivots = A.new_empty(sizes, dtype=torch.int)

# ==================================================
# Occurrences: Lines 1371-1382 (6 instances)

P = LU.new_empty(sizes)

# ==================================================
# Occurrences: Lines 1486-1487 (2 instances)

U = A.new_empty([0])

# ==================================================
# Occurrences: Lines 2427-2428 (2 instances)

save_mean = input_tensor.new_empty((0,))

# ==================================================
# Occurrences: Lines 3196-3203 (4 instances)

out = input.new_empty(out_shape)

# ==================================================
# Occurrences: Lines 3485-3486 (2 instances)

dim1 = batch1.size(1)

# ==================================================
# Occurrences: Lines 3497-3498 (2 instances)

f"Incompatible matrix sizes for bmm ({batch1.size(1)}x{batch1.size(2)} "

# ==================================================
# Occurrences: Lines 4336-4339 (2 instances)

output = batch2.new_empty(output_size).to(out_dtype)

# ==================================================
# Occurrences: Lines 5507-5516 (3 instances)

ensure_nonempty_dim(self.dim()) == ensure_nonempty_dim(index.dim()),

# ==================================================
# Line: 5526

index_d_size = ensure_nonempty_size(index, d)

# ==================================================
# Line: 5533

ensure_nonempty_dim(self.dim()) == ensure_nonempty_dim(index.dim()),

# ==================================================
# Occurrences: Lines 5646-5647 (2 instances)

seed = torch.empty((), dtype=torch.long, device="meta")

# ==================================================
# Occurrences: Lines 5704-5705 (2 instances)

seed = torch.empty((), dtype=torch.long, device="meta")

# ==================================================
# Occurrences: Lines 5745-5746 (2 instances)

seed = torch.empty((), dtype=torch.long, device="meta")

# ==================================================
# Occurrences: Lines 5909-5910 (2 instances)

seed = torch.empty((), dtype=torch.long, device="meta")

# ==================================================
# Line: 6030

batch_size = query.size(0) if cum_seq_q is None else cum_seq_q.numel() - 1

# ==================================================
# Line: 6045

total_q = query.size(0)

# ==================================================
# Occurrences: Lines 6070-6071 (2 instances)

seed = torch.empty((), dtype=torch.long, device="meta")

# ==================================================
# Occurrences: Lines 6161-6162 (2 instances)

seed = torch.empty((), dtype=torch.long, device="meta")

# ==================================================
# Line: 6280

mat2.size(0) % 16 == 0 and mat2.size(1) % 16 == 0,

# ==================================================
# Line: 6287

n = mat2.size(1)

# ==================================================
# Line: 6387

return torch.empty(self.size(0), mat2.size(1), dtype=_out_dtype, device=self.device)

# ==================================================
# Occurrences: Lines 6614-6615 (2 instances)

hy = torch.empty_like(cx, memory_format=torch.contiguous_format)

# ==================================================
# Occurrences: Lines 6638-6640 (2 instances)

is_input_packed = len(batch_sizes) != 0

# ==================================================
# Occurrences: Lines 6704-6708 (2 instances)

hy = torch.empty(0, device=input.device)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_lobpcg.py
# Occurrences: Lines 859-864 (2 instances)

E, Z = _utils.symeig(M, largest)

# ==================================================
# Line: 874

E_, Z = _utils.symeig(M, largest)

# ==================================================
# Line: 881

nc = self.update_converged_count()

# ==================================================
# Occurrences: Lines 1013-1014 (2 instances)

UBU = _utils.qform(self.B, U)

# ==================================================
# Line: 1023

nz = torch.where(abs(d) != 0.0)

# ==================================================
# Occurrences: Lines 1029-1031 (3 instances)

UBU = _utils.qform(self.B, U)

# ==================================================
# Occurrences: Lines 1095-1096 (2 instances)

BU = mm_B(self.B, U)

# ==================================================
# Occurrences: Lines 1114-1116 (3 instances)

BU = mm_B(self.B, U)

# ==================================================
# Occurrences: Lines 1126-1128 (3 instances)

VBU = mm(V.mT, BU)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_functional_collectives.py
# Occurrences: Lines 560-562 (4 instances)

input_split_sizes[dst] = self.numel()

# ==================================================
# Occurrences: Lines 717-727 (8 instances)

if group_size != -1 and group_size != len(rs):

# ==================================================
# Occurrences: Lines 735-736 (2 instances)

rankset = dist.get_process_group_ranks(pg)

# ==================================================
# Occurrences: Lines 747-748 (2 instances)

rankset = dist.get_process_group_ranks(pg)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/run.py
# Occurrences: Lines 645-647 (2 instances)

min_nodes = max_nodes = int(arr[0])

# ==================================================
# Line: 661

num_proc = os.cpu_count()

# ==================================================
# Occurrences: Lines 667-684 (8 instances)

num_proc = torch.cuda.device_count()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/algorithms/ddp_comm_hooks/powerSGD_hook.py
# Line: 574

uncompressed_tensors_memory = fut.value()[0].div_(world_size)

# ==================================================
# Line: 592

state.p_memory_dict[bucket_index] = fut.value()

# ==================================================
# Line: 614

state.q_memory_dict[bucket_index] = fut.value().div_(world_size)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/algorithms/ddp_comm_hooks/default_hooks.py
# Occurrences: Lines 152-157 (4 instances)

bucket.set_buffer(bucket.buffer().to(torch.float16))

# ==================================================
# Occurrences: Lines 191-196 (4 instances)

bucket.set_buffer(bucket.buffer().to(torch.bfloat16))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/algorithms/_quantization/quantization.py
# Occurrences: Lines 115-116 (4 instances)

input_tensors = _quantize_tensor(args[1], qtype)

# ==================================================
# Occurrences: Lines 126-126 (2 instances)

out_tensors = _quantize_tensor_list(tensors, qtype)

# ==================================================
# Occurrences: Lines 138-138 (2 instances)

input_tensors = _quantize_tensor(args[1], qtype)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/utils.py
# Occurrences: Lines 106-110 (4 instances)

return (obj.to(target_device),)

# ==================================================
# Occurrences: Lines 118-118 (2 instances)

output = obj.to(target_device)

# ==================================================
# Occurrences: Lines 172-174 (2 instances)

already_allocated = tensor._typed_storage()._size() == size.numel()

# ==================================================
# Occurrences: Lines 235-235 (2 instances)

od[key] = apply(value)

# ==================================================
# Occurrences: Lines 241-241 (2 instances)

return {key: apply(value) for key, value in x.items()}

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py
# Line: 433

time.monotonic() - self._cache_duration, 0

# ==================================================
# Line: 465

self._last_sync_time = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/etcd_rendezvous.py
# Line: 388

state = json.loads(active_version.value)

# ==================================================
# Line: 414

state = json.loads(active_version.value)

# ==================================================
# Occurrences: Lines 536-540 (4 instances)

assert len(state["participants"]) < self._num_max_workers, (

# ==================================================
# Occurrences: Lines 546-550 (4 instances)

if len(state["participants"]) == self._num_max_workers:

# ==================================================
# Line: 691

active_version, state = self.get_rdzv_state()

# ==================================================
# Line: 747

active_version, state = self.get_rdzv_state()

# ==================================================
# Line: 765

active_version, state = self.get_rdzv_state()

# ==================================================
# Occurrences: Lines 795-795 (2 instances)

active_version, state = self.get_rdzv_state()

# ==================================================
# Occurrences: Lines 821-821 (2 instances)

active_version, state = self.get_rdzv_state()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/etcd_server.py
# Occurrences: Lines 190-191 (2 instances)

sock = find_free_port()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/multiprocessing/api.py
# Occurrences: Lines 336-337 (2 instances)

stdouts = dict.fromkeys(range(nprocs), SYS_STREAM)

# ==================================================
# Line: 536

return self._poll()

# ==================================================
# Line: 543

pr = self._poll()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/timer/file_based_local_timer.py
# Line: 367

start = time.time()

# ==================================================
# Line: 396

now = time.time()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/timer/local_timer.py
# Occurrences: Lines 63-63 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 71-71 (2 instances)

wait = wait - (time.time() - start)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/agent/server/api.py
# Line: 611

role_sizes = defaultdict(lambda: 0)

# ==================================================
# Line: 618

role_ranks = defaultdict(lambda: 0)

# ==================================================
# Occurrences: Lines 707-711 (3 instances)

start_time = time.monotonic()

# ==================================================
# Occurrences: Lines 726-726 (2 instances)

self._total_execution_time = int(time.monotonic() - start_time)

# ==================================================
# Occurrences: Lines 760-764 (2 instances)

start_time = time.perf_counter()

# ==================================================
# Line: 938

start = time.time()

# ==================================================
# Line: 948

time.time() - start,

# ==================================================
# Line: 956

time.time() - start,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_state_dict_utils.py
# Occurrences: Lines 406-406 (2 instances)

t = torch.empty(*tuple(obj.size()), dtype=obj.dtype)

# ==================================================
# Occurrences: Lines 429-431 (4 instances)

return torch.empty(*tuple(obj.size()), dtype=obj.dtype).pin_memory()

# ==================================================
# Line: 656

local_state_dict[key] = local_state_dict[key].cpu()

# ==================================================
# Line: 668

local_state_dict[key] = local_state_dict[key].cpu()

# ==================================================
# Occurrences: Lines 694-699 (4 instances)

value.detach().to(device),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_symmetric_memory/__init__.py
# Line: 165

backend_stream.wait_stream(torch.cuda.current_stream())

# ==================================================
# Line: 246

backend_stream.wait_stream(torch.cuda.current_stream())

# ==================================================
# Line: 255

stream = torch.cuda.current_stream()

# ==================================================
# Line: 268

stream = torch.cuda.current_stream()

# ==================================================
# Line: 274

torch.cuda.current_stream().wait_stream(backend_stream)

# ==================================================
# Line: 330

backend_stream.wait_stream(torch.cuda.current_stream())

# ==================================================
# Line: 348

stream = torch.cuda.current_stream()

# ==================================================
# Line: 417

torch.cuda.current_stream().wait_stream(backend_stream)

# ==================================================
# Line: 545

A_scale_shard = A_scale.movedim(gather_dim, 0).flatten(0, -2)

# ==================================================
# Line: 571

A_scale.movedim(gather_dim, 0).flatten(0, -2).chunk(group.size())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_init_utils.py
# Occurrences: Lines 330-333 (2 instances)

all_modules = all(isinstance(state, nn.Module) for state in ignored_states)

# ==================================================
# Occurrences: Lines 339-340 (2 instances)

if not all(isinstance(state, nn.Module) for state in ignored_states):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_runtime_utils.py
# Occurrences: Lines 259-265 (3 instances)

state._unshard_stream = state._device_handle.Stream(priority=high_priority)

# ==================================================
# Line: 870

grad_to_offload = _accumulate_sharded_grad(
    state, handle, new_sharded_grad
)

# ==================================================
# Line: 881

grad_to_offload = _accumulate_sharded_grad(state, handle, new_sharded_grad)

# ==================================================
# Line: 1096

current_stream = state._device_handle.current_stream()

# ==================================================
# Line: 1107

state._device_handle.current_stream().synchronize()

# ==================================================
# Line: 1446

hook = functools.partial(_post_backward_hook, state, handle)

# ==================================================
# Line: 1463

functools.partial(_post_backward_hook, state, handle)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_optim_utils.py
# Occurrences: Lines 1387-1387 (3 instances)

curr_non_tensor_value = gathered_state.get(name, None)

# ==================================================
# Occurrences: Lines 1398-1398 (3 instances)

curr_scalar_tensor_value = gathered_state.get(name, None)

# ==================================================
# Occurrences: Lines 1447-1450 (4 instances)

value = value.reshape(flat_param._shapes[param_idx])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/fully_sharded_data_parallel.py
# Line: 1765

new_osd["param_groups"] = copy.deepcopy(osd["param_groups"])

# ==================================================
# Line: 1792

new_osd["param_groups"] = copy.deepcopy(osd["param_groups"])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_fully_shard/_fsdp_param_group.py
# Occurrences: Lines 61-69 (3 instances)

self.all_gather_copy_in_stream = self.device_handle.Stream(
    priority=high_priority
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_fully_shard/_fsdp_init.py
# Occurrences: Lines 239-242 (4 instances)

tensor_on_device = nn.Parameter(tensor.to(device))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_fully_shard/_fsdp_collectives.py
# Line: 426

reduce_scatter_event = reduce_scatter_stream.record_event()

# ==================================================
# Line: 438

post_reduce_stream.record_event(),

# ==================================================
# Line: 498

fsdp_param.grad_offload_event = reduce_scatter_stream.record_event()

# ==================================================
# Line: 515

post_reduce_event = post_reduce_stream.record_event()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_fully_shard/_fsdp_param.py
# Line: 349

self._orig_size = param_data.size()

# ==================================================
# Occurrences: Lines 360-365 (2 instances)

f"{param_data.size()} (world size: {shard_world_size})"

# ==================================================
# Line: 476

all_gather_outputs = self._unflatten_all_gather_outputs()

# ==================================================
# Line: 489

all_gather_outputs = self._unflatten_all_gather_outputs()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_debug_utils.py
# Occurrences: Lines 49-53 (2 instances)

begin = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_flat_param.py
# Occurrences: Lines 401-406 (6 instances)

assert len(param_infos) == len(shapes)

# ==================================================
# Occurrences: Lines 547-550 (4 instances)

rank=process_group.rank(), world_size=process_group.size()

# ==================================================
# Line: 688

padding_tensor = _construct_padding_tensor(
    numel_to_pad, dtype, False, device
)

# ==================================================
# Line: 745

padding_tensor = _construct_padding_tensor(
    numel_to_pad, dtype, False, device
)

# ==================================================
# Line: 842

padding_tensor = _construct_padding_tensor(
    numel_to_pad, dtype, False, device
)

# ==================================================
# Line: 855

padding_tensor = _construct_padding_tensor(
    numel_to_pad, dtype, False, device
)

# ==================================================
# Line: 2029

param = getattr(module, param_name)

# ==================================================
# Line: 2046

param.grad = torch.empty_like(param)

# ==================================================
# Line: 2062

param = getattr(module, param_name)

# ==================================================
# Line: 2072

param.grad = torch.empty_like(param)

# ==================================================
# Occurrences: Lines 2187-2193 (4 instances)

param.grad.data = grad[
    offset : offset + numel_in_shard
].reshape(param.shape)

# ==================================================
# Occurrences: Lines 2279-2279 (2 instances)

param_changed = getattr(module, param_name) is not param

# ==================================================
# Occurrences: Lines 2293-2296 (4 instances)

param = getattr(module, param_name)

# ==================================================
# Occurrences: Lines 2308-2308 (2 instances)

expected_shape = torch.Size([numel_in_shard])

# ==================================================
# Occurrences: Lines 2329-2329 (2 instances)

expected_shape = torch.Size([numel_in_shard])

# ==================================================
# Line: 2351

if getattr(module, param_name) is not getattr(prim_module, prim_param_name):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_wrap_utils.py
# Line: 60

overridden_module_classes = _override_module_mixed_precision(
    root_module, mixed_precision._module_classes_to_ignore
)

# ==================================================
# Line: 86

overridden_module_classes = _override_module_mixed_precision(
    root_module, mixed_precision._module_classes_to_ignore
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_tools/ilp_utils.py
# Occurrences: Lines 214-215 (2 instances)

assert len(mod_stats) == len(fw_pre_order)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_tools/fsdp2_mem_tracker.py
# Occurrences: Lines 300-300 (2 instances)

snapshot = self.get_tracker_snapshot()

# ==================================================
# Occurrences: Lines 311-311 (2 instances)

self.get_tracker_snapshot()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_tools/sac_estimator.py
# Occurrences: Lines 810-811 (2 instances)

discarded_mem += sum(sac_stats.memory[i] for i in op_indices)

# ==================================================
# Occurrences: Lines 831-832 (2 instances)

discarded_mem += sum(sac_stats.memory[i] for i in op_indices)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_tools/runtime_estimator.py
# Occurrences: Lines 197-205 (5 instances)

r = func(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_tools/mem_tracker.py
# Occurrences: Lines 170-171 (2 instances)

if st.size() != self.size:

# ==================================================
# Occurrences: Lines 514-521 (2 instances)

mod_stats.snapshots[peak_state][-1][dev] = deepcopy(
    dev_snap
)

# ==================================================
# Line: 591

param_memory += sum(winfo.mem_consumed for winfo in winfos)

# ==================================================
# Line: 615

buffer_memory += sum(winfo.mem_consumed for winfo in winfos)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/distributed_c10d.py
# Occurrences: Lines 337-345 (5 instances)

setattr(Backend, name.upper(), name.lower())

# ==================================================
# Occurrences: Lines 356-361 (3 instances)

Backend.backend_capability[name.lower()] = ["cpu", "cuda"]

# ==================================================
# Line: 881

return torch.device("cpu")

# ==================================================
# Occurrences: Lines 900-901 (2 instances)

if torch.device("cpu") in devices:

# ==================================================
# Line: 949

worker_count = store.add(store_key, 0)

# ==================================================
# Line: 959

start = time.time()

# ==================================================
# Occurrences: Lines 967-972 (2 instances)

worker_count = store.add(store_key, 0)

# ==================================================
# Line: 981

if timedelta(seconds=(time.time() - start)) > timeout:

# ==================================================
# Line: 2576

all_reduce_opts.reduceOp = not_none(op_list[0].redop)

# ==================================================
# Line: 2595

reduce_opts.reduceOp = not_none(op_list[0].redop)

# ==================================================
# Line: 2724

p2p_op.op(
    p2p_op.tensor,
    group=p2p_op.group,
    tag=p2p_op.tag,
    **peer_kwarg(p2p_op),
)

# ==================================================
# Line: 2736

work = p2p_op.op(
    p2p_op.tensor,
    group=p2p_op.group,
    tag=p2p_op.tag,
    **peer_kwarg(p2p_op),
)

# ==================================================
# Line: 3724

max_tensor_size = torch.tensor([0], dtype=torch.long, device=pg_device)

# ==================================================
# Line: 3739

obj_tensor_size = torch.tensor([0], dtype=torch.long, device=pg_device)

# ==================================================
# Line: 5071

len(my_group),

# ==================================================
# Line: 5087

prefix_store, group_rank, len(my_group), pg_options

# ==================================================
# Occurrences: Lines 5098-5103 (2 instances)

backend_class = creator_fn(prefix_store, group_rank, len(my_group), timeout)

# ==================================================
# Line: 5282

group_world_size = len(ranks)

# ==================================================
# Line: 5344

world_size = len(ranks) if use_local_synchronization else get_world_size()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/api.py
# Occurrences: Lines 261-261 (2 instances)

module_path, _, param_name = name.rpartition(".")

# ==================================================
# Occurrences: Lines 272-277 (3 instances)

mod = module.get_submodule(module_path)

# ==================================================
# Line: 294

mod = module.get_submodule(module_path)

# ==================================================
# Line: 305

mod = module.get_submodule(module_path)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharding_spec/api.py
# Occurrences: Lines 160-164 (6 instances)

if rank != -1 and rank != len(shard.shard_offsets):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharded_tensor/_ops/binary_cmp.py
# Line: 11

result_tensor = torch.ones(1, device=torch.device(torch.cuda.current_device()))

# ==================================================
# Line: 17

expected_result = torch.ones(
    1, device=torch.device(torch.cuda.current_device())
) * dist.get_world_size(pg)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharded_tensor/api.py
# Line: 325

pg_rank = dist.get_rank()

# ==================================================
# Line: 352

if rank == dist.get_rank():

# ==================================================
# Line: 545

metadata.placement._device = torch.device("cpu")  # type: ignore[union-attr]

# ==================================================
# Line: 551

meta.placement._device = torch.device("cpu")  # type: ignore[union-attr]

# ==================================================
# Line: 639

current_device = torch.device(torch.cuda.current_device())

# ==================================================
# Line: 668

current_idx = torch.cuda.current_device()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharded_tensor/reshard.py
# Line: 132

local_shard = local_shard.transpose(0, reshard_dim).contiguous()

# ==================================================
# Line: 146

local_tensor = local_shard.transpose(0, reshard_dim).contiguous()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/filesystem.py
# Line: 315

offset = stream.tell()

# ==================================================
# Line: 335

length = stream.tell() - offset

# ==================================================
# Occurrences: Lines 647-653 (4 instances)

file_name = gen_file()

# ==================================================
# Occurrences: Lines 822-822 (3 instances)

read_bytes = io.BytesIO(transform_from.read(-1))

# ==================================================
# Occurrences: Lines 831-831 (3 instances)

seekable = io.BytesIO(transform_from.read(-1))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/utils.py
# Line: 194

local_data = _wrap_exception(e)

# ==================================================
# Line: 210

node_failures[self.rank] = _wrap_exception(e)

# ==================================================
# Line: 241

local_data = _wrap_exception(e)

# ==================================================
# Line: 252

node_failures[self.rank] = _wrap_exception(e)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/_dedup_save_plans.py
# Occurrences: Lines 70-72 (2 instances)

num_plans = len(all_plans)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/planner_helpers.py
# Occurrences: Lines 397-402 (2 instances)

device = getattr(value, "device", None)

# ==================================================
# Line: 418

device = getattr(value, "device", None)

# ==================================================
# Occurrences: Lines 427-432 (2 instances)

device = getattr(value, "device", None)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/logger.py
# Occurrences: Lines 80-80 (3 instances)

t0 = time.time_ns()

# ==================================================
# Occurrences: Lines 92-92 (3 instances)

msg_dict["time"] = time.time_ns()

# ==================================================
# Occurrences: Lines 98-99 (6 instances)

t1 = time.time_ns()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/state_dict.py
# Line: 195

prefix = ".".join(fqn_obj_names)

# ==================================================
# Occurrences: Lines 203-203 (2 instances)

curr_obj = getattr(curr_obj, curr_obj_name)

# ==================================================
# Occurrences: Lines 223-225 (3 instances)

curr_obj = getattr(curr_obj, curr_obj_name)

# ==================================================
# Line: 307

fqns = _get_fqns(model, name)

# ==================================================
# Line: 329

fqns = _get_fqns(model, name)

# ==================================================
# Line: 483

fqns = _get_fqns(model, key)

# ==================================================
# Line: 529

fqns = _get_fqns(model, key)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/default_planner.py
# Occurrences: Lines 365-370 (2 instances)

torch.load(value, weights_only=False),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/optimizer.py
# Occurrences: Lines 300-305 (4 instances)

state_dict[key] = _alloc_tensor(
    value.properties, value.size, dp_pg_device_type
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_ops/_view_ops.py
# Occurrences: Lines 488-490 (2 instances)

assert len(input_src_placements) == len(mesh_sizes)

# ==================================================
# Occurrences: Lines 557-557 (2 instances)

in_dim = get_in_dim_to_shard(cmd.input_dim)

# ==================================================
# Occurrences: Lines 586-586 (2 instances)

in_dim = get_in_dim_to_shard(cmd.input_dim)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_ops/_math_ops.py
# Occurrences: Lines 965-965 (2 instances)

placements=_replicate_dims_start_at(input_src_spec.placements, axis),

# ==================================================
# Occurrences: Lines 977-977 (2 instances)

placements=_replicate_dims_start_at(input_src_spec.placements, axis),

# ==================================================
# Occurrences: Lines 1009-1015 (4 instances)

inp_placements = _replicate_dims_start_at(input_src_spec.placements, axis)

# ==================================================
# Occurrences: Lines 1039-1041 (2 instances)

out_placements = map_placements_after_reduction(
    inp_placements, outer_dims, reduce_dims_map, "sum"
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_ops/_embedding_ops.py
# Line: 199

output_emd_dim = len(indices_shape)

# ==================================================
# Line: 225

for input_dim in range(len(indices_shape)):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_dispatch.py
# Occurrences: Lines 204-207 (2 instances)

local_results = op_call(*local_tensor_args, **op_info.local_kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_tp_conv.py
# Occurrences: Lines 88-103 (4 instances)

grad_in_tensor[:, :, :, -d1:] = torch.add(
    grad_in_tensor[:, :, :, -d1:], recv_from_right
)

# ==================================================
# Line: 124

local_results = op_call(*local_tensor_args, **local_tensor_kwargs)

# ==================================================
# Line: 144

local_results = op_call(*local_tensor_args, **local_tensor_kwargs)

# ==================================================
# Line: 178

local_results = op_call(*local_tensor_args, **local_tensor_kwargs)

# ==================================================
# Line: 214

local_results = op_call(*local_tensor_args, **local_tensor_kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_shards_wrapper.py
# Line: 76

wrapper_shape = torch.Size(cat_tensor_shape)

# ==================================================
# Line: 87

torch.Size(cat_tensor_shape),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_redistribute.py
# Occurrences: Lines 207-215 (6 instances)

partial_spec = cast(Partial, current)

# ==================================================
# Occurrences: Lines 224-224 (2 instances)

partial_spec = cast(Partial, current)

# ==================================================
# Occurrences: Lines 237-237 (2 instances)

shard_spec = cast(Shard, current)

# ==================================================
# Occurrences: Lines 267-270 (4 instances)

current_placement = cast(Shard, current)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/parallel/_data_parallel_utils.py
# Occurrences: Lines 15-17 (2 instances)

grad = grad.wait()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/parallel/loss.py
# Occurrences: Lines 264-266 (2 instances)

result = result.sum()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_op_schema.py
# Occurrences: Lines 409-414 (2 instances)

if len(self.args_schema) != len(other.args_schema):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/experimental/_attention.py
# Occurrences: Lines 679-681 (3 instances)

grad_query = torch.zeros_like(query, dtype=accum_dtype)

# ==================================================
# Occurrences: Lines 750-752 (3 instances)

grad_query_ = torch.zeros_like(query, dtype=accum_dtype)

# ==================================================
# Line: 761

next_grad_kv = dkv_rotater.next_buffer()

# ==================================================
# Line: 810

next_grad_kv = dkv_rotater.next_buffer().to(key.dtype)

# ==================================================
# Occurrences: Lines 1202-1206 (4 instances)

return func(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/debug/_comm_mode.py
# Occurrences: Lines 344-354 (6 instances)

if str(op["name"]) not in trivial_ops

# ==================================================
# Occurrences: Lines 360-380 (18 instances)

op["name"] = str(op["name"])

# ==================================================
# Occurrences: Lines 510-518 (8 instances)

table = add_operations(
    table, operation, collective_indent, operation_indent
)

# ==================================================
# Occurrences: Lines 526-528 (4 instances)

table = add_operations(
    table, operation, collective_indent, operation_indent
)

# ==================================================
# Occurrences: Lines 588-589 (2 instances)

self.comm_module_counts["Global"]["forward"] = defaultdict(int)

# ==================================================
# Occurrences: Lines 706-709 (2 instances)

] = defaultdict(int)

# ==================================================
# Occurrences: Lines 722-723 (4 instances)

self.comm_module_counts[par]["forward"] = defaultdict(int)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_api.py
# Occurrences: Lines 1035-1037 (2 instances)

local_tensor = init_op(local_shape, **kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_adadelta.py
# Occurrences: Lines 85-90 (4 instances)

state["square_avg"] = torch.zeros_like(
    param, memory_format=torch.preserve_format
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_rmsprop.py
# Occurrences: Lines 92-102 (6 instances)

state["square_avg"] = torch.zeros_like(
    param, memory_format=torch.preserve_format
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_adamw.py
# Occurrences: Lines 88-99 (3 instances)

state["exp_avg"] = torch.zeros_like(
    param, memory_format=torch.preserve_format
)

# ==================================================
# Occurrences: Lines 160-171 (6 instances)

state["exp_avg"] = torch.zeros_like(
    param, memory_format=torch.preserve_format
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_adam.py
# Occurrences: Lines 90-99 (3 instances)

state["exp_avg"] = torch.zeros_like(
    param, memory_format=torch.preserve_format
)

# ==================================================
# Occurrences: Lines 159-170 (6 instances)

state["exp_avg"] = torch.zeros_like(
    param, memory_format=torch.preserve_format
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/zero_redundancy_optimizer.py
# Occurrences: Lines 556-561 (2 instances)

local_state_dict = _broadcast_object(
    empty_messenger,
    src_rank=global_rank,
    group=self.process_group,
    device=self._default_device,
)

# ==================================================
# Occurrences: Lines 581-586 (2 instances)

_ = _broadcast_object(
    empty_messenger,
    src_rank=global_rank,
    group=self.process_group,
    device=self._default_device,
)

# ==================================================
# Line: 771

global_rank = dist.distributed_c10d.get_global_rank(
    self.process_group, rank
)

# ==================================================
# Line: 784

global_rank = dist.distributed_c10d.get_global_rank(
    self.process_group, rank
)

# ==================================================
# Line: 987

assigned_rank = self._get_min_index(
    size_per_rank, assigned_ranks_per_bucket[bucket_index]
)

# ==================================================
# Line: 1005

assigned_rank = self._get_min_index(
    size_per_rank, assigned_ranks_per_bucket[bucket_index]
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_adamax.py
# Occurrences: Lines 94-100 (4 instances)

state["exp_avg"] = torch.zeros_like(
    param, memory_format=torch.preserve_format
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/nn/api/remote_module.py
# Line: 234

fut = rpc.rpc_async(
    self.on,
    _instantiate_template,
    (_module_interface_cls, enable_moving_cpu_tensors_to_cuda),
)

# ==================================================
# Line: 245

fut = rpc.rpc_async(
    self.on,
    _instantiate_template,
    (_module_interface_cls, enable_moving_cpu_tensors_to_cuda),
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/nn/functional.py
# Line: 357

world_size = dist.get_world_size(group=ctx.group)

# ==================================================
# Line: 364

out_size[0] = out_size[0] // dist.get_world_size(group=ctx.group)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/pipelining/microbatch.py
# Line: 317

real_num_chunks = len(args_split_dict)

# ==================================================
# Occurrences: Lines 325-328 (2 instances)

if len(kwargs_split) < real_num_chunks:

# ==================================================
# Occurrences: Lines 336-339 (4 instances)

if len(args_split_dict) != len(kwargs_split):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/pipelining/stage.py
# Occurrences: Lines 563-565 (2 instances)

out_val = self.submod(*args, **kwargs)

# ==================================================
# Occurrences: Lines 641-644 (2 instances)

result = perform_backward(backward_type)()

# ==================================================
# Line: 650

result = perform_backward(backward_type)()

# ==================================================
# Line: 671

result = perform_backward(backward_type)()

# ==================================================
# Occurrences: Lines 798-811 (4 instances)

grads_input, _ = self.backward_maybe_with_nosync(
    "full",
    bwd_kwargs,
    last_backward=last_backward,
)

# ==================================================
# Occurrences: Lines 1137-1137 (2 instances)

gi_dsts = act_send_info.setdefault(out_idx, [])

# ==================================================
# Occurrences: Lines 1146-1146 (2 instances)

dsts = act_send_info.setdefault(out_idx, [])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/pipelining/_IR.py
# Line: 777

atoms = fqn.split(".")

# ==================================================
# Line: 901

setattr(parent, fqn.split(".")[-1], tensor)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/pipelining/schedules.py
# Occurrences: Lines 711-717 (2 instances)

fwd_recvs = self._stage.get_fwd_recv_ops(fwd_mb_index)

# ==================================================
# Line: 726

fwd_sends = self._stage.get_fwd_send_ops(fwd_mb_index)

# ==================================================
# Line: 742

bwd_recvs = self._stage.get_bwd_recv_ops(bwd_mb_index)

# ==================================================
# Line: 748

loss = self._maybe_get_loss(self._stage, bwd_mb_index)

# ==================================================
# Line: 756

bwd_sends = self._stage.get_bwd_send_ops(bwd_mb_index)

# ==================================================
# Line: 764

fwd_recvs = self._stage.get_fwd_recv_ops(fwd_mb_index)

# ==================================================
# Line: 770

output = self._stage.forward_one_chunk(
    fwd_mb_index, arg_mbs[fwd_mb_index], kwarg_mbs[fwd_mb_index]
)  # type: ignore[index]

# ==================================================
# Occurrences: Lines 778-791 (4 instances)

fwd_sends = self._stage.get_fwd_send_ops(fwd_mb_index)

# ==================================================
# Occurrences: Lines 802-803 (2 instances)

bwd_sends = self._stage.get_bwd_send_ops(bwd_mb_index)

# ==================================================
# Occurrences: Lines 898-898 (2 instances)

action = compute_actions.pop(0)

# ==================================================
# Occurrences: Lines 904-904 (2 instances)

compute_actions.pop(0)

# ==================================================
# Occurrences: Lines 916-916 (2 instances)

compute_actions.pop(0)

# ==================================================
# Occurrences: Lines 1310-1310 (2 instances)

loss = self._maybe_get_loss(stage, mb_index)

# ==================================================
# Occurrences: Lines 1331-1331 (2 instances)

loss = self._maybe_get_loss(stage, mb_index)

# ==================================================
# Occurrences: Lines 1687-1687 (2 instances)

loss = self._maybe_get_loss(stage, mb_index)

# ==================================================
# Occurrences: Lines 1717-1717 (2 instances)

loss = self._maybe_get_loss(stage, mb_index)

# ==================================================
# Occurrences: Lines 1877-1877 (2 instances)

fwd_stage_index = forward_stage_index(op)

# ==================================================
# Occurrences: Lines 1890-1890 (2 instances)

fwd_stage_index = forward_stage_index(op)

# ==================================================
# Occurrences: Lines 1897-1897 (2 instances)

bwd_stage_index = backward_stage_index(op)

# ==================================================
# Occurrences: Lines 1907-1909 (2 instances)

weight_stage_index = backward_stage_index(
    backward_op_ids[weight_op_count]
)

# ==================================================
# Occurrences: Lines 1928-1928 (2 instances)

bwd_stage_index = backward_stage_index(op)

# ==================================================
# Occurrences: Lines 1938-1940 (2 instances)

weight_stage_index = backward_stage_index(
    backward_op_ids[weight_op_count]
)

# ==================================================
# Line: 1954

weight_stage_index = backward_stage_index(backward_op_ids[weight_op_count])

# ==================================================
# Occurrences: Lines 2499-2502 (2 instances)

for rank in sorted(pipeline_order)

# ==================================================
# Occurrences: Lines 2572-2572 (2 instances)

for rank in sorted(pipeline_order):

# ==================================================
# Occurrences: Lines 2585-2585 (2 instances)

for i in sorted(pipeline_order, reverse=True):

# ==================================================
# Occurrences: Lines 2591-2591 (2 instances)

for rank in sorted(pipeline_order):

# ==================================================
# Occurrences: Lines 2605-2605 (2 instances)

for i in sorted(pipeline_order, reverse=True):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adadelta.py
# Occurrences: Lines 114-119 (4 instances)

state["square_avg"] = torch.zeros_like(
    p, memory_format=torch.preserve_format
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/swa_utils.py
# Occurrences: Lines 277-277 (2 instances)

self_params, model_params, self.n_averaged.to(device)  # type: ignore[arg-type]

# ==================================================
# Occurrences: Lines 285-289 (4 instances)

self_params, model_params, self.n_averaged.to(device)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/sparse_adam.py
# Occurrences: Lines 95-101 (6 instances)

state["exp_avg"] = torch.zeros_like(
    p, memory_format=torch.preserve_format
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/nadam.py
# Occurrences: Lines 141-147 (4 instances)

state["exp_avg"] = torch.zeros_like(
    p, memory_format=torch.preserve_format
)

# ==================================================
# Occurrences: Lines 484-484 (2 instances)

mus = torch._foreach_pow(0.96, exponent)

# ==================================================
# Occurrences: Lines 491-491 (2 instances)

mu_nexts = torch._foreach_pow(0.96, exponent)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adamax.py
# Occurrences: Lines 109-114 (4 instances)

state["exp_avg"] = torch.zeros_like(
    p, memory_format=torch.preserve_format
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adam.py
# Occurrences: Lines 177-188 (6 instances)

state["exp_avg"] = torch.zeros_like(
    p, memory_format=torch.preserve_format
)

# ==================================================
# Occurrences: Lines 416-418 (4 instances)

grad = grad.add(param, alpha=weight_decay)

# ==================================================
# Occurrences: Lines 640-640 (2 instances)

device_max_exp_avg_sqs = cast(list[Tensor], device_max_exp_avg_sqs_)

# ==================================================
# Occurrences: Lines 732-739 (6 instances)

device_max_exp_avg_sqs = cast(list[Tensor], device_max_exp_avg_sqs_)

# ==================================================
# Occurrences: Lines 760-767 (6 instances)

device_max_exp_avg_sqs = cast(list[Tensor], device_max_exp_avg_sqs_)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/sgd.py
# Occurrences: Lines 349-351 (4 instances)

grad = grad.add(param, alpha=weight_decay)

# ==================================================
# Occurrences: Lines 435-435 (2 instances)

bufs.append(cast(Tensor, device_momentum_buffer_list[i]))

# ==================================================
# Occurrences: Lines 448-448 (2 instances)

buf = cast(Tensor, device_momentum_buffer_list[i])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/lbfgs.py
# Occurrences: Lines 48-50 (2 instances)

f_new, g_new = obj_func(x, t, d)

# ==================================================
# Occurrences: Lines 61-61 (2 instances)

bracket_g = [g_prev, g_new.clone(memory_format=torch.contiguous_format)]

# ==================================================
# Occurrences: Lines 75-75 (2 instances)

bracket_g = [g_prev, g_new.clone(memory_format=torch.contiguous_format)]

# ==================================================
# Occurrences: Lines 90-94 (4 instances)

g_prev = g_new.clone(memory_format=torch.contiguous_format)

# ==================================================
# Occurrences: Lines 131-139 (20 instances)

eps = 0.1 * (max(bracket) - min(bracket))

# ==================================================
# Occurrences: Lines 147-149 (2 instances)

f_new, g_new = obj_func(x, t, d)

# ==================================================
# Occurrences: Lines 156-156 (2 instances)

bracket_g[high_pos] = g_new.clone(memory_format=torch.contiguous_format)  # type: ignore[possibly-undefined]

# ==================================================
# Occurrences: Lines 173-173 (2 instances)

bracket_g[low_pos] = g_new.clone(memory_format=torch.contiguous_format)  # type: ignore[possibly-undefined]

# ==================================================
# Occurrences: Lines 330-335 (2 instances)

orig_loss = closure()

# ==================================================
# Occurrences: Lines 363-363 (2 instances)

d = flat_grad.neg()

# ==================================================
# Occurrences: Lines 371-375 (4 instances)

s = d.mul(t)

# ==================================================
# Occurrences: Lines 391-391 (2 instances)

num_old = len(old_dirs)

# ==================================================
# Occurrences: Lines 398-398 (2 instances)

q = flat_grad.neg()

# ==================================================
# Occurrences: Lines 457-458 (2 instances)

loss = float(closure())

# ==================================================
# Occurrences: Lines 480-480 (2 instances)

if d.mul(t).abs().max() <= tolerance_change:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/radam.py
# Occurrences: Lines 112-118 (4 instances)

state["exp_avg"] = torch.zeros_like(
    p, memory_format=torch.preserve_format
)

# ==================================================
# Occurrences: Lines 435-438 (4 instances)

bias_correction1 = torch._foreach_pow(beta2, grouped_state_steps)

# ==================================================
# Occurrences: Lines 508-508 (2 instances)

bias_correction2 = torch._foreach_pow(beta2, grouped_state_steps)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/rmsprop.py
# Occurrences: Lines 122-132 (6 instances)

state["square_avg"] = torch.zeros_like(
    p, memory_format=torch.preserve_format
)

# ==================================================
# Occurrences: Lines 394-399 (4 instances)

grouped_momentum_buffer_list = cast(
    list[Tensor], grouped_momentum_buffer_list_
)

# ==================================================
# Occurrences: Lines 432-432 (2 instances)

grouped_grad_avgs = cast(list[Tensor], grouped_grad_avgs_)

# ==================================================
# Occurrences: Lines 444-446 (2 instances)

grouped_momentum_buffer_list = cast(
    list[Tensor], grouped_momentum_buffer_list_
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_strobelight/cli_function_profiler.py
# Line: 270

return work_function(*args, **kwargs)

# ==================================================
# Line: 279

result = work_function(*args, **kwargs)

# ==================================================
# Occurrences: Lines 285-287 (3 instances)

start = timer()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/rnn.py
# Occurrences: Lines 666-676 (2 instances)

hx = torch.zeros(
    self.num_layers * num_directions,
    max_batch_size,
    self.hidden_size,
    dtype=input.dtype,
    device=input.device,
)

# ==================================================
# Occurrences: Lines 702-712 (2 instances)

hx = torch.zeros(
    self.num_layers * num_directions,
    max_batch_size,
    self.hidden_size,
    dtype=input.dtype,
    device=input.device,
)

# ==================================================
# Occurrences: Lines 1057-1075 (3 instances)

h_zeros = torch.zeros(
    self.num_layers * num_directions,
    max_batch_size,
    real_hidden_size,
    dtype=input.dtype,
    device=input.device,
)

# ==================================================
# Occurrences: Lines 1089-1102 (2 instances)

h_zeros = torch.zeros(
    self.num_layers * num_directions,
    max_batch_size,
    real_hidden_size,
    dtype=input.dtype,
    device=input.device,
)

# ==================================================
# Line: 1124

hx = self.permute_hidden(hx, sorted_indices)

# ==================================================
# Occurrences: Lines 1345-1355 (2 instances)

hx = torch.zeros(
    self.num_layers * num_directions,
    max_batch_size,
    self.hidden_size,
    dtype=input.dtype,
    device=input.device,
)

# ==================================================
# Occurrences: Lines 1382-1392 (2 instances)

hx = torch.zeros(
    self.num_layers * num_directions,
    max_batch_size,
    self.hidden_size,
    dtype=input.dtype,
    device=input.device,
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/module.py
# Occurrences: Lines 996-996 (2 instances)

grad_applied.requires_grad_(param_grad.requires_grad)

# ==================================================
# Occurrences: Lines 1009-1011 (2 instances)

out_param.grad = grad_applied.requires_grad_(
    param_grad.requires_grad
)

# ==================================================
# Line: 1746

return self.forward(*input, **kwargs)

# ==================================================
# Line: 1757

result = self.forward(*input, **kwargs)

# ==================================================
# Line: 1778

return forward_call(*args, **kwargs)

# ==================================================
# Line: 1821

result = forward_call(*args, **kwargs)

# ==================================================
# Occurrences: Lines 1832-1834 (2 instances)

hook_result = hook(self, args, kwargs, result)

# ==================================================
# Line: 1881

hook_result = hook(self, args, result)  # type: ignore[possibly-undefined]

# ==================================================
# Occurrences: Lines 1893-1895 (2 instances)

hook_result = hook(self, args, kwargs, result)  # type: ignore[possibly-undefined]

# ==================================================
# Line: 2003

output = hook(self, name, value)

# ==================================================
# Line: 2014

output = hook(self, name, value)

# ==================================================
# Line: 2579

incompatible_keys = _IncompatibleKeys(missing_keys, unexpected_keys)

# ==================================================
# Line: 2613

return _IncompatibleKeys(missing_keys, unexpected_keys)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/_functions.py
# Line: 78

mean_all, invstd_all, count_all = torch.split(combined, num_channels, dim=1)

# ==================================================
# Line: 85

mean_all, invstd_all, count_all = torch.split(combined, num_channels, dim=1)

# ==================================================
# Occurrences: Lines 225-226 (2 instances)

ctx.scale = ctx.scale or input.new()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/container.py
# Occurrences: Lines 221-222 (2 instances)

len_original = len(self)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/adaptive.py
# Line: 323

return torch.argmax(log_prob, dim=1)

# ==================================================
# Line: 329

output[not_in_shortlist] = torch.argmax(log_prob, dim=1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/conv.py
# Occurrences: Lines 791-792 (2 instances)

min_sizes = torch.jit.annotate(list[int], [])

# ==================================================
# Line: 814

res = torch.jit.annotate(list[int], [])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/prune.py
# Line: 1098

importance_scores.get((module, name), getattr(module, name))

# ==================================================
# Line: 1106

getattr(module, name + "_mask", torch.ones_like(getattr(module, name)))

# ==================================================
# Line: 1132

param = getattr(module, name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/fusion.py
# Occurrences: Lines 84-88 (2 instances)

conv_b = torch.zeros_like(bn_rm)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/parametrize.py
# Line: 169

if not isinstance(new, Tensor) and not isinstance(new, Sequence):

# ==================================================
# Line: 176

self.is_tensor = isinstance(new, Tensor)

# ==================================================
# Line: 382

tensor = parametrization()

# ==================================================
# Line: 406

return parametrization()

# ==================================================
# Line: 551

Y = getattr(module, tensor_name)

# ==================================================
# Line: 603

original = getattr(module, tensor_name)

# ==================================================
# Line: 692

t = getattr(module, tensor_name)

# ==================================================
# Line: 719

t = getattr(module, tensor_name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/clip_grad.py
# Occurrences: Lines 166-166 (2 instances)

torch._foreach_mul_(device_grads, clip_coef_clamped.to(device))

# ==================================================
# Occurrences: Lines 172-172 (2 instances)

clip_coef_clamped_device = clip_coef_clamped.to(device)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/parametrizations.py
# Line: 170

Q = _make_orthogonal(Q)

# ==================================================
# Line: 179

Q = _make_orthogonal(Q)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/experimental/_paged_attention.py
# Line: 238

new_kv_indices = torch.zeros(
    (B, H, ROWS, self.n_pages), dtype=torch.int32, device=device
)

# ==================================================
# Line: 253

new_full_kv_indices = torch.zeros(
    (B, H, ROWS, self.n_pages), dtype=torch.int32, device=device
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/flex_attention.py
# Occurrences: Lines 698-703 (2 instances)

partial_blocks = partial_blocks.to(dtype=torch.int8)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/bias.py
# Occurrences: Lines 227-231 (3 instances)

needs_padding = query.size(-1) % 8 != 0

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/functional.py
# Line: 5726

q_proj = linear(q, w_q, b_q)

# ==================================================
# Line: 5743

return linear(q, w_q, b_q), linear(k, w_k, b_k), linear(v, w_v, b_v)

# ==================================================
# Line: 6357

attn_mask = attn_mask.unsqueeze(0)

# ==================================================
# Occurrences: Lines 6376-6378 (2 instances)

attn_mask = pad(attn_mask, (0, 1))

# ==================================================
# Occurrences: Lines 6420-6422 (2 instances)

attn_mask = pad(attn_mask, (0, 1))

# ==================================================
# Occurrences: Lines 6473-6474 (2 instances)

attn_output = linear(attn_output, out_proj_weight, out_proj_bias)

# ==================================================
# Line: 6483

attn_output = attn_output.squeeze(1)

# ==================================================
# Line: 6492

attn_mask = attn_mask.unsqueeze(0)

# ==================================================
# Occurrences: Lines 6507-6511 (3 instances)

attn_output = linear(attn_output, out_proj_weight, out_proj_bias)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/init.py
# Line: 415

dimensions = tensor.dim()

# ==================================================
# Line: 424

if tensor.dim() > 2:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/parallel/_functions.py
# Occurrences: Lines 19-21 (2 instances)

if len(inputs) == 0:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/parallel/distributed.py
# Line: 872

self._mp_stream = torch.Stream()

# ==================================================
# Line: 898

upcast_stream=torch.Stream(),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/package/package_exporter.py
# Occurrences: Lines 913-920 (3 instances)

storage = cast(Storage, untyped_storage)

# ==================================================
# Line: 932

num_bytes = storage.nbytes()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/package/importer.py
# Line: 92

orig_module_name = self.whichmodule(obj, name)

# ==================================================
# Line: 112

module_name = self.whichmodule(obj, name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/package/package_importer.py
# Occurrences: Lines 278-281 (4 instances)

return func(self, *args)

# ==================================================
# Occurrences: Lines 410-410 (2 instances)

module = self.modules[name] = importlib.import_module(name)

# ==================================================
# Occurrences: Lines 419-419 (2 instances)

module = self.modules[name] = importlib.import_module(name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/__init__.py
# Line: 1908

a_isnan = torch.isnan(a)

# ==================================================
# Line: 1916

a_isnan = torch.isnan(a)

# ==================================================
# Line: 3425

utils.is_float_dtype(input.dtype) or utils.is_complex_dtype(input.dtype),

# ==================================================
# Line: 3477

complex_fft = utils.is_complex_dtype(input.dtype)

# ==================================================
# Line: 4036

if a.dim() == 0 and len(dims) > 0:

# ==================================================
# Line: 4042

len_dims = len(dims)

# ==================================================
# Occurrences: Lines 4634-4639 (2 instances)

t_shape[-1] = builtins.abs(offset)

# ==================================================
# Line: 5439

dtype = torch.get_default_dtype()

# ==================================================
# Line: 5462

torch.get_default_dtype()

# ==================================================
# Line: 6668

return torch.get_default_dtype()

# ==================================================
# Line: 6674

default_dtype = torch.get_default_dtype()

# ==================================================
# Line: 6694

return torch.get_default_dtype()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/linalg/__init__.py
# Occurrences: Lines 159-161 (2 instances)

return to_result_dtype(torch.amax(torch.abs(x), dim=dim, keepdim=keepdim))  # type: ignore[return-value,arg-type]

# ==================================================
# Line: 179

x = torch.abs(x)

# ==================================================
# Line: 189

x = torch.abs(x)

# ==================================================
# Occurrences: Lines 247-252 (4 instances)

A = _maybe_convert_to_dtype(A, dtype)  # type: ignore[assignment]

# ==================================================
# Occurrences: Lines 270-275 (4 instances)

A = _maybe_convert_to_dtype(A, dtype)  # type: ignore[assignment]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/fft.py
# Occurrences: Lines 299-302 (2 instances)

dim is None or len(dim) == len(shape),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/nn/functional/__init__.py
# Occurrences: Lines 490-494 (2 instances)

rhs = torch.true_divide(torch.log1p(torch.exp(scaled_input)), beta)  # type: ignore[arg-type]

# ==================================================
# Line: 834

return _nll_loss_nd(input, target, weight, reduction, ignore_index)

# ==================================================
# Occurrences: Lines 855-857 (2 instances)

return _nll_loss_nd(input, target, weight, reduction, ignore_index)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/_numeric_suite.py
# Occurrences: Lines 27-32 (4 instances)

split_str = key_str.split(".")

# ==================================================
# Occurrences: Lines 40-45 (3 instances)

match_string = "".join(key_str.split(".")[0:-2])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/fx/utils.py
# Occurrences: Lines 62-69 (2 instances)

first_arg = get_normalized_nth_input(node, gm, 0)

# ==================================================
# Occurrences: Lines 87-94 (2 instances)

first_arg = get_normalized_nth_input(node, gm, 0)

# ==================================================
# Occurrences: Lines 114-121 (2 instances)

prev_node = get_normalized_nth_input(node, gm, 0)

# ==================================================
# Occurrences: Lines 129-136 (2 instances)

prev_node = get_normalized_nth_input(node, gm, 0)

# ==================================================
# Occurrences: Lines 146-153 (2 instances)

first_arg = get_normalized_nth_input(node, gm, 0)

# ==================================================
# Line: 255

node_obj = getattr_from_fqn(gm, node.target)  # type: ignore[arg-type]

# ==================================================
# Line: 262

node_obj = getattr_from_fqn(gm, node.target)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/fx/weight_utils.py
# Line: 126

weight = getattr_from_fqn(gm, weight_node.target)  # type: ignore[arg-type]

# ==================================================
# Line: 140

weight = getattr_from_fqn(gm, weight_node.target)  # type: ignore[arg-type]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/fx/graph_passes.py
# Occurrences: Lines 172-172 (2 instances)

env[node.name] = new_graph.node_copy(node, load_arg)

# ==================================================
# Occurrences: Lines 195-195 (2 instances)

env[node.name] = new_graph.node_copy(node, load_arg)

# ==================================================
# Line: 323

new_dtype_cast_name = get_new_attr_name_with_prefix(node_name_prefix)(gm_b)

# ==================================================
# Line: 353

dtype_cast_mod = dtype_cast_mod_cls()

# ==================================================
# Line: 365

new_dtype_cast_name = get_new_attr_name_with_prefix(node_name_prefix)(gm_b)

# ==================================================
# Line: 378

dtype_cast_mod = dtype_cast_mod_cls()

# ==================================================
# Line: 404

node_a_copy_name = get_new_attr_name_with_prefix(node_a.name + "_shadow_copy_")(
    gm_b
)

# ==================================================
# Occurrences: Lines 421-426 (2 instances)

arg_copy = _copy_node_from_a_to_c(
    get_normalized_nth_input(node_a, gm_a, 0), gm_a, gm_b, graph_c
)  # type: ignore[arg-type]

# ==================================================
# Occurrences: Lines 432-437 (2 instances)

arg_copy = _copy_node_from_a_to_c(
    get_normalized_nth_input(node_a, gm_a, 0), gm_a, gm_b, graph_c
)  # type: ignore[arg-type]

# ==================================================
# Occurrences: Lines 682-686 (2 instances)

node_a_shadows_c_name = get_new_attr_name_with_prefix(node_name_prefix)(gm_b)

# ==================================================
# Occurrences: Lines 804-804 (2 instances)

env_c[node_b.name] = graph_c.node_copy(node_b, load_arg)

# ==================================================
# Occurrences: Lines 833-833 (2 instances)

env_c[node_b.name] = graph_c.node_copy(node_b, load_arg)

# ==================================================
# Occurrences: Lines 852-857 (4 instances)

env_c[node_b.name] = graph_c.node_copy(node_b, load_arg)

# ==================================================
# Occurrences: Lines 866-866 (2 instances)

env_c[node_b.name] = graph_c.node_copy(node_b, load_arg)

# ==================================================
# Occurrences: Lines 927-927 (2 instances)

env_c[node_b.name] = graph_c.node_copy(node_b, load_arg)

# ==================================================
# Occurrences: Lines 944-948 (4 instances)

prev_node_c = get_normalized_nth_input(node_c, gm_b, 0)  # type: ignore[possibly-undefined]

# ==================================================
# Occurrences: Lines 1030-1032 (2 instances)

num_non_param_args_node_a = get_number_of_non_param_args(
    subgraph_a.start_node, gm_a
)

# ==================================================
# Occurrences: Lines 1064-1065 (6 instances)

while get_normalized_nth_input(cur_node, gm_b, 0) != input_logger:  # type: ignore[possibly-undefined]

# ==================================================
# Occurrences: Lines 1122-1122 (2 instances)

env_c[node_b.name] = graph_c.node_copy(node_b, load_arg)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/fx/n_shadows_utils.py
# Occurrences: Lines 85-92 (12 instances)

result = node.target(*load_arg(node.args), **load_arg(node.kwargs))

# ==================================================
# Occurrences: Lines 197-202 (4 instances)

list_of_nodes = _order_nodes(node_a, node_b, node_c)

# ==================================================
# Line: 488

attr_name = _get_attr_name(subgraph_idx, subgraph_candidate_idx)

# ==================================================
# Line: 594

attr_name = _get_attr_name(subgraph_idx, subgraph_candidate_idx)

# ==================================================
# Line: 784

maybe_subgraph = _get_subgraph_containing_node(n, subgraphs_dedup)

# ==================================================
# Occurrences: Lines 843-843 (2 instances)

attr_name = _get_attr_name(cur_subgraph_idx, subgraph_candidate_idx)

# ==================================================
# Occurrences: Lines 897-897 (2 instances)

attr_name = _get_attr_name(cur_subgraph_idx, subgraph_candidate_idx)

# ==================================================
# Line: 938

maybe_subgraph = _get_subgraph_containing_node(n, subgraphs_dedup)

# ==================================================
# Occurrences: Lines 1017-1024 (8 instances)

scale_val = getattr_from_fqn(shadow_wrapper, scale_node.target)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/fx/pattern_utils.py
# Occurrences: Lines 153-154 (4 instances)

fusion_el_is_fun = (not isinstance(cur_fusion_el, str)) and (

# ==================================================
# Occurrences: Lines 167-171 (4 instances)

fusion_el_is_mod = isinstance(cur_fusion_el, type)

# ==================================================
# Occurrences: Lines 186-186 (2 instances)

fusion_el_is_meth_without_args = isinstance(cur_fusion_el, str)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/scheduler/base_scheduler.py
# Occurrences: Lines 40-45 (4 instances)

cls = instance_ref().__class__

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/data_scheduler/base_data_scheduler.py
# Occurrences: Lines 65-70 (4 instances)

cls = instance_ref().__class__

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/pruner/prune_functions.py
# Line: 240

weight_parameterizations = cast(ParametrizationList, parametrization_dict.weight)

# ==================================================
# Line: 277

weight_parameterizations = cast(
    ParametrizationList, parametrization_dict.weight
)

# ==================================================
# Occurrences: Lines 320-323 (2 instances)

parametrization_dict = cast(nn.ModuleDict, linear.parametrizations)

# ==================================================
# Occurrences: Lines 351-354 (2 instances)

parametrization_dict = cast(nn.ModuleDict, linear.parametrizations)

# ==================================================
# Occurrences: Lines 378-378 (2 instances)

parametrization_dict = cast(nn.ModuleDict, lstm.parametrizations)

# ==================================================
# Occurrences: Lines 400-400 (2 instances)

parametrization_dict = cast(nn.ModuleDict, lstm.parametrizations)

# ==================================================
# Occurrences: Lines 443-445 (2 instances)

weight_parameterizations.original = nn.Parameter(
    weight_parameterizations.original[:, M_ho]
)

# ==================================================
# Occurrences: Lines 461-463 (2 instances)

parametrization_dict = cast(
    nn.ModuleDict, lstm.parametrizations
)

# ==================================================
# Occurrences: Lines 469-471 (2 instances)

weight_parameterizations.original = nn.Parameter(
    weight_parameterizations.original[:, M_ho]
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/pruner/base_structured_sparsifier.py
# Occurrences: Lines 291-291 (3 instances)

first_module = modules.get(node.target)

# ==================================================
# Occurrences: Lines 301-301 (3 instances)

convert_block.append(modules.get(node.target))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/data_sparsifier/quantization_utils.py
# Line: 85

valid_name = name.replace(".", "_")

# ==================================================
# Line: 116

quantized_emb = fqn_to_module(model, name)

# ==================================================
# Line: 132

name=name.replace(".", "_"),

# ==================================================
# Line: 140

quantized_emb = fqn_to_module(model, name)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/pt2e/export_utils.py
# Occurrences: Lines 68-84 (8 instances)

match_pattern = _get_aten_graph_module_for_pattern(
    _WrapperModule(dropout_train),
    example_inputs,
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/pt2e/_affine_quantization.py
# Occurrences: Lines 341-346 (2 instances)

scale = torch.clamp(scale, min=eps)

# ==================================================
# Line: 646

dequant = dequant.to(output_dtype)

# ==================================================
# Line: 652

dequant = input.to(output_dtype)

# ==================================================
# Line: 662

dequant = input.to(output_dtype)

# ==================================================
# Line: 672

dequant = dequant.to(output_dtype)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/pt2e/qat_utils.py
# Occurrences: Lines 50-54 (4 instances)

kwargs["weight_scale"] = torch.tensor([1], dtype=torch.float)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/pt2e/representation/rewrite.py
# Occurrences: Lines 310-311 (2 instances)

bias_i32 = bias_i32.unsqueeze(-1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/utils.py
# Line: 657

scale = torch.max(scale, eps)

# ==================================================
# Line: 676

scale = torch.max(scale, eps)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_lower_to_native_backend.py
# Occurrences: Lines 420-422 (4 instances)

getattr(self, attr_name), torch._C.ScriptObject

# ==================================================
# Line: 589

ref_node.op == "call_module" and type(_get_module(ref_node, modules)) == nn.ReLU

# ==================================================
# Line: 604

match_key = type(_get_module(ref_node, modules))

# ==================================================
# Occurrences: Lines 916-916 (2 instances)

prepack_op = get_qconv_prepack_op(func_node.target)  # type: ignore[arg-type]

# ==================================================
# Occurrences: Lines 924-924 (2 instances)

prepack_op = get_qconv_prepack_op(func_node.target)  # type: ignore[arg-type]

# ==================================================
# Occurrences: Lines 1197-1199 (2 instances)

is_call_function, is_call_method, is_call_module = is_default_node(
    ref_node, modules
)

# ==================================================
# Occurrences: Lines 1267-1269 (2 instances)

is_call_function, is_call_method, is_call_module = is_default_node(
    ref_node, modules
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/utils.py
# Occurrences: Lines 183-186 (4 instances)

attr_name = get_attr_name(i)

# ==================================================
# Occurrences: Lines 297-301 (2 instances)

result = all_node_args_have_no_tensors(node.args[0], modules, cache)  # type: ignore[arg-type]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/qconfig_mapping_utils.py
# Occurrences: Lines 119-121 (2 instances)

qconfig_with_device_check = _add_module_to_qconfig_obs_ctr(
    qconfig, modules.get(node.target, None)
)

# ==================================================
# Occurrences: Lines 141-143 (2 instances)

qconfig_with_device_check = _add_module_to_qconfig_obs_ctr(
    qconfig, modules.get(node.target, None)
)

# ==================================================
# Occurrences: Lines 160-162 (2 instances)

qconfig_with_device_check = _add_module_to_qconfig_obs_ctr(
    qconfig, modules.get(node.target, None)
)

# ==================================================
# Occurrences: Lines 184-186 (2 instances)

qconfig_with_device_check = _add_module_to_qconfig_obs_ctr(
    qconfig, modules.get(node.target, None)
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/graph_module.py
# Occurrences: Lines 136-138 (4 instances)

getattr(self, attr_name), torch._C.ScriptObject

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_equalize.py
# Line: 530

op_module.weight = nn.Parameter(scaled_weight)

# ==================================================
# Line: 538

op_module.weight = nn.Parameter(scaled_weight)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/prepare.py
# Line: 172

kwargs = _get_observer_kwargs(quantization_spec)

# ==================================================
# Line: 181

kwargs = _get_observer_kwargs(quantization_spec)

# ==================================================
# Occurrences: Lines 1569-1571 (2 instances)

node.meta["target_dtype_info"] = copy.copy(
    _DEFAULT_QUINT8_QCONFIG_FOR_TARGET_DTYPE_INFO
)

# ==================================================
# Occurrences: Lines 1591-1593 (2 instances)

node.meta["target_dtype_info"] = copy.copy(
    _DEFAULT_QUINT8_QCONFIG_FOR_TARGET_DTYPE_INFO
)

# ==================================================
# Line: 1617

_is_pattern_dtype_config_and_qconfig_supported_by_backend(
    pattern, matched_node_pattern, qconfig, backend_config
)

# ==================================================
# Line: 1706

_is_pattern_dtype_config_and_qconfig_supported_by_backend(
    pattern, matched_node_pattern, qconfig, backend_config
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/convert.py
# Line: 169

dtype_ = to_underlying_dtype(dtype)

# ==================================================
# Line: 185

dtype_ = to_underlying_dtype(dtype)

# ==================================================
# Occurrences: Lines 220-229 (2 instances)

quantized_node = graph.create_node(
    node_type, quantize_op, tuple(quantize_op_inputs), {}
)

# ==================================================
# Line: 253

dtype_ = to_underlying_dtype(dtype)

# ==================================================
# Line: 319

quantized_node = graph.create_node(
    node_type, quantize_op, tuple(quantize_op_inputs), {}
)

# ==================================================
# Line: 328

dequantized_node = graph.call_function(
    dequantize_op,
    tuple(dq_inputs),
    add_dequantize_op_kwargs(dequantize_op, input_node),
)

# ==================================================
# Occurrences: Lines 452-455 (2 instances)

quantized_node = graph.create_node(
    node_type, quantize_op, tuple(quantize_op_inputs), {}
)

# ==================================================
# Occurrences: Lines 474-477 (2 instances)

quantized_node = graph.create_node(
    node_type, quantize_op, tuple(quantize_op_inputs), {}
)

# ==================================================
# Occurrences: Lines 492-495 (2 instances)

quantized_node = graph.create_node(
    node_type, quantize_op, tuple(quantize_op_inputs), {}
)

# ==================================================
# Line: 766

parent_name, name = _parent_name(node.target)

# ==================================================
# Occurrences: Lines 803-804 (2 instances)

weight_post_process_ih = qconfig.weight()  # type: ignore[union-attr, operator]

# ==================================================
# Occurrences: Lines 821-824 (2 instances)

weight_post_process = qconfig.weight()  # type: ignore[union-attr, operator]

# ==================================================
# Line: 830

weight_post_process = qconfig.weight()  # type: ignore[union-attr, operator]

# ==================================================
# Line: 857

wq_or_wq_dict.update(get_qparam_dict(weight_post_process))

# ==================================================
# Line: 875

parent_name, name = _parent_name(node.target)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_model_report/model_report_observer.py
# Occurrences: Lines 139-141 (2 instances)

min_val, max_val = torch.aminmax(y, dim=1)

# ==================================================
# Occurrences: Lines 275-279 (5 instances)

self.min_val = torch.tensor([], device=device)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_model_report/detector.py
# Occurrences: Lines 1068-1070 (4 instances)

min_val, max_val = torch.aminmax(y, dim=1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/_equalize.py
# Occurrences: Lines 37-46 (4 instances)

module.weight = torch.nn.Parameter(weight)

# ==================================================
# Occurrences: Lines 137-137 (2 instances)

if weight1.size(output_axis) != weight2.size(input_axis):

# ==================================================
# Occurrences: Lines 157-159 (2 instances)

size1[output_axis] = weight1.size(output_axis)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fake_quantize.py
# Occurrences: Lines 213-218 (2 instances)

assert _is_per_channel(self.qscheme) or _is_per_tensor(self.qscheme), (

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/experimental/adaround_fake_quantize.py
# Occurrences: Lines 53-54 (2 instances)

self.scale = torch.tensor([], requires_grad=False)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/experimental/adaround_optimization.py
# Occurrences: Lines 156-159 (2 instances)

q_w_hard_round = ada_quantizer(q_module.weight)

# ==================================================
# Line: 182

ada_quantizer(q_module.weight)

# ==================================================
# Line: 206

q_weight = ada_quantizer(q_module.weight)

# ==================================================
# Line: 250

q_weight = ada_quantizer(q_module.weight)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/experimental/observer.py
# Occurrences: Lines 30-31 (2 instances)

self.min_val = torch.tensor([])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/observer.py
# Line: 380

scale = torch.max(scale, self.eps)

# ==================================================
# Line: 401

scale = torch.max(scale, self.eps)

# ==================================================
# Occurrences: Lines 669-671 (2 instances)

min_val, max_val = torch.aminmax(x)

# ==================================================
# Occurrences: Lines 776-778 (2 instances)

min_val, max_val = torch.aminmax(y, dim=1)

# ==================================================
# Occurrences: Lines 880-885 (2 instances)

self.min_val = torch.rand(
    0,
)

# ==================================================
# Occurrences: Lines 966-968 (2 instances)

min_val, max_val = torch.aminmax(y, dim=1)

# ==================================================
# Line: 1282

x_min, x_max = torch.aminmax(x)

# ==================================================
# Line: 1291

x_min, x_max = torch.aminmax(x)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/utils.py
# Line: 75

qweight = _clamp_weights(qweight, observer, wt_scale, wt_zp)

# ==================================================
# Line: 85

qweight = _clamp_weights(qweight, observer, wt_scale, wt_zp)

# ==================================================
# Line: 94

qweight = _clamp_weights(qweight, observer, wt_scale, wt_zp)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/activation.py
# Line: 261

sc, zp = torch._choose_qparams_per_tensor(bias_k, reduce_range=False)

# ==================================================
# Line: 267

sc, zp = torch._choose_qparams_per_tensor(
    bias_k, reduce_range=False  # type: ignore[possibly-undefined]
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/dynamic/modules/rnn.py
# Occurrences: Lines 158-159 (6 instances)

b_ih = torch.randn(gate_size).to(torch.float)

# ==================================================
# Line: 370

dtype = weight_observer_method().dtype

# ==================================================
# Line: 427

weight_observer = weight_observer_method()

# ==================================================
# Occurrences: Lines 960-961 (2 instances)

self.bias_ih = torch.randn(num_chunks * hidden_size).to(dtype=torch.float)

# ==================================================
# Line: 1052

dtype = weight_observer_method().dtype

# ==================================================
# Line: 1087

weight_observer = weight_observer_method()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/dynamic/modules/linear.py
# Occurrences: Lines 138-140 (2 instances)

qweight = _quantize_weight(mod.weight.float(), weight_observer)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/intrinsic/qat/modules/conv_fused.py
# Occurrences: Lines 219-225 (3 instances)

running_std = torch.sqrt(self.bn.running_var + self.bn.eps)

# ==================================================
# Occurrences: Lines 243-249 (3 instances)

running_std = torch.sqrt(self.bn.running_var + self.bn.eps)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantizable/modules/rnn.py
# Occurrences: Lines 68-73 (4 instances)

self.gates: torch.nn.Module = torch.ao.nn.quantized.FloatFunctional()

# ==================================================
# Occurrences: Lines 84-95 (8 instances)

self.gates[g] = torch.ao.nn.quantized.FloatFunctional()

# ==================================================
# Occurrences: Lines 286-296 (2 instances)

self.layer_fw = _LSTMSingleLayer(
    input_dim, hidden_dim, bias=bias, split_gates=split_gates, **factory_kwargs
)

# ==================================================
# Line: 339

(h, c) = torch.jit._unwrap_optional(hidden_fw)

# ==================================================
# Line: 345

h, c = torch.jit._unwrap_optional(hidden_fw)  # type: ignore[assignment]

# ==================================================
# Line: 382

layer.layer_fw = _LSTMSingleLayer.from_params(
    wi, wh, bi, bh, split_gates=split_gates
)

# ==================================================
# Line: 391

layer.layer_bw = _LSTMSingleLayer.from_params(
    wi, wh, bi, bh, split_gates=split_gates
)

# ==================================================
# Line: 502

x = x.transpose(0, 1)

# ==================================================
# Line: 551

x = x.transpose(0, 1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantizable/modules/activation.py
# Line: 89

self.linear_Q = nn.Linear(
    self.embed_dim, self.embed_dim, bias=bias, **factory_kwargs
)

# ==================================================
# Line: 99

self.out_proj = nn.Linear(self.embed_dim, self.embed_dim, bias=bias, **factory_kwargs)  # type: ignore[assignment]

# ==================================================
# Occurrences: Lines 106-110 (5 instances)

self.quant_attn_output = torch.ao.quantization.QuantStub()

# ==================================================
# Occurrences: Lines 146-147 (2 instances)

bias = torch.nn.Parameter(bias[_start:_end], bias.requires_grad)

# ==================================================
# Occurrences: Lines 155-156 (2 instances)

bias = torch.nn.Parameter(bias[_start:_end], bias.requires_grad)

# ==================================================
# Line: 164

observed.linear_V.weight = torch.nn.Parameter(weight, weight.requires_grad)

# ==================================================
# Line: 201

(self.linear_Q._weight_bias()[1] is not None),  # type: ignore[operator]

# ==================================================
# Line: 223

wQ, bQ = self.linear_Q._weight_bias()  # type: ignore[operator]

# ==================================================
# Occurrences: Lines 438-440 (2 instances)

attn_mask = F.pad(attn_mask, (0, 1))

# ==================================================
# Occurrences: Lines 486-488 (2 instances)

attn_mask = F.pad(attn_mask, (0, 1))

# ==================================================
# Line: 508

attn_output_weights = attn_output_weights.view(
    bsz, self.num_heads, tgt_len, src_len
)

# ==================================================
# Line: 543

attn_output_weights = attn_output_weights.view(
    bsz, self.num_heads, tgt_len, src_len
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_prims_common/__init__.py
# Occurrences: Lines 1365-1365 (2 instances)

scalar_type = dtype_to_type(arg.dtype)

# ==================================================
# Occurrences: Lines 1377-1377 (2 instances)

arg_type = dtype_to_type(arg.dtype)

# ==================================================
# Line: 1622

torch.get_default_dtype() if result_dtype is None else result_dtype

# ==================================================
# Line: 1631

result_dtype = corresponding_complex_dtype(torch.get_default_dtype())

# ==================================================
# Occurrences: Lines 1640-1649 (4 instances)

return get_computation_dtype(result_dtype), result_dtype

# ==================================================
# Occurrences: Lines 1656-1658 (2 instances)

return get_computation_dtype(result_dtype), result_dtype

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/fx_minifier.py
# Occurrences: Lines 236-236 (6 instances)

f"({len(old_state.graph.nodes)} nodes, {len(old_state.inps)} inputs)",

# ==================================================
# Occurrences: Lines 244-246 (6 instances)

old_nodes = len(old_state.graph.nodes)

# ==================================================
# Occurrences: Lines 291-294 (2 instances)

new_graph = fx.Graph()

# ==================================================
# Line: 303

if len(new_graph.nodes) < len(cur_graph.nodes) and graph_fails(

# ==================================================
# Line: 341

assert len(ph_nodes) == len(cur_inps)

# ==================================================
# Line: 349

if len(new_inps) < len(cur_inps):

# ==================================================
# Line: 373

new_graph = fx.Graph()

# ==================================================
# Occurrences: Lines 382-382 (2 instances)

new_node = new_graph.node_copy(node, lambda x: env[x])

# ==================================================
# Occurrences: Lines 396-396 (2 instances)

new_node = new_graph.node_copy(node, lambda x: env[x])

# ==================================================
# Line: 402

num_nodes = len(cur_graph.nodes)

# ==================================================
# Occurrences: Lines 426-428 (4 instances)

old_len = len(cur_inps)

# ==================================================
# Line: 438

num_nodes = len(failing_state.graph.nodes)

# ==================================================
# Occurrences: Lines 459-460 (2 instances)

dump_state(fx.GraphModule(fail_f, failing_state.graph), failing_state.inps)

# ==================================================
# Line: 493

failing_fx = fx.GraphModule(fail_f, failing_state.graph)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_activation_checkpointing/knapsack_evaluator.py
# Occurrences: Lines 254-261 (4 instances)

runtime_range = max(runtime_values) - min(runtime_values)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/compile_utils.py
# Occurrences: Lines 116-116 (2 instances)

new_node = new_graph.node_copy(n, lambda x: env[x])

# ==================================================
# Occurrences: Lines 164-164 (2 instances)

new_node = new_graph.node_copy(n, lambda x: env[x])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/make_functional.py
# Occurrences: Lines 552-552 (2 instances)

model = model_class(*args, **kwargs).to(device)

# ==================================================
# Occurrences: Lines 559-559 (2 instances)

model_class(*args, **kwargs).to(device) for _ in range(num_models)

# ==================================================
# Occurrences: Lines 579-579 (2 instances)

model = model_class(*args, **kwargs).to(device)

# ==================================================
# Occurrences: Lines 586-586 (2 instances)

model_class(*args, **kwargs).to(device) for _ in range(num_models)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/autograd_function.py
# Line: 410

key = id(Generated)

# ==================================================
# Line: 450

key = id(Generated)

# ==================================================
# Line: 473

key = id(Generated)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/eager_transforms.py
# Occurrences: Lines 605-619 (10 instances)

basis = tree_unflatten(flat_basis_chunk, output_spec)

# ==================================================
# Occurrences: Lines 662-671 (8 instances)

basis = tree_unflatten(flat_basis_chunk, output_spec)

# ==================================================
# Occurrences: Lines 677-679 (2 instances)

flat_results = tree_map(
    lambda t: torch.unsqueeze(t, 0), flat_results
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/benchmark_utils.py
# Occurrences: Lines 56-60 (2 instances)

t0 = time.perf_counter()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/aot_autograd.py
# Line: 633

enable_python_dispatcher() if shape_env is not None else nullcontext()

# ==================================================
# Occurrences: Lines 675-680 (2 instances)

ctx = nullcontext()

# ==================================================
# Occurrences: Lines 1200-1202 (2 instances)

compiled_fn = dispatch_and_compile()

# ==================================================
# Line: 1666

_get_attributes(mod),

# ==================================================
# Line: 1687

new_attrs = _get_attributes(mod)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/utils.py
# Occurrences: Lines 279-280 (4 instances)

new_token_node.meta["val"] = torch.tensor([])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/traced_function_transforms.py
# Occurrences: Lines 337-342 (2 instances)

fwd_seed, fwd_base_offset = CUDARngStateHelper.get_torch_state_as_tuple(
    fake_mode
)

# ==================================================
# Line: 354

fwd_seed, fwd_base_offset = CUDARngStateHelper.get_torch_state_as_tuple(
    fake_mode
)

# ==================================================
# Occurrences: Lines 445-449 (4 instances)

joint_mutates_data = has_data_mutation(f_inpt)

# ==================================================
# Occurrences: Lines 486-489 (4 instances)

assert not has_metadata_mutation(
    f_inpt, before, check_only_storage_mutation=False
), "Found an input to the backward that had metadata mutated during the backward pass. This is not supported"

# ==================================================
# Occurrences: Lines 729-729 (2 instances)

bwd_out_tokens = functional_tensor_mode._tokens.values()

# ==================================================
# Occurrences: Lines 737-737 (2 instances)

out_tokens = [from_fun(t) for t in functional_tensor_mode._tokens.values()]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/dispatch_and_compile_graph.py
# Occurrences: Lines 184-188 (2 instances)

copy_count = assert_functional_graph(fw_module.graph)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/collect_metadata_analysis.py
# Occurrences: Lines 180-181 (4 instances)

prior_grad_enabled = torch.is_grad_enabled()

# ==================================================
# Occurrences: Lines 192-192 (2 instances)

fake_mode = detect_fake_mode()

# ==================================================
# Occurrences: Lines 206-206 (2 instances)

if prior_autocast_states != _get_autocast_states():

# ==================================================
# Occurrences: Lines 567-567 (2 instances)

new_out_idx = len(intermediate_bases)

# ==================================================
# Occurrences: Lines 667-667 (2 instances)

with detect_fake_mode():

# ==================================================
# Occurrences: Lines 782-783 (4 instances)

if torch.is_grad_enabled() != prior_grad_enabled:

# ==================================================
# Occurrences: Lines 798-798 (2 instances)

num_intermediate_bases=len(intermediate_bases),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/autograd_cache.py
# Line: 983

cache_event_time = time.time_ns()

# ==================================================
# Line: 1002

cache_event_time = time.time_ns()

# ==================================================
# Line: 1029

cache_event_time = time.time_ns()

# ==================================================
# Occurrences: Lines 1050-1051 (2 instances)

cache_event_time = time.time_ns()

# ==================================================
# Line: 1063

log_cache_bypass("bypass_aot_autograd", str(e))

# ==================================================
# Line: 1071

cache_key, time.time_ns(), forward_symints=symints

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/jit_compile_runtime_wrappers.py
# Line: 251

compiled_fw = make_boxed_func(compiled_fw)

# ==================================================
# Line: 311

compiled_fw = make_boxed_func(compiled_fw)

# ==================================================
# Occurrences: Lines 484-485 (4 instances)

primals_counter = itertools.count(0)

# ==================================================
# Occurrences: Lines 497-497 (3 instances)

env[node].meta = copy.copy(node.meta)

# ==================================================
# Occurrences: Lines 511-511 (3 instances)

env[node].meta = copy.copy(node.meta)

# ==================================================
# Occurrences: Lines 602-605 (4 instances)

new_hop_graphs[identifier].new_num_sym_nodes = len(symint_outputs)

# ==================================================
# Line: 905

bw_g_inputs = bw_g.find_nodes(op="placeholder")

# ==================================================
# Line: 1176

bw_new_ins = list(bw_g.find_nodes(op="placeholder"))

# ==================================================
# Occurrences: Lines 1376-1378 (3 instances)

fw_metadata.num_symints_saved_for_bw = len(symint_outs_saved_for_bw)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/runtime_wrappers.py
# Occurrences: Lines 521-521 (2 instances)

out = compiled_fn(runtime_args)

# ==================================================
# Occurrences: Lines 529-529 (2 instances)

return compiled_fn(runtime_args)

# ==================================================
# Line: 990

deduped_args = self.remove_dupe_args(args)

# ==================================================
# Line: 1004

new_args = self.add_dupe_args(self.remove_dupe_args(args))

# ==================================================
# Line: 1317

storage_ref_to_idx: dict[StorageWeakRef, list[int]] = collections.defaultdict(list)

# ==================================================
# Line: 1463

arg_to_old_idx_map = collections.defaultdict(list)

# ==================================================
# Line: 1862

x = coerce_to_expected_memory_format(x, meta.memory_format)

# ==================================================
# Line: 1883

runtime_subclass_keys, runtime_meta = x.__tensor_flatten__()

# ==================================================
# Line: 1921

x = coerce_to_expected_memory_format(x, meta.memory_format)

# ==================================================
# Line: 1928

runtime_subclass_keys = x.__tensor_flatten__()[0]

# ==================================================
# Line: 2169

torch._C._autograd._get_current_graph_task_keep_graph()

# ==================================================
# Line: 2255

not torch._C._autograd._get_current_graph_task_keep_graph()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/partitioners.py
# Occurrences: Lines 221-223 (4 instances)

env[node] = new_graph.node_copy(node, lambda x: env[x])

# ==================================================
# Occurrences: Lines 308-309 (2 instances)

idx = len(fwd_module_outputs)

# ==================================================
# Occurrences: Lines 621-623 (2 instances)

] = torch.ops.prims.convert_element_type.default(
    node.meta["val"], dequant_type
)

# ==================================================
# Occurrences: Lines 648-650 (2 instances)

dequant_node.meta["tensor_meta"] = extract_tensor_metadata(
    dequant_node.meta["val"]
)

# ==================================================
# Occurrences: Lines 660-665 (4 instances)

] = torch.ops.prims.convert_element_type.default(
    node.meta["val"], dequant_type
)

# ==================================================
# Line: 756

quant_bwd_input = bwd_module.graph.placeholder(name=fwd_node.name)

# ==================================================
# Line: 780

scale_bwd_input = bwd_module.graph.placeholder(name=fwd_node.name)

# ==================================================
# Line: 1108

env[node] = new_graph.node_copy(node, lambda x: env[x])

# ==================================================
# Line: 1127

env[node] = new_graph.node_copy(node, lambda x: env[x])

# ==================================================
# Line: 1211

fwd_rng_state.meta["val"] = get_cuda_generator_meta_val(device_idx)

# ==================================================
# Line: 1218

bwd_rng_state.meta["val"] = get_cuda_generator_meta_val(device_idx)

# ==================================================
# Line: 1640

output_size = _size_of(node)

# ==================================================
# Line: 1656

mem_sz = _size_of(node)

# ==================================================
# Occurrences: Lines 1853-1855 (4 instances)

(node_info.get_fw_order(start_node), start_node)

# ==================================================
# Occurrences: Lines 1871-1871 (2 instances)

node_info.get_fw_order(start_node),

# ==================================================
# Line: 2184

args, kwargs = pytree.tree_map(materialize_arg, (node.args, node.kwargs))

# ==================================================
# Line: 2192

args, kwargs = pytree.tree_map(materialize_arg, (node.args, node.kwargs))

# ==================================================
# Occurrences: Lines 2610-2614 (4 instances)

node.dist_from_bw = int(1e9)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_appdirs.py
# Occurrences: Lines 116-124 (3 instances)

path = os.path.join(path, appname)

# ==================================================
# Occurrences: Lines 169-173 (2 instances)

path = os.path.join(path, appname)

# ==================================================
# Occurrences: Lines 233-237 (2 instances)

path = os.path.join(path, appname)

# ==================================================
# Line: 341

path = os.path.join(path, appname)

# ==================================================
# Occurrences: Lines 347-351 (2 instances)

path = os.path.join(path, appname)

# ==================================================
# Line: 559

buf = ctypes.create_unicode_buffer(1024)

# ==================================================
# Line: 570

buf2 = ctypes.create_unicode_buffer(1024)

# ==================================================
# Line: 584

buf = array.zeros("c", buf_size)

# ==================================================
# Line: 593

dir = jna.Native.toString(buf.tostring()).rstrip("\0")

# ==================================================
# Occurrences: Lines 603-606 (2 instances)

buf = array.zeros("c", buf_size)

# ==================================================
