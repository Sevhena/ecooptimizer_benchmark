# no-self-use snippets for nltk

# File: /root/ecooptimizer/nltk/nltk/classify/senna.py
# Line: 71

def executable(self, base_path):
    """
    The function that determines the system specific binary that should be
    used in the pipeline. In case, the system is not known the default senna binary will
    be used.
    """
    os_name = system()
    if os_name == "Linux":
        bits = architecture()[0]
        if bits == "64bit":
            return path.join(base_path, "senna-linux64")
        return path.join(base_path, "senna-linux32")
    if os_name == "Windows":
        return path.join(base_path, "senna-win32.exe")
    if os_name == "Darwin":
        return path.join(base_path, "senna-osx")
    return path.join(base_path, "senna")


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/classify/textcat.py
# Line: 71

def remove_punctuation(self, text):
    """Get rid of punctuation except apostrophes"""
    return re.sub(r"[^\P{P}\']+", "", text)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/classify/weka.py
# Line: 360

def _fmt_arff_val(self, fval):
    if fval is None:
        return "?"
    elif isinstance(fval, (bool, int)):
        return "%s" % fval
    elif isinstance(fval, float):
        return "%r" % fval
    else:
        return "%r" % fval



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/boxer.py
# Line: 239

def _find_binary(self, name, bin_dir, verbose=False):
    return find_binary(
        name,
        path_to_bin=bin_dir,
        env_vars=["CANDC"],
        url="http://svn.ask.it.usyd.edu.au/trac/candc/",
        binary_names=[name, name + ".exe"],
        verbose=verbose,
    )


# ==================================================
# Line: 249

def _call(self, input_str, binary, args=[], verbose=False):
    """
    Call the binary with the given input.

    :param input_str: A string whose contents are used as stdin.
    :param binary: The location of the binary to call
    :param args: A list of command-line arguments.
    :return: stdout
    """
    if verbose:
        print("Calling:", binary)
        print("Args:", args)
        print("Input:", input_str)
        print("Command:", binary + " " + " ".join(args))

    # Call via a subprocess
    if input_str is None:
        cmd = [binary] + args
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        cmd = 'echo "{}" | {} {}'.format(input_str, binary, " ".join(args))
        p = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
    stdout, stderr = p.communicate()

    if verbose:
        print("Return code:", p.returncode)
        if stdout:
            print("stdout:\n", stdout, "\n")
        if stderr:
            print("stderr:\n", stderr, "\n")
    if p.returncode != 0:
        raise Exception(
            "ERROR CALLING: {} {}\nReturncode: {}\n{}".format(
                binary, " ".join(args), p.returncode, stderr
            )
        )

    return stdout


# ==================================================
# Line: 332

def _parse_drs(self, drs_string, discourse_id, use_disc_id):
    return BoxerOutputDrsParser([None, discourse_id][use_disc_id]).parse(drs_string)



# ==================================================
# Line: 767

def _make_merge_expression(self, sent_index, word_indices, drs1, drs2):
    return BoxerDrs(drs1.refs + drs2.refs, drs1.conds + drs2.conds)


# ==================================================
# Line: 773

def _make_imp_expression(self, sent_index, word_indices, drs1, drs2):
    return BoxerDrs(drs1.refs, drs1.conds, drs2)


# ==================================================
# Line: 784

def _sent_and_word_indices(self, indices):
    """
    :return: list of (sent_index, word_indices) tuples
    """
    sent_indices = {(i / 1000) - 1 for i in indices if i >= 0}
    if sent_indices:
        pairs = []
        for sent_index in sent_indices:
            word_indices = [
                (i % 1000) - 1 for i in indices if sent_index == (i / 1000) - 1
            ]
            pairs.append((sent_index, word_indices))
        return pairs
    else:
        word_indices = [(i % 1000) - 1 for i in indices]
        return [(None, word_indices)]



# ==================================================
# Line: 1016

def _variables(self):
    """
    :return: (set<variables>, set<events>, set<propositions>)
    """
    return (set(), set(), set())


# ==================================================
# Line: 1022

def atoms(self):
    return set()


# ==================================================
# Line: 1028

def _clean_name(self, name):
    return name.replace("-", "_").replace("'", "_")


# ==================================================
# Line: 1210

def _pred(self):
    return "pred"



# ==================================================
# Line: 1261

def _pred(self):
    return "named"



# ==================================================
# Line: 1301

def _pred(self):
    return "rel"



# ==================================================
# Line: 1343

def _pred(self):
    return "prop"



# ==================================================
# Line: 1371

def _pred(self):
    return "eq"



# ==================================================
# Line: 1398

def _pred(self):
    return "card"



# ==================================================
# Line: 1435

def _pred(self):
    return "or"



# ==================================================
# Occurrences: Lines 1489-1494 (2 instances)

def _pred(self):
    return "whq"



# ==================================================
# Line: 1543

def _make_atom(self, pred, *args):
    accum = DrtVariableExpression(Variable(pred))
    for arg in args:
        accum = DrtApplicationExpression(
            accum, DrtVariableExpression(Variable(arg))
        )
    return accum


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/drt.py
# Occurrences: Lines 76-80 (2 instances)

def get_all_symbols(self):
    """This method exists to be overridden"""
    return DrtTokens.SYMBOLS


# ==================================================
# Line: 108

def make_NegatedExpression(self, expression):
    return DrtNegatedExpression(expression)


# ==================================================
# Occurrences: Lines 150-155 (2 instances)

def make_EqualityExpression(self, first, second):
    """This method serves as a hook for other logic parsers that
    have different equality expression classes"""
    return DrtEqualityExpression(first, second)


# ==================================================
# Occurrences: Lines 175-184 (4 instances)

def make_BooleanExpression(self, factory, first, second):
    return factory(first, second)


# ==================================================
# Occurrences: Lines 265-268 (2 instances)

def make_EqualityExpression(self, first, second):
    return DrtEqualityExpression(first, second)


# ==================================================
# Line: 483

def _order_ref_strings(self, refs):
    strings = ["%s" % ref for ref in refs]
    ind_vars = []
    func_vars = []
    event_vars = []
    other_vars = []
    for s in strings:
        if is_indvar(s):
            ind_vars.append(s)
        elif is_funcvar(s):
            func_vars.append(s)
        elif is_eventvar(s):
            event_vars.append(s)
        else:
            other_vars.append(s)
    return (
        sorted(other_vars)
        + sorted(event_vars, key=lambda v: int([v[2:], -1][len(v[2:]) == 0]))
        + sorted(func_vars, key=lambda v: (v[0], int([v[1:], -1][len(v[1:]) == 0])))
        + sorted(ind_vars, key=lambda v: (v[0], int([v[1:], -1][len(v[1:]) == 0])))
    )


# ==================================================
# Line: 753

def _pretty_subex(self, subex):
    return subex._pretty()



# ==================================================
# Line: 851

def getOp(self):
    return DrtTokens.DRS_CONC


# ==================================================
# Line: 925

def _str_subex(self, subex):
    s = "%s" % subex
    if isinstance(subex, DrtConcatenation) and subex.consequent is None:
        return s[1:-1]
    return s



# ==================================================
# Line: 1234

def _handle_VariableExpression(self, expression, command, x, y):
    return command("%s" % expression, x, y)


# ==================================================
# Line: 1383

def _get_centered_top(self, top, full_height, item_height):
    """Get the y-coordinate of the point that a figure should start at if
    its height is 'item_height' and it needs to be centered in an area that
    starts at 'top' and is 'full_height' tall."""
    return top + (full_height - item_height) / 2



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/chat80.py
# Line: 305

def _make_graph(self, s):
    """
    Convert a set of pairs into an adjacency linked list encoding of a graph.
    """
    g = {}
    for x, y in s:
        if x in g:
            g[x].append(y)
        else:
            g[x] = [y]
    return g


# ==================================================
# Line: 317

def _transclose(self, g):
    """
    Compute the transitive closure of a graph represented as a linked list.
    """
    for x in g:
        for adjacent in g[x]:
            # check that adjacent is a key
            if adjacent in g:
                for y in g[adjacent]:
                    if y not in g[x]:
                        g[x].append(y)
    return g


# ==================================================
# Line: 330

def _make_pairs(self, g):
    """
    Convert an adjacency linked list back into a set of pairs.
    """
    pairs = []
    for node in g:
        for adjacent in g[node]:
            pairs.append((node, adjacent))
    return set(pairs)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/glue.py
# Occurrences: Lines 96-99 (2 instances)

def make_VariableExpression(self, name):
    return VariableExpression(name)


# ==================================================
# Line: 348

def _lookup_semtype_option(self, semtype, node, depgraph):
    relationships = frozenset(
        depgraph.nodes[dep]["rel"].lower()
        for dep in chain.from_iterable(node["deps"].values())
        if depgraph.nodes[dep]["rel"].lower() not in OPTIONAL_RELATIONSHIPS
    )

    try:
        lookup = semtype[relationships]
    except KeyError:
        # An exact match is not found, so find the best match where
        # 'best' is defined as the glue entry whose relationship set has the
        # most relations of any possible relationship set that is a subset
        # of the actual depgraph
        best_match = frozenset()
        for relset_option in set(semtype) - {None}:
            if (
                len(relset_option) > len(best_match)
                and relset_option < relationships
            ):
                best_match = relset_option
        if not best_match:
            if None in semtype:
                best_match = None
            else:
                return None
        lookup = semtype[best_match]

    return lookup


# ==================================================
# Line: 378

def get_semtypes(self, node):
    """
    Based on the node, return a list of plausible semtypes in order of
    plausibility.
    """
    rel = node["rel"].lower()
    word = node["word"].lower()

    if rel == "spec":
        if word in SPEC_SEMTYPES:
            return [SPEC_SEMTYPES[word]]
        else:
            return [SPEC_SEMTYPES["default"]]
    elif rel in ["nmod", "vmod"]:
        return [node["tag"], rel]
    else:
        return [node["tag"]]


# ==================================================
# Line: 414

def get_meaning_formula(self, generic, word):
    """
    :param generic: A meaning formula string containing the
        parameter "<word>"
    :param word: The actual word to be replace "<word>"
    """
    word = word.replace(".", "")
    return generic.replace("<word>", word)


# ==================================================
# Line: 472

def get_label(self, node):
    """
    Pick an alphabetic character as identifier for an entity in the model.

    :param value: where to index into the list of characters
    :type value: int
    """
    value = node["address"]

    letter = [
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "a",
        "b",
        "c",
        "d",
        "e",
    ][value - 1]
    num = int(value) // 26
    if num > 0:
        return letter + str(num)
    else:
        return letter


# ==================================================
# Line: 515

def lookup_unique(self, rel, node, depgraph):
    """
    Lookup 'key'. There should be exactly one item in the associated relation.
    """
    deps = [
        depgraph.nodes[dep]
        for dep in chain.from_iterable(node["deps"].values())
        if depgraph.nodes[dep]["rel"].lower() == rel.lower()
    ]

    if len(deps) == 0:
        raise KeyError(
            "'{}' doesn't contain a feature '{}'".format(node["word"], rel)
        )
    elif len(deps) > 1:
        raise KeyError(
            "'{}' should only have one feature '{}'".format(node["word"], rel)
        )
    else:
        return deps[0]


# ==================================================
# Line: 536

def get_GlueFormula_factory(self):
    return GlueFormula



# ==================================================
# Line: 701

def get_pos_tagger(self):
    from nltk.corpus import brown

    regexp_tagger = RegexpTagger(
        [
            (r"^-?[0-9]+(\.[0-9]+)?$", "CD"),  # cardinal numbers
            (r"(The|the|A|a|An|an)$", "AT"),  # articles
            (r".*able$", "JJ"),  # adjectives
            (r".*ness$", "NN"),  # nouns formed from adjectives
            (r".*ly$", "RB"),  # adverbs
            (r".*s$", "NNS"),  # plural nouns
            (r".*ing$", "VBG"),  # gerunds
            (r".*ed$", "VBD"),  # past tense verbs
            (r".*", "NN"),  # nouns (default)
        ]
    )
    brown_train = brown.tagged_sents(categories="news")
    unigram_tagger = UnigramTagger(brown_train, backoff=regexp_tagger)
    bigram_tagger = BigramTagger(brown_train, backoff=unigram_tagger)
    trigram_tagger = TrigramTagger(brown_train, backoff=bigram_tagger)

    # Override particular words
    main_tagger = RegexpTagger(
        [(r"(A|a|An|an)$", "ex_quant"), (r"(Every|every|All|all)$", "univ_quant")],
        backoff=trigram_tagger,
    )

    return main_tagger



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/logic.py
# Line: 256

