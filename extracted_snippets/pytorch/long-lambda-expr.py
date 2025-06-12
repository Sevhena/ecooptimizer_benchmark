# long-lambda-expr snippets for pytorch

# File: /root/ecooptimizer/pytorch/torchgen/gen.py
# Line: 194

lambda: BackendIndex(
    dispatch_key=DispatchKey.Undefined,
    use_out_as_primary=True,
    external=False,
    device_guard=False,
    # I'm actually not sure about this; undefined could be hit on
    # empty TensorList, hypothetically that could have sizes in it
    index={},
)

# ==================================================
# Line: 1642

lambda: {
    "ns_prologue": ns_helper.prologue,
    "ns_epilogue": ns_helper.epilogue,
    "dispatch_anonymous_definitions": anonymous_definitions[
        kernel_namespace
    ],
    "static_init_dispatch_registrations": ""
    if skip_dispatcher_op_registration
    else registration_body,
    "deferred_dispatch_registrations": "",
    "dispatch_namespace": dispatch_key.lower(),
    "dispatch_namespaced_definitions": ns_definitions[kernel_namespace],
},

# ==================================================
# Line: 1765

lambda: {
    "NativeMetaFunctions_includes": [],
    "NativeMetaFunctions_declarations": list(
        mapMaybe(compute_meta_function_declaration, structured_native_functions)
    ),
},

# ==================================================
# Occurrences: Lines 1780-1821 (3 instances)

lambda: {
    "MethodOperators_includes": [],
    "MethodOperators_declarations": list(
        mapMaybe(
            ComputeOperators(
                Target.DECLARATION,
                static_dispatch_backend_indices=static_dispatch_idx,
            ),
            method_native_functions,
        )
    ),
},

# ==================================================
# Line: 1829

lambda: {
    "NativeFunctions_includes": ["#include <ATen/NativeMetaFunctions.h>"],
    "NativeFunctions_declarations": declarations,
},

# ==================================================
# Line: 1851

lambda: {
    "DispatchKeyFunctions_inl_includes": [],
    "dispatch_namespace": dispatch_key.lower(),
    "dispatch_namespaced_declarations": get_namespaced_declaration(
        grouped_native_functions=grouped_native_functions,
        dispatch_key=dispatch_key,
        backend_idx=backend_indices[dispatch_key],
        selector=selector,
        rocm=rocm,
        symint=True,
    ),
},

# ==================================================
# Line: 1899

lambda: {
    "declarations": list(
        mapMaybe(
            ComputeOperators(
                Target.DECLARATION,
                static_dispatch_backend_indices=static_dispatch_idx,
            ),
            functions,
        )
    ),
},

# ==================================================
# Line: 1946

lambda: {
    "meta_function_declarations": list(
        mapMaybe(
            compute_meta_function_declaration, structured_functions
        )
    ),
},

# ==================================================
# Line: 1962

lambda: {
    "extra_includes": (
        f"#include <ATen/ops/{name}_meta.h>" if is_structured else []
    ),
    "native_function_declarations": declarations,
},

# ==================================================
# Line: 1978

lambda: {
    f"{category}_includes": [
        f"#include <ATen/ops/{name}{suffix}.h>"
        for name in sorted(functions_by_root_name.keys())
    ],
    f"{category}_declarations": [],
},

# ==================================================
# Line: 2018

lambda: {
    "dispatch_namespace": dispatch_namespace,
    "dispatch_namespaced_declarations": declarations,
},

# ==================================================
# Line: 2038

lambda: {
    "dispatch_namespace": dispatch_namespace,
    "DispatchKeyFunctions_inl_includes": [
        f"#include <ATen/ops/{name}_{dispatch_namespace}_dispatch.h>"
        for name in sorted(dispatch_names)
    ],
    "dispatch_namespaced_declarations": [],
},

# ==================================================
# Line: 2051

lambda: {
    "MethodOperators_includes": sorted(
        f"#include <ATen/ops/{name}_ops.h>"
        for name, functions in functions_by_root_name.items()
        if any(Variant.method in fn.variants for fn in functions)
    ),
    "MethodOperators_declarations": [],
},

# ==================================================
# Occurrences: Lines 2135-2149 (2 instances)

lambda: {
    "function_redispatch_definitions": list(
        mapMaybe(ComputeRedispatchFunction(), native_functions)
    ),
},

# ==================================================
# Line: 2362

lambda: {
    "meta_declaration": compute_meta_function_declaration(g),
    "native_declaration": dest.compute_native_function_declaration(
        g, backend_indices[dispatch_key]
    ),
    "native_definitions": dest.compute_ufunc_cpu(g),
},

# ==================================================
# Line: 2385

lambda: {
    "name": name,
    "cuda_headers": cuda_headers,
    "meta_declaration": compute_meta_function_declaration(g),
    "native_declaration": dest.compute_native_function_declaration(
        g, backend_indices[dispatch_key]
    ),
    "native_definitions": dest.compute_ufunc_cuda(g),
},

# ==================================================
# Line: 2481

lambda: gen_aoti_c_shim(
    fallback_native_functions,
    inductor_fallback_ops,
    structured_func_group_dict,
    dispatch_key,
    backend_indices,
    header=False,
    extend_aoti_c_shim=extend_aoti_c_shim,
    includes=headers_for_aoti() + "\n" + extra_headers,
),

# ==================================================
# Line: 2530

lambda: {
    "aten_schema_registrations": []
    if skip_dispatcher_op_registration
    else aten_schema_registrations,
    "schema_registrations": []
    if skip_dispatcher_op_registration
    else schema_registrations,
},

# ==================================================
# Line: 2549

env_callable=lambda fn: {
    "operator_headers": [f"#include <ATen/ops/{fn.root_name}.h>"],
    "definitions": [
        ComputeOperators(
            Target.DEFINITION,
            static_dispatch_backend_indices=static_dispatch_idx,
        )(fn)
    ],
},

# ==================================================
# Line: 2677

