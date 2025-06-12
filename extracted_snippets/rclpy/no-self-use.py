# no-self-use snippets for rclpy

# File: /root/ecooptimizer/rclpy/rclpy/test/test_parameter.py
# Line: 213

def test_parameter_value_to_python(self) -> None:
    """Test the parameter_value_to_python conversion function."""
    test_cases = [
        (ParameterValue(type=int(ParameterType.PARAMETER_NOT_SET)), None),
        (ParameterValue(type=int(ParameterType.PARAMETER_INTEGER), integer_value=42), 42),
        (ParameterValue(type=int(ParameterType.PARAMETER_DOUBLE), double_value=3.5), 3.5),
        (ParameterValue(type=int(ParameterType.PARAMETER_STRING), string_value='foo'), 'foo'),
        (
            ParameterValue(
                type=int(ParameterType.PARAMETER_BYTE_ARRAY),
                byte_array_value=[b'J', b'P']
            ),
            [b'J', b'P']
        ),
        (
            ParameterValue(
                type=int(ParameterType.PARAMETER_INTEGER_ARRAY),
                integer_array_value=[1, 2, 3]),
            [1, 2, 3]
        ),
        (
            ParameterValue(
                type=int(ParameterType.PARAMETER_DOUBLE_ARRAY),
                double_array_value=[1.0, 2.0, 3.0]),
            [1.0, 2.0, 3.0]
        ),
        (
            ParameterValue(
                type=int(ParameterType.PARAMETER_STRING_ARRAY),
                string_array_value=['foo', 'bar']),
            ['foo', 'bar']
        ),
    ]

    for input_value, expected_value in test_cases:
        result_value = parameter_value_to_python(input_value)
        if isinstance(result_value, list) and isinstance(expected_value, list):
            assert len(result_value) == len(expected_value)
            # element-wise comparison for lists
            assert all(x == y for x, y in zip(result_value, expected_value))
        else:
            assert result_value == expected_value

    # Test invalid 'type' member
    parameter_value = ParameterValue(type=42)
    with pytest.raises(RuntimeError):
        parameter_value_to_python(parameter_value)


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_validate_topic_name.py
# Line: 24

def test_validate_topic_name(self) -> None:
    tests = [
        'chatter',
        '{node}/chatter',
        '~/chatter',
    ]
    for topic in tests:
        # Will raise if invalid
        validate_topic_name(topic)


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_logging.py
# Line: 373

def test_get_logging_directory(self) -> None:
    os.environ['HOME'] = '/fake_home_dir'
    os.environ.pop('USERPROFILE', None)
    os.environ.pop('ROS_LOG_DIR', None)
    os.environ.pop('ROS_HOME', None)
    log_dir = rclpy.logging.get_logging_directory()
    assert isinstance(log_dir, Path)
    assert log_dir == Path('/fake_home_dir') / '.ros' / 'log'



# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_waitable.py
# Line: 423

def test_add(self) -> None:
    n1 = NumberOfEntities(1, 2, 3, 4, 5, 6)
    n2 = NumberOfEntities(10, 20, 30, 40, 50, 60)
    n = n1 + n2
    assert n.num_subscriptions == 11
    assert n.num_guard_conditions == 22
    assert n.num_timers == 33
    assert n.num_clients == 44
    assert n.num_services == 55
    assert n.num_events == 66


# ==================================================
# Line: 434

def test_add_assign(self) -> None:
    n1 = NumberOfEntities(1, 2, 3, 4, 5, 6)
    n2 = NumberOfEntities(10, 20, 30, 40, 50, 60)
    n1 += n2
    assert n1.num_subscriptions == 11
    assert n1.num_guard_conditions == 22
    assert n1.num_timers == 33
    assert n1.num_clients == 44
    assert n1.num_services == 55
    assert n1.num_events == 66

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_validate_namespace.py
# Line: 23

