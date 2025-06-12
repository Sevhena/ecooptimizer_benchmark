# long-message-chain snippets for streamlit

# File: /root/ecooptimizer/streamlit/e2e_playwright/st_fragment_multiple_fragments_test.py
# Occurrences: Lines 36-40 (2 instances)

return app.get_by_test_id("stCheckbox").nth(1).locator("span").first

# ==================================================
# Line: 48

app.get_by_test_id("stButton").locator("button").first.click()

# ==================================================
# Line: 57

app.get_by_test_id("stButton").locator("button").last.click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_expander_state_test.py
# Occurrences: Lines 22-24 (2 instances)

app.get_by_test_id("stButton").nth(0).locator("button").click()

# ==================================================
# Line: 30

app.get_by_test_id("stButton").nth(1).locator("button").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_dataframe_selections_test.py
# Line: 320

app.get_by_test_id("stDataFrameColumnMenu").get_by_text("Sort ascending").click()

# ==================================================
# Line: 458

app.get_by_test_id("stButton").locator("button").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_color_picker_test.py
# Line: 48

color_pickers.nth(0).get_by_test_id("stColorPickerBlock").click()

# ==================================================
# Line: 66

color_pickers.nth(0).get_by_test_id("stColorPickerBlock").click()

# ==================================================
# Line: 82

color_pickers.nth(0).get_by_test_id("stColorPickerBlock").click()

# ==================================================
# Line: 101

color_pickers.nth(0).get_by_test_id("stColorPickerBlock").click()

# ==================================================
# Line: 124

color_pickers.nth(0).get_by_test_id("stColorPickerBlock").click()

# ==================================================
# Line: 151

app.get_by_test_id("stColorPicker").nth(5).get_by_test_id(
    "stColorPickerBlock"
).click()

# ==================================================
# Line: 175

app.get_by_test_id("stColorPicker").nth(6).get_by_test_id(
    "stColorPickerBlock"
).click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_chat_input_test.py
# Line: 28

chat_input.get_by_role("button").nth(0).click()

# ==================================================
# Line: 279

uploaded_files.get_by_test_id("stChatInputDeleteBtn").nth(0).click()

# ==================================================
# Line: 313

uploaded_files.get_by_test_id("stChatInputDeleteBtn").nth(0).click()

# ==================================================
# Line: 342

uploaded_files.get_by_test_id("stTooltipHoverTarget").nth(0).hover()

# ==================================================
# Line: 364

uploaded_files.get_by_test_id("stTooltipHoverTarget").nth(0).hover()

# ==================================================
# Line: 371

chat_input.get_by_role("button").nth(0).hover()

# ==================================================
# Line: 378

chat_input.get_by_role("button").nth(0).hover()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_altair_chart_basic_select_test.py
# Occurrences: Lines 74-118 (12 instances)

return app.get_by_test_id("stVegaLiteChart").locator("canvas").nth(0)

# ==================================================
# Line: 404

app.get_by_test_id("stButton").filter(
    has_text="Create some elements to unmount component"
).locator("button").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_map_ensure_no_stale_maps_test.py
# Line: 27

selection_dropdown.locator("li").nth(1).click()

# ==================================================
# Line: 33

selection_dropdown.locator("li").nth(0).click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_fragment_dynamic_form_test.py
# Occurrences: Lines 37-39 (2 instances)

app.get_by_test_id("stSelectbox").locator("input").first.click()

# ==================================================
# Occurrences: Lines 50-52 (2 instances)

app.get_by_test_id("stSelectbox").locator("input").last.click()

# ==================================================
# Line: 68

app.get_by_test_id("stButton").locator("button").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/hostframe_app_test.py
# Line: 165

frame_locator.get_by_test_id("stFileUploaderDropzone").nth(
    uploader_index
).click()

# ==================================================
# Line: 191

frame_locator.get_by_test_id("stFileUploaderDropzone").nth(
    uploader_index
).click()

# ==================================================
# Line: 238

frame_locator.get_by_test_id("stExpander").locator(
    EXPANDER_HEADER_IDENTIFIER
).click()

