# string-concat-loop snippets for nltk

# File: /root/ecooptimizer/nltk/nltk/ccg/lexicon.py
# Occurrences: Lines 115-124 (4 instances)

for ident in sorted(self._entries):
    if not first:
        string = string + "\n"
    string = string + ident + " => "

    first = True
    for cat in self._entries[ident]:
        if not first:
            string = string + " | "
        else:
            first = False
        string = string + "%s" % cat

# ==================================================
# Occurrences: Lines 144-146 (2 instances)

while rest != "" and not rest.startswith(")"):
    if rest.startswith("("):
        (part, rest) = matchBrackets(rest)
        inside = inside + part
    else:
        inside = inside + rest[0]
        rest = rest[1:]

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/ccg/api.py
# Line: 239

for r in self._restrs:
    r_str = r_str + "%s" % r

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/ccg/chart.py
# Occurrences: Lines 388-391 (2 instances)

for leaf, cat in leafcats:
    str_cat = "%s" % cat
    nextlen = 2 + max(len(leaf), len(str_cat))
    lcatlen = (nextlen - len(str_cat)) // 2
    rcatlen = lcatlen + (nextlen - len(str_cat)) % 2
    catstr += " " * lcatlen + str_cat + " " * rcatlen
    lleaflen = (nextlen - len(leaf)) // 2
    rleaflen = lleaflen + (nextlen - len(leaf)) % 2
    leafstr += " " * lleaflen + leaf + " " * rleaflen

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/classify/textcat.py
# Line: 183

for i in range(0, rows):
    cur_sent = " " + " ".join([raw_sentences[i][j] for j in range(0, cols[i])])
    sample += cur_sent


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/lfg.py
# Occurrences: Lines 196-208 (3 instances)

for item in self[feature]:
    if isinstance(item, FStructure):
        next_indent = indent + len(feature) + 3 + len(self.label)
        accum += "\n{}{} {}".format(
            " " * (indent),
            feature,
            item.pretty_format(next_indent),
        )
    elif isinstance(item, tuple):
        accum += "\n{}{} '{}'".format(" " * (indent), feature, item[0])
    elif isinstance(item, list):
        accum += "\n{}{} {{{}}}".format(
            " " * (indent),
            feature,
            ("\n%s" % (" " * (indent + len(feature) + 2))).join(item),
        )
    else:  # ERROR
        raise Exception(
            "feature %s is not an FStruct, a list, or a tuple" % feature
        )

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/glue.py
# Occurrences: Lines 284-290 (5 instances)

for gf in self[pos][relset]:
    if i == 1:
        accum += str_pos + ": "
    else:
        accum += " " * (len(str_pos) + 2)
    accum += "%s" % gf
    if relset and i == len(self[pos][relset]):
        accum += " : %s" % relset
    accum += "\n"
    i += 1

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/evaluate.py
# Line: 353

for val, var in variant:
    gstring += f"[{val}/{var}]"

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sem/logic.py
# Line: 232

while data[i] != end:
    if data[i] == escape:
        if incl_quotes:
            token += data[i]
        i += 1
        if len(data) == i:  # if there are no more chars
            raise LogicalExpressionException(
                None,
                "End of input reached.  "
                "Escape character [%s] found at end." % escape,
            )
        token += data[i]
    else:
        token += data[i]
    i += 1
    if len(data) == i:
        raise LogicalExpressionException(
            None, "End of input reached.  " "Expected: [%s]" % end
        )

# ==================================================
# Occurrences: Lines 240-242 (2 instances)

while data[i] != end:
    if data[i] == escape:
        if incl_quotes:
            token += data[i]
        i += 1
        if len(data) == i:  # if there are no more chars
            raise LogicalExpressionException(
                None,
                "End of input reached.  "
                "Escape character [%s] found at end." % escape,
            )
        token += data[i]
    else:
        token += data[i]
    i += 1
    if len(data) == i:
        raise LogicalExpressionException(
            None, "End of input reached.  " "Expected: [%s]" % end
        )

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/sentiment/util.py
# Occurrences: Lines 266-274 (5 instances)

for k in sorted(kwargs):
    if isinstance(kwargs[k], dict):
        dictionary = kwargs[k]
        text += f"  - **{k}:**\n"
        for entry in sorted(dictionary):
            text += f"    - {entry}: {dictionary[entry]} \n"
    elif isinstance(kwargs[k], list):
        text += f"  - **{k}:**\n"
        for entry in kwargs[k]:
            text += f"    - {entry}\n"
    else:
        text += f"  - **{k}:** {kwargs[k]} \n"

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/app/wordnet_app.py
# Occurrences: Lines 793-798 (2 instances)

