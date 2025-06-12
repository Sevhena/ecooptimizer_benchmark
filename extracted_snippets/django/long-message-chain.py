# long-message-chain snippets for django

# File: /root/ecooptimizer/django/django/template/defaultfilters.py
# Line: 68

return value.replace("\\", "\\\\").replace('"', '\\"').replace("'", "\\'")

# ==================================================
# File: /root/ecooptimizer/django/django/utils/http.py
# Line: 185

return base64.urlsafe_b64encode(s).rstrip(b"\n=").decode("ascii")

# ==================================================
# File: /root/ecooptimizer/django/django/utils/text.py
# Line: 279

s = str(name).strip().replace(" ", "_")

# ==================================================
# Line: 465

unicodedata.normalize("NFKD", value)
.encode("ascii", "ignore")
.decode("ascii")

# ==================================================
# Line: 477

return re_camel_case.sub(r" \1", value).strip().lower()

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/oracle/base.py
# Line: 32

if platform.system().upper().startswith("CYGWIN"):

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/base/operations.py
# Line: 502

return str(x).replace("\\", "\\\\").replace("%", r"\%").replace("_", r"\_")

# ==================================================
# File: /root/ecooptimizer/django/django/db/backends/sqlite3/introspection.py
# Line: 420

columns = str(token).strip("()").split(", ")

# ==================================================
# Line: 437

columns = str(sqlparse.parse(sql)[0][-1]).strip("()").split(", ")

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/base.py
# Line: 1111

cls._base_manager.using(using)
.filter(**filter_args)
.aggregate(
    _order__max=Coalesce(
        ExpressionWrapper(
            Max("_order") + Value(1), output_field=IntegerField()
        ),
        Value(0),
    ),
)["_order__max"]

# ==================================================
# Line: 1269

self.__class__._default_manager.using(self._state.db)
.filter(**kwargs)
.filter(q)
.order_by("%s%s" % (order, field.name), "%spk" % order)

# ==================================================
# Line: 1289

self.__class__._default_manager.filter(**filter_args)
.filter(
    **{
        "_order__%s"
        % op: self.__class__._default_manager.values("_order").filter(
            **{self._meta.pk.name: self.pk}
        )
    }
)
.order_by(order)[:1]

# ==================================================
# Line: 2420

ordered_obj.objects.db_manager(using).filter(**filter_args).bulk_update(
    [ordered_obj(pk=pk, _order=order) for order, pk in enumerate(id_list)],
    ["_order"],
)

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/query.py
# Line: 859

self.model._base_manager.using(self.db)
.filter(reduce(operator.or_, filters))
.values_list(*attnames)
.annotate(_order__max=Max("_order") + 1)

# ==================================================
# Line: 1458

self.annotate(
    datefield=Trunc(field_name, kind, output_field=DateField()),
    plain_field=F(field_name),
)
.values_list("datefield", flat=True)
.distinct()
.filter(plain_field__isnull=False)
.order_by(("-" if order == "DESC" else "") + "datefield")

# ==================================================
# Line: 1486

self.annotate(
    datetimefield=Trunc(
        field_name,
        kind,
        output_field=DateTimeField(),
        tzinfo=tzinfo,
    ),
    plain_field=F(field_name),
)
.values_list("datetimefield", flat=True)
.distinct()
.filter(plain_field__isnull=False)
.order_by(("-" if order == "DESC" else "") + "datetimefield")

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/manager.py
# Line: 213

return super().get_queryset().none()

# ==================================================
# File: /root/ecooptimizer/django/django/db/models/fields/related_descriptors.py
# Line: 797

self.model._base_manager.using(db).filter(pk__in=pks).update(
    **{
        self.field.name: self.instance,
    }
)

# ==================================================
# Occurrences: Lines 1258-1259 (2 instances)

filters = self._build_remove_filters(super().get_queryset().using(db))

# ==================================================
# Line: 1414

self.through._default_manager.using(db)
.values_list(target_field_name, flat=True)
.filter(
    **{
        source_field_name: self.related_val[0],
        "%s__in" % target_field_name: target_ids,
    }
)

