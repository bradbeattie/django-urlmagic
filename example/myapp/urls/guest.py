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
        url_format="^users/(?P<request_user_owner>[^/]+)/{model_plural_short}/$",  # TODO: Would be nice to get "users" automatically
        name_format="guest_request_user_owner_beta_list",  # TODO: Would be nice to get this name format automatically
    ),
    GuestUrlGenerator.list(
        Delta,
        view=filtered.FilteredListView,
        url_format="^alphas/(?P<alphas__slug>[^/]+)/{model_plural_short}/$",  # TODO: Would be nice to get "alphas" automatically
        name_format="guest_alphas__slug_delta_list",
    ),
    GuestUrlGenerator.list(
        Beta,
        view=filtered.FilteredListView,
        url_format="^alphas/(?P<alpha__slug>[^/]+)/{model_plural_short}/$",
        name_format="guest_alpha__slug_beta_list",
    ),
    GuestUrlGenerator.singular_detail(
        Gamma,
        view=filtered.FilteredDetailView,
        url_format="^users/(?P<owner__pk>[^/]+)/{model_singular_short}/$",
        name_format="guest_owner__pk_gamma_detail",
    ),
)
