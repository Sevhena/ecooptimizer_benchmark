# long-lambda-expr snippets for nltk

# File: /root/ecooptimizer/nltk/nltk/classify/naivebayes.py
# Line: 188

key=lambda feature_: (
    minprob[feature_] / maxprob[feature_],
    feature_[0],
    feature_[1] in [None, False, True],
    str(feature_[1]).lower(),
),

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/boxer.py
# Line: 479

return lambda sent_index, word_indices: BoxerWhq(
    self.discourse_id, sent_index, word_indices, ans_types, d1, ref, d2
)

# ==================================================
# Line: 494

return lambda sent_index, word_indices: BoxerNamed(
    self.discourse_id, sent_index, word_indices, variable, name, type, sense
)

# ==================================================
# Line: 509

return lambda sent_index, word_indices: BoxerRel(
    self.discourse_id, sent_index, word_indices, var1, var2, rel, sense
)

# ==================================================
# Line: 538

lambda sent_index, word_indices: BoxerPred(
    self.discourse_id, sent_index, word_indices, arg, tok, "n", 0
)

# ==================================================
# Line: 652

return lambda sent_index, word_indices: BoxerCard(
    self.discourse_id, sent_index, word_indices, variable, value, type
)

# ==================================================
# Line: 663

return lambda sent_index, word_indices: BoxerProp(
    self.discourse_id, sent_index, word_indices, variable, drs
)

# ==================================================
# Line: 763

return lambda sent_index, word_indices: BoxerWhq(
    self.discourse_id, sent_index, word_indices, ans_types, d1, ref, d2
)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/relextract.py
# Line: 253

relfilter = lambda x: (
    x["subjclass"] == subjclass
    and len(x["filler"].split()) <= window
    and pattern.match(x["filler"])
    and x["objclass"] == objclass
)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/dependencygraph.py
# Line: 61

lambda: {
    "address": None,
    "word": None,
    "lemma": None,
    "ctag": None,
    "tag": None,
    "feats": None,
    "head": None,
    "deps": defaultdict(list),
    "rel": None,
}

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/metrics/distance.py
# Line: 277

lambda x, y: abs((1.0 / len(x)) - (1.0 / len(y))) * (label in x and label in y)
or 0.0 * (label not in x and label not in y)
or abs(1.0 / len(x)) * (label in x and label not in y)
or (1.0 / len(y)) * (label not in x and label in y)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/prettyprinter.py
# Line: 241

levels[n].sort(key=lambda n: max(tree[n].leaves()) - min(tree[n].leaves()))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tgrep.py
# Occurrences: Lines 424-441 (3 instances)

retval = lambda n, m=None, l=None: (
    hasattr(n, "parent")
    and bool(n.parent())
    and predicate(n.parent(), m, l)
)

# ==================================================
# Line: 447

lambda i: lambda n, m=None, l=None: (
    _istree(n)
    and bool(list(n))
    and 0 <= i < len(n)
    and predicate(n[i], m, l)
)

# ==================================================
# Occurrences: Lines 459-481 (3 instances)

lambda i: lambda n, m=None, l=None: (
    hasattr(n, "parent")
    and bool(n.parent())
    and 0 <= i < len(n.parent())
    and (n is n.parent()[i])
    and predicate(n.parent(), m, l)
)

# ==================================================
# Line: 487

lambda i: lambda n, m=None, l=None: (
    _istree(n)
    and bool(list(n))
    and 0 <= (i + len(n)) < len(n)
    and predicate(n[i + len(n)], m, l)
)

# ==================================================
# Occurrences: Lines 499-519 (3 instances)

lambda i: lambda n, m=None, l=None: (
    hasattr(n, "parent")
    and bool(n.parent())
    and 0 <= (i + len(n.parent())) < len(n.parent())
    and (n is n.parent()[i + len(n.parent())])
    and predicate(n.parent(), m, l)
)

# ==================================================
# Line: 537

retval = lambda n, m=None, l=None: any(
    (predicate(x, m, l) and n in _leftmost_descendants(x))
    for x in ancestors(n)
)

# ==================================================
# Line: 549

retval = lambda n, m=None, l=None: any(
    (predicate(x, m, l) and n in _rightmost_descendants(x))
    for x in ancestors(n)
)

# ==================================================
# Occurrences: Lines 585-619 (5 instances)

retval = lambda n, m=None, l=None: (
    hasattr(n, "parent")
    and bool(n.parent())
    and any(predicate(x, m, l) for x in n.parent() if x is not n)
)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/text.py
# Line: 441

finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/knbc.py
# Line: 159

knbc.morphs2str = lambda morphs: "/".join(
    "{}({})".format(m[0], m[1].split(" ")[2]) for m in morphs if m[0] != "EOS"
).encode("utf-8")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/framenet.py
# Line: 2642

key=lambda ferel: (
    ferel.type.ID,
    ferel.frameRelation.superFrameName,
    ferel.superFEName,
    ferel.frameRelation.subFrameName,
    ferel.subFEName,
),

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/collocations.py
# Line: 370

word_filter = lambda w: len(w) < 3 or w.lower() in ignored_words

# ==================================================
