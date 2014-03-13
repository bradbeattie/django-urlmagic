from urlmagic.utils import get_user_field_names


class ContextViewMixin(object):
    extra_context = {}

    def get_context_data(self, *args, **kwargs):
        context = super(ContextViewMixin, self).get_context_data(*args, **kwargs)
        context.update(self.extra_context)
        return context


class AutomaticUserFormMixin(object):
    def save(self, *args, **kwargs):
        for field_name in getattr(self, "user_fields", get_user_field_names(self.instance)):
            setattr(self.instance, field_name, self.request.user)
        return super(AutomaticUserFormMixin, self).save(*args, **kwargs)


class SingularViewMixin(object):
    def adjust_kwargs(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if pk is None and slug is None:
            queryset = self.get_queryset()
            if queryset.count():
                self.kwargs["pk"] = queryset[0].pk

    def get(self, request, *args, **kwargs):
        self.adjust_kwargs()
        return super(SingularViewMixin, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.adjust_kwargs()
        return super(SingularViewMixin, self).post(request, *args, **kwargs)


class FormRequestViewMixin(object):
    def get_form_kwargs(self):
        kwargs = super(FormRequestViewMixin, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs
