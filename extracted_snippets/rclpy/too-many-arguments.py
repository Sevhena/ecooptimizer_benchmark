# too-many-arguments snippets for rclpy

# File: /root/ecooptimizer/rclpy/rclpy/rclpy/client.py
# Line: 40

def __init__(
    self,
    context: Context,
    client_impl: '_rclpy.Client[SrvRequestT, SrvResponseT]',
    srv_type: Type[Srv],
    srv_name: str,
    qos_profile: QoSProfile,
    callback_group: CallbackGroup

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/__init__.py
# Line: 214

def create_node(
    node_name: str,
    *,
    context: Optional[Context] = None,
    cli_args: Optional[List[str]] = None,
    namespace: Optional[str] = None,
    use_global_arguments: bool = True,
    enable_rosout: bool = True,
    rosout_qos_profile: Union[QoSProfile, int] = qos_profile_rosout_default,
    start_parameter_services: bool = True,
    parameter_overrides: Optional[List[Parameter[Any]]] = None,
    allow_undeclared_parameters: bool = False,
    automatically_declare_parameters_from_overrides: bool = False,
    enable_logger_service: bool = False

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/service.py
# Line: 37

def __init__(
    self,
    service_impl: '_rclpy.Service[SrvRequestT, SrvResponseT]',
    srv_type: Type[Srv],
    srv_name: str,
    callback: Callable[[SrvRequestT, SrvResponseT], SrvResponseT],
    callback_group: CallbackGroup,
    qos_profile: QoSProfile

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/qos.py
# Line: 75

def __init__(self,
             history: Union['QoSHistoryPolicy', int, None] = None,
             depth: Optional[int] = None,
             reliability: Union['QoSReliabilityPolicy', int, None] = None,
             durability: Union['QoSDurabilityPolicy', int, None] = None,
             lifespan: Optional[Duration] = None,
             deadline: Optional[Duration] = None,
             liveliness: Union['QoSLivelinessPolicy', int, None] = None,
             liveliness_lease_duration: Optional[Duration] = None,
             avoid_ros_namespace_conventions: Optional[bool] = None) -> None:

    if history is None:
        if depth is None:
            raise InvalidQoSProfileException('History and/or depth settings are required.')
        history = QoSHistoryPolicy.KEEP_LAST

    self.history = history

    if (
        QoSHistoryPolicy.KEEP_LAST == self.history and depth is None
    ):
        raise InvalidQoSProfileException('History set to KEEP_LAST without a depth setting.')

    self.depth = QoSProfile.__qos_profile_default_dict['depth'] if depth is None else depth

    self.reliability = QoSProfile.__qos_profile_default_dict['reliability'] \
        if reliability is None else reliability

    self.durability = QoSProfile.__qos_profile_default_dict['durability'] \
        if durability is None else durability

    self.lifespan = QoSProfile.__qos_profile_default_dict['lifespan'] \
        if lifespan is None else lifespan

    self.deadline = QoSProfile.__qos_profile_default_dict['deadline'] \
        if deadline is None else deadline

    self.liveliness = QoSProfile.__qos_profile_default_dict['liveliness'] \
        if liveliness is None else liveliness

    self.liveliness_lease_duration =  \
        QoSProfile.__qos_profile_default_dict['liveliness_lease_duration'] \
        if liveliness_lease_duration is None else liveliness_lease_duration

    self.avoid_ros_namespace_conventions = \
        QoSProfile.__qos_profile_default_dict['avoid_ros_namespace_conventions'] \
        if avoid_ros_namespace_conventions is None else avoid_ros_namespace_conventions


# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/parameter_client.py
# Line: 355

def on_parameter_event(
    self, callback: Union[Callable[[ParameterEvent], None],
                          Callable[[ParameterEvent, MessageInfo], None]],
    qos_profile: QoSProfile = qos_profile_parameter_events,
    *,
    callback_group: Optional[CallbackGroup] = None,
    event_callbacks: Optional[SubscriptionEventCallbacks] = None,
    qos_overriding_options: Optional[QoSOverridingOptions] = None,
    raw: bool = False

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/action/client.py
# Line: 169

def __init__(
    self,
    node: 'Node',
    action_type: Type[Action],
    action_name: str,
    *,
    callback_group: 'Optional[CallbackGroup]' = None,
    goal_service_qos_profile: QoSProfile = qos_profile_services_default,
    result_service_qos_profile: QoSProfile = qos_profile_services_default,
    cancel_service_qos_profile: QoSProfile = qos_profile_services_default,
    feedback_sub_qos_profile: QoSProfile = QoSProfile(depth=10),
    status_sub_qos_profile: QoSProfile = qos_profile_action_status_default

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/action/server.py
# Line: 231

def __init__(
    self,
    node: 'Node',
    action_type: Type[Action],
    action_name: str,
    execute_callback: Callable[[ServerGoalHandle[GoalT, ResultT, FeedbackT]], ResultT],
    *,
    callback_group: 'Optional[CallbackGroup]' = None,
    goal_callback: Callable[[CancelGoal.Request], GoalResponse] = default_goal_callback,
    handle_accepted_callback: Callable[[ServerGoalHandle[GoalT,
                                                         ResultT,
                                                         FeedbackT]],
                                       None] = default_handle_accepted_callback,
    cancel_callback: Callable[[CancelGoal.Request], CancelResponse] = default_cancel_callback,
    goal_service_qos_profile: QoSProfile = qos_profile_services_default,
    result_service_qos_profile: QoSProfile = qos_profile_services_default,
    cancel_service_qos_profile: QoSProfile = qos_profile_services_default,
    feedback_pub_qos_profile: QoSProfile = QoSProfile(depth=10),
    status_pub_qos_profile: QoSProfile = qos_profile_action_status_default,
    result_timeout: int = 10

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/timer.py
# Line: 68

def __init__(
    self,
    callback: Union[Callable[[], None], Callable[[TimerInfo], None], None],
    callback_group: Optional[CallbackGroup],
    timer_period_ns: int,
    clock: Clock,
    *,
    context: Optional[Context] = None,
    autostart: bool = True

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/node.py
# Line: 135

def __init__(
    self,
    node_name: str,
    *,
    context: Optional[Context] = None,
    cli_args: Optional[List[str]] = None,
    namespace: Optional[str] = None,
    use_global_arguments: bool = True,
    enable_rosout: bool = True,
    rosout_qos_profile: Union[QoSProfile, int] = qos_profile_rosout_default,
    start_parameter_services: bool = True,
    parameter_overrides: Optional[List[Parameter[Any]]] = None,
    allow_undeclared_parameters: bool = False,
    automatically_declare_parameters_from_overrides: bool = False,
    enable_logger_service: bool = False

# ==================================================
# Line: 1572

def create_publisher(
    self,
    msg_type: Type[MsgT],
    topic: str,
    qos_profile: Union[QoSProfile, int],
    *,
    callback_group: Optional[CallbackGroup] = None,
    event_callbacks: Optional[PublisherEventCallbacks] = None,
    qos_overriding_options: Optional[QoSOverridingOptions] = None,
    publisher_class: Type[Publisher[MsgT]] = Publisher,

# ==================================================
# Line: 1646

def create_subscription(
    self,
    msg_type: Type[MsgT],
    topic: str,
    callback: Union[Callable[[MsgT], None], Callable[[MsgT, MessageInfo], None]],
    qos_profile: Union[QoSProfile, int],
    *,
    callback_group: Optional[CallbackGroup] = None,
    event_callbacks: Optional[SubscriptionEventCallbacks] = None,
    qos_overriding_options: Optional[QoSOverridingOptions] = None,
    raw: bool = False

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/event_handler.py
# Line: 188

def __init__(
    self,
    *,
    deadline: Optional[Callable[[QoSRequestedDeadlineMissedInfo], None]] = None,
    incompatible_qos: Optional[Callable[[QoSRequestedIncompatibleQoSInfo], None]] = None,
    liveliness: Optional[Callable[[QoSLivelinessChangedInfo], None]] = None,
    message_lost: Optional[Callable[[QoSMessageLostInfo], None]] = None,
    incompatible_type: Optional[Callable[[IncompatibleTypeInfo], None]] = None,
    matched: Optional[Callable[[QoSSubscriptionMatchedInfo], None]] = None,
    use_default_callbacks: bool = True,

# ==================================================
# Line: 309

def __init__(
    self,
    *,
    deadline: Optional[Callable[[QoSOfferedDeadlineMissedInfo], None]] = None,
    liveliness: Optional[Callable[[QoSLivelinessLostInfo], None]] = None,
    incompatible_qos: Optional[Callable[[QoSRequestedIncompatibleQoSInfo], None]] = None,
    incompatible_type: Optional[Callable[[IncompatibleTypeInfo], None]] = None,
    matched: Optional[Callable[[QoSPublisherMatchedInfo], None]] = None,
    use_default_callbacks: bool = True,

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/waitable.py
# Line: 38

def __init__(
    self, num_subs: int = 0, num_gcs: int = 0, num_timers: int = 0,
    num_clients: int = 0, num_services: int = 0, num_events: int = 0

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/publisher.py
# Line: 31

def __init__(
    self,
    publisher_impl: '_rclpy.Publisher[MsgT]',
    msg_type: Type[MsgT],
    topic: str,
    qos_profile: QoSProfile,
    event_callbacks: PublisherEventCallbacks,
    callback_group: CallbackGroup,

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/topic_endpoint_info.py
# Line: 48

def __init__(
    self,
    node_name: str = '',
    node_namespace: str = '',
    topic_type: str = '',
    topic_type_hash: Union[TypeHash, TypeHashDictionary] = TypeHash(),
    endpoint_type: Union[TopicEndpointTypeEnum, int] = TopicEndpointTypeEnum.INVALID,
    endpoint_gid: List[int] = [],
    qos_profile: Union[QoSProfile, '_rclpy._rmw_qos_profile_dict'] =
        QoSPresetProfiles.UNKNOWN.value

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/parameter_event_handler.py
# Line: 183

def __init__(
    self,
    node: Node,
    qos_profile: QoSProfile = qos_profile_parameter_events,
    callback_group: Optional[CallbackGroup] = None,
    event_callbacks: Optional[SubscriptionEventCallbacks] = None,
    qos_overriding_options: Optional[QoSOverridingOptions] = None,
    raw: bool = False,

# ==================================================
# File: /root/ecooptimizer/rclpy/rclpy/rclpy/subscription.py
# Line: 46

def __init__(
     self,
     subscription_impl: '_rclpy.Subscription[MsgT]',
     msg_type: Type[MsgT],
     topic: str,
     callback: Union[Callable[[MsgT], None], Callable[[MsgT, MessageInfo], None]],
     callback_group: CallbackGroup,
     qos_profile: QoSProfile,
     raw: bool,
     event_callbacks: SubscriptionEventCallbacks,

# ==================================================
