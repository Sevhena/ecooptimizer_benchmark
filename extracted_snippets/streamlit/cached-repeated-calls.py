# cached-repeated-calls snippets for streamlit

# File: /root/ecooptimizer/streamlit/e2e_playwright/st_fragment_multiple_fragments_test.py
# Line: 44

fragment_1_text, fragment_2_text = _get_uuids(app)

# ==================================================
# Line: 53

fragment_1_text, fragment_2_text = _get_uuids(app)

# ==================================================
# Line: 69

fragment_1_text, fragment_2_text = _get_uuids(app)

# ==================================================
# Line: 80

fragment_1_text, fragment_2_text = _get_uuids(app)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_popover_test.py
# Line: 70

popover_container = open_popover(themed_app, "popover 3 (with widgets)")

# ==================================================
# Line: 82

popover_container = open_popover(themed_app, "popover 3 (with widgets)")

# ==================================================
# Line: 119

popover_container = open_popover(app, "popover 3 (with widgets)")

# ==================================================
# Line: 125

text_input_element = popover_container.get_by_test_id("stTextInput").nth(0)

# ==================================================
# Occurrences: Lines 134-137 (2 instances)

popover_container = open_popover(app, "popover 3 (with widgets)")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_dataframe_selections_test.py
# Line: 110

selection_text = app.get_by_test_id("stMarkdownContainer").filter(has_text=expected)

# ==================================================
# Line: 122

selection_text = app.get_by_test_id("stMarkdownContainer").filter(has_text=expected)

# ==================================================
# Line: 134

selection_text = app.get_by_test_id("stMarkdownContainer").filter(has_text=expected)

# ==================================================
# Line: 358

toolbar_buttons = dataframe_toolbar.get_by_test_id("stElementToolbarButton")

# ==================================================
# Line: 364

toolbar_buttons = dataframe_toolbar.get_by_test_id("stElementToolbarButton")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_color_picker_test.py
# Occurrences: Lines 103-108 (2 instances)

color_picker_popover = app.get_by_test_id("stColorPickerPopover")

# ==================================================
# Line: 126

color_picker_popover = app.get_by_test_id("stColorPickerPopover")

# ==================================================
# Line: 133

hsl_text_inputs = app.get_by_test_id("stColorPickerPopover").locator("input")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_chat_input_test.py
# Line: 168

chat_input_area = chat_input.locator("textarea")

# ==================================================
# Line: 175

chat_input_area = chat_input.locator("textarea")

# ==================================================
# Line: 309

uploaded_file_names = uploaded_files.get_by_test_id("stChatInputFileName")

# ==================================================
# Line: 317

uploaded_file_names = uploaded_files.get_by_test_id("stChatInputFileName")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/hostframe_app_test.py
# Line: 176

headers = r.value.all_headers()

# ==================================================
# Line: 201

headers = r.value.all_headers()

# ==================================================
# Occurrences: Lines 346-349 (2 instances)

lambda: len(get_observed_connection_statuses(frame)) == 3,

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_dialog_test.py
# Line: 109

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Line: 115

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Occurrences: Lines 133-138 (2 instances)

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Occurrences: Lines 150-150 (2 instances)

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Occurrences: Lines 156-156 (2 instances)

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Occurrences: Lines 167-167 (2 instances)

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Occurrences: Lines 174-174 (2 instances)

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Line: 189

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Line: 195

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Line: 203

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Line: 210

main_dialog = app.get_by_test_id(modal_test_id)

# ==================================================
# Occurrences: Lines 329-331 (3 instances)

large_width_dialog_fragment_id = get_markdown(app, "Fragment Id:").text_content()

# ==================================================
# Line: 337

nested_dialog_fragment_id = get_markdown(app, "Fragment Id:").text_content()

# ==================================================
# Occurrences: Lines 348-350 (2 instances)

dialog = app.get_by_role("dialog")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_segmented_control_test.py
# Line: 81

