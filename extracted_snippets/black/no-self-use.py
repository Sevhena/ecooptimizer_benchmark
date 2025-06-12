# no-self-use snippets for black

# File: /root/ecooptimizer/black/src/black/trans.py
# Line: 1008

def _transform_to_new_line(
    self, line: Line, string_and_rpar_indices: list[int]

# ==================================================
# Line: 1739

def _iter_fexpr_slices(self, string: str) -> Iterator[tuple[Index, Index]]:
    """
    Yields:
        All ranges of @string which, if @string were to be split there,
        would result in the splitting of an f-expression (which is NOT
        allowed).
    """
    if "f" not in get_string_prefix(string).lower():
        return
    yield from iter_fexpr_spans(string)


# ==================================================
# Line: 1850

def _normalize_f_string(self, string: str, prefix: str) -> str:
    """
    Pre-Conditions:
        * assert_is_leaf_string(@string)

    Returns:
        * If @string is an f-string that contains no f-expressions, we
        return a string identical to @string except that the 'f' prefix
        has been stripped and all double braces (i.e. '{{' or '}}') have
        been normalized (i.e. turned into '{' or '}').
            OR
        * Otherwise, we return @string.
    """
    assert_is_leaf_string(string)

    if "f" in prefix and not fstring_contains_expr(string):
        new_prefix = prefix.replace("f", "")

        temp = string[len(prefix) :]
        temp = re.sub(r"\{\{", "{", temp)
        temp = re.sub(r"\}\}", "}", temp)
        new_string = temp

        return f"{new_prefix}{new_string}"
    else:
        return string


# ==================================================
# File: /root/ecooptimizer/black/src/blib2to3/pgen2/driver.py
# Line: 196

def _partially_consume_prefix(self, prefix: str, column: int) -> tuple[str, str]:
    lines: list[str] = []
    current_line = ""
    current_column = 0
    wait_for_nl = False
    for char in prefix:
        current_line += char
        if wait_for_nl:
            if char == "\n":
                if current_line.strip() and current_column < column:
                    res = "".join(lines)
                    return res, prefix[len(res) :]

                lines.append(current_line)
                current_line = ""
                current_column = 0
                wait_for_nl = False
        elif char in " \t":
            current_column += 1
        elif char == "\n":
            # unexpected empty line
            current_column = 0
        elif char == "\f":
            current_column = 0
        else:
            # indent is finished
            wait_for_nl = True
    return "".join(lines), current_line



# ==================================================
# File: /root/ecooptimizer/black/src/blib2to3/pgen2/pgen.py
# Line: 73

def make_label(self, c: PgenGrammar, label: str) -> int:
    # XXX Maybe this should be a method on a subclass of converter?
    ilabel = len(c.labels)
    if label[0].isalpha():
        # Either a symbol name or a named token
        if label in c.symbol2number:
            # A symbol name (a non-terminal)
            if label in c.symbol2label:
                return c.symbol2label[label]
            else:
                c.labels.append((c.symbol2number[label], None))
                c.symbol2label[label] = ilabel
                return ilabel
        else:
            # A named token (NAME, NUMBER, STRING)
            itoken = getattr(token, label, None)
            assert isinstance(itoken, int), label
            assert itoken in token.tok_name, label
            if itoken in c.tokens:
                return c.tokens[itoken]
            else:
                c.labels.append((itoken, None))
                c.tokens[itoken] = ilabel
                return ilabel
    else:
        # Either a keyword or an operator
        assert label[0] in ('"', "'"), label
        value = eval(label)
        if value[0].isalpha():
            if label[0] == '"':
                keywords = c.soft_keywords
            else:
                keywords = c.keywords

            # A keyword
            if value in keywords:
                return keywords[value]
            else:
                c.labels.append((token.NAME, value))
                keywords[value] = ilabel
                return ilabel
        else:
            # An operator (any non-numeric token)
            itoken = grammar.opmap[value]  # Fails if unknown token
            if itoken in c.tokens:
                return c.tokens[itoken]
            else:
                c.labels.append((itoken, None))
                c.tokens[itoken] = ilabel
                return ilabel


# ==================================================
# Line: 189

def make_dfa(self, start: "NFAState", finish: "NFAState") -> list["DFAState"]:
    # To turn an NFA into a DFA, we define the states of the DFA
    # to correspond to *sets* of states of the NFA.  Then do some
    # state reduction.  Let's represent sets as dicts with 1 for
    # values.
    assert isinstance(start, NFAState)
    assert isinstance(finish, NFAState)

    def closure(state: NFAState) -> dict[NFAState, int]:
        base: dict[NFAState, int] = {}
        addclosure(state, base)
        return base

    def addclosure(state: NFAState, base: dict[NFAState, int]) -> None:
        assert isinstance(state, NFAState)
        if state in base:
            return
        base[state] = 1
        for label, next in state.arcs:
            if label is None:
                addclosure(next, base)

    states = [DFAState(closure(start), finish)]
    for state in states:  # NB states grows while we're iterating
        arcs: dict[str, dict[NFAState, int]] = {}
        for nfastate in state.nfaset:
            for label, next in nfastate.arcs:
                if label is not None:
                    addclosure(next, arcs.setdefault(label, {}))
        for label, nfaset in sorted(arcs.items()):
            for st in states:
                if st.nfaset == nfaset:
                    break
            else:
                st = DFAState(nfaset, finish)
                states.append(st)
            state.addarc(st, label)
    return states  # List of DFAState instances; first one is start


# ==================================================
# Line: 228

def dump_nfa(self, name: str, start: "NFAState", finish: "NFAState") -> None:
    print("Dump of NFA for", name)
    todo = [start]
    for i, state in enumerate(todo):
        print("  State", i, state is finish and "(final)" or "")
        for label, next in state.arcs:
            if next in todo:
                j = todo.index(next)
            else:
                j = len(todo)
                todo.append(next)
            if label is None:
                print(f"    -> {j}")
            else:
                print(f"    {label} -> {j}")


# ==================================================
# Line: 244

def dump_dfa(self, name: str, dfa: Sequence["DFAState"]) -> None:
    print("Dump of DFA for", name)
    for i, state in enumerate(dfa):
        print("  State", i, state.isfinal and "(final)" or "")
        for label, next in sorted(state.arcs.items()):
            print(f"    {label} -> {dfa.index(next)}")


# ==================================================
# Line: 251

def simplify_dfa(self, dfa: list["DFAState"]) -> None:
    # This is not theoretically optimal, but works well enough.
    # Algorithm: repeatedly look for two states that have the same
    # set of arcs (same labels pointing to the same nodes) and
    # unify them, until things stop changing.

    # dfa is a list of DFAState instances
    changes = True
    while changes:
        changes = False
        for i, state_i in enumerate(dfa):
            for j in range(i + 1, len(dfa)):
                state_j = dfa[j]
                if state_i == state_j:
                    # print "  unify", i, j
                    del dfa[j]
                    for state in dfa:
                        state.unifystate(state_j, state_i)
                    changes = True
                    break


# ==================================================
