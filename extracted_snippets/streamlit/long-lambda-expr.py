# long-lambda-expr snippets for streamlit

# File: /root/ecooptimizer/streamlit/e2e_playwright/custom_components/component_errors_test.py
# Line: 54

lambda: any(
    "Client Error: Custom Component streamlit_ace.streamlit_ace source error"
    in message
    for message in messages
),

# ==================================================
# Line: 82

lambda: any(
    "Client Error: Custom Component streamlit_ace.streamlit_ace fetch error"
    in message
    for message in messages
),

# ==================================================
# Line: 94

lambda: any(
    "Client Error: Custom Component streamlit_ace.streamlit_ace timeout error"
    in message
    for message in messages
),

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/host_config_test.py
# Line: 88

lambda: any(
    "The page that you have requested does not seem to exist. Running the app's main page."
    in message.text
    for message in messages
),

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_dataframe_interactions_test.py
# Line: 458

lambda response: response.url.endswith("_stcore/host-config")
and response.json()["enforceDownloadInNewTab"] is True,

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_set_page_config_test.py
# Line: 47

lambda: (bbox := expander_container.bounding_box()) is not None
and bbox["width"] > narrow_expander_width,

# ==================================================
# Line: 78

lambda: (bbox := expander_container.bounding_box()) is not None
and bbox["width"] == narrow_expander_width,

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/st_file_uploader_test.py
# Line: 534

lambda: any(
    "Client Error: File uploader error on file upload" in message
    for message in messages
),

# ==================================================
# Line: 589

lambda: any(
    "Client Error: File uploader error on file delete" in message
    for message in messages
),

# ==================================================
# File: /root/ecooptimizer/streamlit/e2e_playwright/help_tooltip_test.py
# Line: 88

lambda: (bbox := tooltip.bounding_box()) is not None
and bbox["x"] + bbox["width"] <= viewport_width,

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/deprecation_util.py
# Line: 147

lambda: show_deprecation_warning(
    make_deprecated_name_warning(
        old_name, new_name, removal_date, include_st_prefix=include_st_prefix
    )
),

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/secrets.py
# Occurrences: Lines 48-70 (4 instances)

self.missing_attr_message: Callable[[str], str] = lambda attr_name: (
    f'st.secrets has no attribute "{attr_name}". '
    "Did you forget to add it to secrets.toml, mount it to secret directory, or the app settings "
    "on Streamlit Cloud? More info: "
    "https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management"
)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/caching/cache_resource_api.py
# Line: 420

return lambda f: make_cached_func_wrapper(  # type: ignore
    CachedResourceFuncInfo(
        func=f,  # type: ignore
        show_spinner=show_spinner,
        max_entries=max_entries,
        ttl=ttl,
        validate=validate,
        hash_funcs=hash_funcs,
    )
)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/runtime/app_session.py
# Line: 519

lambda: self._handle_scriptrunner_event_on_event_loop(
    sender,
    event,
    forward_msg,
    exception,
    client_state,
    page_script_hash,
    fragment_ids_this_run,
    pages,
)

# ==================================================
# File: /root/ecooptimizer/streamlit/lib/streamlit/watcher/local_sources_watcher.py
# Line: 250

lambda m: list(m.__path__._path)
if hasattr(m, "__path__")
# This check prevents issues with torch classes:
# https://github.com/streamlit/streamlit/issues/10992
and type(m.__path__).__name__ == "_NamespacePath"
and hasattr(m.__path__, "_path")
else [],

# ==================================================
