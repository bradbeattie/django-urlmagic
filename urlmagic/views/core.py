from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from urlmagic import mixins


class ContextListView(mixins.ContextViewMixin, ListView):
    pass


class ContextDetailView(mixins.ContextViewMixin, mixins.RedirectOn404Mixin, mixins.SingularViewMixin, DetailView):
    pass


class ContextCreateView(mixins.ContextViewMixin, CreateView):
    pass


class ContextUpdateView(mixins.ContextViewMixin, mixins.RedirectOn404Mixin, mixins.SingularViewMixin, UpdateView):
    pass


class ContextDeleteView(mixins.ContextViewMixin, mixins.RedirectOn404Mixin, mixins.SingularViewMixin, DeleteView):
    pass