def test_validate_namespace(self) -> None:
    tests = [
        '/my_ns',
        '/',
    ]
    for topic in tests:
        # Will raise if invalid
        validate_namespace(topic)


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_qos.py
# Line: 39

def test_depth_only_constructor(self) -> None:
    qos = QoSProfile(depth=1)
    assert qos.depth == 1
    assert qos.history == QoSHistoryPolicy.KEEP_LAST


# ==================================================
# Line: 109

def test_policy_short_names(self) -> None:
    # Full test on History to show the mechanism works
    assert (
        QoSHistoryPolicy.short_keys() ==
        ['system_default', 'keep_last', 'keep_all', 'unknown'])
    assert (
        QoSHistoryPolicy.get_from_short_key('system_default') ==
        QoSHistoryPolicy.SYSTEM_DEFAULT.value)
    assert (
        QoSHistoryPolicy.get_from_short_key('KEEP_ALL') ==
        QoSHistoryPolicy.KEEP_ALL.value)
    assert (
        QoSHistoryPolicy.get_from_short_key('KEEP_last') ==
        QoSHistoryPolicy.KEEP_LAST.value)


# ==================================================
# Line: 124

def test_preset_profiles(self) -> None:
    # Make sure the Enum does what we expect
    assert QoSPresetProfiles.SYSTEM_DEFAULT.value == qos_profile_system_default
    assert (
        QoSPresetProfiles.SYSTEM_DEFAULT.value ==
        QoSPresetProfiles.get_from_short_key('system_default'))


# ==================================================
# Line: 131

def test_keep_last_zero_depth_constructor(self) -> None:
    with warnings.catch_warnings(record=True) as caught_warnings:
        warnings.simplefilter('always', category=UserWarning)
        qos = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, depth=0)
        assert len(caught_warnings) == 1
        assert issubclass(caught_warnings[0].category, UserWarning)
        assert "A zero depth with KEEP_LAST doesn't make sense" in str(caught_warnings[0])
    assert qos.history == QoSHistoryPolicy.KEEP_LAST


# ==================================================
# Line: 140

def test_keep_last_zero_depth_set(self) -> None:
    qos = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, depth=1)
    assert qos.depth == 1

    with warnings.catch_warnings(record=True) as caught_warnings:
        warnings.simplefilter('always', category=UserWarning)
        qos.depth = 0
        assert len(caught_warnings) == 1
        assert issubclass(caught_warnings[0].category, UserWarning)
        assert "A zero depth with KEEP_LAST doesn't make sense" in str(caught_warnings[0])



# ==================================================
# Line: 154

def test_compatible(self) -> None:
    qos = QoSProfile(
        depth=1,
        reliability=QoSReliabilityPolicy.RELIABLE,
        durability=QoSDurabilityPolicy.VOLATILE,
        lifespan=Duration(seconds=1),
        deadline=Duration(seconds=1),
        liveliness=QoSLivelinessPolicy.AUTOMATIC,
        liveliness_lease_duration=Duration(seconds=1),
    )
    compatibility, reason = qos_check_compatible(
        qos, qos
    )

    assert compatibility == QoSCompatibility.OK
    assert reason == ''


# ==================================================
# Line: 171

def test_incompatible(self) -> None:
    """
    This test is assuming a DDS implementation.

    It's possible that a "best effort" publisher and "reliable"
    subscription is a valid match in a non-DDS implementation.
    """
    pub_qos = QoSProfile(
        depth=1,
        reliability=QoSReliabilityPolicy.BEST_EFFORT,
    )
    sub_qos = QoSProfile(
        depth=1,
        reliability=QoSReliabilityPolicy.RELIABLE,
    )

    compatibility, reason = qos_check_compatible(
        pub_qos, sub_qos
    )

    if _rclpy.rclpy_get_rmw_implementation_identifier() != 'rmw_zenoh_cpp':
        assert compatibility == QoSCompatibility.ERROR
        assert reason != ''
    else:
        assert compatibility == QoSCompatibility.OK
        assert reason == ''