# ==================================================
# Occurrences: Lines 270-272 (2 instances)

frame_locator.get_by_test_id("stMainMenu").locator("button").click()

# ==================================================
# Line: 284

frame_locator.get_by_test_id("stMainMenu").locator("button").click()

# ==================================================
# Line: 319

frame_locator.get_by_test_id("stSidebar").locator("button").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_dialog_test.py
# Line: 379

app.get_by_test_id("stTextInput").locator("input").click()

# ==================================================
# Line: 471

app.get_by_test_id("stButton")
.filter(has_text="Close Dialog")
.locator("button")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_rerun_test.py
# Line: 68

app.get_by_test_id("stSelectbox").first.locator("input").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/mega_tester_app.py
# Line: 257

alt.Chart(data)
.mark_circle()
.encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"]),

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_number_input_test.py
# Line: 146

app.get_by_test_id("stNumberInput").nth(0).locator("input")

# ==================================================
# Line: 159

app.get_by_test_id("stNumberInput").nth(0).locator("input")

# ==================================================
# Line: 199

app.get_by_test_id("stNumberInput").nth(11).locator("input").first

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_plotly_chart_select_test.py
# Line: 164

app.locator('[data-title="Zoom in"]').nth(0).click()

# ==================================================
# Line: 188

app.locator('[data-title="Pan"]').nth(0).click()

# ==================================================
# Line: 248

chart.locator('[data-title="Box Select"]').nth(0).click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_select_slider_test.py
# Occurrences: Lines 100-101 (2 instances)

app.get_by_test_id("stExpander").locator("summary").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_markdown_test.py
# Line: 106

app.get_by_test_id("stVerticalBlock").get_by_test_id("stVerticalBlock").nth(0)

# ==================================================
# Line: 120

app.get_by_test_id("stVerticalBlock")
.filter(has=app.get_by_text(text, exact=True))
.nth(1)

# ==================================================
# Line: 220

app.get_by_test_id("stMain").get_by_test_id("stMarkdown").nth(0)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_columns_test.py
# Line: 72

get_expander(app, "Column gap small").get_by_test_id("stHorizontalBlock").nth(0)

# ==================================================
# Line: 85

get_expander(app, "Column gap medium")
.get_by_test_id("stHorizontalBlock")
.nth(0)

# ==================================================
# Line: 100

get_expander(app, "Column gap large").get_by_test_id("stHorizontalBlock").nth(0)

# ==================================================
# Line: 113

get_expander(app, "Column gap none").get_by_test_id("stHorizontalBlock").nth(0)

# ==================================================
# Line: 126

get_expander(app, "Nested columns - one level")
.get_by_test_id("stHorizontalBlock")
.nth(0)

# ==================================================
# Line: 139

get_expander(app, "Variable-width columns (relative numbers)")
.get_by_test_id("stHorizontalBlock")
.nth(0)

# ==================================================
# Line: 152

get_expander(app, "Variable-width columns (absolute numbers)")
.get_by_test_id("stHorizontalBlock")
.nth(0)

# ==================================================
# Line: 165

get_expander(app, "Vertical alignment - top")
.get_by_test_id("stHorizontalBlock")
.nth(0)

# ==================================================
# Line: 189

get_expander(app, "Vertical alignment - center")
.get_by_test_id("stHorizontalBlock")
.nth(0)

# ==================================================
# Line: 209

get_expander(app, "Vertical alignment - bottom")
.get_by_test_id("stHorizontalBlock")
.nth(0)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_map_test.py
# Occurrences: Lines 47-54 (3 instances)

maps.nth(0).locator(".mapboxgl-ctrl-group").nth(0),

# ==================================================
# Line: 60

maps.nth(1).locator("canvas").nth(1),

# ==================================================
# Line: 67

maps.nth(2).locator("canvas").nth(1),

# ==================================================
# Line: 74

maps.nth(3).locator("canvas").nth(1),

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_fragment_mixed_execution_flow_test.py
# Line: 42

app.get_by_test_id("stButton").locator("button").filter(
    has_text="Full app rerun"
).click()

# ==================================================
# Line: 50