lambda: {
    "view_inverse_declarations": list(
        mapMaybe(
            lambda g: gen_functionalization_view_inverse_declaration(
                selector, g
            ),
            view_groups,
        )
    )
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_backend_stubs.py
# Line: 178

            lambda: f'The "autograd" key was specified, which indicates that you would like to override \
the behavior of autograd for some operators on your backend. However "Autograd{backend}" is not a valid DispatchKey.'

# ==================================================
# Line: 392

lambda f: []
if autograd_dispatch_key is None
else dest.compute_native_function_declaration(
    f, backend_indices[autograd_dispatch_key]
),

# ==================================================
# Line: 406

lambda: {
    "generated_comment": generated_comment,
    "namespace_prologue": ns_helper.prologue,
    "class_name": class_name,
    "namespace_epilogue": ns_helper.epilogue,
    "dispatch_declarations": backend_declarations + autograd_declarations,
    "BackendName": backend_name,
    "DispatchKey": backend_dispatch_key,
},

# ==================================================
# Line: 505

lambda: {
    "ns_prologue": ns_helper.prologue,
    "ns_epilogue": ns_helper.epilogue,
    "static_init_dispatch_registrations": static_init_dispatch_registrations,
    "deferred_dispatch_registrations": deferred_dispatch_registrations,
    "dispatch_namespace": dispatch_key.lower(),
    "dispatch_namespaced_definitions": "",
    "dispatch_anonymous_definitions": list(
        concatMap(
            dest.RegisterDispatchKey(
                backend_index,
                Target.ANONYMOUS_DEFINITION,
                selector,
                rocm=False,
                symint=True,
                class_method_name=f"{class_name}",
                skip_dispatcher_op_registration=False,
            ),
            grouped_native_functions,
        )
    ),
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_lazy_tensor.py
# Line: 471

lambda: {
    "includes": [
        f"#include <{path}>"
        for path in [
            tensor_class_hdr,
            shape_inference_hdr,
            "ATen/Functions.h",
            "ATen/native/TensorConversions.h",
            "ATen/NativeFunctions.h",
            "ATen/CompositeExplicitAutogradNonFunctionalFunctions.h",
            "ATen/MetaFunctions.h",
            "ATen/Operators.h",
            "ATen/native/CPUFallback.h",
            "torch/csrc/lazy/core/ir_builder.h",
            "torch/csrc/lazy/core/lazy_graph_executor.h",
            "torch/csrc/lazy/core/metrics.h",
            "torch/csrc/lazy/core/shape.h",
            f"{output_dir}/{backend_key}NativeFunctions.h",
            f"{output_dir}/LazyIr.h",
        ]
        + (
            ["torch/csrc/lazy/ts_backend/ts_eager_fallback.h"]
            if gen_forced_fallback_code
            else []
        )
    ],
    "helper_fns": get_ltc_helper_fns(),
    "native_functions_include": "",
    "namespace_prologue": ns_helper.prologue,
    "namespace_epilogue": ns_helper.epilogue,
    "native_function_definitions": list(
        concat_map_codegen(
            native_func_definition_generator(
                f"{backend_key}NativeFunctions",
                backend_indices[backend_key],
                tensor_class,
                gen_forced_fallback_code,
                backend_namespace,
                get_tensorlist,
                get_tensor_or_wrap_number,
                try_get_tensor,
                metrics_counter,
                create_tensor,
                create_from_first_tensor,
                create_aten_from_ltc_tensor,
                tuple_aten_from_ltc_tensors,
                lazy_tensor_ptr,
                get_device_fn,
            ),
            grouped_native_functions,
        )
    ),
},

# ==================================================
# Line: 563

lambda: {
    "lazy_non_native_ir_inc": [
        f"#include <{path}>"
        for path in [
            "torch/csrc/lazy/core/ir.h",
            "torch/csrc/lazy/core/ir_builder.h",
            "torch/csrc/lazy/core/internal_ops/ltc_ops.h",
            "torch/csrc/lazy/core/shape_inference.h",
        ]
        + ([node_base_hdr] if node_base_hdr else [])
        if path
    ],
    "non_native_ir_nodes": dest.generate_non_native_lazy_ir_nodes(
        non_native, lazy_ir_obj
    ),
    "namespace_prologue": ns_helper.prologue,
    "namespace_epilogue": ns_helper.epilogue,
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/torchbind.py
# Line: 146

lambda x: mode.from_tensor(x, static_shapes=True)
if not isinstance(x, torch._subclasses.fake_tensor.FakeTensor)
else x,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/_nnapi/serializer.py
# Occurrences: Lines 859-864 (2 instances)

"aten::mul": lambda self, node: self.add_pointwise_simple_binary_broadcast_op(
    node, NNAPI_OperationCode.MUL, NNAPI_FuseCode.FUSED_NONE
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler_util.py
# Line: 863

key=lambda evt: getattr(
    evt,
    sort_by.replace("cuda", "device")
    .replace("xpu", "device")
    .replace("privateuse1", "device"),
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/utils.py
# Line: 1095

onerror=lambda func, path, exc_info: log.warning(
    "Failed to remove temporary cache dir at %s",
    inductor_cache_dir,
    exc_info=exc_info,
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/compile_fx.py
# Line: 2081

payload_fn=lambda: model_.print_readable(
    print_output=False, include_stride=True, include_device=True
)
+ f"\n\n # graph id: {id(model_.graph)}",

# ==================================================
# Line: 2105

payload_fn=lambda: model_.print_readable(
    print_output=False, include_stride=True, include_device=True
)
+ f"\n\n # graph id: {id(model_.graph)}",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/scheduler.py
# Line: 2144

lambda: {
    "graph_id": self.post_grad_graph_id,
    "num_nodes_before_fusion": self.num_orig_nodes,
    "num_nodes_after_fusion": len(self.nodes),
}

# ==================================================
# Line: 3036

lambda: {
    "kernel1_path": path1,
    "kernel1_latency": ms1,
    "kernel2_path": path2,
    "kernel2_latency": ms2,
    "fused_kernel_path": path_fused,
    "fused_kernel_latency": ms_fused,
    "slow_down_ratio": ms_fused / (ms1 + ms2),
}

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/cudagraph_trees.py
# Line: 1301

lambda: (
    "Expected all cuda outputs in cuda graph recording. Non cuda output "
    f"from {self.stack_traces[i] if self.stack_traces else '(unknown)'}"
),

# ==================================================
# Line: 1743

lambda: "TODO: graph recording observed an input tensor deallocate during graph "
" recording that did not occur during replay. Please file an issue.",

# ==================================================
# Line: 1821

lambda: f"These storage data ptrs are not allocated in pool {pool_id} but should be {unique_storages}",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/memory.py
# Line: 453

key=lambda node: (
    max(live_memory + node.mpi_node.size, max_memory),
    node.mpi_node.size - node_info[node]["memory_to_free"],
    node.mpi_node.index,
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/post_grad.py
# Line: 165

lambda graph: fuse_ddp_communication(
    graph,
    config._fuse_ddp_communication_passes,
    config._fuse_ddp_bucket_size,
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/pad_mm.py
# Occurrences: Lines 545-578 (3 instances)

lambda: pad_addmm(
    input_pad,
    mat1_pad,
    mat2_pad,
    m_padded_length,
    k_padded_length,
    n_padded_length,
    mat1_pre_padded=mat1_pre_padded,
    mat2_pre_padded=mat2_pre_padded,
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/pre_grad.py
# Line: 226

shape_prop = lambda mod: ShapeProp(  # noqa: E731
    gm=mod,
    # pyre-fixme[16]: Module `torch._dynamo.utils` has no attribute `detect_fake_mode`
    fake_mode=detect_fake_mode(example_inputs),
).propagate(*tuple(example_inputs))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/inductor_prims.py
# Line: 106

lambda self, indices, values, accumulate=False: torch.ops.aten.index_put_(
    self, indices, values, accumulate
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_sympy/value_ranges.py
# Line: 1014

lambda: (
    "\n"
    + "\n".join(
        f"  {k}: {r}" for k, r in ranges.items() if k in expr.free_symbols
    )
    if ranges
    else ""
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/gen_pyi.py
# Line: 328

lambda: {
    "IterDataPipeMethods": iter_method_definitions,
    "MapDataPipeMethods": map_method_definitions,
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/_utils.py
# Line: 31

lambda: _format_graph_code(
    f"===== {format_name()} =====\n",
    gm.forward.__code__.co_filename,
    gm.print_readable(**kwargs),
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/proxy_tensor.py
# Line: 548

lambda x, i: set_meta(
    tracer.create_proxy(
        "call_function", torch.ops.aten.sym_size.int, (proxy, i), {}
    ),
    x,
),

# ==================================================
# Line: 561

lambda x, i: set_meta(
    tracer.create_proxy(
        "call_function", torch.ops.aten.sym_stride.int, (proxy, i), {}
    ),
    x,
),

# ==================================================
# Occurrences: Lines 572-590 (2 instances)

lambda x: set_meta(
    tracer.create_proxy(
        "call_function", torch.ops.aten.sym_numel.default, (proxy,), {}
    ),
    x,
),

# ==================================================
# Line: 2219

payload_fn=lambda: self.fx_tracer.graph.python_code(  # type: ignore[union-attr]
    root_module="self",
    verbose=True,
    include_stride=True,
    include_device=True,
).src,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/symbolic_shapes.py
# Line: 4776

metadata_fn=lambda: {
    "symbol": str(symbol),
    "node_id": id(sym_node),
    "vr": f"[{vr.lower}, {vr.upper}]",
    "user_stack": structured.get_user_stack(3),
    "stack": structured.get_framework_stack(),
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_decomp/decompositions.py
# Line: 939

lambda: "Expected 3D or 4D (batch mode) tensor for input with possible 0 batch size "
f"and non-zero dimensions, but got: {tuple(shape)}",

# ==================================================
# Line: 950

lambda: f"Given an input with spacial size {tuple(shape[-2:])}, "
f"kernel_size={kernel_size}, dilation={dilation}, "
f"padding={padding}, stride={stride}, "
"the calculated shape of the array of sliding blocks "
f"is {output_size}, but its components must be at least one.",

# ==================================================
# Occurrences: Lines 1025-1033 (2 instances)

lambda: "Expected 2D or 3D (batch mode) tensor for input with possible 0 batch size "
f"and non-zero dimensions, but got: {tuple(shape)}",

# ==================================================
# Occurrences: Lines 1044-1052 (2 instances)

lambda: f"Given output_size={output_size}, kernel_size={kernel_size}, "
f"dilation={dilation}, padding={padding}, stride={stride}, "
f"expected input.size(-1) to be {L} but got {shape[-1]}.",

# ==================================================
# Line: 1433

lambda: "tensor_split expected tensor_indices_or_sections to be a zero-dimensional "
f"or one-dimensional tensor, but got a tensor with {split_dim} dims",

# ==================================================
# Line: 2437

lambda: "adaptive_avg_pool2d(): Expected input to have non-zero size for "
f"non-batch dimensions, but input has shape {tuple(shape)}.",

# ==================================================
# Occurrences: Lines 2564-2582 (3 instances)

lambda: (
    f"There should be exactly two elements (height, width) in output_size, "
    f"but got {len(output_size)} elements."
),

# ==================================================
# Line: 2588

lambda: (
    f"max_unpooling2d(): "
    f"Expected input to have non-zero size for non-batch dimensions, "
    f"but got {self.shape} with dimension {i} being empty."
),

# ==================================================
# Occurrences: Lines 2612-2634 (5 instances)

lambda: f"Input to max_unpooling3d should be a 4d or 5d Tensor, but got a tensor with {input.ndim} dimensions.",

# ==================================================
# Line: 2640

lambda: (
    f"max_unpooling3d(): "
    f"Expected input to have non-zero size for non-batch dimensions, "
    f"but got {input.shape} with dimension {i} being empty."
),

# ==================================================
# Line: 2698

lambda: f"Number of indices ({index_size}) should be equal to tensor.size(dim) ({tensor_size}), for {dim=}",

# ==================================================
# Line: 4874

lambda: f"Expected non-empty vector or matrix with optional 0-dim batch size, but got: {input.shape}",

# ==================================================
# Line: 4918

lambda: f"Expected non-empty vector or matrix with optional 0-dim batch size, but got: {orig_input_shape}",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/ops/_symbolic_impl.py
# Line: 225

lambda: f"{onnx_dtype} is invalid as an ONNX data type. Valid values are {list(_ONNX_DTYPE_TO_TORCH_DTYPE.keys())}",

# ==================================================
# Line: 250

lambda: f"{onnx_dtype} is invalid as an ONNX data type. Valid values are {list(_ONNX_DTYPE_TO_TORCH_DTYPE.keys())}",

# ==================================================
# Line: 293

lambda: f"{onnx_dtype} is invalid as an ONNX data type. Valid values are {list(_ONNX_DTYPE_TO_TORCH_DTYPE.keys())}",

# ==================================================
# Line: 325

lambda: f"{onnx_dtype} is invalid as an ONNX data type. Valid values are {list(_ONNX_DTYPE_TO_TORCH_DTYPE.keys())}",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/fx/dynamo_graph_extractor.py
# Line: 92

lambda x: (
    inspect.isclass(x)
    and issubclass(x, modeling_outputs.ModelOutput)
    and x is not modeling_outputs.ModelOutput
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/meta_utils.py
# Line: 1321

lambda: torch.ops.aten._sparse_coo_tensor_with_dims(
    t.sparse_dim,
    t.dense_dim,
    t.size,
    dtype=t.dtype,
    layout=torch.sparse_coo,
    device="meta",
)

# ==================================================
# Line: 1372

lambda: torch.ops.aten._sparse_compressed_tensor_with_dims(
    0,
    t.dense_dim,
    t.shape,
    blocksize,
    index_dtype,
    layout=t.layout,
    dtype=t.dtype,
    device="meta",
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/fake_tensor.py
# Line: 2213

metadata_fn=lambda: {
    "op": str(func),
    "reason": (
        f"Mismatched aliasing spec between fake kernel and real kernel: {exc.reason}"  # noqa: F821
    ),
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/fake_impls.py
# Line: 270

lambda func: torch.Tag.dynamic_output_shape in func.tags
and func
not in [aten.index.Tensor, aten.nonzero.default, aten.repeat_interleave.Tensor]

# ==================================================
# Line: 923

lambda: f"The size of tensor a ({sizeA}) "
f"must match the size of tensor b ({sizeB}) "
f"at non-singleton dimension {i})",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_prims/__init__.py
# Line: 1728

lambda: f"expected src to have a size equal to the slice of self. src size = {src.shape}, slice size = {size}",

# ==================================================
# Line: 1798

lambda: f"Sizes of tensors must match except in dimension {dim}. "
f"Expected {common_length} in dimension {idx} but got {length} for tensor number "
f"{tensor_idx} in the list",

# ==================================================
# Line: 2451

lambda: (
    "Number of dimensions in the tensor input does not match the "
    f"length of the physical layout; i.e. len(size) = {dim} "
    f"is not equal to len(physical_layout) = {len(physical_layout)}"
),

# ==================================================
# Line: 2462

lambda: (
    f"Dimension out of range (expected to be between 0 and {dim - 1}, but got "
    f"{l} at index {p}).  NB: negative dims "
    "not currently supported; file an issue if you want it."
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/overrides.py
# Line: 596

lambda input, weight, offsets, max_norm=None, norm_type=2, scale_grad_by_freq=False, mode="mean", sparse=False, per_sample_weights=None, padding_idx=None: -1  # noqa: B950

# ==================================================
# Line: 610

lambda x, observer_on, fake_quant_on, averaging_const, running_min, running_max, scale, zero_point, quant_min, quant_max, ch_axis, per_row_fake_quant=False, symmetric_quant=False: -1  # noqa: B950

# ==================================================
# Line: 704

lambda input, running_mean, running_var, weight, bias, use_input_stats, momentum, eps, cudnn_enabled: -1

# ==================================================
# Line: 722

lambda input, n_fft, hop_length=None, win_length=None, window=None, center=True, normalized=False, onesided=None, length=None, return_complex=False: -1  # noqa: B950

# ==================================================
# Line: 737

torch.lobpcg: lambda input, k=None, B=None, X=None, n=None, iK=None, niter=None, tol=None, largest=None, method=None, tracker=None, ortho_iparams=None, ortho_fparams=None, ortho_bparams=None: -1,  # noqa: B950

# ==================================================
# Line: 793

lambda input, weight, bias, running_mean, running_var, training, exponential_average_factor, epsilon: -1

# ==================================================
# Line: 799

lambda input, weight, bias, padding, output_padding, stride, dilation, groups, benchmark, deterministic: -1

# ==================================================
# Line: 805

lambda input, weight, weight_stride0, hx, cx, mode, hidden_size, num_layers, batch_first, dropout, train, bidirectional, batch_sizes, dropout_state: -1  # noqa: B950

# ==================================================
# Line: 876

lambda input, weight, offsets=None, max_norm=None, norm_type=2, scale_grad_by_freq=False, mode="mean", sparse=False, per_sample_weights=None, include_last_offset=False, padding_idx=None: -1  # noqa: B950

# ==================================================
# Line: 946

lambda query, key, value, embed_dim_to_check, num_heads, in_proj_weight, in_proj_bias, bias_k, bias_v, add_zero_attn, dropout_p, out_proj_weight, out_proj_bias, training=True, key_padding_mask=None, need_weights=True, attn_mask=None, use_separate_proj_weight=False, q_proj_weight=None, k_proj_weight=None, v_proj_weight=None, static_k=None, static_v=None, average_attn_weights=None, is_causal=False: -1  # noqa: B950

# ==================================================
# Occurrences: Lines 1043-1046 (2 instances)

lambda input, hx, w_ih, w_hh, b_ih, b_hh, packed_ih, packed_hh, col_offsets_ih, col_offsets_hh, scale_ih, scale_hh, zero_point_ih, zero_point_hh: -1  # noqa: B950

# ==================================================
# Occurrences: Lines 1067-1070 (2 instances)

lambda input, hx, w_ih, w_hh, b_ih, b_hh, packed_ih, packed_hh, col_offsets_ih, col_offsets_hh, scale_ih, scale_hh, zero_point_ih, zero_point_hh: -1  # noqa: B950

# ==================================================
# Line: 1137

lambda input, n_fft, hop_length=None, win_length=None, window=None, center=True, pad_mode="reflect", normalized=False, onesided=True, return_complex=None, align_to_window=None: -1  # noqa: B950

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_vmap_internals.py
# Line: 128

lambda: f"vmap({_get_name(func)}, ..., out_dims={out_dims}): `out_dims` must "
f"have one dim per output (got {num_outputs} outputs) of {_get_name(func)}.",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/utils.py
# Line: 1603

lambda: {
    k: list(v) if isinstance(v, set) else v
    for k, v in dataclasses.asdict(compilation_metrics).items()
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/convert_frame.py
# Line: 491

return lambda backend: convert_frame_assert(
    backend,
    self._one_graph,
    self._export,
    self._export_constraints,
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/codegen.py
# Line: 631

lambda: self.extend_output(
    [
        self.create_load_python_module(torch),
        self.create_load_attr("_as_tensor_fullprec"),
    ]
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/compiled_autograd.py
# Line: 973

payload_fn=lambda: GraphModule(
    self.fx_tracer.root,
    self.fx_tracer.graph,
    f"CompiledAutograd{self.id}PreReordering",
).print_readable(print_output=False),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/misc.py
# Line: 1541

lambda: codegen.extend_output(
    [
        codegen.create_load_const(self.format_string),
        codegen.create_load_attr("format"),
    ]
),

# ==================================================
# Line: 1885

lambda: codegen.extend_output(
    [
        codegen.create_load_python_module(random),
        codegen.create_load_attr("Random"),
    ]
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/functions.py
# Line: 2198

lambda: codegen.load_import_from(
    "triton.tools.experimental_descriptor",
    f"create_{len(self.dims)}d_tma_descriptor",
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/builder.py
# Line: 589

lambda self, value: LambdaVariable(
    _dataclasses_fields_lambda,
    source=self.source,
    **self.install_guards(GuardBuilder.FUNCTION_MATCH),
),

# ==================================================
# Line: 921

lambda: UserFunctionVariable(
    torch._dynamo.external_utils.FakeCompiledAutogradEngine.exec_final_callbacks,
).call_function(
    self.tx,
    (self.tx.output.side_effects.get_ca_final_callbacks_var(),),
    {},
)

# ==================================================
# Line: 3542

handlers[dict] = lambda tx, value: ConstDictVariable(
    {create(tx, k): create(tx, v) for k, v in value.items()},
    type(value),
    mutation_type=ValueMutationNew(),
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/builtin.py
# Line: 493

lambda tx, a, b: ListVariable(
    [*a.items, *b.unpack_var_sequence(tx)],
    mutation_type=ValueMutationNew(),
),

# ==================================================
# Line: 658

lambda tx, a, b: ConstantVariable(
    op(
        tx.output.get_submodule(a.module_key),
        tx.output.get_submodule(b.module_key),
    )
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/dicts.py
# Line: 321

lambda: codegen.extend_output(
    [
        codegen.create_load_python_module(collections),
        codegen.create_load_attr("OrderedDict"),
    ]
)

# ==================================================
# Line: 642

lambda: codegen.extend_output(
    [
        codegen.create_load_python_module(types),
        codegen.create_load_attr("MappingProxyType"),
    ]
)

# ==================================================
# Line: 743

lambda: codegen.extend_output(
    [
        codegen.create_load_python_module(collections),
        codegen.create_load_attr("defaultdict"),
    ]
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/iter.py
# Line: 309

lambda: codegen.extend_output(
    [
        codegen.create_load_python_module(itertools),
        codegen.create_load_attr("repeat"),
    ]
)

# ==================================================
# Line: 339

lambda: codegen.extend_output(
    [
        codegen.create_load_python_module(itertools),
        codegen.create_load_attr("count"),
    ]
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_meta_registrations.py
# Line: 137

lambda: f"linspace(): inferred dtype {default_complex_dtype} can't be safely cast to passed dtype {dtype}",

# ==================================================
# Line: 146

        lambda: f"received an invalid combination of arguments - got \
({type(start).__name__}, {type(end).__name__}, {type(steps).__name__})",

# ==================================================
# Line: 189

lambda: (
    f"linalg.cross: inputs dimension {dim} must have length 3. "
    f"Got {self.size(dim)} and {other.size(dim)}"
),

# ==================================================
# Occurrences: Lines 892-903 (2 instances)

lambda: (
    f"Expected b and A to be on the same device, but found b on "
    f"{self.device} and A on {A.device} instead."
),

# ==================================================
# Line: 916

lambda: (
    f"Incompatible matrix sizes for {name}: each A "
    f"matrix is {A.size(-1)} by {A.size(-1)}"
    f" but each b matrix is {self.size(-2)} by {self.size(-1)}"
),

# ==================================================
# Line: 971

lambda: (
    f"{fn_name}: Expected {result_name} and input tensors to be on the same device, but got "
    f"{result_name} on {result.device} and input on {input.device}"
),

# ==================================================
# Occurrences: Lines 1104-1116 (3 instances)

lambda: "torch.linalg.householder_product: input.shape[-2] must be greater than or equal to input.shape[-1]",

# ==================================================
# Occurrences: Lines 1123-1134 (2 instances)

lambda: (
    f"torch.linalg.householder_product: Expected batch dimensions of tau to be "
    f"equal to input.shape[:-2], but got {actual_batch_tau_shape}"
),

# ==================================================
# Occurrences: Lines 1194-1205 (2 instances)

lambda: (
    f"torch.linalg.ldl_solve: Expected B to have at least 2 dimensions, "
    f"but it has {B.ndim} dimensions instead"
),

# ==================================================
# Line: 1302

lambda: (
    f"linalg.lu_solve: Expected LU and B to have the same dtype, "
    f"but found LU of type {LU.dtype} and B of type {B.dtype} instead"
),

# ==================================================
# Line: 1323

lambda: (
    f"linalg.lu_solve: Expected LU.shape[:-1] and pivots.shape to be the same, "
    f"but got pivots with shape {pivots.shape} instead"
),

# ==================================================
# Line: 1360

lambda: (
    "torch.lu_unpack: LU_pivots is expected to be a contiguous tensor of torch.int32 dtype.\n"
    "Note: this function is intended to be used with the output produced by torch.linalg.lu_factor"
),

# ==================================================
# Line: 1400

lambda: (
    f"qr received unrecognized mode '{mode}' "
    f"but expected one of 'reduced' (default), 'r', or 'complete'"
),

# ==================================================
# Line: 1554

lambda: (
    f"linalg.solve: Expected A and B to have the same dtype, but found A of type "
    f"{A.dtype} and B of type {B.dtype} instead"
),

# ==================================================
# Line: 1565

lambda: (
    "linalg.solve: Vector broadcasting of the left hand side is not supported for left=False. "
    "In this case linalg.solve is equivalent to B / A.squeeze(-1)"
),

# ==================================================
# Occurrences: Lines 1635-1645 (2 instances)

lambda: (
    f"torch.triangular_solve: Expected b to have at least 2 dimensions, "
    f"but it has {self.ndim} dimensions instead"
),

# ==================================================
# Line: 1706

lambda: f"torch.ormqr: other.shape[{left_size_condition}] must be greater than or equal to tau.shape[-1]",

# ==================================================
# Occurrences: Lines 1720-1730 (2 instances)

lambda: (
    f"torch.ormqr: Expected tau to have one dimension less than input, "
    f"but got tau.ndim equal to {tau.ndim} and input.ndim is equal to {input.ndim}"
),

# ==================================================
# Line: 1738

lambda: (
    f"torch.ormqr: Expected batch dimensions of tau to be "
    f"equal to input.shape[:-2], but got {actual_batch_tau_shape}"
),

# ==================================================
# Occurrences: Lines 1747-1765 (3 instances)

lambda: (
    f"torch.ormqr: Expected batch dimensions of other to be "
    f"equal to input.shape[:-2], but got {actual_batch_other_shape}"
),

# ==================================================
# Line: 1803

lambda: (
    f"Expected {dim + 1}D or {dim + 2}D (batch mode) tensor with possibly 0 batch size "
    f"and other non-zero dimensions for input, but got: {input.shape}"
),

# ==================================================
# Line: 1831

lambda: (
    f"Argument #4: Padding size should be less than the corresponding input dimension, "
    f"but got: padding ({pad_l}, {pad_r}) at dimension {dim_w} of input {input.shape}"
),

# ==================================================
# Line: 1880

lambda: (
    f"Argument #4: Padding size should be less than the corresponding input dimension, "
    f"but got: padding ({pad_l}, {pad_r}) at dimension {dim_w} of input {input.shape}"
),

# ==================================================
# Occurrences: Lines 1932-1950 (3 instances)

lambda: (
    f"Argument #4: Padding size should be less than the corresponding input dimension, "
    f"but got: padding ({pad_l}, {pad_r}) at dimension {dim_w} of input {input.shape}"
),

# ==================================================
# Occurrences: Lines 2042-2067 (4 instances)

lambda: (
    f"Argument #4: Padding size should be less than the corresponding input dimension, "
    f"but got: padding ({pad_l}, {pad_r}) at dimension {dim_w} of input {input.shape}"
),

# ==================================================
# Line: 2182

lambda: f"Input dtypes must be the same, got: input: {self.dtype}, batch1: {batch1.dtype}, batch2: {batch2.dtype}",

# ==================================================
# Line: 2190

lambda: (
    f"Expected size for first two dimensions of batch2 tensor to be: "
    f"[{bs}, {contraction_size}] but got: [{batch2_sizes[0]}, {batch2_sizes[1]}]."
),

# ==================================================
# Line: 2383

lambda: f"Given input size per channel: {list(dims)}. "
f"Calculated output size per channel: {ret_shape[2:]}. "
f"Output size is too small",

# ==================================================
# Line: 2718

lambda: f"Expected a tensor of dimension {dim} and tensor.size[{dim_size}] == {size}, "
+ f"but got : dimension {tensor.dim()} and tensor.size[{dim_size}] = {tensor.shape[dim_size]}",

# ==================================================
# Line: 3125

lambda: f"adaptive_avg_pool2d_backward(): Expected grad_output to have non-zero \
          size for non-batch dimensions, {grad_out.shape} with dimension {i} being empty",

# ==================================================
# Line: 3154

lambda: (
    f"{arg_name}(): Expected grad_output to have non-zero size for non-batch dimensions, "
    f"but grad_output has sizes {grad_output.shape} with dimension {i} being empty"
),

# ==================================================
# Line: 3172

lambda: (
    f"adaptive_max_pool2d(): Expected input to have non-zero size for non-batch dimensions, "
    f"but input has sizes {input.shape} with dimension {i} being empty"
),

# ==================================================
# Line: 3215

lambda: f"adaptive_max_pooling2d_backward(): Expected 3D or 4D grad_output, but got: {grad_output.shape}",

# ==================================================
# Line: 3240

lambda: (
    f"adaptive_max_pool3d(): Expected input to have non-zero size for non-batch dimensions, "
    f"but input has sizes {input.shape} with dimension {i} being empty"
),

# ==================================================
# Line: 3307

lambda: "The register_meta function for torch.nonzero() raises unimplemented by default, "
"as a correct data-independent implementation does not exist. This implementation "
"returns a fake value, assuming all elements of the tensor are non-zero. "
"To enable this registration, please set "
"'torch.fx.experimental._config.meta_nonzero_assume_all_nonzero' to True.",

# ==================================================
# Line: 3343

lambda: f"The shape of the mask {index.shape} at index {i} "
f"does not match the shape of the indexed tensor {self.shape} at index {k + j}",

# ==================================================
# Occurrences: Lines 3492-3499 (2 instances)

lambda: f"batch1 and batch2 must have same number of batches, got {batch1.size(0)} and {batch2.size(0)}",

# ==================================================
# Line: 3591

lambda: (
    f"Incompatible matrix sizes for _int_mm ({a.size(0)}x{a.size(1)} "
    f"and {b.size(0)}x{b.size(1)})"
),

# ==================================================
# Line: 3954

lambda: (
    f"expected per_sample_weights.numel() ({per_sample_weights.numel()} "
    f"to be the same as indices.numel() ({indices.numel()})"
),

# ==================================================
# Line: 4079

lambda: "Number of dimensions of repeat dims can not be smaller than number of dimensions of tensor",

# ==================================================
# Line: 4281

lambda: "masked_scatter: expected self and source to have same "
f"dtypes but got {self.dtype} and {source.dtype}",

# ==================================================
# Line: 4325

lambda: f"Expected size for first two dimensions of batch2 tensor to be: [{bs}"
f", {contraction_size}] but got: [{batch2_sizes[0]}, {batch2_sizes[1]}].",

# ==================================================
# Line: 4334

lambda: "out_dtype only supported for torch.float32 output with float16/bfloat16 inputs or same as input dtypes",

# ==================================================
# Line: 4345

lambda: f"Expected an input tensor shape with shape {output_size} but got shape: {self_baddbmm.size()}",

# ==================================================
# Line: 4403

lambda: (
    f"pad should be at most half of effective kernel size, but got pad={pad}, "
    f"kernel_size={kernelSize} and dilation={dilation}"
),

# ==================================================
# Line: 4443

lambda: "dilation should be greater than zero, but got dilationH: {dilationH}, dilationW: {dilationW}",

# ==================================================
# Line: 4451

lambda: "Expected 4D (batch mode) tensor expected for input with channels_last layout"
" with optional 0 dim batch size for input, but got: {input.size()}",

# ==================================================
# Occurrences: Lines 4458-4471 (3 instances)

lambda: f"Expected 3D or 4D (batch mode) tensor with optional 0 dim batch size for input, but got: {input.size()}",

# ==================================================
# Line: 4516

lambda: (
    f"dilation should be greater than zero, but got "
    f"dilationT: {dilationT}, dilationH: {dilationH}, dilationW: {dilationW}"
),

# ==================================================
# Line: 4533

lambda: (
    f"{fn_name}: Expected input's non-batch dimensions to have positive length,"
    f" but input has a shape of {input.shape}"
    f" and non-batch dimension {input.size(i)} has length zero!"
),

# ==================================================
# Occurrences: Lines 4543-4563 (3 instances)

lambda: (
    f"input image (T: {itime} H: {iheight} W: {iwidth}) smaller than "
    f"kernel size (kT: {kT} kH: {kH} kW: {kW})"
),

# ==================================================
# Occurrences: Lines 4901-4905 (2 instances)

lambda: f"fractional_max_pool2d: kernel height {kernel_size[0]} is too large relative to input height {input_height}",

# ==================================================
# Occurrences: Lines 5138-5162 (4 instances)

lambda: (
    f"grid_sampler(): expected input and grid to be on same device, but input "
    f"is on {input.device} and grid is on {grid.device}"
),

# ==================================================
# Line: 5168

lambda: (
    f"grid_sampler(): expected input to have non-empty spatial dimensions, "
    f"but input has sizes {input.shape} with dimension {i} being empty"
),

# ==================================================
# Line: 5184

lambda: (
    f"grid_sampler(): expected 5D input and grid with same number of "
    f"dimensions, but got input with sizes {input.shape}"
    f" and grid with sizes {grid.shape}"
),

# ==================================================
# Line: 5432

lambda: f"Size does not match at dimension {i} expected index {index.shape}"
+ f" to be no larger than self {self.shape} apart from dimension {dim}",

# ==================================================
# Occurrences: Lines 5538-5545 (2 instances)

lambda: f"Expected index {index.shape} to be no larger than self {self.shape}"
+ f" apart from dimension {dim} and to be no larger than src {src_opt.shape}",

# ==================================================
# Line: 6253

lambda: f"Expected both inputs to be fp8 or fp4 types but got self.dtype={self.dtype} and mat2.dtype={mat2.dtype}",

# ==================================================
# Line: 6345

lambda: (
    "Invalid blockwise scaling configuration. "
    f"For blockwise scaling, scale_a should have {expected_a_size} elements, got {scale_a.numel()}, "
    f"scale_b should have {expected_b_size} elements, got {scale_b.numel()}."
),

# ==================================================
# Line: 6359

lambda: f"For non-tensorwise scaling, scale tensors must be 2D, but got {scale_a.dim()=} and {scale_b.dim()=}",

# ==================================================
# Line: 6377

lambda: (
    "Invalid scaling configuration. "
    "For tensorwise scaling, both scales should be scalar. "
    f"For rowwise scaling, scale_a should be ({m}, 1), scale_b should be (1, {n}). "
    f"Got scale_a.size()=({scale_a.size(0)}, {scale_a.size(1)}) "
    f"and scale_b.size()=({scale_b.size(0)}, {scale_b.size(1)})"
),

# ==================================================
# Occurrences: Lines 6432-6438 (2 instances)

lambda: f"It is expected input_size equals to {expected_input_dims}, but got size {len(input_size)}",

# ==================================================
# Line: 6510

lambda: (
    f"Expected grad_output to have the same shape as output;"
    f" output.size({i}) = {full_output_size[i]}"
    f" but got grad_output.size({i}) = {grad_output.size(i)}"
),

# ==================================================
# Line: 6593

lambda: f"{prev_hidden.numel()} != {input_gates.size(0)} * {gates_size} // {factor} (aka {expected_prev_hidden_numel})",

# ==================================================
# Line: 7002

            lambda: f"""
Expected grad_output to have the same shape as output; output.size({i}) = {full_output_size[i]}
but got grad_output_size({i}) = {grad_output.size(i)}""",

# ==================================================
# Line: 7102

lambda: (
    "torch.searchsorted(): boundaries tensor should be 1 dimension or the "
    "first N-1 dimensions of boundaries tensor and input value tensor must "
    f"match, but we got boundaries tensor {list(sorted_sequence.shape)} and "
    f"input value tensor {list(self.shape)}"
),

# ==================================================
# Line: 7113

lambda: (
    "torch.searchsorted(): boundary and sorter must have the same size, but "
    f"got boundary tensor {list(sorted_sequence.shape)} and got sorter tensor "
    f"{list(sorter.shape) if sorter is not None else []}"
),

# ==================================================
# Line: 7383

lambda: f"Expected trailing dimension of mat_a to be divisible by 16 but got mat1 shape: {mat_a.size()}",

# ==================================================
# Line: 7503

lambda: "Length of pad should be no more than twice the number of "
f"dimensions of the input. Pad length is {len(pad)} while the input has "
f"{l_inp} dimensions.",

# ==================================================
# Line: 7514

lambda: f"The input size {input_sizes[l_diff + i]}, plus negative padding "
f"{pad[pad_idx]} and {pad[pad_idx + 1]} resulted in a negative output size, "
f"which is invalid. Check dimension {l_diff + i} of your input.",

# ==================================================
# Line: 7667

lambda: (
    "Integer division with addcdiv is no longer supported, and in a future ",
    "release addcdiv will perform a true division of tensor1 and tensor2. ",
    "The historic addcdiv behavior can be implemented as ",
    "(input + value * torch.trunc(tensor1 / tensor2)).to(input.dtype) ",
    "for integer inputs and as ",
    "(input + value * tensor1 / tensor2) for float inputs. ",
    "The future addcdiv behavior is just the latter implementation: ",
    "(input + value * tensor1 / tensor2), for all dtypes.",
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_init_utils.py
# Line: 588

check_fn=lambda submodule: _get_module_fsdp_state(submodule) is None
and submodule not in state._ignored_modules,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/pipelining/stage.py
# Occurrences: Lines 604-618 (2 instances)

return lambda: (
    stage_backward(
        bwd_kwargs["stage_output"],
        bwd_kwargs["output_grads"],
        bwd_kwargs["input_values"],
    ),
    None,
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/_expanded_weights/conv_utils.py
# Line: 221

lambda: F.unfold(
    input.unsqueeze(-2),
    kernel_size=(1, kernel_size[0]),
    dilation=(1, dilation[0]),
    padding=(0, padding[0]),
    stride=(1, stride[0]),
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/__init__.py
# Line: 418

lambda: f"Attempting to broadcast a dimension of length {shape[idx]} at {idx}! "
f"Mismatching argument at index {arg_idx} had {shape}; but expected shape "
f"should be broadcastable to {common_shape}",

# ==================================================
# Line: 870

lambda: (
    "Negation, the `-` operator, on a bool tensor is not supported. "
    "If you are trying to invert a mask, use the `~` or `logical_not()` "
    "operator instead."
),

# ==================================================
# Line: 1015

lambda: f"view_as_complex is only supported for floating point"
f"tensors, but got a tensor of scalar type: {input_dtype}",

# ==================================================
# Occurrences: Lines 1073-1079 (2 instances)

lambda: f"{name}: Received a lhs Python scalar to an elementwise binary "
"operation that does not accept lhs scalars!",

# ==================================================
# Line: 1759

lambda: (
    "Subtraction, the `-` operator, with two bool tensors is not supported. "
    "Use the `^` or `logical_xor()` operator instead."
),

# ==================================================
# Line: 2519

lambda: (
    f"mean(): could not infer output dtype. "
    f"{'Input' if orig_dtype is None else 'Optional'} dtype must be either "
    f"a floating point or complex dtype. Got: {dtype}"
),

# ==================================================
# Line: 2798

lambda: "Number of dimensions of tensors must match.  "
f"Expected {example.ndim}-D tensors, but got {t.ndim}-D for "
f"tensor number {i} in the list",

# ==================================================
# Line: 2826

lambda: f"Number of dimensions of tensors must match.  "
f"Expected {example.ndim}-D tensors, but got 1-D for "
f"tensor number {tensor_idx} in the list",

# ==================================================
# Line: 2903

lambda: "Length of pad should be no more than twice the number of "
f"dimensions of the input. Pad length is {len(pad)} while the input has "
f"{l_inp} dimensions.",

# ==================================================
# Line: 2936

lambda: f"The input size {input_sizes[l_diff + i]}, plus negative padding "
f"{pad[pad_idx]} and {pad[pad_idx + 1]} resulted in a negative output size, "
f"which is invalid. Check dimension {l_diff + i} of your input.",

# ==================================================
# Line: 3132

lambda: f"start out of range (expected to be in range of [{-dim_length}, {dim_length}], but got {start})",

# ==================================================
# Line: 3200

lambda: "Expected number of channels in input to be divisible by num_groups, "
+ f"but got input of shape {input.shape} and num_groups = {num_groups}",

# ==================================================
# Line: 3267

lambda: "Expected normalized_shape to be at least 1-dimensional, i.e., "
+ "containing at least one element, but got normalized_shape = "
+ str(normalized_shape),

# ==================================================
# Line: 3397

lambda: (
    f"stft input and window must be on the same device but got self on {input.device}"
    + f" and window on {window.device}"  # type: ignore[union-attr]
),

# ==================================================
# Line: 3456

lambda: (
    f"expected a 1D window tensor of size equal to win_length={win_length_}, "
    + f"but got window with size {window.shape}"  # type: ignore[union-attr]
),

# ==================================================
# Line: 3513

lambda: (
    f"istft input and window must be on the same device but got self on {input.device}"
    + f" and window on {window.device}"  # type: ignore[union-attr]
),

# ==================================================
# Line: 3524

lambda: (
    "istft input and window must be on the same device but got self on "
    + f"{input.device} and window on {window.device}"  # type: ignore[union-attr]
),

# ==================================================
# Occurrences: Lines 3543-3554 (2 instances)

lambda: (
    "istft expected the frequency dimension (3rd to the last) of the input tensor "
    + "to match n_fft / 2 + 1 when onesided=True, but got {fft_size}"
),

# ==================================================
# Line: 3681

lambda: "repeat: Number of dimensions of repeat dims can not be smaller than number of dimensions of tensor",

# ==================================================
# Line: 4353

lambda: f"Split sizes add up to {builtins.sum(split_sizes)} but got the tensor's size of {self.shape[dim]}",

# ==================================================
# Line: 4448

lambda: (
    "torch.hsplit requires a tensor with at least 1 dimension, but got a tensor with "
    + str(a.ndim)
    + " dimensions!"
),

# ==================================================
# Line: 4473

lambda: (
    "hsplit(): received an invalid combination of arguments. "
    "Expected indices_or_sections to be of type int, list of ints or tuple of ints "
    f"but got type {type(indices_or_sections)}"
),

# ==================================================
# Line: 4490

lambda: (
    "torch.vsplit requires a tensor with at least 2 dimension, but got a tensor with "
    + str(a.ndim)
    + " dimensions!"
),

# ==================================================
# Line: 4500

lambda: (
    f"torch.vsplit attempted to split along dimension 0"
    f", but the size of the dimension "
    f"{a.shape[0]}"
    f" is not divisible by the split_size "
    f"{split_size}"
    f"!"
),

# ==================================================
# Line: 4513

lambda: (
    "vsplit(): received an invalid combination of arguments. "
    "Expected indices_or_sections to be of type int, list of ints or tuple of ints "
    f"but got type {type(indices_or_sections)}"
),

# ==================================================
# Line: 4553

lambda: "expected src to have a size equal to the diagonal of the input."
f"Got {src.shape} for a diagonal of shape {diag.shape}",

# ==================================================
# Line: 4684

lambda: "Input tensors must all be on the same device. "
f"Input 0 is on device {device} and input {i} is on device {tensor.device}.",

# ==================================================
# Line: 4744

lambda: (
    "The use of `x.T` on tensors of dimension other than 0 or 2 "
    "to reverse their shape is not supported."
),

# ==================================================
# Line: 4875

lambda: (
    "torch.take_along_dim(): input and indices should have the same "
    f"number of dimensions, but got {a.ndim} dimensions for input, and "
    f"{indices.ndim} dimensions for indices"
),

# ==================================================
# Line: 5369

lambda: f"linspace(): inferred dtype {default_complex_dtype} can't be safely cast to passed dtype {dtype}",

# ==================================================
# Line: 5378

        lambda: f"received an invalid combination of arguments - got \
({type(start).__name__}, {type(end).__name__}, {type(steps).__name__})",

# ==================================================
# Line: 5579

lambda: (
    "movedim: Invalid source or destination dims: source "  # type: ignore[arg-type]
    f"({list(source)} dims) should contain the same number "  # type: ignore[arg-type]
    f"of dims as destination ({list(destination)} dims)"  # type: ignore[arg-type]
),

# ==================================================
# Line: 6256

lambda: f"Cauchy distribution is a continuous probability distribution. \
dtype must be a floating point but you specified {self.dtype}",

# ==================================================
# Line: 6278

lambda: f"Exponential distribution is a continuous probability distribution. \
dtype must be a floating point but you specified {self.dtype}",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/_conversions.py
# Occurrences: Lines 85-95 (2 instances)

lambda: (
    f"Expected both inputs to be Half, Float or Double tensors but got "
    f"{real.dtype} and {imag.dtype}"
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/linalg/__init__.py
# Occurrences: Lines 50-59 (2 instances)

lambda: "{fn_name}: dtype should be {d} for {d} inputs. Got {dtype}".format(
    fn_name=fn_name,
    d="complex" if utils.is_complex_dtype(x_dtype) else "real",
    dtype=dtype,
),

# ==================================================
# Line: 308

lambda: "linalg.norm: If dim is not specified but ord is, the input must be 1D or 2D. Got {A.ndim}D",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/nn/functional/__init__.py
# Line: 245

lambda: f"input_scale argument of type {type(input_scale)} cannot be safely cast to type {python_type}!",

# ==================================================
# Line: 287

lambda: f"channel_shuffle expects input with > 2 dims, but got input with sizes {list(input.size())}",

# ==================================================
# Line: 334

lambda: "Expected number of channels in input to be divisible by num_groups, "
+ f"but got input of shape {input.shape} and num_groups = {num_groups}",

# ==================================================
# Line: 841

lambda: (
    "Expected input and target to both have ndim > 0 and "
    "target.shape[1:] == input.shape[2:], but got "
    f"target.shape {target.shape} and input.shape {input.shape}"
),

# ==================================================
# Line: 990

lambda: (
    f"The anchor, positive, and negative tensors are expected to have "
    f"the same number of dimensions, but got: anchor {a_dim}D, "
    f"positive {p_dim}D, and negative {n_dim}D inputs"
),

# ==================================================
# Line: 1143

lambda: f"Mismatch of parameter numbers and input channel size. Found parameter numbers ="
f" {weight.numel()} and channel size = {channel_size}.",

# ==================================================
# Line: 1233

lambda: f"pixel_shuffle expects input to have at least 3 dimensions, but got input with {self.dim} dimension(s)",

# ==================================================
# Line: 1261

lambda: f"pixel_unshuffle expects input to have at least 3 dimensions, but got input with {self.dim} dimension(s)",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_prims_common/__init__.py
# Line: 969

lambda: (
    f"The size of tensor a ({sizeA}) must match the size of "
    f"tensor b ({sizeB}) at non-jagged dimension {i}"
),

# ==================================================
# Line: 997

lambda: (
    f"invalid shape dimension {d}. If this was symbolic, it was assumed to not be -1."
    "If this was meant to be inferred, please explicitly pass in -1."
),

# ==================================================
# Line: 2075

lambda: (
    f"{caller} does not have a deterministic implementation, but you set "
    f"'torch.use_deterministic_algorithms(True)'. You can turn off "
    f"determinism just for this operation, or you can use the "
    f"'warn_only=True' option, if that's acceptable for your application. "
    f"You can also file an issue at https://github.com/pytorch/pytorch/issues "
    f"to help us prioritize adding deterministic support for this operation."
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_prims_common/wrappers.py
# Line: 226

lambda: f"Attempting to cast from {copy_from.dtype} to out tensor with dtype {copy_to.dtype}, "
"but this can't be cast because it is not safe!",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/runtime_wrappers.py
# Line: 1509

lambda: (
    "It looks like you're trying to call a compiled backward function within vmap/grad/vjp, "
    "which isn't supported. Try wrapping vmap inside torch.compile, or skip compiling the "
    "backward function."
),

# ==================================================
# Line: 1542

lambda: (
    "This compiled backward function is being run with "
    "torch.use_deterministic_algorithms(True), "
    "but it was previously generated during the forward function while "
    "torch.use_deterministic_algorithms(False) was set."
),

# ==================================================
# Line: 2318

lambda: (
    "This backward function was compiled with non-empty donated "
    "buffers which requires create_graph=False and retain_graph=False. "
    "Please keep backward(create_graph=False, retain_graph=False) "
    "across all backward() function calls, or set "
    "torch._functorch.config.donated_buffer=False to disable "
    "donated buffer."
),

# ==================================================