text = get_markdown(themed_app, "Single selection: Foobar")

# ==================================================
# Line: 89

text = get_markdown(themed_app, "Single selection: Foobar")

# ==================================================
# Line: 117

text = get_markdown(themed_app, "Single icon selection: 1")

# ==================================================
# Line: 127

text = get_markdown(themed_app, "Single icon selection: 1")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/forward_msg_cache_test.py
# Occurrences: Lines 111-111 (2 instances)

payload = payload.encode("utf-8")

# ==================================================
# Occurrences: Lines 119-119 (2 instances)

payload = payload.encode("utf-8")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/fast_rerun_safety_test.py
# Line: 21

counters = app.get_by_test_id("stMarkdown")

# ==================================================
# Line: 28

counters = app.get_by_test_id("stMarkdown")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_write_stream_test.py
# Line: 38

stream_output = get_element_by_key(app, "stream-output")

# ==================================================
# Line: 52

stream_output = get_element_by_key(app, "stream-output")

# ==================================================
# Line: 67

stream_output = get_element_by_key(app, "stream-output")

# ==================================================
# Line: 81

stream_output = get_element_by_key(app, "stream-output")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_plotly_chart_select_test.py
# Line: 211

chart = app.get_by_test_id("stPlotlyChart").nth(5)

# ==================================================
# Line: 231

chart = app.get_by_test_id("stPlotlyChart").nth(5)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_heading_test.py
# Line: 160

link_container = header.get_by_test_id("stHeaderActionElements").locator("a")

# ==================================================
# Line: 167

link_container = header.get_by_test_id("stHeaderActionElements").locator("a")

# ==================================================
# Line: 174

link_container = header.get_by_test_id("stHeaderActionElements").locator("a")

# ==================================================
# Line: 193

link_container = header.get_by_test_id("stHeaderActionElements").locator("a")

# ==================================================
# Line: 200

link_container = header.get_by_test_id("stHeaderActionElements").locator("a")

# ==================================================
# Line: 207

link_container = header.get_by_test_id("stHeaderActionElements").locator("a")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_divider_test.py
# Occurrences: Lines 22-23 (2 instances)

markdown_elements = themed_app.get_by_test_id("stMarkdown")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_date_input_test.py
# Line: 118

empty_number_input = app.get_by_test_id("stDateInput").nth(12).locator("input")

# ==================================================
# Line: 138

empty_number_input = app.get_by_test_id("stDateInput").nth(12).locator("input")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_image_test.py
# Occurrences: Lines 217-221 (4 instances)

image = all_images.nth(i).get_by_test_id("stImageContainer")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_spinner_test.py
# Occurrences: Lines 39-41 (2 instances)

initial_text = app.get_by_test_id("stSpinner").text_content()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_dataframe_interactions_test.py
# Line: 448

result = response.json()

# ==================================================
# Line: 459

and response.json()["enforceDownloadInNewTab"] is True,

# ==================================================
# Line: 642

initial_canvas_bounding_box = df.locator("canvas").first.bounding_box()

# ==================================================
# Line: 652

autosized_canvas_bounding_box = df.locator("canvas").first.bounding_box()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_set_page_config_test.py
# Line: 35

expander_dimensions = expander_container.bounding_box()

# ==================================================
# Line: 47

lambda: (bbox := expander_container.bounding_box()) is not None

# ==================================================
# Line: 59

app_view_container = app.get_by_test_id("stAppViewContainer")

# ==================================================
# Line: 66

expander_dimensions = expander_container.bounding_box()

# ==================================================
# Line: 72

app_view_container = app.get_by_test_id("stAppViewContainer")

# ==================================================
# Line: 78

lambda: (bbox := expander_container.bounding_box()) is not None

# ==================================================
# Occurrences: Lines 223-228 (2 instances)

main_menu_items = app.get_by_test_id("stMainMenuList").first.get_by_role("option")

# ==================================================
# Occurrences: Lines 240-244 (2 instances)

