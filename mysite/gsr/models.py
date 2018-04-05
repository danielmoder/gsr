from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Stratum(models.Model):
    question = models.CharField(max_length=200)
    choices = ArrayField(
        base_field=models.TextField(),
        size=10
    )

class Project(models.Model):
    name = models.CharField(max_length=50)
    participants = ArrayField(
        base_field=models.TextField(),
        size=None
    )
    strata = models.ManyToManyField(Stratum)



