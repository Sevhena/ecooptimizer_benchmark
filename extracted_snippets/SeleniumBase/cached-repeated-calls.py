# cached-repeated-calls snippets for SeleniumBase

# File: /root/ecooptimizer/SeleniumBase/seleniumbase/undetected/__init__.py
# Line: 121

uc_lock = fasteners.InterProcessLock(
    constants.MultiBrowser.DRIVER_FIXING_LOCK
)

# ==================================================
# Line: 278

uc_lock = fasteners.InterProcessLock(
    constants.MultiBrowser.DRIVER_FIXING_LOCK
)

# ==================================================
# Occurrences: Lines 348-351 (2 instances)

return super().__getattribute__(item)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/undetected/cdp_driver/cdp_util.py
# Occurrences: Lines 169-172 (2 instances)

extension_dir, os.path.realpath(dir_path)

# ==================================================
# Line: 208

proxy_dir_lock = fasteners.InterProcessLock(PROXY_DIR_LOCK)

# ==================================================
# Line: 224

proxy_dir_lock = fasteners.InterProcessLock(PROXY_DIR_LOCK)

# ==================================================
# Occurrences: Lines 446-450 (2 instances)

binary_location = binary_location.strip()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/undetected/cdp.py
# Occurrences: Lines 53-56 (2 instances)

self._session = requests.Session()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/undetected/patcher.py
# Occurrences: Lines 296-298 (2 instances)

t = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/behave/behave_sb.py
# Occurrences: Lines 275-275 (2 instances)

browser = userdata[key].lower()

# ==================================================
# Occurrences: Lines 343-343 (2 instances)

protocol = userdata[key].lower()

# ==================================================
# Occurrences: Lines 420-420 (2 instances)

environment = userdata[key].lower()

# ==================================================
# Occurrences: Lines 501-501 (2 instances)

page_load_strategy = userdata[key].lower()

# ==================================================
# Occurrences: Lines 519-519 (2 instances)

database_env = userdata[key].lower()

# ==================================================
# Line: 1205

existing_pytest_style = f.read()

# ==================================================
# Line: 1217

existing_live_js = f.read()

# ==================================================
# Line: 1295

the_html_d = f.read()

# ==================================================
# Line: 1306

dash_pie = f.read().strip()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/behave/behave_helper.py
# Occurrences: Lines 12-12 (2 instances)

action[2] = unquote(action[2], errors="strict")

# ==================================================
# Occurrences: Lines 26-26 (2 instances)

action[2] = unquote(action[2], errors="strict")

# ==================================================
# Occurrences: Lines 85-85 (2 instances)

text = action[2].replace("\n", "\\n")

# ==================================================
# Occurrences: Lines 95-95 (2 instances)

text = action[2].replace("\n", "\\n")

# ==================================================
# Occurrences: Lines 105-105 (2 instances)

text = action[2].replace("\n", "\\n")

# ==================================================
# Occurrences: Lines 123-123 (2 instances)

text = action[2].replace("\n", "\\n")

# ==================================================
# Occurrences: Lines 146-146 (2 instances)

text = action[2].replace("\n", "\\n")

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_mkchart.py
# Line: 87

elif os.path.exists(os.getcwd() + "/" + file_name):

# ==================================================
# Line: 130

dir_name = os.getcwd()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/run.py
# Occurrences: Lines 110-114 (5 instances)

sc = sc.replace("seleniumbase", c1 + "selenium" + c2 + "base" + cr)

# ==================================================
# Occurrences: Lines 122-126 (5 instances)

sc = sc.replace("seleniumbase", c1 + "selenium" + c2 + "base" + cr)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_objectify.py
# Occurrences: Lines 168-169 (4 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 177-178 (4 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 253-260 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 270-271 (4 instances)

selector1 = optimize_selector(selector1)

# ==================================================
# Occurrences: Lines 320-327 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 337-338 (4 instances)

selector1 = optimize_selector(selector1)

# ==================================================
# Occurrences: Lines 387-393 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 404-404 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 446-451 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 461-461 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 501-505 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 514-514 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 552-557 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 567-567 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 607-612 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 622-622 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 662-666 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 675-675 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 713-717 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 726-726 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 764-769 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 779-779 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 819-824 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 834-834 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 874-879 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 889-889 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 929-934 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 944-944 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 984-988 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 997-997 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1035-1039 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1048-1048 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1086-1090 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1099-1099 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1137-1141 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1150-1150 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1188-1192 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1201-1201 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1239-1243 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1252-1252 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1290-1295 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1305-1305 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1345-1350 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1360-1360 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1400-1405 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1415-1415 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1455-1460 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1470-1470 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1510-1515 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1525-1525 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1565-1570 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1580-1580 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1620-1625 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1635-1635 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1675-1680 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1690-1690 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1730-1735 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1745-1745 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1785-1790 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1800-1800 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1840-1845 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1855-1855 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1895-1901 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1912-1912 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 1954-1959 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 1969-1969 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2009-2014 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2024-2024 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2064-2069 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2079-2079 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2119-2124 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2138-2138 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2182-2187 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2197-2197 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2237-2242 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2252-2252 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2292-2297 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2307-2307 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2347-2353 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2364-2364 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2406-2411 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2421-2421 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2461-2466 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2476-2476 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2516-2522 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2533-2533 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2576-2582 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2593-2593 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2636-2642 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2653-2653 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2695-2701 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2712-2712 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2754-2759 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2769-2769 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2809-2814 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2824-2824 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2864-2870 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2881-2881 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2923-2929 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2940-2940 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Occurrences: Lines 2982-2988 (12 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 2999-2999 (2 instances)

selector = optimize_selector(selector)

# ==================================================
# Line: 3102

var_names, existing_selectors, selector_list_dict = scan_objects_file()

# ==================================================
# Line: 3133

aa, bb, cc = scan_objects_file()

# ==================================================
# Line: 3148

token = line.split(p_o_import)[1].strip()

# ==================================================
# Line: 3176

token = line.split(p_o_import)[1].strip()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_caseplans.py
# Line: 367

root = tk.Tk()

# ==================================================
# Line: 481

decoy = tk.Tk()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_install.py
# Occurrences: Lines 211-212 (2 instances)

sb_config.cft_lkgv_json = req.json()

# ==================================================
# Line: 368

uv_low = use_version.lower()

# ==================================================
# Line: 378

use_version = get_latest_dev_chromedriver_version()

# ==================================================
# Line: 393

use_version = use_version.lower()

# ==================================================
# Occurrences: Lines 402-412 (6 instances)

use_version = get_latest_stable_chromedriver_version()

# ==================================================
# Occurrences: Lines 430-446 (9 instances)

use_version = get_latest_stable_chromedriver_version()

# ==================================================
# Occurrences: Lines 452-460 (3 instances)

url_req = requests_get(last)

# ==================================================
# Occurrences: Lines 518-535 (7 instances)

url_req = requests_get(last)

# ==================================================
# Line: 589

found_version = get_latest_stable_chromedriver_version()

# ==================================================
# Occurrences: Lines 596-609 (6 instances)

found_version = get_latest_stable_chromedriver_version()

# ==================================================
# Line: 653

found_version = get_latest_stable_chromedriver_version()

# ==================================================
# Occurrences: Lines 660-673 (6 instances)

found_version = get_latest_stable_chromedriver_version()

# ==================================================
# Occurrences: Lines 705-710 (2 instances)

if use_version.lower() == "latest":

# ==================================================
# Line: 751

url_request = requests_get(download_url)

# ==================================================
# Line: 801

if use_version.lower() == "latest":

# ==================================================
# Line: 826

if IS_ARM_MAC and int(use_version.split(".")[0]) > 104:

# ==================================================
# Line: 845

int(use_version.split(".")[0]) == 115

# ==================================================
# Line: 855

url_request = requests_get_with_retry(download_url)

# ==================================================
# Line: 887

url_request = requests_get_with_retry(headless_ie_url)

# ==================================================
# Occurrences: Lines 914-920 (3 instances)

remote_file = requests_get_with_retry(headless_ie_url)

# ==================================================
# Occurrences: Lines 946-947 (2 instances)

str_name = str(f_name)

# ==================================================
# Line: 960

shutil.copy3(driver_path, os.path.join(downloads_folder, filename))

# ==================================================
# Line: 979

driver_path = os.path.join(downloads_folder, filename)

# ==================================================
# Line: 992

remote_file = requests_get_with_retry(download_url)

# ==================================================
# Occurrences: Lines 999-1000 (2 instances)

zip_ref = zipfile.ZipFile(zip_file_path, "r")

# ==================================================
# Occurrences: Lines 1016-1016 (2 instances)

new_file = os.path.join(downloads_folder, str(f_name))

# ==================================================
# Line: 1047

zipinfos = zip_ref.infolist()

# ==================================================
# Occurrences: Lines 1055-1059 (2 instances)

contents = zip_ref.namelist()

# ==================================================
# Line: 1074

contents = zip_ref.namelist()

# ==================================================
# Occurrences: Lines 1088-1088 (2 instances)

new_file = os.path.join(downloads_folder, str(f_name))

# ==================================================
# Occurrences: Lines 1145-1146 (2 instances)

str_name = str(f_name)

# ==================================================
# Occurrences: Lines 1203-1205 (2 instances)

base_path = os.sep.join(zip_file_path.split(os.sep)[:-1])

# ==================================================
# Occurrences: Lines 1245-1247 (2 instances)

base_path = os.sep.join(zip_file_path.split(os.sep)[:-1])

# ==================================================
# Occurrences: Lines 1294-1294 (2 instances)

new_file = os.path.join(downloads_folder, str(f_name))

# ==================================================
# Occurrences: Lines 1307-1307 (2 instances)

new_file = os.path.join(downloads_folder, str(f_name))

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_behave_gui.py
# Occurrences: Lines 158-163 (7 instances)

if str(error).startswith("b'") and str(error).endswith("\\n'"):

# ==================================================
# Line: 170

root = tk.Tk()

# ==================================================
# Line: 185

brx = tk.StringVar(root)

# ==================================================
# Occurrences: Lines 197-202 (2 instances)

rsx = tk.StringVar(root)

# ==================================================
# Line: 208

dmx = tk.IntVar()

# ==================================================
# Line: 214

mmx = tk.IntVar()

# ==================================================
# Line: 220

dbx = tk.IntVar()

# ==================================================
# Line: 227

hbx = tk.IntVar()

# ==================================================
# Line: 233

ssx = tk.IntVar()

# ==================================================
# Line: 260

ara[count] = tk.IntVar()

# ==================================================
# Line: 344

decoy = tk.Tk()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_commander.py
# Line: 173

root = tk.Tk()

# ==================================================
# Line: 188

brx = tk.StringVar(root)

# ==================================================
# Line: 200

rsx = tk.StringVar(root)

# ==================================================
# Occurrences: Lines 220-225 (2 instances)

ntx = tk.StringVar(root)

# ==================================================
# Line: 232

dmx = tk.IntVar()

# ==================================================
# Line: 238

mmx = tk.IntVar()

# ==================================================
# Line: 244

dbx = tk.IntVar()

# ==================================================
# Line: 251

hrx = tk.IntVar()

# ==================================================
# Line: 258

hbx = tk.IntVar()

# ==================================================
# Line: 264

ssx = tk.IntVar()

# ==================================================
# Line: 295

ara[count] = tk.IntVar()

# ==================================================
# Line: 383

decoy = tk.Tk()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_mkdir.py
# Line: 117

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 155

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 172

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 179

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 315

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 327

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 371

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 464

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 503

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 513

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 548

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 557

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 573

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 597

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 617

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 627

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 660

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 678

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 710

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 737

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 764

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_print.py
# Line: 144

the_code = "\n".join(code_lines)

# ==================================================
# Line: 165

line_length = get_width(line)  # Special characters count 2X

# ==================================================
# Occurrences: Lines 246-246 (2 instances)

slash_one = line2b.find("/")

# ==================================================
# Occurrences: Lines 283-283 (2 instances)

slash_one = line2b.find("/")

# ==================================================
# Occurrences: Lines 410-410 (2 instances)

slash_one = line2.find("/")

# ==================================================
# Occurrences: Lines 429-429 (2 instances)

slash_one = line2.find("/")

# ==================================================
# Occurrences: Lines 563-567 (2 instances)

the_code = "\n".join(code_lines)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_recorder.py
# Line: 82

poll = sb_config.rec_subprocess_p.poll()

# ==================================================
# Line: 88

poll = sb_config.rec_subprocess_p.poll()

# ==================================================
# Line: 159

poll = sb_config.rec_subprocess_p.poll()

# ==================================================
# Line: 214

window = tk.Tk()

# ==================================================
# Occurrences: Lines 225-229 (2 instances)

cbx = tk.IntVar()

# ==================================================
# Line: 287

decoy = tk.Tk()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_mkpres.py
# Line: 87

elif os.path.exists(os.getcwd() + "/" + file_name):

# ==================================================
# Line: 130

dir_name = os.getcwd()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_mkrec.py
# Line: 290

recordings_dir = os.path.join(dir_name, "recordings")

# ==================================================
# Line: 307

recordings_dir = os.path.join(dir_name, "recordings")

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_mkfile.py
# Line: 126

elif os.path.exists(os.getcwd() + "/" + file_name):

# ==================================================
# Line: 204

dir_name = os.getcwd()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/translate/translator.py
# Occurrences: Lines 125-125 (2 instances)

comments = "%s" % data.group(1)

# ==================================================
# Occurrences: Lines 144-144 (2 instances)

comments = "%s" % data.group(1)

# ==================================================
# Occurrences: Lines 172-172 (2 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 181-181 (2 instances)

new_parent = MD_F.get_lang_parent_class(new_lang)

# ==================================================
# Occurrences: Lines 229-229 (2 instances)

new_basecase = MD_F.get_lang_parent_class(new_lang)

# ==================================================
# Line: 566

python_code = "\n".join(seleniumbase_lines)

# ==================================================
# Occurrences: Lines 668-668 (2 instances)

slash_one = line2b.find("/")

# ==================================================
# Occurrences: Lines 704-704 (2 instances)

slash_one = line2b.find("/")

# ==================================================
# Occurrences: Lines 830-830 (2 instances)

slash_one = line2.find("/")

# ==================================================
# Occurrences: Lines 849-849 (2 instances)

slash_one = line2.find("/")

# ==================================================
# Line: 983

python_code = "\n".join(seleniumbase_lines)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/masterqa/master_qa.py
# Line: 235

text = self.execute_script("return window.master_qa_result")

# ==================================================
# Line: 249

text = self.execute_script("return window.master_qa_result")

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/utilities/selenium_ide/convert_ide.py
# Occurrences: Lines 97-97 (2 instances)

ide_base_url = data.group(1)

# ==================================================
# Occurrences: Lines 103-103 (2 instances)

method_name = data.group(1)

# ==================================================
# Occurrences: Lines 137-138 (4 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 151-152 (4 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 164-167 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 182-185 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 200-207 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 225-232 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 249-250 (4 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 262-263 (4 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 275-277 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 294-296 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 312-316 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 327-331 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 342-344 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 351-351 (2 instances)

command = command.replace('\\"', '"')

# ==================================================
# Occurrences: Lines 363-365 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 372-372 (2 instances)

command = command.replace('\\"', '"')

# ==================================================
# Occurrences: Lines 383-385 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 392-392 (2 instances)

command = command.replace('\\"', '"')

# ==================================================
# Occurrences: Lines 404-406 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 413-413 (2 instances)

command = command.replace('\\"', '"')

# ==================================================
# Occurrences: Lines 425-427 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 434-434 (2 instances)

command = command.replace('\\"', '"')

# ==================================================
# Occurrences: Lines 446-453 (10 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 461-461 (2 instances)

command = command.replace('\\"', '"')

# ==================================================
# Occurrences: Lines 473-475 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 482-482 (2 instances)

command = command.replace('\\"', '"')

# ==================================================
# Occurrences: Lines 494-496 (6 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 503-503 (2 instances)

command = command.replace('\\"', '"')

# ==================================================
# Occurrences: Lines 514-515 (4 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 541-542 (4 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 557-558 (4 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 577-580 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 601-604 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 624-627 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 647-650 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 670-673 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 693-696 (8 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 729-729 (2 instances)

whitespace = data.group(1)

# ==================================================
# Occurrences: Lines 744-744 (2 instances)

selector = data.group(1)

# ==================================================
# Occurrences: Lines 758-758 (2 instances)

selector = data.group(1)

# ==================================================
# Occurrences: Lines 775-775 (2 instances)

link_text = data.group(1)

# ==================================================
# Line: 789

for line_num in range(len(lines)):

# ==================================================
# Occurrences: Lines 796-797 (2 instances)

num_lines = len(lines)

# ==================================================
# Occurrences: Lines 806-808 (3 instances)

selector = data.group(2)

# ==================================================
# Occurrences: Lines 814-814 (2 instances)

data2 = re.match(regex_string, lines[line_num + 1])

# ==================================================
# Occurrences: Lines 822-822 (2 instances)

data2 = re.match(regex_string, lines[line_num + 1])

# ==================================================
# Occurrences: Lines 830-831 (2 instances)

num_lines = len(lines)

# ==================================================
# Occurrences: Lines 840-842 (3 instances)

selector = data.group(2)

# ==================================================
# Line: 849

data2 = re.match(regex_string, lines[line_num + 1])

# ==================================================
# Occurrences: Lines 857-858 (2 instances)

num_lines = len(lines)

# ==================================================
# Line: 867

link_text = data.group(2)

# ==================================================
# Line: 875

data2 = re.match(regex_string, lines[line_num + 1])

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/utilities/selenium_grid/grid_node.py
# Line: 91

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# Line: 98

file = codecs.open(file_path, "w+", "utf-8")

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/common/obfuscate.py
# Occurrences: Lines 19-21 (4 instances)

password = getpass.getpass()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/common/decorators.py
# Line: 44

start_time = time.time()

# ==================================================
# Line: 51

end_time = time.time()

# ==================================================
# Line: 104

start_time = time.time()

# ==================================================
# Line: 111

end_time = time.time()

# ==================================================
# Occurrences: Lines 181-185 (6 instances)

elapsed = time.process_time() - last_time_called[0]

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/common/encryption.py
# Occurrences: Lines 17-24 (2 instances)

result = "".join(
    [chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(string, key)]
)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/plugins/sb_manager.py
# Occurrences: Lines 839-843 (2 instances)

if page_load_strategy.lower() not in ["normal", "eager", "none"]:

# ==================================================
# Line: 1265

left_spaces = int(remaining_spaces / 2)

# ==================================================
# Line: 1281

start_time = time.time()

# ==================================================
# Line: 1302

the_traceback = traceback.format_exc().strip()

# ==================================================
# Line: 1324

print(traceback.format_exc().strip())

# ==================================================
# Line: 1340

end_time = time.time()

# ==================================================
# Line: 1362

left_spaces = int(remaining_spaces / 2)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/plugins/pytest_plugin.py
# Occurrences: Lines 1639-1640 (2 instances)

sb_config._time_limit = config.getoption("time_limit")

# ==================================================
# Occurrences: Lines 1653-1654 (2 instances)

sb_config.recorder_mode = config.getoption("recorder_mode")

# ==================================================
# Line: 1718

sb_config.pytest_html_report = config.getoption("htmlpath")  # --html=FILE

# ==================================================
# Line: 1770

sb_config._html_report_name = config.getoption("htmlpath")

# ==================================================
# Line: 1913

existing_pytest_style = f.read()

# ==================================================
# Line: 1925

existing_live_js = f.read()

# ==================================================
# Occurrences: Lines 2216-2224 (3 instances)

abs_path = os.path.abspath(".")

# ==================================================
# Occurrences: Lines 2231-2249 (8 instances)

the_html_r = f.read()

# ==================================================
# Occurrences: Lines 2255-2270 (7 instances)

the_html_r = the_html_r.replace(
    ph_link, "%s and %s" % (sb_link, ph_link)
)

# ==================================================
# Occurrences: Lines 2288-2298 (8 instances)

html_style = f.read()

# ==================================================
# Line: 2329

abs_path = os.path.abspath(".")

# ==================================================
# Line: 2335

the_html_d = f.read()

# ==================================================
# Line: 2346

dash_pie = f.read().strip()

# ==================================================
# Occurrences: Lines 2390-2400 (8 instances)

html_style = f.read()

# ==================================================
# Occurrences: Lines 2408-2414 (2 instances)

html_report_path = os.path.join(
    abs_path, sb_config._html_report_name
)

# ==================================================
# Line: 2424

the_html_r = f.read()

# ==================================================
# Occurrences: Lines 2446-2459 (7 instances)

the_html_r = the_html_r.replace(
    assets_chunk,
    "%s %s" % (assets_chunk, remove_media),
)

# ==================================================
# Occurrences: Lines 2465-2480 (7 instances)

the_html_r = the_html_r.replace(
    ph_link, "%s and %s" % (sb_link, ph_link)
)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/plugins/base_plugin.py
# Occurrences: Lines 207-208 (2 instances)

self.start_time = float(0)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/plugins/driver_manager.py
# Occurrences: Lines 733-737 (2 instances)

if page_load_strategy.lower() not in ["normal", "eager", "none"]:

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/tour_helper.py
# Occurrences: Lines 336-343 (4 instances)

element = driver.execute_script(
    "return Shepherd.activeTour.currentStep"
    ".options.attachTo.element"
)

# ==================================================
# Occurrences: Lines 358-365 (4 instances)

latest_element = driver.execute_script(
    "return Shepherd.activeTour.currentStep"
    ".options.attachTo.element"
)

# ==================================================
# Occurrences: Lines 374-377 (2 instances)

selector = driver.execute_script(
    "return Shepherd.activeTour"
    ".currentStep.options.attachTo.element"
)

# ==================================================
# Occurrences: Lines 469-469 (2 instances)

result = driver.execute_script("return $tour.ended()")

# ==================================================
# Occurrences: Lines 485-485 (2 instances)

result = driver.execute_script("return $tour.ended()")

