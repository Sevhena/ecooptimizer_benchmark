# string-concat-loop snippets for pytorch

# File: /root/ecooptimizer/pytorch/torchgen/gen.py
# Line: 686

for is_redispatching_fn in [False, True]:
    if is_redispatching_fn:
        dispatcher_exprs_str = ", ".join(
            ["dispatchKeySet"] + [a.name for a in sig.arguments()]
        )
        method_base = "redispatch"
    else:
        dispatcher_exprs_str = ", ".join([a.name for a in sig.arguments()])
        method_base = "call"

    dispatcher_call = method_base
    method_name = f"{name}::{method_base}"

    fn_body = f"""

# ==================================================
# Line: 721

for sig in sig_group.signatures():
    # See Note [The ATen Operators API]
    target_sig = DispatcherSignature.from_schema(f.func)
    exprs = translate(sig.arguments(), target_sig.arguments())
    exprs_str = ", ".join([e.expr for e in exprs])

    if sig.symint:
        intlike_t = "c10::SymInt"
    else:
        intlike_t = "int64_t"

    if Variant.function in f.variants:
        result += f"""

# ==================================================
# Line: 734

for sig in sig_group.signatures():
    # See Note [The ATen Operators API]
    target_sig = DispatcherSignature.from_schema(f.func)
    exprs = translate(sig.arguments(), target_sig.arguments())
    exprs_str = ", ".join([e.expr for e in exprs])

    if sig.symint:
        intlike_t = "c10::SymInt"
    else:
        intlike_t = "int64_t"

    if Variant.function in f.variants:
        result += f"""

# ==================================================
# Line: 767

for sig in sig_group.signatures():
    result += f"{sig.decl()} const;\n"

# ==================================================
# Line: 780

for sig in sig_group.signatures():
    target_sig = DispatcherSignature.from_schema(f.func)
    exprs = translate(sig.arguments(), target_sig.arguments(), method=True)
    exprs_str = ", ".join([e.expr for e in exprs])

    result += f"""

# ==================================================
# Line: 809

for sig in sig_group.signatures():
    target_sig = DispatcherSignature.from_schema(f.func)
    exprs = translate(sig.arguments(), target_sig.arguments())
    exprs_str = ", ".join(["dispatchKeySet"] + [a.expr for a in exprs])

    result += f"""

# ==================================================
# Line: 1635

for namespace in registrations[kernel_namespace]:
    if not registrations[kernel_namespace][namespace]:
        continue
    registration_body += f"""

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/shape_functions/gen_jit_shape_functions.py
# Line: 110

for output_str in output_strs:
    start = '+ std::string(R"=====('
    end = '\n)=====")\n'
    final_output += start + output_str + end

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_backend_stubs.py
# Line: 328

for expected_name, funcs in expected_backend_kernel_name_counts.items():
    expected_overload_count = len(funcs)
    actual_overload_count = actual_backend_kernel_name_counts[expected_name]
    if expected_overload_count != actual_overload_count:

        def create_decl(f: NativeFunction) -> str:
            with native_function_manager(f):
                return DispatcherSignature.from_schema(f.func).decl()

        expected_schemas_str = "\n".join([create_decl(f) for f in funcs])
        missing_kernels_err_msg += f"""

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/dest/register_dispatch_key.py
# Line: 284

for arg in args:
    # Only tensor like arguments are eligible
    if arg.type.is_tensor_like():
        device_check += f"""

# ==================================================
# Line: 448

for cpp_sig in cpp_sig_group.signatures(symint=self.symint):
    result += f"TORCH_API {cpp_sig.decl()};\n"

# ==================================================
# Line: 461

for cpp_sig in cpp_sig_group.signatures(symint=self.symint):
    result += generate_defn(cpp_sig)

# ==================================================
# Line: 804

for cpp_sig in cpp_sig_group.signatures(symint=self.symint):
    result += f"TORCH_API {cpp_sig.decl()};\n"

# ==================================================
# Line: 818

