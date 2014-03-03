from django.core.exceptions import PermissionDenied
from django.http import Http404
from urlmagic.views import core


class FilterMixin(object):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return super(FilterMixin, self).get_queryset().filter(owner=self.request.user)
        else:
            raise PermissionDenied


class SingularMixin(object):
    def adjust_kwargs(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if pk is None and slug is None:
            queryset = self.get_queryset()
            if queryset.count():
                self.kwargs["pk"] = queryset[0].pk
                return

    def get(self, request, *args, **kwargs):
        self.adjust_kwargs()
        return super(SingularMixin, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.adjust_kwargs()
        return super(SingularMixin, self).post(request, *args, **kwargs)


class FormRequestMixin(object):
    def get_form(self, form_class):
        form = super(FormRequestMixin, self).get_form(form_class)
        form.request = self.request
        return form


class MyListView(FilterMixin, core.ContextListView):
    pass


class MyDetailView(FilterMixin, SingularMixin, core.ContextDetailView):
    pass


class MyCreateView(FilterMixin, FormRequestMixin, core.ContextCreateView):
    pass


class MyUpdateView(FilterMixin, SingularMixin, FormRequestMixin, core.ContextUpdateView):
    pass


class MyDeleteView(FilterMixin, SingularMixin, core.ContextDeleteView):
    pass
