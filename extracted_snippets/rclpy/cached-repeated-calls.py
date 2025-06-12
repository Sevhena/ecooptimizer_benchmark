# cached-repeated-calls snippets for rclpy

# File: /root/ecooptimizer/rclpy/rclpy/test/test_parameter_service.py
# Line: 67

results = future.result()

# ==================================================
# Line: 78

results = future.result()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_time_source.py
# Occurrences: Lines 107-108 (2 instances)

now = clock.now()

# ==================================================
# Occurrences: Lines 114-115 (2 instances)

now = clock.now()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_rosout_subscription.py
# Occurrences: Lines 62-67 (2 instances)

logger = self.node.get_logger()

# ==================================================
# Line: 73

logger = self.node.get_logger().get_child('child2')

# ==================================================
# Occurrences: Lines 92-93 (2 instances)

logger = self.node.get_logger().get_child('child')

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_logging.py
# Occurrences: Lines 31-35 (2 instances)

original_severity = rclpy.logging._root_logger.get_effective_level()

# ==================================================
# Occurrences: Lines 42-47 (2 instances)

original_severity = rclpy.logging.get_logger_effective_level(name)

# ==================================================
# Line: 312

rclpy.logging._root_logger.get_effective_level(),

# ==================================================
# Line: 324

original_severity = rclpy.logging._root_logger.get_effective_level()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_callback_group.py
# Occurrences: Lines 43-44 (2 instances)

t1 = self.node.create_timer(1.0, lambda: None, callback_group=group)

# ==================================================
# Occurrences: Lines 135-136 (2 instances)

t1 = self.node.create_timer(1.0, lambda: None, callback_group=group)

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_executor.py
# Occurrences: Lines 90-94 (4 instances)

start_time = time.perf_counter()

# ==================================================
# Line: 188

main_thread_name = get_threads()

# ==================================================
# Occurrences: Lines 196-198 (2 instances)

self.assertTrue(main_thread_name != get_threads())

# ==================================================
# Occurrences: Lines 214-216 (4 instances)

start = time.perf_counter()

# ==================================================
# Occurrences: Lines 497-499 (4 instances)

start = time.perf_counter()

# ==================================================
# Occurrences: Lines 524-524 (2 instances)

t = threading.Thread(target=lambda: set_future_result(future))

# ==================================================
# Occurrences: Lines 533-533 (2 instances)

t = threading.Thread(target=lambda: set_future_result(future))

# ==================================================
# Occurrences: Lines 542-542 (2 instances)

t = threading.Thread(target=lambda: set_future_result(future))

# ==================================================
# Occurrences: Lines 649-649 (2 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 658-658 (2 instances)

end = time.time()

# ==================================================
# Line: 677

start = time.time()

# ==================================================
# Line: 686

end = time.time()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_init_shutdown.py
# Occurrences: Lines 49-53 (2 instances)

context = rclpy.context.Context()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_node.py
# Occurrences: Lines 271-272 (2 instances)

self.assertFalse(self.node.get_publishers_info_by_topic(fq_topic_name))

# ==================================================
# Occurrences: Lines 286-289 (2 instances)

publisher_list = self.node.get_publishers_info_by_topic(fq_topic_name)

# ==================================================
# Occurrences: Lines 309-310 (2 instances)

publisher_list = self.node.get_publishers_info_by_topic(fq_topic_name)

# ==================================================
# Line: 786

result = self.node.declare_parameters('', parameters)

# ==================================================
# Line: 848

self.node.declare_parameters('', parameters)

# ==================================================
# Line: 858

self.node.declare_parameters('', parameters)

# ==================================================
# Line: 867

self.node.declare_parameters('', parameters)

# ==================================================
# Line: 877

self.node.declare_parameters('', parameters)

# ==================================================
# Occurrences: Lines 1096-1099 (2 instances)

self.node.set_parameters(parameters)

# ==================================================
# Line: 1144

