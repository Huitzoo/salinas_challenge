from django.db import models


class Comments(models.Model):
    comments = models.CharField(max_length=100,blank=True, null=True)


class Compra(models.Model):
    edad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField()