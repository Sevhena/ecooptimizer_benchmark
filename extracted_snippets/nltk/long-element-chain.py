# long-element-chain snippets for nltk

# File: /root/ecooptimizer/nltk/nltk/sem/relextract.py
# Line: 178

reldict["lcon"] = _join(pairs[0][0][-window:])

# ==================================================
# Line: 187

reldict["rcon"] = _join(pairs[2][0][:window])

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm_model.py
# Line: 223

self.translation_table[t][s] * self.alignment_table[i][j][l][m]

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm3.py
# Line: 210

self.distortion_table[j][i][l][m] = initial_prob

# ==================================================
# Occurrences: Lines 272-275 (3 instances)

counts.distortion[j][i][l][m]

# ==================================================
# Line: 320

self.translation_table[t][s] * self.distortion_table[j][i][l][m]

# ==================================================
# Occurrences: Lines 345-346 (2 instances)

self.distortion[j][i][l][m] += count

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm2.py
# Line: 158

self.alignment_table[i][j][l][m] = initial_prob

# ==================================================
# Occurrences: Lines 193-196 (3 instances)

counts.alignment[i][j][l][m]

# ==================================================
# Line: 230

return self.translation_table[t][s] * self.alignment_table[i][j][l][m]

# ==================================================
# Line: 248

* self.alignment_table[i][j][l][m]

# ==================================================
# Line: 280

* self.alignment_table[0][j + 1][l][m]

# ==================================================
# Line: 287

* self.alignment_table[i + 1][j + 1][l][m]

# ==================================================
# Occurrences: Lines 318-319 (2 instances)

self.alignment[i][j][l][m] += count

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm5.py
# Line: 507

value *= self.head_vacancy_table[dv][max_v][trg_class]

# ==================================================
# Line: 521

value *= self.non_head_vacancy_table[dv][max_v][trg_class]

# ==================================================
# Occurrences: Lines 560-563 (2 instances)

counts.head_vacancy[dv][max_v][t_cls]

# ==================================================
# Occurrences: Lines 570-573 (2 instances)

counts.non_head_vacancy[dv][max_v][t_cls]

# ==================================================
# Line: 616

self.head_vacancy[dv][max_v][trg_class] += count

# ==================================================
# Line: 629

self.non_head_vacancy[dv][max_v][trg_class] += count

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/translate/ibm4.py
# Occurrences: Lines 343-346 (2 instances)

counts.head_distortion[dj][s_cls][t_cls]

# ==================================================
# Line: 419

return ibm_model.head_distortion_table[dj][src_class][trg_class]

# ==================================================
# Line: 482

self.head_distortion[dj][src_class][trg_class] += count

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/nonprojectivedependencyparser.py
# Line: 700

graph.nodes[head_index + 1]["deps"][rel].append(address)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/recursivedescent.py
# Line: 535

return self._history[-1][0][0]

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/parse/dependencygraph.py
# Line: 115

self.nodes[head_address]["deps"][relation].append(mod_address)

# ==================================================
# Occurrences: Lines 369-372 (3 instances)

self.nodes[head]["deps"][rel].append(index)

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/lm/counter.py
# Line: 129

self[ngram_order][context][word] += 1

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tree/tree.py
# Line: 693

tree = stack[0][1][0]

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/brill_trainer.py
# Line: 352

correct_tag = train_sents[sentnum][wordnum][1]

# ==================================================
# Line: 386

correct_tag = train_sents[sentnum][wordnum][1]

# ==================================================
# Line: 495

text = test_sents[sentnum][wordnum][0]

# ==================================================
# Line: 529

correct_tag = train_sents[sentnum][wordnum][1]

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/tag/mapping.py
# Line: 76

_MAPPINGS[fileid]["universal"][fine] = coarse

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/lin.py
# Line: 59

self._thesaurus[fileid][key][ngram.strip('"')] = float(

# ==================================================
# Line: 85

self._thesaurus[fileid][ngram1][ngram2]

# ==================================================
# Line: 94

self._thesaurus[fid][ngram1][ngram2]

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/bcp47.py
# Line: 122

dic["deprecated"][typ][tag] = subfields

# ==================================================
# Line: 156

valstr = self.val2str(self.db[label][subtag]["Description"])

# ==================================================
# Occurrences: Lines 165-171 (3 instances)

if "Preferred-Value" in self.db["deprecated"][label][subtag]:

# ==================================================
# Occurrences: Lines 203-209 (4 instances)

val = f"{self.db[label][tag]['Description']}"

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/panlex_lite.py
# Occurrences: Lines 102-104 (2 instances)

mn_info[mn]["ex"][uid] = []

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/corpus/reader/wordnet.py
# Line: 463

return corpus._lang_data[lang][i][of]

# ==================================================
# Line: 493

return reader._lang_data[lang][0][i]

# ==================================================
# Line: 1514

offset = self._lemma_pos_offset_map[lemma][pos][synset_index]

# ==================================================
# Line: 1783

for l in self._lang_data[lang][1][lemma]:

# ==================================================
# Line: 1836

lemma.extend(self._lang_data[lang][0][i])

# ==================================================
# Occurrences: Lines 2228-2234 (2 instances)

lang_offsets = self._lang_data[lang][1][val.lower()]

# ==================================================
# File: /root/ecooptimizer/nltk/nltk/twitter/twitterclient.py
# Line: 234

self.handler.max_id = results["statuses"][count - 1]["id"] - 1

# ==================================================
# Line: 274

self.handler.max_id = results["statuses"][count - 1]["id"] - 1

# ==================================================