self.node.set_parameters(parameters)

# ==================================================
# Line: 1425

results = self.node.set_parameters([Parameter('foo', Parameter.Type.INTEGER, 42)])

# ==================================================
# Line: 1438

results = self.node.set_parameters([Parameter('foo', Parameter.Type.INTEGER, 42)])

# ==================================================
# Line: 1504

result = self.node.set_parameters(
    [
        Parameter(
            name=parameter_tuple[0],
            value=parameter_tuple[1]
        )
    ]
)

# ==================================================
# Line: 1521

result = self.node.set_parameters(
    [
        Parameter(
            name=parameter_tuple[0],
            value=parameter_tuple[1]
        )
    ]
)

# ==================================================
# Occurrences: Lines 1554-1555 (2 instances)

self.track_value1 = self.node.get_parameter('param1')

# ==================================================
# Occurrences: Lines 1568-1569 (2 instances)

self.assertEqual(self.node.get_parameter('param1').value, 1.0)

# ==================================================
# Line: 1658

self.node.set_parameters([
    Parameter('foo', Parameter.Type.INTEGER, 42)])

# ==================================================
# Line: 1669

results = self.node.set_parameters([Parameter('foo', Parameter.Type.INTEGER, 42)])

# ==================================================
# Occurrences: Lines 1747-1750 (2 instances)

self.node.set_parameters_atomically(parameters)

# ==================================================
# Line: 1791

self.node.set_parameters_atomically(parameters)

# ==================================================
# Line: 1811

self.node.set_parameters_atomically([
    Parameter('foo', Parameter.Type.INTEGER, 42)])

# ==================================================
# Line: 1822

result = self.node.set_parameters_atomically(
              [Parameter('foo', Parameter.Type.INTEGER, 42)])

# ==================================================
# Line: 1957

self.node.describe_parameter('foo')

# ==================================================
# Line: 1973

descriptor = self.node.describe_parameter('foo')

# ==================================================
# Line: 2060

self.node.describe_parameter('foo'),

# ==================================================
# Line: 2080

descriptor = self.node.describe_parameter('foo')

# ==================================================
# Line: 2103

descriptor = self.node.describe_parameter('foo')

# ==================================================
# Line: 2150

declared_parameters_result = self.node.declare_parameters('', parameters)

# ==================================================
# Line: 2193

self.node.declare_parameters('', parameters)

# ==================================================
# Line: 2208

result = self.node.declare_parameters('', parameters)

# ==================================================
# Line: 2232

declared_parameters = self.node.declare_parameters('', parameters)

# ==================================================
# Line: 2275

self.node.declare_parameters('', parameters)

# ==================================================
# Line: 2290

result = self.node.declare_parameters('', parameters)

# ==================================================
# Line: 2312

int_param = self.node.get_parameter('int_param')

# ==================================================
# Line: 2349

self.assertEqual(self.node.get_parameter('int_param').value, 4)

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_events_executor.py
# Occurrences: Lines 465-466 (2 instances)

new_pub_future = sub_node.expect_pub_info()

# ==================================================
# Line: 474

new_sub_future = pub_node.expect_sub_info()

# ==================================================
# Occurrences: Lines 480-482 (2 instances)

new_pub_future = sub_node.expect_pub_info()

# ==================================================
# Occurrences: Lines 489-494 (2 instances)

received_future = sub_node.expect_message()

# ==================================================
# Line: 519

received_future = sub_node.expect_message()

# ==================================================
# Line: 527

received_future = sub_node.expect_message()

# ==================================================
# Line: 588

rostime_tick_future = rostime_node.expect_tick()

# ==================================================
# Line: 600

rostime_tick_future = rostime_node.expect_tick()

# ==================================================
# Occurrences: Lines 617-618 (2 instances)

timer1 = rostime_node.create_timer(0.01, handler)

# ==================================================
# Line: 633