# ==================================================
# Occurrences: Lines 587-589 (2 instances)

current_step = driver.execute_script(
    "return $tour.currentStep"
)

# ==================================================
# Occurrences: Lines 601-603 (2 instances)

latest_step = driver.execute_script(
    "return $tour.currentStep"
)

# ==================================================
# Occurrences: Lines 726-728 (2 instances)

current_step = driver.execute_script(
    "return $tour.getCurrStepNum()"
)

# ==================================================
# Occurrences: Lines 740-742 (2 instances)

latest_step = driver.execute_script(
    "return $tour.getCurrStepNum()"
)

# ==================================================
# Occurrences: Lines 847-847 (2 instances)

result = driver.execute_script("return $tour._currentStep")

# ==================================================
# Occurrences: Lines 860-862 (2 instances)

current_step = driver.execute_script(
    "return $tour._currentStep"
)

# ==================================================
# Occurrences: Lines 877-879 (2 instances)

latest_step = driver.execute_script(
    "return $tour._currentStep"
)

# ==================================================
# Occurrences: Lines 889-889 (2 instances)

result = driver.execute_script("return $tour._currentStep")

# ==================================================
# Occurrences: Lines 975-976 (2 instances)

backdrop_style = backdrop_style.replace("\n", "")

# ==================================================
# Occurrences: Lines 992-993 (2 instances)

backdrop_style = backdrop_style.replace("\n", "")

# ==================================================
# Occurrences: Lines 1002-1003 (2 instances)

backdrop_style = backdrop_style.replace("\n", "")

# ==================================================
# Occurrences: Lines 1020-1021 (2 instances)

backdrop_style = backdrop_style.replace("\n", "")

# ==================================================
# Occurrences: Lines 1038-1039 (2 instances)

backdrop_style = backdrop_style.replace("\n", "")

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/capabilities_parser.py
# Occurrences: Lines 40-41 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 48-49 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 58-59 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 68-69 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 76-76 (2 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 84-84 (2 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 92-92 (2 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 100-100 (2 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 108-109 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 116-117 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 126-127 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 136-137 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 144-144 (2 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 152-152 (2 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 160-160 (2 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 168-168 (2 instances)

key = data.group(1)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/settings_parser.py
# Occurrences: Lines 22-23 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 31-32 (4 instances)

key = data.group(1)

# ==================================================
# Occurrences: Lines 40-41 (4 instances)

key = data.group(1)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/browser_launcher.py
# Line: 121

page = types.SimpleNamespace()

# ==================================================
# Line: 167

js = types.SimpleNamespace()

# ==================================================
# Occurrences: Lines 330-338 (5 instances)

and str(driver_version).split(".")[0].isdigit()

# ==================================================
# Line: 346

use_version = sb_install.get_latest_stable_chromedriver_version()

# ==================================================
# Occurrences: Lines 361-364 (3 instances)

and str(driver_version).split(".")[0].isdigit()

# ==================================================
# Line: 657

cdp = types.SimpleNamespace()

# ==================================================
# Line: 819

core_items = types.SimpleNamespace()

# ==================================================
# Line: 1193

cdp_mode_on_at_start = __is_cdp_swap_needed(driver)

# ==================================================
# Occurrences: Lines 1228-1235 (3 instances)

is_in_frame = js_utils.is_in_frame(driver)

# ==================================================
# Line: 1241

if IS_WINDOWS and not __is_cdp_swap_needed(driver):

# ==================================================
# Line: 1256

elif IS_WINDOWS and __is_cdp_swap_needed(driver):

# ==================================================
# Line: 1374

if __is_cdp_swap_needed(driver):

# ==================================================
# Line: 1395

if __is_cdp_swap_needed(driver):

# ==================================================
# Line: 1412

if __is_cdp_swap_needed(driver):

# ==================================================
# Line: 1462

if not __is_cdp_swap_needed(driver):

# ==================================================
# Line: 1471

if __is_cdp_swap_needed(driver):

# ==================================================
# Line: 1492

if __is_cdp_swap_needed(driver):

# ==================================================
# Line: 1518

if __is_cdp_swap_needed(driver) and _on_a_captcha_page(driver):

# ==================================================
# Line: 1588

is_in_frame = js_utils.is_in_frame(driver)

# ==================================================
# Line: 1597

is_in_frame = js_utils.is_in_frame(driver)

# ==================================================
# Line: 1698

if js_utils.get_active_element_css(driver) == "body":

# ==================================================
# Line: 1705

active_element_css = js_utils.get_active_element_css(driver)

# ==================================================
# Line: 1956

proxy_zip_lock = fasteners.InterProcessLock(PROXY_ZIP_LOCK)

# ==================================================
# Line: 1968

proxy_dir_lock = fasteners.InterProcessLock(PROXY_DIR_LOCK)

# ==================================================
# Line: 1985

proxy_zip_lock = fasteners.InterProcessLock(PROXY_ZIP_LOCK)

# ==================================================
# Line: 2002

proxy_dir_lock = fasteners.InterProcessLock(PROXY_DIR_LOCK)

# ==================================================
# Occurrences: Lines 2323-2334 (4 instances)

and page_load_strategy.lower() in ["eager", "none"]

# ==================================================
# Line: 2643

chunks = proxy_string.split(":")

# ==================================================
# Occurrences: Lines 2654-2655 (2 instances)

proxy_server = proxy_string.split(":")[0]

# ==================================================
# Occurrences: Lines 2871-2874 (2 instances)

binary_location = os.path.join(DRIVER_DIR, binary_folder)

# ==================================================
# Line: 2889

chrome_fixing_lock = fasteners.InterProcessLock(
    constants.MultiBrowser.DRIVER_FIXING_LOCK
)

# ==================================================
# Occurrences: Lines 2925-2928 (2 instances)

binary_location = os.path.join(DRIVER_DIR, binary_folder)

# ==================================================
# Line: 2947

chrome_fixing_lock = fasteners.InterProcessLock(
    constants.MultiBrowser.DRIVER_FIXING_LOCK
)

# ==================================================
# Line: 3402

chrome_options = _set_chrome_options(
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
)

# ==================================================
# Line: 3479

cap_str = str(desired_caps).lower()

# ==================================================
# Line: 3544

cap_str = str(desired_caps).lower()

# ==================================================
# Occurrences: Lines 3573-3634 (2 instances)

driver = webdriver.Remote(
    command_executor=address,
    options=remote_options,
)

# ==================================================
# Line: 3682

driver = webdriver.Remote(
    command_executor=address,
    options=remote_options,
)

# ==================================================
# Occurrences: Lines 3691-3697 (2 instances)

cap_str = str(desired_caps).lower()

# ==================================================
# Line: 3762

use_uc = is_using_uc(undetectable, browser_name)

# ==================================================
# Line: 3818

args = " ".join(sys.argv)

# ==================================================
# Line: 3829

geckodriver_fixing_lock = fasteners.InterProcessLock(
    constants.MultiBrowser.DRIVER_FIXING_LOCK
)

# ==================================================
# Line: 3852

driver = webdriver.Firefox(
    service=service,
    options=firefox_options,
)

# ==================================================
# Line: 3884

driver = webdriver.Firefox(
    service=service,
    options=firefox_options,
)

# ==================================================
# Line: 3894

driver = webdriver.Firefox(
    service=service,
    options=firefox_options,
)

# ==================================================
# Line: 3926

driver = webdriver.Firefox(
    service=service,
    options=firefox_options,
)

# ==================================================
# Line: 3958

args = " ".join(sys.argv)

