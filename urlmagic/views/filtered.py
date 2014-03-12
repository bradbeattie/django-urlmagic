from urlmagic import mixins
from django.contrib.admin.util import NotRelationField
from django.contrib.admin.util import get_model_from_relation
from django.db.models.constants import LOOKUP_SEP
from urlmagic.utils import get_user_field_names
from urlmagic.views import core


# Regular views can be statically filtered by providing a modified queryset paramter (e.g. Foo.objects.filter(flag=True)).
# Sometimes it becomes necessary to filter dynamically using the URL as an indicator of the filtered context object.
# Consider examples such as the following:
#
# /alphas/          Alpha.objects.all()
# /alphas/active/   Alpha.objects.filter(active=True)
# /alphas/1/        Alpha.objects.get(pk=1)
# /alphas/1/betas/  Beta.objects.filter(alphas__pk=1)
#
# It's the concept in this last example that these filtered views address.


class FilteredViewMixin(object):
    queryset_filter = {}
    context_field_chain = None
    REQUEST_USER = "request.user"

    def get_filter_kwargs(self):
        if self.REQUEST_USER in self.queryset_filter.values() and not self.request.user.is_authenticated():
            raise PermissionDenied
        return dict(
            (field_slug, self.request.user if url_variable == self.REQUEST_USER else self.kwargs[url_variable])
            for field_slug, url_variable in self.queryset_filter.iteritems()
        )

    def get_queryset(self):
        return super(FilteredViewMixin, self).get_queryset().filter(**self.get_filter_kwargs())

    def get_context_data(self, *args, **kwargs):
        context = super(FilteredViewMixin, self).get_context_data(*args, **kwargs)

        # Add in the queryset used for this filtered view
        context.update({"queryset_filter": self.get_filter_kwargs()})

        # Add in the object that's been filtered on if clear or explicitly provided
        if self.context_field_chain or len(self.queryset_filter) == 1:
            context_pointer = self.model
            context_field_chain = self.context_field_chain or self.queryset_filter.keys()[0]
            field_names = context_field_chain.split(LOOKUP_SEP)
            try:
                for field_name in field_names:
                    context_pointer = get_model_from_relation(context_pointer._meta.get_field_by_name(field_name)[0])
                field_name = "pk"
                field_value = context["queryset_filter"][context_field_chain].pk
            except NotRelationField:
                field_name = field_names[-1]
                field_value = context["queryset_filter"][context_field_chain]
            context["context_object"] = context_pointer.objects.get(**{field_name: field_value})

        return context


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
