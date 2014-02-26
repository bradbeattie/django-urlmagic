from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models


class MightHaveOwner(models.Model):
    owner = models.ForeignKey(User, db_index=True, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class NamedAndSlugged(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug or self.name)
        super(NamedAndSlugged, self).save(*args, **kwargs)
