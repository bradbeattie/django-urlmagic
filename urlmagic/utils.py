from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify


def model_names(model):
    names = {}
    names["model"] = model
    names["model_system"] = unicode(model._meta.model_name)
    names["model_singular"] = unicode(model._meta.verbose_name)
    names["model_singular_slug"] = unicode(slugify(names["model_singular"]))
    names["model_singular_short"] = names["model_singular_slug"].replace("-", "")
    names["model_plural"] = unicode(model._meta.verbose_name_plural)
    names["model_plural_slug"] = unicode(slugify(names["model_plural"]))
    names["model_plural_short"] = names["model_plural_slug"].replace("-", "")
    names["model_module"] = unicode(model.__module__.split(".")[-2])
    return names


def get_user_field_names(model):
    return [
        field.name
        for field in model._meta.fields
        if isinstance(field, ForeignKey) and field.related_model is User
    ]