# ==================================================
# Line: 198

def test_warn_of_possible_incompatibility(self) -> None:
    """
    This test is assuming a DDS implementation.

    It's possible that a "best effort" publisher and "reliable"
    subscription is a valid match in a non-DDS implementation.
    """
    pub_qos = QoSPresetProfiles.SYSTEM_DEFAULT.value
    sub_qos = QoSProfile(
        depth=1,
        reliability=QoSReliabilityPolicy.RELIABLE,
    )
    compatibility, reason = qos_check_compatible(
        pub_qos, sub_qos
    )

    if _rclpy.rclpy_get_rmw_implementation_identifier() != 'rmw_zenoh_cpp':
        assert compatibility == QoSCompatibility.WARNING
        assert reason != ''
    else:
        assert compatibility == QoSCompatibility.OK
        assert reason == ''

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_validate_full_topic_name.py
# Line: 24

def test_validate_full_topic_name(self) -> None:
    tests = [
        '/chatter',
        '/node_name/chatter',
        '/ns/node_name/chatter',
    ]
    for topic in tests:
        # Will raise if invalid
        validate_full_topic_name(topic)


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_node.py
# Line: 409

def modify_parameter_callback(self, parameters_list: List[Parameter[Any]]):
    modified_list = parameters_list.copy()
    for param in parameters_list:
        if param.name == 'foo':
            modified_list.append(Parameter('bar', Parameter.Type.STRING, 'hello'))

    return modified_list


# ==================================================
# Occurrences: Lines 914-921 (3 instances)

def return_none_parameter_callback(self, parameter_list):
    return None


# ==================================================
# Line: 1389

def modify_parameter_callback(self, parameter_list: List[Parameter[Any]]
                              ) -> List[Parameter[Any]]:
    modified_list = parameter_list.copy()
    for param in parameter_list:
        if param.name == 'foo':
            modified_list.append(Parameter('bar', Parameter.Type.STRING, 'hello'))

    return modified_list


# ==================================================
# Line: 1398

def empty_parameter_callback(self, parameter_list: List[Parameter[Any]]):
    return []


# ==================================================
# Line: 2434

def test_node_get_fully_qualified_name(self) -> None:
    context = rclpy.context.Context()
    rclpy.init(context=context)

    try:
        node = rclpy.create_node(TEST_NODE, namespace=TEST_NAMESPACE, context=context)
        try:
            assert node.get_fully_qualified_name() == '{}/{}'.format(TEST_NAMESPACE, TEST_NODE)
        finally:
            node.destroy_node()

        # When ns is not specified, a leading / should be added
        node_without_ns = rclpy.create_node(TEST_NODE, context=context)
        try:
            assert node_without_ns.get_fully_qualified_name() == '/' + TEST_NODE
        finally:
            node_without_ns.destroy_node()

        remapped_ns = '/another_ns'
        remapped_name = 'another_node'
        node_with_remapped_ns = rclpy.create_node(
            TEST_NODE,
            namespace=TEST_NAMESPACE,
            context=context,
            cli_args=['--ros-args', '-r', '__ns:=' + remapped_ns]
        )
        try:
            expected_name = '{}/{}'.format(remapped_ns, TEST_NODE)
            assert node_with_remapped_ns.get_fully_qualified_name() == expected_name
        finally:
            node_with_remapped_ns.destroy_node()

        node_with_remapped_name = rclpy.create_node(
            TEST_NODE,
            namespace=TEST_NAMESPACE,
            context=context,
            cli_args=['--ros-args', '-r', '__node:=' + remapped_name]
        )
        try:
            expected_name = '{}/{}'.format(TEST_NAMESPACE, remapped_name)
            assert node_with_remapped_name.get_fully_qualified_name() == expected_name
        finally:
            node_with_remapped_name.destroy_node()

        node_with_remapped_ns_name = rclpy.create_node(
            TEST_NODE,
            namespace=TEST_NAMESPACE,
            context=context,
            cli_args=[
                '--ros-args', '-r', '__node:=' + remapped_name, '-r', '__ns:=' + remapped_ns]
        )
        try:
            expected_name = '{}/{}'.format(remapped_ns, remapped_name)
            assert node_with_remapped_ns_name.get_fully_qualified_name() == expected_name
        finally:
            node_with_remapped_ns_name.destroy_node()
    finally:
        rclpy.shutdown(context=context)