app.get_by_test_id("stButton").locator("button").nth(1).click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/markdown_features.py
# Line: 139

st.container(key="st_popover").popover(selected_feature_markdown).write("Expanded!")

# ==================================================
# Line: 157

st.container(key="st_expander").expander(selected_feature_markdown).write("Expanded!")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_date_input_test.py
# Line: 118

empty_number_input = app.get_by_test_id("stDateInput").nth(12).locator("input")

# ==================================================
# Line: 128

app.get_by_test_id("stMarkdown").nth(13).click()

# ==================================================
# Occurrences: Lines 138-142 (2 instances)

empty_number_input = app.get_by_test_id("stDateInput").nth(12).locator("input")

# ==================================================
# Line: 152

app.get_by_test_id("stDateInput").nth(3).click()

# ==================================================
# Line: 167

app.get_by_test_id("stDateInput").nth(4).click()

# ==================================================
# Line: 192

app.get_by_test_id("stDateInput").nth(11).click()

# ==================================================
# Line: 247

themed_app.get_by_test_id("stDateInput").nth(4).click()

# ==================================================
# Line: 283

app.get_by_test_id("stDateInput").nth(4).click()

# ==================================================
# Occurrences: Lines 306-311 (2 instances)

date_input_field = app.get_by_test_id("stDateInput").nth(4).locator("input")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_selectbox_test.py
# Line: 79

app.get_by_test_id("stSelectbox").nth(3).locator("input").click()

# ==================================================
# Line: 85

selection_dropdown.locator("li").nth(1).click()

# ==================================================
# Line: 94

selectbox_input = app.get_by_test_id("stSelectbox").nth(3).locator("input")

# ==================================================
# Line: 110

selectbox_input = app.get_by_test_id("stSelectbox").nth(3).locator("input")

# ==================================================
# Line: 124

empty_selectbox_input = app.get_by_test_id("stSelectbox").locator("input").nth(8)

# ==================================================
# Line: 149

app.get_by_test_id("stSelectbox").nth(3).locator("input").click()

# ==================================================
# Line: 173

app.get_by_test_id("stSelectbox").nth(7).locator("input").click()

# ==================================================
# Line: 237

app.get_by_test_id("stMarkdownContainer").get_by_text(
    "selectbox 14 (test dismiss behavior)"
).click()

# ==================================================
# Line: 253

selectbox_input = app.get_by_test_id("stSelectbox").nth(14).locator("input")

# ==================================================
# Line: 277

selectbox_input = app.get_by_test_id("stSelectbox").nth(0).locator("input")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_fragment_basics_test.py
# Line: 58

app.get_by_test_id("stDownloadButton").locator("button").click()

# ==================================================
# Line: 94

app.locator('[data-baseweb="popover"]').locator("input").fill("0xFFFFFF")

# ==================================================
# Line: 120

app.get_by_test_id("stMultiSelect").locator("input").click()

# ==================================================
# Line: 146

radio = app.get_by_test_id("stRadio").locator('label[data-baseweb="radio"]').nth(1)

# ==================================================
# Occurrences: Lines 159-162 (3 instances)

app.get_by_test_id("stSelectbox").locator("input").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_graphviz_chart_test.py
# Line: 22

return app.get_by_test_id("stGraphVizChart").nth(0).locator("svg")

# ==================================================
# Line: 119

app.get_by_test_id("stGraphVizChart").nth(2).locator("svg"),

# ==================================================
# Line: 131

app.get_by_test_id("stGraphVizChart").nth(5).locator("svg"),

# ==================================================
# Line: 144

app.get_by_test_id("stGraphVizChart").nth(6).locator("svg"),

# ==================================================
# Line: 152

themed_app.get_by_test_id("stGraphVizChart").nth(1).locator("svg"),

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_add_rows.py
# Line: 67

alt.Chart(df).mark_line(point=True).encode(x="a", y="b").interactive(),

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/i18n_test.py
# Line: 52

themed_app.get_by_test_id("stDateInput").nth(0).click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_image_test.py
# Line: 221

image = all_images.nth(i).get_by_test_id("stImageContainer").locator("img")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_dataframe_interactions_test.py
# Line: 333

