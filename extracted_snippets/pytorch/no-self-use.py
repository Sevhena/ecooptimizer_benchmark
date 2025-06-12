# no-self-use snippets for pytorch

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
# Line: 71

def random_multiple_of_128(self, min_num=7, max_num=17):
    ran_pow2 = random.randint(min_num, max_num - 1)
    start = (2**ran_pow2) // 128
    end = (2 ** (ran_pow2 + 1)) // 128
    random_multiple = random.randint(start, end)
    return random_multiple * 128


# ==================================================
# Occurrences: Lines 78-81 (2 instances)

def get_random_pow2(self, min_power2: int, max_power2: int):
    return 2 ** random.randint(min_power2, max_power2)


# ==================================================
# Line: 104

def get_random_num_small(self) -> int:
    pow2 = random.choices([True, False], [0.75, 0.25])[0]
    if pow2:
        return 2 ** random.randint(1, 7)
    else:
        return get_random_between_pow2(1, 7)


# ==================================================
# Line: 131

def get_dtypes(self) -> Any:
    while True:
        dtype_floats = [torch.float16, torch.bfloat16]
        dtype_ints = [torch.int8, torch.uint8]
        mat1_dtype = random.choices(dtype_floats)[0]
        mat2_dtype = random.choices(dtype_ints)[0]
        if mat1_dtype == torch.bfloat16 and mat2_dtype == torch.uint8:
            # this combination seems to cause issues with mixed_mm
            continue
        return (mat1_dtype, mat2_dtype)



# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/mixed_mm/train_decision_mixedmm.py
# Line: 17

def add_new_features(self, results):
    ops = mixed_mm_operations()
    added_categorical_features = []
    for op in ops:
        results[op.name] = results.apply(op.func, axis=1)
        if op.is_categorical:
            added_categorical_features.append(op.name)
    return (results, added_categorical_features)


# ==================================================
# Occurrences: Lines 26-34 (3 instances)

def get_default_config(self, row):
    return "extern_fallback_mixed_mm"


# ==================================================
# Line: 48

def get_grid_search_values(self):
    # A lot of different hyperparameters perform very similar on mixed_mm
    # it is kind of hard to automatically pick one so I just manually picked one with a small max_depth
    return {"max_depth": [5], "min_samples_leaf": [0.01], "criterion": ["entropy"]}



# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train.py
# Occurrences: Lines 101-104 (2 instances)

def filter_df(self, df):
    return df


# ==================================================
# Line: 115