main_menu_items = app.get_by_test_id("stMainMenuList").first.get_by_role("option")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_link_button_test.py
# Occurrences: Lines 46-57 (4 instances)

link_elements = themed_app.get_by_test_id("stLinkButton")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_fragments_nested_test.py
# Line: 165

expect(_get_inner_fragment_counter_text(app)).to_have_count(0)

# ==================================================
# Line: 171

counter_text = _get_inner_fragment_counter_text(app)

# ==================================================
# Occurrences: Lines 177-184 (3 instances)

_, _, previous_inner_fragment_text, _ = _get_uuids(app, number_markdown_elements)

# ==================================================
# Line: 192

expect(_get_inner_fragment_counter_text(app)).to_have_count(0)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/multipage_apps_v2/mpa_v2_basics_test.py
# Occurrences: Lines 255-258 (2 instances)

view_button = app.get_by_test_id("stSidebarNavViewButton")

# ==================================================
# Occurrences: Lines 265-268 (2 instances)

view_button = app.get_by_test_id("stSidebarNavViewButton")

# ==================================================
# Occurrences: Lines 274-277 (2 instances)

view_button = app.get_by_test_id("stSidebarNavViewButton")

# ==================================================
# Occurrences: Lines 287-289 (2 instances)

view_more_button = app.get_by_test_id("stSidebarNavViewButton")

# ==================================================
# Occurrences: Lines 296-298 (2 instances)

view_less_button = app.get_by_test_id("stSidebarNavViewButton")

# ==================================================
# Occurrences: Lines 309-311 (2 instances)

links = app.get_by_test_id("stSidebarNav").locator("a")

# ==================================================
# Occurrences: Lines 318-320 (2 instances)

view_less_button = app.get_by_test_id("stSidebarNavViewButton")

# ==================================================
# Occurrences: Lines 330-332 (2 instances)

links = app.get_by_test_id("stSidebarNav").locator("a")

# ==================================================
# Line: 445

expect(app.get_by_test_id("stSidebarNav")).to_be_visible()

# ==================================================
# Line: 452

nav_exists = app.get_by_test_id("stSidebarNav")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_pydeck_chart_select_test.py
# Line: 192

click_handling_div = get_click_handling_div(app, nth=0)

# ==================================================
# Line: 218

click_handling_div = get_click_handling_div(app, nth=0)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_file_uploader_test.py
# Line: 247

