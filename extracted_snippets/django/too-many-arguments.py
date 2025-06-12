# too-many-arguments snippets for django

# File: /root/ecooptimizer/django/django/template/engine.py
# Line: 20

def __init__(
    self,
    dirs=None,
    app_dirs=False,
    context_processors=None,
    debug=False,
    loaders=None,
    string_if_invalid="",
    file_charset="utf-8",
    libraries=None,
    builtins=None,
    autoescape=True,

# ==================================================
# File: /root/ecooptimizer/django/django/template/response.py
# Line: 13

def __init__(
    self,
    template,
    context=None,
    content_type=None,
    status=None,
    charset=None,
    using=None,
    headers=None,

# ==================================================
# Line: 150

def __init__(
    self,
    request,
    template,
    context=None,
    content_type=None,
    status=None,
    charset=None,
    using=None,
    headers=None,

# ==================================================
# File: /root/ecooptimizer/django/django/template/library.py
# Line: 384

def parse_bits(
    parser,
    bits,
    params,
    varargs,
    varkw,
    defaults,
    kwonly,
    kwonly_defaults,
    takes_context,
    name,

# ==================================================
# File: /root/ecooptimizer/django/django/template/context.py
# Line: 228

def __init__(
    self,
    request,
    dict_=None,
    processors=None,
    use_l10n=None,
    use_tz=None,
    autoescape=True,

# ==================================================
# File: /root/ecooptimizer/django/django/test/client.py
# Line: 484

def post(
    self,
    path,
    data=None,
    content_type=MULTIPART_CONTENT,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 538

def options(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 561

def put(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 585

def patch(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 609

def delete(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 633

def generic(
    self,
    method,
    path,
    data="",
    content_type="application/octet-stream",
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 733

def generic(
    self,
    method,
    path,
    data="",
    content_type="application/octet-stream",
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1110

def get(
    self,
    path,
    data=None,
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1138

def post(
    self,
    path,
    data=None,
    content_type=MULTIPART_CONTENT,
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1173

def head(
    self,
    path,
    data=None,
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1201

def options(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1236

def put(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1271

def patch(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1306

def delete(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1341

def trace(
    self,
    path,
    data="",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1467

async def get(
    self,
    path,
    data=None,
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1495

async def post(
    self,
    path,
    data=None,
    content_type=MULTIPART_CONTENT,
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1530

async def head(
    self,
    path,
    data=None,
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1558

async def options(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1593

async def put(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1628

async def patch(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1663

async def delete(
    self,
    path,
    data="",
    content_type="application/octet-stream",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# Line: 1698

async def trace(
    self,
    path,
    data="",
    follow=False,
    secure=False,
    *,
    headers=None,
    query_params=None,
    **extra,

# ==================================================
# File: /root/ecooptimizer/django/django/test/utils.py
# Line: 173

def setup_databases(
    verbosity,
    interactive,
    *,
    time_keeper=None,
    keepdb=False,
    debug_sql=False,
    parallel=0,
    aliases=None,
    serialized_aliases=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/django/django/test/runner.py
# Line: 410

def _init_worker(
    counter,
    initial_settings=None,
    serialized_contents=None,
    process_setup=None,
    process_setup_args=None,
    debug_mode=None,
    used_aliases=None,

# ==================================================
# Line: 668

def __init__(
    self,
    pattern=None,
    top_level=None,
    verbosity=1,
    interactive=True,
    failfast=False,
    keepdb=False,
    reverse=False,
    debug_mode=False,
    debug_sql=False,
    parallel=0,
    tags=None,
    exclude_tags=None,
    test_name_patterns=None,
    pdb=False,
    buffer=False,
    enable_faulthandler=True,
    timing=False,
    shuffle=False,
    logger=None,
    durations=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/django/django/test/testcases.py
# Line: 396

def assertRedirects(
    self,
    response,
    expected_url,
    status_code=302,
    target_status_code=200,
    msg_prefix="",
    fetch_redirect_response=True,

# ==================================================
# Line: 580

def assertContains(
    self, response, text, count=None, status_code=200, msg_prefix="", html=False

# ==================================================
# Line: 863

def assertFieldOutput(
    self,
    fieldclass,
    valid,
    invalid,
    field_args=None,
    field_kwargs=None,
    empty_value="",

# ==================================================
# File: /root/ecooptimizer/django/django/utils/feedgenerator.py
# Line: 111

def __init__(
    self,
    title,
    link,
    description,
    language=None,
    author_email=None,
    author_name=None,
    author_link=None,
    subtitle=None,
    categories=None,
    feed_url=None,
    feed_copyright=None,
    feed_guid=None,
    ttl=None,
    stylesheets=None,
    **kwargs,

# ==================================================
# Line: 163

def add_item(
    self,
    title,
    link,
    description,
    author_email=None,
    author_name=None,
    author_link=None,
    pubdate=None,
    comments=None,
    unique_id=None,
    unique_id_is_permalink=None,
    categories=(),
    item_copyright=None,
    ttl=None,
    updateddate=None,
    enclosures=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/django/django/utils/numberformat.py
# Line: 7

def format(
    number,
    decimal_sep,
    decimal_pos=None,
    grouping=0,
    thousand_sep="",
    force_grouping=False,
    use_l10n=None,

# ==================================================
# File: /root/ecooptimizer/django/django/templatetags/i18n.py
# Line: 105

def __init__(
    self,
    extra_context,
    singular,
    plural=None,
    countervar=None,
    counter=None,
    message_context=None,
    trimmed=False,
    asvar=None,
    tag_name="blocktranslate",

# ==================================================
# File: /root/ecooptimizer/django/django/http/response.py
# Line: 214

def set_cookie(
    self,
    key,
    value="",
    max_age=None,
    expires=None,
    path="/",
    domain=None,
    secure=False,
    httponly=False,
    samesite=None,

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/postgresql/schema.py
# Line: 152

def _alter_column_type_sql(
    self, model, old_field, new_field, new_type, old_collation, new_collation

# ==================================================
# Line: 263

def _alter_field(
    self,
    model,
    old_field,
    new_field,
    old_type,
    new_type,
    old_db_params,
    new_db_params,
    strict=False,

# ==================================================
# Line: 332

def _create_index_sql(
    self,
    model,
    *,
    fields=None,
    name=None,
    suffix="",
    using="",
    db_tablespace=None,
    col_suffixes=(),
    sql=None,
    opclasses=(),
    condition=None,
    concurrently=False,
    include=None,
    expressions=None,

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/oracle/schema.py
# Line: 169

def _alter_column_type_sql(
    self, model, old_field, new_field, new_type, old_collation, new_collation

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/ddl_references.py
# Line: 151

def __init__(
    self,
    from_table,
    from_columns,
    to_table,
    to_columns,
    suffix_template,
    create_fk_name,

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/mysql/schema.py
# Line: 223

def _alter_column_type_sql(
    self, model, old_field, new_field, new_type, old_collation, new_collation

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/schema.py
# Line: 310

def _iter_column_sql(
    self, column_db_type, params, model, field, field_db_params, include_default

# ==================================================
# Line: 934

def _alter_field(
    self,
    model,
    old_field,
    new_field,
    old_type,
    new_type,
    old_db_params,
    new_db_params,
    strict=False,

# ==================================================
# Line: 1397

def _alter_column_type_sql(
    self, model, old_field, new_field, new_type, old_collation, new_collation

# ==================================================
# Line: 1546

def _create_index_sql(
    self,
    model,
    *,
    fields=None,
    name=None,
    suffix="",
    using="",
    db_tablespace=None,
    col_suffixes=(),
    sql=None,
    opclasses=(),
    condition=None,
    include=None,
    expressions=None,

# ==================================================
# Line: 1791

def _unique_sql(
    self,
    model,
    fields,
    name,
    condition=None,
    deferrable=None,
    include=None,
    opclasses=None,
    expressions=None,
    nulls_distinct=None,

# ==================================================
# Line: 1843

def _create_unique_sql(
    self,
    model,
    fields,
    name=None,
    condition=None,
    deferrable=None,
    include=None,
    opclasses=None,
    expressions=None,
    nulls_distinct=None,

# ==================================================
# Line: 1905

def _delete_unique_sql(
    self,
    model,
    name,
    condition=None,
    deferrable=None,
    include=None,
    opclasses=None,
    expressions=None,
    nulls_distinct=None,

# ==================================================
# Line: 1958

def _constraint_names(
    self,
    model,
    column_names=None,
    unique=None,
    primary_key=None,
    index=None,
    foreign_key=None,
    check=None,
    type_=None,
    exclude=None,

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/sqlite3/schema.py
# Line: 357

def _alter_field(
    self,
    model,
    old_field,
    new_field,
    old_type,
    new_type,
    old_db_params,
    new_db_params,
    strict=False,

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/sql/datastructures.py
# Line: 46

def __init__(
    self,
    table_name,
    parent_alias,
    table_alias,
    join_type,
    join_field,
    nullable,
    filtered_relation=None,

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/sql/compiler.py
# Line: 1173

def get_related_selections(
    self,
    select,
    select_mask,
    opts=None,
    root_alias=None,
    cur_depth=1,
    requested=None,
    restricted=None,

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/sql/query.py
# Line: 1463

def build_filter(
    self,
    filter_expr,
    branch_negated=False,
    current_negated=False,
    can_reuse=None,
    allow_joins=True,
    split_subq=True,
    check_filterable=True,
    summarize=False,
    update_join_types=True,

# ==================================================
# Line: 1657

def _add_q(
    self,
    q_object,
    used_aliases,
    branch_negated=False,
    current_negated=False,
    allow_joins=True,
    split_subq=True,
    check_filterable=True,
    summarize=False,
    update_join_types=True,

# ==================================================
# Line: 2374

def add_extra(self, select, select_params, where, params, tables, order_by):
    """
    Add data to the various extra_* attributes for user-created additions
    to the query.
    """
    if select:
        # We need to pair any placeholder markers in the 'select'
        # dictionary with their parameters in 'select_params' so that
        # subsequent updates to the select dictionary also adjust the
        # parameters appropriately.
        select_pairs = {}
        if select_params:
            param_iter = iter(select_params)
        else:
            param_iter = iter([])
        for name, entry in select.items():
            self.check_alias(name)
            entry = str(entry)
            entry_params = []
            pos = entry.find("%s")
            while pos != -1:
                if pos == 0 or entry[pos - 1] != "%":
                    entry_params.append(next(param_iter))
                pos = entry.find("%s", pos + 2)
            select_pairs[name] = (entry, entry_params)
        self.extra.update(select_pairs)
    if where or params:
        self.where.add(ExtraWhere(where, params), AND)
    if tables:
        self.extra_tables += tuple(tables)
    if order_by:
        self.extra_order_by = order_by


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/constraints.py
# Line: 261

def __init__(
    self,
    *expressions,
    fields=(),
    name=None,
    condition=None,
    deferrable=None,
    include=None,
    opclasses=(),
    nulls_distinct=None,
    violation_error_code=None,
    violation_error_message=None,

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/base.py
# Line: 1038

def _save_table(
    self,
    raw=False,
    cls=None,
    force_insert=False,
    force_update=False,
    using=None,
    update_fields=None,

# ==================================================
# Line: 1136

def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
    """
    Try to update the model. Return True if the model was updated (if an
    update query was done and a matching row was found in the DB).
    """
    filtered = base_qs.filter(pk=pk_val)
    if not values:
        # We can end up here when saving a model in inheritance chain where
        # update_fields doesn't target any field in current model. In that
        # case we just say the update succeeded. Another case ending up here
        # is a model with just PK - in that case check that the PK still
        # exists.
        return update_fields is not None or filtered.exists()
    if self._meta.select_on_save and not forced_update:
        return (
            filtered.exists()
            and
            # It may happen that the object is deleted from the DB right after
            # this check, causing the subsequent UPDATE to return zero matching
            # rows. The same result can occur in some rare cases when the
            # database returns zero despite the UPDATE being executed
            # successfully (a row is matched and updated). In order to
            # distinguish these two cases, the object's existence in the
            # database is again checked for if the UPDATE query returns 0.
            (filtered._update(values) > 0 or filtered.exists())
        )
    return filtered._update(values) > 0


# ==================================================
# File: /root/ecooptimizer/django/django/db/models/deletion.py
# Line: 244

def collect(
    self,
    objs,
    source=None,
    nullable=False,
    collect_related=True,
    source_attr=None,
    reverse_dependency=False,
    keep_parents=False,
    fail_on_restricted=True,

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/query.py
# Line: 745

def bulk_create(
    self,
    objs,
    batch_size=None,
    ignore_conflicts=False,
    update_conflicts=False,
    update_fields=None,
    unique_fields=None,

# ==================================================
# Line: 878

async def abulk_create(
    self,
    objs,
    batch_size=None,
    ignore_conflicts=False,
    update_conflicts=False,
    update_fields=None,
    unique_fields=None,

# ==================================================
# Line: 1767

def extra(
    self,
    select=None,
    where=None,
    params=None,
    tables=None,
    order_by=None,
    select_params=None,

# ==================================================
# Line: 1872

def _insert(
    self,
    objs,
    fields,
    returning_fields=None,
    raw=False,
    using=None,
    on_conflict=None,
    update_fields=None,
    unique_fields=None,

# ==================================================
# Line: 1902

def _batched_insert(
    self,
    objs,
    fields,
    batch_size,
    on_conflict=None,
    update_fields=None,
    unique_fields=None,

# ==================================================
# Line: 2093

def __init__(
    self,
    raw_query,
    model=None,
    query=None,
    params=(),
    translations=None,
    using=None,
    hints=None,

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/related.py
# Line: 533

def __init__(
    self,
    to,
    on_delete,
    from_fields,
    to_fields,
    rel=None,
    related_name=None,
    related_query_name=None,
    limit_choices_to=None,
    parent_link=False,
    swappable=True,
    **kwargs,

# ==================================================
# Line: 982

def __init__(
    self,
    to,
    on_delete,
    related_name=None,
    related_query_name=None,
    limit_choices_to=None,
    parent_link=False,
    to_field=None,
    db_constraint=True,
    **kwargs,

# ==================================================
# Line: 1383

def __init__(
    self,
    to,
    related_name=None,
    related_query_name=None,
    limit_choices_to=None,
    symmetrical=None,
    through=None,
    through_fields=None,
    db_constraint=True,
    db_table=None,
    swappable=True,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/__init__.py
# Line: 186

def __init__(
    self,
    verbose_name=None,
    name=None,
    primary_key=False,
    max_length=None,
    unique=False,
    blank=False,
    null=False,
    db_index=False,
    rel=None,
    default=NOT_PROVIDED,
    editable=True,
    serialize=True,
    unique_for_date=None,
    unique_for_month=None,
    unique_for_year=None,
    choices=None,
    help_text="",
    db_column=None,
    db_tablespace=None,
    auto_created=False,
    validators=(),
    error_messages=None,
    db_comment=None,
    db_default=NOT_PROVIDED,

# ==================================================
# Line: 1948

def __init__(
    self,
    verbose_name=None,
    name=None,
    path="",
    match=None,
    recursive=False,
    allow_files=True,
    allow_folders=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/reverse_related.py
# Line: 39

def __init__(
    self,
    field,
    to,
    related_name=None,
    related_query_name=None,
    limit_choices_to=None,
    parent_link=False,
    on_delete=None,

# ==================================================
# Line: 264

def __init__(
    self,
    field,
    to,
    field_name,
    related_name=None,
    related_query_name=None,
    limit_choices_to=None,
    parent_link=False,
    on_delete=None,

# ==================================================
# Line: 319

def __init__(
    self,
    field,
    to,
    field_name,
    related_name=None,
    related_query_name=None,
    limit_choices_to=None,
    parent_link=False,
    on_delete=None,

# ==================================================
# Line: 352

def __init__(
    self,
    field,
    to,
    related_name=None,
    related_query_name=None,
    limit_choices_to=None,
    symmetrical=True,
    through=None,
    through_fields=None,
    db_constraint=True,

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/indexes.py
# Line: 20

def __init__(
    self,
    *expressions,
    fields=(),
    name=None,
    db_tablespace=None,
    opclasses=(),
    condition=None,
    include=None,

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/state.py
# Line: 746

def __init__(
    self, app_label, name, fields, options=None, bases=None, managers=None

# ==================================================
# File: /root/ecooptimizer/django/django/urls/base.py
# Line: 28

def reverse(
    viewname,
    urlconf=None,
    args=None,
    kwargs=None,
    current_app=None,
    *,
    query=None,
    fragment=None,

# ==================================================
# File: /root/ecooptimizer/django/django/urls/resolvers.py
# Line: 35

def __init__(
    self,
    func,
    args,
    kwargs,
    url_name=None,
    app_names=None,
    namespaces=None,
    route=None,
    tried=None,
    captured_kwargs=None,
    extra_kwargs=None,

# ==================================================
# File: /root/ecooptimizer/django/django/forms/forms.py
# Line: 73

def __init__(
    self,
    data=None,
    files=None,
    auto_id="id_%s",
    prefix=None,
    initial=None,
    error_class=ErrorList,
    label_suffix=None,
    empty_permitted=False,
    field_order=None,
    use_required_attribute=None,
    renderer=None,
    bound_field_class=None,

# ==================================================
# File: /root/ecooptimizer/django/django/forms/formsets.py
# Line: 81

def __init__(
    self,
    data=None,
    files=None,
    auto_id="id_%s",
    prefix=None,
    initial=None,
    error_class=ErrorList,
    form_kwargs=None,
    error_messages=None,

# ==================================================
# Line: 534

def formset_factory(
    form,
    formset=BaseFormSet,
    extra=1,
    can_order=False,
    can_delete=False,
    max_num=None,
    validate_max=False,
    min_num=None,
    validate_min=False,
    absolute_max=None,
    can_delete_extra=True,
    renderer=None,

# ==================================================
# File: /root/ecooptimizer/django/django/forms/widgets.py
# Line: 756

def create_option(
    self, name, value, label, selected, index, subindex=None, attrs=None

# ==================================================
# File: /root/ecooptimizer/django/django/forms/models.py
# Line: 140

def fields_for_model(
    model,
    fields=None,
    exclude=None,
    widgets=None,
    formfield_callback=None,
    localized_fields=None,
    labels=None,
    help_texts=None,
    error_messages=None,
    field_classes=None,
    *,
    apply_limit_choices_to=True,
    form_declared_fields=None,

# ==================================================
# Line: 346

def __init__(
    self,
    data=None,
    files=None,
    auto_id="id_%s",
    prefix=None,
    initial=None,
    error_class=ErrorList,
    label_suffix=None,
    empty_permitted=False,
    instance=None,
    use_required_attribute=None,
    renderer=None,

# ==================================================
# Line: 587

def modelform_factory(
    model,
    form=ModelForm,
    fields=None,
    exclude=None,
    formfield_callback=None,
    widgets=None,
    localized_fields=None,
    labels=None,
    help_texts=None,
    error_messages=None,
    field_classes=None,

# ==================================================
# Line: 689

def __init__(
    self,
    data=None,
    files=None,
    auto_id="id_%s",
    prefix=None,
    queryset=None,
    *,
    initial=None,
    **kwargs,

# ==================================================
# Line: 1033

def modelformset_factory(
    model,
    form=ModelForm,
    formfield_callback=None,
    formset=BaseModelFormSet,
    extra=1,
    can_delete=False,
    can_order=False,
    max_num=None,
    fields=None,
    exclude=None,
    widgets=None,
    validate_max=False,
    localized_fields=None,
    labels=None,
    help_texts=None,
    error_messages=None,
    min_num=None,
    validate_min=False,
    field_classes=None,
    absolute_max=None,
    can_delete_extra=True,
    renderer=None,
    edit_only=False,

# ==================================================
# Line: 1107

def __init__(
    self,
    data=None,
    files=None,
    instance=None,
    save_as_new=False,
    prefix=None,
    queryset=None,
    **kwargs,

# ==================================================
# Line: 1300

def inlineformset_factory(
    parent_model,
    model,
    form=ModelForm,
    formset=BaseInlineFormSet,
    fk_name=None,
    fields=None,
    exclude=None,
    extra=3,
    can_order=False,
    can_delete=True,
    max_num=None,
    formfield_callback=None,
    widgets=None,
    validate_max=False,
    localized_fields=None,
    labels=None,
    help_texts=None,
    error_messages=None,
    min_num=None,
    validate_min=False,
    field_classes=None,
    absolute_max=None,
    can_delete_extra=True,
    renderer=None,
    edit_only=False,

# ==================================================
# Line: 1473

def __init__(
    self,
    queryset,
    *,
    empty_label="---------",
    required=True,
    widget=None,
    label=None,
    initial=None,
    help_text="",
    to_field_name=None,
    limit_choices_to=None,
    blank=False,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/django/django/forms/fields.py
# Line: 97

def __init__(
    self,
    *,
    required=True,
    widget=None,
    label=None,
    initial=None,
    help_text="",
    error_messages=None,
    show_hidden_initial=False,
    validators=(),
    localize=False,
    disabled=False,
    label_suffix=None,
    template_name=None,
    bound_field_class=None,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/filters.py
# Line: 176

def __init__(self, field, request, params, model, model_admin, field_path):
    self.field = field
    self.field_path = field_path
    self.title = getattr(field, "verbose_name", field_path)
    super().__init__(request, params, model, model_admin)
    for p in self.expected_parameters():
        if p in params:
            value = params.pop(p)
            self.used_parameters[p] = prepare_lookup_value(
                p, value, self.list_separator
            )


# ==================================================
# Line: 214

def create(cls, field, request, params, model, model_admin, field_path):
    for test, list_filter_class in cls._field_list_filters:
        if test(field):
            return list_filter_class(
                field, request, params, model, model_admin, field_path=field_path
            )



# ==================================================
# Line: 223

def __init__(self, field, request, params, model, model_admin, field_path):
    other_model = get_model_from_relation(field)
    self.lookup_kwarg = "%s__%s__exact" % (field_path, field.target_field.name)
    self.lookup_kwarg_isnull = "%s__isnull" % field_path
    self.lookup_val = params.get(self.lookup_kwarg)
    self.lookup_val_isnull = get_last_value_from_parameters(
        params, self.lookup_kwarg_isnull
    )
    super().__init__(field, request, params, model, model_admin, field_path)
    self.lookup_choices = self.field_choices(field, request, model_admin)
    if hasattr(field, "verbose_name"):
        self.lookup_title = field.verbose_name
    else:
        self.lookup_title = other_model._meta.verbose_name
    self.title = self.lookup_title
    self.empty_value_display = model_admin.get_empty_value_display()


# ==================================================
# Line: 329

def __init__(self, field, request, params, model, model_admin, field_path):
    self.lookup_kwarg = "%s__exact" % field_path
    self.lookup_kwarg2 = "%s__isnull" % field_path
    self.lookup_val = get_last_value_from_parameters(params, self.lookup_kwarg)
    self.lookup_val2 = get_last_value_from_parameters(params, self.lookup_kwarg2)
    super().__init__(field, request, params, model, model_admin, field_path)
    if (
        self.used_parameters
        and self.lookup_kwarg in self.used_parameters
        and self.used_parameters[self.lookup_kwarg] in ("1", "0")
    ):
        self.used_parameters[self.lookup_kwarg] = bool(
            int(self.used_parameters[self.lookup_kwarg])
        )


# ==================================================
# Line: 400

def __init__(self, field, request, params, model, model_admin, field_path):
    self.lookup_kwarg = "%s__exact" % field_path
    self.lookup_kwarg_isnull = "%s__isnull" % field_path
    self.lookup_val = params.get(self.lookup_kwarg)
    self.lookup_val_isnull = get_last_value_from_parameters(
        params, self.lookup_kwarg_isnull
    )
    super().__init__(field, request, params, model, model_admin, field_path)


# ==================================================
# Line: 465

def __init__(self, field, request, params, model, model_admin, field_path):
    self.field_generic = "%s__" % field_path
    self.date_params = {
        k: v[-1] for k, v in params.items() if k.startswith(self.field_generic)
    }

    now = timezone.now()
    # When time zone support is enabled, convert "now" to the user's time
    # zone so Django's definition of "Today" matches what the user expects.
    if timezone.is_aware(now):
        now = timezone.localtime(now)

    if isinstance(field, models.DateTimeField):
        today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    else:  # field is a models.DateField
        today = now.date()
    tomorrow = today + datetime.timedelta(days=1)
    if today.month == 12:
        next_month = today.replace(year=today.year + 1, month=1, day=1)
    else:
        next_month = today.replace(month=today.month + 1, day=1)
    next_year = today.replace(year=today.year + 1, month=1, day=1)

    self.lookup_kwarg_since = "%s__gte" % field_path
    self.lookup_kwarg_until = "%s__lt" % field_path
    self.links = (
        (_("Any date"), {}),
        (
            _("Today"),
            {
                self.lookup_kwarg_since: today,
                self.lookup_kwarg_until: tomorrow,
            },
        ),
        (
            _("Past 7 days"),
            {
                self.lookup_kwarg_since: today - datetime.timedelta(days=7),
                self.lookup_kwarg_until: tomorrow,
            },
        ),
        (
            _("This month"),
            {
                self.lookup_kwarg_since: today.replace(day=1),
                self.lookup_kwarg_until: next_month,
            },
        ),
        (
            _("This year"),
            {
                self.lookup_kwarg_since: today.replace(month=1, day=1),
                self.lookup_kwarg_until: next_year,
            },
        ),
    )
    if field.null:
        self.lookup_kwarg_isnull = "%s__isnull" % field_path
        self.links += (
            (_("No date"), {self.field_generic + "isnull": True}),
            (_("Has date"), {self.field_generic + "isnull": False}),
        )
    super().__init__(field, request, params, model, model_admin, field_path)


# ==================================================
# Line: 565

def __init__(self, field, request, params, model, model_admin, field_path):
    self.lookup_kwarg = field_path
    self.lookup_kwarg_isnull = "%s__isnull" % field_path
    self.lookup_val = params.get(self.lookup_kwarg)
    self.lookup_val_isnull = get_last_value_from_parameters(
        params, self.lookup_kwarg_isnull
    )
    self.empty_value_display = model_admin.get_empty_value_display()
    parent_model, reverse_path = reverse_field_path(model, field_path)
    # Obey parent ModelAdmin queryset when deciding which options to show
    if model == parent_model:
        queryset = model_admin.get_queryset(request)
    else:
        queryset = parent_model._default_manager.all()
    self.lookup_choices = (
        queryset.distinct().order_by(field.name).values_list(field.name, flat=True)
    )
    super().__init__(field, request, params, model, model_admin, field_path)


# ==================================================
# Line: 655

def __init__(self, field, request, params, model, model_admin, field_path):
    if not field.empty_strings_allowed and not field.null:
        raise ImproperlyConfigured(
            "The list filter '%s' cannot be used with field '%s' which "
            "doesn't allow empty strings and nulls."
            % (
                self.__class__.__name__,
                field.name,
            )
        )
    self.lookup_kwarg = "%s__isempty" % field_path
    self.lookup_val = get_last_value_from_parameters(params, self.lookup_kwarg)
    super().__init__(field, request, params, model, model_admin, field_path)


# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/helpers.py
# Line: 101

def __init__(
    self,
    form,
    name=None,
    readonly_fields=(),
    fields=(),
    classes=(),
    description=None,
    model_admin=None,

# ==================================================
# Line: 306

def __init__(
    self,
    inline,
    formset,
    fieldsets,
    prepopulated_fields=None,
    readonly_fields=None,
    model_admin=None,
    has_add_permission=True,
    has_change_permission=True,
    has_delete_permission=True,
    has_view_permission=True,

# ==================================================
# Line: 470

def __init__(
    self,
    formset,
    form,
    fieldsets,
    prepopulated_fields,
    original,
    readonly_fields=None,
    model_admin=None,
    view_on_site_url=None,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/widgets.py
# Line: 254

def __init__(
    self,
    widget,
    rel,
    admin_site,
    can_add_related=None,
    can_change_related=False,
    can_delete_related=False,
    can_view_related=False,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/views/main.py
# Line: 68

def __init__(
    self,
    request,
    model,
    list_display,
    list_display_links,
    list_filter,
    date_hierarchy,
    search_fields,
    list_select_related,
    list_per_page,
    list_max_show_all,
    list_editable,
    model_admin,
    sortable_by,
    search_help_text,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/options.py
# Line: 1302

def render_change_form(
    self, request, context, add=False, change=False, form_url="", obj=None

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/forms.py
# Line: 391

def send_mail(
    self,
    subject_template_name,
    email_template_name,
    context,
    from_email,
    to_email,
    html_email_template_name=None,

# ==================================================
# Line: 441

def save(
    self,
    domain_override=None,
    subject_template_name="registration/password_reset_subject.txt",
    email_template_name="registration/password_reset_email.html",
    use_https=False,
    token_generator=default_token_generator,
    from_email=None,
    request=None,
    html_email_template_name=None,
    extra_email_context=None,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/contenttypes/forms.py
# Line: 12

def __init__(
    self,
    data=None,
    files=None,
    instance=None,
    save_as_new=False,
    prefix=None,
    queryset=None,
    **kwargs,

# ==================================================
# Line: 77

def generic_inlineformset_factory(
    model,
    form=ModelForm,
    formset=BaseGenericInlineFormSet,
    ct_field="content_type",
    fk_field="object_id",
    fields=None,
    exclude=None,
    extra=3,
    can_order=False,
    can_delete=True,
    max_num=None,
    formfield_callback=None,
    validate_max=False,
    for_concrete_model=True,
    min_num=None,
    validate_min=False,
    absolute_max=None,
    can_delete_extra=True,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/contenttypes/fields.py
# Line: 311

def __init__(
    self,
    to,
    object_id_field="object_id",
    content_type_field="content_type",
    for_concrete_model=True,
    related_query_name=None,
    limit_choices_to=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/utils/ogrinspect.py
# Line: 130

def _ogrinspect(
    data_source,
    model_name,
    geom_name="geom",
    layer_key=0,
    srid=None,
    multi_geom=False,
    name_field=None,
    imports=True,
    decimal=False,
    blank=False,
    null=False,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/utils/layermapping.py
# Line: 96

def __init__(
    self,
    model,
    data,
    mapping,
    layer=0,
    source_srs=None,
    encoding="utf-8",
    transaction_mode="commit_on_success",
    transform=True,
    unique=None,
    using=None,

# ==================================================
# Line: 552

def save(
    self,
    verbose=False,
    fid_range=False,
    step=False,
    progress=False,
    silent=False,
    stream=sys.stdout,
    strict=False,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/oracle/schema.py
# Line: 101

def _alter_field(
    self,
    model,
    old_field,
    new_field,
    old_type,
    new_type,
    old_db_params,
    new_db_params,
    strict=False,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/mysql/schema.py
# Line: 61

def _alter_field(
    self,
    model,
    old_field,
    new_field,
    old_type,
    new_type,
    old_db_params,
    new_db_params,
    strict=False,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/postgis/schema.py
# Line: 32

def _alter_column_type_sql(
    self, table, old_field, new_field, new_type, old_collation, new_collation

# ==================================================
# Line: 62

def _alter_field(
    self,
    model,
    old_field,
    new_field,
    old_type,
    new_type,
    old_db_params,
    new_db_params,
    strict=False,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admindocs/utils.py
# Line: 122

def _role(name, rawtext, text, lineno, inliner, options=None, content=None):
    if options is None:
        options = {}
    _, title, target = split_explicit_title(text)
    node = docutils.nodes.reference(
        rawtext,
        title,
        refuri=(
            urlbase
            % (
                inliner.document.settings.link_base,
                target if is_case_sensitive else target.lower(),
            )
        ),
        **options,
    )
    return [node], []


# ==================================================
# Line: 143

def default_reference_role(
    name, rawtext, text, lineno, inliner, options=None, content=None

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/postgres/search.py
# Line: 281

def __init__(
    self,
    expression,
    query,
    *,
    config=None,
    start_sel=None,
    stop_sel=None,
    max_words=None,
    min_words=None,
    short_word=None,
    highlight_all=None,
    max_fragments=None,
    fragment_delimiter=None,

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/postgres/constraints.py
# Line: 25

def __init__(
    self,
    *,
    name,
    expressions,
    index_type=None,
    condition=None,
    deferrable=None,
    include=None,
    violation_error_code=None,
    violation_error_message=None,

# ==================================================
# File: /root/ecooptimizer/django/django/core/files/uploadhandler.py
# Line: 104

def new_file(
    self,
    field_name,
    file_name,
    content_type,
    content_length,
    charset=None,
    content_type_extra=None,

# ==================================================
# File: /root/ecooptimizer/django/django/core/files/uploadedfile.py
# Line: 30

def __init__(
    self,
    file=None,
    name=None,
    content_type=None,
    size=None,
    charset=None,
    content_type_extra=None,

# ==================================================
# Line: 101

def __init__(
    self,
    file,
    field_name,
    name,
    content_type,
    size,
    charset,
    content_type_extra=None,

# ==================================================
# File: /root/ecooptimizer/django/django/core/serializers/xml_serializer.py
# Line: 430

def entity_decl(
    self, name, is_parameter_entity, value, base, sysid, pubid, notation_name

# ==================================================
# Line: 475

def __init__(self, name, value, base, sysid, pubid, notation_name):
    super().__init__()
    self.name = name
    self.value = value
    self.base = base
    self.sysid = sysid
    self.pubid = pubid
    self.notation_name = notation_name


# ==================================================
# File: /root/ecooptimizer/django/django/core/serializers/base.py
# Line: 84

def serialize(
    self,
    queryset,
    *,
    stream=None,
    fields=None,
    use_natural_foreign_keys=False,
    use_natural_primary_keys=False,
    progress_output=None,
    object_count=0,
    **options,

# ==================================================
# File: /root/ecooptimizer/django/django/core/mail/__init__.py
# Line: 64

def send_mail(
    subject,
    message,
    from_email,
    recipient_list,
    fail_silently=False,
    auth_user=None,
    auth_password=None,
    connection=None,
    html_message=None,

# ==================================================
# File: /root/ecooptimizer/django/django/core/mail/backends/smtp.py
# Line: 19

def __init__(
    self,
    host=None,
    port=None,
    username=None,
    password=None,
    use_tls=None,
    fail_silently=False,
    use_ssl=None,
    timeout=None,
    ssl_keyfile=None,
    ssl_certfile=None,
    **kwargs,

# ==================================================
# File: /root/ecooptimizer/django/django/core/mail/message.py
# Line: 205

def __init__(
    self,
    subject="",
    body="",
    from_email=None,
    to=None,
    bcc=None,
    connection=None,
    attachments=None,
    headers=None,
    cc=None,
    reply_to=None,

# ==================================================
# Line: 449

def __init__(
    self,
    subject="",
    body="",
    from_email=None,
    to=None,
    bcc=None,
    connection=None,
    attachments=None,
    headers=None,
    alternatives=None,
    cc=None,
    reply_to=None,

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/commands/inspectdb.py
# Line: 370

def get_meta(
    self,
    table_name,
    constraints,
    column_to_field_name,
    is_view,
    is_partition,
    comment,

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/base.py
# Line: 477

def check(
    self,
    app_configs=None,
    tags=None,
    display_num_errors=False,
    include_deployment_checks=False,
    fail_level=checks.ERROR,
    databases=None,

# ==================================================
# File: /root/ecooptimizer/django/django/core/servers/basehttp.py
# Line: 256

def run(
    addr,
    port,
    wsgi_handler,
    ipv6=False,
    threading=False,
    on_bind=None,
    server_cls=WSGIServer,

# ==================================================
# File: /root/ecooptimizer/django/django/views/generic/dates.py
# Line: 707

def _date_from_string(
    year, year_format, month="", month_format="", day="", day_format="", delim="__"

# ==================================================