app.get_by_test_id("stButton").locator("button").click()

# ==================================================
# Line: 647

app.get_by_test_id("stDataFrameColumnMenu").get_by_text("Autosize").click()

# ==================================================
# Line: 688

app.get_by_test_id("stDataFrameColumnMenu").get_by_text(
    "Sort ascending"
).click()

# ==================================================
# Line: 699

app.get_by_test_id("stDataFrameColumnMenu").get_by_text(
    "Sort descending"
).click()

# ==================================================
# Line: 712

app.get_by_test_id("stDataFrameColumnMenu").get_by_text(
    "Sort descending"
).click()

# ==================================================
# Line: 745

app.get_by_test_id("stDataFrameColumnMenu").get_by_text("Hide column").click()

# ==================================================
# Occurrences: Lines 793-798 (2 instances)

app.get_by_test_id("stDataFrameColumnMenu").get_by_text("Pin column").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_write_charts.py
# Line: 31

chart = alt.Chart(df).mark_circle().encode(x="a", y="b", size="c", color="c")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_code_test.py
# Occurrences: Lines 114-118 (2 instances)

app.get_by_test_id("stExpander").nth(0).get_by_test_id("stCode").first

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_vega_lite_chart_test.py
# Occurrences: Lines 40-49 (4 instances)

