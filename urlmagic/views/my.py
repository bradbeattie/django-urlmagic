from urlmagic import mixins
from urlmagic.utils import get_user_field_names
from urlmagic.views import filtered


class MyMixin(object):
    additional_kwargs = {
        "%s_owner" % filtered.FilteredViewMixin.REQUEST_USER: True,
    }


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
