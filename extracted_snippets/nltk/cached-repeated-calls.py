# cached-repeated-calls snippets for nltk

# File: /root/ecooptimizer/nltk/nltk/ccg/combinator.py
# Occurrences: Lines 274-275 (4 instances)

while categ.res().is_function():

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/ccg/lexicon.py
# Occurrences: Lines 217-222 (2 instances)

(res, var) = augParseCategory(cat_string[1:-1], primitives, families, var)

# ==================================================
# Occurrences: Lines 231-235 (2 instances)

(arg, var) = augParseCategory(cat_string[1:-1], primitives, families, var)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/ccg/chart.py
# Line: 349

if children[0].label()[0].semantics() is None:

# ==================================================
# Line: 357

function = children[0].label()[0].semantics()

# ==================================================
# Line: 369

return compute_type_raised_semantics(children[0].label()[0].semantics())

# ==================================================
# Occurrences: Lines 414-419 (3 instances)

if not isinstance(tree.label(), tuple):

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/classify/weka.py
# Occurrences: Lines 49-56 (8 instances)

if os.path.exists(os.path.join(path, "weka.jar")):

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/classify/rte_classify.py
# Occurrences: Lines 171-173 (2 instances)

clf = MaxentClassifier.train(featurized_train_set, algorithm)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/classify/positivenaivebayes.py
# Occurrences: Lines 105-106 (2 instances)

positive_feature_freqdist = defaultdict(FreqDist)

# ==================================================
# Occurrences: Lines 150-154 (2 instances)

probdist = estimator(freqdist, bins=len(feature_values[fname]))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/classify/util.py
# Line: 125

new_ll = nltk.classify.util.log_likelihood(classifier, train_toks)

# ==================================================
# Line: 141

new_acc = nltk.classify.util.log_likelihood(classifier, train_toks)

# ==================================================
# Occurrences: Lines 301-302 (2 instances)

if n > len(instances):

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/classify/maxent.py
# Line: 534

if set(mapping.values()) != set(range(len(mapping))):

# ==================================================
# Line: 546

self._length = len(mapping)

# ==================================================
# Line: 869

if set(mapping.values()) != set(range(len(mapping))):

# ==================================================
# Line: 881

self._length = len(mapping)

# ==================================================
# Occurrences: Lines 1008-1009 (6 instances)

if type(fval) in (int, float):

# ==================================================
# Occurrences: Lines 1086-1087 (2 instances)

ll = cutoffchecker.ll or log_likelihood(classifier, train_toks)

# ==================================================
# Occurrences: Lines 1118-1119 (2 instances)

ll = log_likelihood(classifier, train_toks)

# ==================================================
# Occurrences: Lines 1206-1207 (2 instances)

ll = cutoffchecker.ll or log_likelihood(classifier, train_toks)

# ==================================================
# Occurrences: Lines 1238-1239 (2 instances)

ll = log_likelihood(classifier, train_toks)

# ==================================================
# Line: 1572

wgt = numpy.array(list(map(numpy.float64, mdec.txt2list(f))))

# ==================================================
# Line: 1578

lab = mdec.txt2list(f)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/boxer.py
# Occurrences: Lines 433-441 (8 instances)

self.assertToken(self.token(), "(")

# ==================================================
# Occurrences: Lines 473-477 (2 instances)

d1 = self.process_next_expression(None)

# ==================================================
# Occurrences: Lines 485-493 (8 instances)

self.assertToken(self.token(), "(")

# ==================================================
# Occurrences: Lines 500-508 (9 instances)

self.assertToken(self.token(), "(")

# ==================================================
# Occurrences: Lines 524-525 (2 instances)

tok = self.token()

# ==================================================
# Line: 532

self.assertToken(self.token(), ")")

# ==================================================
# Occurrences: Lines 546-551 (4 instances)

((sent_index, word_indices),) = self._sent_and_word_indices(
    self._parse_index_list()
)

# ==================================================
# Occurrences: Lines 563-568 (3 instances)

self.assertToken(self.token(), ",")

# ==================================================
# Occurrences: Lines 582-587 (3 instances)

self.assertToken(self.token(), ",")

# ==================================================
# Occurrences: Lines 600-605 (3 instances)

self.assertToken(self.token(), ",")

# ==================================================
# Occurrences: Lines 625-637 (5 instances)

hour = self.token()

# ==================================================
# Occurrences: Lines 645-651 (6 instances)

self.assertToken(self.token(), "(")

# ==================================================
# Line: 687

indices = self._parse_index_list()

# ==================================================
# Line: 696

indices = self._parse_index_list()

# ==================================================
# Occurrences: Lines 706-708 (2 instances)

drs1 = self.process_next_expression(None)

# ==================================================
# Occurrences: Lines 715-721 (7 instances)

self.assertToken(self.token(), "(")

# ==================================================
# Occurrences: Lines 728-730 (2 instances)

var1 = self.parse_variable()

# ==================================================
# Occurrences: Lines 737-747 (10 instances)

self.assertToken(self.token(), "(")

# ==================================================
# Occurrences: Lines 753-762 (9 instances)

ans_types.append(self.token())

# ==================================================
# Occurrences: Lines 837-850 (10 instances)

self.discourse_id if self.discourse_id is not None else self.token()

# ==================================================
# Occurrences: Lines 856-869 (11 instances)

