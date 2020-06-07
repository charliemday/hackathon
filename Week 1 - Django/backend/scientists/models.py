from django.db import models

# Create your models here.


class Field(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Scientists(models.Model):

    name = models.CharField(max_length=255)

    field = models.ManyToManyField(Field, related_name="scientists_field")

    class Meta:
        verbose_name = "Scientist"
        verbose_name_plural = "Scientists"
