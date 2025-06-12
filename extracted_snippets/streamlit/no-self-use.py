# no-self-use snippets for streamlit

# File: /root/ecooptimizer/streamlit/e2e_playwright/st_write_objects.py
# Line: 73

def _repr_html_(self) -> str:
    return "This is an <b>HTML tag</b>!"



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/external/langchain/streamlit_callback_handler.py
# Line: 101

def get_initial_label(self) -> str:
    """Return the markdown label for a new LLMThought that doesn't have
    an associated tool yet.
    """
    return "Thinking..."


# ==================================================
# Line: 107

def get_tool_label(self, tool: ToolRecord, is_complete: bool) -> str:
    """Return the label for an LLMThought that has an associated
    tool.

    Parameters
    ----------
    tool
        The tool's ToolRecord

    is_complete
        True if the thought is complete; False if the thought
        is still receiving input.

    Returns
    -------
    The markdown label for the thought's container.

    """
    input_str = tool.input_str
    name = tool.name
    if name == "_Exception":
        name = "Parsing error"
    input_str_len = min(MAX_TOOL_INPUT_STR_LENGTH, len(input_str))
    input_str = input_str[:input_str_len]
    if len(tool.input_str) > input_str_len:
        input_str = input_str + "..."
    input_str = input_str.replace("\n", " ")
    return f"**{name}:** {input_str}"


# ==================================================
# Line: 136

def get_final_agent_thought_label(self) -> str:
    """Return the markdown label for the agent's final thought -
    the "Now I have the answer" thought, that doesn't involve
    a tool.
    """
    return "**Complete!**"



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/vega_charts.py
# Line: 248

def serialize(self, selection_state: VegaLiteState) -> str:
    return json.dumps(selection_state, default=str)



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/audio_input.py
# Line: 60

