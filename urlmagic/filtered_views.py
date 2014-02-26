from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.core.exceptions import PermissionDenied
from django.conf import settings
from urlmagic.utils import get_related_model


class DynamicFilter(object):
    filter = None

    def adjust_kwargs(self, request, *args, **kwargs):

        if "filter" in kwargs:
            self.kwargs["filter"] = kwargs["filter"]
        elif request.user.is_authenticated():
            self.kwargs["filter"] = request.user.pk
        else:
            raise PermissionDenied("You must be logged into access your data.")

        if self.queryset is None:
            self.queryset = self.model.objects.all()
        if "filter" in self.kwargs:
            self.queryset = self.queryset.filter(**{
                self.filter: self.kwargs["filter"]
            }).distinct()

        if "pk" not in self.kwargs:
            self.kwargs["pk"] = self.queryset[0].pk if self.queryset.count() else 0


class FilteredListView(DynamicFilter, ListView):
    add_context = ""
    context_object = None

    def get(self, request, *args, **kwargs):

        self.adjust_kwargs(request, *args, **kwargs)
        if self.filter == "owner__pk":
            self.context_object = User
        else:
            self.context_object = self.model
            for p in self.filter.split("__")[0:-1]:
                self.context_object = get_related_model(self.context_object, p)
        if self.context_object == User and request.user.is_authenticated() and self.kwargs["filter"] == request.user.pk:
            self.context_object = request.user
        elif self.context_object == User and settings.FILTERED_LIST_VIEW_USER_RELATED_FIELDS:
            self.context_object = self.context_object.objects.select_related(*settings.FILTERED_LIST_VIEW_USER_RELATED_FIELDS).get(pk=self.kwargs["filter"])
        else:
            self.context_object = self.context_object.objects.get(pk=self.kwargs["filter"])
        return super(FilteredListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FilteredListView, self).get_context_data(**kwargs)
        context["add_context"] = self.add_context.format(**self.kwargs)
        context["context_object"] = self.context_object
        return context


class FilteredCreateView(DynamicFilter, CreateView):

    def get(self, request, *args, **kwargs):
        self.adjust_kwargs(request, *args, **kwargs)
        return super(FilteredCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            if self.filter == "owner__pk":
                setattr(form.instance, "owner", request.user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        return super(FilteredCreateView, self).post(request, *args, **kwargs)


class FilteredDetailView(DynamicFilter, DetailView):
    def get(self, request, *args, **kwargs):
        self.adjust_kwargs(request, *args, **kwargs)
        return super(FilteredDetailView, self).get(request, *args, **kwargs)


class FilteredUpdateView(DynamicFilter, UpdateView):
    def get(self, request, *args, **kwargs):
        self.adjust_kwargs(request, *args, **kwargs)
        return super(FilteredUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.adjust_kwargs(request, *args, **kwargs)
        return super(FilteredUpdateView, self).post(request, *args, **kwargs)


class FilteredDeleteView(DynamicFilter, DeleteView):
    def get(self, request, *args, **kwargs):
        self.adjust_kwargs(request, *args, **kwargs)
        return super(FilteredDeleteView, self).get(request, *args, **kwargs)


class FilteredDetailOrCreateView(DynamicFilter, DetailView, CreateView):
    add_form_class = None
    add_template_name = None
    detail_template_name = None

    def get(self, request, *args, **kwargs):
        self.adjust_kwargs(request, *args, **kwargs)
        try:
            kwargs["pk"] = self.model.objects.get(owner=request.user).pk
            return DetailView.as_view(
                model=self.model,
                template_name=self.detail_template_name,
            )(request, *args, **kwargs)
        except self.model.DoesNotExist:
            return CreateView.as_view(
                model=self.model,
                form_class=self.add_form_class,
                template_name=self.add_template_name,
                success_url=self.success_url,
            )(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.adjust_kwargs(request, *args, **kwargs)
        try:
            kwargs["pk"] = self.model.objects.get(owner=request.user).pk
            return DetailView.as_view(
                model=self.model,
                template_name=self.detail_template_name,
            )(request, *args, **kwargs)
        except self.model.DoesNotExist:
            return CreateView.as_view(
                model=self.model,
                form_class=self.add_form_class,
                template_name=self.add_template_name,
                success_url=self.success_url,
            )(request, *args, **kwargs)


class FilteredUpdateOrCreateView(DynamicFilter, UpdateView, CreateView):
    add_form_class = None
    add_template_name = None
    update_form_class = None
    update_template_name = None

    def get(self, request, *args, **kwargs):
        self.adjust_kwargs(request, *args, **kwargs)
        try:
            kwargs["pk"] = self.model.objects.get(owner=request.user).pk
            return FilteredUpdateView.as_view(
                model=self.model,
                filter=self.filter,
                form_class=self.update_form_class,
                template_name=self.update_template_name,
                success_url=self.success_url,
            )(request, *args, **kwargs)
        except self.model.DoesNotExist:
            return FilteredCreateView.as_view(
                model=self.model,
                filter=self.filter,
                form_class=self.add_form_class,
                template_name=self.add_template_name,
                success_url=self.success_url,
            )(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.adjust_kwargs(request, *args, **kwargs)
        try:
            kwargs["pk"] = self.model.objects.get(owner=request.user).pk
            return FilteredUpdateView.as_view(
                model=self.model,
                filter=self.filter,
                form_class=self.update_form_class,
                template_name=self.update_template_name,
                success_url=self.success_url,
            )(request, *args, **kwargs)
        except self.model.DoesNotExist:
            return FilteredCreateView.as_view(
                model=self.model,
                filter=self.filter,
                form_class=self.add_form_class,
                template_name=self.add_template_name,
                success_url=self.success_url,
            )(request, *args, **kwargs)
