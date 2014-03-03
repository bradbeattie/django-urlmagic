from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from urlmagic import mixins


class ContextListView(mixins.ContextViewMixin, ListView):
    pass


class ContextDetailView(mixins.ContextViewMixin, DetailView):
    pass


class ContextCreateView(mixins.ContextViewMixin, CreateView):
    pass


class ContextUpdateView(mixins.ContextViewMixin, UpdateView):
    pass


class ContextDeleteView(mixins.ContextViewMixin, DeleteView):
    pass
