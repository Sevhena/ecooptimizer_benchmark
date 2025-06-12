# too-many-arguments snippets for SeleniumBase

# File: /root/ecooptimizer/SeleniumBase/seleniumbase/undetected/__init__.py
# Line: 41

def __init__(
    self,
    options=None,
    user_data_dir=None,
    driver_executable_path=None,
    browser_executable_path=None,
    port=0,
    enable_cdp_events=False,
    log_level=0,
    headless=False,
    patch_driver=True,
    version_main=None,
    patcher_force_close=False,
    suppress_welcome=True,
    use_subprocess=True,
    debug=False,
    **kw,

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/undetected/cdp_driver/browser.py
# Line: 90

async def create(
    cls,
    config: Config = None,
    *,
    user_data_dir: PathLike = None,
    headless: bool = False,
    incognito: bool = False,
    guest: bool = False,
    browser_executable_path: PathLike = None,
    browser_args: List[str] = None,
    sandbox: bool = True,
    host: str = None,
    port: int = None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/undetected/cdp_driver/cdp_util.py
# Line: 189

def __add_chrome_proxy_extension(
    extension_dir,
    proxy_string,
    proxy_user,
    proxy_pass,
    proxy_scheme="http",
    proxy_bypass_list=None,
    multi_proxy=False,

# ==================================================
# Line: 245

async def start(
    config: Optional[Config] = None,
    *,
    user_data_dir: Optional[PathLike] = None,
    headless: Optional[bool] = False,
    incognito: Optional[bool] = False,
    guest: Optional[bool] = False,
    browser_executable_path: Optional[PathLike] = None,
    browser_args: Optional[List[str]] = None,
    xvfb_metrics: Optional[List[str]] = None,  # "Width,Height" for Linux
    ad_block: Optional[bool] = False,
    sandbox: Optional[bool] = True,
    lang: Optional[str] = None,  # Set the Language Locale Code
    host: Optional[str] = None,  # Chrome remote-debugging-host
    port: Optional[int] = None,  # Chrome remote-debugging-port
    xvfb: Optional[int] = None,  # Use a special virtual display on Linux
    headed: Optional[bool] = None,  # Override default Xvfb mode on Linux
    expert: Optional[bool] = None,  # Open up closed Shadow-root elements
    agent: Optional[str] = None,  # Set the user-agent string
    proxy: Optional[str] = None,  # "host:port" or "user:pass@host:port"
    tzone: Optional[str] = None,  # Eg "America/New_York", "Asia/Kolkata"
    geoloc: Optional[list | tuple] = None,  # Eg (48.87645, 2.26340)
    extension_dir: Optional[str] = None,  # Chrome extension directory
    **kwargs: Optional[dict],

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/undetected/cdp_driver/config.py
# Line: 30

def __init__(
    self,
    user_data_dir: Optional[PathLike] = AUTO,
    headless: Optional[bool] = False,
    incognito: Optional[bool] = False,
    guest: Optional[bool] = False,
    browser_executable_path: Optional[PathLike] = AUTO,
    browser_args: Optional[List[str]] = AUTO,
    sandbox: Optional[bool] = True,
    lang: Optional[str] = "en-US",
    host: str = AUTO,
    port: int = AUTO,
    expert: bool = AUTO,
    proxy: Optional[str] = None,
    extension_dir: Optional[str] = None,
    **kwargs: dict,

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_behave_gui.py
# Line: 51

def do_behave_run(
    root,
    tests,
    selected_tests,
    command_string,
    browser_string,
    rs_string,
    quiet_mode,
    demo_mode,
    mobile_mode,
    dashboard,
    headless,
    save_screenshots,
    additional_options,

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_commander.py
# Line: 54

def do_pytest_run(
    root,
    tests,
    selected_tests,
    command_string,
    browser_string,
    rs_string,
    thread_string,
    verbose,
    demo_mode,
    mobile_mode,
    dashboard,
    html_report,
    headless,
    save_screenshots,
    additional_options,

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/plugins/sb_manager.py
# Line: 32

def SB(
    test=None,  # Test Mode: Output, Logging, Continue on failure unless "rtf".
    rtf=None,  # Shortcut / Duplicate of "raise_test_failure".
    raise_test_failure=None,  # If "test" mode, raise Exception on 1st failure.
    browser=None,  # Choose from "chrome", "edge", "firefox", or "safari".
    headless=None,  # Use the default headless mode for Chromium and Firefox.
    headless1=None,  # Use Chromium's old headless mode. (Fast, but limited)
    headless2=None,  # Use Chromium's new headless mode. (Has more features)
    locale_code=None,  # Set the Language Locale Code for the web browser.
    protocol=None,  # The Selenium Grid protocol: "http" or "https".
    servername=None,  # The Selenium Grid server/IP used for tests.
    port=None,  # The Selenium Grid port used by the test server.
    proxy=None,  # Use proxy. Format: "SERVER:PORT" or "USER:PASS@SERVER:PORT".
    proxy_bypass_list=None,  # Skip proxy when using the listed domains.
    proxy_pac_url=None,  # Use PAC file. (Format: URL or USERNAME:PASSWORD@URL)
    multi_proxy=None,  # Allow multiple proxies with auth when multi-threaded.
    agent=None,  # Modify the web browser's User-Agent string.
    cap_file=None,  # The desired capabilities to use with a Selenium Grid.
    cap_string=None,  # The desired capabilities to use with a Selenium Grid.
    recorder_ext=None,  # Enables the SeleniumBase Recorder Chromium extension.
    disable_cookies=None,  # Disable Cookies on websites. (Pages might break!)
    disable_js=None,  # Disable JavaScript on websites. (Pages might break!)
    disable_csp=None,  # Disable the Content Security Policy of websites.
    enable_ws=None,  # Enable Web Security on Chromium-based browsers.
    enable_sync=None,  # Enable "Chrome Sync" on websites.
    use_auto_ext=None,  # Use Chrome's automation extension.
    undetectable=None,  # Use undetected-chromedriver to evade bot-detection.
    uc_cdp_events=None,  # Capture CDP events in undetected-chromedriver mode.
    uc_subprocess=None,  # Use undetected-chromedriver as a subprocess.
    log_cdp_events=None,  # Capture {"performance": "ALL", "browser": "ALL"}
    incognito=None,  # Enable Chromium's Incognito mode.
    guest_mode=None,  # Enable Chromium's Guest mode.
    dark_mode=None,  # Enable Chromium's Dark mode.
    devtools=None,  # Open Chromium's DevTools when the browser opens.
    remote_debug=None,  # Enable Chrome's Debugger on "http://localhost:9222".
    enable_3d_apis=None,  # Enable WebGL and 3D APIs.
    swiftshader=None,  # Chrome: --use-gl=angle / --use-angle=swiftshader-webgl
    ad_block_on=None,  # Block some types of display ads from loading.
    host_resolver_rules=None,  # Set host-resolver-rules, comma-separated.
    block_images=None,  # Block images from loading during tests.
    do_not_track=None,  # Tell websites that you don't want to be tracked.
    chromium_arg=None,  # "ARG=N,ARG2" (Set Chromium args, ","-separated.)
    firefox_arg=None,  # "ARG=N,ARG2" (Set Firefox args, comma-separated.)
    firefox_pref=None,  # SET (Set Firefox PREFERENCE:VALUE set, ","-separated)
    user_data_dir=None,  # Set the Chrome user data directory to use.
    extension_zip=None,  # Load a Chrome Extension .zip|.crx, comma-separated.
    extension_dir=None,  # Load a Chrome Extension directory, comma-separated.
    disable_features=None,  # "F1,F2" (Disable Chrome features, ","-separated.)
    binary_location=None,  # Set path of the Chromium browser binary to use.
    driver_version=None,  # Set the chromedriver or uc_driver version to use.
    skip_js_waits=None,  # Skip JS Waits (readyState=="complete" and Angular).
    wait_for_angularjs=None,  # Wait for AngularJS to load after some actions.
    use_wire=None,  # Use selenium-wire's webdriver over selenium webdriver.
    external_pdf=None,  # Set Chrome "plugins.always_open_pdf_externally":True.
    window_position=None,  # Set the browser's starting window position: "X,Y"
    window_size=None,  # Set the browser's starting window size: "Width,Height"
    is_mobile=None,  # Use the mobile device emulator while running tests.
    mobile=None,  # Shortcut / Duplicate of "is_mobile".
    device_metrics=None,  # Set mobile metrics: "CSSWidth,CSSHeight,PixelRatio"
    xvfb=None,  # Run tests using the Xvfb virtual display server on Linux OS.
    xvfb_metrics=None,  # Set Xvfb display size on Linux: "Width,Height".
    start_page=None,  # The starting URL for the web browser when tests begin.
    rec_print=None,  # If Recorder is enabled, prints output after tests end.
    rec_behave=None,  # Like Recorder Mode, but also generates behave-gherkin.
    record_sleep=None,  # If Recorder enabled, also records self.sleep calls.
    data=None,  # Extra test data. Access with "self.data" in tests.
    var1=None,  # Extra test data. Access with "self.var1" in tests.
    var2=None,  # Extra test data. Access with "self.var2" in tests.
    var3=None,  # Extra test data. Access with "self.var3" in tests.
    variables=None,  # DICT (Extra test data. Access with "self.variables")
    account=None,  # Set account. Access with "self.account" in tests.
    environment=None,  # Set the test env. Access with "self.env" in tests.
    headed=None,  # Run tests in headed/GUI mode on Linux, where not default.
    maximize=None,  # Start tests with the browser window maximized.
    disable_ws=None,  # Reverse of "enable_ws". (None and False are different)
    disable_beforeunload=None,  # Disable the "beforeunload" event on Chromium.
    settings_file=None,  # A file for overriding default SeleniumBase settings.
    position=None,  # Shortcut / Duplicate of "window_position".
    size=None,  # Shortcut / Duplicate of "window_size".
    uc=None,  # Shortcut / Duplicate of "undetectable".
    undetected=None,  # Shortcut / Duplicate of "undetectable".
    uc_cdp=None,  # Shortcut / Duplicate of "uc_cdp_events".
    uc_sub=None,  # Shortcut / Duplicate of "uc_subprocess".
    locale=None,  # Shortcut / Duplicate of "locale_code".
    log_cdp=None,  # Shortcut / Duplicate of "log_cdp_events".
    ad_block=None,  # Shortcut / Duplicate of "ad_block_on".
    server=None,  # Shortcut / Duplicate of "servername".
    guest=None,  # Shortcut / Duplicate of "guest_mode".
    wire=None,  # Shortcut / Duplicate of "use_wire".
    pls=None,  # Shortcut / Duplicate of "page_load_strategy".
    sjw=None,  # Shortcut / Duplicate of "skip_js_waits".
    wfa=None,  # Shortcut / Duplicate of "wait_for_angularjs".
    cft=None,  # Use "Chrome for Testing"
    chs=None,  # Use "Chrome-Headless-Shell"
    save_screenshot=None,  # Save a screenshot at the end of each test.
    no_screenshot=None,  # No screenshots saved unless tests directly ask it.
    page_load_strategy=None,  # Set Chrome PLS to "normal", "eager", or "none".
    timeout_multiplier=None,  # Multiplies the default timeout values.
    js_checking_on=None,  # Check for JavaScript errors after page loads.
    slow=None,  # Slow down the automation. Faster than using Demo Mode.
    demo=None,  # Slow down and visually see test actions as they occur.
    demo_sleep=None,  # SECONDS (Set wait time after Slow & Demo Mode actions.)
    message_duration=None,  # SECONDS (The time length for Messenger alerts.)
    highlights=None,  # Number of highlight animations for Demo Mode actions.
    interval=None,  # SECONDS (Autoplay interval for SB Slides & Tour steps.)
    time_limit=None,  # SECONDS (Safely fail tests that exceed the time limit.)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/plugins/driver_manager.py
# Line: 67

def Driver(
    browser=None,  # Choose from "chrome", "edge", "firefox", or "safari".
    headless=None,  # Use the default headless mode for Chromium and Firefox.
    headless1=None,  # Use Chromium's old headless mode. (Fast, but limited)
    headless2=None,  # Use Chromium's new headless mode. (Has more features)
    headed=None,  # Run tests in headed/GUI mode on Linux, where not default.
    locale_code=None,  # Set the Language Locale Code for the web browser.
    protocol=None,  # The Selenium Grid protocol: "http" or "https".
    servername=None,  # The Selenium Grid server/IP used for tests.
    port=None,  # The Selenium Grid port used by the test server.
    proxy=None,  # Use proxy. Format: "SERVER:PORT" or "USER:PASS@SERVER:PORT".
    proxy_bypass_list=None,  # Skip proxy when using the listed domains.
    proxy_pac_url=None,  # Use PAC file. (Format: URL or USERNAME:PASSWORD@URL)
    multi_proxy=None,  # Allow multiple proxies with auth when multi-threaded.
    agent=None,  # Modify the web browser's User-Agent string.
    cap_file=None,  # The desired capabilities to use with a Selenium Grid.
    cap_string=None,  # The desired capabilities to use with a Selenium Grid.
    recorder_ext=None,  # Enables the SeleniumBase Recorder Chromium extension.
    disable_cookies=None,  # Disable Cookies on websites. (Pages might break!)
    disable_js=None,  # Disable JavaScript on websites. (Pages might break!)
    disable_csp=None,  # Disable the Content Security Policy of websites.
    enable_ws=None,  # Enable Web Security on Chromium-based browsers.
    disable_ws=None,  # Reverse of "enable_ws". (None and False are different)
    enable_sync=None,  # Enable "Chrome Sync" on websites.
    use_auto_ext=None,  # Use Chrome's automation extension.
    undetectable=None,  # Use undetected-chromedriver to evade bot-detection.
    uc_cdp_events=None,  # Capture CDP events in undetected-chromedriver mode.
    uc_subprocess=None,  # Use undetected-chromedriver as a subprocess.
    log_cdp_events=None,  # Capture {"performance": "ALL", "browser": "ALL"}
    no_sandbox=None,  # (DEPRECATED) - "--no-sandbox" is always used now.
    disable_gpu=None,  # (DEPRECATED) - GPU is disabled if not "swiftshader".
    incognito=None,  # Enable Chromium's Incognito mode.
    guest_mode=None,  # Enable Chromium's Guest mode.
    dark_mode=None,  # Enable Chromium's Dark mode.
    devtools=None,  # Open Chromium's DevTools when the browser opens.
    remote_debug=None,  # Enable Chrome's Debugger on "http://localhost:9222".
    enable_3d_apis=None,  # Enable WebGL and 3D APIs.
    swiftshader=None,  # Chrome: --use-gl=angle / --use-angle=swiftshader-webgl
    ad_block_on=None,  # Block some types of display ads from loading.
    host_resolver_rules=None,  # Set host-resolver-rules, comma-separated.
    block_images=None,  # Block images from loading during tests.
    do_not_track=None,  # Tell websites that you don't want to be tracked.
    chromium_arg=None,  # "ARG=N,ARG2" (Set Chromium args, ","-separated.)
    firefox_arg=None,  # "ARG=N,ARG2" (Set Firefox args, comma-separated.)
    firefox_pref=None,  # SET (Set Firefox PREFERENCE:VALUE set, ","-separated)
    user_data_dir=None,  # Set the Chrome user data directory to use.
    extension_zip=None,  # Load a Chrome Extension .zip|.crx, comma-separated.
    extension_dir=None,  # Load a Chrome Extension directory, comma-separated.
    disable_features=None,  # "F1,F2" (Disable Chrome features, ","-separated.)
    binary_location=None,  # Set path of the Chromium browser binary to use.
    driver_version=None,  # Set the chromedriver or uc_driver version to use.
    page_load_strategy=None,  # Set Chrome PLS to "normal", "eager", or "none".
    use_wire=None,  # Use selenium-wire's webdriver over selenium webdriver.
    external_pdf=None,  # Set Chrome "plugins.always_open_pdf_externally":True.
    window_position=None,  # Set the browser's starting window position: "X,Y"
    window_size=None,  # Set the browser's starting window size: "Width,Height"
    is_mobile=None,  # Use the mobile device emulator while running tests.
    mobile=None,  # Shortcut / Duplicate of "is_mobile".
    d_width=None,  # Set device width
    d_height=None,  # Set device height
    d_p_r=None,  # Set device pixel ratio
    position=None,  # Shortcut / Duplicate of "window_position".
    size=None,  # Shortcut / Duplicate of "window_size".
    uc=None,  # Shortcut / Duplicate of "undetectable".
    undetected=None,  # Shortcut / Duplicate of "undetectable".
    uc_cdp=None,  # Shortcut / Duplicate of "uc_cdp_events".
    uc_sub=None,  # Shortcut / Duplicate of "uc_subprocess".
    locale=None,  # Shortcut / Duplicate of "locale_code".
    log_cdp=None,  # Shortcut / Duplicate of "log_cdp_events".
    ad_block=None,  # Shortcut / Duplicate of "ad_block_on".
    server=None,  # Shortcut / Duplicate of "servername".
    guest=None,  # Shortcut / Duplicate of "guest_mode".
    wire=None,  # Shortcut / Duplicate of "use_wire".
    pls=None,  # Shortcut / Duplicate of "page_load_strategy".
    cft=None,  # Use "Chrome for Testing"
    chs=None,  # Use "Chrome-Headless-Shell"

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/browser_launcher.py
# Line: 394

def uc_special_open_if_cf(
    driver,
    url,
    proxy_string=None,
    mobile_emulator=None,
    device_width=None,
    device_height=None,
    device_pixel_ratio=None,

# ==================================================
# Line: 1935

def _add_chrome_proxy_extension(
    chrome_options,
    proxy_string,
    proxy_user,
    proxy_pass,
    proxy_scheme,
    proxy_bypass_list=None,
    zip_it=True,
    multi_proxy=False,

# ==================================================
# Line: 2079

def _set_chrome_options(
    browser_name,
    downloads_path,
    headless,
    locale_code,
    proxy_string,
    proxy_auth,
    proxy_user,
    proxy_pass,
    proxy_scheme,
    proxy_bypass_list,
    proxy_pac_url,
    multi_proxy,
    user_agent,
    recorder_ext,
    disable_cookies,
    disable_js,
    disable_csp,
    enable_ws,
    enable_sync,
    use_auto_ext,
    undetectable,
    uc_cdp_events,
    uc_subprocess,
    log_cdp_events,
    no_sandbox,
    disable_gpu,
    headless1,
    headless2,
    incognito,
    guest_mode,
    dark_mode,
    devtools,
    remote_debug,
    enable_3d_apis,
    swiftshader,
    ad_block_on,
    host_resolver_rules,
    block_images,
    do_not_track,
    chromium_arg,
    user_data_dir,
    extension_zip,
    extension_dir,
    disable_features,
    binary_location,
    driver_version,
    page_load_strategy,
    use_wire,
    external_pdf,
    servername,
    mobile_emulator,
    device_width,
    device_height,
    device_pixel_ratio,

# ==================================================
# Line: 2597

def _set_firefox_options(
    downloads_path,
    headless,
    locale_code,
    proxy_string,
    proxy_bypass_list,
    proxy_pac_url,
    user_agent,
    disable_cookies,
    disable_js,
    disable_csp,
    firefox_arg,
    firefox_pref,
    external_pdf,

# ==================================================
# Line: 2767

def get_driver(
    browser_name=None,
    headless=False,
    locale_code=None,
    use_grid=False,
    protocol="http",
    servername="localhost",
    port=4444,
    proxy_string=None,
    proxy_bypass_list=None,
    proxy_pac_url=None,
    multi_proxy=None,
    user_agent=None,
    cap_file=None,
    cap_string=None,
    recorder_ext=False,
    disable_cookies=False,
    disable_js=False,
    disable_csp=False,
    enable_ws=False,
    enable_sync=False,
    use_auto_ext=False,
    undetectable=False,
    uc_cdp_events=False,
    uc_subprocess=False,
    log_cdp_events=False,
    no_sandbox=False,
    disable_gpu=False,
    headless1=False,
    headless2=False,
    incognito=False,
    guest_mode=False,
    dark_mode=False,
    devtools=False,
    remote_debug=False,
    enable_3d_apis=False,
    swiftshader=False,
    ad_block_on=False,
    host_resolver_rules=None,
    block_images=False,
    do_not_track=False,
    chromium_arg=None,
    firefox_arg=None,
    firefox_pref=None,
    user_data_dir=None,
    extension_zip=None,
    extension_dir=None,
    disable_features=None,
    binary_location=None,
    driver_version=None,
    page_load_strategy=None,
    use_wire=False,
    external_pdf=False,
    test_id=None,
    mobile_emulator=False,
    device_width=None,
    device_height=None,
    device_pixel_ratio=None,
    browser=None,  # A duplicate of browser_name to avoid confusion

# ==================================================
# Line: 3259

def get_remote_driver(
    browser_name,
    headless,
    locale_code,
    protocol,
    servername,
    port,
    proxy_string,
    proxy_auth,
    proxy_user,
    proxy_pass,
    proxy_scheme,
    proxy_bypass_list,
    proxy_pac_url,
    multi_proxy,
    user_agent,
    cap_file,
    cap_string,
    recorder_ext,
    disable_cookies,
    disable_js,
    disable_csp,
    enable_ws,
    enable_sync,
    use_auto_ext,
    undetectable,
    uc_cdp_events,
    uc_subprocess,
    log_cdp_events,
    no_sandbox,
    disable_gpu,
    headless1,
    headless2,
    incognito,
    guest_mode,
    dark_mode,
    devtools,
    remote_debug,
    enable_3d_apis,
    swiftshader,
    ad_block_on,
    host_resolver_rules,
    block_images,
    do_not_track,
    chromium_arg,
    firefox_arg,
    firefox_pref,
    user_data_dir,
    extension_zip,
    extension_dir,
    disable_features,
    binary_location,
    driver_version,
    page_load_strategy,
    use_wire,
    external_pdf,
    test_id,
    mobile_emulator,
    device_width,
    device_height,
    device_pixel_ratio,

# ==================================================
# Line: 3701

def get_local_driver(
    browser_name,
    headless,
    locale_code,
    servername,
    proxy_string,
    proxy_auth,
    proxy_user,
    proxy_pass,
    proxy_scheme,
    proxy_bypass_list,
    proxy_pac_url,
    multi_proxy,
    user_agent,
    recorder_ext,
    disable_cookies,
    disable_js,
    disable_csp,
    enable_ws,
    enable_sync,
    use_auto_ext,
    undetectable,
    uc_cdp_events,
    uc_subprocess,
    log_cdp_events,
    no_sandbox,
    disable_gpu,
    headless1,
    headless2,
    incognito,
    guest_mode,
    dark_mode,
    devtools,
    remote_debug,
    enable_3d_apis,
    swiftshader,
    ad_block_on,
    host_resolver_rules,
    block_images,
    do_not_track,
    chromium_arg,
    firefox_arg,
    firefox_pref,
    user_data_dir,
    extension_zip,
    extension_dir,
    disable_features,
    binary_location,
    driver_version,
    page_load_strategy,
    use_wire,
    external_pdf,
    mobile_emulator,
    device_width,
    device_height,
    device_pixel_ratio,

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/sb_cdp.py
# Line: 1589

def __gui_drag_drop(self, x1, y1, x2, y2, timeframe=0.25, uc_lock=False):
    self.__install_pyautogui_if_missing()
    import pyautogui
    pyautogui = self.__get_configured_pyautogui(pyautogui)
    screen_width, screen_height = pyautogui.size()
    if x1 < 0 or y1 < 0 or x1 > screen_width or y1 > screen_height:
        raise Exception(
            "PyAutoGUI cannot drag-drop from point (%s, %s)"
            " outside screen. (Width: %s, Height: %s)"
            % (x1, y1, screen_width, screen_height)
        )
    if x2 < 0 or y2 < 0 or x2 > screen_width or y2 > screen_height:
        raise Exception(
            "PyAutoGUI cannot drag-drop to point (%s, %s)"
            " outside screen. (Width: %s, Height: %s)"
            % (x2, y2, screen_width, screen_height)
        )
    if uc_lock:
        gui_lock = fasteners.InterProcessLock(
            constants.MultiBrowser.PYAUTOGUILOCK
        )
        with gui_lock:  # Prevent issues with multiple processes
            pyautogui.moveTo(x1, y1, 0.25, pyautogui.easeOutQuad)
            self.__add_light_pause()
            if "--debug" in sys.argv:
                print(" <DEBUG> pyautogui.moveTo(%s, %s)" % (x1, y1))
            pyautogui.dragTo(x2, y2, button="left", duration=timeframe)
    else:
        # Called from a method where the gui_lock is already active
        pyautogui.moveTo(x1, y1, 0.25, pyautogui.easeOutQuad)
        self.__add_light_pause()
        if "--debug" in sys.argv:
            print(" <DEBUG> pyautogui.dragTo(%s, %s)" % (x2, y2))
        pyautogui.dragTo(x2, y2, button="left", duration=timeframe)


# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/fixtures/page_actions.py
# Line: 270

def hover_and_click(
    driver,
    hover_selector,
    click_selector,
    hover_by="css selector",
    click_by="css selector",
    timeout=settings.SMALL_TIMEOUT,
    js_click=False,

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/fixtures/base_case.py
# Line: 1943

def set_attribute(
    self,
    selector,
    attribute,
    value,
    by="css selector",
    timeout=None,
    scroll=False,

# ==================================================
# Line: 2447

def click_with_offset(
    self,
    selector,
    x,
    y,
    by="css selector",
    mark=None,
    timeout=None,
    center=None,

# ==================================================
# Line: 2474

def double_click_with_offset(
    self,
    selector,
    x,
    y,
    by="css selector",
    mark=None,
    timeout=None,
    center=None,

# ==================================================
# Line: 2710

def hover_and_click(
    self,
    hover_selector,
    click_selector,
    hover_by="css selector",
    click_by="css selector",
    timeout=None,
    js_click=False,

# ==================================================
# Line: 2923

def drag_and_drop(
    self,
    drag_selector,
    drop_selector,
    drag_by="css selector",
    drop_by="css selector",
    timeout=None,
    jquery=False,

# ==================================================
# Line: 3951

def get_new_driver(
    self,
    browser=None,
    headless=None,
    locale_code=None,
    protocol=None,
    servername=None,
    port=None,
    proxy=None,
    proxy_bypass_list=None,
    proxy_pac_url=None,
    multi_proxy=None,
    agent=None,
    switch_to=True,
    cap_file=None,
    cap_string=None,
    recorder_ext=None,
    disable_cookies=None,
    disable_js=None,
    disable_csp=None,
    enable_ws=None,
    enable_sync=None,
    use_auto_ext=None,
    undetectable=None,
    uc_cdp_events=None,
    uc_subprocess=None,
    log_cdp_events=None,
    no_sandbox=None,
    disable_gpu=None,
    headless1=None,
    headless2=None,
    incognito=None,
    guest_mode=None,
    dark_mode=None,
    devtools=None,
    remote_debug=None,
    enable_3d_apis=None,
    swiftshader=None,
    ad_block_on=None,
    host_resolver_rules=None,
    block_images=None,
    do_not_track=None,
    chromium_arg=None,
    firefox_arg=None,
    firefox_pref=None,
    user_data_dir=None,
    extension_zip=None,
    extension_dir=None,
    disable_features=None,
    binary_location=None,
    driver_version=None,
    page_load_strategy=None,
    use_wire=None,
    external_pdf=None,
    is_mobile=None,
    d_width=None,
    d_height=None,
    d_p_r=None,
    **kwargs,

# ==================================================
# Line: 5976

def highlight_update_text(
    self,
    selector,
    text,
    by="css selector",
    loops=3,
    scroll=True,
    timeout=None,

# ==================================================
# Line: 5994

def highlight_type(
    self,
    selector,
    text,
    by="css selector",
    loops=3,
    scroll=True,
    timeout=None,

# ==================================================
# Line: 7095

def get_pdf_text(
    self,
    pdf,
    page=None,
    maxpages=None,
    password=None,
    codec="utf-8",
    wrap=False,
    nav=False,
    override=False,
    caching=True,

# ==================================================
# Line: 7207

def assert_pdf_text(
    self,
    pdf,
    text,
    page=None,
    maxpages=None,
    password=None,
    codec="utf-8",
    wrap=True,
    nav=False,
    override=False,
    caching=True,

# ==================================================
# Line: 11348

def deferred_check_window(
    self,
    name="default",
    level=0,
    baseline=False,
    check_domain=True,
    full_diff=False,
    fs=False,

# ==================================================
# Line: 11456

def delayed_check_window(
    self,
    name="default",
    level=0,
    baseline=False,
    check_domain=True,
    full_diff=False,
    fs=False,

# ==================================================
# Line: 11585

def add_slide(
    self,
    content=None,
    image=None,
    code=None,
    iframe=None,
    content2=None,
    notes=None,
    transition=None,
    name=None,

# ==================================================
# Line: 11837

def create_pie_chart(
    self,
    chart_name=None,
    title=None,
    subtitle=None,
    data_name=None,
    unit=None,
    libs=True,
    labels=True,
    legend=True,

# ==================================================
# Line: 11881

def create_bar_chart(
    self,
    chart_name=None,
    title=None,
    subtitle=None,
    data_name=None,
    unit=None,
    libs=True,
    labels=True,
    legend=True,

# ==================================================
# Line: 11925

def create_column_chart(
    self,
    chart_name=None,
    title=None,
    subtitle=None,
    data_name=None,
    unit=None,
    libs=True,
    labels=True,
    legend=True,

# ==================================================
# Line: 11969

def create_line_chart(
    self,
    chart_name=None,
    title=None,
    subtitle=None,
    data_name=None,
    unit=None,
    zero=False,
    libs=True,
    labels=True,
    legend=True,

# ==================================================
# Line: 12016

def create_area_chart(
    self,
    chart_name=None,
    title=None,
    subtitle=None,
    data_name=None,
    unit=None,
    zero=False,
    libs=True,
    labels=True,
    legend=True,

# ==================================================
# Line: 12063

def __create_highchart(
    self,
    chart_name=None,
    title=None,
    subtitle=None,
    style=None,
    data_name=None,
    unit=None,
    zero=False,
    libs=True,
    labels=True,
    legend=True,

# ==================================================
# Line: 12787

def add_tour_step(
    self,
    message,
    selector=None,
    name=None,
    title=None,
    theme=None,
    alignment=None,
    duration=None,

# ==================================================
# Line: 12885

def __add_shepherd_tour_step(
    self,
    message,
    selector=None,
    name=None,
    title=None,
    theme=None,
    alignment=None,

# ==================================================
# Line: 12948

def __add_bootstrap_tour_step(
    self,
    message,
    selector=None,
    name=None,
    title=None,
    alignment=None,
    duration=None,

# ==================================================
# Line: 13614

def __click_with_offset(
    self,
    selector,
    x,
    y,
    by="css selector",
    double=False,
    mark=None,
    timeout=None,
    center=None,

# ==================================================
