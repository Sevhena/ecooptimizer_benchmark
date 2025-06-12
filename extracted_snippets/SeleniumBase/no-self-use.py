# no-self-use snippets for SeleniumBase

# File: /root/ecooptimizer/SeleniumBase/seleniumbase/undetected/cdp_driver/connection.py
# Line: 382

async def set_auth(self, username, password, tab):
    async def auth_challenge_handler(event: cdp.fetch.AuthRequired):
        await tab.send(
            cdp.fetch.continue_with_auth(
                request_id=event.request_id,
                auth_challenge_response=cdp.fetch.AuthChallengeResponse(
                    response="ProvideCredentials",
                    username=username,
                    password=password,
                ),
            )
        )

    async def req_paused(event: cdp.fetch.RequestPaused):
        await tab.send(
            cdp.fetch.continue_request(request_id=event.request_id)
        )

    tab.add_handler(
        cdp.fetch.RequestPaused,
        lambda event: asyncio.create_task(req_paused(event)),
    )

    tab.add_handler(
        cdp.fetch.AuthRequired,
        lambda event: asyncio.create_task(auth_challenge_handler(event)),
    )

    await tab.send(cdp.fetch.enable(handle_auth_requests=True))


# ==================================================
# Line: 529

async def _prepare_headless(self):
    return  # (This functionality has moved to a new location!)


# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/masterqa/master_qa.py
# Line: 72

def __get_timestamp(self):
    return str(int(time.time() * 1000))


# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/plugins/selenium_plugin.py
# Line: 1388

def finalize(self, result):
    """This runs after all tests have completed with nosetests."""
    if (
        (hasattr(sb_config, "multi_proxy") and not sb_config.multi_proxy)
        or not hasattr(sb_config, "multi_proxy")
    ):
        proxy_helper.remove_proxy_zip_if_present()


# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/plugins/base_plugin.py
# Line: 356

def handleError(self, test, err, capt=None):
    """After each test error, record testcase run information.
    "Error" also encompasses any states other than Pass or Fail."""
    from nose.exc import SkipTest
    from seleniumbase.fixtures import errors

    if not hasattr(test.test, "testcase_guid"):
        if err[0] == errors.BlockedTest:
            raise SkipTest(err[1])
        elif err[0] == errors.DeprecatedTest:
            raise SkipTest(err[1])
        elif err[0] == errors.SkipTest:
            raise SkipTest(err[1])

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/sb_driver.py
# Line: 189

def is_valid_url(self, url):
    """Return True if the url is a valid url."""
    return page_utils.is_valid_url(url)


# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/s3_manager.py
# Line: 91

def save_uploaded_file_names(self, files):
    """Keep a record of all file names that have been uploaded.
    Upload log files related to each test after its execution.
    Once done, use already_uploaded_files to create an index file."""
    global already_uploaded_files  # noqa
    already_uploaded_files.extend(files)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/sb_cdp.py
# Line: 29

def __slow_mode_pause_if_set(self):
    if (
        (hasattr(sb_config, "demo_mode") and sb_config.demo_mode)
        or "--demo" in sys.argv
    ):
        time.sleep(0.48)
    elif (
        (hasattr(sb_config, "slow_mode") and sb_config.slow_mode)
        or "--slow" in sys.argv
    ):
        time.sleep(0.24)


# ==================================================
# Occurrences: Lines 41-44 (2 instances)

def __add_light_pause(self):
    time.sleep(0.007)


# ==================================================
# Line: 585

def __type(self, element, text):
    with suppress(Exception):
        element.clear_input()
    element.send_keys(text)


# ==================================================
# Line: 605

def __get_attribute(self, element, attribute):
    try:
        return element.get_js_attributes()[attribute]
    except Exception:
        if not attribute:
            raise
        try:
            attribute_str = element.get_js_attributes()
            locate = ' %s="' % attribute
            if locate in attribute_str.outerHTML:
                outer_html = attribute_str.outerHTML
                attr_start = outer_html.find(locate) + len(locate)
                attr_end = outer_html.find('"', attr_start)
                value = outer_html[attr_start:attr_end]
                return value
        except Exception:
            pass
    return None


# ==================================================
# Line: 688

def sleep(self, seconds):
    time.sleep(seconds)


# ==================================================
# Line: 1370

def __make_sure_pyautogui_lock_is_writable(self):
    with suppress(Exception):
        shared_utils.make_writable(constants.MultiBrowser.PYAUTOGUILOCK)


# ==================================================
# Line: 1447