# ==================================================
# Line: 3975

args = " ".join(sys.argv)

# ==================================================
# Line: 3988

driver = webdriver.Ie(service=service, options=ie_options)

# ==================================================
# Line: 3997

driver = webdriver.Ie(service=service, options=ie_options)

# ==================================================
# Line: 4051

detect_b_ver.get_browser_version_from_os(br_app)

# ==================================================
# Occurrences: Lines 4081-4083 (2 instances)

output = output.decode("latin1")

# ==================================================
# Line: 4124

args = " ".join(sys.argv)

# ==================================================
# Line: 4135

edgedriver_fixing_lock = fasteners.InterProcessLock(
    constants.MultiBrowser.DRIVER_FIXING_LOCK
)

# ==================================================
# Occurrences: Lines 4204-4209 (2 instances)

if int(str(use_version).split(".")[0]) >= 132:

# ==================================================
# Occurrences: Lines 4218-4222 (3 instances)

if int(use_version) >= 109:

# ==================================================
# Occurrences: Lines 4346-4358 (4 instances)

and page_load_strategy.lower() in ["eager", "none"]

# ==================================================
# Occurrences: Lines 4416-4419 (2 instances)

args = " ".join(sys.argv)

# ==================================================
# Occurrences: Lines 4514-4517 (2 instances)

args = " ".join(sys.argv)

# ==================================================
# Occurrences: Lines 4527-4531 (2 instances)

args = " ".join(sys.argv)

# ==================================================
# Line: 4549

args = " ".join(sys.argv)

# ==================================================
# Occurrences: Lines 4559-4570 (4 instances)

and page_load_strategy.lower() in ["eager", "none"]

# ==================================================
# Line: 4656

detect_b_ver.get_browser_version_from_os(br_app)

# ==================================================
# Occurrences: Lines 4701-4707 (3 instances)

output = subprocess.check_output(
    '"%s" --version' % LOCAL_CHROMEDRIVER, shell=True
)

# ==================================================
# Occurrences: Lines 4727-4729 (2 instances)

output = output.decode("latin1")

# ==================================================
# Line: 4743

uc_driver_version = get_uc_driver_version()

# ==================================================
# Line: 4754

if int(str(use_version).split(".")[0]) >= 132:

# ==================================================
# Line: 4761

or int(str(use_version).split(".")[0]) >= 109

# ==================================================
# Line: 4770

int_use_version = int(str(use_version).split(".")[0])

# ==================================================
# Line: 4855

and int(use_version) >= 115

# ==================================================
# Line: 4874

args = " ".join(sys.argv)

# ==================================================
# Occurrences: Lines 4899-4903 (2 instances)

d_latest = get_latest_chromedriver_version()

# ==================================================
# Line: 4921

chromedriver_fixing_lock = fasteners.InterProcessLock(
    constants.MultiBrowser.DRIVER_FIXING_LOCK
)

# ==================================================
# Occurrences: Lines 4944-4951 (3 instances)

output = subprocess.check_output(
    '"%s" --version' % LOCAL_CHROMEDRIVER,
    shell=True,
)

# ==================================================
# Line: 4973

!= get_uc_driver_version()

# ==================================================
# Occurrences: Lines 4986-4991 (2 instances)

d_latest = get_latest_chromedriver_version()

# ==================================================
# Line: 5016

uc_lock = fasteners.InterProcessLock(
    constants.MultiBrowser.DRIVER_FIXING_LOCK
)

# ==================================================
# Line: 5050

use_uc = is_using_uc(undetectable, browser_name)

# ==================================================
# Occurrences: Lines 5070-5078 (4 instances)

and int(use_version) >= 72

# ==================================================
# Line: 5085

and int(use_version) <= 74

# ==================================================
# Line: 5116

headless_options = _set_chrome_options(
    browser_name,
    downloads_path,
    True,  # headless
    locale_code,
    None,  # proxy_string
    None,  # proxy_auth
    None,  # proxy_user
    None,  # proxy_pass
    None,  # proxy_scheme
    None,  # proxy_bypass_list
    None,  # proxy_pac_url
    None,  # multi_proxy
    None,  # user_agent
    None,  # recorder_ext
    disable_cookies,
    disable_js,
    disable_csp,
    enable_ws,
    enable_sync,
    use_auto_ext,
    False,  # undetectable
    False,  # uc_cdp_events
    False,  # uc_subprocess
    False,  # log_cdp_events
    no_sandbox,
    disable_gpu,
    False,  # headless1
    False,  # headless2
    incognito,
    guest_mode,
    dark_mode,
    None,  # devtools
    remote_debug,
    enable_3d_apis,
    swiftshader,
    None,  # ad_block_on
    None,  # host_resolver_rules
    block_images,
    do_not_track,
    None,  # chromium_arg
    None,  # user_data_dir
    None,  # extension_zip
    None,  # extension_dir
    None,  # disable_features
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
)

# ==================================================
# Line: 5179

< int(str(
    use_version).split(".")[0]
)

# ==================================================
# Line: 5198

driver = webdriver.Chrome(
    service=service,
    options=headless_options,
)

# ==================================================
# Line: 5207

driver = webdriver.Chrome(
    service=service,
    options=headless_options,
)

# ==================================================
# Line: 5239

driver = undetected.Chrome(
    options=chrome_options,
    user_data_dir=user_data_dir,
    driver_executable_path=uc_path,
    browser_executable_path=b_path,
    enable_cdp_events=cdp_events,
    headless=False,  # Xvfb needed!
    version_main=uc_chrome_version,
    use_subprocess=True,  # Always!
)

# ==================================================
# Line: 5263

driver = undetected.Chrome(
    options=chrome_options,
    user_data_dir=user_data_dir,
    driver_executable_path=uc_path,
    browser_executable_path=b_path,
    enable_cdp_events=cdp_events,
    headless=False,  # Xvfb needed!
    version_main=uc_chrome_version,
    use_subprocess=True,  # Always!
)

# ==================================================
# Occurrences: Lines 5294-5308 (2 instances)

driver = undetected.Chrome(
    options=chrome_options,
    user_data_dir=user_data_dir,
    driver_executable_path=uc_path,
    browser_executable_path=b_path,
    enable_cdp_events=cdp_events,
    headless=False,  # Xvfb needed!
    version_main=uc_chrome_version,
    use_subprocess=True,  # Always!
)

# ==================================================
# Line: 5318

driver = webdriver.Chrome(
    service=service,
    options=chrome_options,
)

# ==================================================
# Line: 5327

driver = webdriver.Chrome(
    service=service,
    options=chrome_options,
)

# ==================================================
# Line: 5349

driver = webdriver.Chrome(
    service=service, options=chrome_options
)

# ==================================================
# Occurrences: Lines 5372-5432 (3 instances)

headless_options = _set_chrome_options(
    browser_name,
    downloads_path,
    True,  # headless
    locale_code,
    None,  # proxy_string
    None,  # proxy_auth
    None,  # proxy_user
    None,  # proxy_pass
    None,  # proxy_scheme
    None,  # proxy_bypass_list
    None,  # proxy_pac_url
    None,  # multi_proxy
    None,  # user_agent
    None,  # recorder_ext
    disable_cookies,
    disable_js,
    disable_csp,
    enable_ws,
    enable_sync,
    use_auto_ext,
    False,  # undetectable
    False,  # uc_cdp_events
    False,  # uc_subprocess
    False,  # log_cdp_events
    no_sandbox,
    disable_gpu,
    False,  # headless1
    False,  # headless2
    incognito,
    guest_mode,
    dark_mode,
    None,  # devtools
    remote_debug,
    enable_3d_apis,
    swiftshader,
    None,  # ad_block_on
    None,  # host_resolver_rules
    block_images,
    do_not_track,
    None,  # chromium_arg
    None,  # user_data_dir
    None,  # extension_zip
    None,  # extension_dir
    None,  # disable_features
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
)

