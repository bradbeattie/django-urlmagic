from urlmagic.core import UrlGenerator


class GuestUrlGenerator(UrlGenerator):

    @classmethod
    def adjust_dict(cls, d):
        d.setdefault("format_kwargs", {})
        d["format_kwargs"].setdefault("role", "guest")
        super(GuestUrlGenerator, cls).adjust_dict(d)
        return d
