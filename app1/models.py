from django.db import models


class City(models.Model):
    city = models.CharField(max_length=60, verbose_name="Miasto", null=False, blank=False)
    citizens = models.BigIntegerField(verbose_name="Liczba obywateli", null=False,
                                      blank=False)

    def __str__(self):
        return self.city