# ==================================================
# Line: 5455

driver = webdriver.Chrome(
    service=service,
    options=chrome_options,
)

# ==================================================
# Line: 5464

driver = webdriver.Chrome(
    service=service,
    options=chrome_options,
)

# ==================================================
# Line: 5633

driver = webdriver.Chrome(
    service=service, options=chrome_options
)

# ==================================================
# Occurrences: Lines 5650-5654 (2 instances)

args = " ".join(sys.argv)

# ==================================================
# Line: 5677

driver = webdriver.Chrome(
    service=service,
    options=chrome_options,
)

# ==================================================
# Line: 5698

driver = webdriver.Chrome(
    service=service, options=chrome_options
)

# ==================================================
# Line: 5710

driver = webdriver.Chrome(
    service=service, options=chrome_options
)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/recorder_helper.py
# Occurrences: Lines 12-12 (2 instances)

action[2] = unquote(action[2], errors="strict")

# ==================================================
# Occurrences: Lines 28-28 (2 instances)

action[2] = unquote(action[2], errors="strict")

# ==================================================
# Occurrences: Lines 108-108 (2 instances)

text = action[2].replace("\n", "\\n")

# ==================================================
# Occurrences: Lines 133-133 (2 instances)

text = action[2].replace("\n", "\\n")

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/sb_cdp.py
# Occurrences: Lines 190-192 (2 instances)

time_now = time.time()

# ==================================================
# Occurrences: Lines 203-204 (4 instances)

element = self.__add_sync_methods(element)

# ==================================================
# Occurrences: Lines 210-211 (4 instances)

element = self.__add_sync_methods(element)

# ==================================================
# Occurrences: Lines 219-219 (2 instances)

return self.__add_sync_methods(element)

# ==================================================
# Occurrences: Lines 228-228 (2 instances)

return self.__add_sync_methods(element)

# ==================================================
# Occurrences: Lines 264-264 (2 instances)

element = self.__add_sync_methods(element)

# ==================================================
# Occurrences: Lines 272-272 (2 instances)

element = self.__add_sync_methods(element)

# ==================================================
# Occurrences: Lines 607-612 (2 instances)

return element.get_js_attributes()[attribute]

# ==================================================
# Occurrences: Lines 1107-1114 (2 instances)

source = self.loop.run_until_complete(
    self.page.evaluate("document.documentElement.outerHTML")
)

# ==================================================
# Line: 2040

actual = self.get_title().strip()

# ==================================================
# Line: 2049

actual = self.get_title().strip()

# ==================================================
# Line: 2055

actual = self.get_title().strip()

# ==================================================
# Line: 2065

actual = self.get_title().strip()

# ==================================================
# Line: 2071

actual = self.get_current_url().strip()

# ==================================================
# Line: 2078

actual = self.get_current_url().strip()

# ==================================================
# Line: 2084

actual = self.get_current_url().strip()

# ==================================================
# Line: 2094

actual = self.get_current_url().strip()

# ==================================================
# Line: 2108

text = text.strip()

# ==================================================
# Line: 2119

and text.strip() == element.text_all.strip()

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/detect_b_ver.py
# Line: 244

quad_version = read_version_from_cmd(cmd_mapping, quad_pattern)

# ==================================================
# Line: 251

quad_version = read_version_from_cmd(cmd_mapping, quad_pattern)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/fixtures/shared_utils.py
# Occurrences: Lines 250-251 (2 instances)

if float(int(time_limit)) == float(time_limit):

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/fixtures/page_actions.py
# Occurrences: Lines 591-596 (4 instances)

and text in element.get_attribute(text_attr)

# ==================================================
# Occurrences: Lines 685-690 (4 instances)

and text.strip() == element.get_property("value").strip()

# ==================================================
# Occurrences: Lines 698-703 (4 instances)

text.strip() == element.get_attribute(text_attr).strip()

# ==================================================
# Occurrences: Lines 710-715 (4 instances)

and text.strip() == element.text.strip()

# ==================================================
# Line: 1269

elements = driver.find_elements(by=by, value=selector)

# ==================================================
# Line: 1277

elements = driver.find_elements(by=by, value=selector)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/fixtures/js_utils.py
# Occurrences: Lines 380-383 (2 instances)

element = driver.find_element(by, selector)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/fixtures/xpath_to_css.py
# Occurrences: Lines 171-174 (4 instances)

s_tag = data.group(1)

# ==================================================
# Occurrences: Lines 184-187 (4 instances)

s_tag = data.group(1)

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/fixtures/base_case.py
# Line: 272

self.driver = self.get_new_driver()

# ==================================================
# Line: 335

self.driver = self.get_new_driver()

# ==================================================
# Line: 419

