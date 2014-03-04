from urlmagic.views import core
from urlmagic import mixins


class MyListView(mixins.FilterViewMixin, core.ContextListView):
    pass


class MyDetailView(mixins.FilterViewMixin, mixins.SingularViewMixin, core.ContextDetailView):
    pass


class MyCreateView(mixins.FilterViewMixin, mixins.FormRequestViewMixin, core.ContextCreateView):
    pass


class MyUpdateView(mixins.FilterViewMixin, mixins.SingularViewMixin, mixins.FormRequestViewMixin, core.ContextUpdateView):
    pass


class MyDeleteView(mixins.FilterViewMixin, mixins.SingularViewMixin, core.ContextDeleteView):
    pass
