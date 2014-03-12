from django.conf.urls import patterns
from django.contrib.auth.models import User
from myapp.models import Alpha, Beta, Gamma, Delta
from urlmagic.guest import GuestUrlGenerator
from urlmagic.views import filtered


urlpatterns = patterns("")


for model in (Alpha, Beta, Gamma, Delta):
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
    GuestUrlGenerator.list(User),
    GuestUrlGenerator.detail(User),
    GuestUrlGenerator.list(
        Beta,
        view=filtered.FilteredListView,
        view_kwargs={"queryset_filter": {"owner": "request.user"}},
        url_format="^users/(?P<user_pk>[^/]+)/{model_plural_short}/$",
        name_format="guest_user_pk_beta_list",
    ),
    GuestUrlGenerator.list(
        Delta,
        view=filtered.FilteredListView,
        view_kwargs={"queryset_filter": {"alphas__slug": "alpha_slug"}},
        url_format="^alphas/(?P<alpha_slug>[^/]+)/{model_plural_short}/$",
        name_format="guest_alpha_slug_delta_list",
    ),
    GuestUrlGenerator.list(
        Beta,
        view=filtered.FilteredListView,
        view_kwargs={"queryset_filter": {"alpha__slug": "alpha_slug"}},
        url_format="^alphas/(?P<alpha_slug>[^/]+)/{model_plural_short}/$",
        name_format="guest_alpha_slug_beta_list",
    )
)
