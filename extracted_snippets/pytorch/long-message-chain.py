# long-message-chain snippets for pytorch

# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train_decision.py
# Line: 417

df.groupby(feature_columns + ["choice"], as_index=False)
.apply(calculate_stats, include_groups=False)
.reset_index()

# ==================================================
# Line: 463

valid_inputs.groupby(feature_columns, as_index=False)
.filter(lambda x: len(x) >= 2)
.groupby(feature_columns, as_index=False)
.apply(get_winner_and_speedup, include_groups=False)
.reset_index()

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train_regression.py
# Line: 116

df.groupby(feature_columns + [CHOICE_COL])
.apply(calculate_stats)
.reset_index()

# ==================================================
# Line: 150

valid_inputs.groupby(feature_columns)
.apply(get_winner_and_speedups)
.reset_index(drop=True)

# ==================================================
# Line: 342

results = df.groupby(feature_columns).apply(predict_winner).reset_index()

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/api/unboxing.py
# Line: 109

CppSignatureGroup.from_native_function(f, method=False)
.most_faithful_signature()
.arguments()

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/api/python.py
# Line: 251

argument_type_str(self.type, symint=symint)
.replace("const ", "")
.replace(" &", "")

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_functionalization_type.py
# Line: 378

return_type = dispatcher_sig.returns_type().remove_const_ref().cpp_type()

# ==================================================
# Line: 520

return_type = dispatcher.returns_type(f.func.returns).remove_const_ref().cpp_type()

# ==================================================
# Line: 676

dispatcher.returns_type(g.functional.func.returns).remove_const_ref().cpp_type()

# ==================================================
# File: /root/ecooptimizer/pytorch/setup.py
# Line: 558

subprocess.check_output(["otool", "-l", libtorch_cpu_path])
.decode("utf-8")
.split("\n")

# ==================================================
# Line: 1032

subprocess.check_output(
    ["xcrun", "--show-sdk-path", "--sdk", "macosx"]
)
.decode("utf-8")
.strip()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/supported_ops.py
# Line: 333

link_target = header.replace("`", "").replace("-", "").lower().replace(" ", "-")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_trace.py
# Line: 161

a.detach()
.clone(memory_format=None if a.is_mkldnn else torch.preserve_format)
.requires_grad_(a.requires_grad)

# ==================================================
# Line: 291

if x.sub(y).abs().max() > 1e-6:

# ==================================================
# Line: 1090

return TS2EPConverter(func, export_args).convert().module()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/scan.py
# Line: 56

y.unsqueeze(0)
.repeat(*([scan_length] + [1] * y.ndim))
.clone(memory_format=torch.contiguous_format)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/xeon/run_cpu.py
# Line: 178

self.cpuinfo.append(regex_out.group(1).strip().split(","))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/_nnapi/serializer.py
# Line: 1021

out_shape = torch.zeros(1).expand(in_oper.shape).reshape(shape).shape

# ==================================================
# Occurrences: Lines 1363-1364 (2 instances)

assert node.inputsAt(0).type().kind() == "TensorType"

# ==================================================
# Occurrences: Lines 1491-1492 (2 instances)

assert node.inputsAt(0).type().kind() == "TensorType"

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/sparse/_semi_structured_conversions.py
# Line: 270

