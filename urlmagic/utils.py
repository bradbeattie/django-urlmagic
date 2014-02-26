from django.utils.text import slugify
from django.db.models.fields.related import RelatedField, RelatedObject


def model_names(model):
    names = {}
    names["model_system"] = unicode(model._meta.module_name)
    names["model_singular"] = unicode(model._meta.verbose_name)
    names["model_singular_slug"] = unicode(slugify(names["model_singular"]))
    names["model_plural"] = unicode(model._meta.verbose_name_plural)
    names["model_plural_slug"] = unicode(slugify(names["model_plural"]))
    names["model_module"] = unicode(model.__module__.split(".")[-2])
    return names


def get_related_data(model, field_name):
    response = {
        "access_name": field_name,
        "field": model._meta.get_field_by_name(field_name)[0],
    }
    is_relatedfield = isinstance(response["field"], RelatedField)
    is_relatedobject = isinstance(response["field"], RelatedObject)
    if is_relatedfield or is_relatedobject:
        response.update({
            "access_name": response["field"].get_accessor_name() if is_relatedobject else field_name,
            "reverse_access_name": response["field"].field.name if is_relatedobject else response["field"].related.get_accessor_name(),
            "related_model": response["field"].field.model if is_relatedobject else response["field"].related.parent_model,
        })
    return response


def get_related_model(model, field_name):
    return get_related_data(model, field_name)["related_model"]