self.discourse_id if self.discourse_id is not None else self.token()

# ==================================================
# Occurrences: Lines 877-890 (11 instances)

self.discourse_id if self.discourse_id is not None else self.token()

# ==================================================
# Occurrences: Lines 896-917 (11 instances)

self.discourse_id if self.discourse_id is not None else self.token()

# ==================================================
# Occurrences: Lines 923-932 (6 instances)

self.discourse_id if self.discourse_id is not None else self.token()

# ==================================================
# Occurrences: Lines 938-947 (8 instances)

self.discourse_id if self.discourse_id is not None else self.token()

# ==================================================
# Occurrences: Lines 953-964 (8 instances)

self.discourse_id if self.discourse_id is not None else self.token()

# ==================================================
# Occurrences: Lines 970-983 (9 instances)

self.discourse_id if self.discourse_id is not None else self.token()

# ==================================================
# Occurrences: Lines 1536-1539 (4 instances)

return DrtOrExpression(self.interpret(ex.drs1), self.interpret(ex.drs2))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/drt.py
# Occurrences: Lines 437-442 (3 instances)

accum = reduce(AndExpression, [c.fol() for c in self.conds])

# ==================================================
# Line: 452

accum = reduce(AndExpression, [c.fol() for c in self.conds])

# ==================================================
# Occurrences: Lines 793-802 (3 instances)

first = first.replace(
    variable, expression, replace_bound, alpha_convert
)

# ==================================================
# Occurrences: Lines 813-818 (3 instances)

first = first.replace(variable, expression, replace_bound, alpha_convert)

# ==================================================
# Line: 1049

consequent = resolve_anaphora(expression.consequent, trail + [expression])

# ==================================================
# Line: 1064

consequent = resolve_anaphora(expression.consequent, trail + [expression])

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/lfg.py
# Line: 58

index = len(nodes)

# ==================================================
# Line: 75

new_index = len(nodes)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/glue.py
# Occurrences: Lines 591-591 (2 instances)

bindings = linearlogic.BindingDict()

# ==================================================
# Occurrences: Lines 617-617 (2 instances)

bindings = linearlogic.BindingDict()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/relextract.py
# Occurrences: Lines 229-230 (2 instances)

if _expand(subjclass) in NE_CLASSES[corpus]:

# ==================================================
# Occurrences: Lines 237-238 (2 instances)

if _expand(objclass) in NE_CLASSES[corpus]:

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/evaluate.py
# Line: 477

new_g = g.copy()

# ==================================================
# Line: 484

new_g = g.copy()

# ==================================================
# Line: 491

new_g = g.copy()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/logic.py
# Line: 174

while data_idx < len(data):

# ==================================================
# Line: 189

if len(data) - data_idx > len(symbol):

# ==================================================
# Occurrences: Lines 216-217 (2 instances)

mapping[len(out)] = len(data)

# ==================================================
# Occurrences: Lines 351-358 (2 instances)

accum = self.make_ApplicationExpression(
    accum, self.process_next_expression(APP)
)

# ==================================================
# Occurrences: Lines 917-920 (2 instances)

signature = expression.typecheck(signature)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/collections.py
# Occurrences: Lines 576-578 (2 instances)

for _ in self.iterate_from(len(self._cache)):

# ==================================================
# Line: 584

v = next(self._it)

# ==================================================
# Line: 592

v = next(self._it)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/draw/table.py
# Occurrences: Lines 1155-1159 (6 instances)

hyper_def = synset.hypernyms()[0].definition()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/draw/util.py
# Occurrences: Lines 1068-1072 (2 instances)

self._oval = canvas.create_oval(1, 1, 1, 1)

# ==================================================
# Occurrences: Lines 1240-1241 (2 instances)

self._obrack = canvas.create_line(1, 1, 1, 1, 1, 1, 1, 1)

# ==================================================
# Line: 1356

(x1, y1, x2, y2) = self._children[i].bbox()

# ==================================================
# Line: 1363

(x1, y1, x2, y2) = self._children[i].bbox()

# ==================================================
# Line: 1382

(x1, y1, x2, y2) = self._children[i].bbox()

# ==================================================
# Line: 1389

(x1, y1, x2, y2) = self._children[i].bbox()

# ==================================================
# Line: 1528

(x1, y1, x2, y2) = self._children[i].bbox()

# ==================================================
# Line: 1535

(x1, y1, x2, y2) = self._children[i].bbox()

# ==================================================
# Line: 1554

(x1, y1, x2, y2) = self._children[i].bbox()

# ==================================================
# Line: 1561

(x1, y1, x2, y2) = self._children[i].bbox()

# ==================================================
# Line: 2422

insert_point = self._textwidget.index("insert")

# ==================================================
# Line: 2442

insert_point = self._textwidget.index("insert")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/draw/tree.py
# Line: 243

(nodex, nodey) = self._node_bottom()

# ==================================================
# Line: 263

(nodex, nodey) = self._node_bottom()

# ==================================================
# Line: 292

(x1, y1, x2, y2) = self._subtrees[i].bbox()

# ==================================================
# Line: 301

(x1, y1, x2, y2) = self._subtrees[i].bbox()

# ==================================================
# Line: 334

(x1, y1, x2, y2) = self._subtrees[i].bbox()

