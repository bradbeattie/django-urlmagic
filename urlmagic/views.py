from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from urlmagic import mixins


class ContextListView(mixins.ContextMixin, ListView):
    pass


class ContextCreateView(mixins.ContextMixin, CreateView):
    pass


class ContextDetailView(mixins.ContextMixin, DetailView):
    pass


class ContextUpdateView(mixins.ContextMixin, UpdateView):
    pass


class ContextDeleteView(mixins.ContextMixin, DeleteView):
    pass
