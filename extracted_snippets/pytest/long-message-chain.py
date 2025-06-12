# long-message-chain snippets for pytest

# File: /root/ecooptimizer/pytest/src/_pytest/assertion/rewrite.py
# Line: 268

set(names).intersection(sys.modules).difference(self._rewritten_names)

# ==================================================
# Line: 573

ret[assert_lineno] = "".join(lines).rstrip().rstrip("\\")

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/assertion/util.py
# Occurrences: Lines 351-352 (2 instances)

left_formatting = PrettyPrinter().pformat(left).splitlines()

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/config/findpaths.py
# Line: 83

result = config.get("tool", {}).get("pytest", {}).get("ini_options", None)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/_py/path.py
# Line: 1109

names = self.new(ext="").relto(pkgroot).split(self.sep)

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/pastebin.py
# Line: 87

urlopen(url, data=urlencode(params).encode("ascii")).read().decode("utf-8")

# ==================================================
# File: /root/ecooptimizer/pytest/src/_pytest/junitxml.py
# Line: 664

timestamp=self.suite_start.as_utc().astimezone().isoformat(),

# ==================================================
