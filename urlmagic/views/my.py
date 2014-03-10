from urlmagic import mixins
from urlmagic.utils import get_user_field_names
from urlmagic.views import filtered


class MyMixin(object):
    def __init__(self, *args, **kwargs):
        super(MyMixin, self).__init__(*args, **kwargs)
        for field_name in get_user_field_names(self.model):
            self.queryset_filter.setdefault(field_name, filtered.FilteredViewMixin.REQUEST_USER)


class MyListView(MyMixin, filtered.FilteredListView):
    pass


class MyDetailView(MyMixin, filtered.FilteredDetailView):
    pass


class MyCreateView(MyMixin, filtered.FilteredCreateView):
    pass


class MyUpdateView(MyMixin, filtered.FilteredUpdateView):
    pass


class MyDeleteView(MyMixin, filtered.FilteredDeleteView):
    pass