# ==================================================
# Line: 343

(x1, y1, x2, y2) = self._subtrees[i].bbox()

# ==================================================
# Occurrences: Lines 966-969 (4 instances)

bold = ("helvetica", -self._size.get(), "bold")

# ==================================================
# Occurrences: Lines 975-977 (2 instances)

if self._size.get() < 20:

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sentiment/sentiment_analyzer.py
# Occurrences: Lines 226-227 (2 instances)

gold_results = defaultdict(set)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sentiment/util.py
# Occurrences: Lines 135-137 (4 instances)

start = time.time()

# ==================================================
# Occurrences: Lines 290-291 (2 instances)

if not n or n > len(all_instances):

# ==================================================
# Occurrences: Lines 828-829 (2 instances)

gold_results = defaultdict(set)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/srparser_app.py
# Line: 463

(x1, y1, x2, y2) = self._stacklabel.bbox()

# ==================================================
# Occurrences: Lines 469-471 (2 instances)

(x1, y1, x2, y2) = self._stacklabel.bbox()

# ==================================================
# Occurrences: Lines 516-520 (2 instances)

self._rtextlabel.move(cx2 - self._rtextlabel.bbox()[2] - 5, 0)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/chartparser_app.py
# Line: 1217

lhs = edge.lhs()

# ==================================================
# Line: 1226

lhs = edge.lhs()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/chunkparser_app.py
# Occurrences: Lines 702-706 (2 instances)

t0 = time.time()

# ==================================================
# Line: 766

self._adaptively_modify_eval_chunk(time.time() - t0)

# ==================================================
# Occurrences: Lines 1188-1190 (6 instances)

self.charnum[sentnum, wordnum] = len(linestr)

# ==================================================
# Occurrences: Lines 1228-1229 (4 instances)

comment_start = m.start(2)

# ==================================================
# Line: 1262

self._last_keypress = time.time()

# ==================================================
# Line: 1300

self.grammar_changed = time.time()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/wordnet_app.py
# Line: 85

if unquote_plus(sp) == "SHUTDOWN THE SERVER":

# ==================================================
# Line: 104

usp = unquote_plus(sp)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/help.py
# Occurrences: Lines 53-58 (2 instances)

_print_entries(sorted(tagdict), tagdict)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/gale_church.py
# Occurrences: Lines 179-179 (3 instances)

min_dist = float("inf")

# ==================================================
# Occurrences: Lines 193-193 (3 instances)

if min_dist == float("inf"):

# ==================================================
# Occurrences: Lines 247-250 (2 instances)

v = it.next()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/nist_score.py
# Line: 100

total_reference_words += len(reference)

# ==================================================
# Occurrences: Lines 128-141 (14 instances)

hyp_len = len(hypothesis)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm_model.py
# Line: 77

self.translation_table = defaultdict(
    lambda: defaultdict(lambda: IBMModel.MIN_PROB)
)

# ==================================================
# Line: 87

lambda: defaultdict(lambda: defaultdict(lambda: IBMModel.MIN_PROB))

# ==================================================
# Line: 297

new_cepts = deepcopy(original_cepts)

# ==================================================
# Line: 321

new_cepts = deepcopy(original_cepts)

# ==================================================
# Occurrences: Lines 524-529 (6 instances)

self.t_given_s = defaultdict(lambda: defaultdict(float))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/chrf_score.py
# Occurrences: Lines 191-194 (2 instances)

assert len(references) == len(
    hypotheses
), "The number of hypotheses and their references should be the same"

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/lepor.py
# Occurrences: Lines 114-114 (2 instances)

distance = abs(hyp_index - ref_index)

# ==================================================
# Occurrences: Lines 126-126 (2 instances)

distance = abs(hyp_index - ref_index)

# ==================================================
# Occurrences: Lines 133-133 (2 instances)

distance = abs(hyp_index - ref_index)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm3.py
# Occurrences: Lines 337-341 (2 instances)

lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(float)))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm2.py
# Occurrences: Lines 307-311 (2 instances)

lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(float)))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm5.py
# Line: 258

self.head_vacancy_table = defaultdict(
    lambda: defaultdict(lambda: defaultdict(lambda: self.MIN_PROB))
)

# ==================================================
# Line: 267

self.non_head_vacancy_table = defaultdict(
    lambda: defaultdict(lambda: defaultdict(lambda: self.MIN_PROB))
)

# ==================================================
# Occurrences: Lines 301-310 (12 instances)

self.head_vacancy_table[dv][max_v] = defaultdict(lambda: initial_prob)

# ==================================================
# Occurrences: Lines 584-589 (6 instances)

self.head_vacancy = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm4.py
# Line: 240

lambda: defaultdict(lambda: defaultdict(lambda: self.MIN_PROB))

# ==================================================
# Line: 248

self.non_head_distortion_table = defaultdict(
    lambda: defaultdict(lambda: self.MIN_PROB)
)

# ==================================================
# Occurrences: Lines 282-289 (12 instances)

self.head_distortion_table[dj] = defaultdict(
    lambda: defaultdict(lambda: initial_prob)
)

# ==================================================
# Occurrences: Lines 460-464 (7 instances)

lambda: defaultdict(lambda: defaultdict(float))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tbl/demo.py
# Line: 256

baseline_tagger = pickle.load(print_rules)