for cpp_sig in cpp_sig_group.signatures(symint=self.symint):
    result += generate_defn(cpp_sig)

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/dest/ufunc.py
# Line: 272

    for config in BinaryScalarSpecializationConfigs:
        if config.ufunc_key not in inner_loops:
            continue
        ufunctor_sig = inner_loops[config.ufunc_key]
        scalar_idx = config.scalar_idx + 1
        # Make a copy and at the same time widen the type (not permissible
        # without copy; we don't want to mutate the input argument anyway)
        ctx: list[Expr | Binding] = list(parent_ctx)
        ctx.append(
            Expr(
                expr=f"iter.scalar_value<opmath_t>({scalar_idx})",
                type=NamedCType(config.ctor_tensor, BaseCType(opmath_t)),
            )
        )
        ufunctor_ctor_exprs_str = ", ".join(
            a.expr for a in translate(ctx, ufunctor_sig.arguments().ctor)
        )

        # NB: ufunctor must be allocated before iter.remove_operand is called,
        # as it relies on iter
        body += f"""\
else if (iter.is_cpu_scalar({scalar_idx})) {{

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_python_dispatcher.py
# Line: 163

for line in state_entries:
    first = line.split(":")[0]
    if any(first.startswith(k) for k in self.supported_keys):
        kernel = line.split("::")[0].split(" ")[1]
        output += self._format_line(first, kernel)

# ==================================================
# Line: 181

for line in table_entries:
    k = line.split(":")[0]
    if k in self.runtime_keys:
        entry = regex.sub("[", line)
        output += self._format_line(k, entry.split(": ")[1])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_script.py
# Line: 1670

for col in self.cols:
    header, rows = col.materialize()
    header_buffer += header
    cells.append((header, dict(rows)))


# ==================================================
# Occurrences: Lines 1680-1682 (2 instances)

for header, rows in cells:
    cell = rows.get(line)
    if cell is None:
        row_buffer += pad("", len(header))
    else:
        row_buffer += cell

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/supported_ops.py
# Line: 339

for fn in op_gathering_fns:
    header, items = fn()
    link_target = header.replace("`", "").replace("-", "").lower().replace(" ", "-")
    if isinstance(items, str):
        section = f"{header}\n{'~' * len(header)}\n{items}\n"
    else:
        section = f"{header}\n{'~' * len(header)}\n{emit_block(items)}"
    section = f".. _{link_target}:" + "\n\n" + section
    body += section


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_trace.py
# Line: 406

for n_mod, n_check in zip(
    mod_canonicalized.nodes(), check_canonicalized.nodes()

# ==================================================
# Line: 423

for n_mod, n_check in zip(
    mod_canonicalized.nodes(), check_canonicalized.nodes()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/__init__.py
# Line: 274

for dll in dlls:
    is_loaded = False
    if with_load_library_flags:
        res = kernel32.LoadLibraryExW(dll, None, 0x00001100)
        last_error = ctypes.get_last_error()
        if res is None and last_error != 126:
            err = ctypes.WinError(last_error)
            err.strerror += (
                f' Error loading "{dll}" or one of its dependencies.'
            )
            raise err
        elif res is not None:
            is_loaded = True
    if not is_loaded:
        if not path_patched:
            os.environ["PATH"] = ";".join(dll_paths + [os.environ["PATH"]])
            path_patched = True
        res = kernel32.LoadLibraryW(dll)
        if res is None:
            err = ctypes.WinError(ctypes.get_last_error())
            err.strerror += (
                f' Error loading "{dll}" or one of its dependencies.'
            )
            raise err


# ==================================================
# Line: 287

for dll in dlls:
    is_loaded = False
    if with_load_library_flags:
        res = kernel32.LoadLibraryExW(dll, None, 0x00001100)
        last_error = ctypes.get_last_error()
        if res is None and last_error != 126:
            err = ctypes.WinError(last_error)
            err.strerror += (
                f' Error loading "{dll}" or one of its dependencies.'
            )
            raise err
        elif res is not None:
            is_loaded = True
    if not is_loaded:
        if not path_patched:
            os.environ["PATH"] = ";".join(dll_paths + [os.environ["PATH"]])
            path_patched = True
        res = kernel32.LoadLibraryW(dll)
        if res is None:
            err = ctypes.WinError(ctypes.get_last_error())
            err.strerror += (
                f' Error loading "{dll}" or one of its dependencies.'
            )
            raise err


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler_util.py
# Occurrences: Lines 292-293 (2 instances)

for entry in reversed(evt.stack):
    stack_str += entry.translate(translate_table)
    stack_str += ";"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/converter.py
# Line: 1503

for i, n in enumerate(graph_converter.unsupported_node_list):
    node_str = "".join(str(n).split("\n")[:1])
    explain_str += f"\n\n    {i}. {n.kind()} [{node_str}]"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/serde/schema_check.py
# Line: 696

for f, d in fields.items():
    if kind == "struct" and "default" not in d:
        reason += (
            f"Field {k}.{f} is added to schema.py without a default value as an incomparible change "
            + "which requires major version bump.\n"
        )
        next_version = [commit.base["SCHEMA_VERSION"][0] + 1, 1]


# ==================================================
# Line: 718

for f in v["fields"]:
    reason += (
        f"Field {k}.{f} is added to schema.py as an compatible change "
        + "which still requires minor version bump.\n"
    )

# ==================================================
# Line: 729

for f in v["fields"]:
    reason += (
        f"Field {k}.{f} is removed from schema.py as an compatible change "
        + "which still requires minor version bump.\n"
    )

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codecache.py
# Line: 1766

for c in consts:
    consts_asm += f"\t.byte {c}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fuzzer.py
# Occurrences: Lines 956-961 (2 instances)

for col_name in input_list:
    col = "<br>".join(col_name)
    html_content += f"<th>{col}</th>"

# ==================================================
# Occurrences: Lines 989-990 (2 instances)

for col_name in input_list:
    # Determine the status class for the cell
    status_enum = results.lookup((row_name, col_name))
    status_class = ""
    status_val = ""
    if status_enum == Status.SKIPPED:
        status_class = "skipped"
        status_val = "-"
    elif status_enum == Status.PASSED:
        status_class = "passed"
        status_val = "O"
    elif status_enum == Status.FAILED_RUN_EAGER_EXCEPTION:
        status_class = "failed"
        status_val = "e"
    elif status_enum == Status.FAILED_RUN_COMPILE_EXCEPTION:
        status_class = "failed"
        status_val = "E"
    elif status_enum == Status.FAILED_RUN_RETURN:
        status_class = "failed"
        status_val = "R"
    elif status_enum == Status.FAILED_COMPILE:
        status_class = "failed"
        status_val = "C"
    else:
        status_class = "skipped"
        status_val = "-"

    html_content += f'<td class="{status_class}">{status_val}</td>'

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_wrapper_cpu.py
# Line: 2301

for idx, (raw_arg, schema_arg) in enumerate(
    zip(raw_args, op_overload._schema.arguments)

# ==================================================
# Line: 2326

for idx, output_arg in enumerate(output_args):
    if output_arg is None:
        continue
    lines += f"{output_arg} = reinterpret_cast<AtenTensorHandle>(PyCapsule_GetPointer(PyList_GET_ITEM(py_{buf_name}.get(), {idx}), NULL));\n"  # noqa: B950


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_micro_gemm.py
# Line: 1255

for num_rows in range(block_m, 0, -16):
    amx_kernel_options = {**options, "num_rows": num_rows}
    result += KernelTemplate._template_from_string(self.TEMPLATE_KERNEL).render(
        amx_kernel_options
    )

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/common.py
# Occurrences: Lines 2288-2296 (3 instances)

for i in range(start, end):
    if i == self.lineno - 1:
        error_info += f"{i + 1}: --> {lines[i]}\n"
        if hasattr(self.original_error, "column"):
            error_info += (
                "     "
                + " " * (self.original_error.column - 1)
                + "^\n"
            )
    else:
        error_info += f"{i + 1}:     {lines[i]}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/cpp_builder.py
# Occurrences: Lines 1572-1580 (4 instances)

for cflag in BuildOption.get_cflags():
    if _IS_WINDOWS:
        self._cflags_args += f"/{cflag} "
    else:
        self._cflags_args += f"-{cflag} "


# ==================================================
# Occurrences: Lines 1593-1616 (9 instances)

for inc_dir in BuildOption.get_include_dirs():
    if _IS_WINDOWS:
        self._include_dirs_args += f'/I "{inc_dir}" '
    else:
        self._include_dirs_args += f"-I{shlex.quote(inc_dir)} "


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/wrapper_benchmark.py
# Line: 290

for category in category_list:
    percent = (
        f"{per_category_wall_time.get(category, 0.0) / wall_time_ms * 100:.2f}%"
    )
    tabulate_line += f", {percent}"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/hipify/hipify_python.py
# Occurrences: Lines 390-392 (2 instances)

for c in string:
    if in_comment == '':
        # Outside comments
        if c == '/' and prev_c == '/':
            in_comment = '//'
        elif c == '*' and prev_c == '/':
            in_comment = '/*'
        elif c == '"' and prev_c != '\\' and prev_c != "'":
            in_comment = '"'
    elif in_comment == '//':
        # In // xxx
        if c == '\r' or c == '\n':
            in_comment = ''
    elif in_comment == '/*':
        # In /* xxx */
        if c == '/' and prev_c == '*':
            in_comment = ''
    elif in_comment == '"':
        # In ""
        if c == '"' and prev_c != '\\':
            in_comment = ''
    prev_c = c
    if in_comment == '':
        new_string += c
    else:
        new_string += 'x'

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/bundled_inputs.py
# Line: 337

for arg_idx, arg in enumerate(args):
    inflate_helper_fn_name = _get_inflate_helper_fn_name(arg_idx, inp_idx, function_name)
    deflated, inflater, helper_definition = _inflate_expr(
        arg,
        f"deflated[{inp_idx}][{arg_idx}]",
        inflate_helper_fn_name,
        skip_size_check=skip_size_check,
    )
    deflated_args.append(deflated)
    parts.append(f"    {inflater},")
    if helper_definition:
        model.define(textwrap.dedent(helper_definition))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/flop_counter.py
# Line: 722

for value in values:
    value[0] = " " + value[0]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/gen_pyi.py
# Occurrences: Lines 41-42 (2 instances)

for i, line in enumerate(lines):
    if i != 0:
        output += new_line_with_indent
    output += line.replace("\n", new_line_with_indent)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/cpp_extension.py
# Line: 1766

for element in s:
    string += (element + ' ')

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/checkpoint.py
# Line: 897

for idx, x_meta, recomputed_meta in nb_meta_different:
    mismatched_tensors += (
        f"tensor at position {idx}:\n"
        f"saved metadata: {x_meta}\n"
        f"recomputed metadata: {recomputed_meta}\n"
    )

# ==================================================
# Line: 1003

for i, (log, tb) in enumerate(zip(capture_logs.logs, capture_logs.tbs)):
    out += f"{log}   ({i + 1} of {total_len} in {label})\n\n"
    found_torch_dispatch = False
    for line in tb:
        # Start printing stack trace only after __torch_dispatch__ is found
        is_torch_dispatch = line['name'] == '__torch_dispatch__'
        if not found_torch_dispatch and not is_torch_dispatch:
            continue
        elif is_torch_dispatch:
            found_torch_dispatch = True
            continue
        out += f"{line['filename']}:{line['line']}:{line['name']}\n"
    out += "\n\n"

# ==================================================
# Occurrences: Lines 1013-1014 (2 instances)

for line in tb:
    # Start printing stack trace only after __torch_dispatch__ is found
    is_torch_dispatch = line['name'] == '__torch_dispatch__'
    if not found_torch_dispatch and not is_torch_dispatch:
        continue
    elif is_torch_dispatch:
        found_torch_dispatch = True
        continue
    out += f"{line['filename']}:{line['line']}:{line['name']}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_ops.py
# Line: 1251

for key, msg in exceptions.items():
    err_msg += f"Overload name {key}:\n {msg}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/graph_module.py
# Occurrences: Lines 632-642 (3 instances)

for module_name, module in self.named_children():
    module_str = _gen_model_repr(module_name, module)
    if module_str is None:
        module_file = folder / f"{module_name}.pt"
        torch.save(module, module_file)
        blobified_modules.append(module_name)
        module_repr = module.__repr__().replace("\r", " ").replace("\n", " ")
        # weights_only=False as this is legacy code that saves the model
        module_str = (
            f"torch.load(r'{module_file}', weights_only=False) # {module_repr}"
        )
    model_str += f"{tab * 2}self.{module_name} = {module_str}\n"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/traceback.py
# Line: 111

for item in self.from_node:
    result += item.print_readable(indent + 1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/unification/multipledispatch/dispatcher.py
# Line: 445

for pair in amb:
    text += "\t" + ", ".join("[" + str_signature(s) + "]" for s in pair) + "\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/symbolic_shapes.py
# Line: 3461

for s, val in forced_specializations.items():
    buf += f"  - solving the guards generated for {s} resulted in a specialized value of {val}.\n"


# ==================================================
# Line: 7932

for i, fix in enumerate(suggested_fixes):
    msg += f"\n  {i + 1}. {fix}"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/splitter_base.py
# Occurrences: Lines 522-527 (2 instances)

for arg_dtypes_tuple, kwarg_dtypes_tuple in dtypes:
    reports += f"{t}: ({arg_dtypes_tuple}, {dict(kwarg_dtypes_tuple)})\n"


# ==================================================
# Occurrences: Lines 549-554 (2 instances)

for i, subgraph in enumerate(subgraphs):
    reports += (
        f"_run_on_acc_{i}: "
        if subgraph.is_acc
        else f"{self.non_acc_submodule_name}{i}: "
    )
    reports += f"{len(subgraph.nodes)} node(s)\n"


# ==================================================
# Line: 598

for n in submod.graph.nodes:
    if n.op == "placeholder":
        if not is_node_output_tensor(n):
            reports += f"Input {n.name} is not a tensor, this might cause problems during lowering!\n"
        else:
            total_input_bytes += get_size_of_node(submod, n)[0]
    if n.op == "output":
        output_node = n


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/net_min_base.py
# Line: 84

for k, v in vars(self).items():
    settings_str += f"\t{k}: {v}\n"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/graph_drawer.py
# Occurrences: Lines 321-331 (3 instances)

for item in tm:
    result += self._tensor_meta_to_label(item)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/_draft_export.py
# Line: 45

for frame in stack:
    if frame["filename"] not in str_to_filename:
        continue

    res += f"""
    File {str_to_filename[frame['filename']]}, lineno {frame['line']}, in {frame['name']}"""  # type: ignore[index]


# ==================================================
# Line: 199

for i, failure in enumerate(self.failures):
    error += f"{i + 1}. {failure.print(self.str_to_filename)}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/backends/debugging.py
# Occurrences: Lines 367-384 (8 instances)

for idx, break_reason in enumerate(self.break_reasons):
    output += f"  Break Reason {idx + 1}:\n"
    output += f"    Reason: {break_reason.reason}\n"
    output += "    User Stack:\n"
    for frame_summary in break_reason.user_stack:
        output += f"      {frame_summary}\n"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/backends/distributed.py
# Line: 526

for name, module in split_gm.named_modules():
    if "." not in name and len(name):
        # only print the submod graphs, not their children
        debug_str += f"\n---{name} graph---\n{module.graph}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/utils.py
# Line: 4123

for lineno in range(inst.positions.lineno + 1, inst.positions.end_lineno):
    line = linecache.getline(code.co_filename, lineno).rstrip()
    segment += line + "\n"
    # don't underline leading spaces
    num_spaces = len(line) - len(line.lstrip())
    markers.append(" " * num_spaces + "~" * (len(line) - num_spaces))

# ==================================================
# Occurrences: Lines 4172-4176 (2 instances)

for i in range(len(markers)):
    result += (
        linecache.getline(code.co_filename, inst.positions.lineno + i).rstrip()
        + "\n"
    )
    result += markers[i] + "\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/debug_utils.py
# Line: 207

for module_name, module in gm.named_children():
    module_str = f"{module.__repr__()}"
    # module should be a core torch.nn.Module, so all parameters
    # should be on the same device.
    example_param = next(module.parameters(), None)
    if example_param is not None and example_param.is_cuda:
        module_str = f"{module_str}.cuda()"
    model_str += f"{tab * 2}self.{module_name} = {module_str}\n"


# ==================================================
# Line: 226

for buffer_name, buffer in gm._buffers.items():
    if buffer is None:
        continue
    # Serialize full data for small buffers
    if buffer.numel() <= MAX_CONSTANT_NUMEL_INLINE:
        from torch._tensor_str import PRINT_OPTS

        assert PRINT_OPTS.threshold >= MAX_CONSTANT_NUMEL_INLINE
        tensor_str = repr(buffer)
    elif torch.is_floating_point(buffer):
        tensor_str = f"torch.randn({list(buffer.shape)}, dtype={buffer.dtype})"
    else:
        tensor_str = (
            f"torch.randint(1, size={list(buffer.shape)}, dtype={buffer.dtype})"
        )
    if buffer.is_cuda:
        tensor_str = f"{tensor_str}.cuda()"
    model_str += (
        f"{tab * 2}self.register_buffer('{buffer_name}', {tensor_str})\n"
    )


# ==================================================
# Line: 237

for param_name, param in gm._parameters.items():
    if param is None:
        continue
    maybe_device = ""
    if param.is_cuda:
        maybe_device = ', device="cuda"'
    tensor_str = f"torch.nn.Parameter(torch.randn({list(param.shape)}, dtype={param.dtype}{maybe_device}))"
    model_str += f"{tab * 2}self.{param_name} = {tensor_str}\n"


# ==================================================
# Line: 270

for name, count in gpu_names.items():
    model_str += f"# {name} : {count} \n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/output_graph.py
# Line: 1513

for node in self.graph.nodes:
    example_value = node.meta.get("example_value", None)
    if isinstance(example_value, torch._subclasses.FakeTensor):
        size = example_value.size()
        graph_sizes_str += f"{node.name}: {tuple(size)}\n"
        concrete_size = []
        has_symint = False
        for sz in size:
            if isinstance(sz, int):
                concrete_size.append(sz)
            elif isinstance(sz, torch.SymInt):
                has_symint = True
                concrete_size.append(sz.node.hint)
            else:
                break
        else:
            if has_symint:
                graph_sizes_str += (
                    f"{node.name} (concrete): {tuple(concrete_size)}\n"
                )

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/polyfills/pytree.py
# Line: 63

for __name in (
    "is_namedtuple",
    "is_namedtuple_class",
    "is_namedtuple_instance",
    "is_structseq",
    "is_structseq_class",
    "is_structseq_instance",
    "namedtuple_fields",
    "structseq_fields",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/collective_utils.py
# Line: 158

for i, sp in enumerate(cast(list[SyncPayload[T]], total_list)):
    if sp.stage_name != stage_name:
        error_msg += (
            f"Unexpected stage name received from rank {i}: {sp.stage_name} "
        )
        continue
    if not sp.success and sp.exception is not None:
        exception_list.append((i, sp.exception))
        continue
    ret_list.append(sp.payload)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_optim_utils.py
# Line: 1171

for rank, keys in enumerate(obj_list):
    keys = cast(list[_OptimStateKey], keys)
    if len(keys) > 0:
        error_msg += (
            f"\nRank {rank} is missing states for the parameters: "
            f"{[key.unflat_param_names for key in keys]}"
        )

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/api.py
# Occurrences: Lines 38-41 (3 instances)

for rank, exc_pair in self._failures.items():
    exc, trace = exc_pair
    str += f"Traceback (most recent call last): (RANK {rank})\n"
    if trace is not None:
        str += "".join(tb.format_list(trace))
    str += "".join(tb.format_exception_only(type(exc), value=exc))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/optimizer.py
# Occurrences: Lines 424-428 (3 instances)

for i, group in enumerate(self.param_groups):
    format_string += "\n"
    format_string += f"Parameter Group {i}\n"
    for key in sorted(group.keys()):
        if key != "params":
            format_string += f"    {key}: {group[key]}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/flex_attention.py
# Occurrences: Lines 606-607 (2 instances)

for idx in batch_idx:
    cur_mask = cur_mask[idx]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/parallel/distributed.py
# Line: 221

for var in relevant_env_vars:
    value = os.environ[var] if var in os.environ else "N/A"
    formatted_output += f"env:{var}={value}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/activation_sparsifier/activation_sparsifier.py
# Occurrences: Lines 463-469 (4 instances)

for name, config in self.data_groups.items():
    format_string += "\n"
    format_string += "\tData Group\n"
    format_string += f"\t    name: {name}\n"
    for key in sorted(config.keys()):
        if key in ["data", "hook", "reduce_fn", "mask_fn", "aggregate_fn"]:
            continue
        format_string += f"\t    {key}: {config[key]}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/data_sparsifier/base_data_sparsifier.py
# Occurrences: Lines 272-278 (4 instances)

for name, sparse_args in self.data_groups.items():
    format_string += "\n"
    format_string += "\tData Group\n"
    format_string += f"\t    name: {name}\n"
    for key in sorted(sparse_args.keys()):
        if key == "data":
            continue
        format_string += f"\t    {key}: {sparse_args[key]}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/sparsifier/base_sparsifier.py
# Occurrences: Lines 77-83 (4 instances)

for i, sparse_args in enumerate(self.groups):
    module = sparse_args["module"]
    format_string += "\n"
    format_string += f"\tGroup {i}\n"
    format_string += f"\t    module: {module}\n"
    for key in sorted(sparse_args.keys()):
        if key == "module":
            continue
        format_string += f"\t    {key}: {sparse_args[key]}\n"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_model_report/detector.py
# Line: 429

for fqn in per_channel_info:
    fqn_dict = per_channel_info[fqn]
    if (
        fqn_dict[self.PER_CHAN_SUPPORTED_KEY]
        and not fqn_dict[self.PER_CHAN_USED_KEY]
    ):
        optimizations_possible = True
        further_optims_str += (
            f"Module {fqn} can be configured to use per_channel quantization.\n"
        )


# ==================================================
# Line: 801

for module_fqn in module_dynamic_static_info.keys():
    # there is at least 1 module for suggestion
    modules_added = True
    module_info = module_dynamic_static_info[module_fqn]
    suggestion_string_template = (
        "For module {} it is suggested to use {} quantization because {}.\n"
    )

    # decide what string formatting values will be
    quantization_type = ""
    quantization_reasoning = "the distribution of data before {} is {} and the distribution after is {}."

    benefit_str = ""

    # strings for if dynamic quantized per tensor is needed
    recommend_per_tensor = (
        ". We recommend to add a {} before this module if it is static."
    )
    rec_lay_to_add = "dynamic quantize per tensor layer"
    dynamic_per_tensor_string = recommend_per_tensor.format(rec_lay_to_add)
    dynamic_per_tensor_reasoning_string = " This is because the input to this module has a non-stationary distribution"

    # start composing explanation
    if module_info[self.DEFAULT_DYNAMIC_REC_KEY]:
        quantization_type = "dynamic"
        # check if currently supported or future supported
        benefit_str = dynamic_benefit
        if not module_info[self.IS_CURRENTLY_SUPPORTED_KEY]:
            benefit_str += future_support_str
    else:
        quantization_type = "static"
        benefit_str = static_benefit

    # now set the quantization explanation string
    quantization_reasoning = (
        quantization_reasoning.format(
            module_fqn,
            module_info[self.PRE_OBS_DATA_DIST_KEY],
            module_info[self.POST_OBS_DATA_DIST_KEY],
        )
        + benefit_str
    )

    # if we have a non-stationary input -> linear -> stationary we suggested static
    # however, we want to also recommend they add a dynamic quantize per tensor right if this change is made
    if (
        module_info[self.PRE_OBS_DATA_DIST_KEY] == self.NON_STATIONARY_STR
        and module_info[self.POST_OBS_DATA_DIST_KEY] == self.STATIONARY_STR
    ):
        quantization_reasoning = (
            quantization_reasoning
            + dynamic_per_tensor_string
            + dynamic_per_tensor_reasoning_string
        )

    # format the overall suggestion string with the specific inputs
    module_suggestion_string = suggestion_string_template.format(
        module_fqn, quantization_type, quantization_reasoning
    )

    # append to overall suggestion
    dynamic_vs_static_string += module_suggestion_string


# ==================================================
# Line: 1298

for module_fqn in input_weight_equalization_info:
    # we added at least 1 module
    added_module = True
    # add the module level description
    input_weight_string += module_suggestion_str.format(
        module_fqn, self.ch_axis
    )

    mod_info: dict[str, Any] = input_weight_equalization_info[module_fqn]

    # gather info on how many channels would benefit from input weight and
    recommendation_per_channel: torch.Tensor = mod_info[self.RECOMMENDED_KEY]
    num_recs = sum(recommendation_per_channel)

    if (
        num_recs / len(recommendation_per_channel)
        >= self.DEFAULT_RECOMMEND_INPUT_WEIGHT_CHANNEL_RATIO
    ):
        input_benefit_formatted = input_weight_benefit_str.format(
            num_recs, len(recommendation_per_channel)
        )
        channel_str = channel_suggestion_str.format(
            use_str, input_benefit_formatted
        )
        input_weight_string += channel_str
    else:
        non_benefit_reason_formatted = (
            input_weight_non_benefit_reasoning.format(
                num_recs, len(recommendation_per_channel)
            )
        )
        non_benefit_str = input_weight_non_benefit_str.format(
            non_benefit_reason_formatted
        )
        channel_str = channel_suggestion_str.format(no_use_str, non_benefit_str)
        input_weight_string += channel_str


# ==================================================
# Line: 1318

for module_fqn in input_weight_equalization_info:
    # we added at least 1 module
    added_module = True
    # add the module level description
    input_weight_string += module_suggestion_str.format(
        module_fqn, self.ch_axis
    )

    mod_info: dict[str, Any] = input_weight_equalization_info[module_fqn]

    # gather info on how many channels would benefit from input weight and
    recommendation_per_channel: torch.Tensor = mod_info[self.RECOMMENDED_KEY]
    num_recs = sum(recommendation_per_channel)

    if (
        num_recs / len(recommendation_per_channel)
        >= self.DEFAULT_RECOMMEND_INPUT_WEIGHT_CHANNEL_RATIO
    ):
        input_benefit_formatted = input_weight_benefit_str.format(
            num_recs, len(recommendation_per_channel)
        )
        channel_str = channel_suggestion_str.format(
            use_str, input_benefit_formatted
        )
        input_weight_string += channel_str
    else:
        non_benefit_reason_formatted = (
            input_weight_non_benefit_reasoning.format(
                num_recs, len(recommendation_per_channel)
            )
        )
        non_benefit_str = input_weight_non_benefit_str.format(
            non_benefit_reason_formatted
        )
        channel_str = channel_suggestion_str.format(no_use_str, non_benefit_str)
        input_weight_string += channel_str


# ==================================================
# Line: 1329

for module_fqn in input_weight_equalization_info:
    # we added at least 1 module
    added_module = True
    # add the module level description
    input_weight_string += module_suggestion_str.format(
        module_fqn, self.ch_axis
    )

    mod_info: dict[str, Any] = input_weight_equalization_info[module_fqn]

    # gather info on how many channels would benefit from input weight and
    recommendation_per_channel: torch.Tensor = mod_info[self.RECOMMENDED_KEY]
    num_recs = sum(recommendation_per_channel)

    if (
        num_recs / len(recommendation_per_channel)
        >= self.DEFAULT_RECOMMEND_INPUT_WEIGHT_CHANNEL_RATIO
    ):
        input_benefit_formatted = input_weight_benefit_str.format(
            num_recs, len(recommendation_per_channel)
        )
        channel_str = channel_suggestion_str.format(
            use_str, input_benefit_formatted
        )
        input_weight_string += channel_str
    else:
        non_benefit_reason_formatted = (
            input_weight_non_benefit_reasoning.format(
                num_recs, len(recommendation_per_channel)
            )
        )
        non_benefit_str = input_weight_non_benefit_str.format(
            non_benefit_reason_formatted
        )
        channel_str = channel_suggestion_str.format(no_use_str, non_benefit_str)
        input_weight_string += channel_str


# ==================================================
# Line: 1689

    for index, outlier_detected in enumerate(mod_info[self.OUTLIER_KEY]):
        if outlier_detected:
            # we found at least 1 outlier
            if not added_model_desc:
                # add the module level description
                outlier_string += module_suggestion_str.format(
                    module_fqn, self.ch_axis
                )
                added_model_desc = True

            # we mark that we found at least one outlier
            added_module = True
            max_value_found_str = channel_max_value_str.format(
                mod_info[self.MAX_VALS_KEY][index]
            )
            channel_str = channel_suggestion_str.format(
                index, max_value_found_str
            )
            outlier_string += channel_str

        # also check if we found constant batch
        if mod_info[self.CONSTANT_COUNTS_KEY][index] != 0:
            # make sure we add a module level highlight.
            if not added_model_desc:
                # add the module level description
                outlier_string += module_suggestion_str.format(
                    module_fqn, self.ch_axis
                )
                added_model_desc = True

            constant_values_for_channel = mod_info[self.CONSTANT_COUNTS_KEY][
                index
            ]
            formatted_str = constant_str.format(
                index, constant_values_for_channel, constant_suggestion
            )
            outlier_string += formatted_str
            # we also added at least one thing to description
            added_module = True

# if found outlier, give suggestion, else give default response

# ==================================================
# Line: 1702

    for index, outlier_detected in enumerate(mod_info[self.OUTLIER_KEY]):
        if outlier_detected:
            # we found at least 1 outlier
            if not added_model_desc:
                # add the module level description
                outlier_string += module_suggestion_str.format(
                    module_fqn, self.ch_axis
                )
                added_model_desc = True

            # we mark that we found at least one outlier
            added_module = True
            max_value_found_str = channel_max_value_str.format(
                mod_info[self.MAX_VALS_KEY][index]
            )
            channel_str = channel_suggestion_str.format(
                index, max_value_found_str
            )
            outlier_string += channel_str

        # also check if we found constant batch
        if mod_info[self.CONSTANT_COUNTS_KEY][index] != 0:
            # make sure we add a module level highlight.
            if not added_model_desc:
                # add the module level description
                outlier_string += module_suggestion_str.format(
                    module_fqn, self.ch_axis
                )
                added_model_desc = True

            constant_values_for_channel = mod_info[self.CONSTANT_COUNTS_KEY][
                index
            ]
            formatted_str = constant_str.format(
                index, constant_values_for_channel, constant_suggestion
            )
            outlier_string += formatted_str
            # we also added at least one thing to description
            added_module = True

# if found outlier, give suggestion, else give default response

# ==================================================
# Line: 1709

    for index, outlier_detected in enumerate(mod_info[self.OUTLIER_KEY]):
        if outlier_detected:
            # we found at least 1 outlier
            if not added_model_desc:
                # add the module level description
                outlier_string += module_suggestion_str.format(
                    module_fqn, self.ch_axis
                )
                added_model_desc = True

            # we mark that we found at least one outlier
            added_module = True
            max_value_found_str = channel_max_value_str.format(
                mod_info[self.MAX_VALS_KEY][index]
            )
            channel_str = channel_suggestion_str.format(
                index, max_value_found_str
            )
            outlier_string += channel_str

        # also check if we found constant batch
        if mod_info[self.CONSTANT_COUNTS_KEY][index] != 0:
            # make sure we add a module level highlight.
            if not added_model_desc:
                # add the module level description
                outlier_string += module_suggestion_str.format(
                    module_fqn, self.ch_axis
                )
                added_model_desc = True

            constant_values_for_channel = mod_info[self.CONSTANT_COUNTS_KEY][
                index
            ]
            formatted_str = constant_str.format(
                index, constant_values_for_channel, constant_suggestion
            )
            outlier_string += formatted_str
            # we also added at least one thing to description
            added_module = True

# if found outlier, give suggestion, else give default response

# ==================================================
# Line: 1720

    for index, outlier_detected in enumerate(mod_info[self.OUTLIER_KEY]):
        if outlier_detected:
            # we found at least 1 outlier
            if not added_model_desc:
                # add the module level description
                outlier_string += module_suggestion_str.format(
                    module_fqn, self.ch_axis
                )
                added_model_desc = True

            # we mark that we found at least one outlier
            added_module = True
            max_value_found_str = channel_max_value_str.format(
                mod_info[self.MAX_VALS_KEY][index]
            )
            channel_str = channel_suggestion_str.format(
                index, max_value_found_str
            )
            outlier_string += channel_str

        # also check if we found constant batch
        if mod_info[self.CONSTANT_COUNTS_KEY][index] != 0:
            # make sure we add a module level highlight.
            if not added_model_desc:
                # add the module level description
                outlier_string += module_suggestion_str.format(
                    module_fqn, self.ch_axis
                )
                added_model_desc = True

            constant_values_for_channel = mod_info[self.CONSTANT_COUNTS_KEY][
                index
            ]
            formatted_str = constant_str.format(
                index, constant_values_for_channel, constant_suggestion
            )
            outlier_string += formatted_str
            # we also added at least one thing to description
            added_module = True

# if found outlier, give suggestion, else give default response

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/qconfig_mapping.py
# Occurrences: Lines 310-316 (3 instances)

for style_name in _QCONFIG_STYLE_ORDER:
    output += f"\n {style_name}"
    qconfigs = getattr(self, style_name)
    if isinstance(qconfigs, OrderedDict) and len(qconfigs) > 0:
        for key, qconfig in qconfigs.items():
            output += f"\n  {key}: {qconfig}"
    else:
        output += f"\n  {qconfigs}"

# ==================================================
