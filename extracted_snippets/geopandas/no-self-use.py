# no-self-use snippets for geopandas

# File: /root/ecooptimizer/geopandas/versioneer.py
# Line: 1950

def run(self) -> None:
    vers = get_versions(verbose=True)
    print("Version: %s" % vers["version"])
    print(" full-revisionid: %s" % vers.get("full-revisionid"))
    print(" dirty: %s" % vers.get("dirty"))
    print(" date: %s" % vers.get("date"))
    if vers["error"]:
        print(" error: %s" % vers["error"])


# ==================================================
# File: /root/ecooptimizer/geopandas/geopandas/io/_pyarrow_hotfix.py
# Line: 46

def __arrow_ext_serialize__(self):
    return b""


# ==================================================
