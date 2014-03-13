from urlmagic import mixins
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.admin.util import NotRelationField
from django.contrib.admin.util import get_model_from_relation
from django.db.models.constants import LOOKUP_SEP
from urlmagic.views import core


# Regular views can be statically filtered by providing a modified queryset paramter (e.g. Foo.objects.filter(flag=True)).
# Sometimes it becomes necessary to filter dynamically using the URL as an indicator of the filtered context object.
# Consider examples such as the following:
#
# /alphas/          Alpha.objects.all()
# /alphas/active/   Alpha.objects.filter(active=True)
# /alphas/1/        Alpha.objects.get(pk=1)
# /alphas/1/betas/  Beta.objects.filter(alphas__pk=1)
# /alphas/1/beta/   Beta.objects.get(alphas__pk=1)
#
# It's the concept in these last two examples that these filtered views address.


class FilteredViewMixin(object):
    context_slug = None
    REQUEST_USER = "request_user"
    additional_kwargs = {}

    def trim_request_user(self, string):
        return string[len(self.REQUEST_USER) + 1:] if string.startswith(self.REQUEST_USER) else string

    def get_merged_kwargs(self):
        kwargs = {}
        kwargs.update(self.kwargs)
        kwargs.update(self.additional_kwargs)
        return kwargs

    def get_filter_kwargs(self):
        if not self.request.user.is_authenticated():
            for key in self.kwargs.keys():
                if key.startswith(self.REQUEST_USER):
                    raise PermissionDenied
        return dict(
            (
                self.trim_request_user(key),
                self.request.user if key.startswith(self.REQUEST_USER) else value,
            )
            for key, value in self.get_merged_kwargs().iteritems()
        )

    def get_queryset(self):
        return super(FilteredViewMixin, self).get_queryset().filter(**self.get_filter_kwargs())

    def get_context_data(self, *args, **kwargs):
        context = super(FilteredViewMixin, self).get_context_data(*args, **kwargs)

        # Add in the queryset used for this filtered view
        context.update({"view_filter_kwargs": self.get_filter_kwargs()})

        # Add in the object that's been filtered on if there's only one or if it's been explicitly provided
        if self.context_slug or len(self.get_merged_kwargs()) == 1:
            context_pointer = self.model
            context_slug = self.context_slug or self.get_merged_kwargs().keys()[0]
            field_names = context_slug.split(LOOKUP_SEP)
            try:
                for field_name in field_names:
                    field_name = self.trim_request_user(field_name)
                    if field_name == "pk":
                        field_name = context_pointer._meta.pk.name
                    context_pointer = get_model_from_relation(context_pointer._meta.get_field_by_name(field_name)[0])
                field_name = "pk"
                field_value = context["view_filter_kwargs"][self.trim_request_user(context_slug)].pk
            except NotRelationField:
                field_name = field_names[-1]
                field_value = context["view_filter_kwargs"][context_slug]
            context["context_object"] = context_pointer.objects.get(**{field_name: field_value})

        return context


class FilteredListView(FilteredViewMixin, core.ContextListView):
    pass


class FilteredDetailView(FilteredViewMixin, core.ContextDetailView):
    pass


class FilteredCreateView(FilteredViewMixin, mixins.FormRequestViewMixin, core.ContextCreateView):
    pass


class FilteredUpdateView(FilteredViewMixin, mixins.FormRequestViewMixin, core.ContextUpdateView):
    pass


class FilteredDeleteView(FilteredViewMixin, core.ContextDeleteView):
    pass
