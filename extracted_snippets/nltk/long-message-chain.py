# long-message-chain snippets for nltk

# File: /root/ecooptimizer/nltk/nltk/ccg/combinator.py
# Line: 254

return left.res().dir().is_forward() and left.arg().is_primitive()

# ==================================================
# Line: 263

return right.res().dir().is_backward() and right.arg().is_primitive()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/drt_glue_demo.py
# Line: 503

self._drs = reading.simplify().normalize().resolve_anaphora()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/rdparser_app.py
# Line: 566

dy = max(dy, leaf.parent().label().bbox()[3] - leaf.bbox()[3] + 10)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/wordnet_app.py
# Line: 778

words = [w for w in [w.strip().lower().replace(" ", "_") for w in words] if w != ""]

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/internals.py
# Line: 952

ElementTree.tostring(self._etree, encoding="utf8").decode("utf8").rstrip()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/viterbi.py
# Line: 438

if sys.stdin.readline().strip().lower().startswith("y"):

# ==================================================
# Line: 447

if sys.stdin.readline().strip().lower().startswith("y"):

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/pchart.py
# Line: 561

draw_parses = sys.stdin.readline().strip().lower().startswith("y")

# ==================================================
# Line: 572

print_parses = sys.stdin.readline().strip().lower().startswith("y")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/featurechart.py
# Occurrences: Lines 659-660 (2 instances)

p.strip_dirs().sort_stats("time", "cum").print_stats(60)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/downloader.py
# Line: 1256

user_input = input("Config> ").strip().lower()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/hunpos.py
# Line: 136

tagged = self._hunpos.stdout.readline().strip().split(b"\t")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/repp.py
# Line: 91

repp_output = self._execute(cmd).decode(self.encoding).strip()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/punkt.py
# Line: 1819

lambda s: re.compile(r"(?:\r|^\s+)", re.MULTILINE).sub("", s).replace("\n", " ")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/util.py
# Line: 60

args = sig.lstrip("(").rstrip(")").split(", ")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/snowball.py
# Line: 1108

word.replace("\xE4", "a")
.replace("\xE1", "a")
.replace("\xEB", "e")
.replace("\xE9", "e")
.replace("\xED", "i")
.replace("\xEF", "i")
.replace("\xF6", "o")
.replace("\xF3", "o")
.replace("\xFC", "u")
.replace("\xFA", "u")

# ==================================================
# Line: 1419

word.replace("\u2019", "\x27")
.replace("\u2018", "\x27")
.replace("\u201B", "\x27")

# ==================================================
# Line: 2570

word = word.replace("I", "i").replace("U", "u").replace("Y", "y")

# ==================================================
# Line: 2756

word.replace("\xE4", "a")
.replace("\xF6", "o")
.replace("\xFC", "u")
.replace("U", "u")
.replace("Y", "y")

# ==================================================
# Line: 3398

word.replace("\xE1", "\xE0")
.replace("\xE9", "\xE8")
.replace("\xED", "\xEC")
.replace("\xF3", "\xF2")
.replace("\xFA", "\xF9")

# ==================================================
# Line: 3885

word.replace("\xE3", "a~")
.replace("\xF5", "o~")
.replace("q\xFC", "qu")
.replace("g\xFC", "gu")

# ==================================================
# Line: 5176

word = word.replace("i^a", "A").replace("i^u", "U").replace("e`", "E")

# ==================================================
# Occurrences: Lines 5193-5194 (2 instances)

r2 = r2.replace("A", "i^a").replace("U", "i^u").replace("E", "e`")

# ==================================================
# Line: 5215

word.replace("\u0410", "a")
.replace("\u0430", "a")
.replace("\u0411", "b")
.replace("\u0431", "b")
.replace("\u0412", "v")
.replace("\u0432", "v")
.replace("\u0413", "g")
.replace("\u0433", "g")
.replace("\u0414", "d")
.replace("\u0434", "d")
.replace("\u0415", "e")
.replace("\u0435", "e")
.replace("\u0401", "e")
.replace("\u0451", "e")
.replace("\u0416", "zh")
.replace("\u0436", "zh")
.replace("\u0417", "z")
.replace("\u0437", "z")
.replace("\u0418", "i")
.replace("\u0438", "i")
.replace("\u0419", "i`")
.replace("\u0439", "i`")
.replace("\u041A", "k")
.replace("\u043A", "k")
.replace("\u041B", "l")
.replace("\u043B", "l")
.replace("\u041C", "m")
.replace("\u043C", "m")
.replace("\u041D", "n")
.replace("\u043D", "n")
.replace("\u041E", "o")
.replace("\u043E", "o")
.replace("\u041F", "p")
.replace("\u043F", "p")
.replace("\u0420", "r")
.replace("\u0440", "r")
.replace("\u0421", "s")
.replace("\u0441", "s")
.replace("\u0422", "t")
.replace("\u0442", "t")
.replace("\u0423", "u")
.replace("\u0443", "u")
.replace("\u0424", "f")
.replace("\u0444", "f")
.replace("\u0425", "kh")
.replace("\u0445", "kh")
.replace("\u0426", "t^s")
.replace("\u0446", "t^s")
.replace("\u0427", "ch")
.replace("\u0447", "ch")
.replace("\u0428", "sh")
.replace("\u0448", "sh")
.replace("\u0429", "shch")
.replace("\u0449", "shch")
.replace("\u042A", "''")
.replace("\u044A", "''")
.replace("\u042B", "y")
.replace("\u044B", "y")
.replace("\u042C", "'")
.replace("\u044C", "'")
.replace("\u042D", "e`")
.replace("\u044D", "e`")
.replace("\u042E", "i^u")
.replace("\u044E", "i^u")
.replace("\u042F", "i^a")
.replace("\u044F", "i^a")

# ==================================================
# Line: 5302

word.replace("i^u", "\u044E")
.replace("i^a", "\u044F")
.replace("shch", "\u0449")
.replace("kh", "\u0445")
.replace("t^s", "\u0446")
.replace("ch", "\u0447")
.replace("e`", "\u044D")
.replace("i`", "\u0439")
.replace("sh", "\u0448")
.replace("k", "\u043A")
.replace("e", "\u0435")
.replace("zh", "\u0436")
.replace("a", "\u0430")
.replace("b", "\u0431")
.replace("v", "\u0432")
.replace("g", "\u0433")
.replace("d", "\u0434")
.replace("e", "\u0435")
.replace("z", "\u0437")
.replace("i", "\u0438")
.replace("l", "\u043B")
.replace("m", "\u043C")
.replace("n", "\u043D")
.replace("o", "\u043E")
.replace("p", "\u043F")
.replace("r", "\u0440")
.replace("s", "\u0441")
.replace("t", "\u0442")
.replace("u", "\u0443")
.replace("f", "\u0444")
.replace("''", "\u044A")
.replace("y", "\u044B")
.replace("'", "\u044C")

# ==================================================
# Line: 5729

word.replace("\xE1", "a")
.replace("\xE9", "e")
.replace("\xED", "i")
.replace("\xF3", "o")
.replace("\xFA", "u")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/porter.py
# Occurrences: Lines 713-715 (2 instances)

print("-Original-".center(70).replace(" ", "*").replace("-", " "))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/bcp47.py
# Line: 47

self.wiki_q = self.wiki_dict(fp.read().strip().split("\n")[1:])

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/sentiwordnet.py
# Line: 56

lines = self.open(self._fileids[0]).read().splitlines()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/util.py
# Line: 635

offset = re.compile(r"\s*").search(block, offset).end()

# ==================================================