# ==================================================
# Line: 1566

self.through._default_manager.using(db).filter(filters).delete()

# ==================================================
# File: /root/ecooptimizer/django/django/db/migrations/autodetector.py
# Line: 702

set(old_base_model_state.fields)
.difference(
    new_base_model_state.fields,
)
.intersection(model_state.fields)

# ==================================================
# File: /root/ecooptimizer/django/django/urls/resolvers.py
# Line: 768

if set(kwargs).symmetric_difference(params).difference(defaults):

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/filters.py
# Line: 580

queryset.distinct().order_by(field.name).values_list(field.name, flat=True)

# ==================================================
# Line: 644

model_admin.get_queryset(request)
.distinct()
.values_list("%s__pk" % self.field_path, flat=True)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/admin/options.py
# Line: 2251

LogEntry.objects.filter(
    object_id=unquote(object_id),
    content_type=get_content_type_for_model(model),
)
.select_related()
.order_by("action_time")

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/sessions/backends/db.py
# Occurrences: Lines 192-198 (2 instances)

cls.get_model_class().objects.filter(expire_date__lt=timezone.now()).delete()

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/hashers.py
# Line: 328

hash = base64.b64encode(hash).decode("ascii").strip()

# ==================================================
# Line: 596

hash_ = base64.b64encode(hash_).decode("ascii").strip()

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/management/__init__.py
# Line: 86

Permission.objects.using(using)
.filter(
    content_type__in=set(ctypes.values()),
)
.values_list("content_type", "codename")

# ==================================================
# Line: 149

unicodedata.normalize("NFKD", default_username)
.encode("ascii", "ignore")
.decode("ascii")
.replace(" ", "")
.lower()

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/auth/migrations/0011_update_proxy_permissions.py
# Line: 47

Permission.objects.using(alias).filter(
    permissions_query,
    content_type=old_content_type,
).update(content_type=new_content_type)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/contenttypes/models.py
# Line: 179

return self.model_class()._base_manager.using(using).get(**kwargs)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/contenttypes/fields.py
# Line: 694

self.model._base_manager.using(db).filter(pk__in=pks).update(
    **{
        self.content_type_field_name: self.content_type,
        self.object_id_field_name: self.pk_val,
    }
)

# ==================================================
# Line: 784

return super().using(db).create(**kwargs)

# ==================================================
# Line: 797

return super().using(db).get_or_create(**kwargs)

# ==================================================
# Line: 810

return super().using(db).update_or_create(**kwargs)

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/geos/geometry.py
# Line: 400

return wkt_w(dim=3 if self.hasz else 2, trim=True).write(self).decode()

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/gis/db/backends/oracle/operations.py
# Line: 139

return super().geo_quote_name(name).upper()

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/sites/managers.py
# Line: 62

super()
.get_queryset()
.filter(**{self._get_field_name() + "__id": settings.SITE_ID})

# ==================================================
# File: /root/ecooptimizer/django/django/contrib/sitemaps/__init__.py
# Line: 196

self.queryset.order_by("-" + self.date_field)
.values_list(self.date_field, flat=True)
.first()

# ==================================================
# File: /root/ecooptimizer/django/django/core/serializers/xml_serializer.py
# Line: 163

query_set = getattr(obj, field.name).select_related(None).only("pk")

# ==================================================
# File: /root/ecooptimizer/django/django/core/serializers/python.py
# Line: 89

query_set = getattr(obj, field.name).select_related(None).only("pk")

# ==================================================
# File: /root/ecooptimizer/django/django/core/handlers/asgi.py
# Line: 324

(b"Set-Cookie", c.output(header="").encode("ascii").strip())

# ==================================================
# File: /root/ecooptimizer/django/django/core/management/__init__.py
# Line: 124

min(s_opt.option_strings).lstrip("-").replace("-", "_"): s_opt.dest

# ==================================================
# File: /root/ecooptimizer/django/django/views/generic/dates.py
# Line: 799

qs = generic_view.get_queryset().filter(**lookup).order_by(ordering)

# ==================================================
