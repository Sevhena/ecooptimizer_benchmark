# cached-repeated-calls snippets for pytest

# File: /root/ecooptimizer/pytest/src/_pytest/stepwise.py
# Line: 133

self.cached_info.last_test_count = len(items)

# ==================================================
# Occurrences: Lines 144-146 (2 instances)

if last_test_count is not None and last_test_count != len(items):

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/fixtures.py
# Line: 920

generator = fixturefunc(**kwargs)

# ==================================================
# Line: 929

fixture_result = fixturefunc(**kwargs)

# ==================================================
# Occurrences: Lines 1641-1642 (4 instances)

while lastlen != len(fixturenames_closure):

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/assertion/rewrite.py
# Occurrences: Lines 914-921 (4 instances)

assertmsg = ast.Constant("")

# ==================================================
# Line: 952

clear_format = ast.Assign(variables, ast.Constant(None))

# ==================================================
# Occurrences: Lines 963-970 (4 instances)

assertmsg = ast.Constant("")

# ==================================================
# Line: 977

clear = ast.Assign(variables, ast.Constant(None))

# ==================================================
# Line: 1011

res_var = self.variable()

# ==================================================
# Line: 1037

pytest_temp = self.variable()

# ==================================================
# Line: 1137

res_variables = [self.variable() for i in range(len(comp.ops))]

# ==================================================
# Line: 1150

next_operand.target.id = self.variable()

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/assertion/util.py
# Occurrences: Lines 566-566 (2 instances)

if getattr(left, field) == getattr(right, field):

# ==================================================
# Occurrences: Lines 583-584 (2 instances)

field_left = getattr(left, field)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_code/source.py
# Occurrences: Lines 33-34 (2 instances)

self.lines = deindent(obj.split("\n"))

# ==================================================
# Occurrences: Lines 41-42 (2 instances)

self.lines = deindent(src.split("\n"))

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/pathlib.py
# Occurrences: Lines 267-270 (2 instances)

pid = os.getpid()

# ==================================================
# Line: 539

pkg_root, module_name = resolve_pkg_root_and_module_name(
    path, consider_namespace_packages=consider_namespace_packages
)

# ==================================================
# Line: 569

pkg_root, module_name = resolve_pkg_root_and_module_name(
    path, consider_namespace_packages=consider_namespace_packages
)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/raises.py
# Line: 1155

self._fail_reason = cast(str, self._fail_reason)

# ==================================================
# Line: 1180

self._fail_reason = cast(str, self._fail_reason)

# ==================================================
# Line: 1210

cast(str, self._fail_reason) + f" on the {type(exception).__name__}"

# ==================================================
# Line: 1370

if results.get_result(i_exp, i_actual) is None:

# ==================================================
# Line: 1386

res = results.get_result(i_exp, i_actual)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/main.py
# Line: 296

excinfo = _pytest._code.ExceptionInfo.from_current()

# ==================================================
# Line: 307

excinfo = _pytest._code.ExceptionInfo.from_current()

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/skipping.py
# Occurrences: Lines 255-257 (2 instances)

xfailed = item.stash.get(xfailed_key, None)

# ==================================================
# Occurrences: Lines 266-268 (2 instances)

xfailed = item.stash.get(xfailed_key, None)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/mark/expression.py
# Occurrences: Lines 185-187 (2 instances)

ret = and_expr(s)

# ==================================================
# Occurrences: Lines 193-195 (2 instances)

ret = not_expr(s)

# ==================================================
# Line: 224

keyword_name = s.accept(TokenType.IDENT, reject=True)

# ==================================================
# Line: 240

value_token = s.accept(TokenType.IDENT, reject=True)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/config/findpaths.py
# Line: 50

iniconfig = _parse_ini_config(filepath)

# ==================================================
# Line: 61

iniconfig = _parse_ini_config(filepath)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/pytester.py
# Line: 169

lines1 = self.get_open_files()

# ==================================================
# Line: 175

lines2 = self.get_open_files()

# ==================================================
# Occurrences: Lines 1429-1433 (2 instances)

popen.wait()

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_io/pprint.py
# Line: 602

objid = id(object)

# ==================================================
# Line: 631

objid = id(object)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/python_api.py
# Occurrences: Lines 170-171 (2 instances)

approx_value = get_value_from_nested_list(approx_side_as_seq, index)

# ==================================================
# Occurrences: Lines 184-185 (2 instances)

str(get_value_from_nested_list(other_side_as_array, index)),

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_py/path.py
# Line: 808

names = error.checked_call(os.listdir, self.strpath)

# ==================================================
# Line: 817

names = error.checked_call(os.listdir, self.strpath)

# ==================================================
# Line: 1097

spec = importlib.util.spec_from_file_location(modname, str(self))

# ==================================================
# Occurrences: Lines 1149-1152 (2 instances)

mod.__file__ = str(self)

# ==================================================
# Line: 1300

mypid = os.getpid()

# ==================================================
# Occurrences: Lines 1314-1314 (2 instances)

mypid = os.getpid()

# ==================================================
# Occurrences: Lines 1322-1322 (2 instances)

if os.getpid() != mypid:

# ==================================================
# Line: 1336

num = parse_num(path)

# ==================================================
# Line: 1379

num = parse_num(path)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/terminal.py
# Line: 622

was_xfail = hasattr(report, "wasxfail")

# ==================================================
# Line: 649

if rep.skipped or hasattr(report, "wasxfail"):

# ==================================================
# Line: 705

progress = len(self._progress_nodeids_reported)

# ==================================================
# Line: 740

return f" [{len(self._progress_nodeids_reported) * 100 // collected:3d}%]"

# ==================================================
# Occurrences: Lines 1258-1262 (3 instances)

verbose_word, verbose_markup = rep._get_verbose_word_with_markup(
    self.config, {_color_for_type["warnings"]: True}
)

# ==================================================
# Occurrences: Lines 1273-1277 (3 instances)

verbose_word, verbose_markup = rep._get_verbose_word_with_markup(
    self.config, {_color_for_type["warnings"]: True}
)

# ==================================================
# Line: 1292

markup_word = self._tw.markup(verbose_word, **verbose_markup)

# ==================================================
# Occurrences: Lines 1310-1314 (3 instances)

verbose_word, verbose_markup = rep._get_verbose_word_with_markup(
    self.config, {_color_for_type["warnings"]: True}
)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/python.py
# Line: 505

ExceptionInfo.from_current().getrepr(style="short")

# ==================================================
# Line: 518

exc_info = ExceptionInfo.from_current()

# ==================================================
# Occurrences: Lines 1407-1412 (3 instances)

num_ids = len(parametersets)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/junitxml.py
# Occurrences: Lines 205-207 (2 instances)

message = str(report.longrepr)

# ==================================================
# Line: 223

reason = str(report.longrepr)

# ==================================================
# Line: 229

self._add_simple("error", bin_xml_escape(msg), str(report.longrepr))

# ==================================================
# Occurrences: Lines 557-575 (4 instances)

reporter = self._opentestcase(report)

# ==================================================
# Line: 582

reporter = self._opentestcase(report)

# ==================================================
# Occurrences: Lines 591-612 (5 instances)

reporter = self._opentestcase(report)

# ==================================================