for pos, pos_str, name in _pos_tuples():
    if pos in pos_forms:
        body += _hlev(3, name) + "\n"
        for w in pos_forms[pos]:
            # Not all words of exc files are in the database, skip
            # to the next word if a KeyError is raised.
            try:
                body += _collect_all_synsets(w, pos, href.synset_relations)
            except KeyError:
                pass

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/projectivedependencyparser.py
# Line: 78

for i in range(len(self._arcs)):
    str += "\n%d <- %d, %s" % (i, self._arcs[i], self._tags[i])

# ==================================================
# Line: 211

for i in range(len(tokens)):
    #                malt_format += '%s\t%s\t%d\t%s\n' % (tokens[i], 'null', parse._arcs[i] + 1, 'null')
    # conll_format += '\t%d\t%s\t%s\t%s\t%s\t%s\t%d\t%s\t%s\t%s\n' % (i+1, tokens[i], tokens[i], 'null', 'null', 'null', parse._arcs[i] + 1, 'null', '-', '-')
    # Modify to comply with the new Dependency Graph requirement (at least must have an root elements)
    conll_format += "\t%d\t%s\t%s\t%s\t%s\t%s\t%d\t%s\t%s\t%s\n" % (
        i + 1,
        tokens[i],
        tokens[i],
        "null",
        "null",
        "null",
        parse._arcs[i] + 1,
        "ROOT",
        "-",
        "-",
    )

# ==================================================
# Occurrences: Lines 360-379 (2 instances)

for i in range(len(tokens)):
    malt_format += "%s\t%s\t%d\t%s\n" % (
        tokens[i],
        "null",
        parse._arcs[i] + 1,
        "null",
    )
    # conll_format += '\t%d\t%s\t%s\t%s\t%s\t%s\t%d\t%s\t%s\t%s\n' % (i+1, tokens[i], tokens[i], parse._tags[i], parse._tags[i], 'null', parse._arcs[i] + 1, 'null', '-', '-')
    # Modify to comply with recent change in dependency graph such that there must be a ROOT element.
    conll_format += "\t%d\t%s\t%s\t%s\t%s\t%s\t%d\t%s\t%s\t%s\n" % (
        i + 1,
        tokens[i],
        tokens[i],
        parse._tags[i],
        parse._tags[i],
        "null",
        parse._arcs[i] + 1,
        "ROOT",
        "-",
        "-",
    )

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/chart.py
# Occurrences: Lines 350-351 (2 instances)

for i in range(len(self._rhs)):
    if i == self._dot:
        str += " *"
    str += " %s" % repr(self._rhs[i])

# ==================================================
# Line: 810

for tok in self._tokens:
    header += tok[: width - 1].center(width - 1) + "."

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/grammar.py
# Line: 392

for elt in self._rhs:
    result += f" '{elt}'"

# ==================================================
# Line: 890

for production in self._productions:
    result += "\n    %s" % production

# ==================================================
# Line: 1163

for production in self._productions:
    str += "\n  %s" % production

# ==================================================
# Occurrences: Lines 1208-1214 (3 instances)

for production in self._productions:
    str += "\n  %s" % production

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/inference/resolution.py
# Line: 170

for i in range(len(clauses)):
    parents = "A"
    taut = ""
    if clauses[i].is_tautology():
        taut = "Tautology"
    if clauses[i]._parents:
        parents = str(clauses[i]._parents)
    parents = " " * (max_clause_len - len(str(clauses[i])) + 1) + parents
    seq = " " * (max_seq_len - len(str(i + 1))) + str(i + 1)
    out += f"[{seq}] {clauses[i]} {parents} {taut}\n"

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/util.py
# Occurrences: Lines 165-168 (2 instances)

while width_sofar < abs_width and chars_sofar < max_chars:
    if width < 0:
        char = s[-(chars_sofar + 1)]
        result = char + result
    else:
        char = s[chars_sofar]
        result = result + char

    chars_sofar += 1
    if not unicodedata.combining(char):
        width_sofar += 1


# ==================================================
# Line: 331

for pair in attr.items():
    dot_string += f"{pair[0]} = {pair[1]};\n"


# ==================================================
# Occurrences: Lines 337-338 (2 instances)

for node in range(2):
    if shape[0] in repr(edge[node]):
        dot_string += f'"{edge[node]}" [shape = {shape[1]}];\n'

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/stem/porter.py
# Occurrences: Lines 189-191 (2 instances)

for i in range(len(stem)):
    if self._is_consonant(stem, i):
        cv_sequence += "c"
    else:
        cv_sequence += "v"


# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/conll.py
# Line: 315

for word, pos_tag, parse_tag in zip(words, pos_tags, parse_tags):
    if word == "(":
        word = "-LRB-"
    if word == ")":
        word = "-RRB-"
    if pos_tag == "(":
        pos_tag = "-LRB-"
    if pos_tag == ")":
        pos_tag = "-RRB-"
    (left, right) = parse_tag.split("*")
    right = right.count(")") * ")"  # only keep ')'.
    treestr += f"{left} ({pos_tag} {word}) {right}"