# ==================================================
# Line: 269

tbrill = time.time()

# ==================================================
# Line: 275

print(f"Trained tbl tagger in {time.time() - tbrill:0.2f} seconds")

# ==================================================
# Line: 310

taggedtest = brill_tagger.tag_sents(testing_data)

# ==================================================
# Occurrences: Lines 323-330 (3 instances)

taggedtest = brill_tagger.tag_sents(testing_data)

# ==================================================
# Occurrences: Lines 345-348 (3 instances)

if num_sents is None or len(tagged_data) <= num_sents:

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/internals.py
# Occurrences: Lines 1060-1066 (3 instances)

stop = len(sequence)

# ==================================================
# Line: 1075

stop = len(sequence)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/transitionparser.py
# Line: 97

feats = token["feats"].split("|")

# ==================================================
# Line: 137

feats = token["feats"].split("|")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/nonprojectivedependencyparser.py
# Line: 483

nr_vertices = len(tokens)

# ==================================================
# Line: 539

for i in range(len(tokens) + 1, nr_vertices + 1):

# ==================================================
# Line: 549

for i in range(1, len(tokens) + 1):

# ==================================================
# Occurrences: Lines 643-648 (6 instances)

if len(possible_heads[i]) == 1:

# ==================================================
# Occurrences: Lines 656-656 (2 instances)

orig_length = len(possible_heads[i])

# ==================================================
# Occurrences: Lines 665-665 (2 instances)

head = possible_heads[i].pop()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/viterbi.py
# Occurrences: Lines 412-418 (4 instances)

t = time.time()

# ==================================================
# Occurrences: Lines 429-433 (2 instances)

p = reduce(lambda a, b: a + b.prob(), parses, 0) / len(parses)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/projectivedependencyparser.py
# Line: 667

trees = pdp.parse(["the", "price", "of", "the", "stock", "fell"])

# ==================================================
# Line: 691

trees = pdp.parse(["the", "price", "of", "the", "stock", "fell"])

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/pchart.py
# Occurrences: Lines 525-527 (4 instances)

t = time.time()

# ==================================================
# Line: 561

draw_parses = sys.stdin.readline().strip().lower().startswith("y")

# ==================================================
# Line: 572

print_parses = sys.stdin.readline().strip().lower().startswith("y")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/dependencygraph.py
# Line: 291

index = int(line_index)

# ==================================================
# Line: 300

index = int(line_index)

# ==================================================
# Occurrences: Lines 323-325 (4 instances)

cell_number = len(cells)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/featurechart.py
# Occurrences: Lines 278-286 (5 instances)

found = right_edge.lhs()

# ==================================================
# Line: 299

bindings = left_edge.bindings()

# ==================================================
# Occurrences: Lines 639-644 (2 instances)

t = perf_counter()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/earleychart.py
# Occurrences: Lines 534-537 (2 instances)

t = perf_counter()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/chart.py
# Line: 1264

end = right_edge.end()

# ==================================================
# Line: 1270

new_edge = left_edge.move_dot_forward(right_edge.end())

# ==================================================
# Occurrences: Lines 1278-1281 (4 instances)

end = right_edge.end()

# ==================================================
# Occurrences: Lines 1791-1795 (4 instances)

t = time.time()

# ==================================================
# Line: 1810

t = time.time()

# ==================================================
# Line: 1824

times["Stepping"] = time.time() - t

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/metrics/confusionmatrix.py
# Line: 45

if len(reference) != len(test):

# ==================================================
# Line: 79

self._total = len(reference)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/metrics/paice.py
# Line: 364

for stem in sorted(stems):

# ==================================================
# Line: 380

for stem in sorted(stems):

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/lm/api.py
# Occurrences: Lines 215-218 (2 instances)

samples = self.context_counts(self.vocab.lookup(context))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/prettyprinter.py
# Occurrences: Lines 89-94 (4 instances)

a.append(len(sentence))

# ==================================================
# Occurrences: Lines 152-164 (14 instances)

minidx, maxidx = min(candidates), max(candidates)

# ==================================================
# Occurrences: Lines 176-176 (4 instances)

for a in row[min(candidates) : max(candidates) + 1]

# ==================================================
# Line: 204

leaves = tree.leaves()

# ==================================================
# Line: 213

"%r\nsentence: %s" % (len(sentence), tree.leaves(), sentence)

# ==================================================
# Line: 261

startoflevel = len(matrix)

# ==================================================
# Occurrences: Lines 453-453 (2 instances)

branchrow[col] = crosscell(branchrow[col])

# ==================================================
# Occurrences: Lines 479-479 (2 instances)

branchrow[col] = crosscell(branchrow[col])

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/parented.py
# Occurrences: Lines 365-366 (4 instances)

while root.parent() is not None:

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/transforms.py
# Occurrences: Lines 136-139 (4 instances)

originalNode = node.label()

# ==================================================
# Occurrences: Lines 314-318 (2 instances)

cnfTree = deepcopy(collapsedTree)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/featstruct.py
# Occurrences: Lines 1241-1246 (2 instances)

vars = find_variables(fstruct, fs_class)

# ==================================================
# Occurrences: Lines 1651-1658 (3 instances)

if isinstance(fval2, CustomFeatureValue) and result != fval2.unify(fval1):

# ==================================================
# Occurrences: Lines 2259-2260 (2 instances)

