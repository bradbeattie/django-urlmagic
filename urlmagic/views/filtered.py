from urlmagic import mixins
from urlmagic.utils import get_user_field_names
from urlmagic.views import core


class FilteredViewMixin(object):
    queryset_filter = {}
    REQUEST_USER = "request.user"

    def get_queryset(self):
        if self.REQUEST_USER in self.queryset_filter.values() and not self.request.user.is_authenticated():
            raise PermissionDenied
        return super(FilteredViewMixin, self).get_queryset().filter(**dict(
            (field_slug, self.request.user if url_variable == self.REQUEST_USER else self.kwargs[url_variable])
            for field_slug, url_variable in self.queryset_filter.iteritems()
        ))


class FilteredListView(FilteredViewMixin, core.ContextListView):
    pass


class FilteredDetailView(FilteredViewMixin, mixins.SingularViewMixin, core.ContextDetailView):
    pass


class FilteredCreateView(FilteredViewMixin, mixins.FormRequestViewMixin, core.ContextCreateView):
    pass


class FilteredUpdateView(FilteredViewMixin, mixins.SingularViewMixin, mixins.FormRequestViewMixin, core.ContextUpdateView):
    pass


class FilteredDeleteView(FilteredViewMixin, mixins.SingularViewMixin, core.ContextDeleteView):
    pass
