from abc import ABCMeta
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.decorators import permission_required
from django.db.models.fields import SlugField
from urlmagic.views import core
from urlmagic.utils import model_names


class UrlGenerator(object):
    __metaclass__ = ABCMeta

    default_views = {
        "add": core.ContextCreateView,
        "delete": core.ContextDeleteView,
        "detail": core.ContextDetailView,
        "edit": core.ContextUpdateView,
        "list": core.ContextListView,
    }

    @classmethod
    def get_model_key(cls, model):
        for field in model._meta.fields:
            if field.db_index and field._unique and isinstance(field, SlugField):
                return field.name
        return "pk"

    @classmethod
    def adjust_result(cls, r):
        return r

    @classmethod
    def adjust_dict(cls, model, d):
        return d

    @classmethod
    def list(cls, model, **kwargs):
        return cls.adjust_result(cls.list_inner(model, **cls.adjust_dict(model, kwargs)))

    @classmethod
    def add(cls, model, **kwargs):
        return cls.adjust_result(cls.add_inner(model, **cls.adjust_dict(model, kwargs)))

    @classmethod
    def detail(cls, model, **kwargs):
        return cls.adjust_result(cls.detail_inner(model, **cls.adjust_dict(model, kwargs)))

    @classmethod
    def edit(cls, model, **kwargs):
        return cls.adjust_result(cls.edit_inner(model, **cls.adjust_dict(model, kwargs)))

    @classmethod
    def delete(cls, model, **kwargs):
        return cls.adjust_result(cls.delete_inner(model, **cls.adjust_dict(model, kwargs)))

    @classmethod
    def list_inner(
        cls,
        model=None,
        queryset=None,
        name_format="{role}_{model_system}_list",
        permission_format=False,
        template_format="{role}/{model_system}_list.html",
        url_format="^{model_plural_short}/$",
        view=None,
        view_kwargs=None,
        format_kwargs=None,
    ):
        format_kwargs = format_kwargs or {}
        format_kwargs.update(model_names(model))
        view_kwargs = view_kwargs or {}
        view_kwargs.setdefault("extra_context", {})
        view_kwargs["extra_context"].update(format_kwargs)
        view_kwargs.setdefault("model", model)
        view_kwargs.setdefault("queryset", queryset)
        view_kwargs.setdefault("paginate_by", getattr(settings, "PAGINATE_PER_PAGE", 50))
        view_kwargs.setdefault("template_name", template_format.format(**format_kwargs))
        response = url(
            url_format.format(**format_kwargs),
            (view or cls.default_views.get("list", core.ContextListView)).as_view(**view_kwargs),
            name=name_format.format(**format_kwargs)
        )
        if permission_format:
            if permission_format is True:
                permission_format = "{model_module}.change_{model_system}"
            response._callback = permission_required(permission_format.format(**format_kwargs))(response._callback)
        return response

    @classmethod
    def add_inner(
        cls,
        model=None,
        queryset=None,
        form_class=None,
        name_format="{role}_{model_system}_add",
        permission_format=False,
        template_format="{role}/{model_system}_add.html",
        url_format="^{model_plural_short}/add/$",
        view=None,
        view_kwargs=None,
        format_kwargs=None,
    ):
        format_kwargs = format_kwargs or {}
        format_kwargs.update(model_names(model))
        view_kwargs = view_kwargs or {}
        view_kwargs.setdefault("extra_context", {})
        view_kwargs["extra_context"].update(format_kwargs)
        view_kwargs.setdefault("form_class", form_class)
        view_kwargs.setdefault("model", model)
        view_kwargs.setdefault("queryset", queryset)
        view_kwargs.setdefault("template_name", template_format.format(**format_kwargs))
        response = url(
            url_format.format(**format_kwargs),
            (view or cls.default_views.get("add", core.ContextCreateView)).as_view(**view_kwargs),
            name=name_format.format(**format_kwargs)
        )
        if permission_format:
            if permission_format is True:
                permission_format = "{model_module}.add_{model_system}"
            response._callback = permission_required(permission_format.format(**format_kwargs))(response._callback)
        return response

    @classmethod
    def detail_inner(
        cls,
        model=None,
        queryset=None,
        name_format="{role}_{model_system}_detail",
        permission_format=False,
        template_format="{role}/{model_system}_detail.html",
        model_key=None,
        url_format="^{model_plural_short}/(?P<{model_key}>[^/]+)/$",
        view=None,
        view_kwargs=None,
        format_kwargs=None,
    ):
        format_kwargs = format_kwargs or {}
        format_kwargs.setdefault("model_key", model_key or cls.get_model_key(model))
        format_kwargs.update(model_names(model))
        view_kwargs = view_kwargs or {}
        view_kwargs.setdefault("extra_context", {})
        view_kwargs["extra_context"].update(format_kwargs)
        view_kwargs.setdefault("model", model)
        view_kwargs.setdefault("queryset", queryset)
        view_kwargs.setdefault("template_name", template_format.format(**format_kwargs))
        response = url(
            url_format.format(**format_kwargs),
            (view or cls.default_views.get("detail", core.ContextDetailView)).as_view(**view_kwargs),
            name=name_format.format(**format_kwargs)
        )
        if permission_format:
            if permission_format is True:
                permission_format = "{model_module}.change_{model_system}"
            response._callback = permission_required(permission_format.format(**format_kwargs))(response._callback)
        return response

    @classmethod
    def edit_inner(
        cls,
        model=None,
        queryset=None,
        form_class=None,
        name_format="{role}_{model_system}_edit",
        permission_format=False,
        template_format="{role}/{model_system}_edit.html",
        model_key=None,
        url_format="^{model_plural_short}/(?P<{model_key}>[^/]+)/edit/$",
        view=None,
        view_kwargs=None,
        format_kwargs=None,
    ):
        format_kwargs = format_kwargs or {}
        format_kwargs.setdefault("model_key", model_key or cls.get_model_key(model))
        format_kwargs.update(model_names(model))
        view_kwargs = view_kwargs or {}
        view_kwargs.setdefault("extra_context", {})
        view_kwargs["extra_context"].update(format_kwargs)
        view_kwargs.setdefault("form_class", form_class)
        view_kwargs.setdefault("model", model)
        view_kwargs.setdefault("queryset", queryset)
        view_kwargs.setdefault("template_name", template_format.format(**format_kwargs))
        response = url(
            url_format.format(**format_kwargs),
            (view or cls.default_views.get("edit", core.ContextUpdateView)).as_view(**view_kwargs),
            name=name_format.format(**format_kwargs)
        )
        if permission_format:
            if permission_format is True:
                permission_format = "{model_module}.change_{model_system}"
            response._callback = permission_required(permission_format.format(**format_kwargs))(response._callback)
        return response

    @classmethod
    def delete_inner(
        cls,
        model=None,
        queryset=None,
        name_format="{role}_{model_system}_delete",
        permission_format=False,
        template_format="{role}/{model_system}_delete.html",
        model_key=None,
        url_format="^{model_plural_short}/(?P<{model_key}>[^/]+)/delete/$",
        view=None,
        view_kwargs=None,
        format_kwargs=None,
    ):
        format_kwargs = format_kwargs or {}
        format_kwargs.setdefault("model_key", model_key or cls.get_model_key(model))
        format_kwargs.update(model_names(model))
        view_kwargs = view_kwargs or {}
        view_kwargs.setdefault("extra_context", {})
        view_kwargs["extra_context"].update(format_kwargs)
        view_kwargs.setdefault("success_url", "../..")
        view_kwargs.setdefault("model", model)
        view_kwargs.setdefault("queryset", queryset)
        view_kwargs.setdefault("template_name", template_format.format(**format_kwargs))
        response = url(
            url_format.format(**format_kwargs),
            (view or cls.default_views.get("delete", core.ContextDeleteView)).as_view(**view_kwargs),
            name=name_format.format(**format_kwargs)
        )
        if permission_format:
            if permission_format is True:
                permission_format = "{model_module}.delete_{model_system}"
            response._callback = permission_required(permission_format.format(**format_kwargs))(response._callback)
        return response

    @classmethod
    def singular_add(cls, model, **kwargs):
        kwargs.setdefault("name_format", "{role}_{model_system}_add")
        kwargs.setdefault("url_format", "^{model_singular_short}/add/$")
        return cls.add(model, **kwargs)

    @classmethod
    def singular_edit(cls, model, **kwargs):
        kwargs.setdefault("name_format", "{role}_{model_system}_edit")
        kwargs.setdefault("url_format", "^{model_singular_short}/edit/$")
        kwargs.setdefault("view_kwargs", {})
        kwargs["view_kwargs"].setdefault("success_url", ".")
        return cls.edit(model, **kwargs)

    @classmethod
    def singular_detail(cls, model, **kwargs):
        kwargs.setdefault("name_format", "{role}_{model_system}_detail")
        kwargs.setdefault("url_format", "^{model_singular_short}/$")
        return cls.detail(model, **kwargs)

    @classmethod
    def singular_delete(cls, model, **kwargs):
        kwargs.setdefault("name_format", "{role}_{model_system}_delete")
        kwargs.setdefault("url_format", "^{model_singular_short}/delete/$")
        return cls.delete(model, **kwargs)