def get_all_symbols(self):
    """This method exists to be overridden"""
    return Tokens.SYMBOLS


# ==================================================
# Line: 278

def isvariable(self, tok):
    return tok not in Tokens.TOKENS


# ==================================================
# Line: 329

def make_NegatedExpression(self, expression):
    return NegatedExpression(expression)


# ==================================================
# Line: 444

def make_QuanifiedExpression(self, factory, variable, term):
    return factory(variable, term)


# ==================================================
# Line: 470

def make_EqualityExpression(self, first, second):
    """This method serves as a hook for other logic parsers that
    have different equality expression classes"""
    return EqualityExpression(first, second)


# ==================================================
# Line: 491

def get_BooleanExpression_factory(self, tok):
    """This method serves as a hook for other logic parsers that
    have different boolean operators"""
    if tok in Tokens.AND_LIST:
        return AndExpression
    elif tok in Tokens.OR_LIST:
        return OrExpression
    elif tok in Tokens.IMP_LIST:
        return ImpExpression
    elif tok in Tokens.IFF_LIST:
        return IffExpression
    else:
        return None


# ==================================================
# Line: 505

def make_BooleanExpression(self, factory, first, second):
    return factory(first, second)


# ==================================================
# Occurrences: Lines 543-549 (3 instances)

def make_ApplicationExpression(self, function, argument):
    return ApplicationExpression(function, argument)


# ==================================================
# Line: 782

def str(self):
    return "IND"



# ==================================================
# Line: 790

def str(self):
    return "BOOL"



# ==================================================
# Line: 798

def str(self):
    return "EVENT"



# ==================================================
# Line: 1209

def make_VariableExpression(self, variable):
    return VariableExpression(variable)



# ==================================================
# Line: 1507

def _get_type(self):
    return ENTITY_TYPE


# ==================================================
# Occurrences: Lines 1753-1763 (3 instances)

def getQuantifier(self):
    return Tokens.EXISTS



# ==================================================
# Line: 1855

def _str_subex(self, subex):
    return "%s" % subex



# ==================================================
# Line: 1876

def getOp(self):
    return Tokens.AND


# ==================================================
# Line: 1889

def getOp(self):
    return Tokens.OR


# ==================================================
# Line: 1902

def getOp(self):
    return Tokens.IMP



# ==================================================
# Line: 1909

def getOp(self):
    return Tokens.IFF



# ==================================================
# Line: 1928

def getOp(self):
    return Tokens.EQ



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/draw/table.py
# Line: 198

def _resize_column_buttonrelease_cb(self, event):
    event.widget.unbind("<ButtonRelease-%d>" % event.num)
    event.widget.unbind("<Motion>")


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/draw/util.py
# Line: 2049

def find_dimentions(self, text, width, height):
    lines = text.split("\n")
    if width is None:
        maxwidth = max(len(line) for line in lines)
        width = min(maxwidth, 80)

    # Now, find height.
    height = 0
    for line in lines:
        while len(line) > width:
            brk = line[:width].rfind(" ")
            line = line[brk:]
            height += 1
        height += 1
    height = min(height, 25)

    return (width, height)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sentiment/vader.py
# Line: 235

def normalize(self, score, alpha=15):
    """
    Normalize the score to be between -1 and 1 using an alpha that
    approximates the max expected value
    """
    norm_score = score / math.sqrt((score * score) + alpha)
    return norm_score


# ==================================================
# Line: 313

def allcap_differential(self, words):
    """
    Check whether just some words in the input are ALL CAPS

    :param list words: The words to inspect
    :returns: `True` if some but not all items in `words` are ALL CAPS
    """
    is_different = False
    allcap_words = 0
    for word in words:
        if word.isupper():
            allcap_words += 1
    cap_differential = len(words) - allcap_words
    if 0 < cap_differential < len(words):
        is_different = True
    return is_different



# ==================================================
# Line: 458

def _but_check(self, words_and_emoticons, sentiments):
    words_and_emoticons = [w_e.lower() for w_e in words_and_emoticons]
    but = {"but"} & set(words_and_emoticons)
    if but:
        bi = words_and_emoticons.index(next(iter(but)))
        for sidx, sentiment in enumerate(sentiments):
            if sidx < bi:
                sentiments[sidx] = sentiment * 0.5
            elif sidx > bi:
                sentiments[sidx] = sentiment * 1.5
    return sentiments


# ==================================================
# Line: 555

def _amplify_ep(self, text):
    # check for added emphasis resulting from exclamation points (up to 4 of them)
    ep_count = text.count("!")
    if ep_count > 4:
        ep_count = 4
    # (empirically derived mean sentiment intensity rating increase for
    # exclamation points)
    ep_amplifier = ep_count * 0.292
    return ep_amplifier


# ==================================================
# Line: 565

def _amplify_qm(self, text):
    # check for added emphasis resulting from question marks (2 or 3+)
    qm_count = text.count("?")
    qm_amplifier = 0
    if qm_count > 1:
        if qm_count <= 3:
            # (empirically derived mean sentiment intensity rating increase for
            # question marks)
            qm_amplifier = qm_count * 0.18
        else:
            qm_amplifier = 0.96
    return qm_amplifier


# ==================================================
# Line: 578

def _sift_sentiment_scores(self, sentiments):
    # want separate positive versus negative sentiment scores
    pos_sum = 0.0
    neg_sum = 0.0
    neu_count = 0
    for sentiment_score in sentiments:
        if sentiment_score > 0:
            pos_sum += (
                float(sentiment_score) + 1
            )  # compensates for neutral words that are counted as 1
        if sentiment_score < 0:
            neg_sum += (
                float(sentiment_score) - 1
            )  # when used with math.fabs(), compensates for neutrals
        if sentiment_score == 0:
            neu_count += 1
    return pos_sum, neg_sum, neu_count


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sentiment/sentiment_analyzer.py
# Line: 37

def all_words(self, documents, labeled=None):
    """
    Return all words/tokens from the documents (with duplicates).

    :param documents: a list of (words, label) tuples.
    :param labeled: if `True`, assume that each document is represented by a
        (words, label) tuple: (list(str), str). If `False`, each document is
        considered as being a simple list of strings: list(str).
    :rtype: list(str)
    :return: A list of all words/tokens in `documents`.
    """
    all_words = []
    if labeled is None:
        labeled = documents and isinstance(documents[0], tuple)
    if labeled:
        for words, _sentiment in documents:
            all_words.extend(words)
    elif not labeled:
        for words in documents:
            all_words.extend(words)
    return all_words


# ==================================================
# Line: 75

def unigram_word_feats(self, words, top_n=None, min_freq=0):
    """
    Return most common top_n word features.

    :param words: a list of words/tokens.
    :param top_n: number of best words/tokens to use, sorted by frequency.
    :rtype: list(str)
    :return: A list of `top_n` words/tokens (with no duplicates) sorted by
        frequency.
    """
    # Stopwords are not removed
    unigram_feats_freqs = FreqDist(word for word in words)
    return [
        w
        for w, f in unigram_feats_freqs.most_common(top_n)
        if unigram_feats_freqs[w] > min_freq
    ]


# ==================================================
# Line: 93

