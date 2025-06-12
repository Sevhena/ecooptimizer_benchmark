# cached-repeated-calls snippets for flask

# File: /root/ecooptimizer/flask/src/flask/cli.py
# Line: 49

app = getattr(module, attr_name, None)

# ==================================================
# Line: 68

app_factory = getattr(module, attr_name, None)

# ==================================================
# Occurrences: Lines 348-352 (2 instances)

import_name = prepare_import(path)

# ==================================================
# File: /root/ecooptimizer/flask/src/flask/testing.py
# Line: 215

builder = copy(args[0])

# ==================================================
# Line: 224

request = copy(args[0])

# ==================================================
# File: /root/ecooptimizer/flask/src/flask/app.py
# Occurrences: Lines 1314-1319 (2 instances)

response = self.ensure_sync(func)(response)

# ==================================================