# ==================================================
# Line: 2493

def test_node_get_fully_qualified_name_global_remap(self) -> None:
    g_context = rclpy.context.Context()
    global_remap_name = 'global_node_name'
    rclpy.init(
        args=['--ros-args', '-r', '__node:=' + global_remap_name],
        context=g_context,
    )
    try:
        node_with_global_arguments = rclpy.create_node(
            TEST_NODE,
            namespace=TEST_NAMESPACE,
            context=g_context,
        )
        try:
            expected_name = '{}/{}'.format(TEST_NAMESPACE, global_remap_name)
            assert node_with_global_arguments.get_fully_qualified_name() == expected_name
        finally:
            node_with_global_arguments.destroy_node()

        node_skip_global_params = rclpy.create_node(
            TEST_NODE,
            namespace=TEST_NAMESPACE,
            context=g_context,
            use_global_arguments=False
        )
        try:
            expected_name = '{}/{}'.format(TEST_NAMESPACE, TEST_NODE)
            assert node_skip_global_params.get_fully_qualified_name() == expected_name
        finally:
            node_skip_global_params.destroy_node()
    finally:
        rclpy.shutdown(context=g_context)


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_client.py
# Line: 175

def test_get_service_name(self) -> None:
    test_service_name_list = [
        # test_service_name, namespace, cli_args for remap, expected service name
        # No namespaces
        ('service', None, None, '/service'),
        ('example/service', None, None, '/example/service'),
        # Using service names with namespaces
        ('service', 'ns', None, '/ns/service'),
        ('example/service', 'ns', None, '/ns/example/service'),
        ('example/service', 'my/ns', None, '/my/ns/example/service'),
        ('example/service', '/my/ns', None, '/my/ns/example/service'),
        # Global service name
        ('/service', 'ns', None, '/service'),
        ('/example/service', 'ns', None, '/example/service')
    ]
    TestClient.do_test_service_name(test_service_name_list)


# ==================================================
# Line: 192

def test_get_service_name_after_remapping(self) -> None:
    test_service_name_list = [
        ('service', None, ['--ros-args', '--remap', 'service:=new_service'], '/new_service'),
        ('service', 'ns', ['--ros-args', '--remap', 'service:=new_service'],
         '/ns/new_service'),
        ('service', 'ns', ['--ros-args', '--remap', 'service:=example/new_service'],
         '/ns/example/new_service'),
        ('example/service', 'ns', ['--ros-args', '--remap', 'example/service:=new_service'],
         '/ns/new_service')
    ]
    TestClient.do_test_service_name(test_service_name_list)


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_clock.py
# Line: 87

def test_clock_now(self) -> None:
    # System time should be roughly equal to time.time()
    # There will still be differences between them, with the bound depending on the scheduler.
    clock = Clock(clock_type=ClockType.SYSTEM_TIME)
    now = clock.now()
    python_time_sec = time.time()
    assert isinstance(now, Time)
    assert abs(now.nanoseconds * 1e-9 - python_time_sec) < 5

    # Unless there is a date change during the test, system time have increased between these
    # calls.
    now2 = clock.now()
    assert now2 > now

    # Steady time should always return increasing values
    clock = Clock(clock_type=ClockType.STEADY_TIME)
    now = clock.now()
    now2 = now
    for i in range(10):
        now2 = clock.now()
        assert now2 > now
        now = now2


# ==================================================
# Line: 110