got_goal_future = server_node.expect_goal()

# ==================================================
# Line: 670

got_goal_future = server_node.expect_goal()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_client.py
# Occurrences: Lines 80-82 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 91-93 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 103-105 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 119-120 (2 instances)

future1 = cli.call_async(GetParameters.Request())

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_clock.py
# Line: 91

now = clock.now()

# ==================================================
# Occurrences: Lines 98-106 (3 instances)

now2 = clock.now()

# ==================================================
# Occurrences: Lines 269-271 (3 instances)

start = clock.now()

# ==================================================
# Occurrences: Lines 280-282 (2 instances)

start = clock.now()

# ==================================================
# Occurrences: Lines 291-293 (3 instances)

start = clock.now()

# ==================================================
# Occurrences: Lines 302-304 (2 instances)

start = clock.now()

# ==================================================
# Line: 317

retval = clock.sleep_until(clock.now() + Duration(seconds=10))

# ==================================================
# Occurrences: Lines 328-330 (2 instances)

start = clock.now()

# ==================================================
# Occurrences: Lines 356-358 (2 instances)

start = clock.now()

# ==================================================
# Line: 371

clock.now() + Duration(seconds=10), context=non_default_context)

# ==================================================
# Occurrences: Lines 382-384 (2 instances)

start = clock.now()

# ==================================================
# Occurrences: Lines 407-409 (2 instances)

start = clock.now()

# ==================================================
# Occurrences: Lines 438-440 (2 instances)

start = clock.now()

# ==================================================
# Occurrences: Lines 470-472 (2 instances)

start = clock.now()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_parameter_client.py
# Line: 82

results = future.result()

# ==================================================
# Line: 89

results = future.result()

# ==================================================
# Line: 129

result = future.result()

# ==================================================
# Line: 137

result = future.result()

# ==================================================
# Line: 189

results = future.result()

# ==================================================
# Line: 198

results = future.result()

# ==================================================
# Line: 232

results = future.result()

# ==================================================
# Line: 252

results = future.result()

# ==================================================
# Line: 265

results = future.result()

# ==================================================
# Line: 282

results = future.result()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_logging_service.py
# Line: 96

response = future.result()

# ==================================================
# Line: 112

response = future.result()

# ==================================================
# Line: 151

response = future.result()

# ==================================================
# Line: 168

response = future.result()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_rate.py
# Occurrences: Lines 52-56 (2 instances)

last_wake_time = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_service_introspection.py
# Occurrences: Lines 76-81 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 122-127 (2 instances)

start = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_action_graph.py
# Line: 107

start = time.monotonic()

# ==================================================
# Line: 113

end = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_serialization.py
# Occurrences: Lines 65-72 (4 instances)

msg_serialized = serialize_message(msg)

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_action_server.py
# Occurrences: Lines 110-111 (2 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 273-277 (3 instances)

future0 = self.mock_action_client.send_goal(goal_msg)

# ==================================================
# Occurrences: Lines 309-310 (2 instances)

future0 = self.mock_action_client.send_goal(goal_msg)

# ==================================================
# Occurrences: Lines 815-819 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 875-879 (2 instances)

start = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_lifecycle.py
# Occurrences: Lines 171-172 (2 instances)

req = GetState.Request()

# ==================================================
# Occurrences: Lines 179-180 (2 instances)

req = GetState.Request()

# ==================================================
# Occurrences: Lines 189-194 (2 instances)

req = GetAvailableTransitions.Request()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_timer.py
# Occurrences: Lines 93-95 (2 instances)

begin_time = time.time()

# ==================================================
# Occurrences: Lines 127-128 (2 instances)

begin_time = time.time()

# ==================================================
# Occurrences: Lines 137-138 (2 instances)

begin_time = time.time()

# ==================================================
# Occurrences: Lines 145-146 (2 instances)

begin_time = time.time()

# ==================================================
# Occurrences: Lines 173-183 (3 instances)

