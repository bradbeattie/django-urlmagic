from django.contrib.auth.models import User
from django.db import models
from myapp.base_models import NamedAndSlugged, MustHaveOwner, MightHaveOwner


class Alpha(NamedAndSlugged):
    pass


class Beta(NamedAndSlugged, MightHaveOwner):
    pass


class Gamma(NamedAndSlugged, MustHaveOwner):
    class Meta:
        verbose_name = "Verbose-named Gamma"


class Delta(NamedAndSlugged):
    owner = models.OneToOneField(User, db_index=True)


class Epsilon(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name