# ==================================================
# Line: 538

for (start, end), argid in inst.tagged_spans:
    if i == start:
        argstr = f"({argid}{argstr}"
    if i == (end - 1):
        argstr += ")"

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/framenet.py
# Occurrences: Lines 80-84 (4 instances)

for k in obj:
    if isinstance(obj[k], str) and len(obj[k]) > 65:
        outstr += f"[{k}]\n"
        outstr += "{}".format(_pretty_longstring(obj[k], prefix="  "))
        outstr += "\n"
    else:
        outstr += f"[{k}] {obj[k]}\n"


# ==================================================
# Line: 212

for line in textwrap.fill(", ".join(sorted(subc)), 60).split("\n"):
    outstr += f"  {line}\n"

# ==================================================
# Line: 234

for i, sent in enumerate(exemplars):
    outstr += f"[{i}] {sent.text}\n"

# ==================================================
# Line: 256

for i, sent in enumerate(sents.sentence):
    outstr += f"[{i}] {sent.text}\n"

# ==================================================
# Line: 309

for j, k, lbl in overt:
    assert j >= i, ("Overlapping targets?", (j, k, lbl))
    s1 += " " * (j - i) + "-" * (k - j)
    if len(lbl) > (k - j):
        # add space in the sentence to make room for the annotation index
        amt = len(lbl) - (k - j)
        s0 = (
            s0[: k + adjust] + "~" * amt + s0[k + adjust :]
        )  # '~' to prevent line wrapping
        s1 = s1[: k + adjust] + " " * amt + s1[k + adjust :]
        adjust += amt
    s2 += " " * (j - i) + lbl.ljust(k - j)
    i = k


# ==================================================
# Line: 318

for j, k, lbl in overt:
    assert j >= i, ("Overlapping targets?", (j, k, lbl))
    s1 += " " * (j - i) + "-" * (k - j)
    if len(lbl) > (k - j):
        # add space in the sentence to make room for the annotation index
        amt = len(lbl) - (k - j)
        s0 = (
            s0[: k + adjust] + "~" * amt + s0[k + adjust :]
        )  # '~' to prevent line wrapping
        s1 = s1[: k + adjust] + " " * amt + s1[k + adjust :]
        adjust += amt
    s2 += " " * (j - i) + lbl.ljust(k - j)
    i = k


# ==================================================
# Line: 349

for k in ("corpID", "docID", "paragNo", "sentNo", "aPos"):
    if k in sentkeys:
        outstr += f"[{k}] {sent[k]}\n"

# ==================================================
# Line: 411

for lyr in ("NER", "WSL", "Other", "Sent"):
    if lyr in sent and sent[lyr]:
        outstr += "\n[{}] {} entr{}\n".format(
            lyr, len(sent[lyr]), "ies" if len(sent[lyr]) != 1 else "y"
        )

# ==================================================
# Line: 419

for lyr in ("Verb", "Noun", "Adj", "Adv", "Prep", "Scon", "Art"):
    if lyr in sent and sent[lyr]:
        outstr += f" + [{lyr}]"

# ==================================================
# Line: 523

while short in fAbbrevs:
    if fAbbrevs[short] == fname:
        break
    r += 1
    short = fname[: k - j - 1] + str(r)

# ==================================================
# Line: 533

while short in fAbbrevs:
    if fAbbrevs[short] == fname:
        break
    r += 1
    short = fname[: k - j - 1] + str(r)

# ==================================================
# Line: 555

for j, k, fename in overt:
    s1 += " " * (j - i) + ("^" if fename.islower() else "-") * (k - j)
    short = fename[: k - j]
    if len(fename) > len(short):
        r = 0
        while short in feAbbrevs:
            if feAbbrevs[short] == fename:
                break
            r += 1
            short = fename[: k - j - 1] + str(r)
        else:  # short not in feAbbrevs
            feAbbrevs[short] = fename
    s2 += " " * (j - i) + short.ljust(k - j)
    i = k


# ==================================================
# Line: 566

while short in feAbbrevs:
    if feAbbrevs[short] == fename:
        break
    r += 1
    short = fename[: k - j - 1] + str(r)

# ==================================================
# Line: 739

for ct in sorted(
    fes.keys(),
    key=lambda ct2: [
        "Core",
        "Core-Unexpressed",
        "Peripheral",
        "Extra-Thematic",
    ].index(ct2),

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/bcp47.py
# Line: 139

for label in ["extlang", "script", "region", "variant", "extension"]:
    if label in lg_record:
        name += f": {lg_record[label]}"

# ==================================================
