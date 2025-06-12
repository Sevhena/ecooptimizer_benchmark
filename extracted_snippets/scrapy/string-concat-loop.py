# string-concat-loop snippets for scrapy

# File: /root/ecooptimizer/scrapy/scrapy/utils/engine.py
# Occurrences: Lines 35-37 (2 instances)

for test in tests:
    try:
        checks += [(test, eval(test))]  # noqa: S307  # pylint: disable=eval-used
    except Exception as e:
        checks += [(test, f"{type(e).__name__} (exception)")]


# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/extensions/debug.py
# Line: 67

for id_, frame in sys._current_frames().items():
    name = id2name.get(id_, "")
    dump = "".join(traceback.format_stack(frame))
    dumps += f"# Thread: {name}({id_})\n{dump}\n"

# ==================================================
# File: /root/ecooptimizer/scrapy/scrapy/downloadermiddlewares/cookies.py
# Occurrences: Lines 160-162 (2 instances)

for key, value in decoded.items():  # path, domain
    cookie_str += f"; {key.capitalize()}={value}"

# ==================================================
