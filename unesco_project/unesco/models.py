from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    justification = models.CharField(max_length=128)
    year = models.PositiveIntegerField(null=True)
    longitiude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    state = models.ForeignKey('state', on_delete=models.CASCADE)
    region = models.ForeignKey('region', on_delete=models.CASCADE)
    iso = models.ForeignKey('iso', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
