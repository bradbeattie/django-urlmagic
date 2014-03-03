from urlmagic.views import core


class FilterMixin(object):
    def get_queryset(self):
        return super(FilterMixin, self).get_queryset().filter(owner=self.request.user)


class FormRequestMixin(object):
    def get_form(self, form_class):
        form = super(FormRequestMixin, self).get_form(form_class)
        form.request = self.request
        return form


class MyListView(FilterMixin, core.ContextListView):
    pass


class MyDetailView(FilterMixin, core.ContextDetailView):
    pass


class MyCreateView(FilterMixin, FormRequestMixin, core.ContextCreateView):
    pass


class MyUpdateView(FilterMixin, FormRequestMixin, core.ContextUpdateView):
    pass


class MyDeleteView(FilterMixin, core.ContextDeleteView):
    pass
