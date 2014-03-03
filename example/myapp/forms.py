from django import forms
from myapp import models
from urlmagic.mixins import AutomaticUserFormMixin


class MyBetaAdd(AutomaticUserFormMixin, forms.ModelForm):
    class Meta:
        model = models.Beta
        exclude = ["owner"]


class MyBetaEdit(forms.ModelForm):
    class Meta:
        model = models.Beta
        exclude = ["owner"]


class MyGammaAdd(AutomaticUserFormMixin, forms.ModelForm):
    class Meta:
        model = models.Gamma
        exclude = ["owner"]


class MyGammaEdit(forms.ModelForm):
    class Meta:
        model = models.Gamma
        exclude = ["owner"]
