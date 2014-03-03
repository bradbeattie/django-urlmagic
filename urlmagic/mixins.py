from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


class ContextViewMixin(object):
    extra_context = {}

    def get_context_data(self, *args, **kwargs):
        context = super(ContextViewMixin, self).get_context_data(*args, **kwargs)
        context.update(self.extra_context)
        return context


class AutomaticUserFormMixin(object):
    def get_user_field_names(self):
        return [
            field.name
            for field in self.instance._meta.fields
            if isinstance(field, ForeignKey) and field.related.parent_model is User
        ]

    def save(self, *args, **kwargs):
        for field_name in getattr(self, "user_fields", self.get_user_field_names()):
            setattr(self.instance, field_name, self.request.user)
        return super(AutomaticUserFormMixin, self).save(*args, **kwargs)