def test_ros_time_is_active(self) -> None:
    clock = ROSClock()
    clock._set_ros_time_is_active(True)
    assert clock.ros_time_is_active
    clock._set_ros_time_is_active(False)
    assert not clock.ros_time_is_active


# ==================================================
# Line: 117

def test_triggered_time_jump_callbacks(self) -> None:
    one_second = Duration(seconds=1)
    half_second = Duration(seconds=0.5)
    negative_half_second = Duration(seconds=-0.5)
    negative_one_second = Duration(seconds=-1)

    threshold1 = JumpThreshold(
        min_forward=one_second, min_backward=negative_half_second, on_clock_change=False)
    threshold2 = JumpThreshold(
        min_forward=half_second, min_backward=negative_one_second, on_clock_change=False)

    pre_callback1 = Mock()
    post_callback1 = Mock()
    pre_callback2 = Mock()
    post_callback2 = Mock()

    clock = ROSClock()
    handler1 = clock.create_jump_callback(
        threshold1, pre_callback=pre_callback1, post_callback=post_callback1)
    handler2 = clock.create_jump_callback(
        threshold2, pre_callback=pre_callback2, post_callback=post_callback2)

    clock.set_ros_time_override(Time(seconds=1))
    clock._set_ros_time_is_active(True)
    pre_callback1.assert_not_called()
    post_callback1.assert_not_called()
    pre_callback2.assert_not_called()
    post_callback2.assert_not_called()

    # forward jump
    clock.set_ros_time_override(Time(seconds=1.75))
    pre_callback1.assert_not_called()
    post_callback1.assert_not_called()
    pre_callback2.assert_called()
    post_callback2.assert_called()

    pre_callback1.reset_mock()
    post_callback1.reset_mock()
    pre_callback2.reset_mock()
    post_callback2.reset_mock()

    # backwards jump
    clock.set_ros_time_override(Time(seconds=1))
    pre_callback1.assert_called()
    post_callback1.assert_called()
    pre_callback2.assert_not_called()
    post_callback2.assert_not_called()

    handler1.unregister()
    handler2.unregister()


# ==================================================
# Line: 168

def test_triggered_clock_change_callbacks(self) -> None:
    one_second = Duration(seconds=1)
    negative_one_second = Duration(seconds=-1)

    threshold1 = JumpThreshold(
        min_forward=one_second, min_backward=negative_one_second, on_clock_change=False)
    threshold2 = JumpThreshold(min_forward=None, min_backward=None, on_clock_change=True)
    threshold3 = JumpThreshold(
        min_forward=one_second, min_backward=negative_one_second, on_clock_change=True)

    pre_callback1 = Mock()
    post_callback1 = Mock()
    pre_callback2 = Mock()
    post_callback2 = Mock()
    pre_callback3 = Mock()
    post_callback3 = Mock()

    clock = ROSClock()
    handler1 = clock.create_jump_callback(
        threshold1, pre_callback=pre_callback1, post_callback=post_callback1)
    handler2 = clock.create_jump_callback(
        threshold2, pre_callback=pre_callback2, post_callback=post_callback2)
    handler3 = clock.create_jump_callback(
        threshold3, pre_callback=pre_callback3, post_callback=post_callback3)

    clock._set_ros_time_is_active(True)
    pre_callback1.assert_not_called()
    post_callback1.assert_not_called()
    pre_callback2.assert_called()
    post_callback2.assert_called()
    pre_callback3.assert_called()
    post_callback3.assert_called()

    pre_callback1.reset_mock()
    post_callback1.reset_mock()
    pre_callback2.reset_mock()
    post_callback2.reset_mock()
    pre_callback3.reset_mock()
    post_callback3.reset_mock()

    clock._set_ros_time_is_active(True)
    pre_callback1.assert_not_called()
    post_callback1.assert_not_called()
    pre_callback2.assert_not_called()
    post_callback2.assert_not_called()
    pre_callback3.assert_not_called()
    post_callback3.assert_not_called()

    handler1.unregister()
    handler2.unregister()
    handler3.unregister()



# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_time.py
# Line: 203

def test_time_message_conversions(self) -> None:
    time1 = Time(nanoseconds=1, clock_type=ClockType.ROS_TIME)
    builtins_msg = Builtins()
    builtins_msg.time_value = time1.to_msg()

    # Default clock type resulting from from_msg will be ROS time
    time2 = Time.from_msg(builtins_msg.time_value)
    assert isinstance(time2, Time)
    assert time1 == time2
    # Clock type can be specified if appropriate
    time3 = Time.from_msg(builtins_msg.time_value, clock_type=ClockType.SYSTEM_TIME)
    assert time3.clock_type == ClockType.SYSTEM_TIME


# ==================================================
# Line: 216

def test_time_message_conversions_big_nanoseconds(self) -> None:
    time1 = Time(nanoseconds=1553575413247045598, clock_type=ClockType.ROS_TIME)
    builtins_msg = Builtins()
    builtins_msg.time_value = time1.to_msg()

    # Default clock type resulting from from_msg will be ROS time
    time2 = Time.from_msg(builtins_msg.time_value)
    assert isinstance(time2, Time)
    assert time1 == time2


# ==================================================
# Line: 226

def test_duration_message_conversions(self) -> None:
    duration = Duration(nanoseconds=1)
    builtins_msg = Builtins()
    builtins_msg.duration_value = duration.to_msg()
    duration2 = Duration.from_msg(builtins_msg.duration_value)
    assert isinstance(duration2, Duration)
    assert duration2.nanoseconds == 1


# ==================================================
# Occurrences: Lines 234-239 (2 instances)

def test_seconds_nanoseconds(self) -> None:
    assert (1, int(5e8)) == Time(seconds=1, nanoseconds=5e8).seconds_nanoseconds()
    assert (1, int(5e8)) == Time(seconds=0, nanoseconds=15e8).seconds_nanoseconds()
    assert (0, 0) == Time().seconds_nanoseconds()


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_service_introspection.py
# Line: 55

def srv_callback(self, req, resp):
    resp.bool_value = not req.bool_value
    resp.int64_value = req.int64_value
    return resp


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_action_graph.py
# Line: 98