def __get_configured_pyautogui(self, pyautogui_copy):
    if (
        shared_utils.is_linux()
        and hasattr(pyautogui_copy, "_pyautogui_x11")
        and "DISPLAY" in os.environ.keys()
    ):
        if (
            hasattr(sb_config, "_pyautogui_x11_display")
            and sb_config._pyautogui_x11_display
            and hasattr(pyautogui_copy._pyautogui_x11, "_display")
            and (
                sb_config._pyautogui_x11_display
                == pyautogui_copy._pyautogui_x11._display
            )
        ):
            pass
        else:
            import Xlib.display
            pyautogui_copy._pyautogui_x11._display = (
                Xlib.display.Display(os.environ['DISPLAY'])
            )
            sb_config._pyautogui_x11_display = (
                pyautogui_copy._pyautogui_x11._display
            )
    return pyautogui_copy


# ==================================================
# Occurrences: Lines 2138-2158 (6 instances)

def assert_true(self, expression):
    if not expression:
        raise AssertionError("%s is not true" % expression)


# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/fixtures/css_to_xpath.py
# Line: 45

def xpath_descendant_combinator(self, left, right):
    """right is a child, grand-child or further descendant of left"""
    return left.join("//", right)



# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/fixtures/base_case.py
# Line: 4631

def delete_saved_cookies(self, name="cookies.txt"):
    """Deletes the cookies file from the "saved_cookies" folder.
    Does NOT delete the cookies from the web browser."""
    if name.endswith("/"):
        raise Exception("Invalid filename for Cookies!")
    if "/" in name:
        name = name.split("/")[-1]
    if len(name) < 1:
        raise Exception("Filename for Cookies is too short!")
    if not name.endswith(".txt"):
        name = name + ".txt"
    folder = constants.SavedCookies.STORAGE_FOLDER
    abs_path = os.path.abspath(".")
    file_path = os.path.join(abs_path, folder)
    cookies_file_path = os.path.join(file_path, name)
    if os.path.exists(cookies_file_path):
        if cookies_file_path.endswith(".txt"):
            os.remove(cookies_file_path)


# ==================================================
# Line: 4650

def get_saved_cookies(self, name="cookies.txt"):
    """Gets the page cookies from the "saved_cookies" folder."""
    if name.endswith("/"):
        raise Exception("Invalid filename for Cookies!")
    if "/" in name:
        name = name.split("/")[-1]
    if "\\" in name:
        name = name.split("\\")[-1]
    if len(name) < 1:
        raise Exception("Filename for Cookies is too short!")
    if not name.endswith(".txt"):
        name = name + ".txt"
    folder = constants.SavedCookies.STORAGE_FOLDER
    abs_path = os.path.abspath(".")
    file_path = os.path.join(abs_path, folder)
    cookies_file_path = os.path.join(file_path, name)
    json_cookies = None
    with open(cookies_file_path, "r") as f:
        json_cookies = f.read().strip()
    return json.loads(json_cookies)


# ==================================================
# Line: 7060

def __fix_unicode_conversion(self, text):
    """Fixing Chinese characters when converting from PDF to HTML."""
    text = text.replace("\u2f8f", "\u884c")
    text = text.replace("\u2f45", "\u65b9")
    text = text.replace("\u2f08", "\u4eba")
    text = text.replace("\u2f70", "\u793a")
    text = text.replace("\xe2\xbe\x8f", "\xe8\xa1\x8c")
    text = text.replace("\xe2\xbd\xb0", "\xe7\xa4\xba")
    text = text.replace("\xe2\xbe\x8f", "\xe8\xa1\x8c")
    text = text.replace("\xe2\xbd\x85", "\xe6\x96\xb9")
    return text


# ==================================================
# Line: 7072

def __get_type_checked_text(self, text):
    """Do type-checking on text. Then return it when valid.
    If the text is acceptable, return the text or str(text).
    If the text is not acceptable, raise a Python Exception."""
    if isinstance(text, str):
        return text
    elif isinstance(text, (int, float)):
        return str(text)  # Convert num to string
    elif isinstance(text, bool):
        raise Exception("text must be a string! Boolean found!")
    elif type(text).__name__ == "NoneType":
        raise Exception("text must be a string! NoneType found!")
    elif isinstance(text, list):
        raise Exception("text must be a string! List found!")
    elif isinstance(text, tuple):
        raise Exception("text must be a string! Tuple found!")
    elif isinstance(text, set):
        raise Exception("text must be a string! Set found!")
    elif isinstance(text, dict):
        raise Exception("text must be a string! Dict found!")
    else:
        return str(text)


# ==================================================
# Line: 7270

def create_folder(self, folder):
    """Creates a folder of the given name if it doesn't already exist."""
    if folder.endswith("/"):
        folder = folder[:-1]
    if len(folder) < 1:
        raise Exception("Minimum folder name length = 1.")
    if not os.path.exists(folder):
        with suppress(Exception):
            os.makedirs(folder)


