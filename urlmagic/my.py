from urlmagic.member import MemberUrlGenerator
from django.contrib.auth.decorators import user_passes_test
from urlmagic.views import my


class MyUrlGenerator(MemberUrlGenerator):

    default_views = {
        "create": my.MyCreateView,
        "delete": my.MyDeleteView,
        "detail": my.MyDetailView,
        "edit": my.MyUpdateView,
        "list": my.MyListView,
    }

    @classmethod
    def adjust_dict(cls, model, d):
        d.setdefault("format_kwargs", {})
        d["format_kwargs"].setdefault("role", "my")
        super(MyUrlGenerator, cls).adjust_dict(model, d)
        return d