expect(vega_lite_charts.nth(0).locator("canvas").nth(0)).to_have_css(

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_page_link_test.py
# Occurrences: Lines 42-53 (4 instances)

page_links.nth(0).get_by_test_id("stMarkdownContainer").hover()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_pydeck_chart_test.py
# Line: 75

pydeck_charts.nth(0).locator("canvas").nth(0),

# ==================================================
# Line: 88

pydeck_charts.nth(0).locator("canvas").nth(1),

# ==================================================
# Line: 101

pydeck_charts.nth(0).locator("canvas").nth(1),

# ==================================================
# Line: 127

pydeck_charts.nth(0).locator("canvas").nth(0),

# ==================================================
# Line: 153

pydeck_charts.nth(0).locator("canvas").nth(0),

# ==================================================
# Line: 161

selectbox_input = app.get_by_test_id("stSelectbox").nth(0).locator("input")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_download_button_test.py
# Line: 74

download_button = app.get_by_test_id("stDownloadButton").nth(12).locator("button")

# ==================================================
# Line: 80

download_button = app.get_by_test_id("stDownloadButton").nth(12).locator("button")

# ==================================================
# Line: 121

download_button = app.get_by_test_id("stDownloadButton").nth(14).locator("button")

# ==================================================
# Line: 140

app.get_by_test_id("stDownloadButton").locator("button").nth(2)

# ==================================================
# Line: 155

app.get_by_test_id("stDownloadButton").locator("button").nth(3)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_form_test.py
# Line: 30

form_1.get_by_test_id("stTextArea").locator("textarea").press_sequentially(
    "this is some text", delay=100
)

# ==================================================
# Line: 43

form_1.get_by_test_id("stDateInput").locator("input").click()

# ==================================================
# Occurrences: Lines 49-78 (12 instances)

form_1.get_by_test_id("stMultiSelect").locator("input").click()

# ==================================================
# Line: 109

app.get_by_test_id("stFormSubmitButton").nth(0).locator("button").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_fragments_nested_test.py
# Occurrences: Lines 33-53 (4 instances)

app.get_by_test_id("stMarkdown")
.filter(has_text="outside all fragments:")
.text_content()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/app_hotkeys_test.py
# Line: 53

app.get_by_test_id("stTextInput").locator("input").press("r")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_expander_test.py
# Line: 91

num_input = main_expanders.nth(2).get_by_test_id("stNumberInput").locator("input")

# ==================================================
# Line: 97

main_expanders.nth(2).locator(EXPANDER_HEADER_IDENTIFIER).click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/multipage_apps_v2/mpa_v2_basics_test.py
# Line: 79

app.get_by_test_id("stSidebarNav").locator("a").nth(page_order.index(page_name))

# ==================================================
# Line: 412

app.get_by_test_id("stSidebarCollapseButton").locator("button").click()

# ==================================================
# Line: 427

app.get_by_test_id("stPageLink-NavLink").filter(has_text="page 5 page link").click()

# ==================================================
# Line: 436

app.get_by_test_id("stPageLink-NavLink").filter(has_text="page 9 page link").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/multipage_apps_v2/mpa_v2_title_test.py
# Line: 29

app.get_by_test_id("stSidebarNav").locator("a").nth(page_order.index(page_name))

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_pydeck_chart_select_test.py
# Occurrences: Lines 85-87 (2 instances)

app.get_by_test_id("stSelectbox").nth(0).locator("input").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_file_uploader_test.py
# Line: 53

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 92

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 124

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 153

app.get_by_test_id("stFileUploaderDeleteBtn").nth(uploader_index).click()

# ==================================================
# Line: 180

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 241

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 252

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 313

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 326

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 384

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 419

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 439

app.get_by_test_id("stFormSubmitButton").first.locator("button").click()

# ==================================================
# Line: 456

app.get_by_test_id("stFormSubmitButton").first.locator("button").click()

# ==================================================
# Line: 484

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 521

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# Line: 572

app.get_by_test_id("stFileUploaderDropzone").nth(uploader_index).click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_sidebar_test.py
# Occurrences: Lines 65-69 (2 instances)

app.get_by_test_id("stSidebarCollapsedControl").locator("button").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_effects_with_fragment_interactions_test.py
# Line: 46

animation_images = app.get_by_test_id("stBalloons").nth(0).locator("img")

# ==================================================
# Occurrences: Lines 57-60 (2 instances)

selectbox = app.get_by_test_id("stSelectbox").nth(0).locator("input")

# ==================================================
# Line: 72

animation_images = app.get_by_test_id("stBalloons").nth(0).locator("img")

# ==================================================
# Line: 99

animation_images = app.get_by_test_id("stSnow").nth(0).locator("img")

# ==================================================
# Occurrences: Lines 110-113 (2 instances)

selectbox = app.get_by_test_id("stSelectbox").nth(0).locator("input")

# ==================================================
# Line: 125

animation_images = app.get_by_test_id("stSnow").nth(0).locator("img")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_multiselect_test.py
# Line: 46

page.locator("li").filter(has_text=option_text).first.click()

# ==================================================
# Line: 169

app.get_by_test_id("stMultiSelect").nth(10).locator("input").click()

# ==================================================
# Line: 191

app.get_by_test_id("stMultiSelect").nth(9).click()

# ==================================================
# Line: 226

expect(app.get_by_test_id("stMultiSelect").locator("span").nth(1)).to_have_text(

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/hello_app_test.py
# Line: 24

app.get_by_test_id("stSidebarNav").locator("a").nth(index).click()

# ==================================================
# Line: 33

app.get_by_test_id("stMarkdownContainer").locator("h1").nth(0)

# ==================================================
# Line: 39

app.get_by_test_id("stSidebarNavLink")
.get_by_test_id("stIconMaterial")
.nth(index)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/conftest.py
# Line: 542

frame_locator.nth(0).get_by_test_id("stAppViewContainer").wait_for(
    timeout=30000, state="attached"
)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/websocket_disconnect_test.py
# Line: 34

app.get_by_test_id("stSlider").nth(0).hover()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_logo_test.py
# Line: 41

themed_app.get_by_test_id("stSidebarCollapseButton").locator("button").click()

# ==================================================
# Line: 57

themed_app.get_by_test_id("stSidebarCollapseButton").locator("button").click()

# ==================================================
# Line: 73

themed_app.get_by_test_id("stSidebarCollapseButton").locator("button").click()

# ==================================================
# Line: 90

selectbox_input = app.get_by_test_id("stSelectbox").nth(0).locator("input")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_text_input_test.py
# Line: 97

text_input_field = app.get_by_test_id("stTextInput").nth(9).locator("input").first

# ==================================================
# Line: 222

expect(app.get_by_test_id("stTextInput").nth(11).locator("input")).to_have_value(

# ==================================================
# Line: 229

text_input_field = app.get_by_test_id("stTextInput").nth(8).locator("input").first

# ==================================================
# Line: 267

text_area_field = app.get_by_test_id("stTextInput").nth(12).locator("input").first

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/multipage_apps/mpa_basics_test.py
# Line: 43

app.get_by_test_id("stSidebarNav").locator("a").nth(1).click()

# ==================================================
# Line: 63

app.get_by_test_id("stSidebarNav").locator("a").nth(2).click()

# ==================================================
# Line: 79

app.get_by_test_id("stSidebarNav").locator("a").nth(3).click()

# ==================================================
# Line: 148

app.get_by_test_id("stButton").nth(0).locator("button").first.click()

# ==================================================
# Line: 174

page.get_by_test_id("stButton").nth(0).locator("button").first.click()

# ==================================================
# Line: 192

page.get_by_test_id("stButton").nth(0).locator("button").first.click()

# ==================================================
# Line: 199

app.get_by_test_id("stButton").nth(1).locator("button").first.click()

# ==================================================
# Line: 218

app.get_by_test_id("stSidebarNav").locator("a").nth(2).click()

# ==================================================
# Line: 229

app.get_by_test_id("stSidebarNav").locator("a").nth(7).click()

# ==================================================
# Line: 241

app.get_by_test_id("stSidebarNav").locator("a").nth(2).click()

# ==================================================
# Line: 255

page.get_by_test_id("stSidebarNav").locator("a").nth(2).click()

# ==================================================
# Line: 268

page.get_by_test_id("stSidebarNav").locator("a").nth(2).click()

# ==================================================
# Line: 280

app.get_by_test_id("stSidebarNav").locator("a").nth(8).click()

# ==================================================
# Line: 293

app.get_by_test_id("stSidebarCollapseButton").locator("button").click()

# ==================================================
# Line: 309

app.get_by_test_id("stSidebarNav").locator("a").nth(9).click()

# ==================================================
# Line: 322

app.get_by_test_id("stSidebarCollapseButton").locator("button").click()

# ==================================================
# Line: 338

app.get_by_test_id("stSidebarNav").locator("a").nth(10).click()

# ==================================================
# Line: 351

app.get_by_test_id("stSidebarCollapseButton").locator("button").click()

# ==================================================
# Line: 364

app.get_by_test_id("stSidebarNav").locator("a").nth(11).click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/help_tooltip_test.py
# Line: 24

app.get_by_test_id("stButton")
.filter(has_text="Sidebar-button with help")
.locator("button")

# ==================================================
# Line: 49

app.get_by_test_id("stPopover")
.filter(has_text="Popover with toggle")
.locator("button")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/websocket_reconnects_test.py
# Line: 65

get_checkbox(app, "do something slow").locator("label").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_empty_test.py
# Line: 32

app.get_by_test_id("stButton").nth(0).get_by_role("button").click()

# ==================================================
# Line: 38

app.get_by_test_id("stButton").nth(1).get_by_role("button").click()

# ==================================================
# Line: 45

app.get_by_test_id("stButton").nth(2).get_by_role("button").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_plotly_chart_test.py
# Line: 72

themed_app.get_by_test_id("stPlotlyChart").nth(index).hover()

# ==================================================
# Line: 94

themed_app.get_by_test_id("stPlotlyChart").nth(index).hover()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/shared/oidc_mock_server.py
# Occurrences: Lines 34-45 (2 instances)

base64.urlsafe_b64encode(
    numbers.n.to_bytes((numbers.n.bit_length() + 7) // 8, byteorder="big")
)
.decode("utf-8")
.rstrip("=")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/shared/git_utils.py
# Line: 23

subprocess.check_output(["git", "rev-parse", "--show-toplevel"])
.strip()
.decode("utf-8")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/shared/app_utils.py
# Line: 129

locator.get_by_test_id("stButton").filter(has_text=label).locator("button")

# ==================================================
# Line: 172

get_popover(locator, label).get_by_role("button").first.click()

# ==================================================
# Line: 197

locator.get_by_test_id("stFormSubmitButton")
.filter(has_text=label)
.locator("button")

# ==================================================
# Line: 341

locator.get_by_test_id("stMarkdown")
.get_by_test_id("stMarkdownContainer")
.filter(has_text=expected_message)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_exception_test.py
# Line: 29

button = themed_app.get_by_test_id("stButton").nth(0).locator("button")

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_altair_chart.py
# Line: 24

chart = alt.Chart(df1).mark_circle().encode(x="a", y="b", size="c", color="c")

# ==================================================
# Line: 34

alt.Chart(df1, usermeta={"embedOptions": {"theme": None}})
.mark_circle()
.encode(x="a", y="b", size="c", color="c")

# ==================================================
# Line: 47

chart = alt.Chart(df2).mark_bar().encode(x="a", y="b")

# ==================================================
# Line: 61

alt.Chart(source)
.mark_arc(innerRadius=50)
.encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="category", type="nominal"),
)

# ==================================================
# Line: 78

alt.Chart(barley)
.mark_bar()
.encode(x="year:O", y="sum(yield):Q", color="year:N", column="site:N")

# ==================================================
# Line: 101

alt.Chart(stocks)
.encode(x="date:T", y="price:Q", color="symbol:N")
.transform_filter(alt.datum.symbol == "GOOG")

# ==================================================
# Occurrences: Lines 115-117 (2 instances)

c1 = alt.Chart(df3).mark_line().encode(alt.X("x"), alt.Y("y1"))

# ==================================================
# Line: 131

alt.Chart(df_cut_off_issue)
.mark_line(point=True)
.encode(
    x=alt.X("x", title="Date"),
    y=alt.Y("y:Q", title="Value"),
    color=alt.Color("category:N").legend(orient="bottom", title=None),
)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_time_input_test.py
# Line: 73

app.get_by_test_id("stTimeInput").nth(0).locator("input").click()

# ==================================================
# Line: 79

selection_dropdown.locator("li").nth(0).click()

# ==================================================
# Line: 90

themed_app.get_by_test_id("stTimeInput").nth(0).locator("input").click()

# ==================================================
# Line: 104

app.get_by_test_id("stTimeInput").nth(6).locator("input").click()

# ==================================================
# Line: 110

selection_dropdown.locator("li").nth(1).click()

# ==================================================
# Line: 168

app.get_by_test_id("stTimeInput").first.locator("input").click()

# ==================================================
# Line: 192

app.get_by_test_id("stTimeInput").nth(5).locator("input").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_text_area_test.py
# Line: 85

app.get_by_test_id("stTextArea").nth(12).locator("textarea").first

# ==================================================
# Line: 103

text_area_field = app.get_by_test_id("stTextArea").nth(9).locator("textarea").first

# ==================================================
# Line: 211

text_area_field = app.get_by_test_id("stTextArea").nth(8).locator("textarea").first

# ==================================================
# Line: 249

text_area_field = app.get_by_test_id("stTextArea").nth(13).locator("textarea").first

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_html_wide_mode_test.py
# Line: 30

app.get_by_test_id("stSidebarCollapseButton").locator("button").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_caption_test.py
# Line: 55

app.get_by_test_id("stMarkdown")
.filter(has=app.get_by_test_id("stCaptionContainer"))
.nth(2)

# ==================================================
# Line: 69

themed_app.get_by_test_id("stElementContainer")
.filter(has=themed_app.get_by_test_id("stCaptionContainer"))
.nth(3)

# ==================================================
# Line: 81

app.get_by_test_id("stElementContainer")
.filter(has=app.get_by_test_id("stCaptionContainer"))
.nth(4)

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_dataframe_config_test.py
# Line: 147

app.get_by_test_id("stDataFrameColumnMenu").get_by_text("Format").click()

# ==================================================
# Line: 169

app.get_by_test_id("stDataFrameColumnMenu").get_by_text("Format").click()

# ==================================================
# Line: 193

app.get_by_test_id("stDataFrameColumnMenu").get_by_text("Format").click()

# ==================================================
# Line: 218

app.get_by_test_id("stDataFrameColumnMenu").get_by_text("Format").click()

# ==================================================
# Line: 241

app.get_by_test_id("stDataFrameColumnMenu").get_by_text("Format").click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_experimental_set_query_params_test.py
# Line: 21

app.get_by_test_id("stButton").locator("button").first.click()

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_altair_chart_basic_select.py
# Line: 49

alt.Chart(cars)
.mark_point()
.encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(point, "Origin:N", alt.value("lightgray")),
    tooltip=alt.value(None),
)

# ==================================================
# Line: 70

alt.Chart(cars)
.mark_point()
.encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(interval, "Origin:N", alt.value("lightgray")),
    tooltip=alt.value(None),
)

