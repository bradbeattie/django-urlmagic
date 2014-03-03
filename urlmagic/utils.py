from django.utils.text import slugify


def model_names(model):
    names = {}
    names["model_system"] = unicode(model._meta.module_name)
    names["model_singular"] = unicode(model._meta.verbose_name)
    names["model_singular_slug"] = unicode(slugify(names["model_singular"]))
    names["model_singular_short"] = names["model_singular_slug"].replace("-", "")
    names["model_plural"] = unicode(model._meta.verbose_name_plural)
    names["model_plural_slug"] = unicode(slugify(names["model_plural"]))
    names["model_plural_short"] = names["model_plural_slug"].replace("-", "")
    names["model_module"] = unicode(model.__module__.split(".")[-2])
    return names
