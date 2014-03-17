from myapp.models import Beta, Gamma
from myapp import forms
from django.conf.urls import patterns
from urlmagic.my import MyUrlGenerator


urlpatterns = patterns(
    "",
    MyUrlGenerator.list(Beta),
    MyUrlGenerator.add(Beta, form_class=forms.MyBetaAdd),
    MyUrlGenerator.edit(Beta, form_class=forms.MyBetaEdit),
    MyUrlGenerator.delete(Beta),
    MyUrlGenerator.detail(Beta),
    MyUrlGenerator.singular_add(Gamma, form_class=forms.MyGammaAdd, view_kwargs={"redirect_on_exists": "my_gamma_detail"}),
    MyUrlGenerator.singular_edit(Gamma, form_class=forms.MyGammaEdit, view_kwargs={"redirect_on_404": "my_gamma_add"}),
    MyUrlGenerator.singular_detail(Gamma, view_kwargs={"redirect_on_404": "my_gamma_add"}),
    MyUrlGenerator.singular_delete(Gamma),
)

print urlpatterns
