# long-lambda-expression snippets for pytorch

# File: /root/ecooptimizer/pytorch/torchgen/gen.py
# Line: 1915

lambda: {
    "static_dispatch_ops_headers": list(
        mapMaybe(
            lambda fn: static_dispatch_ops_header(
                fn, backend_index=static_dispatch_idx
            ),
            functions,
        )
    ),
    "operator_includes": f"#include <ATen/ops/{name}_ops.h>",
    "function_definitions": list(
        mapMaybe(
            ComputeFunction(),
            functions,
        )
    ),
},

# ==================================================
# Line: 2111

lambda: {
    "tensor_method_declarations": list(
        mapMaybe(
            ComputeTensorMethod(
                target=Target.DECLARATION,
                static_dispatch_backend_indices=static_dispatch_idx,
            ),
            native_functions,
        )
    ),
    "tensor_method_definitions": list(
        mapMaybe(
            ComputeTensorMethod(
                target=Target.DEFINITION,
                static_dispatch_backend_indices=static_dispatch_idx,
            ),
            native_functions,
        )
    ),
},

# ==================================================
# Line: 2707

lambda: {
    "ops_headers": [
        "\n".join(
            f"#include <ATen/ops/{f.root_name}_ops.h>\n"
            # NB: this include is important as it ensures we
            # set the visibility on generated view_copy kernels
            # correctly
            f"#include <ATen/ops/{f.root_name}_native.h>"
            for f in (
                [g.view] if g.view_copy is None else [g.view, g.view_copy]
            )
        )
        for g in view_groups
    ]
    + [
        "\n".join(
            f"#include <ATen/ops/{f.root_name}_ops.h>\n"
            # NB: this include is also important for correct visibility
            f"#include <ATen/ops/{f.root_name}_native.h>"
            for f in [g.inplace, g.mutable, g.functional]
            if f is not None and "generated" not in f.tags
        )
        for g in structured_native_functions
    ],
    "CompositeViewCopyKernel_Definitions": list(
        mapMaybe(
            GenCompositeViewCopyKernel(
                backend_indices[
                    DispatchKey.CompositeExplicitAutogradNonFunctional
                ]
            ),
            view_groups,
        )
    ),
    "GeneratedCompositeFunctional_Definitions": list(
        mapMaybe(
            gen_composite_functional_kernel,
            structured_native_functions,
        )
    ),
    "GeneratedCompositeOut_Definitions": list(
        mapMaybe(
            gen_composite_out_kernel,
            structured_native_functions,
        )
    ),
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_backend_stubs.py
# Line: 491

lambda: {
    "extra_cuda_headers": "",
    "external_backend_headers": external_backend_headers_str,
    "ops_headers": "#include <ATen/Functions.h>"
    if not per_operator_headers
    else "",
    "DispatchKey": dispatch_key,
    "dispatch_namespace": dispatch_key.lower(),
    "dispatch_headers": dest.gen_registration_headers(
        backend_index, per_operator_headers=per_operator_headers, rocm=False
    ),
    "dispatch_helpers": dest.gen_registration_helpers(backend_index),
    "dispatch_definitions": fm.substitute_with_template(
        "RegisterDispatchDefinitions.ini",
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
    ).split(newline),
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_lazy_tensor.py
# Line: 533

lambda: {
    "lazy_ir_sysinc": [
        f"#include <{path}>"
        for path in [
            "ATen/core/Formatting.h",
            "c10/core/ScalarType.h",
            "torch/csrc/lazy/core/hash.h",
            "torch/csrc/lazy/core/ir.h",
            "torch/csrc/lazy/core/shape.h",
            "optional",
            "vector",
        ]
    ],
    "lazy_ir_inc": [f'#include "{node_base_hdr}"']
    if node_base_hdr is not None
    else [],
    "ir_declarations": list(
        concat_map_codegen(
            lazy_ir_obj, grouped_native_functions, full_codegen + ir_gen
        )
    ),
    "namespace_prologue": ns_helper.prologue,
    "namespace_epilogue": ns_helper.epilogue,
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/frontend.py
# Line: 266

predicate=lambda m: (inspect.ismethod(m) or inspect.isfunction(m))
and not is_static_fn(cls, m.__name__)
and m.__name__ in cls.__dict__
and not _is_drop_fn(m),

# ==================================================
# Line: 649

predicate=lambda m: (inspect.ismethod(m) or inspect.isfunction(m))
and not is_static_fn(cls, m.__name__)
and m.__name__ in cls.__dict__,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/flex_attention.py
# Line: 131

lambda x: (
    realize_inputs(x)
    if x is not None and not isinstance(x, sympy.Symbol)
    else x
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/compile_fx.py
# Line: 1274

skip_folding_node_fn=lambda node: node.op == "get_attr"
and isinstance(node.target, str)
and (
    node.target.startswith("_torchbind_obj")
    or isinstance(node.meta.get("val", None), FakeScriptObject)
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/metrics.py
# Line: 393

lambda: {
    "kernel_name": kernel_name,
    "kernel_path": kernel_path,
    "kernel_category": kernel_category,
    "size_hints": size_hints,
    "reduction_hint": reduction_hint,
    "line_of_code": kernel_line_of_code,
    "num_load": _count_pattern(proper_kernel_fn_code, "tl.load"),
    "num_store": _count_pattern(proper_kernel_fn_code, "tl.store"),
    "num_for_loop": _count_pattern(proper_kernel_fn_code, "for "),
    "num_atomic_add": _count_pattern(proper_kernel_fn_code, "tl.atomic_add"),
    "num_args": _count_args(proper_kernel_fn_code),
    "xnumel": _parse_numel(proper_kernel_fn_code, "xnumel"),
    "ynumel": _parse_numel(proper_kernel_fn_code, "ynumel"),
    "rnumel": _parse_numel(proper_kernel_fn_code, "rnumel"),
    "kernel_args_num_gb": _parse_kernel_args_num_gb(
        kernel_fn_code, kernel_category
    ),
}

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/comms.py
# Line: 932

criteria_cb=lambda x: not (
    isinstance(x, scheduler.NopKernelSchedulerNode)
    or (
        isinstance(x, scheduler.ExternKernelSchedulerNode)
        and x.node.op_overload in allowed_ops  # type: ignore[union-attr]
    )
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/choices.py
# Line: 316

lambda: {
    "pre_grad_graph_id": V.graph.graph_id,
    "post_grad_graph_id": V.graph.post_grad_graph_id,
    "node1_name": node1.get_name(),
    "node2_name": node2.get_name(),
    "node1_debug_str": write_text(node1.debug_str()),
    "node2_debug_str": write_text(node2.debug_str()),
    "common_buffer_names": list(common_buf_names),  # type: ignore[dict-item]
    "failure_reason": scheduler.decide_fusion_fail_reason(
        node1, node2, common_buf_names
    ),
}

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/sym_node.py
# Line: 1316

metadata_fn=lambda: {
    "method": method,
    "result": str(result),
    "result_id": id(result),
    "arguments": [str(a) for a in arguments],
    "argument_ids": [
        get_id(i) for i in arguments if get_id(i) is not None
    ],
    "user_stack": structured.get_user_stack(3),
    "stack": structured.get_framework_stack(3),
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/symbolic_shapes.py
# Line: 5111

metadata_fn=lambda: {
    "symbol": str(sympy_expr),
    "val": repr(val),
    "vr": range_str,
    "source": source.name(),
    "user_stack": structured.from_traceback(
        TracingContext.extract_stack()
    ),
    "stack": structured.from_traceback(
        CapturedTraceback.extract(skip=1).summary()
    ),
},

# ==================================================
# Line: 6459

metadata_fn=lambda: {
    "expr": repr(expr),
    "result": repr(unsound_expr),
    "stack": structured.from_traceback(
        CapturedTraceback.extract(skip=1).summary()
    ),
},

# ==================================================
# Line: 6534

metadata_fn=lambda: {
    "expr": repr(expr),
    "unhinted_expr": repr(unhinted_expr),
    "expr_id": self._expr_sym_node_id,
    "stack": structured.from_traceback(
        CapturedTraceback.extract(skip=1).summary()
    ),
},

# ==================================================
# Line: 6729

metadata_fn=lambda: {
    "symbol": repr(a),
    "sources": [s.name() for s in self.var_to_sources.get(a, [])],
    "value": repr(tgt),
    "reason": msg,
    "stack": structured.from_traceback(
        CapturedTraceback.extract(skip=1).summary()
    ),
    "user_stack": (
        structured.from_traceback(user_tb) if user_tb else None
    ),
},

# ==================================================
# Occurrences: Lines 7128-7150 (2 instances)

metadata_fn=lambda: {
    "expr": str(g),
    "prefix": prefix,
    "expr_node_id": self._expr_sym_node_id,
    "user_stack": structured.get_user_stack(3),
    "stack": structured.get_framework_stack(3),
    "symbol_to_sources": {
        str(v): k
        for k, v in self.source_to_var.items()
        if v in g.free_symbols
    },
    "frame_locals": asdict(self._find_frame_locals()),
},

# ==================================================
# Occurrences: Lines 7249-7271 (2 instances)

metadata_fn=lambda: {
    "expr": repr(orig_expr),
    "result": repr(unsound_result),
    "stack": structured.from_traceback(
        CapturedTraceback.extract(skip=1).summary()
    ),
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/fake_impls.py
# Line: 641

lambda func: is_builtin(func)
and func.name().startswith("aten::_foreach_")
and has_meta(func)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_prims/__init__.py
# Line: 1719

lambda: (
    f"as_strided_scatter: sizes {size}, strides {stride}, storage offset {storage_offset} "
    f" and itemsize {input.element_size()} requiring a storage size of "
    f"{required_size * input.element_size()} are out of bounds "
    f"for storage of size {input.numel() * input.element_size()}"
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/debug_utils.py
# Line: 472

lambda x: x.to(dtype)
if isinstance(x, torch.Tensor) and x.is_floating_point()
else x,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/guards.py
# Line: 3070

lambda: {
    "code": code_part,
    "stack": (
        structured.from_traceback(guard.stack.summary())
        if guard and guard.stack
        else None
    ),
    "user_stack": (
        structured.from_traceback(guard.user_stack)
        if guard and guard.user_stack
        else None
    ),
}

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/convert_frame.py
# Line: 1071

lambda: {
    "stack": list(
        itertools.takewhile(
            lambda f: f["filename"] != convert_frame_intern,
            structured.from_traceback(
                CapturedTraceback.extract(skip=4 + skip).summary()
            ),
        )
    )
    + [
        {
            "line": code.co_firstlineno,
            "name": code.co_name,
            "filename": structured.intern_string(code.co_filename),
        }
    ]
},

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_meta_registrations.py
# Line: 955

lambda: (
    f"{f_name}: Incompatible shapes of A and B for the equation "
    f"{'AX = B' if left else 'XA = B'}"
    f" ({A.size(-2)}x{A.size(-1)} and {B.size(-2)}x{B.size(-1)})"
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_optim_utils.py
# Line: 333

lambda v: v.cpu() if v.dim() == 0 else _PosDimTensorInfo(v.shape, v.dtype),  # type: ignore[union-attr]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/__init__.py
# Occurrences: Lines 3276-3298 (3 instances)

lambda: "Expected weight to be of same shape as normalized_shape, but got "
+ "weight of shape "
+ str(weight.shape)  # type: ignore[union-attr]
+ " and normalized_shape = "
+ str(normalized_shape),

# ==================================================
# Line: 4459

lambda: (
    "torch.hsplit attempted to split along dimension "
    + str(dim)
    + ", but the size of the dimension "
    + str(a.shape[dim])
    + " is not divisible by the split_size "
    + str(split_size)
    + "!"
),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_prims_common/__init__.py
# Line: 1011

lambda: (
    f"cannot reshape tensor of 0 elements into shape {list(shape)} because the "
    f"unspecified dimension size -1 can be any value and is ambiguous"
    if guard_or_false(numel == 0)
    else f"shape '{list(shape)}' is invalid for input of size {numel}"
),

# ==================================================