# ==================================================
# Line: 7453

def save_file_as(self, file_url, new_file_name, destination_folder=None):
    """Similar to self.download_file(), except that you get to rename the
    file being downloaded to whatever you want."""
    download_file_lock = fasteners.InterProcessLock(
        constants.MultiBrowser.DOWNLOAD_FILE_LOCK
    )
    with download_file_lock:
        with suppress(Exception):
            shared_utils.make_writable(
                constants.MultiBrowser.DOWNLOAD_FILE_LOCK
            )
        if not destination_folder:
            destination_folder = constants.Files.DOWNLOADS_FOLDER
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
    page_utils._download_file_to(
        file_url, destination_folder, new_file_name
    )


# ==================================================
# Line: 7472

def save_data_as(self, data, file_name, destination_folder=None):
    """Saves the data specified to the file specified.
    If no destination folder is specified, the default one is used.
    (The default folder = "./downloaded_files")
    Use "." as the destination folder for the current directory."""
    if not destination_folder:
        destination_folder = constants.Files.DOWNLOADS_FOLDER
    page_utils._save_data_as(data, destination_folder, file_name)


# ==================================================
# Line: 7481

def append_data_to_file(self, data, file_name, destination_folder=None):
    """Appends the data specified to the file specified.
    If no destination folder is specified, the default one is used.
    (The default folder = "./downloaded_files")
    Use "." as the folder for the current directory."""
    if not destination_folder:
        destination_folder = constants.Files.DOWNLOADS_FOLDER
    page_utils._append_data_to_file(data, destination_folder, file_name)


# ==================================================
# Line: 7490

def get_file_data(self, file_name, folder=None):
    """Gets the data from the file specified.
    If no folder is specified, the default one is used.
    The default folder = "./downloaded_files"
    For the "latest_logs/" test data folders, use:
        self.data_path OR self.data_abspath
    Use "." as the folder for the current directory."""
    if not folder:
        folder = constants.Files.DOWNLOADS_FOLDER
    return page_utils._get_file_data(folder, file_name)


# ==================================================
# Line: 8247

def is_valid_url(self, url):
    """Return True if the url is a valid url."""
    return page_utils.is_valid_url(url)


# ==================================================
# Line: 8352

def get_mfa_code(self, totp_key=None):
    """Same as get_totp_code() and get_google_auth_password().
    Returns a time-based one-time password based on the
    Google Authenticator algorithm for multi-factor authentication.
    If the "totp_key" is not specified, this method defaults
    to using the one provided in [seleniumbase/config/settings.py].
    Google Authenticator codes expire & change at 30-sec intervals.
    If the fetched password expires in the next 1.2 seconds, waits
    for a new one before returning it (may take up to 1.2 seconds).
    See https://pyotp.readthedocs.io/en/latest/ for details."""
    import pyotp

    if not totp_key:
        totp_key = settings.TOTP_KEY

    epoch_interval = time.time() / 30.0
    cycle_lifespan = float(epoch_interval) - int(epoch_interval)
    if float(cycle_lifespan) > 0.96:
        # Password expires in the next 1.2 seconds. Wait for a new one.
        for i in range(30):
            time.sleep(0.04)
            epoch_interval = time.time() / 30.0
            cycle_lifespan = float(epoch_interval) - int(epoch_interval)
            if not float(cycle_lifespan) > 0.96:
                # The new password cycle has begun
                break

    totp = pyotp.TOTP(totp_key)
    return str(totp.now())


# ==================================================
# Occurrences: Lines 8411-8417 (3 instances)

def convert_css_to_xpath(self, css):
    return css_to_xpath.convert_css_to_xpath(css)


# ==================================================
# Line: 9308

def _print(self, msg):
    """Same as Python's print(), but also prints during multithreaded runs.
    Normally, Python's print() command won't print for multithreaded tests.
    Here's an example of running tests using multithreading: "pytest -n=4".
    Here's how to print directly from sys without using a print() command:
    To force a print during multithreaded tests, use: "sys.stderr.write()".
    To print without the new-line character end, use: "sys.stdout.write()".
    """
    if hasattr(sb_config, "_multithreaded") and sb_config._multithreaded:
        if not isinstance(msg, str):
            with suppress(Exception):
                msg = str(msg)
        sys.stderr.write(msg + "\n")
    else:
        print(msg)


# ==================================================
# Line: 11134

