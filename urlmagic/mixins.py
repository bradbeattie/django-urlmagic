class ContextViewMixin(object):
    extra_context = {}

    def get_context_data(self, *args, **kwargs):
        context = super(ContextViewMixin, self).get_context_data(*args, **kwargs)
        context.update(self.extra_context)
        return context


class AutomaticUserFormMixin(object):
    def save(self, *args, **kwargs):
        self.instance.owner = self.request.user
        return super(AutomaticUserFormMixin, self).save(*args, **kwargs)