def handle_categorical_features(
    self, cat_feature2cats, categorical_features, results

# ==================================================
# Line: 142

def gen_precondition(self, opt_name, shared_memory, device_capa):
    return f"""    def check_precondition(self, metadata: AHMetadata, context: AHContext,) -> bool:
    return (
        metadata.name == self.get_name()
        and metadata.shared_memory == {shared_memory}
        and str(metadata.device_capa) == "{device_capa}"
    )"""


# ==================================================
# Line: 158

def write_heuristic_to_file(self, lines, heuristic_name):
    output_file = (
        f"../../../torch/_inductor/autoheuristic/artifacts/_{heuristic_name}.py"
    )
    path = f"{output_file}"
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


# ==================================================
# Line: 173

def deserialize_metadata(self, json_string):
    return json.loads(json_string)



# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/ah_tree.py
# Line: 140

def _format_class_prob(self, num: float) -> str:
    if num == 0:
        return "0"
    return f"{num:.2f}"


# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train_decision.py
# Line: 42

def debug_time(self, row, top_k_choices):
    choices_feedback = json.loads(row["choice2time"])
    timings = sorted(choices_feedback.items(), key=lambda x: x[1])
    for choice, time in timings:
        result = f"{choice} {time}"
        if choice in top_k_choices:
            result += " TOPK"
        print(result)


# ==================================================
# Line: 51

def is_unsafe_leaf(self, row, predicted_config, choice2time):
    """
    Can be overridden by subclasses to define their own logic for deciding when a leaf is unsafe. Returns a sample
    that landed in the leaf, the choice predicted by the tree, and a dictionary that maps each choice to the
    execution time. One can for example decide to mark a leaf as unsafe if the predicted choice is 2x slower
    than the fastest choice.
    If a leaf is unsafe, the learned heuristic will always return 'unsure' if an input lands in that leaf.
    """

    return False


# ==================================================
# Line: 87

def get_allowed_wrong_prediction_pct(self):
    """
    This is used to determine a threshold for when a learned heuristic returns 'unsure'.
    If this function returns 0.01, we will set the probability required for the decision tree to return a decision
    such that at most 1% of the predictions will be wrong on the validation set.
    """
    return 0.01


# ==================================================
# Line: 95

def get_grid_search_values(self):
    """
    Standard values for grid search. Can be overriden.
    """
    return {
        "max_depth": [5, 6, 7],
        "min_samples_leaf": [1, 5, 10, 0.01, 0.05, 0.02],
        "criterion": ["gini", "entropy"],
    }


# ==================================================
# Line: 105

def predict(self, model, df, feature_columns):
    """
    Returns the predictions, probabilities, and leaf ids for a given dataframe.
    """
    predictions = model.predict(df[feature_columns])
    proba = model.predict_proba(df[feature_columns])
    leaf_ids = model.apply(df[feature_columns])
    return predictions, proba, leaf_ids


# ==================================================
# Line: 241

def get_test_and_val_size(self):
    """
    Returns the size of the test and validation sets.
    """
    return (0.15, 0.15)


# ==================================================
# Line: 267

def export_to_dot(self, best_model, df, feature_columns):
    """
    Export a learned decision tree to a dot file.
    """
    dot_str = best_model.to_dot()
    with open("best_model.dot", "w") as f:
        f.write(dot_str)


# ==================================================
# Line: 275

def get_feature_columns(self, df):
    """
    The dataframe contains columns that are not features, such as 'winner', 'speedup' that are only used for
    debugging purposes. This function returns the columns that are actually features.
    """
    exclude_columns = [
        "speedup",
        "winner",
        "target",
        "avail_choices",
        "choice2time",
        "index",
        "actual_winner",
        "relative_performance",
    ]
    feature_columns = [col for col in df.columns if col not in exclude_columns]
    return feature_columns


# ==================================================
# Line: 293

def add_training_data(self, df_train, datasets):
    return datasets["train"]


# ==================================================
# Occurrences: Lines 504-507 (2 instances)

def ranking_always_included_choices(self):
    return []


# ==================================================
# Line: 519

def get_default_config(self, row):
    """
    Returns the default config for a given sample. The default config could for example be the config that is
    the chosen by a current handwritten heuristic. This can for example be used in get_unsafe_leaf to
    compare the predicted config with the default config.
    """
    return None


# ==================================================
# Line: 779

def get_time(self, row, choice):
    choices_feedback = json.loads(row["choice2time"])
    return choices_feedback.get(choice, None)


# ==================================================
# Line: 848

def compute_safe_proba(self, num_predictions, wrong_probas, wrong_pct):
    wrong_probas.sort()
    num_wrong = len(wrong_probas)
    allowed_wrong = int(num_predictions * wrong_pct)
    if allowed_wrong >= num_wrong:
        return 0.0
    too_many_wrong = num_wrong - allowed_wrong
    idx = min(too_many_wrong, len(wrong_probas) - 1)
    return wrong_probas[idx]


# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/mm/gen_data_mm.py
# Line: 36

def run_benchmark(
    self,
    m: int,
    k: int,
    n: int,
    dtype: Any,

# ==================================================
# Line: 69

def random_multiple_of_128(self, min_num: int = 7, max_num: int = 17) -> int:
    # generates a random number ran_pow2 between min_num and max_num -1
    # and returns a random multiple of 128 between 2^ran_pow2 and 2^(ran_pow2+1)
    ran_pow2 = random.randint(min_num, max_num - 1)
    start = (2**ran_pow2) // 128
    end = (2 ** (ran_pow2 + 1)) // 128
    random_multiple = random.randint(start, end)
    return random_multiple * 128


# ==================================================
# Line: 78

def get_distr_type(self) -> str:
    # 85%: choose a random multiple of 128 between 2^10 and 2^17
    # 10%: choose a random power of 2 between 2^0 and 2^17
    #  4%: choose a random number between 1 and 131072
    #  1%: choose a random number between 2^i and 2^(i+1) with i in [1, 16]
    return random.choices(
        ["mult_128", "pow2", "uniform", "uniform-between-pow2"],
        [0.85, 0.1, 0.04, 0.01],
    )[0]


# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/mm/train_decision_mm.py
# Line: 19

def add_new_features(self, results):
    ops = mm_operations()
    added_categorical_features = []
    for op in ops:
        results[op.name] = results.apply(op.func, axis=1)
        if op.is_categorical:
            added_categorical_features.append(op.name)
    return (results, added_categorical_features)


# ==================================================
# Occurrences: Lines 28-40 (5 instances)

def get_default_config(self, row):
    return "extern_mm"


# ==================================================
# Line: 58

def ranking_always_included_choices(self):
    return ["extern_mm"]



# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/train_regression.py
# Line: 171

def custom_train_test_split(
    self, df, test_size=0.2, val_size=0.25, random_state=42

# ==================================================
# Line: 292

def evaluate_model(self, model, df, feature_columns, choice_columns, threshold):
    """
    Custom evaluation function that evaluates a learned decision tree.
    """

    def predict_winner(group):
        predictions = model.predict(group[feature_columns + choice_columns])

        # Find the index of the maximum prediction (best choice)
        best_choice_index = np.argmax(predictions)

        # Get the corresponding choice
        predicted_choice = (
            group[choice_columns].iloc[best_choice_index].idxmax().split("_")[-1]
        )

        # Calculate the ratio between the best and second-best prediction
        sorted_predictions = np.sort(predictions)[::-1]
        top_pred_ratio = (
            sorted_predictions[0] / sorted_predictions[1]
            if len(sorted_predictions) > 1
            else np.inf
        )

        # If the best choice is not "significantly" better than the second best choice,
        # the learned heuristic will return "unsure"
        if top_pred_ratio <= threshold:
            predicted_winner = "unsure"
        else:
            predicted_winner = predicted_choice

        actual_winner = group["winner"].iloc[0]
        is_correct = (
            predicted_winner == actual_winner
            if predicted_winner != "unsure"
            else "unsure"
        )

        return pd.Series(
            {
                "predicted_winner": predicted_winner,
                "ratio": top_pred_ratio,
                "actual_winner": actual_winner,
                "is_correct": is_correct,
                "speedup": group["speedup"].iloc[
                    0
                ],  # Speedup is the same for all rows in the group
            }
        )

    results = df.groupby(feature_columns).apply(predict_winner).reset_index()
    correct = (results["is_correct"].eq(True)).sum()
    unsure = (results["is_correct"] == "unsure").sum()
    wrong_results = results[results["is_correct"].eq(False)]
    wrong = len(wrong_results)

    # Calculate max and geometric mean of speedup for wrong predictions
    # Used for debugging purposes
    wrong_speedups = wrong_results["speedup"]
    max_wrong_speedup = wrong_speedups.max() if not wrong_speedups.empty else np.nan
    geo_mean_wrong_speedup = (
        gmean(wrong_speedups) if not wrong_speedups.empty else np.nan
    )
    wrong_max_ratio = wrong_results["ratio"].max()

    total = correct + wrong + unsure
    return {
        "correct": correct,
        "wrong": wrong,
        "unsure": unsure,
        "total": total,
        "max_wrong_speedup": max_wrong_speedup,
        "gman_wrong_speedup": geo_mean_wrong_speedup,
        "wrong_max_ratio": wrong_max_ratio,
    }


# ==================================================
# Line: 426

def handle_leaf(self, tree_, node, indent, unsafe_leaves):
    """
    Generates the code for a leaf node. This is just the value predicted by the regression tree.
    """
    value = tree_.value[node][0][0]
    return f"{indent}return {str(value)}"


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
# Line: 112

def is_aligned(self, dim: int, align_size: int) -> bool:
    return dim % align_size == 0


# ==================================================
# Occurrences: Lines 137-141 (2 instances)

def prepadded(self, p_prepadded: float = 0.2) -> bool:
    # p_prepadded: probability that a tensor is "prepadded", i.e. pad_mm excludes time it takes to pad from benchmarking
    return random.choices([True, False], [p_prepadded, 1 - p_prepadded])[0]


# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/pad_mm/train_regression_pad_mm.py
# Line: 17

def add_new_features(self, results):
    ops = pad_mm_operations()
    for op in ops:
        results[op.name] = results.apply(op.func, axis=1)
    added_categorical_features = [op.name for op in ops if op.is_categorical]
    return (results, added_categorical_features)



# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/pad_mm/train_decision_pad_mm.py
# Line: 17

def add_new_features(self, results):
    ops = pad_mm_operations()
    for op in ops:
        results[op.name] = results.apply(op.func, axis=1)
    added_categorical_features = [op.name for op in ops if op.is_categorical]
    return (results, added_categorical_features)



# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/_autoheuristic/pad_mm/train_pad_mm.py
# Line: 17

def add_new_features(self, results):
    ops = pad_mm_operations()
    for op in ops:
        results[op.name] = results.apply(op.func, axis=1)
    added_categorical_features = [op.name for op in ops if op.is_categorical]
    return (results, added_categorical_features)



# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/utils.py
# Line: 139

def _write_if_changed(self, filename: str | Path, contents: str) -> None:
    file = Path(filename)
    old_contents: str | None = None
    try:
        old_contents = file.read_text(encoding="utf-8")
    except OSError:
        pass
    if contents != old_contents:
        # Create output directory if it doesn't exist
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(contents, encoding="utf-8")


# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/static_runtime/generator.py
# Line: 661

def out_variant_op_generator(
    self, g: NativeFunctionsGroup, backend_index: BackendIndex

# ==================================================
# Line: 686

def view_op_generator(
    self, g: NativeFunctionsViewGroup, backend_index: BackendIndex

# ==================================================
# Line: 727

def out_variant_op_test_case_generator(self, g: NativeFunctionsGroup) -> str:
    schema = g.functional.func
    schema_str = str(schema)
    assert schema_str.find("(") > 0
    type_variant_op_name = schema_str[: schema_str.find("(")].replace(".", "_")
    op_name = op_name_from_group(g)
    assert type_variant_op_name.startswith(op_name)

    arg_types = generate_test_ir_arguments(schema)
    arg_declarations = ", ".join(
        (
            arg_name if arg_type is None else f"{arg_name}: {arg_type}"
            for arg_name, arg_type in arg_types
        )
    )
    arg_names = ", ".join((arg_name for arg_name, _ in arg_types))
    assert (
        len(schema.returns) == 1
        and isinstance(schema.returns[0].type, BaseType)
        and schema.returns[0].type.name is BaseTy.Tensor
    )
    test_value_definitions = generate_test_value_definitions(schema, 0)
    test_value_names = generate_test_value_names(schema, 0)
    test_value_definitions2 = generate_test_value_definitions(schema, 1)
    test_value_names2 = generate_test_value_names(schema, 1)
    check_resize = "true" if should_check_resize(schema) else "false"
    generated = f"""

# ==================================================
# Line: 775

def view_op_test_case_generator(self, g: NativeFunctionsViewGroup) -> str:
    schema = g.view.func
    schema_str = str(schema)
    assert schema_str.find("(") > 0
    type_variant_op_name = schema_str[: schema_str.find("(")].replace(".", "_")
    op_name = g.view.root_name
    assert type_variant_op_name.startswith(op_name)

    arg_types = generate_test_ir_arguments(schema)
    arg_declarations = ", ".join(
        (
            arg_name if arg_type is None else f"{arg_name}: {arg_type}"
            for arg_name, arg_type in arg_types
        )
    )
    arg_names = ", ".join((arg_name for arg_name, _ in arg_types))
    assert (
        len(schema.returns) == 1
        and isinstance(schema.returns[0].type, BaseType)
        and schema.returns[0].type.name is BaseTy.Tensor
    )
    test_value_definitions = generate_test_value_definitions(schema, 0)
    test_value_names = generate_test_value_names(schema, 0)
    generated = f"""

# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/dest/register_dispatch_key.py
# Line: 675

def gen_class_ctor(self, k: SchemaKind, class_name: str, returns: int) -> str:
    if k is SchemaKind.functional:
        return ""
    elif k is SchemaKind.inplace:
        # TODO: Make sure out argument is guaranteed to be self
        return f"{class_name}(Tensor& self) : outputs_{{std::ref(self)}} {{}}"
    elif k is SchemaKind.out:
        out_args = ", ".join(f"Tensor& out{i}" for i in range(returns))
        out_refs = ", ".join(f"std::ref(out{i})" for i in range(returns))
        return f"{class_name}({out_args}) : outputs_{{ {out_refs} }} {{}}"
    elif k is SchemaKind.mutable or k is SchemaKind.scratch:
        raise AssertionError(
            f"{k} structured operators are currently not supported"
        )
    else:
        assert_never(k)


# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/dest/ufunc.py
# Line: 82

def returns_type(self) -> CType:
    # TODO: don't hardcode; return type will be inferred based on tags on
    # the native function
    return BaseCType(scalar_t)


# ==================================================
# File: /root/ecooptimizer/pytorch/torchgen/dest/lazy_ir.py
# Occurrences: Lines 188-194 (3 instances)

def lowering_function(self, schema: LazyIrSchema) -> str:
    return ""


# ==================================================
# File: /root/ecooptimizer/pytorch/setup.py
# Line: 795

def create_compile_commands(self):
    def load(filename):
        with open(filename) as f:
            return json.load(f)

    ninja_files = glob.glob("build/*compile_commands.json")
    cmake_files = glob.glob("torch/lib/build/*/compile_commands.json")
    all_commands = [entry for f in ninja_files + cmake_files for entry in load(f)]

    # cquery does not like c++ compiles that start with gcc.
    # It forgets to include the c++ header directories.
    # We can work around this by replacing the gcc calls that python
    # setup.py generates with g++ calls instead
    for command in all_commands:
        if command["command"].startswith("gcc "):
            command["command"] = "g++ " + command["command"][4:]

    new_contents = json.dumps(all_commands, indent=2)
    contents = ""
    if os.path.exists("compile_commands.json"):
        with open("compile_commands.json") as f:
            contents = f.read()
    if contents != new_contents:
        with open("compile_commands.json", "w") as f:
            f.write(new_contents)



# ==================================================
# Line: 908

def run(self):
    import glob
    import re

    with open(".gitignore") as f:
        ignores = f.read()
        pat = re.compile(r"^#( BEGIN NOT-CLEAN-FILES )?")
        for wildcard in filter(None, ignores.split("\n")):
            match = pat.match(wildcard)
            if match:
                if match.group(1):
                    # Marker is found and stop reading .gitignore.
                    break
                # Ignore lines which begin with '#'.
            else:
                # Don't remove absolute paths from the system
                wildcard = wildcard.lstrip("./")

                for filename in glob.glob(wildcard):
                    try:
                        os.remove(filename)
                    except OSError:
                        shutil.rmtree(filename, ignore_errors=True)



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_python_dispatcher.py
# Line: 119

def _format_line(self, key, kernel):
    return f"{key:<15} {kernel}\n"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_check.py
# Line: 84

def _is_empty_container(self, node: ast.AST, ann_type: str) -> bool:
    if ann_type == "List":
        # Assigning `[]` to a `List` type gives you a Node where
        # value=List(elts=[], ctx=Load())
        if not isinstance(node, ast.List):
            return False
        if node.elts:
            return False
    elif ann_type == "Dict":
        # Assigning `{}` to a `Dict` type gives you a Node where
        # value=Dict(keys=[], values=[])
        if not isinstance(node, ast.Dict):
            return False
        if node.keys:
            return False
    elif ann_type == "Optional":
        # Assigning `None` to an `Optional` type gives you a
        # Node where value=Constant(value=None, kind=None)
        if not isinstance(node, ast.Constant):
            return False
        if node.value:  # type: ignore[attr-defined]
            return False

    return True


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_trace.py
# Line: 1407

def forward(self, *args, **kwargs):
    raise RuntimeError("Trace submodules cannot be called.")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_monkeytype_config.py
# Line: 156

def code_filter(self) -> Optional[CodeFilter]:
    return jit_code_filter


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/jit/_state.py
# Line: 28

def parse_env(self, name, default, true_message, false_message):
    value = os.environ.get(name)
    if value is None:
        return default
    if value.lower() in {"1", "true", "yes"}:
        return True
    elif value.lower() in {"0", "false", "no"}:
        return False
    if value == "1v":
        print(true_message)
        return True
    elif value == "0v":
        print(false_message)
        return False
    raise ValueError(f"Unknown setting of {name}. Try using 0 or 1.")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/wrap.py
# Line: 230

def tag_nodes(self, gmod, is_sac):
    from torch.utils.checkpoint import CheckpointPolicy

    unique_graph_id = next(uid)
    for node in gmod.graph.nodes:
        if node.op in ("call_function", "call_method", "call_module"):
            node.meta["ac_graph_id"] = unique_graph_id
            if is_sac:
                # For selective checkpointing, we will populate this tag later in _CachingTorchDispatchMode.
                node.meta["recompute"] = None
            else:
                # Under vanilla activation checkpointing, all nodes should be recomputed.
                node.meta["recompute"] = CheckpointPolicy.PREFER_RECOMPUTE
    return gmod


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/triton_kernel_wrap.py
# Line: 1826

def store_non_graphable_args(
    self,
    combined_args: dict[str, Any],

# ==================================================
# Line: 1913

def specialize_symbolic(self, arg: Sequence[Any]) -> Any:
    import torch

    # See [Note: Specialize tl.constexpr args in user-defined triton kernels]
    if isinstance(arg, (torch.SymInt, torch.SymBool, torch.SymFloat)):
        return guard_scalar(arg)
    return arg

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_higher_order_ops/base_hop.py
# Line: 85

def _call_CompositeExplicitAutograd(self, subgraph, *operands, **kwargs):
    from torch.utils._python_dispatch import _get_current_dispatch_mode

    mode = _get_current_dispatch_mode()
    assert mode is None, "Mode should never be enabled for CPU/CUDA key"
    return subgraph(*operands)


# ==================================================
# Line: 110

def _call_FakeTensorMode(self, mode, subgraph, *operands, **kwargs):
    # TODO: this should probably route through FakeTensorMode to reuse caching
    with mode:
        return subgraph(*operands)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/__init__.py
# Occurrences: Lines 559-583 (9 instances)

def __pow_by_natural__(self, other) -> "SymInt":
    raise TypeError("type stub not overridden")


# ==================================================
# Occurrences: Lines 703-712 (4 instances)

def __float_pow__(self, other) -> "SymFloat":
    raise TypeError("type stub not overridden")


# ==================================================
# Occurrences: Lines 718-727 (4 instances)

def __sym_max__(self, other):
    raise TypeError("type stub not overridden")


# ==================================================
# Occurrences: Lines 798-801 (2 instances)

def __sym_not__(self) -> "SymBool":
    raise TypeError("type stub not overridden")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/mkldnn/__init__.py
# Line: 97

def is_available(self):
    return is_available()


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/xeon/run_cpu.py
# Line: 272

def add_lib_preload(self, lib_type):
    """Enable TCMalloc/JeMalloc/intel OpenMP."""
    library_paths = []
    if "CONDA_PREFIX" in os.environ:
        library_paths.append(f"{os.environ['CONDA_PREFIX']}/lib")
    if "VIRTUAL_ENV" in os.environ:
        library_paths.append(f"{os.environ['VIRTUAL_ENV']}/lib")

    library_paths += [
        f"{expanduser('~')}/.local/lib",
        "/usr/local/lib",
        "/usr/local/lib64",
        "/usr/lib",
        "/usr/lib64",
    ]

    lib_find = False
    lib_set = False
    for item in os.getenv("LD_PRELOAD", "").split(":"):
        if item.endswith(f"lib{lib_type}.so"):
            lib_set = True
            break
    if not lib_set:
        for lib_path in library_paths:
            library_file = os.path.join(lib_path, f"lib{lib_type}.so")
            matches = glob.glob(library_file)
            if len(matches) > 0:
                ld_preloads = [f"{matches[0]}", os.getenv("LD_PRELOAD", "")]
                os.environ["LD_PRELOAD"] = os.pathsep.join(
                    [p.strip(os.pathsep) for p in ld_preloads if p]
                )
                lib_find = True
                break
    return lib_set or lib_find


# ==================================================
# Line: 307

def is_numactl_available(self):
    numactl_available = False
    try:
        cmd = ["numactl", "-C", "0", "-m", "0", "hostname"]
        r = subprocess.run(
            cmd,
            env=os.environ,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if r.returncode == 0:
            numactl_available = True
    except Exception:
        pass
    return numactl_available


# ==================================================
# Line: 378

def log_env_var(self, env_var_name=""):
    if env_var_name in os.environ:
        logger.info("%s=%s", env_var_name, os.environ[env_var_name])


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/backends/_nnapi/serializer.py
# Line: 685

def get_conv_pool_args_2d_common(
    self, kernel_size, strides, paddings, dilations, group_num

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler_util.py
# Line: 265

def supported_export_stacks_metrics(self):
    return [
        "self_cpu_time_total",
        "self_cuda_time_total",
        "self_xpu_time_total",
        "self_privateuse1_time_total",
    ]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/autograd/profiler.py
# Line: 323

def default_trace_id(self):
    # Generate a UUID
    uuid_raw = uuid.uuid4()

    return f"{uuid_raw.int:032X}"


# ==================================================
# Line: 503

def toggle_collection_dynamic(
    self, enabled: bool, activities: Iterable[ProfilerActivity]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/non_strict_utils.py
# Line: 890

def _override(self, func, args, kwargs):
    if torch.distributed.is_available():
        from torch.distributed._functional_collectives import (
            REDUCE_OP_TO_STR,
            traceable_collective_remaps,
        )

        if func in traceable_collective_remaps:
            # Redirect to a corresponding functional collective, following Dynamo.
            # See torch/distributed/_functional_collectives.py for details.
            # The following is an adaptation of CollectiveFunctionRewriteVariable.
            mapped_func = traceable_collective_remaps[func]
            signature = inspect.signature(func)
            kwargs = dict(signature.bind(*args, **kwargs).arguments)
            args = ()
            if func in (
                torch.distributed.all_reduce,
                torch.distributed.reduce_scatter_tensor,
                torch.distributed._reduce_scatter_base,
            ):
                if "op" in kwargs:
                    kwargs["op"] = REDUCE_OP_TO_STR[kwargs["op"]]
            return mapped_func, args, kwargs
    if func is torch.tensor:
        # Redirect to Python implementation of torch.tensor for data with symints.
        # NOTE(avik): We don't unconditionally redirect to this implementation
        # because it has some known incompletenesses, e.g., it doesn't support
        # empty data. See https://github.com/pytorch/pytorch/issues/143216
        if any(
            isinstance(a, (torch.SymInt, torch.SymFloat, torch.SymBool))
            for a in pytree.tree_flatten(args[0])[0]
        ):
            return torch._refs.tensor, args, kwargs
    if func.__name__ == "__getitem__" and isinstance(args[0], torch.Tensor):

        def rewrite(dim, item):
            # Redirect to torch.select for indexing.
            if isinstance(item, (int, torch.SymInt)):
                return dim, (torch.select, [dim, item])
            # Redirect to torch.ops.aten.slice for slicing.
            if isinstance(item, slice):
                return dim + 1, (
                    torch.ops.aten.slice,
                    [dim, item.start, item.stop, item.step or 1],
                )
            # Otherwise do nothing.

        items = args[1] if isinstance(args[1], tuple) else (args[1],)
        dim = 0
        # Sequence rewrites.
        sequence = []
        for item in items:
            if (r := rewrite(dim, item)) is None:
                return func, args, kwargs
            dim, call_spec = r
            sequence.append(call_spec)

        def run():
            # Run sequence.
            t = args[0]
            for _method, _args in sequence:
                t = _method(t, *_args)
            return t

        return run, [], {}

    return func, args, kwargs


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/verifier.py
# Line: 129

def allowed_builtin_ops(self) -> list:
    return [
        operator.getitem,
        operator.add,
        operator.mul,
        operator.sub,
        operator.truediv,
        operator.ge,
        operator.le,
        operator.gt,
        operator.lt,
        operator.eq,
        operator.ne,
        operator.floordiv,
        operator.mod,
        operator.and_,
        operator.or_,
        operator.not_,
        operator.pow,
        operator.neg,
        operator.abs,
        operator.lshift,
        operator.rshift,
        math.ceil,
        math.floor,
        math.trunc,
        round,
    ]


# ==================================================
# Occurrences: Lines 158-164 (3 instances)

def allowed_op_types(self) -> tuple[type[Any], ...]:
    return (OpOverload, HigherOrderOperator)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/converter.py
# Line: 1131

def _check_set_attr_in_if_block(self, if_node: torch._C.Node):
    for block in if_node.blocks():
        for node in block.nodes():
            if node.kind() == "prim::SetAttr":
                raise RuntimeError(
                    "During converting prim::If to torch.cond, found prim::SetAttr op"
                    " which is not supported yet. Please file an issue if you come "
                    "across this error."
                )


# ==================================================
# Line: 1184

def convert_prim_Enter(self, node: torch._C.Node):
    # export generally treats prim::Enter as noop
    # The only context manager export supports is aten::enable_grad.
    # Unfortunately, TorchScript does not support aten::enable_grad yet.
    # TODO: support aten::enable_grad in both TorchScript and Converter.
    return


# ==================================================
# Line: 1191

def convert_prim_Exit(self, node: torch._C.Node):
    # export treats prim::Exit as noop
    return


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/serde/serialize.py
# Line: 522

def serialize_operator(self, target) -> str:
    if isinstance(target, str):
        return target
    elif target.__module__.startswith("torch._ops"):
        # TODO(zhxchen17) Maybe provide a function name helper in FX.
        # From torch.fx.node._get_qualified_name
        module = target.__module__.replace("torch._ops", "torch.ops")
        return f"{module}.{target.__name__}"
    else:  # TODO(zhxchen17) Don't catch all here.
        return f"{target.__module__}.{target.__name__}"


# ==================================================
# Line: 650

def handle_get_attr(self, node):
    log.debug("[handle_get_attr] %s", node.name)


# ==================================================
# Line: 716

def serialize_script_obj_meta(
    self, script_obj_meta: ep.CustomObjArgument

# ==================================================
# Line: 811

def is_inductor_sym_int_arg(self, arg) -> bool:
    # This is a special branch for handling SymInt args in inductor's
    # ExternalFallbackNode.
    # For regular FX graph, SymInt arg should be a fx.Node and should be
    # verified with is_sym_int_arg()
    return type(arg) is int or isinstance(arg, torch.SymInt)


# ==================================================
# Line: 1565

def serialize_graph_module_metadata(self, meta: dict[str, Any]):
    ret = {}
    if custom := meta.get("custom"):
        log.debug("\n[serialize_graph_module_metadata] %s", custom)
        try:
            ret["custom"] = json.dumps(custom)
        except Exception as e:
            raise SerializeError(
                f"Failed to serialize custom metadata for graph with error {e}"
            ) from e

    return ret


# ==================================================
# Line: 1701

def deserialize_extension_operator(self, serialized_target: str):
    namespace, op_name = serialized_target.split(":")
    namespace = namespace[1:]  # starting with #
    handler = _deserialization_registry[namespace]
    return handler.from_op_name(op_name)


# ==================================================
# Line: 1843

def deserialize_script_obj_meta(
    self, script_obj_meta: CustomObjArgument

# ==================================================
# Line: 2457

def deserialize_constant_input(self, inp: ConstantValue) -> Any:
    if inp.type == "as_int":
        return int(inp.as_int)
    elif inp.type == "as_float":
        return float(inp.as_float)
    elif inp.type == "as_string":
        return str(inp.as_string)
    elif inp.type == "as_bool":
        return bool(inp.as_bool)
    elif inp.type == "as_none":
        return None
    else:
        raise SerializeError(f"Unhandled constant argument {inp} to deserialize")


# ==================================================
# Line: 2786

def deserialize_range_constraints(
    self,
    symbol_name_to_range: dict[str, symbolic_shapes.ValueRanges],
    symbol_name_to_symbol: dict[str, sympy.Symbol],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_export/passes/constant_folding.py
# Line: 65

def is_impure(self, node: torch.fx.Node) -> bool:
    if (
        node.target == torch.ops.prims.convert_element_type.default
        and node.args[0].op == "get_attr"  # type: ignore[union-attr]
        and node.args[0].meta["val"].dtype == torch.int8  # type: ignore[union-attr]
        and node.args[1] == torch.bfloat16
    ):
        # For int8_weight -> dq -> bf16_weight
        return True
    if node.target in [
        torch.ops.quantized_decomposed.dequantize_per_channel.default,
        torch.ops.quantized_decomposed.dequantize_per_tensor.default,
        torch.ops.quantized_decomposed.dequantize_per_tensor.tensor,
        torch.ops.pt2e_quant.dequantize_affine,
    ]:
        # For the pattern fp32_weight -> q -> dq
        # We only folding fp32_weight -> q
        # int8_weight and leave dq in graph to be fused
        return True
    return False


# ==================================================
# Line: 193

def insertable_tensor_check(self, tensor: torch.Tensor) -> bool:
    return True


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/sizevars.py
# Line: 401

def statically_known_power_of_2(self, expr: Expr) -> bool:
    """
    Returns a bool indicating if x is known to be a power of 2.
    """
    return isinstance(expr, sympy.Integer) and is_power_of_2(int(expr))


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codecache.py
# Line: 545

def _reduce_fake_tensor(
    self, t: Tensor

# ==================================================
# Line: 554

def _reduce_tensor(
    self, t: Tensor

# ==================================================
# Line: 588

def _reduce_symint(self, s: SymInt) -> tuple[Callable[[T], T], tuple[str]]:
    """
    Custom reducer to pickle SymInts.
    """
    # For hashing purposes, we only care about the name of the symbol and not the
    # backed value. We evaluate guards stored with a cached graph to ensure a cached
    # entity with SymInt args is safe to reuse.
    return (_ident, (str(s),))


# ==================================================
# Line: 597

def _reduce_unsupported(self, s: Any) -> NoReturn:
    """
    Custom reducer to handle any objects that we don't support and therefore
    raise to bypass caching.
    """
    raise BypassFxGraphCache("Reduce unsupported")


# ==================================================
# Line: 604

def _reduce_graph_module(
    self, gm: torch.fx.GraphModule

# ==================================================
# Line: 894

def _get_custom_pass_detail(
    self, custom_pass: CustomGraphPassType

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fuzzer.py
# Line: 714

def timeout_handler(self, signum: int, frame: Optional[FrameType]) -> None:
    raise TimeoutError("Test execution timed out")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/pattern_matcher.py
# Line: 434

def has_multiple_users(self) -> bool:
    return False


# ==================================================
# Line: 476

def pretty_print(self, pp: PatternPrettyPrinter) -> str:
    return "Ignored()"



# ==================================================
# Line: 931

def _match_from_anchors(
    self, pattern: PatternExpr, ctx: MatchContext

# ==================================================
# Line: 2014

def placeholder(
    self,
    target: str,  # type: ignore[override]
    args: Sequence[Any],
    kwargs: Mapping[str, Any],

# ==================================================
# Line: 2034

def call_function(
    self,
    target: str,  # type: ignore[override]
    args: Sequence[Any],
    kwargs: Mapping[str, Any],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/ir.py
# Line: 567

def get_defining_op(self) -> Optional[Operation]:
    return None


# ==================================================
# Line: 659

def get_device(self) -> Optional[torch.device]:
    return None


# ==================================================
# Line: 667

def has_exceeded_max_reads(self) -> bool:
    return False


# ==================================================
# Line: 700

def has_large_inner_fn(self, threshold: Optional[int] = None) -> bool:
    return False


# ==================================================
# Occurrences: Lines 754-757 (2 instances)

def is_extern(self) -> bool:
    return False


# ==================================================
# Occurrences: Lines 798-801 (2 instances)

def is_extern(self) -> bool:
    return False


# ==================================================
# Occurrences: Lines 819-822 (2 instances)

def get_unbacked_symbol_defs(self) -> OrderedSet[sympy.Symbol]:
    return OrderedSet()


# ==================================================
# Line: 846

def get_workspace_size(self) -> int:
    """
    Gets extra global memory size needed by this buffer.
    Some algorithms (e.g. group gemm) may require extra global memory in the generated code.
    """
    return 0



# ==================================================
# Line: 4097

def get_unbacked_symbol_defs(self) -> OrderedSet[sympy.Symbol]:
    return OrderedSet()


# ==================================================
# Line: 4103

def should_allocate(self) -> bool:
    # Returns False by default.
    return False



# ==================================================
# Occurrences: Lines 4725-4729 (2 instances)

def info_dict(self) -> dict[str, Union[PrimitiveInfoType, list[PrimitiveInfoType]]]:
    """Information returned here is logged to the autotune log file when that is enabled."""
    return {}


# ==================================================
# Line: 6483

def has_side_effects(self) -> bool:
    return True



# ==================================================
# Line: 6732

def has_side_effects(self) -> bool:
    return True


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/compile_worker/subproc_pool.py
# Occurrences: Lines 89-92 (2 instances)

def dumps(self, obj: object) -> bytes:
    return pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_utils.py
# Line: 86

def hash_node(self, node: torch.fx.Node):
    # todo(chilli): Not a great hash function
    return (node, node.target, id(node.args), id(node.kwargs))


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/dependencies.py
# Occurrences: Lines 324-327 (2 instances)

def is_scalar(self) -> bool:
    return False


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
# Line: 436

def triton_config(
    self, num_stages: int, num_warps: int, **kwargs: Any

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/triton_combo_kernel.py
# Line: 486

def select_heuristics(self, sub_kernel: TritonKernel) -> tuple[str, dict[str, int]]:
    size_hints = {
        prefix: next_power_of_2(V.graph.sizevars.size_hint(numel))
        for prefix, numel in sub_kernel.numels.items()
        if not prefix_is_reduction(prefix) or sub_kernel.inside_reduction
    }
    if sub_kernel.persistent_reduction:
        assert sub_kernel.inside_reduction
        heuristics = "persistent_reduction"
    elif sub_kernel.inside_reduction:
        heuristics = "reduction"
    else:
        heuristics = "pointwise"
    return heuristics, size_hints


# ==================================================
# Line: 892

def imports_for_benchmark_kernel(self) -> str:
    return textwrap.dedent(
        """
        from torch._dynamo.testing import rand_strided
        {}
        import torch
    """.format(V.graph.device_ops.import_get_raw_stream_as("get_raw_stream"))
    )


# ==================================================
# Line: 901

def uniquify_block_sizes(
    self, code: IndentedBuffer, num_kernel: int, uniquify: list[str]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cutlass_lib_extensions/gemm_operation_extensions.py
# Line: 79

def instance_template(self):
    return """

# ==================================================
# Line: 90

def emit_block_scale_epilogue_functor(self, operation):
    block_scaled_template = """
    ${epilogue_functor}<
        ${epi_vs},
        ${element_d},
        ${element_accumulator},
        ${element_sfd},
        ${layout_sfd},
        ${element_c},
        ${element_scalar}
    >
    """
    block_scaled_values = {
        "epi_vs": str(operation.ScaleFactorVectorSize),
        "element_d": str(DataTypeTag[operation.D.element]),
        "element_sfd": str(DataTypeTag[operation.ScaleFactorD.element]),
        "layout_sfd": LayoutTag[operation.ScaleFactorD.layout],
        "epilogue_functor": EpilogueFunctor3xTag[
            EpilogueFunctor3x.LinearCombinationBlockScaleFactor
        ],
        "element_accumulator": str(DataTypeTag[operation.accumulator_type()]),
        "element_scalar": str(DataTypeTag[operation.accumulator_type()]),
        "element_c": str(DataTypeTag[operation.C.element]),
    }
    return SubstituteTemplate(block_scaled_template, block_scaled_values)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cuda_cpp_scheduling.py
# Line: 88

def define_kernel(self, src_code: str, node_schedule) -> str:
    wrapper = V.graph.wrapper_code
    if src_code in wrapper.src_to_kernel:
        kernel_name = wrapper.src_to_kernel[src_code]
    else:
        fused_name = (
            get_fused_kernel_name(node_schedule, config.triton.descriptive_names)
            if config.triton.descriptive_names
            else ""
        )

        # use the original src_code as the key
        kernel_hash = hashlib.sha256(src_code.encode("utf-8")).hexdigest()[:8]
        if fused_name == "fused":
            # no EVT kernel, use the original kernel name
            kernel_name = f"cutlass_{kernel_hash}"
        else:
            kernel_name = f"cutlass_{fused_name}_{kernel_hash}"
        wrapper.src_to_kernel[src_code] = kernel_name
        src_code = src_code.replace(str(Placeholder.KERNEL_NAME), kernel_name)

        _, _, kernel_path = get_path(code_hash(src_code), "py")

        compile_wrapper = IndentedBuffer()
        compile_wrapper.writeline("async_compile.cuda(r'''")
        compile_wrapper.splice(src_code, strip=True)
        compile_wrapper.writeline(
            f"''', 'so', aot_compile={str(V.graph.aot_mode)})"
        )

        metadata_comment = f"# kernel path: {kernel_path}"
        origins, detailed_origins = get_kernel_metadata(node_schedule, wrapper)
        metadata_comment += "\n" + origins + "\n" + detailed_origins
        wrapper.define_kernel(
            kernel_name, compile_wrapper.getvalue(), metadata_comment
        )
    return kernel_name


# ==================================================
# Line: 195

def _can_fuse_epilogue_impl(
    self,
    cuda_template_buffer: CUDATemplateBuffer,
    existing_epilogue_nodes: list[BaseSchedulerNode],
    node_to_fuse: BaseSchedulerNode,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cuda_kernel.py
# Line: 401

def dtype(self, node: IRNode) -> Optional[str]:
    """
    Generates code which represents dtype of a given node.
    """

    if node is None:
        return "void"
    return DTYPE_TO_CPP.get(node.get_layout().dtype)


# ==================================================
# Line: 410

def cutlass_dtype(self, node: IRNode, default_dtype="void") -> Optional[str]:
    # Helper method, called into from CUTLASSGemmTemplate
    if node is None:
        return default_dtype
    from torch._inductor.codegen.cuda.cuda_template import CUTLASSTemplate

    return CUTLASSTemplate._DTYPE_TO_CUTLASS[node.get_layout().dtype]


# ==================================================
# Line: 418

def max_valid_index(self, node: IRNode, default=-1):
    # Helper method, called into from CUTLASSGemmTemplate
    if node is None:
        return default
    max_valid_offset = 0
    for i in range(len(node.get_size())):
        max_valid_offset += (node.get_size()[i] - 1) * node.get_stride()[i]
    return max_valid_offset


# ==================================================
# Line: 427

def offset(self, node: IRNode) -> str:
    """
    Generates code which represents offset of a given node.
    """

    if node is None:
        return "0"
    return str(node.get_layout().offset)  # type: ignore[union-attr]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cuda_template.py
# Line: 177

def header(self) -> IndentedBuffer:
    res = IndentedBuffer()
    res.splice(
        """
            #include <exception>
            #include <iostream>
            #include <memory>
            #include <random>
            #include <vector>
        """
    )
    return res


# ==================================================
# Line: 190

def globals(self) -> IndentedBuffer:
    res = IndentedBuffer()
    res.splice(
        """
            // We compile all models with -fvisibility=hidden. Any symbols that need to be
            // exposed in the final shared library must be declared with PT_EXPORT to make
            // them visible.
            #ifdef __GNUC__ // Applies to any compiler with GNU extensions (clang and g++)
            #define PT_EXPORT __attribute__((__visibility__("default")))
            #else
            #ifdef _WIN32
            #define PT_EXPORT __declspec(dllexport)
            #else
            #define PT_EXPORT
            #endif
            #endif
        """
    )
    return res


# ==================================================
# Occurrences: Lines 213-216 (2 instances)

def get_runtime_arg_info(self) -> list[ArgInfo]:
    return []


# ==================================================
# Line: 268

def cute_int(self, int_str: str, var_name: str) -> str:
    res = ""
    if int_str in ("1", "1L"):
        res = "cute::Int<1>{}"
    else:
        res = int_str

    return f"{res} /* {var_name} */"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cuda/cutlass_python_evt.py
# Line: 295

def _stride_compatible(
    self, left: Iterable[sympy.Expr], right: Iterable[sympy.Expr]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/debug_utils.py
# Line: 131

def _get_debug_filtered_kernel_names(self) -> list[str]:
    if config.aot_inductor.filtered_kernel_names is None:
        return []
    return [
        x.strip()
        for x in config.aot_inductor.filtered_kernel_names.lower().split(",")
    ]


# ==================================================
# Line: 188

def codegen_intermediate_tensor_value_save(
    self,
    args_to_save,
    kernel_name,
    before_launch=True,
    arg_signatures: Optional[list[type]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_wrapper_cpu.py
# Line: 630

def codegen_tensor_dtype_var_decl(self, code: IndentedBuffer, name):
    code.writeline(f"int32_t {name}_dtype;")
    code.writeline(
        f"AOTI_TORCH_ERROR_CODE_CHECK(aoti_torch_get_dtype({name}, &{name}_dtype));"
    )


# ==================================================
# Occurrences: Lines 636-642 (3 instances)

def codegen_input_size_var_decl(self, code: IndentedBuffer, name):
    code.writeline(f"auto {name}_size = {name}.sizes();")


# ==================================================
# Line: 2123

def generate_scoped_gil_acquire(self, declarations_before_scope, lines_in_scope):
    scoped_lines = IndentedBuffer()
    for declaration in declarations_before_scope:
        scoped_lines.writeline(declaration)

    scoped_lines.writeline("{")
    with scoped_lines.indent():
        scoped_lines.writeline("py::gil_scoped_acquire acquire;")
        scoped_lines.writelines(lines_in_scope.split("\n"))
    scoped_lines.writelines("}")
    return scoped_lines._lines


# ==================================================
# Line: 2158

def generate_float_value(self, val):
    assert isinstance(val, float)
    if val == float("inf"):
        return "std::numeric_limits<double>::infinity()"
    elif val == float("-inf"):
        return "-std::numeric_limits<double>::infinity()"
    elif math.isnan(val):
        return "std::numeric_limits<double>::quiet_NaN()"
    else:
        return f"{val}"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/rocm/rocm_cpp_scheduling.py
# Line: 41

def define_kernel(self, src_code: str, node_schedule) -> str:
    wrapper = V.graph.wrapper_code
    if src_code in wrapper.src_to_kernel:
        kernel_name = wrapper.src_to_kernel[src_code]
    else:
        fused_name = (
            get_fused_kernel_name(node_schedule, config.triton.descriptive_names)
            if config.triton.descriptive_names
            else ""
        )
        kernel_name = "_".join(["rocm", fused_name, wrapper.next_kernel_suffix()])
        # use the original src_code as the key
        wrapper.src_to_kernel[src_code] = kernel_name
        src_code = src_code.replace("KERNEL_NAME", kernel_name)

        _, _, kernel_path = get_path(code_hash(src_code), "py")

        compile_wrapper = IndentedBuffer()
        compile_wrapper.writeline("async_compile.rocm(r'''")
        compile_wrapper.splice(src_code, strip=True)
        compile_wrapper.writeline(
            f"''', 'so', aot_compile={str(V.graph.aot_mode)})"
        )

        metadata_comment = f"# kernel path: {kernel_path}"
        origins, detailed_origins = get_kernel_metadata(node_schedule, wrapper)
        metadata_comment += "\n" + origins + "\n" + detailed_origins
        wrapper.define_kernel(
            kernel_name, compile_wrapper.getvalue(), metadata_comment
        )
    return kernel_name


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/rocm/rocm_template.py
# Line: 152

def header(self) -> IndentedBuffer:
    res = IndentedBuffer()
    res.splice(
        """
            #include <exception>
            #include <iostream>
            #include <memory>
            #include <random>
            #include <vector>
        """
    )
    return res


# ==================================================
# Line: 165

def globals(self) -> IndentedBuffer:
    res = IndentedBuffer()
    res.splice(
        """
            // We compile all models with -fvisibility=hidden. Any symbols that need to be
            // exposed in the final shared library must be declared with PT_EXPORT to make
            // them visible.
            #ifdef __GNUC__ // Applies to any compiler with GNU extensions (clang and g++)
            #define PT_EXPORT __attribute__((__visibility__("default")))
            #else
            #ifdef _WIN32
            #define PT_EXPORT __declspec(dllexport)
            #else
            #define PT_EXPORT
            #endif
            #endif
        """
    )
    return res


# ==================================================
# Occurrences: Lines 188-191 (2 instances)

def get_runtime_arg_info(self) -> list[ArgInfo]:
    return []


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/rocm/ck_tile_universal_gemm_template.py
# Line: 540

def check_warp_tiles(self, op: "CKTileGemmOperation"):
    if op.tile_m % (op.warp_m * op.warp_tile_m) != 0:
        return False
    if op.tile_n % (op.warp_n * op.warp_tile_n) != 0:
        return False
    if op.tile_k % (op.warp_k * op.warp_tile_k) != 0:
        return False
    return True


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/rocm/ck_universal_gemm_template.py
# Line: 383

def inline_utils(self):
    res = IndentedBuffer()
    res.splice(
        """
            #include "host_tensor.cpp"
            #include "device_memory.cpp"
        """
    )
    return res


# ==================================================
# Line: 393

def _has_padding(self, dimension, gemm_specialization):
    # Get the relevant padding map for the given dimension
    dimension_padding = padding_lookup.get(dimension, {})

    # Check if the specialization is in the dimension's padding map
    return dimension_padding.get(gemm_specialization, False)


# ==================================================
# Line: 537

def _prefetch_stages(self, op, a_dtype_size, b_dtype_size, warp_size: int = 64):
    version_str = op.block_gemm_pipeline_version.split("::")[-1]
    try:
        version = int(version_str[1:])  # Assuming the format is always 'vX'
    except ValueError as e:
        raise ValueError(f"Invalid version string: {version_str}") from e
    if version not in [1, 2, 3, 4, 5]:
        raise ValueError(
            f"unknown prefetch stages for {op.block_gemm_pipeline_version}"
        )
    # Define the mapping of versions to stages
    version_to_stages = {1: 1, 3: 2, 4: 4, 5: 3}
    # Get the stages for the given version
    stages = version_to_stages.get(version, None)
    if stages is None:
        # This means we're at stage 2, and this requires computation
        # See github.com/ROCm/composable_kernel/blob/d6a4605/include/ck/tensor_operation/gpu/block/blockwise_gemm_pipeline_xdlops_v2.hpp#L143 # noqa: B950
        wgp_per_cu = max(4 * warp_size // op.block_size, 1)
        full_mem_band_prefetch_stages = math.ceil(
            32768
            / wgp_per_cu
            / (
                (op.m_per_block * a_dtype_size + op.n_per_block * b_dtype_size)
                * op.k_per_block
            )
        )
        stages = min(max(full_mem_band_prefetch_stages, 2), 8)

    return stages


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp.py
# Line: 516

def check_outer_fusion_loop_level_attr(
    self, cpp_kernel_proxy_list, outer_loop_fusion_depth

# ==================================================
# Line: 2096

def _gen_reduction_prefix(
    self,
    acc: Union[CSEVariable, str],
    acc_type: str,
    rtype: str,
    dtype: torch.dtype,
    init_fn,

# ==================================================
# Line: 2393

def get_to_dtype_expr(self, src, dtype, src_dtype):
    return f"c10::convert<{DTYPE_TO_CPP[dtype]}>({src})"


# ==================================================
# Line: 3751

def _select_tiling_indices(
    self,
    fn_list,
    var_sizes_list,
    tiling_factor,

# ==================================================
# Line: 3809

def data_type_propagation(self, nodes):
    for _node in nodes:
        assert isinstance(_node, SchedulerNode)
        DataTypePropagation.propagate_scheduler_node(_node)


# ==================================================
# Line: 3815

def is_lowp_fp_scheduler(self, scheduler_node: SchedulerNode):
    if not isinstance(scheduler_node._body, LoopBody):
        return True
    # Propagate the dtype to check if all the fx node is bf16/fp16
    DataTypePropagation.propagate_scheduler_node(scheduler_node)
    return (
        get_loop_body_lowp_fp(scheduler_node._body)[0] is not None
        and not get_loop_body_lowp_fp(scheduler_node._body)[1]
    )


# ==================================================
# Line: 3825

def legalize_lowp_fp_dtype_loopbody(self, loop_body: LoopBody):
    def add_to_dtype(sub_graph: torch.fx.Graph):
        def get_input_dtype(node: torch.fx.Node) -> Optional[torch.dtype]:
            """Get input dtype for nodes that may consumes lowp fp dt"""
            if node.target == "store":
                return V.graph.get_dtype(node.args[1])  # type: ignore[arg-type]
            elif node.target == "to_dtype_bitcast":
                return node.args[-1]  # type: ignore[return-value]
            elif node.target == "to_dtype":
                if len(node.args) > 3:
                    return node.args[3]  # type: ignore[return-value]
                else:
                    return node.kwargs.get("src_dtype", None)  # type: ignore[return-value]
            else:
                return None

        def get_output_dtype(node: torch.fx.Node) -> Optional[torch.dtype]:
            """Get output dtype for nodes that may produce lowp fp dt"""
            if node.target == "load":
                assert len(node.args) == 3
                return V.graph.get_dtype(node.args[1])  # type: ignore[arg-type]
            elif node.target in ["to_dtype", "constant", "index_expr"]:
                return node.args[-1]  # type: ignore[return-value]
            elif node.target == "to_dtype_bitcast":
                return node.args[2]  # type: ignore[return-value]
            else:
                return None

        def is_lowp_fp_source(node: torch.fx.Node, dt: torch.dtype):
            """Check if the given node produces output with expected low precision floating point data type."""
            assert dt in DTYPE_LOWP_FP
            return get_output_dtype(node) == dt

        def is_lowp_fp_sink(node: torch.fx.Node, dt: torch.dtype):
            """Check if the given node accept input with expected low precision floating point data type."""
            assert dt in DTYPE_LOWP_FP
            if input_dtype := get_input_dtype(node):
                return input_dtype == dt
            elif node.target == "to_dtype":
                # The `src_dtype` of a `to_dtype` node might miss, in which case the node accept any input dtype.
                return True
            else:
                return False

        def is_lowp_fp_source_no_promote(node: torch.fx.Node, dt: torch.dtype):
            """Check if the node is a lowp fp sources which are all directly fed to ops that accepts lowp fp input
            thus no need to promote to float
            """
            return is_lowp_fp_source(node, dt) and all(
                is_lowp_fp_sink(user, dt) for user in node.users
            )

        sub_graph_nodes = list(sub_graph.nodes)
        to_lowp_fp_legalized_nodes = []
        for _node in sub_graph_nodes:
            if (
                _node.target in ["load", "index_expr"]
                and (dt := get_output_dtype(_node)) in DTYPE_LOWP_FP
            ):
                # No need to promote to float if all users are ops that accepts lowp fp input
                if all(is_lowp_fp_sink(user, dt) for user in _node.users):
                    continue
                ops = _node.args[0]
                with sub_graph.inserting_after(_node):
                    to_type_node = sub_graph.call_method(
                        "to_dtype", args=(ops, _node, torch.float)
                    )
                    _node.replace_all_uses_with(
                        to_type_node, lambda n: n is not to_type_node
                    )
                    metrics.cpp_to_dtype_count += 1
            elif (
                _node.target == "store"
                and (dt := get_input_dtype(_node)) in DTYPE_LOWP_FP
            ):
                ops, name, _, value_var, _ = _node.args
                if is_lowp_fp_source_no_promote(value_var, dt):
                    continue
                dtype = V.graph.get_dtype(name)
                with sub_graph.inserting_before(_node):
                    to_type_node = sub_graph.call_method(
                        "to_dtype", args=(ops, value_var, dtype)
                    )
                    _node.replace_input_with(value_var, to_type_node)
                    metrics.cpp_to_dtype_count += 1
            elif _node.target == "reduction":
                (
                    ops,
                    dtype,
                    src_dtype,
                    reduction_type,
                    value,
                ) = _node.args
                if src_dtype in DTYPE_LOWP_FP:
                    # Since we always convert the load/store value to float if the tensor is bfloat16/float16.
                    # Therefore, the reduction should never work with bfloat16/float16 value. Hence, we update
                    # the bfloat16/float16 reduction by
                    #     1) updating the src_dtype to float
                    # and 2) updating the dtype to float if it is bfloat16/float16.
                    assert dtype in [
                        torch.float,
                        torch.bfloat16,
                        torch.float16,
                        torch.int64,
                    ]
                    _node.args = (
                        ops,
                        torch.float if dtype in DTYPE_LOWP_FP else dtype,
                        torch.float,
                        reduction_type,
                        value,
                    )
            elif _node.target == "constant" and _node.args[-1] in DTYPE_LOWP_FP:
                # No need to promote to float if all users are ops that accepts lowp fp input
                (ops, value, dt) = _node.args
                if all(is_lowp_fp_sink(user, dt) for user in _node.users):  # type: ignore[arg-type]
                    continue
                _node.args = (ops, value, torch.float)
            elif _node.target == "to_dtype" and _node.args[-1] in DTYPE_LOWP_FP:
                # No need to promote to float if all users are ops that accepts lowp fp input
                (ops, x, dt) = _node.args
                if all(is_lowp_fp_sink(user, dt) for user in _node.users):  # type: ignore[arg-type]
                    continue
                # The legalization always loads the BF16/FP16 tensor as FP32 for computation
                # and converts back to BF16/FP16 after the computation.
                # Hence, there should be no computation w/ BF16/FP16.
                # Therefore, we update the to_dtype by replacing the bf16/fp16 dtype with fp32.
                # Save the legalized to_dtype node for the elimination(eliminate_to_dtype step):
                #  1) Eliminate the redundant to_dtype node if we have a pattern as follows:
                #     graph():
                #       %lowp_fp_legalized = call_method[target=to_dtype](args = (%ops, %input, torch.float))
                #       %to_dtype2 = call_method[target=to_dtype](args = (%ops, %lowp_fp_legalized, torch.bfloat16/float16))
                # Regarding the first to_dtype, it is redundant because
                # the second to_type also converts to the torch.bfloat16/torch.float16.
                # Hence, we remove the first to_type.
                to_lowp_fp_legalized_nodes.append(_node)
                _node.args = (ops, x, torch.float)
            elif _node.target == "to_dtype_bitcast":
                (ops, value_var, dtype, src_dtype) = _node.args

                # to_dtype_bitcast act as a lowp fp sink:
                # c10::bit_cast requires the source and target have the same bitwidth. Because the input tensor's
                # dtype could be promoted, e.g. from float16 to float, we have to cast the tensor to its original
                # source dtype before invoking bit_cast.
                if src_dtype in DTYPE_LOWP_FP:
                    # No need to promote to float if it is a user of a lowp fp sources
                    # which are all directly fed to ops that accepts lowp fp input
                    if not is_lowp_fp_source_no_promote(value_var, src_dtype):
                        with sub_graph.inserting_before(_node):
                            to_type_node = sub_graph.call_method(
                                "to_dtype", args=(ops, value_var, src_dtype)
                            )
                            _node.replace_input_with(value_var, to_type_node)
                            metrics.cpp_to_dtype_count += 1

                # to_dtype_bitcast act as a lowp fp source:
                # We also need to convert the bit-casted tensor back to float to make sure we keep using higher
                # precision values for the rest of the computation.
                if dtype in DTYPE_LOWP_FP:
                    # No need to promote to float if all users are ops that accepts lowp fp input
                    if not (
                        all(is_lowp_fp_sink(user, dtype) for user in _node.users)
                    ):
                        ops = _node.args[0]
                        with sub_graph.inserting_after(_node):
                            to_type_node = sub_graph.call_method(
                                "to_dtype", args=(ops, _node, torch.float)
                            )
                            _node.replace_all_uses_with(
                                to_type_node, lambda n: n is not to_type_node
                            )
                            metrics.cpp_to_dtype_count += 1
            else:
                pass

        def eliminate_to_dtype(sub_graph: torch.fx.Graph):
            def _eliminate_duplicate_to_node(sub_graph: torch.fx.Graph):
                # Eliminate the redundant to_dtype node. Let's consider a pattern as follows:
                #   graph():
                #     %to_dtype1 = call_method[target=to_dtype](args = (%ops, %input, torch.float), kwargs = {})
                #     %to_dtype2 = call_method[target=to_dtype](args = (%ops, %to_dtype1, torch.float), kwargs = {})
                # Regarding the first to_dtype, it is redundant because the second to_type also converts to the
                # torch.float. Hence, we remove the first to_type
                def _used_by_to(to_node: torch.fx.Node):
                    return all(usr.target == "to_dtype" for usr in to_node.users)

                all_to_nodes = [
                    node for node in sub_graph.nodes if node.target == "to_dtype"
                ]
                all_to_nodes_and_users = [
                    {node: node.users} for node in all_to_nodes if _used_by_to(node)
                ]
                for node_users in all_to_nodes_and_users:
                    for node, users in node_users.items():
                        if node in sub_graph.nodes and (
                            all(usr.args[-1] == node.args[-1] for usr in users)
                            or (
                                node in to_lowp_fp_legalized_nodes
                                and all(
                                    usr.args[-1] in DTYPE_LOWP_FP for usr in users
                                )
                            )
                        ):
                            val_node = node.all_input_nodes[-1]
                            node.replace_all_uses_with(val_node)
                            sub_graph.erase_node(node)

                # For debug mode, the graph of LoopBody will attach a new GraphModule as
                # owning_module for debugging while the release mode will not. The lint will
                # check whether the graph has owning_module to decide if it needs to check
                # call_module. LoopBody might contain get_index as a module call. But it
                # is just a function. Hence, it cannot pass the lint check for debug mode.
                # We bypass the check if the owning_module is None. Eventually, we should call
                # get_index via call_function but not call_module.
                if sub_graph.owning_module is None:
                    sub_graph.lint()

            _eliminate_duplicate_to_node(sub_graph)

        eliminate_to_dtype(sub_graph)

    sub_blocks = [loop_body.root_block] + list(loop_body.subblocks.values())
    for sub_block in sub_blocks:
        add_to_dtype(sub_block.graph)


# ==================================================
# Line: 4569

def _can_fuse_nodes_with_compatible_ranges(self, node1, node2):
    # Here we try to fuse SchedulerNode/FusedSchedulerNode with compatible ranges
    # e.g. (s0, s1, s2) and (s0 * s1 * s2)
    _, (vars1, reduce1) = node1.group
    _, (vars2, reduce2) = node2.group

    c1 = reduce1 == () and reduce2 == ()
    c2 = math.prod(vars1) == math.prod(vars2)
    c3 = len(vars1) == 1 or len(vars2) == 1
    if not (c1 and c2 and c3):
        return False

    node_to_recomp = node1 if len(vars1) < len(vars2) else node2
    ref_node = node2 if len(vars1) < len(vars2) else node1

    # We can not recompute sizes and body for nodes other than SchedulerNode
    # TODO: we can extend fusion support with compatible ranges for FusedSchedulerNode
    if isinstance(node_to_recomp, FusedSchedulerNode):
        return False

    # It may happen that node1 and node2 compatible number of elements
    # but different original ranges, for example:
    # {d0: s0, d1: s1, d2: s2} vs {d0: s0*s1*s2}
    # See https://github.com/pytorch/pytorch/pull/120077/files#r1500427848 for more details
    # TODO: we can fix if it allows us to CSE at least one of the variables

    assert isinstance(node_to_recomp, SchedulerNode)
    if isinstance(node_to_recomp.node, ir.TemplateBuffer):
        return False
    assert isinstance(node_to_recomp.node, ir.ComputedBuffer)
    # node.data.get_size() is a cheaper version of node.get_read_writes().var_ranges
    # but without variable name
    ranges2 = node_to_recomp.node.data.get_size()
    ranges1 = None
    if isinstance(ref_node, FusedSchedulerNode):
        ranges_set = OrderedSet[tuple[Any, ...]]()
        for snode in ref_node.snodes:
            if isinstance(snode.node, ir.TemplateBuffer):
                break
            assert isinstance(snode.node, ir.ComputedBuffer)
            ranges_set.add(tuple(snode.node.data.get_size()))

        if len(ranges_set) != 1:
            return False

        ranges1 = list(next(iter(ranges_set)))
    else:
        assert isinstance(ref_node, SchedulerNode)
        assert isinstance(ref_node.node, ir.ComputedBuffer)
        ranges1 = ref_node.node.data.get_size()  # type: ignore[assignment]

    if ranges1 != ranges2:
        return False

    return True


# ==================================================
# Line: 4657

def _get_outer_loop_fusion_depth(self, node1, node2):
    DISABLE_OUTER_LOOP_FUSION = 0
    if not all(
        type(node)
        in (OuterLoopFusedSchedulerNode, FusedSchedulerNode, SchedulerNode)
        for node in (node1, node2)
    ):
        return DISABLE_OUTER_LOOP_FUSION

    _node1 = (
        node1.get_outer_nodes()[-1]
        if isinstance(node1, OuterLoopFusedSchedulerNode)
        else node1
    )
    assert isinstance(_node1, (FusedSchedulerNode, SchedulerNode))
    _node2 = (
        node2.get_outer_nodes()[0]
        if isinstance(node2, OuterLoopFusedSchedulerNode)
        else node2
    )
    assert isinstance(_node2, (FusedSchedulerNode, SchedulerNode))

    _, (vars1, reduce1) = _node1.group
    _, (vars2, reduce2) = _node2.group
    if vars1 == () and vars2 == () and reduce1 != () and reduce2 != ():
        # Reduction only
        return DISABLE_OUTER_LOOP_FUSION
    if all(type(node) is OuterLoopFusedSchedulerNode for node in (node1, node2)):
        return (
            node1.outer_loop_fusion_depth
            if node1.outer_loop_fusion_depth == node2.outer_loop_fusion_depth
            else DISABLE_OUTER_LOOP_FUSION
        )
    outer_loop_fusion_depth = min(len(vars1), len(vars2))
    if (
        outer_loop_fusion_depth >= 1
        and vars1[:outer_loop_fusion_depth] == vars2[:outer_loop_fusion_depth]
    ):
        if any(
            type(node) is OuterLoopFusedSchedulerNode for node in (node1, node2)
        ):
            _compare_node = (
                node1 if type(node1) is OuterLoopFusedSchedulerNode else node2
            )
            if _compare_node.outer_loop_fusion_depth == outer_loop_fusion_depth:
                # Same outer loop fusion depth as prev nodes in OuterLoopFusedSchedulerNode
                return outer_loop_fusion_depth
            else:
                return DISABLE_OUTER_LOOP_FUSION
        else:
            # First 2 nodes to generate OuterLoopFusedSchedulerNode
            return outer_loop_fusion_depth
    return DISABLE_OUTER_LOOP_FUSION


# ==================================================
# Line: 4743

def try_loop_split(self, nodes: list[SchedulerNode]):
    """
    Apply loop split optimization.
    When one of the indexing_exprs contains a division, we eliminate the division by splitting the loop
    to avoid non-contiguous loads, subject to the following conditions:
        1. No reduction and no mudular index for all nodes.
        2. The indexing_exprs of all nodes contain only one (or more, but all the same) division,
           where the divisor is an integer and not too small (the divisor > 8), the dividend is
           one of the iter_vars, and this var, i.e. the dimension that needs to be split, is
           contiguous in all other indexing_exprs.

    For example, if the node's var_ranges: {z0: 2, z1: 9216, z2: 960} and indexing_exprs:
    {'index0': 8847360*z0 + 960*z1 + z2, 'index1': 32*z0 + (z2//30), 'index2': z2},
    we will split z2 -> 30*z2 + z3, then the node's var_ranges will be changed to
    {z0: 2, z1: 9216, z2: 32, z3: 30} and indexing_exprs will be changed to
    {'index0': 8847360*z0 + 960*z1 + 30*z2 + z3, 'index1': 32*z0 + z2, 'index2': 30*z2 + z3}.
    """

    # No reduction and no mudular
    if any(
        len(node.group[1][1]) != 0
        or any(
            expr.has(ModularIndexing) for expr in node._body.indexing_exprs.values()
        )
        for node in nodes
    ):
        return nodes

    split_var = None
    split_number = None
    num_div = 0
    div_expr_ = None
    match_div = False
    matched_node = None

    for node in nodes:
        assert isinstance(node.node, ir.ComputedBuffer)
        _, original_body, _ = node.node.get_default_sizes_body()
        for name, expr in original_body.indexing_exprs.items():
            if not isinstance(expr, sympy.Expr):
                continue
            for div_expr in expr.find(FloorDiv):
                if (
                    any(div_expr.has(var) for var in original_body.iter_vars)
                    and div_expr != div_expr_
                ):
                    div_expr_ = div_expr
                    num_div += 1
                if num_div > 1:
                    return nodes
                if (
                    isinstance(div_expr.args[1], sympy.core.numbers.Integer)
                    and div_expr.args[0] in original_body.iter_vars
                    and name is not None
                    and all(
                        stride_at_vec_range(expr_, div_expr.args[0]) in (0, 1)
                        for name_, expr_ in original_body.indexing_exprs.items()
                        if name_ != name
                    )
                    and div_expr.args[1] > 8
                ):
                    split_var = div_expr.args[0]
                    split_number = div_expr.args[1]
                    match_div = True
                    matched_node = node

    # Only one node contains a division, and the split dimension is contiguous in all other indexing_exprs.
    if not match_div:
        return nodes

    extra_indexing_constraints = None

    def loop_split(sizes, body, vars):
        index_size, reduce_size = sizes
        index_vars, reduce_vars = vars
        split_idx = index_vars.index(split_var)
        new_index_size = index_size.copy()
        new_index_size[split_idx] = index_size[split_idx] // split_number
        new_index_size.insert(split_idx + 1, split_number)
        (new_index_vars, _), var_ranges = dependencies.index_vars_no_squeeze(
            new_index_size, reduce_size, prefix="y"
        )
        iter_vars = new_index_vars.copy()
        divisor_var = iter_vars.pop(split_idx + 1)
        iter_vars[split_idx] = split_number * iter_vars[split_idx] + divisor_var
        body = ir.LoopBody(
            body, [iter_vars, reduce_vars], var_ranges, new_index_vars, reduce_vars
        )
        nonlocal extra_indexing_constraints
        if not extra_indexing_constraints:
            extra_indexing_constraints = (
                body.var_ranges,
                list(body.indexing_exprs.values()),
            )
        return (
            (new_index_size, reduce_size),
            body,
            (new_index_vars, reduce_vars),
        )

    # Here decide the final loop order
    for node in nodes:
        if node == matched_node:
            node.recompute_size_and_body(recompute_sizes_body_func=loop_split)
    for node in nodes:
        if node != matched_node:
            node.recompute_size_and_body(
                extra_indexing_constraints=extra_indexing_constraints,
                recompute_sizes_body_func=loop_split,
            )

    return nodes


# ==================================================
# Line: 5070

def is_cpp_template(self, node: BaseSchedulerNode) -> bool:
    return isinstance(node, SchedulerNode) and isinstance(
        node.node, ir.CppTemplateBuffer
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/halide.py
# Line: 1048

def apply_offset_to_dimension(self, dims, offset):
    if offset == 0:
        return
    for i in reversed(range(len(dims))):
        if dims[i].stride == 1 or V.graph.sizevars.statically_known_geq(
            offset, dims[i].stride
        ):
            part = FloorDiv(offset, dims[i].stride)
            offset -= part * dims[i].stride
            dims[i].expr += part
    assert offset == 0


# ==================================================
# Line: 1095

def make_index_str(self, dims, replacements=None, zero_vars=False):
    index_str = ", ".join(d.index_str(replacements, zero_vars) for d in dims)
    if len(dims) == 0:
        index_str = "()"
    elif len(dims) == 1:
        # workaround for https://github.com/halide/Halide/issues/8299
        index_str = f"{index_str},"
    return index_str


# ==================================================
# Line: 1371

def halide_buffer_numel(self, name: str):
    """
    We map all tensors to 1D buffers in Halide since Halide has trouble representing some strides that PyTorch
    supports.  If there are gaps in the underlying layout the numel we pass to Halide includes the gaps while
    PyTorch's numel excludes them.
    """
    return V.graph.get_buffer(name).get_layout().storage_size()


# ==================================================
# Line: 1647

def generate_assert(self, check):
    return False  # TODO(jansel): support asserts


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_wrapper_gpu.py
# Line: 146

def generate_grid(
    self,
    prefix: IndentedBuffer,
    inductor_meta: dict[str, Any],
    params: dict[str, Any],

# ==================================================
# Line: 166

def generate_load_kernel(self, prefix, kernel_var_name, params):
    prefix.writeline(f"if ({kernel_var_name} == nullptr) {{")
    with prefix.indent():
        embed_kernel_args = [f"__{params['inductor_meta']['kernel_name']}_start"]
        if torch.xpu.is_available():
            # XPU needs the end address of the kernel to calculate the size of the kernel binary.
            embed_kernel_args.append(
                f"__{params['inductor_meta']['kernel_name']}_end"
            )

        load_kernel_args = (
            [
                *embed_kernel_args,
                cpp_string_literal(params["mangled_name"]),
                str(params["shared_mem"]),
            ]
            if V.graph.aot_mode and config.aot_inductor.embed_kernel_binary
            else [
                cpp_string_literal(params[get_cpp_wrapper_cubin_path_name()]),
                cpp_string_literal(params["mangled_name"]),
                str(params["shared_mem"]),
                "cubin_dir_",
            ]
        )
        prefix.writeline(
            f"{kernel_var_name} = loadKernel({', '.join(load_kernel_args)}); "
        )
    prefix.writeline("}")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/simd.py
# Line: 446

def want_no_x_dim(self) -> bool:
    return False


# ==================================================
# Occurrences: Lines 528-531 (2 instances)

def should_use_cooperative_reduction(self) -> bool:
    return False  # defined in subclass


# ==================================================
# Line: 590

def _combine_contiguous_dims(
    self, index: sympy.Expr, tree: IterationRangesRoot

# ==================================================
# Line: 796

def is_indirect_indexing(self, index: sympy.Expr) -> bool:
    # tmpX  means indirect indexing
    return free_symbol_is_type(index, SymT.TMP)


# ==================================================
# Line: 1097

def prepare_softmax_twopass_fallback(self, dtype, value):
    vmax = ops.reduction(dtype, dtype, "max", value)
    sub = ops.sub(value, vmax)
    exp = ops.exp(sub)
    vsum = ops.reduction(dtype, dtype, "sum", exp)
    return OpsWrapper._unwrap((vmax, vsum))


# ==================================================
# Line: 1257

def generate_node_schedule(self, nodes, numel, rnumel):
    node_schedule: list[Any] = []
    done = OrderedSet[scheduler.BaseSchedulerNode]()
    # Writes with a reduced shape, meaning they are only present once the
    # reduction loop has ended
    not_ready_yet_nodes: OrderedSet[str] = OrderedSet()
    current_loop_buffer_usage: OrderedSet[str] = OrderedSet()
    maybe_split_index: Optional[int] = None

    def fits_in_main_body(n):
        _, (node_numel, node_rnumel) = n.group
        return (node_numel == numel and node_rnumel == rnumel) or (
            node_numel == numel * rnumel and node_rnumel == 1
        )

    def fits_outside_reduction(n):
        _, (node_numel, node_rnumel) = n.group
        return node_numel == numel and node_rnumel == 1 and rnumel != 1

    def expect_improved_memory_usage(n):
        for read in n.read_writes.reads:
            if read.name in current_loop_buffer_usage:
                return True
        return False

    def schedule_node_in_loop(n):
        done.add(n)
        node_schedule.append(n)
        current_loop_buffer_usage.update([x.name for x in n.read_writes.reads])

        # A scan is modelled as a reduction in the scheduler but has a
        # full sized output that can be used inside the loop body
        if (
            n.is_reduction()
            and isinstance(n, scheduler.SchedulerNode)
            and isinstance(n.node, ir.ComputedBuffer)
            and not isinstance(n.node.data, ir.Scan)
        ):
            not_ready_yet_nodes.add(n.get_name())
        else:  # this node is available within the loop
            current_loop_buffer_usage.update([x.name for x in n.read_writes.writes])

    @contextlib.contextmanager
    def end_current_reduction_loop():
        nonlocal maybe_split_index
        if node_schedule and node_schedule[-1] is EnableReduction:
            node_schedule.pop()
        else:
            node_schedule.append(DisableReduction)
        if maybe_split_index:
            node_schedule.insert(maybe_split_index, DisableReduction)
            node_schedule.insert(maybe_split_index + 1, EnableReduction)
            maybe_split_index = None
        yield
        node_schedule.append(EnableReduction)
        not_ready_yet_nodes.clear()
        current_loop_buffer_usage.clear()

    def requires_closing_previous_reduction(node, node_schedule):
        if rnumel == 1:
            return False
        if not not_ready_yet_nodes & node.ancestors:
            return False
        assert node_schedule and not isinstance(
            node_schedule[-1], (EnableReduction, DisableReduction)
        )
        return bool(not_ready_yet_nodes)

    for node in nodes:
        if node in done:
            continue
        done.add(node)

        if fits_in_main_body(node):
            if requires_closing_previous_reduction(node, node_schedule):
                with end_current_reduction_loop():
                    pass  # need to start a new reduction loop

            if current_loop_buffer_usage and not expect_improved_memory_usage(node):
                # If we don't improve memory usage, then it is better to split into two loops
                maybe_split_index = maybe_split_index or len(node_schedule)
            else:
                # Memory usage got improved, cancel the loop split
                maybe_split_index = None

            schedule_node_in_loop(node)
        elif fits_outside_reduction(node):
            with end_current_reduction_loop():
                node_schedule.append(node)
        else:
            raise NotImplementedError(
                f"unexpected group: ({numel}, {rnumel}) != {node.group[1]}"
            )

    return node_schedule


# ==================================================
# Line: 1488

def codegen_node_schedule_with_kernel(self, node_schedule, kernel):
    with kernel:
        stack = contextlib.ExitStack()
        all_indexing = {}

        # First pass to collect indexing and decide inplace updates
        for node in node_schedule:
            if node is DisableReduction:
                stack.enter_context(kernel.disable_reduction())
            elif node is EnableReduction:
                stack.close()
            else:
                node.decide_inplace_update()
                index_vars = kernel.split_and_set_ranges(node.get_ranges())
                all_indexing.update(
                    dict.fromkeys(
                        node._body.indexing_from_args(index_vars).values()
                    )
                )

        kernel.finalize_indexing(all_indexing.keys())

        # Second pass to do codegen
        for node in node_schedule:
            if node is DisableReduction:
                stack.enter_context(kernel.disable_reduction())
            elif node is EnableReduction:
                stack.close()
            else:
                # TODO - use split ranges ?
                indexing_dtype_strength_reduction(node._body)
                index_vars = kernel.split_and_set_ranges(node.get_ranges())
                node.codegen(index_vars)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/wrapper.py
# Line: 441

def codegen(self, code: IndentedBuffer) -> None:
    if not V.graph.cpp_wrapper:
        code.do_unindent()


# ==================================================
# Occurrences: Lines 1091-1099 (3 instances)

def mark_output_type(self) -> None:
    return


# ==================================================
# Line: 1175

def get_graph_input_names(self) -> list[str]:
    return V.graph.graph_input_names


# ==================================================
# Line: 1285

def generate_before_suffix(self, result: IndentedBuffer) -> None:
    return


# ==================================================
# Line: 1302

def generate_end(self, result: IndentedBuffer) -> None:
    return


# ==================================================
# Line: 1432

def get_wrapper_call_indent(self) -> int:
    if config.graph_partition:
        return 2
    else:
        return 1


# ==================================================
# Occurrences: Lines 1714-1717 (2 instances)

def codegen_cpp_sizevar(self, x: Expr, *, simplify: bool = True) -> str:
    raise RuntimeError("codegen_cpp_sizevar is only implemented for cpp_wrapper!")


# ==================================================
# Line: 1723

def codegen_tuple_access(self, basename: str, name: str, index: str) -> str:
    return f"{basename}[{index}]"


# ==================================================
# Line: 2349

def prepare_triton_kernel_call(self, call_args):
    def wrap_arg(arg):
        if isinstance(arg, str):
            # dynamo wraps unspec variable as 0d CPU tensor, need convert to scalar
            return arg + ".item()" if should_unwrap_unspec_arg(arg) else arg
        elif isinstance(arg, (int, float, bool, SymbolicCallArg)):
            return str(arg)
        else:
            return pexpr(V.graph.sizevars.simplify(arg))

    return [wrap_arg(arg) for arg in call_args]


# ==================================================
# Occurrences: Lines 2716-2719 (2 instances)

def make_buffer_free(self, buffer: Union[BufferLike, ir.TorchBindObject]):
    return f"del {buffer.get_name()}"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_micro_gemm.py
# Occurrences: Lines 124-127 (2 instances)

def get_kernel_extra_args_declare(self) -> str:
    return ""


# ==================================================
# Line: 180

def codegen_init(
    self,
    kernel: CppTemplateKernel,

# ==================================================
# Line: 186

def codegen_finalize(
    self,
    kernel: CppTemplateKernel,

# ==================================================
# Line: 192

def get_b_layout(self) -> LayoutType:
    return LayoutType.NORMAL


# ==================================================
# Line: 222

def is_woq_int4(self):
    return False



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/mps.py
# Occurrences: Lines 394-398 (2 instances)

def _special_unary(self, a: CSEVariable, name: str) -> str:
    V.kernel.headers.add("special_math")
    return f"c10::metal::{name}({a})"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/wrapper_fxir.py
# Line: 116

def compile_graph(self, gm: GraphModule) -> Callable[..., Any]:
    """
    Converts the graph module into a runnable function. The default implementation
    is simply an interpreter calling kernels in eager mode. Derived backends can
    override this to do further compilation.
    """
    return gm.forward


# ==================================================
# Line: 178

def _fake_tensor(
    self,
    size: tuple[Any, ...],
    stride: tuple[Any, ...],
    dtype: Optional[torch.dtype] = None,
    device: Optional[torch.device] = None,

# ==================================================
# Line: 193

def _create_meta_from_buffer(
    self, node: torch.fx.Node, buffer: CodegenBuffer

# ==================================================
# Occurrences: Lines 379-395 (5 instances)

def _generate_comment(self, line: WrapperLine) -> None:
    assert isinstance(line, CommentLine)
    # We ignore comments in FX IR.


# ==================================================
# Line: 417

def _generate_line_context(self, line: WrapperLine) -> None:
    assert isinstance(line, LineContext)
    # We ignore line context in FX IR.


# ==================================================
# Occurrences: Lines 496-500 (2 instances)

def _generate_null(self, line: WrapperLine) -> None:
    assert isinstance(line, NullLine)
    # Does nothing.


# ==================================================
# Line: 691

def _generate_symbolic_call_arg(self, line: WrapperLine) -> None:
    assert isinstance(line, SymbolicCallArgLine)
    # No need for an FX node, as we will pass the arg to kernels via a SymInt.

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_template_kernel.py
# Occurrences: Lines 124-127 (2 instances)

def dtype(self, node: ir.Buffer) -> str:
    return DTYPE_TO_CPP[node.get_dtype()]


# ==================================================
# Line: 151

def slice_nd(self, node, ranges: list[tuple[Any, Any]]) -> ir.ReinterpretView:
    """
    Slice the given node with a list of ranges (start and end) corresponding to its dims.
    The dim is not sliced if the corresponding range is empty.
    """
    assert len(ranges) == len(node.get_size()), f"{ranges=}, {node=}"
    sliced = wrap_with_tensorbox(node)
    for dim, _range in enumerate(ranges):
        if len(_range) == 0:
            continue
        assert len(_range) == 2
        start, end = parse_expr_with_index_symbols(_range)
        sliced = L.slice_(sliced, dim, start, end, clamp=False)
    assert isinstance(sliced.data, ir.ReinterpretView), sliced.data
    return sliced.data


# ==================================================
# Line: 167

def select(self, node, dim: int, idx: int) -> ir.ReinterpretView:
    # We avoid using L.select here because we need clamp=False so the dim after slicing
    # is 1 instead of a sympy expression of symbol - dim_size.
    node = wrap_with_tensorbox(node)
    idx = ir.View.handle_negative_index(idx, node.get_size()[dim])
    sliced = L.squeeze(L.slice_(node, dim, idx, idx + 1, clamp=False), dim)
    assert isinstance(sliced.data, ir.ReinterpretView), sliced.data
    return sliced.data


# ==================================================
# Occurrences: Lines 176-181 (2 instances)

def view(self, node, sizes: list[Any]) -> ir.View:
    node = wrap_with_tensorbox(node)
    sizes = parse_expr_with_index_symbols(sizes)
    return L.view(node, sizes).data


# ==================================================
# Line: 195

def unroll_pragma(self, unroll):
    if cpp_builder.is_gcc():
        return f"#pragma GCC unroll {unroll}"
    else:
        return f"#pragma unroll {unroll}"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_gemm_template.py
# Line: 1288

def get_default_reindexers(self, epilogue_nodes):
    return [None] * len(epilogue_nodes)


# ==================================================
# Line: 1541

def is_int8_woq_gemm_small_m_dim(
    self,
    X: ir.ReinterpretView,
    W: ir.ReinterpretView,
    N,
    K,
    micro_gemm,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/triton.py
# Line: 395

def replace_offset(
    self, expr: sympy.Expr, replacement: sympy.Expr, symt: SymT

# ==================================================
# Line: 491

def has_indirect(self) -> bool:
    return False  # block_ptr can't do indirect indexing


# ==================================================
# Line: 503

def has_tmpmask(self) -> bool:
    return False  # block_ptr can't do indirect indexing


# ==================================================
# Line: 1732

def need_numel_args(self):
    """
    Indicate whether we need provide numel as arguments for the generated
    kernel calls in the benchmark.

    Should be true for pointwise/reduction kernels but false for triton
    matmul kernels.
    """
    return True


# ==================================================
# Line: 2104

def codegen_block_ptr_store_line(self, name, indexing, block_ptr, value, other=""):
    # Stores require an explicit broadcast. We do this in two phases:
    #  1. Broadcast the operand to the final shape of the range trees, e.g. [ZBLOCK,
    #     YBLOCK, XBLOCK]. This protects against implicit broadcasting from loads.
    #  2. In case the block pointer has different dimensionality, broadcast/reshape the
    #     result to the shape of the pointer.
    value = f"tl.broadcast_to({value}, {indexing.final_shape})"

    # These dims no longer need broadcasting.
    for idx, (dim, broadcast_dim) in enumerate(
        zip(indexing.final_shape, indexing.broadcast_shape)
    ):
        if V.graph.sizevars.statically_known_equals(dim, broadcast_dim):
            indexing.broadcasting_dims[idx] = False

    value = indexing.codegen_broadcast_and_reshape(
        value, indexing.final_shape, indexing.block_shape, False
    )

    # workaround https://github.com/triton-lang/triton/issues/2814
    value = f"{value}.to({triton_store_type(V.graph.get_dtype(name))})"
    return f"tl.store({block_ptr}, {value}{other})"


# ==================================================
# Line: 3448

def imports_for_benchmark_kernel(self):
    return textwrap.dedent(
        """
        from torch._dynamo.testing import rand_strided
        {}
        import torch
    """.format(V.graph.device_ops.import_get_raw_stream_as("get_raw_stream"))
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/memory_planning.py
# Line: 105

def allocate(self, block: Allocation, is_last: bool) -> bool:
    """
    Try to assign block to a memory location in this bool.  Return True if
    an assignment was made.
    """
    return False


# ==================================================
# Line: 128

def is_empty(self):
    return False



# ==================================================
# Line: 749

def mark_first_last_usage(self, lines):
    """
    Populate the AllocFromPoolLine.is_first_pool_usage and
    DeallocFromPoolLine.is_last_pool_usage fields so that pools
    are created/destroyed.
    """
    seen = OrderedSet[AllocationPool]()
    for line in lines:
        if isinstance(line, AllocFromPoolLine):
            assert line.group.allocation
            pool = line.group.allocation.pool
            assert pool is not None
            if pool not in seen:
                line.is_first_pool_usage = True
                seen.add(pool)

    seen = OrderedSet[AllocationPool]()
    for line in reversed(lines):
        if isinstance(line, DeallocFromPoolLine):
            assert line.group.allocation
            pool = line.group.allocation.pool
            assert pool is not None
            if pool not in seen:
                line.is_last_pool_usage = (
                    pool.root.get_live_ranges().end <= line.timestep
                )
                seen.add(pool)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/common.py
# Line: 242

def get_offset(self) -> sympy.Expr:
    return sympy.S.Zero


# ==================================================
# Line: 248

def get_stride(self) -> list[sympy.Expr]:
    return [sympy.S.One]


# ==================================================
# Line: 254

def get_inputs_that_alias_output(self) -> list[str]:
    return []



# ==================================================
# Line: 649

def deduce_node_dtype_by_inputs(self, node: torch.fx.Node) -> Optional[torch.dtype]:
    inputs = node.all_input_nodes
    input_nodes = [
        n for n in inputs if isinstance(n, torch.fx.Node) and n.op != "placeholder"
    ]
    if len(input_nodes) == 0:
        return None

    all_input_nodes_propagated = all(
        OptimizationContext.key in n.meta
        and n.meta[OptimizationContext.key].dtype is not None
        for n in input_nodes
    )
    if not all_input_nodes_propagated:
        return None

    return functools.reduce(
        torch.promote_types,
        [n.meta[OptimizationContext.key].dtype for n in input_nodes],
    )


# ==================================================
# Occurrences: Lines 1564-1567 (2 instances)

def wrap_ptr_arg(self, buf: str, dtype: torch.dtype) -> str:
    return buf


# ==================================================
# Line: 1806

def augment_key(self, cache_key: str) -> AugmentedKeyT:
    "Override this method to augment cache key with backend specifics"
    return cast(AugmentedKeyT, cache_key)


# ==================================================
# Line: 2206

def create_cse_var(self, *args: Any, **kwargs: Any) -> CSEVariable:
    return CSEVariable(*args, **kwargs)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/codegen/cpp_template.py
# Line: 123

def header(self) -> IndentedBuffer:
    res = IndentedBuffer()
    res.writeline("#include <torch/csrc/inductor/cpp_prefix.h>")
    # TODO: add c10::ForcedUnroll test to test_aoti_abi_check
    res.splice("""#include <c10/util/Unroll.h>""")
    res.splice("""#include <torch/csrc/inductor/aoti_torch/c/shim.h>""")
    enable_kernel_profile = config.cpp.enable_kernel_profile and sys.platform in [
        "linux",
        "win32",
    ]
    if enable_kernel_profile:
        res.writelines(["#include <ATen/record_function.h>"])
    return res


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/coordinate_descent_tuner.py
# Line: 63

def get_warpsmax(self):
    # Currently, CUDA has a maximum of 1024 threads, so 32 is the max
    # number of warps.
    return 1024 // 32


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/static_cuda_launcher.py
# Line: 142

def extract_type(self, ty: str) -> str:
    """
    Takes a triton type from CompiledKernel.signature and
    converts it into a single char encoding. _StaticCudaLauncher
    will switch on this char to figure out what type the underlying
    value should be passed to the triton kernel as.
    """
    if ty[0] == "*":
        return "O"
    elif ty == "nvTmaDesc":
        raise NotImplementedError("nvTmaDesc kernels are not yet supported")
    return StaticallyLaunchedCudaKernel.type_mappings()[ty]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/triton_heuristics.py
# Line: 854

def restore_args_from_cpu(self, cpu_copies):
    for pair in cpu_copies.values():
        arg, cpu_arg = pair
        required_storage_length = compute_required_storage_length(
            arg.size(),
            arg.stride(),
            0,
        )
        arg.as_strided((required_storage_length,), (1,)).copy_(
            cpu_arg, non_blocking=True
        )


# ==================================================
# Line: 1225

def make_launcher(self) -> LauncherType: ...


# ==================================================
# Line: 2836

def _constant_fold(
    self, fn: Callable[[list[int]], int], seq: list[Union[int, str]]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/runtime/benchmarking.py
# Line: 98

def benchmark_cpu(
    self: Self, _callable: Callable[[], Any], warmup: int = 20, rep: int = 100

# ==================================================
# Line: 184

def get_event_pairs(
    self: Self, iters: int

# ==================================================
# Line: 196

def get_event_pairs_min_timing(
    self: Self, event_pairs: list[tuple[torch.cuda.Event, torch.cuda.Event]]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/constant_folding.py
# Line: 101

def _support_dynamic_shape(self) -> bool:
    # ConstantFolder not support dynamic shape now
    return False


# ==================================================
# Line: 286

def insertable_tensor_check(self, tensor: torch.Tensor) -> bool:
    return True


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/select_algorithm.py
# Line: 677

def _handle_scatter_graph(self, scatter_graph):
    """Handle processing for a single scatter graph.

    Args:
        scatter_graph: The scatter graph to process
    """
    assert isinstance(scatter_graph, ir.ComputedBuffer), (
        f"scatter_graph must be an instance of ComputeBuffer but got {type(scatter_graph)}"
    )

    def contiguous_strides(x):
        # We always create a fresh contiguous grad for scattering into
        return sum(
            x_i * stride for x_i, stride in zip(x, scatter_graph.get_stride())
        )

    return scatter_graph.data.store_output(  # type: ignore[attr-defined]
        scatter_graph.name, contiguous_strides, []
    )


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
# File: /root/ecooptimizer/pytorch/torch/_inductor/scheduler.py
# Line: 260

def debug_str_extra(self) -> str:
    return ""


# ==================================================
# Line: 289

def reorder_loops_by_dep_pair(
    self, self_dep: MemoryDep, other_dep: MemoryDep

# ==================================================
# Occurrences: Lines 423-441 (7 instances)

def is_reduction(self) -> bool:
    return False


# ==================================================
# Line: 867

def get_template_node(self) -> Optional[ir.TemplateBuffer]:
    return None


# ==================================================
# Occurrences: Lines 926-932 (3 instances)

def is_reduction(self) -> bool:
    return False


# ==================================================
# Line: 2167

def current_device(self, device: Optional[torch.device]) -> None:
    V.graph.current_device = device


# ==================================================
# Line: 2490

def topological_sort_schedule(
    self, nodes: list[BaseSchedulerNode]

# ==================================================
# Line: 2798

def _any_atomic_add(self, node_list: Sequence[BaseSchedulerNode]) -> bool:
    return any(
        hasattr(n.node, "data")
        and n.node is not None
        and hasattr(n.node.data, "scatter_mode")
        and n.node.data.scatter_mode == "atomic_add"
        for n in node_list
    )


# ==================================================
# Line: 3378

def are_long_distant_nodes(
    self, node1: BaseSchedulerNode, node2: BaseSchedulerNode

# ==================================================
# Line: 3405

def decide_fusion_fail_reason(
    self,
    node1: BaseSchedulerNode,
    node2: BaseSchedulerNode,
    common_buf_names: Union[tuple[str], OrderedSet[str]],

# ==================================================
# Line: 3542

def unfusable_node(self, node: BaseSchedulerNode) -> bool:
    """
    Is this node unfusable under any conditions.
    """
    return (
        isinstance(node, (ExternKernelSchedulerNode, NopKernelSchedulerNode))
        and not node.is_template()
        and not is_output_of_multi_outputs_template(node.node)
    )


# ==================================================
# Line: 3552

def check_prologue_fusion_heuristics_fusable(
    self,
    prologue_node: BaseSchedulerNode,
    template_node: BaseSchedulerNode,
    why: WhyNoFuse,

# ==================================================
# Line: 4124

def compute_graph_partition_maps(
    self,
    signatures: list[GraphPartitionSignature],

# ==================================================
# Line: 4165

def get_graph_partition_symbol_inputs(
    self,
    partition: PartitionType,
    input_nodes: dict[str, Union[ir.IRNode, ir.TorchBindObject, sympy.Expr]],

# ==================================================
# Line: 4397

def clean_removed_buffer_from_partition_signatures(
    self, signature: GraphPartitionSignature

# ==================================================
# Line: 4896

def get_backend_features(self, device: torch.device) -> OrderedSet[BackendFeature]:
    """Return a set of .codegen.common.BackendFeature()"""
    return OrderedSet()


# ==================================================
# Line: 4916

def can_fuse_multi_outputs_template(
    self, node1: BaseSchedulerNode, node2: BaseSchedulerNode

# ==================================================
# Line: 4928

def fuse(
    self, node1: BaseSchedulerNode, node2: BaseSchedulerNode

# ==================================================
# Line: 4981

def ready_to_flush(self) -> bool:
    """
    Check whether the backend is requesting the scheduler to flush the generated kernel.
    If not supported, please return False.
    """
    return False


# ==================================================
# Line: 5010

def get_fusion_pair_priority(
    self, node1: BaseSchedulerNode, node2: BaseSchedulerNode

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/cpp_builder.py
# Line: 1818

def save_src_to_cmake(self, cmake_path: str, src_path: str) -> None:
    # Remove the directory part of file_path
    src_path = "${CMAKE_CURRENT_SOURCE_DIR}/" + Path(src_path).name
    with open(cmake_path, "a") as f:
        f.write(f"target_sources(aoti_model PRIVATE {src_path})\n")


# ==================================================
# Line: 1824

def save_kernel_asm_to_cmake(self, cmake_path: str, asm_files: list[str]) -> None:
    # TODO: make this work beyond CUDA
    with open(cmake_path, "a") as f:
        for asm_file in asm_files:
            kernel_name = Path(asm_file).name.split(".")[0]
            asm_file = f"${{CMAKE_CURRENT_SOURCE_DIR}}/{Path(asm_file).name}"
            contents = textwrap.dedent(
                f"""
                embed_gpu_kernel({kernel_name} {asm_file})
                """
            )
            f.write(contents)
        f.write("add_dependencies(aoti_model ${KERNEL_TARGETS})\n")
        f.write(
            "target_link_libraries(aoti_model PRIVATE ${KERNEL_OBJECT_FILES})\n"
        )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autoheuristic/artifacts/_MixedMMH100.py
# Line: 30

def get_confidence_threshold(self) -> float:
    return 0.0


# ==================================================
# Occurrences: Lines 61-64 (2 instances)

def get_name(self) -> str:
    return 'mixed_mm'


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autoheuristic/artifacts/_PadMMA100.py
# Occurrences: Lines 27-33 (3 instances)

def get_confidence_threshold(self) -> float:
    return 1.7025303314066


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autoheuristic/artifacts/_MMRankingA100.py
# Line: 30

def get_confidence_threshold(self) -> float:
    return 0.0


# ==================================================
# Occurrences: Lines 238-241 (2 instances)

def get_name(self) -> str:
    return 'mm'


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autoheuristic/artifacts/_MixedMMA100.py
# Line: 30

def get_confidence_threshold(self) -> float:
    return 0.0


# ==================================================
# Occurrences: Lines 62-65 (2 instances)

def get_name(self) -> str:
    return 'mixed_mm'


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autoheuristic/learned_heuristic_controller.py
# Line: 72

def get_heuristics(self, name: str) -> list[LearnedHeuristic]:
    """
    Returns a list of learned heuristics for the given optimization name.
    """

    if not LearnedHeuristicController.heuristics_initialized:
        # learned heuristics are generated into the following package
        learned_heuristics_package = "torch._inductor.autoheuristic.artifacts"

        # learned heuristics have to be of type LearnedHeuristic
        base_class = LearnedHeuristic
        found_heuristics = find_and_instantiate_subclasses(
            learned_heuristics_package, base_class
        )

        for learned_heuristic in found_heuristics:
            opt_name = learned_heuristic.get_name()
            LearnedHeuristicController.existing_heuristics[opt_name].append(
                learned_heuristic
            )
        LearnedHeuristicController.heuristics_initialized = True

    return LearnedHeuristicController.existing_heuristics[name]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autoheuristic/learnedheuristic_interface.py
# Line: 19

def check_precondition(
    self,
    metadata: AHMetadata,
    context: AHContext,

# ==================================================
# Occurrences: Lines 26-37 (4 instances)

def get_decision(
    self, context: AHContext, choices: list[Choice]

# ==================================================
# Line: 45

def get_feedback(self, context: AHContext, choice: Choice) -> float:
    return 1.0


# ==================================================
# Line: 70

def get_choice(self, idx: int) -> Optional[str]:
    return None


# ==================================================
# Line: 94

def get_best_choices(self, context: AHContext) -> Optional[list[tuple[float, int]]]:
    return []

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/remote_cache.py
# Line: 229

def _create_sample(self) -> Optional[Sample]:
    return None


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/cudagraph_trees.py
# Line: 1635

def create_storage(self, metadata: dict[str, Any]) -> torch.types.Storage:
    return torch._C._construct_storage_from_data_pointer(
        metadata["data_ptr"], metadata["device"], metadata["nbytes"]
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/loop_body.py
# Line: 444

def bind_scan_shim(self, combine_fn):
    def shim(dtypes, values):
        return V.ops.scan(dtypes, combine_fn, values)

    shim.clone = functools.partial(LoopBody.bind_scan_shim, combine_fn=combine_fn)  # type: ignore[attr-defined]
    return shim


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/graph.py
# Line: 526

def static_sizes_strides(
    self, ex: torch.Tensor

# ==================================================
# Line: 874

def add_symbol_graph_input(self, symbol: sympy.Expr) -> None:
    raise RuntimeError("Should not be called for the main graph")


# ==================================================
# Occurrences: Lines 1328-1331 (2 instances)

def call_module(self, target: Any, args: Any, kwargs: Any) -> NoReturn:
    raise AssertionError


# ==================================================
# Line: 1965

def validate_can_generate_cpp_wrapper(self) -> None:
    if config.disable_cpp_codegen:
        raise CppWrapperCodegenError("C++ codegen is disabled")

    if sys.platform not in ("linux", "darwin", "win32"):
        raise CppWrapperCodegenError(f"Unsupported platform {sys.platform}")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/bounds.py
# Line: 119

def masked_subblock(
    self,
    subblock: LoopBodyBlock,
    env: dict[torch.fx.Node, ValueRanges[Expr]],
    mask: Any,
    value: Any,
    submodules: dict[str, Callable[..., Any]],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/post_grad.py
# Line: 1507

def allow_cpu_device(self, node: fx.Node) -> bool:
    """
    Returns whether a node that returns a tensor on the target device may have
    cpu tensors as input.
    """
    return node.target in (
        torch.ops.aten.index.Tensor,
        torch.ops.aten.index_put.default,
        torch.ops.aten.index_put_.default,
        torch.ops.aten.copy.default,
        torch.ops.aten.copy_.default,
        torch.ops.aten.slice_scatter.default,
    )


# ==================================================
# Line: 1541

def get_node_device(self, node: fx.Node) -> Optional[torch.device]:
    """
    Get the device of a node.
    """
    ten = node.meta.get("val")
    return None if not isinstance(ten, torch.Tensor) else ten.device


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/group_batch_fusion.py
# Line: 173

def _addmm_node_can_be_fused(self, node: torch.fx.Node) -> bool:
    # pyre-fixme[7]: Incompatible return type
    return (
        node.kwargs.get("beta", DEFAULT_BETA) == DEFAULT_BETA
        and node.kwargs.get("alpha", DEFAULT_ALPHA) == DEFAULT_ALPHA  # type: ignore[return-value]
    )


# ==================================================
# Line: 180

def _is_input_2d(self, input: torch.fx.Node) -> bool:
    input_shapes = input.meta["val"].shape
    return (
        len(input_shapes) == 2
        and isinstance(input_shapes[0], int)
        and isinstance(input_shapes[1], int)
    )


# ==================================================
# Line: 388

def _pointwise_node_can_be_fused(self, node: torch.fx.Node):
    # note: we only consider the case where the inputs are tensors
    # for mixed precision training, we need to make sure the inputs
    # of the aten.cat when do the stack should be the same dtype
    # otherwise, the output of the aten.cat may be not the same as
    # its inputs, and cause dtype not same error in mm or addmm
    input, other = node.args
    return (
        input.meta["val"].shape == other.meta["val"].shape  # type: ignore[union-attr]
        # input and other can be scalars, where they have no attribute 'meta'
        if hasattr(input, "meta")
        and hasattr(other, "meta")
        and is_node_meta_valid(input)  # type: ignore[arg-type, union-attr]
        and is_node_meta_valid(other)  # type: ignore[arg-type, union-attr]
        # torch.SymInt or torch.SymFloat object has no attribute 'shape'
        and isinstance(input.meta["val"], torch.Tensor)  # type: ignore[union-attr]
        and isinstance(other.meta["val"], torch.Tensor)  # type: ignore[union-attr]
        else False
    )


# ==================================================
# Line: 617

def _getitem_args(self, getitem_node: torch.fx.Node):
    if getitem_node.target != operator.__getitem__ or (
        getitem_node.op != "call_function"
    ):
        return None
    return getitem_node.args[0]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/dedupe_symint_uses.py
# Line: 52

def _wrap_to_sym_expr_hash(self, key):
    return _SymExprHash(key) if isinstance(key, py_sym_types) else key



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/fx_passes/split_cat.py
# Line: 752

def get_non_cat_node_input(
    self, split_node: torch.fx.Node, node: torch.fx.Node

# ==================================================
# Line: 766

def merge_consecutive_inputs(
    self, inputs: list[Union[torch.fx.Node, int]]

# ==================================================
# Line: 823

def has_non_overlapping_ranges(self, ranges: list[_Range]) -> bool:
    for range_, next_range in zip(ranges, ranges[1:]):
        if range_[1] > next_range[0]:
            return False
    return True


# ==================================================
# Line: 829

def fill_gaps(self, ranges: list[_Range], min_: int, max_: int) -> list[_Range]:
    cur = min_
    filled_ranges = []
    for a, b in ranges:
        if cur < a:
            filled_ranges.append((cur, a))
        filled_ranges.append((a, b))
        cur = b
    if filled_ranges[-1][1] < max_:
        filled_ranges.append((filled_ranges[-1][1], max_))
    return filled_ranges


# ==================================================
# Line: 841

def get_transform_params(
    self,
    split_node: torch.fx.Node,
    next_users: list[torch.fx.Node],
    user_inputs_list: list[list[Union[torch.fx.Node, _Range]]],

# ==================================================
# Line: 894

def replace_split(
    self,
    graph: torch.fx.Graph,
    split_node: torch.fx.Node,
    split_sections: list[int],
    user_inputs_list: list[list[Union[torch.fx.Node, _Range]]],
    split_ranges: list[_Range],

# ==================================================
# Line: 961

def replace_cat(
    self,
    graph: torch.fx.Graph,
    split_node: torch.fx.Node,
    next_users: list[torch.fx.Node],
    user_inputs_list_new,
    transform_params_list: list[list[_TransformParam]],

# ==================================================
# Line: 1114

def erase_old_nodes(
    self,
    graph: torch.fx.Graph,
    split_node: torch.fx.Node,
    next_users: list[torch.fx.Node],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/choices.py
# Line: 56

def get_config_heuristics(
    self, device_type: Optional[str] = "cuda"

# ==================================================
# Line: 130

def triton_kernel_kwargs(
    self,
    kernel_cls: type[TritonKernel],
    features: SIMDKernelFeatures,
    groups: list[sympy.Expr],
    kernel_kwargs: dict[str, Any],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/async_compile.py
# Line: 414

def multi_kernel(self, *args, **kwargs) -> Any:
    from torch._inductor.codegen.multi_kernel import MultiKernelCall

    # no need to call this in parallel since the sub-kernels are already parallel tasks
    return MultiKernelCall(*args, **kwargs)


# ==================================================
# Line: 490

def _wait_futures(self, scope: dict[str, Any]) -> None:
    kernels = {
        key: value
        for key, value in scope.items()
        if isinstance(value, (Future, CodeCacheFuture))
    }
    pbar = tqdm(
        total=len(kernels),
        desc="Inductor Compilation",
        disable=config.disable_progress,
        delay=0,
    )
    for key, result in kernels.items():
        if config.verbose_progress and not isinstance(pbar, _Faketqdm):
            pbar.set_postfix_str(key)
        try:
            kernel = result.result()
            scope[key] = kernel
        except BrokenProcessPool as e:
            raise RuntimeError(
                "A compilation subprocess exited unexpectedly. This "
                "is likely due to a crash. To facilitate debugging, "
                "you can re-run with TORCHINDUCTOR_COMPILE_THREADS=1 "
                "to cause compilation to occur in the main process."
            ) from e
        pbar.update(1)



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/output_code.py
# Line: 363

def unwrap(self, g: CompiledFxGraph) -> dict[str, torch.Tensor]:
    assert g.constants is not None
    return g.constants



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_inductor/autotune_process.py
# Line: 527

def do_bench(
    self,
    fn,
    *input_tensors: torch.Tensor,
    out: Optional[torch.Tensor] = None,

# ==================================================
# Line: 562

def do_bench(
    self,
    fn,
    *input_tensors: torch.Tensor,
    out: Optional[torch.Tensor] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_classes.py
# Line: 34

def load_library(self, path):
    """
    Loads a shared library from the given path into the current process.

    The library being loaded may run global initialization code to register
    custom classes with the PyTorch JIT runtime. This allows dynamically
    loading custom classes. For this, you should compile your class
    and the static registration code into a shared library object, and then
    call ``torch.classes.load_library('path/to/libcustom.so')`` to load the
    shared object.

    After the library is loaded, it is added to the
    ``torch.classes.loaded_libraries`` attribute, a set that may be inspected
    for the paths of all libraries loaded using this function.

    Args:
        path (str): A path to a shared library to load.
    """
    torch.ops.load_library(path)



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cuda/_sanitizer.py
# Line: 291

def _state_wait_for_other(
    self, state: dict[StreamId, SeqNum], other: dict[StreamId, SeqNum]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_lazy/closure.py
# Line: 13

def run(self, closure):
    """Run closure function

    Args:
    closure: callable function to run
    """
    closure()


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/hipify/hipify_python.py
# Line: 701

def quote(self, char):
    """ Escape a char for regex. """
    return re.escape(char)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_sympy/printers.py
# Line: 50

def _print_Float(self, expr: sympy.Expr) -> str:
    if expr._prec == 53:
        # IEEE-754 double precision have 53 bits. SymPy prints them with
        # 15 digits, but we need 17 for round-trip correctness
        return str(sympy.Float(expr, dps=17))
    else:
        # We don't use other precisions in pytorch
        return str(expr)


# ==================================================
# Line: 283

def _print_Integer(self, expr: sympy.Expr) -> str:
    suffix = "LL" if sys.platform in ["darwin", "win32"] else "L"
    i = int(expr)
    if i > INDEX_TYPE_MAX or i < INDEX_TYPE_MIN:
        raise OverflowError(f"{i} too big to convert to {INDEX_TYPE}")
    elif i == INDEX_TYPE_MIN:
        assert i == (-1) << 63
        # Writing -9223372036854775808L makes the value overflow
        # as it is parsed as -(9223372036854775808L) by the C/C++ compiler
        return f"(-1{suffix} << 63)"
    return f"{i}{suffix}"


# ==================================================
# Line: 397

def _print_Rational(self, expr: sympy.Expr) -> str:
    # Uses float constants to perform FP div
    if expr.q == 1:
        r = f"{expr.p}"
    else:
        r = f"{expr.p}.0/{expr.q}.0"
    return f"static_cast<{INDEX_TYPE}>({r})" if expr.is_integer else r


# ==================================================
# Occurrences: Lines 496-499 (2 instances)

def _print_BooleanTrue(self, expr: sympy.Expr) -> str:
    return "true"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_sympy/numbers.py
# Line: 44

def _sympystr(self, printer):
    return "int_oo"


# ==================================================
# Line: 144

def _as_mpf_val(self, prec):
    return mlib.finf


# ==================================================
# Line: 238

def _sympystr(self, printer):
    return "-int_oo"


# ==================================================
# Line: 309

def _eval_power(self, expt):
    if expt.is_number:
        if expt in (
            S.NaN,
            S.Infinity,
            S.NegativeInfinity,
            S.IntInfinity,
            S.NegativeIntInfinity,
        ):
            return S.NaN

        if isinstance(expt, sympy.Integer) and expt.is_extended_positive:
            if expt.is_odd:
                return S.NegativeIntInfinity
            else:
                return S.IntInfinity

        inf_part = S.IntInfinity**expt
        s_part = S.NegativeOne**expt
        if inf_part == 0 and s_part.is_finite:
            return inf_part
        if (
            inf_part is S.ComplexInfinity
            and s_part.is_finite
            and not s_part.is_zero
        ):
            return S.ComplexInfinity
        return s_part * inf_part


# ==================================================
# Line: 338

def _as_mpf_val(self, prec):
    return mlib.fninf


# ==================================================
# Line: 396

def as_powers_dict(self):
    return {S.NegativeOne: 1, S.IntInfinity: 1}

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_config_module.py
# Line: 412

def _get_alias_module_and_name(
    self, entry: _ConfigEntry

# ==================================================
# Line: 628

def patch(
    self,
    arg1: Optional[Union[str, dict[str, Any]]] = None,
    arg2: Any = None,
    **kwargs: dict[str, Any],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_ordered_set.py
# Occurrences: Lines 89-93 (2 instances)

def difference_update(self, *others: Iterable[T]) -> None:
    for other in others:
        self -= other  # type: ignore[arg-type]


# ==================================================
# Line: 104

def intersection_update(self, *others: Iterable[T]) -> None:
    for other in others:
        self &= other  # type: ignore[arg-type]


# ==================================================
# Line: 117

def symmetric_difference_update(self, other: Iterable[T]) -> None:
    self ^= other  # type: ignore[arg-type]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/_freeze.py
# Line: 150

def write_frozen(self, m: FrozenModule, outfp):
    """Write a single frozen module's bytecode out to a C variable."""
    outfp.write(f"unsigned char {m.c_name}[] = {{")
    for i in range(0, len(m.bytecode), 16):
        outfp.write("\n\t")
        for c in bytes(m.bytecode[i : i + 16]):
            outfp.write(f"{c:d},")
    outfp.write("\n};\n")


# ==================================================
# Line: 185

def get_module_qualname(self, file_path: Path, top_package_path: Path) -> list[str]:
    # `path` looks like 'Lib/foo/bar/baz.py'

    # chop off 'Lib/' to get something that represents a Python module hierarchy.
    # e.g. 'foo/bar/baz.py', which maps to 'foo.bar.baz'
    normalized_path = file_path.relative_to(top_package_path.parent)

    if normalized_path.name == "__init__.py":
        # Special handling for `__init__.py`. In this case, this file
        # specifies that the containing directory should be treated as a package.
        # For 'foo/bar/baz/__init__.py':
        # - The module name is 'baz'
        module_basename = normalized_path.parent.name
        # - The parent is foo.bar (need to shave off the 'baz')
        module_parent = normalized_path.parent.parent.parts
    else:
        module_basename = normalized_path.stem
        module_parent = normalized_path.parent.parts
    return list(module_parent) + [module_basename]


# ==================================================
# Line: 205

def compile_string(self, file_content: str) -> types.CodeType:
    # instead of passing in the real build time path to 'compile', we
    # pass in a marker instead. This prevents the build time path being
    # leaked to runtime. That path may not be available at runtime.
    # Setting the path to a mark make sure it's a hard error rather
    # than a flaky error when inspect module tries to retrieve python source
    # code during torchscripting.
    path_marker = PATH_MARKER
    return compile(file_content, path_marker, "exec")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/datapipe.py
# Line: 240

def _is_dfpipe(self):
    return True



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/dataframe/dataframes.py
# Line: 430

def collate(self, *args, **kwargs):
    raise RuntimeError("Can't collate unbatched DataFrames stream")


# ==================================================
# Line: 450

def is_shardable(self):
    return False


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/data/datapipes/dataframe/datapipes.py
# Line: 120

def _as_list(self, item):
    try:
        return list(item)
    except (
        Exception
    ):  # TODO(VitalyFedyunin): Replace with better iterable exception
        return [item]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/hooks.py
# Line: 115

def _pack_with_none(self, indices, values, size):
    res = [None] * size
    for idx, val in zip(indices, values):
        res[idx] = val

    return tuple(res)


# ==================================================
# Line: 122

def _unpack_none(self, indices, values):
    res = [values[idx] for idx in indices]

    return tuple(res)


# ==================================================
# Line: 154

def _apply_on_tensors(self, fn, args):
    # Can be used to apply the given function to the tensors contained in the
    # args. Will return updated args and the tensors indices
    tensors_idx = []
    tensors = []

    requires_grad = False
    for i, arg in enumerate(args):
        if isinstance(arg, torch.Tensor):
            tensors_idx.append(i)
            tensors.append(arg)
            requires_grad |= arg.requires_grad

    if not (requires_grad and torch.is_grad_enabled()):
        return args, None

    new_tensors = torch.nn.modules._functions.BackwardHookFunction.apply(*tensors)
    if len(new_tensors) == 0:
        raise RuntimeError("Cannot set Module backward hook for a Module with no input Tensors.")

    grad_fns = [t.grad_fn for t in new_tensors if t.grad_fn is not None and t.grad_fn.name() == "BackwardHookFunctionBackward"]
    if len(grad_fns) == 0:
        raise RuntimeError("Error while setting up backward hooks. Please open "
                           "an issue with a code sample to reproduce this.")

    fn(grad_fns[0])

    arg_list = list(args)
    for idx, val in zip(tensors_idx, new_tensors):
        arg_list[idx] = val

    if type(args) is tuple:
        out = tuple(arg_list)
    else:
        out = type(args)(*arg_list)
    return out, tensors_idx


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/deterministic.py
# Line: 18

def fill_uninitialized_memory(self, mode):
    return torch._C._set_deterministic_fill_uninitialized_memory(mode)



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/benchmark/utils/compare.py
# Line: 332

def _group_by_label(self, results: list[common.Measurement]):
    grouped_results: collections.defaultdict[str, list[common.Measurement]] = collections.defaultdict(list)
    for r in results:
        grouped_results[r.label].append(r)
    return grouped_results


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/utils/cpp_extension.py
# Line: 1094

def _add_compile_flag(self, extension, flag):
    extension.extra_compile_args = copy.deepcopy(extension.extra_compile_args)
    if isinstance(extension.extra_compile_args, dict):
        for args in extension.extra_compile_args.values():
            args.append(flag)
    else:
        extension.extra_compile_args.append(flag)


# ==================================================
# Line: 1104

def _hipify_compile_flags(self, extension):
    if isinstance(extension.extra_compile_args, dict) and 'nvcc' in extension.extra_compile_args:
        modified_flags = []
        for flag in extension.extra_compile_args['nvcc']:
            if flag.startswith("-") and "CUDA" in flag and not flag.startswith("-I"):
                # check/split flag into flag and value
                parts = flag.split("=", 1)
                if len(parts) == 2:
                    flag_part, value_part = parts
                    # replace fist instance of "CUDA" with "HIP" only in the flag and not flag value
                    modified_flag_part = flag_part.replace("CUDA", "HIP", 1)
                    modified_flag = f"{modified_flag_part}={value_part}"
                else:
                    # replace fist instance of "CUDA" with "HIP" in flag
                    modified_flag = flag.replace("CUDA", "HIP", 1)
                modified_flags.append(modified_flag)
                logger.info('Modified flag: %s -> %s', flag, modified_flag)
            else:
                modified_flags.append(flag)
        extension.extra_compile_args['nvcc'] = modified_flags


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_ops.py
# Line: 1397

def import_module(self, module):
    """
    Imports a Python module that has torch.library registrations.

    Generally, to extend PyTorch with custom operators, a user will
    create a Python module whose import triggers registration of
    the custom operators via a torch.ops.load_library call or a call
    to one or more torch.library.* APIs.

    It is unexpected for Python modules to have side effects, so some
    linters and formatters will complain. Use this API to import Python
    modules that contain these torch.library side effects.

    Args:
        module (str): The name of the Python module to import

    """
    importlib.import_module(module)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/interpreter.py
# Line: 301

def call_function(
    self, target: "Target", args: tuple[Argument, ...], kwargs: dict[str, Any]

# ==================================================
# Line: 323

def call_method(
    self, target: "Target", args: tuple[Argument, ...], kwargs: dict[str, Any]

# ==================================================
# Line: 372

def output(
    self, target: "Target", args: tuple[Argument, ...], kwargs: dict[str, Any]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/graph_module.py
# Line: 887

def _deepcopy_init(self):
    return GraphModule.__init__


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/validator.py
# Line: 182

def sym_sum(self, args: z3.ArithRef) -> z3.ArithRef:
    return sum(args)


# ==================================================
# Line: 190

def floor(self, number: z3.ArithRef) -> z3.ArithRef:
    # Z3 ToInt function rounds a real number towards negative infinity.
    return _Z3Ops.to_int(number)


# ==================================================
# Occurrences: Lines 213-216 (2 instances)

def max(self, a: z3.ArithRef, b: z3.ArithRef) -> z3.ArithRef:
    return z3.If(a > b, a, b)  # type: ignore[return-value]


# ==================================================
# Line: 238

def abs(self, number: z3.ArithRef) -> z3.ArithRef:
    return z3.Abs(number)


# ==================================================
# Line: 387

def constant(self, value: Any, dtype: torch.dtype) -> z3.ExprRef:
    # TODO: Probably OK to relax this and allow lower precision
    if dtype is torch.int64:
        return z3.IntVal(int(value))
    if dtype is torch.double:
        return z3.RealVal(float(value))
    if dtype is torch.bool:
        return z3.BoolVal(bool(value))
    raise ValueError(f"unsupported dtype (SympyToZ3): {dtype}")


# ==================================================
# Occurrences: Lines 397-402 (2 instances)

def to_dtype(self, x: z3.ArithRef, dtype: torch.dtype) -> z3.ArithRef:
    if dtype == torch.float64:
        return z3.ToReal(x)
    raise NotImplementedError(f"to_dtype {dtype} NYI")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/schema_type_annotation.py
# Line: 121

def _extract_python_return_type(self, target: Target) -> Optional[Any]:
    """
    Given a Python call target, try to extract the Python return annotation
    if it is available, otherwise return None

    Args:

        target (Callable): Python callable to get return annotation for

    Returns:

        Optional[Any]: Return annotation from the `target`, or None if it was
            not available.
    """
    assert callable(target)
    try:
        sig = inspect.signature(target)
    except (ValueError, TypeError):
        return None

    return (
        sig.return_annotation
        if sig.return_annotation is not inspect.Signature.empty
        else None
    )

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/sym_node.py
# Occurrences: Lines 616-622 (3 instances)

def is_symbolic(self):
    return True


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/rewriter.py
# Line: 72

def visit_Assert(self, node):
    """
    Swap out the Assert node (Python's `assert`) with a callsite to the
    symbolically-traceable torch._assert function
    """
    # Create the Call node
    n = ast.parse("torch._assert()", mode="eval")
    assert isinstance(n, ast.Expression)
    call_node = n.body
    assert isinstance(call_node, ast.Call)
    msg = node.msg if node.msg else ast.Constant(value="", kind=None)
    call_node.args = [node.test, msg]

    # Ensure that the new node conforms to the Python AST grammar
    expr_wrapper = ast.Expr(value=call_node)

    # Return the new Call node to signify that we want to use it as
    # a replacement for the original _assert node
    return ast.copy_location(expr_wrapper, node)


# ==================================================
# Line: 92

def visit_AnnAssign(self, node):
    """
    Swap out Python's AnnAssign with an Assign node where the annotation function is called.
    Example:
         Original:
         y: Tensor_Type(1,2,3, Dyn) = f2(x)
        Output:
         y = annotate(f2(x),Tensor_Type((1,2,3,Dyn)))
    """
    return ast.Assign(
        targets=[node.target],
        value=ast.Call(
            func=ast.Name(id="annotate", ctx=ast.Load()),
            args=[node.value, node.annotation],
            keywords=[],
        ),
    )



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/_constant_symnode.py
# Line: 11

def is_constant(self) -> bool:
    return True


# ==================================================
# Occurrences: Lines 17-26 (4 instances)

def is_int(self) -> bool:
    return True


# ==================================================
# Line: 65

def is_symbolic(self) -> bool:
    return False


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/experimental/symbolic_shapes.py
# Line: 1042

def get(self, b: bool) -> IntLikeType:
    """Get the int value from bool"""
    return cast_symbool_to_symint_guardless(b)



# ==================================================
# Line: 1863

def render(self, source: Source) -> str:
    return f"RelaxedUnspecConstraint({source.name()})"



# ==================================================
# Line: 2592

def _print_Float(self, expr: sympy.Float) -> str:
    """Convert a sympy Float to a Python float string representation."""
    return str(float(expr))


# ==================================================
# Occurrences: Lines 3176-3181 (2 instances)

def _is_derived_dim(
    self, dim: object

# ==================================================
# Line: 4149

def _ignore_fresh_unbacked_symbols_tls(self) -> bool:
    return getattr(TLS, "ignore_fresh_unbacked_symbols", False)


# ==================================================
# Line: 4299

def _suppress_guards_exit(self) -> None:
    old = (
        TLS.suppress_guards_stack.pop()
        if len(TLS.suppress_guards_stack) > 0
        else False
    )
    TLS.suppress_guards = old


# ==================================================
# Line: 4835

def is_unbacked_symint(self, symbol: sympy.Symbol) -> bool:
    """Check if a sympy symbol matches the naming convention for unbacked symbols"""
    return symbol_is_type(symbol, SymT.UNBACKED_INT)


# ==================================================
# Line: 6014

def evaluate_guards_expression(self, code: str, args: Sequence[object]) -> bool:
    """
    Expected to be used with produce_guards_expression(). Evaluates an expression
    generated by produce_guards_expression for the given concrete args.
    """
    arg_names = [f"t{i}" for i in range(len(args))]
    return eval(code, SYMPY_INTERP, {"L": dict(zip(arg_names, args))})


# ==================================================
# Line: 6048

def bind_symbols(
    self, placeholders: Sequence[FakeTensor], args: Sequence[Tensor]

# ==================================================
# Line: 6168

def get_implications(
    self, e: SympyBoolean

# ==================================================
# Line: 6947

def _default_unspecified_value_range(self) -> ValueRanges:
    return ValueRanges.unknown_int()


# ==================================================
# Line: 6988

def _get_user_frame(self) -> types.FrameType:
    frame = inspect.currentframe()
    while frame is not None:
        if frame.f_code.co_filename not in uninteresting_files():
            return frame
        frame = frame.f_back
    assert frame is not None
    return frame


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/graph.py
# Line: 340

def generate_output(self, output_args: Argument) -> str:
    """
    Given the output arguments, generates the return statement of the FX function.
    Note: The returned statement should not be indented.
    """
    return f"return {repr(output_args)}"


# ==================================================
# Line: 347

def process_inputs(self, *args: Any) -> Any:
    """
    Transforms the inputs so that the graph can take them as arguments, as
    non-default codegen may result in the inputs to the function being
    different from the inputs to the graph.

    If the graph was directly runnable, this invariant should hold true
    `f.graph.process_outputs(f.graph(*f.graph.process_inputs(*inputs))) == f(*inputs)`
    """
    return args


# ==================================================
# Line: 358

def process_outputs(self, outputs: Any) -> Any:
    """
    Transforms the outputs of the graph to be identical to the codegen.

    See ``process_inputs`` for more details.
    """
    return outputs


# ==================================================
# Line: 366

def additional_globals(self) -> list[tuple[str, Any]]:
    """
    If your codegen uses extra global values, add tuples of (identifier,reference to the value) here.
    For example, return ['List', typing.List] if you need ``List`` in the global context.
    """
    return []


# ==================================================
# Line: 865

def _key(self, node) -> tuple[str, Optional[Target]]:
    return (node.op, node.target if node.op == "call_function" else None)


# ==================================================
# Line: 1517

def _target_to_str(self, target: Target) -> str:
    if callable(target):
        op = target.__name__
    else:
        assert isinstance(target, str)
        op = target
        if _is_magic(op):
            op = op[2:-2]
    op = _snake_case(op)
    return op


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/utils/matcher_utils.py
# Line: 122

def _match_attributes(self, pn: Node, gn: Node) -> bool:
    # Attributes matching is complicated. Right now we only support matching constant tensor
    assert isinstance(pn.target, str), f"pn.target {pn.target} must be a string."
    assert isinstance(gn.target, str), f"gn.target {gn.target} must be a string."

    pn_value = torch.fx.graph_module._get_attr(pn.graph.owning_module, pn.target)
    gn_value = torch.fx.graph_module._get_attr(gn.graph.owning_module, gn.target)

    if type(pn_value) != type(gn_value):
        return False

    # Don't require exact match on tensor values.
    if isinstance(pn_value, torch.Tensor):
        return isinstance(gn_value, torch.Tensor)
    else:
        raise RuntimeError(f"Unsupported type {pn_value} when matching attributes")
    return False


# ==================================================
# Line: 174

def _remove_overlapping_matches(
    self, matches: list[InternalMatch]

# ==================================================
# Line: 194

def _match_literals(self, pn: Any, gn: Any, match: InternalMatch) -> bool:
    assert not (
        isinstance(pn, Node) and isinstance(gn, Node)
    ), "pn and gn cannot both be Node"

    if isinstance(pn, Node) and not isinstance(gn, Node):
        if pn.op == "placeholder":
            # Check if we've already matched these nodes in the current
            # traversal
            if pn in match.nodes_map:
                return match.nodes_map[pn] == gn

            match.nodes_map[pn] = gn
            return True
        else:
            return False
    elif not isinstance(pn, Node) and isinstance(gn, Node):
        return False
    else:
        return type(gn) == type(pn) and gn == pn


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/splitter_base.py
# Line: 424

def _lower_model_to_backend(
    self, mod: torch.fx.GraphModule, inputs: Tensors

# ==================================================
# Line: 433

def _find_culprit(self, mod: torch.fx.GraphModule, inputs: Tensors) -> str:
    """
    When an error occurs during lowering or running the lowered mod, we use this
    function to find culprits in the `mod` that causes the error.
    """

    return "Unable to find a culprit because _find_culprit() function is not implemented."


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/net_min_base.py
# Line: 165

def run_a(
    self, mod: torch.fx.GraphModule, inputs: Tensors, report_idx: int = -1

# ==================================================
# Line: 174

def run_b(
    self, mod: torch.fx.GraphModule, inputs: Tensors, report_idx: int = -1

# ==================================================
# Line: 911

def print_report(self, report: list[str]):
    for i in range(len(report)):
        if i > 0:
            print(" . " + report[i])
        else:
            print(report[i])


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/passes/graph_drawer.py
# Line: 186

def _get_leaf_node(
    self, module: torch.nn.Module, node: torch.fx.Node

# ==================================================
# Line: 200

def _typename(self, target: Any) -> str:
    if isinstance(target, torch.nn.Module):
        ret = torch.typename(target)
    elif isinstance(target, str):
        ret = target
    else:
        ret = _get_qualified_name(target)

    # Escape "{" and "}" to prevent dot files like:
    # https://gist.github.com/SungMinCho/1a017aab662c75d805c5954d62c5aabc
    # which triggers `Error: bad label format (...)` from dot
    return ret.replace("{", r"\{").replace("}", r"\}")


# ==================================================
# Line: 216

def _shorten_file_name(
    self,
    full_file_name: str,
    truncate_to_last_n: int = 2,

# ==================================================
# Line: 336

def _stringify_tensor_meta(self, tm: TensorMetadata) -> str:
    result = ""
    if not hasattr(tm, "dtype"):
        print("tm", tm)
    result += "|" + "dtype" + "=" + str(tm.dtype) + r"\n"
    result += "|" + "shape" + "=" + str(tuple(tm.shape)) + r"\n"
    result += "|" + "requires_grad" + "=" + str(tm.requires_grad) + r"\n"
    result += "|" + "stride" + "=" + str(tm.stride) + r"\n"
    if tm.is_quantized:
        assert tm.qparams is not None
        assert "qscheme" in tm.qparams
        qscheme = tm.qparams["qscheme"]
        if qscheme in {
            torch.per_tensor_affine,
            torch.per_tensor_symmetric,
        }:
            result += "|" + "q_scale" + "=" + str(tm.qparams["scale"]) + r"\n"
            result += (
                "|"
                + "q_zero_point"
                + "="
                + str(tm.qparams["zero_point"])
                + r"\n"
            )
        elif qscheme in {
            torch.per_channel_affine,
            torch.per_channel_symmetric,
            torch.per_channel_affine_float_qparams,
        }:
            result += (
                "|"
                + "q_per_channel_scale"
                + "="
                + str(tm.qparams["scale"])
                + r"\n"
            )
            result += (
                "|"
                + "q_per_channel_zero_point"
                + "="
                + str(tm.qparams["zero_point"])
                + r"\n"
            )
            result += (
                "|"
                + "q_per_channel_axis"
                + "="
                + str(tm.qparams["axis"])
                + r"\n"
            )
        else:
            raise RuntimeError(f"Unsupported qscheme: {qscheme}")
        result += "|" + "qscheme" + "=" + str(tm.qparams["qscheme"]) + r"\n"
    return result


# ==================================================
# Line: 391

def _get_tensor_label(self, t: torch.Tensor) -> str:
    return str(t.dtype) + str(list(t.shape)) + r"\n"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/_symbolic_trace.py
# Line: 442

def is_leaf_module(self, m: torch.nn.Module, module_qualified_name: str) -> bool:
    """
    A method to specify whether a given ``nn.Module`` is a "leaf" module.

    Leaf modules are the atomic units that appear in
    the IR, referenced by ``call_module`` calls. By default,
    Modules in the PyTorch standard library namespace (torch.nn)
    are leaf modules. All other modules are traced through and
    their constituent ops are recorded, unless specified otherwise
    via this parameter.

    Args:

        m (Module): The module being queried about
        module_qualified_name (str): The path to root of this module. For example,
            if you have a module hierarchy where submodule ``foo`` contains
            submodule ``bar``, which contains submodule ``baz``, that module will
            appear with the qualified name ``foo.bar.baz`` here.
    """
    return (
        m.__module__.startswith("torch.nn")
        or m.__module__.startswith("torch.ao.nn")
    ) and not isinstance(m, torch.nn.Sequential)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/fx/proxy.py
# Line: 275

def _find_user_frame(self):
    """
    Find the Python stack frame executing the user code during
    symbolic tracing.
    """
    # We have to do a little dance here. Basically, walk up the callstack and
    # record the first frame not in the pytorch source. This is the frame executing
    # the user code during tracing.
    frame = inspect.currentframe()

    pt_files = [
        "torch/fx/proxy.py",
        "torch/fx/_symbolic_trace.py",
        "torch/fx/experimental/proxy_tensor.py",
        "torch/_ops.py",
        "torch/_tensor.py",
        "torch/utils/_python_dispatch.py",
        "torch/_prims_common/wrappers.py",
        "torch/_refs/__init__.py",
        "torch/_refs/nn/functional/__init__.py",
        "torch/utils/_stats.py",
    ]
    while frame:
        frame = frame.f_back
        if frame and all(
            not frame.f_code.co_filename.endswith(file) for file in pt_files
        ):
            break

    if not frame:
        return None

    return frame


# ==================================================
# Line: 382

def to_bool(self, obj: "Proxy") -> bool:
    """Called when a proxy object is being converted to a boolean, such as
    when used in control flow.  Normally we don't know what to do because
    we don't know the value of the proxy, but a custom tracer can attach more
    information to the graph node using create_node and can choose to return a value.
    """
    raise TraceError(
        "symbolically traced variables cannot be used as inputs to control flow"
    )


# ==================================================
# Line: 393

def iter(self, obj: "Proxy") -> Iterator:
    """Called when a proxy object is being iterated over, such as
    when used in control flow.  Normally we don't know what to do because
    we don't know the value of the proxy, but a custom tracer can attach more
    information to the graph node using create_node and can choose to return an iterator.
    """
    raise TraceError(
        "Proxy object cannot be iterated. This can be "
        "attempted when the Proxy is used in a loop or"
        " as a *args or **kwargs function argument. "
        "See the torch.fx docs on pytorch.org for a "
        "more detailed explanation of what types of "
        "control flow can be traced, and check out the"
        " Proxy docstring for help troubleshooting "
        "Proxy iteration errors"
    )


# ==================================================
# Line: 411

def keys(self, obj: "Proxy") -> Any:
    """Called when a proxy object is has the keys() method called.
    This is what happens when ** is called on a proxy. This should return an
    iterator it ** is suppose to work in your custom tracer.
    """
    return Attribute(obj, "keys")()



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_weights_only_unpickler.py
# Line: 568

def persistent_load(self, pid):
    raise UnpicklingError("unsupported persistent id encountered")



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/verification.py
# Line: 484

def _indent(self, lines: str) -> str:
    return "\n".join(["\t" + line for line in lines.splitlines()])


# ==================================================
# Line: 1590

def _args_and_params_for_partition_graph(
    self,
    graph: torch.Graph,
    bridge_kwargs: Mapping[str, _NumericType | Sequence[_NumericType]],
    full_kwargs: Mapping[str, torch.Tensor],
    full_params: Mapping[str, torch.Tensor],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/fx/_pass.py
# Line: 211

def _maybe_fakefy_args(
    self, fake_mode: fake_tensor.FakeTensorMode | None, *args: Any

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/fx/fx_onnx_interpreter.py
# Line: 476

def placeholder(
    self,
    node: torch.fx.Node,
    onnxscript_graph: onnxscript_graph_building.TorchScriptGraph,
    fx_name_to_onnxscript_value: dict[
        str,
        onnxscript_graph_building.TorchScriptTensor
        | tuple[onnxscript_graph_building.TorchScriptTensor, ...],
    ],

# ==================================================
# Line: 529

def call_function(
    self,
    node: torch.fx.Node,
    onnxscript_tracer: onnxscript_graph_building.TorchScriptTracingEvaluator,
    fx_name_to_onnxscript_value: dict[
        str,
        onnxscript_graph_building.TorchScriptTensor
        | tuple[onnxscript_graph_building.TorchScriptTensor, ...],
    ],
    onnxfunction_dispatcher: onnxfunction_dispatcher.OnnxFunctionDispatcher,
    fx_graph_module: torch.fx.GraphModule,

# ==================================================
# Line: 593

def output(
    self,
    node: torch.fx.Node,
    onnxscript_graph: onnxscript_graph_building.TorchScriptGraph,
    fx_name_to_onnxscript_value: dict[
        str,
        onnxscript_graph_building.TorchScriptTensor
        | tuple[onnxscript_graph_building.TorchScriptTensor, ...],
    ],

# ==================================================
# Line: 617

def call_method(self, node: torch.fx.Node):
    # TODO(wechi): Support call_method.
    raise RuntimeError("call_method is not supported yet.")


# ==================================================
# Line: 694

def get_attr(
    self,
    node: torch.fx.Node,
    onnxscript_graph: onnxscript_graph_building.TorchScriptGraph,
    fx_name_to_onnxscript_value: dict[
        str,
        onnxscript_graph_building.TorchScriptTensor
        | tuple[onnxscript_graph_building.TorchScriptTensor, ...],
    ],
    fx_graph_module: torch.fx.GraphModule,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/fx/onnxfunction_dispatcher.py
# Line: 197

def _get_aten_name(self, node: torch.fx.Node) -> registration.OpName:
    """Get the OpName from the target.

    Args:
        node: The TorchFX node to get the aten name for.

    Returns:
        The internal op name within dataclass: registration.OpName.
    """
    if node.target == operator.getitem:
        return registration.OpName.from_name_parts(
            namespace="aten", op_name="getitem"
        )
    if isinstance(node.target, torch._ops.OpOverloadPacket):
        # aten::sym_size is the only OverloadPacket that we support.
        # schema: aten::sym_size(Tensor self, int dim) -> Tensor
        if node.target != torch.ops.aten.sym_size:
            raise RuntimeError(
                f"Unsupported OverloadPacket: {node.target}, aten.sym_size is the only allowed OverloadPacket!",
            )
        # TODO(titaiwang): aten::sym_size has overload, but fx graph is using
        # overloadpacket for some reasons.
        # https://github.com/pytorch/pytorch/issues/97201
        aten_op_default = node.target.default
        return registration.OpName.from_op_overload(op_overload=aten_op_default)  # type: ignore[no-any-return]

    if isinstance(node.target, types.BuiltinFunctionType):
        # Make sure it's symint/symfloat consuming builtin ops.
        for node_arg in node.args:
            if (not isinstance(node_arg, (torch.fx.Node, int, float))) or (
                isinstance(node_arg, torch.fx.Node)
                and not fx_type_utils.is_torch_symbolic_type(node_arg.meta["val"])
            ):
                raise RuntimeError(
                    f"Unsupported node arg: {node_arg} (type {type(node_arg)}) with builtin function: {node.target},"
                    " only int/float/SymInt/SymFloat is supported with built-in ops!",
                )
        return registration.OpName.from_builtin_function(node.target)

    if isinstance(node.target, torch._ops.OpOverload):
        return registration.OpName.from_op_overload(op_overload=node.target)

    # Unexpected target, raise error.
    raise RuntimeError(f"Unknown call_function target: {node.target}")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/fx/passes/functionalization.py
# Line: 73

def _functionalize(self, function: Callable) -> Callable:
    # Working around a dispatcher issue with `torch.func.functionalize` when used
    # together with `make_fx`.
    # Ref: https://github.com/pytorch/pytorch/issues/99774#issuecomment-1527949391
    def wrapped(*inputs):
        inputs_functional = pytree.tree_map_only(
            torch.Tensor, torch._to_functional_tensor, inputs
        )
        torch._enable_functionalization(reapply_views=True)
        try:
            out = function(*inputs_functional)
        finally:
            torch._disable_functionalization()

        flat_inputs_functional = pytree.tree_leaves(inputs_functional)
        for input_functional in flat_inputs_functional:
            if isinstance(input_functional, torch.Tensor):
                torch._sync(input_functional)
        pytree.tree_map(torch._sync, out)
        out_unwrapped = pytree.tree_map(torch._from_functional_tensor, out)
        return out_unwrapped

    return wrapped


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/onnx/_internal/exporter/_capture_strategies.py
# Occurrences: Lines 139-145 (3 instances)

def _enter(self, model: torch.nn.Module | torch.jit.ScriptFunction) -> None:
    return


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/torch_version.py
# Line: 32

def _convert_to_version(self, inp: Any) -> Any:
    if isinstance(inp, Version):
        return inp
    elif isinstance(inp, str):
        return Version(inp)
    elif isinstance(inp, Iterable):
        # Ideally this should work for most cases by attempting to group
        # the version tuple, assuming the tuple looks (MAJOR, MINOR, ?PATCH)
        # Examples:
        #   * (1)         -> Version("1")
        #   * (1, 20)     -> Version("1.20")
        #   * (1, 20, 1)  -> Version("1.20.1")
        return Version(".".join(str(item) for item in inp))
    else:
        raise InvalidVersion(inp)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/functional_tensor.py
# Line: 163

def __torch_dispatch__(self, func, types, args=(), kwargs=None):
    unrecognized_types = [
        t
        for t in types
        if t not in [torch.Tensor, torch._subclasses.FakeTensor, FunctionalTensor]
    ]
    if unrecognized_types:
        not_implemented_log.debug(
            "FunctionalTensor unrecognized subclass(es): %s", unrecognized_types
        )
        return NotImplemented

    if kwargs is None:
        kwargs = {}

    # FunctionalTensor needs to plumb all metadata requests to the inner tensor.
    # In theory we don't have to do this - but if we want to service metadata requests here,
    # we need to carefully make sure all metadata is accurate (including metadata mutations)
    if func in FunctionalTensor.metadata_fns:
        # All metadata accesses should be plumbed to the inner tensor, that way we don't have to worry
        # about the problem of keeping metadata in sync between the wrapper and inner tensor.
        # This also alleviates us from having to manually handle metadata mutations on the wrapper.
        assert len(kwargs) == 0
        if func in [
            torch.ops.aten.is_strides_like_format.default,
            torch.ops.aten.is_contiguous.memory_format,
        ]:
            assert len(args) == 2 and isinstance(args[0], FunctionalTensor)
            return func(torch._from_functional_tensor(args[0].elem), args[1])
        assert len(args) == 1 and isinstance(args[0], FunctionalTensor)

        return func(torch._from_functional_tensor(args[0].elem))
    # Originally I tried to implement my subclass without giving it a torch_dispatch, but I gave up:
    # - _make_wrapper_subclass requires a __torch_dispatch__
    # - If we want to use _make_subclass(), we have a problem: the subclass will share a TensorImpl with the inner tensor,
    #   which is of type FunctionalTensorWrapper! We explicitly do not want our wrapper to be a FunctionalTensorWrapper.
    # - If we use the default tensor.__new__(), we have another problem: it returns inner_tensor.alias(),
    #   which causes every subclass created above autograd to have autograd view metadata
    #   (in addition to also being a FunctionalTensorWrapper).
    raise RuntimeError(
        "Attempting to use FunctionalTensor on its own. Instead, please use it with a corresponding FunctionalTensorMode()"
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_subclasses/fake_tensor.py
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
# File: /root/ecooptimizer/pytorch/torch/serialization.py
# Line: 1127

def persistent_id(self, obj):
    return persistent_id(obj)


# ==================================================
# Line: 1209

def persistent_id(self, obj):
    return persistent_id(obj)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/transforms.py
# Line: 203

def forward_shape(self, shape):
    """
    Infers the shape of the forward computation, given the input shape.
    Defaults to preserving shape.
    """
    return shape


# ==================================================
# Line: 210

def inverse_shape(self, shape):
    """
    Infers the shapes of the inverse computation, given the output shape.
    Defaults to preserving shape.
    """
    return shape



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributions/bernoulli.py
# Line: 140

def _log_normalizer(self, x):
    return torch.log1p(torch.exp(x))

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_tensor.py
# Line: 761

def reinforce(self, reward):
    def trim(str):
        return "\n".join([line.strip() for line in str.split("\n")])

    raise RuntimeError(
        trim(
            r"""reinforce() was removed.
        Use torch.distributions instead.
        See https://pytorch.org/docs/main/distributions.html

        Instead of:

        probs = policy_network(state)
        action = probs.multinomial()
        next_state, reward = env.step(action)
        action.reinforce(reward)
        action.backward()

        Use:

        probs = policy_network(state)
        # NOTE: categorical is equivalent to what used to be called multinomial
        m = torch.distributions.Categorical(probs)
        action = m.sample()
        next_state, reward = env.step(action)
        loss = -m.log_prob(action) * reward
        loss.backward()
    """
        )
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nested/_internal/nested_int.py
# Occurrences: Lines 45-57 (5 instances)

def maybe_as_int(self) -> Optional[int]:
    return None


# ==================================================
# Line: 105

def is_symbolic(self) -> bool:
    return False


# ==================================================
# Occurrences: Lines 111-114 (2 instances)

def is_constant(self) -> bool:
    return False


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_library/fake_impl.py
# Line: 31

def kernel(self, value):
    raise RuntimeError("Unable to directly set kernel.")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/unflatten.py
# Line: 1458

def _is_mutable(self, target):
    if isinstance(target, torch._ops.OpOverload):
        return target._schema.is_mutable
    return False


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/_draft_export.py
# Line: 220

def _hash(self, element: tuple[str, dict[str, Any]]) -> int:
    key, data = element

    if key == "missing_fake_kernel":
        return hash((key, data["op"]))
    elif key == "mismatched_fake_kernel":
        return hash((key, data["op"], data["reason"]))
    elif key == "propagate_real_tensors_provenance":
        return hash((key, json.dumps(data["user_stack"])))
    elif key == "guard_added":
        return hash((key, json.dumps(data["user_stack"])))
    elif key == "create_unbacked_symbol":
        return hash((key, json.dumps(data["user_stack"])))

    return hash((key, json.dumps(data)))


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/export/exported_program.py
# Line: 954

def graph_module(self, value):
    raise RuntimeError("Unable to set ExportedProgram's graph_module attribute.")


# ==================================================
# Line: 964

def graph(self, value):
    raise RuntimeError("Unable to set ExportedProgram's graph attribute.")


# ==================================================
# Line: 974

def graph_signature(self, value):
    raise RuntimeError("Unable to set ExportedProgram's graph_signature attribute.")


# ==================================================
# Line: 984

def state_dict(self, value):
    raise RuntimeError("Unable to set ExportedProgram's state_dict attribute.")


# ==================================================
# Line: 1032

def range_constraints(self, value):
    raise RuntimeError(
        "Unable to set ExportedProgram's range_constraints attribute."
    )


# ==================================================
# Line: 1044

def module_call_graph(self, value):
    raise RuntimeError(
        "Unable to set ExportedProgram's module_call_graph attribute."
    )


# ==================================================
# Line: 1096

def call_spec(self, value):
    raise RuntimeError("Unable to set ExportedProgram's call_spec attribute.")


# ==================================================
# Line: 1106

def verifier(self, value):
    raise RuntimeError("Unable to set ExportedProgram's verifier attribute.")


# ==================================================
# Line: 1117

def dialect(self, value):
    raise RuntimeError("Unable to set ExportedProgram's dialect attribute.")


# ==================================================
# Line: 1127

def verifiers(self, value):
    raise RuntimeError("Unable to set ExportedProgram's verifiers attribute.")


# ==================================================
# Line: 1137

def tensor_constants(self, value):
    raise RuntimeError(
        "Unable to set ExportedProgram's tensor_constants attribute."
    )


# ==================================================
# Line: 1149

def constants(self, value):
    raise RuntimeError("Unable to set ExportedProgram's constants attribute.")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/profiler/_pattern_matcher.py
# Line: 105

def root_of(self, event: _ProfilerEvent):
    while event.parent:
        event = event.parent
    return event


# ==================================================
# Line: 126

def go_up_until(self, event: _ProfilerEvent, predicate):
    if not event:
        return None
    while event.parent and not predicate(event):
        event = event.parent
    return event



# ==================================================
# Line: 218

def benchmark(self, events: list[_ProfilerEvent]):
    shapes_factor_map = {input_shapes(event): 0.0 for event in events}
    for shape in shapes_factor_map:
        size = shape[0]
        to_timer = benchmark.Timer(
            stmt='torch.ones(size).to("cuda")', globals={"size": size}
        )
        de_timer = benchmark.Timer(
            stmt='torch.ones(size, device="cuda")', globals={"size": size}
        )
        to_time = to_timer.timeit(10).mean
        de_time = de_timer.timeit(10).mean
        shapes_factor_map[shape] = de_time / to_time
    return shapes_factor_map



# ==================================================
# Line: 329

def benchmark(self, events: list[_ProfilerEvent]):
    shapes_factor_map = {input_shapes(event): 0.0 for event in events}
    for shape in shapes_factor_map:
        matrixA = torch.randn(shape[0], device="cuda", dtype=torch.float32)
        matrixB = torch.randn(shape[1], device="cuda", dtype=torch.float32)
        fp32_timer = benchmark.Timer(
            stmt="torch.mm(matrixA, matrixB)",
            globals={"matrixA": matrixA, "matrixB": matrixB},
        )
        tf32_timer = benchmark.Timer(
            stmt="torch.mm(matrixA, matrixB)",
            setup="torch.backends.cuda.matmul.allow_tf32 = True",
            globals={"matrixA": matrixA, "matrixB": matrixB},
        )
        torch.backends.cuda.matmul.allow_tf32 = False
        fp32_time = fp32_timer.timeit(10).mean
        tf32_time = tf32_timer.timeit(10).mean
        shapes_factor_map[shape] = tf32_time / fp32_time
    return shapes_factor_map



# ==================================================
# Line: 556

def benchmark(self, events: list[_ProfilerEvent]):
    def closest_multiple(shapes, multiple):
        return [multiple * math.ceil(shape / multiple) for shape in shapes]

    shapes_factor_map = {input_shapes(event): 0.0 for event in events}
    for shape in shapes_factor_map:
        matrixA = torch.randn(shape[0], device="cuda", dtype=torch.float16)
        matrixB = torch.randn(shape[1], device="cuda", dtype=torch.float16)
        not_aligned_dim_timer = benchmark.Timer(
            stmt="torch.mm(matrixA, matrixB)",
            globals={"matrixA": matrixA, "matrixB": matrixB},
        )
        matrixA = torch.randn(
            closest_multiple(shape[0], 8), device="cuda", dtype=torch.float16
        )
        matrixB = torch.randn(
            closest_multiple(shape[1], 8), device="cuda", dtype=torch.float16
        )
        aligned_dim_timer = benchmark.Timer(
            stmt="torch.mm(matrixA, matrixB)",
            globals={"matrixA": matrixA, "matrixB": matrixB},
        )
        not_aligned_dim_time = not_aligned_dim_timer.timeit(10).mean
        aligned_dim_time = aligned_dim_timer.timeit(10).mean
        shapes_factor_map[shape] = aligned_dim_time / not_aligned_dim_time
    return shapes_factor_map



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/profiler/profiler.py
# Line: 344

def add_metadata(self, key: str, value: str):
    """
    Adds a user defined metadata with a string key and a string value
    into the trace file
    """
    wrapped_value = '"' + value.replace('"', '\\"') + '"'
    torch.autograd._add_metadata_json(key, wrapped_value)


# ==================================================
# Line: 352

def add_metadata_json(self, key: str, value: str):
    """
    Adds a user defined metadata with a string key and a valid json value
    into the trace file
    """
    torch.autograd._add_metadata_json(key, value)


# ==================================================
# Line: 367

def _get_distributed_info(self):
    import torch.distributed as dist

    if not dist.is_available() or not dist.is_initialized():
        return None

    backend = dist.get_backend()
    dist_info = {
        "backend": backend,
        "rank": dist.get_rank(),
        "world_size": dist.get_world_size(),
        "pg_count": dist.get_pg_count(),
        "pg_config": dist.distributed_c10d._get_all_pg_configs(),
    }
    if backend == "nccl":
        nccl_version = torch.cuda.nccl.version()
        dist_info["nccl_version"] = ".".join(str(v) for v in nccl_version)
    return dist_info


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/comptime.py
# Line: 190

def graph_break(self, msg="ComptimeContext.graph_break"):
    """
    Manually trigger a graph break
    """
    unimplemented_v2(
        gb_type="ComptimeContext graph break",
        context=msg,
        explanation=f"Manually triggered ComptimeContext graph break with message {msg}.",
        hints=[],
    )


# ==================================================
# Line: 208

def assert_static(self, val):
    """
    Asserts that the int is static (and not dynamic, per dynamic shapes)
    """
    assert not val.is_dynamic(), (
        "expected static but got dynamic (run with TORCH_LOGS=dynamic for more info)"
    )


# ==================================================
# Line: 234

def print(self, val, *, file=None):
    print(repr(val), file=file)


# ==================================================
# Line: 319

def sleep(self, sec):
    time.sleep(sec)



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/backends/distributed.py
# Occurrences: Lines 399-402 (2 instances)

def _ignore_parameter(self, parameter):
    return hasattr(parameter, "_ddp_ignored") and parameter._ddp_ignored


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/utils.py
# Line: 1880

def _log_timed_event(
    self,
    event_name: str,
    time_ns: int,
    phase: str,
    metadata: Optional[dict[str, Any]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/test_minifier_common.py
# Line: 43

def _get_module(self, t):
    match = re.search(r"class Repro\(torch\.nn\.Module\):\s+([ ].*\n| *\n)+", t)
    assert match is not None, "failed to find module"
    r = match.group(0)
    r = re.sub(r"\s+$", "\n", r, flags=re.MULTILINE)
    r = re.sub(r"\n{3,}", "\n\n", r)
    return r.strip()


# ==================================================
# Line: 102

def _gen_codegen_fn_patch_code(self, device, bug_type):
    assert bug_type in ("compile_error", "runtime_error", "accuracy")
    return f"""\

# ==================================================
# Line: 110

def _maybe_subprocess_run(self, args, *, isolate, cwd=None):
    if not isolate:
        assert len(args) >= 2, args
        assert args[0] == "python3", args
        if args[1] == "-c":
            assert len(args) == 3, args
            code = args[2]
            args = ["-c"]
        else:
            assert len(args) >= 2, args
            with open(args[1]) as f:
                code = f.read()
            args = args[1:]

        # WARNING: This is not a perfect simulation of running
        # the program out of tree.  We only interpose on things we KNOW we
        # need to handle for tests.  If you need more stuff, you will
        # need to augment this appropriately.

        # NB: Can't use save_config because that will omit some fields,
        # but we must save and reset ALL fields
        dynamo_config = torch._dynamo.config.get_config_copy()
        inductor_config = torch._inductor.config.get_config_copy()
        try:
            stderr = io.StringIO()
            log_handler = logging.StreamHandler(stderr)
            log = logging.getLogger("torch._dynamo")
            log.addHandler(log_handler)
            try:
                prev_cwd = _as_posix_path(os.getcwd())
                if cwd is not None:
                    cwd = _as_posix_path(cwd)
                    os.chdir(cwd)
                with patch("sys.argv", args), report_compile_source_on_error():
                    exec(code, {"__name__": "__main__", "__compile_source__": code})
                rc = 0
            except Exception:
                rc = 1
                traceback.print_exc(file=stderr)
            finally:
                log.removeHandler(log_handler)
                if cwd is not None:
                    os.chdir(prev_cwd)  # type: ignore[possibly-undefined]
                # Make sure we don't leave buggy compiled frames lying
                # around
                torch._dynamo.reset()
        finally:
            torch._dynamo.config.load_config(dynamo_config)
            torch._inductor.config.load_config(inductor_config)

        # TODO: return a more appropriate data structure here
        return subprocess.CompletedProcess(
            args,
            rc,
            b"",
            stderr.getvalue().encode("utf-8"),
        )
    else:
        if cwd is not None:
            cwd = _as_posix_path(cwd)
        return subprocess.run(args, capture_output=True, cwd=cwd, check=False)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/side_effects.py
# Line: 286

def is_attribute_mutation(self, item):
    return isinstance(item.mutation_type, AttributeMutation)


# ==================================================
# Line: 371

def get_variable_cls(self, user_cls):
    from torch.overrides import TorchFunctionMode

    from .variables.ctx_manager import GenericContextWrappingVariable
    from .variables.torch_function import TorchFunctionModeVariable
    from .variables.user_defined import is_forbidden_context_manager

    variable_cls: type[variables.UserDefinedObjectVariable] = (
        variables.UserDefinedObjectVariable
    )
    if issubclass(
        user_cls, TorchFunctionMode
    ) and TorchFunctionModeVariable.is_supported_torch_function_mode(user_cls):
        variable_cls = TorchFunctionModeVariable
    elif (
        hasattr(user_cls, "__enter__")
        and hasattr(user_cls, "__exit__")
        and not is_forbidden_context_manager(user_cls)
    ):
        variable_cls = GenericContextWrappingVariable
    elif issubclass(user_cls, torch.nn.Module):
        variable_cls = variables.UnspecializedNNModuleVariable
    elif issubclass(user_cls, (dict, collections.OrderedDict)):
        variable_cls = variables.UserDefinedDictVariable
    elif issubclass(user_cls, tuple):
        variable_cls = variables.UserDefinedTupleVariable
    elif issubclass(user_cls, list):
        variable_cls = variables.UserDefinedListVariable
    elif issubclass(user_cls, MutableMapping):
        variable_cls = variables.MutableMappingVariable
    elif is_frozen_dataclass(user_cls):
        variable_cls = FrozenDataClassVariable
    elif issubclass(user_cls, BaseException):
        variable_cls = variables.UserDefinedExceptionObjectVariable
    assert issubclass(variable_cls, variables.UserDefinedObjectVariable)
    return variable_cls


# ==================================================
# Line: 408

def get_example_value(
    self,
    base_cls_vt,
    cls_vt,
    init_args,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/guards.py
# Line: 297

def get_guard_lines(self, guard):
    guard_name = guard.__class__.__name__
    parts = guard.verbose_code_parts()
    parts = [guard_name + ": " + part for part in parts]
    return parts


# ==================================================
# Line: 303

def get_manager_line(self, guard_manager, accessor_str=None):
    source = guard_manager.get_source()
    t = guard_manager.__class__.__name__
    s = t + ": source=" + source
    if accessor_str:
        s += ", " + accessor_str
    return s


# ==================================================
# Line: 948

def manager_guards_on_keys(self, mgr_enum):
    return mgr_enum == GuardManagerType.DICT_GUARD_MANAGER


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/source.py
# Line: 133

def guard_source(self):
    return GuardSource.LOCAL


# ==================================================
# Line: 147

def guard_source(self):
    return GuardSource.SYNTHETIC_LOCAL


# ==================================================
# Line: 158

def guard_source(self):
    return GuardSource.RANDOM_VALUE


# ==================================================
# Line: 177

def guard_source(self):
    return GuardSource.GLOBAL


# ==================================================
# Line: 196

def guard_source(self):
    return GuardSource.GLOBAL


# ==================================================
# Line: 334

def guard_source(self):
    return GuardSource.EPHEMERAL


# ==================================================
# Line: 343

def is_ephemeral(self):
    return True



# ==================================================
# Line: 586

def is_dict_key(self):
    return True



# ==================================================
# Occurrences: Lines 750-753 (2 instances)

def name(self):
    return ""


# ==================================================
# Line: 778

def guard_source(self):
    return GuardSource.GLOBAL



# ==================================================
# Line: 789

def guard_source(self):
    return GuardSource.CONSTANT


# ==================================================
# Occurrences: Lines 847-850 (2 instances)

def name(self):
    return ""


# ==================================================
# Occurrences: Lines 856-859 (2 instances)

def name(self):
    return ""


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/codegen.py
# Line: 388

def create_binary_subscr(self) -> Instruction:
    return create_instruction("BINARY_SUBSCR")


# ==================================================
# Occurrences: Lines 444-447 (2 instances)

def create_load_const(self, value) -> Instruction:
    return create_load_const(value)


# ==================================================
# Line: 690

def create_delete(self, value) -> Instruction:
    return create_instruction("DELETE_FAST", argval=value)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/symbolic_convert.py
# Line: 1022

def _break_context_reference_cycle(self, val):
    # See test_exceptions::test_raise_does_not_create_context_chain_cycle
    # Based on https://github.com/python/cpython/blob/e635bf2e49797ecb976ce45a67fce2201a25ca68/Python/errors.c#L207-L228
    # As noted on CPython, this is O(chain length) but the context chains
    # are usually very small
    o = slow_o = val
    slow_update_toggle = False  # floyd's algorithm for detecting cycle
    while True:
        context = o.__context__
        if type(context) is ConstantVariable:  # context not set
            break

        if context is val:
            o.set_context(ConstantVariable(None))
            break

        o = context
        if o is slow_o:
            # pre-existing cycle - all exceptions on the path were
            # visited and checked
            break

        if slow_update_toggle:
            slow_o = slow_o.__context__  # visited all exceptions
        slow_update_toggle = not slow_update_toggle


# ==================================================
# Line: 1347

def run_ctx_mgr(self):
    # NB: Don't push the top level frame summary; set_current_loc will
    # take care of it.  However, DO make sure we attach real_stack to
    # exceptions
    return TracingContext.current_frame(None)


# ==================================================
# Line: 1563

def resolve_name(self, name, package, level):
    """
    Copied from the Cpython implementation of __import__
    Resolve a relative module name to an absolute one.
    https://github.com/python/cpython/blob/5a094f0255eea1db58fb2cf14c200971e64ec36e/Lib/importlib/_bootstrap.py#L902
    """
    bits = package.rsplit(".", level - 1)
    if len(bits) < level:
        raise ImportError("attempted relative import beyond top-level package")
    base = bits[0]
    return f"{base}.{name}" if name else base


# ==================================================
# Line: 1861

def _isinstance_exception(self, val):
    return isinstance(
        val,
        (
            variables.ExceptionVariable,
            UserDefinedExceptionClassVariable,
            UserDefinedExceptionObjectVariable,
        ),
    )


# ==================================================
# Line: 2786

def LOAD_BUILD_CLASS(self, inst):
    unimplemented_v2(
        gb_type="LOAD_BUILD_CLASS bytecode not supported",
        context="",
        explanation="Dynamo does not support tracing classes that are defined in the compiled region.",
        hints=[
            "Move the class definition out of the compiled region.",
            *graph_break_hints.SUPPORTABLE,
        ],
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/output_graph.py
# Line: 1139

def _get_stack_values_to_restore(self, tx, stack_pops):
    """
    Gets the stack + locals values belonging to tx that need to be restored.

    Also prunes dead tx locals and realizes all VTs in the tx's stack.

    NullVariables in stack/locals will NOT be restored, unless they are the top `stack_pops`
    elements of the stack - it is expected that the next instruction to run will pop the top
    `stack_pops` elements of the stack, so we should codegen NULLs.

    Returns:
        - stack_values: stack and locals values that need to be restored
        - restore_vars: names of locals corresponding to the locals part of `stack_values`
        - meta: locations of NULLs and ContextWrappingVariables in the stack/locals
            (ignores the top `stack_pops` values on the stack)
    """
    tx.prune_dead_locals()

    stack_values = []
    meta = StackLocalsMetadata()

    # realize any unrealized tensor VTs in case they
    # need to be added to self.nn_modules as attributes
    for i, value in enumerate(tx.stack):
        variables.LazyVariableTracker.realize_all(value)
        # ignore top `stack_pops` values on the stack
        if len(tx.stack) - i <= stack_pops:
            stack_values.append(value)
            continue
        if isinstance(value, NullVariable):
            meta.stack_null_idxes.append(i)
        else:
            stack_values.append(value)
        if isinstance(value, ContextWrappingVariable):
            target_values = (
                () if value.target_values is None else tuple(value.target_values)
            )
            # NOTE: track index in stack after NULLs have been removed
            meta.stack_ctx_args.append((len(stack_values) - 1, target_values))
            meta.stack_ctx_idxes_orig.append(i)

    # Add all the local vars to the "stack" so restore at the end
    restore_vars: list[str] = []
    val_to_names: dict[VariableTracker, list[str]] = {}
    # NB: Typically (i.e., for graph compile from RETURN_VALUE),
    # symbolic_locals will be empty at this point, as prune_dead_locals
    # will clear out all of symbolic_locals because RETURN_VALUE is the
    # last instruction and no more locals are used.  The fanciness here
    # is only needed for partial graphs.
    # NOTE: All cell and free variables are represented as CellVariable,
    # so checks for NULLs and context managers in the case of codegen'ing resume
    # functions will not be performed on them. This is expected behavior.
    for k, v in tx.symbolic_locals.items():
        # Note! this explicitly uses .local_name for matching
        # Failure to do so will cause spurious registrations in val_to_names.
        # This will in turn result in spurious variables showing up in the graph.
        # This was very tricky to debug. For an example, dump the graph at call_user_compiler
        # while running test_subgraphs.py
        if isinstance(v.source, LocalSource) and v.source.local_name == k:
            continue  # no need to restore initial state
        if isinstance(v, CellVariable) and v.local_name == k:
            continue  # no need to restore initial state
        # Do not load variable if it is NULL.
        if sys.version_info >= (3, 12):
            # Continuation function will load the NULL for v.
            if type.__instancecheck__(NullVariable, v):
                meta.locals_null_keys.append(k)
                continue
        else:
            # A variable should never be NULL in < 3.12
            assert not type.__instancecheck__(NullVariable, v)
        if isinstance(v, ContextWrappingVariable):
            target_values = (
                () if v.target_values is None else tuple(v.target_values)
            )
            meta.locals_ctx_args.append((k, target_values))
        if v not in val_to_names:
            val_to_names[v] = []
        val_to_names[v].append(k)
    for v in val_to_names.keys():
        restore_vars.extend(val_to_names[v])
        stack_values.extend([v] * len(val_to_names[v]))

    return stack_values, restore_vars, meta


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/compiled_autograd.py
# Line: 383

def log_compile_reasons(
    self,
    compile_reasons: list[str],

# ==================================================
# Occurrences: Lines 673-678 (2 instances)

def allocate_dummy(self):
    with disable_proxy_modes_tracing():
        # Weird quantity so it's easy to grep
        return torch.zeros([0, 123456789])


# ==================================================
# Line: 825

def move_graph_nodes_to_cuda(self, graph) -> list[int]:
    to_move: dict[int, torch.fx.Node] = {}
    has_cuda_inputs = False
    nodes = list(graph.nodes)
    assert nodes[0].target == "inputs"
    inputs = nodes[0]
    inputs_users = list(inputs.users.keys())
    # input access nodes should immediately follow placeholder nodes
    first_getitem_idx = len(_graph_placeholders)
    assert nodes[first_getitem_idx] == inputs_users[0]
    last_getitem_idx = first_getitem_idx + len(inputs_users) - 1
    assert nodes[last_getitem_idx] == inputs_users[-1]
    # getitem nodes on inputs
    for i, node in enumerate(inputs_users):
        if not has_cuda_inputs and node.meta["val"].device.type == "cuda":
            has_cuda_inputs = True
            continue

        is_cpu = node.meta["val"].device.type == "cpu"
        is_scalar = len(node.meta["val"].size()) == 0
        if is_cpu and is_scalar:
            node_users = list(node.users.keys())
            # We can only move the cpu scalar if it is not exposed to user code.
            if all(
                (
                    isinstance(user.target, torch._ops.OpOverload)
                    and user.target.namespace in ("prims", "aten")
                )
                or (
                    isinstance(user.target, Op)
                    and not user.target.is_custom_function
                )
                for user in node_users
            ):
                # all users are prims/aten, can move safely
                to_move[i] = node

    # only move cpu scalars to cuda if there were cuda activations in this graph,
    # this is to handle the case where cudagraphs is enabled on a cpu-only graph
    if has_cuda_inputs:
        for node in to_move.values():
            verbose_log.debug("Moving node %s from cpu to cuda", node)
            node.meta["val"] = node.meta["val"].cuda()

        # return runtime indices we need to move to cuda
        return list(to_move.keys())

    return []


# ==================================================
# Line: 874

def is_sym_node(self, node):
    return (
        isinstance(node, torch.fx.Node)
        and node.op == "call_function"
        and node.target
        in [torch.ops.aten.sym_size.int, torch.ops.aten.sym_numel.default]
    )


# ==================================================
# Line: 1342

def set_node_origin(
    self,
    node_name: str,
    nodecall_index: int,
    pyobj: Optional[torch.autograd.Function],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/tensor.py
# Occurrences: Lines 608-611 (2 instances)

def _strict_mode_banned_ops(self):
    return torch._dynamo.config._autograd_backward_strict_mode_banned_ops


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/functions.py
# Line: 308

def closure_vars(self, tx):
    return {}



# ==================================================
# Line: 358

def self_args(self):
    return []


# ==================================================
# Line: 574

def has_self(self):
    return False


# ==================================================
# Line: 1156

def self_args(self):
    return []


# ==================================================
# Line: 1211

def has_self(self):
    return False


# ==================================================
# Line: 1938

def exc_info(self, tx):
    if len(tx.exn_vt_stack):
        exn = tx.exn_vt_stack[-1]
        typ = exn.exc_type
        tb = None
        items = [
            VariableTracker.build(tx, typ),
            exn,
            VariableTracker.build(tx, tb),
        ]
    else:
        items = [
            variables.ConstantVariable(None),
            variables.ConstantVariable(None),
            variables.ConstantVariable(None),
        ]
    return variables.TupleVariable(items)


# ==================================================
# Line: 2163

def specialize_symbolic(self, arg: Any) -> Any:
    from .constant import ConstantVariable
    from .tensor import SymNodeVariable

    # See [Note: Specialize tl.constexpr args in user-defined triton kernels]
    if isinstance(arg, SymNodeVariable):
        return ConstantVariable.create(arg.evaluate_expr())
    return arg



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/ctx_manager.py
# Occurrences: Lines 140-143 (2 instances)

def supports_graph_breaks(self):
    return True


# ==================================================
# Occurrences: Lines 192-195 (2 instances)

def supports_graph_breaks(self):
    return False


# ==================================================
# Line: 552

def _call_func(self, tx: "InstructionTranslator", values):
    assert len(values) == 1
    value = values[0]
    # Coalesce grad mode mutations
    if torch.is_grad_enabled() != value:
        tx.output.create_node(
            "call_function", torch._C._set_grad_enabled, (value,), {}
        )
        torch._C._set_grad_enabled(value)


# ==================================================
# Line: 778

def _call_func(self, tx: "InstructionTranslator", values):
    assert len(values) == 1
    value = values[0]
    (
        tx.output.create_node(
            "call_function", torch._C._set_deterministic_algorithms, (value,), {}
        ),
    )
    torch._C._set_deterministic_algorithms(value)


# ==================================================
# Line: 819

def _call_func(self, tx: "InstructionTranslator", values):
    assert len(values) == 1
    value = values[0]
    if value is not None:
        # Disable `saved_tensors_hooks` with message (`value`)
        # OR
        # we are exiting this context and restoring the previous message.
        tx.output.create_node(
            "call_function",
            torch._C._autograd._saved_tensors_hooks_disable,
            (value,),
            {},
        )
        torch._C._autograd._saved_tensors_hooks_disable(value)
    else:
        # We are exiting this context and if prev_message was None, we re-enable `saved_tensors_hooks`.
        tx.output.create_node(
            "call_function", torch._C._autograd._saved_tensors_hooks_enable, (), {}
        )
        torch._C._autograd._saved_tensors_hooks_enable()


# ==================================================
# Line: 1393

def _call_func(self, tx: "InstructionTranslator", values):
    assert len(values) == 1
    value = values[0]
    # manually patch dynamo config
    for key, val in value:
        torch._dynamo.config.__setattr__(key, val)
    # No need to keep track of global side effects because
    # dynamo will properly restore this context manager for
    # unsupported instructions and continuation functions.
    # Dynamo config also should not affect the semantics of the compiled graph.


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/nn_module.py
# Line: 181

def _wrap_submodule(
    self, tx: "InstructionTranslator", source, submod, *key_extra, **options

# ==================================================
# Line: 892

def _wrap_source(self, attr_source):
    # the vt is already wrapped with UnspecializedNNModuleSource
    return attr_source


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/builder.py
# Line: 453

def _can_lift_attrs_to_inputs(self, vt):
    return type(vt) in {
        TensorVariable,
        TensorWithTFOverrideVariable,
        UserDefinedObjectVariable,
        NumpyNdarrayVariable,
    }


# ==================================================
# Line: 526

def wrap_removable_handle(self, value):
    # This means that the removable handle was created in some other frame.
    # Our current infra requires the hook to be registered and removed in
    # the same frame. So graph break.
    # Related test - PYTORCH_TEST_WITH_DYNAMO=1 python test/test_autograd.py -k TestAutograd.test_hooks
    unimplemented_v2(
        gb_type="Attempted to represent unregistered RemovableHandle",
        context="",
        explanation="Dynamo attempted to build a representation of a torch.utils.hooks.RemovableHandle, "
        "which is not supported. This happens because the RemovableHandle was created in another frame.",
        hints=[],
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/base.py
# Line: 568

def is_realized(self):
    """Used by LazyVariableTracker to indicate an unrealized node"""
    return True


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/builtin.py
# Occurrences: Lines 770-773 (2 instances)

def constant_args(self, *args, **kwargs):
    return check_constant_args(args, kwargs)


# ==================================================
# Line: 781

def tensor_args_type(self, arg_types):
    any_tensor = False
    for arg_type in arg_types:
        if issubclass(arg_type, variables.GetAttrVariable):
            return False
        any_tensor = any_tensor or issubclass(arg_type, variables.TensorVariable)
    return any_tensor


# ==================================================
# Line: 1306

def call_str(self, tx: "InstructionTranslator", arg):
    # Handle `str` on a user defined function or object
    if isinstance(arg, (variables.UserFunctionVariable)):
        return variables.ConstantVariable.create(value=str(arg.fn))
    elif isinstance(arg, (variables.UserDefinedObjectVariable)):
        # Check if object has __str__ method
        if hasattr(arg.value, "__str__"):
            str_method = arg.value.__str__
        elif hasattr(arg.value, "__repr__"):
            # account for __repr__ functions when __str__ is absent
            str_method = arg.value.__repr__
        else:
            unimplemented_v2(
                gb_type="failed to call str() on user defined object",
                context=str(arg),
                explanation="User defined object has no __str__ or __repr__ method",
                hints=[*graph_break_hints.USER_ERROR],
            )

        if type(arg.value).__str__ is object.__str__:
            # Rely on the object str method
            try:
                return variables.ConstantVariable.create(value=str_method())
            except AttributeError:
                # Graph break
                return
        elif is_wrapper_or_member_descriptor(str_method):
            unimplemented_v2(
                gb_type="Attempted to a str() method implemented in C/C++",
                context="",
                explanation=f"{type(arg.value)} has a C/C++ based str method. This is not supported.",
                hints=["Write the str method in Python"],
            )
        else:
            # Overrides for custom str method
            # Pass method as function to call tx.inline_user_function_return
            bound_method = str_method.__func__  # type: ignore[attr-defined]

            try:
                # Only supports certain function types
                user_func_variable = variables.UserFunctionVariable(bound_method)
            except AssertionError as e:
                # Won't be able to do inline the str method, return to avoid graph break
                log.warning("Failed to create UserFunctionVariable: %s", e)
                return

            # Inline the user function
            return tx.inline_user_function_return(user_func_variable, [arg], {})
    elif isinstance(arg, (variables.ExceptionVariable,)):
        if len(arg.args) == 0:
            value = f"{arg.exc_type}"
        else:
            value = ", ".join(a.as_python_constant() for a in arg.args)
        return variables.ConstantVariable.create(value=value)


# ==================================================
# Line: 1479

def call_abs(self, tx: "InstructionTranslator", arg: "VariableTracker"):
    # Call arg.__abs__()
    abs_method = BuiltinVariable(getattr).call_function(
        tx, [arg, ConstantVariable.create("__abs__")], {}
    )
    return abs_method.call_function(tx, [], {})


# ==================================================
# Line: 1486

def call_pos(self, tx: "InstructionTranslator", arg: "VariableTracker"):
    # Call arg.__pos__()
    pos_method = BuiltinVariable(getattr).call_function(
        tx, [arg, ConstantVariable.create("__pos__")], {}
    )
    return pos_method.call_function(tx, [], {})


# ==================================================
# Line: 1493

def call_index(self, tx: "InstructionTranslator", arg: "VariableTracker"):
    if isinstance(arg, variables.TensorVariable):
        unimplemented_v2(
            gb_type="unsupported index(Tensor)",
            context="",
            explanation="Dynamo does not support tracing builtin index() on a Tensor",
            hints=[],
        )

    arg = guard_if_dyn(arg)
    constant_value = operator.index(arg)
    return variables.ConstantVariable.create(constant_value)


# ==================================================
# Line: 1506

def call_round(self, tx: "InstructionTranslator", arg, *args, **kwargs):
    # Call arg.__round__()
    round_method = BuiltinVariable(getattr).call_function(
        tx, [arg, ConstantVariable.create("__round__")], {}
    )
    return round_method.call_function(tx, args, kwargs)


# ==================================================
# Occurrences: Lines 1524-1529 (2 instances)

def _dynamic_args(self, *args, **kwargs):
    return any(isinstance(x, SymNodeVariable) for x in args) or any(
        isinstance(x, SymNodeVariable) for x in kwargs.values()
    )


# ==================================================
# Line: 1619

def call_callable(self, tx: "InstructionTranslator", arg):
    from .functions import BaseUserFunctionVariable, FunctoolsPartialVariable
    from .nn_module import NNModuleVariable

    if isinstance(
        arg,
        (
            variables.UserDefinedClassVariable,
            BaseUserFunctionVariable,
            FunctoolsPartialVariable,
            NNModuleVariable,
        ),
    ):
        return variables.ConstantVariable.create(True)
    elif isinstance(arg, UserDefinedVariable):
        return variables.ConstantVariable.create(callable(arg.value))
    elif isinstance(
        arg,
        (
            ConstantVariable,
            SymNodeVariable,
            TensorVariable,
            ListVariable,
            TupleVariable,
            ListIteratorVariable,
        ),
    ):
        return variables.ConstantVariable.create(False)


# ==================================================
# Line: 1648

def call_cast(self, _, *args, **kwargs):
    if len(args) == 2:
        return args[1]

    unimplemented_v2(
        gb_type="bad args to builtin cast()",
        context=f"got args {args} {kwargs}",
        explanation="Dynamo expects exactly 2 args to builtin cast().",
        hints=["Ensure your call to cast() has exactly 2 arguments."],
    )


# ==================================================
# Line: 1659

def call_dict(self, tx: "InstructionTranslator", *args, **kwargs):
    return BuiltinVariable.call_custom_dict(tx, dict, *args, **kwargs)


# ==================================================
# Line: 1716

def call_set(self, tx: "InstructionTranslator", *args, **kwargs):
    # Can we merge this implementation and call_dict's one?
    assert not kwargs
    if not args:
        return SetVariable([], mutation_type=ValueMutationNew())
    if len(args) != 1:
        raise_observed_exception(
            TypeError,
            tx,
            args=[
                ConstantVariable.create(
                    f"set() takes 1 positional argument but {len(args)} were given"
                )
            ],
        )
    arg = args[0]
    if isinstance(arg, variables.SetVariable):
        return arg.clone(mutation_type=ValueMutationNew())
    elif arg.has_force_unpack_var_sequence(tx):
        items = arg.force_unpack_var_sequence(tx)
        return SetVariable(items, mutation_type=ValueMutationNew())
    elif isinstance(arg, variables.UserDefinedObjectVariable) and isinstance(
        arg.value, KeysView
    ):
        iter_fn = arg.var_getattr(tx, "__iter__")
        if isinstance(iter_fn, variables.UserMethodVariable):
            out = tx.inline_user_function_return(iter_fn, args, kwargs)
            if isinstance(out, SetVariable):
                return out
            return BuiltinVariable(set).call_set(tx, out)
    raise_observed_exception(
        TypeError,
        tx,
        args=[ConstantVariable.create("failed to construct builtin set()")],
    )


# ==================================================
# Line: 1752

def call_frozenset(self, tx: "InstructionTranslator", *args, **kwargs):
    assert not kwargs
    if not args:
        return FrozensetVariable([])
    if len(args) != 1:
        raise_observed_exception(
            TypeError,
            tx,
            args=[
                ConstantVariable.create(
                    f"frozenset() takes 1 positional argument but {len(args)} were given"
                )
            ],
        )
    arg = args[0]
    if isinstance(arg, variables.FrozensetVariable):
        return FrozensetVariable([x.vt for x in arg.set_items])
    elif arg.has_unpack_var_sequence(tx):
        items = arg.unpack_var_sequence(tx)
        return FrozensetVariable(items)
    raise_observed_exception(
        TypeError,
        tx,
        args=[ConstantVariable.create("failed to construct builtin frozenset()")],
    )


# ==================================================
# Line: 1778

def call_zip(self, tx: "InstructionTranslator", *args, **kwargs):
    if kwargs:
        assert len(kwargs) == 1 and "strict" in kwargs
    strict = kwargs.pop("strict", False)
    args = [
        arg.unpack_var_sequence(tx) if arg.has_unpack_var_sequence(tx) else arg
        for arg in args
    ]
    return variables.ZipVariable(
        args, strict=strict, mutation_type=ValueMutationNew()
    )


# ==================================================
# Line: 1790

def call_len(self, tx: "InstructionTranslator", *args, **kwargs):
    try:
        return args[0].call_method(tx, "__len__", args[1:], kwargs)
    except AttributeError as e:
        raise_observed_exception(type(e), tx, args=list(e.args))


# ==================================================
# Occurrences: Lines 1796-1799 (2 instances)

def call_getitem(self, tx: "InstructionTranslator", *args, **kwargs):
    return args[0].call_method(tx, "__getitem__", args[1:], kwargs)


# ==================================================
# Line: 1901

def call_issubclass(self, tx: "InstructionTranslator", left_ty, right_ty):
    """Checks if first arg is subclass of right arg"""
    try:
        left_ty_py = left_ty.as_python_constant()
        right_ty_py = right_ty.as_python_constant()
    except NotImplementedError:
        unimplemented_v2(
            gb_type="issubclass() with non-constant arguments",
            context=f"issubclass({left_ty}, {right_ty})",
            explanation="issubclass() with non-constant arguments not supported.",
            hints=[
                "Make sure your arguments are types.",
                *graph_break_hints.USER_ERROR,
            ],
        )

    # WARNING: This might run arbitrary user code `__subclasscheck__`.
    # See the comment in call_isinstance above.
    return variables.ConstantVariable(issubclass(left_ty_py, right_ty_py))


# ==================================================
# Occurrences: Lines 1921-1924 (2 instances)

def call_super(self, tx: "InstructionTranslator", a, b):
    return variables.SuperVariable(a, b)


# ==================================================
# Line: 1933

def call_hasattr(self, tx: "InstructionTranslator", obj, attr):
    if attr.is_python_constant():
        name = attr.as_python_constant()
        if isinstance(obj, variables.BuiltinVariable):
            return variables.ConstantVariable(hasattr(obj.fn, name))
        return obj.call_obj_hasattr(tx, name)


# ==================================================
# Line: 1940

def call_map(self, tx: "InstructionTranslator", fn, *seqs):
    seqs = [
        seq.unpack_var_sequence(tx) if seq.has_unpack_var_sequence(tx) else seq
        for seq in seqs
    ]
    return variables.MapVariable(fn, seqs, mutation_type=ValueMutationNew())


# ==================================================
# Line: 1947

def call_filter(self, tx: "InstructionTranslator", fn, seq):
    seq = seq.unpack_var_sequence(tx) if seq.has_unpack_var_sequence(tx) else seq
    return variables.FilterVariable(fn, seq, mutation_type=ValueMutationNew())


# ==================================================
# Line: 2105

def call_setattr(
    self,
    tx: "InstructionTranslator",
    obj: VariableTracker,
    name_var: VariableTracker,
    val: VariableTracker,

# ==================================================
# Line: 2252

def call_delattr(
    self,
    tx: "InstructionTranslator",
    obj: VariableTracker,
    name_var: VariableTracker,

# ==================================================
# Line: 2260

def call_type(self, tx: "InstructionTranslator", obj: VariableTracker):
    try:
        py_type = obj.python_type()
    except NotImplementedError as error:
        raise UserError(
            UserErrorType.INVALID_INPUT,
            str(error),
            case_name="unknown_python_type",
        ) from None

    source = obj.source and TypeSource(obj.source)
    if (
        source is None
        and isinstance(obj, variables.UserDefinedObjectVariable)
        and obj.cls_source
    ):
        source = obj.cls_source
    if py_type is torch.Tensor:
        # In some cases torch isn't available in globals
        name = tx.output.install_global_by_id("", torch)
        source = AttrSource(GlobalSource(name), "Tensor")

    return VariableTracker.build(tx, py_type, source)


# ==================================================
# Occurrences: Lines 2284-2289 (2 instances)

def call_reversed(self, tx: "InstructionTranslator", obj: VariableTracker):
    if obj.has_unpack_var_sequence(tx):
        items = list(reversed(obj.unpack_var_sequence(tx)))
        return variables.TupleVariable(items)


# ==================================================
# Line: 2306

def call_neg(self, tx: "InstructionTranslator", a):
    if isinstance(a, SymNodeVariable):
        return SymNodeVariable.create(
            tx,
            (operator.neg)(a.as_proxy()),
            sym_num=None,
        )
    # None no-ops this handler and lets the driving function proceed
    return None


# ==================================================
# Occurrences: Lines 2316-2321 (2 instances)

def call_format(self, tx: "InstructionTranslator", _format_string, *args, **kwargs):
    format_string = _format_string.as_python_constant()
    format_string = str(format_string)
    return variables.StringFormatVariable.create(format_string, args, kwargs)


# ==================================================
# Line: 2355

def call_deepcopy(self, tx: "InstructionTranslator", x):
    unimplemented_v2(
        gb_type="copy.deepcopy()",
        context=f"copy.deepcopy({x})",
        explanation="Dynamo does not support copy.deepcopy()",
        hints=[
            "Avoid calling copy.deepcopy()",
            *graph_break_hints.SUPPORTABLE,
        ],
    )


# ==================================================
# Line: 2446

def call_and_(self, tx: "InstructionTranslator", a, b):
    # Rely on constant_handler
    if isinstance(a, ConstantVariable) and isinstance(b, ConstantVariable):
        return None
    if isinstance(a, (SymNodeVariable, ConstantVariable)) and isinstance(
        b, (SymNodeVariable, ConstantVariable)
    ):
        return SymNodeVariable.create(
            tx,
            tx.output.create_proxy(
                "call_function", operator.and_, *proxy_args_kwargs([a, b], {})
            ),
            sym_num=None,
        )
    if hasattr(a, "set_items") and hasattr(b, "set_items"):
        return SetVariable(list(a.set_items & b.set_items))
    # None no-ops this handler and lets the driving function proceed


# ==================================================
# Line: 2466

def call_or_(self, tx: "InstructionTranslator", a, b):
    # Rely on constant_handler
    if isinstance(a, ConstantVariable) and isinstance(b, ConstantVariable):
        return None
    if isinstance(a, (SymNodeVariable, ConstantVariable)) and isinstance(
        b, (SymNodeVariable, ConstantVariable)
    ):
        return SymNodeVariable.create(
            tx,
            tx.output.create_proxy(
                "call_function", operator.or_, *proxy_args_kwargs([a, b], {})
            ),
            sym_num=None,
        )
    if hasattr(a, "set_items") and hasattr(b, "set_items"):
        return SetVariable(list(a.set_items | b.set_items))
    # This call looks like `{"one": torch.ones(1)} | {"two": torch.ones(2)}`.
    if isinstance(a, ConstDictVariable):
        return a.call_method(tx, "__or__", args=[b], kwargs={})
    # None no-ops this handler and lets the driving function proceed
    return None


# ==================================================
# Line: 2490

def call_not_(self, tx: "InstructionTranslator", a):
    if isinstance(a, SymNodeVariable):
        return SymNodeVariable.create(
            tx,
            tx.output.create_proxy(
                "call_function", operator.not_, *proxy_args_kwargs([a], {})
            ),
            sym_num=None,
        )

    # Unwrap the underlying ConstDictVariable
    if isinstance(a, DictViewVariable):
        a = a.dv_dict
    if isinstance(a, (ListVariable, ConstDictVariable)):
        return ConstantVariable.create(len(a.items) == 0)

    return None


# ==================================================
# Line: 2508

def call_contains(
    self, tx: "InstructionTranslator", a: VariableTracker, b: VariableTracker

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/user_defined.py
# Line: 291

def _call_cross_entropy_loss(self, tx: "InstructionTranslator", args, kwargs):
    """
    functional: input, target, weight=None, size_average=None, ignore_index=- 100, reduce=None, reduction='mean',
    label_smoothing=0.0

    non functional ctor: weight=None, size_average=None, ignore_index=- 100, reduce=None, reduction='mean',
    label_smoothing=0.0

    non functional loss call: input, target, optional_output
    """
    from . import ConstantVariable

    def normalize_args(
        weight=ConstantVariable.create(None),
        size_average=ConstantVariable.create(None),
        ignore_index=ConstantVariable.create(-100),
        reduce=ConstantVariable.create(None),
        reduction=ConstantVariable.create("mean"),
        label_smoothing=ConstantVariable.create(0.0),
    ):
        return (
            weight,
            size_average,
            ignore_index,
            reduce,
            reduction,
            label_smoothing,
        )

    (
        weight,
        size_average,
        ignore_index,
        reduce_arg,
        reduction,
        label_smoothing,
    ) = normalize_args(*args, **kwargs)

    def fake_cross_entropy_loss(input, target):
        from .builder import wrap_fx_proxy

        return wrap_fx_proxy(
            tx=tx,
            proxy=tx.output.create_proxy(
                "call_function",
                torch.nn.functional.cross_entropy,
                *proxy_args_kwargs(
                    [
                        input,
                        target,
                        weight,
                        size_average,
                        ignore_index,
                        reduce_arg,
                        reduction,
                        label_smoothing,
                    ],
                    {},
                ),
            ),
        )

    return variables.LambdaVariable(fake_cross_entropy_loss)


# ==================================================
# Line: 797

def is_underlying_vt_modified(self, side_effects):
    return False


# ==================================================
# Line: 1045

def _is_c_defined_property(self, subobj):
    if not isinstance(subobj, property):
        return False

    # pybind def_readwrite is implemented via PyCFunction. At the python level, it is visible as a property whose
    # fget is an instancemethod wrapper - https://docs.python.org/3/c-api/method.html#c.PyInstanceMethod_Check

    # If we have a PyCFunction, we make an assumption that there is no side effect.
    return isinstance(
        subobj.fget, types.BuiltinFunctionType
    ) or torch._C._dynamo.utils.is_instancemethod(subobj.fget)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/lists.py
# Line: 242

def _get_slice_indices(self, length, slice):
    step_is_negative = 0

    if slice.step is None:
        step = 1
        step_is_negative = False
    else:
        step = slice.step
        step_is_negative = slice.step < 0

    # Find lower and upper bounds for start and stop.
    if step_is_negative:
        lower = -1
        upper = length + lower
    else:
        lower = 0
        upper = length

    # Compute start
    if slice.start is None:
        start = upper if step_is_negative else lower
    else:
        start = slice.start

    if start < 0:
        start += length
        if start < lower:
            start = lower
    else:
        if start > upper:
            start = upper

    # Compute stop.
    if slice.stop is None:
        stop = lower if step_is_negative else upper

    else:
        stop = slice.stop

        if stop < 0:
            stop += length
            if stop < lower:
                stop = lower
        else:
            if stop > upper:
                stop = upper

    return [start, stop, step]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/dicts.py
# Line: 299

def is_new_item(self, value, other):
    # compare the id of the realized values if both values are not lazy VTs
    if value and value.is_realized() and other.is_realized():
        return id(value.realize()) != id(other.realize())
    return id(value) != id(other)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/higher_order_ops.py
# Line: 2058

def install_subgraph_in_output_graph(
    self, tx, fn_vt, fn_args_vt, kwargs, body_gmod, attr_name="wrap_body"

# ==================================================
# Line: 2683

def proxy_submod(self, tx, arg):
    assert isinstance(arg.source.base, DictGetItemSource)
    submod_name = tx.output.install_subgraph(arg.source.base.index, arg.value)
    p_submod = make_attr(tx, submod_name)
    set_example_value(p_submod.node, arg.value)
    return p_submod


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/torch_function.py
# Line: 430

def reconstruct_type(self, codegen: "PyCodegen"):
    ty = NoEnterTorchFunctionMode
    codegen(
        AttrSource(
            codegen.tx.import_source(ty.__module__),
            ty.__name__,
        )
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_dynamo/variables/torch.py
# Line: 1555

def is_constant_fold_method(self, name):
    return name in ["has"]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/amp/grad_scaler.py
# Line: 238

def _unscale_grads_(
    self,
    optimizer: torch.optim.Optimizer,
    inv_scale: torch.Tensor,
    found_inf: torch.Tensor,
    allow_fp16: bool,

# ==================================================
# Line: 351

def _maybe_opt_step(
    self,
    optimizer: torch.optim.Optimizer,
    optimizer_state: dict[str, Any],
    *args: Any,
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_guards.py
# Occurrences: Lines 1031-1034 (2 instances)

def is_dict_key(self):
    return False


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_functional_collectives.py
# Line: 599

def __tensor_flatten__(self):
    return ["elem"], None


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/dynamic_rendezvous.py
# Line: 1125

def _create_tcp_store_server(self, master_addr, master_port) -> dist.TCPStore:
    return dist.TCPStore(
        host_name=master_addr,
        port=master_port,
        is_master=True,
        multi_tenant=True,
    )


# ==================================================
# Line: 1377

def _get_deadline(self, timeout: timedelta) -> float:
    return time.monotonic() + timeout.total_seconds()



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/_etcd_stub.py
# Occurrences: Lines 64-72 (3 instances)

def read(self, key: str) -> None:
    raise EtcdStubError


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/etcd_store.py
# Line: 151

def _encode(self, value) -> str:
    if type(value) == bytes:
        return b64encode(value).decode()
    elif type(value) == str:
        return b64encode(value.encode()).decode()
    raise ValueError("Value must be of type str or bytes")


# ==================================================
# Line: 162

def _decode(self, value) -> bytes:
    if type(value) == bytes:
        return b64decode(value)
    elif type(value) == str:
        return b64decode(value.encode())
    raise ValueError("Value must be of type str or bytes")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/rendezvous/etcd_rendezvous_backend.py
# Line: 131

def _decode_state(self, result: etcd.EtcdResult) -> tuple[bytes, Token]:
    base64_state = result.value.encode()

    try:
        state = b64decode(base64_state)
    except binascii.Error as exc:
        raise RendezvousStateError(
            "The state object is corrupt. See inner exception for details."
        ) from exc

    return state, result.modifiedIndex



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/multiprocessing/api.py
# Line: 274

def _make_log_dir(self, log_dir: Optional[str], rdzv_run_id: str):
    base_log_dir = log_dir or tempfile.mkdtemp(prefix="torchelastic_")
    os.makedirs(base_log_dir, exist_ok=True)
    dir = tempfile.mkdtemp(prefix=f"{rdzv_run_id}_", dir=base_log_dir)
    logger.info("log directory set to: %s", dir)
    return dir


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/multiprocessing/errors/__init__.py
# Line: 147

def _get_error_data(self, error_file_data: dict[str, Any]) -> tuple[str, int]:
    message = error_file_data["message"]
    if isinstance(message, str):
        timestamp = int(error_file_data.get("timestamp", 0))
    else:
        timestamp = int(message["extraInfo"]["timestamp"])
    return (message, timestamp)


# ==================================================
# Line: 273

def _format_failure(
    self, idx: int, rank: int, failure: ProcessFailure

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/multiprocessing/errors/error_handler.py
# Line: 36

def _get_error_file_path(self) -> Optional[str]:
    """
    Return the error file path.

    May return ``None`` to have the structured error be logged only.
    """
    return os.environ.get("TORCHELASTIC_ERROR_FILE", None)


# ==================================================
# Line: 44

def initialize(self) -> None:
    """
    Call prior to running code that we wish to capture errors/exceptions.

    Typically registers signal/fault handlers. Users can override this
    function to add custom initialization/registrations that aid in
    propagation/information of errors/signals/exceptions/faults.
    """
    try:
        faulthandler.enable(all_threads=True)
    except Exception as e:
        warnings.warn(f"Unable to enable fault handler. {type(e).__name__}: {e}")


# ==================================================
# Line: 57

def _write_error_file(self, file_path: str, error_msg: str) -> None:
    """Write error message to the file."""
    try:
        with open(file_path, "w") as fp:
            fp.write(error_msg)
    except Exception as e:
        warnings.warn(f"Unable to write error to file. {type(e).__name__}: {e}")


# ==================================================
# Line: 86

def override_error_code_in_rootcause_data(
    self,
    rootcause_error_file: str,
    rootcause_error: dict[str, Any],
    error_code: int = 0,

# ==================================================
# Line: 146

def _rm(self, my_error_file):
    if os.path.isfile(my_error_file):
        # Log the contents of the original file.
        with open(my_error_file) as fp:
            try:
                original = json.dumps(json.load(fp), indent=2)
                logger.warning(
                    "%s already exists"
                    " and will be overwritten."
                    " Original contents:\n%s",
                    my_error_file,
                    original,
                )
            except json.decoder.JSONDecodeError:
                logger.warning(
                    "%s already exists"
                    " and will be overwritten."
                    " Unable to load original contents:\n",
                    my_error_file,
                )
        os.remove(my_error_file)

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/timer/api.py
# Line: 210

def _get_scopes(self, timer_requests):
    return [r.scope_id for r in timer_requests]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/timer/file_based_local_timer.py
# Line: 361

def _get_scopes(self, timer_requests: list[FileTimerRequest]) -> list[str]:
    return [r.scope_id for r in timer_requests]


# ==================================================
# Line: 430

def _reap_worker(self, worker_pid: int, signal: int) -> bool:
    try:
        os.kill(worker_pid, signal)
        return True
    except ProcessLookupError:
        logger.info("Process with pid=%s does not exist. Skipping", worker_pid)
        return True
    except Exception:
        logger.exception("Error terminating pid=%s", worker_pid)
    return False


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/timer/local_timer.py
# Line: 119

def _reap_worker(self, worker_id: int) -> bool:
    try:
        os.kill(worker_id, signal.SIGKILL)
        return True
    except ProcessLookupError:
        logger.info("Process with pid=%s does not exist. Skipping", worker_id)
        return True
    except Exception:
        logger.exception("Error terminating pid=%s", worker_id)
    return False

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/agent/server/api.py
# Line: 553

def _assign_worker_ranks(
    self, store, group_rank: int, group_world_size: int, spec: WorkerSpec

# ==================================================
# Line: 748

def _get_worker_state(self, worker: Worker, result: RunResult) -> str:
    failure = result.failures.get(worker.global_rank)
    if result.state in {WorkerState.UNHEALTHY, WorkerState.FAILED} and not failure:
        # The worker got terminated by the torchelastic agent via SIGTERM signal
        return "TERMINATED"
    elif failure or worker.global_rank in result.return_values:
        return result.state.value
    else:
        raise ValueError(f"Unknown worker: {worker.global_rank}")


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/agent/server/health_check_server.py
# Line: 44

def start(self) -> None:
    """
    Unsupported functionality for Pytorch, doesn't start any health check server
    """
    log.warning("No health check server started")


# ==================================================
# Line: 50

def stop(self) -> None:
    """
    Function to stop health check server
    """
    log.info("Stopping noop health check server.")



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/elastic/agent/server/local_elastic_agent.py
# Line: 241

def _get_fq_hostname(self) -> str:
    return socket.getfqdn(socket.gethostname())


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
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_exec_order_utils.py
# Line: 306

def _get_handle_indices(
    self,
    handle: FlatParamHandle,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_fully_shard/_fully_shard.py
# Line: 570

def wait(self) -> None:
    """
    Waits on the unshard op. This ensures that the current stream can use
    the unsharded parameters, which are now registered to the module.
    """
    return



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/fsdp/_flat_param.py
# Line: 2587

def _check_on_cpu(self, tensor: Tensor):
    _p_assert(
        tensor.device == torch.device("cpu"),
        f"Expects tensor to be on CPU but got {tensor.device}",
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_tools/sac_estimator.py
# Line: 276

def _get_force_store_random(self, inputs: Any) -> bool:
    flat_inputs, _ = tree_flatten(inputs)
    return all(not isinstance(x, torch.Tensor) for x in flat_inputs)


# ==================================================
# Line: 457

def _get_greedy_order_meta(self, sac_stats: SACStats) -> SACGreedyOrderMeta:
    # An inplace-op group is a set of inplace-ops that operate on the same underlying tensor storage.
    # 1. inplace_op_groups: A dictionary from the top-most parent of inplace-ops to the inplace-ops in the group
    #   The top-most op can itself be an inplace-op or can be a non-inplace op.
    # 2. inplace_op_to_group_head: A dictionary that maps all the inplace-ops to their respective group heads.
    inplace_op_groups: dict[int, set[int]] = {}
    inplace_op_to_group_head: dict[int, int] = dict(sac_stats.inplace_ops)

    # Initialize inplace_op_groups using inplace_op_to_group_head
    for op_idx, group_head_idx in inplace_op_to_group_head.items():
        op_group = inplace_op_groups.setdefault(group_head_idx, {group_head_idx})
        op_group.add(op_idx)

    # Like inplace ops, all of the random ops in the function/module should all be either recomputed or saved
    # as a group. This is because, they affect the ranom seed generator. If force_store_random is set True,
    # all of the random ops will be stored by default. For easy of manageability, we store the top-most random op
    # as the leader of the random_ops_group.
    random_ops_group: dict[int, set[int]] = {}
    random_group_head_idx = min(sac_stats.rand_ops, default=-1)
    has_rand_ops = bool(sac_stats.rand_ops)
    if has_rand_ops:
        random_ops_group[random_group_head_idx] = set(sac_stats.rand_ops)

    # 1. Random ops are stored if force_store_random is set
    # 2. View-like ops are recomputed by default
    # 3. For inplace_op_groups:
    #   a) If the head of this group is an inplace op, then we have to store the entire group.
    #   b) If any op in the group is random and force_store_random is set, then entire group will be stored.
    #   c) If none of ops in the group are random and the head of the group is not an in-place op, then
    #       this group can be considered for recomputation in its entireity
    stored_ops: set[int] = set()
    recomputed_ops: set[int] = set()
    # Case 1:
    if has_rand_ops and sac_stats.force_store_random:
        stored_ops.add(random_group_head_idx)
    # Case 2:
    recomputed_ops.update(set(sac_stats.view_like_ops))

    for group_head_idx, op_group in inplace_op_groups.items():
        # Case 3a:
        if group_head_idx in inplace_op_to_group_head:
            stored_ops.add(group_head_idx)
        # Case 3b:
        if (
            sac_stats.force_store_random & len(op_group & set(sac_stats.rand_ops))
            > 0
        ):
            stored_ops.add(group_head_idx)

    # The potential recompute candidates are populated as:
    recompute_candidates: set[int] = set()
    # 1) The random group head if it is not stored
    if has_rand_ops and random_group_head_idx not in stored_ops:
        recompute_candidates.add(random_group_head_idx)
    # 2) The in-place op group heads that are not stored
    recompute_candidates.update(set(inplace_op_groups.keys()) - stored_ops)
    # 3) The non-inplace and non-random ops that are neither stored nor recomputed by default
    recompute_candidates.update(
        set(range(len(sac_stats.memory)))
        - recomputed_ops
        - stored_ops
        - set(inplace_op_to_group_head.keys())
        - set(sac_stats.rand_ops)
    )

    # We define msps for a recomp candidate as the ratio of memory/runtime aka memory savings per second
    msps_meta: list[MSPS] = []
    for cand_idx in recompute_candidates:
        op_indices = {cand_idx}
        if cand_idx in inplace_op_groups:
            op_indices.update(inplace_op_groups[cand_idx])
        if has_rand_ops and cand_idx == random_group_head_idx:
            op_indices.update(sac_stats.rand_ops)

        mem = sum(sac_stats.memory[op_idx] for op_idx in op_indices)
        runtime = sum(sac_stats.runtimes[op_idx] for op_idx in op_indices)
        func_names = {sac_stats.func_names[op_idx] for op_idx in op_indices}
        msps = (mem / runtime) if runtime > 0 else sys.float_info.max
        msps_meta.append(MSPS(func_names, cand_idx, mem, runtime, msps))
    # We choose canidates to be recomputed based on increasing msps
    msps_meta.sort(key=lambda x: x.msps, reverse=True)
    return SACGreedyOrderMeta(
        recomputed_ops, stored_ops, inplace_op_groups, random_ops_group, msps_meta
    )


# ==================================================
# Line: 542

def _get_sac_tradeoff_pwlf_stats(
    self,
    sac_stats: SACStats,
    greedy_order_meta: SACGreedyOrderMeta,
    n_segments: int = 2,
    save_tradeoff_graph: bool = False,
    filename: str = "ac_tradeoff",

# ==================================================
# Line: 670

def display_sac_stats(
    self, sac_stats: SACStats, print_tabular: bool = False

# ==================================================
# Line: 742

def display_sac_tradeoff_stats(
    self,
    greedy_order_meta: SACGreedyOrderMeta,
    sac_stats: SACStats,
    print_tabular: bool = False,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/distributed_c10d.py
# Line: 665

def group_count(self, value: int) -> None:
    """Use to compute the name of ProcessGroups when using global synchronization."""
    global _group_count
    _group_count = value


# ==================================================
# Line: 727

def WORLD(cls, pg: Optional[ProcessGroup]):
    _world.default_pg = pg



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/device_mesh.py
# Line: 267

def get_mesh_dim_by_name(
    self, device_mesh: "DeviceMesh", mesh_dim_name: str

# ==================================================
# Line: 904

def get_rank(self) -> int:
    """
    Returns the current global rank.
    """
    return get_rank()


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/filesystem.py
# Line: 253

def writeable(self) -> bool:
    return True


# ==================================================
# Line: 542

def ls(self, path: Union[str, os.PathLike]) -> list[str]:
    if not isinstance(path, Path):
        path = Path(path)
    return [str(p) for p in path.iterdir()]



# ==================================================
# Line: 789

def _slice_file(self, file, sinfo: _StorageInfo) -> IO[bytes]:
    return cast(IO[bytes], _create_file_view(file, sinfo.offset, sinfo.length))


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/_hf_storage.py
# Line: 134

def _split_by_storage_plan(
    self, storage_plan: dict[str, int], items: list[WriteItem]

# ==================================================
# Line: 149

def _gen_file_name(self, index: int, largest_index: int) -> str:
    return (
        FILE_NAME.format(
            cpt_idx=f"{index}".zfill(5), num_shards=f"{largest_index}".zfill(5)
        )
        + SUFFIX
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/storage.py
# Line: 155

def storage_meta(self) -> Optional[StorageMeta]:
    """
    Return the storage-specific metadata. This is used to store additional information
    in a checkpoint that can be useful for providing request-level observability. StorageMeta
    is passed to the ``SavePlanner`` during save calls. Returns None by default.

    TODO: provide an example
    """
    return None



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/default_planner.py
# Line: 261

def transform_object(self, write_item: WriteItem, object: Any):
    """Extension from the planner interface to make it easy to extend the default planner."""
    if write_item.type == WriteItemType.BYTE_IO:
        bytes = io.BytesIO()
        torch.save(object, bytes)
        object = bytes
    return object



# ==================================================
# Line: 383

def transform_tensor(self, read_item: ReadItem, tensor: torch.Tensor):
    """Extension from the planner interface to make it easy to extend the default planner."""
    return narrow_tensor_by_index(tensor, read_item.dest_offsets, read_item.lengths)



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/checkpoint/_extension.py
# Line: 131

def writeable(self) -> bool:
    return True


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/rpc/internal.py
# Line: 60

def _tensor_reducer(self, tensor):
    global _thread_local_tensor_tables
    _thread_local_tensor_tables.send_tables.append(tensor)
    tensor_index = len(_thread_local_tensor_tables.send_tables) - 1
    return (_InternalRPCPickler._tensor_receiver, (tensor_index,))


# ==================================================
# Line: 70

def _py_rref_reducer(self, py_rref):
    rref_fork_data = py_rref._serialize()
    return (_InternalRPCPickler._py_rref_receiver, (rref_fork_data,))


# ==================================================
# Line: 87

def _script_module_reducer(self, script_module):
    """
    Serializes a ScriptModule.
    """
    f = io.BytesIO()
    torch.jit.save(script_module, f)
    return (_InternalRPCPickler._script_module_receiver, (f.getvalue(),))


# ==================================================
# Line: 148

def deserialize(self, binary_data, tensor_table):
    r"""
    Deserialize binary string + tensor table to original obj
    """
    # save _thread_local_tensor_tables.recv_tables if it is in nested call
    global _thread_local_tensor_tables
    if hasattr(_thread_local_tensor_tables, "recv_tables"):
        old_recv_tables = _thread_local_tensor_tables.recv_tables
    else:
        old_recv_tables = None
    _thread_local_tensor_tables.recv_tables = tensor_table

    try:
        unpickler = _unpickler(io.BytesIO(binary_data))
        ret = unpickler.load()
    except AttributeError as e:
        # Occurs when function is not found on module/class during
        # unpickling.
        except_str = (
            str(e)
            + """ Default RPC pickler does not serialize
        function code. Ensure that UDFs are defined on both caller and
        callee modules."""
        )
        ret = AttributeError(except_str)
        # Ensure the stack trace gets preserved
        ret.__cause__ = e

    # restore _thread_local_tensor_tables.recv_tables if return
    # from nested call, otherwise clean up the table
    if old_recv_tables is not None:
        _thread_local_tensor_tables.recv_tables = old_recv_tables
    else:
        del _thread_local_tensor_tables.recv_tables

    return ret



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_ops/_view_ops.py
# Line: 37

def inputs(self) -> Iterable["DimSpec"]:
    return ()



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_random.py
# Line: 375

def _calc_shard_linear_idx(
    self, shard_coord: list[int], shard_size: list[int]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/placement_types.py
# Line: 628

def _replicate_tensor(
    self,
    tensor: torch.Tensor,
    mesh: DeviceMesh,
    mesh_dim: int,
    src_data_rank: Optional[int] = 0,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/parallel/style.py
# Line: 374

def _replicate_module_fn(
    self, name: str, module: nn.Module, device_mesh: DeviceMesh

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/_sharding_prop.py
# Line: 110

def _propagate_tensor_meta_non_cached(
    self, op_schema: OpSchema

# ==================================================
# Line: 161

def _wrap_output_spec_tensor_meta(
    self,
    op: OpOverload,
    output_specs: OutputSpecType,
    output_tensor_meta: Union[None, TensorMeta, Sequence[Optional[TensorMeta]]],

# ==================================================
# Line: 221

def _wrap_with_op_strategy(self, op_schema: OpSchema) -> OpSchema:
    """
    wrap a op_schema that contains DTensorSpec to another op_schema that contains
    OpStrategy/TupleStrategy, the returned op_schema is then used for sharding
    strategy propagation on pytorch operators.
    """

    def spec_to_strategy(spec: object) -> object:
        if isinstance(spec, DTensorSpec):
            return OpStrategy([PlacementStrategy(spec)])
        elif (
            isinstance(spec, (list, tuple))
            and len(spec) > 0
            and isinstance(spec[0], DTensorSpec)
        ):
            # tensor list create tuple strategy
            tuple_strategy = [spec_to_strategy(s) for s in spec]
            tuple_strategy = cast(Sequence[StrategyType], tuple_strategy)
            return TupleStrategy(
                tuple(tuple_strategy) if isinstance(spec, tuple) else tuple_strategy
            )
        else:
            return spec

    args_op_strategy = [spec_to_strategy(i) for i in op_schema.args_schema]

    kwargs_op_strategy = {
        k: spec_to_strategy(v) for k, v in op_schema.kwargs_schema.items()
    }

    return OpSchema(
        op=op_schema.op,
        args_schema=tuple(args_op_strategy),
        kwargs_schema=kwargs_op_strategy,
    )


# ==================================================
# Line: 490

def _select_strategy(self, strategy: OpStrategy) -> PlacementStrategy:
    if len(strategy.strategies) == 1:
        # short cut with only one possible strategy
        return strategy.strategies[0]

    strategy_costs: list[float] = []
    for strtg in strategy.strategies:
        assert strtg.redistribute_cost is not None, (
            "must set redistribute cost each strategy!"
        )
        redistribute_cost = sum(chain.from_iterable(strtg.redistribute_cost))
        strategy_costs.append(redistribute_cost)

    # for eager execution, we just select the one with the minimal redistribute cost
    return strategy.strategies[strategy_costs.index(min(strategy_costs))]


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/tensor/debug/_comm_mode.py
# Line: 550

def _get_operations_list(self, module_operation_counts):
    forward_operations = [
        op for op in module_operation_counts["operations_list"] if not op["is_bw"]
    ]
    backward_operations = [
        op
        for op in module_operation_counts["operations_list"]
        if op["is_bw"] and not op["is_activation_checkpointing"]
    ]
    checkpointing_operations = [
        op
        for op in module_operation_counts["operations_list"]
        if op["is_activation_checkpointing"]
    ]

    return forward_operations, backward_operations, checkpointing_operations


# ==================================================
# Line: 613

def _set_noise_parameters(self, noise_level):
    """
    sets variables controlling what information displays based on noise level
    """
    include_DTensor_ops = False
    include_module_data = False
    include_ops = False
    include_trivial_ops = False

    if noise_level > 0:
        include_DTensor_ops = True
        include_module_data = True

    if noise_level > 1:
        include_ops = True

    if noise_level > 2:
        include_trivial_ops = True

    return (
        include_DTensor_ops,
        include_module_data,
        include_ops,
        include_trivial_ops,
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/optim/zero_redundancy_optimizer.py
# Line: 858

def _get_min_index(
    self,
    values: list[int],
    disallowed_indices: Optional[set[int]] = None,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/pipelining/stage.py
# Line: 523

def _map_tensor_from_recv_info(
    self,
    recv_infos: tuple[InputInfo, ...],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/distributed/_serialization.py
# Line: 83

def serialization_id(self) -> str:
    return "torchft"



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/flatten.py
# Line: 127

def _require_tuple_tuple(self, input):
    if isinstance(input, tuple):
        for idx, elem in enumerate(input):
            if not isinstance(elem, tuple):
                raise TypeError(
                    "unflattened_size must be tuple of tuples, "
                    + f"but found element of type {type(elem).__name__} at pos {idx}"
                )
        return
    raise TypeError(
        "unflattened_size must be a tuple of tuples, "
        + f"but found type {type(input).__name__}"
    )


# ==================================================
# Line: 141

def _require_tuple_int(self, input):
    if isinstance(input, (tuple, list)):
        for idx, elem in enumerate(input):
            if not isinstance(elem, int):
                raise TypeError(
                    "unflattened_size must be tuple of ints, "
                    + f"but found element of type {type(elem).__name__} at pos {idx}"
                )
        return
    raise TypeError(
        f"unflattened_size must be a tuple of ints, but found type {type(input).__name__}"
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/rnn.py
# Line: 340

def check_hidden_size(
    self,
    hx: Tensor,
    expected_hidden_size: tuple[int, int, int],
    msg: str = "Expected hidden size {}, got {}",

# ==================================================
# Line: 368

def permute_hidden(self, hx: Tensor, permutation: Optional[Tensor]):
    if permutation is None:
        return hx
    return _apply_permutation(hx, permutation)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/activation.py
# Line: 328

def forward(self, input: Tensor) -> Tensor:
    return torch.sigmoid(input)



# ==================================================
# Line: 393

def forward(self, input: Tensor) -> Tensor:
    return torch.tanh(input)



# ==================================================
# Line: 858

def forward(self, input: Tensor) -> Tensor:
    return F.logsigmoid(input)



# ==================================================
# Line: 1547

def forward(self, input: Tensor) -> Tensor:
    return F.softsign(input)



# ==================================================
# Line: 1570

def forward(self, input: Tensor) -> Tensor:
    return F.tanhshrink(input)



# ==================================================
# Line: 1705

def forward(self, input: Tensor) -> Tensor:
    if input.dim() not in (3, 4):
        raise ValueError(
            f"Softmax2d: expected input to be 3D or 4D, got {input.dim()}D instead"
        )
    return F.softmax(input, -3, _stacklevel=5)



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/module.py
# Line: 886

def get_extra_state(self) -> Any:
    """Return any extra state to include in the module's state_dict.

    Implement this and a corresponding :func:`set_extra_state` for your module
    if you need to store extra state. This function is called when building the
    module's `state_dict()`.

    Note that extra state should be picklable to ensure working serialization
    of the state_dict. We only provide backwards compatibility guarantees
    for serializing Tensors; other objects may break backwards compatibility if
    their serialized pickled form changes.

    Returns:
        object: Any extra state to store in the module's state_dict
    """
    raise RuntimeError(
        "Reached a code path in Module.get_extra_state() that should never be called. "
        "Please file an issue at https://github.com/pytorch/pytorch/issues/new?template=bug-report.yml "
        "to report this bug."
    )


# ==================================================
# Line: 907

def set_extra_state(self, state: Any) -> None:
    """Set extra state contained in the loaded `state_dict`.

    This function is called from :func:`load_state_dict` to handle any extra state
    found within the `state_dict`. Implement this function and a corresponding
    :func:`get_extra_state` for your module if you need to store extra state within its
    `state_dict`.

    Args:
        state (dict): Extra state from the `state_dict`
    """
    raise RuntimeError(
        "Reached a code path in Module.set_extra_state() that should never be called. "
        "Please file an issue at https://github.com/pytorch/pytorch/issues/new?template=bug-report.yml "
        "to report this bug."
    )


# ==================================================
# Line: 1537

def _maybe_warn_non_full_backward_hook(self, inputs, result, grad_fn):
    if not isinstance(result, torch.Tensor):
        if not (
            isinstance(result, tuple)
            and all(isinstance(r, torch.Tensor) for r in result)
        ):
            warnings.warn(
                "Using non-full backward hooks on a Module that does not return a "
                "single Tensor or a tuple of Tensors is deprecated and will be removed "
                "in future versions. This hook will be missing some of the grad_output. "
                "Please use register_full_backward_hook to get the documented behavior.",
                FutureWarning,
                stacklevel=2,
            )
            return
    else:
        result = (result,)

    if not isinstance(inputs, torch.Tensor):
        if not (
            isinstance(inputs, tuple)
            and all(isinstance(i, torch.Tensor) for i in inputs)
        ):
            warnings.warn(
                "Using non-full backward hooks on a Module that does not take as input a "
                "single Tensor or a tuple of Tensors is deprecated and will be removed "
                "in future versions. This hook will be missing some of the grad_input. "
                "Please use register_full_backward_hook to get the documented behavior.",
                FutureWarning,
                stacklevel=2,
            )
            return
    else:
        inputs = (inputs,)

    # At this point we are sure that inputs and result are tuple of Tensors
    out_grad_fn = {r.grad_fn for r in result if r.grad_fn is not None}
    if len(out_grad_fn) == 0 or (
        len(out_grad_fn) == 1 and grad_fn not in out_grad_fn
    ):
        warnings.warn(
            "Using a non-full backward hook when outputs are nested in python data structure "
            "is deprecated and will be removed in future versions. This hook will be missing "
            "some grad_output.",
            FutureWarning,
            stacklevel=2,
        )
    elif len(out_grad_fn) > 1:
        warnings.warn(
            "Using a non-full backward hook when outputs are generated by different autograd Nodes "
            "is deprecated and will be removed in future versions. This hook will be missing "
            "some grad_output. Please use register_full_backward_hook to get the documented behavior.",
            FutureWarning,
            stacklevel=2,
        )
    else:
        # At this point the grad_output part of the hook will most likely be correct
        inputs_grad_fn = {i.grad_fn for i in inputs if i.grad_fn is not None}

        next_functions = {n[0] for n in grad_fn.next_functions}

        if inputs_grad_fn != next_functions:
            warnings.warn(
                "Using a non-full backward hook when the forward contains multiple autograd Nodes "
                "is deprecated and will be removed in future versions. This hook will be missing "
                "some grad_input. Please use register_full_backward_hook to get the documented "
                "behavior.",
                FutureWarning,
                stacklevel=2,
            )


# ==================================================
# Line: 2949

def extra_repr(self) -> str:
    r"""Return the extra representation of the module.

    To print customized extra information, you should re-implement
    this method in your own modules. Both single-line and multi-line
    strings are acceptable.
    """
    return ""


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/batchnorm.py
# Line: 724

def _check_non_zero_input_channels(self, input):
    if input.size(1) == 0:
        raise ValueError(
            "SyncBatchNorm number of input channels should be non-zero"
        )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/container.py
# Line: 824

def _key_to_attr(self, key: str) -> str:
    if not isinstance(key, str):
        raise TypeError(
            "Index given to ParameterDict cannot be used as a key as it is "
            f"not a string (type is '{type(key).__name__}'). Open an issue on "
            "github if you need non-string keys."
        )
    else:
        # Use the key as-is so that `.named_parameters()` returns the right thing
        return key


# ==================================================
# Line: 922

def fromkeys(
    self, keys: Iterable[str], default: Optional[Any] = None

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/lazy.py
# Line: 282

def _replicate_for_data_parallel(self: _LazyProtocol):
    raise RuntimeError(
        "Modules with uninitialized parameters can't be used with `DataParallel`. "
        "Run a dummy forward pass to correctly initialize the modules"
    )

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/linear.py
# Line: 46

def forward(self, input: Tensor) -> Tensor:
    return input



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/modules/conv.py
# Line: 69

def _conv_forward(self, input: Tensor, weight: Tensor, bias: Optional[Tensor]) -> Tensor:  # type: ignore[empty-body]
    ...


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/spectral_norm.py
# Line: 131

def _solve_v_and_rescale(self, weight_mat, u, target_sigma):
    # Tries to returns a vector `v` s.t. `u = F.normalize(W @ v)`
    # (the invariant at top of this class) and `u @ W @ v = sigma`.
    # This uses pinverse in case W^T W is not invertible.
    v = torch.linalg.multi_dot(
        [weight_mat.t().mm(weight_mat).pinverse(), weight_mat.t(), u.unsqueeze(1)]
    ).squeeze(1)
    return v.mul_(target_sigma / torch.dot(u, torch.mv(weight_mat, v)))


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/utils/parametrizations.py
# Line: 521

def right_inverse(self, value: torch.Tensor) -> torch.Tensor:
    # we may want to assert here that the passed value already
    # satisfies constraints
    return value



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/parameter.py
# Line: 146

def share_memory_(self):
    raise RuntimeError(
        "Can't share memory on an uninitialized parameter or buffer. "
        "Call `forward` to initialize the parameters before calling "
        "`module.share_memory()`."
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/parallel/data_parallel.py
# Line: 197

def replicate(
    self, module: T, device_ids: Sequence[Union[int, torch.device]]

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/nn/parallel/distributed.py
# Line: 1391

def _get_parameters(self, m, recurse=True):
    """Return a generator of module parameters."""

    def model_parameters(m):
        ps = (
            m._former_parameters.values()
            if hasattr(m, "_former_parameters")
            else m.parameters(recurse=False)
        )
        yield from ps

    for mod in m.modules() if recurse else [m]:
        yield from model_parameters(mod)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/package/package_exporter.py
# Line: 436

def _get_source_of_module(self, module: types.ModuleType) -> Optional[str]:
    filename = None
    spec = getattr(module, "__spec__", None)
    if spec is not None:
        loader = getattr(spec, "loader", None)
        if loader is not None and isinstance(loader, SourceFileLoader):
            try:
                filename = loader.get_filename(module.__name__)
            except ImportError:
                pass
    if filename is None:
        filename = getattr(module, "__file__", None)
    if isinstance(filename, str) and filename.endswith(".py"):
        return "".join(linecache.getlines(filename, module.__dict__))
    return None


# ==================================================
# Occurrences: Lines 1086-1091 (2 instances)

def _filename(self, package, resource):
    package_path = package.replace(".", "/")
    resource = _normalize_path(resource)
    return f"{package_path}/{resource}"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/package/find_file_dependencies.py
# Occurrences: Lines 45-48 (2 instances)

def _grab_node_int(self, node):
    return node.value


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/package/importer.py
# Line: 189

def _is_torchpackage_dummy(self, module):
    """Returns true iff this module is an empty PackageNode in a torch.package.

    If you intern `a.b` but never use `a` in your code, then `a` will be an
    empty module with no source. This can break cases where we are trying to
    re-package an object after adding a real dependency on `a`, since
    OrderedImportere will resolve `a` to the dummy package and stop there.

    See: https://github.com/pytorch/pytorch/pull/71520#issuecomment-1029603769
    """
    if not getattr(module, "__torch_package__", False):
        return False
    if not hasattr(module, "__path__"):
        return False
    if not hasattr(module, "__file__"):
        return True
    return module.__file__ is None


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/scheduler/base_scheduler.py
# Line: 99

def print_sl(self, is_verbose, group, sl, epoch=None):
    """Display the current sparsity level."""
    if is_verbose:
        if epoch is None:
            print(f"Adjusting sparsity level of group {group} to {sl:.4e}.")
        else:
            print(
                f"Epoch {epoch:5d}: adjusting sparsity level of group {group} to {sl:.4e}."
            )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/pruner/lstm_saliency_pruner.py
# Line: 28

def update_mask(self, module, tensor_name, **kwargs):
    weights = getattr(module, tensor_name)

    for p in getattr(module.parametrizations, tensor_name):
        if isinstance(p, FakeStructuredSparsity):
            mask = cast(torch.Tensor, p.mask)

            # select weights based on magnitude
            if weights.dim() <= 1:
                raise Exception(  # noqa: TRY002
                    "Structured pruning can only be applied to a 2+dim weight tensor!"
                )
            # take norm over all but first dim
            dims = tuple(range(1, weights.dim()))
            saliency = weights.norm(dim=dims, p=1)

            # handle weights in 4 groups
            split_size = len(mask) // 4
            masks = torch.split(mask, split_size)
            saliencies = torch.split(saliency, split_size)

            for keep_mask, sal in zip(masks, saliencies):
                # mask smallest k values to be removed
                k = int(len(keep_mask) * kwargs["sparsity_level"])
                prune = sal.topk(k, largest=False, sorted=False).indices
                keep_mask.data[prune] = False  # modifies underlying p.mask directly

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/activation_sparsifier/activation_sparsifier.py
# Line: 383

def _convert_mask(self, states_dict, sparse_coo=True):
    r"""Converts the mask to sparse coo or dense depending on the `sparse_coo` argument.
    If `sparse_coo=True`, then the mask is stored as sparse coo else dense tensor
    """
    states = copy.deepcopy(states_dict)
    for state in states.values():
        if state["mask"] is not None:
            if isinstance(state["mask"], list):
                for idx in range(len(state["mask"])):
                    if sparse_coo:
                        state["mask"][idx] = state["mask"][idx].to_sparse_coo()
                    else:
                        state["mask"][idx] = state["mask"][idx].to_dense()
            else:
                if sparse_coo:
                    state["mask"] = state["mask"].to_sparse_coo()
                else:
                    state["mask"] = state["mask"].to_dense()
    return states


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/data_sparsifier/data_norm_sparsifier.py
# Line: 60

def __get_scatter_folded_mask(
    self, data, dim, indices, output_size, sparse_block_shape

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/pruning/_experimental/data_sparsifier/base_data_sparsifier.py
# Line: 77

def _extract_weight(self, data):
    # extract the weight parameter instead of underlying data
    if type(data) in [torch.Tensor, nn.Parameter]:
        return data
    elif type(data) in EMBEDDING_TYPES:
        return data.weight


# ==================================================
# Line: 152

def _convert_mask(self, states, sparse_coo=True):
    r"""Converts the mask to sparse coo or dense tensors depending on the `sparse_coo` argument."""
    states = copy.deepcopy(states)
    for state in states.values():
        if sparse_coo:
            state["mask"] = state["mask"].to_sparse_coo()
        else:
            state["mask"] = state["mask"].to_dense()

    return states


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
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/stubs.py
# Line: 25

def forward(self, x: torch.Tensor) -> torch.Tensor:
    return x



# ==================================================
# Line: 43

def forward(self, x: torch.Tensor) -> torch.Tensor:
    return x



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/quantize_handler.py
# Line: 79

def is_general_tensor_value_op(self) -> bool:
    """
    Returns True if the operator works for both floating point and
    quantized input, and does some computation based on the input Tensor,
    or the ops that only re-arranges the Tensor values or query some metadata
    about the Tensor
    so we need to insert observer/fake_quant for the output of the
    operator (same observer instance as input)
    since the distribution of values is different for input and output
    Tensors (for HistogramObserver) while they share the same quantization
    parameters
    Example operator: avgpool2d, reshape, transpose, maxpool2d
    Example observed operator:
    observer_0 - avgpool2d - observer_0 (same observer instance as input)
    """
    return False


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_model_report/model_report_visualizer.py
# Line: 180

def _generate_tensor_table(
    self,
    filtered_data: OrderedDict[str, dict[str, Any]],
    tensor_features: list[str],

# ==================================================
# Line: 236

def _generate_channels_table(
    self,
    filtered_data: OrderedDict[str, Any],
    channel_features: list[str],
    num_channels: int,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_model_report/model_report.py
# Line: 340

def _is_same_info_for_same_key(self, info_dict_a: dict, info_dict_b: dict) -> bool:
    r"""
    Takes in two dictionaries and ensures that any common keys between the two have the same
    values.

    Args:
        info_dict_a (Dict): First dictionary we wish to compare
        info_dict_b (Dict): Second dictionary we wish to compare

    Returns True if all shared keys have same values, false otherwise
    """
    # get the set of keys for both
    dict_a_keys: set = set(info_dict_a.keys())
    dict_b_keys: set = set(info_dict_b.keys())

    # get the insersection keys and check if same value for both dicts
    intersecting_keys: set = dict_a_keys.intersection(dict_b_keys)

    for key in intersecting_keys:
        dict_a_val = info_dict_a[key]
        dict_b_val = info_dict_b[key]

        # if it's a tensor we have to handle separately
        if type(dict_a_val) == torch.Tensor:
            # if dict_b_val not tensor, automatically false
            if (
                type(dict_b_val) != torch.Tensor
                or sum(dict_a_val != dict_b_val) != 0
            ):
                return False
        else:
            # for non-tensor vals
            if dict_a_val != dict_b_val:
                return False

    # if no non matching shared keys found, return true
    return True


# ==================================================
# Line: 485

def _update_detector_quantizaiton_qconfig_info(
    self, combined_info: DetectorQConfigInfo, new_info: DetectorQConfigInfo

# ==================================================
# Line: 503

def _update_detector_equalization_qconfig_info(
    self, combined_info: DetectorQConfigInfo, new_info: DetectorQConfigInfo

# ==================================================
# Line: 613

def _quantization_config_generator(
    self, detector_qconfig_info: DetectorQConfigInfo, module: torch.nn.Module

# ==================================================
# Line: 621

def _equalization_config_generator(
    self, detector_qconfig_info: DetectorQConfigInfo, module: torch.nn.Module

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/fx/_model_report/detector.py
# Line: 112

def generate_equalization_qconfig(self) -> EqualizationQConfig:
    r"""
    This returns the equalization configuration for a module.

    For now, it just returns the default, but as more equalization options become
    possible, this method can get more fleshed out with more nuanced granularity.


    Returns the generated equalization QConfig according to what a valid configuration is
    """
    # in this case, we just return default equalization config
    # we know this is valid because only valid modules would even
    # have this option
    return default_equalization_qconfig



# ==================================================
# Line: 1432

def _supports_insertion(self, module: nn.Module) -> bool:
    r"""Returns whether the given module is supported for observers insertion

    Any module that doesn't have children and isn't an observer itself is supported

    Args
        module: The module to check and ensure is supported

    Returns True if the module is supported by observer, False otherwise
    """
    # case for insertion of module
    # check if the module has any children and isn't observer
    num_children = len(list(module.children()))
    return num_children == 0 and not _is_activation_post_process(module)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/quantizer/x86_inductor_quantizer.py
# Line: 558

def _annotate_conv_node_helper(
    self,
    conv_node: torch.fx.Node,
    annotate_output: bool,
    quantization_config: Optional[QuantizationConfig],

# ==================================================
# Line: 590

def _annotate_linear_node_helper(
    self,
    linear_node: torch.fx.Node,
    annotate_output: bool,
    quantization_config: Optional[QuantizationConfig],

# ==================================================
# Line: 630

def _get_output_nodes_of_partitions(
    self,
    partition_list: list[SourcePartition],

# ==================================================
# Line: 648

def _get_input_idx_for_binary_node(
    self,
    conv_gemm_node: torch.fx.Node,
    binary_node: torch.fx.Node,

# ==================================================
# Line: 1018

def _annotate_matmul(
    self,
    model: torch.fx.GraphModule,
    quantization_config: Optional[QuantizationConfig],
    filter_fn: Optional[FilterFn] = None,

# ==================================================
# Line: 1216

def _annotate_maxpool2d(
    self,
    node: Node,
    quantization_config: Optional[QuantizationConfig],

# ==================================================
# Line: 1245

def _annotate_cat(
    self, node: Node, quantization_config: QuantizationConfig

# ==================================================
# Line: 1353

def _annotate_output_share_observer_as_input(
    self, input_node: Node, source_node: Node

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/quantizer/xnnpack_quantizer.py
# Line: 354

def transform_for_annotation(
    self, model: torch.fx.GraphModule

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/quantizer/quantizer.py
# Line: 138

def transform_for_annotation(
    self, model: torch.fx.GraphModule

# ==================================================
# Line: 163

def prepare_obs_or_fq_callback(
    self,
    model: torch.fx.GraphModule,
    edge_or_node_to_obs_or_fq: dict[EdgeOrNode, ObserverOrFakeQuantize],

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/quantizer/embedding_quantizer.py
# Line: 73

def _annotate_embedding_ops(self, graph: torch.fx.Graph) -> None:
    embedding_config: OperatorConfig = get_embedding_operators_config()
    for node in graph.nodes:
        # Keep node parsing based annotations instead of module partitioners
        # just as an example of alternate ways of annotating
        if (
            node.op == "call_function"
            and node.target == torch.ops.aten.embedding.default
        ):
            if embedding_config.config.weight is None:
                raise ValueError(
                    "Embedding config must have a valid weight quantization spec."
                )
            node.meta["quantization_annotation"] = QuantizationAnnotation(
                input_qspec_map={
                    node.args[0]: embedding_config.config.weight,
                }
            )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/experimental/adaround_optimization.py
# Line: 127

def feed_forward(self, x, weight, module):
    if isinstance(module, torch.nn.Conv1d):
        out = torch.nn.functional.conv1d(
            x,
            weight,
            stride=module.stride,
            padding=module.padding,
            dilation=module.dilation,
            groups=module.groups,
        )
    elif isinstance(module, torch.nn.Linear):
        out = torch.nn.functional.linear(
            x,
            weight,
            bias=module.bias,
        )
    else:
        raise NotImplementedError
    return out


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/experimental/adaround_loss.py
# Line: 70

def reconstruction_loss(
    self,
    soft_quantized_output: torch.Tensor,
    original_output: torch.Tensor,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/experimental/linear.py
# Line: 79

def bitshift_mul(self, weight_val, r):
    r"""
    Compute multiplication of weight_val * r using bitshifting
    method discussed in APoT paper: https://arxiv.org/pdf/1909.13144.pdf
    Args:
        weight_val: list of binary digits representing APoT quantized weight value
        r: int representing uniformly quantized activation value
    """
    product = 0

    idx = len(weight_val) - 1
    place = 0

    while idx >= 0:
        block = weight_val[idx]

        # reverse digits in block
        block = block[::-1]

        curr_block_result = 0

        for ele in block:
            if int(ele):
                curr_block_result += r << place
            place += 1

        idx -= 1
        product += curr_block_result

    return product


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/quantization/observer.py
# Line: 318

def _validate_qmin_qmax(self, quant_min: int, quant_max: int) -> None:
    r"""Validates that the user-specified quantization range is properly initialized
    and within the given bound supported by the observer dtype.

    To accommodate lower-bit quantization with respect to the existing torch.qint8 and
    torch.quint8 datatypes, the user can choose to use dynamic quantization range by passing
    in a tuple of initial qmin and qmax values. One use case is these customized qmin and qmax
    values are used to calculate static estimates of the scale and zero point for aggressive lower-bit
    fake quantization. These estimates are compared against parameters learned through backpropagation.
    The related literatures for scale and zero point via backpropagation are as follows:

    Learned Step Size Quantization: https://openreview.net/pdf?id=rkgO66VKDS
    Trained Quantization Thresholds: https://arxiv.org/pdf/1903.08066.pdf
    """
    # The variable names are prefixed with "initial" because their values (qmin and qmax) might be adjusted
    # based on whether quantization range is reduced and the datatype (signed/unsigned) used by the observer.
    assert (
        quant_min <= 0 <= quant_max
    ), "Used-specified quantization range must include 0."
    assert (
        quant_min < quant_max
    ), "qmin must be strictly less than qmax for user-specified quantization range."


# ==================================================
# Line: 1051

def _get_norm(
    self, delta_begin: torch.Tensor, delta_end: torch.Tensor, density: torch.Tensor

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/sparse/quantized/linear.py
# Line: 29

def _get_name(self):
    return "SparseQuantizedLinearPackedParams"


# ==================================================
# Line: 52

def forward(self, x):
    return x


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/__init__.py
# Line: 157

def forward(self, Xq):
    return Xq.dequantize()


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/rnn.py
# Line: 37

def _get_name(self):
    return "QuantizedLSTM"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/activation.py
# Line: 51

def _get_name(self):
    return "QuantizedReLU6"


# ==================================================
# Line: 76

def _get_name(self):
    return "QuantizedHardswish"


# ==================================================
# Line: 108

def _get_name(self):
    return "QuantizedELU"


# ==================================================
# Line: 149

def _get_name(self):
    return "QuantizedLeakyReLU"


# ==================================================
# Line: 215

def _get_name(self):
    return "QuantizedSoftmax"


# ==================================================
# Line: 231

def _get_name(self):
    return "QuantizedMultiheadAttention"


# ==================================================
# Line: 307

def _get_name(self):
    return "QuantizedPReLU"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/embedding_ops.py
# Line: 53

def forward(self, x):
    return x


# ==================================================
# Line: 169

def _get_name(self):
    return "QuantizedEmbedding"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/batchnorm.py
# Occurrences: Lines 62-65 (2 instances)

def _get_name(self):
    return "QuantizedBatchNorm2d"


# ==================================================
# Occurrences: Lines 101-104 (2 instances)

def _get_name(self):
    return "QuantizedBatchNorm3d"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/normalization.py
# Line: 58

def _get_name(self):
    return "QuantizedLayerNorm"


# ==================================================
# Line: 129

def _get_name(self):
    return "QuantizedGroupNorm"


# ==================================================
# Line: 185

def _get_name(self):
    return "QuantizedInstanceNorm1d"


# ==================================================
# Line: 252

def _get_name(self):
    return "QuantizedInstanceNorm2d"


# ==================================================
# Line: 319

def _get_name(self):
    return "QuantizedInstanceNorm3d"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/functional_modules.py
# Line: 42

def forward(self, x):
    raise RuntimeError(
        "FloatFunctional is not intended to use the "
        + "'forward'. Please use the underlying operation"
    )


# ==================================================
# Line: 57

def add_scalar(self, x: Tensor, y: float) -> Tensor:
    r = torch.add(x, y)
    # Note: this operation is not observed because the observation is not
    # needed for the quantized op.
    return r


# ==================================================
# Line: 72

def mul_scalar(self, x: Tensor, y: float) -> Tensor:
    r = torch.mul(x, y)
    # Note: this operation is not observed because the observation is not
    # needed for the quantized op.
    return r


# ==================================================
# Line: 114

def forward(self, x):
    raise RuntimeError(
        "FloatFunctional is not intended to use the "
        + "'forward'. Please use the underlying operation"
    )


# ==================================================
# Line: 122

def add(self, x: Tensor, y: Tensor) -> Tensor:
    r = torch.add(x, y)
    return r


# ==================================================
# Line: 128

def add_scalar(self, x: Tensor, y: float) -> Tensor:
    r = torch.add(x, y)
    return r


# ==================================================
# Line: 134

def mul(self, x: Tensor, y: Tensor) -> Tensor:
    r = torch.mul(x, y)
    return r


# ==================================================
# Line: 140

def mul_scalar(self, x: Tensor, y: float) -> Tensor:
    r = torch.mul(x, y)
    return r


# ==================================================
# Line: 146

def cat(self, x: list[Tensor], dim: int = 0) -> Tensor:
    r = torch.cat(x, dim=dim)
    return r


# ==================================================
# Line: 152

def add_relu(self, x: Tensor, y: Tensor) -> Tensor:
    r = torch.add(x, y)
    r = torch.nn.functional.relu(r)
    return r


# ==================================================
# Line: 159

def matmul(self, x: Tensor, y: Tensor) -> Tensor:
    r = torch.matmul(x, y)
    return r



# ==================================================
# Line: 225

def _get_name(self):
    return "QFunctional"


# ==================================================
# Line: 231

def forward(self, x):
    raise RuntimeError(
        "Functional is not intended to use the "
        + "'forward'. Please use the underlying operation"
    )


# ==================================================
# Line: 246

def add_scalar(self, x: Tensor, y: float) -> Tensor:
    r = ops.quantized.add_scalar(x, y)
    # Note: this operation is not observed because the observation is not
    # needed for the quantized op.
    return r


# ==================================================
# Line: 261

def mul_scalar(self, x: Tensor, y: float) -> Tensor:
    r = ops.quantized.mul_scalar(x, y)
    # Note: this operation is not observed because the observation is not
    # needed for the quantized op.
    return r


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/dropout.py
# Occurrences: Lines 18-21 (2 instances)

def forward(self, input):
    return input


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/linear.py
# Line: 53

def forward(self, x):
    return x


# ==================================================
# Line: 177

def _get_name(self):
    return "QuantizedLinear"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/modules/conv.py
# Line: 431

def _get_name(self):
    return "QuantizedConv1d"


# ==================================================
# Line: 562

def _get_name(self):
    return "QuantizedConv2d"


# ==================================================
# Line: 692

def _get_name(self):
    return "QuantizedConv3d"


# ==================================================
# Line: 785

def _input_padding(
    self, kernel_size: list[int], dilation: list[int], padding: list[int]

# ==================================================
# Line: 954

def _get_name(self):
    return "QuantizedConvTranspose1d"


# ==================================================
# Line: 1077

def _get_name(self):
    return "QuantizedConvTranspose2d"


# ==================================================
# Line: 1202

def _get_name(self):
    return "QuantizedConvTranspose3d"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/dynamic/modules/rnn.py
# Line: 264

def check_hidden_size(
    self,
    hx: Tensor,
    expected_hidden_size: tuple[int, int, int],
    msg: str = "Expected hidden size {}, got {}",

# ==================================================
# Line: 282

def permute_hidden(self, hx: Tensor, permutation: Optional[Tensor]) -> Tensor:
    if permutation is None:
        return hx
    return _apply_permutation(hx, permutation)


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/dynamic/modules/conv.py
# Line: 92

def _get_name(self):
    return "DynamicQuantizedConv1d"


# ==================================================
# Line: 177

def _get_name(self):
    return "DynamicQuantizedConv2d"


# ==================================================
# Line: 262

def _get_name(self):
    return "DynamicQuantizedConv3d"


# ==================================================
# Line: 347

def _get_name(self):
    return "DynamicQuantizedConvTranspose1d"


# ==================================================
# Line: 429

def _get_name(self):
    return "DynamicQuantizedConvTranspose2d"


# ==================================================
# Line: 511

def _get_name(self):
    return "DynamicQuantizedConvTranspose3d"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/reference/modules/rnn.py
# Line: 138

def _get_name(self):
    return "QuantizedRNNCellBase(Reference)"


# ==================================================
# Line: 491

def permute_hidden(  # type: ignore[override]
    self,
    hx: tuple[Tensor, Tensor],
    permutation: Optional[Tensor],

# ==================================================
# Line: 669

def _get_name(self):
    return "QuantizedLSTM(Reference)"


# ==================================================
# Line: 828

def _get_name(self):
    return "QuantizedGRU(Reference)"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/reference/modules/linear.py
# Line: 36

def _get_name(self) -> str:
    return "QuantizedLinear(Reference)"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantized/reference/modules/conv.py
# Line: 109

def _get_name(self):
    return "QuantizedConv1d(Reference)"


# ==================================================
# Line: 172

def _get_name(self):
    return "QuantizedConv2d(Reference)"


# ==================================================
# Line: 235

def _get_name(self):
    return "QuantizedConv3d(Reference)"


# ==================================================
# Line: 345

def _get_name(self):
    return "QuantizedConvTranspose1d(Reference)"


# ==================================================
# Line: 426

def _get_name(self):
    return "QuantizedConvTranspose2d(Reference)"


# ==================================================
# Line: 506

def _get_name(self):
    return "QuantizedConvTranspose3d(Reference)"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/intrinsic/quantized/modules/conv_add.py
# Line: 66

def _get_name(self):
    return "QuantizedConvAdd2d"


# ==================================================
# Line: 134

def _get_name(self):
    return "QuantizedConvAddReLU2d"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/intrinsic/quantized/modules/bn_relu.py
# Line: 45

def _get_name(self):
    return "QuantizedBNReLU2d"


# ==================================================
# Line: 93

def _get_name(self):
    return "QuantizedBNReLU3d"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/intrinsic/quantized/modules/linear_relu.py
# Line: 43

def _get_name(self):
    return "QuantizedLinearReLU"


# ==================================================
# Line: 90

def _get_name(self):
    return "QuantizedLinearLeakyReLU"


# ==================================================
# Line: 158

def _get_name(self):
    return "QuantizedLinearTanh"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/ao/nn/quantizable/modules/activation.py
# Line: 112

def _get_name(self):
    return "QuantizableMultiheadAttention"


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/cpu/__init__.py
# Line: 107

def query(self) -> bool:
    return True


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_activation_checkpointing/knapsack_evaluator.py
# Line: 25

def _get_backward_memory_from_topologically_sorted_graph(
    self,
    node_graph: nx.DiGraph,
    node_memories: dict[str, float],
    saved_nodes_set: set[str],
    peak_memory_after_forward_pass: float,

# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/pyfunctorch.py
# Line: 68

def lower(self):
    return temporarily_pop_interpreter_stack()


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/aot_autograd.py
# Line: 1002

def forward(self, *args, **kwargs):
    return compiled_f(
        named_params,
        named_buffers,
        *args,
        **kwargs,
    )


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/autograd_cache.py
# Line: 354

def _reduce_aot_config(self, aot_config: AOTConfig):
    """
    Reduce the config to a stable key for caching.
    """
    return (
        _ident,
        (
            aot_config.num_params_buffers,
            aot_config.keep_inference_input_mutations,
            aot_config.is_export,
            aot_config.no_tangents,
            aot_config.dynamic_shapes,
            aot_config.aot_autograd_arg_pos_to_source,
            aot_config.enable_log,
            aot_config.pre_dispatch,
        ),
    )


# ==================================================
# Line: 488

def _is_backward(self) -> bool:
    return False


# ==================================================
# File: /root/ecooptimizer/pytorch/torch/_functorch/_aot_autograd/runtime_wrappers.py
# Line: 93

def pre_compile(
    self,
    flat_fn,
    flat_args: list[Tensor],
    aot_config: AOTConfig,
    *,
    fw_metadata: ViewAndMutationMeta,

# ==================================================
# Line: 111

def post_compile(self, compiled_fn, aot_config, *, runtime_metadata) -> Callable:
    """
    Given an output of the compiler, wrap it with information received from prologue.
    Args:
    compiled_fn: Callable after calling compiler_fn
    aot_config: AOTConfig after calling prologue
    runtime_metadata: ViewAndMutationMeta after calling all wrappers's pre_compile steps.
    Example:

    def wrapped_compiled_fn(args):
        # do something with args, aot_config, fw_metadata
        return compiled_fn(args)

    return wrapped_compiled_fn
    """
    return compiled_fn



# ==================================================
# File: /root/ecooptimizer/pytorch/torch/hub.py
# Line: 47

def write(self, s):
    sys.stderr.write(f"{s}\n")


# ==================================================