# ==================================================
# Line: 94

alt.Chart(cars)
.mark_point()
.encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(interval, "Origin:N", alt.value("lightgray")),
    tooltip=["Horsepower", "Miles_per_Gallon"],
)

# ==================================================
# Line: 131

alt.Chart(source)
.mark_bar()
.encode(
    x="a",
    y="b",
    fillOpacity=alt.condition(point, alt.value(1), alt.value(0.3)),
    tooltip=alt.value(None),
)
.add_params(point)

# ==================================================
# Line: 149

alt.Chart(source)
.mark_bar()
.encode(
    x="a",
    y="b",
    fillOpacity=alt.condition(interval, alt.value(1), alt.value(0.3)),
    tooltip=alt.value(None),
)
.add_params(interval)

# ==================================================
# Line: 174

alt.Chart(source)
.mark_area()
.encode(
    x="year:T",
    y="net_generation:Q",
    color=alt.condition(point, "source:N", alt.value("lightgray")),
    tooltip=alt.value(None),
)

# ==================================================
# Line: 193

alt.Chart(source)
.mark_area()
.encode(
    x="year:T",
    y="net_generation:Q",
    color=alt.condition(interval, "source:N", alt.value("lightgray")),
    tooltip=alt.value(None),
)

# ==================================================
# Line: 220

