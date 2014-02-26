from urlmagic.member import MemberUrlGenerator
from urlmagic import filtered_views
from django.contrib.auth.decorators import user_passes_test


class MyUrlGenerator(MemberUrlGenerator):

    @classmethod
    def adjust_dict(cls, d):
        d.setdefault("format_kwargs", {})
        d["format_kwargs"].setdefault("role", "my")
        d.setdefault("view_kwargs", {})
        d["view_kwargs"].setdefault("filter", d.pop("view_filter", "owner__pk"))
        super(MemberUrlGenerator, cls).adjust_dict(d)
        return d

    @classmethod
    def adjust_result(cls, r):
        super(MemberUrlGenerator, cls).adjust_result(r)
        r._callback = user_passes_test(lambda u: u.is_staff)(r._callback)
        return r

    @classmethod
    def list(cls, model, **kwargs):
        kwargs.setdefault("view", filtered_views.FilteredListView)
        return super(MyUrlGenerator, cls).list(model, **kwargs)

    @classmethod
    def add(cls, model, **kwargs):
        kwargs.setdefault("view", filtered_views.FilteredCreateView)
        return super(MyUrlGenerator, cls).add(model, **kwargs)

    @classmethod
    def detail(cls, model, **kwargs):
        kwargs.setdefault("view", filtered_views.FilteredDetailView)
        return super(MyUrlGenerator, cls).detail(model, **kwargs)

    @classmethod
    def edit(cls, model, **kwargs):
        kwargs.setdefault("view", filtered_views.FilteredUpdateView)
        return super(MyUrlGenerator, cls).edit(model, **kwargs)

    @classmethod
    def delete(cls, model, **kwargs):
        kwargs.setdefault("view", filtered_views.FilteredDeleteView)
        return super(MyUrlGenerator, cls).delete(model, **kwargs)

    @classmethod
    def singular_add(cls, model, **kwargs):
        kwargs.setdefault("view", filtered_views.FilteredCreateView)
        return super(MyUrlGenerator, cls).singular_add(model, **kwargs)

    @classmethod
    def singular_detail(cls, model, **kwargs):
        kwargs.setdefault("view", filtered_views.FilteredDetailView)
        return super(MyUrlGenerator, cls).singular_detail(model, **kwargs)

    @classmethod
    def singular_edit(cls, model, **kwargs):
        kwargs.setdefault("view", filtered_views.FilteredUpdateView)
        return super(MyUrlGenerator, cls).singular_edit(model, **kwargs)

    @classmethod
    def singular_delete(cls, model, **kwargs):
        kwargs.setdefault("view", filtered_views.FilteredDeleteView)
        return super(MyUrlGenerator, cls).singular_delete(model, **kwargs)
