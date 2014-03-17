from urlmagic.utils import get_user_field_names
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import Http404


class ContextViewMixin(object):
    extra_context = {}

    def get_context_data(self, *args, **kwargs):
        context = super(ContextViewMixin, self).get_context_data(*args, **kwargs)
        context.update(self.extra_context)
        return context


class RedirectOn404Mixin(object):
    redirect_on_404 = None

    def get(self, request, *args, **kwargs):
        try:
            return super(RedirectOn404Mixin, self).get(request, *args, **kwargs)
        except Http404:
            if self.redirect_on_404:
                # TODO: Investigate why django.shortcuts.redirect isn't properly handling relative URLs like "../add/"
                if self.redirect_on_404.startswith("."):
                    return HttpResponseRedirect(self.redirect_on_404)
                else:
                    return redirect(self.redirect_on_404)
            else:
                raise


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
                self.kwargs["pk"] = queryset.first().pk
            else:
                raise Http404

    def get(self, request, *args, **kwargs):
        self.adjust_kwargs()
        return super(SingularViewMixin, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.adjust_kwargs()
        return super(SingularViewMixin, self).post(request, *args, **kwargs)


class FormRequestViewMixin(object):
    def get_form_kwargs(self):
        kwargs = super(FormRequestViewMixin, self).get_form_kwargs()
        if hasattr(self.get_form_class(), "request"):
            kwargs["request"] = self.request
        return kwargs

    def get_form(self, form_class):
        form = super(FormRequestViewMixin, self).get_form(form_class)
        form.request = self.request
        return form
