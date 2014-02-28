class ContextMixin(object):
    extra_context = {}

    def get_context_data(self, *args, **kwargs):
        context = super(ContextMixin, self).get_context_data(*args, **kwargs)
        context.update(self.extra_context)
        return context