time_until_next_call = timer.time_until_next_call()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_action_client.py
# Occurrences: Lines 115-116 (2 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 150-152 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 161-163 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 172-174 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 323-325 (3 instances)

future_0 = ac.send_goal_async(Fibonacci.Goal())

# ==================================================
# Occurrences: Lines 432-436 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 473-477 (2 instances)

start = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_logging_rosout.py
# Occurrences: Lines 78-80 (2 instances)

begin_time = time.time()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/test/test_qos_event.py
# Line: 73

publisher = self.node.create_publisher(
    EmptyMsg, self.topic_name, 10, event_callbacks=callbacks)

# ==================================================
# Line: 82

publisher = self.node.create_publisher(
    EmptyMsg, self.topic_name, 10, event_callbacks=callbacks)

# ==================================================
# Line: 90

publisher = self.node.create_publisher(
    EmptyMsg, self.topic_name, 10, event_callbacks=callbacks)

# ==================================================
# Line: 97

publisher = self.node.create_publisher(
    EmptyMsg, self.topic_name, 10, event_callbacks=callbacks)

# ==================================================
# Line: 117

subscription = self.node.create_subscription(
    EmptyMsg, self.topic_name, message_callback, 10, event_callbacks=callbacks)

# ==================================================
# Line: 126

subscription = self.node.create_subscription(
    EmptyMsg, self.topic_name, message_callback, 10, event_callbacks=callbacks)

# ==================================================
# Line: 134

subscription = self.node.create_subscription(
    EmptyMsg, self.topic_name, message_callback, 10, event_callbacks=callbacks)

# ==================================================
# Line: 141

subscription = self.node.create_subscription(
    EmptyMsg, self.topic_name, message_callback, 10, event_callbacks=callbacks)

# ==================================================
# Line: 386

matched_event_index = wait_set.add_event(matched_event_handle)

# ==================================================
# Line: 394

matched_event_index = wait_set.add_event(matched_event_handle)

# ==================================================
# Line: 402

matched_status = matched_event_handle.take_event()

# ==================================================
# Line: 411

matched_event_index = wait_set.add_event(matched_event_handle)

# ==================================================
# Line: 419

matched_status = matched_event_handle.take_event()

# ==================================================
# Line: 435

matched_event_index = wait_set.add_event(matched_event_handle)

# ==================================================
# Line: 443

matched_event_index = wait_set.add_event(matched_event_handle)

# ==================================================
# Line: 451

matched_status = matched_event_handle.take_event()

# ==================================================
# Line: 460

matched_event_index = wait_set.add_event(matched_event_handle)

# ==================================================
# Line: 468

matched_status = matched_event_handle.take_event()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/node.py
# Occurrences: Lines 1479-1484 (2 instances)

return self.get_parameter(name).get_parameter_value()

# ==================================================
# Line: 1505

return self.get_parameter(name).get_parameter_value()

# ==================================================
# Occurrences: Lines 2368-2372 (2 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/lifecycle/node.py
# Line: 401

cb_return_code = self.__execute_callback(
    self._state_machine.current_state[0], life_cycle_state)

# ==================================================
# Line: 413

error_cb_ret_code = self.__execute_callback(
    self._state_machine.current_state[0], life_cycle_state)

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/impl/rcutils_logger.py
# Line: 64

file_path = os.path.realpath(inspect.getframeinfo(frame).filename)

# ==================================================
# Line: 71

file_path = os.path.realpath(inspect.getframeinfo(frame).filename)

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/qos_overriding_options.py
# Line: 183

policy_name = policy.name.lower()

# ==================================================
# Occurrences: Lines 197-202 (2 instances)

f'Unexpected QoS override for policy `{policy.name.lower()}`: `{value}`')

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/executors.py
# Line: 370

start = time.monotonic()

# ==================================================
# Line: 381

now = time.monotonic()

# ==================================================