if match.group(1):

# ==================================================
# Occurrences: Lines 2283-2290 (6 instances)

match = self._END_FSTRUCT_RE.match(s, position)

# ==================================================
# Occurrences: Lines 2297-2297 (2 instances)

position = match.end()

# ==================================================
# Occurrences: Lines 2306-2306 (2 instances)

if self._END_FSTRUCT_RE.match(s, position):

# ==================================================
# Occurrences: Lines 2313-2313 (2 instances)

position = match.end()

# ==================================================
# Occurrences: Lines 2320-2323 (2 instances)

if match.group(2):

# ==================================================
# Line: 2331

return self._finalize(s, match.end(), reentrances, fstruct)

# ==================================================
# Occurrences: Lines 2344-2346 (4 instances)

match = self._END_FSTRUCT_RE.match(s, position)

# ==================================================
# Occurrences: Lines 2352-2353 (3 instances)

name = match.group(2)

# ==================================================
# Occurrences: Lines 2366-2368 (4 instances)

if match.group(1) == "+":

# ==================================================
# Occurrences: Lines 2375-2382 (6 instances)

position = match.end()

# ==================================================
# Occurrences: Lines 2389-2389 (2 instances)

position = match.end()

# ==================================================
# Occurrences: Lines 2399-2399 (2 instances)

if self._END_FSTRUCT_RE.match(s, position):

# ==================================================
# Occurrences: Lines 2406-2406 (2 instances)

position = match.end()

# ==================================================
# Line: 2541

return seq_class(), m.end()

# ==================================================
# Occurrences: Lines 2550-2552 (4 instances)

return plus_class(values), m.end()

# ==================================================
# Occurrences: Lines 2564-2564 (2 instances)

position = m.end()

# ==================================================
# Occurrences: Lines 2687-2687 (2 instances)

input = sys.stdin.readline().strip()

# ==================================================
# Occurrences: Lines 2719-2719 (2 instances)

input = sys.stdin.readline().strip()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tgrep.py
# Line: 444

idx = int(operator[1:])

# ==================================================
# Line: 456

idx = int(operator[1:])

# ==================================================
# Occurrences: Lines 864-865 (2 instances)

tgrep_expr = pyparsing.Forward()

# ==================================================
# Line: 909

tgrep_rel_conjunction = pyparsing.Forward()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/downloader.py
# Line: 687

os.makedirs(os.path.join(download_dir, info.subdir), exist_ok=True)

# ==================================================
# Line: 716

zipdir = os.path.join(download_dir, info.subdir)

# ==================================================
# Occurrences: Lines 865-868 (2 instances)

return self._pkg_status(info, filepath)

# ==================================================
# Line: 928

or time.time() - self._index_timestamp > self.INDEX_TIMEOUT

# ==================================================
# Line: 939

self._index_timestamp = time.time()

# ==================================================
# Occurrences: Lines 1448-1455 (4 instances)

tabframe = tkinter.Frame(f1)

# ==================================================
# Line: 1557

filemenu = tkinter.Menu(menubar, tearoff=0)

# ==================================================
# Line: 1583

viewmenu = tkinter.Menu(menubar, tearoff=0)

# ==================================================
# Line: 1598

sortmenu = tkinter.Menu(menubar, tearoff=0)

# ==================================================
# Line: 1613

helpmenu = tkinter.Menu(menubar, tearoff=0)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/probability.py
# Occurrences: Lines 659-663 (2 instances)

total = sum(randrow)

# ==================================================
# Line: 851

if (bins is not None) and (bins < freqdist.B()):

# ==================================================
# Line: 857

+ "to create it (%d)." % freqdist.B()

# ==================================================
# Line: 865

bins = freqdist.B()

# ==================================================
# Occurrences: Lines 1259-1266 (5 instances)