expect(app.get_by_test_id("stFileUploaderFileName")).to_have_text(

# ==================================================
# Line: 259

uploaded_file_names = app.get_by_test_id("stFileUploaderFileName")

# ==================================================
# Line: 321

expect(app.get_by_test_id("stFileUploaderFileName")).to_have_text(

# ==================================================
# Line: 333

uploaded_file_names = app.get_by_test_id("stFileUploaderFileName")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_sidebar_test.py
# Occurrences: Lines 67-71 (2 instances)

app.get_by_test_id("stSidebar").get_by_test_id("stTextInput").locator(

# ==================================================
# Line: 97

initial_width: int = sidebar.evaluate("el => el.getBoundingClientRect().width")

# ==================================================
# Line: 121

current_width: int = sidebar.evaluate("el => el.getBoundingClientRect().width")

# ==================================================
# Occurrences: Lines 127-132 (2 instances)

after_drag_width = sidebar.evaluate("el => el.getBoundingClientRect().width")

# ==================================================
# Line: 147

current_width = sidebar.evaluate("el => el.getBoundingClientRect().width")

# ==================================================
# Occurrences: Lines 162-163 (2 instances)

click_width = cast(
    "int", sidebar.evaluate("el => el.getBoundingClientRect().width")
)

# ==================================================
# Occurrences: Lines 171-172 (2 instances)

reset_width = cast(
    "int", sidebar.evaluate("el => el.getBoundingClientRect().width")
)

# ==================================================
# Line: 179

after_dblclick_width = sidebar.evaluate("el => el.getBoundingClientRect().width")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_effects_with_fragment_interactions_test.py
# Line: 46

animation_images = app.get_by_test_id("stBalloons").nth(0).locator("img")

# ==================================================
# Line: 72

animation_images = app.get_by_test_id("stBalloons").nth(0).locator("img")

# ==================================================
# Line: 99

animation_images = app.get_by_test_id("stSnow").nth(0).locator("img")

# ==================================================
# Line: 125

animation_images = app.get_by_test_id("stSnow").nth(0).locator("img")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_multiselect_test.py
# Occurrences: Lines 280-283 (2 instances)

multiselect_elem.locator("input").click()

# ==================================================
# Occurrences: Lines 294-295 (2 instances)

multiselect_elem.locator("input").click()

# ==================================================
# Occurrences: Lines 314-315 (2 instances)

multiselect_elem.locator("input").click()

# ==================================================
# Line: 333

multiselect_elem.locator("input").click()

# ==================================================
# Occurrences: Lines 366-369 (2 instances)

multiselect_elem.locator("input").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_html_test.py
# Occurrences: Lines 116-123 (4 instances)

main_container = app.get_by_test_id("stMain")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/conftest.py
# Occurrences: Lines 229-232 (2 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 290-294 (2 instances)

streamlit_stdout = streamlit_proc.terminate()

# ==================================================
# Occurrences: Lines 1002-1005 (2 instances)

start = time.time()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/multipage_apps/mpa_configure_sidebar_test.py
# Line: 75

page_links = themed_app.get_by_test_id("stPageLink-NavLink")

# ==================================================
# Line: 81

page_links = themed_app.get_by_test_id("stPageLink-NavLink")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_altair_chart_test.py
# Occurrences: Lines 25-27 (2 instances)

themed_app.get_by_test_id("stVegaLiteChart").locator("canvas")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/basic_app_test.py
# Occurrences: Lines 117-117 (2 instances)

payload = payload.encode("utf-8")

# ==================================================
# Occurrences: Lines 125-125 (2 instances)

payload = payload.encode("utf-8")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/shared/dataframe_utils.py
# Occurrences: Lines 367-372 (3 instances)

start_time = time.time()

# ==================================================
# Occurrences: Lines 391-393 (4 instances)

last_change_time = time.time()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/shared/oidc_mock_server.py
# Line: 100

code = str(uuid.uuid4())

# ==================================================
# Line: 122

"access_token": str(uuid.uuid4()),

# ==================================================
# Line: 128

"sub": str(uuid.uuid4()),

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/shared/performance.py
# Occurrences: Lines 146-146 (2 instances)

payload = payload.encode("utf-8")

# ==================================================
# Occurrences: Lines 154-154 (2 instances)

payload = payload.encode("utf-8")

# ==================================================
# Line: 165

start_time = time.time()

# ==================================================
# Line: 171

execution_time = time.time() - start_time

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/shared/app_utils.py
# Occurrences: Lines 364-366 (2 instances)

exception_el = locator.get_by_test_id("stException")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_dataframe_stable_rendering_test.py
# Occurrences: Lines 39-39 (2 instances)

dataframe_elements = app.get_by_test_id("stDataFrame")

# ==================================================
# Occurrences: Lines 45-45 (2 instances)

dataframe_elements = app.get_by_test_id("stDataFrame")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_fragment_run_every_test.py
# Line: 19

fragment_text = app.get_by_test_id("stMarkdown").first.text_content()

# ==================================================
# Line: 26

fragment_text = app.get_by_test_id("stMarkdown").first.text_content()

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/vendor/pympler/asizeof.py
# Line: 2178

if (len(self._profs) - len(t)) < 9:  # just show all

# ==================================================
# Occurrences: Lines 2192-2198 (3 instances)

len(t),

# ==================================================
# Line: 2212

z = len(self._profs) - len(t)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/navigation/page.py
# Occurrences: Lines 292-295 (2 instances)

code = ctx.pages_manager.get_page_script_byte_code(str(self._page))

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/components/v1/custom_component.py
# Occurrences: Lines 167-167 (2 instances)

element.component_instance.form_id = current_form_id(dg)

# ==================================================
# Occurrences: Lines 197-197 (2 instances)

form_id=current_form_id(dg),

# ==================================================
# Occurrences: Lines 207-207 (2 instances)

form_id=current_form_id(dg),

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/vega_charts.py
# Line: 1901

if on_select not in ["ignore", "rerun"] and not callable(on_select):

# ==================================================
# Line: 1913

is_callback = callable(on_select)

# ==================================================
# Line: 1992

on_change_handler=on_select if callable(on_select) else None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/audio_input.py
# Line: 237

form_id=current_form_id(self.dg),

# ==================================================
# Line: 247

audio_input_proto.form_id = current_form_id(self.dg)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/selectbox.py
# Line: 523

form_id=current_form_id(self.dg),

# ==================================================
# Line: 544

selectbox_proto.form_id = current_form_id(self.dg)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/camera_input.py
# Line: 231

form_id=current_form_id(self.dg),

# ==================================================
# Line: 241

camera_input_proto.form_id = current_form_id(self.dg)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/slider.py
# Line: 675

form_id=current_form_id(self.dg),

# ==================================================
# Line: 778

"step": timedelta(minutes=15),

# ==================================================
# Line: 793

step = timedelta(minutes=15)

# ==================================================
# Line: 923

slider_proto.form_id = current_form_id(self.dg)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/color_picker.py
# Occurrences: Lines 213-216 (2 instances)

form_id=current_form_id(self.dg),

# ==================================================
# Occurrences: Lines 244-245 (2 instances)

color_picker_proto.default = str(value)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/radio.py
# Line: 362

form_id=current_form_id(self.dg),

# ==================================================
# Line: 402

radio_proto.form_id = current_form_id(self.dg)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/checkbox.py
# Occurrences: Lines 327-330 (2 instances)

form_id=current_form_id(self.dg),

# ==================================================
# Occurrences: Lines 338-340 (2 instances)

checkbox_proto.default = bool(value)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/select_slider.py
# Line: 371

form_id=current_form_id(self.dg),

# ==================================================
# Line: 391

slider_proto.form_id = current_form_id(self.dg)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/chat.py
# Occurrences: Lines 331-334 (2 instances)

name.lower() in {item.value for item in PresetNames} or is_emoji(name)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/time_widgets.py
# Line: 527

form_id=current_form_id(self.dg),

# ==================================================
# Line: 546

time_input_proto.form_id = current_form_id(self.dg)

# ==================================================
# Line: 908

form_id=current_form_id(self.dg),

# ==================================================
# Line: 969

date_input_proto.form_id = current_form_id(self.dg)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/button.py
# Line: 1090

string_data = data.read()

# ==================================================
# Occurrences: Lines 1103-1107 (2 instances)

data_as_bytes = data.read()

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/data_editor.py
# Line: 938

form_id=current_form_id(self.dg),

# ==================================================
# Line: 981

proto.form_id = current_form_id(self.dg)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/number_input.py
# Line: 447

form_id=current_form_id(self.dg),

# ==================================================
# Line: 456

placeholder=None if placeholder is None else str(placeholder),

# ==================================================
# Occurrences: Lines 585-586 (2 instances)

number_input_proto.placeholder = str(placeholder)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/file_uploader.py
# Line: 446

form_id=current_form_id(self.dg),

# ==================================================
# Line: 467

file_uploader_proto.form_id = current_form_id(self.dg)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/text_widgets.py
# Line: 321

form_id=current_form_id(self.dg),

# ==================================================
# Line: 329

placeholder=str(placeholder),

# ==================================================
# Line: 343

text_input_proto.form_id = current_form_id(self.dg)

# ==================================================
# Line: 356

text_input_proto.placeholder = str(placeholder)

# ==================================================
# Line: 620

form_id=current_form_id(self.dg),

# ==================================================
# Line: 627

placeholder=str(placeholder),

# ==================================================
# Line: 640

text_area_proto.form_id = current_form_id(self.dg)

# ==================================================
# Line: 656

text_area_proto.placeholder = str(placeholder)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/plotly_chart.py
# Line: 461

if on_select not in ["ignore", "rerun"] and not callable(on_select):

# ==================================================
# Line: 473

is_callback = callable(on_select)

# ==================================================
# Line: 532

on_change_handler=on_select if callable(on_select) else None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/arrow.py
# Line: 537

if on_select not in ["ignore", "rerun"] and not callable(on_select):

# ==================================================
# Line: 548

is_callback = callable(on_select)

# ==================================================
# Line: 641

on_change_handler=on_select if callable(on_select) else None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/deck_gl_json_chart.py
# Line: 486

if on_select not in ["ignore", "rerun"] and not callable(on_select):

# ==================================================
# Line: 497

is_callback = callable(on_select)

# ==================================================
# Line: 525

on_change_handler=on_select if callable(on_select) else None,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/metrics_util.py
# Occurrences: Lines 173-177 (2 instances)

machine_id = f.read()

# ==================================================
# Occurrences: Lines 401-401 (2 instances)

exec_start = timer()

# ==================================================
# Occurrences: Lines 448-448 (4 instances)

command_telemetry.time = to_microseconds(timer() - exec_start)

# ==================================================
# Occurrences: Lines 459-459 (4 instances)

command_telemetry.time = to_microseconds(timer() - exec_start)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/caching/hashing.py
# Line: 476

obj = obj.sample(n=_PANDAS_SAMPLE_SIZE, seed=0)

# ==================================================
# Line: 497

obj = obj.sample(n=_PANDAS_SAMPLE_SIZE, seed=0)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/runtime_util.py
# Line: 73

msg_str = msg.SerializeToString()

# ==================================================
# Line: 88

msg_str = msg.SerializeToString()

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/stats.py
# Occurrences: Lines 51-55 (2 instances)

label = metric.labels.add()

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/state/session_state.py
# Line: 613

metadata = self._new_widget_state.widget_metadata.get(state_id)

# ==================================================
# Line: 624

metadata = self._new_widget_state.widget_metadata.get(state_id)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/scriptrunner/script_runner.py
# Line: 372

request = self._requests.on_scriptrunner_ready()

# ==================================================
# Line: 379

request = self._requests.on_scriptrunner_ready()

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/watcher/util.py
# Occurrences: Lines 137-140 (2 instances)

dirfiles = _dirfiles(dir_path, glob_pattern)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/auth_util.py
# Occurrences: Lines 132-139 (6 instances)

if auth_section.get("client_id"):

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/dataframe_util.py
# Occurrences: Lines 596-601 (2 instances)

data = data.copy(deep=True)

# ==================================================
# Line: 610

data = data.to_frame()

# ==================================================
# Line: 620

data = data.limit(max_unevaluated_rows).to_pandas()

# ==================================================
# Line: 633

data = data.to_frame()

# ==================================================
# Line: 655

data = data.to_frame()

# ==================================================
# Line: 665

data = data.limit(max_unevaluated_rows).to_pandas()

# ==================================================
# Line: 822

table = pa.Table.from_pandas(df)

# ==================================================
# Line: 831

table = pa.Table.from_pandas(df)

# ==================================================
# Line: 1127

df_copy = df.copy()

# ==================================================
# Line: 1142

df_copy = df.copy()

# ==================================================
# Occurrences: Lines 1381-1388 (4 instances)

return _unify_missing_values(df).to_dict(orient="records")

# ==================================================
# Line: 1396

df = _unify_missing_values(df)

# ==================================================
# Line: 1412

df = _unify_missing_values(df)

# ==================================================
