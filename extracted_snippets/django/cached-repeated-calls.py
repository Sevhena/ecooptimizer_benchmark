# cached-repeated-calls snippets for django

# File: /root/ecooptimizer/django/django/apps/config.py
# Line: 111

app_module = import_module(entry)

# ==================================================
# Line: 123

mod = import_module(mod_path)

# ==================================================
# Line: 178

mod = import_module(mod_path)

# ==================================================
# Line: 193

import_module(entry)

# ==================================================
# File: /root/ecooptimizer/django/django/middleware/cache.py
# Line: 165

response = self.cache.get(cache_key)

# ==================================================
# Line: 171

response = self.cache.get(cache_key)

# ==================================================
# File: /root/ecooptimizer/django/django/template/base.py
# Line: 388

content = token_string[2:-2].strip()

# ==================================================
# Line: 400

content = token_string[2:-2].strip()

# ==================================================
# Occurrences: Lines 1065-1068 (2 instances)

value = str(value)

# ==================================================
# Line: 1113

match = kwarg_re.match(bits[0])

# ==================================================
# Line: 1124

match = kwarg_re.match(bits[0])

# ==================================================
# File: /root/ecooptimizer/django/django/template/defaulttags.py
# Occurrences: Lines 280-285 (2 instances)

compare_to = nodelist_true_output = self.nodelist_true.render(context)

# ==================================================
# Occurrences: Lines 965-976 (6 instances)

condition = TemplateIfParser(parser, bits).parse()

# ==================================================
# Line: 982

token = parser.next_token()

# ==================================================
# Line: 1095

lib = find_library(parser, name)

# ==================================================
# Line: 1101

lib = find_library(parser, name)

# ==================================================
# Occurrences: Lines 1136-1144 (3 instances)

bits.pop()

# ==================================================
# Occurrences: Lines 1460-1462 (4 instances)

kwargs[name] = parser.compile_filter(value)

# ==================================================
# File: /root/ecooptimizer/django/django/template/smartif.py
# Occurrences: Lines 205-209 (2 instances)

self.current_token = self.next_token()

# ==================================================
# File: /root/ecooptimizer/django/django/template/defaultfilters.py
# Line: 165

_, digits, exponent = d.as_tuple()

# ==================================================
# Line: 195

tupl = d.as_tuple()

# ==================================================
# Occurrences: Lines 696-699 (5 instances)

item = next(item_iterator)

# ==================================================
# Occurrences: Lines 710-710 (3 instances)

item = next(item_iterator)

# ==================================================
# File: /root/ecooptimizer/django/django/test/html.py
# Line: 246

element = self.open_tags.pop()

# ==================================================
# Line: 252

element = self.open_tags.pop()

# ==================================================
# File: /root/ecooptimizer/django/django/test/utils.py
# Occurrences: Lines 801-804 (2 instances)

orig_stdout = getattr(sys, stream_name)

# ==================================================
# Occurrences: Lines 949-953 (2 instances)

start_time = time.perf_counter()

# ==================================================
# File: /root/ecooptimizer/django/django/test/testcases.py
# Occurrences: Lines 703-704 (2 instances)

if form_index is not None and form_index >= formset.total_form_count():

# ==================================================
# Line: 889

required = fieldclass(*field_args, **field_kwargs)

# ==================================================
# Line: 914

self.assertIsInstance(fieldclass(*field_args, **field_kwargs), fieldclass)

# ==================================================
# Occurrences: Lines 1473-1478 (3 instances)

start_count = len(connections[using].run_on_commit)

# ==================================================
# Occurrences: Lines 1497-1497 (2 instances)

if callback_count == len(connections[using].run_on_commit):

# ==================================================
# File: /root/ecooptimizer/django/django/utils/html.py
# Occurrences: Lines 352-354 (2 instances)

url = smart_urlquote(html.unescape(middle))

# ==================================================
# Occurrences: Lines 448-452 (4 instances)

rstripped = middle.rstrip(self.trailing_punctuation_chars)

# ==================================================
# Occurrences: Lines 461-462 (4 instances)

rstripped = middle.rstrip(self.trailing_punctuation_chars)

# ==================================================
# File: /root/ecooptimizer/django/django/utils/numberformat.py
# Occurrences: Lines 41-42 (2 instances)

if isinstance(number, float) and "e" in str(number).lower():

# ==================================================
# Line: 71

str_number = str(number)

# ==================================================
# Line: 93

active_interval = intervals.pop(0)

# ==================================================
# Line: 99

active_interval = intervals.pop(0) or active_interval

# ==================================================
# File: /root/ecooptimizer/django/django/utils/formats.py
# Occurrences: Lines 231-235 (2 instances)

