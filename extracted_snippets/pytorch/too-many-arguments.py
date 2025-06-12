# too-many-arguments snippets for pytorch

# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/mixed_mm/gen_data_mixed_mm.py
# Line: 41

def run_benchmark(
    self,
    m: int,
    k: int,
    n: int,
    transpose_left: bool,
    transpose_right: bool,
    dtype_left: Any,
    dtype_right: Any,

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/benchmark_utils.py
# Line: 26

def get_mm_tensors(
    m: int,
    k: int,
    n: int,
    transpose_left: bool,
    transpose_right: bool,
    dtype_left: Any,
    dtype_right: Any,

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train.py
# Line: 150

def codegen_boilerplate(
    self, heuristic_name, opt_name, threshold, shared_memory, device_capa, dt

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/ah_tree.py
# Line: 8

def __init__(
    self,
    feature: Optional[str] = None,
    threshold: Optional[float] = None,
    left: Optional["DecisionTreeNode"] = None,
    right: Optional["DecisionTreeNode"] = None,
    class_probs: Any = None,
    num_samples: int = 0,
    node_id: int = 0,

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train_decision.py
# Line: 121

def train_and_evaluate_models(
    self,
    datasets,
    max_depths,
    min_samples_leafs,
    criterion_list,
    feature_columns,
    ranking=False,

# ==================================================
# Line: 296

def main(
    self,
    log_path,
    other_datasets,
    nrows,
    heuristic_name,
    save_dot=False,
    ranking=False,

# ==================================================
# Line: 533

def codegen_boilerplate(
    self, heuristic_name, opt_name, threshold, shared_memory, device_capa, classes

# ==================================================
# Line: 596

def codegen(
    self,
    tree,
    metadata,
    heuristic_name,
    threshold,
    dummy_col_2_col_val,
    unsafe_leaves,

# ==================================================
# Line: 723

def __init__(
    self,
    train,
    model,
    predictions,
    df,
    probas,
    wrong_pct=0.01,
    threshold=0.0,
    k=10,
    unsafe_leaves=None,
    leaf_ids=None,
    ranking=False,

# ==================================================
# Line: 800

def eval_prediction(
    self, avail_choices, leaf_id, pred, true, prob, threshold, default_config, i

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train_regression.py
# Line: 37

def main(
    self,
    log_path,
    other_datasets,
    nrows,
    heuristic_name,
    save_dot=False,
    ranking=False,

# ==================================================
# Line: 223

def train_and_evaluate_models(
    self,
    datasets,
    feature_columns,
    choice_columns,
    max_depths,
    min_samples_leafs,
    threshold=0.99,

# ==================================================
# Line: 368

def dt_to_python(
    self,
    dt,
    metadata,
    feature_names,
    dummy_col_2_col_val,
    heuristic_name,
    threshold,
    unsafe_leaves=None,

# ==================================================
# Line: 436

def codegen_boilerplate(
    self, heuristic_name, opt_name, threshold, shared_memory, device_capa, classes

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/pad_mm/gen_data_pad_mm.py
# Line: 51

def run_benchmark(
    self,
    m: int,
    k: int,
    n: int,
    transpose_left: bool,
    transpose_right: bool,
    dtype: Any,
    prepadded_left: bool,
    prepadded_right: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/utils.py
# Line: 231

def write_sharded(
    self,
    filename: str | Path,
    items: Iterable[T],
    *,
    key_fn: Callable[[T], str],
    env_callable: Callable[[T], dict[str, list[str]]],
    num_shards: int,
    base_env: dict[str, Any] | None = None,
    sharded_keys: set[str],

# ==================================================
# Line: 253

def write_sharded_with_template(
    self,
    filename: str | Path,
    template_fn: str | Path,
    items: Iterable[T],
    *,
    key_fn: Callable[[T], str],
    env_callable: Callable[[T], dict[str, list[str]]],
    num_shards: int,
    base_env: dict[str, Any] | None = None,
    sharded_keys: set[str],

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen.py
# Line: 1563

def get_native_function_definitions(
    *,
    fm: FileManager,
    grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup],
    dispatch_key: DispatchKey,
    backend_idx: BackendIndex,
    selector: SelectiveBuilder,
    rocm: bool,
    symint: bool,
    skip_dispatcher_op_registration: bool,
    gen_dispatch_helpers: bool,

# ==================================================
# Line: 1747

def gen_aggregated_headers(
    *,
    native_functions: Sequence[NativeFunction],
    grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup],
    structured_native_functions: Sequence[NativeFunctionsGroup],
    static_dispatch_idx: list[BackendIndex],
    selector: SelectiveBuilder,
    backend_indices: dict[DispatchKey, BackendIndex],
    cpu_fm: FileManager,
    device_fms: dict[str, FileManager],
    functions_keys: set[DispatchKey],
    dispatch_keys: Sequence[DispatchKey],
    rocm: bool,

# ==================================================
# Line: 1868

def gen_per_operator_headers(
    *,
    native_functions: Sequence[NativeFunction],
    grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup],
    static_dispatch_idx: list[BackendIndex],
    selector: SelectiveBuilder,
    backend_indices: dict[DispatchKey, BackendIndex],
    cpu_fm: FileManager,
    device_fms: dict[str, FileManager],
    ops_fm: FileManager,
    functions_keys: set[DispatchKey],
    dispatch_keys: Sequence[DispatchKey],
    rocm: bool,

# ==================================================
# Line: 2062

def gen_headers(
    *,
    native_functions: Sequence[NativeFunction],
    valid_tags: set[str],
    grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup],
    structured_native_functions: Sequence[NativeFunctionsGroup],
    static_dispatch_idx: list[BackendIndex],
    selector: SelectiveBuilder,
    backend_indices: dict[DispatchKey, BackendIndex],
    core_fm: FileManager,
    cpu_fm: FileManager,
    device_fms: dict[str, FileManager],
    ops_fm: FileManager,
    dispatch_keys: Sequence[DispatchKey],
    functions_keys: set[DispatchKey],
    rocm: bool,
    per_operator_headers: bool,

# ==================================================
# Line: 2200

def gen_source_files(
    *,
    native_functions: Sequence[NativeFunction],
    grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup],
    structured_native_functions: Sequence[NativeFunctionsGroup],
    view_groups: Sequence[NativeFunctionsViewGroup],
    selector: SelectiveBuilder,
    static_dispatch_idx: list[BackendIndex],
    backend_indices: dict[DispatchKey, BackendIndex],
    aoti_fm: FileManager,
    core_fm: FileManager,
    cpu_vec_fm: FileManager,
    cpu_fm: FileManager,
    device_fms: dict[str, FileManager],
    dispatch_keys: Sequence[DispatchKey],
    functions_keys: set[DispatchKey],
    rocm: bool,
    force_schema_registration: bool,
    per_operator_headers: bool,
    skip_dispatcher_op_registration: bool,
    update_aoti_c_shim: bool,
    aoti_backends: set[DispatchKey],
    extend_aoti_c_shim: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_backend_stubs.py
# Line: 252

def error_on_missing_kernels(
    native_functions: Sequence[NativeFunction],
    backend_indices: dict[DispatchKey, BackendIndex],
    backend_key: DispatchKey,
    autograd_key: DispatchKey | None,
    class_name: str,
    kernel_defn_file_path: str,
    full_codegen: list[OperatorName] | None = None,

# ==================================================
# Line: 361

def gen_dispatchkey_nativefunc_headers(
    fm: FileManager,
    class_name: str,
    cpp_namespace: str,
    backend_indices: dict[DispatchKey, BackendIndex],
    grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup],
    backend_dispatch_key: DispatchKey,
    autograd_dispatch_key: DispatchKey | None,
    backend_name: str = "",

# ==================================================
# Line: 418

def gen_dispatcher_registrations(
    fm: FileManager,
    output_dir: str,
    class_name: str,
    backend_indices: dict[DispatchKey, BackendIndex],
    grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup],
    backend_dispatch_key: DispatchKey,
    dispatch_key: DispatchKey,
    selector: SelectiveBuilder,
    # build_in_tree is true for lazy TS backend and affects include paths, not used for external backends
    build_in_tree: bool = False,
    per_operator_headers: bool = False,
    backend_name: str = "",
    eager_registration: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_lazy_tensor.py
# Line: 285

def run_gen_lazy_tensor(
    aten_path: str,
    source_yaml: str,
    output_dir: str,
    dry_run: bool,
    impl_path: str | None,
    node_base: str = default_args.node_base,
    node_base_hdr: str | None = default_args.node_base_hdr,
    tensor_class: str = default_args.tensor_class,
    tensor_class_hdr: str = default_args.tensor_class_hdr,
    shape_inference_hdr: str = default_args.shape_inference_hdr,
    lazy_ir_generator: type[GenLazyIR] = default_args.lazy_ir_generator,
    native_func_definition_generator: type[
        GenLazyNativeFuncDefinition
    ] = default_args.native_func_definition_generator,
    # build_in_tree is true for TS backend and affects include paths
    build_in_tree: bool = False,
    # per_operator_headers changes whether ATen/Functions.h or individual operator headers are used
    # it must match how ATen was built
    per_operator_headers: bool = False,
    backend_name: str = default_args.backend_name,
    gen_forced_fallback_code: bool = False,
    use_lazy_shape: bool = True,
    # the following arguments are temporary customization points for xla backend migration.
    # do not rely on them otherwise, they should be removed once migration is complete
    backend_namespace: str = "torch::lazy",
    get_tensorlist: str = "GetTensorList",
    get_tensor_or_wrap_number: str = "GetLtcTensorOrCreateForWrappedNumber",
    try_get_tensor: str = "TryGetLtcTensor",
    metrics_counter: str = 'TORCH_LAZY_FN_COUNTER("lazy::")',
    create_tensor: str = "LazyTensor::Create",
    create_from_first_tensor: bool = False,
    create_aten_from_ltc_tensor: str = "torch::lazy::CreateAtenFromLtcTensor",
    tuple_aten_from_ltc_tensors: str = "torch::lazy::TupleAtenFromLtcTensors",
    lazy_value_class: str = "torch::lazy::Value",
    lazy_tensor_ptr: str = "LazyTensorPtr",
    get_device_fn: str = "torch::lazy::GetBackendDevice",

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/gen_aoti_c_shim.py
# Line: 454

def gen_c_shim(
    func: NativeFunction,
    version_info: dict[str, list[str]],
    func_group_mapping: dict[OperatorName, NativeFunctionsGroup],
    dispatch_key: DispatchKey,
    backend_indices: dict[DispatchKey, BackendIndex],
    header: bool,
    extend_aoti_c_shim: bool,

# ==================================================
# Line: 519

def gen_aoti_c_shim(
    native_functions: Sequence[NativeFunction],
    inductor_fallback_ops: dict[str, dict[str, list[str]]],
    func_group_mapping: dict[OperatorName, NativeFunctionsGroup],
    dispatch_key: DispatchKey,
    backend_indices: dict[DispatchKey, BackendIndex],
    header: bool,
    extend_aoti_c_shim: bool,
    includes: str = "",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_shape_functions.py
# Line: 200

def pooling_output_shape_pad_lr(
    inputSize: int,
    kernelSize: int,
    pad_l: int,
    pad_r: int,
    stride: int,
    dilation: int,
    ceil_mode: bool,

# ==================================================
# Line: 241

def pool2d_shape_check(
    input: list[int],
    kH: int,
    kW: int,
    dH: int,
    dW: int,
    padH: int,
    padW: int,
    dilationH: int,
    dilationW: int,
    nInputPlane: int,
    inputHeight: int,
    inputWidth: int,
    outputHeight: int,
    outputWidth: int,

# ==================================================
# Line: 685

def check_shape_forward(
    input: list[int],
    weight_sizes: list[int],
    bias: Optional[list[int]],
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    groups: int,

# ==================================================
# Line: 716

def conv_output_size(
    input_size: list[int],
    weight_size: list[int],
    bias: Optional[list[int]],
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    groups: int,

# ==================================================
# Line: 746

def conv1d(
    input: list[int],
    weight: list[int],
    bias: Optional[list[int]],
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    groups: int,

# ==================================================
# Line: 760

def conv2d(
    input: list[int],
    weight: list[int],
    bias: Optional[list[int]],
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    groups: int,

# ==================================================
# Line: 784

def conv_transpose2d_input(
    input: list[int],
    weight: list[int],
    bias: Optional[list[int]] = None,
    stride: Optional[list[int]] = None,
    padding: Optional[list[int]] = None,
    output_padding: Optional[list[int]] = None,
    groups: int = 1,
    dilation: Optional[list[int]] = None,

# ==================================================
# Line: 823

def conv_forwards(
    input: list[int],
    weight: list[int],
    bias: Optional[list[int]],
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    transposed: bool,
    output_padding: list[int],
    groups: int,

# ==================================================
# Line: 866

def _conv_forwards(
    input: list[int],
    weight: list[int],
    bias: Optional[list[int]],
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    transposed: bool,
    output_padding: list[int],
    groups: int,
    benchmark: bool,
    deterministic: bool,
    cudnn_enabled: bool,
    allow_tf32: bool,

# ==================================================
# Line: 894

def batch_norm(
    input: list[int],
    weight: Optional[list[int]],
    bias: Optional[list[int]],
    running_mean: Optional[list[int]],
    running_var: Optional[list[int]],
    training: bool,
    momentum: float,
    eps: float,
    cudnn_enabled: bool,

# ==================================================
# Line: 911

def conv3d(
    input: list[int],
    weight: list[int],
    bias: Optional[list[int]],
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    groups: int,

# ==================================================
# Line: 962

def arange_start_step(
    start: number, end: number, step: number, inp0: Any, inp1: Any, inp2: Any, inp3: Any

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_trace.py
# Line: 319

def _check_trace(
    check_inputs,
    func,
    traced_func,
    check_tolerance,
    strict,
    force_outplace,
    is_trace_module,
    _module_class,
    example_inputs_is_kwarg=False,

# ==================================================
# Line: 668

def _trace_impl(
    func,
    example_inputs=None,
    optimize=None,
    check_trace=True,
    check_inputs=None,
    check_tolerance=1e-5,
    strict=True,
    _force_outplace=False,
    _module_class=None,
    _compilation_unit=_python_cu,
    example_kwarg_inputs=None,
    _store_inputs=True,

# ==================================================
# Line: 825

def trace(
    func,
    example_inputs=None,
    optimize=None,
    check_trace=True,
    check_inputs=None,
    check_tolerance=1e-5,
    strict=True,
    _force_outplace=False,
    _module_class=None,
    _compilation_unit=_python_cu,
    example_kwarg_inputs=None,
    _store_inputs=True,

# ==================================================
# Line: 1120

def trace_module(
    mod,
    inputs,
    optimize=None,
    check_trace=True,
    check_inputs=None,
    check_tolerance=1e-5,
    strict=True,
    _force_outplace=False,
    _module_class=None,
    _compilation_unit=_python_cu,
    example_inputs_is_kwarg=False,
    _store_inputs=True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/triton_kernel_wrap.py
# Line: 874

def __call__(
    self,
    kernel_idx: int,
    constant_args_idx: int,
    grid: list["TritonGridType"],
    tma_descriptor_metadata: TMADescriptorMetadata,
    kwargs: dict[str, Any],
    tensors_to_clone: list[str],

# ==================================================
# Line: 1116

def triton_kernel_wrapper_functional_fake_tensor_mode(
    mode: FakeTensorMode,
    *,
    kernel_idx: int,
    constant_args_idx: int,
    grid: list["TritonGridType"],
    tma_descriptor_metadata: TMADescriptorMetadata,
    kwargs: dict[str, Any],
    tensors_to_clone: list[str],

# ==================================================
# Line: 1139

def triton_kernel_wrapper_functional_proxy_torch_dispatch_mode(
    mode: ProxyTorchDispatchMode,
    *,
    kernel_idx: int,
    constant_args_idx: int,
    grid: list["TritonGridType"],
    tma_descriptor_metadata: TMADescriptorMetadata,
    kwargs: dict[str, Any],
    tensors_to_clone: list[str],

# ==================================================
# Line: 1166

def triton_kernel_wrapper_functional_functionalize(
    ctx: "BaseFunctionalizeAPI",
    kernel_idx: int,
    constant_args_idx: int,
    grid: list["TritonGridType"],
    tma_descriptor_metadata: TMADescriptorMetadata,
    kwargs: dict[str, Any],
    tensors_to_clone: list[str],

# ==================================================
# Line: 1282

def do_prune_configs(  # type: ignore[no-untyped-def]
    autotuner: "TritonAutotunerType",
    early_config_prune: Optional[Callable],
    perf_model: Optional[Callable],
    top_k: float,
    configs: list,
    named_args: dict,
    kwargs: dict,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/flex_attention.py
# Line: 81

def __call__(
    self,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 114

def __call__(
    self,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    grad_out: torch.Tensor,
    grad_logsumexp: torch.Tensor,
    fw_graph: Union[Callable, GraphModule],
    joint_graph: GraphModule,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 155

def _math_attention_inner(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 198

def math_attention(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 257

def sdpa_dense(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 283

def trace_flex_attention(
    proxy_mode: ProxyTorchDispatchMode,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 353

def flex_attention_proxy_torch_dispatch_mode(
    mode: ProxyTorchDispatchMode,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 381

def flex_attention_functionalize(
    ctx: torch._subclasses.functional_tensor.BaseFunctionalizeAPI,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 469

def flex_attention_fake_tensor_mode(
    mode: FakeTensorMode,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 592

def forward(
    ctx: Any,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    fw_graph: Callable,
    joint_graph: Callable,
    block_mask: tuple[Any, ...],
    scale: float,
    kernel_options: dict[str, Any],
    mask_mod_other_buffers: tuple[Any, ...],
    *score_mod_other_buffers: tuple[Any, ...],

# ==================================================
# Line: 724

def flex_attention_autograd(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple[Tensor, ...] = (),
    mask_mod_other_buffers: tuple[Tensor, ...] = (),

# ==================================================
# Line: 774

def sdpa_dense_backward(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    grad_out: torch.Tensor,
    grad_logsumexp: torch.Tensor,
    fw_graph: Callable,  # GraphModule type hint?
    joint_graph: Callable,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple,
    mask_mod_other_buffers: tuple,

# ==================================================
# Line: 938

def trace_flex_attention_backward(
    proxy_mode: ProxyTorchDispatchMode,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    grad_out: torch.Tensor,
    grad_logsumexp: torch.Tensor,
    fw_graph: Union[Callable, GraphModule],
    joint_graph: GraphModule,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 1035

def flex_attention_backward_proxy_torch_dispatch_mode(
    mode: ProxyTorchDispatchMode,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    grad_out: torch.Tensor,
    grad_logsumexp: torch.Tensor,
    fw_graph: Union[Callable, GraphModule],
    joint_graph: GraphModule,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 1075

def flex_attention_backward_functionalize(
    ctx: torch._subclasses.functional_tensor.BaseFunctionalizeAPI,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    grad_out: torch.Tensor,
    grad_logsumexp: torch.Tensor,
    fw_graph: Union[Callable, GraphModule],
    joint_graph: GraphModule,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# Line: 1153

def flex_attention_backward_fake_tensor_mode(
    mode: FakeTensorMode,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    grad_out: torch.Tensor,
    grad_logsumexp: torch.Tensor,
    fw_graph: Union[Callable, GraphModule],
    joint_graph: GraphModule,
    block_mask: tuple,
    scale: float,
    kernel_options: dict[str, Any],
    score_mod_other_buffers: tuple = (),
    mask_mod_other_buffers: tuple = (),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/__init__.py
# Line: 2455

def compile(
    model: _Callable[_InputT, _RetT],
    *,
    fullgraph: builtins.bool = False,
    dynamic: _Optional[builtins.bool] = None,
    backend: _Union[str, _Callable] = "inductor",
    mode: _Union[str, None] = None,
    options: _Optional[
        dict[str, _Union[str, builtins.int, builtins.bool, _Callable]]
    ] = None,
    disable: builtins.bool = False,

# ==================================================
# Line: 2470

def compile(
    model: None = None,
    *,
    fullgraph: builtins.bool = False,
    dynamic: _Optional[builtins.bool] = None,
    backend: _Union[str, _Callable] = "inductor",
    mode: _Union[str, None] = None,
    options: _Optional[
        dict[str, _Union[str, builtins.int, builtins.bool, _Callable]]
    ] = None,
    disable: builtins.bool = False,

# ==================================================
# Line: 2484

def compile(
    model: _Optional[_Callable[_InputT, _RetT]] = None,
    *,
    fullgraph: builtins.bool = False,
    dynamic: _Optional[builtins.bool] = None,
    backend: _Union[str, _Callable] = "inductor",
    mode: _Union[str, None] = None,
    options: _Optional[
        dict[str, _Union[str, builtins.int, builtins.bool, _Callable]]
    ] = None,
    disable: builtins.bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/xeon/run_cpu.py
# Line: 400

def set_multi_thread_and_allocator(
    self,
    ncores_per_instance,
    disable_iomp=False,
    set_kmp_affinity=True,
    enable_tcmalloc=True,
    enable_jemalloc=False,
    use_default_allocator=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/_nnapi/serializer.py
# Line: 2064

def add_conv2d_common(
    self,
    jit_out,
    out_scale,
    out_zero_point,
    jit_image,
    weight_tensor,
    bias_id,
    args,
    transpose,
    fuse_code,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/_nnapi/prepare.py
# Line: 27

def __init__(
    self,
    shape_compute_module: torch.nn.Module,
    ser_model: torch.Tensor,
    weights: list[torch.Tensor],
    inp_mem_fmts: list[int],
    out_mem_fmts: list[int],
    compilation_preference: int,
    relax_f32_to_f16: bool,

# ==================================================
# Line: 97

def convert_model_to_nnapi(
    model,
    inputs,
    serializer=None,
    return_shapes=None,
    use_int16_for_qint16=False,
    compilation_preference=ANEURALNETWORKS_PREFER_SUSTAINED_SPEED,
    relax_f32_to_f16=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/sparse/_triton_ops.py
# Line: 500

def scatter_mm_meta(
    M,
    K,
    N,
    Ms,
    Ks,
    GROUP_SIZE=None,
    TILE_M=None,
    TILE_N=None,
    SPLIT_N=None,
    num_warps=None,
    num_stages=None,
    **extra,

# ==================================================
# Line: 738

def bsr_dense_addmm_meta(
    M,
    K,
    N,
    Ms,
    Ks,
    beta,
    alpha,
    SPLIT_N=None,
    GROUP_SIZE_ROW=None,
    num_warps=None,
    num_stages=None,
    sparsity=None,
    dtype=None,
    out_dtype=None,
    _version=0,
    **extra,

# ==================================================
# Line: 916

def _bsr_scatter_mm_indices_data(
    indices_format, M, K, N, Ms, Ks, nbatches, SPLIT_N, compressed_sparse_tensor_as_key

# ==================================================
# Line: 1116

def _int_bsr_dense_addmm(
    input: torch.Tensor,
    bsr: torch.Tensor,
    dense: torch.Tensor,
    *,
    beta=1,
    alpha=1,
    left_alpha: Optional[torch.Tensor] = None,
    right_alpha: Optional[torch.Tensor] = None,
    out: Optional[torch.Tensor] = None,
    skip_checks: bool = False,
    max_grid: Optional[tuple[Optional[int], Optional[int], Optional[int]]] = None,
    meta: Optional[dict] = None,

# ==================================================
# Line: 1157

def bsr_dense_addmm(
    input: torch.Tensor,
    bsr: torch.Tensor,
    dense: torch.Tensor,
    *,
    beta=1,
    alpha=1,
    left_alpha: Optional[torch.Tensor] = None,
    right_alpha: Optional[torch.Tensor] = None,
    out: Optional[torch.Tensor] = None,
    skip_checks: bool = False,
    max_grid: Optional[tuple[Optional[int], Optional[int], Optional[int]]] = None,
    meta: Optional[dict] = None,

# ==================================================
# Line: 1331

def _sampled_addmm_kernel(
    alpha,
    beta,
    IS_BETA_ZERO: tl.constexpr,
    BLOCKSIZE_ROW: tl.constexpr,
    BLOCKSIZE_COL: tl.constexpr,
    k,
    TILE_K: tl.constexpr,
    values_ptr,
    values_batch_stride,
    values_nnz_stride,
    values_row_block_stride,
    values_col_block_stride,
    crow_indices_ptr,
    crow_indices_batch_stride,
    crow_indices_stride,
    col_indices_ptr,
    col_indices_batch_stride,
    col_indices_stride,
    mat1_ptr,
    mat1_batch_stride,
    mat1_tiled_row_stride,
    mat1_tiled_col_stride,
    mat1_row_block_stride,
    mat1_col_block_stride,
    mat2_ptr,
    mat2_batch_stride,
    mat2_tiled_row_stride,
    mat2_tiled_col_stride,
    mat2_row_block_stride,
    mat2_col_block_stride,
    acc_dtype: tl.constexpr,
    allow_tf32: tl.constexpr,

# ==================================================
# Line: 1457

def _bsr_strided_dense_rowspace_kernel(
    # values prologue
    values_ptr,
    values_batch_stride,
    values_nnz_stride,
    values_row_block_stride,
    values_col_block_stride,
    # values epilogue
    # crow_indices prologue
    crow_indices_ptr,
    crow_indices_batch_stride,
    crow_indices_stride,
    # crow_indices epilogue
    # col_indices prologue
    col_indices_ptr,
    col_indices_batch_stride,
    col_indices_stride,
    # col_indices epilogue
    # dense prologue
    dense_ptr,
    dense_batch_stride,
    dense_tiled_row_stride,
    dense_tiled_col_stride,
    dense_row_block_stride,
    dense_col_block_stride,
    # dense epilogue
    # output prologue
    output_ptr,
    output_batch_stride,
    output_tiled_row_stride,
    output_tiled_col_stride,
    output_row_block_stride,
    output_col_block_stride,
    # output epilogue
    #
    # gh-113754: Always keep all constexpr arguments at the end of
    # triton kernel arguments list because with triton 2.1 or
    # earlier non-contiguous outputs will corrupt CUDA state due
    # to a triton bug (fixed in openai/triton#2262).
    BLOCKSIZE_ROW: tl.constexpr,
    BLOCKSIZE_COL: tl.constexpr,
    acc_dtype: tl.constexpr,
    allow_tf32: tl.constexpr,
    GROUP_SIZE_ROW: tl.constexpr,

# ==================================================
# Line: 1588

def _run_sampled_addmm_kernel(
    alpha,
    beta,
    is_beta_zero,
    blocksize,
    k,
    tile_k,
    values,
    crow_indices,
    col_indices,
    mat1,
    mat2,
    max_grid,

# ==================================================
# Line: 1641

def sampled_addmm(
    input: torch.Tensor,
    mat1: torch.Tensor,
    mat2: torch.Tensor,
    *,
    beta=1.0,
    alpha=1.0,
    out: Optional[torch.Tensor] = None,
    skip_checks: bool = False,
    max_grid: Optional[tuple[Optional[int], Optional[int], Optional[int]]] = None,

# ==================================================
# Line: 1784

def _bsr_softmax_kernel(
    crow_indices_ptr,
    crow_indices_batch_stride,
    crow_indices_stride,
    values_ptr,
    values_batch_stride,
    values_row_block_stride,
    values_nnz_col_block_stride,
    row_block,
    col_block,
    MAX_ROW_NNZ: tl.constexpr,
    TILE: tl.constexpr,

# ==================================================
# Line: 1943

def _scaled_dot_product_attention(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attn_mask: Optional[torch.Tensor],
    dropout_p: float = 0.0,
    is_causal: bool = False,
    scale: Optional[float] = None,

# ==================================================
# Line: 1990

def _scatter_mm2_kernel(
    M: tl.constexpr,
    K: tl.constexpr,
    N: tl.constexpr,
    blocks_ptr,
    blocks_stride_P,
    blocks_stride_M,
    blocks_stride_K,
    others_ptr,
    others_stride_Q,
    others_stride_K,
    others_stride_N,
    accumulators_ptr,
    accumulators_stride_R,
    accumulators_stride_M,
    accumulators_stride_N,
    pq_offsets_ptr,
    pq_offsets_stride,
    pq_ptr,
    pq_stride_T,
    pq_stride_1,
    dot_out_dtype: tl.constexpr,
    TILE_M: tl.constexpr,
    TILE_N: tl.constexpr,
    allow_tf32: tl.constexpr,

# ==================================================
# Line: 2115

def _scatter_mm6_kernel(
    nbatches,
    Ms,
    Ks: tl.constexpr,
    N,
    blocks_ptr,
    blocks_stride_P,
    blocks_stride_M,
    blocks_stride_K,
    others_ptr,
    others_stride_B,
    others_stride_K,
    others_stride_N,
    accumulators_ptr,
    accumulators_stride_B,
    accumulators_stride_M,
    accumulators_stride_N,
    c_indices_ptr,
    r_offsets_ptr,
    p_offsets_ptr,
    q_offsets_ptr,
    is_compressed: tl.constexpr,
    dot_out_dtype: tl.constexpr,
    SPLIT_N: tl.constexpr,
    TILE_M: tl.constexpr,
    TILE_N: tl.constexpr,
    GROUP_SIZE: tl.constexpr,
    allow_tf32: tl.constexpr,

# ==================================================
# Line: 2228

def _scatter_mm6(
    blocks: torch.Tensor,
    others: torch.Tensor,
    c_indices: torch.Tensor,
    r_offsets: torch.Tensor,
    p_offsets: torch.Tensor,
    q_offsets: torch.Tensor,
    meta: dict,
    accumulators: torch.Tensor,
    force_contiguous: bool = True,

# ==================================================
# Line: 2319

def _bsr_strided_addmm_kernel(
    # values prologue
    values_ptr,
    values_batch_stride,
    values_nnz_stride,
    values_row_block_stride,
    values_col_block_stride,
    # values epilogue
    # crow_indices prologue
    crow_indices_ptr,
    crow_indices_batch_stride,
    crow_indices_stride,
    # crow_indices epilogue
    # col_indices prologue
    col_indices_ptr,
    col_indices_batch_stride,
    col_indices_stride,
    # col_indices epilogue
    # input prologue
    input_ptr,
    input_batch_stride,
    input_tiled_row_stride,
    input_tiled_col_stride,
    input_row_block_stride,
    input_col_block_stride,
    # input epilogue
    # dense prologue
    dense_ptr,
    dense_batch_stride,
    dense_tiled_row_stride,
    dense_tiled_col_stride,
    dense_row_block_stride,
    dense_col_block_stride,
    # dense epilogue
    # left_alpha prologue
    left_alpha_ptr,
    left_alpha_batch_stride,
    left_alpha_tiled_row_stride,
    left_alpha_tiled_col_stride: tl.constexpr,
    left_alpha_row_block_stride,
    left_alpha_col_block_stride: tl.constexpr,
    # left_alpha epilogue
    # right_alpha prologue
    right_alpha_ptr,
    right_alpha_batch_stride,
    right_alpha_tiled_row_stride: tl.constexpr,
    right_alpha_tiled_col_stride,
    right_alpha_row_block_stride: tl.constexpr,
    right_alpha_col_block_stride,
    # right_alpha epilogue
    # output prologue
    output_ptr,
    output_batch_stride,
    output_tiled_row_stride,
    output_tiled_col_stride,
    output_row_block_stride,
    output_col_block_stride,
    # output epilogue
    beta,
    alpha,
    beta_is_one: tl.constexpr,
    beta_is_nonzero: tl.constexpr,
    alpha_is_one: tl.constexpr,
    left_alpha_is_one: tl.constexpr,
    right_alpha_is_one: tl.constexpr,
    BLOCKSIZE_ROW: tl.constexpr,
    BLOCKSIZE_COL: tl.constexpr,
    BLOCKSIZE_INNER: tl.constexpr,
    acc_dtype: tl.constexpr,
    allow_tf32: tl.constexpr,
    GROUP_SIZE_ROW: tl.constexpr,
    SPLIT_N: tl.constexpr,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/sparse/_triton_ops_meta.py
# Line: 245

def minimize(
    target_func,
    initial_parameters,
    reference_parameters,
    step_func,
    max_step=2,
    verbose=False,
    all_values=None,

# ==================================================
# Line: 434

def create_blocked_tensor(B, M, N, blocksize, sparsity, dtype, device):
    assert (
        sparsity <= 1.0 and sparsity >= 0.0
    ), "sparsity should be a value between 0 and 1"
    assert M % blocksize[0] == 0
    assert N % blocksize[1] == 0
    shape = (B, M // blocksize[0], N // blocksize[1])[int(B == 0) :]
    A = torch.bernoulli(
        torch.full(shape, 1 - sparsity, dtype=torch.float32, device=device)
    ).to(dtype)
    expected_nnz = int((1 - sparsity) * M * N / (blocksize[0] * blocksize[1]))
    nonzero_indices = A.flatten().nonzero()
    actual_nnz = nonzero_indices.shape[0]
    if actual_nnz > expected_nnz:
        selected_nonzeros = torch.randperm(actual_nnz)[: actual_nnz - expected_nnz]
        A.flatten()[nonzero_indices[selected_nonzeros]] = 0
    elif actual_nnz < expected_nnz:
        zero_indices = (A == 0).flatten().nonzero()
        selected_zeros = torch.randperm(zero_indices.shape[0])[
            : expected_nnz - actual_nnz
        ]
        A.flatten()[zero_indices[selected_zeros]] = 1
    A = torch.repeat_interleave(A, blocksize[0], dim=-2)
    A = torch.repeat_interleave(A, blocksize[1], dim=-1)
    return A



# ==================================================
# Line: 461

def optimize_scatter_mm(
    m, k, n, bm, bk, dtype=torch.float16, device="cuda", sparsity=0.5, force=False

# ==================================================
# Line: 516

def step_meta_parameter(name, value, direction, meta, m=m, n=n, k=k, bm=bm, bk=bk):
    # return next value in positive or negative direction, or
    # input value if the step will result an invalid
    # value. The input value is assumed to be valid.

    is_log = name in {"SPLIT_N", "TILE_M", "TILE_N", "num_warps"}
    min_value = dict(
        SPLIT_N=1, TILE_M=16, TILE_N=16, num_warps=1, num_stages=1, GROUP_SIZE=1
    )[name]
    max_value = dict(
        SPLIT_N=n // meta["TILE_N"], TILE_M=bm, TILE_N=n // meta["SPLIT_N"]
    ).get(name)
    value_step = dict(
        SPLIT_N=2, TILE_M=2, TILE_N=2, num_warps=2, num_stages=1, GROUP_SIZE=1
    )[name]
    if is_log:
        next_value = (
            value * value_step**direction
            if direction > 0
            else value // (value_step ** abs(direction))
        )
    else:
        next_value = value + value_step * direction
    if min_value is not None:
        next_value = max(next_value, min_value)
    if max_value is not None:
        next_value = min(next_value, max_value)
    if name == "SPLIT_N" and n % next_value != 0:
        return value
    # Hard-skip parameter combinations that break CUDA state for pytorch:
    if (dtype, name, next_value, m, n, k, bm, bk) in {
        (torch.float32, "num_warps", 32, 256, 256, 256, 16, 16),
        (torch.float32, "num_warps", 16, 256, 256, 256, 32, 32),
        (torch.float32, "num_warps", 16, 256, 256, 256, 64, 64),
        (torch.float32, "num_warps", 16, 256, 256, 256, 128, 128),
        (torch.float32, "num_warps", 16, 512, 512, 256, 128, 128),
    } and re.match(r"NVIDIA A100[^\d]", device_name) is not None:
        return value
    return next_value


# ==================================================
# Line: 571

def tune__int_bsr_dense_addmm(
    input,
    bsr,
    dense,
    *,
    beta=1,
    alpha=1,
    out=None,
    store=False,
    verbose=False,
    force=False,

# ==================================================
# Line: 597

def tune_bsr_dense_addmm(
    input,
    bsr,
    dense,
    *,
    beta=1,
    alpha=1,
    left_alpha=None,
    right_alpha=None,
    out=None,
    store=False,
    verbose=False,
    force=False,
    opname=None,

# ==================================================
# Line: 687

def step_meta_parameter(name, value, direction, meta, M=M, N=N, K=K, BM=BM, BK=BK):
    # return next value in positive or negative direction, or
    # input value if the step will result an invalid
    # value. The input value is assumed to be valid.
    is_log = name in {"SPLIT_N", "num_warps"}
    min_value = dict(SPLIT_N=1, num_warps=1, num_stages=1, GROUP_SIZE_ROW=1)[name]
    max_value = dict(SPLIT_N=max(N // BM, 1)).get(name)
    value_step = dict(SPLIT_N=2, num_warps=2, num_stages=1, GROUP_SIZE_ROW=1)[name]
    if is_log:
        next_value = (
            value * value_step**direction
            if direction > 0
            else value // (value_step ** abs(direction))
        )
    else:
        next_value = value + value_step * direction
    if min_value is not None:
        next_value = max(next_value, min_value)
    if max_value is not None:
        next_value = min(next_value, max_value)
    if name == "SPLIT_N" and N % next_value != 0:
        return value
    return next_value


# ==================================================
# Line: 738

def optimize_bsr_dense_addmm(
    m,
    k,
    n,
    bm,
    bk,
    beta=1,
    alpha=1,
    use_left_alpha=False,
    use_right_alpha=False,
    dtype=torch.float16,
    out_dtype=None,
    device="cuda",
    sparsity=0.5,
    force=False,
    verbose=False,
    opname=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/sparse/semi_structured.py
# Line: 76

def __new__(  # noqa: PYI034
    cls,
    shape: torch.Size,
    packed: Optional[torch.Tensor],
    meta: Optional[torch.Tensor],
    packed_t: Optional[torch.Tensor],
    meta_t: Optional[torch.Tensor],
    compressed_swizzled_bitmask: Optional[torch.Tensor],
    fuse_transpose_cusparselt: bool = False,
    alg_id_cusparselt: int = 0,
    requires_grad: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/__init__.py
# Line: 365

def grad(
    outputs: _TensorOrTensorsOrGradEdge,
    inputs: _TensorOrTensorsOrGradEdge,
    grad_outputs: Optional[_TensorOrTensors] = None,
    retain_graph: Optional[bool] = None,
    create_graph: bool = False,
    only_inputs: bool = True,
    allow_unused: Optional[bool] = None,
    is_grads_batched: bool = False,
    materialize_grads: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler_util.py
# Line: 167

def table(
    self,
    sort_by=None,
    row_limit=100,
    max_src_column_width=75,
    max_name_column_width=55,
    max_shapes_column_width=80,
    header=None,
    top_level_events_only=False,

# ==================================================
# Line: 462

def __init__(
    self,
    id,
    name,
    thread,
    start_us,
    end_us,
    overload_name=None,
    fwd_thread=None,
    input_shapes=None,
    stack=None,
    scope=0,
    use_device=None,
    cpu_memory_usage=0,
    device_memory_usage=0,
    is_async=False,
    is_remote=False,
    sequence_nr=-1,
    node_id=-1,
    device_type=DeviceType.CPU,
    device_index=0,
    device_resource_id=None,
    is_legacy=False,
    flops=None,
    trace_name=None,
    concrete_inputs=None,
    kwinputs=None,
    is_user_annotation=False,

# ==================================================
# Line: 824

def _build_table(
    events,
    sort_by=None,
    header=None,
    row_limit=100,
    max_src_column_width=75,
    max_name_column_width=55,
    max_shapes_column_width=80,
    with_flops=False,
    profile_memory=False,
    top_level_events_only=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler_legacy.py
# Line: 36

def __init__(
    self,
    enabled=True,
    *,
    use_cuda=False,
    record_shapes=False,
    with_flops=False,
    profile_memory=False,
    with_stack=False,
    with_modules=False,

# ==================================================
# Line: 127

def table(
    self,
    sort_by=None,
    row_limit=100,
    max_src_column_width=75,
    max_name_column_width=55,
    max_shapes_column_width=80,
    header=None,
    top_level_events_only=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler.py
# Line: 199

def __init__(
    self,
    enabled=True,
    *,
    use_cuda=False,  # Deprecated
    use_device=None,
    record_shapes=False,
    with_flops=False,
    profile_memory=False,
    with_stack=False,
    with_modules=False,
    use_kineto=False,
    use_cpu=True,
    experimental_config=None,
    acc_events=False,
    custom_trace_id_callback=None,

# ==================================================
# Line: 460

def table(
    self,
    sort_by=None,
    row_limit=100,
    max_src_column_width=75,
    max_name_column_width=55,
    max_shapes_column_width=80,
    header=None,
    top_level_events_only=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/gradcheck.py
# Line: 469

def get_numerical_jacobian_wrt_specific_input(
    fn, input_idx, inputs, outputs, eps, input=None, is_forward_ad=False

# ==================================================
# Line: 676

def _get_numerical_vJu(
    fn, inputs, inp_indices, func_out, all_u, all_v, eps, is_forward_ad

# ==================================================
# Line: 990

def _check_no_differentiable_outputs_fast(
    func, func_out, all_inputs, inputs_indices, all_u, eps, nondet_tol

# ==================================================
# Line: 1376

def _get_notallclose_msg(
    analytical,
    numerical,
    output_idx,
    input_idx,
    complex_indices,
    test_imag=False,
    is_forward_ad=False,

# ==================================================
# Line: 1443

def _gradcheck_real_imag(
    gradcheck_fn,
    func,
    func_out,
    tupled_inputs,
    outputs,
    eps,
    rtol,
    atol,
    check_grad_dtypes,
    check_forward_ad,
    check_backward_ad,
    nondet_tol,
    check_undefined_grad,

# ==================================================
# Line: 1578

def _slow_gradcheck(
    func,
    func_out,
    tupled_inputs,
    outputs,
    eps,
    rtol,
    atol,
    check_grad_dtypes,
    nondet_tol,
    *,
    use_forward_ad=False,
    complex_indices=None,
    test_imag=False,
    masked=False,

# ==================================================
# Line: 1751

def _run_slow_mode_and_get_error(
    func, tupled_inputs, outputs, input_idx, output_idx, rtol, atol, eps, is_forward_ad

# ==================================================
# Line: 1829

def _check_analytical_numerical_equal(
    all_analytical,
    all_numerical,
    complex_indices,
    tupled_inputs,
    outputs,
    func,
    all_v,
    all_u,
    rtol,
    atol,
    eps,
    test_imag,
    *,
    is_forward_ad=False,

# ==================================================
# Line: 1866

def _fast_gradcheck(
    func,
    func_out,
    inputs,
    outputs,
    eps,
    rtol,
    atol,
    check_grad_dtypes,
    nondet_tol,
    *,
    use_forward_ad=False,
    complex_indices=None,
    test_imag=False,
    masked=False,

# ==================================================
# Line: 1954

def gradcheck(
    func: Callable[..., Union[_TensorOrTensors]],  # See Note [VarArg of Tensors]
    inputs: _TensorOrTensors,
    *,
    eps: float = 1e-6,
    atol: float = 1e-5,
    rtol: float = 1e-3,
    raise_exception: bool = True,
    nondet_tol: float = 0.0,
    check_undefined_grad: bool = True,
    check_grad_dtypes: bool = False,
    check_batched_grad: bool = False,
    check_batched_forward_grad: bool = False,
    check_forward_ad: bool = False,
    check_backward_ad: bool = True,
    fast_mode: bool = False,
    masked: Optional[bool] = None,

# ==================================================
# Line: 2059

def _gradcheck_helper(
    func,
    inputs,
    eps,
    atol,
    rtol,
    nondet_tol,
    check_undefined_grad,
    check_grad_dtypes,
    check_batched_grad,
    check_batched_forward_grad,
    check_forward_ad,
    check_backward_ad,
    fast_mode,
    masked,

# ==================================================
# Line: 2119

def gradgradcheck(
    func: Callable[..., _TensorOrTensors],  # See Note [VarArg of Tensors]
    inputs: _TensorOrTensors,
    grad_outputs: Optional[_TensorOrTensors] = None,
    *,
    eps: float = 1e-6,
    atol: float = 1e-5,
    rtol: float = 1e-3,
    gen_non_contig_grad_outputs: bool = False,
    raise_exception: bool = True,
    nondet_tol: float = 0.0,
    check_undefined_grad: bool = True,
    check_grad_dtypes: bool = False,
    check_batched_grad: bool = False,
    check_fwd_over_rev: bool = False,
    check_rev_over_rev: bool = True,
    fast_mode: bool = False,
    masked: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/non_strict_utils.py
# Line: 481

def _constrain_user_specified_dimhint_range(
    symint: torch.SymInt,
    hint: int,
    dim: _DimHint,
    range_constraints,
    shape_env,
    keypath: KeyPath,
    i: Optional[int] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/__init__.py
# Line: 76

def aot_compile(
    f: Callable,
    args: tuple[Any],
    kwargs: Optional[dict[str, Any]] = None,
    *,
    dynamic_shapes: Optional[dict[str, Any]] = None,
    options: Optional[dict[str, Any]] = None,
    remove_runtime_assertions: bool = False,
    disable_constraint_solver: bool = False,
    same_signature: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/utils.py
# Line: 441

def register_dataclass_as_pytree_node(
    cls: type[Any],
    flatten_fn: Optional[FlattenFunc] = None,
    unflatten_fn: Optional[UnflattenFunc] = None,
    *,
    serialized_type_name: Optional[str] = None,
    to_dumpable_context: Optional[ToDumpableContextFn] = None,
    from_dumpable_context: Optional[FromDumpableContextFn] = None,
    return_none_fields: bool = False,

# ==================================================
# Line: 909

def placeholder_naming_pass(
    gm: torch.fx.GraphModule,
    export_graph_signature: "ExportGraphSignature",
    mod: torch.nn.Module,
    fake_args,
    fake_kwargs,
    fake_params_buffers,
    constants: dict[str, Any],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/converter.py
# Line: 393

def __init__(
    self,
    ts_graph: Union[torch._C.Graph, torch._C.Block],
    name_to_param: dict[str, torch.Tensor],
    name_to_buffer: dict[str, torch.Tensor],
    blocks_to_lifted_attrs: dict[torch._C.Block, set[str]],
    name_to_non_tensor_attribute: dict[str, Any],
    name_to_constant: dict[str, Any],
    name_to_attribute_fqn: dict[str, str],

# ==================================================
# Line: 1333

def __init__(
    self,
    ts_graph: Union[torch._C.Graph, torch._C.Block],
    name_to_param: dict[str, torch.Tensor],
    name_to_buffer: dict[str, torch.Tensor],
    blocks_to_lifted_attrs: dict[torch._C.Block, set[str]],
    name_to_non_tensor_attribute: dict[str, Any],
    name_to_constant: dict[str, Any],
    name_to_attribute_fqn: dict[str, str],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/passes/replace_quantized_ops_with_standard_ops_pass.py
# Line: 43

def insert_quantized_node(
    gm: torch.fx.GraphModule,
    val_node: torch.fx.Node,
    scale_node: Union[float, torch.fx.Node],
    zero_point_node: Union[float, torch.fx.Node],
    qmin_node: Union[float, int, torch.fx.Node],
    qmax_node: Union[float, int, torch.fx.Node],
    dtype_node: Union[torch.dtype, torch.fx.Node],
    qscheme: Optional[torch.qscheme],

# ==================================================
# Line: 66

def get_dequantized(
    val: torch.Tensor,
    scale: Union[float, torch.Tensor],
    zero_point: Union[float, torch.Tensor],
    qmin: Union[float, int],
    qmax: Union[float, int],
    dtype: torch.dtype,
    axis: Optional[int],
    qscheme: Optional[torch.qscheme],

# ==================================================
# Line: 99

def insert_dequantized_node(
    gm: torch.fx.GraphModule,
    val_node: torch.fx.Node,
    scale_node: Union[float, torch.fx.Node],
    zero_point_node: Union[float, torch.fx.Node],
    qmin_node: Union[float, int, torch.fx.Node],
    qmax_node: Union[float, int, torch.fx.Node],
    dtype_node: Union[torch.dtype, torch.fx.Node],
    axis_node: Optional[Union[int, torch.fx.Node]],
    qscheme: Optional[torch.qscheme],

# ==================================================
# Line: 268

def _conv1d_op_with_squeeze(
    inp: torch.Tensor,
    weight: torch.Tensor,
    bias: Optional[torch.Tensor],
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    groups: int,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/ops_handler.py
# Line: 276

def bucketize(
    self,
    values: T,
    boundaries: tuple[str, sympy.Expr, sympy.Expr, sympy.Expr],
    boundary_indices: T,
    indexing_dtype: torch.dtype,
    right: bool,
    sorter: Optional[tuple[str, sympy.Expr]] = None,
    sorter_indices: Optional[T] = None,

# ==================================================
# Line: 1071

def bucketize(
    self,
    values: T,
    boundaries: tuple[str, sympy.Expr, sympy.Expr, sympy.Expr],
    boundary_indices: T,
    indexing_dtype: torch.dtype,
    right: bool,
    sorter: Optional[tuple[str, sympy.Expr]] = None,
    sorter_indices: Optional[T] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/__init__.py
# Line: 158

def _aoti_compile_and_package_inner(
    gm: torch.nn.Module,
    # flat_example_inputs: List[Any],
    args: tuple[Any],
    kwargs: Optional[dict[str, Any]] = None,
    *,
    load_and_run: bool = False,
    check_accuracy: Optional[str] = None,
    package_path: Optional[Union[str, io.BytesIO]] = None,
    inductor_configs: Optional[dict[str, Any]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codecache.py
# Line: 1449

def load_with_key(
    key: str,
    debug_lines: list[str],
    example_inputs: Sequence[InputType],
    local: bool,
    remote_cache: Optional[RemoteCache[JsonDataTy]],
    is_backward: bool,
    constants: CompiledFxGraphConstants,
    evaluate_guards: Optional[
        Callable[[str, Union[list[int], list[torch.SymInt]]], bool]
    ] = None,

# ==================================================
# Line: 1549

def set(
    cls,
    key: str,
    params: dict[str, Optional[str]],
    cubin: str,
    bin_type: str,
    asm: Optional[str] = None,
    asm_type: Optional[str] = None,

# ==================================================
# Line: 1623

def compile(
    cls,
    graph: GraphLowering,
    wrapper_code: str,
    kernel_code: str,
    serialized_extern_kernel_nodes: Optional[str],
    *,
    device_type: str,
    additional_files: list[str],

# ==================================================
# Line: 2663

def load_pybinding_async(
    cls,
    argtypes: Sequence[str],
    main_code: str,
    device_type: str = "cpu",
    num_outputs: int = -1,
    submit_fn: Any = None,
    extra_flags: Sequence[str] = (),
    kernel_code: Optional[str] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/utils.py
# Line: 1777

def use_cpp_gemm_template(
    layout: Layout,
    mat1: IRNode,
    mat2: IRNode,
    mat2_transposed: bool = False,
    require_constant_mat2: bool = True,
    is_woq_int4: bool = False,
    q_group_size: Optional[int] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fuzzer.py
# Line: 576

def __init__(
    self,
    config_module: ConfigModule,
    test_model_fn_factory: FactoryType,
    seed: int,
    default: Optional[ConfigType] = None,
    sm: SamplingMethod = SamplingMethod.TOGGLE,
    test_timeout: int = 3600,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/mm.py
# Line: 1022

def tuned_scaled_mm(
    mat_a,
    mat_b,
    scale_a,
    scale_b,
    bias=None,
    scale_result=None,
    out_dtype=None,
    use_fast_accum=False,
    layout=None,

# ==================================================
# Line: 1184

def mm_autoheuristic(
    mat1,
    mat2,
    m,
    n,
    k,
    choices,
    name,
    input_nodes,
    ops,
    precondition,
    top_k: Optional[int] = None,
    always_included=None,

# ==================================================
# Line: 1203

def get_context(m, k, n, mat1, mat2, mat1_stride, mat2_stride):
    context = AHContext()
    context.add_feature("m", m)
    context.add_feature("k", k)
    context.add_feature("n", n)
    context.add_feature("mat1_dtype", mat1.layout.dtype, is_categorical=True)
    context.add_feature("mat2_dtype", mat2.layout.dtype, is_categorical=True)
    context_add_strides(context, "mat1", mat1_stride)
    context_add_strides(context, "mat2", mat2_stride)
    context.add_feature(
        "mat1_iscontig", mat1.layout.is_contiguous(), is_categorical=True
    )
    context.add_feature(
        "mat2_iscontig", mat2.layout.is_contiguous(), is_categorical=True
    )
    if name == "mm":
        context_add_using_tf32(context, mat1.layout.dtype)
    return context


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/mm_scaled_grouped.py
# Line: 392

def tuned_scaled_grouped_mm(
    mat_a: TensorBox,
    mat_b: TensorBox,
    scale_a: TensorBox,
    scale_b: TensorBox,
    offs: Optional[TensorBox] = None,
    bias: Optional[TensorBox] = None,
    scale_result: Optional[TensorBox] = None,
    out_dtype: Optional[torch.dtype] = None,
    use_fast_accum: bool = False,
    layout: Optional[Layout] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/mm_common.py
# Line: 90

def scaled_mm_options(  # type: ignore[no-untyped-def]
    config,  # triton.Config
    sym_m: sympy.core.numbers.Integer,
    sym_n: sympy.core.numbers.Integer,
    sym_k: sympy.core.numbers.Integer,
    layout: Layout,
    scale_a,
    scale_b,
    use_fast_accum: bool,
    device_tma: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/flex_attention.py
# Line: 1052

def lower_cpu(
    query,
    key,
    value,
    subgraph,
    block_mask,
    scale,
    kernel_options,
    score_mod_other_buffers,
    mask_mod_other_buffers,

# ==================================================
# Line: 1395

def flex_attention(
    query,
    key,
    value,
    subgraph,
    block_mask,
    scale,
    kernel_options,
    score_mod_other_buffers,
    mask_mod_other_buffers,

# ==================================================
# Line: 1738

def flex_attention_backward_grid(
    batch_size, q_heads, num_queries, d_model, kv_heads, num_key_value, meta

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/kernel/conv.py
# Line: 56

def conv3d_grid(n, c, d, h, w, meta, *, cdiv):
    return (
        cdiv(n * d * h * w, meta["BLOCK_M"]),
        cdiv(c, meta["BLOCK_N"]),
        meta["GROUPS"],
    )



# ==================================================
# Line: 360

def conv_layout(
    x: TensorBox,
    weight: TensorBox,
    bias: Optional[TensorBox],
    stride: Sequence[int],
    padding: tuple[int, ...],
    dilation: tuple[int, ...],
    transposed: bool,
    output_padding: tuple[int, ...],
    groups: int,

# ==================================================
# Line: 425

def convolution(
    x: TensorBox,
    weight: TensorBox,
    bias: Optional[TensorBox],
    stride: Sequence[int],
    padding: Sequence[int],
    dilation: Sequence[int],
    transposed: bool,
    output_padding: Sequence[int],
    groups: int,

# ==================================================
# Line: 668

def _convolution(
    x,
    weight,
    bias,
    stride,
    padding,
    dilation,
    transposed,
    output_padding,
    groups,
    benchmark,
    deterministic,
    cudnn_enabled,
    allow_tf32,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/pattern_matcher.py
# Line: 1370

def register_replacement(
    search_fn: SearchFn,
    replace_fn: ReplaceFn,
    example_inputs: Iterable[Any],
    trace_fn: TraceFn,
    pass_dicts: Union[_PassDictsType, Sequence[_PassDictsType]],
    extra_check: Callable[[Match], bool] = _return_true,
    scalar_workaround: Union[dict[str, Union[float, int]], None] = None,
    exclusive_arg_names: Sequence[str] = (),
    search_fn_pattern: Union[PatternExpr, None] = None,
    skip_duplicates: bool = False,

# ==================================================
# Line: 1662

def gen_register_replacement(
    unique_name: str,
    search_fn: SearchFn,
    replace_fn: ReplaceFn,
    example_inputs: Iterable[Any],
    trace_fn: TraceFn,
    pass_dicts: Union[_PassDictsType, Sequence[_PassDictsType]],
    extra_check: Callable[[Match], bool] = _return_true,
    scalar_workaround: Union[dict[str, Union[float, int]], None] = None,
    exclusive_arg_names: Sequence[str] = (),
    skip_duplicates: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/ir.py
# Line: 1202

def num_splits(
    device: torch.device,
    dst_dtype: torch.dtype,
    src_dtype: torch.dtype,
    inner_fn: Callable[..., OpsValue],
    ranges: Sequence[_IntLike],
    reduction_ranges: Sequence[_IntLike],
    reduction_type: Union[ReductionType, Literal["scan"]],
    reduction_numel: Expr,
    input_node: Optional[IRNode] = None,

# ==================================================
# Line: 1414

def create(
    cls,
    device: torch.device,
    dst_dtype: torch.dtype,
    src_dtype: torch.dtype,
    inner_fn: Callable[..., Any],
    ranges: Sequence[Expr],
    reduction_ranges: Sequence[Expr],
    reduction_type: ReductionType,
    reduction_hint: ReductionHint = ReductionHint.DEFAULT,
    input_node: Optional[IRNode] = None,

# ==================================================
# Line: 1651

def _multilayer_wrap_loader(
    cls,
    loader: Callable[..., OpsValue],
    reduction_ranges: Sequence[_IntLike],
    reduction_numel: _IntLike,
    split: _IntLike,
    block_size: _IntLike,
    default: Union[_NumLike, Sequence[_NumLike]],
    input_node: Optional[IRNode] = None,

# ==================================================
# Line: 1723

def create_multilayer_helper(
    cls,
    device: torch.device,
    dst_dtype: torch.dtype,
    src_dtype: torch.dtype,
    wrapper_fn: Callable[..., Any],
    original_ranges: Sequence[Expr],
    original_reduction_ranges: Sequence[Expr],
    new_ranges: list[Expr],
    new_reduction_ranges: list[Integer],
    reduction_type: ReductionType,
    split: _IntLike,
    reduction_hint: ReductionHint,

# ==================================================
# Line: 1787

def create_multilayer(
    cls,
    device: torch.device,
    dst_dtype: torch.dtype,
    src_dtype: torch.dtype,
    inner_fn: Callable[..., Any],
    ranges: Sequence[Expr],
    reduction_ranges: Sequence[Expr],
    reduction_type: ReductionType,
    split: _IntLike,
    reduction_hint: ReductionHint,
    input_node: Optional[IRNode] = None,

# ==================================================
# Line: 1833

def create_multilayer_existing_ranges(
    cls,
    device: torch.device,
    dst_dtype: torch.dtype,
    src_dtype: torch.dtype,
    inner_fn: Callable[..., Any],
    original_ranges: Sequence[Expr],
    original_reduction_ranges: Sequence[Expr],
    new_ranges: list[Integer],
    new_reduction_ranges: list[Integer],
    reduction_type: ReductionType,
    reduction_hint: ReductionHint,

# ==================================================
# Line: 1878

def __init__(
    self,
    device: torch.device,
    dst_dtype: torch.dtype,
    inner_fns: Union[INNER_FN_TY, Sequence[INNER_FN_TY]],
    ranges: Sequence[Integer],
    reduction_ranges: Sequence[Integer],
    reduction_type: ReductionType,
    src_dtype: torch.dtype,
    reduction_hint: ReductionHint,
    output_index: int,

# ==================================================
# Line: 1935

def create(  # type: ignore[override]
    cls,
    device: torch.device,
    dst_dtype: torch.dtype,
    src_dtype: torch.dtype,
    inner_fn: Callable[..., Any],
    ranges: Sequence[Expr],
    reduction_ranges: Sequence[Expr],
    num_output: int,
    reduction_hint: ReductionHint = ReductionHint.DEFAULT,
    input_node: Optional[IRNode] = None,

# ==================================================
# Line: 1973

def create(  # type: ignore[override]
    cls,
    device: torch.device,
    dtype: torch.dtype,
    inner_fns: Sequence[Callable[..., Any]],
    ranges: list[Integer],
    reduction_ranges: list[Integer],
    reduction_type: ReductionType,
    reduction_hint: ReductionHint = ReductionHint.DEFAULT,

# ==================================================
# Line: 2100

def create_multilayer(  # type: ignore[override]
    cls,
    device: torch.device,
    dtype: torch.dtype,
    inner_fns: Sequence[Callable[..., Any]],
    ranges: list[Integer],
    reduction_ranges: list[Integer],
    reduction_type: ReductionType,
    split: _IntLike,
    reduction_hint: ReductionHint,

# ==================================================
# Line: 2268

def create(  # type: ignore[override]
    cls,
    device: torch.device,
    dtypes: tuple[torch.dtype, ...],
    inner_fns: tuple[Callable[[Sequence[Expr]], Any], ...],
    size: list[Integer],
    axis: int,
    combine_fn: Callable[[tuple[Any, ...], tuple[Any, ...]], tuple[Any, ...]],
    reduction_hint: ReductionHint = ReductionHint.DEFAULT,
    *,
    # Whether we have the option to fallback to aten
    can_fallback_to_aten: bool = True,
    **kwargs: Any,

# ==================================================
# Line: 2366

def num_splits(
    cls,
    device: torch.device,
    dtype: torch.dtype,
    inner_fn: Callable[[Sequence[Expr]], OpsValue],
    axis: int,
    pointwise_ranges: list[Integer],
    scan_ranges: list[Integer],
    combine_fn: Callable[[tuple[Any, ...], tuple[Any, ...]], tuple[Any, ...]],
    scan_numel: Expr,

# ==================================================
# Line: 2473

def create(  # type: ignore[override]
    cls,
    device: torch.device,
    dtypes: tuple[torch.dtype, ...],
    inner_fns: tuple[Callable[[list[Expr]], Any], ...],
    size: list[Integer],
    axis: int,
    stable: bool,
    descending: bool,
    reduction_hint: ReductionHint = ReductionHint.DEFAULT,
    **kwargs: Any,

# ==================================================
# Line: 3308

def create(cls, x, dim, start, end, step=1, clamp=True):  # type: ignore[no-untyped-def]
    step = sympy.expand(step)
    assert isinstance(step, sympy.Expr) or step > 0
    try:
        if start == 0 and end >= 2**63 - 1 and step == 1:
            return x
    except TypeError:
        pass

    new_size = list(x.get_size())

    # NB: Ordinarily we default to clamping.
    # We only don't clamp for split_with_sizes. For split_with_sizes, sizes should be already valid
    # failing in this situation is ok, since invalid sizes could trigger silent errors.
    if clamp:
        start, end = cls.normalize_start_end(x, dim, start, end)

    new_size[dim] = FloorDiv(end - start + (step - 1), step)

    if is_storage_and_layout(x):
        # Fast path
        storage, old_layout = as_storage_and_layout(x)
        new_stride = list(old_layout.stride)
        new_stride[dim] = new_stride[dim] * step
        new_layout = FixedLayout(
            old_layout.device,
            old_layout.dtype,
            new_size,
            new_stride,
            old_layout.offset + old_layout.stride[dim] * start,
        )
        return ReinterpretView(data=storage, layout=new_layout)

    def reindex(index):  # type: ignore[no-untyped-def]
        assert len(index) == len(new_size), f"wrong ndim {index} {new_size}"
        index = list(index)
        index[dim] = index[dim] * step + start
        return index

    # redirect to a generic view
    return SliceView(data=x, size=new_size, reindex=reindex)



# ==================================================
# Line: 4810

def __init__(  # type: ignore[no-untyped-def]
    self,
    layout,
    inputs,
    make_kernel_render,
    workspace_size: int,
    template: CUDATemplate,
    supports_epilogue_fusion: bool,

# ==================================================
# Line: 5119

def __init__(  # type: ignore[no-untyped-def]
    self,
    name,
    layout,
    inputs,
    constant_args=(),
    kwargs=None,
    output_view=None,
    python_kernel_name=None,
    cpp_kernel_name=None,
    ordered_kwargs_for_cpp_kernel=(),
    op_overload=None,

# ==================================================
# Line: 5949

def __init__(  # type: ignore[no-untyped-def]
    self,
    layout,
    inputs,
    constant_args=(),
    kwargs=None,
    output_view=None,
    python_kernel_name=None,
    cpp_kernel_name=None,
    ordered_kwargs_for_cpp_kernel=(),
    op_overload=None,

# ==================================================
# Line: 6004

def __init__(  # type: ignore[no-untyped-def]
    self,
    layout,
    inputs,
    constant_args=(),
    kwargs=None,
    python_kernel_name=None,
    cpp_kernel_name=None,
    ordered_kwargs_for_cpp_kernel=(),
    op_overload=None,

# ==================================================
# Line: 6565

def __init__(  # type: ignore[no-untyped-def]
    self,
    op_overload,
    x,
    dim: int,
    index,
    src,
    *,
    reduce: Optional[str] = None,
    include_self: bool = True,

# ==================================================
# Line: 6780

def __init__(  # type: ignore[no-untyped-def]
    self,
    layout,
    kernel,
    tensor_args,
    nontensor_args,
    unflatten_args,
    kwargs=None,
    *,
    unbacked_bindings=None,

# ==================================================
# Line: 7274

def __init__(  # type: ignore[no-untyped-def]
    self,
    layout,
    kernel,
    tensor_args,
    nontensor_args,
    unflatten_args,
    *,
    unbacked_bindings=None,

# ==================================================
# Line: 7722

def __init__(
    self,
    predicate: IRNode,
    operands: list[Union[TensorBox, ShapeAsConstantBuffer]],
    true_subgraph: Subgraph,
    false_subgraph: Subgraph,
    layout: MultiOutputLayout,
    unbacked_bindings: Optional[dict[sympy.Symbol, pytree.KeyPath]],

# ==================================================
# Line: 8074

def __init__(  # type: ignore[no-untyped-def]
    self,
    layout,
    kernel,
    tensor_args,
    nontensor_args,
    unflatten_args,
    kwargs=None,
    *,
    unbacked_bindings=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/dependencies.py
# Line: 537

def bucketize(
    self,
    values: T,
    boundaries: tuple[str, sympy.Expr, sympy.Expr, sympy.Expr],
    boundary_indices: T,
    indexing_dtype: torch.dtype,
    right: bool,
    sorter: Optional[tuple[str, sympy.Expr]] = None,
    sorter_indices: Optional[T] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/template_heuristics.py
# Line: 359

def _scale_mm_configs(
    self,
    m: int,
    n: int,
    k: int,
    configs: list[BaseConfig],
    scale: float,
    has_int8_tensor: bool,
    exclude: Callable[[int, int, int], bool],

# ==================================================
# Line: 421

def preprocess_mm_configs(
    self,
    m: int,
    n: int,
    k: int,
    configs: list[BaseConfig],
    has_int8_tensor: bool = False,
    scale: int = 1,
    exclude: Callable[[int, int, int], bool] = lambda m, n, k: False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/triton_combo_kernel.py
# Line: 580

def jit_line(
    self,
    heuristics: str,
    size_hints: dict[str, int],
    selected_kernel: TritonKernel,
    signature: list[Any],
    argdefs: list[ArgName],
    pointwise_with_reduce: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_flex_attention_template.py
# Line: 688

def __init__(
    self,
    input_nodes,
    layout: ir.Layout,
    scale,
    score_mod,
    mask_mod,
    kv_block_size,
    q_block_size,
    has_other_buffer,
    no_full_kv_block,
    fake_buffers,
    len_score_other,
    len_mask_other,
    kernel_input_name_to_buffer,
    block_vars,

# ==================================================
# Line: 907

def add_choices(
    choices,
    input_nodes,
    layout,
    scale,
    score_mod,
    mask_mod,
    kv_block_size,
    q_block_size,
    has_other_buffer,
    no_full_kv_block,
    fake_buffers,
    len_score_other,
    len_mask_other,
    kernel_input_name_to_buffer,
    block_vars,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cutlass_lib_extensions/evt_extensions.py
# Line: 96

def trace(
    fn_src: str,
    example_tensors: dict[str, CutlassTensor],
    accum_type: DataType,
    output_type: DataType,
    tile_description: TileDescription,
    epilogue_schedule: EpilogueScheduleType,
    name_to_buffer: dict[str, Buffer],
    size_hint_fn: Callable[[Union[Expr, int]], int],
    **kwargs: dict[str, Any],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/gemm_template.py
# Line: 418

def __init__(
    self,
    input_nodes: list[Buffer],
    layout: Layout,
    alpha: float,
    beta: float,
    input_reorder: Optional[list[int]] = None,
    use_fast_accum: Optional[bool] = None,

# ==================================================
# Line: 451

def add_cutlass_gemm_choices(
    choices: list[ChoiceCaller],
    layout: ir.Layout,
    input_nodes: list[Buffer],
    alpha: Union[float, int] = 1,
    beta: Union[float, int] = 0,
    input_reorder: Optional[list[int]] = None,
    use_fast_accum: Optional[bool] = None,
    **extra_kwargs,

# ==================================================
# Line: 532

def _add_cutlass_gemm_choices(
    self,
    choices: list[ChoiceCaller],
    layout: ir.Layout,
    input_nodes: list[Buffer],
    alpha: Union[float, int] = 1,
    beta: Union[float, int] = 0,
    input_reorder: Optional[list[int]] = None,
    **extra_kwargs,

# ==================================================
# Line: 1248

def __init__(
    self,
    input_nodes: list[Buffer],
    layout: Layout,
    alpha: float,
    beta: float,
    input_reorder: Optional[list[int]] = None,
    use_fast_accum: Optional[bool] = None,

# ==================================================
# Line: 1262

def add_cutlass_gemm_choices(
    choices: list[ChoiceCaller],
    layout: ir.Layout,
    input_nodes: list[Buffer],
    alpha: Union[float, int] = 1,
    beta: Union[float, int] = 0,
    input_reorder: Optional[list[int]] = None,
    use_fast_accum: Optional[bool] = None,
    **extra_kwargs,

# ==================================================
# Line: 1537

def render_gemm_arguments(
    self,
    argument_template: str,
    epilogue_template: str,
    should_swap_xw: bool,
    X: IRNode,
    W: IRNode,
    Bias: IRNode,
    Y: IRNode,
    alpha: float,
    beta: float,
    kernel: CUDATemplateKernel,
    epilogue_args,

# ==================================================
# Line: 1640

def add_cutlass_gemm_choices(
    choices: list[ChoiceCaller],
    layout: ir.Layout,
    input_nodes: list[Buffer],
    alpha: Union[float, int] = 1,
    beta: Union[float, int] = 0,
    input_reorder: Optional[list[int]] = None,
    use_fast_accum: Optional[bool] = False,
    **extra_kwargs,

# ==================================================
# Line: 1824

def render_gemm_arguments(
    self,
    instance_type: str,
    argument_template: str,
    epilogue_template: str,
    should_swap_xw: bool,
    X: IRNode,
    W: IRNode,
    Bias: IRNode,
    Meta: IRNode,
    Y: IRNode,
    alpha: float,
    beta: float,
    kernel: CUDATemplateKernel,
    epilogue_args,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cuda_kernel.py
# Line: 575

def __init__(
    self,
    name: str,
    category: str,
    input_nodes: list[Buffer],
    layout: Layout,
    make_kernel_render: Callable[
        [CUDATemplateBuffer, Optional[list[BaseSchedulerNode]]],
        tuple[CUDATemplateKernel, functools.partial[str]],
    ],
    bmreq: CUDABenchmarkRequest,
    supports_epilogue_fusion: bool,
    template: "CUDATemplate",  # type: ignore[name-defined]
    info_kwargs: Optional[
        dict[str, Union[PrimitiveInfoType, list[PrimitiveInfoType]]]
    ],  # type: ignore[type-arg]
    description: str,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/debug_utils.py
# Line: 56

def __init__(
    self,
    debug_printer_level,
    use_array_ref: bool,
    writeline: Optional[Callable[..., None]] = None,
    args_to_print_or_save: Optional[list[str]] = None,
    kernel_name: str = "",
    kernel=None,
    arg_signatures: Optional[list[type]] = None,
    kernel_type=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_grouped_gemm_template.py
# Line: 153

def __init__(
    self,
    input_nodes: list[ir.IRNode],
    layout: ir.Layout,
    num_threads: int,
    register_blocking: GemmBlocking,
    beta: int = 1,
    alpha: int = 1,
    has_bias: bool = False,
    epilogue_creator: Optional[Callable[[ir.Buffer], ir.Pointwise]] = None,
    act_mapping: Optional[dict[int, ir.IRNode]] = None,
    gemm_grouped_num: int = 1,

# ==================================================
# Line: 192

def add_choices(
    cls,
    choices: list[ChoiceCaller],
    layout: ir.Layout,
    input_nodes: list[ir.IRNode],
    beta: int = 1,
    alpha: int = 1,
    has_bias: tuple[bool, ...] = (False, False),
    trans_w: bool = False,
    input_indices: Optional[list[int]] = None,
    epilogue_creator: Optional[Callable[[ir.Buffer], ir.Pointwise]] = None,
    act_mapping: Optional[dict[int, ir.IRNode]] = None,  # gemm idx to its act buf

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_wrapper_cpu.py
# Line: 112

def _generate_kernel_call_helper(
    self,
    kernel_name: str,
    call_args,
    *,
    device=None,
    triton=True,
    arg_types=None,
    raw_keys=None,
    raw_args=None,
    triton_meta=None,
    graph_name="",
    original_fxnode_name=None,

# ==================================================
# Line: 1309

def generate_scatter_fallback(
    self,
    output,
    inputs,
    cpp_kernel_name,
    python_kernel_name,
    src_is_tensor,
    reduce,
    kwargs,

# ==================================================
# Line: 1508

def make_allocation(
    self, name, device, dtype, shape, stride, allocation_shape=None

# ==================================================
# Line: 1603

def codegen_reinterpret_view(
    self,
    data,
    size,
    stride,
    offset,
    writeline: Callable[..., None],
    dtype=None,

# ==================================================
# Line: 2049

def generate_fallback_kernel_with_runtime_lookup(
    self,
    buf_name: str,
    python_kernel_name: str,
    cpp_kernel_name: str,
    codegen_args: list[str],
    op_overload: Optional[torch._ops.OpOverload] = None,
    raw_args=None,
    outputs=None,

# ==================================================
# Line: 2266

def generate_fallback_kernel_with_runtime_lookup_jit(
    self,
    buf_name: str,
    python_kernel_name: str,
    cpp_kernel_name: str,
    codegen_args: list[str],
    op_overload: Optional[torch._ops.OpOverload] = None,
    raw_args=None,
    output_args: Optional[list[Optional[str]]] = None,
    raw_outputs: Optional[list[ir.Buffer]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/rocm/ck_conv_template.py
# Line: 385

def add_ck_conv_choices(
    choices,
    layout,
    input_nodes,
    *,
    stride,
    padding,
    dilation,
    groups,
    n_spatial_dimensions,

# ==================================================
# Line: 412

def __init__(
    self,
    input_nodes,
    layout,
    *,
    stride,
    padding,
    dilation,
    groups,
    n_spatial_dimensions,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/rocm/rocm_kernel.py
# Line: 224

def __init__(
    self,
    name: str,
    category: str,
    input_nodes: list[Buffer],
    layout: Layout,
    make_kernel_render: Callable[
        [ROCmTemplateBuffer, Optional[Sequence[IRNode]]], str
    ],
    bmreq: ROCmBenchmarkRequest,
    template: "ROCmTemplate",  # type: ignore[name-defined]
    info_kwargs: Optional[
        dict[str, Union[PrimitiveInfoType, list[PrimitiveInfoType]]]
    ],  # type: ignore[type-arg]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp.py
# Line: 1920

def _gen_parallel_reduction_buffers(
    self,
    acc,
    acc_type,
    reduction_type,
    dtype,
    reduction_combine_fn=reduction_combine,
    reduction_init_fn=reduction_init,

# ==================================================
# Line: 2550

def _load_or_store_non_contiguous(
    self,
    var: Optional[str],
    index: sympy.Expr,
    dtype: torch.dtype,
    buffer: Optional[IndentedBuffer] = None,
    store_value: Optional[Union[str, CppCSEVariable]] = None,
    accu_store: bool = False,

# ==================================================
# Line: 3152

def reduction_combine_vec(
    self,
    reduction_type,
    var,
    next_value,
    welford_helper_val=None,
    index: Optional[sympy.Symbol] = None,
    horizontal_reduction: Optional[bool] = None,
    src_dtype: Optional[torch.dtype] = torch.float32,

# ==================================================
# Line: 3340

def __init__(
    self,
    args,
    num_threads,
    tiling_factor,
    tiling_indices,
    inner_tail_size=None,
    outer_tail_size=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_wrapper_gpu.py
# Line: 469

def _generate_kernel_call_helper(
    self,
    kernel_name: str,
    call_args,
    *,
    device=None,
    triton=True,
    arg_types=None,
    raw_keys=None,
    raw_args=None,
    triton_meta=None,
    graph_name="",
    original_fxnode_name=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/simd.py
# Line: 110

def __init__(
    self,
    name: str,
    var_list: list[sympy.Symbol],
    var_ranges: dict[sympy.Symbol, sympy.Expr],
    numel: sympy.Expr,
    prefix: str,
    *,
    kernel: SIMDKernel,
    divisor=sympy.S.One,
    length=sympy.S.One,
    root: IterationRangesRoot,

# ==================================================
# Line: 158

def __init__(
    self,
    name: str,
    numel: sympy.Expr,
    prefix: str,
    index: int,
    kernel: SIMDKernel,
    pid_cache: Optional[dict[str, str]] = None,
    *,
    is_loop: bool,
    tensor_dim: Optional[int],
    grid_dim: Optional[int],
    has_zdim: bool,

# ==================================================
# Line: 381

def __init__(
    self,
    tiling: dict[str, sympy.Expr],
    features: SIMDKernelFeatures,
    pid_cache: Optional[dict[str, str]] = None,
    override_persistent_reduction: Optional[bool] = None,
    override_cooperative_reduction: Optional[bool] = None,
    tiling_scores: Optional[dict[str, sympy.Expr]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/wrapper.py
# Line: 750

def make_allocation_line(
    comm_buffer_type, group_name, wrapper, name, device, dtype, shape, stride

# ==================================================
# Line: 1392

def generate_scatter_fallback(
    self,
    output,
    inputs,
    cpp_kernel_name,
    python_kernel_name,
    src_is_tensor,
    reduce,
    kwargs,

# ==================================================
# Line: 1416

def generate_fallback_kernel_with_runtime_lookup(
    self,
    buf_name: str,
    python_kernel_name: str,
    cpp_kernel_name: str,
    codegen_args: list[str],
    op_overload: Optional[torch._ops.OpOverload] = None,
    raw_args=None,
    outputs=None,

# ==================================================
# Line: 1750

def codegen_reinterpret_view(
    self,
    data,
    size,
    stride,
    offset,
    writeline: Callable[..., None],
    dtype=None,

# ==================================================
# Line: 1972

def define_user_defined_triton_kernel(
    self,
    kernel,
    configs,
    kwargs,
    restore_value_args,
    reset_to_zero_args,
    grids: list[list[Union[int, sympy.Expr]]],

# ==================================================
# Line: 2454

def generate_kernel_call(
    self,
    kernel_name: str,
    call_args,
    *,
    device=None,
    triton=True,
    arg_types=None,
    raw_keys=None,
    raw_args=None,
    triton_meta=None,
    original_fxnode_name=None,

# ==================================================
# Line: 2501

def _generate_kernel_call_helper(
    self,
    kernel_name: str,
    call_args,
    *,
    device=None,
    triton=True,
    arg_types=None,
    raw_keys=None,
    raw_args=None,
    triton_meta=None,
    graph_name="",
    original_fxnode_name=None,

# ==================================================
# Line: 2678

def make_allocation(
    self, name, device, dtype, shape, stride, allocation_shape=None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_wrapper_cpu_array_ref.py
# Line: 105

def _generate_kernel_call_helper(
    self,
    kernel_name: str,
    call_args,
    *,
    device=None,
    triton=True,
    arg_types=None,
    raw_keys=None,
    raw_args=None,
    triton_meta=None,
    graph_name="",
    original_fxnode_name=None,

# ==================================================
# Line: 568

def make_allocation(
    self, name, device, dtype, shape, stride, buffer_if_can_stack_allocate=None

# ==================================================
# Line: 686

def generate_scatter_fallback(
    self,
    output,
    inputs,
    cpp_kernel_name,
    python_kernel_name,
    src_is_tensor,
    reduce,
    kwargs,

# ==================================================
# Line: 748

def generate_fallback_kernel_with_runtime_lookup(
    self,
    buf_name: str,
    python_kernel_name: str,
    cpp_kernel_name: str,
    codegen_args: list[str],
    op_overload: Optional[torch._ops.OpOverload] = None,
    raw_args=None,
    outputs=None,

# ==================================================
# Line: 813

def codegen_reinterpret_view(
    self,
    data,
    size,
    stride,
    offset,
    writeline: Callable[..., None],
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_micro_gemm.py
# Line: 74

def __init__(
    self,
    name,
    input_dtype,
    input2_dtype,
    output_dtype,
    compute_dtype,
    register_blocking,
    alpha=1,

# ==================================================
# Line: 133

def codegen_call(
    self,
    kernel: CppTemplateKernel,
    A: ir.Buffer,
    B: ir.Buffer,
    C: ir.Buffer,
    accum: bool,
    prefetch: bool = False,
    **kwargs_for_extra_args,

# ==================================================
# Line: 252

def generate_gemm_config(
    vec_isa_cls,
    register_blockings,
    input_dtype=torch.float,
    input2_dtype=None,
    output_dtype=None,
    compute_dtype=None,
    extra_check=None,

# ==================================================
# Line: 301

def __init__(
    self, name, input_dtype, input2_dtype, output_dtype, compute_dtype, alpha

# ==================================================
# Line: 884

def __init__(
    self,
    name,
    input_dtype,
    input2_dtype,
    output_dtype,
    compute_dtype,
    register_blocking,
    alpha=1,
    tail_n=False,
    trans_b=False,

# ==================================================
# Line: 1895

def create_micro_gemm(
    name,
    m,
    n,
    k,
    input_dtype,
    input2_dtype,
    output_dtype=None,
    compute_dtype=None,
    alpha=1,
    num_threads=-1,
    use_ref=True,
    q_group_size=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_template_kernel.py
# Line: 54

def def_kernel(
    self,
    inputs: dict[str, ir.Buffer],
    outputs: dict[str, ir.Buffer],
    aliases: Optional[dict[str, str]] = None,
    function_name: str = "",
    extra_sizevars: Optional[list[sympy.Expr]] = None,
    placeholder: str = "<DEF_KERNEL>",

# ==================================================
# Line: 347

def store_output(
    self,
    dst: ir.Buffer,
    src: ir.Buffer,
    orig_src: Optional[ir.Buffer] = None,
    epilogue_nodes: Optional[list[ir.IRNode]] = None,
    offsets: Optional[list[Any]] = None,
    reindexers: Optional[list[Optional[Callable[[list[Any]], list[Any]]]]] = None,

# ==================================================
# Line: 408

def store_outputs(
    self,
    dst: tuple[ir.Buffer],
    src: tuple[ir.IRNode],
    orig_src: Optional[tuple[ir.IRNode]] = None,
    epilogue_nodes: Optional[list[ir.IRNode]] = None,
    offsets: Optional[list[Any]] = None,
    reindexers: Optional[list[Optional[Callable[[list[Any]], list[Any]]]]] = None,
    multi_output_buffers: Optional[tuple[ir.MultiOutput]] = None,

# ==================================================
# Line: 537

def __init__(
    self,
    name: str,
    category: str,
    input_nodes: list[ir.Buffer],
    layout: ir.Layout,
    make_kernel_render: Callable[
        [
            ir.CppTemplateBuffer,
            bool,
            Optional[list[ir.IRNode]],
        ],
        str,
    ],
    bmreq: CppBenchmarkRequest,
    template: "CppTemplate",  # type: ignore[name-defined]  # noqa: F821
    info_kwargs: Optional[
        dict[str, Union[ir.PrimitiveInfoType, list[ir.PrimitiveInfoType]]]
    ] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_gemm_template.py
# Line: 581

def __init__(
    self,
    input_nodes,
    layout: ir.Layout,
    num_threads: int,
    register_blocking: GemmBlocking,
    beta=1,
    alpha=1,
    has_bias=False,
    epilogue_creator: Optional[Callable[[ir.Buffer], ir.Pointwise]] = None,
    should_block_weights: bool = True,
    name="packed_gemm",

# ==================================================
# Line: 878

def add_choices(
    cls,
    choices,
    layout,
    input_nodes,
    beta=1,
    alpha=1,
    has_bias=False,
    trans_w=False,
    input_indices=None,
    epilogue_creator: Optional[Callable[[ir.Buffer], ir.Pointwise]] = None,
    act_mapping: Optional[dict[int, ir.IRNode]] = None,

# ==================================================
# Line: 1083

def prep_weight(
    cls,
    inputs,
    layout: ir.Layout,
    micro_gemm: CppMicroGemm,
    should_block_weight: bool,
    use_int8_fast_compensation_path: bool = False,
    skip_int8_compensation: bool = False,

# ==================================================
# Line: 1592

def codegen_blocks(
    self,
    num_threads,
    N,
    K,
    micro_gemm,
    is_dynamic_M,
    kernel,
    GemmOut,
    config,
    L1_cache_size,
    L2_cache_size,
    X,
    W,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/triton.py
# Line: 2354

def bucketize(
    self,
    values: CSEVariable,
    boundaries: tuple[str, sympy.Expr, sympy.Expr, sympy.Expr],
    boundary_indices: CSEVariable,
    indexing_dtype: torch.dtype,
    right: bool,
    sorter: Optional[tuple[str, sympy.Expr]] = None,
    sorter_indices: Optional[CSEVariable] = None,

# ==================================================
# Line: 2838

def _welford(self, buffer, mean, m2, weight, dim, dtype: torch.dtype):
    """
    Helper to codegen triton_helpers.welford.
    """
    mean, m2, weight = (
        self.reduction_collapse_dims(buffer, value, dtype)
        for value in (mean, m2, weight)
    )
    welford = f"triton_helpers.welford({mean}, {m2}, {weight}, {dim})"
    welford_results = [str(self.cse.newvar(dtype=dtype)) for _ in range(3)]
    buffer.writeline(f"{', '.join(welford_results)} = {welford}")

    result_values = tuple(self.reduction_resize(value) for value in welford_results)
    return result_values


# ==================================================
# Line: 2853

def welford_reduce(
    self, result_var, reduction_type, value, where_cond, acc_type, dtype

# ==================================================
# Line: 2912

def welford_reduce_final_reduction(
    self,
    buffer,
    result_mean,
    result_m2,
    result_weight,
    mean,
    m2,
    weight,
    dim,
    dtype,

# ==================================================
# Line: 2932

def online_softmax_reduce_final_reduction(
    self, buffer, result_max, result_sum, peer_max, peer_sum, dim, dtype

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_bmm_template.py
# Line: 76

def __init__(
    self,
    input_nodes,
    layout: ir.Layout,
    num_threads: int,
    register_blocking: GemmBlocking,
    beta=1,
    alpha=1,
    has_bias=False,
    epilogue_creator: Optional[Callable[[ir.Buffer], ir.Pointwise]] = None,
    should_block_weights: bool = False,
    name="bmm",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/common.py
# Line: 977

def bucketize(
    self,
    values: OpVarT,
    boundaries: tuple[str, sympy.Expr, sympy.Expr, sympy.Expr],
    boundary_indices: OpVarT,
    indexing_dtype: torch.dtype,
    right: bool,
    sorter: Optional[tuple[str, sympy.Expr]] = None,
    sorter_indices: Optional[OpVarT] = None,

# ==================================================
# Line: 1753

def __init__(
    self,
    prefix: str = "",
    suffix: str = "",
    name_prefix: str = "tmp",
    iter_buffers: Optional[itertools.count[int]] = None,
    store_cache: Optional[MutableMapping[str, CSEVariableType]] = None,
    reduction_cache: Optional[
        MutableMapping[ReductionCacheKey, CSEVariableType]
    ] = None,
    varname_map: Optional[dict[str, CSEVariableType]] = None,

# ==================================================
# Line: 1822

def generate(
    self,
    buffer: IndentedBuffer,
    expr: Union[str, CSEVariable, OpsValue, IndentedBuffer, DeferredLineBase],
    *,
    bounds: ValueRanges[Any] = ValueRanges.unknown(),
    write: bool = True,
    assignment: bool = True,
    dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 2061

def bucketize(
    self,
    values: CSEVariable,
    boundaries: tuple[str, sympy.Expr, sympy.Expr, sympy.Expr],
    boundary_indices: CSEVariable,
    indexing_dtype: torch.dtype,
    right: bool,
    sorter: Optional[tuple[str, sympy.Expr]] = None,
    sorter_indices: Optional[CSEVariable] = None,

# ==================================================
# Line: 2591

def bucketize(
    self,
    values: CSEVariable,
    boundaries: tuple[str, sympy.Expr, sympy.Expr, sympy.Expr],
    boundary_indices: CSEVariable,
    indexing_dtype: torch.dtype,
    right: bool,
    sorter: Optional[tuple[str, sympy.Expr]] = None,
    sorter_indices: Optional[CSEVariable] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/dtype_propagation.py
# Line: 308

def bucketize(
    values: DTypeArg,
    boundaries: tuple[str, sympy.Expr, sympy.Expr, sympy.Expr],
    boundary_indices: DTypeArg,
    indexing_dtype: torch.dtype,
    right: bool,
    sorter: Optional[tuple[str, sympy.Expr]] = None,
    sorter_indices: Optional[T] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/aoti_eager.py
# Line: 167

def aoti_compile_with_persistent_cache(
    ns: str,
    op_func_name_with_overload: str,
    device_type: str,
    dynamic: bool,
    f: Callable[..., Any],
    args: tuple[Any],
    kwargs: dict[str, Any],
    *,
    dynamic_shapes: Optional[dict[str, Any]] = None,
    options: Optional[dict[str, Any]] = None,
    remove_runtime_assertions: bool = False,
    disable_constraint_solver: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/compile_fx.py
# Line: 1569

def cudagraphify(
    model: Callable[..., Any],
    static_input_idxs: Sequence[int] = (),
    *,
    device_index: int,
    stack_traces: list[Optional[str]],
    is_backward: bool,
    is_inference: bool,
    constants: tuple[torch.Tensor, ...] = (),
    placeholders: Sequence[PlaceholderInfo] = (),
    mutated_input_idxs: tuple[int, ...] = (),

# ==================================================
# Line: 1791

def fw_compiler_freezing(
    aot_autograd_model: GraphModule,
    aot_example_inputs: Sequence[InputType],
    dynamo_model: GraphModule,
    num_example_inputs: int,
    inner_compile: Callable[..., Any],
    cudagraphs: BoxedBool,
    graph_id: int,
    forward_device: BoxedDeviceIndex,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/triton_helpers.py
# Line: 262

def bucketize_binary_search(
    values: tl.tensor,
    boundaries_ptr: tl.tensor,
    BOUNDARIES_SIZE: int,
    BOUNDARIES_UNDERLYING_NUMEL: int,
    BOUNDARIES_STRIDE: int,
    boundary_indices: tl.tensor,
    indexing_dtype: tl.dtype,
    right: "bool",  # triton can't handle the unquoted bool annotation
    sorter_ptr: tl.tensor,
    SORTER_STRIDE: int,
    sorter_indices: tl.tensor,

# ==================================================
# Line: 511

def _compare_and_swap_with_index(
    x,
    idxs,
    rnumel,
    flip,
    i: tl.constexpr,
    n_dims: tl.constexpr,
    stable: tl.constexpr,
    descending: tl.constexpr,

# ==================================================
# Line: 580

def _bitonic_merge_with_index(
    x,
    idxs,
    rnumel,
    stage: tl.constexpr,
    alternating: tl.constexpr,
    n_dims: tl.constexpr,
    stable: tl.constexpr,
    descending: tl.constexpr,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/triton_heuristics.py
# Line: 248

def __init__(
    self,
    fn,
    triton_meta,  # passed directly to triton
    configs,
    save_cache_hook,
    mutated_arg_names: list[str],  # see [Note: clone mutated buffers]
    optimize_mem,
    heuristic_type,
    size_hints=None,
    inductor_meta=None,  # metadata not relevant to triton
    custom_kernel=False,  # whether the kernel is inductor-generated or custom
    filename: Optional[str] = None,
    reset_to_zero_arg_names: Optional[list[str]] = None,
    autotune_cache_info: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 1820

def cached_autotune(
    size_hints: Optional[list[int]],
    configs: list[Config],
    triton_meta,
    heuristic_type,
    filename=None,
    inductor_meta=None,
    custom_kernel=False,

# ==================================================
# Line: 1977

def triton_config(
    size_hints,
    x,
    y=None,
    z=None,
    num_stages=1,
    num_elements_per_warp=256,
    min_elem_per_thread=0,

# ==================================================
# Line: 2443

def adapt_config_for_tiling(
    size_hints,
    tiling_scores,
    original_x,
    original_r,
    num_warps=None,
    num_stages=1,
    register_intensive=False,
    persistent_reduction=False,

# ==================================================
# Line: 2667

def template(
    num_stages,
    num_warps,
    triton_meta,
    num_consumer_groups=0,
    num_buffers_warp_spec=0,
    filename=None,
    inductor_meta=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/halide_helpers.py
# Line: 45

def philox_impl(c0, c1, c2, c3, k0, k1, n_rounds):
    def umulhi(a, b):
        a = hl.cast(hl.UInt(64), a)
        b = hl.cast(hl.UInt(64), b)
        return hl.cast(hl.UInt(32), ((a * b) >> 32) & hl.u64(0xFFFFFFFF))

    for _ in range(n_rounds):
        _c0, _c2 = c0, c2

        c0 = umulhi(PHILOX_ROUND_B_U32, _c2) ^ c1 ^ k0
        c2 = umulhi(PHILOX_ROUND_A_U32, _c0) ^ c3 ^ k1
        c1 = PHILOX_ROUND_B_U32 * _c2
        c3 = PHILOX_ROUND_A_U32 * _c0
        # raise key
        k0 = k0 + PHILOX_KEY_A_U32
        k1 = k1 + PHILOX_KEY_B_U32

    return c0, c1, c2, c3



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/select_algorithm.py
# Line: 295

def __init__(
    self,
    kernel_name,
    input_nodes,
    output_node,
    defines,
    num_stages,
    num_warps,
    grid_fn,
    meta,
    call_sizes,
    num_consumer_groups=0,
    num_buffers_warp_spec=0,
    use_jit=False,
    prefix_args=0,
    suffix_args=0,
    epilogue_fn=identity,
    subgraphs: Optional[list[ir.ComputedBuffer]] = None,
    workspace_arg: Optional[WorkspaceArg] = None,
    prologue_loads_all_inputs=False,

# ==================================================
# Line: 750

def load_input(
    self,
    input_name: str,
    output_name: str,
    indices: Union[list[Any], tuple[Any]],
    mask: Optional[str] = None,
    other: Optional[Union[float, int]] = 0.0,
    indent_width: int = 4,

# ==================================================
# Line: 1174

def make_key(
    self,
    input_nodes: tuple[ir.IRNode],
    num_stages: int,
    num_warps: int,
    call_sizes: list[sympy.core.symbol.Symbol],
    prefix_args: int,
    suffix_args: int,
    epilogue_fn: Optional[Callable[..., Any]],
    epilogue_fn_hash: Optional[str],
    subgraphs: Optional[list[ir.Buffer]],  # has to be none to cache
    workspace_arg: Optional[WorkspaceArg],  # has to be none to cache
    layout: ir.Layout,
    num_consumer_groups: int,
    num_buffers_warp_spec: int,
    kwargs: dict[str, Any],

# ==================================================
# Line: 1277

def __init__(
    self,
    name: str,
    grid: Any,
    source: str,
    debug=False,
    cache_codegen_enabled_for_template=False,
    prologue_loads_all_inputs=False,

# ==================================================
# Line: 1327

def generate_and_load(
    self,
    input_nodes: tuple[ir.IRNode],
    num_stages: int,
    num_warps: int,
    call_sizes: list[sympy.core.symbol.Symbol],
    prefix_args: int,
    suffix_args: int,
    epilogue_fn: Optional[Callable[..., Any]],
    epilogue_fn_hash: Optional[str],
    subgraphs: Optional[list[ir.Buffer]],
    workspace_arg: Optional[WorkspaceArg],
    num_consumer_groups: int,
    num_buffers_warp_spec: int,
    layout: ir.Layout,
    kwargs: dict[str, Any],
    generate_with_caching,

# ==================================================
# Line: 1518

def generate(  # type: ignore[override]
    self,
    input_nodes: tuple[ir.IRNode],
    layout: ir.Layout,
    num_stages: int,
    num_warps: int,
    num_consumer_groups: int = 0,
    num_buffers_warp_spec: int = 0,
    prefix_args: int = 0,
    suffix_args: int = 0,
    epilogue_fn: Optional[Callable[..., Any]] = identity,
    epilogue_fn_hash: Optional[str] = None,
    subgraphs: Optional[list[ir.Buffer]] = None,
    mutated_inputs: Optional[list[ir.IRNode]] = None,
    call_sizes: Optional[list[sympy.core.symbol.Symbol]] = None,
    workspace_arg: Optional[WorkspaceArg] = None,
    generate_with_caching=False,
    **kwargs,

# ==================================================
# Line: 1700

def __init__(
    self,
    kernel,
    cpp_kernel=None,
    *,
    name=None,
    has_out_variant=True,
    op_overload=None,
    use_fallback_kernel=False,
    kernel_creator=None,

# ==================================================
# Line: 1757

def __init__(
    self,
    name,
    input_nodes,
    layout,
    make_kernel_render,
    description,
    bmreq,
    log_info: Optional[
        dict[str, Union[PrimitiveInfoType, list[PrimitiveInfoType]]]
    ] = None,
    mutated_inputs=None,
    workspace_arg: Optional[WorkspaceArg] = None,
    allowed_prologue_inps: Optional[OrderedSet[str]] = None,

# ==================================================
# Line: 2131

def __call__(
    self,
    name,
    choices: list[ChoiceCaller],
    input_nodes,
    layout,
    # optional dict mapping arg indices to the functions
    # generating a torch.Tensor for that input from the
    # corresponding ir.Buffer. if passed for a given
    # arg, the function will be called instead of
    # generating a random torch.Tensor for benchmarking.
    input_gen_fns: Optional[dict[int, Callable[[ir.Buffer], torch.Tensor]]] = None,
    precompilation_timeout_seconds: int = 60 * 60,
    return_multi_template=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/scheduler.py
# Line: 1675

def __init__(
    self,
    scheduler: Scheduler,
    snodes: list[BaseSchedulerNode],
    use_custom_partition_algo: bool,
    prev_node_1: Optional[BaseSchedulerNode] = None,
    prev_node_2: Optional[BaseSchedulerNode] = None,
    enable_autotune: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/lowering.py
# Line: 813

def register_pointwise(
    aten_fn,
    name=None,
    broadcast=True,
    type_promotion_kind=ELEMENTWISE_TYPE_PROMOTION_KIND.DEFAULT,
    convert_input_to_bool=False,
    override_return_dtype=None,
    override_fn_when_input_bool=None,
    allow_alpha=False,
    triton_fallback=None,

# ==================================================
# Line: 1281

def quantized_decomposed_quantize_per_channel(
    input: TensorBox,
    scales: TensorBox,
    zero_points: TensorBox,
    axis: int,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,

# ==================================================
# Line: 1334

def quantized_decomposed_dequantize_per_channel(
    input: TensorBox,
    scales: TensorBox,
    zero_points: TensorBox,
    axis: int,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 1426

def quantized_decomposed_dequantize_per_tensor_default(
    input: TensorBox,
    scale: float,
    zero_point: int,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 1513

def quantized_decomposed_dequantize_per_tensor_tensor(
    input: TensorBox,
    scale: TensorBox,
    zero_point: TensorBox,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 3319

def new_empty_strided(
    x, size, stride, *, dtype=None, layout=None, device=None, pin_memory=None

# ==================================================
# Line: 3446

def index_output_size_and_inner_fn(
    x_size,
    indices,
    tensor_indices,
    tensor_size,
    indices_loaders,
    indexed_size,
    x_loader,
    check,
    wrap_neg=True,

# ==================================================
# Line: 3822

def scatter_fallback(
    op_overload: torch._ops.OpOverload,
    self,
    dim: int,
    index,
    src,
    *,
    reduce: Optional[str] = None,
    include_self: bool = True,

# ==================================================
# Line: 4324

def pooling_size(x, i, kernel_size, stride, padding, ceil_mode, *, dilation=None):
    if dilation is None:
        dilation = [1] * len(padding)

    x_out = FloorDiv(
        x + 2 * padding[i] - dilation[i] * (kernel_size[i] - 1) + (stride[i] - 1),
        stride[i],
    )

    if ceil_mode:
        x_alt = FloorDiv(
            x
            + 2 * padding[i]
            - dilation[i] * (kernel_size[i] - 1)
            + 2 * (stride[i] - 1),
            stride[i],
        )
        if V.graph.sizevars.size_hint((x_alt - 1) * stride[i] - x - padding[i]) >= 0:
            # Sliding windows must start within the input or left padding
            x_alt -= 1  # type: ignore[assignment]
            V.graph.sizevars.guard_leq(0, x_alt * stride[i] - x - padding[i])  # type: ignore[arg-type]
        if V.graph.sizevars.size_hint(x_out - x_alt) == 0:
            # ceil mode is actually a no-op, lets guard on that
            V.graph.sizevars.guard_equals(x_out, x_alt)
            ceil_mode = False
        else:
            x_out = x_alt
    return x_out, ceil_mode



# ==================================================
# Line: 4360

def max_pool_checks(
    x, kernel_size, stride, padding, dilation, n_dim, *, assert_fallback=None

# ==================================================
# Line: 4389

def _max_pool_with_offsets(
    x,
    kernel_size,
    stride,
    padding,
    dilation,
    ceil_mode,
    *,
    n_dim,

# ==================================================
# Line: 4551

def _max_pool_with_indices(
    x,
    kernel_size,
    stride,
    padding,
    dilation,
    ceil_mode,
    n_dim,

# ==================================================
# Line: 4617

def max_pool2d_with_indices_backward(
    grad_output, x, kernel_size, stride, padding, dilation, ceil_mode, indices

# ==================================================
# Line: 5208

def avg_pool2d(
    x,
    kernel_size,
    stride=(),
    padding=0,
    ceil_mode=False,
    count_include_pad=True,
    divisor_override=None,

# ==================================================
# Line: 5230

def avg_pool3d(
    x,
    kernel_size,
    stride=(),
    padding=0,
    ceil_mode=False,
    count_include_pad=True,
    divisor_override=None,

# ==================================================
# Line: 5251

def _avg_poolnd(
    x,
    kernel_size,
    stride,
    padding,
    ceil_mode,
    count_include_pad,
    divisor_override,
    dim,

# ==================================================
# Line: 5379

def avg_pool2d_backward(
    grad_output,
    x,
    kernel_size,
    stride,
    padding,
    ceil_mode,
    count_include_pad,
    divisor_override=None,

# ==================================================
# Line: 5550

def avg_pool3d_backward(
    grad_output,
    x,
    kernel_size,
    stride,
    padding,
    ceil_mode,
    count_include_pad,
    divisor_override=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/cpp_builder.py
# Line: 418

def __init__(
    self,
    compiler: str = "",
    definitions: Optional[list[str]] = None,
    include_dirs: Optional[list[str]] = None,
    cflags: Optional[list[str]] = None,
    ldflags: Optional[list[str]] = None,
    libraries_dirs: Optional[list[str]] = None,
    libraries: Optional[list[str]] = None,
    passthrough_args: Optional[list[str]] = None,
    aot_mode: bool = False,
    use_relative_path: bool = False,
    compile_only: bool = False,
    precompiling: bool = False,
    preprocessing: bool = False,

# ==================================================
# Line: 695

def __init__(
    self,
    compile_only: bool = False,
    warning_all: bool = True,
    extra_flags: Sequence[str] = (),
    use_relative_path: bool = False,
    compiler: str = "",
    min_optimize: bool = False,
    precompiling: bool = False,
    preprocessing: bool = False,

# ==================================================
# Line: 1175

def __init__(
    self,
    vec_isa: VecISA = invalid_vec_isa,
    include_pytorch: bool = False,
    warning_all: bool = True,
    aot_mode: bool = False,
    compile_only: bool = False,
    use_relative_path: bool = False,
    use_mmap_weights: bool = False,
    shared: bool = True,
    extra_flags: Sequence[str] = (),
    compiler: str = "",
    min_optimize: bool = False,
    precompiling: bool = False,
    preprocessing: bool = False,

# ==================================================
# Line: 1347

def __init__(
    self,
    vec_isa: VecISA = invalid_vec_isa,
    include_pytorch: bool = False,
    device_type: str = "cuda",
    aot_mode: bool = False,
    compile_only: bool = False,
    use_relative_path: bool = False,
    use_mmap_weights: bool = False,
    shared: bool = True,
    extra_flags: Sequence[str] = (),
    min_optimize: bool = False,
    precompiling: bool = False,
    preprocessing: bool = False,

# ==================================================
# Line: 1619

def format_build_command(
    compiler: str,
    sources: str,
    include_dirs_args: str,
    definitions_args: str,
    cflags_args: str,
    ldflags_args: str,
    libraries_args: str,
    libraries_dirs_args: str,
    passthrough_args: str,
    output: str,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/mkldnn_ir.py
# Line: 30

def _prepare_convolution_fusion_create(
    cls,
    x: "TensorBox",
    weight: "TensorBox",
    bias: "TensorBox",
    padding: Sequence[int],
    stride: Sequence[int],
    dilation: Sequence[int],
    groups: int,
    transposed: bool = False,
    output_padding: Optional[Sequence[int]] = None,
    quantize_args: Optional[list["TensorBox"]] = None,
    other: Optional["TensorBox"] = None,

# ==================================================
# Line: 53

def _conv_input_size(
    output_size, weight_size, padding, output_padding, stride, dilation, groups

# ==================================================
# Line: 216

def _prepare_linear_fusion_create(
    cls,
    x: "TensorBox",
    weight: "TensorBox",
    bias: "TensorBox",
    quantize_args: Optional[list["TensorBox"]] = None,
    other: Optional["TensorBox"] = None,
    binary_sum: bool = False,

# ==================================================
# Line: 311

def create(
    cls,
    x: "TensorBox",
    weight: "TensorBox",
    bias: "TensorBox",
    padding_: list[int],
    stride_: list[int],
    dilation_: list[int],
    groups: int,
    attr,
    scalars: Optional[list[Any]],
    algorithm,

# ==================================================
# Line: 369

def create(
    cls,
    x: "TensorBox",
    other: "TensorBox",
    weight: "TensorBox",
    bias: "TensorBox",
    padding_: list[int],
    stride_: list[int],
    dilation_: list[int],
    groups: int,
    binary_attr: str,
    binary_alpha: Optional[float],
    unary_attr: Optional[str],
    unary_scalars: Optional[list[Any]],
    unary_algorithm: Optional[str],

# ==================================================
# Line: 443

def create(
    cls,
    x: "TensorBox",
    other: "TensorBox",
    weight: "TensorBox",
    bias: "TensorBox",
    padding_: list[int],
    stride_: list[int],
    dilation_: list[int],
    groups: int,
    binary_attr: str,
    binary_alpha: Optional[float],
    unary_attr: Optional[str],
    unary_scalars: Optional[list[Any]],
    unary_algorithm: Optional[str],

# ==================================================
# Line: 509

def create(
    cls,
    x: "TensorBox",
    weight: "TensorBox",
    bias: "TensorBox",
    padding_: list[int],
    output_padding_: list[int],
    stride_: list[int],
    dilation_: list[int],
    groups_: int,
    attr,
    scalars: Optional[list[Any]],
    algorithm,

# ==================================================
# Line: 589

def create(
    cls,
    qx: "TensorBox",
    x_scale: "TensorBox",
    x_zero_point: "TensorBox",
    qw: "TensorBox",  # qw
    w_scale: "TensorBox",
    w_zero_point: "TensorBox",
    bias: "TensorBox",
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    groups: int,
    output_scale: float,
    output_zero_point: int,
    output_dtype,
    attr,
    scalars,
    algorithm,

# ==================================================
# Line: 700

def create(
    cls,
    qx: "TensorBox",
    x_scale: "TensorBox",
    x_zero_point: "TensorBox",
    qw: "TensorBox",  # packed_weight
    w_scale,
    w_zero_point,
    qaccum: "TensorBox",
    bias: "TensorBox",
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    groups: int,
    output_scale: "TensorBox",
    output_zero_point: "TensorBox",
    output_dtype,
    accum_scale,
    accum_zero_point,
    binary_attr,
    alpha,
    unary_attr,
    unary_scalars,
    unary_algorithm,

# ==================================================
# Line: 846

def create(cls, x, w, B, attr, scalars, algorithm):
    x = cls.require_contiguous(cls.realize_input(x))
    w = cls.require_contiguous(cls.realize_input(w))

    *m, _ic = x.get_size()
    oc, _ic = w.get_size()
    output_size = list(m) + [oc]
    inputs = [x, w]
    constant_args = [attr, scalars if scalars else [-1], algorithm]
    if B is not None:
        B = cls.require_contiguous(cls.realize_input(B))
        inputs.append(B)
    else:
        constant_args.insert(0, None)

    packed = LinearUnary(
        layout=FixedLayout(
            device=x.get_device(),
            dtype=x.get_dtype(),
            size=output_size,
        ),
        inputs=inputs,
        constant_args=constant_args,
    )
    return _create_output_node(packed)


# ==================================================
# Line: 966

def create(
    cls,
    qx: "TensorBox",
    x_scale: "TensorBox",
    x_zero_point: "TensorBox",
    qw: "TensorBox",  # packed_weight
    w_scale: "TensorBox",
    w_zero_point: "TensorBox",
    bias: "TensorBox",
    output_scale: float,
    output_zero_point: int,
    output_dtype,
    post_op_name,
    post_op_args,
    post_op_algorithm,

# ==================================================
# Line: 1056

def create(
    cls,
    qx: "TensorBox",
    x_scale: "TensorBox",
    x_zero_point: "TensorBox",
    qw: "TensorBox",  # packed_weight
    w_scale: "TensorBox",
    w_zero_point: "TensorBox",
    other: "TensorBox",
    bias: "TensorBox",
    output_scale: float,
    output_zero_point: int,
    output_dtype,
    other_scale,
    other_zp,
    binary_post_op,
    binary_alpha,
    unary_post_op,
    unary_post_op_args,
    unary_post_op_algorithm,

# ==================================================
# Line: 1147

def create(
    cls,
    x: "TensorBox",
    w0: "TensorBox",
    w1: "TensorBox",
    w2: "TensorBox",
    w3: "TensorBox",
    hx: "TensorBox",
    cx: "TensorBox",
    reverse: bool,
    batch_sizes: list[int],
    mode: int,
    hidden_size: int,
    num_layers: int,
    has_biases: bool,
    bidirectional: bool,
    batch_first: bool,
    train: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autoheuristic/autoheuristic.py
# Line: 55

def __init__(
    self,
    fallback: Callable[[], Choice],
    choices: list[Choice],
    feedback: Optional[LocalFeedback],
    context: AHContext,
    name: str,
    augment_context: Optional[list[AHOperation]] = None,
    precondition: Optional[Callable[[AHMetadata, AHContext], bool]] = None,

# ==================================================
# Line: 223

def __init__(
    self,
    fallback: Callable[[], Optional[ChoiceCaller]],
    choices: list[ChoiceCaller],
    input_nodes: list[Any],
    context: AHContext,
    name: str,
    augment_context: Optional[list[AHOperation]] = None,
    precondition: Optional[Callable[[AHMetadata, AHContext], bool]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/cudagraph_trees.py
# Line: 423

def cudagraphify(
    model: ModelType,
    inputs: list[InputType],
    static_input_idxs: Sequence[int] = (),
    *,
    device_index: int,
    is_backward: bool,
    is_inference: bool,
    stack_traces: Optional[StackTraces] = None,
    constants: tuple[torch.Tensor, ...] = (),
    placeholders: tuple[PlaceholderInfo, ...] = (),
    mutated_input_idxs: tuple[int, ...] = (),
    compile_id: Optional[CompileId] = None,

# ==================================================
# Line: 612

def __init__(
    self,
    wrapped_function: WrappedFunction,
    parent: Optional[Union[CUDAGraphNode, CUDAWarmupNode]],
    cuda_graphs_pool: tuple[int, int],
    existing_cuda_graph: Optional[torch.cuda.CUDAGraph],
    device_index: int,
    stack_traces: Optional[StackTraces],
    stream: torch.cuda.Stream,
    already_warm: bool,
    id: GraphID,

# ==================================================
# Line: 799

def __init__(
    self,
    wrapped_function: WrappedFunction,
    id: GraphID,
    parent: Optional[CUDAGraphNode],
    inputs: list[InputType],
    cuda_graphs_pool: tuple[int, int],
    device_index: int,
    stack_traces: Optional[StackTraces],
    stream: torch.cuda.Stream,
    mode: Optional[CompilationMode],
    compile_id: Optional[CompileId],

# ==================================================
# Line: 2270

def add_function(
    self,
    model: ModelType,
    inputs: list[InputType],
    static_input_idxs: Sequence[int],
    stack_traces: Optional[StackTraces],
    mode: CompilationMode,
    constants: tuple[torch.Tensor, ...],
    placeholders: tuple[PlaceholderInfo, ...],
    mutated_input_idxs: tuple[int, ...],
    compile_id: Optional[CompileId],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/loop_body.py
# Line: 598

def bucketize(
    self,
    values: T,
    boundaries: tuple[str, sympy.Expr, sympy.Expr, sympy.Expr],
    boundary_indices: T,
    indexing_dtype: torch.dtype,
    right: bool,
    sorter: Optional[tuple[str, sympy.Expr]] = None,
    sorter_indices: Optional[T] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/graph.py
# Line: 291

def __init__(
    self,
    gm: torch.fx.GraphModule,
    example_inputs: Optional[Sequence[object]] = None,
    shape_env: Optional[ShapeEnv] = None,
    graph_id: Optional[int] = None,
    cpp_wrapper: bool = False,
    aot_mode: bool = False,
    layout_opt: Optional[bool] = None,
    extern_node_serializer: Optional[
        Callable[[list[ir.ExternKernelNode]], Any]
    ] = None,
    is_inference: bool = False,
    is_backward: bool = False,
    is_const_graph: bool = False,
    const_output_index: Optional[dict[str, int]] = None,
    const_wrapper_code: Optional[str] = None,
    const_kernel_code: Optional[str] = None,
    const_module: Optional[GraphLowering] = None,
    name: Optional[str] = None,
    inputs_to_check: Optional[Sequence[int]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/post_grad.py
# Line: 714

def scatter_upon_const_tensor(
    match: Match, shape, background_val, dtype, dim, selector, val

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/freezing_patterns.py
# Line: 195

def addmm_fuse_pattern_second(inp, w1, w2, w3, b1, b2, b3):
    return (
        aten.addmm(b1, inp, w1),
        aten.addmm(b2, inp, w2),
        aten.addmm(b3, inp, w3),
    )


# ==================================================
# Line: 202

def addmm_fuse_replacement_second(inp, w1, w2, w3, b1, b2, b3):
    cat_w = torch.cat((w1, w2, w3), dim=1)
    cat_b = torch.cat((b1, b2, b3))
    return aten.addmm(cat_b, inp, cat_w).chunk(3, dim=1)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/replace_random.py
# Line: 95

def replace_random(
    match: Match,
    size,
    *,
    generator=None,
    dtype=None,
    device=None,
    layout=None,
    pin_memory=None,

# ==================================================
# Line: 127

def replace_randint(
    match: Match,
    low,
    high,
    size,
    *,
    dtype=torch.int64,
    device=None,
    layout=None,
    pin_memory=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/efficient_conv_bn_eval.py
# Line: 78

def efficient_conv_bn_eval_decomposed(
    bn_weight,
    bn_bias,
    bn_running_mean,
    bn_running_var,
    bn_eps,
    conv: torch._ops.OpOverload,
    conv_weight,
    conv_bias,
    x,
    conv_remainging_args,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/b2b_gemm.py
# Line: 215

def load_ratio_left(
    M: int, N: int, O: int, P: int, m: int, n: int, o: int, p: int

# ==================================================
# Line: 237

def load_ratio_right(
    M: int, N: int, O: int, P: int, m: int, n: int, o: int, p: int

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/mkldnn_fusion.py
# Line: 630

def _register_binary_unary_maybe_inplace_fusion_lowering(
    pattern,
    computation_op,
    binary_op,
    inplace_fusion_op,
    outplace_fusion_op,
    unary_attr=None,
    other_index=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/joint_graph.py
# Line: 629

def fix_iota_device(match: Match, length, start, step, dtype, device, requires_grad):
    """
    Eager supports:

        aten.index(cuda_tensor, torch.arange(..., device="cpu"))

    But this results in an implicit host-device-copy and breaks cudagraphs.
    Rewrite the arange to use CUDA.
    """
    (node,) = match.nodes
    user_devices = OrderedSet[torch.device]()
    for user in node.users:
        if (
            user.op == "call_function"
            and user.target in (aten.index.Tensor, aten.index_put.default)
            and hasattr(user.meta.get("val"), "device")
        ):
            user_devices.add(user.meta["val"].device)  # type: ignore[union-attr]
        else:
            return  # bail out

    if len(user_devices) == 1 and "val" in node.meta:
        (user_device,) = user_devices
        if device.type != user_device.type:
            repl = match.graph.call_function(
                torch.ops.prims.iota.default,
                (length,),
                {
                    "start": start,
                    "step": step,
                    "dtype": dtype,
                    "device": user_device,
                    "requires_grad": requires_grad,
                },
            )
            repl.meta.update(node.meta)
            repl.meta["val"] = repl.meta["val"].to(user_device)
            node.replace_all_uses_with(repl)
            match.erase_nodes()



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/pad_mm.py
# Line: 153

def pad_addmm(
    input: Optional[Tensor],
    mat1: Tensor,
    mat2: Tensor,
    m_padded_length: int,
    k_padded_length: int,
    n_padded_length: int,
    beta: float = 1.0,
    alpha: float = 1.0,
    mat1_pre_padded: bool = False,
    mat2_pre_padded: bool = False,

# ==================================================
# Line: 621

def get_context(
    mat1: Tensor,
    mat2: Tensor,
    mat1_pre_padded: bool,
    mat2_pre_padded: bool,
    m_padded_length: int,
    k_padded_length: int,
    n_padded_length: int,

# ==================================================
# Line: 656

def run_autoheuristic(
    mat1: Tensor,
    mat2: Tensor,
    orig_bench_fn: Callable[[], None],
    pad_bench_fn: Callable[[], None],
    m_padded_length: int,
    k_padded_length: int,
    n_padded_length: int,
    do_bench: Callable[[Callable[[], Any]], float],
    mat1_pre_padded: bool,
    mat2_pre_padded: bool,
    ori_time: float,
    ori_time_key: str,
    key: str,

# ==================================================
# Line: 761

def pad_mm(
    mat1: Tensor,
    mat2: Tensor,
    m_padded_length: int,
    k_padded_length: int,
    n_padded_length: int,
    mat1_pre_padded: bool = False,
    mat2_pre_padded: bool = False,

# ==================================================
# Line: 810

def pad_bmm(
    mat1: Tensor,
    mat2: Tensor,
    m_padded_length: int,
    k_padded_length: int,
    n_padded_length: int,
    mat1_pre_padded: bool = False,
    mat2_pre_padded: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/micro_pipeline_tp.py
# Line: 796

def _insert_fused_matmul_reduce_scatter(
    graph: torch.fx.Graph,
    matmul: _Matmul,
    reduce_op: str,
    orig_scatter_dim: int,
    group_name: str,
    scatter_dim_after_reshape: int,  # only used for reshape -> scaled_mm -> reshape pattern
    output_shape: list[int],  # only used for reshape -> scaled_mm -> reshape pattern

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/split_cat.py
# Line: 2061

def update_args_from_split_getitem(
    graph: torch.fx.Graph,
    node: torch.fx.Node,
    getitem_indices: list[int],
    parents_seen: list[torch.fx.Node],
    new_cat_args: list[torch.fx.Node],
    new_cat_args_meta: list[torch.fx.Node],
    idx_to_getitems: dict[int, torch.fx.Node],
    threshold_to_cat: int = 2,

# ==================================================
# Line: 2154

def update_args_from_unbind_getitem(
    graph: torch.fx.Graph,
    node: torch.fx.Node,  # cat or stack node
    getitem_indices: list[int],
    parents_seen: list[torch.fx.Node],
    new_cat_args: list[torch.fx.Node],
    new_cat_args_meta: list[torch.fx.Node],
    idx_to_getitems: dict[int, torch.fx.Node],
    threshold_to_cat: int = 2,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/pre_grad.py
# Line: 436

def __init__(
    self,
    bn_node,
    conv_module,
    bn_module=None,  # For BN Module
    bn_running_mean=None,  # For Functional BN
    bn_running_var=None,
    bn_eps=None,
    bn_weight=None,
    bn_bias=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/mkldnn_lowerings.py
# Line: 127

def grouped_gemm_lowering(
    x: TensorBox,
    w: list[TensorBox],
    b: list[TensorBox],
    attr=None,
    scalars=None,
    algorithm=None,
    layout=None,

# ==================================================
# Line: 232

def convolution_unary(
    x: TensorBox,
    weight: TensorBox,
    bias: TensorBox,
    padding,
    stride,
    dilation,
    groups,
    attr,
    scalars,
    algorithm,

# ==================================================
# Line: 260

def convolution_binary(
    x: TensorBox,
    other: TensorBox,
    weight: TensorBox,
    bias: TensorBox,
    padding,
    stride,
    dilation,
    groups,
    binary_attr,
    binary_alpha,
    unary_attr,
    unary_scalars,
    unary_algorithm,

# ==================================================
# Line: 294

def convolution_binary_inplace(
    x: TensorBox,
    other: TensorBox,
    weight: TensorBox,
    bias: TensorBox,
    padding,
    stride,
    dilation,
    groups,
    binary_attr,
    binary_alpha,
    unary_attr,
    unary_scalars,
    unary_algorithm,

# ==================================================
# Line: 328

def linear_unary(
    x: TensorBox,
    w: TensorBox,
    b: TensorBox,
    attr,
    scalars,
    algorithm,
    layout=None,

# ==================================================
# Line: 456

def convolution_transpose_unary(
    x: TensorBox,
    weight: TensorBox,
    bias: TensorBox,
    padding,
    output_padding,
    stride,
    dilation,
    groups,
    attr,
    scalars,
    algorithm,

# ==================================================
# Line: 486

def mkldnn_rnn_layer(
    x: TensorBox,
    w0: TensorBox,
    w1: TensorBox,
    w2: TensorBox,
    w3: TensorBox,
    hx: TensorBox,
    cx: TensorBox,
    reverse: bool,
    batch_sizes: list[int],
    mode: int,
    hidden_size: int,
    num_layers: int,
    has_biases: bool,
    bidirectional: bool,
    batch_first: bool,
    train: bool,

# ==================================================
# Line: 527

def qconvolution_unary(
    x: TensorBox,
    x_scale,
    x_zp,
    packed_weight: TensorBox,
    w_scale: TensorBox,
    w_zp: TensorBox,
    bias: TensorBox,
    stride,
    padding,
    dilation,
    groups,
    o_inv_scale,
    o_zero_point,
    output_dtype,
    attr,
    scalars,
    algorithm,

# ==================================================
# Line: 584

def qconvolution_binary(
    x: TensorBox,
    x_scale,
    x_zp,
    packed_weight: TensorBox,
    w_scale: TensorBox,
    w_zp: TensorBox,
    accum: TensorBox,
    bias: TensorBox,
    stride,
    padding,
    dilation,
    groups,
    o_inv_scale,
    o_zero_point,
    output_dtype,
    accum_scale,
    accum_zp,
    binary_attr,
    alpha,
    unary_attr,
    unary_scalars,
    unary_algorithmm,

# ==================================================
# Line: 657

def qlinear_unary(
    x: TensorBox,
    x_scale,
    x_zp,
    packed_weight: TensorBox,
    w_scale: TensorBox,
    w_zp: TensorBox,
    bias: TensorBox,
    o_scale,
    o_zero_point,
    output_dtype,
    attr,
    scalars,
    algorithm,
    layout=None,

# ==================================================
# Line: 963

def qlinear_binary(
    x: TensorBox,
    x_scale,
    x_zp,
    packed_weight: TensorBox,
    w_scale: TensorBox,
    w_zp: TensorBox,
    x2: TensorBox,
    bias: TensorBox,
    o_scale,
    o_zero_point,
    output_dtype,
    x2_scale,
    x2_zp,
    binary_attr,
    alpha,
    unary_attr,
    unary_scalars,
    unary_algorithmm,
    layout=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/output_code.py
# Line: 432

def __init__(
    self,
    current_callable: Optional[Callable[..., Any]],
    graph: GraphLowering,
    gm: torch.fx.GraphModule,
    output_strides: list[Optional[tuple[_StrideExprStr, ...]]],
    disabled_cudagraphs_reason: Optional[str],
    metrics_deltas: metrics.CachedMetricsDeltas,
    counter_deltas: Counter[str],
    cudagraphs: BoxedBool,
    example_inputs: Sequence[InputType],
    static_input_idxs: Sequence[int],
    fx_kwargs: _CompileFxKwargs,
    inputs_to_check: Sequence[int],
    runnable_graph_str: str,
    inductor_post_grad_graph_str: str,
    compiled_fn_runner: Optional[Any] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/decomposition.py
# Line: 246

def convolution_backward(
    grad_output: torch.Tensor,
    input: torch.Tensor,
    weight: torch.Tensor,
    bias_sizes: list[int],
    stride: Union[int, list[int]],
    padding: Union[int, list[int]],
    dilation: Union[int, list[int]],
    transposed: bool,
    output_padding: list[int],
    groups: int,
    output_mask: list[bool],

# ==================================================
# Line: 620

def full_like(
    self: torch.Tensor,
    fill_value: Union[int, float],
    *,
    dtype: Optional[torch.dtype] = None,
    layout: Optional[torch.layout] = None,
    device: Optional[torch.device] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,
    memory_format: torch.memory_format = torch.preserve_format,

# ==================================================
# Line: 704

def wrapped_quantized_linear(
    input: torch.Tensor,
    input_scale: torch.Tensor,
    input_zero_point: torch.Tensor,
    weight: torch.Tensor,
    weight_scale: torch.Tensor,
    weight_zero_point: torch.Tensor,
    bias: torch.Tensor,
    out_scale: torch.Tensor,
    out_zero_point: torch.Tensor,
    out_channel: int,

# ==================================================
# Line: 829

def miopen_batch_norm(
    input: torch.Tensor,
    weight: torch.Tensor,
    bias: typing.Optional[torch.Tensor],
    running_mean: typing.Optional[torch.Tensor],
    running_var: typing.Optional[torch.Tensor],
    training: bool,
    exponential_average_factor: float,
    epsilon: float,

# ==================================================
# Line: 1008

def _max_pool_with_indices(
    x: torch.Tensor,
    kernel_size: list[int],
    stride: Optional[Union[int, list[int]]],
    padding: Union[int, list[int]],
    dilation: Union[int, list[int]],
    ceil_mode: bool,
    dim: int,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autotune_process.py
# Line: 574

def __init__(
    self,
    kernel_name: str,
    input_tensor_meta: Union[TensorMeta, list[TensorMeta]],
    output_tensor_meta: Union[TensorMeta, list[TensorMeta]],
    extra_args: Iterable[Any],
    module_path: str,  # the path of the module defining the triton kernel
    module_cache_key: str,
    num_stages: int,
    num_warps: int,
    num_consumer_groups: int = 0,
    num_buffers_warp_spec: int = 0,
    matrix_instr_nonkdim: int = 0,  # only used for hip to choose the shape of mfma instruction.
    waves_per_eu: int = 0,  # only used for hip to schedule waves per execution unit
    kpack: int = 0,  # ROCm specific gemm paramete

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_logging/_internal.py
# Line: 203

def set_logs(
    *,
    all: Optional[int] = None,
    dynamo: Optional[int] = None,
    aot: Optional[int] = None,
    autograd: Optional[int] = None,
    dynamic: Optional[int] = None,
    inductor: Optional[int] = None,
    distributed: Optional[int] = None,
    c10d: Optional[int] = None,
    ddp: Optional[int] = None,
    fsdp: Optional[int] = None,
    dtensor: Optional[int] = None,
    onnx: Optional[int] = None,
    bytecode: bool = False,
    aot_graphs: bool = False,
    aot_joint_graph: bool = False,
    ddp_graphs: bool = False,
    graph: bool = False,
    graph_code: bool = False,
    graph_code_verbose: bool = False,
    graph_breaks: bool = False,
    graph_sizes: bool = False,
    guards: bool = False,
    recompiles: bool = False,
    recompiles_verbose: bool = False,
    trace_source: bool = False,
    trace_call: bool = False,
    trace_bytecode: bool = False,
    output_code: bool = False,
    kernel_code: bool = False,
    schedule: bool = False,
    perf_hints: bool = False,
    pre_grad_graphs: bool = False,
    post_grad_graphs: bool = False,
    ir_pre_fusion: bool = False,
    ir_post_fusion: bool = False,
    onnx_diagnostics: bool = False,
    fusion: bool = False,
    overlap: bool = False,
    export: Optional[int] = None,
    modules: Optional[dict[str, Union[int, bool]]] = None,
    cudagraphs: bool = False,
    sym_node: bool = False,
    compiled_autograd: bool = False,
    compiled_autograd_verbose: bool = False,
    cudagraph_static_inputs: bool = False,
    benchmarking: bool = False,
    autotuning: bool = False,
    graph_region_expansion: bool = False,
    inductor_metrics: bool = False,
    hierarchical_compile: bool = False,

# ==================================================
# Line: 1219

def trace_structured(
    name: str,
    # NB: metadata expected to be dict so adding more info is forward compatible
    # Tuple[str, int] is a special case for string interning
    metadata_fn: Callable[[], Union[dict[str, Any], tuple[str, int]]] = dict,
    *,
    payload_fn: Callable[[], Optional[Union[str, object]]] = lambda: None,
    suppress_context: bool = False,
    expect_trace_id: bool = True,  # Whether or not we expect to have a current trace id
    record_logging_overhead: bool = True,  # Whether or not to record the time spent on structured logging
    compile_id: Optional[CompileId] = None,  # Optional if unavailable in the trace

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/nccl.py
# Line: 82

def reduce(
    inputs: Sequence[torch.Tensor],
    output: Optional[Union[torch.Tensor, Sequence[torch.Tensor]]] = None,
    root: int = 0,
    op: int = SUM,
    streams: Optional[Sequence[torch.cuda.Stream]] = None,
    comms=None,
    *,
    outputs: Optional[Sequence[torch.Tensor]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/_sanitizer.py
# Line: 350

def _handle_kernel_launch(
    self,
    stream: StreamId,
    read_only: set[DataPtr],
    read_write: set[DataPtr],
    outputs: set[DataPtr],
    operator: str,
    tensor_aliases: dict[int, list[str]],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/graphs.py
# Line: 404

def make_graphed_autograd_function(
    fwd_graph,
    bwd_graph,
    module_params,
    len_user_args,
    output_unflatten_spec,
    static_input_surface,
    static_outputs,
    static_grad_outputs,
    static_grad_inputs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/memory.py
# Line: 841

def _record_memory_history_legacy(
    enabled: bool,
    record_context=True,
    trace_alloc_max_entries=1,
    trace_alloc_record_context=False,
    device: "Device" = None,
    record_context_cpp=False,
    clear_history=False,
    compile_context=False,
    global_record_annotations=False,

# ==================================================
# Line: 909

def _record_memory_history_impl(
    enabled: Optional[str] = "all",
    context: Optional[str] = "all",
    stacks: str = "all",
    max_entries: int = sys.maxsize,
    device: "Device" = None,
    clear_history: bool = False,
    compile_context: bool = False,
    global_record_annotations: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/tunable.py
# Line: 440

def _create_matrices(
    m: int,
    n: int,
    k: int,
    lda: int,
    ldb: int,
    ldc: int,
    transA: bool,
    transB: bool,
    dtypeA: torch.dtype,
    deviceid: str,
    dtypeB: Optional[torch.dtype] = None,
    randn: bool = True,
    subMatrix: bool = False,

# ==================================================
# Line: 509

def _create_batch_matrices(
    m: int,
    n: int,
    k: int,
    b: int,
    lda: int,
    ldb: int,
    ldc: int,
    transA: bool,
    transB: bool,
    dtype: torch.dtype,
    deviceid: str,
    subMatrix: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/signal/windows/windows.py
# Line: 135

def exponential(
    M: int,
    *,
    center: Optional[float] = None,
    tau: float = 1.0,
    sym: bool = True,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    device: Optional[torch.device] = None,
    requires_grad: bool = False,

# ==================================================
# Line: 294

def gaussian(
    M: int,
    *,
    std: float = 1.0,
    sym: bool = True,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    device: Optional[torch.device] = None,
    requires_grad: bool = False,

# ==================================================
# Line: 373

def kaiser(
    M: int,
    *,
    beta: float = 12.0,
    sym: bool = True,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    device: Optional[torch.device] = None,
    requires_grad: bool = False,

# ==================================================
# Line: 711

def general_cosine(
    M,
    *,
    a: Iterable,
    sym: bool = True,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    device: Optional[torch.device] = None,
    requires_grad: bool = False,

# ==================================================
# Line: 806

def general_hamming(
    M,
    *,
    alpha: float = 0.54,
    sym: bool = True,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    device: Optional[torch.device] = None,
    requires_grad: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/hipify/hipify_python.py
# Line: 199

def preprocess_file_and_save_result(
        output_directory: str,
        filepath: str,
        all_files: Iterable,
        header_include_dirs: Iterable,
        stats: dict[str, list],
        hip_clang_launch: bool,
        is_pytorch_extension: bool,
        clean_ctx: GeneratedFileCleaner,
        show_progress: bool) -> None:
    fin_path = os.path.abspath(os.path.join(output_directory, filepath))
    hipify_result = HipifyResult(current_state=CurrentState.INITIALIZED, hipified_path=fin_path)
    HIPIFY_FINAL_RESULT[fin_path] = hipify_result
    result = preprocessor(output_directory, filepath, all_files, header_include_dirs, stats,
                          hip_clang_launch, is_pytorch_extension, clean_ctx, show_progress)

    # Show what happened
    if show_progress and "ignored" not in result.status:
        print(
            fin_path, "->",
            result.hipified_path, result.status, flush=True)

    HIPIFY_FINAL_RESULT[fin_path] = result



# ==================================================
# Line: 820

def preprocessor(
        output_directory: str,
        filepath: str,
        all_files: Iterable,
        header_include_dirs: Iterable,
        stats: dict[str, list],
        hip_clang_launch: bool,
        is_pytorch_extension: bool,
        clean_ctx: GeneratedFileCleaner,
        show_progress: bool) -> HipifyResult:
    """ Executes the CUDA -> HIP conversion on the specified file. """
    fin_path = os.path.abspath(os.path.join(output_directory, filepath))
    filepath = _to_unix_path(filepath)
    hipify_result = HIPIFY_FINAL_RESULT[fin_path]
    if filepath not in all_files:
        hipify_result.hipified_path = None
        hipify_result.status = "[ignored, not to be hipified]"
        hipify_result.current_state = CurrentState.DONE
        return hipify_result

    rel_filepath = _to_unix_path(os.path.relpath(filepath, output_directory))

    with open(fin_path, encoding='utf-8') as fin:
        if fin.readline() == HIPIFY_C_BREADCRUMB:
            hipify_result.hipified_path = None
            hipify_result.status = "[ignored, input is hipified output]"
            hipify_result.current_state = CurrentState.DONE
            return hipify_result
        fin.seek(0)
        output_source = fin.read()

    orig_output_source = output_source

    # get_hip_file_path needs a relative path to work correctly
    fout_path = os.path.abspath(os.path.join(output_directory, get_hip_file_path(rel_filepath, is_pytorch_extension)))
    if not os.path.exists(os.path.dirname(fout_path)):
        clean_ctx.makedirs(os.path.dirname(fout_path))

    # unsupported_calls statistics reporting is broken atm
    def pt_repl(m):
        return PYTORCH_MAP[m.group(0)]

    def pt_special_repl(m):
        # checks SPECIAL map first, and if a miss occurs, falls back to pytorch mappings
        return PYTORCH_SPECIAL_MAP.get(m.group(0), pt_repl(m))


    if is_pytorch_extension:
        output_source = RE_PYTORCH_PREPROCESSOR.sub(pt_repl, output_source)
    else:
        if is_special_file(rel_filepath):
            output_source = RE_PYTORCH_PREPROCESSOR.sub(pt_special_repl, output_source)
        elif is_pytorch_file(rel_filepath):
            output_source = RE_PYTORCH_PREPROCESSOR.sub(pt_repl, output_source)
        else:
            def c2_repl(m):
                return CAFFE2_MAP[m.group(0)]
            output_source = RE_CAFFE2_PREPROCESSOR.sub(c2_repl, output_source)

    # Header rewrites
    def mk_repl(templ, include_current_dir=True):
        def repl(m):
            f = m.group(1)
            filename = os.path.basename(f)
            if (
                f.startswith(("ATen/cuda",
                              "ATen/native/cuda",
                              "ATen/native/nested/cuda",
                              "ATen/native/quantized/cuda",
                              "ATen/native/sparse/cuda",
                              "ATen/native/transformers/cuda",
                              "THC/")) or
                (f.startswith("THC") and not f.startswith("THCP"))
            ):
                return templ.format(get_hip_file_path(m.group(1), is_pytorch_extension))
            # if filename is one of the files being hipified for this extension
            if (is_pytorch_extension and any(s.endswith(filename) for s in all_files)):
                header_dir = None
                header_filepath = None
                # If include_current_dir True, look first in same dir as the including source file
                if include_current_dir:
                    header_dir_to_check = os.path.dirname(fin_path)
                    header_path_to_check = os.path.abspath(os.path.join(header_dir_to_check, f))
                    if os.path.exists(header_path_to_check):
                        header_dir = header_dir_to_check
                        header_filepath = header_path_to_check
                # If not found, look in include dirs one by one and first match wins
                if header_filepath is None:
                    for header_include_dir in header_include_dirs:
                        header_dir_to_check = os.path.join(output_directory, header_include_dir)
                        header_path_to_check = os.path.abspath(os.path.join(header_dir_to_check, f))
                        if os.path.exists(header_path_to_check):
                            header_dir = header_dir_to_check
                            header_filepath = header_path_to_check
                # If header file not found, keep as is
                if header_filepath is None:
                    return m.group(0)
                # Hipify header file first if needed
                if header_filepath not in HIPIFY_FINAL_RESULT:
                    preprocess_file_and_save_result(output_directory,
                                                    header_filepath,
                                                    all_files, header_include_dirs, stats, hip_clang_launch,
                                                    is_pytorch_extension, clean_ctx, show_progress)
                elif header_filepath in HIPIFY_FINAL_RESULT:
                    header_result = HIPIFY_FINAL_RESULT[header_filepath]
                    if header_result.current_state == CurrentState.INITIALIZED:
                        # get_hip_file_path needs a relative path to work correctly
                        header_rel_path = os.path.relpath(header_filepath, output_directory)
                        header_fout_path = os.path.abspath(os.path.join(output_directory,
                                                                        get_hip_file_path(header_rel_path, is_pytorch_extension)))
                        header_result.hipified_path = header_fout_path
                        HIPIFY_FINAL_RESULT[header_filepath] = header_result
                        return templ.format(os.path.relpath(header_fout_path if header_fout_path is not None
                                                            else header_filepath, header_dir))
                hipified_header_filepath = HIPIFY_FINAL_RESULT[header_filepath].hipified_path
                return templ.format(_to_unix_path(os.path.relpath(hipified_header_filepath if hipified_header_filepath is not None
                                                                  else header_filepath, header_dir)))

            return m.group(0)
        return repl
    output_source = RE_QUOTE_HEADER.sub(mk_repl('#include "{0}"', True), output_source)
    output_source = RE_ANGLE_HEADER.sub(mk_repl('#include <{0}>', False), output_source)
    output_source = RE_THC_GENERIC_FILE.sub(mk_repl('#define THC_GENERIC_FILE "{0}"'), output_source)

    # CMakeLists.txt rewrites
    if filepath.endswith('CMakeLists.txt'):
        output_source = output_source.replace('CUDA', 'HIP')
        output_source = output_source.replace('THC', 'THH')
        output_source = RE_CU_SUFFIX.sub('.hip', output_source)

    # Perform Kernel Launch Replacements
    if not hip_clang_launch:
        output_source = processKernelLaunches(output_source, stats)

    # Replace std:: with non-std:: versions
    if (filepath.endswith((".cu", ".cuh"))) and "PowKernel" not in filepath:
        output_source = replace_math_functions(output_source)

    # Include header if device code is contained.
    output_source = hip_header_magic(output_source)

    # Replace the extern __shared__
    # NOTE: No longer needed after transition from hcc to hipclang.
    # output_source = replace_extern_shared(output_source)

    # Don't write out identical hipified files for extensions if dirpath has not changed
    if (
        is_pytorch_extension
        and orig_output_source == output_source
        and os.path.dirname(fin_path) == os.path.dirname(fout_path)
    ):
        hipify_result.hipified_path = fin_path
        hipify_result.status = "[skipped, no changes]"
        hipify_result.current_state = CurrentState.DONE
        return hipify_result

    # Add hipify breadcrumb for C-style files to avoid re-hipification
    if fin_path != fout_path and match_extensions(fin_path, (".cu", ".cuh", ".c", ".cc", ".cpp", ".h", ".hpp")):
        output_source = HIPIFY_C_BREADCRUMB + output_source

    do_write = True
    if os.path.exists(fout_path):
        with open(fout_path, encoding='utf-8') as fout_old:
            do_write = fout_old.read() != output_source
    if do_write:
        try:
            with clean_ctx.open(fout_path, 'w', encoding='utf-8') as fout:
                fout.write(output_source)
            hipify_result.hipified_path = fout_path
            hipify_result.status = "[ok]"
            hipify_result.current_state = CurrentState.DONE
            return hipify_result
        except OSError as e:
            print(f'{bcolors.WARNING}Failed to save {fout_path} with "{e.strerror}", leaving {fin_path} unchanged.{bcolors.ENDC}',
                  file=sys.stderr)
            hipify_result.hipified_path = fin_path
            hipify_result.status = "[skipped, no permissions]"
            hipify_result.current_state = CurrentState.DONE
            return hipify_result
    else:
        hipify_result.hipified_path = fout_path
        hipify_result.status = "[skipped, already hipified]"
        hipify_result.current_state = CurrentState.DONE
        return hipify_result


# ==================================================
# Line: 1094

def hipify(
    project_directory: str,
    show_detailed: bool = False,
    extensions: Iterable = (".cu", ".cuh", ".c", ".cc", ".cpp", ".h", ".in", ".hpp"),
    header_extensions: Iterable = (".cuh", ".h", ".hpp"),
    output_directory: str = "",
    header_include_dirs: Iterable = (),
    includes: Iterable = ('*',),
    extra_files: Iterable = (),
    out_of_place_only: bool = False,
    ignores: Iterable = (),
    show_progress: bool = True,
    hip_clang_launch: bool = False,
    is_pytorch_extension: bool = False,
    hipify_extra_files_only: bool = False,
    clean_ctx: Optional[GeneratedFileCleaner] = None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_cxx_pytree.py
# Line: 124

def register_pytree_node(
    cls: type[Any],
    flatten_fn: FlattenFunc,
    unflatten_fn: UnflattenFunc,
    *,
    serialized_type_name: Optional[str] = None,
    to_dumpable_context: Optional[ToDumpableContextFn] = None,
    from_dumpable_context: Optional[FromDumpableContextFn] = None,
    flatten_with_keys_fn: Optional[FlattenWithKeysFunc] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/flop_counter.py
# Line: 94

def _scaled_mm_flop(
    a_shape,
    b_shape,
    scale_a_shape,
    scale_b_shape,
    bias_shape=None,
    scale_result_shape=None,
    out_dtype=None,
    use_fast_accum=False,
    out_shape=None,
    **kwargs,

# ==================================================
# Line: 298

def _unpack_flash_attention_nested_shapes(
    *,
    query,
    key,
    value,
    grad_out=None,
    cum_seq_q,
    cum_seq_k,
    max_q,
    max_k,

# ==================================================
# Line: 344

def _unpack_efficient_attention_nested_shapes(
    *,
    query,
    key,
    value,
    grad_out=None,
    cu_seqlens_q,
    cu_seqlens_k,
    max_seqlen_q,
    max_seqlen_k,

# ==================================================
# Line: 393

def _flash_attention_forward_flop(
    query,
    key,
    value,
    cum_seq_q,
    cum_seq_k,
    max_q,
    max_k,
    *args,
    out_shape=None,
    **kwargs

# ==================================================
# Line: 425

def _efficient_attention_forward_flop(
    query,
    key,
    value,
    bias,
    cu_seqlens_q,
    cu_seqlens_k,
    max_seqlen_q,
    max_seqlen_k,
    *args,
    **kwargs

# ==================================================
# Line: 491

def _flash_attention_backward_flop(
    grad_out,
    query,
    key,
    value,
    out,  # named _out_shape to avoid kwarg collision with out_shape created in wrapper
    logsumexp,
    cum_seq_q,
    cum_seq_k,
    max_q,
    max_k,
    *args,
    **kwargs,

# ==================================================
# Line: 524

def _efficient_attention_backward_flop(
    grad_out,
    query,
    key,
    value,
    bias,
    out,  # named _out to avoid kwarg collision with out created in wrapper
    cu_seqlens_q,
    cu_seqlens_k,
    max_seqlen_q,
    max_seqlen_k,
    *args,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_config_module.py
# Line: 87

def __init__(
    self,
    default: Union[T, object] = _UNSET_SENTINEL,
    justknob: Optional[str] = None,
    env_name_default: Optional[Union[str, list[str]]] = None,
    env_name_force: Optional[Union[str, list[str]]] = None,
    value_type: Optional[type] = None,
    alias: Optional[str] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/show_pickle.py
# Line: 29

def pp_format(printer, obj, stream, indent, allowance, context, level):
    if not obj.args and obj.state is None:
        stream.write(repr(obj))
        return
    if obj.state is None:
        stream.write(f"{obj.module}.{obj.name}")
        printer._format(obj.args, stream, indent + 1, allowance + 1, context, level)
        return
    if not obj.args:
        stream.write(f"{obj.module}.{obj.name}()(state=\n")
        indent += printer._indent_per_level
        stream.write(" " * indent)
        printer._format(obj.state, stream, indent, allowance + 1, context, level + 1)
        stream.write(")")
        return
    raise Exception("Need to implement")  # noqa: TRY002



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_pytree.py
# Line: 201

def register_pytree_node(
    cls: type[Any],
    flatten_fn: FlattenFunc,
    unflatten_fn: UnflattenFunc,
    *,
    serialized_type_name: Optional[str] = None,
    to_dumpable_context: Optional[ToDumpableContextFn] = None,
    from_dumpable_context: Optional[FromDumpableContextFn] = None,
    flatten_with_keys_fn: Optional[FlattenWithKeysFunc] = None,

# ==================================================
# Line: 522

def _register_pytree_node(
    cls: type[Any],
    flatten_fn: FlattenFunc,
    unflatten_fn: UnflattenFunc,
    to_str_fn: Optional[ToStrFunc] = None,  # deprecated
    maybe_from_str_fn: Optional[MaybeFromStrFunc] = None,  # deprecated
    *,
    serialized_type_name: Optional[str] = None,
    to_dumpable_context: Optional[ToDumpableContextFn] = None,
    from_dumpable_context: Optional[FromDumpableContextFn] = None,
    flatten_with_keys_fn: Optional[FlattenWithKeysFunc] = None,

# ==================================================
# Line: 591

def _private_register_pytree_node(
    cls: type[Any],
    flatten_fn: FlattenFunc,
    unflatten_fn: UnflattenFunc,
    *,
    serialized_type_name: Optional[str] = None,
    to_dumpable_context: Optional[ToDumpableContextFn] = None,
    from_dumpable_context: Optional[FromDumpableContextFn] = None,
    flatten_with_keys_fn: Optional[FlattenWithKeysFunc] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_cpp_extension_versioner.py
# Line: 37

def bump_version_if_changed(self,
                            name,
                            source_files,
                            build_arguments,
                            build_directory,
                            with_cuda,
                            with_sycl,
                            is_python_module,
                            is_standalone):
    hash_value = 0
    hash_value = hash_source_files(hash_value, source_files)
    hash_value = hash_build_arguments(hash_value, build_arguments)
    hash_value = update_hash(hash_value, build_directory)
    hash_value = update_hash(hash_value, with_cuda)
    hash_value = update_hash(hash_value, with_sycl)
    hash_value = update_hash(hash_value, is_python_module)
    hash_value = update_hash(hash_value, is_standalone)

    entry = self.entries.get(name)
    if entry is None:
        self.entries[name] = entry = Entry(0, hash_value)
    elif hash_value != entry.hash:
        self.entries[name] = entry = Entry(entry.version + 1, hash_value)

    return entry.version

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/tensorboard/summary.py
# Line: 122

def _draw_single_box(
    image,
    xmin,
    ymin,
    xmax,
    ymax,
    display_str,
    color="black",
    color_text="black",
    thickness=2,

# ==================================================
# Line: 434

def histogram_raw(name, min, max, num, sum, sum_squares, bucket_limits, bucket_counts):
    # pylint: disable=line-too-long
    """Output a `Summary` protocol buffer with a histogram.

    The generated
    [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
    has one summary value containing a histogram for `values`.
    Args:
      name: A name for the generated node. Will also serve as a series name in
        TensorBoard.
      min: A float or int min value
      max: A float or int max value
      num: Int number of values
      sum: Float or int sum of all values
      sum_squares: Float or int sum of squares for all values
      bucket_limits: A numeric `Tensor` with upper value per bucket
      bucket_counts: A numeric `Tensor` with number of values per bucket
    Returns:
      A scalar `Tensor` of type `string`. The serialized `Summary` protocol
      buffer.
    """
    hist = HistogramProto(
        min=min,
        max=max,
        num=num,
        sum=sum,
        sum_squares=sum_squares,
        bucket_limit=bucket_limits,
        bucket=bucket_counts,
    )
    return Summary(value=[Summary.Value(tag=name, histo=hist)])



# ==================================================
# Line: 777

def pr_curve_raw(
    tag, tp, fp, tn, fn, precision, recall, num_thresholds=127, weights=None

# ==================================================
# Line: 863

def _get_tensor_summary(
    name, display_name, description, tensor, content_type, components, json_config

# ==================================================
# Line: 931

def mesh(
    tag, vertices, colors, faces, config_dict, display_name=None, description=None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/tensorboard/_pytorch_graph.py
# Line: 37

def __init__(
    self,
    debugName=None,
    inputs=None,
    scope=None,
    tensor_size=None,
    op_type="UnSpecified",
    attributes="",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/tensorboard/_proto_graph.py
# Line: 32

def node_proto(
    name,
    op="UnSpecified",
    input=None,
    dtype=None,
    shape: Optional[tuple] = None,
    outputsize=None,
    attributes="",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/tensorboard/writer.py
# Line: 182

def __init__(
    self,
    log_dir=None,
    comment="",
    purge_step=None,
    max_queue=10,
    flush_secs=120,
    filename_suffix="",

# ==================================================
# Line: 342

def add_scalar(
    self,
    tag,
    scalar_value,
    global_step=None,
    walltime=None,
    new_style=False,
    double_precision=False,

# ==================================================
# Line: 459

def add_histogram(
    self,
    tag,
    values,
    global_step=None,
    bins="tensorflow",
    walltime=None,
    max_bins=None,

# ==================================================
# Line: 502

def add_histogram_raw(
    self,
    tag,
    min,
    max,
    num,
    sum,
    sum_squares,
    bucket_limits,
    bucket_counts,
    global_step=None,
    walltime=None,

# ==================================================
# Line: 672

def add_image_with_boxes(
    self,
    tag,
    img_tensor,
    box_tensor,
    global_step=None,
    walltime=None,
    rescale=1,
    dataformats="CHW",
    labels=None,

# ==================================================
# Line: 853

def add_embedding(
    self,
    mat,
    metadata=None,
    label_img=None,
    global_step=None,
    tag="default",
    metadata_header=None,

# ==================================================
# Line: 958

def add_pr_curve(
    self,
    tag,
    labels,
    predictions,
    global_step=None,
    num_thresholds=127,
    weights=None,
    walltime=None,

# ==================================================
# Line: 1007

def add_pr_curve_raw(
    self,
    tag,
    true_positive_counts,
    false_positive_counts,
    true_negative_counts,
    false_negative_counts,
    precision,
    recall,
    global_step=None,
    num_thresholds=127,
    weights=None,
    walltime=None,

# ==================================================
# Line: 1118

def add_mesh(
    self,
    tag,
    vertices,
    colors=None,
    faces=None,
    config_dict=None,
    global_step=None,
    walltime=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/dataloader.py
# Line: 243

def __init__(
    self,
    dataset: Dataset[_T_co],
    batch_size: Optional[int] = 1,
    shuffle: Optional[bool] = None,
    sampler: Union[Sampler, Iterable, None] = None,
    batch_sampler: Union[Sampler[list], Iterable[list], None] = None,
    num_workers: int = 0,
    collate_fn: Optional[_collate_fn_t] = None,
    pin_memory: bool = False,
    drop_last: bool = False,
    timeout: float = 0,
    worker_init_fn: Optional[_worker_init_fn_t] = None,
    multiprocessing_context=None,
    generator=None,
    *,
    prefetch_factor: Optional[int] = None,
    persistent_workers: bool = False,
    pin_memory_device: str = "",
    in_order: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/_utils/worker.py
# Line: 228

def _worker_loop(
    dataset_kind,
    dataset,
    index_queue,
    data_queue,
    done_event,
    auto_collation,
    collate_fn,
    drop_last,
    base_seed,
    init_fn,
    worker_id,
    num_workers,
    persistent_workers,
    shared_seed,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/iter/filelister.py
# Line: 37

def __init__(
    self,
    root: Union[str, Sequence[str], IterDataPipe] = ".",
    masks: Union[str, list[str]] = "",
    *,
    recursive: bool = False,
    abspath: bool = False,
    non_deterministic: bool = False,
    length: int = -1,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/iter/grouping.py
# Line: 199

def __init__(
    self,
    datapipe: IterDataPipe[_T_co],
    group_key_fn: Callable[[_T_co], Any],
    *,
    keep_key: bool = False,
    buffer_size: int = 10000,
    group_size: Optional[int] = None,
    guaranteed_group_size: Optional[int] = None,
    drop_remaining: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/utils/common.py
# Line: 260

def _deprecation_warning(
    old_class_name: str,
    *,
    deprecation_version: str,
    removal_version: str,
    old_functional_name: str = "",
    old_argument_name: str = "",
    new_class_name: str = "",
    new_functional_name: str = "",
    new_argument_name: str = "",
    deprecate_functional_name_only: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/distributed.py
# Line: 66

def __init__(
    self,
    dataset: Dataset,
    num_replicas: Optional[int] = None,
    rank: Optional[int] = None,
    shuffle: bool = True,
    seed: int = 0,
    drop_last: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/compare.py
# Line: 81

def __init__(self, results, row_group, render_env, env_str_len,
             row_name_str_len, time_scale, colorize, num_threads=None):
    super().__init__()
    self._results = results
    self._row_group = row_group
    self._render_env = render_env
    self._env_str_len = env_str_len
    self._row_name_str_len = row_name_str_len
    self._time_scale = time_scale
    self._colorize = colorize
    self._columns: tuple[_Column, ...] = ()
    self._num_threads = num_threads


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/timer.py
# Line: 189

def __init__(
    self,
    stmt: str = "pass",
    setup: str = "pass",
    global_setup: str = "",
    timer: Callable[[], float] = timer,
    globals: Optional[dict[str, Any]] = None,
    label: Optional[str] = None,
    sub_label: Optional[str] = None,
    description: Optional[str] = None,
    env: Optional[str] = None,
    num_threads: int = 1,
    language: Union[Language, str] = Language.PYTHON,

# ==================================================
# Line: 292

def _threaded_measurement_loop(
    self,
    number: int,
    time_hook: Callable[[], float],
    stop_hook: Callable[[list[float]], bool],
    min_run_time: float,
    max_run_time: Optional[float] = None,
    callback: Optional[Callable[[int, float], NoReturn]] = None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/fuzzer.py
# Line: 182

def __init__(
    self,
    name: str,
    size: tuple[Union[str, int], ...],
    steps: Optional[tuple[Union[str, int], ...]] = None,
    probability_contiguous: float = 0.5,
    min_elements: Optional[int] = None,
    max_elements: Optional[int] = None,
    max_allocation_bytes: Optional[int] = None,
    dim_parameter: Optional[str] = None,
    roll_parameter: Optional[str] = None,
    dtype=torch.float32,
    cuda=False,
    tensor_constructor: Optional[Callable] = None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/sparse_fuzzer.py
# Line: 9

def __init__(
    self,
    name: str,
    size: tuple[Union[str, int], ...],
    min_elements: Optional[int] = None,
    max_elements: Optional[int] = None,
    dim_parameter: Optional[str] = None,
    sparse_dim: Optional[str] = None,
    nnz: Optional[str] = None,
    density: Optional[str] = None,
    coalesced: Optional[str] = None,
    dtype=torch.float32,
    cuda=False

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/compile.py
# Line: 74

def benchmark_compile(
    model: Union[torch.nn.Module, Callable],
    sample_input: Union[torch.Tensor, Any],
    num_iters: int = 5,
    backend: Optional[str] = None,
    mode: Optional[str] = "default",
    optimizer: Optional[torch.optim.Optimizer] = None,
    loss_fn : Union[torch.nn.Module, Callable, None] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py
# Line: 520

def collect_callgrind(
    self,
    task_spec: common.TaskSpec,
    globals: dict[str, Any],
    *,
    number: int,
    repeats: int,
    collect_baseline: bool,
    is_python: bool,
    retain_out_file: bool,

# ==================================================
# Line: 560

def _invoke(
    self,
    *,
    task_spec: common.TaskSpec,
    globals: dict[str, Any],
    number: int,
    repeats: int,
    collect_baseline: bool,
    is_python: bool,
    retain_out_file: bool,

# ==================================================
# Line: 749

def _construct_script(
    task_spec: common.TaskSpec,
    globals: GlobalsBridge,
    *,
    number: int,
    repeats: int,
    collect_baseline: bool,
    error_log: str,
    stat_log: str,
    bindings: Optional[CallgrindModuleType],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/cpp_extension.py
# Line: 751

def unix_wrap_ninja_compile(sources,
                            output_dir=None,
                            macros=None,
                            include_dirs=None,
                            debug=0,
                            extra_preargs=None,
                            extra_postargs=None,
                            depends=None):
    r"""Compiles sources by outputting a ninja file and running it."""
    # NB: I copied some lines from self.compiler (which is an instance
    # of distutils.UnixCCompiler). See the following link.
    # https://github.com/python/cpython/blob/f03a8f8d5001963ad5b5b28dbd95497e9cc15596/Lib/distutils/ccompiler.py#L564-L567
    # This can be fragile, but a lot of other repos also do this
    # (see https://github.com/search?q=_setup_compile&type=Code)
    # so it is probably OK; we'll also get CI signal if/when
    # we update our python version (which is when distutils can be
    # upgraded)

    # Use absolute path for output_dir so that the object file paths
    # (`objects`) get generated with absolute paths.
    output_dir = os.path.abspath(output_dir)

    # See Note [Absolute include_dirs]
    convert_to_absolute_paths_inplace(self.compiler.include_dirs)

    _, objects, extra_postargs, pp_opts, _ = \
        self.compiler._setup_compile(output_dir, macros,
                                     include_dirs, sources,
                                     depends, extra_postargs)
    common_cflags = self.compiler._get_cc_args(pp_opts, debug, extra_preargs)
    extra_cc_cflags = self.compiler.compiler_so[1:]
    with_cuda = any(map(_is_cuda_file, sources))
    with_sycl = any(map(_is_sycl_file, sources))

    # extra_postargs can be either:
    # - a dict mapping cxx/nvcc/sycl to extra flags
    # - a list of extra flags.
    if isinstance(extra_postargs, dict):
        post_cflags = extra_postargs['cxx']
    else:
        post_cflags = list(extra_postargs)
    if IS_HIP_EXTENSION:
        post_cflags = COMMON_HIP_FLAGS + post_cflags
    append_std17_if_no_std_present(post_cflags)

    cuda_post_cflags = None
    cuda_cflags = None
    if with_cuda:
        cuda_cflags = common_cflags
        if isinstance(extra_postargs, dict):
            cuda_post_cflags = extra_postargs['nvcc']
        else:
            cuda_post_cflags = list(extra_postargs)
        if IS_HIP_EXTENSION:
            cuda_post_cflags = cuda_post_cflags + _get_rocm_arch_flags(cuda_post_cflags)
            cuda_post_cflags = COMMON_HIP_FLAGS + COMMON_HIPCC_FLAGS + cuda_post_cflags
        else:
            cuda_post_cflags = unix_cuda_flags(cuda_post_cflags)
        append_std17_if_no_std_present(cuda_post_cflags)
        cuda_cflags = [shlex.quote(f) for f in cuda_cflags]
        cuda_post_cflags = [shlex.quote(f) for f in cuda_post_cflags]

    if isinstance(extra_postargs, dict) and 'nvcc_dlink' in extra_postargs:
        cuda_dlink_post_cflags = unix_cuda_flags(extra_postargs['nvcc_dlink'])
        cuda_dlink_post_cflags = [shlex.quote(f) for f in cuda_dlink_post_cflags]
    else:
        cuda_dlink_post_cflags = None

    sycl_post_cflags = None
    sycl_cflags = None
    sycl_dlink_post_cflags = None
    if with_sycl:
        sycl_cflags = extra_cc_cflags + common_cflags + _COMMON_SYCL_FLAGS
        sycl_cflags += _get_sycl_target_flags()
        if isinstance(extra_postargs, dict):
            sycl_post_cflags = extra_postargs['sycl']
        else:
            sycl_post_cflags = list(extra_postargs)
        append_std17_if_no_std_present(sycl_cflags)
        _append_sycl_std_if_no_std_present(sycl_cflags)
        host_cflags = extra_cc_cflags + common_cflags + post_cflags
        append_std17_if_no_std_present(host_cflags)
        # escaping quoted arguments to pass them thru SYCL compiler
        host_cflags = [item.replace('"', '\\\\"') for item in host_cflags]
        host_cflags = ' '.join(host_cflags)
        # Note the order: shlex.quote sycl_flags first, _wrap_sycl_host_flags
        # second. Reason is that sycl host flags are quoted, space containing
        # strings passed to SYCL compiler.
        sycl_cflags = [shlex.quote(f) for f in sycl_cflags]
        sycl_cflags += _wrap_sycl_host_flags(host_cflags)
        sycl_dlink_post_cflags = _SYCL_DLINK_FLAGS
        sycl_dlink_post_cflags += _get_sycl_device_flags()
        sycl_post_cflags = [shlex.quote(f) for f in sycl_post_cflags]

    _write_ninja_file_and_compile_objects(
        sources=sources,
        objects=objects,
        cflags=[shlex.quote(f) for f in extra_cc_cflags + common_cflags],
        post_cflags=[shlex.quote(f) for f in post_cflags],
        cuda_cflags=cuda_cflags,
        cuda_post_cflags=cuda_post_cflags,
        cuda_dlink_post_cflags=cuda_dlink_post_cflags,
        sycl_cflags=sycl_cflags,
        sycl_post_cflags=sycl_post_cflags,
        sycl_dlink_post_cflags=sycl_dlink_post_cflags,
        build_directory=output_dir,
        verbose=True,
        with_cuda=with_cuda,
        with_sycl=with_sycl)

    # Return *all* object filenames, not just the ones we just built.
    return objects


# ==================================================
# Line: 871

def win_wrap_single_compile(sources,
                            output_dir=None,
                            macros=None,
                            include_dirs=None,
                            debug=0,
                            extra_preargs=None,
                            extra_postargs=None,
                            depends=None):

    self.cflags = copy.deepcopy(extra_postargs)
    extra_postargs = None

    def spawn(cmd):
        # Using regex to match src, obj and include files
        src_regex = re.compile('/T(p|c)(.*)')
        src_list = [
            m.group(2) for m in (src_regex.match(elem) for elem in cmd)
            if m
        ]

        obj_regex = re.compile('/Fo(.*)')
        obj_list = [
            m.group(1) for m in (obj_regex.match(elem) for elem in cmd)
            if m
        ]

        include_regex = re.compile(r'((\-|\/)I.*)')
        include_list = [
            m.group(1)
            for m in (include_regex.match(elem) for elem in cmd) if m
        ]

        if len(src_list) >= 1 and len(obj_list) >= 1:
            src = src_list[0]
            obj = obj_list[0]
            if _is_cuda_file(src):
                if IS_HIP_EXTENSION:
                    nvcc = _get_hipcc_path()
                else:
                    nvcc = _join_cuda_home('bin', 'nvcc')
                if isinstance(self.cflags, dict):
                    cflags = self.cflags['nvcc']
                elif isinstance(self.cflags, list):
                    cflags = self.cflags
                else:
                    cflags = []

                if IS_HIP_EXTENSION:
                    cflags = win_hip_flags(cflags)
                else:
                    cflags = win_cuda_flags(cflags) + ['-std=c++17', '--use-local-env']
                    for ignore_warning in MSVC_IGNORE_CUDAFE_WARNINGS:
                        cflags = ['-Xcudafe', '--diag_suppress=' + ignore_warning] + cflags
                for flag in COMMON_MSVC_FLAGS:
                    cflags = ['-Xcompiler', flag] + cflags
                cmd = [nvcc, '-c', src, '-o', obj] + include_list + cflags
            elif isinstance(self.cflags, dict):
                cflags = COMMON_MSVC_FLAGS + self.cflags['cxx']
                append_std17_if_no_std_present(cflags)
                cmd += cflags
            elif isinstance(self.cflags, list):
                cflags = COMMON_MSVC_FLAGS + self.cflags
                append_std17_if_no_std_present(cflags)
                cmd += cflags

        return original_spawn(cmd)

    try:
        self.compiler.spawn = spawn
        return original_compile(sources, output_dir, macros,
                                include_dirs, debug, extra_preargs,
                                extra_postargs, depends)
    finally:
        self.compiler.spawn = original_spawn


# ==================================================
# Line: 946

def win_wrap_ninja_compile(sources,
                           output_dir=None,
                           macros=None,
                           include_dirs=None,
                           debug=0,
                           extra_preargs=None,
                           extra_postargs=None,
                           depends=None,
                           is_standalone=False):
    if not self.compiler.initialized:
        self.compiler.initialize()
    output_dir = os.path.abspath(output_dir)

    # Note [Absolute include_dirs]
    # Convert relative path in self.compiler.include_dirs to absolute path if any.
    # For ninja build, the build location is not local, but instead, the build happens
    # in a script-created build folder. Thus, relative paths lose their correctness.
    # To be consistent with jit extension, we allow user to enter relative include_dirs
    # in setuptools.setup, and we convert the relative path to absolute path here.
    convert_to_absolute_paths_inplace(self.compiler.include_dirs)

    _, objects, extra_postargs, pp_opts, _ = \
        self.compiler._setup_compile(output_dir, macros,
                                     include_dirs, sources,
                                     depends, extra_postargs)
    # Replace space with \ when using hipcc (hipcc passes includes to clang without ""s so clang sees space in include paths as new argument)
    if IS_HIP_EXTENSION:
        pp_opts = ["-I{}".format(s[2:].replace(" ", "\\")) if s.startswith('-I') else s for s in pp_opts]
    common_cflags = extra_preargs or []
    cflags = []
    if debug:
        cflags.extend(self.compiler.compile_options_debug)
    else:
        cflags.extend(self.compiler.compile_options)
    cflags = cflags + common_cflags + pp_opts + COMMON_MSVC_FLAGS
    if IS_HIP_EXTENSION:
        _set_hipcc_runtime_lib(is_standalone, debug)
        common_cflags.extend(COMMON_HIP_FLAGS)
    else:
        common_cflags.extend(COMMON_MSVC_FLAGS)
    with_cuda = any(map(_is_cuda_file, sources))

    # extra_postargs can be either:
    # - a dict mapping cxx/nvcc to extra flags
    # - a list of extra flags.
    if isinstance(extra_postargs, dict):
        post_cflags = extra_postargs['cxx']
    else:
        post_cflags = list(extra_postargs)
    if IS_HIP_EXTENSION:
        post_cflags = COMMON_HIP_FLAGS + post_cflags
    append_std17_if_no_std_present(post_cflags)

    cuda_post_cflags = None
    cuda_cflags = None
    if with_cuda:
        cuda_cflags = ['-std=c++17']
        for common_cflag in common_cflags:
            cuda_cflags.append('-Xcompiler')
            cuda_cflags.append(common_cflag)
        if not IS_HIP_EXTENSION:
            cuda_cflags.append('--use-local-env')
            for ignore_warning in MSVC_IGNORE_CUDAFE_WARNINGS:
                cuda_cflags.append('-Xcudafe')
                cuda_cflags.append('--diag_suppress=' + ignore_warning)
        cuda_cflags.extend(pp_opts)
        if isinstance(extra_postargs, dict):
            cuda_post_cflags = extra_postargs['nvcc']
        else:
            cuda_post_cflags = list(extra_postargs)
        if IS_HIP_EXTENSION:
            cuda_post_cflags = win_hip_flags(cuda_post_cflags)
        else:
            cuda_post_cflags = win_cuda_flags(cuda_post_cflags)
    cflags = _nt_quote_args(cflags)
    post_cflags = _nt_quote_args(post_cflags)
    if with_cuda:
        cuda_cflags = _nt_quote_args(cuda_cflags)
        cuda_post_cflags = _nt_quote_args(cuda_post_cflags)
    if isinstance(extra_postargs, dict) and 'nvcc_dlink' in extra_postargs:
        cuda_dlink_post_cflags = win_cuda_flags(extra_postargs['nvcc_dlink'])
    else:
        cuda_dlink_post_cflags = None

    _write_ninja_file_and_compile_objects(
        sources=sources,
        objects=objects,
        cflags=cflags,
        post_cflags=post_cflags,
        cuda_cflags=cuda_cflags,
        cuda_post_cflags=cuda_post_cflags,
        cuda_dlink_post_cflags=cuda_dlink_post_cflags,
        sycl_cflags=None,
        sycl_post_cflags=None,
        sycl_dlink_post_cflags=None,
        build_directory=output_dir,
        verbose=True,
        with_cuda=with_cuda,
        with_sycl=False)

    # Return *all* object filenames, not just the ones we just built.
    return objects

# ==================================================
# Line: 1561

def load(name,
         sources: Union[str, list[str]],
         extra_cflags=None,
         extra_cuda_cflags=None,
         extra_sycl_cflags=None,
         extra_ldflags=None,
         extra_include_paths=None,
         build_directory=None,
         verbose=False,
         with_cuda: Optional[bool] = None,
         with_sycl: Optional[bool] = None,
         is_python_module=True,
         is_standalone=False,
         keep_intermediates=True):
    """
    Load a PyTorch C++ extension just-in-time (JIT).

    To load an extension, a Ninja build file is emitted, which is used to
    compile the given sources into a dynamic library. This library is
    subsequently loaded into the current Python process as a module and
    returned from this function, ready for use.

    By default, the directory to which the build file is emitted and the
    resulting library compiled to is ``<tmp>/torch_extensions/<name>``, where
    ``<tmp>`` is the temporary folder on the current platform and ``<name>``
    the name of the extension. This location can be overridden in two ways.
    First, if the ``TORCH_EXTENSIONS_DIR`` environment variable is set, it
    replaces ``<tmp>/torch_extensions`` and all extensions will be compiled
    into subfolders of this directory. Second, if the ``build_directory``
    argument to this function is supplied, it overrides the entire path, i.e.
    the library will be compiled into that folder directly.

    To compile the sources, the default system compiler (``c++``) is used,
    which can be overridden by setting the ``CXX`` environment variable. To pass
    additional arguments to the compilation process, ``extra_cflags`` or
    ``extra_ldflags`` can be provided. For example, to compile your extension
    with optimizations, pass ``extra_cflags=['-O3']``. You can also use
    ``extra_cflags`` to pass further include directories.

    CUDA support with mixed compilation is provided. Simply pass CUDA source
    files (``.cu`` or ``.cuh``) along with other sources. Such files will be
    detected and compiled with nvcc rather than the C++ compiler. This includes
    passing the CUDA lib64 directory as a library directory, and linking
    ``cudart``. You can pass additional flags to nvcc via
    ``extra_cuda_cflags``, just like with ``extra_cflags`` for C++. Various
    heuristics for finding the CUDA install directory are used, which usually
    work fine. If not, setting the ``CUDA_HOME`` environment variable is the
    safest option.

    SYCL support with mixed compilation is provided. Simply pass SYCL source
    files (``.sycl``) along with other sources. Such files will be detected
    and compiled with SYCL compiler (such as Intel DPC++ Compiler) rather
    than the C++ compiler. You can pass additional flags to SYCL compiler
    via ``extra_sycl_cflags``, just like with ``extra_cflags`` for C++.
    SYCL compiler is expected to be found via system PATH environment
    variable.

    Args:
        name: The name of the extension to build. This MUST be the same as the
            name of the pybind11 module!
        sources: A list of relative or absolute paths to C++ source files.
        extra_cflags: optional list of compiler flags to forward to the build.
        extra_cuda_cflags: optional list of compiler flags to forward to nvcc
            when building CUDA sources.
        extra_sycl_cflags: optional list of compiler flags to forward to SYCL
            compiler when building SYCL sources.
        extra_ldflags: optional list of linker flags to forward to the build.
        extra_include_paths: optional list of include directories to forward
            to the build.
        build_directory: optional path to use as build workspace.
        verbose: If ``True``, turns on verbose logging of load steps.
        with_cuda: Determines whether CUDA headers and libraries are added to
            the build. If set to ``None`` (default), this value is
            automatically determined based on the existence of ``.cu`` or
            ``.cuh`` in ``sources``. Set it to `True`` to force CUDA headers
            and libraries to be included.
        with_sycl: Determines whether SYCL headers and libraries are added to
            the build. If set to ``None`` (default), this value is
            automatically determined based on the existence of ``.sycl`` in
            ``sources``. Set it to `True`` to force SYCL headers and
            libraries to be included.
        is_python_module: If ``True`` (default), imports the produced shared
            library as a Python module. If ``False``, behavior depends on
            ``is_standalone``.
        is_standalone: If ``False`` (default) loads the constructed extension
            into the process as a plain dynamic library. If ``True``, build a
            standalone executable.

    Returns:
        If ``is_python_module`` is ``True``:
            Returns the loaded PyTorch extension as a Python module.

        If ``is_python_module`` is ``False`` and ``is_standalone`` is ``False``:
            Returns nothing. (The shared library is loaded into the process as
            a side effect.)

        If ``is_standalone`` is ``True``.
            Return the path to the executable. (On Windows, TORCH_LIB_PATH is
            added to the PATH environment variable as a side effect.)

    Example:
        >>> # xdoctest: +SKIP
        >>> from torch.utils.cpp_extension import load
        >>> module = load(
        ...     name='extension',
        ...     sources=['extension.cpp', 'extension_kernel.cu'],
        ...     extra_cflags=['-O2'],
        ...     verbose=True)
    """
    return _jit_compile(
        name,
        [sources] if isinstance(sources, str) else sources,
        extra_cflags,
        extra_cuda_cflags,
        extra_sycl_cflags,
        extra_ldflags,
        extra_include_paths,
        build_directory or _get_build_directory(name, verbose),
        verbose,
        with_cuda,
        with_sycl,
        is_python_module,
        is_standalone,
        keep_intermediates=keep_intermediates)


# ==================================================
# Line: 1770

def format_precompiler_header_cmd(compiler, head_file, head_file_pch, common_cflags, torch_include_dirs, extra_cflags, extra_include_paths):
    return re.sub(
        r"[ \n]+",
        " ",
        f"""
            {compiler} -x c++-header {head_file} -o {head_file_pch} {torch_include_dirs} {extra_include_paths} {extra_cflags} {common_cflags}
        """,
    ).strip()


# ==================================================
# Line: 1861

def load_inline(name,
                cpp_sources,
                cuda_sources=None,
                sycl_sources=None,
                functions=None,
                extra_cflags=None,
                extra_cuda_cflags=None,
                extra_sycl_cflags=None,
                extra_ldflags=None,
                extra_include_paths=None,
                build_directory=None,
                verbose=False,
                with_cuda=None,
                with_sycl=None,
                is_python_module=True,
                with_pytorch_error_handling=True,
                keep_intermediates=True,
                use_pch=False,
                no_implicit_headers=False):
    r'''
    Load a PyTorch C++ extension just-in-time (JIT) from string sources.

    This function behaves exactly like :func:`load`, but takes its sources as
    strings rather than filenames. These strings are stored to files in the
    build directory, after which the behavior of :func:`load_inline` is
    identical to :func:`load`.

    See `the
    tests <https://github.com/pytorch/pytorch/blob/master/test/test_cpp_extensions_jit.py>`_
    for good examples of using this function.

    Sources may omit two required parts of a typical non-inline C++ extension:
    the necessary header includes, as well as the (pybind11) binding code. More
    precisely, strings passed to ``cpp_sources`` are first concatenated into a
    single ``.cpp`` file. This file is then prepended with ``#include
    <torch/extension.h>``

    Furthermore, if the ``functions`` argument is supplied, bindings will be
    automatically generated for each function specified. ``functions`` can
    either be a list of function names, or a dictionary mapping from function
    names to docstrings. If a list is given, the name of each function is used
    as its docstring.

    The sources in ``cuda_sources`` are concatenated into a separate ``.cu``
    file and  prepended with ``torch/types.h``, ``cuda.h`` and
    ``cuda_runtime.h`` includes. The ``.cpp`` and ``.cu`` files are compiled
    separately, but ultimately linked into a single library. Note that no
    bindings are generated for functions in ``cuda_sources`` per se. To bind
    to a CUDA kernel, you must create a C++ function that calls it, and either
    declare or define this C++ function in one of the ``cpp_sources`` (and
    include its name in ``functions``).

    The sources in ``sycl_sources`` are concatenated into a separate ``.sycl``
    file and  prepended with ``torch/types.h``, ``sycl/sycl.hpp`` includes.
    The ``.cpp`` and ``.sycl`` files are compiled separately, but ultimately
    linked into a single library. Note that no bindings are generated for
    functions in ``sycl_sources`` per se. To bind to a SYCL kernel, you must
    create a C++ function that calls it, and either declare or define this
    C++ function in one of the ``cpp_sources`` (and include its name
    in ``functions``).



    See :func:`load` for a description of arguments omitted below.

    Args:
        cpp_sources: A string, or list of strings, containing C++ source code.
        cuda_sources: A string, or list of strings, containing CUDA source code.
        sycl_sources: A string, or list of strings, containing SYCL source code.
        functions: A list of function names for which to generate function
            bindings. If a dictionary is given, it should map function names to
            docstrings (which are otherwise just the function names).
        with_cuda: Determines whether CUDA headers and libraries are added to
            the build. If set to ``None`` (default), this value is
            automatically determined based on whether ``cuda_sources`` is
            provided. Set it to ``True`` to force CUDA headers
            and libraries to be included.
        with_sycl: Determines whether SYCL headers and libraries are added to
            the build. If set to ``None`` (default), this value is
            automatically determined based on whether ``sycl_sources`` is
            provided. Set it to ``True`` to force SYCL headers
            and libraries to be included.
        with_pytorch_error_handling: Determines whether pytorch error and
            warning macros are handled by pytorch instead of pybind. To do
            this, each function ``foo`` is called via an intermediary ``_safe_foo``
            function. This redirection might cause issues in obscure cases
            of cpp. This flag should be set to ``False`` when this redirect
            causes issues.
        no_implicit_headers: If ``True``, skips automatically adding headers, most notably
            ``#include <torch/extension.h>`` and ``#include <torch/types.h>`` lines.
            Use this option to improve cold start times when you
            already include the necessary headers in your source code. Default: ``False``.

    Example:
        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CPP_EXT)
        >>> from torch.utils.cpp_extension import load_inline
        >>> source = """
        at::Tensor sin_add(at::Tensor x, at::Tensor y) {
          return x.sin() + y.sin();
        }
        """
        >>> module = load_inline(name='inline_extension',
        ...                      cpp_sources=[source],
        ...                      functions=['sin_add'])

    .. note::
        Since load_inline will just-in-time compile the source code, please ensure
        that you have the right toolchains installed in the runtime. For example,
        when loading C++, make sure a C++ compiler is available. If you're loading
        a CUDA extension, you will need to additionally install the corresponding CUDA
        toolkit (nvcc and any other dependencies your code has). Compiling toolchains
        are not included when you install torch and must be additionally installed.

        During compiling, by default, the Ninja backend uses #CPUS + 2 workers to build
        the extension. This may use up too many resources on some systems. One
        can control the number of workers by setting the `MAX_JOBS` environment
        variable to a non-negative number.
    '''
    build_directory = build_directory or _get_build_directory(name, verbose)

    if isinstance(cpp_sources, str):
        cpp_sources = [cpp_sources]
    cuda_sources = cuda_sources or []
    if isinstance(cuda_sources, str):
        cuda_sources = [cuda_sources]
    sycl_sources = sycl_sources or []
    if isinstance(sycl_sources, str):
        sycl_sources = [sycl_sources]

    if not no_implicit_headers:
        cpp_sources.insert(0, '#include <torch/extension.h>')

    if use_pch is True:
        # Using PreCompile Header('torch/extension.h') to reduce compile time.
        _check_and_build_extension_h_precompiler_headers(extra_cflags, extra_include_paths)
    else:
        remove_extension_h_precompiler_headers()

    # If `functions` is supplied, we create the pybind11 bindings for the user.
    # Here, `functions` is (or becomes, after some processing) a map from
    # function names to function docstrings.
    if functions is not None:
        module_def = []
        module_def.append('PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {')
        if isinstance(functions, str):
            functions = [functions]
        if isinstance(functions, list):
            # Make the function docstring the same as the function name.
            functions = {f: f for f in functions}
        elif not isinstance(functions, dict):
            raise ValueError(f"Expected 'functions' to be a list or dict, but was {type(functions)}")
        for function_name, docstring in functions.items():
            if with_pytorch_error_handling:
                module_def.append(f'm.def("{function_name}", torch::wrap_pybind_function({function_name}), "{docstring}");')
            else:
                module_def.append(f'm.def("{function_name}", {function_name}, "{docstring}");')
        module_def.append('}')
        cpp_sources += module_def

    cpp_source_path = os.path.join(build_directory, 'main.cpp')
    _maybe_write(cpp_source_path, "\n".join(cpp_sources))

    sources = [cpp_source_path]

    if cuda_sources:
        if not no_implicit_headers:
            cuda_sources.insert(0, '#include <torch/types.h>')
            cuda_sources.insert(1, '#include <cuda.h>')
            cuda_sources.insert(2, '#include <cuda_runtime.h>')

        cuda_source_path = os.path.join(build_directory, 'cuda.cu')
        _maybe_write(cuda_source_path, "\n".join(cuda_sources))

        sources.append(cuda_source_path)

    if sycl_sources:
        if not no_implicit_headers:
            sycl_sources.insert(0, '#include <torch/types.h>')
            sycl_sources.insert(1, '#include <sycl/sycl.hpp>')

        sycl_source_path = os.path.join(build_directory, 'sycl.sycl')
        _maybe_write(sycl_source_path, "\n".join(sycl_sources))

        sources.append(sycl_source_path)

    return _jit_compile(
        name,
        sources,
        extra_cflags,
        extra_cuda_cflags,
        extra_sycl_cflags,
        extra_ldflags,
        extra_include_paths,
        build_directory,
        verbose,
        with_cuda,
        with_sycl,
        is_python_module,
        is_standalone=False,
        keep_intermediates=keep_intermediates)



# ==================================================
# Line: 2063

def _jit_compile(name,
                 sources,
                 extra_cflags,
                 extra_cuda_cflags,
                 extra_sycl_cflags,
                 extra_ldflags,
                 extra_include_paths,
                 build_directory: str,
                 verbose: bool,
                 with_cuda: Optional[bool],
                 with_sycl: Optional[bool],
                 is_python_module,
                 is_standalone,
                 keep_intermediates=True) -> None:
    if is_python_module and is_standalone:
        raise ValueError("`is_python_module` and `is_standalone` are mutually exclusive.")

    if with_cuda is None:
        with_cuda = any(map(_is_cuda_file, sources))
    with_cudnn = any('cudnn' in f for f in extra_ldflags or [])
    if with_sycl is None:
        with_sycl = any(map(_is_sycl_file, sources))
    old_version = JIT_EXTENSION_VERSIONER.get_version(name)
    version = JIT_EXTENSION_VERSIONER.bump_version_if_changed(
        name,
        sources,
        build_arguments=[extra_cflags, extra_cuda_cflags, extra_ldflags, extra_include_paths],
        build_directory=build_directory,
        with_cuda=with_cuda,
        with_sycl=with_sycl,
        is_python_module=is_python_module,
        is_standalone=is_standalone,
    )
    if version > 0:
        if version != old_version and verbose:
            logger.info('The input conditions for extension module %s have changed.', name)
            logger.info('Bumping to version %s and re-building as %s_v%s...', version, name, version)
        name = f'{name}_v{version}'

    baton = FileBaton(os.path.join(build_directory, 'lock'))
    if baton.try_acquire():
        try:
            if version != old_version:
                with GeneratedFileCleaner(keep_intermediates=keep_intermediates) as clean_ctx:
                    if IS_HIP_EXTENSION and (with_cuda or with_cudnn):
                        hipify_result = hipify_python.hipify(
                            project_directory=build_directory,
                            output_directory=build_directory,
                            header_include_dirs=(extra_include_paths if extra_include_paths is not None else []),
                            extra_files=[os.path.abspath(s) for s in sources],
                            ignores=[_join_rocm_home('*'), os.path.join(_TORCH_PATH, '*')],  # no need to hipify ROCm or PyTorch headers
                            show_detailed=verbose,
                            show_progress=verbose,
                            is_pytorch_extension=True,
                            clean_ctx=clean_ctx
                        )

                        hipified_sources = set()
                        for source in sources:
                            s_abs = os.path.abspath(source)
                            hipified_sources.add(hipify_result[s_abs].hipified_path if s_abs in hipify_result else s_abs)

                        sources = list(hipified_sources)

                    _write_ninja_file_and_build_library(
                        name=name,
                        sources=sources,
                        extra_cflags=extra_cflags or [],
                        extra_cuda_cflags=extra_cuda_cflags or [],
                        extra_sycl_cflags=extra_sycl_cflags or [],
                        extra_ldflags=extra_ldflags or [],
                        extra_include_paths=extra_include_paths or [],
                        build_directory=build_directory,
                        verbose=verbose,
                        with_cuda=with_cuda,
                        with_sycl=with_sycl,
                        is_standalone=is_standalone)
            elif verbose:
                logger.debug('No modifications detected for re-loaded extension module %s, skipping build step...', name)
        finally:
            baton.release()
    else:
        baton.wait()

    if verbose:
        logger.info('Loading extension module %s...', name)

    if is_standalone:
        return _get_exec_path(name, build_directory)

    return _import_module_from_library(name, build_directory, is_python_module)


# ==================================================
# Line: 2163

def _write_ninja_file_and_compile_objects(
        sources: list[str],
        objects,
        cflags,
        post_cflags,
        cuda_cflags,
        cuda_post_cflags,
        cuda_dlink_post_cflags,
        sycl_cflags,
        sycl_post_cflags,
        sycl_dlink_post_cflags,
        build_directory: str,
        verbose: bool,
        with_cuda: Optional[bool],
        with_sycl: Optional[bool]) -> None:
    verify_ninja_availability()

    compiler = get_cxx_compiler()

    get_compiler_abi_compatibility_and_version(compiler)
    if with_cuda is None:
        with_cuda = any(map(_is_cuda_file, sources))
    if with_sycl is None:
        with_sycl = any(map(_is_sycl_file, sources))
    build_file_path = os.path.join(build_directory, 'build.ninja')
    if verbose:
        logger.debug('Emitting ninja build file %s...', build_file_path)

    # Create build_directory if it does not exist
    if not os.path.exists(build_directory):
        if verbose:
            logger.debug('Creating directory %s...', build_directory)
        # This is like mkdir -p, i.e. will also create parent directories.
        os.makedirs(build_directory, exist_ok=True)

    _write_ninja_file(
        path=build_file_path,
        cflags=cflags,
        post_cflags=post_cflags,
        cuda_cflags=cuda_cflags,
        cuda_post_cflags=cuda_post_cflags,
        cuda_dlink_post_cflags=cuda_dlink_post_cflags,
        sycl_cflags=sycl_cflags,
        sycl_post_cflags=sycl_post_cflags,
        sycl_dlink_post_cflags=sycl_dlink_post_cflags,
        sources=sources,
        objects=objects,
        ldflags=None,
        library_target=None,
        with_cuda=with_cuda,
        with_sycl=with_sycl)
    if verbose:
        logger.info('Compiling objects...')
    _run_ninja_build(
        build_directory,
        verbose,
        # It would be better if we could tell users the name of the extension
        # that failed to build but there isn't a good way to get it here.
        error_prefix='Error compiling objects for extension')



# ==================================================
# Line: 2224

def _write_ninja_file_and_build_library(
        name,
        sources: list[str],
        extra_cflags,
        extra_cuda_cflags,
        extra_sycl_cflags,
        extra_ldflags,
        extra_include_paths,
        build_directory: str,
        verbose: bool,
        with_cuda: Optional[bool],
        with_sycl: Optional[bool],
        is_standalone: bool = False) -> None:
    verify_ninja_availability()

    compiler = get_cxx_compiler()

    get_compiler_abi_compatibility_and_version(compiler)
    if with_cuda is None:
        with_cuda = any(map(_is_cuda_file, sources))
    if with_sycl is None:
        with_sycl = any(map(_is_sycl_file, sources))
    extra_ldflags = _prepare_ldflags(
        extra_ldflags or [],
        with_cuda,
        verbose,
        is_standalone)
    build_file_path = os.path.join(build_directory, 'build.ninja')
    if verbose:
        logger.debug('Emitting ninja build file %s...', build_file_path)

    # Create build_directory if it does not exist
    if not os.path.exists(build_directory):
        if verbose:
            logger.debug('Creating directory %s...', build_directory)
        # This is like mkdir -p, i.e. will also create parent directories.
        os.makedirs(build_directory, exist_ok=True)

    # NOTE: Emitting a new ninja build file does not cause re-compilation if
    # the sources did not change, so it's ok to re-emit (and it's fast).
    _write_ninja_file_to_build_library(
        path=build_file_path,
        name=name,
        sources=sources,
        extra_cflags=extra_cflags or [],
        extra_cuda_cflags=extra_cuda_cflags or [],
        extra_sycl_cflags=extra_sycl_cflags or [],
        extra_ldflags=extra_ldflags or [],
        extra_include_paths=extra_include_paths or [],
        with_cuda=with_cuda,
        with_sycl=with_sycl,
        is_standalone=is_standalone)

    if verbose:
        logger.info('Building extension module %s...', name)
    _run_ninja_build(
        build_directory,
        verbose,
        error_prefix=f"Error building extension '{name}'")



# ==================================================
# Line: 2630

def _write_ninja_file_to_build_library(path,
                                       name,
                                       sources,
                                       extra_cflags,
                                       extra_cuda_cflags,
                                       extra_sycl_cflags,
                                       extra_ldflags,
                                       extra_include_paths,
                                       with_cuda,
                                       with_sycl,
                                       is_standalone) -> None:
    extra_cflags = [flag.strip() for flag in extra_cflags]
    extra_cuda_cflags = [flag.strip() for flag in extra_cuda_cflags]
    extra_sycl_cflags = [flag.strip() for flag in extra_sycl_cflags]
    extra_ldflags = [flag.strip() for flag in extra_ldflags]
    extra_include_paths = [flag.strip() for flag in extra_include_paths]

    # Turn into absolute paths so we can emit them into the ninja build
    # file wherever it is.
    user_includes = [os.path.abspath(file) for file in extra_include_paths]

    # include_paths() gives us the location of torch/extension.h
    # TODO generalize with_cuda as specific device type.
    if with_cuda:
        system_includes = include_paths("cuda")
    else:
        system_includes = include_paths("cpu")
    # sysconfig.get_path('include') gives us the location of Python.h
    # Explicitly specify 'posix_prefix' scheme on non-Windows platforms to workaround error on some MacOS
    # installations where default `get_path` points to non-existing `/Library/Python/M.m/include` folder
    python_include_path = sysconfig.get_path('include', scheme='nt' if IS_WINDOWS else 'posix_prefix')
    if python_include_path is not None:
        system_includes.append(python_include_path)

    common_cflags = []
    if not is_standalone:
        common_cflags.append(f'-DTORCH_EXTENSION_NAME={name}')
        common_cflags.append('-DTORCH_API_INCLUDE_EXTENSION_H')

    common_cflags += [f"{x}" for x in _get_pybind11_abi_build_flags()]

    # Windows does not understand `-isystem` and quotes flags later.
    if IS_WINDOWS:
        common_cflags += [f'-I{include}' for include in user_includes + system_includes]
    else:
        common_cflags += [f'-I{shlex.quote(include)}' for include in user_includes]
        common_cflags += [f'-isystem {shlex.quote(include)}' for include in system_includes]

    if IS_WINDOWS:
        cflags = common_cflags + ['/std:c++17'] + extra_cflags
        cflags += COMMON_HIP_FLAGS if IS_HIP_EXTENSION else COMMON_MSVC_FLAGS
        cflags = _nt_quote_args(cflags)
    else:
        cflags = common_cflags + ['-fPIC', '-std=c++17'] + extra_cflags

    if with_cuda and IS_HIP_EXTENSION:
        cuda_flags = ['-DWITH_HIP'] + cflags + COMMON_HIP_FLAGS + COMMON_HIPCC_FLAGS
        cuda_flags += _get_rocm_arch_flags(cuda_flags)
        cuda_flags += extra_cuda_cflags
    elif with_cuda:
        cuda_flags = common_cflags + COMMON_NVCC_FLAGS + _get_cuda_arch_flags()
        if IS_WINDOWS:
            for flag in COMMON_MSVC_FLAGS:
                cuda_flags = ['-Xcompiler', flag] + cuda_flags
            for ignore_warning in MSVC_IGNORE_CUDAFE_WARNINGS:
                cuda_flags = ['-Xcudafe', '--diag_suppress=' + ignore_warning] + cuda_flags
            cuda_flags = cuda_flags + ['-std=c++17']
            cuda_flags = _nt_quote_args(cuda_flags)
            cuda_flags += _nt_quote_args(extra_cuda_cflags)
        else:
            cuda_flags += ['--compiler-options', "'-fPIC'"]
            cuda_flags += extra_cuda_cflags
            if not any(flag.startswith('-std=') for flag in cuda_flags):
                cuda_flags.append('-std=c++17')
            cc_env = os.getenv("CC")
            if cc_env is not None:
                cuda_flags = ['-ccbin', cc_env] + cuda_flags
    else:
        cuda_flags = None

    if with_sycl:
        sycl_cflags = cflags + _COMMON_SYCL_FLAGS
        sycl_cflags += _get_sycl_target_flags()
        sycl_cflags += extra_sycl_cflags
        _append_sycl_std_if_no_std_present(sycl_cflags)
        host_cflags = cflags
        # escaping quoted arguments to pass them thru SYCL compiler
        host_cflags = [item.replace('\\"', '\\\\"') for item in host_cflags]
        host_cflags = ' '.join(host_cflags)
        sycl_cflags += _wrap_sycl_host_flags(host_cflags)
        sycl_dlink_post_cflags = _SYCL_DLINK_FLAGS
        sycl_dlink_post_cflags += _get_sycl_device_flags()
    else:
        sycl_cflags = None
        sycl_dlink_post_cflags = None

    def object_file_path(source_file: str) -> str:
        # '/path/to/file.cpp' -> 'file'
        file_name = os.path.splitext(os.path.basename(source_file))[0]
        if _is_cuda_file(source_file) and with_cuda:
            # Use a different object filename in case a C++ and CUDA file have
            # the same filename but different extension (.cpp vs. .cu).
            target = f'{file_name}.cuda.o'
        elif _is_sycl_file(source_file) and with_sycl:
            target = f'{file_name}.sycl.o'
        else:
            target = f'{file_name}.o'
        return target

    objects = [object_file_path(src) for src in sources]
    ldflags = ([] if is_standalone else [SHARED_FLAG]) + extra_ldflags

    # The darwin linker needs explicit consent to ignore unresolved symbols.
    if IS_MACOS:
        ldflags.append('-undefined dynamic_lookup')
    elif IS_WINDOWS:
        ldflags = _nt_quote_args(ldflags)

    ext = EXEC_EXT if is_standalone else LIB_EXT
    library_target = f'{name}{ext}'

    _write_ninja_file(
        path=path,
        cflags=cflags,
        post_cflags=None,
        cuda_cflags=cuda_flags,
        cuda_post_cflags=None,
        cuda_dlink_post_cflags=None,
        sycl_cflags=sycl_cflags,
        sycl_post_cflags=[],
        sycl_dlink_post_cflags=sycl_dlink_post_cflags,
        sources=sources,
        objects=objects,
        ldflags=ldflags,
        library_target=library_target,
        with_cuda=with_cuda,
        with_sycl=with_sycl)



# ==================================================
# Line: 2769

def _write_ninja_file(path,
                      cflags,
                      post_cflags,
                      cuda_cflags,
                      cuda_post_cflags,
                      cuda_dlink_post_cflags,
                      sycl_cflags,
                      sycl_post_cflags,
                      sycl_dlink_post_cflags,
                      sources,
                      objects,
                      ldflags,
                      library_target,
                      with_cuda,
                      with_sycl) -> None:
    r"""Write a ninja file that does the desired compiling and linking.

    `path`: Where to write this file
    `cflags`: list of flags to pass to $cxx. Can be None.
    `post_cflags`: list of flags to append to the $cxx invocation. Can be None.
    `cuda_cflags`: list of flags to pass to $nvcc. Can be None.
    `cuda_post_cflags`: list of flags to append to the $nvcc invocation. Can be None.
    `cuda_dlink_post_cflags`: list of flags to append to the $nvcc device code link invocation. Can be None.
    `sycl_cflags`: list of flags to pass to SYCL compiler. Can be None.
    `sycl_post_cflags`: list of flags to append to the SYCL compiler invocation. Can be None.
    `sycl_dlink_post_cflags`: list of flags to append to the SYCL compiler device code link invocation. Can be None.

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_strobelight/cli_function_profiler.py
# Line: 71

def __init__(
    self,
    *,
    stop_at_error: bool = False,
    max_profile_duration_sec: int = 60 * 10,
    sample_each: float = 1e7,  # sample each sample_each cycles.
    run_user_name: str = "pytorch-strobelight-ondemand",
    timeout_wait_for_running_sec: int = 60,
    timeout_wait_for_finished_sec: int = 60,
    recorded_env_variables: Optional[list[str]] = None,
    sample_tags: Optional[list[str]] = None,
    stack_max_len: int = 127,
    async_stack_max_len: int = 127,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/multiprocessing/reductions.py
# Line: 123

def rebuild_meta_tensor(
    tensor_cls,
    tensor_size,
    tensor_stride,
    tensor_offset,
    dtype,
    storage_size_bytes,
    requires_grad,

# ==================================================
# Line: 155

def rebuild_cuda_tensor(
    tensor_cls,
    tensor_size,
    tensor_stride,
    tensor_offset,
    storage_cls,
    dtype,
    storage_device,
    storage_handle,
    storage_size_bytes,
    storage_offset_bytes,
    requires_grad,
    ref_counter_handle,
    ref_counter_offset,
    event_handle,
    event_sync_required,

# ==================================================
# Line: 403

def rebuild_nested_tensor(
    rebuild_buffer_func,
    rebuild_buffer_args,
    rebuild_sizes_func,
    rebuild_sizes_args,
    rebuild_strides_func,
    rebuild_strides_args,
    rebuild_offsets_func,
    rebuild_offsets_args,

# ==================================================
# Line: 458

def rebuild_sparse_compressed_tensor(
    rebuild_compressed_indices_func,
    rebuild_compressed_indices_args,
    rebuild_plain_indices_func,
    rebuild_plain_indices_args,
    rebuild_values_func,
    rebuild_values_args,
    shape,
    layout,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/node.py
# Line: 270

def __init__(
    self,
    graph: "Graph",
    name: str,
    op: str,
    target: "Target",
    args: tuple["Argument", ...],
    kwargs: dict[str, "Argument"],
    return_type: Optional[Any] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py
# Line: 998

def apply_padding(
    e1_var: TVar,
    e11: BinConstraintT,
    e2: BinConstraintT,
    e12: BinConstraintT,
    d2: list[DVar],
    d11: list[DVar],
    d12: list[DVar],
    counter: int,

# ==================================================
# Line: 1127

def create_equality_constraints_for_broadcasting(
    e1: TVar,
    e2: TVar,
    e11: TVar,
    e12: TVar,
    d1: list[DVar],
    d2: list[DVar],
    d11: list[DVar],
    d12: list[DVar],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/migrate_gradual_types/constraint.py
# Line: 396

def __init__(
    self,
    conv_result,
    input_var,
    c_out,
    kernel,
    padding,
    stride,
    dilation,
    matching_constraint_vars,

# ==================================================
# Line: 448

def __init__(
    self,
    maxpool_result,
    input_var,
    kernel,
    padding,
    stride,
    dilation,
    matching_constraint_vars,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/shape_inference/infer_symbol_values.py
# Line: 119

def update_equation(
    symints: list[Union[torch.SymInt, int]],
    init_symints: list[Union[torch.SymInt, int]],
    padding_constraints: defaultdict[torch.SymInt, list[Union[sp.Expr, int]]],
    init_eq: sp.Expr,
    new_mod_num: int,
    var: torch.SymInt,
    idx: int,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/meta_tracer.py
# Line: 163

def create_proxy(
    self,
    kind,
    target,
    args,
    kwargs,
    name=None,
    type_expr=None,
    proxy_factory_fn=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/proxy_tensor.py
# Line: 1102

def create_node(
    self,
    kind: str,
    target: Target,
    args: tuple[Argument, ...],
    kwargs: dict[str, Argument],
    name: Optional[str] = None,
    type_expr: Optional[Any] = None,

# ==================================================
# Line: 1996

def _restore_modes(
    self,
    prev_fake_tensor_mode: Optional[FakeTensorMode],
    prev_proxy_mode: Union[nullcontext, ProxyTorchDispatchMode],
    prev_proxy_function_mode: Union[nullcontext, PreDispatchTorchFunctionMode],
    prev_fx_tracer: Optional[PythonKeyTracer],
    prev_python_dispatcher_mode: Union[nullcontext, Any],
    prev_torch_fn_metadata_mode: Union[nullcontext, TorchFunctionMetadataMode],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/sym_node.py
# Line: 86

def __init__(
    self,
    expr,
    shape_env,
    pytype,
    hint: Optional[Union[int, float, bool]],
    constant=None,
    fx_node=None,
    optimized_summation=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/symbolic_shapes.py
# Line: 3627

def _init(
    self,
    *,
    allow_scalar_outputs: bool = True,
    allow_dynamic_output_shape_ops: bool = True,
    # NB: These are legacy configuration that help us make good choices
    # when the constraint/dynamic dims are not explicitly passed to us.
    # Ideally we will fix all call sites to be explicit and not have
    # implicit choices, but this apparently was pretty involved.
    assume_static_by_default: bool = False,
    # Note - On 0/1 specialization
    #
    # The following options affect decisions we make about eager
    # specialization.  Disabling them will increase trace time (as we do
    # more symbolic reasoning) and can also harm the quality of generated
    # code (because inductor may not be able to specialize for bounds
    # being equal--although if we later respecialize because of a guard,
    # your code may be just as good as it was before.)
    #
    # When True, eagerly specialize input sizes which have 0/1.
    specialize_zero_one: bool = True,
    # When True, assume input sizes which have the same size are
    # symbolically equal.
    duck_shape: Optional[bool] = None,
    # For debugging
    co_fields: Optional[dict[str, str]] = None,
    # When True, whenever safe, we will generate a deferred runtime assert
    # instead of a guard whenever we know that an expression must be True,
    # otherwise it would be an error, even for backed SymInts (where we
    # could ostensibly unconditionally generate guards).  This is useful
    # for export, where preventing "error checking" sizes from showing up
    # in guards is helpful, since these guards in some sense are overly
    # pedantic.  See also https://github.com/pytorch/pytorch/issues/121749
    prefer_deferred_runtime_asserts_over_guards: bool = False,
    # When True, does not emit or raise constraint violation errors on
    # implicit guards generated by ops, and defers to runtime assertions
    # in the graph instead. For export.
    allow_complex_guards_as_runtime_asserts: bool = False,
    # XXX Add any new settings that could affect FakeTensor evaluation
    # to: torch._subclasses.fake_tensor._ShapeEnvSettings
    trace_asserts: bool = False,

# ==================================================
# Line: 4474

def _create_symbolic_sizes_strides_storage_offset(
    self,
    # NB: SymInt is allowed here due to nested int, normally you don't
    # actually pass true symbolic sizes to this function
    ex_size: Sequence[IntLikeType],
    ex_stride: Sequence[IntLikeType],
    ex_storage_offset: IntLikeType,
    is_dim_dynamic: Sequence[bool],
    source: Source,
    *,
    symbolic_context: Optional[SymbolicContext] = None,

# ==================================================
# Line: 4588

def _compute_symbolic_stride(
    self,
    source: Source,
    size: Sequence[sympy.Expr],
    ex_size: Sequence[IntLikeType],
    ex_stride: Sequence[IntLikeType],
    dynamic_strides: Sequence[DimDynamic],
    constraint_strides: Sequence[
        Optional[Union[StrictMinMaxConstraint, RelaxedUnspecConstraint]]
    ],
    are_sizes_static: bool,
    symbolic_context: SymbolicContext,

# ==================================================
# Line: 4895

def create_symbol(
    self,
    val: int,
    source: Source,
    dynamic_dim: DimDynamic = DimDynamic.DUCK,
    constraint_dim: DimConstraint = None,  # NB: includes None
    positive: Optional[bool] = True,
    do_not_specialize_zero_one: bool = False,
    symbolic_context: Optional[StatelessSymbolicContext] = None,

# ==================================================
# Line: 5190

def produce_guards_verbose(
    self,
    placeholders: Sequence[FakeTensor],
    sources: Sequence[Source],
    source_ref: Callable[[Source], str] = lambda n: n.name(),
    *,
    guards: Optional[list[ShapeGuard]] = None,
    input_contexts: Optional[DimList[SymbolicContext]] = None,
    # Encodes user-specified input shape equations of the form s = s' and s = fn(s').
    # (See docs on EqualityConstraint for details of the encoding.)
    equalities_inputs: Optional[EqualityConstraint] = None,
    _simplified: bool = False,
    # Indicates if we should produce guards for known static values.
    ignore_static: bool = True,
    langs: tuple[str, ...] = ("python", "verbose_python"),

# ==================================================
# Line: 6209

def _maybe_evaluate_static(
    self,
    expr: sympy.Basic,
    *,
    unbacked_only: bool = False,
    compute_hint: bool = False,
    size_oblivious: bool = False,
    axioms: Optional[tuple[SympyBoolean]] = None,
    var_to_range: Optional[tuple[tuple[sympy.Symbol, ValueRanges]]] = None,

# ==================================================
# Line: 7274

def evaluate_expr(
    self,
    orig_expr: sympy.Basic,
    hint: Optional[Union[int, bool, float]] = None,
    fx_node: Optional[torch.fx.Node] = None,
    size_oblivious: bool = False,
    fallback_value: Optional[bool] = None,
    *,
    forcing_spec: bool = False,

# ==================================================
# Line: 7303

def _inner_evaluate_expr(
    self,
    orig_expr: sympy.Basic,
    hint: Optional[Union[int, bool, float]],
    fx_node: Optional[torch.fx.Node],
    size_oblivious: bool,
    forcing_spec: bool,
    _suppress_guards_tls: bool,
    fallback_value: Optional[bool] = None,

# ==================================================
# Line: 7345

def _evaluate_expr(
    self,
    orig_expr: sympy.Basic,
    hint: Optional[Union[bool, int, float]] = None,
    fx_node: Optional[torch.fx.Node] = None,
    size_oblivious: bool = False,
    fallback_value: Optional[bool] = None,
    *,
    forcing_spec: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/graph.py
# Line: 373

def _gen_python_code(
    self,
    nodes,
    root_module: str,
    namespace: _Namespace,
    *,
    verbose: bool = False,
    include_stride: bool = False,
    include_device: bool = False,
    colored: bool = False,

# ==================================================
# Line: 1066

def create_node(
    self,
    op: str,
    target: "Target",
    args: Optional[tuple["Argument", ...]] = None,
    kwargs: Optional[dict[str, "Argument"]] = None,
    name: Optional[str] = None,
    type_expr: Optional[Any] = None,

# ==================================================
# Line: 1605

def _python_code(
    self,
    root_module: str,
    namespace: _Namespace,
    *,
    verbose: bool = False,
    include_stride: bool = False,
    include_device: bool = False,
    colored: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/splitter_base.py
# Line: 327

def __init__(
    self,
    module: torch.fx.GraphModule,
    sample_input: Sequence[Any],
    operator_support: OperatorSupportBase,
    settings: _SplitterSettingBase,
    non_acc_submodule_name: str = "_run_on_cpu_",
    return_tuple: bool = False,
    nodes_finder: Optional[FxNetAccNodesFinder] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/net_min_base.py
# Line: 104

def __init__(
    self,
    module: torch.fx.GraphModule,
    sample_input: Tensors,
    compare_fn: Callable[
        [TensorOrTensors, TensorOrTensors, Names], tuple[float, bool]
    ],
    settings: _MinimizerSettingBase,
    module_exporter: Optional[
        Callable[[Tensors, torch.fx.GraphModule, str], None]
    ] = None,
    exclusion_fn: Optional[Callable[[NodeList, int, int], None]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/graph_drawer.py
# Line: 78

def __init__(
    self,
    graph_module: torch.fx.GraphModule,
    name: str,
    ignore_getattr: bool = False,
    ignore_parameters_and_buffers: bool = False,
    skip_node_names_in_args: bool = True,
    parse_stack_trace: bool = False,
    dot_graph_shape: Optional[str] = None,
    normalize_args: bool = False,

# ==================================================
# Line: 396

def _to_dot(
    self,
    graph_module: torch.fx.GraphModule,
    name: str,
    ignore_getattr: bool,
    ignore_parameters_and_buffers: bool,
    skip_node_names_in_args: bool,
    parse_stack_trace: bool,

# ==================================================
# Line: 487

def __init__(
    self,
    graph_module: torch.fx.GraphModule,
    name: str,
    ignore_getattr: bool = False,
    ignore_parameters_and_buffers: bool = False,
    skip_node_names_in_args: bool = True,
    parse_stack_trace: bool = False,
    dot_graph_shape: Optional[str] = None,
    normalize_args: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/proxy.py
# Line: 149

def create_node(
    self,
    kind: str,
    target: Target,
    args: tuple[Argument, ...],
    kwargs: dict[str, Argument],
    name: Optional[str] = None,
    type_expr: Optional[Any] = None,

# ==================================================
# Line: 215

def create_proxy(
    self,
    kind: str,
    target: Target,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    name: Optional[str] = None,
    type_expr: Optional[Any] = None,
    # fix noqa when updating bc tests
    proxy_factory_fn: Callable[[Node], "Proxy"] = None,  # noqa: RUF013

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_utils.py
# Line: 216

def _rebuild_tensor_v2(
    storage,
    storage_offset,
    size,
    stride,
    requires_grad,
    backward_hooks,
    metadata=None,

# ==================================================
# Line: 239

def _rebuild_tensor_v3(
    storage,
    storage_offset,
    size,
    stride,
    requires_grad,
    backward_hooks,
    dtype,
    metadata=None,

# ==================================================
# Line: 394

def _rebuild_wrapper_subclass(
    cls,
    dtype,
    size,
    stride,
    storage_offset,
    layout,
    device,
    requires_grad,

# ==================================================
# Line: 419

def _rebuild_qtensor(
    storage,
    storage_offset,
    size,
    stride,
    quantizer_params,
    requires_grad,
    backward_hooks,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_decomp/decompositions.py
# Line: 323

def rrelu_with_noise_backward(
    grad_output: Tensor,
    self: Tensor,
    noise: Tensor,
    lower: float,
    upper: float,
    training: bool,
    self_is_result: bool,

# ==================================================
# Line: 482

def _nll_loss_backward(
    grad_output: Tensor,
    self: Tensor,
    target: Tensor,
    weight: Optional[Tensor],
    reduction: int,
    ignore_index: int,
    total_weight: Tensor,

# ==================================================
# Line: 537

def nll_loss_backward(
    grad_output: Tensor,
    self: Tensor,
    target: Tensor,
    weight: Optional[Tensor],
    reduction: int,
    ignore_index: int,
    total_weight: Tensor,

# ==================================================
# Line: 581

def nll_loss2d_backward(
    grad_output: Tensor,
    self: Tensor,
    target: Tensor,
    weight: Optional[Tensor],
    reduction: int,
    ignore_index: int,
    total_weight: Tensor,

# ==================================================
# Line: 1512

def native_group_norm_backward(
    grad_output: Tensor,
    input: Tensor,
    mean: Tensor,
    rstd: Tensor,
    gamma: Optional[Tensor],
    N: int,
    C: int,
    HxW: int,
    group: int,
    output_mask: list[bool],

# ==================================================
# Line: 1600

def native_group_norm_backward_out(
    grad_output: Tensor,
    input: Tensor,
    mean: Tensor,
    rstd: Tensor,
    gamma: Optional[Tensor],
    N: int,
    C: int,
    HxW: int,
    group: int,
    output_mask: list[bool],
    *,
    out0: torch.Tensor,
    out1: torch.Tensor,
    out2: torch.Tensor,

# ==================================================
# Line: 1636

def native_layer_norm_backward(
    grad_out: Tensor,
    input: Tensor,
    normalized_shape: list[int],
    mean: Tensor,
    rstd: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    output_mask: list[bool],

# ==================================================
# Line: 1719

def native_layer_norm_backward_out(
    grad_out: Tensor,
    input: Tensor,
    normalized_shape: list[int],
    mean: Tensor,
    rstd: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    output_mask: list[bool],
    *,
    out0: torch.Tensor,
    out1: torch.Tensor,
    out2: torch.Tensor,

# ==================================================
# Line: 1745

def native_batch_norm_helper(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    training: bool,
    momentum: float,
    eps: float,
    functional: bool,

# ==================================================
# Line: 1829

def native_batch_norm(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    training: bool,
    momentum: float,
    eps: float,

# ==================================================
# Line: 1857

def native_batch_norm_decomposition(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    training: bool,
    momentum: float,
    eps: float,

# ==================================================
# Line: 1905

def _native_batch_norm_legit_no_training(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Tensor,
    running_var: Tensor,
    momentum: float,
    eps: float,

# ==================================================
# Line: 1927

def _native_batch_norm_legit(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Tensor,
    running_var: Tensor,
    training: bool,
    momentum: float,
    eps: float,

# ==================================================
# Line: 1959

def _native_batch_norm_legit_functional(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Tensor,
    running_var: Tensor,
    training: bool,
    momentum: float,
    eps: float,

# ==================================================
# Line: 1983

def _get_batch_norm_reserve_tensor(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Tensor,
    running_var: Tensor,
    eps: float,
    training: bool,

# ==================================================
# Line: 2013

def _batch_norm_with_update(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Tensor,
    running_var: Tensor,
    momentum: float,
    eps: float,

# ==================================================
# Line: 2040

def _batch_norm_with_update_functional(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Tensor,
    running_var: Tensor,
    momentum: float,
    eps: float,

# ==================================================
# Line: 2067

def _batch_norm_no_update(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    running_mean: Tensor,
    running_var: Tensor,
    momentum: float,
    eps: float,

# ==================================================
# Line: 2105

def _to_copy(
    x: Union[Tensor, NumberType],
    *,
    dtype: Optional[torch.dtype] = None,
    layout=None,
    device: Optional[torch.device] = None,
    pin_memory: bool = False,
    non_blocking: bool = False,
    memory_format: Optional[torch.memory_format] = None,

# ==================================================
# Line: 2160

def cudnn_batch_norm(
    input: Tensor,
    weight: Tensor,
    bias: Optional[Tensor],
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    training: bool,
    exponential_average_factor: float,
    epsilon: float,

# ==================================================
# Line: 2199

def batch_norm_backward(
    grad_out: Tensor,
    input: Tensor,
    weight: Optional[Tensor],
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    save_mean: Optional[Tensor],
    save_invstd: Optional[Tensor],
    train: bool,
    eps: float,
    output_mask: list[bool],
    reserve: Tensor,

# ==================================================
# Line: 2227

def native_batch_norm_backward(
    grad_out: Tensor,
    input: Tensor,
    weight: Optional[Tensor],
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    save_mean: Optional[Tensor],
    save_invstd: Optional[Tensor],
    train: bool,
    eps: float,
    output_mask: list[bool],

# ==================================================
# Line: 2332

def native_batch_norm_backward_out(
    grad_out: Tensor,
    input: Tensor,
    weight: Optional[Tensor],
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    save_mean: Optional[Tensor],
    save_invstd: Optional[Tensor],
    train: bool,
    eps: float,
    output_mask: list[bool],
    *,
    out0: torch.Tensor,
    out1: torch.Tensor,
    out2: torch.Tensor,

# ==================================================
# Line: 2371

def miopen_batch_norm_backward(
    input: Tensor,
    grad_output: Tensor,
    weight: Tensor,
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    save_mean: Optional[Tensor],
    save_var: Optional[Tensor],
    epsilon: float,

# ==================================================
# Line: 2397

def cudnn_batch_norm_backward(
    input: Tensor,
    grad_output: Tensor,
    weight: Tensor,
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    save_mean: Optional[Tensor],
    save_var: Optional[Tensor],
    epsilon: float,
    reserveSpace: Tensor,

# ==================================================
# Line: 3085

def one_layer_rnn_data(
    inp, hidden, params, has_biases, hidden_fn, batch_sizes, reverse=False

# ==================================================
# Line: 3218

def _rnn_helper(
    input,
    hidden,
    params,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,
    batch_first,
    layer_fn,

# ==================================================
# Line: 3262

def rnn_tanh_input(
    input,
    hx,
    params,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,
    batch_first,

# ==================================================
# Line: 3293

def rnn_relu_input(
    input,
    hx,
    params,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,
    batch_first,

# ==================================================
# Line: 3324

def rnn_relu_data(
    data,
    batch_sizes,
    hx,
    params,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,

# ==================================================
# Line: 3359

def rnn_tanh_data(
    data,
    batch_sizes,
    hx,
    params,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,

# ==================================================
# Line: 3391

def lstm_cell(inp, hx, cx, hh_weight, hh_bias, hr_weight, chunk_dim):
    gates = F.linear(hx, hh_weight, hh_bias) + inp
    chunked_gates = gates.chunk(4, chunk_dim)
    in_gate = chunked_gates[0].sigmoid()
    forget_gate = chunked_gates[1].sigmoid()
    cell_gate = chunked_gates[2].tanh()
    out_gate = chunked_gates[3].sigmoid()
    cy = forget_gate * cx + (in_gate * cell_gate)
    hy = out_gate * cy.tanh()
    hy = hy if hr_weight is None else F.linear(hy, hr_weight, None)

    return hy, cy



# ==================================================
# Line: 3549

def lstm_impl(
    input,
    hx,
    params,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,
    batch_first,

# ==================================================
# Line: 3583

def lstm_data_impl(
    data,
    batch_sizes,
    hx,
    params,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,

# ==================================================
# Line: 3634

def gru_impl_data(
    data,
    batch_sizes,
    hx,
    params,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,

# ==================================================
# Line: 3664

def gru_impl(
    input,
    hx,
    params,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,
    batch_first,

# ==================================================
# Line: 4967

def scaled_dot_product_flash_attention_for_cpu(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    *,
    attn_mask: Optional[Tensor] = None,
    scale: Optional[float] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_decomp/decompositions_for_jvp.py
# Line: 132

def native_layer_norm_backward(
    grad_out: Tensor,
    input: Tensor,
    normalized_shape: list[int],
    mean: Tensor,
    rstd: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    output_mask: list[bool],

# ==================================================
# Line: 216

def native_batch_norm_backward(
    grad_out: Tensor,
    input: Tensor,
    weight: Optional[Tensor],
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    save_mean: Optional[Tensor],
    save_invstd: Optional[Tensor],
    train: bool,
    eps: float,
    output_mask: list[bool],

# ==================================================
# Line: 298

def batch_norm_backward(
    grad_out: Tensor,
    input: Tensor,
    weight: Tensor,
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    save_mean: Optional[Tensor],
    save_var: Optional[Tensor],
    update: bool,
    eps: float,
    output_mask: list[bool],
    reserve: Tensor,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/__init__.py
# Line: 115

def export(
    model: torch.nn.Module
    | torch.export.ExportedProgram
    | torch.jit.ScriptModule
    | torch.jit.ScriptFunction,
    args: tuple[Any, ...] = (),
    f: str | os.PathLike | None = None,
    *,
    kwargs: dict[str, Any] | None = None,
    export_params: bool = True,
    verbose: bool | None = None,
    input_names: Sequence[str] | None = None,
    output_names: Sequence[str] | None = None,
    opset_version: int | None = None,
    dynamic_axes: Mapping[str, Mapping[int, str]]
    | Mapping[str, Sequence[int]]
    | None = None,
    keep_initializers_as_inputs: bool = False,
    dynamo: bool = False,
    # Dynamo only options
    external_data: bool = True,
    dynamic_shapes: dict[str, Any] | tuple[Any, ...] | list[Any] | None = None,
    custom_translation_table: dict[Callable, Callable | Sequence[Callable]]
    | None = None,
    report: bool = False,
    optimize: bool = True,
    verify: bool = False,
    profile: bool = False,
    dump_exported_program: bool = False,
    artifacts_dir: str | os.PathLike = ".",
    fallback: bool = False,
    # Deprecated options
    training: _C_onnx.TrainingMode = _C_onnx.TrainingMode.EVAL,
    operator_export_type: _C_onnx.OperatorExportTypes = _C_onnx.OperatorExportTypes.ONNX,
    do_constant_folding: bool = True,
    custom_opsets: Mapping[str, int] | None = None,
    export_modules_as_functions: bool | Collection[type[torch.nn.Module]] = False,
    autograd_inlining: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_helper.py
# Line: 762

def _topk_helper(
    g: jit_utils.GraphContext, input, k, dim, largest=True, sorted=False, out=None

# ==================================================
# Line: 1094

def __interpolate_helper(
    g: jit_utils.GraphContext,
    input,
    size,
    scale_factor,
    mode,
    align_corners,
    recompute_scale_factor,

# ==================================================
# Line: 1946

def _embedding_bag_helper(
    g: jit_utils.GraphContext,
    embedding_matrix,
    indices,
    offsets,
    scale_grad_by_freq,
    mode,
    sparse,
    per_sample_weights,
    include_last_offset,
    padding_idx,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset8.py
# Line: 121

def __interpolate(
    g: jit_utils.GraphContext,
    input,
    size,
    scale_factor,
    mode,
    align_corners,
    recompute_scale_factor,
    antialias,

# ==================================================
# Line: 349

def empty(
    g: jit_utils.GraphContext,
    sizes,
    dtype,
    layout,
    device,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 363

def empty_like(
    g: jit_utils.GraphContext,
    input,
    dtype,
    layout,
    device,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 384

def zeros_like(
    g: jit_utils.GraphContext,
    input,
    dtype,
    layout,
    device,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 405

def ones_like(
    g: jit_utils.GraphContext,
    input,
    dtype,
    layout,
    device,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 419

def full(
    g: jit_utils.GraphContext, sizes, value, dtype, layout, device, pin_memory=False

# ==================================================
# Line: 433

def full_like(
    g: jit_utils.GraphContext,
    input,
    fill_value,
    dtype,
    layout,
    device,
    pin_memory=False,
    memory_format=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/utils.py
# Line: 195

def export(
    model: torch.nn.Module | torch.jit.ScriptModule | torch.jit.ScriptFunction,
    args: tuple[Any, ...] | torch.Tensor,
    f: str,
    *,
    kwargs: dict[str, Any] | None = None,
    export_params: bool = True,
    verbose: bool = False,
    training: _C_onnx.TrainingMode = _C_onnx.TrainingMode.EVAL,
    input_names: Sequence[str] | None = None,
    output_names: Sequence[str] | None = None,
    operator_export_type: _C_onnx.OperatorExportTypes = _C_onnx.OperatorExportTypes.ONNX,
    opset_version: int | None = None,
    do_constant_folding: bool = True,
    dynamic_axes: Mapping[str, Mapping[int, str]]
    | Mapping[str, Sequence[int]]
    | None = None,
    keep_initializers_as_inputs: bool | None = None,
    custom_opsets: Mapping[str, int] | None = None,
    export_modules_as_functions: bool | Collection[type[torch.nn.Module]] = False,
    autograd_inlining: bool = True,

# ==================================================
# Line: 580

def _optimize_graph(
    graph: _C.Graph,
    operator_export_type: _C_onnx.OperatorExportTypes,
    _disable_torch_constant_prop: bool = False,
    fixed_batch_size: bool = False,
    params_dict=None,
    dynamic_axes=None,
    input_names=None,
    module=None,

# ==================================================
# Line: 1042

def _model_to_graph(
    model,
    args,
    verbose=False,
    input_names=None,
    output_names=None,
    operator_export_type=_C_onnx.OperatorExportTypes.ONNX,
    do_constant_folding=True,
    _disable_torch_constant_prop=False,
    fixed_batch_size=False,
    training=_C_onnx.TrainingMode.EVAL,
    dynamic_axes=None,

# ==================================================
# Line: 1359

def _export(
    model,
    args,
    f,
    export_params=True,
    verbose=False,
    training=_C_onnx.TrainingMode.EVAL,
    input_names=None,
    output_names=None,
    operator_export_type=_C_onnx.OperatorExportTypes.ONNX,
    export_type=None,
    opset_version=None,
    do_constant_folding=True,
    dynamic_axes=None,
    keep_initializers_as_inputs=None,
    fixed_batch_size=False,
    custom_opsets=None,
    add_node_names=True,
    onnx_shape_inference=True,
    export_modules_as_functions: Any = False,
    autograd_inlining=True,

# ==================================================
# Line: 1658

def _run_symbolic_function(
    graph: _C.Graph,
    block: _C.Block,
    node: _C.Node,
    inputs: Any,
    env: dict[_C.Value, _C.Value],
    values_in_env: set[_C.Value],
    new_nodes: list[_C.Node],
    operator_export_type=_C_onnx.OperatorExportTypes.ONNX,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset16.py
# Line: 121

def scatter_reduce(
    g: jit_utils.GraphContext,
    self: torch._C.Value,
    dim: int,
    index: torch._C.Value,
    src: torch._C.Value,
    reduce: str,
    include_self: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset18.py
# Line: 61

def col2im(
    g,
    input: _C.Value,
    output_size: _C.Value,
    kernel_size: _C.Value,
    dilation: Sequence[int],
    padding: Sequence[int],
    stride: Sequence[int],

# ==================================================
# Line: 229

def embedding_bag(
    g: jit_utils.GraphContext,
    embedding_matrix,
    indices,
    offsets,
    scale_grad_by_freq,
    mode,
    sparse,
    per_sample_weights,
    include_last_offset,
    padding_idx,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/ops/__init__.py
# Line: 73

def symbolic(
    domain_op: str,
    /,
    inputs: Sequence[torch.Tensor | None],
    attrs: dict[
        str,
        int
        | float
        | str
        | bool
        | Sequence[int]
        | Sequence[float]
        | Sequence[str]
        | Sequence[bool],
    ]
    | None = None,
    *,
    dtype: torch.dtype | int,
    shape: Sequence[int | torch.SymInt],
    version: int | None = None,
    metadata_props: dict[str, str] | None = None,

# ==================================================
# Line: 174

def symbolic_multi_out(
    domain_op: str,
    /,
    inputs: Sequence[torch.Tensor | None],
    attrs: dict[
        str,
        int
        | float
        | str
        | bool
        | Sequence[int]
        | Sequence[float]
        | Sequence[str]
        | Sequence[bool],
    ]
    | None = None,
    *,
    dtypes: Sequence[torch.dtype | int],
    shapes: Sequence[Sequence[int | torch.SymInt]],
    version: int | None = None,
    metadata_props: dict[str, str] | None = None,

# ==================================================
# Line: 282

def rotary_embedding(
    X: torch.Tensor,
    cos_cache: torch.Tensor,
    sin_cache: torch.Tensor,
    position_ids: torch.Tensor | None = None,
    *,
    interleaved: bool = False,
    num_heads: int = 0,
    rotary_embedding_dim: int = 0,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/ops/_symbolic_impl.py
# Line: 206

def _symbolic(
    inputs: Sequence[Optional[torch.Tensor]],
    op_type: str,
    onnx_dtype: int,
    *,
    shape: Sequence[Union[int, torch.SymInt]],
    attr_keys: Sequence[str],
    attr_types: Sequence[str],
    attr_pos: Sequence[tuple[int, int]],
    attr_ints: Sequence[int],
    attr_floats: Sequence[float],
    attr_strs: Sequence[str],
    metadata_props_keys: Sequence[str] = (),
    metadata_props_values: Sequence[str] = (),
    domain: str = "",
    version: Optional[int] = None,

# ==================================================
# Line: 231

def _(
    inputs: Sequence[torch.Tensor],
    op_type: str,
    onnx_dtype: int,
    *,
    shape: Sequence[Union[int, torch.SymInt]],
    attr_keys: Sequence[str],
    attr_types: Sequence[str],
    attr_pos: Sequence[tuple[int, int]],
    attr_ints: Sequence[int],
    attr_floats: Sequence[float],
    attr_strs: Sequence[str],
    metadata_props_keys: Sequence[str] = (),
    metadata_props_values: Sequence[str] = (),
    domain: str = "",
    version: Optional[int] = None,

# ==================================================
# Line: 268

def _symbolic_multi_out(
    inputs: Sequence[Optional[torch.Tensor]],
    op_type: str,
    onnx_dtypes: Sequence[int],
    *,
    shapes: Sequence[Sequence[Union[int, torch.SymInt]]],
    attr_keys: Sequence[str],
    attr_types: Sequence[str],
    attr_pos: Sequence[tuple[int, int]],
    attr_ints: Sequence[int],
    attr_floats: Sequence[float],
    attr_strs: Sequence[str],
    metadata_props_keys: Sequence[str] = (),
    metadata_props_values: Sequence[str] = (),
    domain: str = "",
    version: Optional[int] = None,

# ==================================================
# Line: 300

def _(
    inputs: Sequence[torch.Tensor],
    op_type: str,
    onnx_dtypes: Sequence[int],
    *,
    shapes: Sequence[Sequence[Union[int, torch.SymInt]]],
    attr_keys: Sequence[str],
    attr_types: Sequence[str],
    attr_pos: Sequence[tuple[int, int]],
    attr_ints: Sequence[int],
    attr_floats: Sequence[float],
    attr_strs: Sequence[str],
    metadata_props_keys: Sequence[str] = (),
    metadata_props_values: Sequence[str] = (),
    domain: str = "",
    version: Optional[int] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/ops/_impl.py
# Line: 33

def rotary_embedding(
    x: torch.Tensor,
    cos_cache: torch.Tensor,
    sin_cache: torch.Tensor,
    position_ids: Optional[torch.Tensor] = None,
    *,
    interleaved: bool = False,
    num_heads: int = 0,
    rotary_embedding_dim: int = 0,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_caffe2.py
# Line: 81

def conv_prepack(
    g: jit_utils.GraphContext, input, weight, bias, stride, padding, dilation, groups

# ==================================================
# Line: 93

def conv2d(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    scale,
    zero_point,

# ==================================================
# Line: 122

def conv2d_relu(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    scale,
    zero_point,

# ==================================================
# Line: 191

def _empty_affine_quantized(
    g: jit_utils.GraphContext,
    input,
    shape,
    scale,
    zero_point,
    dtype,
    pin_memory,
    memory_format,
    layout,

# ==================================================
# Line: 230

def max_pool2d(
    g: jit_utils.GraphContext,
    input,
    kernel_size,
    stride,
    padding,
    dilation,
    ceil_mode,

# ==================================================
# Line: 259

def avg_pool2d(
    g: jit_utils.GraphContext,
    input,
    kernel_size,
    stride,
    padding,
    ceil_mode,
    count_include_pad,
    divisor_override=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset14.py
# Line: 69

def batch_norm(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    running_mean,
    running_var,
    training,
    momentum,
    eps,
    cudnn_enabled,

# ==================================================
# Line: 137

def scaled_dot_product_attention(
    g: jit_utils.GraphContext,
    query: torch._C.Value,
    key: torch._C.Value,
    value: torch._C.Value,
    attn_mask: torch._C.Value | None = None,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    scale: torch._C.Value | None = None,
    enable_gqa: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset10.py
# Line: 125

def topk(g: jit_utils.GraphContext, self, k, dim, largest, sorted, out=None):
    return symbolic_helper._topk_helper(
        g, self, k, dim, largest=largest, sorted=sorted, out=out
    )



# ==================================================
# Line: 131

def _aten_max_pool_onnx(
    g: jit_utils.GraphContext,
    self: _C.Value,
    kernel_shape: Sequence[int],
    strides: Sequence[int],
    pads: Sequence[int],
    dilations: Sequence[int],
    ceil_mode: bool,
    unbatched_rank: int,

# ==================================================
# Line: 214

def _aten_max_pool_with_indices_onnx(
    g: jit_utils.GraphContext,
    self: _C.Value,
    kernel_shape: Sequence[int],
    strides: Sequence[int],
    pads: Sequence[int],
    dilations: Sequence[int],
    ceil_mode: bool,
    unbatched_rank: int,
    n_dims_one: Sequence[int],
    n_dims_zero: Sequence[int],
    n_dims_axes: Sequence[int],

# ==================================================
# Line: 315

def symbolic_fn(
    g: jit_utils.GraphContext,
    input: _C.Value,
    kernel_size: Sequence[int],
    stride: Sequence[int],
    padding: int | Sequence[int],
    dilation: Sequence[int],
    ceil_mode: bool,

# ==================================================
# Line: 405

def symbolic_fn(
    g,
    input: _C.Value,
    kernel_size: Sequence[int],
    stride: Sequence[int],
    padding: int | Sequence[int],
    ceil_mode: int,
    count_include_pad: int,
    divisor_override=None,

# ==================================================
# Line: 478

def __interpolate(
    g: jit_utils.GraphContext,
    input,
    size,
    scale_factor,
    mode,
    align_corners,
    recompute_scale_factor,
    antialias,

# ==================================================
# Line: 594

def embedding_bag(
    g: jit_utils.GraphContext,
    embedding_matrix,
    indices,
    offsets,
    scale_grad_by_freq,
    mode,
    sparse,
    per_sample_weights,
    include_last_offset,
    padding_idx,

# ==================================================
# Line: 900

def quantized_layer_norm(
    g: jit_utils.GraphContext,
    x,
    normalized_shape,
    weight,
    bias,
    eps,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 918

def quantized_group_norm(
    g: jit_utils.GraphContext,
    x,
    num_groups,
    weight,
    bias,
    eps,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 937

def quantized_instance_norm(
    g: jit_utils.GraphContext,
    q_input,
    weight,
    bias,
    eps,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 956

def quantized_conv1d_relu(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 980

def quantized_conv2d_relu(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1004

def quantized_conv3d_relu(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1028

def quantized_conv1d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1051

def quantized_conv2d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1074

def quantized_conv3d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1097

def quantized_conv_transpose1d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    output_padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1123

def quantized_conv_transpose2d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    output_padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1149

def quantized_conv_transpose3d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    output_padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset17.py
# Line: 40

def layer_norm(
    g: jit_utils.GraphContext,
    input: _C.Value,
    normalized_shape: Sequence[int],
    weight: _C.Value,
    bias: _C.Value,
    eps: float,
    cudnn_enable: bool,

# ==================================================
# Line: 75

def quantized_layer_norm(
    g: jit_utils.GraphContext,
    x,
    normalized_shape,
    weight,
    bias,
    eps,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 102

def stft(
    g: jit_utils.GraphContext,
    input: _C.Value,
    n_fft: int,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: Optional[_C.Value] = None,
    normalized: bool = False,
    onesided: Optional[bool] = True,
    return_complex: Optional[bool] = False,
    align_to_window: Optional[bool] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/verification.py
# Line: 812

def verify(
    model: _ModelType,
    input_args: _InputArgsType,
    input_kwargs: _InputKwargsType | None = None,
    do_constant_folding: bool = True,
    dynamic_axes: Mapping[str, Mapping[int, str] | Mapping[str, Sequence[int]]]
    | None = None,
    input_names: Sequence[str] | None = None,
    output_names: Sequence[str] | None = None,
    training: _C_onnx.TrainingMode = _C_onnx.TrainingMode.EVAL,
    opset_version: int | None = None,
    keep_initializers_as_inputs: bool = True,
    verbose: bool = False,
    fixed_batch_size: bool = False,
    use_external_data: bool = False,
    additional_test_inputs: Sequence[_InputArgsType] | None = None,
    options: VerificationOptions | None = None,

# ==================================================
# Line: 1504

def _partition_node(
    self,
    node: torch.Node,
    complete_upper_nodes_set: set[torch.Node],
    complete_lower_nodes_set: set[torch.Node],
    original_graph_outputs: set[torch.Value],
    covered_bridge_values: set[torch.Value],
    process_bridge_value: Callable[[torch.Value], torch.Value],

# ==================================================
# Line: 1741

def find_mismatch(
    model: torch.nn.Module | torch.jit.ScriptModule,
    input_args: tuple[Any, ...],
    do_constant_folding: bool = True,
    training: _C_onnx.TrainingMode = _C_onnx.TrainingMode.EVAL,
    opset_version: int | None = None,
    keep_initializers_as_inputs: bool = True,
    verbose: bool = False,
    options: VerificationOptions | None = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset11.py
# Line: 372

def __interpolate(
    g: jit_utils.GraphContext,
    input,
    size,
    scale_factor,
    mode,
    align_corners,
    recompute_scale_factor,
    antialias,

# ==================================================
# Line: 560

def topk(g: jit_utils.GraphContext, self, k, dim, largest, sorted, out=None):
    return symbolic_helper._topk_helper(
        g, self, k, dim, largest=largest, sorted=sorted, out=out
    )



# ==================================================
# Line: 1205

def embedding_bag(
    g: jit_utils.GraphContext,
    embedding_matrix,
    indices,
    offsets,
    scale_grad_by_freq,
    mode,
    sparse,
    per_sample_weights,
    include_last_offset,
    padding_idx,

# ==================================================
# Line: 1288

def normal(
    g: jit_utils.GraphContext,
    mean,
    std,
    sizes=None,
    generator=None,
    dtype=None,
    layout=None,
    device=None,
    pin_memory=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset9.py
# Line: 934

def embedding_bag(
    g: jit_utils.GraphContext,
    embedding_matrix,
    indices,
    offsets,
    scale_grad_by_freq,
    mode,
    sparse,
    per_sample_weights,
    include_last_offset,
    padding_idx,

# ==================================================
# Line: 1439

def symbolic_fn(g, input, kernel_size, stride, padding, dilation, ceil_mode):
    if set(tuple_fn(dilation)) != {1}:
        return symbolic_helper._unimplemented(name, "dilation", input)
    if not stride:
        stride = kernel_size
    padding = tuple(tuple_fn(padding))
    if ceil_mode:
        padding_ceil = get_pool_ceil_padding(input, kernel_size, stride, padding)
        padding = padding + tuple(a + b for (a, b) in zip(padding_ceil, padding))
    else:
        padding = padding * 2
    kwargs = {
        "kernel_shape_i": tuple_fn(kernel_size),
        "pads_i": padding,
        "strides_i": tuple_fn(stride),
    }
    # easy but hacky way to get flattened indices values
    # to be used to convert the indices values to non-flattened.
    # In ONNX the indices are computed as a flatten 1-D tensor,
    # so the values in indices are in [0, N x C x D1 x ... x Dn).
    # To convert the indices to the same format used by Pytorch,
    # we first execute a maxpool with a kernel and stride of 1 on the same input.
    # This will result in a tensor of indices in which each index will have it's own value.
    # Using this tensor as a reference, we extract the first index of each axis and subtract
    # it from each index of this axis in the indices to convert.
    # This step will result in a tensor were each dimension has values of indices within
    # the dimension it is in.
    # For more information :
    # https://github.com/pytorch/pytorch/pull/16455#issuecomment-460776407
    if return_indices:
        r, indices = g.op("MaxPool", input, outputs=2, **kwargs)
        _, flattened_indices = g.op(
            "MaxPool",
            input,
            outputs=2,
            kernel_shape_i=[1 for _ in range(ndims)],
            strides_i=[1 for _ in range(ndims)],
        )
        # convert indices to have non-flattened indices values
        s = symbolic_helper._slice_helper(
            g,
            flattened_indices,
            axes=[2 + i for i in range(ndims)],
            starts=list(tuple_fn(0)),
            ends=list(tuple_fn(1)),
        )
        indices = sub(g, indices, s)
        return r, indices
    else:
        r = g.op("MaxPool", input, outputs=1, **kwargs)
        return r


# ==================================================
# Line: 1544

def symbolic_fn(
    g,
    input: _C.Value,
    kernel_size: Sequence[int],
    stride: Sequence[int],
    padding: int | Sequence[int],
    ceil_mode: int,
    count_include_pad: int,
    divisor_override=None,

# ==================================================
# Line: 1913

def __interpolate(
    g: jit_utils.GraphContext,
    input,
    size,
    scale_factor,
    mode,
    align_corners,
    recompute_scale_factor,
    antialias,

# ==================================================
# Line: 2259

def _convolution(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    stride,
    padding,
    dilation,
    transposed,
    output_padding,
    groups,
    benchmark,
    deterministic,
    cudnn_enabled,
    allow_tf32=None,

# ==================================================
# Line: 2336

def _convolution_mode(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    stride,
    padding,
    dilation,
    groups,

# ==================================================
# Line: 2393

def convolution(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    stride,
    padding,
    dilation,
    transposed,
    output_padding,
    groups,

# ==================================================
# Line: 2425

def conv1d(
    g: jit_utils.GraphContext, input, weight, bias, stride, padding, dilation, groups

# ==================================================
# Line: 2462

def conv2d(
    g: jit_utils.GraphContext, input, weight, bias, stride, padding, dilation, groups

# ==================================================
# Line: 2499

def conv3d(
    g: jit_utils.GraphContext, input, weight, bias, stride, padding, dilation, groups

# ==================================================
# Line: 2536

def conv_transpose1d(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    stride,
    padding,
    output_padding,
    groups,
    dilation,

# ==================================================
# Line: 2567

def conv_transpose2d(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    stride,
    padding,
    output_padding,
    groups,
    dilation,

# ==================================================
# Line: 2598

def conv_transpose3d(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    stride,
    padding,
    output_padding,
    groups,
    dilation,

# ==================================================
# Line: 2629

def batch_norm(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    running_mean,
    running_var,
    training,
    momentum,
    eps,
    cudnn_enabled,

# ==================================================
# Line: 2766

def layer_norm(
    g: jit_utils.GraphContext,
    input: _C.Value,
    normalized_shape: Sequence[int],
    weight: _C.Value,
    bias: _C.Value,
    eps: float,
    cudnn_enable: bool,

# ==================================================
# Line: 2781

def instance_norm(
    g: jit_utils.GraphContext,
    input,
    weight,
    bias,
    running_mean,
    running_var,
    use_input_stats: bool,
    momentum: Number,
    eps: Number,
    cudnn_enabled: bool,

# ==================================================
# Line: 3374

def empty(
    g: jit_utils.GraphContext,
    sizes,
    dtype,
    layout,
    device,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 3388

def empty_like(
    g: jit_utils.GraphContext,
    input,
    dtype=None,
    layout=None,
    device=None,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 3401

def new_empty(
    g: jit_utils.GraphContext, self, sizes, dtype, layout, device, pin_memory=False

# ==================================================
# Line: 3472

def zeros_like(
    g: jit_utils.GraphContext,
    input,
    dtype=None,
    layout=None,
    device=None,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 3496

def new_zeros(
    g: jit_utils.GraphContext, self, sizes, dtype, layout, device, pin_memory=False

# ==================================================
# Line: 3531

def ones_like(
    g: jit_utils.GraphContext,
    input,
    dtype=None,
    layout=None,
    device=None,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 3555

def new_ones(
    g: jit_utils.GraphContext, self, sizes, dtype, layout, device, pin_memory=False

# ==================================================
# Line: 3565

def full(
    g: jit_utils.GraphContext, sizes, value, dtype, layout, device, pin_memory=False

# ==================================================
# Line: 3590

def full_like(
    g: jit_utils.GraphContext,
    input,
    fill_value,
    dtype=None,
    layout=None,
    device=None,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 3622

def new_full(
    g: jit_utils.GraphContext,
    self,
    size,
    fill_value,
    dtype,
    layout,
    device,
    pin_memory=False,

# ==================================================
# Line: 3885

def topk(g: jit_utils.GraphContext, self, k, dim, largest, sorted, out=None):
    if out is not None:
        symbolic_helper._unimplemented(
            "TopK", "Out parameter is not supported for topk", self
        )
    if not largest:
        symbolic_helper._unimplemented("TopK", "Ascending TopK is not supported", self)

    return g.op("TopK", self, k_i=k, axis_i=dim, outputs=2)



# ==================================================
# Line: 4230

def _generic_rnn(
    g: jit_utils.GraphContext,
    variant,
    input,
    initial_states,
    all_weights,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,
    batch_first=None,
    batch_sizes=None,

# ==================================================
# Line: 4457

def _lstm_full(
    g: jit_utils.GraphContext,
    input,
    hidden_v,
    weight_v,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,
    batch_first,

# ==================================================
# Line: 4489

def _lstm_packed(
    g: jit_utils.GraphContext,
    input,
    batch_sizes,
    hidden_v,
    weight_v,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,

# ==================================================
# Line: 4529

def lstm_cell(g: jit_utils.GraphContext, self, hidden, w_ih, w_hh, b_ih, b_hh):
    input = symbolic_helper._unsqueeze_helper(g, self, [0])
    hidden = symbolic_helper._unpack_list(hidden)
    hidden = [symbolic_helper._unsqueeze_helper(g, x, [0]) for x in hidden]
    weight = (
        (w_ih, w_hh, b_ih, b_hh) if symbolic_helper._is_tensor(b_ih) else (w_ih, w_hh)
    )
    has_biases = True if symbolic_helper._is_tensor(b_ih) else False
    _, h_outs, c_outs = _generic_rnn(
        g,
        "LSTM",
        input,
        hidden,
        weight,
        has_biases,
        num_layers=1,
        dropout=0,
        train=0,
        bidirectional=False,
        batch_first=False,
    )
    return symbolic_helper._squeeze_helper(
        g, h_outs, [0]
    ), symbolic_helper._squeeze_helper(g, c_outs, [0])



# ==================================================
# Line: 4568

def _rnn_full(
    g,
    input,
    hidden,
    weight_v,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,
    batch_first,

# ==================================================
# Line: 4596

def _rnn_packed(
    g,
    input,
    batch_sizes,
    hidden,
    weight_v,
    has_biases,
    num_layers,
    dropout,
    train,
    bidirectional,

# ==================================================
# Line: 4828

def randn_like(
    g: jit_utils.GraphContext,
    self,
    dtype,
    layout=None,
    device=None,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 4848

def rand_like(
    g: jit_utils.GraphContext,
    self,
    dtype,
    layout=None,
    device=None,
    pin_memory=False,
    memory_format=None,

# ==================================================
# Line: 5244

def linspace(
    g: jit_utils.GraphContext, start, end, steps, dtype, layout, device, pin_memory

# ==================================================
# Line: 5678

def group_norm(
    g: jit_utils.GraphContext, input, num_groups, weight, bias, eps, cudnn_enabled

# ==================================================
# Line: 5947

def hann_window(
    g: jit_utils.GraphContext,
    window_length,
    periodic=True,
    dtype: int | None = None,
    layout=None,
    device=None,
    pin_memory=None,
    requires_grad=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset13.py
# Line: 319

def fake_quantize_per_channel_affine(
    g: jit_utils.GraphContext,
    inputs,
    scale,
    zero_point,
    axis,
    quant_min=-128,
    quant_max=127,

# ==================================================
# Line: 880

def quantized_conv1d_relu(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 906

def quantized_conv2d_relu(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 932

def quantized_conv3d_relu(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 958

def quantized_conv1d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 983

def quantized_conv2d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1008

def quantized_conv3d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1033

def quantized_conv_transpose1d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    output_padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1061

def quantized_conv_transpose2d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    output_padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# Line: 1089

def quantized_conv_transpose3d(
    g: jit_utils.GraphContext,
    q_input,
    q_weight,
    bias,
    stride,
    padding,
    output_padding,
    dilation,
    groups,
    op_scale,
    op_zero_point,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/onnxruntime.py
# Line: 443

def _run_onnx_session_with_ortvaluevector(
    sess: "onnxruntime.InferenceSession",
    input_names: tuple[str, ...],
    inputs: tuple[torch.Tensor, ...],
    input_devices: tuple["ORTC.OrtDevice", ...],
    output_names: tuple[str, ...],
    outputs: tuple[torch.Tensor, ...],
    output_devices: tuple["ORTC.OrtDevice", ...],
    preallocate_output: bool,
    input_value_infos: tuple["onnx.ValueInfoProto", ...],  # type: ignore[name-defined]
    normalized_prim_outputs: tuple[
        Union[
            torch.Tensor, torch.SymInt, int, torch.SymFloat, float, torch.SymBool, bool
        ],
        ...,
    ],

# ==================================================
# Line: 526

def _run_onnx_session_with_fetch(
    sess: "onnxruntime.InferenceSession",
    input_names: tuple[str, ...],
    inputs: tuple[torch.Tensor, ...],
    input_devices: tuple["ORTC.OrtDevice", ...],
    output_names: tuple[str, ...],
    outputs: tuple[torch.Tensor, ...],
    output_devices: tuple["ORTC.OrtDevice", ...],
    preallocate_output: bool,
    input_value_infos: tuple["onnx.ValueInfoProto", ...],  # type: ignore[name-defined]
    normalized_prim_outputs: tuple[
        Union[
            torch.Tensor, torch.SymInt, int, torch.SymFloat, float, torch.SymBool, bool
        ],
        ...,
    ],

# ==================================================
# Line: 590

def __init__(
    self,
    session: "onnxruntime.InferenceSession",
    input_names: tuple[str, ...],
    input_value_infos: tuple["onnx.ValueInfoProto", ...],  # type: ignore[name-defined]
    output_names: tuple[str, ...],
    output_value_infos: tuple["onnx.ValueInfoProto", ...],  # type: ignore[name-defined]
    input_devices: tuple["ORTC.OrtDevice", ...],
    output_devices: tuple["ORTC.OrtDevice", ...],
    example_outputs: Union[tuple[torch.Tensor, ...], torch.Tensor],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/jit_utils.py
# Line: 274

def _create_node(
    graph_or_block: _C.Graph | _C.Block,
    domain_op: str,
    inputs: Sequence,
    attributes: dict,
    params_dict: dict,
    opset_version: int,
    n_outputs: int,
    shape_inference: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/fx/fx_onnx_interpreter.py
# Line: 343

def run_node(
    self,
    node,
    fx_graph_module: torch.fx.GraphModule,
    onnxfunction_dispatcher: onnxfunction_dispatcher.OnnxFunctionDispatcher,
    onnxscript_graph: onnxscript_graph_building.TorchScriptGraph,
    onnxscript_tracer: onnxscript_graph_building.TorchScriptTracingEvaluator,
    fx_name_to_onnxscript_value: dict[
        str,
        onnxscript_graph_building.TorchScriptTensor
        | tuple[onnxscript_graph_building.TorchScriptTensor, ...],
    ],

# ==================================================
# Line: 621

def call_module(
    self,
    node: torch.fx.Node,
    parent_onnxscript_graph: onnxscript_graph_building.TorchScriptGraph,
    fx_name_to_onnxscript_value: dict[
        str,
        onnxscript_graph_building.TorchScriptTensor
        | tuple[onnxscript_graph_building.TorchScriptTensor, ...],
    ],
    tracer: onnxscript_graph_building.TorchScriptTracingEvaluator,
    root_fx_graph_module: torch.fx.GraphModule,
    onnxfunction_dispatcher: onnxfunction_dispatcher.OnnxFunctionDispatcher,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_tensors.py
# Line: 13

def __init__(
    self,
    opset: onnxscript.values.Opset,
    name: str | None = None,
    shape: ir.Shape | None = None,
    type: ir.TypeProtocol | None = None,
    doc_string: str | None = None,
    const_value: ir.TensorProtocol | None = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_torchlib/ops/symbolic.py
# Line: 20

def _call_symbolic_op(
    op_type: str,
    domain: str,
    args: Sequence[ir.Value | None],
    kwargs: dict[str, int | float | str | bool | list[int] | list[float] | list[str]],
    dtypes: Sequence[int],
    version: int | None,
    metadata_props: dict[str, str] | None,

# ==================================================
# Line: 75

def onnx_symbolic_symbolic(
    inputs: Sequence[ir.Value | None],
    op_type: str,
    onnx_dtype: int,
    *,
    shape: Sequence[int | ir.Value],
    attr_keys: Sequence[str],
    attr_types: Sequence[str],
    attr_pos: Sequence[tuple[int, int]],
    attr_ints: Sequence[int],
    attr_floats: Sequence[float],
    attr_strs: Sequence[str],
    metadata_props_keys: Sequence[str] = (),
    metadata_props_values: Sequence[str] = (),
    domain: str = "",
    version: int | None = None,

# ==================================================
# Line: 114

def onnx_symbolic_symbolic_multi_out(
    inputs: Sequence[ir.Value | None],
    op_type: str,
    onnx_dtypes: Sequence[int],
    *,
    shapes: Sequence[Sequence[int | ir.Value]],
    attr_keys: Sequence[str],
    attr_types: Sequence[str],
    attr_pos: Sequence[tuple[int, int]],
    attr_ints: Sequence[int],
    attr_floats: Sequence[float],
    attr_strs: Sequence[str],
    metadata_props_keys: Sequence[str] = (),
    metadata_props_values: Sequence[str] = (),
    domain: str = "",
    version: int | None = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_torchlib/ops/nn.py
# Line: 60

def aten_scaled_dot_product_attention_23(
    query: TFloat,
    key: TFloat,
    value: TFloat,
    attn_mask: Optional[TFloat] = None,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    scale: Optional[float] = None,
    enable_gqa: bool = False,

# ==================================================
# Line: 238

def _aten_scaled_dot_product_attention_float_mask_onnx(
    query: TFloat,
    key: TFloat,
    value: TFloat,
    attn_mask: TFloat,
    scale: TFloat,
    dropout_p: float,
    op: Opset,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_reporting.py
# Line: 167

def create_onnx_export_report(
    filename: str | os.PathLike,
    formatted_traceback: str,
    program: torch.export.ExportedProgram,
    *,
    decomp_comparison: str | None = None,
    export_status: ExportStatus,
    profile_result: str | None,
    model: ir.Model | None = None,
    registry: _registration.ONNXRegistry | None = None,
    verification_result: str | None = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_compat.py
# Line: 40

def export_compat(
    model: torch.nn.Module
    | torch.export.ExportedProgram
    | torch.jit.ScriptModule
    | torch.jit.ScriptFunction,
    args: tuple[Any, ...],
    f: str | os.PathLike | None = None,
    *,
    kwargs: dict[str, Any] | None = None,
    export_params: bool = True,
    verbose: bool | None = None,
    input_names: Sequence[str] | None = None,
    output_names: Sequence[str] | None = None,
    opset_version: int | None = _constants.TORCHLIB_OPSET,
    custom_translation_table: dict[Callable, Callable | Sequence[Callable]]
    | None = None,
    dynamic_axes: Mapping[str, Mapping[int, str]]
    | Mapping[str, Sequence[int]]
    | None = None,
    dynamic_shapes: dict[str, Any] | tuple[Any, ...] | list[Any] | None = None,
    keep_initializers_as_inputs: bool = False,
    external_data: bool = True,
    report: bool = False,
    optimize: bool = False,
    verify: bool = False,
    profile: bool = False,
    dump_exported_program: bool = False,
    artifacts_dir: str | os.PathLike = ".",
    fallback: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_core.py
# Line: 494

def _handle_call_function_node_with_lowering(
    model: ir.Model,
    node: torch.fx.Node,
    node_name_to_values: dict[str, ir.Value | Sequence[ir.Value]],
    *,
    graph_like: ir.Graph | ir.Function,
    constant_farm: dict[Any, ir.Value],
    registry: _registration.ONNXRegistry,
    opset: onnxscript.values.Opset,
    node_name_to_local_functions: dict[str, ir.Function],

# ==================================================
# Line: 1245

def export(
    model: torch.nn.Module
    | torch.export.ExportedProgram
    | torch.fx.GraphModule
    | torch.jit.ScriptModule
    | torch.jit.ScriptFunction,
    args: tuple[Any, ...] = (),
    kwargs: dict[str, Any] | None = None,
    *,
    registry: _registration.ONNXRegistry | None = None,
    dynamic_shapes: dict[str, Any] | tuple[Any, ...] | list[Any] | None = None,
    input_names: Sequence[str] | None = None,
    output_names: Sequence[str] | None = None,
    report: bool = False,
    verify: bool = False,
    profile: bool = False,
    dump_exported_program: bool = False,
    artifacts_dir: str | os.PathLike = ".",
    verbose: bool | None = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/symbolic_opset12.py
# Line: 163

def cross_entropy_loss(
    g: jit_utils.GraphContext,
    self,
    target,
    weight,
    reduction,
    ignore_index,
    label_smoothing,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/meta_utils.py
# Line: 1835

def __call__(
    self,
    t: torch.Tensor,
    shape_env: Optional[ShapeEnv] = None,
    *,
    callback: Optional[_MetaTensorCallback[_TensorT]] = None,
    source: Optional[Source] = None,
    symbolic_context: Optional[SymbolicContext] = None,
    # Controls whether or not we should dump the tensor metadata to structured logs
    # when source is not None.  Because we refakify after Dynamo is done,
    # we don't want to dump info again from AOTAutograd, it is redundant.
    trace: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/fake_utils.py
# Line: 172

def _check_fake_real_tensors(
    real_out: torch.Tensor,
    fake_out: FakeTensor,
    context="",
    sizes=True,
    strides=False,
    storage_offset=True,
    requires_grad=True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/fake_tensor.py
# Line: 347

def from_real_tensor(
    self,
    fake_mode: FakeTensorMode,
    t: Tensor,
    make_constant: bool = False,
    shape_env: Optional[ShapeEnv] = None,
    *,
    source: Optional[Source] = None,
    symbolic_context: Optional[SymbolicContext] = None,
    trace: bool = True,

# ==================================================
# Line: 709

def __new__(
    cls,
    fake_mode: FakeTensorMode,
    elem: Tensor,
    device: torch.device,
    constant: Optional[Tensor] = None,
    real_tensor: Optional[Tensor] = None,
    pytype: Optional[type[Tensor]] = None,
    dispatch_keys: Optional[torch.DispatchKeySet] = None,

# ==================================================
# Line: 1695

def _validate_output_for_cache_entry(
    self,
    state: _CacheKeyState,
    key: _DispatchCacheKey,
    func: OpOverload,
    args: Sequence[object],
    kwargs: Mapping[str, object],
    output: Optional[FakeTensor],

# ==================================================
# Line: 1739

def _get_output_info_for_cache_entry(
    self,
    state: _CacheKeyState,
    key: _DispatchCacheKey,
    func: OpOverload,
    args: Sequence[object],
    kwargs: Mapping[str, object],
    output: FakeTensor,

# ==================================================
# Line: 1813

def _make_cache_entry(
    self,
    state: _CacheKeyState,
    key: _DispatchCacheKey,
    func: OpOverload,
    args: Sequence[object],
    kwargs: Mapping[str, object],
    output: Optional[FakeTensor],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/fake_impls.py
# Line: 278

def _unique(
    fake_mode,
    func,
    arg,
    dim,
    sorted=True,
    return_inverse=False,
    return_counts=False,
    *,
    unique_consecutive=False,

# ==================================================
# Line: 362

def unique_dim(
    fake_mode, func, arg, dim, sorted=True, return_inverse=False, return_counts=False

# ==================================================
# Line: 565

def assert_tensor_metadata(
    fake_mode,
    func,
    t,
    sizes=None,
    strides=None,
    dtype=None,
    *,
    device=None,
    layout=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/functional.py
# Line: 557

def stft(
    input: Tensor,
    n_fft: int,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: Optional[Tensor] = None,
    center: bool = True,
    pad_mode: str = "reflect",
    normalized: bool = False,
    onesided: Optional[bool] = None,
    return_complex: Optional[bool] = None,
    align_to_window: Optional[bool] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_jit_internal.py
# Line: 602

def boolean_dispatch(
    arg_name,
    arg_index,
    default,
    if_true,
    if_false,
    module_name,
    func_name,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_prims/__init__.py
# Line: 267

def _make_prim(
    *,
    schema: str,
    return_type: Union[RETURN_TYPE, tuple[RETURN_TYPE, ...]],
    meta: Callable,
    impl_aten: Callable,
    doc: str,
    tags: Optional[Sequence[torch.Tag]] = None,
    use_old_custom_ops_api: bool = False,
    register_conj_neg_fallthrough: bool = False,

# ==================================================
# Line: 2685

def _normal_meta(
    shape: ShapeType,
    *,
    mean: Union[float, complex],
    std: float,
    dtype: torch.dtype,
    device: torch.device,
    requires_grad: bool,
    generator: Optional[torch.Generator] = None,

# ==================================================
# Line: 2709

def _normal_aten(
    shape: ShapeType,
    *,
    mean: Union[float, complex],
    std: float,
    dtype: torch.dtype,
    device: torch.device,
    requires_grad: bool,
    generator: Optional[torch.Generator] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/masked/_ops.py
# Line: 1590

def _std_var(
    input: Union[Tensor, MaskedTensor],
    dim: DimOrDims,
    unbiased: Optional[bool],
    *,
    correction_opt: Optional[Union[int, float]],
    keepdim: Optional[bool],
    dtype: Optional[DType],
    mask: Optional[Tensor],
    take_sqrt: Optional[bool],

# ==================================================
# Line: 1663

def var(
    input: Union[Tensor, MaskedTensor],
    dim: DimOrDims = None,
    unbiased: Optional[bool] = None,
    *,
    correction: Optional[Union[int, float]] = None,
    keepdim: Optional[bool] = False,
    dtype: Optional[DType] = None,
    mask: Optional[Tensor] = None,

# ==================================================
# Line: 1694

def std(
    input: Union[Tensor, MaskedTensor],
    dim: DimOrDims = None,
    unbiased: Optional[bool] = None,
    *,
    correction: Optional[int] = None,
    keepdim: Optional[bool] = False,
    dtype: Optional[DType] = None,
    mask: Optional[Tensor] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_tensor.py
# Line: 932

def stft(
    self,
    n_fft: int,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: "Optional[Tensor]" = None,
    center: bool = True,
    pad_mode: str = "reflect",
    normalized: bool = False,
    onesided: Optional[bool] = None,
    return_complex: Optional[bool] = None,
    align_to_window: Optional[bool] = None,

# ==================================================
# Line: 981

def istft(
    self,
    n_fft: int,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: "Optional[Tensor]" = None,
    center: bool = True,
    normalized: bool = False,
    onesided: Optional[bool] = None,
    length: Optional[int] = None,
    return_complex: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nested/_internal/ops.py
# Line: 39

def _wrap_jagged_dim(
    ndim,
    dim,
    ragged_dim,
    op_name,
    convert_to_inner_dim=True,
    allow_ragged_dim=False,
    allow_batch_dim=False,

# ==================================================
# Line: 2613

def flex_njt(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    score_mod: Callable,
    block_mask: Tuple,
    scale: float,
    kernel_options: Dict[str, Any],
    score_mod_other_buffers: Tuple = (),
    mask_mod_other_buffers: Tuple = (),

# ==================================================
# Line: 2670

def flex_njt_backward(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    grad_out: torch.Tensor,
    grad_logsumexp: torch.Tensor,
    fw_graph: Union[Callable, GraphModule],
    joint_graph: GraphModule,
    block_mask: Tuple,
    scale: float,
    kernel_options: Dict[str, Any],
    score_mod_other_buffers: Tuple = (),
    mask_mod_other_buffers: Tuple = (),

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nested/_internal/sdpa.py
# Line: 26

def _validate_sdpa_input(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attn_mask: Optional[torch.Tensor] = None,
    dropout_p=0.0,
    is_causal=False,
    scale=None,

# ==================================================
# Line: 293

def _select_sdp_backend(query, key, value, attn_mask, dropout, is_causal, enable_gqa):
    if (
        not flash_sdp_enabled()
        and not mem_efficient_sdp_enabled()
        and not math_sdp_enabled()
        and not cudnn_sdp_enabled()
    ):
        return SDPBackend.ERROR

    ordering = (
        SDPBackend.FLASH_ATTENTION,
        SDPBackend.EFFICIENT_ATTENTION,
        SDPBackend.MATH,
        SDPBackend.CUDNN_ATTENTION,
    )

    params = SDPAParams(query, key, value, attn_mask, dropout, is_causal, enable_gqa)

    for backend in ordering:
        if backend == SDPBackend.CUDNN_ATTENTION:
            if can_use_cudnn_attention(params):
                return SDPBackend.CUDNN_ATTENTION
        if backend == SDPBackend.FLASH_ATTENTION:
            if can_use_flash_attention(params) and _can_use_flash_sdpa_jagged(params):
                return SDPBackend.FLASH_ATTENTION
        if backend == SDPBackend.EFFICIENT_ATTENTION:
            if can_use_efficient_attention(params) and _can_use_efficient_sdpa_jagged(
                params
            ):
                return SDPBackend.EFFICIENT_ATTENTION
        if backend == SDPBackend.MATH:
            if math_sdp_enabled() and _can_use_math_sdpa_jagged(params):
                return SDPBackend.MATH

    log.warning("Memory efficient kernel not used because:")
    can_use_efficient_attention(params, debug=True)
    _can_use_efficient_sdpa_jagged(params, debug=True)
    log.warning("Flash attention kernel not used because:")
    can_use_flash_attention(params, debug=True)
    _can_use_flash_sdpa_jagged(params, debug=True)
    log.warning("Math attention kernel not used because:")
    _can_use_math_sdpa_jagged(params, debug=True)
    log.warning("cuDNN attention kernel not used because:")
    can_use_cudnn_attention(params, debug=True)
    return SDPBackend.ERROR



# ==================================================
# Line: 713

def jagged_scaled_dot_product_attention(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attn_mask: Optional[torch.Tensor] = None,
    dropout_p=0.0,
    is_causal=False,
    scale=None,
    enable_gqa=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_numpy/_ndarray.py
# Line: 510

def array(obj, dtype=None, *, copy=True, order="K", subok=False, ndmin=0, like=None):
    if subok is not False:
        raise NotImplementedError("'subok' parameter is not supported.")
    if like is not None:
        raise NotImplementedError("'like' parameter is not supported.")
    if order != "K":
        raise NotImplementedError

    # a happy path
    if (
        isinstance(obj, ndarray)
        and copy is False
        and dtype is None
        and ndmin <= obj.ndim
    ):
        return obj

    if isinstance(obj, (list, tuple)):
        # FIXME and they have the same dtype, device, etc
        if obj and all(isinstance(x, torch.Tensor) for x in obj):
            # list of arrays: *under torch.Dynamo* these are FakeTensors
            obj = torch.stack(obj)
        else:
            # XXX: remove tolist
            # lists of ndarrays: [1, [2, 3], ndarray(4)] convert to lists of lists
            obj = _tolist(obj)

    # is obj an ndarray already?
    if isinstance(obj, ndarray):
        obj = obj.tensor

    # is a specific dtype requested?
    torch_dtype = None
    if dtype is not None:
        torch_dtype = _dtypes.dtype(dtype).torch_dtype

    tensor = _util._coerce_to_tensor(obj, torch_dtype, copy, ndmin)
    return ndarray(tensor)



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_numpy/_funcs_impl.py
# Line: 297

def linspace(
    start: ArrayLike,
    stop: ArrayLike,
    num=50,
    endpoint=True,
    retstep=False,
    dtype: Optional[DTypeLike] = None,
    axis=0,

# ==================================================
# Line: 334

def logspace(
    start,
    stop,
    num=50,
    endpoint=True,
    base=10.0,
    dtype: Optional[DTypeLike] = None,
    axis=0,

# ==================================================
# Line: 559

def cov(
    m: ArrayLike,
    y: Optional[ArrayLike] = None,
    rowvar=True,
    bias=False,
    ddof=None,
    fweights: Optional[ArrayLike] = None,
    aweights: Optional[ArrayLike] = None,
    *,
    dtype: Optional[DTypeLike] = None,

# ==================================================
# Line: 1926

def histogram2d(
    x,
    y,
    bins=10,
    range: Optional[ArrayLike] = None,
    normed=None,
    weights: Optional[ArrayLike] = None,
    density=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_numpy/_ufuncs.py
# Line: 75

def wrapped(
    x1: ArrayLikeOrScalar,
    x2: ArrayLikeOrScalar,
    /,
    out: Optional[OutArray] = None,
    *,
    where: NotImplementedType = True,
    casting: Optional[CastingModes] = "same_kind",
    order: NotImplementedType = "K",
    dtype: Optional[DTypeLike] = None,
    subok: NotImplementedType = False,
    signature: NotImplementedType = None,
    extobj: NotImplementedType = None,

# ==================================================
# Line: 122

def matmul(
    x1: ArrayLike,
    x2: ArrayLike,
    /,
    out: Optional[OutArray] = None,
    *,
    casting: Optional[CastingModes] = "same_kind",
    order: NotImplementedType = "K",
    dtype: Optional[DTypeLike] = None,
    subok: NotImplementedType = False,
    signature: NotImplementedType = None,
    extobj: NotImplementedType = None,
    axes: NotImplementedType = None,
    axis: NotImplementedType = None,

# ==================================================
# Line: 149

def ldexp(
    x1: ArrayLikeOrScalar,
    x2: ArrayLikeOrScalar,
    /,
    out: Optional[OutArray] = None,
    *,
    where: NotImplementedType = True,
    casting: Optional[CastingModes] = "same_kind",
    order: NotImplementedType = "K",
    dtype: Optional[DTypeLike] = None,
    subok: NotImplementedType = False,
    signature: NotImplementedType = None,
    extobj: NotImplementedType = None,

# ==================================================
# Line: 189

def divmod(
    x1: ArrayLike,
    x2: ArrayLike,
    out1: Optional[OutArray] = None,
    out2: Optional[OutArray] = None,
    /,
    out: tuple[Optional[OutArray], Optional[OutArray]] = (None, None),
    *,
    where: NotImplementedType = True,
    casting: Optional[CastingModes] = "same_kind",
    order: NotImplementedType = "K",
    dtype: Optional[DTypeLike] = None,
    subok: NotImplementedType = False,
    signature: NotImplementedType = None,
    extobj: NotImplementedType = None,

# ==================================================
# Line: 297

def wrapped(
    x: ArrayLike,
    /,
    out: Optional[OutArray] = None,
    *,
    where=True,
    casting: Optional[CastingModes] = "same_kind",
    order="K",
    dtype: Optional[DTypeLike] = None,
    subok: NotImplementedType = False,
    signature=None,
    extobj=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_numpy/_reductions_impl.py
# Line: 186

def sum(
    a: ArrayLike,
    axis: AxisLike = None,
    dtype: Optional[DTypeLike] = None,
    out: Optional[OutArray] = None,
    keepdims: KeepDims = False,
    initial: NotImplementedType = None,
    where: NotImplementedType = None,

# ==================================================
# Line: 205

def prod(
    a: ArrayLike,
    axis: AxisLike = None,
    dtype: Optional[DTypeLike] = None,
    out: Optional[OutArray] = None,
    keepdims: KeepDims = False,
    initial: NotImplementedType = None,
    where: NotImplementedType = None,

# ==================================================
# Line: 245

def std(
    a: ArrayLike,
    axis: AxisLike = None,
    dtype: Optional[DTypeLike] = None,
    out: Optional[OutArray] = None,
    ddof=0,
    keepdims: KeepDims = False,
    *,
    where: NotImplementedType = None,

# ==================================================
# Line: 263

def var(
    a: ArrayLike,
    axis: AxisLike = None,
    dtype: Optional[DTypeLike] = None,
    out: Optional[OutArray] = None,
    ddof=0,
    keepdims: KeepDims = False,
    *,
    where: NotImplementedType = None,

# ==================================================
# Line: 375

def quantile(
    a: ArrayLike,
    q: ArrayLike,
    axis: AxisLike = None,
    out: Optional[OutArray] = None,
    overwrite_input=False,
    method="linear",
    keepdims: KeepDims = False,
    *,
    interpolation: NotImplementedType = None,

# ==================================================
# Line: 418

def percentile(
    a: ArrayLike,
    q: ArrayLike,
    axis: AxisLike = None,
    out: Optional[OutArray] = None,
    overwrite_input=False,
    method="linear",
    keepdims: KeepDims = False,
    *,
    interpolation: NotImplementedType = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/library.py
# Line: 456

def _del_library(
    captured_impls,
    op_impls,
    captured_defs,
    op_defs,
    registration_handles,
    m,
    schema_to_signature_cache,

# ==================================================
# Line: 1493

def opcheck(
    op: Union[torch._ops.OpOverload, torch._ops.OpOverloadPacket, CustomOpDef],
    args: tuple[Any, ...],
    kwargs: Optional[dict[str, Any]] = None,
    *,
    test_utils: Union[str, Sequence[str]] = _OPCHECK_DEFAULT_UTILS,
    raise_exception: bool = True,
    atol=None,
    rtol=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/dynamic_shapes.py
# Line: 459

def _process_equalities(
    constraint: Constraint,
    get_sources: Callable[[int, int], list["Source"]],
    shape_env: "ShapeEnv",
    names: dict[str, tuple[int, int]],
    source_pairs: list[tuple["Source", "Source"]],
    derived_equalities: list[tuple["Source", Union["Source", "Symbol"], Callable]],
    phantom_symbols: dict[str, "Symbol"],
    relaxed_sources: set["Source"],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/_trace.py
# Line: 515

def _produce_aten_artifact(
    *,
    gm: torch.fx.GraphModule,
    mod,
    constant_attrs,
    graph_signature,
    pre_dispatch,
    fake_args,
    fake_kwargs,
    fake_params_buffers,
    _prettify_placeholder_names=True,

# ==================================================
# Line: 739

def _export_to_torch_ir(
    f: Callable,
    args: tuple[Any, ...],
    kwargs: Optional[dict[str, Any]] = None,
    dynamic_shapes: Optional[Union[dict[str, Any], tuple[Any], list[Any]]] = None,
    *,
    preserve_module_call_signature: tuple[str, ...] = (),
    disable_constraint_solver: bool = False,
    allow_complex_guards_as_runtime_asserts: bool = False,
    restore_fqn: bool = True,
    _log_export_usage: bool = True,
    same_signature: bool = True,

# ==================================================
# Line: 832

def _export_to_aten_ir(
    mod: torch.nn.Module,
    fake_args,
    fake_kwargs,
    fake_params_buffers,
    constant_attrs: ConstantAttrMap,
    produce_guards_callback=None,
    *,
    transform=lambda x: x,  # TODO(zhxchen17) Revisit if this is needed later.
    pre_dispatch=False,
    decomp_table=None,
    _check_autograd_state: bool = True,
    _is_torch_jit_trace: bool = False,
    _prettify_placeholder_names: bool = True,
    decompose_custom_triton_ops: bool = False,

# ==================================================
# Line: 1390

def _strict_export(
    mod: torch.nn.Module,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    dynamic_shapes: Optional[Union[dict[str, Any], tuple[Any], list[Any]]],
    preserve_module_call_signature: tuple[str, ...],
    orig_in_spec: TreeSpec,
    allow_complex_guards_as_runtime_asserts: bool,
    _is_torch_jit_trace: bool,
    _to_aten_func: Callable,

# ==================================================
# Line: 1545

def _export_to_aten_ir_make_fx(
    mod: torch.nn.Module,
    fake_args,
    fake_kwargs,
    fake_params_buffers,
    constant_attrs: ConstantAttrMap,
    produce_guards_callback=None,
    transform=lambda x: x,

# ==================================================
# Line: 1836

def _non_strict_export(
    mod: torch.nn.Module,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    dynamic_shapes: Optional[Union[dict[str, Any], tuple[Any], list[Any]]],
    preserve_module_call_signature: tuple[str, ...],
    orig_in_spec: TreeSpec,
    allow_complex_guards_as_runtime_asserts: bool,
    _is_torch_jit_trace: bool,
    _to_aten_func: Callable,

# ==================================================
# Line: 2094

def _export(
    mod: torch.nn.Module,
    args: tuple[Any, ...],
    kwargs: Optional[dict[str, Any]] = None,
    dynamic_shapes: Optional[Union[dict[str, Any], tuple[Any], list[Any]]] = None,
    *,
    strict: bool = True,
    preserve_module_call_signature: tuple[str, ...] = (),
    pre_dispatch: bool = False,
    allow_complex_guards_as_runtime_asserts: bool = False,
    _is_torch_jit_trace: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/_unlift.py
# Line: 225

def _unlift(
    gm: torch.fx.GraphModule,
    lifted_inputs: Sequence[Optional[str]],
    mutated_outputs: Sequence[Optional[str]],
    in_spec: pytree.TreeSpec,
    out_spec: Optional[pytree.TreeSpec],
    state_dict: dict[str, Any],
    constants: dict[str, Any],
    forward_arg_names: Optional[list[str]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/unflatten.py
# Line: 931

def __init__(
    self,
    flat_graph: torch.fx.Graph,
    nodes: tuple[torch.fx.Node, ...],
    seen_nodes,
    seen_modules,
    seen_attrs,
    created_modules,
    parent,
    module_stack: list[tuple[str, Optional[str], int]],
    module_id,
    module_call_graph: dict[str, ModuleCallSignature],
    module: Optional[Union[torch.fx.GraphModule, UnflattenedModule]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/_draft_export.py
# Line: 362

def draft_export(
    mod: torch.nn.Module,
    args: tuple[Any, ...],
    kwargs: Optional[dict[str, Any]] = None,
    *,
    dynamic_shapes: Optional[Union[dict[str, Any], tuple[Any], list[Any]]] = None,
    preserve_module_call_signature: tuple[str, ...] = (),
    strict: bool = False,
    pre_dispatch: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/exported_program.py
# Line: 910

def __init__(
    self,
    root: Union[torch.nn.Module, dict[str, Any]],
    graph: torch.fx.Graph,
    graph_signature: ExportGraphSignature,
    state_dict: dict[str, Union[torch.Tensor, torch.nn.Parameter]],
    range_constraints: "dict[sympy.Symbol, Any]",
    module_call_graph: list[ModuleCallEntry],
    example_inputs: Optional[tuple[tuple[Any, ...], dict[str, Any]]] = None,
    constants: Optional[dict[str, _ConstantAttributeType]] = None,
    *,
    verifiers: Optional[list[type[Verifier]]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/profiler/profiler.py
# Line: 135

def __init__(
    self,
    *,
    activities: Optional[Iterable[ProfilerActivity]] = None,
    record_shapes: bool = False,
    profile_memory: bool = False,
    with_stack: bool = False,
    with_flops: bool = False,
    with_modules: bool = False,
    experimental_config: Optional[_ExperimentalConfig] = None,
    execution_trace_observer: Optional[_ITraceObserver] = None,
    acc_events: bool = False,
    custom_trace_id_callback: Optional[Callable[[], str]] = None,

# ==================================================
# Line: 688

def __init__(
    self,
    *,
    activities: Optional[Iterable[ProfilerActivity]] = None,
    schedule: Optional[Callable[[int], ProfilerAction]] = None,
    on_trace_ready: Optional[Callable[..., Any]] = None,
    record_shapes: bool = False,
    profile_memory: bool = False,
    with_stack: bool = False,
    with_flops: bool = False,
    with_modules: bool = False,
    experimental_config: Optional[_ExperimentalConfig] = None,
    execution_trace_observer: Optional[_ITraceObserver] = None,
    acc_events: bool = False,
    # deprecated:
    use_cuda: Optional[bool] = None,
    custom_trace_id_callback: Optional[Callable[[], str]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_sources.py
# Line: 88

def __init__(
    self,
    source,
    filename,
    file_lineno,
    leading_whitespace_len,
    uses_true_division=True,
    funcname=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/resume_execution.py
# Line: 285

def generate(
    cls,
    code,
    lineno,
    offset: int,
    setup_fn_target_offsets: tuple[int, ...],  # only used in Python 3.11+
    nstack: int,
    argnames: tuple[str, ...],
    argnames_null: tuple[str, ...],
    setup_fns: tuple[ReenterWith, ...],
    stack_ctx_vars: tuple[tuple[int, tuple[Any, ...]], ...],
    argnames_ctx_vars: tuple[tuple[str, tuple[Any, ...]], ...],
    null_idxes: tuple[int, ...],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/graph_deduplication.py
# Line: 120

def _replace_region_with_subgraph(
    graph: torch.fx.Graph,
    region: Region,
    get_subgraph_node: Node,
    external_node_usages: Iterable[OrderedSet[UsageIndex]],
    inds_with_external_users: list[int],
    subgraph_name: str,
    node_to_additional_deps: dict[Node, OrderedSet[Node]],
    node_to_mutated_arg_positions: dict[Node, OrderedSet[int]],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/repro/after_dynamo.py
# Line: 172

def generate_dynamo_fx_repro_string(
    gm,
    args,
    compiler_name,
    check_accuracy=False,
    *,
    stable_output=False,
    save_dir=None,
    command="run",

# ==================================================
# Line: 484

def run_repro(
    mod,
    load_args,
    *,
    command="run",
    accuracy: Union[bool, str] = "",
    save_dir=None,
    autocast=False,
    backend="inductor",
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/repro/aoti.py
# Line: 134

def save_graph_repro_ep(
    fd,
    compiler_name,
    *,
    exported_program: Optional[ExportedProgram] = None,
    gm: Optional[torch.nn.Module] = None,
    args: Optional[tuple[Any]] = None,
    config_patches: Optional[dict[str, str]] = None,
    stable_output=False,
    save_dir=None,
    command="run",
    accuracy=None,
    check_str=None,
    module_in_comment=False,
    strict=False,

# ==================================================
# Line: 449

def run_repro(
    exported_program,
    *,
    config_patches: Optional[dict[str, str]] = None,
    command="run",
    accuracy: Union[bool, str] = "",
    save_dir=None,
    tracing_mode=None,
    check_str=None,
    minifier_export_mode="python",
    skip_export_error=True,
    **more_kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/repro/after_aot.py
# Line: 340

def save_graph_repro(
    fd,
    gm,
    args,
    compiler_name,
    *,
    stable_output=False,
    save_dir=None,
    command="run",
    accuracy=None,
    tracing_mode=None,
    check_str=None,
    stable_hash=False,

# ==================================================
# Line: 431

def isolate_fails(
    fx_g,
    args,
    compiler_name: str,
    env=None,
    save_dir=None,
    accuracy=None,
    tracing_mode=None,
    check_str=None,

# ==================================================
# Line: 839

def run_repro(
    mod,
    load_args,
    *,
    command="run",
    accuracy: Union[bool, str] = "",
    save_dir=None,
    tracing_mode=None,
    patch_code=None,
    check_str=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/utils.py
# Line: 617

def dynamo_timed(
    key: str,
    # TODO(masneral): Deprecate this param.
    phase_name: Optional[str] = None,
    log_pt2_compile_event: bool = False,
    metadata: Optional[dict[str, object]] = None,
    dynamo_compile_column_us: Optional[str] = None,
    compile_id: Optional[CompileId] = None,
    is_backward: Optional[bool] = None,
    log_waitcounter: bool = False,
    waitcounter_name_override: Optional[str] = None,

# ==================================================
# Line: 1807

def log_event_end(
    self,
    event_name: str,
    time_ns: int,
    metadata: dict[str, Any],
    start_time_ns: int,
    log_pt2_compile_event: bool,
    compile_id: Optional[CompileId] = None,

# ==================================================
# Line: 2776

def same(
    ref,
    res,
    fp64_ref=None,
    cos_similarity=False,
    tol=1e-4,
    equal_nan=False,
    exact_dtype=True,
    relax_numpy_equality=False,
    ignore_non_fp=False,
    log_error=log.error,
    use_larger_multiplier_for_smaller_tensor=False,
    force_max_multiplier: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/debug_utils.py
# Line: 594

def tensor(
    self,
    storage,
    shape,
    stride=None,
    *,
    storage_offset=None,
    dtype=None,
    requires_grad=None,
    is_leaf=None,
    **metadata,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/side_effects.py
# Line: 104

def __init__(
    self,
    output_graph,
    id_to_variable=None,
    store_attr_mutations=None,
    keepalive=None,
    save_for_backward=None,
    tensor_hooks=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/guards.py
# Line: 632

def __init__(
    self,
    f_code: types.CodeType,
    id_ref: Callable[[Any, str], str],
    source_ref: Callable[[Source], str],
    lookup_weakrefs: Callable[[object], ReferenceType[object]],
    local_scope: dict[str, object],
    global_scope: dict[str, object],
    guard_manager: GuardManagerWrapper,
    check_fn_manager: CheckFunctionManager,
    serialization_mode: Optional[str] = None,

# ==================================================
# Line: 781

def getattr_on_nn_module(
    self,
    source,
    base_guard_manager,
    base_example_value,
    example_value,
    base_source_name,
    source_name,
    guard_manager_enum,

# ==================================================
# Line: 2624

def _unpickle_traceable_wrapper_subclass(
    cls, meta_tensor, device, pytype, dispatch_keys_raw, ctx, inner_data

# ==================================================
# Line: 2745

def __init__(
    self,
    f_code,
    output_graph=None,
    cache_entry=None,
    guard_fail_fn: Optional[Callable[[GuardFail], None]] = None,
    guard_filter_fn: Optional[
        Callable[[list[GuardFilterEntry]], list[bool]]
    ] = None,
    guards_serialization_mode: Optional[str] = None,
    shape_code_parts: Optional[ShapeCodeParts] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/eval_frame.py
# Line: 523

def __init__(
    self,
    callback: DynamoCallback,
    on_enter=nothing,
    backend_ctx_ctor=null_context,
    patch_fn=nothing,
    first_ctx=False,
    *,
    export=False,
    dynamic=None,
    compiler_config=None,

# ==================================================
# Line: 783

def __init__(
    self,
    callback,
    backend_ctx_ctor,
    first_ctx=False,
    *,
    export=False,
    dynamic=None,
    compiler_config=None,
    rebuild_ctx: Optional[
        Callable[[], Union[OptimizeContext, _NullDecorator]]
    ] = None,

# ==================================================
# Line: 923

def _optimize_catch_errors(
    compile_fn,
    hooks: Hooks,
    backend_ctx_ctor=null_context,
    export=False,
    dynamic=None,
    compiler_config=None,
    rebuild_ctx=None,

# ==================================================
# Line: 1020

def _optimize(
    rebuild_ctx: Callable[[], Union[OptimizeContext, _NullDecorator]],
    backend="inductor",
    *,
    nopython=False,
    guard_export_fn=None,
    guard_fail_fn=None,
    guard_filter_fn=None,
    frame_traced_fn=None,
    disable=False,
    dynamic=None,

# ==================================================
# Line: 1184

def __init__(
    self,
    m: torch.fx.GraphModule,
    flat_args: tuple[Any],
    matched_input_elements_positions: list[int],
    flat_results: list[Any],
    matched_output_elements_positions: list[int],
    example_fake_inputs: list[torch.Tensor],
    flat_args_dynamic_dims: list[set[int]],
    fake_mode: Optional[fake_tensor.FakeTensorMode] = None,

# ==================================================
# Line: 1350

def rewrite_signature(
    f_sig,
    graph,
    fake_mode,
    flat_args,
    in_spec,
    example_fake_inputs,
    graph_captured_input,
    graph_captured_output,
    dynamo_traced_result,
    flat_args_dynamic_dims,

# ==================================================
# Line: 1551

def export(
    f: Callable[..., Any],
    *extra_args,
    aten_graph: bool = False,
    pre_dispatch: bool = False,
    decomposition_table: Optional[
        dict[torch._ops.OpOverload, Callable[..., Any]]
    ] = None,
    tracing_mode: str = "symbolic",
    dynamic_shapes: Optional[Union[dict[str, Any], tuple[Any], list[Any]]] = None,
    specialize_float: bool = True,
    assume_static_by_default: bool = False,
    same_signature: bool = True,
    disable_constraint_solver: bool = False,
    prefer_deferred_runtime_asserts_over_guards: bool = False,
    allow_complex_guards_as_runtime_asserts: bool = False,
    _log_export_usage: bool = True,
    constraints: Optional[list[Constraint]] = None,
    **extra_kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/convert_frame.py
# Line: 678

def _compile(
    code: CodeType,
    globals: dict[str, object],
    locals: dict[str, object],
    builtins: dict[str, object],
    closure: tuple[CellType],
    compiler_fn: CompilerFn,
    one_graph: bool,
    export: bool,
    export_constraints: Optional[typing.Never],
    hooks: Hooks,
    cache_entry: Optional[CacheEntry],
    cache_size: CacheSizeRelevantForFrame,
    frame: Optional[DynamoFrameType] = None,
    frame_state: Optional[dict[str, Union[int, FrameStateSizeEntry]]] = None,
    *,
    compile_id: CompileId,
    skip: int = 0,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/symbolic_convert.py
# Line: 3171

def __init__(
    self,
    output: OutputGraph,
    instructions: list[Instruction],
    f_locals: dict[str, Any],
    f_globals: dict[str, Any],
    f_builtins: dict[str, Any],
    code_options: dict[str, Any],
    symbolic_locals: dict[str, VariableTracker],
    symbolic_globals: dict[str, VariableTracker],
    symbolic_torch_function_state: SymbolicTorchFunctionState,
    f_code: types.CodeType,
    export: bool,
    inline_depth: int,
    speculation_log: SpeculationLog,
    exn_vt_stack: ExceptionStack,
    distributed_state: Optional[DistributedState],
    # This determines whether to use the execution recorder.
    closure: Optional[tuple[types.CellType]] = None,

# ==================================================
# Line: 3290

def __init__(
    self,
    instructions: list[Instruction],
    f_code,
    f_locals,
    f_globals,
    f_builtins,
    closure,
    torch_function_mode_stack,
    code_options,
    compiler_fn,
    one_graph,
    export,
    export_constraints,
    frame_state,
    speculation_log: SpeculationLog,
    exn_vt_stack: ExceptionStack,
    distributed_state: Optional[DistributedState],

# ==================================================
# Line: 3930

def __init__(
    self,
    parent: InstructionTranslatorBase,
    code: types.CodeType,
    symbolic_locals: dict[str, VariableTracker],
    symbolic_globals: dict[str, VariableTracker],
    symbolic_torch_function_state: SymbolicTorchFunctionState,
    funcvar: BaseUserFunctionVariable,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/output_graph.py
# Line: 358

def __init__(
    self,
    code_options: dict[str, Any],
    compiler_fn: Optional[CompilerFn],
    root_tx,
    export: bool,
    export_constraints,
    frame_state,
    local_scope: Scope,
    global_scope: Scope,
    f_code,
    torch_function_mode_stack,

# ==================================================
# Line: 2363

def create_proxy(
    self,
    kind,
    target,
    args,
    kwargs,
    name=None,
    type_expr=None,
    proxy_factory_fn=None,

# ==================================================
# Line: 2546

def create_node(
    self, op, target, args=None, kwargs=None, name=None, type_expr=None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/compiled_autograd.py
# Line: 271

def begin_capture(
    self,
    inputs: list[torch.Tensor],
    sizes: list[int],
    scalars: list[Union[int, float]],
    origins: list[list[tuple[int, str]]],
    accumulate_grad: bool,
    check_nans: bool,

# ==================================================
# Line: 397

def proxy_call_aot_backward(
    self,
    pinputs,
    psaved_tensors,
    saved_tensors,
    pctx,
    ctx,
    maybe_backward_state_idx,

# ==================================================
# Line: 594

def proxy_call_backward(
    self,
    inputs,
    output_metadatas,
    saved_tensors,
    backward_idx: int,
    ctx: torch.autograd.function.BackwardCFunction,
    maybe_backward_state_idx: Optional[int],

# ==================================================
# Line: 645

def call_copy_slices_prologue(
    self,
    inputs,
    base_sizes,
    base_strides,
    base_storage_offset,
    view_sizes,
    view_strides,
    view_storage_offset,

# ==================================================
# Line: 1471

def copy_slices_prologue(
    inputs,
    base_sizes,
    base_strides,
    base_storage_offset,
    view_sizes,
    view_strides,
    view_storage_offset,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/misc.py
# Line: 874

def __init__(
    self,
    value,
    value_type=None,
    inference=False,
    saved_tensors=None,
    needs_input_grad=None,
    non_differentiable=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/tensor.py
# Line: 165

def __init__(
    self,
    proxy: torch.fx.Proxy,
    *,
    dtype,
    device,
    layout,
    ndim,
    requires_grad,
    is_nested,
    is_quantized,
    is_sparse,
    class_type,
    has_grad_fn,
    _size=None,
    stride=None,
    is_contiguous=None,
    _is_name_set=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/functions.py
# Line: 230

def _create_nested_fn(
    code, f_globals, name, defaults, closure, kwdefaults, annotations

# ==================================================
# Line: 1127

def __init__(
    self,
    fn_name,
    code,
    f_globals,
    defaults,
    kwdefaults,
    annotations,
    closure,
    # This is present when this function is created by
    # `functools.wrap(wrapped_fn)(this_fn)`.
    wrapped_fn=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/higher_order_ops.py
# Line: 601

def speculate_subgraph(
    tx,
    f,
    sub_args,
    sub_kwargs,
    description,
    *,
    # source_target is the .value of HigherOrderOpVariable and is the
    # target of the proxy that we created for the higherOrderOperator.
    source_target=None,
    always_restore=False,
    enable_grad=None,
    # NOTE [argument `set_subgraph_inputs`]
    # set_subgraph_inputs controls what how to construct subgraphs' placeholders from sub_args.
    # 1. if your HOP supports arbitrary inputs, use set_subgraph_inputs="automatic" (most recommended).
    # 2. if your HOP supports only Tensor and symnode inputs, use set_subgraph_inputs="flatten_manual" (recommended).
    # If sub_args contain Pytree structure (e.g. dict/list/tuple/set), the sub_args will be flattened first.
    # Then the flattened args are manually set as subgraph's placeholders.
    # 3. if your HOP must preserve inputs that are not tensor or symnode as placeholders e.g. AutogradFunctionContextVariable
    # use set_subgraph_inputs="manual" (not recommended). We do not recommend it in general because it has the
    # restriction that user need to manually control how to create placeholders and VariableTrackers for the args.
    set_subgraph_inputs="automatic",
    restore_side_effects=True,
    should_flatten_outputs=False,
    under_activation_checkpoint=False,
    # TODO - supports input_mutation and aliasing should be False by default for strictness
    supports_input_mutation=True,
    supports_aliasing=True,
    # Pass in an originating tracer - this is needed for preserving context
    # across fwd-bwd for autograd.Function
    tracer=None,

# ==================================================
# Line: 2058

def install_subgraph_in_output_graph(
    self, tx, fn_vt, fn_args_vt, kwargs, body_gmod, attr_name="wrap_body"

# ==================================================
# Line: 2066

def create_wrapped_node(
    self,
    tx: "InstructionTranslator",
    fn_vt,
    fn_args_vt,
    kwargs,
    description,
    under_activation_checkpoint=False,
    *,
    subgraph_name="wrap_body",

# ==================================================
# Line: 3347

def install_subgraph_in_output_graph(
    self, tx, fn_vt, fn_args_vt, kwargs, body_gmod, attr_name

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/amp/grad_scaler.py
# Line: 123

def __init__(
    self,
    device: str = "cuda",
    init_scale: float = 2.0**16,
    growth_factor: float = 2.0,
    backoff_factor: float = 0.5,
    growth_interval: int = 2000,
    enabled: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_meta_registrations.py
# Line: 106

def meta_linspace_logspace(
    start,
    end,
    steps,
    base=None,
    dtype=None,
    device=None,
    layout=torch.strided,
    pin_memory=False,
    requires_grad=False,

# ==================================================
# Line: 427

def meta_randint_low(
    low,
    high,
    size,
    *,
    dtype=torch.long,
    layout=None,
    device=None,
    pin_memory=None,

# ==================================================
# Line: 597

def meta_sparse_structured_addmm(
    input: Tensor,
    mat1: Tensor,
    mat1_meta: Tensor,
    mat2: Tensor,
    *,
    alpha=1,
    beta=1,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 632

def meta__cslt_sparse_mm(
    compressed_A: torch.Tensor,
    dense_B: torch.Tensor,
    bias: Optional[Tensor] = None,
    alpha: Optional[Tensor] = None,
    out_dtype: Optional[torch.dtype] = None,
    transpose_result: bool = False,
    alg_id: int = 0,
    split_k: int = 1,
    split_k_mode: int = -1,

# ==================================================
# Line: 717

def meta_segment_reduce(
    data: Tensor,
    reduce: str,
    *,
    lengths: Optional[Tensor] = None,
    indices: Optional[Tensor] = None,
    offsets: Optional[Tensor] = None,
    axis: int = 0,
    unsafe: bool = False,
    initial=None,

# ==================================================
# Line: 1540

def _linalg_solve_ex(
    A: Tensor,
    B: Tensor,
    *,
    left: bool = True,
    check_errors: bool = False,
    result: Optional[Tensor] = None,
    LU: Optional[Tensor] = None,
    pivots: Optional[Tensor] = None,
    info: Optional[Tensor] = None,

# ==================================================
# Line: 2223

def meta__fused_moving_avg_obs_fq_helper(
    self,
    observer_on,
    fake_quant_on,
    running_min,
    running_max,
    scale,
    zero_point,
    averaging_const,
    quant_min,
    quant_max,
    ch_axis,
    per_row_fake_quant=False,
    symmetric_quant=False,

# ==================================================
# Line: 2284

def calc_conv_nd_return_shape(
    input_tensor: torch.Tensor,
    weight: torch.Tensor,
    stride: Union[list[int], int],
    padding: Union[list[int], int],
    dilation: Union[list[int], int],
    is_transposed: bool,
    groups: int,
    output_padding: Optional[Union[list[int], int]] = None,

# ==================================================
# Line: 2396

def meta_miopen_batch_norm(
    input_tensor: torch.Tensor,
    weight: torch.Tensor,
    bias: Optional[torch.Tensor],
    running_mean: Optional[torch.Tensor],
    running_var: Optional[torch.Tensor],
    training: bool,
    exponential_average_factor: float,
    epsilon: float,

# ==================================================
# Line: 2434

def meta_conv(
    input_tensor: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    stride: list[int],
    padding: list[int],
    dilation: list[int],
    is_transposed: bool,
    output_padding: list[int],
    groups: int,

# ==================================================
# Line: 2484

def meta_mkldnn_convolution_default(
    input_tensor,
    weight,
    bias,
    padding,
    stride,
    dilation,
    groups,
    attr,
    scalars,
    algorithm,

# ==================================================
# Line: 2529

def meta_qconv_pointwise(
    x,
    x_scale,
    x_zp,
    w,  # prepacked_weight
    w_scale,
    w_zp,
    bias,
    stride,
    padding,
    dilation,
    groups,
    output_scale,
    output_zero_point,
    output_dtype,
    attr,
    scalars,
    algorithm,

# ==================================================
# Line: 2566

def meta_qconv2d_pointwise_binary(
    x,
    x_scale,
    x_zp,
    w,
    w_scale,
    w_zp,
    accum,
    bias,
    stride,
    padding,
    dilation,
    groups,
    output_scale,
    output_zero_point,
    output_dtype,
    accum_scale,
    accum_zero_point,
    binary_op_name,
    alpha,
    unary_op_name,
    unary_op_args,
    unary_op_algorithm,

# ==================================================
# Line: 2595

def meta_qlinear_pointwise(
    x,
    x_scale,
    x_zp,
    w,
    w_scale,
    w_zp,
    bias,
    output_scale,
    output_zero_point,
    output_dtype,
    post_op_name,
    post_op_args,
    post_op_algorithm,

# ==================================================
# Line: 2619

def meta_qlinear_pointwise_binary(
    x,
    x_scale,
    x_zp,
    w,
    w_scale,
    w_zp,
    x_2,
    bias,
    output_scale,
    output_zero_point,
    output_dtype,
    x2_scale,
    x2_zp,
    binary_op_name,
    alpha,
    unary_op_name,
    unary_op_args,
    unary_op_algorithm,

# ==================================================
# Line: 2724

def meta_avg_pool2d(
    input,
    kernel_size,
    stride=(),
    padding=(0,),
    ceil_mode=False,
    count_include_pad=True,
    divisor_override=None,

# ==================================================
# Line: 2805

def avg_pool2d_backward_shape_check(
    input,
    gradOutput,
    nbatch,
    kH,
    kW,
    dH,
    dW,
    padH,
    padW,
    nInputPlane,
    inputHeight,
    inputWidth,
    outputHeight,
    outputWidth,
    mem_format,

# ==================================================
# Line: 2850

def meta_avg_pool2d_backward(
    gradOutput_,
    input,
    kernel_size,
    stride,
    padding,
    ceil_mode,
    count_include_pad,
    divisor_override,

# ==================================================
# Line: 2924

def meta_avg_pool3d(
    input,
    kernel_size,
    stride=(),
    padding=(0,),
    ceil_mode=False,
    count_include_pad=True,
    divisor_override=None,

# ==================================================
# Line: 3014

def meta_avg_pool3d_backward(
    grad_output,
    input,
    kernel_size,
    stride,
    padding,
    ceil_mode,
    count_include_pad,
    divisor_override,

# ==================================================
# Line: 3453

def meta_convolution_backward(
    grad_output_,
    input_,
    weight_,
    bias_sizes_opt,
    stride,
    padding,
    dilation,
    transposed,
    output_padding,
    groups,
    output_mask,

# ==================================================
# Line: 3514

def meta__fused_adam_(
    self,
    grads,
    exp_avgs,
    exp_avg_sqs,
    max_exp_avg_sqs,
    state_steps,
    *,
    lr,
    beta1,
    beta2,
    weight_decay,
    eps,
    amsgrad,
    maximize,
    grad_scale=None,
    found_inf=None,

# ==================================================
# Line: 3540

def meta__fused_adam(
    self,
    grads,
    exp_avgs,
    exp_avg_sqs,
    max_exp_avg_sqs,
    state_steps,
    *,
    lr,
    beta1,
    beta2,
    weight_decay,
    eps,
    amsgrad,
    maximize,
    grad_scale=None,
    found_inf=None,

# ==================================================
# Line: 3909

def meta_embedding_bag(
    weight,
    indices,
    offsets,
    scale_grad_by_freq=False,
    mode=0,
    sparse=False,
    per_sample_weights=None,
    include_last_offset=False,
    padding_idx=-1,

# ==================================================
# Line: 4371

def pooling_output_shape_pad_lr(
    inputSize,
    kernelSize,
    pad_l,
    pad_r,
    stride,
    dilation,
    ceil_mode,

# ==================================================
# Line: 4413

def pool2d_shape_check(
    input,
    kH,
    kW,
    dH,
    dW,
    padH,
    padW,
    dilationH,
    dilationW,
    nInputPlane,
    inputHeight,
    inputWidth,
    outputHeight,
    outputWidth,
    memory_format,

# ==================================================
# Line: 4475

def pool3d_shape_check(
    input: Tensor,
    nslices: int,
    kT: int,
    kH: int,
    kW: int,
    dT: int,
    dH: int,
    dW: int,
    pT: int,
    pH: int,
    pW: int,
    dilationT: int,
    dilationH: int,
    dilationW: int,
    itime: int,
    iheight: int,
    iwidth: int,
    otime: int,
    oheight: int,
    owidth: int,
    fn_name: str,
    check_input_size: bool = False,

# ==================================================
# Line: 4567

def max_pool3d_backward_shape_check(
    input,
    grad_output,
    indices,
    nslices,
    kT,
    kH,
    kW,
    dT,
    dH,
    dW,
    pT,
    pH,
    pW,
    dilationT,
    dilationH,
    dilationW,
    itime,
    iheight,
    iwidth,
    otime,
    oheight,
    owidth,
    fn_name,

# ==================================================
# Line: 4629

def avg_pool3d_backward_shape_check(
    input: Tensor,
    grad_output: Tensor,
    nslices: int,
    kT: int,
    kH: int,
    kW: int,
    dT: int,
    dH: int,
    dW: int,
    pT: int,
    pH: int,
    pW: int,
    itime: int,
    iheight: int,
    iwidth: int,
    otime: int,
    oheight: int,
    owidth: int,
    fn_name: str,

# ==================================================
# Line: 4760

def meta_max_pool2d_with_indices_backward(
    grad_output,
    self,
    kernel_size,
    stride,
    padding,
    dilation,
    ceil_mode,
    indices,

# ==================================================
# Line: 5034

def meta_max_pool3d_with_indices_backward(
    grad_output,
    input,
    kernel_size,
    stride,
    padding,
    dilation,
    ceil_mode,
    indices,

# ==================================================
# Line: 5200

def grid_sampler_2d_backward_meta(
    grad_output,
    input,
    grid,
    interpolation_mode,
    padding_mode,
    align_corners,
    output_mask,

# ==================================================
# Line: 5239

def grid_sampler_3d_backward(
    grad_output,
    input,
    grid,
    interpolation_mode,
    padding_mode,
    align_corners,
    output_mask,

# ==================================================
# Line: 5601

def meta__scaled_dot_product_flash_attention(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    return_debug_mask: bool = False,
    scale: Optional[float] = None,

# ==================================================
# Line: 5666

def meta__scaled_dot_product_cudnn_attention(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    attn_bias: Optional[Tensor],
    compute_log_sumexp: bool,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    return_debug_mask: bool = False,
    scale: Optional[float] = None,

# ==================================================
# Line: 5721

def meta__scaled_dot_product_fused_attention_overrideable(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    attn_bias: Optional[Tensor] = None,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    return_debug_mask: bool = False,
    scale: Optional[float] = None,

# ==================================================
# Line: 5766

def meta__scaled_dot_product_flash_backward(
    grad_out: Tensor,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    out: Tensor,
    logsumexp: Tensor,
    cum_seq_q: Tensor,
    cum_seq_k: Tensor,
    max_q: int,
    max_k: int,
    dropout_p: float,
    is_causal: bool,
    philox_seed: Tensor,
    philox_offset: Tensor,
    scale: Optional[float] = None,

# ==================================================
# Line: 5794

def meta__scaled_dot_product_flash_attention_for_cpu(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    attn_mask: Optional[Tensor] = None,
    scale: Optional[float] = None,

# ==================================================
# Line: 5828

def meta__scaled_dot_product_flash_attention_for_cpu_backward(
    grad_out: Tensor,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    out: Tensor,
    logsumexp: Tensor,
    dropout_p: float,
    is_causal: bool,
    attn_mask: Optional[Tensor] = None,
    scale: Optional[float] = None,

# ==================================================
# Line: 5871

def meta__scaled_dot_product_efficient_attention(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    attn_bias: Optional[Tensor],
    compute_log_sumexp: bool,
    dropout_p=0.0,
    is_causal: bool = False,
    scale: Optional[float] = None,

# ==================================================
# Line: 5920

def meta__scaled_dot_product_efficient_backward(
    grad_out: Tensor,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    attn_bias: Optional[Tensor],
    out: Tensor,
    logsumexp: Tensor,
    philox_seed: Tensor,
    philox_offset: Tensor,
    dropout_p: float,
    grad_input_mask: list[bool],
    is_causal: bool = False,
    scale: Optional[float] = None,

# ==================================================
# Line: 5980

def meta__scaled_dot_product_cudnn_backward(
    grad_out: Tensor,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    out: Tensor,
    logsumexp: Tensor,
    philox_seed: Tensor,
    philox_offset: Tensor,
    attn_bias: Tensor,
    cum_seq_q: Tensor,
    cum_seq_k: Tensor,
    max_q: int,
    max_k: int,
    dropout_p: float,
    is_causal: bool,
    scale: Optional[float] = None,

# ==================================================
# Line: 6009

def meta__flash_attention_forward(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    cum_seq_q: Optional[Tensor],
    cum_seq_k: Optional[Tensor],
    max_q: int,
    max_k: int,
    dropout_p: float,
    is_causal: bool,
    return_debug_mask: bool,
    scale: Optional[float] = None,
    window_size_left: Optional[int] = None,
    window_size_right: Optional[int] = None,
    seqused_k: Optional[Tensor] = None,
    alibi_slopes: Optional[Tensor] = None,

# ==================================================
# Line: 6089

def meta__flash_attention_backward(
    grad_out: Tensor,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    out: Tensor,
    logsumexp: Tensor,
    cum_seq_q: Tensor,
    cum_seq_k: Tensor,
    max_q: int,
    max_k: int,
    dropout_p: float,
    is_causal: bool,
    philox_seed: Tensor,
    philox_offset: Tensor,
    scale: Optional[float] = None,
    window_size_left: Optional[int] = None,
    window_size_right: Optional[int] = None,

# ==================================================
# Line: 6120

def meta__efficient_attention_forward(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    bias: Optional[Tensor],
    cu_seqlens_q: Optional[Tensor],
    cu_seqlens_k: Optional[Tensor],
    max_seqlen_q: Optional[int],
    max_seqlen_k: Optional[int],
    dropout_p: float,
    custom_mask_type: int,
    compute_log_sumexp: bool = False,
    scale: Optional[float] = None,
    causal_diagonal: Optional[Tensor] = None,
    seqlen_k: Optional[Tensor] = None,
    window_size: Optional[int] = None,

# ==================================================
# Line: 6172

def meta__efficient_attention_backward(
    grad_out: Tensor,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    bias: Optional[Tensor],
    cu_seqlens_q: Optional[Tensor],
    cu_seqlens_k: Optional[Tensor],
    max_seqlen_q: torch.SymInt,
    max_seqlen_k: torch.SymInt,
    logsumexp: Tensor,
    dropout_p: float,
    philox_seed: Tensor,
    philox_offset: Tensor,
    custom_mask_type: int,
    bias_requires_grad: bool,
    scale: Optional[float] = None,
    num_splits_key: Optional[int] = None,
    shared_storage_dqdkdv: bool = False,

# ==================================================
# Line: 6228

def meta_scaled_mm(
    self: torch.Tensor,
    mat2: torch.Tensor,
    scale_a: torch.Tensor,
    scale_b: torch.Tensor,
    bias: Optional[torch.Tensor] = None,
    scale_result: Optional[torch.Tensor] = None,
    out_dtype: Optional[torch.dtype] = None,
    use_fast_accum: bool = False,

# ==================================================
# Line: 6620

def _cudnn_rnn(
    input,
    weight,
    weight_stride0,
    weight_buf,
    hx,
    cx,
    mode,
    hidden_size,
    proj_size,
    num_layers,
    batch_first,
    dropout,
    train,
    bidirectional,
    batch_sizes,
    dropout_state,

# ==================================================
# Line: 6676

def mkldnn_rnn_layer(
    input,
    w0,
    w1,
    w2,
    w3,
    hx_,
    cx_,
    reverse,
    batch_sizes,
    mode,
    hidden_size,
    num_layers,
    has_biases,
    bidirectional,
    batch_first,
    train,

# ==================================================
# Line: 6776

def meta__segment_reduce_backward(
    grad, output, data, reduce, lengths=None, offsets=None, axis=0, initial=None

# ==================================================
# Line: 6889

def mkldnn_rnn_layer_backward(
    input,
    weight0,
    weight1,
    weight2,
    weight3,
    hx_,
    cx_tmp,
    output,
    hy_,
    cy_,
    grad_output_r_opt,
    grad_hy_r_opt,
    grad_cy_r_opt,
    reverse,
    mode,
    hidden_size,
    num_layers,
    has_biases,
    train,
    bidirectional,
    batch_sizes,
    batch_first,
    workspace,

# ==================================================
# Line: 7156

def meta_embedding_bag_backward(
    grad,
    indices,
    offsets,
    offset2bag,
    bag_size,
    maximum_indices,
    num_weights,
    scale_grad_by_freq,
    mode,
    sparse,
    per_sample_weights,
    padding_idx=-1,

# ==================================================
# Line: 7199

def meta_embedding_bag_dense_backward(
    grad,
    indices,
    offset2bag,
    bag_size,
    maximum_indices,
    num_weights,
    scale_grad_by_freq,
    mode,
    per_sample_weights,
    padding_idx=-1,

# ==================================================
# Line: 7222

def meta_embedding_bag_per_sample_weights_backward(
    grad,
    weight,
    indices,
    offsets,
    offset2bag,
    mode,
    padding_idx=-1,

# ==================================================
# Line: 7348

def meta_scaled_grouped_mm(
    mat_a: torch.Tensor,
    mat_b: torch.Tensor,
    scale_a: torch.Tensor,
    scale_b: torch.Tensor,
    offs: Optional[torch.Tensor] = None,
    bias: Optional[torch.Tensor] = None,
    scale_result: Optional[torch.Tensor] = None,
    out_dtype: Optional[torch.dtype] = None,
    use_fast_accum: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_lobpcg.py
# Line: 258

def forward(  # type: ignore[override]
    ctx,
    A: Tensor,
    k: Optional[int] = None,
    B: Optional[Tensor] = None,
    X: Optional[Tensor] = None,
    n: Optional[int] = None,
    iK: Optional[Tensor] = None,
    niter: Optional[int] = None,
    tol: Optional[float] = None,
    largest: Optional[bool] = None,
    method: Optional[str] = None,
    tracker: None = None,
    ortho_iparams: Optional[dict[str, int]] = None,
    ortho_fparams: Optional[dict[str, float]] = None,
    ortho_bparams: Optional[dict[str, bool]] = None,

# ==================================================
# Line: 345

def lobpcg(
    A: Tensor,
    k: Optional[int] = None,
    B: Optional[Tensor] = None,
    X: Optional[Tensor] = None,
    n: Optional[int] = None,
    iK: Optional[Tensor] = None,
    niter: Optional[int] = None,
    tol: Optional[float] = None,
    largest: Optional[bool] = None,
    method: Optional[str] = None,
    tracker: None = None,
    ortho_iparams: Optional[dict[str, int]] = None,
    ortho_fparams: Optional[dict[str, float]] = None,
    ortho_bparams: Optional[dict[str, bool]] = None,

# ==================================================
# Line: 582

def _lobpcg(
    A: Tensor,
    k: Optional[int] = None,
    B: Optional[Tensor] = None,
    X: Optional[Tensor] = None,
    n: Optional[int] = None,
    iK: Optional[Tensor] = None,
    niter: Optional[int] = None,
    tol: Optional[float] = None,
    largest: Optional[bool] = None,
    method: Optional[str] = None,
    tracker: None = None,
    ortho_iparams: Optional[dict[str, int]] = None,
    ortho_fparams: Optional[dict[str, float]] = None,
    ortho_bparams: Optional[dict[str, bool]] = None,

# ==================================================
# Line: 694

def __init__(
    self,
    A: Optional[Tensor],
    B: Optional[Tensor],
    X: Tensor,
    iK: Optional[Tensor],
    iparams: dict[str, int],
    fparams: dict[str, float],
    bparams: dict[str, bool],
    method: str,
    tracker: None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_functional_collectives.py
# Line: 1077

def reduce_scatter_tensor_inplace(
    output: torch.Tensor,
    input: torch.Tensor,
    op: str = "sum",  # TODO type is actually c10d ReduceOp. is this ok?
    group=None,  # TODO add a type
    async_op: bool = False,
    scatter_dim: int = 0,
    tag: str = "",

# ==================================================
# Line: 1125

def all_to_all_inplace(
    output: torch.Tensor,
    input: torch.Tensor,
    output_split_sizes=None,
    input_split_sizes=None,
    group=None,
    async_op=False,
    tag: str = "",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/algorithms/ddp_comm_hooks/powerSGD_hook.py
# Line: 179

def __init__(
    self,
    process_group,
    matrix_approximation_rank=1,
    start_powerSGD_iter=1_000,
    min_compression_rate=2,
    use_error_feedback=True,
    warm_start=True,
    orthogonalization_epsilon=0,
    random_seed=0,
    compression_stats_logging_frequency=10_000,
    batch_tensors_with_same_shape: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/events/__init__.py
# Line: 83

def construct_and_record_rdzv_event(
    run_id: str,
    message: str,
    node_state: NodeState,
    name: str = "",
    hostname: str = "",
    pid: Optional[int] = None,
    master_endpoint: str = "",
    local_id: Optional[int] = None,
    rank: Optional[int] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py
# Line: 1011

def from_backend(
    cls,
    run_id: str,
    store: Store,
    backend: RendezvousBackend,
    min_nodes: int,
    max_nodes: int,
    local_addr: Optional[str] = None,
    timeout: Optional[RendezvousTimeout] = None,
    keep_alive_interval: int = 5,
    keep_alive_max_attempt: int = 3,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/etcd_rendezvous.py
# Line: 225

def __init__(
    self,
    client,
    prefix,
    run_id,
    num_min_workers,
    num_max_workers,
    timeout,
    last_call_timeout,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/api.py
# Line: 260

def __init__(
    self,
    backend: str,
    endpoint: str,
    run_id: str,
    min_nodes: int,
    max_nodes: int,
    local_addr: Optional[str] = None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/static_tcp_rendezvous.py
# Line: 39

def __init__(
    self,
    master_addr: str,
    master_port: int,
    rank: int,
    world_size: int,
    run_id: str,
    timeout: int,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/utils/store.py
# Line: 167

def barrier(
    store,
    world_size: int,
    key_prefix: str,
    barrier_timeout: float = 300,
    rank: Optional[int] = None,
    rank_tracing_decoder: Optional[Callable[[int], str]] = None,
    trace_timeout: float = 10,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/utils/distributed.py
# Line: 30

def create_c10d_store(
    is_server: bool,
    server_addr: str,
    server_port: int = -1,
    world_size: int = 1,
    timeout: float = (60 * 10),  # 10 min
    wait_for_workers: bool = True,
    retries=3,
    use_libuv: Optional[bool] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/multiprocessing/__init__.py
# Line: 101

def start_processes(
    name: str,
    entrypoint: Union[Callable, str],
    args: dict[int, tuple],
    envs: dict[int, dict[str, str]],
    logs_specs: LogsSpecs,
    log_line_prefixes: Optional[dict[int, str]] = None,
    start_method: str = "spawn",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/multiprocessing/api.py
# Line: 441

def __init__(
    self,
    name: str,
    entrypoint: Union[Callable, str],
    args: dict[int, tuple],
    envs: dict[int, dict[str, str]],
    logs_specs: LogsSpecs,
    log_line_prefixes: Optional[dict[int, str]] = None,

# ==================================================
# Line: 591

def _wrap(
    local_rank: int,
    fn: Callable,
    args: dict[int, tuple],
    envs: dict[int, dict[str, str]],
    stdout_redirects: dict[int, str],  # redirect file for stdout (to console if None)
    stderr_redirects: dict[int, str],  # redirect file for stderr (to console if None)
    ret_vals: dict[int, mp.SimpleQueue],
    queue_finished_reading_event: synchronize.Event,

# ==================================================
# Line: 624

def __init__(
    self,
    name: str,
    entrypoint: Callable,
    args: dict[int, tuple],
    envs: dict[int, dict[str, str]],
    start_method: str,
    logs_specs: LogsSpecs,
    log_line_prefixes: Optional[dict[int, str]] = None,

# ==================================================
# Line: 806

def __init__(
    self,
    name: str,
    entrypoint: str,
    args: dict[int, tuple],
    envs: dict[int, dict[str, str]],
    logs_specs: LogsSpecs,
    log_line_prefixes: Optional[dict[int, str]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/multiprocessing/subprocess_handler/subprocess_handler.py
# Line: 34

def __init__(
    self,
    entrypoint: str,
    args: tuple,
    env: dict[str, str],
    stdout: Optional[str],
    stderr: Optional[str],
    local_rank_id: int,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_state_dict_utils.py
# Line: 73

def _iterate_state_dict(
    iter_object: Any,
    sharded_tensor_func: Callable,
    dtensor_func: Callable,
    tensor_func: Callable,
    *,
    pg: Optional[dist.ProcessGroup] = None,
    device: Optional[torch.device] = None,
    cpu_offload: bool = False,
    companion_obj: Any = None,
    ranks_only: tuple[int, ...] = (),
    type_check: bool = True,
    non_blocking: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_symmetric_memory/__init__.py
# Line: 490

def _fused_all_gather_matmul_impl(
    mm_out_op: torch._ops.OpOverload,
    A_shard: torch.Tensor,
    Bs: list[torch.Tensor],
    A_scale: Optional[torch.Tensor],
    kwargs_list: list[dict[str, Any]],
    out_dtypes: list[Optional[torch.dtype]],
    gather_dim: int,
    group_name: str,
    return_A: bool,

# ==================================================
# Line: 808

def _fused_all_gather_scaled_matmul_fallback(
    A_shard: torch.Tensor,
    Bs: list[torch.Tensor],
    A_scale: torch.Tensor,
    B_scales: list[torch.Tensor],
    gather_dim: int,
    group_name: str,
    biases: list[Optional[torch.Tensor]],
    result_scales: list[Optional[torch.Tensor]],
    out_dtypes: list[Optional[torch.dtype]],
    use_fast_accum: list[bool],

# ==================================================
# Line: 848

def scaled_matmul(
    A: torch.Tensor,
    B: torch.Tensor,
    A_scale: torch.Tensor,
    B_scale: torch.Tensor,
    bias: Optional[torch.Tensor],
    result_scale: Optional[torch.Tensor],
    out_dtype: Optional[torch.dtype],
    use_fast_accum: bool,

# ==================================================
# Line: 882

def _fused_all_gather_scaled_matmul(
    A_shard: torch.Tensor,
    Bs: list[torch.Tensor],
    A_scale: torch.Tensor,
    B_scales: list[torch.Tensor],
    gather_dim: int,
    group_name: str,
    biases: list[Optional[torch.Tensor]],
    result_scales: list[Optional[torch.Tensor]],
    out_dtypes: list[Optional[torch.dtype]],
    use_fast_accum: list[bool],

# ==================================================
# Line: 1037

def _fused_matmul_reduce_scatter_impl(
    mm_out_op: torch._ops.OpOverload,
    A: torch.Tensor,
    B: torch.Tensor,
    kwargs: dict[str, Any],
    out_dtype: Optional[torch.dtype],
    reduce_op: str,
    scatter_dim: int,
    group_name: str,

# ==================================================
# Line: 1094

def _fused_scaled_matmul_reduce_scatter(
    A: torch.Tensor,
    B: torch.Tensor,
    A_scale: torch.Tensor,
    B_scale: torch.Tensor,
    reduce_op: str,
    orig_scatter_dim: int,
    scatter_dim_after_maybe_reshape: int,
    group_name: str,
    output_shape: list[int],
    bias: Optional[torch.Tensor] = None,
    result_scale: Optional[torch.Tensor] = None,
    out_dtype: Optional[torch.dtype] = None,
    use_fast_accum: bool = False,

# ==================================================
# Line: 1148

def _fused_scaled_matmul_reduce_scatter_fallback(
    A: torch.Tensor,
    B: torch.Tensor,
    A_scale: torch.Tensor,
    B_scale: torch.Tensor,
    reduce_op: str,
    orig_scatter_dim: int,
    scatter_dim_after_maybe_reshape: int,
    group_name: str,
    output_shape: list[int],
    bias: Optional[torch.Tensor] = None,
    result_scale: Optional[torch.Tensor] = None,
    out_dtype: Optional[torch.dtype] = None,
    use_fast_accum: bool = False,

# ==================================================
# Line: 1198

def _fused_scaled_matmul_reduce_scatter_impl(
    mm_out_op: torch._ops.OpOverload,
    A: torch.Tensor,
    B: torch.Tensor,
    A_scale: torch.Tensor,
    kwargs: dict[str, Any],
    out_dtype: Optional[torch.dtype],
    reduce_op: str,
    orig_scatter_dim: int,
    scatter_dim_after_maybe_reshape: int,
    group_name: str,
    output_shape: list[int],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_trace_utils.py
# Line: 115

def _patched_call_module(
    self,
    call_module: Callable,
    exec_info: _ExecutionInfo,
    # Below are the expected arguments to `call_module()`
    module: nn.Module,
    forward: Callable,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],

# ==================================================
# Line: 159

def _patched_create_proxy(
    self,
    create_proxy: Callable,
    exec_info: _ExecutionInfo,
    fqn_to_param: dict[str, nn.Parameter],
    # Below are the expected arguments to `create_proxy()`
    kind: str,
    target: torch.fx.node.Target,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    name: Optional[str] = None,
    type_expr: Optional[Any] = None,
    proxy_factory_fn: Optional[Callable[[torch.fx.Node], torch.fx.Proxy]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_init_utils.py
# Line: 415

def _init_core_state(
    state: _FSDPState,
    sharding_strategy: Optional[ShardingStrategy],
    mixed_precision: Optional[MixedPrecision],
    cpu_offload: Optional[CPUOffload],
    limit_all_gathers: bool,
    use_orig_params: bool,
    backward_prefetch_limit: int,
    forward_prefetch_limit: int,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_optim_utils.py
# Line: 1700

def _convert_state_with_orig_params(
    all_optim_state_keys: list[_OptimStateKey],
    optim_state_key_to_param_key: dict[_OptimStateKey, Union[int, str]],
    fqn_to_fsdp_param_info: dict[str, FSDPParamInfo],
    optim_state_dict: dict[Union[str, int], Any],
    to_save: bool,
    shard_state: bool,
    cpu_offload: bool = True,

# ==================================================
# Line: 1791

def _convert_state_with_flat_params(
    all_optim_state_keys: list[_OptimStateKey],
    optim_state_key_to_param_key: dict[_OptimStateKey, Union[int, str]],
    fqn_to_fsdp_param_info: dict[str, FSDPParamInfo],
    optim_state_dict: dict[Union[str, int], Any],
    to_save: bool,
    shard_state: bool,
    cpu_offload: bool = True,

# ==================================================
# Line: 1850

def _optim_state_dict(
    model: nn.Module,
    optim: torch.optim.Optimizer,
    optim_state_dict: dict[str, Any],
    optim_input: Optional[
        Union[
            list[dict[str, Any]],
            Iterable[nn.Parameter],
        ]
    ],
    rank0_only: bool,
    shard_state: bool,
    group: Optional[dist.ProcessGroup],
    using_optim_input: bool,
    use_orig_params: bool = False,
    cpu_offload: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/fully_sharded_data_parallel.py
# Line: 401

def __init__(
    self,
    module: nn.Module,
    process_group: ProcessGroupType = None,
    sharding_strategy: Optional[ShardingStrategy] = None,
    cpu_offload: Optional[CPUOffload] = None,
    auto_wrap_policy: Optional[
        Union[Callable, ModuleWrapPolicy, CustomPolicy]
    ] = None,
    backward_prefetch: Optional[BackwardPrefetch] = BackwardPrefetch.BACKWARD_PRE,
    mixed_precision: Optional[MixedPrecision] = None,
    ignored_modules: Optional[Iterable[torch.nn.Module]] = None,
    param_init_fn: Optional[Callable[[nn.Module], None]] = None,
    device_id: Optional[Union[int, torch.device]] = None,
    sync_module_states: bool = False,
    forward_prefetch: bool = False,
    limit_all_gathers: bool = True,
    use_orig_params: bool = False,
    ignored_states: Union[
        Optional[Iterable[torch.nn.Parameter]], Optional[Iterable[torch.nn.Module]]
    ] = None,
    device_mesh: Optional[DeviceMesh] = None,

# ==================================================
# Line: 1250

def _optim_state_dict_impl(
    model: torch.nn.Module,
    optim: torch.optim.Optimizer,
    optim_state_dict: dict[str, Any],
    optim_input: Optional[
        Union[
            list[dict[str, Any]],
            Iterable[torch.nn.Parameter],
        ]
    ] = None,
    rank0_only: bool = True,
    full_state_dict: bool = True,
    group: Optional[dist.ProcessGroup] = None,
    cpu_offload: bool = True,
    *,
    _stacklevel: int = 1,

# ==================================================
# Line: 1307

def _optim_state_dict_to_load_impl(
    optim_state_dict: dict[str, Any],
    model: torch.nn.Module,
    optim_input: Optional[
        Union[
            list[dict[str, Any]],
            Iterable[torch.nn.Parameter],
        ]
    ] = None,
    optim: Optional[torch.optim.Optimizer] = None,
    full_state_dict: bool = True,
    rank0_only: bool = False,
    is_named_optimizer: bool = False,
    group: Optional[dist.ProcessGroup] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_fsdp_extensions.py
# Line: 41

def chunk_tensor(
    self,
    tensor: torch.Tensor,
    rank: int,
    world_size: int,
    num_devices_per_node: int,
    pg: dist.ProcessGroup,
    device: Optional[torch.device] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_fully_shard/_fsdp_param_group.py
# Line: 117

def __init__(
    self,
    params: list[nn.Parameter],
    modules: tuple[nn.Module, ...],
    mesh_info: FSDPMeshInfo,
    post_forward_mesh_info: Optional[FSDPMeshInfo],
    device: torch.device,
    shard_placement_fn: Optional[Callable[[nn.Parameter], Optional[Shard]]],
    mp_policy: MixedPrecisionPolicy,
    offload_policy: OffloadPolicy,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_fully_shard/_fsdp_collectives.py
# Line: 50

def all_gather_copy_in_meta(
    all_gather_inputs: list[torch.Tensor],
    inp_split_sizes: list[int],
    all_gather_input_numel: int,
    world_size: int,
    rank: int,
    dtype: torch.dtype,
    device: torch.device,

# ==================================================
# Line: 74

def all_gather_copy_in_cuda(
    all_gather_inputs: list[torch.Tensor],
    inp_split_sizes: list[int],
    all_gather_input_numel: int,
    world_size: int,
    rank: int,
    dtype: torch.dtype,
    device: torch.device,

# ==================================================
# Line: 349

def foreach_reduce(
    fsdp_params: list[FSDPParam],
    unsharded_grads: list[torch.Tensor],
    reduce_scatter_group: dist.ProcessGroup,
    reduce_scatter_stream: torch.Stream,
    orig_dtype: Optional[torch.dtype],
    reduce_dtype: Optional[torch.dtype],
    device: torch.device,
    reduce_scatter_reduce_op: Optional[Union[dist.ReduceOp, dist.ReduceOp.RedOpType]],
    all_reduce_group: Optional[dist.ProcessGroup],  # not `None` iff HSDP
    all_reduce_stream: torch.Stream,
    all_reduce_grads: bool,
    partial_reduce_output: Optional[torch.Tensor],  # only used for HSDP
    all_reduce_hook: Optional[Callable[[torch.Tensor], None]],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_fully_shard/_fsdp_param.py
# Line: 222

def __init__(
    self,
    param: nn.Parameter,
    module_info: ParamModuleInfo,
    mesh_info: FSDPMeshInfo,
    post_forward_mesh_info: Optional[FSDPMeshInfo],
    device: torch.device,
    shard_placement_fn: Optional[Callable[[nn.Parameter], Optional[Shard]]],
    mp_policy: MixedPrecisionPolicy,
    offload_policy: OffloadPolicy,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/sharded_grad_scaler.py
# Line: 92

def __init__(
    self,
    device: str = "cuda",
    init_scale: float = 2.0**16,
    backoff_factor: float = 0.5,
    growth_factor: float = 2.0,
    growth_interval: int = 2000,
    enabled: bool = True,
    process_group: Optional[ProcessGroup] = dist.group.WORLD,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_flat_param.py
# Line: 372

def _init_metadata(
    cls,
    self,
    param_infos: list[ParamInfo],
    numels: list[int],
    shapes: list[torch.Size],
    strides: list[tuple[int, ...]],
    contiguities: list[bool],
    fqns: list[str],
    shared_param_infos: list[SharedParamInfo],
    param_extensions: list[Optional[Any]],
    params: Optional[list[nn.Parameter]],
    shared_params: Optional[list[nn.Parameter]],
    is_padding_mask: list[bool],

# ==================================================
# Line: 488

def __init__(
    self,
    params: Sequence[Union[nn.Parameter, Tensor]],
    fully_sharded_module: nn.Module,
    device: torch.device,
    sharding_strategy: HandleShardingStrategy,
    offload_params: bool,
    mp_param_dtype: Optional[torch.dtype],
    mp_reduce_dtype: Optional[torch.dtype],
    keep_low_precision_grads: bool,
    process_group: dist.ProcessGroup,
    use_orig_params: bool,
    *,
    fsdp_extension: Optional[FSDPExtensions] = None,

# ==================================================
# Line: 2357

def _writeback_tensor(
    self,
    src_tensor: Optional[Tensor],
    dst_tensor: Tensor,
    tensor_index: int,
    expected_shape: torch.Size,
    offset: int,
    is_param: bool,  # else gradient

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/distributed_c10d.py
# Line: 493

def __init__(
    self,
    op: Callable,
    tensor: torch.Tensor,
    peer: Optional[int] = None,
    group: Optional[ProcessGroup] = None,
    tag: int = 0,
    group_peer: Optional[int] = None,

# ==================================================
# Line: 512

def __new__(
    cls,
    op: Callable,
    tensor: torch.Tensor,
    peer: Optional[int] = None,
    group: Optional[ProcessGroup] = None,
    tag: int = 0,
    group_peer: Optional[int] = None,

# ==================================================
# Line: 1542

def init_process_group(
    backend: Optional[str] = None,
    init_method: Optional[str] = None,
    timeout: Optional[timedelta] = None,
    world_size: int = -1,
    rank: int = -1,
    store: Optional[Store] = None,
    group_name: str = "",
    pg_options: Optional[Any] = None,
    device_id: Optional[torch.device] = None,

# ==================================================
# Line: 1811

def _new_process_group_helper(
    group_size,
    group_rank,
    global_ranks_in_group,
    backend,
    store,
    group_name,
    backend_options=None,
    timeout=None,
    pg_tag=None,
    device_id=None,
    group_desc=None,

# ==================================================
# Line: 5140

def new_group(
    ranks=None,
    timeout=None,
    backend=None,
    pg_options=None,
    use_local_synchronization=False,
    group_desc=None,
    device_id: Optional[torch.device] = None,

# ==================================================
# Line: 5229

def _new_group_with_tag(
    ranks=None,
    timeout=None,
    backend=None,
    backend_options=None,
    pg_tag=None,
    use_local_synchronization=False,
    group_desc=None,
    device_id: Optional[torch.device] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharding_spec/chunk_sharding_spec_ops/_common.py
# Line: 83

def _handle_col_wise_sharding_base(
    op_func,
    col_dim,
    input,
    world_size,
    weight,
    local_shard,
    pg,
    gathered_inputs,
    mode=None,
    gathered_per_sample_weights=None,
    gathered_offsets=None,
    padding_idx=None,

# ==================================================
# Line: 221

def _handle_max_norm_col_wise(
    max_norm,
    norm_type,
    local_shard,
    input,
    world_size,
    gathered_inputs,
    pg,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharding_spec/chunk_sharding_spec_ops/embedding.py
# Line: 186

def _handle_col_wise_sharding(
    input, world_size, weight, local_shard, max_norm, norm_type, padding_idx, pg

# ==================================================
# Line: 234

def _handle_row_wise_sharding(
    input, world_size, weight, local_shard, max_norm, norm_type, padding_idx, rank, pg

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharding_spec/chunk_sharding_spec_ops/embedding_bag.py
# Line: 239

def _handle_col_wise_sharding(
    input,
    world_size,
    weight,
    local_shard,
    offsets,
    per_sample_weights,
    mode,
    max_norm,
    norm_type,
    padding_idx,
    pg,

# ==================================================
# Line: 312

def _handle_row_wise_sharding(
    input,
    world_size,
    weight,
    local_shard,
    offsets,
    per_sample_weights,
    mode,
    max_norm,
    norm_type,
    padding_idx,
    rank,
    pg,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharded_tensor/__init__.py
# Line: 26

def empty(
    sharding_spec: ShardingSpec,
    *size,
    dtype=None,
    layout=torch.strided,
    requires_grad=False,
    pin_memory=False,
    memory_format=torch.contiguous_format,
    process_group=None,
    init_rrefs=False,

# ==================================================
# Line: 81

def ones(
    sharding_spec: ShardingSpec,
    *size,
    dtype=None,
    layout=torch.strided,
    requires_grad=False,
    pin_memory=False,
    memory_format=torch.contiguous_format,
    process_group=None,
    init_rrefs=False,

# ==================================================
# Line: 135

def zeros(
    sharding_spec: ShardingSpec,
    *size,
    dtype=None,
    layout=torch.strided,
    requires_grad=False,
    pin_memory=False,
    memory_format=torch.contiguous_format,
    process_group=None,
    init_rrefs=False,

# ==================================================
# Line: 189

def full(
    sharding_spec: ShardingSpec,
    size,
    fill_value,
    *,
    dtype=None,
    layout=torch.strided,
    requires_grad=False,
    pin_memory=False,
    memory_format=torch.contiguous_format,
    process_group=None,
    init_rrefs=False,

# ==================================================
# Line: 245

def rand(
    sharding_spec: ShardingSpec,
    *size,
    dtype=None,
    layout=torch.strided,
    requires_grad=False,
    pin_memory=False,
    memory_format=torch.contiguous_format,
    process_group=None,
    init_rrefs=False,

# ==================================================
# Line: 301

def randn(
    sharding_spec: ShardingSpec,
    *size,
    dtype=None,
    layout=torch.strided,
    requires_grad=False,
    pin_memory=False,
    memory_format=torch.contiguous_format,
    process_group=None,
    init_rrefs=False,

# ==================================================
# Line: 426

def pre_load_state_dict_hook(
    module,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_shard/sharded_tensor/api.py
# Line: 247

def __init__(
    self,
    sharding_spec: shard_spec.ShardingSpec,
    *size,
    dtype=None,
    layout=torch.strided,
    requires_grad=False,
    pin_memory=False,
    memory_format=torch.contiguous_format,
    process_group=None,
    init_rrefs=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/filesystem.py
# Line: 357

def _write_files_from_queue(
    create_stream: Callable,
    file_queue: queue.Queue,
    result_queue: queue.Queue,
    planner: SavePlanner,
    transforms: _StorageWriterTransforms,
    inflight_threshhold: int,
    use_fsync: bool,
    thread_count: int,
    serialization_format: SerializationFormat,

# ==================================================
# Line: 562

def __init__(
    self,
    path: Union[str, os.PathLike],
    single_file_per_rank: bool = True,
    sync_files: bool = True,
    thread_count: int = 1,
    per_thread_copy_ahead: int = 10_000_000,
    overwrite: bool = True,
    _extensions: Optional[Sequence[StreamTransformExtension]] = None,
    serialization_format: SerializationFormat = SerializationFormat.TORCH_SAVE,
    *args: Any,
    **kwargs: Any,

# ==================================================
# Line: 905

def __init__(
    self,
    path: Union[str, os.PathLike],
    single_file_per_rank: bool = True,
    sync_files: bool = True,
    thread_count: int = 1,
    per_thread_copy_ahead: int = 10_000_000,
    cache_staged_state_dict: bool = False,
    overwrite: bool = True,
    _extensions: Optional[Sequence[StreamTransformExtension]] = None,
    serialization_format: SerializationFormat = SerializationFormat.TORCH_SAVE,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/_fsspec_filesystem.py
# Line: 115

def __init__(
    self,
    path: Union[str, os.PathLike],
    single_file_per_rank: bool = True,
    sync_files: bool = True,
    thread_count: int = 1,
    per_thread_copy_ahead: int = 10_000_000,
    overwrite: bool = True,
    _extensions: Optional[Sequence[StreamTransformExtension]] = None,
    serialization_format: SerializationFormat = SerializationFormat.TORCH_SAVE,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/_checkpointer.py
# Line: 32

def __init__(
    self,
    storage_writer: StorageWriter,
    storage_reader: StorageReader,
    *,
    process_group: Optional[dist.ProcessGroup] = None,
    coordinator_rank: int = 0,
    no_dist: bool = False,
    load_planner: Optional[LoadPlanner] = None,
    save_planner: Optional[SavePlanner] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_tp_conv.py
# Line: 40

def _ring_send_recv_construct(in_tensor, d1, d2, left, right, rank, size):
    # dist comms and reconstruct local input tensor
    send_to_right = in_tensor[:, :, :, -d1:].contiguous()
    send_to_left = in_tensor[:, :, :, :d2].contiguous()
    recv_from_right = torch.zeros_like(send_to_left)
    recv_from_left = torch.zeros_like(send_to_right)

    send_op_right = dist.P2POp(dist.isend, send_to_right, right)
    send_op_left = dist.P2POp(dist.isend, send_to_left, left)
    recv_op_right = dist.P2POp(dist.irecv, recv_from_right, right)
    recv_op_left = dist.P2POp(dist.irecv, recv_from_left, left)

    reqs = dist.batch_isend_irecv(
        [send_op_right, send_op_left, recv_op_left, recv_op_right]
    )
    for req in reqs:
        req.wait()

    if rank == 0:
        in_tensor = torch.cat([in_tensor, recv_from_right], dim=-1)
    elif rank == size - 1:
        in_tensor = torch.cat([recv_from_left, in_tensor], dim=-1)
    else:
        in_tensor = torch.cat([recv_from_left, in_tensor, recv_from_right], dim=-1)

    return in_tensor



# ==================================================
# Line: 68

def _ring_send_recv_aggregate(grad_in_tensor, d1, d2, left, right, rank, size):
    # dist comms and aggregate gradients for edge pixels
    send_to_right = grad_in_tensor[:, :, :, -d2:].contiguous()
    send_to_left = grad_in_tensor[:, :, :, :d1].contiguous()
    recv_from_right = torch.zeros_like(send_to_left)
    recv_from_left = torch.zeros_like(send_to_right)

    send_op_right = dist.P2POp(dist.isend, send_to_right, right)
    send_op_left = dist.P2POp(dist.isend, send_to_left, left)
    recv_op_right = dist.P2POp(dist.irecv, recv_from_right, right)
    recv_op_left = dist.P2POp(dist.irecv, recv_from_left, left)

    reqs = dist.batch_isend_irecv(
        [send_op_right, send_op_left, recv_op_left, recv_op_right]
    )
    for req in reqs:
        req.wait()

    if rank == 0:
        grad_in_tensor = grad_in_tensor[:, :, :, :-d2]
        grad_in_tensor[:, :, :, -d1:] = torch.add(
            grad_in_tensor[:, :, :, -d1:], recv_from_right
        )
    elif rank == size - 1:
        grad_in_tensor = grad_in_tensor[:, :, :, d1:]
        grad_in_tensor[:, :, :, :d2] = torch.add(
            grad_in_tensor[:, :, :, :d2], recv_from_left
        )
    else:
        grad_in_tensor = grad_in_tensor[:, :, :, d1:-d2]
        grad_in_tensor[:, :, :, -d1:] = torch.add(
            grad_in_tensor[:, :, :, -d1:], recv_from_right
        )
        grad_in_tensor[:, :, :, :d2] = torch.add(
            grad_in_tensor[:, :, :, :d2], recv_from_left
        )



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_redistribute.py
# Line: 285

def forward(  # type: ignore[override]
    # pyre-fixme[2]: Parameter must be annotated.
    ctx,
    input: "dtensor.DTensor",
    device_mesh: DeviceMesh,
    placements: tuple[Placement, ...],
    async_op: bool = False,
    forward_dtype: Optional[torch.dtype] = None,
    backward_dtype: Optional[torch.dtype] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/parallel/fsdp.py
# Line: 360

def chunk_tensor(
    self,
    tensor: torch.Tensor,
    rank: int,
    world_size: int,
    num_devices_per_node: int,
    pg: dist.ProcessGroup,
    device: Optional[torch.device] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/parallel/style.py
# Line: 764

def __init__(
    self,
    *,
    input_layouts: Optional[Union[Placement, tuple[Optional[Placement]]]] = None,
    desired_input_layouts: Optional[
        Union[Placement, tuple[Optional[Placement]]]
    ] = None,
    input_kwarg_layouts: Optional[dict[str, Placement]] = None,
    desired_input_kwarg_layouts: Optional[dict[str, Placement]] = None,
    use_local_input: bool = False,
    output_layouts: Union[Placement, tuple[Placement]],
    desired_output_layouts: Union[Placement, tuple[Placement]],
    use_local_output: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/parallel/loss.py
# Line: 198

def _nll_loss_forward(
    x: Tensor,
    target: Tensor,
    weight: Optional[Tensor],
    local_weight: Optional[Tensor],
    reduction: int,
    ignore_index: int,
    input_shape: torch.Size,
    channel_dim: int,
    mesh: DeviceMesh,
    mesh_dim: int,

# ==================================================
# Line: 346

def _nll_loss_and_log_softmax_backward(
    grad_output: Tensor,
    x: Tensor,
    target: Tensor,
    weight: Optional[Tensor],
    reduction: int,
    ignore_index: int,
    total_weight: Tensor,
    input_shape: torch.Size,
    channel_dim: int,
    mesh: DeviceMesh,
    mesh_dim: int,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/experimental/_attention.py
# Line: 196

def _scaled_dot_product_ring_flash_attention(
    mesh: DeviceMesh,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    return_debug_mask: bool = False,
    *,
    scale: Optional[float] = None,

# ==================================================
# Line: 224

def _scaled_dot_product_ring_efficient_attention(
    mesh: DeviceMesh,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attn_bias: Optional[torch.Tensor] = None,
    compute_log_sumexp: bool = True,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    *,
    scale: Optional[float] = None,

# ==================================================
# Line: 259

def _scaled_dot_product_ring_cudnn_attention(
    mesh: DeviceMesh,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attn_bias: Optional[torch.Tensor] = None,
    compute_log_sumexp: bool = True,
    dropout_p: float = 0.0,
    is_causal: bool = False,
    return_debug_mask: bool = False,
    *,
    scale: Optional[float] = None,

# ==================================================
# Line: 392

def _templated_ring_attention(
    mesh: DeviceMesh,
    seq_dim: int,
    op: _AttentionOp,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    is_causal: bool = False,
    **kwargs: object,

# ==================================================
# Line: 652

def _templated_ring_attention_backward(
    mesh: DeviceMesh,
    seq_dim: int,
    op: _AttentionOp,
    grad_out: torch.Tensor,
    grad_out_name: str,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    is_causal: bool,
    **kwargs: Any,

# ==================================================
# Line: 821

def _scaled_dot_product_ring_flash_attention_backward(
    mesh: DeviceMesh,
    grad_out: torch.Tensor,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    cum_seq_q: torch.Tensor,
    cum_seq_k: torch.Tensor,
    max_q: int,
    max_k: int,
    dropout_p: float,
    is_causal: bool,
    philox_seed: torch.Tensor,
    philox_offset: torch.Tensor,
    *,
    scale: Optional[float] = None,

# ==================================================
# Line: 864

def _scaled_dot_product_ring_efficient_attention_backward(
    mesh: DeviceMesh,
    grad_out: torch.Tensor,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    bias: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    philox_seed: torch.Tensor,
    philox_offset: torch.Tensor,
    dropout_p: float,
    grad_input_mask: tuple[bool, ...],
    is_causal: bool = False,
    *,
    scale: Optional[float] = None,

# ==================================================
# Line: 903

def _scaled_dot_product_ring_cudnn_attention_backward(
    mesh: DeviceMesh,
    grad_out: torch.Tensor,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    out: torch.Tensor,
    logsumexp: torch.Tensor,
    philox_seed: torch.Tensor,
    philox_offset: torch.Tensor,
    attn_bias: torch.Tensor,
    cum_seq_q: torch.Tensor,
    cum_seq_k: torch.Tensor,
    max_q: int,
    max_k: int,
    dropout_p: float,
    is_causal: bool,
    *,
    scale: Optional[float] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/experimental/_tp_transform.py
# Line: 76

def __init__(
    self,
    rank: int,
    world_size: int,
    device_type: str,
    state_dict: dict[str, torch.Tensor],
    graph_signature: ExportGraphSignature,
    parallel_strategies: dict[str, ParallelStyle],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_api.py
# Line: 120

def forward(  # type: ignore[override]
    ctx,  # pyre-ignore[2]: Parameter must be annotated.
    input: torch.Tensor,
    device_mesh: DeviceMesh,
    placements: tuple[Placement, ...],
    run_check: bool,
    shape: Optional[torch.Size] = None,
    stride: Optional[tuple[int, ...]] = None,

# ==================================================
# Line: 1142

def full(  # type: ignore[no-untyped-def]
    size,
    fill_value,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    requires_grad: bool = False,
    device_mesh: Optional[DeviceMesh] = None,
    placements: Optional[Sequence[Placement]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_adadelta.py
# Line: 26

def __init__(
    self,
    params: list[Tensor],
    lr: float = 1.0,
    rho: float = 0.9,
    eps: float = 1e-6,
    weight_decay: float = 0.0,
    foreach: bool = False,
    maximize: bool = False,
    _allow_empty_param_list: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_rmsprop.py
# Line: 26

def __init__(
    self,
    params: list[Tensor],
    lr: float = 1e-2,
    alpha: float = 0.99,
    eps: float = 1e-8,
    weight_decay: float = 0.0,
    momentum: float = 0.0,
    centered: bool = False,
    foreach: bool = False,
    maximize: bool = False,
    _allow_empty_param_list: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_adamw.py
# Line: 26

def __init__(
    self,
    params: list[Tensor],
    lr: float = 1e-3,
    betas: tuple[float, float] = (0.9, 0.999),
    eps: float = 1e-8,
    weight_decay: float = 1e-2,
    amsgrad: bool = False,
    maximize: bool = False,
    foreach: bool = False,
    fused: bool = False,
    _allow_empty_param_list: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_rprop.py
# Line: 26

def __init__(
    self,
    params: list[Tensor],
    lr: float = 1e-2,
    etas: tuple[float, float] = (0.5, 1.2),
    step_sizes: tuple[float, float] = (1e-6, 50),
    foreach: bool = False,
    maximize: bool = False,
    _allow_empty_param_list: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_adam.py
# Line: 26

def __init__(
    self,
    params: list[Tensor],
    lr: float = 1e-3,
    betas: tuple[float, float] = (0.9, 0.999),
    eps: float = 1e-8,
    weight_decay: float = 0.0,
    amsgrad: bool = False,
    maximize: bool = False,
    foreach: bool = False,
    fused: bool = False,
    _allow_empty_param_list: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_sgd.py
# Line: 26

def __init__(
    self,
    params: list[Tensor],
    lr: float = 1e-2,
    momentum: float = 0.0,
    dampening: float = 0.0,
    weight_decay: float = 0.0,
    nesterov: bool = False,
    maximize: bool = False,
    foreach: bool = False,
    fused: bool = False,
    _allow_empty_param_list: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_adagrad.py
# Line: 26

def __init__(
    self,
    params: list[Tensor],
    lr: float = 1e-2,
    lr_decay: float = 0.0,
    weight_decay: float = 0.0,
    initial_accumulator_value: float = 0.0,
    warmup_lr_multiplier: float = 1.0,
    warmup_num_iters: float = 0.0,
    eps: float = 1e-10,
    coalesce_grad: bool = True,
    foreach: bool = False,
    fused: bool = False,
    maximize: bool = False,
    _allow_empty_param_list: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/functional_adamax.py
# Line: 26

def __init__(
    self,
    params: list[Tensor],
    lr: float = 1e-3,
    betas: tuple[float, float] = (0.9, 0.999),
    eps: float = 1e-8,
    weight_decay: float = 0.0,
    foreach: bool = False,
    maximize: bool = False,
    _allow_empty_param_list: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/pipelining/stage.py
# Line: 121

def __init__(
    self,
    submodule: torch.nn.Module,
    stage_index: int,
    num_stages: int,
    device: torch.device,
    group: Optional[dist.ProcessGroup] = None,
    dw_builder: Optional[Callable[[], Callable[..., None]]] = None,

# ==================================================
# Line: 1261

def __init__(
    self,
    submodule: nn.Module,
    stage_index: int,
    num_stages: int,
    device: torch.device,
    input_args: Optional[Union[torch.Tensor, tuple[torch.Tensor, ...]]] = None,
    output_args: Optional[Union[torch.Tensor, tuple[torch.Tensor, ...]]] = None,
    group: Optional[dist.ProcessGroup] = None,
    dw_builder: Optional[Callable[[], Callable[..., None]]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/pipelining/schedules.py
# Line: 216

def __init__(
    self,
    n_microbatches: int,
    loss_fn: Optional[Callable[..., torch.Tensor]] = None,
    args_chunk_spec: Optional[tuple[TensorChunkSpec, ...]] = None,
    kwargs_chunk_spec: Optional[dict[str, TensorChunkSpec]] = None,
    output_merge_spec: Optional[Union[dict[str, Any], tuple[Any]]] = None,
    scale_grads: bool = True,

# ==================================================
# Line: 456

def __init__(
    self,
    stage: _PipelineStageBase,
    n_microbatches: int,
    loss_fn: Optional[Callable] = None,
    args_chunk_spec: Optional[tuple[TensorChunkSpec, ...]] = None,
    kwargs_chunk_spec: Optional[dict[str, TensorChunkSpec]] = None,
    output_merge_spec: Optional[Union[dict[str, Any], tuple[Any]]] = None,
    scale_grads: bool = True,

# ==================================================
# Line: 1113

def __init__(
    self,
    stages: list[_PipelineStageBase],
    n_microbatches: int,
    loss_fn: Optional[Callable] = None,
    args_chunk_spec: Optional[tuple[TensorChunkSpec, ...]] = None,
    kwargs_chunk_spec: Optional[dict[str, TensorChunkSpec]] = None,
    output_merge_spec: Optional[Union[dict[str, Any], tuple[Any]]] = None,
    use_full_backward: Optional[bool] = None,
    scale_grads: bool = True,

# ==================================================
# Line: 1831

def _get_1f1b_rank_ops(
    n_local_stages,
    pp_group_size,
    warmup_ops,
    fwd_bwd_ops,
    cooldown_ops,
    rank,
    forward_stage_index,
    backward_stage_index,
    num_1f1b_microbatches=0,
    enable_zero_bubble=False,

# ==================================================
# Line: 1986

def __init__(
    self,
    stages: list[_PipelineStageBase],
    n_microbatches: int,
    loss_fn: Optional[Callable] = None,
    args_chunk_spec: Optional[tuple[TensorChunkSpec, ...]] = None,
    kwargs_chunk_spec: Optional[dict[str, TensorChunkSpec]] = None,
    output_merge_spec: Optional[Union[dict[str, Any], tuple[Any]]] = None,
    scale_grads: bool = True,

# ==================================================
# Line: 2095

def __init__(
    self,
    stages: list[_PipelineStageBase],
    n_microbatches: int,
    loss_fn: Optional[Callable] = None,
    args_chunk_spec: Optional[tuple[TensorChunkSpec, ...]] = None,
    kwargs_chunk_spec: Optional[dict[str, TensorChunkSpec]] = None,
    output_merge_spec: Optional[Union[dict[str, Any], tuple[Any]]] = None,
    scale_grads: bool = True,

# ==================================================
# Line: 2296

def __init__(
    self,
    stages: list[_PipelineStageBase],
    n_microbatches: int,
    loss_fn: Optional[Callable] = None,
    args_chunk_spec: Optional[tuple[TensorChunkSpec, ...]] = None,
    kwargs_chunk_spec: Optional[dict[str, TensorChunkSpec]] = None,
    output_merge_spec: Optional[Union[dict[str, Any], tuple[Any]]] = None,
    scale_grads: bool = True,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adagrad.py
# Line: 28

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1e-2,
    lr_decay: float = 0,
    weight_decay: float = 0,
    initial_accumulator_value: float = 0,
    eps: float = 1e-10,
    foreach: Optional[bool] = None,
    *,
    maximize: bool = False,
    differentiable: bool = False,
    fused: Optional[bool] = None,

# ==================================================
# Line: 243

def adagrad(
    params: list[Tensor],
    grads: list[Tensor],
    state_sums: list[Tensor],
    state_steps: list[Tensor],
    fused: Optional[bool] = None,
    grad_scale: Optional[Tensor] = None,
    found_inf: Optional[Tensor] = None,
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting these as kwargs for now as functional API is compiled by torch/distributed/optim
    has_sparse_grad: bool = False,
    foreach: Optional[bool] = None,
    differentiable: bool = False,
    has_complex: bool = False,
    *,
    lr: float,
    weight_decay: float,
    lr_decay: float,
    eps: float,
    maximize: bool,

# ==================================================
# Line: 322

def _single_tensor_adagrad(
    params: list[Tensor],
    grads: list[Tensor],
    state_sums: list[Tensor],
    state_steps: list[Tensor],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    lr: float,
    weight_decay: float,
    lr_decay: float,
    eps: float,
    has_sparse_grad: bool,
    maximize: bool,
    differentiable: bool,
    has_complex: bool,

# ==================================================
# Line: 387

def _multi_tensor_adagrad(
    params: list[Tensor],
    grads: list[Tensor],
    state_sums: list[Tensor],
    state_steps: list[Tensor],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    lr: float,
    weight_decay: float,
    lr_decay: float,
    eps: float,
    has_sparse_grad: bool,
    maximize: bool,
    differentiable: bool,
    has_complex: bool,

# ==================================================
# Line: 496

def _fused_adagrad(
    params: list[Tensor],
    grads: list[Tensor],
    state_sums: list[Tensor],
    state_steps: list[Tensor],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    lr: float,
    weight_decay: float,
    lr_decay: float,
    eps: float,
    has_sparse_grad: bool,
    maximize: bool,
    differentiable: bool,
    has_complex: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/rprop.py
# Line: 30

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1e-2,
    etas: tuple[float, float] = (0.5, 1.2),
    step_sizes: tuple[float, float] = (1e-6, 50),
    *,
    capturable: bool = False,
    foreach: Optional[bool] = None,
    maximize: bool = False,
    differentiable: bool = False,

# ==================================================
# Line: 79

def _init_group(self, group, params, grads, prevs, step_sizes, state_steps):
    has_complex = False
    for p in group["params"]:
        if p.grad is None:
            continue
        has_complex |= torch.is_complex(p)
        params.append(p)
        grad = p.grad
        if grad.is_sparse:
            raise RuntimeError("Rprop does not support sparse gradients")

        grads.append(grad)
        state = self.state[p]

        # State initialization
        if len(state) == 0:
            state["step"] = (
                torch.zeros((), dtype=_get_scalar_dtype(), device=p.device)
                if group["capturable"]
                else torch.zeros((), dtype=_get_scalar_dtype())
            )

            state["prev"] = torch.zeros_like(p, memory_format=torch.preserve_format)
            if p.dtype.is_complex:
                # Complex Number should be as if they are two independent real numbers.
                # Hence the step_size shouldn't be zero for imaginary part.
                state["step_size"] = torch.full_like(
                    grad, complex(group["lr"], group["lr"])
                )
            else:
                state["step_size"] = torch.full_like(grad, _to_scalar(group["lr"]))

        prevs.append(state["prev"])
        step_sizes.append(state["step_size"])
        state_steps.append(state["step"])

    return has_complex


# ==================================================
# Line: 222

def _single_tensor_rprop(
    params: list[Tensor],
    grads: list[Tensor],
    prevs: list[Tensor],
    step_sizes: list[Tensor],
    state_steps: list[Tensor],
    *,
    step_size_min: float,
    step_size_max: float,
    etaminus: float,
    etaplus: float,
    maximize: bool,
    capturable: bool,
    differentiable: bool,
    has_complex: bool,

# ==================================================
# Line: 290

def _multi_tensor_rprop(
    params: list[Tensor],
    grads: list[Tensor],
    prevs: list[Tensor],
    step_sizes: list[Tensor],
    state_steps: list[Tensor],
    *,
    step_size_min: float,
    step_size_max: float,
    etaminus: float,
    etaplus: float,
    maximize: bool,
    capturable: bool,
    differentiable: bool,
    has_complex: bool,

# ==================================================
# Line: 405

def rprop(
    params: list[Tensor],
    grads: list[Tensor],
    prevs: list[Tensor],
    step_sizes: list[Tensor],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    foreach: Optional[bool] = None,
    capturable: bool = False,
    maximize: bool = False,
    differentiable: bool = False,
    has_complex: bool = False,
    *,
    step_size_min: float,
    step_size_max: float,
    etaminus: float,
    etaplus: float,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adadelta.py
# Line: 29

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1.0,
    rho: float = 0.9,
    eps: float = 1e-6,
    weight_decay: float = 0,
    foreach: Optional[bool] = None,
    *,
    capturable: bool = False,
    maximize: bool = False,
    differentiable: bool = False,

# ==================================================
# Line: 84

def _init_group(
    self,
    group: dict[str, Any],
    params_with_grad: list[Tensor],
    grads: list[Tensor],
    square_avgs: list[Tensor],
    acc_deltas: list[Tensor],
    state_steps: list[Tensor],

# ==================================================
# Line: 245

def _single_tensor_adadelta(
    params: list[Tensor],
    grads: list[Tensor],
    square_avgs: list[Tensor],
    acc_deltas: list[Tensor],
    state_steps: list[Tensor],
    *,
    lr: float,
    rho: float,
    eps: float,
    weight_decay: float,
    maximize: bool,
    differentiable: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 302

def _multi_tensor_adadelta(
    params: list[Tensor],
    grads: list[Tensor],
    square_avgs: list[Tensor],
    acc_deltas: list[Tensor],
    state_steps: list[Tensor],
    *,
    lr: float,
    rho: float,
    eps: float,
    weight_decay: float,
    maximize: bool,
    differentiable: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 405

def adadelta(
    params: list[Tensor],
    grads: list[Tensor],
    square_avgs: list[Tensor],
    acc_deltas: list[Tensor],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    capturable: bool = False,
    foreach: Optional[bool] = None,
    differentiable: bool = False,
    has_complex: bool = False,
    *,
    lr: float,
    rho: float,
    eps: float,
    weight_decay: float,
    maximize: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/_functional.py
# Line: 23

def sparse_adam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    state_steps: list[int],
    *,
    eps: float,
    beta1: float,
    beta2: float,
    lr: float,
    maximize: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/_adafactor.py
# Line: 24

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1e-2,
    beta2_decay: float = -0.8,
    eps: tuple[Optional[float], float] = (None, 1e-3),
    d: float = 1.0,
    weight_decay: float = 0.0,
    *,
    foreach: Optional[bool] = None,
    maximize: bool = False,

# ==================================================
# Line: 71

def _init_group(
    self,
    group,
    params_with_grad,
    grads,
    row_vars,
    col_vars,
    variances,
    state_steps,

# ==================================================
# Line: 327

def _single_tensor_adafactor(
    params: list[Tensor],
    grads: list[Tensor],
    # If grad is 1-dimensional (aka a vector), there is no factorization necessary
    # so row_var and col_var will be None while variance will be filled.
    # Contrarily, for a grad with multiple dimensions, we will factor along the last
    # 2 dimensions, and so row_var and col_var will be filled and variance will be None.
    row_vars: list[Optional[Tensor]],
    col_vars: list[Optional[Tensor]],
    variances: list[Optional[Tensor]],
    state_steps: list[Tensor],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    d: float,
    lr: Union[Tensor, float],
    beta2_decay: float,
    weight_decay: float,
    eps1: Optional[float],
    eps2: float,
    maximize: bool,
    has_complex: bool,

# ==================================================
# Line: 449

def _multi_tensor_adafactor(
    params: list[Tensor],
    grads: list[Tensor],
    # If grad is 1-dimensional (aka a vector), there is no factorization necessary
    # so row_var and col_var will be None while variance will be filled.
    # Contrarily, for a grad with multiple dimensions, we will factor along the last
    # 2 dimensions, and so row_var and col_var will be filled and variance will be None.
    row_vars: list[Optional[Tensor]],
    col_vars: list[Optional[Tensor]],
    variances: list[Optional[Tensor]],
    state_steps: list[Tensor],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    d: float,
    lr: Union[Tensor, float],
    beta2_decay: float,
    weight_decay: float,
    eps1: Optional[float],
    eps2: float,
    maximize: bool,
    has_complex: bool,

# ==================================================
# Line: 599

def adafactor(
    params: list[Tensor],
    grads: list[Tensor],
    row_vars: list[Optional[Tensor]],
    col_vars: list[Optional[Tensor]],
    variances: list[Optional[Tensor]],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    foreach: Optional[bool] = None,
    grad_scale: Optional[Tensor] = None,
    found_inf: Optional[Tensor] = None,
    has_complex: bool = False,
    *,
    d: float,
    lr: Union[float, Tensor],
    beta2_decay: float,
    weight_decay: float,
    eps1: float,
    eps2: float,
    maximize: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adamw.py
# Line: 22

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1e-3,
    betas: tuple[Union[float, Tensor], Union[float, Tensor]] = (0.9, 0.999),
    eps: float = 1e-8,
    weight_decay: float = 1e-2,
    amsgrad: bool = False,
    *,
    maximize: bool = False,
    foreach: Optional[bool] = None,
    capturable: bool = False,
    differentiable: bool = False,
    fused: Optional[bool] = None,

# ==================================================
# Line: 130

def adamw(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    max_exp_avg_sqs: list[Tensor],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    foreach: Optional[bool] = None,
    capturable: bool = False,
    differentiable: bool = False,
    fused: Optional[bool] = None,
    grad_scale: Optional[Tensor] = None,
    found_inf: Optional[Tensor] = None,
    has_complex: bool = False,
    *,
    amsgrad: bool,
    beta1: float,
    beta2: float,
    lr: Union[float, Tensor],
    weight_decay: float,
    eps: float,
    maximize: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/nadam.py
# Line: 32

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 2e-3,
    betas: tuple[float, float] = (0.9, 0.999),
    eps: float = 1e-8,
    weight_decay: float = 0,
    momentum_decay: float = 4e-3,
    decoupled_weight_decay: bool = False,
    *,
    foreach: Optional[bool] = None,
    maximize: bool = False,
    capturable: bool = False,
    differentiable: bool = False,

# ==================================================
# Line: 105

def _init_group(
    self,
    group,
    params_with_grad,
    grads,
    exp_avgs,
    exp_avg_sqs,
    mu_products,
    state_steps,

# ==================================================
# Line: 280

def _single_tensor_nadam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    mu_products: list[Tensor],
    state_steps: list[Tensor],
    *,
    beta1: float,
    beta2: float,
    lr: float,
    weight_decay: float,
    momentum_decay: float,
    eps: float,
    decoupled_weight_decay: bool,
    maximize: bool,
    capturable: bool,
    differentiable: bool,
    has_complex: bool,

# ==================================================
# Line: 377

def _multi_tensor_nadam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    mu_products: list[Tensor],
    state_steps: list[Tensor],
    *,
    beta1: float,
    beta2: float,
    lr: float,
    weight_decay: float,
    momentum_decay: float,
    eps: float,
    decoupled_weight_decay: bool,
    maximize: bool,
    capturable: bool,
    differentiable: bool,
    has_complex: bool,

# ==================================================
# Line: 587

def nadam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    mu_products: list[Tensor],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    decoupled_weight_decay: bool = False,
    foreach: Optional[bool] = None,
    capturable: bool = False,
    differentiable: bool = False,
    has_complex: bool = False,
    maximize: bool = False,
    *,
    beta1: float,
    beta2: float,
    lr: float,
    weight_decay: float,
    momentum_decay: float,
    eps: float,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adamax.py
# Line: 30

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 2e-3,
    betas: tuple[float, float] = (0.9, 0.999),
    eps: float = 1e-8,
    weight_decay: float = 0,
    foreach: Optional[bool] = None,
    *,
    maximize: bool = False,
    differentiable: bool = False,
    capturable: bool = False,

# ==================================================
# Line: 87

def _init_group(
    self, group, params_with_grad, grads, exp_avgs, exp_infs, state_steps

# ==================================================
# Line: 226

def _single_tensor_adamax(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_infs: list[Tensor],
    state_steps: list[Tensor],
    *,
    eps: float,
    beta1: float,
    beta2: float,
    lr: float,
    weight_decay: float,
    maximize: bool,
    differentiable: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 303

def _multi_tensor_adamax(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_infs: list[Tensor],
    state_steps: list[Tensor],
    *,
    eps: float,
    beta1: float,
    beta2: float,
    lr: float,
    weight_decay: float,
    maximize: bool,
    differentiable: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 418

def adamax(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_infs: list[Tensor],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    foreach: Optional[bool] = None,
    maximize: bool = False,
    differentiable: bool = False,
    capturable: bool = False,
    has_complex: bool = False,
    *,
    eps: float,
    beta1: float,
    beta2: float,
    lr: float,
    weight_decay: float,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/adam.py
# Line: 35

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1e-3,
    betas: tuple[Union[float, Tensor], Union[float, Tensor]] = (0.9, 0.999),
    eps: float = 1e-8,
    weight_decay: float = 0,
    amsgrad: bool = False,
    *,
    foreach: Optional[bool] = None,
    maximize: bool = False,
    capturable: bool = False,
    differentiable: bool = False,
    fused: Optional[bool] = None,
    decoupled_weight_decay: bool = False,

# ==================================================
# Line: 138

def _init_group(
    self,
    group,
    params_with_grad,
    grads,
    exp_avgs,
    exp_avg_sqs,
    max_exp_avg_sqs,
    state_steps,

# ==================================================
# Line: 345

def _single_tensor_adam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    max_exp_avg_sqs: list[Tensor],
    state_steps: list[Tensor],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    amsgrad: bool,
    has_complex: bool,
    beta1: Union[float, Tensor],
    beta2: Union[float, Tensor],
    lr: Union[float, Tensor],
    weight_decay: float,
    eps: float,
    maximize: bool,
    capturable: bool,
    differentiable: bool,
    decoupled_weight_decay: bool,

# ==================================================
# Line: 538

def _multi_tensor_adam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    max_exp_avg_sqs: list[Tensor],
    state_steps: list[Tensor],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    amsgrad: bool,
    has_complex: bool,
    beta1: Union[float, Tensor],
    beta2: Union[float, Tensor],
    lr: Union[float, Tensor],
    weight_decay: float,
    eps: float,
    maximize: bool,
    capturable: bool,
    differentiable: bool,
    decoupled_weight_decay: bool,

# ==================================================
# Line: 776

def _fused_adam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    max_exp_avg_sqs: list[Tensor],
    state_steps: list[Tensor],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    amsgrad: bool,
    has_complex: bool,  # Needed for consistency.
    beta1: float,
    beta2: float,
    lr: Union[float, Tensor],
    weight_decay: float,
    eps: float,
    maximize: bool,
    capturable: bool,  # Needed for consistency.
    differentiable: bool,
    decoupled_weight_decay: bool,

# ==================================================
# Line: 873

def adam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    max_exp_avg_sqs: list[Tensor],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    foreach: Optional[bool] = None,
    capturable: bool = False,
    differentiable: bool = False,
    fused: Optional[bool] = None,
    grad_scale: Optional[Tensor] = None,
    found_inf: Optional[Tensor] = None,
    has_complex: bool = False,
    decoupled_weight_decay: bool = False,
    *,
    amsgrad: bool,
    beta1: float,
    beta2: float,
    lr: Union[float, Tensor],
    weight_decay: float,
    eps: float,
    maximize: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/sgd.py
# Line: 28

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1e-3,
    momentum: float = 0,
    dampening: float = 0,
    weight_decay: Union[float, Tensor] = 0,
    nesterov: bool = False,
    *,
    maximize: bool = False,
    foreach: Optional[bool] = None,
    differentiable: bool = False,
    fused: Optional[bool] = None,

# ==================================================
# Line: 249

def sgd(
    params: list[Tensor],
    d_p_list: list[Tensor],
    momentum_buffer_list: list[Optional[Tensor]],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    has_sparse_grad: bool = False,
    foreach: Optional[bool] = None,
    fused: Optional[bool] = None,
    grad_scale: Optional[Tensor] = None,
    found_inf: Optional[Tensor] = None,
    *,
    weight_decay: float,
    momentum: float,
    lr: float,
    dampening: float,
    nesterov: bool,
    maximize: bool,

# ==================================================
# Line: 319

def _single_tensor_sgd(
    params: list[Tensor],
    grads: list[Tensor],
    momentum_buffer_list: list[Optional[Tensor]],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    weight_decay: float,
    momentum: float,
    lr: float,
    dampening: float,
    nesterov: bool,
    maximize: bool,
    has_sparse_grad: bool,

# ==================================================
# Line: 377

def _multi_tensor_sgd(
    params: list[Tensor],
    grads: list[Tensor],
    momentum_buffer_list: list[Optional[Tensor]],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    weight_decay: float,
    momentum: float,
    lr: float,
    dampening: float,
    nesterov: bool,
    maximize: bool,
    has_sparse_grad: bool,

# ==================================================
# Line: 471

def _fused_sgd(
    params: list[Tensor],
    grads: list[Tensor],
    momentum_buffer_list: list[Optional[Tensor]],
    grad_scale: Optional[Tensor],
    found_inf: Optional[Tensor],
    *,
    weight_decay: float,
    momentum: float,
    lr: float,
    dampening: float,
    nesterov: bool,
    maximize: bool,
    has_sparse_grad: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/asgd.py
# Line: 30

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1e-2,
    lambd: float = 1e-4,
    alpha: float = 0.75,
    t0: float = 1e6,
    weight_decay: float = 0,
    foreach: Optional[bool] = None,
    maximize: bool = False,
    differentiable: bool = False,
    capturable: bool = False,

# ==================================================
# Line: 87

def _init_group(self, group, params_with_grad, grads, mus, axs, etas, state_steps):
    has_complex = False
    for p in group["params"]:
        if p.grad is not None:
            has_complex |= torch.is_complex(p)
            params_with_grad.append(p)
            if p.grad.is_sparse:
                raise RuntimeError("ASGD does not support sparse gradients")
            grads.append(p.grad)

            state = self.state[p]
            # State initialization
            if len(state) == 0:
                state["step"] = torch.zeros(
                    (), device=p.device, dtype=_get_scalar_dtype()
                )
                state["eta"] = (
                    torch.as_tensor(
                        _to_scalar(group["lr"]),
                        device=p.device,
                        dtype=_get_scalar_dtype(),
                    )
                    .clone()
                    .detach()
                )
                state["mu"] = torch.ones(
                    (), device=p.device, dtype=_get_scalar_dtype()
                )
                state["ax"] = torch.zeros_like(
                    p, memory_format=torch.preserve_format
                )

            mus.append(state["mu"])
            axs.append(state["ax"])
            etas.append(state["eta"])
            state_steps.append(state["step"])
    return has_complex


# ==================================================
# Line: 197

def _single_tensor_asgd(
    params: list[Tensor],
    grads: list[Tensor],
    axs: list[Tensor],
    mus: list[Tensor],
    etas: list[Tensor],
    state_steps: list[Tensor],
    *,
    lambd: float,
    lr: float,
    t0: float,
    alpha: float,
    weight_decay: float,
    maximize: bool,
    differentiable: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 276

def _multi_tensor_asgd(
    params: list[Tensor],
    grads: list[Tensor],
    axs: list[Tensor],
    mus: list[Tensor],
    etas: list[Tensor],
    state_steps: list[Tensor],
    *,
    lambd: float,
    lr: float,
    t0: float,
    alpha: float,
    weight_decay: float,
    maximize: bool,
    differentiable: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 418

def asgd(
    params: list[Tensor],
    grads: list[Tensor],
    axs: list[Tensor],
    mus: list[Tensor],
    etas: list[Tensor],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    foreach: Optional[bool] = None,
    maximize: bool = False,
    differentiable: bool = False,
    capturable: bool = False,
    has_complex: bool = False,
    *,
    lambd: float,
    lr: float,
    t0: float,
    alpha: float,
    weight_decay: float,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/lbfgs.py
# Line: 13

def _cubic_interpolate(x1, f1, g1, x2, f2, g2, bounds=None):
    # ported from https://github.com/torch/optim/blob/master/polyinterp.lua
    # Compute bounds of interpolation area
    if bounds is not None:
        xmin_bound, xmax_bound = bounds
    else:
        xmin_bound, xmax_bound = (x1, x2) if x1 <= x2 else (x2, x1)

    # Code for most common case: cubic interpolation of 2 points
    #   w/ function and derivative values for both
    # Solution in this case (where x2 is the farthest point):
    #   d1 = g1 + g2 - 3*(f1-f2)/(x1-x2);
    #   d2 = sqrt(d1^2 - g1*g2);
    #   min_pos = x2 - (x2 - x1)*((g2 + d2 - d1)/(g2 - g1 + 2*d2));
    #   t_new = min(max(min_pos,xmin_bound),xmax_bound);
    d1 = g1 + g2 - 3 * (f1 - f2) / (x1 - x2)
    d2_square = d1**2 - g1 * g2
    if d2_square >= 0:
        d2 = d2_square.sqrt()
        if x1 <= x2:
            min_pos = x2 - (x2 - x1) * ((g2 + d2 - d1) / (g2 - g1 + 2 * d2))
        else:
            min_pos = x1 - (x1 - x2) * ((g1 + d2 - d1) / (g1 - g2 + 2 * d2))
        return min(max(min_pos, xmin_bound), xmax_bound)
    else:
        return (xmin_bound + xmax_bound) / 2.0



# ==================================================
# Line: 41

def _strong_wolfe(
    obj_func, x, t, d, f, g, gtd, c1=1e-4, c2=0.9, tolerance_change=1e-9, max_ls=25

# ==================================================
# Line: 217

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1,
    max_iter: int = 20,
    max_eval: Optional[int] = None,
    tolerance_grad: float = 1e-7,
    tolerance_change: float = 1e-9,
    history_size: int = 100,
    line_search_fn: Optional[str] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/radam.py
# Line: 31

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1e-3,
    betas: tuple[float, float] = (0.9, 0.999),
    eps: float = 1e-8,
    weight_decay: float = 0,
    decoupled_weight_decay: bool = False,
    *,
    foreach: Optional[bool] = None,
    maximize: bool = False,
    capturable: bool = False,
    differentiable: bool = False,

# ==================================================
# Line: 91

def _init_group(
    self, group, params_with_grad, grads, exp_avgs, exp_avg_sqs, state_steps

# ==================================================
# Line: 255

def _single_tensor_radam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    state_steps: list[Tensor],
    *,
    beta1: float,
    beta2: float,
    lr: float,
    weight_decay: float,
    eps: float,
    decoupled_weight_decay: bool,
    differentiable: bool,
    maximize: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 357

def _multi_tensor_radam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    state_steps: list[Tensor],
    *,
    beta1: float,
    beta2: float,
    lr: float,
    weight_decay: float,
    eps: float,
    decoupled_weight_decay: bool,
    differentiable: bool,
    maximize: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 555

def radam(
    params: list[Tensor],
    grads: list[Tensor],
    exp_avgs: list[Tensor],
    exp_avg_sqs: list[Tensor],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    decoupled_weight_decay: bool = False,
    foreach: Optional[bool] = None,
    differentiable: bool = False,
    capturable: bool = False,
    has_complex: bool = False,
    maximize: bool = False,
    *,
    beta1: float,
    beta2: float,
    lr: float,
    weight_decay: float,
    eps: float,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/rmsprop.py
# Line: 30

def __init__(
    self,
    params: ParamsT,
    lr: Union[float, Tensor] = 1e-2,
    alpha: float = 0.99,
    eps: float = 1e-8,
    weight_decay: float = 0,
    momentum: float = 0,
    centered: bool = False,
    capturable: bool = False,
    foreach: Optional[bool] = None,
    maximize: bool = False,
    differentiable: bool = False,

# ==================================================
# Line: 92

def _init_group(
    self,
    group,
    params_with_grad,
    grads,
    square_avgs,
    momentum_buffer_list,
    grad_avgs,
    state_steps,

# ==================================================
# Line: 264

def _single_tensor_rmsprop(
    params: list[Tensor],
    grads: list[Tensor],
    square_avgs: list[Tensor],
    grad_avgs: list[Tensor],
    momentum_buffer_list: list[Tensor],
    state_steps: list[Tensor],
    *,
    lr: float,
    alpha: float,
    eps: float,
    weight_decay: float,
    momentum: float,
    centered: bool,
    maximize: bool,
    differentiable: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 338

def _multi_tensor_rmsprop(
    params: list[Tensor],
    grads: list[Tensor],
    square_avgs: list[Tensor],
    grad_avgs: list[Tensor],
    momentum_buffer_list: list[Tensor],
    state_steps: list[Tensor],
    *,
    lr: float,
    alpha: float,
    eps: float,
    weight_decay: float,
    momentum: float,
    centered: bool,
    maximize: bool,
    differentiable: bool,
    capturable: bool,
    has_complex: bool,

# ==================================================
# Line: 469

def rmsprop(
    params: list[Tensor],
    grads: list[Tensor],
    square_avgs: list[Tensor],
    grad_avgs: list[Tensor],
    momentum_buffer_list: list[Tensor],
    state_steps: list[Tensor],
    # kwonly args with defaults are not supported by functions compiled with torchscript issue #70627
    # setting this as kwarg for now as functional API is compiled by torch/distributed/optim
    foreach: Optional[bool] = None,
    maximize: bool = False,
    differentiable: bool = False,
    capturable: bool = False,
    has_complex: bool = False,
    *,
    lr: float,
    alpha: float,
    eps: float,
    weight_decay: float,
    momentum: float,
    centered: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/optim/lr_scheduler.py
# Line: 1284

def __init__(
    self,
    optimizer: Optimizer,
    mode: Literal["min", "max"] = "min",
    factor: float = 0.1,
    patience: int = 10,
    threshold: float = 1e-4,
    threshold_mode: Literal["rel", "abs"] = "rel",
    cooldown: int = 0,
    min_lr: Union[list[float], float] = 0,
    eps: float = 1e-8,

# ==================================================
# Line: 1518

def __init__(
    self,
    optimizer: Optimizer,
    base_lr: Union[float, list[float]],
    max_lr: Union[float, list[float]],
    step_size_up: int = 2000,
    step_size_down: Optional[int] = None,
    mode: Literal["triangular", "triangular2", "exp_range"] = "triangular",
    gamma: float = 1.0,
    scale_fn: Optional[Callable[[float], float]] = None,
    scale_mode: Literal["cycle", "iterations"] = "cycle",
    cycle_momentum: bool = True,
    base_momentum: float = 0.8,
    max_momentum: float = 0.9,
    last_epoch: int = -1,

# ==================================================
# Line: 1952

def __init__(
    self,
    optimizer: Optimizer,
    max_lr: Union[float, list[float]],
    total_steps: Optional[int] = None,
    epochs: Optional[int] = None,
    steps_per_epoch: Optional[int] = None,
    pct_start: float = 0.3,
    anneal_strategy: Literal["cos", "linear"] = "cos",
    cycle_momentum: bool = True,
    base_momentum: Union[float, list[float]] = 0.85,
    max_momentum: Union[float, list[float]] = 0.95,
    div_factor: float = 25.0,
    final_div_factor: float = 1e4,
    three_phase: bool = False,
    last_epoch: int = -1,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_strobelight/cli_function_profiler.py
# Line: 72

def __init__(
    self,
    *,
    stop_at_error: bool = False,
    max_profile_duration_sec: int = 60 * 10,
    sample_each: float = 1e7,  # sample each sample_each cycles.
    run_user_name: str = "pytorch-strobelight-ondemand",
    timeout_wait_for_running_sec: int = 60,
    timeout_wait_for_finished_sec: int = 60,
    recorded_env_variables: Optional[list[str]] = None,
    sample_tags: Optional[list[str]] = None,
    stack_max_len: int = 127,
    async_stack_max_len: int = 127,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/pooling.py
# Line: 57

def __init__(
    self,
    kernel_size: _size_any_t,
    stride: Optional[_size_any_t] = None,
    padding: _size_any_t = 0,
    dilation: _size_any_t = 1,
    return_indices: bool = False,
    ceil_mode: bool = False,

# ==================================================
# Line: 755

def __init__(
    self,
    kernel_size: _size_2_t,
    stride: Optional[_size_2_t] = None,
    padding: _size_2_t = 0,
    ceil_mode: bool = False,
    count_include_pad: bool = True,
    divisor_override: Optional[int] = None,

# ==================================================
# Line: 871

def __init__(
    self,
    kernel_size: _size_3_t,
    stride: Optional[_size_3_t] = None,
    padding: _size_3_t = 0,
    ceil_mode: bool = False,
    count_include_pad: bool = True,
    divisor_override: Optional[int] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/sparse.py
# Line: 133

def __init__(
    self,
    num_embeddings: int,
    embedding_dim: int,
    padding_idx: Optional[int] = None,
    max_norm: Optional[float] = None,
    norm_type: float = 2.0,
    scale_grad_by_freq: bool = False,
    sparse: bool = False,
    _weight: Optional[Tensor] = None,
    _freeze: bool = False,
    device=None,
    dtype=None,

# ==================================================
# Line: 215

def from_pretrained(
    cls,
    embeddings,
    freeze=True,
    padding_idx=None,
    max_norm=None,
    norm_type=2.0,
    scale_grad_by_freq=False,
    sparse=False,

# ==================================================
# Line: 370

def __init__(
    self,
    num_embeddings: int,
    embedding_dim: int,
    max_norm: Optional[float] = None,
    norm_type: float = 2.0,
    scale_grad_by_freq: bool = False,
    mode: str = "mean",
    sparse: bool = False,
    _weight: Optional[Tensor] = None,
    include_last_offset: bool = False,
    padding_idx: Optional[int] = None,
    device=None,
    dtype=None,

# ==================================================
# Line: 491

def from_pretrained(
    cls,
    embeddings: Tensor,
    freeze: bool = True,
    max_norm: Optional[float] = None,
    norm_type: float = 2.0,
    scale_grad_by_freq: bool = False,
    mode: str = "mean",
    sparse: bool = False,
    include_last_offset: bool = False,
    padding_idx: Optional[int] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/rnn.py
# Line: 84

def __init__(
    self,
    mode: str,
    input_size: int,
    hidden_size: int,
    num_layers: int = 1,
    bias: bool = True,
    batch_first: bool = False,
    dropout: float = 0.0,
    bidirectional: bool = False,
    proj_size: int = 0,
    device=None,
    dtype=None,

# ==================================================
# Line: 602

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    num_layers: int = 1,
    nonlinearity: str = "tanh",
    bias: bool = True,
    batch_first: bool = False,
    dropout: float = 0.0,
    bidirectional: bool = False,
    device=None,
    dtype=None,

# ==================================================
# Line: 960

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    num_layers: int = 1,
    bias: bool = True,
    batch_first: bool = False,
    dropout: float = 0.0,
    bidirectional: bool = False,
    proj_size: int = 0,
    device=None,
    dtype=None,

# ==================================================
# Line: 1296

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    num_layers: int = 1,
    bias: bool = True,
    batch_first: bool = False,
    dropout: float = 0.0,
    bidirectional: bool = False,
    device=None,
    dtype=None,

# ==================================================
# Line: 1447

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    bias: bool,
    num_chunks: int,
    device=None,
    dtype=None,

# ==================================================
# Line: 1552

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    bias: bool = True,
    nonlinearity: str = "tanh",
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/activation.py
# Line: 1050

def __init__(
    self,
    embed_dim,
    num_heads,
    dropout=0.0,
    bias=True,
    add_bias_kv=False,
    add_zero_attn=False,
    kdim=None,
    vdim=None,
    batch_first=False,
    device=None,
    dtype=None,

# ==================================================
# Line: 1144

def forward(
    self,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    key_padding_mask: Optional[Tensor] = None,
    need_weights: bool = True,
    attn_mask: Optional[Tensor] = None,
    average_attn_weights: bool = True,
    is_causal: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/module.py
# Line: 2320

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/_functions.py
# Line: 9

def forward(
    self,
    input,
    weight,
    bias,
    running_mean,
    running_var,
    eps,
    momentum,
    process_group,
    world_size,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/batchnorm.py
# Line: 38

def __init__(
    self,
    num_features: int,
    eps: float = 1e-5,
    momentum: Optional[float] = 0.1,
    affine: bool = True,
    track_running_stats: bool = True,
    device=None,
    dtype=None,

# ==================================================
# Line: 108

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 144

def __init__(
    self,
    num_features: int,
    eps: float = 1e-5,
    momentum: Optional[float] = 0.1,
    affine: bool = True,
    track_running_stats: bool = True,
    device=None,
    dtype=None,

# ==================================================
# Line: 212

def __init__(
    self,
    eps=1e-5,
    momentum=0.1,
    affine=True,
    track_running_stats=True,
    device=None,
    dtype=None,

# ==================================================
# Line: 703

def __init__(
    self,
    num_features: int,
    eps: float = 1e-5,
    momentum: Optional[float] = 0.1,
    affine: bool = True,
    track_running_stats: bool = True,
    process_group: Optional[Any] = None,
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/normalization.py
# Line: 177

def __init__(
    self,
    normalized_shape: _shape_t,
    eps: float = 1e-5,
    elementwise_affine: bool = True,
    bias: bool = True,
    device=None,
    dtype=None,

# ==================================================
# Line: 280

def __init__(
    self,
    num_groups: int,
    num_channels: int,
    eps: float = 1e-5,
    affine: bool = True,
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/adaptive.py
# Line: 116

def __init__(
    self,
    in_features: int,
    n_classes: int,
    cutoffs: Sequence[int],
    div_value: float = 4.0,
    head_bias: bool = False,
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/loss.py
# Line: 339

def __init__(
    self,
    log_input: bool = True,
    full: bool = False,
    size_average=None,
    eps: float = 1e-8,
    reduce=None,
    reduction: str = "mean",

# ==================================================
# Line: 1283

def __init__(
    self,
    weight: Optional[Tensor] = None,
    size_average=None,
    ignore_index: int = -100,
    reduce=None,
    reduction: str = "mean",
    label_smoothing: float = 0.0,

# ==================================================
# Line: 1561

def __init__(
    self,
    p: int = 1,
    margin: float = 1.0,
    weight: Optional[Tensor] = None,
    size_average=None,
    reduce=None,
    reduction: str = "mean",

# ==================================================
# Line: 1666

def __init__(
    self,
    margin: float = 1.0,
    p: float = 2.0,
    eps: float = 1e-6,
    swap: bool = False,
    size_average=None,
    reduce=None,
    reduction: str = "mean",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/lazy.py
# Line: 24

def _lazy_load_hook(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 205

def _lazy_load_hook(
    self: _LazyProtocol,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/instancenorm.py
# Line: 22

def __init__(
    self,
    num_features: int,
    eps: float = 1e-5,
    momentum: float = 0.1,
    affine: bool = False,
    track_running_stats: bool = False,
    device=None,
    dtype=None,

# ==================================================
# Line: 58

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/transformer.py
# Line: 99

def __init__(
    self,
    d_model: int = 512,
    nhead: int = 8,
    num_encoder_layers: int = 6,
    num_decoder_layers: int = 6,
    dim_feedforward: int = 2048,
    dropout: float = 0.1,
    activation: Union[str, Callable[[Tensor], Tensor]] = F.relu,
    custom_encoder: Optional[Any] = None,
    custom_decoder: Optional[Any] = None,
    layer_norm_eps: float = 1e-5,
    batch_first: bool = False,
    norm_first: bool = False,
    bias: bool = True,
    device=None,
    dtype=None,

# ==================================================
# Line: 172

def forward(
    self,
    src: Tensor,
    tgt: Tensor,
    src_mask: Optional[Tensor] = None,
    tgt_mask: Optional[Tensor] = None,
    memory_mask: Optional[Tensor] = None,
    src_key_padding_mask: Optional[Tensor] = None,
    tgt_key_padding_mask: Optional[Tensor] = None,
    memory_key_padding_mask: Optional[Tensor] = None,
    src_is_causal: Optional[bool] = None,
    tgt_is_causal: Optional[bool] = None,
    memory_is_causal: bool = False,

# ==================================================
# Line: 581

def forward(
    self,
    tgt: Tensor,
    memory: Tensor,
    tgt_mask: Optional[Tensor] = None,
    memory_mask: Optional[Tensor] = None,
    tgt_key_padding_mask: Optional[Tensor] = None,
    memory_key_padding_mask: Optional[Tensor] = None,
    tgt_is_causal: Optional[bool] = None,
    memory_is_causal: bool = False,

# ==================================================
# Line: 723

def __init__(
    self,
    d_model: int,
    nhead: int,
    dim_feedforward: int = 2048,
    dropout: float = 0.1,
    activation: Union[str, Callable[[Tensor], Tensor]] = F.relu,
    layer_norm_eps: float = 1e-5,
    batch_first: bool = False,
    norm_first: bool = False,
    bias: bool = True,
    device=None,
    dtype=None,

# ==================================================
# Line: 1005

def __init__(
    self,
    d_model: int,
    nhead: int,
    dim_feedforward: int = 2048,
    dropout: float = 0.1,
    activation: Union[str, Callable[[Tensor], Tensor]] = F.relu,
    layer_norm_eps: float = 1e-5,
    batch_first: bool = False,
    norm_first: bool = False,
    bias: bool = True,
    device=None,
    dtype=None,

# ==================================================
# Line: 1061

def forward(
    self,
    tgt: Tensor,
    memory: Tensor,
    tgt_mask: Optional[Tensor] = None,
    memory_mask: Optional[Tensor] = None,
    tgt_key_padding_mask: Optional[Tensor] = None,
    memory_key_padding_mask: Optional[Tensor] = None,
    tgt_is_causal: bool = False,
    memory_is_causal: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/linear.py
# Line: 194

def __init__(
    self,
    in1_features: int,
    in2_features: int,
    out_features: int,
    bias: bool = True,
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/conv.py
# Line: 86

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: tuple[int, ...],
    stride: tuple[int, ...],
    padding: Union[str, tuple[int, ...]],
    dilation: tuple[int, ...],
    transposed: bool,
    output_padding: tuple[int, ...],
    groups: int,
    bias: bool,
    padding_mode: str,
    device=None,
    dtype=None,

# ==================================================
# Line: 321

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_1_t,
    stride: _size_1_t = 1,
    padding: Union[str, _size_1_t] = 0,
    dilation: _size_1_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",  # TODO: refine this type
    device=None,
    dtype=None,

# ==================================================
# Line: 502

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_2_t,
    stride: _size_2_t = 1,
    padding: Union[str, _size_2_t] = 0,
    dilation: _size_2_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",  # TODO: refine this type
    device=None,
    dtype=None,

# ==================================================
# Line: 673

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_3_t,
    stride: _size_3_t = 1,
    padding: Union[str, _size_3_t] = 0,
    dilation: _size_3_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 729

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride,
    padding,
    dilation,
    transposed,
    output_padding,
    groups,
    bias,
    padding_mode,
    device=None,
    dtype=None,

# ==================================================
# Line: 768

def _output_padding(
    self,
    input: Tensor,
    output_size: Optional[list[int]],
    stride: list[int],
    padding: list[int],
    kernel_size: list[int],
    num_spatial_dims: int,
    dilation: Optional[list[int]] = None,

# ==================================================
# Line: 919

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_1_t,
    stride: _size_1_t = 1,
    padding: _size_1_t = 0,
    output_padding: _size_1_t = 0,
    groups: int = 1,
    bias: bool = True,
    dilation: _size_1_t = 1,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 1109

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_2_t,
    stride: _size_2_t = 1,
    padding: _size_2_t = 0,
    output_padding: _size_2_t = 0,
    groups: int = 1,
    bias: bool = True,
    dilation: _size_2_t = 1,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 1302

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_3_t,
    stride: _size_3_t = 1,
    padding: _size_3_t = 0,
    output_padding: _size_3_t = 0,
    groups: int = 1,
    bias: bool = True,
    dilation: _size_3_t = 1,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 1497

def __init__(
    self,
    out_channels: int,
    kernel_size: _size_1_t,
    stride: _size_1_t = 1,
    padding: _size_1_t = 0,
    dilation: _size_1_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 1566

def __init__(
    self,
    out_channels: int,
    kernel_size: _size_2_t,
    stride: _size_2_t = 1,
    padding: _size_2_t = 0,
    dilation: _size_2_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",  # TODO: refine this type
    device=None,
    dtype=None,

# ==================================================
# Line: 1636

def __init__(
    self,
    out_channels: int,
    kernel_size: _size_3_t,
    stride: _size_3_t = 1,
    padding: _size_3_t = 0,
    dilation: _size_3_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 1703

def __init__(
    self,
    out_channels: int,
    kernel_size: _size_1_t,
    stride: _size_1_t = 1,
    padding: _size_1_t = 0,
    output_padding: _size_1_t = 0,
    groups: int = 1,
    bias: bool = True,
    dilation: _size_1_t = 1,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 1772

def __init__(
    self,
    out_channels: int,
    kernel_size: _size_2_t,
    stride: _size_2_t = 1,
    padding: _size_2_t = 0,
    output_padding: _size_2_t = 0,
    groups: int = 1,
    bias: bool = True,
    dilation: int = 1,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 1841

def __init__(
    self,
    out_channels: int,
    kernel_size: _size_3_t,
    stride: _size_3_t = 1,
    padding: _size_3_t = 0,
    output_padding: _size_3_t = 0,
    groups: int = 1,
    bias: bool = True,
    dilation: _size_3_t = 1,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/prune.py
# Line: 760

def apply(cls, module, name, amount, n, dim, importance_scores=None):
    r"""Add pruning on the fly and reparametrization of a tensor.

    Adds the forward pre-hook that enables pruning on the fly and
    the reparametrization of a tensor in terms of the original tensor
    and the pruning mask.

    Args:
        module (nn.Module): module containing the tensor to prune
        name (str): parameter name within ``module`` on which pruning
            will act.
        amount (int or float): quantity of parameters to prune.
            If ``float``, should be between 0.0 and 1.0 and represent the
            fraction of parameters to prune. If ``int``, it represents the
            absolute number of parameters to prune.
        n (int, float, inf, -inf, 'fro', 'nuc'): See documentation of valid
            entries for argument ``p`` in :func:`torch.norm`.
        dim (int): index of the dim along which we define channels to
            prune.
        importance_scores (torch.Tensor): tensor of importance scores (of same
            shape as module parameter) used to compute mask for pruning.
            The values in this tensor indicate the importance of the corresponding
            elements in the parameter being pruned.
            If unspecified or None, the module parameter will be used in its place.
    """
    return super().apply(
        module,
        name,
        amount=amount,
        n=n,
        dim=dim,
        importance_scores=importance_scores,
    )



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/fusion.py
# Line: 56

def fuse_conv_bn_weights(
    conv_w: torch.Tensor,
    conv_b: torch.Tensor | None,
    bn_rm: torch.Tensor,
    bn_rv: torch.Tensor,
    bn_eps: float,
    bn_w: torch.Tensor | None,
    bn_b: torch.Tensor | None,
    transpose: bool = False,

# ==================================================
# Line: 156

def fuse_linear_bn_weights(
    linear_w: torch.Tensor,
    linear_b: torch.Tensor | None,
    bn_rm: torch.Tensor,
    bn_rv: torch.Tensor,
    bn_eps: float,
    bn_w: torch.Tensor,
    bn_b: torch.Tensor,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/spectral_norm.py
# Line: 202

def __call__(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/_expanded_weights/conv_utils.py
# Line: 36

def conv_normalizer(
    input,
    weight,
    bias=None,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,

# ==================================================
# Line: 203

def conv_unfold_weight_grad_sample(
    input,
    grad_output,
    weight_shape,
    kernel_size,
    stride,
    padding,
    dilation,
    groups,
    func,

# ==================================================
# Line: 256

def conv_group_weight_grad_sample(
    input,
    grad_output,
    weight_shape,
    stride,
    padding,
    dilation,
    batch_size,
    func,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/parametrizations.py
# Line: 380

def _weight_norm_compat_hook(
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/_utils.py
# Line: 34

def _validate_sdpa_input(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attn_mask: Optional[torch.Tensor] = None,
    dropout_p=0.0,
    is_causal=False,
    scale=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/experimental/_paged_attention.py
# Line: 130

def assign(
    self,
    batch_idx: torch.Tensor,
    input_pos: torch.Tensor,
    k_val: torch.Tensor,
    v_val: torch.Tensor,
    k_cache: torch.Tensor,
    v_cache: torch.Tensor,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/flex_attention.py
# Line: 276

def __init__(
    self,
    seq_lengths: tuple[int, int],
    kv_num_blocks: Tensor,
    kv_indices: Tensor,
    full_kv_num_blocks: Optional[Tensor],
    full_kv_indices: Optional[Tensor],
    q_num_blocks: Optional[Tensor],
    q_indices: Optional[Tensor],
    full_q_num_blocks: Optional[Tensor],
    full_q_indices: Optional[Tensor],
    BLOCK_SIZE: tuple[int, int],
    mask_mod: _mask_mod_signature,

# ==================================================
# Line: 316

def from_kv_blocks(
    cls,
    kv_num_blocks: Tensor,
    kv_indices: Tensor,
    full_kv_num_blocks: Optional[Tensor] = None,
    full_kv_indices: Optional[Tensor] = None,
    BLOCK_SIZE: Union[int, tuple[int, int]] = _DEFAULT_SPARSE_BLOCK_SIZE,
    mask_mod: Optional[_mask_mod_signature] = None,
    seq_lengths: Optional[tuple[int, int]] = None,

# ==================================================
# Line: 826

def create_block_mask(
    mask_mod: _mask_mod_signature,
    B: Optional[int],
    H: Optional[int],
    Q_LEN: int,
    KV_LEN: int,
    device: DeviceLikeType = "cuda",
    BLOCK_SIZE: Union[int, tuple[int, int]] = _DEFAULT_SPARSE_BLOCK_SIZE,
    _compile=False,

# ==================================================
# Line: 1216

def flex_attention(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    score_mod: Optional[_score_mod_signature] = None,
    block_mask: Optional[BlockMask] = None,
    scale: Optional[float] = None,
    enable_gqa: bool = False,
    return_lse: bool = False,
    kernel_options: Optional[dict[str, Any]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/attention/bias.py
# Line: 170

def _dispatch(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attn_mask: "CausalBias",
    dropout_p: float = 0.0,
    is_causal: bool = False,
    scale: Optional[float] = None,
    enable_gqa: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/grad.py
# Line: 8

def conv1d_input(
    input_size,
    weight,
    grad_output,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,

# ==================================================
# Line: 58

def conv1d_weight(
    input,
    weight_size,
    grad_output,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,

# ==================================================
# Line: 106

def conv2d_input(
    input_size,
    weight,
    grad_output,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,

# ==================================================
# Line: 156

def conv2d_weight(
    input,
    weight_size,
    grad_output,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,

# ==================================================
# Line: 204

def conv3d_input(
    input_size,
    weight,
    grad_output,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,

# ==================================================
# Line: 254

def conv3d_weight(
    input,
    weight_size,
    grad_output,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/functional.py
# Line: 673

def max_pool1d_with_indices(
    input: Tensor,
    kernel_size: BroadcastingList1[int],
    stride: Optional[BroadcastingList1[int]] = None,
    padding: BroadcastingList1[int] = 0,
    dilation: BroadcastingList1[int] = 1,
    ceil_mode: bool = False,
    return_indices: bool = False,

# ==================================================
# Line: 726

def _max_pool1d(
    input: Tensor,
    kernel_size: BroadcastingList1[int],
    stride: Optional[BroadcastingList1[int]] = None,
    padding: BroadcastingList1[int] = 0,
    dilation: BroadcastingList1[int] = 1,
    ceil_mode: bool = False,
    return_indices: bool = False,

# ==================================================
# Line: 763

def max_pool2d_with_indices(
    input: Tensor,
    kernel_size: BroadcastingList2[int],
    stride: Optional[BroadcastingList2[int]] = None,
    padding: BroadcastingList2[int] = 0,
    dilation: BroadcastingList2[int] = 1,
    ceil_mode: bool = False,
    return_indices: bool = False,

# ==================================================
# Line: 816

def _max_pool2d(
    input: Tensor,
    kernel_size: BroadcastingList2[int],
    stride: Optional[BroadcastingList2[int]] = None,
    padding: BroadcastingList2[int] = 0,
    dilation: BroadcastingList2[int] = 1,
    ceil_mode: bool = False,
    return_indices: bool = False,

# ==================================================
# Line: 853

def max_pool3d_with_indices(
    input: Tensor,
    kernel_size: BroadcastingList3[int],
    stride: Optional[BroadcastingList3[int]] = None,
    padding: BroadcastingList3[int] = 0,
    dilation: BroadcastingList3[int] = 1,
    ceil_mode: bool = False,
    return_indices: bool = False,

# ==================================================
# Line: 906

def _max_pool3d(
    input: Tensor,
    kernel_size: BroadcastingList3[int],
    stride: Optional[BroadcastingList3[int]] = None,
    padding: BroadcastingList3[int] = 0,
    dilation: BroadcastingList3[int] = 1,
    ceil_mode: bool = False,
    return_indices: bool = False,

# ==================================================
# Line: 2446

def embedding(
    input: Tensor,
    weight: Tensor,
    padding_idx: Optional[int] = None,
    max_norm: Optional[float] = None,
    norm_type: float = 2.0,
    scale_grad_by_freq: bool = False,
    sparse: bool = False,

# ==================================================
# Line: 2563

def embedding_bag(
    input: Tensor,
    weight: Tensor,
    offsets: Optional[Tensor] = None,
    max_norm: Optional[float] = None,
    norm_type: float = 2,
    scale_grad_by_freq: bool = False,
    mode: str = "mean",
    sparse: bool = False,
    per_sample_weights: Optional[Tensor] = None,
    include_last_offset: bool = False,
    padding_idx: Optional[int] = None,

# ==================================================
# Line: 2800

def batch_norm(
    input: Tensor,
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    weight: Optional[Tensor] = None,
    bias: Optional[Tensor] = None,
    training: bool = False,
    momentum: float = 0.1,
    eps: float = 1e-5,

# ==================================================
# Line: 2855

def instance_norm(
    input: Tensor,
    running_mean: Optional[Tensor] = None,
    running_var: Optional[Tensor] = None,
    weight: Optional[Tensor] = None,
    bias: Optional[Tensor] = None,
    use_input_stats: bool = True,
    momentum: float = 0.1,
    eps: float = 1e-5,

# ==================================================
# Line: 3024

def ctc_loss(
    log_probs: Tensor,
    targets: Tensor,
    input_lengths: Tensor,
    target_lengths: Tensor,
    blank: int = 0,
    reduction: str = "mean",
    zero_infinity: bool = False,

# ==================================================
# Line: 3104

def nll_loss(
    input: Tensor,
    target: Tensor,
    weight: Optional[Tensor] = None,
    size_average: Optional[bool] = None,
    ignore_index: int = -100,
    reduce: Optional[bool] = None,
    reduction: str = "mean",

# ==================================================
# Line: 3166

def poisson_nll_loss(
    input: Tensor,
    target: Tensor,
    log_input: bool = True,
    full: bool = False,
    size_average: Optional[bool] = None,
    eps: float = 1e-8,
    reduce: Optional[bool] = None,
    reduction: str = "mean",

# ==================================================
# Line: 3393

def cross_entropy(
    input: Tensor,
    target: Tensor,
    weight: Optional[Tensor] = None,
    size_average: Optional[bool] = None,
    ignore_index: int = -100,
    reduce: Optional[bool] = None,
    reduction: str = "mean",
    label_smoothing: float = 0.0,

# ==================================================
# Line: 3547

def binary_cross_entropy_with_logits(
    input: Tensor,
    target: Tensor,
    weight: Optional[Tensor] = None,
    size_average: Optional[bool] = None,
    reduce: Optional[bool] = None,
    reduction: str = "mean",
    pos_weight: Optional[Tensor] = None,

# ==================================================
# Line: 3908

def margin_ranking_loss(
    input1: Tensor,
    input2: Tensor,
    target: Tensor,
    margin: float = 0,
    size_average: Optional[bool] = None,
    reduce: Optional[bool] = None,
    reduction: str = "mean",

# ==================================================
# Line: 4145

def cosine_embedding_loss(
    input1: Tensor,
    input2: Tensor,
    target: Tensor,
    margin: float = 0,
    size_average: Optional[bool] = None,
    reduce: Optional[bool] = None,
    reduction: str = "mean",

# ==================================================
# Line: 4192

def multi_margin_loss(
    input: Tensor,
    target: Tensor,
    p: int = 1,
    margin: float = 1.0,
    weight: Optional[Tensor] = None,
    size_average: Optional[bool] = None,
    reduce: Optional[bool] = None,
    reduction: str = "mean",

# ==================================================
# Line: 4497

def interpolate(  # noqa: F811
    input: Tensor,
    size: Optional[int] = None,
    scale_factor: Optional[list[float]] = None,
    mode: str = "nearest",
    align_corners: Optional[bool] = None,
    recompute_scale_factor: Optional[bool] = None,
    antialias: bool = False,

# ==================================================
# Line: 4510

def interpolate(  # noqa: F811
    input: Tensor,
    size: Optional[list[int]] = None,
    scale_factor: Optional[list[float]] = None,
    mode: str = "nearest",
    align_corners: Optional[bool] = None,
    recompute_scale_factor: Optional[bool] = None,
    antialias: bool = False,

# ==================================================
# Line: 4523

def interpolate(  # noqa: F811
    input: Tensor,
    size: Optional[int] = None,
    scale_factor: Optional[float] = None,
    mode: str = "nearest",
    align_corners: Optional[bool] = None,
    recompute_scale_factor: Optional[bool] = None,
    antialias: bool = False,

# ==================================================
# Line: 4536

def interpolate(  # noqa: F811
    input: Tensor,
    size: Optional[list[int]] = None,
    scale_factor: Optional[float] = None,
    mode: str = "nearest",
    align_corners: Optional[bool] = None,
    recompute_scale_factor: Optional[bool] = None,
    antialias: bool = False,

# ==================================================
# Line: 4548

def interpolate(  # noqa: F811
    input: Tensor,
    size: Optional[int] = None,
    scale_factor: Optional[list[float]] = None,
    mode: str = "nearest",
    align_corners: Optional[bool] = None,
    recompute_scale_factor: Optional[bool] = None,
    antialias: bool = False,

# ==================================================
# Line: 5432

def triplet_margin_loss(
    anchor: Tensor,
    positive: Tensor,
    negative: Tensor,
    margin: float = 1.0,
    p: float = 2,
    eps: float = 1e-6,
    swap: bool = False,
    size_average: Optional[bool] = None,
    reduce: Optional[bool] = None,
    reduction: str = "mean",

# ==================================================
# Line: 5474

def triplet_margin_with_distance_loss(
    anchor: Tensor,
    positive: Tensor,
    negative: Tensor,
    *,
    distance_function: Optional[Callable[[Tensor, Tensor], Tensor]] = None,
    margin: float = 1.0,
    swap: bool = False,
    reduction: str = "mean",

# ==================================================
# Line: 5746

def _in_projection(
    q: Tensor,
    k: Tensor,
    v: Tensor,
    w_q: Tensor,
    w_k: Tensor,
    w_v: Tensor,
    b_q: Optional[Tensor] = None,
    b_k: Optional[Tensor] = None,
    b_v: Optional[Tensor] = None,

# ==================================================
# Line: 6091

def multi_head_attention_forward(
    query: Tensor,
    key: Tensor,
    value: Tensor,
    embed_dim_to_check: int,
    num_heads: int,
    in_proj_weight: Optional[Tensor],
    in_proj_bias: Optional[Tensor],
    bias_k: Optional[Tensor],
    bias_v: Optional[Tensor],
    add_zero_attn: bool,
    dropout_p: float,
    out_proj_weight: Tensor,
    out_proj_bias: Optional[Tensor],
    training: bool = True,
    key_padding_mask: Optional[Tensor] = None,
    need_weights: bool = True,
    attn_mask: Optional[Tensor] = None,
    use_separate_proj_weight: bool = False,
    q_proj_weight: Optional[Tensor] = None,
    k_proj_weight: Optional[Tensor] = None,
    v_proj_weight: Optional[Tensor] = None,
    static_k: Optional[Tensor] = None,
    static_v: Optional[Tensor] = None,
    average_attn_weights: bool = True,
    is_causal: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/parallel/distributed.py
# Line: 638

def __init__(
    self,
    module,
    device_ids=None,
    output_device=None,
    dim=0,
    broadcast_buffers=True,
    init_sync=True,
    process_group=None,
    bucket_cap_mb=None,
    find_unused_parameters=False,
    check_reduction=False,
    gradient_as_bucket_view=False,
    static_graph=False,
    delay_all_reduce_named_params=None,
    param_to_hook_all_reduce=None,
    mixed_precision: Optional[_MixedPrecision] = None,
    device_mesh=None,
    skip_all_reduce_unused_params=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/__init__.py
# Line: 1047

def _make_elementwise_binary_reference(
    type_promotion_kind,
    aten_op=infer_aten_op,
    name=None,
    has_out=True,
    supports_lhs_python_scalar=True,
    supports_rhs_python_scalar=True,
    supports_two_python_scalars=False,
    should_register_decomposition=True,

# ==================================================
# Line: 2008

def _to_will_alias(
    a: TensorLikeType,
    device: Optional[DeviceLikeType] = None,
    dtype: Optional[torch.dtype] = None,
    copy: Optional[bool] = None,
    layout: Optional[torch.layout] = None,
    memory_format: Optional[torch.memory_format] = None,
    pin_memory: Optional[bool] = False,
    non_blocking: bool = False,  # not using non_blocking

# ==================================================
# Line: 2177

def _reduction(
    a: TensorLikeType,
    prim: Callable,
    *,
    has_identity: bool = True,
    accepts_dim_tuple: bool = True,  # to handle min/argmin that accept single dim only
    dims: Optional[DimsType] = None,
    keepdims: bool = False,
    dtype: Optional[torch.dtype] = None,  # should be specified for ops that support it
    out: Optional[Tensor] = None,
    output_dtype_kind: REDUCTION_OUTPUT_TYPE_KIND,

# ==================================================
# Line: 3184

def native_group_norm(
    input: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    batch_size: int,
    num_channels: int,
    flattened_inner_size: int,
    num_groups: int,
    eps: float,

# ==================================================
# Line: 3382

def stft(
    input: Tensor,
    n_fft: int,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: Optional[Tensor] = None,
    center: bool = True,
    pad_mode: str = "reflect",
    normalized: bool = False,
    onesided: Optional[bool] = None,
    return_complex: Optional[bool] = None,
    align_to_window: Optional[bool] = None,

# ==================================================
# Line: 3499

def istft(
    input: Tensor,
    n_fft: int,
    hop_length: Optional[int] = None,
    win_length: Optional[int] = None,
    window: Optional[Tensor] = None,
    center: bool = True,
    normalized: bool = False,
    onesided: Optional[bool] = None,
    length: Optional[int] = None,
    return_complex=False,

# ==================================================
# Line: 4946

def empty_permuted(
    shape,
    physical_layout,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    device: Optional[DeviceLikeType] = None,
    requires_grad: bool = False,
    pin_memory: bool = False,

# ==================================================
# Line: 4990

def new_empty_strided(
    a: TensorLikeType,
    size: ShapeType,
    stride: StrideType,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: Optional[torch.layout] = None,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,

# ==================================================
# Line: 5046

def new_zeros(
    a: TensorLikeType,
    size: ShapeType,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: Optional[torch.layout] = None,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,

# ==================================================
# Line: 5099

def new_ones(
    a: TensorLikeType,
    size: ShapeType,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: Optional[torch.layout] = None,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,

# ==================================================
# Line: 5126

def new_full(
    a: TensorLikeType,
    size: ShapeType,
    fill_value: NumberType,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: Optional[torch.layout] = None,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,

# ==================================================
# Line: 5161

def empty_like(
    a: TensorLikeType,
    *,
    dtype: Optional[torch.dtype] = None,
    device: Optional[DeviceLikeType] = None,
    layout: Optional[torch.layout] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,
    memory_format: torch.memory_format = torch.preserve_format,

# ==================================================
# Line: 5204

def arange(
    start: NumberType = 0,
    end: Optional[NumberType] = None,
    step: NumberType = 1,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,

# ==================================================
# Line: 5336

def linspace(
    start: Union[NumberType, TensorLikeType],
    end: Union[NumberType, TensorLikeType],
    steps: NumberType,
    *,
    dtype: Optional[torch.dtype] = None,
    device: Optional[DeviceLikeType] = None,
    layout: torch.layout = torch.strided,
    pin_memory: bool = False,
    requires_grad: bool = False,

# ==================================================
# Line: 5426

def logspace(
    start: Union[NumberType, TensorLikeType],
    end: Union[NumberType, TensorLikeType],
    steps: NumberType,
    base: NumberType = 10,
    *,
    dtype: Optional[torch.dtype] = None,
    device: Optional[DeviceLikeType] = None,
    layout: torch.layout = torch.strided,
    pin_memory: bool = False,
    requires_grad: bool = False,

# ==================================================
# Line: 5627

def empty_strided(
    shape: Union[ShapeType, tuple[ShapeType]],
    strides: StrideType,
    *,
    dtype: Optional[torch.dtype] = None,
    device: Optional[DeviceLikeType] = None,
    layout: torch.layout = torch.strided,
    requires_grad: bool = False,
    pin_memory: bool = False,

# ==================================================
# Line: 5656

def eye(
    n: int,
    m: Optional[int] = None,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,  # TODO: unused

# ==================================================
# Line: 5698

def full(
    shape: ShapeType,
    fill_value: NumberType,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: torch.layout = torch.strided,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,

# ==================================================
# Line: 5725

def full_like(
    a: TensorLikeType,
    fill_value: NumberType,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: Optional[torch.layout] = None,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,
    memory_format: torch.memory_format = torch.preserve_format,

# ==================================================
# Line: 5750

def zeros_like(
    a: TensorLikeType,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: Optional[torch.layout] = None,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,
    memory_format: torch.memory_format = torch.preserve_format,

# ==================================================
# Line: 5774

def ones_like(
    a: TensorLikeType,
    *,
    dtype: Optional[torch.dtype] = None,
    layout: Optional[torch.layout] = None,
    device: Optional[DeviceLikeType] = None,
    pin_memory: bool = False,
    requires_grad: bool = False,
    memory_format: torch.memory_format = torch.preserve_format,

# ==================================================
# Line: 6083

def tril_indices(
    row: int,
    col: int,
    offset: int = 0,
    *,
    dtype: torch.dtype = torch.long,
    layout: torch.layout = torch.strided,
    device: DeviceLikeType = "cpu",
    pin_memory: bool = False,

# ==================================================
# Line: 6143

def triu_indices(
    row: int,
    col: int,
    offset: int = 0,
    *,
    dtype: torch.dtype = torch.long,
    layout: torch.layout = torch.strided,
    device: DeviceLikeType = "cpu",
    pin_memory: bool = False,

# ==================================================
# Line: 6352

def normal(
    mean=0,
    std=1,
    size=None,
    *,
    generator=None,
    dtype=None,
    layout=None,
    device=None,
    pin_memory=None,

# ==================================================
# Line: 6744

def _internal_new_from_data(
    options,
    scalar_type,
    device_opt,
    data,
    copy_variables,
    copy_numpy,
    type_inference,
    pin_memory=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/fft.py
# Line: 144

def _fft_r2c(
    func_name: str,
    input: TensorLikeType,
    n: Optional[int],
    dim: int,
    norm: NormType,
    forward: bool,
    onesided: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_refs/nn/functional/__init__.py
# Line: 789

def nll_loss(
    input: TensorLikeType,
    target: TensorLikeType,
    weight: Optional[TensorLikeType] = None,
    size_average: Optional[bool] = None,
    ignore_index: int = -100,
    reduce: Optional[bool] = None,
    reduction: str = "mean",

# ==================================================
# Line: 935

def triplet_margin_loss(
    anchor: TensorLikeType,
    positive: TensorLikeType,
    negative: TensorLikeType,
    margin: float = 1.0,
    p: float = 2,
    eps: float = 1e-6,
    swap: bool = False,
    size_average: Optional[bool] = None,
    reduce: Optional[bool] = None,
    reduction: str = "mean",

# ==================================================
# Line: 971

def _triplet_margin_with_distance_loss(
    anchor: TensorLikeType,
    positive: TensorLikeType,
    negative: TensorLikeType,
    *,
    distance_function: Optional[
        Callable[[TensorLikeType, TensorLikeType], TensorLikeType]
    ] = None,
    margin: float = 1.0,
    swap: bool = False,
    reduction: str = "mean",

# ==================================================
# Line: 1087

def poisson_nll_loss(
    input: TensorLikeType,
    target: TensorLikeType,
    log_input: bool = True,
    full: bool = False,
    size_average: Optional[bool] = None,
    eps: float = 1e-8,
    reduce: Optional[bool] = None,
    reduction: str = "mean",

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/_numeric_suite_fx.py
# Line: 149

def __init__(
    self,
    ref_node_name: str,
    prev_node_name: str,
    model_name: str,
    ref_name: str,
    prev_node_target_type: str,
    ref_node_target_type: str,
    results_type: str,
    index_within_arg: int,
    index_of_arg: int,
    fqn: Optional[str],
    qconfig_str: Optional[str] = "",

# ==================================================
# Line: 327

def _extract_weights_impl(
    model_name_a: str,
    gm_a: GraphModule,
    model_name_b: str,
    gm_b: GraphModule,
    base_name_to_sets_of_related_ops: Optional[dict[str, set[NSNodeTargetType]]] = None,
    unmatchable_types_map: Optional[dict[str, set[NSNodeTargetType]]] = None,
    op_to_type_to_weight_extraction_fn: Optional[
        dict[str, dict[Callable, Callable]]
    ] = None,

# ==================================================
# Line: 379

def extract_weights(
    model_name_a: str,
    model_a: nn.Module,
    model_name_b: str,
    model_b: nn.Module,
    base_name_to_sets_of_related_ops: Optional[dict[str, set[NSNodeTargetType]]] = None,
    unmatchable_types_map: Optional[dict[str, set[NSNodeTargetType]]] = None,
    op_to_type_to_weight_extraction_fn: Optional[
        dict[str, dict[Callable, Callable]]
    ] = None,

# ==================================================
# Line: 469

def _add_loggers_impl(
    name_a: str,
    gm_a: GraphModule,
    name_b: str,
    gm_b: GraphModule,
    logger_cls: Callable,
    should_log_inputs: bool,
    base_name_to_sets_of_related_ops: Optional[dict[str, set[NSNodeTargetType]]] = None,
    unmatchable_types_map: Optional[dict[str, set[NSNodeTargetType]]] = None,

# ==================================================
# Line: 525

def add_loggers(
    name_a: str,
    model_a: nn.Module,
    name_b: str,
    model_b: nn.Module,
    logger_cls: Callable,
    should_log_inputs: bool = False,
    base_name_to_sets_of_related_ops: Optional[dict[str, set[NSNodeTargetType]]] = None,
    unmatchable_types_map: Optional[dict[str, set[NSNodeTargetType]]] = None,

# ==================================================
# Line: 671

def _add_shadow_loggers_impl(
    name_a: str,
    gm_a: GraphModule,
    name_b: str,
    gm_b: GraphModule,
    logger_cls: Callable,
    should_log_inputs: bool,
    base_name_to_sets_of_related_ops: Optional[dict[str, set[NSNodeTargetType]]] = None,
    node_type_to_io_type_map: Optional[dict[str, set[NSNodeTargetType]]] = None,
    unmatchable_types_map: Optional[dict[str, set[NSNodeTargetType]]] = None,

# ==================================================
# Line: 701

def add_shadow_loggers(
    name_a: str,
    model_a: nn.Module,
    name_b: str,
    model_b: nn.Module,
    logger_cls: Callable,
    should_log_inputs: bool = False,
    base_name_to_sets_of_related_ops: Optional[dict[str, set[NSNodeTargetType]]] = None,
    node_type_to_io_type_map: Optional[dict[str, set[NSNodeTargetType]]] = None,
    unmatchable_types_map: Optional[dict[str, set[NSNodeTargetType]]] = None,

# ==================================================
# Line: 846

def prepare_n_shadows_model(
    model: torch.nn.Module,
    example_inputs: Any,
    qconfig_multi_mapping: QConfigMultiMapping,
    backend_config: BackendConfig,
    custom_prepare_fn: Optional[Callable] = None,
    custom_prepare_kwargs: Optional[dict[str, Any]] = None,
    custom_tracer: Any = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/fx/graph_passes.py
# Line: 42

def _insert_logger_after_node(
    node: Node,
    gm: GraphModule,
    logger_cls: Callable,
    logger_node_name_suffix: str,
    ref_node_name: str,
    model_name: str,
    ref_name: str,
    ref_node_target_type: str,
    results_type: str,
    index_within_arg: int,
    index_of_arg: int,
    fqn: Optional[str],

# ==================================================
# Line: 201

def _insert_quantize_per_tensor_node(
    prev_node_c: Node,
    node_a: Node,
    gm_b: GraphModule,
    graph_c: Graph,
    scale: Union[torch.Tensor, float],
    zero_point: Union[torch.Tensor, int],
    dtype_cast_name: str,

# ==================================================
# Line: 234

def _insert_dtype_cast_after_node(
    node_a: Node,
    node_c: Node,
    prev_node_c: Union[Node, list[Node]],
    gm_a: GraphModule,
    gm_b: GraphModule,
    graph_c: Graph,
    node_name_prefix: str,
    logger_cls: Callable,
    node_type_to_io_type_map: dict[str, set[NSNodeTargetType]],

# ==================================================
# Line: 703

def create_a_shadows_b(
    name_a: str,
    gm_a: GraphModule,
    name_b: str,
    gm_b: GraphModule,
    matched_subgraph_pairs: dict[str, tuple[NSSubgraph, NSSubgraph]],
    logger_cls: Callable,
    should_log_inputs: bool,
    node_type_to_io_type_map: Optional[dict[str, set[NSNodeTargetType]]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/ns/fx/n_shadows_utils.py
# Line: 212

def _get_logger_for_subgraph(
    model: GraphModule,
    first_node: Node,
    last_node: Node,
    subgraph_idx: int,
    subgraph_candidate_idx: int,
    qconfig_str: str,
    logger_cls: Callable,
    fqn: Optional[str],

# ==================================================
# Line: 445

def create_one_transformed_and_logged_copy_of_subgraph(
    mt: GraphModule,
    subgraph_idx: int,
    subgraph_candidate_idx: int,
    first_node: Node,
    last_node: Node,
    fqn: Optional[str],
    list_of_node_name_to_qconfig: list[dict[str, QConfigAny]],
    example_inputs: Any,
    last_added_shadow_node_list: list[Optional[Node]],
    custom_prepare_fn: Optional[Callable] = None,
    custom_prepare_kwargs: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 606

def create_n_transformed_and_logged_copies_of_subgraph(
    mt: GraphModule,
    subgraph_idx: int,
    match_name: str,
    nodes_in_this_subgraph: list[Any],
    qconfig_mappings: list[QConfigMapping],
    list_of_node_name_to_qconfig: list[dict[str, QConfigAny]],
    custom_prepare_fn: Optional[Callable] = None,
    custom_prepare_kwargs: Optional[dict[str, Any]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/scheduler/cubic_scheduler.py
# Line: 42

def __init__(
    self,
    sparsifier,
    init_sl=0.0,
    init_t=0,
    delta_t=10,
    total_t=100,
    initially_zero=False,
    last_epoch=-1,
    verbose=False,

# ==================================================
# Line: 65

def sparsity_compute_fn(s_0, s_f, t, t_0, dt, n, initially_zero=False):
    r""" "Computes the current level of sparsity.

    Based on https://arxiv.org/pdf/1710.01878.pdf

    Args:
        s_0: Initial level of sparsity, :math:`s_i`
        s_f: Target level of sparsity, :math:`s_f`
        t: Current step, :math:`t`
        t_0: Initial step, :math:`t_0`
        dt: Pruning frequency, :math:`\Delta T`
        n: Pruning steps, :math:`n`
        initially_zero: Sets the level of sparsity to 0 before t_0.
            If False, sets to s_0

    Returns:
        The sparsity level :math:`s_t` at the current step :math:`t`
    """
    if initially_zero and t < t_0:
        return 0
    s_t = s_f + (s_0 - s_f) * (1.0 - (t - t_0) / (dt * n)) ** 3
    s_t = _clamp(s_t, s_0, s_f)
    return s_t


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/activation_sparsifier/activation_sparsifier.py
# Line: 90

def __init__(
    self,
    model: nn.Module,
    aggregate_fn=None,
    reduce_fn=None,
    mask_fn=None,
    features=None,
    feature_dim=None,
    **sparse_config,

# ==================================================
# Line: 185

def register_layer(
    self,
    layer: nn.Module,
    aggregate_fn=None,
    reduce_fn=None,
    mask_fn=None,
    features=None,
    feature_dim=None,
    **sparse_config,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/sparsifier/weight_norm_sparsifier.py
# Line: 85

def _scatter_fold_block_mask(
    self,
    output_shape,
    dim,
    indices,
    block_shape,
    mask=None,
    input_shape=None,
    device=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/quantize_jit.py
# Line: 218

def _quantize_jit(
    model,
    qconfig_dict,
    run_fn=None,
    run_args=None,
    inplace=False,
    debug=False,
    quant_type=QuantType.STATIC,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/__init__.py
# Line: 203

def __init__(
    self,
    dtype: torch.dtype,
    obs_or_fqs: list[ObserverOrFakeQuantize],
    derive_qparams_fn: Callable[
        [list[ObserverOrFakeQuantize]], tuple[Tensor, Tensor]
    ],
    quant_min: Optional[int] = None,
    quant_max: Optional[int] = None,
    qscheme: Optional[torch.qscheme] = None,
    ch_axis: Optional[int] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/pt2e/_affine_quantization.py
# Line: 192

def choose_qparams_affine_with_min_max(
    min_val: torch.Tensor,
    max_val: torch.Tensor,
    mapping_type: MappingType,
    block_size: tuple[int, ...],
    target_dtype: torch.dtype,
    quant_min: Optional[int] = None,
    quant_max: Optional[int] = None,
    eps: Optional[float] = None,
    scale_dtype: Optional[torch.dtype] = None,
    zero_point_dtype: Optional[torch.dtype] = None,
    preserve_zero: bool = True,
    zero_point_domain: Optional[ZeroPointDomain] = ZeroPointDomain.INT,

# ==================================================
# Line: 234

def _choose_qparams_affine(
    input: Optional[torch.Tensor],
    mapping_type: str,
    block_size: list[int],
    target_dtype: torch.dtype,
    quant_min: Optional[Union[int, float, bool]] = None,
    quant_max: Optional[Union[int, float, bool]] = None,
    eps: Optional[float] = None,
    scale_dtype: Optional[torch.dtype] = None,
    zero_point_dtype: Optional[torch.dtype] = None,
    preserve_zero: bool = True,
    zero_point_domain: Optional[str] = "INT",
    min_val: Optional[torch.Tensor] = None,
    max_val: Optional[torch.Tensor] = None,

# ==================================================
# Line: 366

def quantize_affine(
    input: torch.Tensor,
    block_size: tuple[int, ...],
    scale: torch.Tensor,
    zero_point: Optional[torch.Tensor],
    output_dtype: torch.dtype,
    quant_min: Optional[Union[int, float]] = None,
    quant_max: Optional[Union[int, float]] = None,
    zero_point_domain: Optional[ZeroPointDomain] = ZeroPointDomain.INT,

# ==================================================
# Line: 423

def _quantize_affine(
    input: torch.Tensor,
    block_size: list[int],
    scale: torch.Tensor,
    zero_point: Optional[torch.Tensor],
    output_dtype: torch.dtype,
    quant_min: Optional[Union[int, float, bool]] = None,
    quant_max: Optional[Union[int, float, bool]] = None,
    zero_point_domain: Optional[str] = ZeroPointDomain.INT.name,

# ==================================================
# Line: 458

def _quantize_affine_no_dtype_cast(
    input: torch.Tensor,
    block_size: list[int],
    scale: torch.Tensor,
    zero_point: Optional[torch.Tensor],
    quant_min: Union[int, float],
    quant_max: Union[int, float],
    zero_point_domain: Optional[str] = ZeroPointDomain.INT.name,

# ==================================================
# Line: 523

def dequantize_affine(
    input: torch.Tensor,
    block_size: tuple[int, ...],
    scale: torch.Tensor,
    zero_point: Optional[torch.Tensor],
    input_dtype: torch.dtype,
    quant_min: Optional[Union[int, float]] = None,
    quant_max: Optional[Union[int, float]] = None,
    zero_point_domain: ZeroPointDomain = ZeroPointDomain.INT,
    *,
    output_dtype: torch.dtype = torch.float32,

# ==================================================
# Line: 571

def _dequantize_affine(
    input: torch.Tensor,
    block_size: list[int],
    scale: torch.Tensor,
    zero_point: Optional[torch.Tensor],
    input_dtype: torch.dtype,
    quant_min: Optional[Union[int, float, bool]] = None,
    quant_max: Optional[Union[int, float, bool]] = None,
    zero_point_domain: Optional[str] = ZeroPointDomain.INT.name,
    output_dtype: torch.dtype = torch.float32,

# ==================================================
# Line: 606

def _dequantize_affine_no_dtype_check(
    input: torch.Tensor,
    block_size: list[int],
    scale: torch.Tensor,
    zero_point: Optional[torch.Tensor],
    quant_min: Union[int, float],
    quant_max: Union[int, float],
    zero_point_domain: Optional[str] = ZeroPointDomain.INT.name,
    output_dtype: torch.dtype = torch.float32,

# ==================================================
# Line: 734

def __init__(
    self,
    mapping_type: MappingType,
    target_dtype: torch.dtype,
    granularity: Granularity,
    averaging_constant=0.01,
    quant_min: Optional[int] = None,
    quant_max: Optional[int] = None,
    eps: Optional[float] = None,
    is_dynamic=False,
    scale_dtype: Optional[torch.dtype] = None,
    zero_point_dtype: Optional[torch.dtype] = None,
    preserve_zero: bool = True,
    zero_point_domain: Optional[ZeroPointDomain] = ZeroPointDomain.INT,
    # there could be some extra args that's ignored
    **kwargs,

# ==================================================
# Line: 827

def __init__(
    self,
    mapping_type: MappingType,
    target_dtype: torch.dtype,
    granularity: Granularity,
    quant_min: Optional[int] = None,
    quant_max: Optional[int] = None,
    eps: Optional[float] = None,
    is_dynamic=False,
    scale_dtype: Optional[torch.dtype] = None,
    zero_point_dtype: Optional[torch.dtype] = None,
    preserve_zero: bool = True,
    zero_point_domain: Optional[ZeroPointDomain] = ZeroPointDomain.INT,
    # there could be some extra args that's ignored
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/pt2e/prepare.py
# Line: 314

def _maybe_insert_input_observer_for_arg_or_kwarg(
    node: Union[Node, Any],
    arg: Argument,
    qconfig: QConfigAny,
    model: torch.nn.Module,
    named_modules: dict[str, torch.nn.Module],
    obs_or_fq_map: dict[EdgeOrNode, ObserverOrFakeQuantize],
    is_qat: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/pt2e/qat_utils.py
# Line: 65

def _conv_bn_pattern(
    x: torch.Tensor,
    conv_weight: torch.Tensor,
    conv_bias: torch.Tensor,
    bn_weight: torch.Tensor,
    bn_bias: torch.Tensor,
    bn_running_mean: torch.Tensor,
    bn_running_var: torch.Tensor,

# ==================================================
# Line: 85

def _qat_conv_bn_pattern(
    x: torch.Tensor,
    conv_weight: torch.Tensor,
    conv_bias: torch.Tensor,
    bn_weight: torch.Tensor,
    bn_bias: torch.Tensor,
    bn_running_mean: torch.Tensor,
    bn_running_var: torch.Tensor,

# ==================================================
# Line: 128

def _qat_conv_bn_pattern_no_conv_bias(
    x: torch.Tensor,
    conv_weight: torch.Tensor,
    # Not used, only for matching convenience
    conv_bias: torch.Tensor,
    bn_weight: torch.Tensor,
    bn_bias: torch.Tensor,
    bn_running_mean: torch.Tensor,
    bn_running_var: torch.Tensor,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/pt2e/representation/rewrite.py
# Line: 26

def _qdq_quantized_linear(
    x_i8,
    x_scale,
    x_zero_point,
    x_quant_min,
    x_quant_max,
    weight_i8,
    weight_scale,
    weight_zero_point,
    weight_quant_min,
    weight_quant_max,
    bias_fp32,
    out_scale,
    out_zero_point,
    out_quant_min,
    out_quant_max,

# ==================================================
# Line: 61

def _reference_quantized_linear(
    x_i8,
    x_scale,
    x_zero_point,
    x_quant_min,
    x_quant_max,
    weight_i8,
    weight_scale,
    weight_zero_point,
    weight_quant_min,
    weight_quant_max,
    bias_fp32,
    out_scale,
    out_zero_point,
    out_quant_min,
    out_quant_max,

# ==================================================
# Line: 114

def _qdq_dynamic_quantized_linear(
    x_fp32,
    x_quant_min,
    x_quant_max,
    x_eps,
    weight_i8,
    weight_scale,
    weight_zero_point,
    weight_quant_min,
    weight_quant_max,
    bias_fp32,

# ==================================================
# Line: 147

def _reference_dynamic_quantized_linear(
    x_fp32,
    x_quant_min,
    x_quant_max,
    x_eps,
    weight_i8,
    weight_scale,
    weight_zero_point,
    weight_quant_min,
    weight_quant_max,
    bias_fp32,

# ==================================================
# Line: 194

def _qdq_quantized_conv2d(
    x_i8,
    x_scale,
    x_zero_point,
    x_quant_min,
    x_quant_max,
    weight_i8,
    weight_scale,
    weight_zero_point,
    weight_quant_min,
    weight_quant_max,
    bias_fp32,
    out_scale,
    out_zero_point,
    out_quant_min,
    out_quant_max,

# ==================================================
# Line: 245

def _reference_quantized_conv2d(
    x_i8,
    x_scale,
    x_zero_point,
    x_quant_min,
    x_quant_max,
    weight_i8,
    weight_scale,
    weight_zero_point,
    weight_quant_min,
    weight_quant_max,
    bias_fp32,
    out_scale,
    out_zero_point,
    out_quant_min,
    out_quant_max,

# ==================================================
# Line: 327

def _qdq_quantized_add_relu(
    x_i8,
    x_scale,
    x_zero_point,
    y_i8,
    y_scale,
    y_zero_point,
    out_scale,
    out_zero_point,
    quant_min,
    quant_max,

# ==================================================
# Line: 353

def _reference_quantized_add_relu(
    x_i8,
    x_scale,
    x_zero_point,
    y_i8,
    y_scale,
    y_zero_point,
    out_scale,
    out_zero_point,
    quant_min,
    quant_max,

# ==================================================
# Line: 390

def _qdq_quantized_add(
    x_i8,
    x_scale,
    x_zero_point,
    y_i8,
    y_scale,
    y_zero_point,
    out_scale,
    out_zero_point,
    quant_min,
    quant_max,

# ==================================================
# Line: 415

def _reference_quantized_add(
    x_i8,
    x_scale,
    x_zero_point,
    y_i8,
    y_scale,
    y_zero_point,
    out_scale,
    out_zero_point,
    quant_min,
    quant_max,

# ==================================================
# Line: 456

def _qdq_quantized_max_pool2d(
    x_i8,
    x_scale,
    x_zero_point,
    x_quant_min,
    x_quant_max,
    out_scale,
    out_zero_point,
    out_quant_min,
    out_quant_max,

# ==================================================
# Line: 484

def _reference_quantized_max_pool2d(
    x_i8,
    x_scale,
    x_zero_point,
    x_quant_min,
    x_quant_max,
    out_scale,
    out_zero_point,
    out_quant_min,
    out_quant_max,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/backend_config/onednn.py
# Line: 518

def _add_eltwise_fusion_configs(
    configs,
    root_module,
    root_op,
    post_module,
    post_op,
    dtype_configs,
    fuser_method,
    fused_module,
    observation_type,
    ref_quant_module,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/utils.py
# Line: 620

def determine_qparams(
    min_val: torch.Tensor,
    max_val: torch.Tensor,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    eps: torch.Tensor,
    has_customized_qrange: bool,
    qscheme: torch.qscheme = torch.per_tensor_affine,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/_learnable_fake_quantize.py
# Line: 36

def __init__(
    self,
    observer,
    quant_min=0,
    quant_max=255,
    scale=1.0,
    zero_point=0.0,
    channel_len=-1,
    use_grad_scaling=False,
    **observer_kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_lower_to_native_backend.py
# Line: 426

def _load_packed_weight(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/lstm_utils.py
# Line: 19

def _get_lstm_with_individually_observed_parts(
    float_lstm: torch.nn.LSTM,
    example_inputs: tuple[Any, ...],
    backend_config: Optional[BackendConfig] = None,
    linear_output_obs_ctr: Optional[_PartialWrapper] = None,
    sigmoid_obs_ctr: Optional[_PartialWrapper] = None,
    tanh_obs_ctr: Optional[_PartialWrapper] = None,
    cell_state_obs_ctr: Optional[_PartialWrapper] = None,
    hidden_state_obs_ctr: Optional[_PartialWrapper] = None,
    split_gates: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/match_utils.py
# Line: 80

def _find_matches(
    graph: Graph,
    modules: dict[str, torch.nn.Module],
    patterns: dict[Pattern, QuantizeHandler],
    root_node_getter_mapping: dict[Pattern, Callable],
    standalone_module_names: Optional[list[str]] = None,
    standalone_module_classes: Optional[list[type]] = None,
    custom_module_classes: Optional[list[Any]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/graph_module.py
# Line: 166

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/fuse_handler.py
# Line: 36

def fuse(
    self,
    load_arg: Callable,
    named_modules: dict[str, torch.nn.Module],
    fused_graph: Graph,
    root_node: Node,
    extra_inputs: list[Any],
    matched_node_pattern: NodePattern,
    fuse_custom_config: FuseCustomConfig,
    fuser_method_mapping: dict[Pattern, Union[torch.nn.Sequential, Callable]],
    is_qat: bool,

# ==================================================
# Line: 55

def fuse(
    self,
    load_arg: Callable,
    named_modules: dict[str, torch.nn.Module],
    fused_graph: Graph,
    root_node: Node,
    extra_inputs: list[Any],
    matched_node_pattern: NodePattern,
    fuse_custom_config: FuseCustomConfig,
    fuser_method_mapping: dict[Pattern, Union[torch.nn.Sequential, Callable]],
    is_qat: bool,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/prepare.py
# Line: 505

def _set_target_dtype_info_for_matched_node_pattern(
    matched_node_pattern: NodePattern,
    last_node: Node,
    qconfig: QConfigAny,
    qhandler: Optional[QuantizeHandler],
    backend_config: BackendConfig,
    named_modules: dict[str, torch.nn.Module],
    cache_for_no_tensor_check: dict[Node, bool],
    processed_nodes: set[Node],

# ==================================================
# Line: 796

def _maybe_insert_input_observer_for_arg_or_kwarg(
    node: Union[Node, Any],
    arg: Argument,
    qconfig: QConfigAny,
    model: torch.nn.Module,
    named_modules: dict[str, torch.nn.Module],
    graph: Graph,
    qhandler: Optional[QuantizeHandler],
    prepare_custom_config: PrepareCustomConfig,
    obs_or_fq_map: dict[EdgeOrNode, ObserverOrFakeQuantize],
    is_qat: bool,
    backend_config: Optional[BackendConfig] = None,

# ==================================================
# Line: 959

def _maybe_insert_input_observers_for_node(
    node: Node,
    qconfig: QConfigAny,
    model: torch.nn.Module,
    named_modules: dict[str, torch.nn.Module],
    graph: Graph,
    qhandler: Optional[QuantizeHandler],
    prepare_custom_config: PrepareCustomConfig,
    obs_or_fq_map: dict[EdgeOrNode, ObserverOrFakeQuantize],
    is_qat: bool,
    backend_config: Optional[BackendConfig] = None,

# ==================================================
# Line: 1441

def insert_observers_for_model(
    model: GraphModule,
    node_name_to_match_result_with_qconfig: dict[str, _MatchResultWithQConfig],
    node_name_to_qconfig: dict[str, QConfigAny],
    prepare_custom_config: PrepareCustomConfig,
    equalization_config_map: dict[str, Any],
    backend_config: BackendConfig,
    observed_node_names: set[str],
    is_qat: bool,

# ==================================================
# Line: 1957

def _save_state(
    observed: GraphModule,
    node_name_to_qconfig: dict[str, QConfigAny],
    node_name_to_scope: dict[str, tuple[str, type]],
    prepare_custom_config: PrepareCustomConfig,
    equalization_node_name_to_qconfig: dict[str, Any],
    qconfig_mapping: QConfigMapping,
    is_qat: bool,
    observed_node_names: set[str],

# ==================================================
# Line: 1978

def prepare(
    model: GraphModule,
    qconfig_mapping: Union[QConfigMapping, dict[str, Any]],
    is_qat: bool,
    node_name_to_scope: dict[str, tuple[str, type]],
    example_inputs: tuple[Any, ...],
    prepare_custom_config: Union[PrepareCustomConfig, dict[str, Any], None] = None,
    _equalization_config: Union[QConfigMapping, dict[str, Any], None] = None,
    backend_config: Union[BackendConfig, dict[str, Any], None] = None,
    is_standalone_module: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/convert.py
# Line: 735

def convert_weighted_module(
    node: Node,
    modules: dict[str, torch.nn.Module],
    observed_node_names: set[str],
    node_name_to_qconfig: dict[str, QConfigAny],
    backend_config: BackendConfig,
    is_decomposed: bool = False,
    is_reference: bool = False,

# ==================================================
# Line: 986

def convert(
    model: GraphModule,
    is_reference: bool = False,
    convert_custom_config: Union[ConvertCustomConfig, dict[str, Any], None] = None,
    is_standalone_module: bool = False,
    _remove_qconfig_flag: bool = True,
    qconfig_mapping: Union[QConfigMapping, dict[str, Any], None] = None,
    backend_config: Union[BackendConfig, dict[str, Any], None] = None,
    is_decomposed: bool = False,
    keep_original_weights: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_decomposed.py
# Line: 223

def dequantize_per_tensor(
    input: torch.Tensor,
    scale: float,
    zero_point: int,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 274

def dequantize_per_tensor_meta(
    input: torch.Tensor,
    scale: torch.Tensor,
    zero_point: torch.Tensor,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 300

def dequantize_per_tensor_tensor(
    input: torch.Tensor,
    scale: torch.Tensor,
    zero_point: torch.Tensor,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 333

def dequantize_per_tensor_tensor_meta(
    input: torch.Tensor,
    scale: torch.Tensor,
    zero_point: torch.Tensor,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 370

def dequantize_per_tensor_tensor2(
    input: torch.Tensor,
    scale: torch.Tensor,
    zero_point: torch.Tensor,
    quant_min: torch.Tensor,
    quant_max: torch.Tensor,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 403

def dequantize_per_tensor_tensor2_meta(
    input,
    scale,
    zero_point,
    quant_min,
    quant_max,
    dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 557

def quantize_per_channel(
    input: torch.Tensor,
    scales: torch.Tensor,
    zero_points: torch.Tensor,
    axis: int,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,

# ==================================================
# Line: 605

def quantize_per_channel_meta(
    input: torch.Tensor,
    scales: torch.Tensor,
    zero_points: torch.Tensor,
    axis: int,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,

# ==================================================
# Line: 635

def dequantize_per_channel(
    input: torch.Tensor,
    scales: torch.Tensor,
    zero_points: Optional[torch.Tensor],
    axis: int,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 698

def dequantize_per_channel_meta(
    input: torch.Tensor,
    scales: torch.Tensor,
    zero_points: Optional[torch.Tensor],
    axis: int,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    *,
    out_dtype: Optional[torch.dtype] = None,

# ==================================================
# Line: 939

def dequantize_per_token(
    input: torch.Tensor,
    scales: torch.Tensor,
    zero_points: torch.Tensor,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    output_dtype: torch.dtype = torch.float32,

# ==================================================
# Line: 973

def dequantize_per_token_meta(
    input: torch.Tensor,
    scales: torch.Tensor,
    zero_points: torch.Tensor,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    output_dtype: torch.dtype = torch.float32,

# ==================================================
# Line: 997

def quantize_per_channel_group(
    input: torch.Tensor,
    scales: torch.Tensor,
    zero_points: torch.Tensor,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    group_size=128,

# ==================================================
# Line: 1034

def quantize_per_channel_group_meta(
    input: torch.Tensor,
    scales: torch.Tensor,
    zero_points: torch.Tensor,
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    group_size=128,

# ==================================================
# Line: 1082

def dequantize_per_channel_group(
    w_int8: torch.Tensor,
    scales: torch.Tensor,
    zero_points: Optional[torch.Tensor],
    quant_min: int,
    quant_max: int,
    dtype: torch.dtype,
    group_size: int = 128,
    output_dtype: torch.dtype = torch.float32,

# ==================================================
# Line: 1136

def forward(ctx, input, scales, zero_points, axis, quant_min, quant_max):
    if scales.dtype != torch.float32:
        scales = scales.to(torch.float32)
    if zero_points.dtype != torch.int32:
        zero_points = zero_points.to(torch.int32)
    assert (
        input.dtype == torch.float32
    ), f"Expecting input to have dtype torch.float32, but got dtype: {input.dtype}"
    assert axis < input.dim(), f"Expecting axis to be < {input.dim()}"
    broadcast_dims = list(range(0, axis)) + list(range(axis + 1, input.ndim))
    unsqueeze_scales = _unsqueeze_multiple(scales, broadcast_dims)
    unsqueeze_zero_points = _unsqueeze_multiple(zero_points, broadcast_dims)
    temp = torch.round(input * (1.0 / unsqueeze_scales)) + unsqueeze_zero_points
    out = (
        torch.clamp(temp, quant_min, quant_max) - unsqueeze_zero_points
    ) * unsqueeze_scales
    mask = torch.logical_and((temp >= quant_min), (temp <= quant_max))

    ctx.save_for_backward(mask)
    return out


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/quantizer/xnnpack_quantizer.py
# Line: 106

def get_symmetric_quantization_config(
    is_per_channel: bool = False,
    is_qat: bool = False,
    is_dynamic: bool = False,
    act_qmin: int = -128,
    act_qmax: int = 127,
    weight_qmin: int = -127,
    weight_qmax: int = 127,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/quantizer/xnnpack_quantizer_utils.py
# Line: 512

def _conv_bn(x, conv_weight, conv_bias, bn_weight, bn_bias, bn_rm, bn_rv):
    conv = conv_fn(x, conv_weight, conv_bias)
    bn = F.batch_norm(conv, bn_rm, bn_rv, bn_weight, bn_bias, training=True)
    if has_relu:
        output = F.relu_(bn) if relu_is_inplace else F.relu(bn)
    else:
        output = bn
    return output, {
        "input": x,
        "conv": conv,
        "weight": conv_weight,
        "bias": conv_bias,
        "output": output,
    }


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fake_quantize.py
# Line: 273

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/experimental/adaround_optimization.py
# Line: 17

def __init__(
    self,
    model: Union[torch.nn.Module, torch.nn.DataParallel],
    callback: Callable[
        [
            Union[torch.nn.Module, torch.nn.DataParallel],
            Any,
            Optional[torch.nn.Module],
        ],
        None,
    ],
    forward_hook_wrapper: Callable[[list[torch.Tensor]], Callable],
    data: Any,
    observer: type[torch.ao.quantization.observer.ObserverBase] = MinMaxObserver,
    max_iter=10000,
    dtype: torch.dtype = torch.qint8,
    quant_min=-128,
    quant_max=127,
    qscheme: torch.qscheme = torch.per_tensor_symmetric,
    batch_size: int = 256,
    feed_forward_wrapper: Optional[torch.nn.Module] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/quantize_fx.py
# Line: 92

def _prepare_fx(
    model: torch.nn.Module,
    qconfig_mapping: Union[QConfigMapping, dict[str, Any]],
    is_qat: bool,
    example_inputs: tuple[Any, ...],
    prepare_custom_config: Union[PrepareCustomConfig, dict[str, Any], None] = None,
    _equalization_config: Optional[Union[QConfigMapping, dict[str, Any]]] = None,
    backend_config: Union[BackendConfig, dict[str, Any], None] = None,
    is_standalone_module: bool = False,

# ==================================================
# Line: 513

def _convert_fx(
    graph_module: GraphModule,
    is_reference: bool,
    convert_custom_config: Union[ConvertCustomConfig, dict[str, Any], None] = None,
    is_standalone_module: bool = False,
    _remove_qconfig: bool = True,
    qconfig_mapping: Union[QConfigMapping, dict[str, Any], None] = None,
    backend_config: Union[BackendConfig, dict[str, Any], None] = None,
    is_decomposed: bool = False,
    keep_original_weights: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/observer.py
# Line: 230

def __init__(
    self,
    dtype=torch.quint8,
    qscheme=torch.per_tensor_affine,
    reduce_range=False,
    quant_min=None,
    quant_max=None,
    factory_kwargs=None,
    eps=torch.finfo(torch.float32).eps,
    is_dynamic=False,
    **kwargs,

# ==================================================
# Line: 290

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 500

def __init__(
    self,
    dtype=torch.quint8,
    qscheme=torch.per_tensor_affine,
    reduce_range=False,
    quant_min=None,
    quant_max=None,
    factory_kwargs=None,
    eps=torch.finfo(torch.float32).eps,
    is_dynamic=False,
    **kwargs,

# ==================================================
# Line: 626

def __init__(
    self,
    averaging_constant=0.01,
    dtype=torch.quint8,
    qscheme=torch.per_tensor_affine,
    reduce_range=False,
    quant_min=None,
    quant_max=None,
    eps=torch.finfo(torch.float32).eps,
    is_dynamic=False,
    **kwargs,

# ==================================================
# Line: 710

def __init__(
    self,
    ch_axis=0,
    dtype=torch.quint8,
    qscheme=torch.per_channel_affine,
    reduce_range=False,
    quant_min=None,
    quant_max=None,
    factory_kwargs=None,
    eps=torch.finfo(torch.float32).eps,
    is_dynamic=False,
    **kwargs,

# ==================================================
# Line: 794

def _load_from_state_dict(
    self,
    state_dict: dict[str, Any],
    prefix: str,
    local_metadata: dict[str, torch.Tensor],
    strict: bool,
    missing_keys: list[str],
    unexpected_keys: list[str],
    error_msgs: list[str],

# ==================================================
# Line: 854

def _load_from_state_dict_script(
    self,
    state_dict: dict[str, Any],
    prefix: str,
    local_metadata: dict[str, torch.Tensor],
    strict: bool,
    missing_keys: list[str],
    unexpected_keys: list[str],
    error_msgs: list[str],

# ==================================================
# Line: 916

def __init__(
    self,
    averaging_constant=0.01,
    ch_axis=0,
    dtype=torch.quint8,
    qscheme=torch.per_channel_affine,
    reduce_range=False,
    quant_min=None,
    quant_max=None,
    eps=torch.finfo(torch.float32).eps,
    is_dynamic=False,
    **kwargs,

# ==================================================
# Line: 1007

def __init__(
    self,
    bins: int = 2048,
    dtype: torch.dtype = torch.quint8,
    qscheme=torch.per_tensor_affine,
    reduce_range=False,
    quant_min=None,
    quant_max=None,
    factory_kwargs=None,
    eps=torch.finfo(torch.float32).eps,
    is_dynamic=False,
    **kwargs,

# ==================================================
# Line: 1225

def _combine_histograms(
    self,
    orig_hist: torch.Tensor,
    orig_min: torch.Tensor,
    orig_max: torch.Tensor,
    update_hist: torch.Tensor,
    update_min: torch.Tensor,
    update_max: torch.Tensor,

# ==================================================
# Line: 1359

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 1419

def __init__(
    self,
    scale,
    zero_point,
    dtype=torch.quint8,
    qscheme=torch.per_tensor_affine,
    quant_min=0,
    quant_max=255,
    is_dynamic=False,
    **kwargs,

# ==================================================
# Line: 1473

def __init__(
    self,
    dtype=torch.float32,
    custom_op_name="",
    compute_dtype=None,
    quant_min=None,
    quant_max=None,
    qscheme=None,
    eps=None,
    is_dynamic=False,

# ==================================================
# Line: 1815

def __init__(
    self,
    mapping_type: MappingType,
    target_dtype: torch.dtype,
    granularity: Granularity,
    quant_min: Optional[int] = None,
    quant_max: Optional[int] = None,
    eps: Optional[float] = None,
    scale_dtype: Optional[torch.dtype] = None,
    zero_point_dtype: Optional[torch.dtype] = None,
    preserve_zero: bool = True,
    zero_point_domain: Optional[ZeroPointDomain] = ZeroPointDomain.INT,
    # there could be some extra args that's ignored
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/quantize.py
# Line: 627

def convert(
    module,
    mapping=None,
    inplace=False,
    remove_qconfig=True,
    is_reference=False,
    convert_custom_config_dict=None,
    use_precomputed_fake_quant=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/sparse/quantized/dynamic/linear.py
# Line: 25

def __init__(
    self,
    in_features,
    out_features,
    row_block_size,
    col_block_size,
    bias=True,
    dtype=torch.qint8,

# ==================================================
# Line: 75

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/sparse/quantized/linear.py
# Line: 60

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 109

def __init__(
    self,
    in_features,
    out_features,
    row_block_size,
    col_block_size,
    bias=True,
    dtype=torch.qint8,

# ==================================================
# Line: 168

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/activation.py
# Line: 130

def __init__(
    self,
    scale: float,
    zero_point: int,
    negative_slope: float = 1e-2,
    inplace: bool = False,
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/embedding_ops.py
# Line: 66

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 120

def __init__(
    self,
    num_embeddings: int,
    embedding_dim: int,
    padding_idx: Optional[int] = None,
    max_norm: Optional[float] = None,
    norm_type: float = 2.0,
    scale_grad_by_freq: bool = False,
    sparse: bool = False,
    _weight: Optional[Tensor] = None,
    dtype=torch.quint8,

# ==================================================
# Line: 284

def __init__(
    self,
    num_embeddings: int,
    embedding_dim: int,
    max_norm: Optional[float] = None,
    norm_type: float = 2.0,
    scale_grad_by_freq: bool = False,
    mode: str = "sum",
    sparse: bool = False,
    _weight: Optional[Tensor] = None,
    include_last_offset: bool = False,
    dtype=torch.quint8,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/normalization.py
# Line: 23

def __init__(
    self,
    normalized_shape,
    weight,
    bias,
    scale,
    zero_point,
    eps=1e-5,
    elementwise_affine=True,
    device=None,
    dtype=None,

# ==================================================
# Line: 98

def __init__(
    self,
    num_groups,
    num_channels,
    weight,
    bias,
    scale,
    zero_point,
    eps=1e-5,
    affine=True,
    device=None,
    dtype=None,

# ==================================================
# Line: 157

def __init__(
    self,
    num_features,
    weight,
    bias,
    scale,
    zero_point,
    eps=1e-5,
    momentum=0.1,
    affine=False,
    track_running_stats=False,
    device=None,
    dtype=None,

# ==================================================
# Line: 224

def __init__(
    self,
    num_features,
    weight,
    bias,
    scale,
    zero_point,
    eps=1e-5,
    momentum=0.1,
    affine=False,
    track_running_stats=False,
    device=None,
    dtype=None,

# ==================================================
# Line: 291

def __init__(
    self,
    num_features,
    weight,
    bias,
    scale,
    zero_point,
    eps=1e-5,
    momentum=0.1,
    affine=False,
    track_running_stats=False,
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/functional_modules.py
# Line: 203

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/linear.py
# Line: 77

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 231

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/conv.py
# Line: 40

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 57

def _init(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride,
    padding,
    dilation,
    transposed,
    output_padding,
    groups,
    bias,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 190

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 394

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_1_t,
    stride: _size_1_t = 1,
    padding: _size_1_t = 0,
    dilation: _size_1_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 526

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 655

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 747

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride,
    padding,
    dilation,
    transposed,
    output_padding,
    groups,
    bias,
    padding_mode,
    device=None,
    dtype=None,

# ==================================================
# Line: 917

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    output_padding=0,
    groups=1,
    bias=True,
    dilation=1,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 1040

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    output_padding=0,
    groups=1,
    bias=True,
    dilation=1,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 1165

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    output_padding=0,
    groups=1,
    bias=True,
    dilation=1,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/dynamic/modules/rnn.py
# Line: 68

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 95

def __init__(
    self,
    mode,
    input_size,
    hidden_size,
    num_layers=1,
    bias=True,
    batch_first=False,
    dropout=0.0,
    bidirectional=False,
    dtype=torch.qint8,

# ==================================================
# Line: 287

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 1172

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/dynamic/modules/linear.py
# Line: 77

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/dynamic/modules/conv.py
# Line: 55

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_1_t,
    stride: _size_1_t = 1,
    padding: _size_1_t = 0,
    dilation: _size_1_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,
    reduce_range=True,

# ==================================================
# Line: 140

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 224

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 314

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    output_padding=0,
    groups=1,
    bias=True,
    dilation=1,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 396

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    output_padding=0,
    groups=1,
    bias=True,
    dilation=1,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 478

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    output_padding=0,
    groups=1,
    bias=True,
    dilation=1,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/reference/modules/utils.py
# Line: 161

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 186

def _quantize_weight_decomposed(
    weight: torch.Tensor,
    weight_qscheme: torch.qscheme,
    weight_dtype: torch.dtype,
    weight_scale: torch.Tensor,
    weight_zero_point: torch.Tensor,
    weight_axis: int,
    weight_quant_min: typing.Optional[int],
    weight_quant_max: typing.Optional[int],

# ==================================================
# Line: 248

def _dequantize_weight_decomposed(
    weight: torch.Tensor,
    weight_qscheme: torch.qscheme,
    weight_dtype: torch.dtype,
    weight_scale: torch.Tensor,
    weight_zero_point: torch.Tensor,
    weight_axis: int,
    weight_quant_min: typing.Optional[int],
    weight_quant_max: typing.Optional[int],

# ==================================================
# Line: 333

def _quantize_and_dequantize_weight_decomposed(
    weight: torch.Tensor,
    weight_qscheme: torch.qscheme,
    weight_dtype: torch.dtype,
    weight_scale: torch.Tensor,
    weight_zero_point: torch.Tensor,
    weight_axis_int: int,
    weight_quant_min: typing.Optional[int],
    weight_quant_max: typing.Optional[int],

# ==================================================
# Line: 406

def _save_weight_qparams(
    destination,
    prefix,
    weight_qscheme,
    weight_dtype,
    weight_scale,
    weight_zero_point,
    weight_axis,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/reference/modules/sparse.py
# Line: 22

def __init__(
    self,
    num_embeddings: int,
    embedding_dim: int,
    padding_idx: Optional[int] = None,
    max_norm: Optional[float] = None,
    norm_type: float = 2.0,
    scale_grad_by_freq: bool = False,
    sparse: bool = False,
    _weight: Optional[Tensor] = None,
    device=None,
    dtype=None,
    weight_qparams: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 90

def __init__(
    self,
    num_embeddings: int,
    embedding_dim: int,
    max_norm: Optional[float] = None,
    norm_type: float = 2.0,
    scale_grad_by_freq: bool = False,
    mode: str = "mean",
    sparse: bool = False,
    _weight: Optional[Tensor] = None,
    include_last_offset: bool = False,
    padding_idx: Optional[int] = None,
    device=None,
    dtype=None,
    weight_qparams: Optional[dict[str, Any]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/reference/modules/rnn.py
# Line: 59

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    bias: bool,
    num_chunks: int,
    device=None,
    dtype=None,
    weight_qparams_dict=None,

# ==================================================
# Line: 161

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    bias: bool = True,
    nonlinearity: str = "tanh",
    device=None,
    dtype=None,
    weight_qparams_dict: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 252

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    bias: bool = True,
    device=None,
    dtype=None,
    weight_qparams_dict: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 327

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    bias: bool = True,
    device=None,
    dtype=None,
    weight_qparams_dict: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 394

def __init__(
    self,
    mode: str,
    input_size: int,
    hidden_size: int,
    num_layers: int = 1,
    bias: bool = True,
    batch_first: bool = False,
    dropout: float = 0.0,
    bidirectional: bool = False,
    proj_size: int = 0,
    device=None,
    dtype=None,
    weight_qparams_dict: Optional[dict[str, Any]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/reference/modules/linear.py
# Line: 24

def __init__(
    self,
    in_features: int,
    out_features: int,
    bias_: bool = True,
    device: Optional[torch.device] = None,
    dtype: Optional[torch.dtype] = None,
    weight_qparams: Optional[dict[str, Any]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/reference/modules/conv.py
# Line: 55

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_1_t,
    stride: _size_1_t = 1,
    padding: _size_1_t = 0,
    dilation: _size_1_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,
    weight_qparams: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 118

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,
    weight_qparams: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 181

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,
    weight_qparams: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 274

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_1_t,
    stride: _size_1_t = 1,
    padding: _size_1_t = 0,
    output_padding: _size_1_t = 0,
    groups: int = 1,
    bias: bool = True,
    dilation: _size_1_t = 1,
    padding_mode: str = "zeros",
    device=None,
    dtype=None,
    weight_qparams: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 354

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    output_padding=0,
    groups=1,
    bias=True,
    dilation=1,
    padding_mode="zeros",
    device=None,
    dtype=None,
    weight_qparams: Optional[dict[str, Any]] = None,

# ==================================================
# Line: 435

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    output_padding=0,
    groups=1,
    bias=True,
    dilation=1,
    padding_mode="zeros",
    device=None,
    dtype=None,
    weight_qparams: Optional[dict[str, Any]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/functional.py
# Line: 43

def avg_pool2d(
    input,
    kernel_size,
    stride=None,
    padding=0,
    ceil_mode=False,
    count_include_pad=True,
    divisor_override=None,

# ==================================================
# Line: 89

def avg_pool3d(
    input,
    kernel_size,
    stride=None,
    padding=0,
    ceil_mode=False,
    count_include_pad=True,
    divisor_override=None,

# ==================================================
# Line: 173

def conv1d(
    input,
    weight,
    bias,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    padding_mode="zeros",
    scale=1.0,
    zero_point=0,
    dtype=torch.quint8,

# ==================================================
# Line: 245

def conv2d(
    input,
    weight,
    bias,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    padding_mode="zeros",
    scale=1.0,
    zero_point=0,
    dtype=torch.quint8,

# ==================================================
# Line: 317

def conv3d(
    input,
    weight,
    bias,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    padding_mode="zeros",
    scale=1.0,
    zero_point=0,
    dtype=torch.quint8,

# ==================================================
# Line: 477

def max_pool1d(
    input,
    kernel_size,
    stride=None,
    padding=0,
    dilation=1,
    ceil_mode=False,
    return_indices=False,

# ==================================================
# Line: 508

def max_pool2d(
    input,
    kernel_size,
    stride=None,
    padding=0,
    dilation=1,
    ceil_mode=False,
    return_indices=False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py
# Line: 33

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 114

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 195

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/intrinsic/quantized/modules/conv_add.py
# Line: 24

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# Line: 92

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/intrinsic/qat/modules/linear_fused.py
# Line: 33

def __init__(
    self,
    # Linear args
    in_features,
    out_features,
    bias=True,
    # BatchNorm1d args
    # num_features: out_features
    eps=1e-05,
    momentum=0.1,
    # affine: True
    # track_running_stats: True
    # Args for this module
    freeze_bn=False,
    qconfig=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/intrinsic/qat/modules/conv_fused.py
# Line: 40

def __init__(
    self,
    # ConvNd args
    in_channels,
    out_channels,
    kernel_size,
    stride,
    padding,
    dilation,
    transposed,
    output_padding,
    groups,
    bias,
    padding_mode,
    # BatchNormNd args
    # num_features: out_channels
    eps=1e-05,
    momentum=0.1,
    # affine: True
    # track_running_stats: True
    # Args for this module
    freeze_bn=False,
    qconfig=None,
    dim=2,

# ==================================================
# Line: 308

def _load_from_state_dict(
    self,
    state_dict,
    prefix,
    local_metadata,
    strict,
    missing_keys,
    unexpected_keys,
    error_msgs,

# ==================================================
# Line: 464

def __init__(
    self,
    # Conv1d args
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=None,
    padding_mode="zeros",
    # BatchNorm1d args
    # num_features: out_channels
    eps=1e-05,
    momentum=0.1,
    # affine: True
    # track_running_stats: True
    # Args for this module
    freeze_bn=False,
    qconfig=None,

# ==================================================
# Line: 535

def __init__(
    self,
    # Conv1d args
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=None,
    padding_mode="zeros",
    # BatchNorm1d args
    # num_features: out_channels
    eps=1e-05,
    momentum=0.1,
    # affine: True
    # track_running_stats: True
    # Args for this module
    freeze_bn=False,
    qconfig=None,

# ==================================================
# Line: 598

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    qconfig=None,

# ==================================================
# Line: 661

def __init__(
    self,
    # ConvNd args
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=None,
    padding_mode="zeros",
    # BatchNorm2d args
    # num_features: out_channels
    eps=1e-05,
    momentum=0.1,
    # affine: True
    # track_running_stats: True
    # Args for this module
    freeze_bn=False,
    qconfig=None,

# ==================================================
# Line: 732

def __init__(
    self,
    # Conv2d args
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=None,
    padding_mode="zeros",
    # BatchNorm2d args
    # num_features: out_channels
    eps=1e-05,
    momentum=0.1,
    # affine: True
    # track_running_stats: True
    # Args for this module
    freeze_bn=False,
    qconfig=None,

# ==================================================
# Line: 795

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    qconfig=None,

# ==================================================
# Line: 858

def __init__(
    self,
    # ConvNd args
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=None,
    padding_mode="zeros",
    # BatchNorm3d args
    # num_features: out_channels
    eps=1e-05,
    momentum=0.1,
    # affine: True
    # track_running_stats: True
    # Args for this module
    freeze_bn=False,
    qconfig=None,

# ==================================================
# Line: 928

def __init__(
    self,
    # Conv3d args
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=None,
    padding_mode="zeros",
    # BatchNorm3d args
    # num_features: out_channels
    eps=1e-05,
    momentum=0.1,
    # affine: True
    # track_running_stats: True
    # Args for this module
    freeze_bn=False,
    qconfig=None,

# ==================================================
# Line: 993

def __init__(
    self,
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True,
    padding_mode="zeros",
    qconfig=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/qat/modules/embedding_ops.py
# Line: 28

def __init__(
    self,
    num_embeddings,
    embedding_dim,
    padding_idx=None,
    max_norm=None,
    norm_type=2.0,
    scale_grad_by_freq=False,
    sparse=False,
    _weight=None,
    device=None,
    dtype=None,
    qconfig=None,

# ==================================================
# Line: 142

def __init__(
    self,
    num_embeddings,
    embedding_dim,
    max_norm=None,
    norm_type=2.0,
    scale_grad_by_freq=False,
    mode="mean",
    sparse=False,
    _weight=None,
    include_last_offset=False,
    padding_idx=None,
    qconfig=None,
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/qat/modules/linear.py
# Line: 33

def __init__(
    self,
    in_features,
    out_features,
    bias=True,
    qconfig=None,
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/qat/modules/conv.py
# Line: 17

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: tuple[int, ...],
    stride: tuple[int, ...],
    padding: Union[str, tuple[int, ...]],
    dilation: tuple[int, ...],
    transposed: bool,
    output_padding: tuple[int, ...],
    groups: int,
    bias: bool,
    padding_mode: str,
    qconfig=None,
    device=None,
    dtype=None,

# ==================================================
# Line: 140

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_1_t,
    stride: _size_1_t = 1,
    padding: Union[str, _size_1_t] = 0,
    dilation: _size_1_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    qconfig=None,
    device=None,
    dtype=None,

# ==================================================
# Line: 201

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_2_t,
    stride: _size_2_t = 1,
    padding: Union[str, _size_2_t] = 0,
    dilation: _size_2_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    qconfig=None,
    device=None,
    dtype=None,

# ==================================================
# Line: 265

def __init__(
    self,
    in_channels: int,
    out_channels: int,
    kernel_size: _size_3_t,
    stride: _size_3_t = 1,
    padding: Union[str, _size_3_t] = 0,
    dilation: _size_3_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    qconfig=None,
    device=None,
    dtype=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/qat/dynamic/modules/linear.py
# Line: 26

def __init__(
    self,
    in_features: int,
    out_features: int,
    bias: bool = True,
    qconfig: Optional["QConfig"] = None,
    device: Optional[Union[int, str, torch.device]] = None,
    dtype: Optional[str] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantizable/modules/rnn.py
# Line: 44

def __init__(
    self,
    input_dim: int,
    hidden_dim: int,
    bias: bool = True,
    device=None,
    dtype=None,
    *,
    split_gates=False,

# ==================================================
# Line: 232

def __init__(
    self,
    input_dim: int,
    hidden_dim: int,
    bias: bool = True,
    device=None,
    dtype=None,
    *,
    split_gates=False,

# ==================================================
# Line: 270

def __init__(
    self,
    input_dim: int,
    hidden_dim: int,
    bias: bool = True,
    batch_first: bool = False,
    bidirectional: bool = False,
    device=None,
    dtype=None,
    *,
    split_gates=False,

# ==================================================
# Line: 426

def __init__(
    self,
    input_size: int,
    hidden_size: int,
    num_layers: int = 1,
    bias: bool = True,
    batch_first: bool = False,
    dropout: float = 0.0,
    bidirectional: bool = False,
    device=None,
    dtype=None,
    *,
    split_gates: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantizable/modules/activation.py
# Line: 62

def __init__(
    self,
    embed_dim: int,
    num_heads: int,
    dropout: float = 0.0,
    bias: bool = True,
    add_bias_kv: bool = False,
    add_zero_attn: bool = False,
    kdim: Optional[int] = None,
    vdim: Optional[int] = None,
    batch_first: bool = False,
    device=None,
    dtype=None,

# ==================================================
# Line: 276

def forward(
    self,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    key_padding_mask: Optional[Tensor] = None,
    need_weights: bool = True,
    attn_mask: Optional[Tensor] = None,
    average_attn_weights: bool = True,
    is_causal: bool = False,

# ==================================================
# Line: 344

def _forward_impl(
    self,
    query: Tensor,
    key: Tensor,
    value: Tensor,
    key_padding_mask: Optional[Tensor] = None,
    need_weights: bool = True,
    attn_mask: Optional[Tensor] = None,
    average_attn_weights: bool = True,
    is_causal: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/fx_minifier.py
# Line: 174

def minifier(
    fail_f: fx.GraphModule,
    inps,
    module_fails,
    dump_state: Callable = dump_state,
    *,
    save_dir=None,
    offload_to_disk=False,
    skip_offload=False,
    skip_sanity=False,
    max_granularity=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_activation_checkpointing/graph_info_provider.py
# Line: 21

def __init__(
    self,
    graph_nodes_in_order: list[str],
    graph_edges: list[tuple[str, str]],
    all_recomputable_banned_nodes: list[str],
    all_node_runtimes: Optional[dict[str, float]] = None,
    all_node_memories: Optional[dict[str, float]] = None,
    recorded_knapsack_input_memories: Optional[list[float]] = None,
    recorded_knapsack_input_runtimes: Optional[list[float]] = None,
    joint_graph: Optional[Graph] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_activation_checkpointing/ac_logging_utils.py
# Line: 55

def create_activation_checkpointing_logging_structure_payload(
    joint_graph: Graph,
    joint_graph_node_information: dict[str, Any],
    joint_graph_edges: list[tuple[str, str]],
    all_recomputable_banned_nodes: list[Node],
    expected_runtime: float,
    saved_node_idxs: list[int],
    recomputable_node_idxs: list[int],
    memories_banned_nodes: list[float],
    runtimes_banned_nodes: list[float],
    min_cut_saved_values: list[Node],

# ==================================================
# Line: 87

def create_structured_trace_for_min_cut_info(
    joint_graph: Graph,
    all_recomputable_banned_nodes: list[Node],
    saved_node_idxs: list[int],
    recomputable_node_idxs: list[int],
    expected_runtime: float,
    memories_banned_nodes: list[float],
    runtimes_banned_nodes: list[float],
    min_cut_saved_values: list[Node],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/benchmark_utils.py
# Line: 17

def dump_chrome_trace(
    f,
    input,
    trace_filename,
    optimize_ctx,
    activities,
    num_runs=1,
    devices=None,
    kwargs_for_f=None,
    kwargs_for_profiler=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/vmap.py
# Line: 477

def _flat_vmap(
    func, batch_size, flat_in_dims, flat_args, args_spec, out_dims, randomness, **kwargs

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/aot_autograd.py
# Line: 845

def aot_function(
    fn: Callable,
    fw_compiler: Callable,
    bw_compiler: Optional[Callable] = None,
    partition_fn: Callable = default_partition,
    decompositions: Optional[dict] = None,
    num_params_buffers: int = 0,
    keep_inference_input_mutations: bool = False,
    inference_compiler: Optional[Callable] = None,
    *,
    # Whether or not to trace with dynamic shapes
    dynamic=False,
    enable_log=True,

# ==================================================
# Line: 1085

def aot_module_simplified(
    mod: nn.Module,
    args,
    fw_compiler: AOTDispatchCompiler,
    bw_compiler: Optional[AOTDispatchCompiler] = None,
    partition_fn: Callable = default_partition,
    decompositions: Optional[dict] = None,
    keep_inference_input_mutations=False,
    inference_compiler: Optional[AOTDispatchCompiler] = None,
    cudagraphs: Optional[BoxedBool] = None,
    boxed_forward_device_index: Optional[BoxedDeviceIndex] = None,
    ignore_shape_env: bool = False,

# ==================================================
# Line: 1241

def aot_export_module(
    mod: nn.Module,
    args,
    *,
    decompositions: Optional[dict] = None,
    # If true, we'll return a joint forward-backward graph,
    # As well as metadata on the loss + gradients in the backward.
    trace_joint: bool,
    # If trace_joint is True, we expect your module to return a scalar loss.
    # Your module can return multiple outputs, so you must specify which output the loss is.
    output_loss_index: Optional[int] = None,
    pre_dispatch: bool = False,
    # If None, will be infered from inputs and mod.graph.nodes if mod is a graph module, but the inferred result might be wrong.
    dynamic_shapes: Optional[bool] = None,
    kwargs=None,

# ==================================================
# Line: 1548

def _aot_export_function(
    func: Callable,
    args,
    *,
    num_params_buffers: int = 0,
    decompositions: Optional[dict] = None,
    # If we're exporting a joint graph and we don't want any tangent inputs in the graph
    # (because we are backpropping through a scalar 1 loss),
    # we need to explicitly specify not to include tangents in the graph.
    # It's not enough just to check that our tangent is a scalar, since we also
    # need to know if it is a 1 (no need to make it a graph input), or something else
    # (requiring it to be a graph input).
    # We don't know this info at trace time though, so we need to make it an explicit config.
    no_tangents: bool = False,
    pre_dispatch: bool = False,
    # If None, `dynamic_shapes` will be infered from inputs, but the inferred result might be wrong.
    dynamic_shapes: Optional[bool] = None,
    kwargs=None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/input_output_analysis.py
# Line: 363

def create_graph_signature(
    fx_g: torch.fx.GraphModule,
    fw_metadata: ViewAndMutationMeta,
    in_spec: pytree.TreeSpec,
    out_spec: pytree.TreeSpec,
    *,
    user_args_flat: list[Tensor],
    params_and_buffers_flat: list[Tensor],
    param_names: list[str],
    buffer_names: list[str],
    trace_joint: bool,
    num_user_fw_outs: Optional[int],
    loss_index: Optional[int],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/schemas.py
# Line: 817

def from_tracing_metadata(
    cls,
    *,
    in_spec: pytree.TreeSpec,
    out_spec: pytree.TreeSpec,
    graph_input_names: list[str],
    graph_output_names: list[str],
    view_mutation_metadata: ViewAndMutationMeta,
    named_parameters: list[str],
    named_buffers: list[str],
    num_user_inputs: int,
    num_user_outputs: int,
    loss_index: Optional[int],
    backward_signature: Optional[BackwardSignature],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/autograd_cache.py
# Line: 964

def load(
    dispatch_and_compile: Callable,
    mod: Union[torch.fx.GraphModule, torch._dynamo.utils.GmWrapper],
    args,
    aot_config: AOTConfig,
    cudagraphs: BoxedBool,
    boxed_forward_device_index: Optional[BoxedDeviceIndex],
    local: bool,
    remote: bool,

# ==================================================
# Line: 1246

def make_entry(
    compiled_fw_func: CompiledFxGraph,
    compiled_bw_func: Optional[CompiledFxGraph],
    aot_joint_graph_str: Optional[str],
    aot_forward_graph_str: Optional[str],
    aot_backward_graph_str: Optional[str],
    runtime_metadata: ViewAndMutationMeta,
    dispatch_wrappers: list[CompilerWrapper],
    maybe_subclass_meta: Optional[SubclassMeta],
    num_fw_outs_saved_for_bw: Optional[int],
    indices_of_inps_to_detach: list[int],
    forward_time_taken_ns: int,
    backward_time_taken_ns: int,
    sanitized_aot_config: AOTConfig,
    guards_expr: Optional[str],
    backward_state_indices: Optional[list[int]],
    num_symints_saved_for_bw: Optional[int],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/functional_utils.py
# Line: 487

def _check_if_mutation_can_be_in_graph(
    keep_input_mutations: bool,
    mutates_data,
    mutates_metadata,
    mutations_hidden_from_autograd,
    mutations_under_no_grad_or_inference_mode,
    mutates_storage_metadata,
    mutation_inductor_storage_resize,
    requires_grad,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/runtime_wrappers.py
# Line: 1944

def post_compile(
    compiled_fw_func,  # fw_module after compilation + wrappers
    compiled_bw_func,  # bw_module after compilation + wrappers
    maybe_subclass_meta: Optional[SubclassMeta],
    num_symints_saved_for_bw_: int,
    backward_state_indices: list[int],
    disable_amp: bool,
    indices_of_inps_to_detach: list[int],
    lazy_backward_info: Optional[AutogradLazyBackwardCompileInfo],
    aot_config: AOTConfig,
    *,
    fw_metadata: ViewAndMutationMeta,  # runtime metadata
    try_save_cache_entry: Optional[Callable],  # Save cache entry after compilation

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/partitioners.py
# Line: 1157

def apply_graphsafe_rng_functionalization(
    fw_module: torch.fx.GraphModule,
    bw_module: torch.fx.GraphModule,
    fw_node: torch.fx.Node,
    bw_node: torch.fx.Node,
    device: torch.device,
    rng_count: int,
    last_fwd_input: torch.fx.Node,
    last_bwd_input: torch.fx.Node,

# ==================================================
# Line: 2684

def draw_graph(
    traced: torch.fx.GraphModule,
    fname: str,
    figname: str = "fx_graph",
    clear_meta: bool = True,
    prog: Optional[Union[str, list[str]]] = None,
    parse_stack_trace: bool = False,
    dot_graph_shape: Optional[str] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/hub.py
# Line: 549

def load(
    repo_or_dir,
    model,
    *args,
    source="github",
    trust_repo=None,
    force_reload=False,
    verbose=True,
    skip_validation=False,
    **kwargs,

# ==================================================
# Line: 807

def load_state_dict_from_url(
    url: str,
    model_dir: Optional[str] = None,
    map_location: MAP_LOCATION = None,
    progress: bool = True,
    check_hash: bool = False,
    file_name: Optional[str] = None,
    weights_only: bool = False,

# ==================================================
