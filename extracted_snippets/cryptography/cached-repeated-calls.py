# cached-repeated-calls snippets for cryptography

# File: /root/ecooptimizer/cryptography/src/cryptography/hazmat/backends/openssl/backend.py
# Occurrences: Lines 89-90 (2 instances)

assert rust_openssl.is_fips_enabled()

# ==================================================
# File: /root/ecooptimizer/cryptography/src/cryptography/hazmat/primitives/serialization/ssh.py
# Occurrences: Lines 320-321 (2 instances)

e, data = _get_mpint(data)

# ==================================================
# Occurrences: Lines 337-342 (6 instances)

n, data = _get_mpint(data)

# ==================================================
# Occurrences: Lines 392-395 (4 instances)

p, data = _get_mpint(data)

# ==================================================
# Occurrences: Lines 471-472 (2 instances)

curve, data = _get_sshstr(data)

# ==================================================
# Occurrences: Lines 705-707 (3 instances)

ciphername, data = _get_sshstr(data)

# ==================================================
# Line: 713

pubdata, data = _get_sshstr(data)

# ==================================================
# Line: 730

edata, data = _get_sshstr(data)

# ==================================================
# Occurrences: Lines 759-769 (4 instances)

edata, data = _get_sshstr(data)

# ==================================================
# Line: 778

_, edata = _get_sshstr(edata)

# ==================================================
# Line: 815

f_kdfoptions = _FragList()

# ==================================================
# Line: 839

f_public_key = _FragList()

# ==================================================
# Occurrences: Lines 847-850 (2 instances)

f_secrets.put_raw(_PADDING[: blklen - (f_secrets.size() % blklen)])

# ==================================================
# Line: 860

slen = f_secrets.size()

# ==================================================
# Occurrences: Lines 1059-1082 (11 instances)

inner_key_type, rest = _get_sshstr(rest)

# ==================================================
# Line: 1090

signature_raw, rest = _get_sshstr(rest)

# ==================================================
# Occurrences: Lines 1136-1136 (2 instances)

name, exts_opts = _get_sshstr(exts_opts)

# ==================================================
# Occurrences: Lines 1142-1142 (2 instances)

value, exts_opts = _get_sshstr(exts_opts)

# ==================================================
# Line: 1536

f = _FragList()

# ==================================================
# Line: 1543

fprincipals = _FragList()

# ==================================================
# Occurrences: Lines 1549-1553 (2 instances)

fcrit = _FragList()

# ==================================================
# Occurrences: Lines 1559-1563 (2 instances)

fext = _FragList()

# ==================================================
# Line: 1573

caf = _FragList()

# ==================================================
# Line: 1582

fsig = _FragList()

# ==================================================
# Occurrences: Lines 1590-1592 (2 instances)

fsig = _FragList()

# ==================================================
# Line: 1604

fsig = _FragList()

# ==================================================