format = sanitize_strftime_format(format)

# ==================================================
# File: /root/ecooptimizer/django/django/utils/decorators.py
# Occurrences: Lines 169-176 (9 instances)

result = _pre_process_request(request, *args, **kwargs)

# ==================================================
# Occurrences: Lines 185-192 (9 instances)

result = _pre_process_request(request, *args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/django/django/utils/regex_helper.py
# Line: 75

ch, escaped = next(pattern_iter)

# ==================================================
# Occurrences: Lines 105-112 (8 instances)

ch, escaped = next(pattern_iter)

# ==================================================
# Occurrences: Lines 120-120 (2 instances)

ch, escaped = next(pattern_iter)

# ==================================================
# Occurrences: Lines 133-133 (2 instances)

ch, escaped = next(pattern_iter)

# ==================================================
# Occurrences: Lines 146-149 (4 instances)

ch, escaped = next(pattern_iter)

# ==================================================
# Occurrences: Lines 185-185 (2 instances)

ch, escaped = next(pattern_iter)

# ==================================================
# Line: 249

ch2, escaped = next(input_iter)

# ==================================================
# Line: 260

ch, escaped = next(input_iter)

# ==================================================
# Line: 267

ch, escaped = next(input_iter)

# ==================================================
# File: /root/ecooptimizer/django/django/utils/functional.py
# Line: 110

return func(*self._args, **self._kw)

# ==================================================
# Occurrences: Lines 123-148 (6 instances)

other = other.__cast()

# ==================================================
# Line: 187

result = func(*self._args, **self._kw)

# ==================================================
# Occurrences: Lines 279-280 (2 instances)

return super().__getattribute__(name)

# ==================================================
# File: /root/ecooptimizer/django/django/utils/translation/__init__.py
# Line: 144

return self._translate(number_value).format(*args, **kwargs)

# ==================================================
# Line: 151

translated = self._translate(number_value)

# ==================================================
# File: /root/ecooptimizer/django/django/utils/translation/trans_real.py
# Occurrences: Lines 343-347 (2 instances)

lang = get_language()

# ==================================================
# File: /root/ecooptimizer/django/django/utils/translation/template.py
# Occurrences: Lines 183-183 (2 instances)

cmatches = constant_re.findall(t.contents)

# ==================================================
# Occurrences: Lines 196-198 (4 instances)

message_context = message_context.strip('"')

# ==================================================
# Occurrences: Lines 208-208 (2 instances)

for fmatch in constant_re.findall(t.contents):

# ==================================================
# Occurrences: Lines 215-217 (4 instances)

message_context = message_context.strip('"')

# ==================================================
# File: /root/ecooptimizer/django/django/utils/text.py
# Occurrences: Lines 387-393 (3 instances)

yield buf.read()

# ==================================================
# File: /root/ecooptimizer/django/django/templatetags/i18n.py
# Occurrences: Lines 413-413 (2 instances)

option = remaining.pop(0)

# ==================================================
# Occurrences: Lines 422-422 (2 instances)

value = remaining.pop(0)

# ==================================================
# Occurrences: Lines 436-436 (2 instances)

value = remaining.pop(0)

# ==================================================
# Occurrences: Lines 505-505 (2 instances)

option = remaining_bits.pop(0)

# ==================================================
# Occurrences: Lines 511-511 (2 instances)

value = token_kwargs(remaining_bits, parser, support_legacy=True)

# ==================================================
# Occurrences: Lines 517-517 (2 instances)

value = token_kwargs(remaining_bits, parser, support_legacy=True)

# ==================================================
# Occurrences: Lines 525-525 (2 instances)

value = remaining_bits.pop(0)

# ==================================================
# Occurrences: Lines 535-535 (2 instances)

value = remaining_bits.pop(0)

# ==================================================
# Line: 563

token = parser.next_token()

# ==================================================
# Line: 574

token = parser.next_token()

# ==================================================
# File: /root/ecooptimizer/django/django/http/response.py
# Occurrences: Lines 584-594 (4 instances)

initial_position = filelike.tell()

# ==================================================
# File: /root/ecooptimizer/django/django/http/multipartparser.py
# Occurrences: Lines 230-230 (2 instances)

raw_data = field_stream.read(size=read_size)

# ==================================================
# Occurrences: Lines 237-237 (2 instances)

data = field_stream.read(size=read_size)

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/postgresql/schema.py
# Line: 183

column = strip_quotes(new_field.column)

# ==================================================
# Occurrences: Lines 212-218 (3 instances)

"column": self.quote_name(strip_quotes(new_field.column)),

# ==================================================
# Occurrences: Lines 234-237 (2 instances)

fragment, _ = super()._alter_column_type_sql(
    model, old_field, new_field, new_type, old_collation, new_collation
)

# ==================================================
# Line: 259

return super()._alter_column_type_sql(
    model, old_field, new_field, new_type, old_collation, new_collation
)

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/postgresql/operations.py
# Occurrences: Lines 375-376 (2 instances)

if serialize.upper() in {"TEXT", "BINARY"}:

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/oracle/schema.py
# Line: 116

new_temp_field.null = new_field.get_internal_type() not in (

# ==================================================
# Line: 133

new_internal_type = new_field.get_internal_type()

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/oracle/base.py
# Line: 306

cursor = self.create_cursor()

# ==================================================
# Line: 328

cursor = self.create_cursor()

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/oracle/introspection.py
# Line: 337

constraint = self.identifier_converter(constraint)

# ==================================================
# Line: 371

constraint = self.identifier_converter(constraint)

# ==================================================
# Line: 404

constraint = self.identifier_converter(constraint)

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/utils.py
# Occurrences: Lines 132-136 (2 instances)

start = time.monotonic()

# ==================================================
# Occurrences: Lines 168-173 (2 instances)

start = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/schema.py
# Occurrences: Lines 470-475 (2 instances)

if field.get_internal_type() == "BinaryField":

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/creation.py
# Occurrences: Lines 357-371 (6 instances)

test_case_name, _, test_method_name = test_name.rpartition(".")

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/sqlite3/schema.py
# Occurrences: Lines 168-173 (4 instances)

"col": self.quote_name(old_field.column),

# ==================================================
# Line: 205

body_copy = copy.deepcopy(body)

# ==================================================
# Line: 220

meta = type("Meta", (), meta_contents)

# ==================================================
# Line: 226

body_copy = copy.deepcopy(body)

# ==================================================
# Line: 235

meta = type("Meta", (), meta_contents)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/sql/compiler.py
# Occurrences: Lines 371-371 (2 instances)

field = field.copy()

# ==================================================
# Occurrences: Lines 383-383 (2 instances)

field = field.copy()

# ==================================================
# Occurrences: Lines 389-389 (2 instances)

field = field.copy()

# ==================================================
# Occurrences: Lines 654-656 (2 instances)

part_sql = "({})".format(part_sql)

# ==================================================
# Occurrences: Lines 1474-1474 (2 instances)

col = _get_first_selected_col_from_model(klass_info)

# ==================================================
# Occurrences: Lines 1494-1494 (2 instances)

col = _get_first_selected_col_from_model(klass_info)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/sql/query.py
# Line: 468

aggregate_refs = aggregate.get_refs()

# ==================================================
# Line: 477

aggregate = aggregate.replace_expressions(replacements)

# ==================================================
# Line: 553

annotation_mask |= aggregate.get_refs()

# ==================================================
# Line: 580

outer_query.annotations[alias] = aggregate.replace_expressions(
    replacements
)

# ==================================================
# Line: 609

alias: aggregate.replace_expressions(replacements)

# ==================================================
# Line: 618

for expression in outer_query.annotation_select.values()

# ==================================================
# Line: 630

cols = outer_query.annotation_select.values()

# ==================================================
# Occurrences: Lines 818-818 (2 instances)

select_mask.setdefault(field, {})

# ==================================================
# Occurrences: Lines 829-829 (2 instances)

field_select_mask = select_mask.setdefault(field, {})

# ==================================================
# Line: 1165

joins_len = len(self.alias_map)

# ==================================================
# Line: 1171

if joins_len < len(self.alias_map):

# ==================================================
# Line: 1405

lookup_class = lhs.get_lookup(lookup_name)

# ==================================================
# Line: 1411

lookup_class = lhs.get_lookup(lookup_name)

# ==================================================
# Line: 2111

lookup_class = select_field.get_lookup("exact")

# ==================================================
# Line: 2118

lookup_class = select_field.get_lookup("exact")

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/constraints.py
# Line: 602

field_expression_map = instance._get_field_expression_map(
    meta=model._meta, exclude=exclude
)

# ==================================================
# Line: 625

for field, value in instance._get_field_expression_map(
    meta=model._meta, exclude=exclude
).items()

# ==================================================
# Line: 668

against = instance._get_field_expression_map(
    meta=model._meta, exclude=exclude
)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/base.py
# Occurrences: Lines 338-338 (2 instances)

new_field = copy.deepcopy(field)

# ==================================================
# Occurrences: Lines 368-368 (2 instances)

field = copy.deepcopy(field)

# ==================================================
# Occurrences: Lines 544-549 (6 instances)

val = kwargs.pop(field.attname)

# ==================================================
# Occurrences: Lines 555-557 (4 instances)

val = field.get_default()

# ==================================================
# Occurrences: Lines 1066-1069 (2 instances)

if not self._is_pk_set(meta):

# ==================================================
# Line: 1084

base_qs = cls._base_manager.using(using)

# ==================================================
# Line: 1111

cls._base_manager.using(using)

# ==================================================
# Line: 1608

errors = e.update_error_dict(errors)

# ==================================================
# Line: 1615

errors = e.update_error_dict(errors)

# ==================================================
# Line: 1625

errors = e.update_error_dict(errors)

# ==================================================
# Line: 1635

errors = e.update_error_dict(errors)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/deletion.py
# Line: 100

self.data = defaultdict(set)

# ==================================================
# Line: 114

self.dependencies = defaultdict(set)  # {model: {models}}

# ==================================================
# Occurrences: Lines 307-308 (2 instances)

model_fast_deletes = defaultdict(list)

# ==================================================
# Line: 380

restricted_objects = defaultdict(list)

# ==================================================
# Line: 448

count = sql.DeleteQuery(model).delete_batch(

# ==================================================
# Line: 499

query = sql.DeleteQuery(model)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/query.py
# Line: 423

qs = self._chain()

# ==================================================
# Line: 435

qs = self._chain()

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/expressions.py
# Occurrences: Lines 817-819 (2 instances)

sql, params = compiler.compile(side)

# ==================================================
# Line: 1721

default_sql, default_params = compiler.compile(default)

# ==================================================
# Line: 1730

return compiler.compile(default)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/related.py
# Line: 1559

seen_self = sum(
    from_model == getattr(field.remote_field, "model", None)
    for field in self.remote_field.through._meta.fields
)

# ==================================================
# Line: 1584

seen_from = sum(
    from_model == getattr(field.remote_field, "model", None)
    for field in self.remote_field.through._meta.fields
)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/tuple_lookups.py
# Occurrences: Lines 182-188 (4 instances)

lookup = next(lookups)

# ==================================================
# Occurrences: Lines 210-216 (4 instances)

lookup = next(lookups)

# ==================================================
# Occurrences: Lines 238-244 (4 instances)

lookup = next(lookups)

# ==================================================
# Occurrences: Lines 266-272 (4 instances)

lookup = next(lookups)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/related_descriptors.py
# Line: 676

if getattr(self.instance, field.attname) is None:

# ==================================================
# Line: 696

val = getattr(self.instance, field.attname)

# ==================================================
# Occurrences: Lines 711-716 (4 instances)

getattr(self.instance, target_field.attname)

# ==================================================
# Line: 744

queryset = super().get_queryset()

# ==================================================
# Line: 753

queryset = querysets[0] if querysets else super().get_queryset()

# ==================================================
# Line: 774

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Line: 819

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Line: 832

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Line: 845

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Line: 903

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Line: 923

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Occurrences: Lines 1015-1025 (12 instances)

self.query_field_name = rel.field.related_query_name()

# ==================================================
# Line: 1031

self.source_field = self.through._meta.get_field(self.source_field_name)

# ==================================================
# Line: 1113

queryset = super().get_queryset()

# ==================================================
# Line: 1122

queryset = querysets[0] if querysets else super().get_queryset()

# ==================================================
# Line: 1136

fk = self.through._meta.get_field(self.source_field_name)

# ==================================================
# Line: 1207

db = router.db_for_write(self.through, instance=self.instance)

# ==================================================
# Line: 1246

db = router.db_for_write(self.through, instance=self.instance)

# ==================================================
# Line: 1258

filters = self._build_remove_filters(super().get_queryset().using(db))

# ==================================================
# Line: 1283

db = router.db_for_write(self.through, instance=self.instance)

# ==================================================
# Line: 1320

db = router.db_for_write(self.instance.__class__, instance=self.instance)

# ==================================================
# Line: 1335

db = router.db_for_write(self.instance.__class__, instance=self.instance)

# ==================================================
# Line: 1355

db = router.db_for_write(self.instance.__class__, instance=self.instance)

# ==================================================
# Line: 1470

db = router.db_for_write(self.through, instance=self.instance)

# ==================================================
# Line: 1546

db = router.db_for_write(self.through, instance=self.instance)

# ==================================================
# Line: 1558

target_model_qs = super().get_queryset()

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/functions/datetime.py
# Line: 68

sql, params = connection.ops.time_extract_sql(
    self.lookup_name, sql, tuple(params)
)

# ==================================================
# Line: 76

sql, params = connection.ops.time_extract_sql(
    self.lookup_name, sql, tuple(params)
)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/functions/comparison.py
# Line: 25

sql, params = super().as_sql(
    compiler, connection, template=template, **extra_context
)

# ==================================================
# Line: 33

return super().as_sql(
    compiler, connection, template=template, **extra_context
)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/options.py
# Occurrences: Lines 205-208 (4 instances)

self.original_attrs[attr_name] = getattr(self, attr_name)

# ==================================================
# Line: 220

self.verbose_name_plural = format_lazy("{}s", self.verbose_name)

# ==================================================
# Line: 231

self.verbose_name_plural = format_lazy("{}s", self.verbose_name)

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/questioner.py
# Occurrences: Lines 101-106 (2 instances)

result = input()

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/executor.py
# Line: 122

state = self._create_project_state(with_applied_migrations=True)

# ==================================================
# Line: 134

state = self._create_project_state(with_applied_migrations=True)

# ==================================================
# Occurrences: Lines 364-364 (2 instances)

model = global_apps.get_model(model._meta.swapped)

# ==================================================
# Occurrences: Lines 378-378 (2 instances)

model = global_apps.get_model(model._meta.swapped)

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/writer.py
# Occurrences: Lines 35-36 (3 instances)

args = arg_string.splitlines()

# ==================================================
# Occurrences: Lines 52-53 (3 instances)

args = arg_string.splitlines()

# ==================================================
# Occurrences: Lines 64-65 (3 instances)

args = arg_string.splitlines()

# ==================================================
# Line: 94

i = len(args)

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/autodetector.py
# Line: 307

num_ops = sum(len(x) for x in self.generated_operations.values())

# ==================================================
# Line: 404

new_num_ops = sum(len(x) for x in self.generated_operations.values())

# ==================================================
# Occurrences: Lines 935-935 (2 instances)

for name in sorted(related_fields):

# ==================================================
# Occurrences: Lines 972-972 (2 instances)

for name in sorted(related_fields):

# ==================================================
# Occurrences: Lines 1344-1344 (2 instances)

new_index_dec = new_index.deconstruct()

# ==================================================
# Occurrences: Lines 1376-1376 (2 instances)

_, args, kwargs = new_index.deconstruct()

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/migration.py
# Occurrences: Lines 115-115 (2 instances)

collected_sql_before = len(schema_editor.collected_sql)

# ==================================================
# Occurrences: Lines 135-135 (2 instances)

if collect_sql and collected_sql_before == len(schema_editor.collected_sql):

# ==================================================
# Occurrences: Lines 164-165 (4 instances)

new_state = new_state.clone()

# ==================================================
# Occurrences: Lines 180-180 (2 instances)

collected_sql_before = len(schema_editor.collected_sql)

# ==================================================
# Occurrences: Lines 196-196 (2 instances)

if collect_sql and collected_sql_before == len(schema_editor.collected_sql):

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/serializer.py
# Line: 102

arg_string, arg_imports = serializer_factory(arg).serialize()

# ==================================================
# Line: 108

arg_string, arg_imports = serializer_factory(arg).serialize()

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/state.py
# Occurrences: Lines 159-163 (4 instances)

changed_field = field.clone()

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/recorder.py
# Occurrences: Lines 33-34 (2 instances)

app = models.CharField(max_length=255)

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/operations/models.py
# Line: 248

options = self.options.copy()

# ==================================================
# Line: 265

order_with_respect_to = options.get("order_with_respect_to")

# ==================================================
# Line: 280

options = self.options.copy()

# ==================================================
# Line: 291

order_with_respect_to = options.get("order_with_respect_to")

# ==================================================
# Occurrences: Lines 452-453 (4 instances)

model = to_state.apps.get_model(*related_key)

# ==================================================
# File: /root/ecooptimizer/django/django/forms/models.py
# Line: 868

form._errors[NON_FIELD_ERRORS] = self.error_class(
    [self.get_form_error()],
    renderer=self.renderer,
)

# ==================================================
# Line: 904

form._errors[NON_FIELD_ERRORS] = self.error_class(
    [self.get_form_error()],
    renderer=self.renderer,
)

# ==================================================
# File: /root/ecooptimizer/django/django/forms/fields.py
# Occurrences: Lines 806-807 (2 instances)

url_fields = split_url(urlunsplit(url_fields))

# ==================================================
# Occurrences: Lines 1218-1218 (2 instances)

f = os.path.join(root, f)

# ==================================================
# Occurrences: Lines 1225-1225 (2 instances)

f = os.path.join(root, f)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/filters.py
# Occurrences: Lines 483-486 (2 instances)

next_month = today.replace(year=today.year + 1, month=1, day=1)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/utils.py
# Occurrences: Lines 298-301 (2 instances)

value = attr(obj)

# ==================================================
# Occurrences: Lines 408-410 (2 instances)

label = pretty_name(name)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/helpers.py
# Occurrences: Lines 394-399 (2 instances)

or label_for_field(
    field_name,
    self.opts.model,
    self.opts,
    form=empty_form,
),

# ==================================================
# Occurrences: Lines 409-411 (2 instances)

label = label_for_field(
    field_name, self.opts.model, self.opts, form=empty_form
)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/sites.py
# Line: 421

index_path = reverse("admin:index", current_app=self.name)

# ==================================================
# Line: 441

context[REDIRECT_FIELD_NAME] = reverse("admin:index", current_app=self.name)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/views/main.py
# Occurrences: Lines 185-185 (2 instances)

lookup_params_count = len(lookup_params)

# ==================================================
# Occurrences: Lines 214-214 (2 instances)

if lookup_params_count > len(lookup_params):

# ==================================================
# Occurrences: Lines 221-221 (2 instances)

if lookup_params_count > len(lookup_params):

# ==================================================
# Occurrences: Lines 445-445 (2 instances)

field = self.lookup_opts.get_field(field_name)

# ==================================================
# Occurrences: Lines 470-470 (2 instances)

self.lookup_opts.get_field(field_name) for field_name in field_names

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/options.py
# Line: 1386

obj_repr = str(obj)

# ==================================================
# Line: 1404

"obj": str(obj),

# ==================================================
# Line: 1427

msg = _("The {name} “{obj}” was added successfully.")

# ==================================================
# Line: 1465

_("The {name} “{obj}” was added successfully."), **msg_dict

# ==================================================
# Line: 1521

redirect_url = add_preserved_filters(
    {
        "preserved_filters": preserved_filters,
        "preserved_qsl": preserved_qsl,
        "opts": opts,
    },
    redirect_url,
)

# ==================================================
# Line: 1544

redirect_url = add_preserved_filters(
    {
        "preserved_filters": preserved_filters,
        "preserved_qsl": preserved_qsl,
        "opts": opts,
    },
    redirect_url,
)

# ==================================================
# Line: 1837

request, obj, change=not add, fields=flatten_fieldsets(fieldsets)

# ==================================================
# Line: 1879

readonly_fields = flatten_fieldsets(fieldsets)

# ==================================================
# Line: 2015

response = self.response_action(
    request, queryset=cl.get_queryset(request)
)

# ==================================================
# Line: 2039

response = self.response_action(
    request, queryset=cl.get_queryset(request)
)

# ==================================================
# Line: 2062

FormSet = self.get_changelist_formset(request)

# ==================================================
# Line: 2097

FormSet = self.get_changelist_formset(request)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/staticfiles/storage.py
# Occurrences: Lines 361-361 (2 instances)

hashed_file_exists = self.exists(hashed_name)

# ==================================================
# Occurrences: Lines 387-394 (8 instances)

self._save(hashed_name, content_file)

# ==================================================
# Occurrences: Lines 406-406 (2 instances)

hashed_name = self.clean_name(saved_name)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/management/commands/createsuperuser.py
# Line: 113

error_msg = self._validate_username(
    username, verbose_field_name, database
)

# ==================================================
# Line: 132

error_msg = self._validate_username(
    username, verbose_field_name, database
)

# ==================================================
# Line: 147

field = self.UserModel._meta.get_field(field_name)

# ==================================================
# Line: 214

error_msg = self._validate_username(
    username, verbose_field_name, database
)

# ==================================================
# Line: 224

field = self.UserModel._meta.get_field(field_name)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/contenttypes/views.py
# Occurrences: Lines 58-58 (2 instances)

site_qs = getattr(obj, field.name).all()

# ==================================================
# Occurrences: Lines 75-75 (2 instances)

site = getattr(obj, field.name)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/contenttypes/fields.py
# Line: 616

return queryset.using(db).filter(**self.core_filters)

# ==================================================
# Line: 628

queryset = super().get_queryset()

# ==================================================
# Line: 637

queryset = querysets[0] if querysets else super().get_queryset()

# ==================================================
# Line: 672

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Occurrences: Lines 737-738 (2 instances)

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Line: 755

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Line: 783

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Line: 796

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# Line: 809

db = router.db_for_write(self.model, instance=self.instance)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/geos/polygon.py
# Line: 33

n_holes = len(init_holes)

# ==================================================
# Line: 43

n_holes = len(init_holes)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/geos/linestring.py
# Occurrences: Lines 76-78 (4 instances)

ndim = len(coord)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/geos/factory.py
# Occurrences: Lines 12-14 (2 instances)

buf = file_h.read()

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/geos/prototypes/io.py
# Occurrences: Lines 228-229 (2 instances)

if bool(flag) != self._trim:

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/utils/ogrinspect.py
# Occurrences: Lines 179-181 (2 instances)

if field_name.lower() in null_fields:

# ==================================================
# Occurrences: Lines 201-201 (2 instances)

mfield = field_name.lower()

# ==================================================
# Occurrences: Lines 212-212 (2 instances)

if field_name.lower() in decimal_fields:

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/utils/layermapping.py
# Occurrences: Lines 658-660 (6 instances)

m = self.model(**kwargs)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/models/lookups.py
# Occurrences: Lines 63-66 (2 instances)

return super().process_rhs(compiler, connection)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/gdal/srs.py
# Line: 67

self.ptr = capi.new_srs(c_char_p(b""))

# ==================================================
# Line: 94

buf = c_char_p(b"")

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/flatpages/views.py
# Occurrences: Lines 37-41 (2 instances)

f = get_object_or_404(FlatPage, url=url, sites=site_id)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/flatpages/templatetags/flatpages.py
# Occurrences: Lines 38-40 (2 instances)

flatpages = flatpages.filter(registration_required=False)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admindocs/utils.py
# Line: 49

body = "\n\n".join(parts[1:])

# ==================================================
# Line: 55

body = "\n\n".join(parts[1:])

# ==================================================
# File: /root/ecooptimizer/django/django/dispatch/dispatcher.py
# Line: 202

response = receiver(signal=self, sender=sender, **named)

# ==================================================
# Line: 209

receiver(signal=self, sender=sender, **named)

# ==================================================
# Line: 319

response = receiver(signal=self, sender=sender, **named)

# ==================================================
# Line: 329

response = await receiver(signal=self, sender=sender, **named)

# ==================================================
# File: /root/ecooptimizer/django/django/core/files/base.py
# Occurrences: Lines 41-43 (2 instances)

pos = self.file.tell()

# ==================================================
# File: /root/ecooptimizer/django/django/core/files/storage/filesystem.py
# Line: 69

full_path = self.path(name)

# ==================================================
# Line: 135

full_path = self.path(name)

# ==================================================
# File: /root/ecooptimizer/django/django/core/files/storage/base.py
# Occurrences: Lines 95-97 (2 instances)

name = os.path.join(
    dir_name, self.get_alternative_name(file_root, file_ext)
)

# ==================================================
# Occurrences: Lines 112-114 (2 instances)

name = os.path.join(
    dir_name, self.get_alternative_name(file_root, file_ext)
)

# ==================================================
# File: /root/ecooptimizer/django/django/core/cache/backends/db.py
# Line: 122

num = cursor.fetchone()[0]

# ==================================================
# Line: 153

result = cursor.fetchone()

# ==================================================
# File: /root/ecooptimizer/django/django/core/serializers/xml_serializer.py
# Line: 151

attr = getattr(obj, field.name)

# ==================================================
# Line: 163

query_set = getattr(obj, field.name).select_related(None).only("pk")

# ==================================================
# Occurrences: Lines 324-333 (4 instances)

field_value = getInnerText(node).strip()

# ==================================================
# Line: 355

obj_pk = model._meta.pk.to_python(n.getAttribute("pk"))

# ==================================================
# Line: 361

return model._meta.pk.to_python(n.getAttribute("pk"))

# ==================================================
# File: /root/ecooptimizer/django/django/core/serializers/json.py
# Line: 93

r = o.isoformat()

# ==================================================
# Occurrences: Lines 100-104 (2 instances)

return o.isoformat()

# ==================================================
# File: /root/ecooptimizer/django/django/core/serializers/python.py
# Line: 77

attr = getattr(obj, field.name)

# ==================================================
# Line: 89

query_set = getattr(obj, field.name).select_related(None).only("pk")

# ==================================================
# File: /root/ecooptimizer/django/django/core/handlers/exception.py
# Line: 42

response = await get_response(request)

# ==================================================
# Line: 55

response = get_response(request)

# ==================================================
# Line: 85

response = get_exception_response(
    request, get_resolver(get_urlconf()), 400, exc
)

# ==================================================
# Occurrences: Lines 98-104 (2 instances)

response = debug.technical_500_response(
    request, *sys.exc_info(), status_code=400
)

# ==================================================
# Occurrences: Lines 120-126 (2 instances)

response = debug.technical_500_response(
    request, *sys.exc_info(), status_code=400
)

# ==================================================
# File: /root/ecooptimizer/django/django/core/handlers/base.py
# Line: 199

response = self.process_exception_by_middleware(e, request)

# ==================================================
# Line: 222

response = self.process_exception_by_middleware(e, request)

# ==================================================
# File: /root/ecooptimizer/django/django/core/checks/model_checks.py
# Occurrences: Lines 13-15 (3 instances)

db_table_models = defaultdict(list)

# ==================================================
# Line: 71

", ".join(sorted(model_labels)),

# ==================================================
# Line: 85

", ".join(sorted(model_labels)),

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/showmigrations.py
# Occurrences: Lines 145-147 (2 instances)

targets = [key for key in graph.leaf_nodes() if key[0] in app_names]

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/makemessages.py
# Line: 706

_, errors, status = popen_wrapper(args)

# ==================================================
# Line: 729

msgs, errors, status = popen_wrapper(args)

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/squashmigrations.py
# Occurrences: Lines 196-199 (2 instances)

new_migration = subclass(name, app_label)

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/migrate.py
# Occurrences: Lines 183-186 (2 instances)

key for key in executor.loader.graph.leaf_nodes() if key[0] == app_label

# ==================================================
# Occurrences: Lines 394-399 (2 instances)

self.start = time.monotonic()

# ==================================================
# Occurrences: Lines 407-412 (2 instances)

self.start = time.monotonic()

# ==================================================
# Occurrences: Lines 420-425 (2 instances)

self.start = time.monotonic()

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/optimizemigration.py
# Line: 83

migration_file_string = writer.as_string()

# ==================================================
# Line: 105

migration_file_string = writer.as_string()

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/dumpdata.py
# Occurrences: Lines 140-140 (2 instances)

app_config = apps.get_app_config(app_label)

# ==================================================
# Occurrences: Lines 167-167 (2 instances)

app_config = apps.get_app_config(app_label)

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/inspectdb.py
# Line: 272

new_name = col_name.lower()

# ==================================================
# Line: 289

if col_name.lower().find(LOOKUP_SEP) >= 0:

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/makemigrations.py
# Occurrences: Lines 349-349 (3 instances)

migration_string = self.get_relative_path(writer.path)

# ==================================================
# Occurrences: Lines 365-365 (3 instances)

migration_string = writer.as_string()

# ==================================================
# Occurrences: Lines 373-373 (3 instances)

migration_path = self.get_relative_path(writer.path)

# ==================================================
# Occurrences: Lines 394-394 (3 instances)

self.log(writer.as_string())

# ==================================================
# File: /root/ecooptimizer/django/django/core/validators.py
# Line: 545

digits = len(digit_tuple)

# ==================================================
# Occurrences: Lines 556-560 (5 instances)

if abs(exponent) > len(digit_tuple):

# ==================================================
# File: /root/ecooptimizer/django/django/views/decorators/vary.py
# Occurrences: Lines 24-24 (2 instances)

response = await func(request, *args, **kwargs)

# ==================================================
# Occurrences: Lines 31-31 (2 instances)

response = func(request, *args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/django/django/views/decorators/cache.py
# Occurrences: Lines 46-46 (2 instances)

response = await viewfunc(request, *args, **kw)

# ==================================================
# Occurrences: Lines 54-54 (2 instances)

response = viewfunc(request, *args, **kw)

# ==================================================
# Line: 72

response = await view_func(request, *args, **kwargs)

# ==================================================
# Line: 80

response = view_func(request, *args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/django/django/views/decorators/http.py
# Occurrences: Lines 138-142 (4 instances)

response, res_etag, res_last_modified = _pre_process_request(
    request, *args, **kwargs
)

# ==================================================
# Occurrences: Lines 150-154 (4 instances)

response, res_etag, res_last_modified = _pre_process_request(
    request, *args, **kwargs
)

# ==================================================
# File: /root/ecooptimizer/django/django/views/decorators/clickjacking.py
# Line: 20

response = await view_func(*args, **kwargs)

# ==================================================
# Line: 28

response = view_func(*args, **kwargs)

# ==================================================
# Line: 50

response = await view_func(*args, **kwargs)

# ==================================================
# Line: 58

response = view_func(*args, **kwargs)

# ==================================================
# Line: 79

response = await view_func(*args, **kwargs)

# ==================================================
# Line: 86

response = view_func(*args, **kwargs)

# ==================================================
# File: /root/ecooptimizer/django/django/views/debug.py
# Line: 288

value = self.cleanse_special_types(request, value)

# ==================================================
# Line: 294

cleansed[name] = self.cleanse_special_types(request, value)

# ==================================================
# Occurrences: Lines 521-526 (2 instances)

exc_value = exceptions.pop()

# ==================================================
# File: /root/ecooptimizer/django/django/views/generic/dates.py
# Line: 771

if allow_future or result <= timezone_today():

# ==================================================
# Line: 796

now = timezone_today()

# ==================================================
