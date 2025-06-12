# long-lambda-expr snippets for django

# File: /root/ecooptimizer/django/django/db/models/fields/related_descriptors.py
# Occurrences: Lines 1150-1160 (2 instances)

lambda result: tuple(
    f.get_db_prep_value(
        getattr(result, f"_prefetch_related_val_{f.attname}"),
        connection,
    )
    for f in fk.local_related_fields
),

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/contenttypes/fields.py
# Line: 660

lambda relobj: (
    object_id_converter(getattr(relobj, self.object_id_field_name)),
    getattr(relobj, content_type_id_field_name),
),

# ==================================================