assert bins is None or bins >= freqdist.B(), (

# ==================================================
# Occurrences: Lines 1731-1733 (3 instances)

self._wordtypes_after = defaultdict(float)

# ==================================================
# Occurrences: Lines 2478-2480 (3 instances)

fdist1 = _create_rand_fdist(numsamples, numoutcomes)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/senna.py
# Occurrences: Lines 111-117 (4 instances)

_chunk_str = " ".join(current_chunk)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/brill_trainer.py
# Occurrences: Lines 339-343 (4 instances)

self._rules_by_position = defaultdict(set)

# ==================================================
# Occurrences: Lines 588-590 (2 instances)

assert self._rule_scores[rule] == sum(self._positions_by_rule[rule].values())

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/sequential.py
# Occurrences: Lines 716-721 (2 instances)

prevword = tokens[index - 1].lower()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/hmm.py
# Line: 496

symbol = self._sample_probdist(
    self._outputs[state], rng.random(), self._symbols
)

# ==================================================
# Line: 506

symbol = self._sample_probdist(
    self._outputs[state], rng.random(), self._symbols
)

# ==================================================
# Occurrences: Lines 897-898 (2 instances)

A_denom = _ninf_array(N)

# ==================================================
# Occurrences: Lines 920-922 (4 instances)

A_denom = np.logaddexp2(A_denom, alpha_plus_beta)

# ==================================================
# Occurrences: Lines 1004-1005 (4 instances)

A_denom = _ninf_array(N)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/brill.py
# Line: 432

testing_stats["initialerrors"] = counterrors(tagged_tokenses)

# ==================================================
# Line: 441

errors.append(counterrors(tagged_tokenses))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/perceptron.py
# Occurrences: Lines 44-48 (2 instances)

self._totals = defaultdict(int)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/grammar.py
# Line: 827

start = grammar.start()

# ==================================================
# Line: 836

result.append(Production(start, [grammar.start()]))

# ==================================================
# Line: 1370

lhs, pos = nonterm_parser(line, pos)

# ==================================================
# Line: 1376

pos = m.end()

# ==================================================
# Occurrences: Lines 1385-1385 (2 instances)

pos = m.end()

# ==================================================
# Occurrences: Lines 1399-1399 (2 instances)

pos = m.end()

# ==================================================
# Occurrences: Lines 1406-1410 (3 instances)

pos = m.end()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/chat/util.py
# Line: 76

pos = response.find("%")

# ==================================================
# Line: 84

pos = response.find("%")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/legality_principle.py
# Occurrences: Lines 131-131 (2 instances)

vowel = bool(char_lower in self.vowels)

# ==================================================
# Occurrences: Lines 144-144 (2 instances)

vowel = bool(char_lower in self.vowels)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/texttiling.py
# Occurrences: Lines 214-218 (6 instances)

if pb.start() - last_break < MIN_PARAGRAPH:

# ==================================================
# Occurrences: Lines 240-243 (2 instances)

current_par_break = next(pb_iter)

# ==================================================
# Line: 252

current_par_break = next(pb_iter)

# ==================================================
# Occurrences: Lines 365-366 (6 instances)

if best_fit > abs(br - char_count):

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/treebank.py
# Occurrences: Lines 137-152 (5 instances)

text = regexp.sub(substitution, text)

# ==================================================
# Occurrences: Lines 158-163 (3 instances)

text = regexp.sub(substitution, text)

# ==================================================
# Occurrences: Lines 367-398 (10 instances)

text = regexp.sub(r"\1\2", text)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/destructive.py
# Occurrences: Lines 158-173 (5 instances)

text = regexp.sub(substitution, text)

# ==================================================
# Occurrences: Lines 179-184 (3 instances)

text = regexp.sub(substitution, text)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/nist.py
# Occurrences: Lines 133-136 (2 instances)

text = regexp.sub(substitution, text)

# ==================================================
# Occurrences: Lines 165-167 (2 instances)

text = regexp.sub(substitution, text)

# ==================================================
# Line: 174

text = regexp.sub(substitution, text)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/sexpr.py
# Occurrences: Lines 122-132 (10 instances)

result += text[pos : m.start()].split()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tokenize/punkt.py
# Occurrences: Lines 1431-1431 (2 instances)

yield slice(last_break, match.end())

# ==================================================
# Occurrences: Lines 1437-1437 (2 instances)

last_break = match.end()

# ==================================================
# Line: 1660

is_sent_starter = self._ortho_heuristic(aug_tok2)

# ==================================================
# Line: 1680

is_sent_starter = self._ortho_heuristic(aug_tok2)

# ==================================================
# Occurrences: Lines 1766-1768 (2 instances)

params.sent_starters = pdec.txt2set(f)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/mace.py
# Occurrences: Lines 68-75 (6 instances)

num_entities = int(l[l.index("(") + 1 : l.index(",")].strip())

# ==================================================
# Occurrences: Lines 93-93 (2 instances)

value = int(l[l.index("[") + 1 : l.index("]")].strip())

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/resolution.py
# Occurrences: Lines 510-513 (4 instances)

return _clausify(expression.first) + _clausify(expression.second)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/nonmonotonic.py
# Occurrences: Lines 229-234 (4 instances)

antecedent = self._make_antecedent(p, new_sig)

# ==================================================
# Occurrences: Lines 334-335 (2 instances)

self.signature_len = len(new_sig)

# ==================================================
# Occurrences: Lines 348-350 (3 instances)

p1 = lexpr(r"exists x.walk(x)")

# ==================================================
# Occurrences: Lines 360-363 (4 instances)

p1 = lexpr(r"exists x.walk(x)")

# ==================================================
# Occurrences: Lines 373-376 (4 instances)

p1 = lexpr(r"exists x.walk(x)")

# ==================================================
# Line: 386

p1 = lexpr(r"walk(Socrates)")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/data.py
# Occurrences: Lines 188-192 (2 instances)

name = normalize_resource_name(name, False, None)

# ==================================================
# Line: 547

pieces = resource_name.split("/")

# ==================================================
# Line: 556

resource_zipname = resource_name.split("/")[1]

# ==================================================
# Occurrences: Lines 839-841 (2 instances)

resource_val = opened_resource.read()

# ==================================================
# Line: 859

binary_data = opened_resource.read()

# ==================================================
# Line: 1370

return self.stream.tell() - len(self.bytebuffer)

# ==================================================
# Line: 1376

orig_filepos = self.stream.tell()

# ==================================================
# Line: 1387

filepos = self.stream.tell()

# ==================================================
# Line: 1428

chars, bytes_decoded = self._incr_decode(bytes)

# ==================================================
# Line: 1437

chars, bytes_decoded = self._incr_decode(bytes)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/util.py
# Occurrences: Lines 1034-1037 (2 instances)

max_len = len(sequence)

# ==================================================
# Line: 1123

end = file.tell() - 1

# ==================================================
# Line: 1142

offset = file.tell()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/cluster/em.py
# Line: 93

lastl = self._loglikelihood(vectors, priors, means, covariances)

# ==================================================
# Line: 127

l = self._loglikelihood(vectors, priors, means, covariances)

# ==================================================
# Occurrences: Lines 206-211 (2 instances)

vector = numpy.array([2, 2])

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/snowball.py
# Occurrences: Lines 1519-1523 (6 instances)

word = "".join((word, "e"))

# ==================================================
# Occurrences: Lines 1543-1549 (6 instances)

word = "".join((word, "e"))

# ==================================================
# Occurrences: Lines 1606-1614 (3 instances)

word = suffix_replace(word, suffix, "ate")

# ==================================================
# Occurrences: Lines 1701-1709 (3 instances)

word = suffix_replace(word, suffix, "ate")

# ==================================================
# Line: 2285

word = "".join((word[:i], "U", word[i + 1 :]))

# ==================================================
# Line: 2294

word = "".join((word[:i], "U", word[i + 1 :]))

# ==================================================
# Occurrences: Lines 2366-2366 (2 instances)

word = "".join((word[:-2], "l"))

# ==================================================
# Occurrences: Lines 2409-2409 (2 instances)

word = "".join((word[:-2], "iqU"))

# ==================================================
# Occurrences: Lines 2431-2431 (2 instances)

word = "".join((word[:-2], "l"))

# ==================================================
# Occurrences: Lines 2437-2437 (2 instances)

word = "".join((word[:-2], "iqU"))

# ==================================================
# Occurrences: Lines 2454-2454 (2 instances)

word = "".join((word[:-2], "iqU"))

# ==================================================
# Occurrences: Lines 3025-3029 (4 instances)

word = suffix_replace(word, suffix, "e")

# ==================================================
# Occurrences: Lines 3036-3041 (4 instances)

word = suffix_replace(word, suffix, "a")

# ==================================================
# Occurrences: Lines 3062-3067 (4 instances)

word = suffix_replace(word, suffix, "a")

# ==================================================
# Occurrences: Lines 3078-3083 (4 instances)

word = suffix_replace(word, suffix, "a")

# ==================================================
# Occurrences: Lines 3101-3102 (2 instances)

word = suffix_replace(word, suffix, "a")

# ==================================================
# Occurrences: Lines 3112-3113 (2 instances)

word = suffix_replace(word, suffix, "e")

# ==================================================
# Occurrences: Lines 3124-3126 (2 instances)

word = suffix_replace(word, suffix, "a")

# ==================================================
# Line: 3409

word = "".join((word[:i], "U", word[i + 1 :]))

# ==================================================
# Line: 3416

word = "".join((word[:i], "U", word[i + 1 :]))

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/lancaster.py
# Occurrences: Lines 262-264 (3 instances)

word = self.__applyRule(
    word, remove_total, append_string
)

# ==================================================
# Occurrences: Lines 270-272 (3 instances)

word = self.__applyRule(
    word, remove_total, append_string
)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/isri.py
# Occurrences: Lines 209-210 (2 instances)

token = self.pro_w6(token)

# ==================================================
# Occurrences: Lines 216-217 (2 instances)

token = self.pro_w6(token)

# ==================================================
# Occurrences: Lines 228-233 (4 instances)

word = self.re_short_vowels.sub("", word)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/chunk/named_entity.py
# Occurrences: Lines 71-80 (4 instances)

prevword = tokens[index - 1][0].lower()

# ==================================================
# Occurrences: Lines 89-95 (4 instances)

nextword = tokens[index + 1][0].lower()

# ==================================================
# Line: 270

for s, e, typ in sorted(entities):

# ==================================================
# Line: 285

for s, e, typ in sorted(entities):

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/chunk/regexp.py
# Occurrences: Lines 1348-1362 (6 instances)

if chunkscore.missed():

# ==================================================
# Line: 1395

cp = chunk.RegexpParser(grammar)

# ==================================================
# Line: 1404

cp = chunk.RegexpParser(grammar)

# ==================================================
# Line: 1411

cp = chunk.RegexpParser(grammar)

# ==================================================
# Line: 1421

cp = chunk.RegexpParser(grammar)

# ==================================================
# Line: 1443

cp = chunk.RegexpParser(grammar)

# ==================================================
# Line: 1456

cp = chunk.RegexpParser(grammar)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/pl196x.py
# Occurrences: Lines 107-108 (2 instances)

self._f2t = defaultdict(list)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/ipipan.py
# Line: 270

lines = self._read_data(stream)

# ==================================================
# Line: 276

lines = self._read_data(stream)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/childes.py
# Occurrences: Lines 373-374 (6 instances)

elif replace and xmlsent.find(f".//{{{NS}}}w/{{{NS}}}wk"):

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/reviews.py
# Occurrences: Lines 287-290 (2 instances)

line = stream.readline()

# ==================================================
# Line: 300

line = stream.readline()

# ==================================================
# Line: 306

if re.match(TITLE, line):

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/conll.py
# Occurrences: Lines 370-372 (2 instances)

rolesets = self._get_column(grid, self._colmap["srl"])

# ==================================================
# Line: 546

pos[wordnum] = tree.label()

# ==================================================
# Line: 554

synt[wordnum] = f"({tree.label()}{synt[wordnum]}"

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/comparative_sents.py
# Occurrences: Lines 226-226 (2 instances)

line = stream.readline()

# ==================================================
# Occurrences: Lines 234-238 (4 instances)

comparison_text = stream.readline().strip()

# ==================================================
# Occurrences: Lines 245-258 (16 instances)

comp_type = int(re.match(r"<cs-(\d)>", comp).group(1))

# ==================================================
# Occurrences: Lines 268-268 (2 instances)

comp_type = int(re.match(r"<cs-(\d)>", comp).group(1))

# ==================================================
# Occurrences: Lines 285-288 (4 instances)

line = stream.readline()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/api.py
# Occurrences: Lines 332-333 (2 instances)

self._f2c = defaultdict(set)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/framenet.py
# Line: 813

outstr = _pretty_any(self)

# ==================================================
# Line: 843

outstr = _pretty_any(self)

# ==================================================
# Line: 1783

f = self.frame_by_id(luinfo.frameID)

# ==================================================
# Line: 1789

f = self.frame_by_id(luinfo.frameID)

# ==================================================
# Line: 2222

frameIDs = {f.ID for f in self.frames(frame)}

# ==================================================
# Line: 2230

frames = self.frames(frame)

# ==================================================
# Occurrences: Lines 3023-3025 (4 instances)

luinfo["sentenceCount"] = self._load_xml_attributes(PrettyDict(), sub)

# ==================================================
# Occurrences: Lines 3032-3032 (2 instances)

semtypeinfo = self._load_xml_attributes(PrettyDict(), sub)

# ==================================================
# Occurrences: Lines 3276-3281 (6 instances)

stinfo = self._load_xml_attributes(AttrDict(), sub)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/nkjp.py
# Occurrences: Lines 262-270 (10 instances)

ret = " ".join(x)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/nombank.py
# Occurrences: Lines 123-127 (2 instances)

if framefile not in self.fileids():

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/wordnet.py
# Occurrences: Lines 1161-1169 (3 instances)

self._lemma_pos_offset_map = defaultdict(dict)

# ==================================================
# Occurrences: Lines 1393-1414 (36 instances)

lemma = _next_token()

# ==================================================
# Occurrences: Lines 1615-1630 (12 instances)

synset._offset = int(_next_token())

# ==================================================
# Occurrences: Lines 1640-1645 (11 instances)

n_pointers = int(_next_token())

# ==================================================
# Occurrences: Lines 1658-1658 (2 instances)

frame_count = int(_next_token())

# ==================================================
# Occurrences: Lines 1664-1669 (8 instances)

plus = _next_token()

# ==================================================
# Occurrences: Lines 1889-1890 (4 instances)

offset = data_file.tell()

# ==================================================
# Occurrences: Lines 1910-1911 (4 instances)

offset = data_file.tell()

# ==================================================
# Occurrences: Lines 2354-2355 (2 instances)

ic[NOUN] = defaultdict(float)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/ieer.py
# Line: 101

line = stream.readline()

# ==================================================
# Line: 109

line = stream.readline()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/xmldocs.py
# Occurrences: Lines 157-162 (2 instances)

s = infile.readline()

# ==================================================
# Line: 253

startpos = stream.tell()

# ==================================================
# Line: 265

pos = stream.tell() - (

# ==================================================
# Line: 302

context = list(self._tag_context.get(stream.tell()))

# ==================================================
# Line: 313

startpos = stream.tell()

# ==================================================
# Occurrences: Lines 329-329 (3 instances)

name = self._XML_TAG_NAME.match(piece.group()).group(1)

# ==================================================
# Occurrences: Lines 336-339 (6 instances)

elt_depth = len(context)

# ==================================================
# Occurrences: Lines 346-346 (3 instances)

if elt_start is not None and elt_depth == len(context):

# ==================================================
# Occurrences: Lines 355-355 (3 instances)

name = self._XML_TAG_NAME.match(piece.group()).group(1)

# ==================================================
# Line: 385

pos = stream.tell()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/util.py
# Occurrences: Lines 212-215 (2 instances)

open(self._fileid, "rb"), self._encoding

# ==================================================
# Line: 562

line = stream.readline()

# ==================================================
# Line: 572

line = stream.readline()

# ==================================================
# Line: 608

block = stream.read(block_size)

# ==================================================
# Line: 647

next_block = stream.read(block_size)

# ==================================================
# Line: 725

return sorted(items)

# ==================================================
# Line: 741

return sorted(items)

# ==================================================
# Occurrences: Lines 752-754 (4 instances)

child, dirname = os.path.split(child)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/verbnet.py
# Occurrences: Lines 40-44 (2 instances)

self._lemma_to_class = defaultdict(list)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/util.py
# Occurrences: Lines 73-84 (4 instances)

root = nltk.data.find(f"{self.subdir}/{zip_name}")

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/toolbox.py
# Line: 75

mkr, line_value = mobj.groups()

# ==================================================
# Line: 81

line_mkr, line_value = mobj.groups()

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/twitter/twitterclient.py
# Line: 229

count = len(results["statuses"])

# ==================================================
# Line: 265

count = len(results["statuses"])

# ==================================================