alt.Chart(source)
.mark_bar()
.encode(
    alt.X("IMDB_Rating:Q", bin=True),
    y="count()",
    color=alt.condition(point, "IMDB_Rating:Q", alt.value("lightgray")),
    tooltip=alt.value(None),
)

# ==================================================
# Line: 243

alt.Chart(source)
.mark_bar()
.encode(
    alt.X("IMDB_Rating:Q", bin=True),
    y="count()",
    color=alt.condition(interval, "IMDB_Rating:Q", alt.value("lightgray")),
    tooltip=alt.value(None),
)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/vendor/pympler/asizeof.py
# Line: 504

return _repr(obj, clip=clip).strip("<>").replace("'", _NN)  # remove <''>

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/commands/page_config.py
# Line: 61

return {str(k).lower().strip(): v for k, v in dict.items()}

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/slider.py
# Line: 190

_micros_to_datetime(int(value), self.orig_tz)
.time()
.replace(tzinfo=self.orig_tz)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/widgets/time_widgets.py
# Line: 94

return datetime.now().time().replace(second=0, microsecond=0)

# ==================================================
# Line: 102

datetime.fromisoformat(value)
.time()
.replace(second=0, microsecond=0)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/elements/lib/built_in_chart_utils.py
# Occurrences: Lines 311-322 (2 instances)

chart.mark_point(filled=True, size=65)
.encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
.add_params(nearest)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/caching/hashing.py
# Line: 429

h, pd.util.hash_pandas_object(series_obj).to_numpy().tobytes()

# ==================================================
# Line: 479

self.update(h, obj.hash(seed=0).to_arrow().to_string().encode())

# ==================================================
# Line: 504

obj.hash_rows(seed=0).hash(seed=0).to_arrow().to_string().encode()

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/hello/dataframe_demo.py
# Line: 49

alt.Chart(data)
.mark_area(opacity=0.3)
.encode(
    x="year:T",
    y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
    color="Region:N",
)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/dataframe_util.py
# Line: 586

data = data.limit(max_unevaluated_rows).collect().to_pandas()

# ==================================================
# Line: 1384

return _unify_missing_values(df).to_numpy().tolist()

# ==================================================