element = page_actions.wait_for_element_visible(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Line: 432

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Occurrences: Lines 448-450 (3 instances)

href = element.get_attribute("href").strip()

# ==================================================
# Line: 468

element = page_actions.wait_for_element_clickable(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Line: 498

element = page_actions.wait_for_element_visible(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Line: 512

element = page_actions.wait_for_element_visible(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Occurrences: Lines 525-527 (3 instances)

href = element.get_attribute("href").strip()

# ==================================================
# Line: 552

element = page_actions.wait_for_element_visible(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Line: 569

element = page_actions.wait_for_element_clickable(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Occurrences: Lines 592-600 (2 instances)

element = page_actions.wait_for_element_visible(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Line: 688

element = page_actions.wait_for_element_visible(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Line: 702

element = page_actions.wait_for_element_visible(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Line: 769

element = page_actions.wait_for_element_visible(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Line: 783

element = page_actions.wait_for_element_visible(
    self.driver,
    selector,
    by,
    timeout=timeout,
    original_selector=original_selector,
)

# ==================================================
# Line: 895

element = self.wait_for_element_clickable(
    selector, by=by, timeout=timeout
)

# ==================================================
# Line: 910

element = self.wait_for_element_clickable(
    selector, by=by, timeout=timeout
)

# ==================================================
# Occurrences: Lines 1125-1129 (2 instances)

css_selector = self.convert_to_css_selector(selector, by=by)

# ==================================================
# Line: 1199

element = self.wait_for_element_visible(
    selector, by=by, timeout=timeout
)

# ==================================================
# Line: 1210

element = self.wait_for_element_visible(
    selector, by=by, timeout=timeout
)

# ==================================================
# Line: 1632

element = self.wait_for_link_text_visible(
    link_text, timeout=timeout
)

# ==================================================
# Line: 1658

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 1667

element = self.wait_for_link_text_visible(
    link_text, timeout=timeout
)

# ==================================================
# Line: 1708

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 1760

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 1822

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Occurrences: Lines 1867-1892 (8 instances)

element = page_actions.wait_for_element_visible(
    self.driver, selector, by, timeout
)

# ==================================================
# Occurrences: Lines 1920-1931 (4 instances)

element = page_actions.wait_for_element_present(
    self.driver, selector, by, timeout
)

# ==================================================
# Occurrences: Lines 2113-2124 (4 instances)

element = page_actions.wait_for_element_present(
    self.driver, selector, by, timeout
)

# ==================================================
# Line: 2263

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2294

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2307

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2337

elements = self.find_visible_elements(selector, by=by)

# ==================================================
# Line: 2350

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2358

elements = self.find_visible_elements(selector, by=by)

# ==================================================
# Line: 2369

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2410

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2417

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2746

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2795

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2872

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Line: 2900

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Occurrences: Lines 3048-3054 (2 instances)

element = self.wait_for_element_present(
    dropdown_selector, by=dropdown_by, timeout=timeout
)

# ==================================================
# Line: 3064

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Occurrences: Lines 3077-3083 (2 instances)

element = self.wait_for_element_present(
    dropdown_selector, by=dropdown_by, timeout=timeout
)

# ==================================================
# Line: 3121

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Occurrences: Lines 3275-3285 (7 instances)

if not line.strip().startswith("//"):

# ==================================================
# Occurrences: Lines 3298-3308 (6 instances)

if base.get("href"):

# ==================================================
# Occurrences: Lines 3314-3322 (4 instances)

if soup.head and len(str(soup.head)) > 12:

# ==================================================
# Occurrences: Lines 3361-3363 (2 instances)

line = line.strip()

# ==================================================
# Occurrences: Lines 3631-3635 (2 instances)

time_stamp = self.execute_script("return Date.now();")

# ==================================================
# Occurrences: Lines 3755-3758 (2 instances)

current_page_source = self.get_page_source()

# ==================================================
# Line: 3787

origin = self.get_origin()

# ==================================================
# Line: 3805

origin = self.get_origin()

# ==================================================
# Line: 3821

time_stamp = self.execute_script("return Date.now();")

# ==================================================
# Occurrences: Lines 3846-3848 (2 instances)

url_of_past_tab = self.get_current_url()

# ==================================================
# Line: 3855

time_stamp = self.execute_script("return Date.now();")

# ==================================================
# Occurrences: Lines 3866-3867 (2 instances)

current_url = self.get_current_url()

# ==================================================
# Line: 3875

past_content = self.__page_sources.pop()

# ==================================================
# Line: 3885

time_stamp = self.execute_script("return Date.now();")

# ==================================================
# Line: 5144

elif url1.replace("http://", "https://") == url2:

# ==================================================
# Line: 5274

url1 = url1.replace("http://", "https://")

# ==================================================
# Occurrences: Lines 5619-5621 (2 instances)

extra_file_path = os.path.join(recordings_folder, extra_file_name)

# ==================================================
# Occurrences: Lines 5667-5669 (2 instances)

extra_file_path = os.path.join(recordings_folder, extra_file_name)

# ==================================================
# Occurrences: Lines 5688-5690 (2 instances)

extra_file_path = os.path.join(recordings_folder, extra_file_name)

# ==================================================
# Occurrences: Lines 5809-5810 (2 instances)

file_path = os.path.join(features_folder, file_name)

# ==================================================
# Occurrences: Lines 5846-5848 (2 instances)

file_path = os.path.join(features_folder, file_name)

# ==================================================
# Occurrences: Lines 5859-5861 (2 instances)

file_path = os.path.join(features_folder, file_name)

# ==================================================
# Occurrences: Lines 5898-5900 (2 instances)

file_path = os.path.join(features_folder, file_name)

# ==================================================
# Occurrences: Lines 5908-5910 (2 instances)

file_path = os.path.join(steps_folder, file_name)

# ==================================================
# Occurrences: Lines 5919-5921 (2 instances)

file_path = os.path.join(steps_folder, file_name)

# ==================================================
# Occurrences: Lines 6039-6043 (2 instances)

style = element.get_attribute("style")

# ==================================================
# Line: 6060

element = self.wait_for_element_visible(
    selector, by=by, timeout=settings.SMALL_TIMEOUT
)

# ==================================================
# Line: 6080

element = self.wait_for_element_visible(
    selector, by=by, timeout=settings.SMALL_TIMEOUT
)

# ==================================================
# Line: 6101

style = element.get_attribute("style")

# ==================================================
# Line: 6108

style = element.get_attribute("style")

# ==================================================
# Occurrences: Lines 6118-6124 (4 instances)

selector = re.escape(selector)

# ==================================================
# Line: 6289

element = self.wait_for_element_visible(
    selector, by=by, timeout=timeout
)

# ==================================================
# Line: 6297

element = self.wait_for_element_visible(
    selector, by=by, timeout=timeout
)

# ==================================================
# Line: 6319

element = self.wait_for_element_visible(
    original_selector, by=original_by, timeout=timeout
)

# ==================================================
# Line: 6336

element = self.wait_for_element_visible(
    original_selector, by=original_by, timeout=timeout
)

# ==================================================
# Occurrences: Lines 6442-6448 (2 instances)

success = js_utils.scroll_to_element(self.driver, element)

# ==================================================
# Occurrences: Lines 6457-6459 (2 instances)

pre_window_count = len(self.driver.window_handles)

# ==================================================
# Occurrences: Lines 6480-6487 (3 instances)

success = js_utils.scroll_to_element(self.driver, element)

# ==================================================
# Line: 6519

element = self.wait_for_element_present(
    selector, by, timeout=settings.MINI_TIMEOUT
)

# ==================================================
# Line: 6529

element = self.wait_for_element_present(
    selector, by, timeout=settings.MINI_TIMEOUT
)

# ==================================================
# Line: 6539

latest_window_count = len(self.driver.window_handles)

# ==================================================
# Occurrences: Lines 6980-6983 (2 instances)

status_code = str(self.get_link_status_code(link))

# ==================================================
# Occurrences: Lines 7066-7068 (2 instances)

text = text.replace("\xe2\xbe\x8f", "\xe8\xa1\x8c")

# ==================================================
# Line: 7298

element = self.wait_for_element_present(
    selector, by=by, timeout=timeout
)

# ==================================================
# Line: 7340

element = self.wait_for_element_present(
    selector, by=by, timeout=timeout
)

# ==================================================
# Occurrences: Lines 7412-7413 (4 instances)

if len(text_row) > max_width:

# ==================================================
# Line: 7912

actual = self.get_page_title().strip()

# ==================================================
# Line: 7922

actual = self.get_page_title().strip()

# ==================================================
# Line: 7930

actual = self.get_page_title().strip()

# ==================================================
# Line: 7961

actual = self.get_page_title().strip()

# ==================================================
# Line: 7972

actual = self.get_page_title().strip()

# ==================================================
# Line: 7980

actual = self.get_page_title().strip()

# ==================================================
# Line: 8007

actual = self.get_current_url().strip()

# ==================================================
# Line: 8014

actual = self.get_current_url().strip()

# ==================================================
# Line: 8020

actual = self.get_current_url().strip()

# ==================================================
# Line: 8045

actual = self.get_current_url().strip()

# ==================================================
# Line: 8055

actual = self.get_current_url().strip()

# ==================================================
# Line: 8061

actual = self.get_current_url().strip()

# ==================================================
# Line: 8394

mfa_code = self.get_mfa_code(totp_key)

# ==================================================
# Line: 8408

mfa_code = self.get_mfa_code(totp_key)

# ==================================================
# Occurrences: Lines 8479-8487 (2 instances)

element = self.wait_for_element_present(
    original_selector, by=by, timeout=timeout
)

# ==================================================
# Occurrences: Lines 8650-8658 (2 instances)

element = self.wait_for_element_present(
    original_selector, by=original_by, timeout=0.2
)

# ==================================================
# Occurrences: Lines 10036-10037 (2 instances)

a_t = SD.translate_assert_text(self._language)

# ==================================================
# Occurrences: Lines 10062-10063 (2 instances)

a_t = SD.translate_assert_text(self._language)

# ==================================================
# Line: 10897

baseline_png_path = os.path.join(visual_baseline_path, baseline_png)

# ==================================================
# Line: 10951

baseline_path = os.path.join(visual_baseline_path, baseline_png)

# ==================================================
# Occurrences: Lines 10971-10977 (3 instances)

level_1_data = json.loads(f.read())

# ==================================================
# Line: 11138

exception_info = sys.exc_info()[1]

# ==================================================
# Line: 11146

exc_message = sys.exc_info()

# ==================================================
# Occurrences: Lines 13231-13236 (3 instances)

if theme.lower() not in valid_themes:

# ==================================================
# Occurrences: Lines 13247-13263 (6 instances)

if color.lower() not in valid_colors:

# ==================================================
# Occurrences: Lines 13386-13392 (3 instances)

detected_color = str(button[1]).lower()

# ==================================================
# Occurrences: Lines 13510-13511 (2 instances)

is_visible = self.is_element_visible(selector, by=by)

# ==================================================
# Occurrences: Lines 13533-13534 (2 instances)

(is_visible and not self.is_element_visible(selector, by=by))

# ==================================================
# Occurrences: Lines 13559-13560 (2 instances)

is_visible = element.is_displayed()

# ==================================================
# Occurrences: Lines 13581-13582 (2 instances)

(is_visible and not element.is_displayed())

# ==================================================
# Line: 13972

element = self.wait_for_element_visible(
    selector, by=by, timeout=settings.SMALL_TIMEOUT
)

# ==================================================
# Line: 13989

element = self.wait_for_element_visible(
    selector, by=by, timeout=settings.SMALL_TIMEOUT
)

# ==================================================
# Line: 14068

element = self.wait_for_element_visible(
    selector, by=by, timeout=settings.SMALL_TIMEOUT
)

# ==================================================
# Line: 14085

element = self.wait_for_element_visible(
    selector, by=by, timeout=settings.SMALL_TIMEOUT
)

# ==================================================
# Line: 14098

style = element.get_attribute("style")

# ==================================================
# Line: 14105

style = element.get_attribute("style")

# ==================================================
# Occurrences: Lines 14116-14122 (4 instances)

selector = re.escape(selector)

# ==================================================
# Occurrences: Lines 14308-14308 (2 instances)

and int(self.__get_major_browser_version()) >= 96

# ==================================================
# Occurrences: Lines 14321-14321 (2 instances)

self.__get_major_browser_version()

# ==================================================
# Occurrences: Lines 14351-14358 (4 instances)

shadow_root = self.execute_script(
    "return arguments[0].shadowRoot;", element
)

# ==================================================
# Occurrences: Lines 14365-14367 (2 instances)

shadow_root = self.execute_script(
    "return arguments[0].shadowRoot;", element
)

# ==================================================
# Occurrences: Lines 14377-14389 (6 instances)

and int(self.__get_major_browser_version()) >= 96

# ==================================================
# Occurrences: Lines 14405-14407 (2 instances)

element = shadow_root.find_element(
    By.CSS_SELECTOR, value=selector_part
)

# ==================================================
# Occurrences: Lines 14508-14511 (2 instances)

actual_text = self.__get_shadow_text(
    selector, timeout=1
).strip()

# ==================================================
# Occurrences: Lines 14526-14527 (2 instances)

actual_text = self.__get_shadow_text(selector, timeout=1).strip()

# ==================================================
# Occurrences: Lines 14542-14545 (2 instances)

actual_text = self.__get_shadow_text(
    selector, timeout=1
).strip()

# ==================================================
# Occurrences: Lines 14560-14561 (2 instances)

actual_text = self.__get_shadow_text(selector, timeout=1).strip()

# ==================================================
# Occurrences: Lines 14575-14576 (2 instances)

actual_text = self.__get_shadow_text(selector, timeout=1)

# ==================================================
# Occurrences: Lines 14588-14589 (2 instances)

actual_text = self.__get_shadow_text(selector, timeout=1)

# ==================================================
# Line: 14852

test_id = self.__get_test_id()

# ==================================================
# Line: 15030

self.execution_guid = str(uuid.uuid4())

# ==================================================
# Line: 15038

exec_payload.execution_start_time = int(time.time() * 1000.0)

# ==================================================
# Line: 15045

self.testcase_guid = str(uuid.uuid4())

# ==================================================
# Line: 15061

self.case_start_time = int(time.time() * 1000.0)

# ==================================================
# Occurrences: Lines 15118-15122 (2 instances)

self.data_path = os.path.join(self.log_path, self.__get_test_id())

# ==================================================
# Occurrences: Lines 15149-15150 (2 instances)

metrics_string = metrics_string.replace(" ", "")

# ==================================================
# Occurrences: Lines 15160-15161 (2 instances)

self.__device_width = int(metrics_list[0])

# ==================================================
# Occurrences: Lines 15218-15219 (2 instances)

metrics_string = metrics_string.replace(" ", "")

# ==================================================
# Occurrences: Lines 15230-15231 (2 instances)

self._xvfb_width = int(metrics_list[0])

# ==================================================
# Line: 15281

self.__js_start_time = int(time.time() * 1000.0)

# ==================================================
# Line: 15292

url = self.get_current_url()

# ==================================================
# Line: 15310

self.__js_start_time = int(time.time() * 1000.0)

# ==================================================
# Occurrences: Lines 15325-15330 (2 instances)

if self.get_current_url() != "about:blank":

# ==================================================
# Line: 15424

sb_config.start_time_ms = int(time.time() * 1000.0)

# ==================================================
# Line: 15471

self.driver.get_screenshot_as_base64()

# ==================================================
# Line: 15480

self.driver.get_screenshot_as_base64()

# ==================================================
# Line: 15493

self.driver.get_screenshot_as_png()

# ==================================================
# Line: 15511

self.driver.get_screenshot_as_png()

# ==================================================
# Occurrences: Lines 15799-15804 (2 instances)

parts = test_id.split(".")

# ==================================================
# Occurrences: Lines 15858-15860 (2 instances)

abs_path = os.path.abspath(".")

# ==================================================
# Line: 15912

sb_config._d_t_log_path[test_id] = os.path.join(log_dir, ft_id)

# ==================================================
# Line: 15978

sb_config._d_t_log_path[test_id] = os.path.join(
    log_dir, ft_id
)

# ==================================================
# Line: 16018

abs_path = os.path.abspath(".")

# ==================================================
# Line: 16060

sb_config._d_t_log_path[key] = os.path.join(log_dir, ft_id)

# ==================================================
# Line: 16180

abs_path = os.path.abspath(".")

# ==================================================
# Line: 16194

dash_jsonpath = os.path.join(abs_path, dash_json_loc)

# ==================================================
# Line: 16514

test_id = self.__get_test_id()

# ==================================================
# Line: 16526

test_logpath = os.path.join(self.log_path, test_id)

# ==================================================
# Line: 16551

test_logpath = os.path.join(self.log_path, test_id)

# ==================================================
# Line: 16643

path = os.path.join(self.log_path, test_id)

# ==================================================
# Occurrences: Lines 16696-16697 (2 instances)

test_id = self.__get_test_id()

# ==================================================
# Occurrences: Lines 16720-16721 (2 instances)

test_id = self.__get_test_id()

# ==================================================
