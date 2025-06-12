# use-a-generator snippets for django

# File: /root/ecooptimizer/django/django/forms/formsets.py
# Line: 387

forms_valid = all(
    [
        form.is_valid()
        for form in self.forms
        if not (self.can_delete and self._should_delete_form(form))
    ]
)

# ==================================================
# Line: 584

return all([formset.is_valid() for formset in formsets])

# ==================================================