dense_offsets = meta_2.view(-1) + (
    torch.arange(0, 2 * m * k // ksparse, device=device) * 4
).view(-1, 1).repeat(1, 2).view(-1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/sparse/_triton_ops.py
# Occurrences: Lines 1085-1108 (2 instances)

as1Dbatch(other)
.transpose(-2, -1)
.view(
    nbatches,
    Ns // blocksize[0],
    blocksize[0],
    Ks // blocksize[1],
    blocksize[1],
)
.movedim(
    (3, 1, 4, 2), (1, 2, 3, 4)
)  # equivalent to .transpose(-3, -2).transpose(-2, -1).transpose(-4, -3)
.flatten(0, 2)

# ==================================================
# Line: 1890

crow_indices = input.crow_indices().unsqueeze(0).flatten(0, -2)

# ==================================================
# Line: 1896

if input.values().transpose(-3, -2).is_contiguous():

# ==================================================
# Line: 1902

values.transpose(-3, -2)
.contiguous()
.unsqueeze(0)
.flatten(0, -4)
.reshape(-1, row_block, nnz * col_block)

# ==================================================
# Line: 1930

values.reshape(-1, row_block, nnz, col_block)
.transpose(-3, -2)
.reshape(*input.values().shape)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/_functions/tensor.py
# Line: 57

result = tensor.new(tensor).contiguous().view(*sizes)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler_util.py
# Line: 285

metric.replace("cuda", "device")
.replace("xpu", "device")
.replace("privateuse1", "device"),

# ==================================================
# Line: 865

sort_by.replace("cuda", "device")
.replace("xpu", "device")
.replace("privateuse1", "device"),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/gradcheck.py
# Line: 106

indices = tmp.nonzero().t().to(dtype=indices_dtype)

# ==================================================
# Occurrences: Lines 114-126 (2 instances)

x_coalesced.indices()
.mul(
    torch.tensor(stride, dtype=indices_dtype, device=device).unsqueeze(
        1
    )
)
.sum(0)

# ==================================================
# Line: 204

torch._convert_indices_from_csr_to_coo(
    x_tensor.crow_indices(), x_tensor.col_indices()
)
.repeat_interleave(x_blocksize[0] * x_blocksize[1], 1)
.mul_(torch.tensor(x_blocksize, device=x_tensor.device).reshape(2, 1))
.add_(
    torch.stack(
        torch.where(torch.ones(x_blocksize, device=x_tensor.device))
    ).repeat(1, x_nnz)
)
.t()

# ==================================================
# Line: 222

torch._convert_indices_from_csr_to_coo(
    x_tensor.ccol_indices(), x_tensor.row_indices(), transpose=True
)
.repeat_interleave(x_blocksize[0] * x_blocksize[1], 1)
.mul_(torch.tensor(x_blocksize, device=x_tensor.device).reshape(2, 1))
.add_(
    torch.stack(
        torch.where(torch.ones(x_blocksize, device=x_tensor.device))
    ).repeat(1, x_nnz)
)
.t()

# ==================================================
# Line: 1203

sparse_kind = str(gi.layout).replace("torch.", "").replace("_coo", "")

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
# File: /root/ecooptimizer/pytorch/torch/_inductor/codecache.py
# Line: 324

if choice_hash in cache.get(op, {}).get(inputs, {}).get(precision, {}):

# ==================================================
# Line: 752

return parutil.get_file_contents("torch/src_hash.txt").rstrip().encode("ascii")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/ir.py
# Line: 4271

indexer = self.get_layout().as_fixed().make_indexer()

# ==================================================
# Line: 5567

(order and x.get_layout().real_layout().is_stride_ordered(order))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/debug_utils.py
# Occurrences: Lines 35-39 (5 instances)

print("Dtype: ", arg.float().mean().item())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_wrapper_cpu.py
# Line: 842

x.replace("\\", "\\\\")
.replace('"', '\\"')
.replace("\n", "\\n")
.replace("\t", "\\t")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/rocm/ck_universal_gemm_template.py
# Line: 597

operation_name = op.name().replace("(", "").replace(",", "").replace(")", "")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/halide.py
# Line: 1377

return V.graph.get_buffer(name).get_layout().storage_size()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_template_kernel.py
# Line: 140

indexer = node.get_layout().as_fixed().make_indexer()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_gemm_template.py
# Line: 1221

torch.nn.functional.pad(W, (0, padding))  # type: ignore[assignment]
.reshape(*blocked_size)
.transpose(-3, -2)
.contiguous()

# ==================================================
# Line: 1279

W = W.view(vnni_view_size).transpose(-1, -2).contiguous().view(new_size)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/aoti_eager.py
# Line: 267

Path(kernel_lib_path).relative_to(persistent_cache).as_posix()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/scheduler.py
# Line: 603

+ stack_trace_last_line.replace("{", "{{")
.replace("}", "}}")
.replace("\n", "\\")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/exc.py
# Line: 96

textwrap.dedent(
    """
        C++ compile error

        Command:
        {cmd}

        Output:
        {output}
    """
)
.strip()
.format(cmd=" ".join(cmd), output=output)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/cpp_builder.py
# Line: 240

subprocess.check_output([cpp_compiler, "/help"], stderr=subprocess.STDOUT)
.strip()
.decode(*SUBPROCESS_DECODE_ARGS)

# ==================================================
# Line: 265

subprocess.check_output(
    [cpp_compiler, "--version"], stderr=subprocess.DEVNULL
)
.strip()
.decode(*SUBPROCESS_DECODE_ARGS)

# ==================================================
# Line: 909

subprocess.check_output(["brew", "--prefix", "libomp"])
.decode("utf8")
.strip()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/fuse_attention.py
# Line: 27

torch.matmul(query, key.transpose(-2, -1))
.div(inv_scale)
.softmax(dim=-1)
.matmul(value)

# ==================================================
# Line: 49

torch.matmul(query, key.transpose(-2, -1))
.mul(scale_factor)
.softmax(dim=-1)
.matmul(value)

# ==================================================
# Line: 71

torch.matmul(query, key.transpose(-2, -1))
.div(inv_scale_factor)
.softmax(dim=-1),

# ==================================================
# Line: 93

torch.matmul(query, key.transpose(-2, -1)).mul(scale_factor).softmax(dim=-1),

# ==================================================
# Line: 274

return torch.matmul(q, k.transpose(-2, -1)).div(inv_scale).softmax(dim=-1).matmul(v)

# ==================================================
# Line: 295

torch.matmul(q, k.transpose(-2, -1)).div(inv_scale_factor).softmax(dim=-1),

# ==================================================
# Line: 399

torch.nn.functional.dropout(
    (torch.matmul(q, k.transpose(-2, -1)).div(inv_scale) + attn_mask).softmax(
        dim=-1
    ),
    dropout_p,
)
.to(dtype=query.dtype)
.matmul(v)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/decomposition.py
# Line: 437

return inp.unsqueeze(dim).expand(*shape).flatten(dim, dim + 1).clone()

# ==================================================
# Line: 994

index.to(torch.int64)
.repeat_interleave(repeats)
.reshape(index_shape)
.permute(perm)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/hipify/hipify_python.py
# Line: 416

hip_kernel = "hipLaunchKernelGGL(" + cuda_kernel_dim3[0:-1].replace(
    ">>>", ", 0" * (4 - num_klp) + ">>>").replace("<<<", ", ").replace(
    ">>>", ", ").replace(kernel_name_with_template, "(" + kernel_name_with_template + ")")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_triton.py
# Line: 124

return hashlib.sha256(key.encode("utf-8")).hexdigest().upper()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_content_store.py
# Line: 78

torch.randint(-(2**31), 2**31, x.shape, device=x.device, dtype=torch.int32)
.abs()
.long()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/tensorboard/summary.py
# Line: 81

return torch.view_as_real(t).flatten().tolist()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/tensorboard/_pytorch_graph.py
# Line: 270

if node.output().type().kind() != CLASSTYPE_KIND:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/tensorboard/_convert_np.py
# Line: 32

x = x.detach().cpu().numpy()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/dataloader.py
# Line: 701

torch.empty((), dtype=torch.int64)
.random_(generator=loader.generator)
.item()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/sampler.py
# Line: 170

seed = int(torch.empty((), dtype=torch.int64).random_().item())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/graph_settings.py
# Line: 170

torch.empty((), dtype=torch.int64).random_(generator=rng).item()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/iter/combinatorics.py
# Line: 156

self._seed = int(torch.empty((), dtype=torch.int64).random_().item())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/map/combinatorics.py
# Line: 92

self._seed = int(torch.empty((), dtype=torch.int64).random_().item())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/compare.py
# Line: 48

int(_tensor(r.median / self._time_scale).log10().ceil()) if r else None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/timer.py
# Line: 320

overhead = torch.tensor([self._timeit(0) for _ in range(5)]).median().item()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/sparse_fuzzer.py
# Line: 81

i.mul_(torch.tensor(size[:sparse_dim]).unsqueeze(1).to(i))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/cpp_jit.py
# Line: 69

CXX_FLAGS = torch.__config__._cxx_flags().strip().split()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py
# Line: 797

return textwrap.dedent(r"""
    import gc
    import os
    import pickle
    import subprocess
    import sys
    import time

    # Mitigate https://github.com/pytorch/pytorch/issues/37377
    # which can sometimes cause the subprocess call to fail.
    import numpy as np

    import torch
    torch.set_num_threads({num_threads})

    {bindings_import}

    PID = os.getpid()

    def log_failure(msg):
        with open({error_log_repr}, "wt") as f:
            f.write(msg)
        sys.exit(1)

    def check_result(completed_process):
        if completed_process.returncode:
            log_failure(f"Command failed: {{' '.join(completed_process.args)}}")
        return completed_process

    # =============================================================================
    # == Check that subprocess matches parent =====================================
    # =============================================================================
    if os.path.realpath(sys.executable) != "{parent_interpreter}":
        log_failure(
            "Interpreter mismatch:\n"
            f"  {{os.path.realpath(sys.executable)}}\n    vs.\n  {parent_interpreter}"
        )

    if torch.__file__ != "{torch_file}":
        log_failure(
            "PyTorch does not match expected file:\n"
            f"  {{torch.__file__}}\n    vs.\n  {torch_file}"
        )

    # =============================================================================
    # == User specified setup =====================================================
    # =============================================================================
    # Load serialized globals
    {load_globals}

    # User setup str
    {setup}

    for _ in range({warmup_number}):
    {indented_stmt}

    # =============================================================================
    # == Callgrind management =====================================================
    # =============================================================================
    with open("{stat_log}", "wb") as stat_file:
        # If many instances of callgrind are running at once, the output of
        # `callgrind_control` may exceed 16kb which would cause `subprocess.PIPE`
        # to deadlock. So instead we use a file.
        callgrind_stat = check_result(subprocess.run(
            ["callgrind_control", "--stat"],
            stdout=stat_file,
            stderr=subprocess.STDOUT,
        ))

    with open("{stat_log}", "rt") as stat_file:
        stat_lines = stat_file.read().splitlines()

    if f"PID {{PID}}: python {{__file__}}" not in stat_lines:
        log_failure("Process does not appear to be running callgrind.")

    gc.collect()
    time.sleep(0.01)

    # =============================================================================
    # == User code block ==========================================================
    # =============================================================================
    for _ in range({repeats}):
        callgrind_bindings._valgrind_toggle()
    {blocked_stmt}
        callgrind_bindings._valgrind_toggle_and_dump_stats()
        gc.collect()

    {baseline}
""").strip().format(
    indented_stmt=textwrap.indent(task_spec.stmt, " " * 4),
    blocked_stmt=block_stmt(task_spec.stmt, indent=4),
    baseline=(pass_baseline if collect_baseline else ""),
    number=number,
    repeats=repeats,
    load_globals=globals.construct(),
    setup=task_spec.setup,
    warmup_number=min(number, 10),
    num_threads=task_spec.num_threads,
    error_log_repr=repr(error_log),
    stat_log=stat_log,
    parent_interpreter=os.path.realpath(sys.executable),
    torch_file=torch.__file__,
    bindings_import=(
        "import torch._C as callgrind_bindings" if bindings is None
        else f"import {bindings.__name__} as callgrind_bindings"),
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/common.py
# Occurrences: Lines 149-154 (3 instances)

std = torch.tensor(interquartile_points).std(unbiased=False).item()

# ==================================================
# Line: 263

time_unit = {-3: "ns", -2: "us", -1: "ms"}.get(int(torch.tensor(t).log10().item() // 3), "s")

# ==================================================
# Line: 280

magnitude = int(torch.tensor(x).abs().log10().ceil().item())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/cpp_extension.py
# Line: 447

version = versionstr.decode(*SUBPROCESS_DECODE_ARGS).strip().split('.')

# ==================================================
# Line: 479

cuda_version_str = subprocess.check_output([nvcc, '--version']).strip().decode(*SUBPROCESS_DECODE_ARGS)

# ==================================================
# Line: 2935

cl_paths = subprocess.check_output(['where',
                                    'cl']).decode(*SUBPROCESS_DECODE_ARGS).split('\r\n')

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/model_dump/__init__.py
# Line: 224

version = zf.read(path_prefix + "/version").decode("utf-8").strip()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/quantization/_quantized_conversions.py
# Occurrences: Lines 81-98 (3 instances)

(torch.arange(0, ncols // magic0, device=device) * (nrows // 4 * magic0))
.view(-1, 1)
.repeat(1, nrows // 4 * magic0)
.view(-1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/graph_module.py
# Line: 627

module_repr = module.__repr__().replace("\r", " ").replace("\n", " ")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_decomp/decompositions.py
# Line: 1549

ds = torch.mul(grad_output, input).view(N, C, HxW).sum(dim=[2])

# ==================================================
# Occurrences: Lines 1558-1559 (2 instances)

ds_val = torch.mul(ds, gamma.unsqueeze(0)).reshape(N, group, cpg).sum(2)

# ==================================================
# Line: 4512

tensor2.expand(tensor2_expand_size)
.reshape(expand_batch_product, m2)
.unsqueeze(2)

# ==================================================
# Line: 4530

return tensor1_expanded.bmm(tensor2_expanded).squeeze(-1).view(output_shape)

# ==================================================
# Line: 5027

output.permute(2, 0, 1, 3)
.contiguous(memory_format=torch.contiguous_format)
.permute(1, 2, 0, 3)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/utils.py
# Line: 571

g.create("prim::ListConstruct", inputs)
.insertBefore(node)
.output()
.setType(_C.ListType.ofTensors())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_type_utils.py
# Occurrences: Lines 214-218 (2 instances)

return cls.from_dtype(value.type().getElementType().dtype())

# ==================================================
# Line: 224

return cls.from_dtype(value.type().getElementType().dtype())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/verification.py
# Line: 139

return elem.detach().cpu().numpy()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset9.py
# Line: 894

if torch.equal(self_t.mean(d).unsqueeze(d).expand_as(self_t), self_t):

# ==================================================
# Occurrences: Lines 6558-6564 (3 instances)

if node.output().type().isSubtypeOf(
    _C.ListType.ofInts()
) or node.output().type().isSubtypeOf(_C.ListType.ofFloats()):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_core.py
# Line: 137

self.raw.view(torch.uint16).numpy(force=True).view(self.dtype.numpy())

# ==================================================
# Line: 145

return self.raw.view(torch.uint8).numpy(force=True).view(self.dtype.numpy())

# ==================================================
# Line: 167

tensor = self.raw.detach().cpu().contiguous()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_type_casting.py
# Line: 9

data = tensor.view(torch.uint8).numpy(force=True).flatten()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/lowrank_multivariate_normal.py
# Line: 36

return 2 * capacitance_tril.diagonal(dim1=-2, dim2=-1).log().sum(-1) + D.log().sum(

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/kl.py
# Line: 160

flat_trace = bmat.reshape(-1, m * n).pow(2).sum(-1)

# ==================================================
# Line: 384

) - 2 * p._unbroadcasted_scale_tril.diagonal(dim1=-2, dim2=-1).log().sum(-1)

# ==================================================
# Line: 412

term1 = 2 * q._unbroadcasted_scale_tril.diagonal(dim1=-2, dim2=-1).log().sum(
    -1
) - _batch_lowrank_logdet(

# ==================================================
# Occurrences: Lines 450-452 (2 instances)

half_term1 = q._unbroadcasted_scale_tril.diagonal(dim1=-2, dim2=-1).log().sum(
    -1
) - p._unbroadcasted_scale_tril.diagonal(dim1=-2, dim2=-1).log().sum(-1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/constraints.py
# Line: 584

unit_row_norm = (row_norm - 1.0).abs().le(tol).all(dim=-1)

# ==================================================
# Line: 613

return torch.isclose(value, value.mT, atol=1e-6).all(-2).all(-1)

# ==================================================
# Line: 625

return torch.linalg.eigvalsh(value).ge(0).all(-1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/wishart.py
# Line: 24

- torch.arange(p, dtype=x.dtype, device=x.device).div(2).expand(x.shape + (-1,))

# ==================================================
# Occurrences: Lines 304-312 (2 instances)

+ self._unbroadcasted_scale_tril.diagonal(dim1=-2, dim2=-1)
.log()
.sum(-1)

# ==================================================
# Line: 323

+ self._unbroadcasted_scale_tril.diagonal(dim1=-2, dim2=-1)
.log()
.sum(-1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/transforms.py
# Line: 603

return self.exponent.eq(other.exponent).all().item()

# ==================================================
# Line: 669

return (-y).expm1().neg().log() + y

# ==================================================
# Occurrences: Lines 1032-1035 (2 instances)

return x.tril(-1) + x.diagonal(dim1=-2, dim2=-1).exp().diag_embed()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/multivariate_normal.py
# Line: 67

torch.linalg.solve_triangular(flat_L, flat_x_swap, upper=False).pow(2).sum(-2)

# ==================================================
# Line: 241

self._unbroadcasted_scale_tril.pow(2)
.sum(-1)
.expand(self._batch_shape + self._event_shape)

# ==================================================
# Line: 257

self._unbroadcasted_scale_tril.diagonal(dim1=-2, dim2=-1).log().sum(-1)

# ==================================================
# Line: 263

self._unbroadcasted_scale_tril.diagonal(dim1=-2, dim2=-1).log().sum(-1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/masked/_ops.py
# Line: 318

argument_declarations.get(
    a.split("=", 1)[0], f'{a.split("__", 1)[0]}: TBD.'
)
.format(default=a.split("=", 1)[1])
.splitlines()

# ==================================================
# Line: 1064

input = input.to_sparse_coo().to(dtype=torch.int64).to_sparse_csr()

# ==================================================
# Line: 1117

input = input.to_sparse_coo().to(dtype=torch.int64).to_sparse_csr()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/masked/maskedtensor/core.py
# Line: 58

return (a.dim() == b.dim()) and torch.eq(a, b).all().item()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_tensor.py
# Line: 362

else self.cpu().to(torch.float32).numpy()

# ==================================================
# Line: 1130

return self.detach().item().__format__(format_spec)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/storage.py
# Line: 275

torch.tensor([], dtype=torch.uint8, device=self.device)
.set_(cast(Storage, self))
.to(dtype)
._typed_storage()

# ==================================================
# Line: 364

torch.tensor([], dtype=torch.uint8, device=self.device)
.set_(cast(Storage, self))
.is_pinned(device)

# ==================================================
# Line: 383

torch.tensor([], dtype=torch.uint8, device=self.device)
.set_(cast(Storage, self))
.pin_memory(device)

# ==================================================
# Line: 1309

torch.tensor([], dtype=self.dtype, device=self.device)
.set_(self)
.to(dtype)
._typed_storage()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nested/__init__.py
# Line: 108

buffer = ts.contiguous().view(-1).to(device=device, dtype=dtype)

# ==================================================
# Line: 125

values = ts.contiguous().flatten(0, 1).to(device=device, dtype=dtype)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nested/_internal/ops.py
# Line: 1720

inp._offsets.diff().unsqueeze(1).unsqueeze(1) * padded_input.shape[2]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nested/_internal/sdpa.py
# Line: 359

qkv.lengths().cumsum(0).to(dtype=torch.int32, device=qkv.device)

# ==================================================
# Line: 920

attn_out = attn_out.transpose(1, 2).contiguous().values()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_numpy/_ndarray.py
# Line: 371

str(self.tensor)
.replace("tensor", "torch.ndarray")
.replace("dtype=torch.", "dtype=")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_numpy/_funcs_impl.py
# Line: 1992

range = torch.cat(mm).reshape(2, -1).T.flatten()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_library/utils.py
# Line: 461

return t.detach().float().mean()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_library/fake_class_registry.py
# Line: 295

) and obj._type().qualified_name().startswith(  # type: ignore[attr-defined]
    "__torch__.torch.classes"
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/__init__.py
# Line: 471

version = zipf.read("version").decode().split(".")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/utils.py
# Line: 2908

log.warning("Similarity score=%s", score.detach().cpu().item())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/guards.py
# Line: 654

name = name.replace(">", "_").replace("<", "_").replace(".", "_dot_")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/test_case.py
# Line: 167

py_ver = py_ver.group().strip(os.sep).replace("_", "")  # type: ignore[assignment]

# ==================================================
# Line: 185

test_py_ver = tuple(map(int, m.group().removeprefix(prefix).split("_")))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/symbolic_convert.py
# Line: 1552

module_name.replace(">", "_").replace("<", "_").replace(".", "_dot_")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/testing.py
# Line: 66

return x.detach().clone().requires_grad_(x.requires_grad)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/misc.py
# Line: 830

trace_rules.lookup(func)
.create_with_source(func, source=source)
.call_function(tx, args, kwargs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/nn_module.py
# Occurrences: Lines 973-976 (4 instances)

self.var_getattr(tx, "_backward_hooks").realize().len()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/higher_order_ops.py
# Line: 257

BuiltinVariable(callable).call_function(tx, [func_var], {}).as_python_constant()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/amp/grad_scaler.py
# Line: 340

self._scale.double().reciprocal().float()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/algorithms/ddp_comm_hooks/quantization_hooks.py
# Line: 155

nn.functional.pad(
    input=tensor,
    pad=(0, bucket_size - len(tensor) % bucket_size),
    mode="constant",
    value=0,
)
.view(-1, bucket_size)
.to(tensor.device)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/algorithms/ddp_comm_hooks/powerSGD_hook.py
# Line: 584

dist.all_reduce(
    state.p_memory_dict[bucket_index], group=group_to_use, async_op=True
)
.get_future()
.wait()[0]

# ==================================================
# Line: 606

dist.all_reduce(
    state.q_memory_dict[bucket_index], group=group_to_use, async_op=True
)
.get_future()
.wait()[0]

# ==================================================
# Line: 644

allreduce_contiguous_uncompressed_tensors_fut.then(
    unpack_uncompressed_tensors_and_allreduce_ps
)
.then(compute_qs)
.then(decompress)

# ==================================================
# Line: 829

dist.all_reduce(
    state.q_memory_dict[bucket_index], group=group_to_use, async_op=True
)
.get_future()
.wait()[0]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/algorithms/ddp_comm_hooks/default_hooks.py
# Line: 27

dist.all_reduce(tensor, group=group_to_use, async_op=True)
.get_future()
.then(lambda fut: fut.value()[0])

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/c10d_rendezvous_backend.py
# Line: 250

store_type = params.get("store_type", "tcp").strip().lower()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/etcd_rendezvous_backend.py
# Line: 153

protocol = params.get("protocol", "http").strip().lower()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/utils/data/elastic_distributed_sampler.py
# Line: 76

torch.randperm(len(sized_dataset) - self.start_index, generator=g)
.add(self.start_index)
.tolist()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/multiprocessing/errors/__init__.py
# Line: 287

failure.message.get("extraInfo", {})
.get("py_callstack", failure.message.get("message", "<N/A>"))
.replace("\n", "\n  ")  # to properly indent the traceback

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_symmetric_memory/__init__.py
# Line: 525

return t.view(*leading_dims, -1).flatten(0, 1).movedim(0, gather_dim)

# ==================================================
# Line: 571

A_scale.movedim(gather_dim, 0).flatten(0, -2).chunk(group.size())

# ==================================================
# Line: 629

A = A.view(group_size, *A_shard.shape).movedim(gather_dim + 1, 1).flatten(0, 1)

# ==================================================
# Line: 827

A = A.view(group_size, *A_shard.shape).movedim(gather_dim + 1, 1).flatten(0, 1)

# ==================================================
# Line: 839

A_scale.view(group_size, *A_scale_shard.shape)
.movedim(gather_dim + 1, 1)
.flatten(0, -2)

# ==================================================
# Line: 972

return t.permute(perm).contiguous().permute(inv_perm)

# ==================================================
# Line: 1086

stacked_partials.view(*leading_dims, -1)
.movedim(1, scatter_dim + 1)
.movedim(0, scatter_dim),

# ==================================================
# Line: 1261

A_scale.movedim(scatter_dim_after_maybe_reshape, 0)
.contiguous()
.flatten(0, -2)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/sharded_grad_scaler.py
# Line: 242

inv_scale = self._scale.double().reciprocal().float()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharding_spec/chunk_sharding_spec.py
# Line: 162

narrowed_tensor.detach().clone().resize_(scatter_shape)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharding_spec/chunk_sharding_spec_ops/_common.py
# Line: 275

torch.div(torch.mul(local_shard_t, normalized_tensor), local_shard_norm)
.t()
.contiguous()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/parallel/input_reshard.py
# Line: 77

DTensor.from_local(x, device_mesh=mesh)
.redistribute(device_mesh=mesh, placements=[Shard(input_reshard_dim)])
.to_local()

# ==================================================
# Line: 99

DTensor.from_local(
    x, device_mesh=mesh, placements=[Shard(input_reshard_dim)]
)
.redistribute(device_mesh=mesh, placements=[Replicate()])
.to_local()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/debug/_comm_mode.py
# Line: 138

str(type(mod)).replace("<", "").replace(">", "")

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adagrad.py
# Line: 366

std_values = std._values().sqrt_().add_(eps)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/_functional.py
# Line: 69

grad_values.pow(2).sub_(old_exp_avg_sq_values).mul_(1 - beta2)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/_adafactor.py
# Occurrences: Lines 389-394 (2 instances)

torch.norm(grad, dim=-1, keepdim=True).square_().div_(grad.size(-1))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adamax.py
# Line: 284

[exp_inf.mul_(beta2).unsqueeze(0), grad.abs().add_(eps).unsqueeze_(0)],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/asgd.py
# Line: 104

torch.as_tensor(
    _to_scalar(group["lr"]),
    device=p.device,
    dtype=_get_scalar_dtype(),
)
.clone()
.detach()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/lbfgs.py
# Line: 480

if d.mul(t).abs().max() <= tolerance_change:

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/prune.py
# Line: 176

getattr(module, name + "_mask")
.detach()
.clone(memory_format=torch.contiguous_format)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/spectral_norm.py
# Line: 136

[weight_mat.t().mm(weight_mat).pinverse(), weight_mat.t(), u.unsqueeze(1)]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/_expanded_weights/embedding_expanded_weights.py
# Line: 48

input.unsqueeze(-1)
.expand(*input.shape, embedding_dim)
.reshape(batch_size, -1, embedding_dim)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/parametrizations.py
# Line: 31

Q *= X.diagonal(dim1=-2, dim2=-1).sgn().unsqueeze(-2)

# ==================================================
# Line: 110

Q = Q * X.diagonal(dim1=-2, dim2=-1).int().unsqueeze(-2)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/experimental/_paged_attention.py
# Occurrences: Lines 193-194 (2 instances)

k_val = k_val.permute(1, 0, 2, 3).contiguous().view(1, H, B * S, K_D)

# ==================================================
# Line: 242

torch.gather(
    page_table, 1, block_mask.kv_indices.view(B, -1).to(torch.int64)
)
.view(block_mask.kv_indices.shape)
.to(torch.int32)

# ==================================================
# Line: 257

torch.gather(
    page_table,
    1,
    block_mask.full_kv_indices.view(B, -1).to(torch.int64),
)
.view(block_mask.full_kv_indices.shape)
.to(torch.int32)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/flex_attention.py
# Line: 584

percentage = section.float().mean().item()

# ==================================================
# Line: 1212

value = value.transpose(-2, -1).contiguous().transpose(-2, -1)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/functional.py
# Line: 2209

-torch.empty_like(logits, memory_format=torch.legacy_contiguous_format)
.exponential_()
.log()

# ==================================================
# Line: 3017

div = div.mul(alpha).add(k).pow(beta)

# ==================================================
# Occurrences: Lines 5581-5584 (2 instances)

denom = input.norm(p, dim, keepdim=True).clamp_min(eps).expand_as(input)

# ==================================================
# Line: 5712

proj.unflatten(-1, (3, E))
.unsqueeze(0)
.transpose(0, -2)
.squeeze(-2)
.contiguous()

# ==================================================
# Line: 5730

kv_proj.unflatten(-1, (2, E))
.unsqueeze(0)
.transpose(0, -2)
.squeeze(-2)
.contiguous()

# ==================================================
# Line: 6433

key_padding_mask.view(bsz, 1, 1, src_len)
.expand(-1, num_heads, -1, -1)
.reshape(bsz * num_heads, 1, src_len)

# ==================================================
# Line: 6471

attn_output.transpose(0, 1).contiguous().view(tgt_len * bsz, embed_dim)

# ==================================================
# Line: 6504

attn_output.permute(2, 0, 1, 3).contiguous().view(bsz * tgt_len, embed_dim)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/package/package_importer.py
# Line: 352

self.zip_reader.get_record(python_version_path).decode("utf-8").strip()

# ==================================================
# Line: 359

self.zip_reader.get_record(".data/extern_modules")
.decode("utf-8")
.splitlines(keepends=False)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/__init__.py
# Line: 6721

return obj.detach().to(dtype=scalarType, device="cpu", copy=True).view(())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/nn/functional/__init__.py
# Line: 308

input.reshape(n, groups, cg, *dhw)
.transpose(1, 2)
.reshape(input.shape)
.contiguous()

# ==================================================
# Line: 1242

self.view(
    *batch,
    C_out,
    upscale_factor,
    upscale_factor,
    self.shape[-2],
    self.shape[-1],
)
.permute(*B_dims, C_dim, H_dim, r1_dim, W_dim, r2_dim)
.reshape(*batch, C_out, *HW_out)
.clone(memory_format=utils.suggest_memory_format(self))

# ==================================================
# Line: 1270

self.view(
    *batch,
    self.shape[-3],
    HW_out[0],
    downscale_factor,
    HW_out[1],
    downscale_factor,
)
.permute(*B_dims, C_dim, r1_dim, r2_dim, H_dim, W_dim)
.reshape(*batch, C_out, *HW_out)
.clone(memory_format=utils.suggest_memory_format(self))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/activation_sparsifier/activation_sparsifier.py
# Line: 166

torch.Tensor([features[feature_idx]])
.long()
.to(input_data.device)

# ==================================================
# Line: 336

torch.Tensor([features[feature_idx]])
.long()
.to(input_data.device)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/sparsifier/weight_norm_sparsifier.py
# Line: 208

mask.data = mask_reshape.squeeze().reshape(mask.shape).contiguous()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/pt2e/lowering.py
# Line: 53

torch.export.export_for_training(model, example_inputs, strict=True)
.run_decompositions(_post_autograd_decomp_table())
.module()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/native.py
# Line: 145

BackendConfig("_native_and_fp16")
.set_backend_pattern_configs(_get_conv_configs(conv_dtype_configs))
.set_backend_pattern_configs(_get_linear_configs(linear_dtype_configs))
.set_backend_pattern_configs(_get_binary_op_configs(binary_op_dtype_configs))
.set_backend_pattern_config(_get_cat_config(default_op_dtype_configs))
.set_backend_pattern_configs(_get_default_op_configs(default_op_dtype_configs))
.set_backend_pattern_configs(
    _get_fixed_qparams_op_configs(fixed_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_share_qparams_op_configs(share_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_tensor_info_op_configs(tensor_info_op_dtype_configs)
)
.set_backend_pattern_configs(_get_bn_configs(default_op_dtype_configs))
.set_backend_pattern_configs(_get_ln_configs(layer_norm_op_dtype_configs))
.set_backend_pattern_configs(_get_rnn_op_configs(rnn_op_dtype_configs))
.set_backend_pattern_configs(
    _get_embedding_op_configs(embedding_op_dtype_configs)
)

# ==================================================
# Line: 195

BackendConfig("native")
.set_backend_pattern_configs(_get_conv_configs(conv_dtype_configs))
.set_backend_pattern_configs(_get_linear_configs(linear_dtype_configs))
.set_backend_pattern_configs(_get_binary_op_configs(binary_op_dtype_configs))
.set_backend_pattern_config(_get_cat_config(default_op_dtype_configs))
.set_backend_pattern_configs(_get_default_op_configs(default_op_dtype_configs))
.set_backend_pattern_configs(
    _get_fixed_qparams_op_configs(fixed_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_share_qparams_op_configs(share_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_tensor_info_op_configs(tensor_info_op_dtype_configs)
)
.set_backend_pattern_configs(_get_bn_configs(default_op_dtype_configs))
.set_backend_pattern_configs(_get_ln_configs(layer_norm_op_dtype_configs))
.set_backend_pattern_configs(_get_rnn_op_configs(rnn_op_dtype_configs))
.set_backend_pattern_configs(
    _get_embedding_op_configs(embedding_op_dtype_configs)
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/executorch.py
# Occurrences: Lines 115-135 (3 instances)

BackendPatternConfig(torch.nn.Linear)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)
.set_root_module(torch.nn.Linear)
.set_reference_quantized_module(nnqr.Linear)
.set_qat_module(nnqat.Linear)

# ==================================================
# Occurrences: Lines 155-175 (3 instances)

BackendPatternConfig(convs.root)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)
.set_root_module(convs.root)
.set_reference_quantized_module(convs.reference)
.set_qat_module(convs.qat)

# ==================================================
# Occurrences: Lines 182-234 (8 instances)

BackendPatternConfig((convs.root, nn.ReLU))
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_fuser_method(_sequential_wrapper2(convs.fused_conv_relu))
.set_fused_module(convs.fused_conv_relu)

# ==================================================
# Occurrences: Lines 241-259 (3 instances)

BackendPatternConfig((convs.root, convs.bn))
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_fuser_method(fuse_conv_bn)
.set_fused_module(convs.fused_conv_bn)

# ==================================================
# Occurrences: Lines 265-291 (4 instances)

BackendPatternConfig(convs.fused_conv_bn)
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_qat_module(convs.bn_qat)

# ==================================================
# Line: 328

BackendPatternConfig(bop_pattern)
.set_dtype_configs(dtype_configs)  # noqa: E131
._set_num_tensor_args_to_observation_type(
    num_tensor_args_to_observation_type_mapping
)

# ==================================================
# Line: 388

BackendPatternConfig(op)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)

# ==================================================
# Line: 407

BackendPatternConfig(nn.BatchNorm2d)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)

# ==================================================
# Occurrences: Lines 421-433 (3 instances)

BackendPatternConfig(torch.cat)
.set_observation_type(ObservationType.OUTPUT_SHARE_OBSERVER_WITH_INPUT)
.set_dtype_configs(dtype_configs)

# ==================================================
# Occurrences: Lines 448-475 (3 instances)

BackendPatternConfig(embedding_op)
.set_observation_type(
    ObservationType.OUTPUT_USE_DIFFERENT_OBSERVER_AS_INPUT
)  # noqa: E131
.set_dtype_configs(dtype_configs)
.set_qat_module(qat_embedding_op)
.set_root_module(embedding_op)
.set_reference_quantized_module(ref_embedding_op)

# ==================================================
# Line: 490

BackendConfig("executorch")
.set_backend_pattern_configs(_get_linear_configs())
.set_backend_pattern_configs(_get_conv_configs())
.set_backend_pattern_configs(_get_binary_ops_configs())
.set_backend_pattern_configs(_get_share_qparams_ops_configs())
.set_backend_pattern_configs(_get_bn_configs())
.set_backend_pattern_configs(_get_cat_configs())
.set_backend_pattern_configs(_get_embedding_op_configs())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/fbgemm.py
# Line: 109

BackendConfig("fbgemm")
.set_backend_pattern_configs(_get_conv_configs(conv_dtype_configs))
.set_backend_pattern_configs(_get_linear_configs(linear_dtype_configs))
.set_backend_pattern_configs(_get_binary_op_configs(binary_op_dtype_configs))
.set_backend_pattern_config(_get_cat_config(default_op_dtype_configs))
.set_backend_pattern_configs(_get_default_op_configs(default_op_dtype_configs))
.set_backend_pattern_configs(
    _get_fixed_qparams_op_configs(fixed_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_share_qparams_op_configs(share_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_tensor_info_op_configs(tensor_info_op_dtype_configs)
)
.set_backend_pattern_configs(_get_bn_configs(default_op_dtype_configs))
.set_backend_pattern_configs(_get_rnn_op_configs(rnn_op_dtype_configs))
.set_backend_pattern_configs(
    _get_embedding_op_configs(embedding_op_dtype_configs)
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/_qnnpack_pt2e.py
# Occurrences: Lines 61-71 (2 instances)

BackendPatternConfig(torch.ops.aten.addmm.default)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)
._set_input_type_to_index({"weight": 2, "bias": 0})

# ==================================================
# Occurrences: Lines 81-101 (3 instances)

BackendPatternConfig(torch.ops.aten.convolution.default)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)
._set_input_type_to_index({"weight": 1, "bias": 2})

# ==================================================
# Line: 116

BackendPatternConfig()
._set_pattern_complex_format(
    (operator.getitem, torch.ops.aten.max_pool2d_with_indices.default, 0)
)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)
._set_root_node_getter(root_node_getter)

# ==================================================
# Line: 133

BackendPatternConfig(torch.ops.aten.relu.default)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)

# ==================================================
# Line: 162

BackendPatternConfig(bop_pattern)
.set_dtype_configs(dtype_configs)  # noqa: E131
._set_num_tensor_args_to_observation_type(
    num_tensor_args_to_observation_type_mapping
)

# ==================================================
# Line: 175

BackendConfig("qnnpack_pytorch_2.0_export")
.set_backend_pattern_configs(get_linear_configs())
.set_backend_pattern_configs(get_binary_op_configs())
.set_backend_pattern_configs(get_conv_configs())
.set_backend_pattern_configs(get_pooling_configs())
.set_backend_pattern_configs(get_relu_configs())

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/x86.py
# Line: 106

BackendConfig("x86")
.set_backend_pattern_configs(_get_conv_configs(conv_dtype_configs))
.set_backend_pattern_configs(_get_linear_configs(linear_dtype_configs))
.set_backend_pattern_configs(_get_binary_op_configs(binary_op_dtype_configs))
.set_backend_pattern_config(_get_cat_config(default_op_dtype_configs))
.set_backend_pattern_configs(_get_default_op_configs(default_op_dtype_configs))
.set_backend_pattern_configs(
    _get_fixed_qparams_op_configs(fixed_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_share_qparams_op_configs(share_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_tensor_info_op_configs(tensor_info_op_dtype_configs)
)
.set_backend_pattern_configs(_get_bn_configs(default_op_dtype_configs))
.set_backend_pattern_configs(_get_rnn_op_configs(rnn_op_dtype_configs))
.set_backend_pattern_configs(
    _get_embedding_op_configs(embedding_op_dtype_configs)
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/tensorrt.py
# Occurrences: Lines 45-59 (2 instances)

BackendPatternConfig(torch.addmm)
.set_observation_type(ObservationType.OUTPUT_USE_DIFFERENT_OBSERVER_AS_INPUT)
.add_dtype_config(weighted_op_qint8_dtype_config)
._set_input_type_to_index(
    {
        "bias": 0,
        "input": 1,
        "weight": 2,
    }
)

# ==================================================
# Line: 79

BackendConfig("tensorrt")
.set_backend_pattern_configs(_get_conv_configs(conv_dtype_configs))
.set_backend_pattern_config(addmm_config)
.set_backend_pattern_config(cat_config)
.set_backend_pattern_configs(_get_linear_configs(linear_dtype_configs))
.set_backend_pattern_configs(_get_binary_op_configs(binary_op_dtype_configs))
.set_backend_pattern_configs(
    _get_share_qparams_op_configs(share_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_tensor_info_op_configs(tensor_info_op_dtype_configs)
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/onednn.py
# Occurrences: Lines 189-211 (2 instances)

BackendPatternConfig()
._set_pattern_complex_format(
    (add_op, (nn.BatchNorm2d, nn.Conv2d), MatchAllNode)
)  # noqa: E131
.set_observation_type(observation_type)
.set_dtype_configs(conv_dtype_configs)
.set_fuser_method(_fuse_conv_bn_add_left)
._set_root_node_getter(_conv_bn_add_root_node_getter_left)
._set_extra_inputs_getter(_conv_bn_add_extra_inputs_getter_left)
.set_fused_module(nni.ConvAdd2d)

# ==================================================
# Occurrences: Lines 274-304 (3 instances)

BackendPatternConfig()
._set_pattern_complex_format(
    (add_op, MatchAllNode, (nn.BatchNorm2d, nn.Conv2d))
)  # noqa: E131
.set_observation_type(observation_type)
.set_dtype_configs(conv_dtype_configs)
.set_fuser_method(_fuse_conv_bn_add_right)
._set_root_node_getter(_conv_bn_add_root_node_getter_right)
._set_extra_inputs_getter(_conv_bn_add_extra_inputs_getter_right)
.set_fused_module(nni.ConvAdd2d)

# ==================================================
# Occurrences: Lines 379-401 (2 instances)

BackendPatternConfig()
._set_pattern_complex_format(
    (nn.ReLU, (add_op, (nn.BatchNorm2d, nn.Conv2d), MatchAllNode))
)  # noqa: E131
.set_observation_type(observation_type)
.set_dtype_configs(conv_dtype_configs)
.set_fuser_method(_fuse_conv_bn_add_relu_left)
._set_root_node_getter(_conv_bn_add_relu_root_node_getter_left)
._set_extra_inputs_getter(_conv_bn_add_relu_extra_inputs_getter_left)
.set_fused_module(nni.ConvAddReLU2d)

# ==================================================
# Occurrences: Lines 474-504 (3 instances)

BackendPatternConfig()
._set_pattern_complex_format(
    (nn.ReLU, (add_op, MatchAllNode, (nn.BatchNorm2d, nn.Conv2d)))
)  # noqa: E131
.set_observation_type(observation_type)
.set_dtype_configs(conv_dtype_configs)
.set_fuser_method(_fuse_conv_bn_add_relu_right)
._set_root_node_getter(_conv_bn_add_relu_root_node_getter_right)
._set_extra_inputs_getter(_conv_bn_add_relu_extra_inputs_getter_right)
.set_fused_module(nni.ConvAddReLU2d)

# ==================================================
# Occurrences: Lines 532-563 (5 instances)

BackendPatternConfig((root_module, post_module))
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_fuser_method(fuser_method)
.set_fused_module(fused_module)

# ==================================================
# Line: 583

BackendPatternConfig((nn.Linear, nn.BatchNorm1d, nn.LeakyReLU))
.set_dtype_configs(linear_dtype_configs)  # noqa: E131
.set_fuser_method(_fuse_linear_bn_leaky_relu)
.set_fused_module(nni.LinearLeakyReLU)

# ==================================================
# Line: 625

BackendConfig("onednn")
.set_backend_pattern_configs(conv_configs)
.set_backend_pattern_configs(linear_configs)
.set_backend_pattern_configs(_get_binary_op_configs(binary_op_dtype_configs))
.set_backend_pattern_config(_get_cat_config(default_op_dtype_configs))
.set_backend_pattern_configs(_get_default_op_configs(default_op_dtype_configs))
.set_backend_pattern_configs(
    _get_fixed_qparams_op_configs(fixed_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_share_qparams_op_configs(share_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(_get_bn_configs(default_op_dtype_configs))
.set_backend_pattern_configs(_get_ln_configs(layer_norm_op_dtype_configs))
.set_backend_pattern_configs(_get_rnn_op_configs(rnn_op_dtype_configs))
.set_backend_pattern_configs(
    _get_embedding_op_configs(embedding_op_dtype_configs)
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/_common_operator_config_utils.py
# Line: 159

BackendPatternConfig(bop_pattern)
.set_dtype_configs(dtype_configs)  # noqa: E131
._set_num_tensor_args_to_observation_type(
    num_tensor_args_to_observation_type_mapping
)

# ==================================================
# Occurrences: Lines 186-206 (3 instances)

BackendPatternConfig(torch.nn.Linear)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)
.set_root_module(torch.nn.Linear)
.set_reference_quantized_module(nnqr.Linear)
.set_qat_module(nnqat.Linear)

# ==================================================
# Occurrences: Lines 214-224 (2 instances)

BackendPatternConfig((torch.nn.Linear, torch.nn.ReLU))
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_fuser_method(_sequential_wrapper2(nni.LinearReLU))
.set_fused_module(nni.LinearReLU)

# ==================================================
# Occurrences: Lines 230-256 (4 instances)

BackendPatternConfig(nni.LinearReLU)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)
.set_root_module(torch.nn.Linear)
.set_reference_quantized_module(nnqr.Linear)
.set_qat_module(nniqat.LinearReLU)

# ==================================================
# Line: 263

BackendPatternConfig((nn.Linear, nn.BatchNorm1d))
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_fuser_method(fuse_linear_bn)
.set_fused_module(nni.LinearBn1d)

# ==================================================
# Occurrences: Lines 272-285 (2 instances)

BackendPatternConfig(nni.LinearBn1d)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)
.set_root_module(torch.nn.Linear)
.set_reference_quantized_module(nnqr.Linear)
.set_qat_module(nniqat.LinearBn1d)

# ==================================================
# Occurrences: Lines 301-321 (3 instances)

BackendPatternConfig(convs.root)
.set_observation_type(observation_type)  # noqa: E131
.set_dtype_configs(dtype_configs)
.set_root_module(convs.root)
.set_reference_quantized_module(convs.reference)
.set_qat_module(convs.qat)

# ==================================================
# Occurrences: Lines 329-384 (8 instances)

BackendPatternConfig((convs.root, torch.nn.ReLU))
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_fuser_method(_sequential_wrapper2(convs.fused_conv_relu))
.set_fused_module(convs.fused_conv_relu)

# ==================================================
# Occurrences: Lines 392-410 (3 instances)

BackendPatternConfig((convs.root, convs.bn))
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_fuser_method(fuse_conv_bn)
.set_fused_module(convs.fused_conv_bn)

# ==================================================
# Occurrences: Lines 417-443 (4 instances)

BackendPatternConfig(convs.fused_conv_bn)
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_qat_module(convs.bn_qat)

# ==================================================
# Occurrences: Lines 449-468 (3 instances)

BackendPatternConfig(convs.transpose)
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_root_module(convs.transpose)
.set_reference_quantized_module(convs.transpose_reference)

# ==================================================
# Line: 476

BackendPatternConfig(torch.cat)
.set_observation_type(ObservationType.OUTPUT_SHARE_OBSERVER_WITH_INPUT)
.set_dtype_configs(dtype_configs)

# ==================================================
# Occurrences: Lines 485-497 (2 instances)

BackendPatternConfig(torch.nn.LayerNorm)
.set_observation_type(
    ObservationType.OUTPUT_USE_DIFFERENT_OBSERVER_AS_INPUT
)  # noqa: E131
.set_dtype_configs(dtype_configs)

# ==================================================
# Occurrences: Lines 520-543 (3 instances)

BackendPatternConfig(op)
.set_observation_type(
    ObservationType.OUTPUT_USE_DIFFERENT_OBSERVER_AS_INPUT
)  # noqa: E131
.set_dtype_configs(dtype_configs)

# ==================================================
# Line: 596

BackendPatternConfig(fixed_qparam_op)
.set_observation_type(
    ObservationType.OUTPUT_USE_DIFFERENT_OBSERVER_AS_INPUT
)  # noqa: E131
.set_dtype_configs(new_dtype_configs)

# ==================================================
# Line: 616

BackendPatternConfig(op)
.set_observation_type(ObservationType.OUTPUT_SHARE_OBSERVER_WITH_INPUT)
.set_dtype_configs(dtype_configs)

# ==================================================
# Occurrences: Lines 696-713 (3 instances)

BackendPatternConfig((bn, nn.ReLU))
.set_dtype_configs(dtype_configs)  # noqa: E131
.set_fuser_method(_sequential_wrapper2(fused_bn))
.set_fused_module(fused_bn)

# ==================================================
# Line: 719

BackendPatternConfig(fused_bn)
.set_observation_type(
    ObservationType.OUTPUT_USE_DIFFERENT_OBSERVER_AS_INPUT
)  # noqa: E131
.set_dtype_configs(dtype_configs)

# ==================================================
# Line: 738

BackendPatternConfig(rnn_op)
.set_observation_type(
    ObservationType.OUTPUT_USE_DIFFERENT_OBSERVER_AS_INPUT
)  # noqa: E131
.set_dtype_configs(dtype_configs)
.set_root_module(rnn_op)
.set_reference_quantized_module(ref_rnn_op)

# ==================================================
# Occurrences: Lines 758-776 (2 instances)

BackendPatternConfig(embedding_op)
.set_observation_type(
    ObservationType.OUTPUT_USE_DIFFERENT_OBSERVER_AS_INPUT
)  # noqa: E131
.set_dtype_configs(dtype_configs)
.set_qat_module(qat_embedding_op)
.set_root_module(embedding_op)
.set_reference_quantized_module(ref_embedding_op)

# ==================================================
# Line: 789

BackendPatternConfig(op)
.set_observation_type(ObservationType.INPUT_OUTPUT_NOT_OBSERVED)
.set_dtype_configs(dtype_configs)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/qnnpack.py
# Line: 154

BackendConfig("qnnpack")
.set_backend_pattern_configs(_get_conv_configs(conv_dtype_configs))
.set_backend_pattern_configs(_get_linear_configs(linear_dtype_configs))
.set_backend_pattern_configs(_get_binary_op_configs(binary_op_dtype_configs))
.set_backend_pattern_config(_get_cat_config(default_op_dtype_configs))
.set_backend_pattern_configs(_get_default_op_configs(default_op_dtype_configs))
.set_backend_pattern_configs(
    _get_fixed_qparams_op_configs(fixed_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(
    _get_share_qparams_op_configs(share_qparams_op_dtype_configs)
)
.set_backend_pattern_configs(_get_bn_configs(default_op_dtype_configs))
.set_backend_pattern_configs(_get_rnn_op_configs(rnn_op_dtype_configs))
.set_backend_pattern_configs(
    _get_embedding_op_configs(embedding_op_dtype_configs)
)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/_learnable_fake_quantize.py
# Line: 94

self.toggle_qparam_learning(enabled=True).toggle_fake_quant(
    enabled=True
).toggle_observer_update(enabled=False)

# ==================================================
# Line: 106

self.toggle_qparam_learning(enabled=False).toggle_fake_quant(
    enabled=True
).toggle_observer_update(enabled=True)

# ==================================================
# Line: 117

self.toggle_qparam_learning(enabled=False).toggle_fake_quant(
    enabled=False
).toggle_observer_update(enabled=True)

# ==================================================
# Line: 152

self.zero_point.detach()
.round()
.clamp(self.quant_min, self.quant_max)
.long()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_lower_to_native_backend.py
# Line: 511

packed_weight_name.replace(":", "_")
.replace("/", "_")
.replace("|", "_")
.replace(" ", "")
.lower()

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/convert.py
# Line: 1213

elif type_before_parametrizations(mod) in set(root_module_classes).union(
    qat_module_classes
).union(fused_module_classes):

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_decomposed.py
# Line: 910

input.mul(1.0 / scales)
.add(zero_points)
.round()
.clamp(quant_min, quant_max)
.to(dtype)

# ==================================================
# Line: 1022

to_quant.mul(1.0 / scales)
.add(zero_points)
.round()
.clamp_(quant_min, quant_max)
.to(dtype)
.reshape_as(input)

# ==================================================
# Line: 1124

w_dq = w_int8_grouped.sub(zp).mul(scales).reshape_as(w_int8).to(output_dtype)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/qconfig_mapping.py
# Line: 91

QConfigMapping()
.set_global(qconfig)
.set_object_type("reshape", default_reuse_input_qconfig)
.set_object_type(torch.nn.ConvTranspose1d, qconfig_transpose)
.set_object_type(torch.nn.ConvTranspose2d, qconfig_transpose)
.set_object_type(torch.nn.ConvTranspose3d, qconfig_transpose)
.set_object_type(torch.nn.functional.conv_transpose1d, qconfig_transpose)
.set_object_type(torch.nn.functional.conv_transpose2d, qconfig_transpose)
.set_object_type(torch.nn.functional.conv_transpose3d, qconfig_transpose)
.set_object_type(torch.nn.functional.layer_norm, qconfig_layernorm)
.set_object_type(torch.nn.LayerNorm, qconfig_layernorm)
.set_object_type(torch.nn.PReLU, default_quint8_weight_qconfig)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/experimental/adaround_optimization.py
# Line: 190

torch.abs(out[0] - module(fp_in[0])).sum().item() == 0

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/experimental/adaround_loss.py
# Line: 66

inner_term = torch.add(2 * h_alpha, -1).abs().pow(beta)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantizable/modules/activation.py
# Occurrences: Lines 448-452 (3 instances)

q = q.contiguous().view(tgt_len, bsz * self.num_heads, head_dim).transpose(0, 1)

# ==================================================
# Line: 530

attn_output.transpose(0, 1)
.contiguous()
.view(tgt_len, bsz, self.embed_dim)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/mtia/memory.py
# Line: 36

return memory_stats(device).get("dram", 0).get("peak_bytes", 0)

# ==================================================
