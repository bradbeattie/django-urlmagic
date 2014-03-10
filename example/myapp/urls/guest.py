from myapp.models import Alpha, Beta, Gamma
from django.conf.urls import patterns
from urlmagic.guest import GuestUrlGenerator
from urlmagic.views import filtered


urlpatterns = patterns("")


for model in (Alpha, Beta, Gamma):
    urlpatterns += patterns(
        "",
        GuestUrlGenerator.add(model),
        GuestUrlGenerator.edit(model),
        GuestUrlGenerator.list(model),
        GuestUrlGenerator.detail(model),
        GuestUrlGenerator.delete(model),
    )


urlpatterns += patterns(
    "",
    GuestUrlGenerator.list(
        Beta,
        view=filtered.FilteredListView,
        view_kwargs={"queryset_filter": {"alpha__slug": "alpha_slug"}},
        url_format="^alphas/(?P<alpha_slug>[^/]+)/{model_plural_short}/$",
        name_format="guest_alpha_pk_beta_list",
    )
)
