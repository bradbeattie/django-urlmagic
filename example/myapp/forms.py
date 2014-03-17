from django import forms
from myapp import models
from urlmagic.mixins import AutomaticUserFormMixin, ChokeIfAlreadyExists


class MyBetaAdd(AutomaticUserFormMixin, forms.ModelForm):
    class Meta:
        model = models.Beta
        exclude = ["owner"]


class MyBetaEdit(forms.ModelForm):
    class Meta:
        model = models.Beta
        exclude = ["owner"]


class MyGammaAdd(AutomaticUserFormMixin, ChokeIfAlreadyExists, forms.ModelForm):
    class Meta:
        model = models.Gamma
        exclude = ["owner"]


class MyGammaEdit(forms.ModelForm):
    class Meta:
        model = models.Gamma
        exclude = ["owner"]


class GuestGammaAdd(forms.ModelForm):
    class Meta:
        model = models.Gamma
        exclude = ["owner"]

    def save(self, *args, **kwargs):
        raise Exception(self.instance, args, kwargs, self.request)
