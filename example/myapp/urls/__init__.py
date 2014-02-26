from django.conf.urls import patterns, include, url


urlpatterns = patterns("",
    url(r'^staff/', include('myapp.urls.staff')),
    url(r'^member/', include('myapp.urls.member')),
    url(r'^my/', include('myapp.urls.my')),
    url(r'^', include('myapp.urls.guest')),
)
