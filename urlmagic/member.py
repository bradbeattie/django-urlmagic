from urlmagic.core import UrlGenerator
from django.contrib.auth.decorators import user_passes_test


class MemberUrlGenerator(UrlGenerator):

    @classmethod
    def adjust_dict(cls, d):
        d.setdefault("format_kwargs", {})
        d["format_kwargs"].setdefault("role", "member")
        super(MemberUrlGenerator, cls).adjust_dict(d)
        return d

    @classmethod
    def adjust_result(cls, r):
        super(MemberUrlGenerator, cls).adjust_result(r)
        r._callback = user_passes_test(lambda u: u.is_authenticated)(r._callback)
        return r