def get_names_and_types(
    self,
    get_names_and_types_func: Callable[..., List[Any]],
    *args: Any,
    expected_num_names: int,
    timeout: float = 5.0

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_context.py
# Line: 27

def on_shutdown(self) -> None:
    nonlocal callback_called
    callback_called = True


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_action_server.py
# Line: 114

def execute_goal_callback(self, goal_handle: ServerGoalHandle[Any, Fibonacci.Result, Any]
                          ) -> Fibonacci.Result:
    goal_handle.succeed()
    return Fibonacci.Result()


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_action_client.py
# Line: 64

def goal_callback(self, request: Fibonacci.Impl.SendGoalService.Request,
                  response: Fibonacci.Impl.SendGoalService.Response
                  ) -> Fibonacci.Impl.SendGoalService.Response:
    response.accepted = True
    return response


# ==================================================
# Line: 70

def cancel_callback(self, request: Fibonacci.Impl.CancelGoalService.Request,
                    response: Fibonacci.Impl.CancelGoalService.Response
                    ) -> Fibonacci.Impl.CancelGoalService.Response:
    response.goals_canceling.append(request.goal_info)
    return response


# ==================================================
# Line: 76

def result_callback(self, request: Fibonacci.Impl.GetResultService.Request,
                    response: Fibonacci.Impl.GetResultService.Response
                    ) -> Fibonacci.Impl.GetResultService.Response:
    return response


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_task.py
# Line: 283

def test_cancel_invokes_callbacks(self) -> None:
    called = False

    def cb(fut: Future[Any]) -> None:
        nonlocal called
        called = True

    f: Future[Any] = Future()
    f.add_done_callback(cb)
    f.cancel()
    assert called


# ==================================================
# Line: 295

def test_set_result_invokes_callbacks(self) -> None:
    called = False

    def cb(fut: Future[Any]) -> None:
        nonlocal called
        called = True

    f: Future[str] = Future()
    f.add_done_callback(cb)
    f.set_result('Anything')
    assert called


# ==================================================
# Line: 307

def test_set_exception_invokes_callbacks(self) -> None:
    called = False

    def cb(fut: Future[Any]) -> None:
        nonlocal called
        called = True

    f: Future[Any] = Future()
    f.add_done_callback(cb)
    f.set_exception(Exception('Anything'))
    assert called


# ==================================================
# Line: 319

def test_add_done_callback_invokes_callback(self) -> None:
    called = False

    def cb(fut: Future[Any]) -> None:
        nonlocal called
        called = True

    f: Future[str] = Future()
    f.set_result('Anything')
    f.add_done_callback(cb)
    assert called


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_qos_event.py
# Line: 158

def warning(self, message, once=False):
    nonlocal pub_log_msg, sub_log_msg, log_msgs_future

    if message.startswith('New subscription discovered'):
        pub_log_msg = message
    elif message.startswith('New publisher discovered'):
        sub_log_msg = message

    if pub_log_msg is not None and sub_log_msg is not None:
        log_msgs_future.set_result(True)


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_validate_node_name.py
# Line: 23

def test_validate_node_name(self) -> None:
    tests = [
        'my_node',
    ]
    for topic in tests:
        # Will raise if invalid
        validate_node_name(topic)


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/action/client.py
# Line: 246

def _generate_random_uuid(self) -> UUID:
    return UUID(uuid=list(uuid.uuid4().bytes))


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/node.py
# Line: 362

def handle(self, value: None) -> None:
    raise AttributeError('handle cannot be modified after node creation')


# ==================================================
# Line: 1323

def _apply_integer_range(
    self,
    parameter: Parameter[int],
    integer_range: IntegerRange

# ==================================================
# Line: 1517

def _validate_qos_or_depth_parameter(self, qos_or_depth: Union[QoSProfile, int]) -> QoSProfile:
    if isinstance(qos_or_depth, QoSProfile):
        return qos_or_depth
    elif isinstance(qos_or_depth, int):
        if qos_or_depth < 0:
            raise ValueError('history depth must be greater than or equal to zero')
        return QoSProfile(depth=qos_or_depth)
    else:
        raise TypeError(
            'Expected QoSProfile or int, but received {!r}'.format(type(qos_or_depth)))


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/logging_service.py
# Line: 48

def _get_logger_levels(self, request: GetLoggerLevels.Request,
                       response: GetLoggerLevels.Response) -> GetLoggerLevels.Response:
    for name in request.names:
        logger_level = LoggerLevel()
        logger_level.name = name
        try:
            ret_level = rclpy.logging.get_logger_level(name)
        except RuntimeError:
            ret_level = LoggingSeverity.UNSET
        logger_level.level = ret_level
        response.levels.append(logger_level)
    return response


# ==================================================
# Line: 61

def _set_logger_levels(self, request: SetLoggerLevels.Request,
                       response: SetLoggerLevels.Response) -> SetLoggerLevels.Response:
    for level in request.levels:
        result = SetLoggerLevelsResult()
        result.successful = False
        try:
            rclpy.logging.set_logger_level(level.name, level.level, detailed_error=True)
            result.successful = True
        except ValueError:
            result.reason = 'Failed reason: Invalid logger level.'
        except RuntimeError as e:
            result.reason = str(e)
        response.results.append(result)
    return response

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/lifecycle/managed_entity.py
# Occurrences: Lines 30-50 (6 instances)

def on_configure(self, state: 'LifecycleState') -> TransitionCallbackReturn:
    """Handle configure transition request."""
    return TransitionCallbackReturn.SUCCESS


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/executors.py
# Line: 425

def _take_timer(self, tmr: Timer) -> Optional[Callable[[], Coroutine[None, None, None]]]:
    try:
        with tmr.handle:
            info = tmr.handle.call_timer_with_info()
            timer_info = TimerInfo(
                expected_call_time=info['expected_call_time'],
                actual_call_time=info['actual_call_time'],
                clock_type=tmr.clock.clock_type)

            def check_argument_type(callback_func: Union[Callable[[], None],
                                                         Callable[[TimerInfo], None]],
                                    target_type: Type[TimerInfo]) -> Optional[str]:
                sig = inspect.signature(callback_func)
                for param in sig.parameters.values():
                    if param.annotation == target_type:
                        # return 1st one immediately
                        return param.name
                # We could not find the target type in the signature
                return None

            # User might change the Timer.callback function signature at runtime,
            # so it needs to check the signature every time.
            if tmr.callback:
                arg_name = check_argument_type(tmr.callback, target_type=TimerInfo)
            if arg_name is not None:
                prefilled_arg = {arg_name: timer_info}

                async def _execute() -> None:
                    if tmr.callback:
                        await await_or_execute(partial(tmr.callback, **prefilled_arg))
                return _execute
            else:
                async def _execute() -> None:
                    if tmr.callback:
                        await await_or_execute(tmr.callback)
                return _execute
    except InvalidHandle:
        # Timer is a Destroyable, which means that on __enter__ it can throw an
        # InvalidHandle exception if the entity has already been destroyed.  Handle that here
        # by just returning an empty argument, which means we will skip doing any real work
        # in _execute_timer below
        pass

    return None


# ==================================================
# Line: 470

def _take_subscription(self, sub: Subscription[Any]
                       ) -> Optional[Callable[[], Coroutine[None, None, None]]]:
    try:
        with sub.handle:
            msg_info = sub.handle.take_message(sub.msg_type, sub.raw)
            if msg_info is None:
                return None

            if sub._callback_type is Subscription.CallbackType.MessageOnly:
                msg_tuple: Union[Tuple[Msg], Tuple[Msg, MessageInfo]] = (msg_info[0], )
            else:
                msg_tuple = msg_info

            async def _execute() -> None:
                await await_or_execute(sub.callback, *msg_tuple)

            return _execute
    except InvalidHandle:
        # Subscription is a Destroyable, which means that on __enter__ it can throw an
        # InvalidHandle exception if the entity has already been destroyed.  Handle that here
        # by just returning an empty argument, which means we will skip doing any real work
        # in _execute_subscription below
        pass

    return None


# ==================================================
# Line: 526

def _take_service(self, srv: Service[Any, Any]
                  ) -> Optional[Callable[[], Coroutine[None, None, None]]]:
    try:
        with srv.handle:
            request_and_header = srv.handle.service_take_request(srv.srv_type.Request)

        async def _execute() -> None:
            (request, header) = request_and_header
            if header is None:
                return

            response = await await_or_execute(srv.callback, request, srv.srv_type.Response())
            srv.send_response(response, header)
        return _execute
    except InvalidHandle:
        # Service is a Destroyable, which means that on __enter__ it can throw an
        # InvalidHandle exception if the entity has already been destroyed.  Handle that here
        # by just returning an empty argument, which means we will skip doing any real work
        # in _execute_service below
        pass

    return None


# ==================================================
# Line: 549

def _take_guard_condition(self, gc: GuardCondition
                          ) -> Callable[[], Coroutine[None, None, None]]:
    gc._executor_triggered = False

    async def _execute() -> None:
        if gc.callback:
            await await_or_execute(gc.callback)
    return _execute


# ==================================================
# Line: 623

def can_execute(self, entity: 'Entity') -> bool:
    """
    Determine if a callback for an entity can be executed.

    :param entity: Subscription, Timer, Guard condition, etc
    :returns: ``True`` if the entity callback can be executed, ``False`` otherwise.
    """
    return not entity._executor_event and entity.callback_group is not None \
        and entity.callback_group.can_execute(entity)


# ==================================================