def serialize(
    self,
    audio_file: SomeUploadedAudioFile,

# ==================================================
# Line: 77

def deserialize(
    self, ui_value: FileUploaderStateProto | None

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/camera_input.py
# Line: 60

def serialize(
    self,
    snapshot: SomeUploadedSnapshotFile,

# ==================================================
# Line: 77

def deserialize(
    self, ui_value: FileUploaderStateProto | None

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/color_picker.py
# Line: 58

def serialize(self, v: str) -> str:
    return str(v)


# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/checkbox.py
# Line: 56

def serialize(self, v: bool) -> bool:
    return bool(v)


# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/chat.py
# Line: 221

def serialize(self, v: str | None) -> ChatInputValueProto:
    return ChatInputValueProto(data=v)



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/time_widgets.py
# Line: 278

def serialize(self, v: datetime | time | None) -> str | None:
    if v is None:
        return None
    if isinstance(v, datetime):
        v = v.time()
    return time.strftime(v, "%H:%M")



# ==================================================
# Line: 306

def serialize(self, v: DateWidgetReturn) -> list[str]:
    if v is None:
        return []

    to_serialize = list(v) if isinstance(v, Sequence) else [v]
    return [date.strftime(v, "%Y/%m/%d") for v in to_serialize]



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/button.py
# Occurrences: Lines 80-83 (2 instances)

def serialize(self, v: bool) -> bool:
    return bool(v)


# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/data_editor.py
# Line: 140

def deserialize(self, ui_value: str | None) -> EditingState:
    data_editor_state: EditingState = (
        {
            "edited_rows": {},
            "added_rows": [],
            "deleted_rows": [],
        }
        if ui_value is None
        else json.loads(ui_value)
    )

    # Make sure that all editing state keys are present:
    if "edited_rows" not in data_editor_state:
        data_editor_state["edited_rows"] = {}

    if "deleted_rows" not in data_editor_state:
        data_editor_state["deleted_rows"] = []

    if "added_rows" not in data_editor_state:
        data_editor_state["added_rows"] = []

    # Convert the keys (numerical row positions) to integers.
    # The keys are strings because they are serialized to JSON.
    data_editor_state["edited_rows"] = {
        int(k): v for k, v in data_editor_state["edited_rows"].items()
    }
    return data_editor_state


# ==================================================
# Line: 168

def serialize(self, editing_state: EditingState) -> str:
    return json.dumps(editing_state, default=str)



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/number_input.py
# Line: 75

def serialize(self, v: Number | None) -> Number | None:
    return v


# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/file_uploader.py
# Line: 128

def serialize(self, files: SomeUploadedFiles) -> FileUploaderStateProto:
    state_proto = FileUploaderStateProto()

    if not files:
        return state_proto
    if not isinstance(files, list):
        files = [files]

    for f in files:
        if isinstance(f, DeletedFile):
            continue
        file_info: UploadedFileInfoProto = state_proto.uploaded_file_info.add()
        file_info.file_id = f.file_id
        file_info.name = f.name
        file_info.size = f.size
        file_info.file_urls.CopyFrom(f._file_urls)

    return state_proto



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/text_widgets.py
# Line: 65

def serialize(self, v: str | None) -> str | None:
    return v



# ==================================================
# Line: 76

def serialize(self, v: str | None) -> str | None:
    return v



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/plotly_chart.py
# Line: 217

def deserialize(self, ui_value: str | None) -> PlotlyState:
    empty_selection_state: PlotlyState = {
        "selection": {
            "points": [],
            "point_indices": [],
            "box": [],
            "lasso": [],
        },
    }

    selection_state = (
        empty_selection_state
        if ui_value is None
        else cast("PlotlyState", AttributeDictionary(json.loads(ui_value)))
    )

    if "selection" not in selection_state:
        selection_state = empty_selection_state  # type: ignore[unreachable]

    return cast("PlotlyState", AttributeDictionary(selection_state))


# ==================================================
# Line: 238

def serialize(self, selection_state: PlotlyState) -> str:
    return json.dumps(selection_state, default=str)



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/arrow.py
# Line: 163

def deserialize(self, ui_value: str | None) -> DataframeState:
    empty_selection_state: DataframeState = {
        "selection": {
            "rows": [],
            "columns": [],
        },
    }
    selection_state: DataframeState = (
        empty_selection_state if ui_value is None else json.loads(ui_value)
    )

    if "selection" not in selection_state:
        selection_state = empty_selection_state

    return cast("DataframeState", AttributeDictionary(selection_state))


# ==================================================
# Line: 179

def serialize(self, editing_state: DataframeState) -> str:
    return json.dumps(editing_state, default=str)



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/deck_gl_json_chart.py
# Line: 236

def deserialize(self, ui_value: str | None) -> PydeckState:
    empty_selection_state: PydeckState = {
        "selection": {
            "indices": {},
            "objects": {},
        }
    }

    selection_state = (
        empty_selection_state if ui_value is None else json.loads(ui_value)
    )

    # We have seen some situations where the ui_value was just an empty
    # dict, so we want to ensure that it always returns the empty state in
    # case this happens.
    if "selection" not in selection_state:
        selection_state = empty_selection_state

    return cast("PydeckState", AttributeDictionary(selection_state))


# ==================================================
# Line: 256

def serialize(self, selection_state: PydeckState) -> str:
    return json.dumps(selection_state, default=str)



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/secrets.py
# Line: 250

def _parse_toml_file(self, path: str) -> tuple[Mapping[str, Any], bool]:
    """Parse a TOML file and return the secrets as a dictionary."""
    secrets = {}
    found_secrets_file = False

    try:
        with open(path, encoding="utf-8") as f:
            secrets_file_str = f.read()

        found_secrets_file = True
    except FileNotFoundError:
        # the default config for secrets contains two paths. It's likely one of will not have secrets file.
        return {}, False

    try:
        import toml

        secrets.update(toml.loads(secrets_file_str))
    except (TypeError, toml.TomlDecodeError) as ex:
        msg = (
            secret_error_messages_singleton.get_error_parsing_file_at_path_message(
                path, ex
            )
        )
        raise StreamlitSecretNotFoundError(msg) from ex

    return secrets, found_secrets_file


# ==================================================
# Line: 278

def _parse_directory(self, path: str) -> tuple[Mapping[str, Any], bool]:
    """Parse a directory for secrets. Directory style can be used to support Kubernetes secrets that are
    mounted to folders.

    Example structure:
    - top_level_secret_folder
        - user_pass_secret (folder)
            - username (file), content: myuser
            - password (file), content: mypassword
        - my_plain_secret (folder)
            - regular_secret (file), content: mysecret

    See: https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#create-a-pod-that-has-access-to-the-secret-data-through-a-volume
    And: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/additional-considerations-services-jobs#passing-secrets-in-local-container-files
    """
    secrets: dict[str, Any] = {}
    found_secrets_file = False

    for dirname in os.listdir(path):
        sub_folder_path = os.path.join(path, dirname)
        if not os.path.isdir(sub_folder_path):
            error_msg = secret_error_messages_singleton.get_subfolder_path_is_not_a_folder_message(
                sub_folder_path
            )
            raise StreamlitSecretNotFoundError(error_msg)
        sub_secrets = {}

        for filename in os.listdir(sub_folder_path):
            file_path = os.path.join(sub_folder_path, filename)

            # ignore folders
            if os.path.isdir(file_path):
                continue

            with open(file_path) as f:
                sub_secrets[filename] = f.read().strip()
                found_secrets_file = True

        if len(sub_secrets) == 1:
            # if there's just one file, collapse it so it's directly under `dirname`
            secrets[dirname] = sub_secrets[next(iter(sub_secrets.keys()))]
        else:
            secrets[dirname] = sub_secrets

    return secrets, found_secrets_file


# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/caching/cache_resource_api.py
# Line: 248

def _decorator(
    self,
    func: F | None,
    *,
    ttl: float | timedelta | str | None,
    max_entries: int | None,
    show_spinner: bool | str,
    validate: ValidateFunc | None,
    experimental_allow_widgets: bool,
    hash_funcs: HashFuncsDict | None = None,

# ==================================================
# Line: 443

def clear(self) -> None:
    """Clear all cache_resource caches."""
    _resource_caches.clear_all()



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/caching/cache_data_api.py
# Line: 285

def create_cache_storage_context(
    self,
    function_key: str,
    function_name: str,
    persist: CachePersistType,
    ttl_seconds: float | None,
    max_entries: int | None,

# ==================================================
# Line: 301

def get_storage_manager(self) -> CacheStorageManager:
    if runtime.exists():
        return runtime.get_instance().cache_storage_manager
    # When running in "raw mode", we can't access the CacheStorageManager,
    # so we're falling back to InMemoryCache.
    _LOGGER.warning("No runtime found, using MemoryCacheStorageManager")
    return MemoryCacheStorageManager()



# ==================================================
# Line: 382

def _decorator(
    self,
    func: F | None = None,
    *,
    ttl: float | timedelta | str | None,
    max_entries: int | None,
    show_spinner: bool | str,
    persist: CachePersistType | bool,
    experimental_allow_widgets: bool,
    hash_funcs: HashFuncsDict | None = None,

# ==================================================
# Line: 600

def clear(self) -> None:
    """Clear all in-memory and on-disk data caches."""
    _data_caches.clear_all()



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/caching/storage/dummy_cache_storage.py
# Line: 28

def create(self, context: CacheStorageContext) -> CacheStorage:
    """Creates a new cache storage instance wrapped with in-memory cache layer."""
    persist_storage = DummyCacheStorage()
    return InMemoryCacheStorageWrapper(
        persist_storage=persist_storage, context=context
    )


# ==================================================
# Line: 43

def get(self, key: str) -> bytes:  # noqa: ARG002
    """
    Dummy gets the value for a given key,
    always raises an CacheStorageKeyNotFoundError.
    """
    raise CacheStorageKeyNotFoundError("Key not found in dummy cache")


# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/runtime_util.py
# Line: 38

def _get_message(self, failed_msg_str: Any) -> str:
    # This needs to have zero indentation otherwise the markdown will render incorrectly.
    return (
        f"""

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/state/query_params_proxy.py
# Line: 113

def get_all(self, key: str) -> list[str]:
    """
    Get a list of all query parameter values associated to a given key.

    When a key is repeated as a query parameter within the URL, this method
    allows all values to be obtained. In contrast, dict-like methods only
    retrieve the last value when a key is repeated in the URL.

    Parameters
    ----------
    key: str
        The label of the query parameter in the URL.

    Returns
    -------
    List[str]
        A list of values associated to the given key. May return zero, one,
        or multiple values.
    """
    with get_session_state().query_params() as qp:
        return qp.get_all(key)


# ==================================================
# Line: 148

def to_dict(self) -> dict[str, str]:
    """
    Get all query parameters as a dictionary.

    This method primarily exists for internal use and is not needed for
    most cases. ``st.query_params`` returns an object that inherits from
    ``dict`` by default.

    When a key is repeated as a query parameter within the URL, this method
    will return only the last value of each unique key.

    Returns
    -------
    Dict[str,str]
        A dictionary of the current query parameters in the app's URL.
    """
    with get_session_state().query_params() as qp:
        return qp.to_dict()


# ==================================================
# Line: 176

def from_dict(
    self,
    params: SupportsKeysAndGetItem[str, str | Iterable[str]]
    | Iterable[tuple[str, str | Iterable[str]]],

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/state/session_state_proxy.py
# Line: 144

def to_dict(self) -> dict[str, Any]:
    """Return a dict containing all session_state and keyed widget values."""
    return get_session_state().filtered_state



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/state/query_params.py
# Line: 195

def _ensure_single_query_api_used(self) -> None:
    ctx = get_script_run_ctx()
    if ctx is None:
        return
    ctx.mark_production_query_params_used()



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/scriptrunner/script_runner.py
# Line: 754

def _new_module(self, name: str) -> types.ModuleType:
    """Create a new module with the given name."""
    return types.ModuleType(name)



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/runtime.py
# Line: 679

def _send_message(self, session_info: ActiveSessionInfo, msg: ForwardMsg) -> None:
    """Send a message to a client.
    If the client is likely to have already cached the message, we may
    instead send a "reference" message that contains only the hash of the
    message.

    Parameters
    ----------
    session_info : ActiveSessionInfo
        The ActiveSessionInfo associated with websocket
    msg : ForwardMsg
        The message to send to the client

    Notes
    -----
    Threading: UNSAFE. Must be called on the eventloop thread.
    """

    # If this was a `script_finished` message, we increment the
    # script_run_count for this session
    if msg.WhichOneof("type") == "script_finished" and (
        msg.script_finished == ForwardMsg.FINISHED_SUCCESSFULLY
    ):
        session_info.script_run_count += 1

    # Ship it off!
    session_info.client.write_forward_msg(msg)


# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/memory_media_file_storage.py
# Line: 161

def _read_file(self, filename: str) -> bytes:
    """Read a file into memory. Raise MediaFileStorageError if we can't."""
    try:
        with open(filename, "rb") as f:
            return f.read()
    except Exception as ex:
        raise MediaFileStorageError(f"Error opening '{filename}'") from ex


# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/app_session.py
# Line: 710

def _create_file_change_message(self) -> ForwardMsg:
    """Create and return a 'script_changed_on_disk' ForwardMsg."""
    msg = ForwardMsg()
    msg.session_event.script_changed_on_disk = True
    return msg


# ==================================================
# Line: 769

def _create_script_finished_message(
    self, status: ForwardMsg.ScriptFinishedStatus.ValueType

# ==================================================
# Line: 777

def _create_exception_message(self, e: BaseException) -> ForwardMsg:
    """Create and return an Exception ForwardMsg."""
    msg = ForwardMsg()
    exception_utils.marshall(msg.delta.new_element.exception, e)
    return msg


# ==================================================
# Line: 892

def _populate_app_pages(
    self, msg: NewSession, pages: dict[PageHash, PageInfo]

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/user_info.py
# Line: 510

def to_dict(self) -> UserInfo:
    """
    Get user info as a dictionary.

    This method primarily exists for internal use and is not needed for
    most cases. ``st.user`` returns an object that inherits from
    ``dict`` by default.

    Returns
    -------
    Dict[str,str]
        A dictionary of the current user's information.
    """
    return _get_user_info()



# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/delta_generator.py
# Line: 401

def _count_num_of_parent_columns(
    self, ancestor_block_types: AncestorBlockTypes

# ==================================================
