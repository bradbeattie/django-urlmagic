from urlmagic import filtered_views, member


def adjust_dict(d):
    d.setdefault("format_kwargs", {})
    d["format_kwargs"].setdefault("role", "my")
    d.setdefault("view_kwargs", {})
    d["view_kwargs"].setdefault("filter", d.pop("view_filter", "owner__pk"))
    return d


def list(model, **kwargs):
    kwargs = adjust_dict(kwargs)
    kwargs["view"] = filtered_views.FilteredListView
    return member.list(model, **kwargs)


def add(model, **kwargs):
    kwargs = adjust_dict(kwargs)
    kwargs.setdefault("view", filtered_views.FilteredCreateView)
    return member.add(model, **kwargs)


def detail(model, **kwargs):
    kwargs = adjust_dict(kwargs)
    kwargs.setdefault("view", filtered_views.FilteredDetailView)
    return member.detail(model, **kwargs)


def edit(model, **kwargs):
    kwargs = adjust_dict(kwargs)
    kwargs.setdefault("view", filtered_views.FilteredUpdateView)
    return member.edit(model, **kwargs)


def delete(model, **kwargs):
    kwargs = adjust_dict(kwargs)
    kwargs.setdefault("view", filtered_views.FilteredDeleteView)
    return member.delete(model, **kwargs)


def singular_add(model, **kwargs):
    kwargs = adjust_dict(kwargs)
    kwargs.setdefault("view", filtered_views.FilteredCreateView)
    return member.singular_add(model, **kwargs)


def singular_detail(model, **kwargs):
    kwargs = adjust_dict(kwargs)
    kwargs.setdefault("view", filtered_views.FilteredDetailView)
    return member.singular_detail(model, **kwargs)


def singular_edit(model, **kwargs):
    kwargs = adjust_dict(kwargs)
    kwargs.setdefault("view", filtered_views.FilteredUpdateView)
    return member.singular_edit(model, **kwargs)


def singular_delete(model, **kwargs):
    kwargs = adjust_dict(kwargs)
    kwargs.setdefault("view", filtered_views.FilteredDeleteView)
    return member.singular_delete(model, **kwargs)
