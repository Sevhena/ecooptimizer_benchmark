# use-a-generator snippets for tensorflow

# File: /root/ecooptimizer/tensorflow/tensorflow/dtensor/python/config.py
# Line: 165

if any([name.startswith("/bns/") for name in d_jobs_list]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
# Line: 124

return all([
    attr1 == attr2
    for attr1, attr2 in zip(self.__dict__.items(), other.__dict__.items())
])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/tpu/tpu_embedding_v3_utils.py
# Line: 102

is_init_value_padded = all(
    [i >= j for i, j in zip(checkpoint_value_shape, variable_shape)]
)

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
# Line: 777

if any(
    [not x.is_uniform() for x in self.row_partitions[-new_dimensions:]]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Line: 89

if not any([_divides(x, first_candidate) for x in primes_so_far]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/saved_model/function_deserialization.py
# Line: 312

if any([inp is None for inp in function.captured_inputs]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/distributed_save_ft_test.py
# Line: 83

return all([snapshot_is_done(path) for path in paths])

# ==================================================
# Line: 89

while not all([snapshot_is_done(path) or snapshot_has_error(path)
               for path in paths]):

# ==================================================
# Line: 315

each_worker_has_enough_assignments = all([
    len(per_worker_assignments) >= worker_max_concurrent_snapshots
    for per_worker_assignments in assignments.values()])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/checkpoint/functional_saver.py
# Line: 636

if any([context.is_custom_device(st.device.to_string()) for st in sts]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
# Line: 355

ops.get_default_graph()) or not all(
    [_is_gpu_device(d) for d in self._devices])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# Line: 393

) or not all([_is_gpu_device(d) for d in self._devices])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver.py
# Line: 48

assert all([x in os.environ for x in [_SM_CURRENT_HOST, _SM_HOSTS]
           ]), 'Not a SageMaker Environment'

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/distribute/mirrored_run.py
# Line: 66

if fn._jit_compile and all(  # pylint: disable=protected-access
    [_is_gpu_device(d) for d in strategy.extended.worker_devices]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
# Line: 52

if not all([isinstance(x, tensor.Tensor) for x in flat_args]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir_test.py
# Line: 35

if not all([isinstance(x, tensor.Tensor) for x in flat_args]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
# Line: 1128

distributed_model._recompile_exec_function = any(
    [e.sample_weights_mismatch() for e in model._training_endpoints])

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
# Line: 591

if not ops.executing_eagerly_outside_functions() and any([
    spec._tensor.op.type in _REF_VARIABLE_OPS
    for spec in self.specs
    if isinstance(spec._tensor, tensor_lib.Tensor)]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/capture/restore_captures.py
# Line: 127

if any([inp is None for inp in captured_inputs_list]):

# ==================================================
# File: /root/ecooptimizer/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
# Line: 57

if all([self._object == other._object for other in others]):

# ==================================================