def bigram_collocation_feats(
    self, documents, top_n=None, min_freq=3, assoc_measure=BigramAssocMeasures.pmi

# ==================================================
# Line: 185

def save_file(self, content, filename):
    """
    Store `content` in `filename`. Can be used to store a SentimentAnalyzer.
    """
    print("Saving", filename, file=sys.stderr)
    with open(filename, "wb") as storage_file:
        import pickle

        # The protocol=2 parameter is for python2 compatibility
        pickle.dump(content, storage_file, protocol=2)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/nemo_app.py
# Line: 68

def initScrollText(self, frm, txt, contents):
    scl = Scrollbar(frm)
    scl.config(command=txt.yview)
    scl.pack(side="right", fill="y")
    txt.pack(side="left", expand=True, fill="x")
    txt.config(yscrollcommand=scl.set)
    txt.insert("1.0", contents)
    frm.pack(fill="x")
    Frame(height=2, bd=1, relief="ridge").pack(fill="x")


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/chartparser_app.py
# Line: 672

def _init_divider(self, root):
    divider = Frame(root, border=2, relief="sunken")
    divider.pack(side="top", fill="x", ipady=2)


# ==================================================
# Line: 1094

def _sb_canvas(self, root, expand="y", fill="both", side="bottom"):
    """
    Helper for __init__: construct a canvas with a scrollbar.
    """
    cframe = Frame(root, relief="sunk", border=2)
    cframe.pack(fill=fill, expand=expand, side=side)
    canvas = Canvas(cframe, background="#e0e0e0")

    # Give the canvas a scrollbar.
    sb = Scrollbar(cframe, orient="vertical")
    sb.pack(side="right", fill="y")
    canvas.pack(side="left", fill=fill, expand="yes")

    # Connect the scrollbars to the canvas.
    sb["command"] = canvas.yview
    canvas["yscrollcommand"] = sb.set

    return (sb, canvas)


# ==================================================
# Line: 2248

def about(self, *e):
    ABOUT = "NLTK Chart Parser Application\n" + "Written by Edward Loper"
    showinfo("About: Chart Parser Application", ABOUT)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/chunkparser_app.py
# Line: 308

def normalize_grammar(self, grammar):
    # Strip comments
    grammar = re.sub(r"((\\.|[^#])*)(#.*)?", r"\1", grammar)
    # Normalize whitespace
    grammar = re.sub(" +", " ", grammar)
    grammar = re.sub(r"\n\s+", r"\n", grammar)
    grammar = grammar.strip()
    # [xx] Hack: automatically backslash $!
    grammar = re.sub(r"([^\\])\$", r"\1\\$", grammar)
    return grammar


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/rdparser_app.py
# Line: 446

def _get(self, widget, treeloc):
    for i in treeloc:
        widget = widget.subtrees()[i]
    if isinstance(widget, TreeSegmentWidget):
        widget = widget.label()
    return widget


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/bleu_score.py
# Line: 561

def method0(self, p_n, *args, **kwargs):
    """
    No smoothing.
    """
    p_n_new = []
    for i, p_i in enumerate(p_n):
        if p_i.numerator != 0:
            p_n_new.append(p_i)
        else:
            _msg = str(
                "\nThe hypothesis contains 0 counts of {}-gram overlaps.\n"
                "Therefore the BLEU score evaluates to 0, independently of\n"
                "how many N-gram overlaps of lower order it contains.\n"
                "Consider using lower n-gram order or use "
                "SmoothingFunction()"
            ).format(i + 1)
            warnings.warn(_msg)
            # When numerator==0 where denonminator==0 or !=0, the result
            # for the precision score should be equal to 0 or undefined.
            # Due to BLEU geometric mean computation in logarithm space,
            # we we need to take the return sys.float_info.min such that
            # math.log(sys.float_info.min) returns a 0 precision score.
            p_n_new.append(sys.float_info.min)
    return p_n_new


# ==================================================
# Line: 599

def method2(self, p_n, *args, **kwargs):
    """
    Smoothing method 2: Add 1 to both numerator and denominator from
    Chin-Yew Lin and Franz Josef Och (2004) ORANGE: a Method for
    Evaluating Automatic Evaluation Metrics for Machine Translation.
    In COLING 2004.
    """
    return [
        (
            Fraction(p_n[i].numerator + 1, p_n[i].denominator + 1, _normalize=False)
            if i != 0
            else p_n[0]
        )
        for i in range(len(p_n))
    ]


# ==================================================
# Line: 615

def method3(self, p_n, *args, **kwargs):
    """
    Smoothing method 3: NIST geometric sequence smoothing
    The smoothing is computed by taking 1 / ( 2^k ), instead of 0, for each
    precision score whose matching n-gram count is null.
    k is 1 for the first 'n' value for which the n-gram match count is null/

    For example, if the text contains:

    - one 2-gram match
    - and (consequently) two 1-gram matches

    the n-gram count for each individual precision score would be:

    - n=1  =>  prec_count = 2     (two unigrams)
    - n=2  =>  prec_count = 1     (one bigram)
    - n=3  =>  prec_count = 1/2   (no trigram,  taking 'smoothed' value of 1 / ( 2^k ), with k=1)
    - n=4  =>  prec_count = 1/4   (no fourgram, taking 'smoothed' value of 1 / ( 2^k ), with k=2)
    """
    incvnt = 1  # From the mteval-v13a.pl, it's referred to as k.
    for i, p_i in enumerate(p_n):
        if p_i.numerator == 0:
            p_n[i] = 1 / (2**incvnt * p_i.denominator)
            incvnt += 1
    return p_n


# ==================================================
# Line: 662

def method5(self, p_n, references, hypothesis, hyp_len=None, *args, **kwargs):
    """
    Smoothing method 5:
    The matched counts for similar values of n should be similar. To a
    calculate the n-gram matched count, it averages the n−1, n and n+1 gram
    matched counts.
    """
    hyp_len = hyp_len if hyp_len else len(hypothesis)
    m = {}
    # Requires an precision value for an addition ngram order.
    p_n_plus1 = p_n + [modified_precision(references, hypothesis, 5)]
    m[-1] = p_n[0] + 1
    for i, p_i in enumerate(p_n):
        p_n[i] = (m[i - 1] + p_i + p_n_plus1[i + 1]) / 3
        m[i] = p_n[i]
    return p_n


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm_model.py
# Line: 272

def neighboring(self, alignment_info, j_pegged=None):
    """
    Determine the neighbors of ``alignment_info``, obtained by
    moving or swapping one alignment point

    :param j_pegged: If specified, neighbors that have a different
        alignment point from j_pegged will not be considered
    :type j_pegged: int

    :return: A set neighboring alignments represented by their
        ``AlignmentInfo``
    :rtype: set(AlignmentInfo)
    """
    neighbors = set()

    l = len(alignment_info.src_sentence) - 1  # exclude NULL
    m = len(alignment_info.trg_sentence) - 1
    original_alignment = alignment_info.alignment
    original_cepts = alignment_info.cepts

    for j in range(1, m + 1):
        if j != j_pegged:
            # Add alignments that differ by one alignment point
            for i in range(0, l + 1):
                new_alignment = list(original_alignment)
                new_cepts = deepcopy(original_cepts)
                old_i = original_alignment[j]

                # update alignment
                new_alignment[j] = i

                # update cepts
                insort_left(new_cepts[i], j)
                new_cepts[old_i].remove(j)

                new_alignment_info = AlignmentInfo(
                    tuple(new_alignment),
                    alignment_info.src_sentence,
                    alignment_info.trg_sentence,
                    new_cepts,
                )
                neighbors.add(new_alignment_info)

    for j in range(1, m + 1):
        if j != j_pegged:
            # Add alignments that have two alignment points swapped
            for other_j in range(1, m + 1):
                if other_j != j_pegged and other_j != j:
                    new_alignment = list(original_alignment)
                    new_cepts = deepcopy(original_cepts)
                    other_i = original_alignment[other_j]
                    i = original_alignment[j]

                    # update alignments
                    new_alignment[j] = other_i
                    new_alignment[other_j] = i

                    # update cepts
                    new_cepts[other_i].remove(other_j)
                    insort_left(new_cepts[other_i], j)
                    new_cepts[i].remove(j)
                    insort_left(new_cepts[i], other_j)

                    new_alignment_info = AlignmentInfo(
                        tuple(new_alignment),
                        alignment_info.src_sentence,
                        alignment_info.trg_sentence,
                        new_cepts,
                    )
                    neighbors.add(new_alignment_info)

    return neighbors


# ==================================================
# Line: 370

def prob_t_a_given_s(self, alignment_info):
    """
    Probability of target sentence and an alignment given the
    source sentence

    All required information is assumed to be in ``alignment_info``
    and self.

    Derived classes should override this method
    """
    return 0.0



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/stack_decoder.py
# Line: 261

def future_score(self, hypothesis, future_score_table, sentence_length):
    """
    Determines the approximate score for translating the
    untranslated words in ``hypothesis``
    """
    score = 0.0
    for span in hypothesis.untranslated_spans(sentence_length):
        score += future_score_table[span[0]][span[1]]
    return score


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tabdata.py
# Line: 18

def list2txt(self, s):
    return "\n".join(s)


# ==================================================
# Line: 24

def tup2tab(self, tup):
    return "\t".join(tup)


# ==================================================
# Occurrences: Lines 40-46 (3 instances)

def txt2list(self, f):
    return [rm_nl(x) for x in f]


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/transitionparser.py
# Line: 62

def _check_informative(self, feat, flag=False):
    """
    Check whether a feature is informative
    The flag control whether "_" is informative or not
    """
    if feat is None:
        return False
    if feat == "":
        return False
    if flag is False:
        if feat == "_":
            return False
    return True


# ==================================================
# Line: 277

def shift(self, conf):
    """
    Note that the algorithm for shift is the SAME for arc-standard and arc-eager

    :param configuration: is the current configuration
    :return: A new configuration or -1 if the pre-condition is not satisfied
    """
    if len(conf.buffer) <= 0:
        return -1
    idx_wi = conf.buffer.pop(0)
    conf.stack.append(idx_wi)



# ==================================================
# Line: 314

def _get_dep_relation(self, idx_parent, idx_child, depgraph):
    p_node = depgraph.nodes[idx_parent]
    c_node = depgraph.nodes[idx_child]

    if c_node["word"] is None:
        return None  # Root word

    if c_node["head"] == p_node["address"]:
        return c_node["rel"]
    else:
        return None


# ==================================================
# Line: 342

def _is_projective(self, depgraph):
    arc_list = []
    for key in depgraph.nodes:
        node = depgraph.nodes[key]

        if "head" in node:
            childIdx = node["address"]
            parentIdx = node["head"]
            if parentIdx is not None:
                arc_list.append((parentIdx, childIdx))

    for parentIdx, childIdx in arc_list:
        # Ensure that childIdx < parentIdx
        if childIdx > parentIdx:
            temp = childIdx
            childIdx = parentIdx
            parentIdx = temp
        for k in range(childIdx + 1, parentIdx):
            for m in range(len(depgraph.nodes)):
                if (m < childIdx) or (m > parentIdx):
                    if (k, m) in arc_list:
                        return False
                    if (m, k) in arc_list:
                        return False
    return True


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/nonprojectivedependencyparser.py
# Line: 285

def collapse_nodes(self, new_node, cycle_path, g_graph, b_graph, c_graph):
    """
    Takes a list of nodes that have been identified to belong to a cycle,
    and collapses them into on larger node.  The arcs of all nodes in
    the graph must be updated to account for this.

    :type new_node: Node.
    :param new_node: A Node (Dictionary) to collapse the cycle nodes into.
    :type cycle_path: A list of integers.
    :param cycle_path: A list of node addresses, each of which is in the cycle.
    :type g_graph, b_graph, c_graph: DependencyGraph
    :param g_graph, b_graph, c_graph: Graphs which need to be updated.
    """
    logger.debug("Collapsing nodes...")
    # Collapse all cycle nodes into v_n+1 in G_Graph
    for cycle_node_index in cycle_path:
        g_graph.remove_by_address(cycle_node_index)
    g_graph.add_node(new_node)
    g_graph.redirect_arcs(cycle_path, new_node["address"])


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/corenlp.py
# Line: 591

def make_tree(self, result):
    return Tree.fromstring(result["parse"])



# ==================================================
# Line: 776

def make_tree(self, result):
    return DependencyGraph(
        (
            " ".join(n_items[1:])  # NLTK expects an iterable of strings...
            for n_items in sorted(transform(result))
        ),
        cell_separator=" ",  # To make sure that a non-breaking space is kept inside of a token.
    )



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/viterbi.py
# Line: 315

def _trace_lexical_insertion(self, token, index, width):
    str = "   Insert: |" + "." * index + "=" + "." * (width - index - 1) + "| "
    str += f"{token}"
    print(str)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/recursivedescent.py
# Line: 229

def _production_to_tree(self, production):
    """
    :rtype: Tree
    :return: The Tree that is licensed by ``production``.
        In particular, given the production ``[lhs -> elt[1] ... elt[n]]``
        return a tree that has a node ``lhs.symbol``, and
        ``n`` children.  For each nonterminal element
        ``elt[i]`` in the production, the tree token has a
        childless subtree with node value ``elt[i].symbol``; and
        for each terminal element ``elt[j]``, the tree token has
        a leaf token with type ``elt[j]``.

    :param production: The CFG production that licenses the tree
        token that should be returned.
    :type production: Production
    """
    children = []
    for elt in production.rhs():
        if isinstance(elt, Nonterminal):
            children.append(Tree(elt.symbol(), []))
        else:
            # This will be matched.
            children.append(elt)
    return Tree(production.lhs().symbol(), children)


# ==================================================
# Line: 382

def _freeze(self, tree):
    c = tree.copy()
    #        for pos in c.treepositions('leaves'):
    #            c[pos] = c[pos].freeze()
    return ImmutableTree.convert(c)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/stanford.py
# Line: 336

def _make_tree(self, result):
    return Tree.fromstring(result)



# ==================================================
# Line: 401

def _make_tree(self, result):
    return DependencyGraph(result, top_relation_label="root")



# ==================================================
# Line: 467

def _make_tree(self, result):
    return DependencyGraph(result, top_relation_label="ROOT")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/shiftreduce.py
# Line: 123

def _match_rhs(self, rhs, rightmost_stack):
    """
    :rtype: bool
    :return: true if the right hand side of a CFG production
        matches the rightmost elements of the stack.  ``rhs``
        matches ``rightmost_stack`` if they are the same length,
        and each element of ``rhs`` matches the corresponding
        element of ``rightmost_stack``.  A nonterminal element of
        ``rhs`` matches any Tree whose node value is equal
        to the nonterminal's symbol.  A terminal element of ``rhs``
        matches any string whose type is equal to the terminal.
    :type rhs: list(terminal and Nonterminal)
    :param rhs: The right hand side of a CFG production.
    :type rightmost_stack: list(string and Tree)
    :param rightmost_stack: The rightmost elements of the parser's
        stack.
    """

    if len(rightmost_stack) != len(rhs):
        return False
    for i in range(len(rightmost_stack)):
        if isinstance(rightmost_stack[i], Tree):
            if not isinstance(rhs[i], Nonterminal):
                return False
            if rightmost_stack[i].label() != rhs[i].symbol():
                return False
        else:
            if isinstance(rhs[i], Nonterminal):
                return False
            if rightmost_stack[i] != rhs[i]:
                return False
    return True


# ==================================================
# Line: 216

def _trace_stack(self, stack, remaining_text, marker=" "):
    """
    Print trace output displaying the given stack and text.

    :rtype: None
    :param marker: A character that is printed to the left of the
        stack.  This is used with trace level 2 to print 'S'
        before shifted stacks and 'R' before reduced stacks.
    """
    s = "  " + marker + " [ "
    for elt in stack:
        if isinstance(elt, Tree):
            s += repr(Nonterminal(elt.label())) + " "
        else:
            s += repr(elt) + " "
    s += "* " + " ".join(remaining_text) + "]"
    print(s)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/pchart.py
# Line: 51

def prob(self):
    return 1.0



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/dependencygraph.py
# Line: 380

def _word(self, node, filter=True):
    w = node["word"]
    if filter:
        if w != ",":
            return w
    return w


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/featurechart.py
# Line: 118

def _bind(self, nt, bindings):
    if not isinstance(nt, FeatStructNonterminal):
        return nt
    return nt.substitute_bindings(bindings)


# ==================================================
# Line: 222

def _get_type_if_possible(self, item):
    """
    Helper function which returns the ``TYPE`` feature of the ``item``,
    if it exists, otherwise it returns the ``item`` itself
    """
    if isinstance(item, dict) and TYPE in item:
        return item[TYPE]
    else:
        return item


# ==================================================
# Line: 578

def inst_vars(self, edge):
    return {
        var: logic.unique_variable()
        for var in edge.lhs().variables()
        if var.name.startswith("@")
    }



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/earleychart.py
# Line: 181

def _apply_incomplete(self, chart, grammar, left_edge):
    end = left_edge.end()
    # When the chart is incremental, we only have to look for
    # empty complete edges here.
    for right_edge in chart.select(
        start=end, end=end, is_complete=True, lhs=left_edge.nextsym()
    ):
        new_edge = left_edge.move_dot_forward(right_edge.end())
        if chart.insert_with_backpointer(new_edge, left_edge, right_edge):
            yield new_edge



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/evaluate.py
# Line: 79

def _remove_punct(self, inStr):
    """
    Function to remove punctuation from Unicode string.
    :param input: the input string
    :return: Unicode string after remove all punctuation
    """
    punc_cat = {"Pc", "Pd", "Ps", "Pe", "Pi", "Pf", "Po"}
    return "".join(x for x in inStr if unicodedata.category(x) not in punc_cat)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/chart.py
# Line: 1072

def _apply_complete(self, chart, grammar, right_edge):
    for left_edge in chart.select(
        end=right_edge.start(), is_complete=False, nextsym=right_edge.lhs()
    ):
        new_edge = left_edge.move_dot_forward(right_edge.end())
        if chart.insert_with_backpointer(new_edge, left_edge, right_edge):
            yield new_edge


# ==================================================
# Line: 1080

def _apply_incomplete(self, chart, grammar, left_edge):
    for right_edge in chart.select(
        start=left_edge.end(), is_complete=True, lhs=left_edge.nextsym()
    ):
        new_edge = left_edge.move_dot_forward(right_edge.end())
        if chart.insert_with_backpointer(new_edge, left_edge, right_edge):
            yield new_edge



# ==================================================
# Line: 1408

def _trace_new_edges(self, chart, rule, new_edges, trace, edge_width):
    if not trace:
        return
    print_rule_header = trace > 1
    for edge in new_edges:
        if print_rule_header:
            print("%s:" % rule)
            print_rule_header = False
        print(chart.pretty_format_edge(edge, edge_width))


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/immutable.py
# Line: 84

def _frozen_class(self):
    return ImmutableProbabilisticTree


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/probabilistic.py
# Line: 28

def _frozen_class(self):
    return ImmutableProbabilisticTree


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/tree.py
# Line: 560

def _frozen_class(self):
    from nltk.tree.immutable import ImmutableTree

    return ImmutableTree


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/featstruct.py
# Line: 1879

def subst(self, v, bindings):
    if isinstance(v, SubstituteBindingsI):
        return v.substitute_bindings(bindings)
    else:
        return bindings.get(v, v)



# ==================================================
# Occurrences: Lines 2054-2057 (2 instances)

def read_value(self, s, position, reentrances, parser):
    return parser.read_value(s, position, reentrances)


# ==================================================
# Line: 2442

def _error(self, s, expected, position):
    lines = s.split("\n")
    while position > len(lines[0]):
        position -= len(lines.pop(0)) + 1  # +1 for the newline.
    estr = (
        "Error parsing feature structure\n    "
        + lines[0]
        + "\n    "
        + " " * position
        + "^ "
        + "Expected %s" % expected
    )
    raise ValueError(estr)


# ==================================================
# Occurrences: Lines 2490-2497 (3 instances)

def read_str_value(self, s, position, reentrances, match):
    return read_str(s, position)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/downloader.py
# Line: 632

def _num_packages(self, item):
    if isinstance(item, Package):
        return 1
    else:
        return len(item.packages)


# ==================================================
# Line: 1034

def default_download_dir(self):
    """
    Return the directory to which packages will be downloaded by
    default.  This value can be overridden using the constructor,
    or on a case-by-case basis using the ``download_dir`` argument when
    calling ``download()``.

    On Windows, the default download directory is
    ``PYTHONHOME/lib/nltk``, where *PYTHONHOME* is the
    directory containing Python, e.g. ``C:\\Python25``.

    On all other platforms, the default directory is the first of
    the following which exists or which can be created with write
    permission: ``/usr/share/nltk_data``, ``/usr/local/share/nltk_data``,
    ``/usr/lib/nltk_data``, ``/usr/local/lib/nltk_data``, ``~/nltk_data``.
    """
    # Check if we are on GAE where we cannot write into filesystem.
    if "APPENGINE_RUNTIME" in os.environ:
        return

    # Check if we have sufficient permissions to install in a
    # variety of system-wide locations.
    for nltkdir in nltk.data.path:
        if os.path.exists(nltkdir) and nltk.internals.is_writable(nltkdir):
            return nltkdir

    # On Windows, use %APPDATA%
    if sys.platform == "win32" and "APPDATA" in os.environ:
        homedir = os.environ["APPDATA"]

    # Otherwise, install in the user's home directory.
    else:
        homedir = os.path.expanduser("~/")
        if homedir == "~/":
            raise ValueError("Could not find a default download directory")

    # append "nltk_data" to the home directory
    return os.path.join(homedir, "nltk_data")


# ==================================================
# Line: 1121

def _simple_interactive_menu(self, *options):
    print("-" * 75)
    spc = (68 - sum(len(o) for o in options)) // (len(options) - 1) * " "
    print("    " + spc.join(options))
    print("-" * 75)


# ==================================================
# Line: 1230

def _simple_interactive_help(self):
    print()
    print("Commands:")
    print(
        "  d) Download a package or collection     u) Update out of date packages"
    )
    print("  l) List packages & collections          h) Help")
    print("  c) View & Modify Configuration          q) Quit")


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/probability.py
# Line: 562

def discount(self):
    """
    Return the ratio by which counts are discounted on average: c*/c

    :rtype: float
    """
    return 0.0


# ==================================================
# Line: 1480

def _variance(self, r, nr, nr_1):
    r = float(r)
    nr = float(nr)
    nr_1 = float(nr_1)
    return (r + 1.0) ** 2 * (nr_1 / nr**2) * (1.0 + nr_1 / nr)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/senna.py
# Line: 78

def bio_to_chunks(self, tagged_sent, chunk_type):
    """
    Extracts the chunks in a BIO chunk-tagged sentence.

    >>> from nltk.tag import SennaChunkTagger
    >>> chktagger = SennaChunkTagger('/usr/share/senna-v3.0')  # doctest: +SKIP
    >>> sent = 'What is the airspeed of an unladen swallow ?'.split()
    >>> tagged_sent = chktagger.tag(sent)  # doctest: +SKIP
    >>> tagged_sent  # doctest: +SKIP
    [('What', 'B-NP'), ('is', 'B-VP'), ('the', 'B-NP'), ('airspeed', 'I-NP'),
    ('of', 'B-PP'), ('an', 'B-NP'), ('unladen', 'I-NP'), ('swallow', 'I-NP'),
    ('?', 'O')]
    >>> list(chktagger.bio_to_chunks(tagged_sent, chunk_type='NP'))  # doctest: +SKIP
    [('What', '0'), ('the airspeed', '2-3'), ('an unladen swallow', '5-6-7')]

    :param tagged_sent: A list of tuples of word and BIO chunk tag.
    :type tagged_sent: list(tuple)
    :param tagged_sent: The chunk tag that users want to extract, e.g. 'NP' or 'VP'
    :type tagged_sent: str

    :return: An iterable of tuples of chunks that users want to extract
      and their corresponding indices.
    :rtype: iter(tuple(str))
    """
    current_chunk = []
    current_chunk_position = []
    for idx, word_pos in enumerate(tagged_sent):
        word, pos = word_pos
        if "-" + chunk_type in pos:  # Append the word to the current_chunk.
            current_chunk.append(word)
            current_chunk_position.append(idx)
        else:
            if current_chunk:  # Flush the full chunk when out of an NP.
                _chunk_str = " ".join(current_chunk)
                _chunk_pos_str = "-".join(map(str, current_chunk_position))
                yield _chunk_str, _chunk_pos_str
                current_chunk = []
                current_chunk_position = []
    if current_chunk:  # Flush the last chunk.
        yield " ".join(current_chunk), "-".join(map(str, current_chunk_position))



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/brill_trainer.py
# Line: 574

 def _trace_header(self):
     print(
         """
        B      |
S   F   r   O  |        Score = Fixed - Broken
c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
e   d   n   r  |  e

# ==================================================
# Occurrences: Lines 615-620 (2 instances)

def _trace_apply(self, num_updates):
    prefix = " " * 18 + "|"
    print(prefix)
    print(prefix, f"Applying rule to {num_updates} positions.")


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/hmm.py
# Line: 513

def _sample_probdist(self, probdist, p, samples):
    cum_p = 0
    for sample in samples:
        add_p = probdist.prob(sample)
        if cum_p <= p <= cum_p + add_p:
            return sample
        cum_p += add_p
    raise Exception("Invalid probability distribution - " "does not sum to one")


# ==================================================
# Line: 883

def _baum_welch_step(self, sequence, model, symbol_to_number):
    N = len(model._states)
    M = len(model._symbols)
    T = len(sequence)

    # compute forward and backward probabilities
    alpha = model._forward_probability(sequence)
    beta = model._backward_probability(sequence)

    # find the log probability of the sequence
    lpk = logsumexp2(alpha[T - 1])

    A_numer = _ninf_array((N, N))
    B_numer = _ninf_array((N, M))
    A_denom = _ninf_array(N)
    B_denom = _ninf_array(N)

    transitions_logprob = model._transitions_matrix().T

    for t in range(T):
        symbol = sequence[t][_TEXT]  # not found? FIXME
        next_symbol = None
        if t < T - 1:
            next_symbol = sequence[t + 1][_TEXT]  # not found? FIXME
        xi = symbol_to_number[symbol]

        next_outputs_logprob = model._outputs_vector(next_symbol)
        alpha_plus_beta = alpha[t] + beta[t]

        if t < T - 1:
            numer_add = (
                transitions_logprob
                + next_outputs_logprob
                + beta[t + 1]
                + alpha[t].reshape(N, 1)
            )
            A_numer = np.logaddexp2(A_numer, numer_add)
            A_denom = np.logaddexp2(A_denom, alpha_plus_beta)
        else:
            B_denom = np.logaddexp2(A_denom, alpha_plus_beta)

        B_numer[:, xi] = np.logaddexp2(B_numer[:, xi], alpha_plus_beta)

    return lpk, A_numer, A_denom, B_numer, B_denom


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/api.py
# Line: 285

def _check_params(self, train, model):
    if (train and model) or (not train and not model):
        raise ValueError("Must specify either training data or trained model.")



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/tnt.py
# Line: 254

def _safe_div(self, v1, v2):
    """
    Safe floating point division function, does not allow division by 0
    returns -1 if the denominator is 0
    """
    if v2 == 0:
        return -1
    else:
        return v1 / v2


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/perceptron.py
# Line: 52

def _softmax(self, scores):
    s = np.fromiter(scores.values(), dtype=float)
    exps = np.exp(s)
    return exps / np.sum(exps)


# ==================================================
# Line: 302

def normalize(self, word):
    """
    Normalization used in pre-processing.
    - All words are lower cased
    - Groups of digits of length 4 are represented as !YEAR;
    - Other digits are represented as !DIGITS

    :rtype: str
    """
    if "-" in word and word[0] != "-":
        return "!HYPHEN"
    if word.isdigit() and len(word) == 4:
        return "!YEAR"
    if word and word[0].isdigit():
        return "!DIGITS"
    return word.lower()


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/grammar.py
# Line: 1038

def _get_type_if_possible(self, item):
    """
    Helper function which returns the ``TYPE`` feature of the ``item``,
    if it exists, otherwise it returns the ``item`` itself
    """
    if isinstance(item, dict) and TYPE in item:
        return FeatureValueType(item[TYPE])
    else:
        return item



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/texttiling.py
# Line: 204

def _mark_paragraph_breaks(self, text):
    """Identifies indented text or line breaks as the beginning of
    paragraphs"""
    MIN_PARAGRAPH = 100
    pattern = re.compile("[ \t\r\f\v]*\n[ \t\r\f\v]*\n[ \t\r\f\v]*")
    matches = pattern.finditer(text)

    last_break = 0
    pbreaks = [0]
    for pb in matches:
        if pb.start() - last_break < MIN_PARAGRAPH:
            continue
        else:
            pbreaks.append(pb.start())
            last_break = pb.start()

    return pbreaks


# ==================================================
# Line: 234

def _create_token_table(self, token_sequences, par_breaks):
    "Creates a table of TokenTableFields"
    token_table = {}
    current_par = 0
    current_tok_seq = 0
    pb_iter = par_breaks.__iter__()
    current_par_break = next(pb_iter)
    if current_par_break == 0:
        try:
            current_par_break = next(pb_iter)  # skip break at 0
        except StopIteration as e:
            raise ValueError(
                "No paragraph breaks were found(text too short perhaps?)"
            ) from e
    for ts in token_sequences:
        for word, index in ts.wrdindex_list:
            try:
                while index > current_par_break:
                    current_par_break = next(pb_iter)
                    current_par += 1
            except StopIteration:
                # hit bottom
                pass

            if word in token_table:
                token_table[word].total_count += 1

                if token_table[word].last_par != current_par:
                    token_table[word].last_par = current_par
                    token_table[word].par_count += 1

                if token_table[word].last_tok_seq != current_tok_seq:
                    token_table[word].last_tok_seq = current_tok_seq
                    token_table[word].ts_occurences.append([current_tok_seq, 1])
                else:
                    token_table[word].ts_occurences[-1][1] += 1
            else:  # new word
                token_table[word] = TokenTableField(
                    first_pos=index,
                    ts_occurences=[[current_tok_seq, 1]],
                    total_count=1,
                    par_count=1,
                    last_par=current_par,
                    last_tok_seq=current_tok_seq,
                )

        current_tok_seq += 1

    return token_table


# ==================================================
# Line: 313

def _depth_scores(self, scores):
    """Calculates the depth of each gap, i.e. the average difference
    between the left and right peaks and the gap's score"""

    depth_scores = [0 for x in scores]
    # clip boundaries: this holds on the rule of thumb(my thumb)
    # that a section shouldn't be smaller than at least 2
    # pseudosentences for small texts and around 5 for larger ones.

    clip = min(max(len(scores) // 10, 2), 5)
    index = clip

    for gapscore in scores[clip:-clip]:
        lpeak = gapscore
        for score in scores[index::-1]:
            if score >= lpeak:
                lpeak = score
            else:
                break
        rpeak = gapscore
        for score in scores[index:]:
            if score >= rpeak:
                rpeak = score
            else:
                break
        depth_scores[index] = lpeak + rpeak - 2 * gapscore
        index += 1

    return depth_scores


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/simple.py
# Occurrences: Lines 75-78 (2 instances)

def tokenize(self, s):
    return list(s)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/repp.py
# Line: 138

def find_repptokenizer(self, repp_dirname):
    """
    A module to find REPP tokenizer binary and its *repp.set* config file.
    """
    if os.path.exists(repp_dirname):  # If a full path is given.
        _repp_dir = repp_dirname
    else:  # Try to find path to REPP directory in environment variables.
        _repp_dir = find_dir(repp_dirname, env_vars=("REPP_TOKENIZER",))
    # Checks for the REPP binary and erg/repp.set config file.
    assert os.path.exists(_repp_dir + "/src/repp")
    assert os.path.exists(_repp_dir + "/erg/repp.set")
    return _repp_dir

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/punkt.py
# Line: 813

def _unique_types(self, tokens):
    return {aug_tok.type for aug_tok in tokens}


# ==================================================
# Line: 864

def _freq_threshold(self, fdist, threshold):
    """
    Returns a FreqDist containing only data with counts below a given
    threshold, as well as a mapping (None -> count_removed).
    """
    # We assume that there is more data below the threshold than above it
    # and so create a new FreqDist rather than working in place.
    res = FreqDist()
    num_removed = 0
    for tok in fdist:
        count = fdist[tok]
        if count < threshold:
            num_removed += 1
        else:
            res[tok] += count
    res[None] += num_removed
    return res


# ==================================================
# Line: 1183

def _is_potential_sent_starter(self, cur_tok, prev_tok):
    """
    Returns True given a token and the token that precedes it if it
    seems clear that the token is beginning a sentence.
    """
    # If a token (i) is preceded by a sentence break that is
    # not a potential ordinal number or initial, and (ii) is
    # alphabetic, then it is a a sentence-starter.
    return (
        prev_tok.sentbreak
        and not (prev_tok.is_number or prev_tok.is_initial)
        and cur_tok.is_alpha
    )


# ==================================================
# Line: 1226

def _get_sentbreak_count(self, tokens):
    """
    Returns the number of sentence breaks marked in a given set of
    augmented tokens.
    """
    return sum(1 for aug_tok in tokens if aug_tok.sentbreak)



# ==================================================
# Line: 1342

def _get_last_whitespace_index(self, text: str) -> int:
    """
    Given a text, find the index of the *last* occurrence of *any*
    whitespace character, i.e. " ", "\n", "\t", "\r", etc.
    If none is found, return 0.
    """
    for i in range(len(text) - 1, -1, -1):
        if text[i] in string.whitespace:
            return i
    return 0


# ==================================================
# Line: 1532

def _build_sentence_list(
    self, text: str, tokens: Iterator[PunktToken]

# ==================================================
# Line: 1589

def dump(self, tokens: Iterator[PunktToken]) -> None:
    print("writing to /tmp/punkt.new...")
    with open("/tmp/punkt.new", "w") as outfile:
        for aug_tok in tokens:
            if aug_tok.parastart:
                outfile.write("\n\n")
            elif aug_tok.linestart:
                outfile.write("\n")
            else:
                outfile.write(" ")

            outfile.write(str(aug_tok))


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/prover9.py
# Line: 137

def prover9_input(self, goal, assumptions):
    """
    :return: The input string that should be provided to the
        prover9 binary.  This string is formed based on the goal,
        assumptions, and timeout value of this object.
    """
    s = ""

    if assumptions:
        s += "formulas(assumptions).\n"
        for p9_assumption in convert_to_prover9(assumptions):
            s += "    %s.\n" % p9_assumption
        s += "end_of_list.\n\n"

    if goal:
        s += "formulas(goals).\n"
        s += "    %s.\n" % convert_to_prover9(goal)
        s += "end_of_list.\n\n"

    return s


# ==================================================
# Line: 158

def binary_locations(self):
    """
    A list of directories that should be searched for the prover9
    executables.  This list is used by ``config_prover9`` when searching
    for the prover9 executables.
    """
    return [
        "/usr/local/bin/prover9",
        "/usr/local/bin/prover9/bin",
        "/usr/local/bin",
        "/usr/bin",
        "/usr/local/prover9",
        "/usr/local/share/prover9",
    ]


# ==================================================
# Line: 186

def _call(self, input_str, binary, args=[], verbose=False):
    """
    Call the binary with the given input.

    :param input_str: A string whose contents are used as stdin.
    :param binary: The location of the binary to call
    :param args: A list of command-line arguments.
    :return: A tuple (stdout, returncode)
    :see: ``config_prover9``
    """
    if verbose:
        print("Calling:", binary)
        print("Args:", args)
        print("Input:\n", input_str, "\n")

    # Call prover9 via a subprocess
    cmd = [binary] + args
    try:
        input_str = input_str.encode("utf8")
    except AttributeError:
        pass
    p = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE
    )
    (stdout, stderr) = p.communicate(input=input_str)

    if verbose:
        print("Return code:", p.returncode)
        if stdout:
            print("stdout:\n", stdout, "\n")
        if stderr:
            print("stderr:\n", stderr, "\n")

    return (stdout.decode("utf-8"), p.returncode)



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/tableau.py
# Line: 538

def _categorize_NegatedExpression(self, current):
    negated = current.term

    if isinstance(negated, NegatedExpression):
        return Categories.D_NEG
    elif isinstance(negated, FunctionVariableExpression):
        return Categories.N_PROP
    elif TableauProver.is_atom(negated):
        return Categories.N_ATOM
    elif isinstance(negated, AllExpression):
        return Categories.N_ALL
    elif isinstance(negated, AndExpression):
        return Categories.N_AND
    elif isinstance(negated, OrExpression):
        return Categories.N_OR
    elif isinstance(negated, ImpExpression):
        return Categories.N_IMP
    elif isinstance(negated, IffExpression):
        return Categories.N_IFF
    elif isinstance(negated, EqualityExpression):
        return Categories.N_EQ
    elif isinstance(negated, ExistsExpression):
        return Categories.N_EXISTS
    elif isinstance(negated, ApplicationExpression):
        return Categories.N_APP
    else:
        raise ProverParseError("cannot categorize %s" % negated.__class__.__name__)



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/api.py
# Line: 301

def decorate_proof(self, proof_string, simplify=True):
    """
    Modify and return the proof string
    :param proof_string: str the proof to decorate
    :param simplify: bool simplify the proof?
    :return: str
    """
    return proof_string


# ==================================================
# Line: 357

def _decorate_model(self, valuation_str, format=None):
    """
    :param valuation_str: str with the model builder's output
    :param format: str indicating the format for displaying
    :return: str
    """
    return valuation_str


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/resolution.py
# Line: 75

def _attempt_proof(self, clauses):
    # map indices to lists of indices, to store attempted unifications
    tried = defaultdict(list)

    i = 0
    while i < len(clauses):
        if not clauses[i].is_tautology():
            # since we try clauses in order, we should start after the last
            # index tried
            if tried[i]:
                j = tried[i][-1] + 1
            else:
                j = i + 1  # nothing tried yet for 'i', so start with the next

            while j < len(clauses):
                # don't: 1) unify a clause with itself,
                #       2) use tautologies
                if i != j and j and not clauses[j].is_tautology():
                    tried[i].append(j)
                    newclauses = clauses[i].unify(clauses[j])
                    if newclauses:
                        for newclause in newclauses:
                            newclause._parents = (i + 1, j + 1)
                            clauses.append(newclause)
                            if not len(newclause):  # if there's an empty clause
                                return (True, clauses)
                        i = -1  # since we added a new clause, restart from the top
                        break
                j += 1
        i += 1
    return (False, clauses)



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/discourse.py
# Line: 70

def process_thread(self, sentence_readings):
    """
    This method should be used to handle dependencies between readings such
    as resolving anaphora.

    :param sentence_readings: readings to process
    :type sentence_readings: list(Expression)
    :return: the list of readings after processing
    :rtype: list(Expression)
    """
    return sentence_readings


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/nonmonotonic.py
# Line: 243

def _make_unique_signature(self, predHolder):
    """
    This method figures out how many arguments the predicate takes and
    returns a tuple containing that number of unique variables.
    """
    return tuple(unique_variable() for i in range(predHolder.signature_len))


# ==================================================
# Line: 250

def _make_antecedent(self, predicate, signature):
    """
    Return an application expression with 'predicate' as the predicate
    and 'signature' as the list of arguments.
    """
    antecedent = predicate
    for v in signature:
        antecedent = antecedent(VariableExpression(v))
    return antecedent


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/cluster/em.py
# Line: 150

def _gaussian(self, mean, cvm, x):
    m = len(mean)
    assert cvm.shape == (m, m), "bad sized covariance matrix, %s" % str(cvm.shape)
    try:
        det = numpy.linalg.det(cvm)
        inv = numpy.linalg.inv(cvm)
        a = det**-0.5 * (2 * numpy.pi) ** (-m / 2.0)
        dx = x - mean
        print(dx, inv)
        b = -0.5 * numpy.dot(numpy.dot(dx, inv), dx)
        return a * numpy.exp(b)
    except OverflowError:
        # happens when the exponent is negative infinity - i.e. b = 0
        # i.e. the inverse of cvm is huge (cvm is almost zero)
        return 0


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/cluster/api.py
# Line: 70

def cluster_name(self, index):
    """
    Returns the names of the cluster at index.
    """
    return index

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/cluster/util.py
# Line: 109

def _normalise(self, vector):
    """
    Normalises the vector to unit length.
    """
    return vector / sqrt(numpy.dot(vector, vector))



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/cluster/gaac.py
# Line: 80

def _merge_similarities(self, dist, cluster_len, i, j):
    # the new cluster i merged from i and j adopts the average of
    # i and j's similarity to each other cluster, weighted by the
    # number of points in the clusters i and j
    i_weight = cluster_len[i]
    j_weight = cluster_len[j]
    weight_sum = i_weight + j_weight

    # update for x<i
    dist[:i, i] = dist[:i, i] * i_weight + dist[:i, j] * j_weight
    dist[:i, i] /= weight_sum
    # update for i<x<j
    dist[i, i + 1 : j] = (
        dist[i, i + 1 : j] * i_weight + dist[i + 1 : j, j] * j_weight
    )
    # update for i<j<x
    dist[i, j + 1 :] = dist[i, j + 1 :] * i_weight + dist[j, j + 1 :] * j_weight
    dist[i, i + 1 :] /= weight_sum


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/snowball.py
# Line: 179

def _r1_scandinavian(self, word, vowels):
    """
    Return the region R1 that is used by the Scandinavian stemmers.

    R1 is the region after the first non-vowel following a vowel,
    or is the null region at the end of the word if there is no
    such non-vowel. But then R1 is adjusted so that the region
    before it contains at least three letters.

    :param word: The word whose region R1 is determined.
    :type word: str or unicode
    :param vowels: The vowels of the respective language that are
                   used to determine the region R1.
    :type vowels: unicode
    :return: the region R1 for the respective word.
    :rtype: unicode
    :note: This helper method is invoked by the respective stem method of
           the subclasses DanishStemmer, NorwegianStemmer, and
           SwedishStemmer. It is not to be invoked directly!

    """
    r1 = ""
    for i in range(1, len(word)):
        if word[i] not in vowels and word[i - 1] in vowels:
            if 3 > len(word[: i + 1]) > 0:
                r1 = word[3:]
            elif len(word[: i + 1]) >= 3:
                r1 = word[i + 1 :]
            else:
                return word
            break

    return r1



# ==================================================
# Line: 221

def _r1r2_standard(self, word, vowels):
    """
    Return the standard interpretations of the string regions R1 and R2.

    R1 is the region after the first non-vowel following a vowel,
    or is the null region at the end of the word if there is no
    such non-vowel.

    R2 is the region after the first non-vowel following a vowel
    in R1, or is the null region at the end of the word if there
    is no such non-vowel.

    :param word: The word whose regions R1 and R2 are determined.
    :type word: str or unicode
    :param vowels: The vowels of the respective language that are
                   used to determine the regions R1 and R2.
    :type vowels: unicode
    :return: (r1,r2), the regions R1 and R2 for the respective word.
    :rtype: tuple
    :note: This helper method is invoked by the respective stem method of
           the subclasses DutchStemmer, FinnishStemmer,
           FrenchStemmer, GermanStemmer, ItalianStemmer,
           PortugueseStemmer, RomanianStemmer, and SpanishStemmer.
           It is not to be invoked directly!
    :note: A detailed description of how to define R1 and R2
           can be found at http://snowball.tartarus.org/texts/r1r2.html

    """
    r1 = ""
    r2 = ""
    for i in range(1, len(word)):
        if word[i] not in vowels and word[i - 1] in vowels:
            r1 = word[i + 1 :]
            break

    for i in range(1, len(r1)):
        if r1[i] not in vowels and r1[i - 1] in vowels:
            r2 = r1[i + 1 :]
            break

    return (r1, r2)


# ==================================================
# Line: 263

def _rv_standard(self, word, vowels):
    """
    Return the standard interpretation of the string region RV.

    If the second letter is a consonant, RV is the region after the
    next following vowel. If the first two letters are vowels, RV is
    the region after the next following consonant. Otherwise, RV is
    the region after the third letter.

    :param word: The word whose region RV is determined.
    :type word: str or unicode
    :param vowels: The vowels of the respective language that are
                   used to determine the region RV.
    :type vowels: unicode
    :return: the region RV for the respective word.
    :rtype: unicode
    :note: This helper method is invoked by the respective stem method of
           the subclasses ItalianStemmer, PortugueseStemmer,
           RomanianStemmer, and SpanishStemmer. It is not to be
           invoked directly!

    """
    rv = ""
    if len(word) >= 2:
        if word[1] not in vowels:
            for i in range(2, len(word)):
                if word[i] in vowels:
                    rv = word[i + 1 :]
                    break

        elif word[0] in vowels and word[1] in vowels:
            for i in range(2, len(word)):
                if word[i] not in vowels:
                    rv = word[i + 1 :]
                    break
        else:
            rv = word[3:]

    return rv



# ==================================================
# Line: 2574

def __rv_french(self, word, vowels):
    """
    Return the region RV that is used by the French stemmer.

    If the word begins with two vowels, RV is the region after
    the third letter. Otherwise, it is the region after the first
    vowel not at the beginning of the word, or the end of the word
    if these positions cannot be found. (Exceptionally, u'par',
    u'col' or u'tap' at the beginning of a word is also taken to
    define RV as the region to their right.)

    :param word: The French word whose region RV is determined.
    :type word: str or unicode
    :param vowels: The French vowels that are used to determine
                   the region RV.
    :type vowels: unicode
    :return: the region RV for the respective French word.
    :rtype: unicode
    :note: This helper method is invoked by the stem method of
           the subclass FrenchStemmer. It is not to be invoked directly!

    """
    rv = ""
    if len(word) >= 2:
        if word.startswith(("par", "col", "tap")) or (
            word[0] in vowels and word[1] in vowels
        ):
            rv = word[3:]
        else:
            for i in range(1, len(word)):
                if word[i] in vowels:
                    rv = word[i + 1 :]
                    break

    return rv



# ==================================================
# Line: 3133

def __r1_hungarian(self, word, vowels, digraphs):
    """
    Return the region R1 that is used by the Hungarian stemmer.

    If the word begins with a vowel, R1 is defined as the region
    after the first consonant or digraph (= two letters stand for
    one phoneme) in the word. If the word begins with a consonant,
    it is defined as the region after the first vowel in the word.
    If the word does not contain both a vowel and consonant, R1
    is the null region at the end of the word.

    :param word: The Hungarian word whose region R1 is determined.
    :type word: str or unicode
    :param vowels: The Hungarian vowels that are used to determine
                   the region R1.
    :type vowels: unicode
    :param digraphs: The digraphs that are used to determine the
                     region R1.
    :type digraphs: tuple
    :return: the region R1 for the respective word.
    :rtype: unicode
    :note: This helper method is invoked by the stem method of the subclass
           HungarianStemmer. It is not to be invoked directly!

    """
    r1 = ""
    if word[0] in vowels:
        for digraph in digraphs:
            if digraph in word[1:]:
                r1 = word[word.index(digraph[-1]) + 1 :]
                return r1

        for i in range(1, len(word)):
            if word[i] not in vowels:
                r1 = word[i + 1 :]
                break
    else:
        for i in range(1, len(word)):
            if word[i] in vowels:
                r1 = word[i + 1 :]
                break

    return r1



# ==================================================
# Line: 5150

def __regions_russian(self, word):
    """
    Return the regions RV and R2 which are used by the Russian stemmer.

    In any word, RV is the region after the first vowel,
    or the end of the word if it contains no vowel.

    R2 is the region after the first non-vowel following
    a vowel in R1, or the end of the word if there is no such non-vowel.

    R1 is the region after the first non-vowel following a vowel,
    or the end of the word if there is no such non-vowel.

    :param word: The Russian word whose regions RV and R2 are determined.
    :type word: str or unicode
    :return: the regions RV and R2 for the respective Russian word.
    :rtype: tuple
    :note: This helper method is invoked by the stem method of the subclass
           RussianStemmer. It is not to be invoked directly!

    """
    r1 = ""
    r2 = ""
    rv = ""

    vowels = ("A", "U", "E", "a", "e", "i", "o", "u", "y")
    word = word.replace("i^a", "A").replace("i^u", "U").replace("e`", "E")

    for i in range(1, len(word)):
        if word[i] not in vowels and word[i - 1] in vowels:
            r1 = word[i + 1 :]
            break

    for i in range(1, len(r1)):
        if r1[i] not in vowels and r1[i - 1] in vowels:
            r2 = r1[i + 1 :]
            break

    for i in range(len(word)):
        if word[i] in vowels:
            rv = word[i + 1 :]
            break

    r2 = r2.replace("A", "i^a").replace("U", "i^u").replace("E", "e`")
    rv = rv.replace("A", "i^a").replace("U", "i^u").replace("E", "e`")

    return (rv, r2)


# ==================================================
# Line: 5198

def __cyrillic_to_roman(self, word):
    """
    Transliterate a Russian word into the Roman alphabet.

    A Russian word whose letters consist of the Cyrillic
    alphabet are transliterated into the Roman alphabet
    in order to ease the forthcoming stemming process.

    :param word: The word that is transliterated.
    :type word: unicode
    :return: the transliterated word.
    :rtype: unicode
    :note: This helper method is invoked by the stem method of the subclass
           RussianStemmer. It is not to be invoked directly!

    """
    word = (
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
    )

    return word


# ==================================================
# Line: 5285

def __roman_to_cyrillic(self, word):
    """
    Transliterate a Russian word back into the Cyrillic alphabet.

    A Russian word formerly transliterated into the Roman alphabet
    in order to ease the stemming process, is transliterated back
    into the Cyrillic alphabet, its original form.

    :param word: The word that is transliterated.
    :type word: str or unicode
    :return: word, the transliterated word.
    :rtype: unicode
    :note: This helper method is invoked by the stem method of the subclass
           RussianStemmer. It is not to be invoked directly!

    """
    word = (
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
    )

    return word



# ==================================================
# Line: 5717

def __replace_accented(self, word):
    """
    Replaces all accented letters on a word with their non-accented
    counterparts.

    :param word: A spanish word, with or without accents
    :type word: str or unicode
    :return: a word with the accented letters (á, é, í, ó, ú) replaced with
             their non-accented counterparts (a, e, i, o, u)
    :rtype: str or unicode
    """
    return (
        word.replace("\xE1", "a")
        .replace("\xE9", "e")
        .replace("\xED", "i")
        .replace("\xF3", "o")
        .replace("\xFA", "u")
    )



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/lancaster.py
# Line: 282

def __getLastLetter(self, word):
    """Get the zero-based index of the last alphabetic character in this string"""
    last_letter = -1
    for position in range(len(word)):
        if word[position].isalpha():
            last_letter = position
        else:
            break
    return last_letter


# ==================================================
# Line: 292

def __isAcceptable(self, word, remove_total):
    """Determine if the word is acceptable for stemming."""
    word_is_acceptable = False
    # If the word starts with a vowel, it must be at least 2
    # characters long to be stemmed
    if word[0] in "aeiouy":
        if len(word) - remove_total >= 2:
            word_is_acceptable = True
    # If the word starts with a consonant, it must be at least 3
    # characters long (including one vowel) to be stemmed
    elif len(word) - remove_total >= 3:
        if word[1] in "aeiouy":
            word_is_acceptable = True
        elif word[2] in "aeiouy":
            word_is_acceptable = True
    return word_is_acceptable


# ==================================================
# Line: 309

def __applyRule(self, word, remove_total, append_string):
    """Apply the stemming rule to the word"""
    # Remove letters from the end of the word
    new_word_length = len(word) - remove_total
    word = word[0:new_word_length]

    # And add new letters to the end of the truncated word
    if append_string:
        word += append_string
    return word


# ==================================================
# Line: 320

def __stripPrefix(self, word):
    """Remove prefix from a word.

    This function originally taken from Whoosh.

    """
    for prefix in (
        "kilo",
        "micro",
        "milli",
        "intra",
        "ultra",
        "mega",
        "nano",
        "pico",
        "pseudo",
    ):
        if word.startswith(prefix):
            return word[len(prefix) :]
    return word


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/arlstem.py
# Line: 203

def fem2masc(self, token):
    """
    transform the word from the feminine form to the masculine form.
    """
    if token.endswith("\u0629") and len(token) > 3:
        return token[:-1]


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/isri.py
# Line: 260

def waw(self, word):
    """remove connective ‘و’ if it precedes a word beginning with ‘و’"""
    if len(word) >= 4 and word[:2] == "\u0648\u0648":
        word = word[1:]
    return word


# ==================================================
# Line: 366

def pro_w64(self, word):
    """process length six patterns and extract length four roots"""
    if word[0] == "\u0627" and word[4] == "\u0627":  # افعلال
        word = word[1:4] + word[5]
    elif word.startswith("\u0645\u062a"):  # متفعلل
        word = word[2:]
    return word


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/porter.py
# Line: 240

def _replace_suffix(self, word, suffix, replacement):
    """Replaces `suffix` of `word` with `replacement"""
    assert word.endswith(suffix), "Given word doesn't end with given suffix"
    if suffix == "":
        return word + replacement
    else:
        return word[: -len(suffix)] + replacement


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/wordnet.py
# Line: 30

def _morphy(self, form, pos, check_exceptions=True):
    """
    _morphy() is WordNet's _morphy lemmatizer.
    It returns a list of all lemmas found in WordNet.

    >>> from nltk.stem import WordNetLemmatizer as wnl
    >>> print(wnl()._morphy('us', 'n'))
    ['us', 'u']
    """
    from nltk.corpus import wordnet as wn

    return wn._morphy(form, pos, check_exceptions)


# ==================================================
# Line: 43

def morphy(self, form, pos=None, check_exceptions=True):
    """
    morphy() is a restrictive wrapper around _morphy().
    It returns the first lemma found in WordNet,
    or None if no lemma is found.

    >>> from nltk.stem import WordNetLemmatizer as wnl
    >>> print(wnl().morphy('us', 'n'))
    us

    >>> print(wnl().morphy('catss'))
    None
    """
    from nltk.corpus import wordnet as wn

    return wn.morphy(form, pos, check_exceptions)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/rslp.py
# Line: 64

def read_rule(self, filename):
    rules = load("nltk:stemmers/rslp/" + filename, format="raw").decode("utf8")
    lines = rules.split("\n")

    lines = [line for line in lines if line != ""]  # remove blank lines
    lines = [line for line in lines if line[0] != "#"]  # remove comments

    # NOTE: a simple but ugly hack to make this parser happy with double '\t's
    lines = [line.replace("\t\t", "\t") for line in lines]

    # parse rules
    rules = []
    for line in lines:
        rule = []
        tokens = line.split("\t")

        # text to be searched for at the end of the string
        rule.append(tokens[0][1:-1])  # remove quotes

        # minimum stem size to perform the replacement
        rule.append(int(tokens[1]))

        # text to be replaced into
        rule.append(tokens[2][1:-1])  # remove quotes

        # exceptions to this rule
        rule.append([token[1:-1] for token in tokens[3].split(",")])

        # append to the results
        rules.append(rule)

    return rules


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/arlstem2.py
# Line: 221

def adjective(self, token):
    """
    remove the infixes from adjectives
    """
    # ^Alif, Alif, $Yaa
    if len(token) > 5:
        if (
            token.startswith("\u0627")
            and token[-3] == "\u0627"
            and token.endswith("\u064A")
        ):
            return token[:-3] + token[-2]


# ==================================================
# Line: 264

def fem2masc(self, token):
    """
    transform the word from the feminine form to the masculine form.
    """
    if len(token) > 6:
        # ^Taa, Yaa, $Yaa and Taa Marbuta
        if (
            token.startswith("\u062A")
            and token[-4] == "\u064A"
            and token.endswith("\u064A\u0629")
        ):
            return token[1:-4] + token[-3]
        # ^Alif, Yaa, $Yaa and Taa Marbuta
        if (
            token.startswith("\u0627")
            and token[-4] == "\u0627"
            and token.endswith("\u064A\u0629")
        ):
            return token[:-4] + token[-3]
    # $Alif, Yaa and Taa Marbuta
    if token.endswith("\u0627\u064A\u0629") and len(token) > 5:
        return token[:-2]
    if len(token) > 4:
        # Alif, $Taa Marbuta
        if token[1] == "\u0627" and token.endswith("\u0629"):
            return token[0] + token[2:-1]
        # $Yaa and Taa Marbuta
        if token.endswith("\u064A\u0629"):
            return token[:-2]
    # $Taa Marbuta
    if token.endswith("\u0629") and len(token) > 3:
        return token[:-1]


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/text.py
# Line: 563

def _train_default_ngram_lm(self, tokenized_sents, n=3):
    train_data, padded_sents = padded_everygram_pipeline(n, tokenized_sents)
    model = MLE(order=n)
    model.fit(train_data, padded_sents)
    return model


# ==================================================
# Line: 723

def tf(self, term, text):
    """The frequency of the term in text."""
    return text.count(term) / len(text)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/chunk/named_entity.py
# Line: 44

def _classifier_builder(self, train):
    return MaxentClassifier.train(
        #          "megam" cannot be the default algorithm since it requires compiling with ocaml
        train,
        algorithm="iis",
        gaussian_prior_sigma=1,
        trace=2,
    )


# ==================================================
# Line: 144

def _tagged_to_parse(self, tagged_tokens):
    """
    Convert a list of tagged tokens to a chunk-parse tree.
    """
    sent = Tree("S", [])

    for tok, tag in tagged_tokens:
        if tag == "O":
            sent.append(tok)
        elif tag.startswith("B-"):
            sent.append(Tree(tag[2:], [tok]))
        elif tag.startswith("I-"):
            if sent and isinstance(sent[-1], Tree) and sent[-1].label() == tag[2:]:
                sent[-1].append(tok)
            else:
                sent.append(Tree(tag[2:], [tok]))
    return sent


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/chunk/regexp.py
# Line: 101

def _tag(self, tok):
    if isinstance(tok, tuple):
        return tok[1]
    elif isinstance(tok, Tree):
        return tok.label()
    else:
        raise ValueError("chunk structures must contain tagged " "tokens or trees")


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/senseval.py
# Line: 58

def _entry(self, tree):
    elts = []
    for lexelt in tree.findall("lexelt"):
        for inst in lexelt.findall("instance"):
            sense = inst[0].attrib["senseid"]
            context = [(w.text, w.attrib["pos"]) for w in inst[1]]
            elts.append((sense, context))
    return elts



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/rte.py
# Line: 119

def _read_etree(self, doc):
    """
    Map the XML input into an RTEPair.

    This uses the ``getiterator()`` method from the ElementTree package to
    find all the ``<pair>`` elements.

    :param doc: a parsed XML document
    :rtype: list(RTEPair)
    """
    try:
        challenge = doc.attrib["challenge"]
    except KeyError:
        challenge = None
    pairiter = doc.iter("pair")
    return [RTEPair(pair, challenge=challenge) for pair in pairiter]


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/ppattach.py
# Line: 83

def _read_tuple_block(self, stream):
    line = stream.readline()
    if line:
        return [tuple(line.split())]
    else:
        return []


# ==================================================
# Line: 90

def _read_obj_block(self, stream):
    line = stream.readline()
    if line:
        return [PPAttachment(*line.split())]
    else:
        return []

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/pl196x.py
# Line: 83

def _parse_tag(self, tag_word_tuple):
    (tag, word) = tag_word_tuple
    if tag.startswith("w"):
        tag = ANA.search(tag).group(1)
    else:  # tag.startswith('c')
        tag = TYPE.search(tag).group(1)
    return word, tag



# ==================================================
# Line: 158

def decode_tag(self, tag):
    # to be implemented
    return tag


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/ipipan.py
# Line: 189

def _get_tag(self, f, tag):
    tags = []
    with open(f) as infile:
        header = infile.read()
    tag_end = 0
    while True:
        tag_pos = header.find("<" + tag, tag_end)
        if tag_pos < 0:
            return tags
        tag_end = header.find("</" + tag + ">", tag_pos)
        tags.append(header[tag_pos + len(tag) + 2 : tag_end])


# ==================================================
# Line: 201

def _map_category(self, cat):
    pos = cat.find(">")
    if pos == -1:
        return cat
    else:
        return cat[pos + 1 :]


# ==================================================
# Line: 208

def _view(self, filename, **kwargs):
    tags = kwargs.pop("tags", True)
    mode = kwargs.pop("mode", 0)
    simplify_tags = kwargs.pop("simplify_tags", False)
    one_tag = kwargs.pop("one_tag", True)
    disamb_only = kwargs.pop("disamb_only", True)
    append_no_space = kwargs.pop("append_no_space", False)
    append_space = kwargs.pop("append_space", False)
    replace_xmlentities = kwargs.pop("replace_xmlentities", True)

    if len(kwargs) > 0:
        raise ValueError("Unexpected arguments: %s" % kwargs.keys())
    if not one_tag and not disamb_only:
        raise ValueError(
            "You cannot specify both one_tag=False and " "disamb_only=False"
        )
    if not tags and (simplify_tags or not one_tag or not disamb_only):
        raise ValueError(
            "You cannot specify simplify_tags, one_tag or "
            "disamb_only with functions other than tagged_*"
        )

    return IPIPANCorpusView(
        filename,
        tags=tags,
        mode=mode,
        simplify_tags=simplify_tags,
        one_tag=one_tag,
        disamb_only=disamb_only,
        append_no_space=append_no_space,
        append_space=append_space,
        replace_xmlentities=replace_xmlentities,
    )



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/childes.py
# Line: 217

def _get_corpus(self, fileid):
    results = dict()
    xmldoc = ElementTree.parse(fileid).getroot()
    for key, value in xmldoc.items():
        results[key] = value
    return results


# ==================================================
# Line: 234

def _get_participants(self, fileid):
    # multidimensional dicts
    def dictOfDicts():
        return defaultdict(dictOfDicts)

    xmldoc = ElementTree.parse(fileid).getroot()
    # getting participants' data
    pat = dictOfDicts()
    for participant in xmldoc.findall(
        f".//{{{NS}}}Participants/{{{NS}}}participant"
    ):
        for key, value in participant.items():
            pat[participant.get("id")][key] = value
    return pat


# ==================================================
# Line: 277

def convert_age(self, age_year):
    "Caclculate age in months from a string in CHILDES format"
    m = re.match(r"P(\d+)Y(\d+)M?(\d?\d?)D?", age_year)
    age_month = int(m.group(1)) * 12 + int(m.group(2))
    try:
        if int(m.group(3)) > 15:
            age_month += 1
    # some corpora don't have age information?
    except ValueError as e:
        pass
    return age_month


# ==================================================
# Line: 350

def _get_words(
    self, fileid, speaker, sent, stem, relation, pos, strip_space, replace

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/twitter.py
# Line: 125

def _read_tweets(self, stream):
    """
    Assumes that each line in ``stream`` is a JSON-serialised object.
    """
    tweets = []
    for i in range(10):
        line = stream.readline()
        if not line:
            return tweets
        tweet = json.loads(line)
        tweets.append(tweet)
    return tweets

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/tagged.py
# Line: 336

def _read_block(self, stream):
    return read_regexp_block(stream, r".*", r".*_\.")



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/bnc.py
# Line: 103

def _words(self, fileid, bracket_sent, tag, strip_space, stem):
    """
    Helper used to implement the view methods -- returns a list of
    words or a list of sentences, optionally tagged.

    :param fileid: The name of the underlying file.
    :param bracket_sent: If true, include sentence bracketing.
    :param tag: The name of the tagset to use, or None for no tags.
    :param strip_space: If true, strip spaces from word tokens.
    :param stem: If true, then substitute stems for words.
    """
    result = []

    xmldoc = ElementTree.parse(fileid).getroot()
    for xmlsent in xmldoc.findall(".//s"):
        sent = []
        for xmlword in _all_xmlwords_in(xmlsent):
            word = xmlword.text
            if not word:
                word = ""  # fixes issue 337?
            if strip_space or stem:
                word = word.strip()
            if stem:
                word = xmlword.get("hw", word)
            if tag == "c5":
                word = (word, xmlword.get("c5"))
            elif tag == "pos":
                word = (word, xmlword.get("pos", xmlword.get("c5")))
            sent.append(word)
        if bracket_sent:
            result.append(BNCSentence(xmlsent.attrib["n"], sent))
        else:
            result.extend(sent)

    assert None not in result
    return result



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/reviews.py
# Line: 276

def _read_features(self, stream):
    features = []
    for i in range(20):
        line = stream.readline()
        if not line:
            return features
        features.extend(re.findall(FEATURES, line))
    return features


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/bracket_parse.py
# Line: 79

def _normalize(self, t):
    # Replace leaves of the form (!), (,), with (! !), (, ,)
    t = re.sub(r"\((.)\)", r"(\1 \1)", t)
    # Replace leaves of the form (tag word root) with (tag word)
    t = re.sub(r"\(([^\s()]+) ([^\s()]+) [^\s()]+\)", r"(\1 \2)", t)
    return t


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/knbc.py
# Occurrences: Lines 64-68 (2 instances)

def _read_block(self, stream):
    # blocks are split by blankline (or EOF) - default
    return read_blankline_block(stream)


# ==================================================
# Line: 79

def _tag(self, t, tagset=None):
    res = []
    for line in t.splitlines():
        # ignore the Bunsets headers
        if not re.match(r"EOS|\*|\#|\+", line):
            cells = line.strip().split(" ")
            # convert cells to morph tuples
            res.append((cells[0], " ".join(cells[1:])))

    return res


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/sinica_treebank.py
# Line: 57

def _read_block(self, stream):
    sent = stream.readline()
    sent = IDENTIFIER.sub("", sent)
    sent = APPENDIX.sub("", sent)
    return [sent]


# ==================================================
# Line: 63

def _parse(self, sent):
    return sinica_parse(sent)


# ==================================================
# Line: 74

def _word(self, sent):
    return WORD.findall(sent)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/framenet.py
# Line: 2468

def _exemplar_of_fes(self, ex, fes=None):
    """
    Given an exemplar sentence and a set of FE names, return the subset of FE names
    that are realized overtly in the sentence on the FE, FE2, or FE3 layer.

    If 'fes' is None, returns all overt FE names.
    """
    overtNames = set(list(zip(*ex.FE[0]))[2]) if ex.FE[0] else set()
    if "FE2" in ex:
        overtNames |= set(list(zip(*ex.FE2[0]))[2]) if ex.FE2[0] else set()
        if "FE3" in ex:
            overtNames |= set(list(zip(*ex.FE3[0]))[2]) if ex.FE3[0] else set()
    return overtNames & fes if fes is not None else overtNames


# ==================================================
# Line: 2672

def _load_xml_attributes(self, d, elt):
    """
    Extracts a subset of the attributes from the given element and
    returns them in a dictionary.

    :param d: A dictionary in which to store the attributes.
    :type d: dict
    :param elt: An ElementTree Element
    :type elt: Element
    :return: Returns the input dict ``d`` possibly including attributes from ``elt``
    :rtype: dict
    """

    d = type(d)(d)

    try:
        attr_dict = elt.attrib
    except AttributeError:
        return d

    if attr_dict is None:
        return d

    # Ignore these attributes when loading attributes from an xml node
    ignore_attrs = [  #'cBy', 'cDate', 'mDate', # <-- annotation metadata that could be of interest
        "xsi",
        "schemaLocation",
        "xmlns",
        "bgColor",
        "fgColor",
    ]

    for attr in attr_dict:
        if any(attr.endswith(x) for x in ignore_attrs):
            continue

        val = attr_dict[attr]
        if val.isdigit():
            d[attr] = int(val)
        else:
            d[attr] = val

    return d


# ==================================================
# Line: 2716

def _strip_tags(self, data):
    """
    Gets rid of all tags and newline characters from the given input

    :return: A cleaned-up version of the input string
    :rtype: str
    """

    try:
        r"""
        # Look for boundary issues in markup. (Sometimes FEs are pluralized in definitions.)
        m = re.search(r'\w[<][^/]|[<][/][^>]+[>](s\w|[a-rt-z0-9])', data)
        if m:
            print('Markup boundary:', data[max(0,m.start(0)-10):m.end(0)+10].replace('\n',' '), file=sys.stderr)
        """

        data = data.replace("<t>", "")
        data = data.replace("</t>", "")
        data = re.sub('<fex name="[^"]+">', "", data)
        data = data.replace("</fex>", "")
        data = data.replace("<fen>", "")
        data = data.replace("</fen>", "")
        data = data.replace("<m>", "")
        data = data.replace("</m>", "")
        data = data.replace("<ment>", "")
        data = data.replace("</ment>", "")
        data = data.replace("<ex>", "'")
        data = data.replace("</ex>", "'")
        data = data.replace("<gov>", "")
        data = data.replace("</gov>", "")
        data = data.replace("<x>", "")
        data = data.replace("</x>", "")

        # Get rid of <def-root> and </def-root> tags
        data = data.replace("<def-root>", "")
        data = data.replace("</def-root>", "")

        data = data.replace("\n", " ")
    except AttributeError:
        pass

    return data


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/nkjp.py
# Line: 77

def _view(self, filename, tags=None, **kwargs):
    """
    Returns a view specialised for use with particular corpus file.
    """
    mode = kwargs.pop("mode", NKJPCorpusReader.WORDS_MODE)
    if mode is NKJPCorpusReader.WORDS_MODE:
        return NKJPCorpus_Morph_View(filename, tags=tags)
    elif mode is NKJPCorpusReader.SENTS_MODE:
        return NKJPCorpus_Segmentation_View(filename, tags=tags)
    elif mode is NKJPCorpusReader.HEADER_MODE:
        return NKJPCorpus_Header_View(filename, tags=tags)
    elif mode is NKJPCorpusReader.RAW_MODE:
        return NKJPCorpus_Text_View(
            filename, tags=tags, mode=NKJPCorpus_Text_View.RAW_MODE
        )

    else:
        raise NameError("No such mode!")


# ==================================================
# Occurrences: Lines 303-310 (3 instances)

def get_segm_id(self, example_word):
    return example_word.split("(")[1].split(",")[0]


# ==================================================
# Line: 407

def get_segm_id(self, elt):
    for attr in elt.attrib:
        if attr.endswith("id"):
            return elt.get(attr)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/bcp47.py
# Line: 49

def wiki_dict(self, lines):
    """Convert Wikidata list of Q-codes to a BCP-47 dictionary"""
    return {
        pair[1]: pair[0].split("/")[-1]
        for pair in [line.strip().split("\t") for line in lines]
    }


# ==================================================
# Line: 56

def subdiv_dict(self, subdivs):
    """Convert the CLDR subdivisions list to a dictionary"""
    return {sub.attrib["type"]: sub.text for sub in subdivs}


# ==================================================
# Line: 127

def val2str(self, val):
    """Return only first value"""
    if type(val) == list:
        #            val = "/".join(val) # Concatenate all values
        val = val[0]
    return val


# ==================================================
# Line: 134

def lang2str(self, lg_record):
    """Concatenate subtag values"""
    name = f"{lg_record['language']}"
    for label in ["extlang", "script", "region", "variant", "extension"]:
        if label in lg_record:
            name += f": {lg_record[label]}"
    return name


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/chunked.py
# Line: 201

def _read_block(self, stream):
    return [tagstr2tree(t) for t in read_blankline_block(stream)]



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/nps_chat.py
# Line: 67

def _wrap_elt(self, elt, handler):
    return ElementWrapper(elt)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/panlex_swadesh.py
# Line: 50

def license(self):
    return "CC0 1.0 Universal"


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/timit.py
# Occurrences: Lines 242-248 (3 instances)

def spkrid(self, utterance):
    return utterance.split("/")[0]


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/wordnet.py
# Line: 1307

def ss2of(self, ss):
    """return the ID of the synset"""
    if ss:
        return f"{ss.offset():08d}-{ss.pos()}"


# ==================================================
# Occurrences: Lines 1982-2007 (6 instances)

def path_similarity(self, synset1, synset2, verbose=False, simulate_root=True):
    return synset1.path_similarity(synset2, verbose, simulate_root)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/ieer.py
# Line: 90

def _parse(self, doc):
    val = nltk.chunk.ieerstr2tree(doc, root_label="DOCUMENT")
    if isinstance(val, dict):
        return IEERDocument(**val)
    else:
        return IEERDocument(val)


# ==================================================
# Line: 97

def _read_block(self, stream):
    out = []
    # Skip any preamble.
    while True:
        line = stream.readline()
        if not line:
            break
        if line.strip() == "<DOC>":
            break
    out.append(line)
    # Read the document
    while True:
        line = stream.readline()
        if not line:
            break
        out.append(line)
        if line.strip() == "</DOC>":
            break
    # Return the document
    return ["\n".join(out)]

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/xmldocs.py
# Line: 153

def _detect_encoding(self, fileid):
    if isinstance(fileid, PathPointer):
        try:
            infile = fileid.open()
            s = infile.readline()
        finally:
            infile.close()
    else:
        with open(fileid, "rb") as infile:
            s = infile.readline()
    if s.startswith(codecs.BOM_UTF16_BE):
        return "utf-16-be"
    if s.startswith(codecs.BOM_UTF16_LE):
        return "utf-16-le"
    if s.startswith(codecs.BOM_UTF32_BE):
        return "utf-32-be"
    if s.startswith(codecs.BOM_UTF32_LE):
        return "utf-32-le"
    if s.startswith(codecs.BOM_UTF8):
        return "utf-8"
    m = re.match(rb'\s*<\?xml\b.*\bencoding="([^"]+)"', s)
    if m:
        return m.group(1).decode()
    m = re.match(rb"\s*<\?xml\b.*\bencoding='([^']+)'", s)
    if m:
        return m.group(1).decode()
    # No encoding found -- what should the default be?
    return "utf-8"


# ==================================================
# Line: 182

def handle_elt(self, elt, context):
    """
    Convert an element into an appropriate value for inclusion in
    the view.  Unless overridden by a subclass or by the
    ``elt_handler`` constructor argument, this method simply
    returns ``elt``.

    :return: The view value corresponding to ``elt``.

    :type elt: ElementTree
    :param elt: The element that should be converted.

    :type context: str
    :param context: A string composed of element tags separated by
        forward slashes, indicating the XML context of the given
        element.  For example, the string ``'foo/bar/baz'``
        indicates that the element is a ``baz`` element whose
        parent is a ``bar`` element and whose grandparent is a
        top-level ``foo`` element.
    """
    return elt


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/verbnet.py
# Line: 348

def _get_semantics_within_frame(self, vnframe):
    """Returns semantics within a single frame

    A utility function to retrieve semantics within a frame in VerbNet
    Members of the semantics dictionary:
    1) Predicate value
    2) Arguments

    :param vnframe: An ElementTree containing the xml contents of
        a VerbNet frame.
    :return: semantics: semantics dictionary
    """
    semantics_within_single_frame = []
    for pred in vnframe.findall("SEMANTICS/PRED"):
        arguments = [
            {"type": arg.get("type"), "value": arg.get("value")}
            for arg in pred.findall("ARGS/ARG")
        ]
        semantics_within_single_frame.append(
            {
                "predicate_value": pred.get("value"),
                "arguments": arguments,
                "negated": pred.get("bool") == "!",
            }
        )
    return semantics_within_single_frame


# ==================================================
# Line: 375

def _get_example_within_frame(self, vnframe):
    """Returns example within a frame

    A utility function to retrieve an example within a frame in VerbNet.

    :param vnframe: An ElementTree containing the xml contents of
        a VerbNet frame.
    :return: example_text: The example sentence for this particular frame
    """
    example_element = vnframe.find("EXAMPLES/EXAMPLE")
    if example_element is not None:
        example_text = example_element.text
    else:
        example_text = ""
    return example_text


# ==================================================
# Line: 391

def _get_description_within_frame(self, vnframe):
    """Returns member description within frame

    A utility function to retrieve a description of participating members
    within a frame in VerbNet.

    :param vnframe: An ElementTree containing the xml contents of
        a VerbNet frame.
    :return: description: a description dictionary with members - primary and secondary
    """
    description_element = vnframe.find("DESCRIPTION")
    return {
        "primary": description_element.attrib["primary"],
        "secondary": description_element.get("secondary", ""),
    }


# ==================================================
# Line: 407

def _get_syntactic_list_within_frame(self, vnframe):
    """Returns semantics within a frame

    A utility function to retrieve semantics within a frame in VerbNet.
    Members of the syntactic dictionary:
    1) POS Tag
    2) Modifiers

    :param vnframe: An ElementTree containing the xml contents of
        a VerbNet frame.
    :return: syntax_within_single_frame
    """
    syntax_within_single_frame = []
    for elt in vnframe.find("SYNTAX"):
        pos_tag = elt.tag
        modifiers = dict()
        modifiers["value"] = elt.get("value") if "value" in elt.attrib else ""
        modifiers["selrestrs"] = [
            {"value": restr.get("Value"), "type": restr.get("type")}
            for restr in elt.findall("SELRESTRS/SELRESTR")
        ]
        modifiers["synrestrs"] = [
            {"value": restr.get("Value"), "type": restr.get("type")}
            for restr in elt.findall("SYNRESTRS/SYNRESTR")
        ]
        syntax_within_single_frame.append(
            {"pos_tag": pos_tag, "modifiers": modifiers}
        )
    return syntax_within_single_frame


# ==================================================
# Line: 560

def _pprint_example_within_frame(self, vnframe, indent=""):
    """Returns pretty printed version of example within frame in a VerbNet class

    Return a string containing a pretty-printed representation of
    the given VerbNet frame example.

    :param vnframe: An ElementTree containing the xml contents of
        a Verbnet frame.
    """
    if vnframe["example"]:
        return indent + " Example: " + vnframe["example"]


# ==================================================
# Line: 572

def _pprint_description_within_frame(self, vnframe, indent=""):
    """Returns pretty printed version of a VerbNet frame description

    Return a string containing a pretty-printed representation of
    the given VerbNet frame description.

    :param vnframe: An ElementTree containing the xml contents of
        a VerbNet frame.
    """
    description = indent + vnframe["description"]["primary"]
    if vnframe["description"]["secondary"]:
        description += " ({})".format(vnframe["description"]["secondary"])
    return description


# ==================================================
# Line: 586

def _pprint_syntax_within_frame(self, vnframe, indent=""):
    """Returns pretty printed version of syntax within a frame in a VerbNet class

    Return a string containing a pretty-printed representation of
    the given VerbNet frame syntax.

    :param vnframe: An ElementTree containing the xml contents of
        a VerbNet frame.
    """
    pieces = []
    for element in vnframe["syntax"]:
        piece = element["pos_tag"]
        modifier_list = []
        if "value" in element["modifiers"] and element["modifiers"]["value"]:
            modifier_list.append(element["modifiers"]["value"])
        modifier_list += [
            "{}{}".format(restr["value"], restr["type"])
            for restr in (
                element["modifiers"]["selrestrs"]
                + element["modifiers"]["synrestrs"]
            )
        ]
        if modifier_list:
            piece += "[{}]".format(" ".join(modifier_list))
        pieces.append(piece)

    return indent + " ".join(pieces)


# ==================================================
# Line: 614

def _pprint_semantics_within_frame(self, vnframe, indent=""):
    """Returns a pretty printed version of semantics within frame in a VerbNet class

    Return a string containing a pretty-printed representation of
    the given VerbNet frame semantics.

    :param vnframe: An ElementTree containing the xml contents of
        a VerbNet frame.
    """
    pieces = []
    for predicate in vnframe["semantics"]:
        arguments = [argument["value"] for argument in predicate["arguments"]]
        pieces.append(
            f"{'¬' if predicate['negated'] else ''}{predicate['predicate_value']}({', '.join(arguments)})"
        )
    return "\n".join(f"{indent}* {piece}" for piece in pieces)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/opinion_lexicon.py
# Line: 118

def _read_word_block(self, stream):
    words = []
    for i in range(20):  # Read 20 lines at a time.
        line = stream.readline()
        if not line:
            continue
        words.append(line.strip())
    return words

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/twitter/twitterclient.py
# Line: 79

def on_error(self, status_code, data):
    """
    :param status_code: The status code returned by the Twitter API
    :param data: The response from Twitter API

    """
    print(status_code)


# ==================================================
