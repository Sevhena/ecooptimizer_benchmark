# too-many-arguments snippets for nltk

# File: /root/ecooptimizer/nltk/nltk/classify/decisiontree.py
# Line: 137

def train(
    labeled_featuresets,
    entropy_cutoff=0.05,
    depth_cutoff=100,
    support_cutoff=10,
    binary=False,
    feature_values=None,
    verbose=False,

# ==================================================
# Line: 206

def refine(
    self,
    labeled_featuresets,
    entropy_cutoff,
    depth_cutoff,
    support_cutoff,
    binary=False,
    feature_values=None,
    verbose=False,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/classify/maxent.py
# Line: 247

def train(
    cls,
    train_toks,
    algorithm=None,
    trace=3,
    encoding=None,
    labels=None,
    gaussian_prior_sigma=0,
    **cutoffs,

# ==================================================
# Line: 1274

def calculate_deltas(
    train_toks,
    classifier,
    unattested,
    ffreq_empirical,
    nfmap,
    nfarray,
    nftranspose,
    encoding,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/boxer.py
# Line: 1163

def __init__(self, discourse_id, sent_index, word_indices, var, name, pos, sense):
    BoxerIndexed.__init__(self, discourse_id, sent_index, word_indices)
    self.var = var
    self.name = name
    self.pos = pos
    self.sense = sense


# ==================================================
# Line: 1215

def __init__(self, discourse_id, sent_index, word_indices, var, name, type, sense):
    BoxerIndexed.__init__(self, discourse_id, sent_index, word_indices)
    self.var = var
    self.name = name
    self.type = type
    self.sense = sense


# ==================================================
# Line: 1266

def __init__(self, discourse_id, sent_index, word_indices, var1, var2, rel, sense):
    BoxerIndexed.__init__(self, discourse_id, sent_index, word_indices)
    self.var1 = var1
    self.var2 = var2
    self.rel = rel
    self.sense = sense


# ==================================================
# Line: 1376

def __init__(self, discourse_id, sent_index, word_indices, var, value, type):
    BoxerIndexed.__init__(self, discourse_id, sent_index, word_indices)
    self.var = var
    self.value = value
    self.type = type


# ==================================================
# Line: 1440

def __init__(
    self, discourse_id, sent_index, word_indices, ans_types, drs1, variable, drs2

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/hole.py
# Line: 206

def _plug_hole(self, hole, ancestors0, queue, potential_labels0, plug_acc0, record):
    """
    Try all possible ways of plugging a single hole.
    See _plug_nodes for the meanings of the parameters.
    """
    # Add the current hole we're trying to plug into the list of ancestors.
    assert hole not in ancestors0
    ancestors = [hole] + ancestors0

    # Try each potential label in this hole in turn.
    for l in potential_labels0:
        # Is the label valid in this hole?
        if self._violates_constraints(l, ancestors):
            continue

        plug_acc = plug_acc0.copy()
        plug_acc[hole] = l
        potential_labels = potential_labels0.copy()
        potential_labels.remove(l)

        if len(potential_labels) == 0:
            # No more potential labels.  That must mean all the holes have
            # been filled so we have found a legal plugging so remember it.
            #
            # Note that the queue might not be empty because there might
            # be labels on there that point to formula fragments with
            # no holes in them.  _sanity_check_plugging will make sure
            # all holes are filled.
            self._sanity_check_plugging(plug_acc, self.top_hole, [])
            record.append(plug_acc)
        else:
            # Recursively try to fill in the rest of the holes in the
            # queue.  The label we just plugged into the hole could have
            # holes of its own so at the end of the queue.  Putting it on
            # the end of the queue gives us a breadth-first search, so that
            # all the holes at level i of the formula tree are filled
            # before filling level i+1.
            # A depth-first search would work as well since the trees must
            # be finite but the bookkeeping would be harder.
            self._plug_nodes(
                queue + [(l, ancestors)], potential_labels, plug_acc, record
            )


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/draw/table.py
# Line: 620

def __init__(
    self,
    master,
    column_names,
    rows=None,
    column_weights=None,
    scrollbar=True,
    click_to_sort=True,
    reprfunc=None,
    cnf={},
    **kw

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/draw/tree.py
# Line: 422

def _tree_to_treeseg(
    canvas,
    t,
    make_node,
    make_leaf,
    tree_attribs,
    node_attribs,
    leaf_attribs,
    loc_attribs,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sentiment/sentiment_analyzer.py
# Line: 196

def evaluate(
    self,
    test_set,
    classifier=None,
    accuracy=True,
    f_measure=True,
    precision=True,
    recall=True,
    verbose=False,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sentiment/util.py
# Line: 327

def json2csv_preprocess(
    json_file,
    outfile,
    fields,
    encoding="utf8",
    errors="replace",
    gzip_compress=False,
    skip_retweets=True,
    skip_tongue_tweets=True,
    skip_ambiguous_tweets=True,
    strip_off_emoticons=True,
    remove_duplicates=True,
    limit=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/meteor_score.py
# Line: 282

def single_meteor_score(
    reference: Iterable[str],
    hypothesis: Iterable[str],
    preprocess: Callable[[str], str] = str.lower,
    stemmer: StemmerI = PorterStemmer(),
    wordnet: WordNetCorpusReader = wordnet,
    alpha: float = 0.9,
    beta: float = 3.0,
    gamma: float = 0.5,

# ==================================================
# Line: 347

def meteor_score(
    references: Iterable[Iterable[str]],
    hypothesis: Iterable[str],
    preprocess: Callable[[str], str] = str.lower,
    stemmer: StemmerI = PorterStemmer(),
    wordnet: WordNetCorpusReader = wordnet,
    alpha: float = 0.9,
    beta: float = 3.0,
    gamma: float = 0.5,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/phrase_based.py
# Line: 9

def extract(
    f_start,
    f_end,
    e_start,
    e_end,
    alignment,
    f_aligned,
    srctext,
    trgtext,
    srclen,
    trglen,
    max_phrase_length,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tbl/demo.py
# Line: 140

def postag(
    templates=None,
    tagged_data=None,
    num_sents=1000,
    max_rules=300,
    min_score=3,
    min_acc=None,
    train=0.8,
    trace=3,
    randomize=False,
    ruleformat="str",
    incremental_stats=False,
    template_stats=False,
    error_output=None,
    serialize_output=None,
    learning_curve_output=None,
    learning_curve_take=300,
    baseline_backoff_tagger=None,
    separate_baseline_data=False,
    cache_baseline_tagger=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/internals.py
# Line: 494

def find_file_iter(
    filename,
    env_vars=(),
    searchpath=(),
    file_names=None,
    url=None,
    verbose=False,
    finding_dir=False,

# ==================================================
# Line: 643

def find_binary_iter(
    name,
    path_to_bin=None,
    env_vars=(),
    searchpath=(),
    binary_names=None,
    url=None,
    verbose=False,

# ==================================================
# Line: 668

def find_binary(
    name,
    path_to_bin=None,
    env_vars=(),
    searchpath=(),
    binary_names=None,
    url=None,
    verbose=False,

# ==================================================
# Line: 684

def find_jar_iter(
    name_pattern,
    path_to_jar=None,
    env_vars=(),
    searchpath=(),
    url=None,
    verbose=False,
    is_regex=False,

# ==================================================
# Line: 826

def find_jar(
    name_pattern,
    path_to_jar=None,
    env_vars=(),
    searchpath=(),
    url=None,
    verbose=False,
    is_regex=False,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/corenlp.py
# Line: 44

def __init__(
    self,
    path_to_jar=None,
    path_to_models_jar=None,
    verbose=False,
    java_options=None,
    corenlp_options=None,
    port=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/stanford.py
# Line: 38

def __init__(
    self,
    path_to_jar=None,
    path_to_models_jar=None,
    model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz",
    encoding="utf8",
    verbose=False,
    java_options="-mx4g",
    corenlp_options="",

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/featurechart.py
# Line: 618

def demo(
    print_times=True,
    print_grammar=True,
    print_trees=True,
    print_sentence=True,
    trace=1,
    parser=FeatureChartParser,
    sent="I saw John with a dog with my cookie",

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/chart.py
# Line: 1353

def __init__(
    self,
    grammar,
    strategy=BU_LC_STRATEGY,
    trace=0,
    trace_chart_width=50,
    use_agenda=True,
    chart_class=Chart,

# ==================================================
# Line: 1723

def demo(
    choice=None,
    print_times=True,
    print_grammar=False,
    print_trees=True,
    trace=2,
    sent="I saw John with a dog with my cookie",
    numparses=5,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/metrics/aline.py
# Line: 1368

def _retrieve(i, j, s, S, T, str1, str2, out):
    """
    Retrieve the path through the similarity matrix S starting at (i, j).

    :rtype: list(tuple(str, str))
    :return: Alignment of str1 and str2
    """
    if S[i, j] == 0:
        return out
    else:
        if j > 1 and S[i - 1, j - 2] + sigma_exp(str1[i - 1], str2[j - 2 : j]) + s >= T:
            out.insert(0, (str1[i - 1], str2[j - 2 : j]))
            _retrieve(
                i - 1,
                j - 2,
                s + sigma_exp(str1[i - 1], str2[j - 2 : j]),
                S,
                T,
                str1,
                str2,
                out,
            )
        elif (
            i > 1 and S[i - 2, j - 1] + sigma_exp(str2[j - 1], str1[i - 2 : i]) + s >= T
        ):
            out.insert(0, (str1[i - 2 : i], str2[j - 1]))
            _retrieve(
                i - 2,
                j - 1,
                s + sigma_exp(str2[j - 1], str1[i - 2 : i]),
                S,
                T,
                str1,
                str2,
                out,
            )
        elif S[i, j - 1] + sigma_skip(str2[j - 1]) + s >= T:
            out.insert(0, ("-", str2[j - 1]))
            _retrieve(i, j - 1, s + sigma_skip(str2[j - 1]), S, T, str1, str2, out)
        elif S[i - 1, j] + sigma_skip(str1[i - 1]) + s >= T:
            out.insert(0, (str1[i - 1], "-"))
            _retrieve(i - 1, j, s + sigma_skip(str1[i - 1]), S, T, str1, str2, out)
        elif S[i - 1, j - 1] + sigma_sub(str1[i - 1], str2[j - 1]) + s >= T:
            out.insert(0, (str1[i - 1], str2[j - 1]))
            _retrieve(
                i - 1,
                j - 1,
                s + sigma_sub(str1[i - 1], str2[j - 1]),
                S,
                T,
                str1,
                str2,
                out,
            )
    return out



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/metrics/distance.py
# Line: 41

def _edit_dist_step(
    lev, i, j, s1, s2, last_left, last_right, substitution_cost=1, transpositions=False

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/prettyprinter.py
# Line: 331

def text(
    self,
    nodedist=1,
    unicodelines=False,
    html=False,
    ansi=False,
    nodecolor="blue",
    leafcolor="red",
    funccolor="green",
    abbreviate=None,
    maxwidth=16,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/tree.py
# Line: 582

def fromstring(
    cls,
    s,
    brackets="()",
    read_node=None,
    read_leaf=None,
    node_pattern=None,
    leaf_pattern=None,
    remove_empty_top_bracketing=False,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/misc/wordfinder.py
# Line: 32

def check(word, dir, x, y, grid, rows, cols):
    if dir == 1:
        if x - len(word) < 0 or y - len(word) < 0:
            return False
        return step(word, x, lambda i: x - i, y, lambda i: y - i, grid)
    elif dir == 2:
        if x - len(word) < 0:
            return False
        return step(word, x, lambda i: x - i, y, lambda i: y, grid)
    elif dir == 3:
        if x - len(word) < 0 or y + (len(word) - 1) >= cols:
            return False
        return step(word, x, lambda i: x - i, y, lambda i: y + i, grid)
    elif dir == 4:
        if y - len(word) < 0:
            return False
        return step(word, x, lambda i: x, y, lambda i: y - i, grid)



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/featstruct.py
# Line: 1348

def unify(
    fstruct1,
    fstruct2,
    bindings=None,
    trace=False,
    fail=None,
    rename_vars=True,
    fs_class="default",

# ==================================================
# Line: 1475

def _destructively_unify(
    fstruct1, fstruct2, bindings, forward, trace, fail, fs_class, path

# ==================================================
# Line: 1578

def _unify_feature_values(
    fname, fval1, fval2, bindings, forward, trace, fail, fs_class, fpath

# ==================================================
# Line: 2530

def _read_seq_value(
    self, s, position, reentrances, match, close_paren, seq_class, plus_class

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/downloader.py
# Line: 196

def __init__(
    self,
    id,
    url,
    name=None,
    subdir="",
    size=None,
    unzipped_size=None,
    checksum=None,
    svn_revision=None,
    copyright="Unknown",
    contact="Unknown",
    license="Unknown",
    author="Unknown",
    unzip=True,
    **kw,

# ==================================================
# Line: 509

def list(
    self,
    download_dir=None,
    show_packages=True,
    show_collections=True,
    header=True,
    more_prompt=False,
    skip_installed=False,

# ==================================================
# Line: 729

def download(
    self,
    info_or_id=None,
    download_dir=None,
    quiet=False,
    force=False,
    prefix="[nltk_data] ",
    halt_on_error=True,
    raise_on_error=False,
    print_error_to=sys.stderr,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/probability.py
# Line: 1922

def plot(
    self,
    *args,
    samples=None,
    title="",
    cumulative=False,
    percents=False,
    conditions=None,
    show=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/sequential.py
# Line: 287

def __init__(
    self, n, train=None, model=None, backoff=None, cutoff=0, verbose=False

# ==================================================
# Line: 443

def __init__(
    self,
    train=None,
    model=None,
    affix_length=-3,
    min_stem_length=2,
    backoff=None,
    cutoff=0,
    verbose=False,

# ==================================================
# Line: 610

def __init__(
    self,
    feature_detector=None,
    train=None,
    classifier_builder=NaiveBayesClassifier.train,
    classifier=None,
    backoff=None,
    cutoff_prob=None,
    verbose=False,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/hmm.py
# Line: 139

def __init__(
    self, symbols, states, transitions, outputs, priors, transform=_identity

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/texttiling.py
# Line: 64

def __init__(
    self,
    w=20,
    k=10,
    similarity_method=BLOCK_COMPARISON,
    stopwords=None,
    smoothing_method=DEFAULT_SMOOTHING,
    smoothing_width=2,
    smoothing_rounds=1,
    cutoff_policy=HC,
    demo_mode=False,

# ==================================================
# Line: 381

def __init__(
    self,
    first_pos,
    ts_occurences,
    total_count=1,
    par_count=1,
    last_par=0,
    last_tok_seq=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/stanford_segmenter.py
# Line: 56

def __init__(
    self,
    path_to_jar=None,
    path_to_slf4j=None,
    java_class=None,
    path_to_model=None,
    path_to_dict=None,
    path_to_sihan_corpora_dict=None,
    sihan_post_processing="false",
    keep_whitespaces="false",
    encoding="UTF-8",
    options=None,
    verbose=False,
    java_options="-mx2g",

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/tableau.py
# Line: 103

def _attempt_proof_atom(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 126

def _attempt_proof_n_atom(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 149

def _attempt_proof_prop(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 163

def _attempt_proof_n_prop(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 177

def _attempt_proof_app(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 194

def _attempt_proof_n_app(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 212

def _attempt_proof_n_eq(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 231

def _attempt_proof_d_neg(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 237

def _attempt_proof_n_all(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 245

def _attempt_proof_n_some(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 253

def _attempt_proof_and(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 260

def _attempt_proof_n_or(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 267

def _attempt_proof_n_imp(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 274

def _attempt_proof_or(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 284

def _attempt_proof_imp(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 294

def _attempt_proof_n_and(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 304

def _attempt_proof_iff(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 316

def _attempt_proof_n_iff(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 328

def _attempt_proof_eq(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 341

def _attempt_proof_some(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# Line: 351

def _attempt_proof_all(
    self, current, context, agenda, accessible_vars, atoms, debug

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/resolution.py
# Line: 340

def _iterate_first(first, second, bindings, used, skipped, finalize_method, debug):
    """
    This method facilitates movement through the terms of 'self'
    """
    debug.line(f"unify({first},{second}) {bindings}")

    if not len(first) or not len(second):  # if no more recursions can be performed
        return finalize_method(first, second, bindings, used, skipped, debug)
    else:
        # explore this 'self' atom
        result = _iterate_second(
            first, second, bindings, used, skipped, finalize_method, debug + 1
        )

        # skip this possible 'self' atom
        newskipped = (skipped[0] + [first[0]], skipped[1])
        result += _iterate_first(
            first[1:], second, bindings, used, newskipped, finalize_method, debug + 1
        )

        try:
            newbindings, newused, unused = _unify_terms(
                first[0], second[0], bindings, used
            )
            # Unification found, so progress with this line of unification
            # put skipped and unused terms back into play for later unification.
            newfirst = first[1:] + skipped[0] + unused[0]
            newsecond = second[1:] + skipped[1] + unused[1]
            result += _iterate_first(
                newfirst,
                newsecond,
                newbindings,
                newused,
                ([], []),
                finalize_method,
                debug + 1,
            )
        except BindingException:
            # the atoms could not be unified,
            pass

        return result



# ==================================================
# Line: 384

def _iterate_second(first, second, bindings, used, skipped, finalize_method, debug):
    """
    This method facilitates movement through the terms of 'other'
    """
    debug.line(f"unify({first},{second}) {bindings}")

    if not len(first) or not len(second):  # if no more recursions can be performed
        return finalize_method(first, second, bindings, used, skipped, debug)
    else:
        # skip this possible pairing and move to the next
        newskipped = (skipped[0], skipped[1] + [second[0]])
        result = _iterate_second(
            first, second[1:], bindings, used, newskipped, finalize_method, debug + 1
        )

        try:
            newbindings, newused, unused = _unify_terms(
                first[0], second[0], bindings, used
            )
            # Unification found, so progress with this line of unification
            # put skipped and unused terms back into play for later unification.
            newfirst = first[1:] + skipped[0] + unused[0]
            newsecond = second[1:] + skipped[1] + unused[1]
            result += _iterate_second(
                newfirst,
                newsecond,
                newbindings,
                newused,
                ([], []),
                finalize_method,
                debug + 1,
            )
        except BindingException:
            # the atoms could not be unified,
            pass

        return result



# ==================================================
# File: /root/ecooptimizer/nltk/nltk/data.py
# Line: 105

def gzip_open_unicode(
    filename,
    mode="rb",
    compresslevel=9,
    encoding="utf-8",
    fileobj=None,
    errors=None,
    newline=None,

# ==================================================
# Line: 734

def load(
    resource_url,
    format="auto",
    cache=True,
    verbose=False,
    logic_parser=None,
    fstruct_reader=None,
    encoding=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/cluster/em.py
# Line: 31

def __init__(
    self,
    initial_means,
    priors=None,
    covariance_matrices=None,
    conv_threshold=1e-6,
    bias=0.1,
    normalise=False,
    svd_dimensions=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/cluster/kmeans.py
# Line: 32

def __init__(
    self,
    num_means,
    distance,
    repeats=1,
    conv_test=1e-6,
    initial_means=None,
    normalise=False,
    svd_dimensions=None,
    rng=None,
    avoid_empty_clusters=False,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/rte.py
# Line: 63

def __init__(
    self,
    pair,
    challenge=None,
    id=None,
    text=None,
    hyp=None,
    value=None,
    task=None,
    length=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/plaintext.py
# Line: 37

def __init__(
    self,
    root,
    fileids,
    word_tokenizer=WordPunctTokenizer(),
    sent_tokenizer=None,
    para_block_reader=read_blankline_block,
    encoding="utf8",

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/ppattach.py
# Line: 46

def __init__(self, sent, verb, noun1, prep, noun2, attachment):
    self.sent = sent
    self.verb = verb
    self.noun1 = noun1
    self.prep = prep
    self.noun2 = noun2
    self.attachment = attachment


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/pl196x.py
# Line: 24

def __init__(
    self,
    corpus_file,
    tagged,
    group_by_sent,
    group_by_para,
    tagset=None,
    head_len=0,
    textids=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/childes.py
# Line: 42

def words(
    self,
    fileids=None,
    speaker="ALL",
    stem=False,
    relation=False,
    strip_space=True,
    replace=False,

# ==================================================
# Line: 82

def tagged_words(
    self,
    fileids=None,
    speaker="ALL",
    stem=False,
    relation=False,
    strip_space=True,
    replace=False,

# ==================================================
# Line: 124

def sents(
    self,
    fileids=None,
    speaker="ALL",
    stem=False,
    relation=None,
    strip_space=True,
    replace=False,

# ==================================================
# Line: 166

def tagged_sents(
    self,
    fileids=None,
    speaker="ALL",
    stem=False,
    relation=None,
    strip_space=True,
    replace=False,

# ==================================================
# Line: 350

def _get_words(
    self, fileid, speaker, sent, stem, relation, pos, strip_space, replace

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/tagged.py
# Line: 39

def __init__(
    self,
    root,
    fileids,
    sep="/",
    word_tokenizer=WhitespaceTokenizer(),
    sent_tokenizer=RegexpTokenizer("\n", gaps=True),
    para_block_reader=read_blankline_block,
    encoding="utf8",
    tagset=None,

# ==================================================
# Line: 264

def __init__(
    self,
    corpus_file,
    encoding,
    tagged,
    group_by_sent,
    group_by_para,
    sep,
    word_tokenizer,
    sent_tokenizer,
    para_block_reader,
    tag_mapping_function=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/bracket_parse.py
# Line: 34

def __init__(
    self,
    root,
    fileids,
    comment_char=None,
    detect_blocks="unindented_paren",
    encoding="utf8",
    tagset=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/conll.py
# Line: 67

def __init__(
    self,
    root,
    fileids,
    columntypes,
    chunk_types=None,
    root_label="S",
    pos_in_tree=False,
    srl_includes_roleset=True,
    encoding="utf8",
    tree_class=Tree,
    tagset=None,
    separator=None,

# ==================================================
# Line: 567

def __init__(
    self, root, fileids, chunk_types, encoding="utf8", tagset=None, separator=None

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/comparative_sents.py
# Line: 56

def __init__(
    self,
    text=None,
    comp_type=None,
    entity_1=None,
    entity_2=None,
    feature=None,
    keyword=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/nombank.py
# Line: 32

def __init__(
    self,
    root,
    nomfile,
    framefiles="",
    nounsfile=None,
    parse_fileid_xform=None,
    parse_corpus=None,
    encoding="utf8",

# ==================================================
# Line: 171

def __init__(
    self,
    fileid,
    sentnum,
    wordnum,
    baseform,
    sensenumber,
    predicate,
    predid,
    arguments,
    parse_corpus=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/chunked.py
# Line: 38

def __init__(
    self,
    root,
    fileids,
    extension="",
    str2chunktree=tagstr2tree,
    sent_tokenizer=RegexpTokenizer("\n", gaps=True),
    para_block_reader=read_blankline_block,
    encoding="utf8",
    tagset=None,

# ==================================================
# Line: 206

def __init__(
    self,
    fileid,
    encoding,
    tagged,
    group_by_sent,
    group_by_para,
    chunked,
    str2chunktree,
    sent_tokenizer,
    para_block_reader,
    source_tagset=None,
    target_tagset=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/timit.py
# Line: 481

def __init__(
    self, id, sex, dr, use, recdate, birthdate, ht, race, edu, comments=None

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/wordnet.py
# Line: 280

def __init__(
    self,
    wordnet_corpus_reader,
    synset,
    name,
    lexname_index,
    lex_id,
    syntactic_marker,

# ==================================================
# Line: 2247

def digraph(
    self,
    inputs,
    rel=lambda s: s.hypernyms(),
    pos=None,
    maxdepth=-1,
    shapes=None,
    attr=None,
    verbose=False,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/chasen.py
# Line: 74

def __init__(
    self,
    corpus_file,
    encoding,
    tagged,
    group_by_sent,
    group_by_para,
    sent_splitter=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/semcor.py
# Line: 252

def __init__(self, fileid, unit, bracket_sent, pos_tag, sem_tag, wordnet):
    """
    :param fileid: The name of the underlying file.
    :param unit: One of `'token'`, `'word'`, or `'chunk'`.
    :param bracket_sent: If true, include sentence bracketing.
    :param pos_tag: Whether to include part-of-speech tags.
    :param sem_tag: Whether to include semantic tags, namely WordNet lemma
        and OOV named entity status.
    """
    if bracket_sent:
        tagspec = ".*/s"
    else:
        tagspec = ".*/s/(punc|wf)"

    self._unit = unit
    self._sent = bracket_sent
    self._pos_tag = pos_tag
    self._sem_tag = sem_tag
    self._wordnet = wordnet

    XMLCorpusView.__init__(self, fileid, tagspec)


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/dependency.py
# Line: 17

def __init__(
    self,
    root,
    fileids,
    encoding="utf8",
    word_tokenizer=TabTokenizer(),
    sent_tokenizer=RegexpTokenizer("\n", gaps=True),
    para_block_reader=read_blankline_block,

# ==================================================
# Line: 75

def __init__(
    self,
    corpus_file,
    tagged,
    group_by_sent,
    dependencies,
    chunk_types=None,
    encoding="utf8",

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/toolbox.py
# Line: 29

def fields(
    self,
    fileids,
    strip=True,
    unwrap=True,
    encoding="utf8",
    errors="strict",
    unicode_fields=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/aligned.py
# Line: 24

def __init__(
    self,
    root,
    fileids,
    sep="/",
    word_tokenizer=WhitespaceTokenizer(),
    sent_tokenizer=RegexpTokenizer("\n", gaps=True),
    alignedsent_block_reader=read_alignedsent_block,
    encoding="latin1",

# ==================================================
# Line: 121

def __init__(
    self,
    corpus_file,
    encoding,
    aligned,
    group_by_sent,
    word_tokenizer,
    sent_tokenizer,
    alignedsent_block_reader,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/propbank.py
# Line: 32

def __init__(
    self,
    root,
    propfile,
    framefiles="",
    verbsfile=None,
    parse_fileid_xform=None,
    parse_corpus=None,
    encoding="utf8",

# ==================================================
# Line: 167

def __init__(
    self,
    fileid,
    sentnum,
    wordnum,
    tagger,
    roleset,
    inflection,
    predicate,
    arguments,
    parse_corpus=None,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/twitter/twitterclient.py
# Line: 320

def tweets(
    self,
    keywords="",
    follow="",
    to_screen=True,
    stream=True,
    limit=100,
    date_limit=None,
    lang="en",
    repeat=False,
    gzip_compress=False,

# ==================================================
# Line: 446

def __init__(
    self,
    limit=2000,
    upper_date_limit=None,
    lower_date_limit=None,
    fprefix="tweets",
    subdir="twitter-files",
    repeat=False,
    gzip_compress=False,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/twitter/common.py
# Line: 147

def json2csv_entities(
    tweets_file,
    outfile,
    main_fields,
    entity_type,
    entity_fields,
    encoding="utf8",
    errors="replace",
    gzip_compress=False,

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/collocations.py
# Line: 276

def __init__(self, word_fd, quadgram_fd, ii, iii, ixi, ixxi, iixi, ixii):
    """Construct a QuadgramCollocationFinder, given FreqDists for appearances of words,
    bigrams, trigrams, two words with one word and two words between them, three words
    with a word between them in both variations.
    """
    AbstractCollocationFinder.__init__(self, word_fd, quadgram_fd)
    self.iii = iii
    self.ii = ii
    self.ixi = ixi
    self.ixxi = ixxi
    self.iixi = iixi
    self.ixii = ixii


# ==================================================
