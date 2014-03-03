from urlmagic.core import UrlGenerator
from django.contrib.auth.decorators import login_required


class MemberUrlGenerator(UrlGenerator):

    @classmethod
    def adjust_dict(cls, model, d):
        d.setdefault("format_kwargs", {})
        d["format_kwargs"].setdefault("role", "member")
        super(MemberUrlGenerator, cls).adjust_dict(model, d)
        return d

    @classmethod
    def adjust_result(cls, r):
        super(MemberUrlGenerator, cls).adjust_result(r)
        r._callback = login_required(r._callback)
        return r
