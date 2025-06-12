# too-many-arguments snippets for streamlit

# File: /root/ecooptimizer/streamlit/e2e_playwright/st_pydeck_chart_select_test.py
# Line: 95

def _click_point_and_verify_selection(
    app: Page,
    click_handling_div: Locator,
    coords: Position,
    expected_selection: str,
    markdown_prefix: str = "managed_map selection:",
    markdown_prefix_session_state: str | None = "session_state.managed_map:",
    wait_delay: int = STANDARD_WAIT_DELAY,

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/conftest.py
# Line: 604

def __call__(
    self,
    element: ElementHandle | Locator | Page,
    *,
    image_threshold: float = 0.002,
    pixel_threshold: float = 0.05,
    name: str | None = None,
    fail_fast: bool = False,
    style: str | None = None,

# ==================================================
# Line: 728

def compare(
    element: ElementHandle | Locator | Page,
    *,
    image_threshold: float = 0.002,
    pixel_threshold: float = 0.05,
    name: str | None = None,
    fail_fast: bool = False,
    file_type: Literal["png", "jpg"] = "png",
    style: str | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/shared/dataframe_utils.py
# Line: 173

def click_on_cell(
    dataframe_element: Locator,
    row_pos: int,
    col_pos: int,
    column_width: Literal["small", "medium", "large"] = "small",
    has_row_marker_col: bool = False,
    double_click: bool = False,
    wait_after_ms: int = 200,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/vendor/pympler/asizeof.py
# Line: 1092

def reset(
    self,
    base=0,
    item=0,
    leng=None,
    refs=None,
    both=True,
    kind=None,
    type=None,
    vari=_Not_vari,
    xtyp=False,
    **extra,

# ==================================================
# Line: 1173

def _typedef_both(
    t,
    base=0,
    item=0,
    leng=None,
    refs=None,
    kind=_kind_static,
    heap=False,
    vari=_Not_vari,

# ==================================================
# Line: 2366

def reset(
    self,
    above=1024,
    align=8,
    clip=80,
    code=False,  # PYCHOK too many args
    cutoff=10,
    derive=False,
    detail=0,
    frames=False,
    ignored=True,
    infer=False,
    limit=100,
    stats=0,
    stream=None,
    **extra,

# ==================================================
# Line: 2441

def set(
    self,
    above=None,
    align=None,
    code=None,
    cutoff=None,
    frames=None,
    detail=None,
    limit=None,
    stats=None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/config_option.py
# Line: 98

def __init__(
    self,
    key: str,
    description: str | None = None,
    default_val: Any | None = None,
    visibility: str = "visible",
    scriptable: bool = False,
    deprecated: bool = False,
    deprecation_text: str | None = None,
    expiration_date: str | None = None,
    replaced_by: str | None = None,
    type_: type = str,
    sensitive: bool = False,
    multiple: bool = False,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/iframe.py
# Line: 193

def marshall(
    proto: IFrameProto,
    src: str | None = None,
    srcdoc: str | None = None,
    width: int | None = None,
    height: int | None = None,
    scrolling: bool = False,
    tab_index: int | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/image.py
# Line: 48

def image(
    self,
    image: ImageOrImageList,
    # TODO: Narrow type of caption, dependent on type of image,
    #  by way of overload
    caption: str | list[str] | None = None,
    width: int | None = None,
    use_column_width: UseColumnWith = None,
    clamp: bool = False,
    channels: Channels = "RGB",
    output_format: ImageFormatOrAuto = "auto",
    *,
    use_container_width: bool = False,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/form.py
# Line: 71

def form(
    self,
    key: str,
    clear_on_submit: bool = False,
    *,
    enter_to_submit: bool = True,
    border: bool = True,
    width: Width = "stretch",
    height: Height = "content",

# ==================================================
# Line: 206

def form_submit_button(
    self,
    label: str = "Submit",
    help: str | None = None,
    on_click: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    type: Literal["primary", "secondary", "tertiary"] = "secondary",
    icon: str | None = None,
    disabled: bool = False,
    use_container_width: bool = False,

# ==================================================
# Line: 334

def _form_submit_button(
    self,
    label: str = "Submit",
    help: str | None = None,
    on_click: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    type: Literal["primary", "secondary", "tertiary"] = "secondary",
    icon: str | None = None,
    disabled: bool = False,
    use_container_width: bool = False,
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/map.py
# Line: 79

def map(
    self,
    data: Data = None,
    *,
    latitude: str | None = None,
    longitude: str | None = None,
    color: None | str | Color = None,
    size: None | str | float = None,
    zoom: int | None = None,
    use_container_width: bool = True,
    width: int | None = None,
    height: int | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/code.py
# Line: 37

def code(
    self,
    body: SupportsStr,
    language: str | None = "python",
    *,
    line_numbers: bool = False,
    wrap_lines: bool = False,
    height: Height = "content",
    width: WidthWithoutContent = "stretch",

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/vega_charts.py
# Line: 586

def line_chart(
    self,
    data: Data = None,
    *,
    x: str | None = None,
    y: str | Sequence[str] | None = None,
    x_label: str | None = None,
    y_label: str | None = None,
    color: str | Color | list[Color] | None = None,
    width: int | None = None,
    height: int | None = None,
    use_container_width: bool = True,

# ==================================================
# Line: 783

def area_chart(
    self,
    data: Data = None,
    *,
    x: str | None = None,
    y: str | Sequence[str] | None = None,
    x_label: str | None = None,
    y_label: str | None = None,
    color: str | Color | list[Color] | None = None,
    stack: bool | ChartStackType | None = None,
    width: int | None = None,
    height: int | None = None,
    use_container_width: bool = True,

# ==================================================
# Line: 1025

def bar_chart(
    self,
    data: Data = None,
    *,
    x: str | None = None,
    y: str | Sequence[str] | None = None,
    x_label: str | None = None,
    y_label: str | None = None,
    color: str | Color | list[Color] | None = None,
    horizontal: bool = False,
    stack: bool | ChartStackType | None = None,
    width: int | None = None,
    height: int | None = None,
    use_container_width: bool = True,

# ==================================================
# Line: 1293

def scatter_chart(
    self,
    data: Data = None,
    *,
    x: str | None = None,
    y: str | Sequence[str] | None = None,
    x_label: str | None = None,
    y_label: str | None = None,
    color: str | Color | list[Color] | None = None,
    size: str | float | int | None = None,
    width: int | None = None,
    height: int | None = None,
    use_container_width: bool = True,

# ==================================================
# Line: 1505

def altair_chart(
    self,
    altair_chart: AltairChart,
    *,
    use_container_width: bool | None = None,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["ignore"] = "ignore",
    selection_mode: str | Iterable[str] | None = None,

# ==================================================
# Line: 1518

def altair_chart(
    self,
    altair_chart: AltairChart,
    *,
    use_container_width: bool | None = None,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["rerun"] | WidgetCallback,
    selection_mode: str | Iterable[str] | None = None,

# ==================================================
# Line: 1530

def altair_chart(
    self,
    altair_chart: AltairChart,
    *,
    use_container_width: bool | None = None,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
    selection_mode: str | Iterable[str] | None = None,

# ==================================================
# Line: 1663

def vega_lite_chart(
    self,
    data: Data = None,
    spec: VegaLiteSpec | None = None,
    *,
    use_container_width: bool | None = None,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["ignore"] = "ignore",
    selection_mode: str | Iterable[str] | None = None,
    **kwargs: Any,

# ==================================================
# Line: 1678

def vega_lite_chart(
    self,
    data: Data = None,
    spec: VegaLiteSpec | None = None,
    *,
    use_container_width: bool | None = None,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["rerun"] | WidgetCallback,
    selection_mode: str | Iterable[str] | None = None,
    **kwargs: Any,

# ==================================================
# Line: 1692

def vega_lite_chart(
    self,
    data: Data = None,
    spec: VegaLiteSpec | None = None,
    *,
    use_container_width: bool | None = None,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
    selection_mode: str | Iterable[str] | None = None,
    **kwargs: Any,

# ==================================================
# Line: 1842

def _altair_chart(
    self,
    altair_chart: AltairChart,
    use_container_width: bool | None = None,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
    selection_mode: str | Iterable[str] | None = None,
    add_rows_metadata: AddRowsMetadata | None = None,

# ==================================================
# Line: 1877

def _vega_lite_chart(
    self,
    data: Data = None,
    spec: VegaLiteSpec | None = None,
    use_container_width: bool | None = None,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
    selection_mode: str | Iterable[str] | None = None,
    add_rows_metadata: AddRowsMetadata | None = None,
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/audio_input.py
# Line: 89

def audio_input(
    self,
    label: str,
    *,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 209

def _audio_input(
    self,
    label: str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/selectbox.py
# Line: 141

def selectbox(
    self,
    label: str,
    options: Sequence[Never],  # Type for empty or Never-inferred options
    index: int = 0,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: Literal[False] = False,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 161

def selectbox(
    self,
    label: str,
    options: OptionSequence[T],
    index: int = 0,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: Literal[False] = False,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 181

def selectbox(
    self,
    label: str,
    options: OptionSequence[T],
    index: int = 0,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: Literal[True] = True,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 201

def selectbox(
    self,
    label: str,
    options: OptionSequence[T],
    index: None,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: Literal[False] = False,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 221

def selectbox(
    self,
    label: str,
    options: OptionSequence[T],
    index: None,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: Literal[True] = True,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 241

def selectbox(
    self,
    label: str,
    options: OptionSequence[T],
    index: int | None = 0,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: bool = False,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 261

def selectbox(
    self,
    label: str,
    options: OptionSequence[T],
    index: int | None = 0,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: bool = False,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 466

def _selectbox(
    self,
    label: str,
    options: OptionSequence[T],
    index: int | None = 0,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: bool = False,
    width: WidthWithoutContent = "stretch",
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/camera_input.py
# Line: 89

def camera_input(
    self,
    label: str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 203

def _camera_input(
    self,
    label: str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/slider.py
# Line: 232

def slider(
    self,
    label: str,
    min_value: None = None,
    max_value: None = None,
    value: None = None,
    step: int | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 254

def slider(
    self,
    label: str,
    min_value: SliderNumericT | None = None,
    max_value: SliderNumericT | None = None,
    value: SliderNumericT | None = None,
    step: StepNumericT[SliderNumericT] | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 276

def slider(
    self,
    label: str,
    min_value: SliderNumericT | None = None,
    max_value: SliderNumericT | None = None,
    *,
    value: SliderNumericSpanT[SliderNumericT],
    step: StepNumericT[SliderNumericT] | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 298

def slider(
    self,
    label: str,
    min_value: SliderNumericT,
    max_value: SliderNumericT,
    value: SliderNumericSpanT[SliderNumericT],
    step: StepNumericT[SliderNumericT] | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 320

def slider(
    self,
    label: str,
    min_value: SliderDatelikeT,
    max_value: SliderDatelikeT | None = None,
    value: SliderDatelikeT | None = None,
    step: StepDatelikeT | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 342

def slider(
    self,
    label: str,
    min_value: None = None,
    *,
    max_value: SliderDatelikeT,
    value: SliderDatelikeT | None = None,
    step: StepDatelikeT | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 363

def slider(
    self,
    label: str,
    min_value: None = None,
    max_value: None = None,
    *,
    value: SliderDatelikeT,
    step: StepDatelikeT | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 385

def slider(
    self,
    label: str,
    min_value: SliderDatelikeT | None = None,
    max_value: SliderDatelikeT | None = None,
    *,
    value: list[SliderDatelikeT]
    | tuple[SliderDatelikeT]
    | tuple[SliderDatelikeT, SliderDatelikeT],
    step: StepDatelikeT | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 409

def slider(
    self,
    label: str,
    min_value: SliderDatelikeT,
    max_value: SliderDatelikeT,
    value: SliderDatelikeSpanT[SliderDatelikeT],
    /,
    step: StepDatelikeT | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 431

def slider(
    self,
    label: str,
    min_value: SliderScalar | None = None,
    max_value: SliderScalar | None = None,
    value: SliderValue | None = None,
    step: SliderStep | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 643

def _slider(
    self,
    label: str,
    min_value: Any = None,
    max_value: Any = None,
    value: Any = None,
    step: Any = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/color_picker.py
# Line: 67

def color_picker(
    self,
    label: str,
    value: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: Width = "content",

# ==================================================
# Line: 182

def _color_picker(
    self,
    label: str,
    value: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: Width = "content",
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/button_group.py
# Line: 214

def _build_proto(
    widget_id: str,
    formatted_options: Sequence[ButtonGroupProto.Option],
    default_values: list[int],
    disabled: bool,
    current_form_id: str,
    click_mode: ButtonGroupProto.ClickMode.ValueType,
    selection_visualization: ButtonGroupProto.SelectionVisualization.ValueType = (
        ButtonGroupProto.SelectionVisualization.ONLY_SELECTED
    ),
    style: Literal["borderless", "pills", "segmented_control"] = "pills",
    label: str | None = None,
    label_visibility: LabelVisibility = "visible",
    help: str | None = None,

# ==================================================
# Line: 270

def feedback(
    self,
    options: Literal["thumbs"] = ...,
    *,
    key: Key | None = None,
    disabled: bool = False,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,

# ==================================================
# Line: 281

def feedback(
    self,
    options: Literal["faces", "stars"] = ...,
    *,
    key: Key | None = None,
    disabled: bool = False,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,

# ==================================================
# Line: 292

def feedback(
    self,
    options: Literal["thumbs", "faces", "stars"] = "thumbs",
    *,
    key: Key | None = None,
    disabled: bool = False,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,

# ==================================================
# Line: 415

def pills(
    self,
    label: str,
    options: OptionSequence[V],
    *,
    selection_mode: Literal["single"] = "single",
    default: V | None = None,
    format_func: Callable[[Any], str] | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",

# ==================================================
# Line: 432

def pills(
    self,
    label: str,
    options: OptionSequence[V],
    *,
    selection_mode: Literal["multi"],
    default: Sequence[V] | V | None = None,
    format_func: Callable[[Any], str] | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",

# ==================================================
# Line: 449

def pills(
    self,
    label: str,
    options: OptionSequence[V],
    *,
    selection_mode: Literal["single", "multi"] = "single",
    default: Sequence[V] | V | None = None,
    format_func: Callable[[Any], str] | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",

# ==================================================
# Line: 624

def segmented_control(
    self,
    label: str,
    options: OptionSequence[V],
    *,
    selection_mode: Literal["single"] = "single",
    default: V | None = None,
    format_func: Callable[[Any], str] | None = None,
    key: str | int | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",

# ==================================================
# Line: 641

def segmented_control(
    self,
    label: str,
    options: OptionSequence[V],
    *,
    selection_mode: Literal["multi"],
    default: Sequence[V] | V | None = None,
    format_func: Callable[[Any], str] | None = None,
    key: str | int | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",

# ==================================================
# Line: 659

def segmented_control(
    self,
    label: str,
    options: OptionSequence[V],
    *,
    selection_mode: Literal["single", "multi"] = "single",
    default: Sequence[V] | V | None = None,
    format_func: Callable[[Any], str] | None = None,
    key: str | int | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",

# ==================================================
# Line: 836

def _internal_button_group(
    self,
    options: OptionSequence[V],
    *,
    key: Key | None = None,
    default: Sequence[V] | V | None = None,
    selection_mode: Literal["single", "multi"] = "single",
    disabled: bool = False,
    format_func: Callable[[Any], str] | None = None,
    style: Literal["pills", "segmented_control"] = "segmented_control",
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    label: str | None = None,
    label_visibility: LabelVisibility = "visible",
    help: str | None = None,

# ==================================================
# Line: 912

def _button_group(
    self,
    indexable_options: Sequence[Any],
    *,
    key: Key | None = None,
    default: list[int] | None = None,
    selection_mode: SelectionMode = "single",
    disabled: bool = False,
    style: Literal[
        "borderless", "pills", "segmented_control"
    ] = "segmented_control",
    format_func: Callable[[V], ButtonGroupProto.Option] | None = None,
    deserializer: WidgetDeserializer[T],
    serializer: WidgetSerializer[T],
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    selection_visualization: ButtonGroupProto.SelectionVisualization.ValueType = (
        ButtonGroupProto.SelectionVisualization.ONLY_SELECTED
    ),
    label: str | None = None,
    label_visibility: LabelVisibility = "visible",
    help: str | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/radio.py
# Line: 90

def radio(
    self,
    label: str,
    options: Sequence[Never],
    index: int = 0,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only args:
    disabled: bool = False,
    horizontal: bool = False,
    captions: Sequence[str] | None = None,
    label_visibility: LabelVisibility = "visible",
    width: Width = "content",

# ==================================================
# Line: 110

def radio(
    self,
    label: str,
    options: OptionSequence[T],
    index: int = 0,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only args:
    disabled: bool = False,
    horizontal: bool = False,
    captions: Sequence[str] | None = None,
    label_visibility: LabelVisibility = "visible",
    width: Width = "content",

# ==================================================
# Line: 130

def radio(
    self,
    label: str,
    options: OptionSequence[T],
    index: None,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only args:
    disabled: bool = False,
    horizontal: bool = False,
    captions: Sequence[str] | None = None,
    label_visibility: LabelVisibility = "visible",
    width: Width = "content",

# ==================================================
# Line: 150

def radio(
    self,
    label: str,
    options: OptionSequence[T],
    index: int | None = 0,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only args:
    disabled: bool = False,
    horizontal: bool = False,
    captions: Sequence[str] | None = None,
    label_visibility: LabelVisibility = "visible",
    width: Width = "content",

# ==================================================
# Line: 324

def _radio(
    self,
    label: str,
    options: OptionSequence[T],
    index: int | None = 0,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only args:
    disabled: bool = False,
    horizontal: bool = False,
    label_visibility: LabelVisibility = "visible",
    captions: Sequence[str] | None = None,
    ctx: ScriptRunContext | None,
    width: Width = "content",

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/checkbox.py
# Line: 65

def checkbox(
    self,
    label: str,
    value: bool = False,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: Width = "content",

# ==================================================
# Line: 182

def toggle(
    self,
    label: str,
    value: bool = False,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: Width = "content",

# ==================================================
# Line: 298

def _checkbox(
    self,
    label: str,
    value: bool = False,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    type: CheckboxProto.StyleType.ValueType = CheckboxProto.StyleType.DEFAULT,
    ctx: ScriptRunContext | None = None,
    width: Width = "content",

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/select_slider.py
# Line: 109

def select_slider(
    self,
    label: str,
    options: OptionSequence[T],
    value: tuple[T, T] | list[T],
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 127

def select_slider(
    self,
    label: str,
    options: OptionSequence[T] = (),
    value: T | None = None,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 145

def select_slider(
    self,
    label: str,
    options: OptionSequence[T] = (),
    value: T | Sequence[T] | None = None,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 317

def _select_slider(
    self,
    label: str,
    options: OptionSequence[T] = (),
    value: T | Sequence[T] | None = None,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    ctx: ScriptRunContext | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/chat.py
# Line: 363

def chat_input(
    self,
    placeholder: str = "Your message",
    *,
    key: Key | None = None,
    max_chars: int | None = None,
    accept_file: Literal[False] = False,
    file_type: str | Sequence[str] | None = None,
    disabled: bool = False,
    on_submit: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 379

def chat_input(
    self,
    placeholder: str = "Your message",
    *,
    key: Key | None = None,
    max_chars: int | None = None,
    accept_file: Literal[True, "multiple"],
    file_type: str | Sequence[str] | None = None,
    disabled: bool = False,
    on_submit: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 395

def chat_input(
    self,
    placeholder: str = "Your message",
    *,
    key: Key | None = None,
    max_chars: int | None = None,
    accept_file: bool | Literal["multiple"] = False,
    file_type: str | Sequence[str] | None = None,
    disabled: bool = False,
    on_submit: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/time_widgets.py
# Line: 316

def time_input(
    self,
    label: str,
    value: TimeValue = "now",
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    step: int | timedelta = timedelta(minutes=DEFAULT_STEP_MINUTES),
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 334

def time_input(
    self,
    label: str,
    value: None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    step: int | timedelta = timedelta(minutes=DEFAULT_STEP_MINUTES),
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 352

def time_input(
    self,
    label: str,
    value: TimeValue | None = "now",
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    step: int | timedelta = timedelta(minutes=DEFAULT_STEP_MINUTES),
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 495

def _time_input(
    self,
    label: str,
    value: TimeValue | None = "now",
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    step: int | timedelta = timedelta(minutes=DEFAULT_STEP_MINUTES),
    width: WidthWithoutContent = "stretch",
    ctx: ScriptRunContext | None = None,

# ==================================================
# Line: 590

def date_input(
    self,
    label: str,
    value: date | datetime | str | Literal["today"] = "today",
    min_value: NullableScalarDateValue = None,
    max_value: NullableScalarDateValue = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    format: str = "YYYY/MM/DD",
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 609

def date_input(
    self,
    label: str,
    value: None,
    min_value: NullableScalarDateValue = None,
    max_value: NullableScalarDateValue = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    format: str = "YYYY/MM/DD",
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 628

def date_input(
    self,
    label: str,
    value: tuple[NullableScalarDateValue]
    | tuple[NullableScalarDateValue, NullableScalarDateValue]
    | list[NullableScalarDateValue],
    min_value: NullableScalarDateValue = None,
    max_value: NullableScalarDateValue = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    format: str = "YYYY/MM/DD",
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 649

def date_input(
    self,
    label: str,
    value: DateValue = "today",
    min_value: NullableScalarDateValue = None,
    max_value: NullableScalarDateValue = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    format: str = "YYYY/MM/DD",
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 847

def _date_input(
    self,
    label: str,
    value: DateValue = "today",
    min_value: NullableScalarDateValue = None,
    max_value: NullableScalarDateValue = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    format: str = "YYYY/MM/DD",
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/button.py
# Line: 89

def button(
    self,
    label: str,
    key: Key | None = None,
    help: str | None = None,
    on_click: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    type: Literal["primary", "secondary", "tertiary"] = "secondary",
    icon: str | None = None,
    disabled: bool = False,
    use_container_width: bool = False,

# ==================================================
# Line: 259

def download_button(
    self,
    label: str,
    data: DownloadButtonDataType,
    file_name: str | None = None,
    mime: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_click: WidgetCallback | Literal["rerun", "ignore"] | None = "rerun",
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    type: Literal["primary", "secondary", "tertiary"] = "secondary",
    icon: str | None = None,
    disabled: bool = False,
    use_container_width: bool = False,

# ==================================================
# Line: 546

def link_button(
    self,
    label: str,
    url: str,
    *,
    help: str | None = None,
    type: Literal["primary", "secondary", "tertiary"] = "secondary",
    icon: str | None = None,
    disabled: bool = False,
    use_container_width: bool = False,

# ==================================================
# Line: 663

def page_link(
    self,
    page: str | Path | StreamlitPage,
    *,
    label: str | None = None,
    icon: str | None = None,
    help: str | None = None,
    disabled: bool = False,
    use_container_width: bool | None = None,

# ==================================================
# Line: 782

def _download_button(
    self,
    label: str,
    data: DownloadButtonDataType,
    file_name: str | None = None,
    mime: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_click: WidgetCallback | Literal["rerun", "ignore"] | None = "rerun",
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    type: Literal["primary", "secondary", "tertiary"] = "secondary",
    icon: str | None = None,
    disabled: bool = False,
    use_container_width: bool = False,
    ctx: ScriptRunContext | None = None,

# ==================================================
# Line: 874

def _link_button(
    self,
    label: str,
    url: str,
    help: str | None,
    *,  # keyword-only arguments:
    type: Literal["primary", "secondary", "tertiary"] = "secondary",
    icon: str | None = None,
    disabled: bool = False,
    use_container_width: bool = False,

# ==================================================
# Line: 900

def _page_link(
    self,
    page: str | Path | StreamlitPage,
    *,  # keyword-only arguments:
    label: str | None = None,
    icon: str | None = None,
    help: str | None = None,
    disabled: bool = False,
    use_container_width: bool | None = None,

# ==================================================
# Line: 979

def _button(
    self,
    label: str,
    key: str | None,
    help: str | None,
    is_form_submitter: bool,
    on_click: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    type: Literal["primary", "secondary", "tertiary"] = "secondary",
    icon: str | None = None,
    disabled: bool = False,
    use_container_width: bool = False,
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/data_editor.py
# Line: 577

def data_editor(
    self,
    data: EditableData,
    *,
    width: int | None = None,
    height: int | None = None,
    use_container_width: bool | None = None,
    hide_index: bool | None = None,
    column_order: Iterable[str] | None = None,
    column_config: ColumnConfigMappingInput | None = None,
    num_rows: Literal["fixed", "dynamic"] = "fixed",
    disabled: bool | Iterable[str] = False,
    key: Key | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    row_height: int | None = None,

# ==================================================
# Line: 598

def data_editor(
    self,
    data: Any,
    *,
    width: int | None = None,
    height: int | None = None,
    use_container_width: bool | None = None,
    hide_index: bool | None = None,
    column_order: Iterable[str] | None = None,
    column_config: ColumnConfigMappingInput | None = None,
    num_rows: Literal["fixed", "dynamic"] = "fixed",
    disabled: bool | Iterable[str] = False,
    key: Key | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    row_height: int | None = None,

# ==================================================
# Line: 619

def data_editor(
    self,
    data: DataTypes,
    *,
    width: int | None = None,
    height: int | None = None,
    use_container_width: bool | None = None,
    hide_index: bool | None = None,
    column_order: Iterable[str] | None = None,
    column_config: ColumnConfigMappingInput | None = None,
    num_rows: Literal["fixed", "dynamic"] = "fixed",
    disabled: bool | Iterable[str] = False,
    key: Key | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    row_height: int | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/number_input.py
# Line: 93

def number_input(
    self,
    label: str,
    min_value: int,
    max_value: int | None = None,
    value: IntOrNone | Literal["min"] = "min",
    step: int | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 119

def number_input(
    self,
    label: str,
    min_value: None = None,
    *,
    max_value: int,
    value: IntOrNone | Literal["min"] = "min",
    step: int | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 143

def number_input(
    self,
    label: str,
    min_value: int | None = None,
    max_value: int | None = None,
    *,
    value: int,
    step: int | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 169

def number_input(
    self,
    label: str,
    min_value: None = None,
    max_value: None = None,
    value: IntOrNone | Literal["min"] = "min",
    *,
    step: int,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 195

def number_input(
    self,
    label: str,
    min_value: float | None = None,
    max_value: float | None = None,
    value: FloatOrNone | Literal["min"] = "min",
    step: float | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 217

def number_input(
    self,
    label: str,
    min_value: Number | None = None,
    max_value: Number | None = None,
    value: Number | Literal["min"] | None = "min",
    step: Number | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 413

def _number_input(
    self,
    label: str,
    min_value: Number | None = None,
    max_value: Number | None = None,
    value: Number | Literal["min"] | None = "min",
    step: Number | None = None,
    format: str | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/file_uploader.py
# Line: 162

def file_uploader(
    self,
    label: str,
    type: str | Sequence[str] | None,
    accept_multiple_files: Literal[True],
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 181

def file_uploader(
    self,
    label: str,
    type: str | Sequence[str] | None,
    accept_multiple_files: Literal[False] = False,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 205

def file_uploader(
    self,
    label: str,
    *,
    accept_multiple_files: Literal[True],
    type: str | Sequence[str] | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 224

def file_uploader(
    self,
    label: str,
    *,
    accept_multiple_files: Literal[False] = False,
    type: str | Sequence[str] | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 241

def file_uploader(
    self,
    label: str,
    type: str | Sequence[str] | None = None,
    accept_multiple_files: bool = False,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 416

def _file_uploader(
    self,
    label: str,
    type: str | Sequence[str] | None = None,
    accept_multiple_files: bool = False,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    label_visibility: LabelVisibility = "visible",
    disabled: bool = False,
    ctx: ScriptRunContext | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/multiselect.py
# Line: 156

def multiselect(
    self,
    label: str,
    options: OptionSequence[T],
    default: Any | None = None,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    max_selections: int | None = None,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: Literal[False] = False,

# ==================================================
# Line: 176

def multiselect(
    self,
    label: str,
    options: OptionSequence[T],
    default: Any | None = None,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    max_selections: int | None = None,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: Literal[True] = True,

# ==================================================
# Line: 196

def multiselect(
    self,
    label: str,
    options: OptionSequence[T],
    default: Any | None = None,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    max_selections: int | None = None,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: bool = False,

# ==================================================
# Line: 216

def multiselect(
    self,
    label: str,
    options: OptionSequence[T],
    default: Any | None = None,
    format_func: Callable[[Any], str] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    max_selections: int | None = None,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: Literal[False, True] | bool = False,

# ==================================================
# Line: 403

def _multiselect(
    self,
    label: str,
    options: OptionSequence[T],
    default: Sequence[Any] | Any | None = None,
    format_func: Callable[[Any], Any] = str,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    max_selections: int | None = None,
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    accept_new_options: bool = False,
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/text_widgets.py
# Line: 82

def text_input(
    self,
    label: str,
    value: str = "",
    max_chars: int | None = None,
    key: Key | None = None,
    type: Literal["default", "password"] = "default",
    help: str | None = None,
    autocomplete: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 104

def text_input(
    self,
    label: str,
    value: SupportsStr | None = None,
    max_chars: int | None = None,
    key: Key | None = None,
    type: Literal["default", "password"] = "default",
    help: str | None = None,
    autocomplete: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 126

def text_input(
    self,
    label: str,
    value: str | SupportsStr | None = "",
    max_chars: int | None = None,
    key: Key | None = None,
    type: Literal["default", "password"] = "default",
    help: str | None = None,
    autocomplete: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 285

def _text_input(
    self,
    label: str,
    value: SupportsStr | None = "",
    max_chars: int | None = None,
    key: Key | None = None,
    type: str = "default",
    help: str | None = None,
    autocomplete: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    icon: str | None = None,
    width: WidthWithoutContent = "stretch",
    ctx: ScriptRunContext | None = None,

# ==================================================
# Line: 401

def text_area(
    self,
    label: str,
    value: str = "",
    height: int | None = None,
    max_chars: int | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 421

def text_area(
    self,
    label: str,
    value: SupportsStr | None = None,
    height: int | None = None,
    max_chars: int | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 441

def text_area(
    self,
    label: str,
    value: str | SupportsStr | None = "",
    height: int | None = None,
    max_chars: int | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 587

def _text_area(
    self,
    label: str,
    value: SupportsStr | None = "",
    height: int | None = None,
    max_chars: int | None = None,
    key: Key | None = None,
    help: str | None = None,
    on_change: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    *,  # keyword-only arguments:
    placeholder: str | None = None,
    disabled: bool = False,
    label_visibility: LabelVisibility = "visible",
    width: WidthWithoutContent = "stretch",
    ctx: ScriptRunContext | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/plotly_chart.py
# Line: 272

def plotly_chart(
    self,
    figure_or_data: FigureOrData,
    use_container_width: bool = True,
    *,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["ignore"],  # No default value here to make it work with mypy
    selection_mode: SelectionMode | Iterable[SelectionMode] = (
        "points",
        "box",
        "lasso",
    ),
    **kwargs: Any,

# ==================================================
# Line: 289

def plotly_chart(
    self,
    figure_or_data: FigureOrData,
    use_container_width: bool = True,
    *,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["rerun"] | WidgetCallback = "rerun",
    selection_mode: SelectionMode | Iterable[SelectionMode] = (
        "points",
        "box",
        "lasso",
    ),
    **kwargs: Any,

# ==================================================
# Line: 306

def plotly_chart(
    self,
    figure_or_data: FigureOrData,
    use_container_width: bool = True,
    *,
    theme: Literal["streamlit"] | None = "streamlit",
    key: Key | None = None,
    on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
    selection_mode: SelectionMode | Iterable[SelectionMode] = (
        "points",
        "box",
        "lasso",
    ),
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/arrow.py
# Line: 225

def dataframe(
    self,
    data: Data = None,
    width: int | None = None,
    height: int | None = None,
    *,
    use_container_width: bool | None = None,
    hide_index: bool | None = None,
    column_order: Iterable[str] | None = None,
    column_config: ColumnConfigMappingInput | None = None,
    key: Key | None = None,
    on_select: Literal["ignore"] = "ignore",
    selection_mode: SelectionMode | Iterable[SelectionMode] = "multi-row",
    row_height: int | None = None,

# ==================================================
# Line: 242

def dataframe(
    self,
    data: Data = None,
    width: int | None = None,
    height: int | None = None,
    *,
    use_container_width: bool | None = None,
    hide_index: bool | None = None,
    column_order: Iterable[str] | None = None,
    column_config: ColumnConfigMappingInput | None = None,
    key: Key | None = None,
    on_select: Literal["rerun"] | WidgetCallback,
    selection_mode: SelectionMode | Iterable[SelectionMode] = "multi-row",
    row_height: int | None = None,

# ==================================================
# Line: 259

def dataframe(
    self,
    data: Data = None,
    width: int | None = None,
    height: int | None = None,
    *,
    use_container_width: bool | None = None,
    hide_index: bool | None = None,
    column_order: Iterable[str] | None = None,
    column_config: ColumnConfigMappingInput | None = None,
    key: Key | None = None,
    on_select: Literal["ignore", "rerun"] | WidgetCallback = "ignore",
    selection_mode: SelectionMode | Iterable[SelectionMode] = "multi-row",
    row_height: int | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/deck_gl_json_chart.py
# Line: 262

def pydeck_chart(
    self,
    pydeck_obj: Deck | None = None,
    *,
    use_container_width: bool = True,
    width: int | None = None,
    height: int | None = None,
    selection_mode: Literal[
        "single-object"
    ],  # Selection mode will only be activated by on_select param; default value here to make it work with mypy
    # No default value here to make it work with mypy
    on_select: Literal["ignore"],
    key: Key | None = None,

# ==================================================
# Line: 278

def pydeck_chart(
    self,
    pydeck_obj: Deck | None = None,
    *,
    use_container_width: bool = True,
    width: int | None = None,
    height: int | None = None,
    selection_mode: SelectionMode = "single-object",
    on_select: Literal["rerun"] | WidgetCallback = "rerun",
    key: Key | None = None,

# ==================================================
# Line: 291

def pydeck_chart(
    self,
    pydeck_obj: Deck | None = None,
    *,
    use_container_width: bool = True,
    width: int | None = None,
    height: int | None = None,
    selection_mode: SelectionMode = "single-object",
    on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
    key: Key | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/media.py
# Line: 75

def audio(
    self,
    data: MediaData,
    format: str = "audio/wav",
    start_time: MediaTime = 0,
    *,
    sample_rate: int | None = None,
    end_time: MediaTime | None = None,
    loop: bool = False,
    autoplay: bool = False,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 225

def video(
    self,
    data: MediaData,
    format: str = "video/mp4",
    start_time: MediaTime = 0,
    *,  # keyword-only arguments:
    subtitles: SubtitleData = None,
    end_time: MediaTime | None = None,
    loop: bool = False,
    autoplay: bool = False,
    muted: bool = False,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 495

def marshall_video(
    coordinates: str,
    proto: VideoProto,
    data: MediaData,
    mimetype: str = "video/mp4",
    start_time: int = 0,
    subtitles: SubtitleData = None,
    end_time: int | None = None,
    loop: bool = False,
    autoplay: bool = False,
    muted: bool = False,
    form_id: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# Line: 758

def marshall_audio(
    coordinates: str,
    proto: AudioProto,
    data: MediaData,
    mimetype: str = "audio/wav",
    start_time: int = 0,
    sample_rate: int | None = None,
    end_time: int | None = None,
    loop: bool = False,
    autoplay: bool = False,
    form_id: str | None = None,
    width: WidthWithoutContent = "stretch",

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/metric.py
# Line: 53

def metric(
    self,
    label: str,
    value: Value,
    delta: Delta = None,
    delta_color: DeltaColor = "normal",
    help: str | None = None,
    label_visibility: LabelVisibility = "visible",
    border: bool = False,
    width: Width = "stretch",

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/lib/image_utils.py
# Line: 345

def marshall_images(
    coordinates: str,
    image: ImageOrImageList,
    caption: str | npt.NDArray[Any] | list[str] | None,
    width: int | WidthBehavior,
    proto_imgs: ImageListProto,
    clamp: bool,
    channels: Channels = "RGB",
    output_format: ImageFormatOrAuto = "auto",

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/lib/column_types.py
# Line: 351

def NumberColumn(
    label: str | None = None,
    *,
    width: ColumnWidth | None = None,
    help: str | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    pinned: bool | None = None,
    default: int | float | None = None,
    format: str | NumberFormat | None = None,
    min_value: int | float | None = None,
    max_value: int | float | None = None,
    step: int | float | None = None,

# ==================================================
# Line: 509

def TextColumn(
    label: str | None = None,
    *,
    width: ColumnWidth | None = None,
    help: str | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    pinned: bool | None = None,
    default: str | None = None,
    max_chars: int | None = None,
    validate: str | None = None,

# ==================================================
# Line: 629

def LinkColumn(
    label: str | None = None,
    *,
    width: ColumnWidth | None = None,
    help: str | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    pinned: bool | None = None,
    default: str | None = None,
    max_chars: int | None = None,
    validate: str | None = None,
    display_text: str | None = None,

# ==================================================
# Line: 788

def CheckboxColumn(
    label: str | None = None,
    *,
    width: ColumnWidth | None = None,
    help: str | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    pinned: bool | None = None,
    default: bool | None = None,

# ==================================================
# Line: 895

def SelectboxColumn(
    label: str | None = None,
    *,
    width: ColumnWidth | None = None,
    help: str | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    pinned: bool | None = None,
    default: str | int | float | None = None,
    options: Iterable[str | int | float] | None = None,

# ==================================================
# Line: 1484

def DatetimeColumn(
    label: str | None = None,
    *,
    width: ColumnWidth | None = None,
    help: str | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    pinned: bool | None = None,
    default: datetime.datetime | None = None,
    format: str | Literal["localized", "distance", "calendar", "iso8601"] | None = None,
    min_value: datetime.datetime | None = None,
    max_value: datetime.datetime | None = None,
    step: int | float | datetime.timedelta | None = None,
    timezone: str | None = None,

# ==================================================
# Line: 1648

def TimeColumn(
    label: str | None = None,
    *,
    width: ColumnWidth | None = None,
    help: str | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    pinned: bool | None = None,
    default: datetime.time | None = None,
    format: str | Literal["localized", "iso8601"] | None = None,
    min_value: datetime.time | None = None,
    max_value: datetime.time | None = None,
    step: int | float | datetime.timedelta | None = None,

# ==================================================
# Line: 1801

def DateColumn(
    label: str | None = None,
    *,
    width: ColumnWidth | None = None,
    help: str | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    pinned: bool | None = None,
    default: datetime.date | None = None,
    format: str | Literal["localized", "distance", "iso8601"] | None = None,
    min_value: datetime.date | None = None,
    max_value: datetime.date | None = None,
    step: int | None = None,

# ==================================================
# Line: 1955

def ProgressColumn(
    label: str | None = None,
    *,
    width: ColumnWidth | None = None,
    help: str | None = None,
    pinned: bool | None = None,
    format: str | NumberFormat | None = None,
    min_value: int | float | None = None,
    max_value: int | float | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/lib/built_in_chart_utils.py
# Line: 148

def generate_chart(
    chart_type: ChartType,
    data: Data | None,
    x_from_user: str | None = None,
    y_from_user: str | Sequence[str] | None = None,
    x_axis_label: str | None = None,
    y_axis_label: str | None = None,
    color_from_user: str | Color | list[Color] | None = None,
    size_from_user: str | float | None = None,
    width: int | None = None,
    height: int | None = None,
    use_container_width: bool = True,
    # Bar & Area charts only:
    stack: bool | ChartStackType | None = None,
    # Bar charts only:
    horizontal: bool = False,

# ==================================================
# Line: 818

def _get_axis_encodings(
    df: pd.DataFrame,
    chart_type: ChartType,
    x_column: str | None,
    y_column: str | None,
    x_from_user: str | None,
    y_from_user: str | Sequence[str] | None,
    x_axis_label: str | None,
    y_axis_label: str | None,
    stack: bool | ChartStackType | None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/connections/sql_connection.py
# Line: 222

def query(
    self,
    sql: str,
    *,  # keyword-only arguments:
    show_spinner: bool | str = "Running `sql.query(...)`.",
    ttl: float | int | timedelta | None = None,
    index_col: str | list[str] | None = None,
    chunksize: int | None = None,
    params: Any | None = None,
    **kwargs: Any,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/caching/cache_resource_api.py
# Line: 146

def __init__(
    self,
    func: types.FunctionType,
    show_spinner: bool | str,
    max_entries: int | None,
    ttl: float | timedelta | str | None,
    validate: ValidateFunc | None,
    hash_funcs: HashFuncsDict | None = None,

# ==================================================
# Line: 216

def __call__(
    self,
    *,
    ttl: float | timedelta | str | None = None,
    max_entries: int | None = None,
    show_spinner: bool | str = True,
    validate: ValidateFunc | None = None,
    experimental_allow_widgets: bool = False,
    hash_funcs: HashFuncsDict | None = None,

# ==================================================
# Line: 227

def __call__(
    self,
    func: F | None = None,
    *,
    ttl: float | timedelta | str | None = None,
    max_entries: int | None = None,
    show_spinner: bool | str = True,
    validate: ValidateFunc | None = None,
    experimental_allow_widgets: bool = False,
    hash_funcs: HashFuncsDict | None = None,

# ==================================================
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
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/caching/legacy_cache_api.py
# Line: 34

def cache(
    func: F | None = None,
    persist: bool = False,
    allow_output_mutation: bool = False,
    show_spinner: bool = True,
    suppress_st_warning: bool = False,  # noqa: ARG001
    hash_funcs: HashFuncsDict | None = None,
    max_entries: int | None = None,
    ttl: float | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/caching/cache_data_api.py
# Line: 90

def __init__(
    self,
    func: types.FunctionType,
    show_spinner: bool | str,
    persist: CachePersistType,
    max_entries: int | None,
    ttl: float | timedelta | str | None,
    hash_funcs: HashFuncsDict | None = None,

# ==================================================
# Line: 350

def __call__(
    self,
    *,
    ttl: float | timedelta | str | None = None,
    max_entries: int | None = None,
    show_spinner: bool | str = True,
    persist: CachePersistType | bool = None,
    experimental_allow_widgets: bool = False,
    hash_funcs: HashFuncsDict | None = None,

# ==================================================
# Line: 361

def __call__(
    self,
    func: F | None = None,
    *,
    ttl: float | timedelta | str | None = None,
    max_entries: int | None = None,
    show_spinner: bool | str = True,
    persist: CachePersistType | bool = None,
    experimental_allow_widgets: bool = False,
    hash_funcs: HashFuncsDict | None = None,

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
# Line: 608

def __init__(
    self,
    key: str,
    storage: CacheStorage,
    persist: CachePersistType,
    max_entries: int | None,
    ttl_seconds: float | None,
    display_name: str,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/state/widgets.py
# Line: 36

def register_widget(
    element_id: str,
    *,
    deserializer: WidgetDeserializer[T],
    serializer: WidgetSerializer[T],
    ctx: ScriptRunContext | None,
    on_change_handler: WidgetCallback | None = None,
    args: WidgetArgs | None = None,
    kwargs: WidgetKwargs | None = None,
    value_type: ValueFieldName,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/scriptrunner/script_runner.py
# Line: 169

def __init__(
    self,
    session_id: str,
    main_script_path: str,
    session_state: SessionState,
    uploaded_file_mgr: UploadedFileManager,
    script_cache: ScriptCache,
    initial_rerun_data: RerunData,
    user_info: dict[str, str | bool | None],
    fragment_storage: FragmentStorage,
    pages_manager: PagesManager,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/app_session.py
# Line: 86

def __init__(
    self,
    script_data: ScriptData,
    uploaded_file_manager: UploadedFileManager,
    script_cache: ScriptCache,
    message_enqueued_callback: Callable[[], None] | None,
    user_info: dict[str, str | bool | None],
    session_id_override: str | None = None,

# ==================================================
# Line: 501

def _on_scriptrunner_event(
    self,
    sender: ScriptRunner | None,
    event: ScriptRunnerEvent,
    forward_msg: ForwardMsg | None = None,
    exception: BaseException | None = None,
    client_state: ClientState | None = None,
    page_script_hash: str | None = None,
    fragment_ids_this_run: list[str] | None = None,
    pages: dict[PageHash, PageInfo] | None = None,

# ==================================================
# Line: 531

def _handle_scriptrunner_event_on_event_loop(
    self,
    sender: ScriptRunner | None,
    event: ScriptRunnerEvent,
    forward_msg: ForwardMsg | None = None,
    exception: BaseException | None = None,
    client_state: ClientState | None = None,
    page_script_hash: str | None = None,
    fragment_ids_this_run: list[str] | None = None,
    pages: dict[PageHash, PageInfo] | None = None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/config.py
# Line: 237

def _create_option(
    key: str,
    description: str | None = None,
    default_val: Any | None = None,
    scriptable: bool = False,
    visibility: str = "visible",
    deprecated: bool = False,
    deprecation_text: str | None = None,
    expiration_date: str | None = None,
    replaced_by: str | None = None,
    type_: type = str,
    sensitive: bool = False,
    multiple: bool = False,

# ==================================================
