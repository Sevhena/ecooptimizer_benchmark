# string-concat-loop snippets for scikit-learn

# File: /root/ecooptimizer/scikit-learn/sklearn/datasets/_openml.py
# Occurrences: Lines 320-323 (2 instances)

for r in res:
    warning_msg += f"- version {r['version']}, status: {r['status']}\n"
    warning_msg += (
        f"  url: https://www.openml.org/search?type=data&id={r['did']}\n"
    )

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_metadata_requests.py
# Line: 1335

for metadata in self.keys:
    doc += REQUESTER_DOC_PARAM.format(metadata=metadata, method=self.name)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/_testing.py
# Occurrences: Lines 676-684 (4 instances)

for docstring, group in docstrings_grouped.items():
    if not ref_str and not ref_group:
        ref_str += docstring
        ref_group.extend(group)
    diff = list(
        context_diff(
            ref_str.split(),
            docstring.split(),
            fromfile=str(ref_group),
            tofile=str(group),
            n=8,
        )
    )
    # Add header
    msg_diff += "".join((diff[:3]))
    # Group consecutive 'diff' words to shorten error message
    for start, group in groupby(diff[3:], key=_diff_key):
        if start is None:
            msg_diff += "\n" + "\n".join(group)
        else:
            msg_diff += "\n" + start + " ".join(word[2:] for word in group)
    # Add new lines at end of diff, to separate comparisons
    msg_diff += "\n\n"

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/utils/validation.py
# Occurrences: Lines 2782-2784 (2 instances)

for i, name in enumerate(names):
    if i >= max_n_names:
        output += "- ...\n"
        break
    output += f"- {name}\n"

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/metrics/_classification.py
# Line: 2983

for row in rows:
    report += row_fmt.format(*row, width=width, digits=digits)

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/externals/_arff.py
# Line: 806

for row in s:
    self._current_line += 1
    # Ignore empty lines
    row = row.strip(' \r\n')
    if not row: continue

    u_row = row.upper()

    # DESCRIPTION -----------------------------------------------------
    if u_row.startswith(_TK_DESCRIPTION) and STATE == _TK_DESCRIPTION:
        obj['description'] += self._decode_comment(row) + '\n'
    # -----------------------------------------------------------------

    # RELATION --------------------------------------------------------
    elif u_row.startswith(_TK_RELATION):
        if STATE != _TK_DESCRIPTION:
            raise BadLayout()

        STATE = _TK_RELATION
        obj['relation'] = self._decode_relation(row)
    # -----------------------------------------------------------------

    # ATTRIBUTE -------------------------------------------------------
    elif u_row.startswith(_TK_ATTRIBUTE):
        if STATE != _TK_RELATION and STATE != _TK_ATTRIBUTE:
            raise BadLayout()

        STATE = _TK_ATTRIBUTE

        attr = self._decode_attribute(row)
        if attr[0] in attribute_names:
            raise BadAttributeName(attr[0], attribute_names[attr[0]])
        else:
            attribute_names[attr[0]] = self._current_line
        obj['attributes'].append(attr)

        if isinstance(attr[1], (list, tuple)):
            if encode_nominal:
                conversor = EncodedNominalConversor(attr[1])
            else:
                conversor = NominalConversor(attr[1])
        else:
            CONVERSOR_MAP = {'STRING': str,
                             'INTEGER': lambda x: int(float(x)),
                             'NUMERIC': float,
                             'REAL': float}
            conversor = CONVERSOR_MAP[attr[1]]

        self._conversors.append(conversor)
    # -----------------------------------------------------------------

    # DATA ------------------------------------------------------------
    elif u_row.startswith(_TK_DATA):
        if STATE != _TK_ATTRIBUTE:
            raise BadLayout()

        break
    # -----------------------------------------------------------------

    # COMMENT ---------------------------------------------------------
    elif u_row.startswith(_TK_COMMENT):
        pass
    # -----------------------------------------------------------------

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/compose/_column_transformer.py
# Line: 1185

for transformer_name, X in zip(transformer_names, Xs):
    if X.shape[1] == 0:
        continue
    dup_cols_in_transformer = sorted(
        set(X.columns).intersection(duplicated_feature_names)
    )
    if len(dup_cols_in_transformer):
        err_msg += (
            f"Transformer {transformer_name} has conflicting "
            f"columns names: {dup_cols_in_transformer}.\n"
        )

# ==================================================
# File: /root/ecooptimizer/scikit-learn/sklearn/model_selection/_validation.py
# Occurrences: Lines 897-901 (3 instances)

for scorer_name in sorted(test_scores):
    result_msg += f" {scorer_name}: ("
    if return_train_score:
        scorer_scores = train_scores[scorer_name]
        result_msg += f"train={scorer_scores:.3f}, "
    result_msg += f"test={test_scores[scorer_name]:.3f})"

# ==================================================