def __get_exception_message(self):
    """This method extracts the message from an exception if there
    was an exception that occurred during the test, assuming
    that the exception was in a try/except block and not thrown."""
    exception_info = sys.exc_info()[1]
    if hasattr(exception_info, "msg"):
        exc_message = exception_info.msg
    elif hasattr(exception_info, "message"):
        exc_message = exception_info.message
    elif hasattr(exception_info, "args") and len(exception_info.args) == 1:
        exc_message = exception_info.args[0]
    else:
        exc_message = sys.exc_info()
    return exc_message


# ==================================================
# Line: 12756

def set_introjs_colors(self, theme_color=None, hover_color=None):
    """Use this method to set the theme colors for IntroJS tours.
    Args must be hex color values that start with a "#" sign.
    If a color isn't specified, the color will reset to the default.
    The border color of buttons is set to the hover color.
    @Params
    theme_color - The color of buttons.
    hover_color - The color of buttons after hovering over them."""
    if not hasattr(sb_config, "introjs_theme_color"):
        sb_config.introjs_theme_color = constants.TourColor.theme_color
    if not hasattr(sb_config, "introjs_hover_color"):
        sb_config.introjs_hover_color = constants.TourColor.hover_color
    if theme_color:
        match = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", theme_color)
        if not match:
            raise Exception(
                'Expecting a hex value color that starts with "#"!'
            )
        sb_config.introjs_theme_color = theme_color
    else:
        sb_config.introjs_theme_color = constants.TourColor.theme_color
    if hover_color:
        match = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", hover_color)
        if not match:
            raise Exception(
                'Expecting a hex value color that starts with "#"!'
            )
        sb_config.introjs_hover_color = hover_color
    else:
        sb_config.introjs_hover_color = constants.TourColor.hover_color


# ==================================================
# Occurrences: Lines 13493-13496 (2 instances)

def __are_quotes_escaped(self, string):
    return js_utils.are_quotes_escaped(string)


# ==================================================
# Line: 13906

def __recalculate_selector(self, selector, by, xp_ok=True):
    """Use autodetection to return the correct selector with "by" updated.
    If "xp_ok" is False, don't call convert_css_to_xpath(), which is
    used to make the ":contains()" selector valid outside of JS calls.
    Returns a (selector, by) tuple."""
    return page_utils.recalculate_selector(selector, by, xp_ok=xp_ok)


# ==================================================
# Occurrences: Lines 13913-13916 (2 instances)

def __looks_like_a_page_url(self, url):
    return page_utils.looks_like_a_page_url(url)


# ==================================================
# Line: 14277

def jq_format(self, code):
    # DEPRECATED - re.escape() already performs this action.
    return js_utils._jq_format(code)


# ==================================================
# Line: 14440

def __fail_if_invalid_shadow_selector_usage(self, selector):
    if selector.strip().endswith("::shadow"):
        msg = (
            "A Shadow DOM selector cannot end on a shadow root element!"
            " End the selector with an element inside the shadow root!"
        )
        raise Exception(msg)


# ==================================================
# Line: 15822

def __create_log_path_as_needed(self, test_logpath):
    if not os.path.exists(test_logpath):
        try:
            os.makedirs(test_logpath)
        except Exception:
            pass  # Only reachable during multi-threaded runs


# ==================================================
# Line: 16199

def __activate_behave_post_mortem_debug_mode(self):
    """Activate Post Mortem Debug Mode for failing tests that use Behave"""
    import pdb

    pdb.post_mortem(sb_config.behave_step.exc_traceback)
    # Post Mortem Debug Mode ("behave -D pdb")


# ==================================================
# Line: 16206

def __activate_sb_mgr_post_mortem_debug_mode(self):
    """Activate Post Mortem Debug Mode for failing tests that use SB Mgr"""
    import pdb

    pdb.post_mortem()
    # Post Mortem Debug Mode ("python --pdb")


# ==================================================
# Line: 16213

def __activate_debug_mode_in_teardown(self):
    """Activate Final Trace / Debug Mode"""
    import pdb

    pdb.set_trace()
    # Final Trace ("--ftrace")


# ==================================================
# Line: 16323

def _get_rec_shift_esc_script(self):
    return (
        """document.onkeydown = function(evt) {
            evt = evt || window.event;
            var isEscape = false;
            if ("key" in evt) {
                isEscape = (evt.key === "Escape" || evt.key === "Esc");
                last_key = evt.key;
            } else {
                isEscape = (evt.keyCode === 27);
                last_key = evt.keyCode;
                if (last_key === 16) {
                    last_key = "Shift";
                }
            }
            if (isEscape && document.sb_last_key === "Shift") {
                document.sb_esc_end = "yes";
            }
            document.sb_last_key = last_key;
        };"""
    )


# ==================================================
