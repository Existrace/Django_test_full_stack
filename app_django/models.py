from django.db import models


class Ressource(models.Model):
    libelle = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    localisation = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.libelle


class Booking(models.Model):
    title = models.CharField(max_length=200)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
