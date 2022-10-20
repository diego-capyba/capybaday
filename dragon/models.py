from django.db import models


class Dragon(models.Model):

    class Color(models.TextChoices):
        RED = ('red', "Red")
        GREEN = ('green', "Green")
        BLUE = ('blue', "Blue")

    name = models.CharField(max_length=100, verbose_name="nome")
    color = models.CharField(choices=Color.choices, max_length=10, verbose_name="cor")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="peso", help_text="tons")
    location = models.ForeignKey('Location', on_delete=models.PROTECT, verbose_name="local")
    riders = models.ManyToManyField('Rider', verbose_name="montadores")

    class Meta:
        verbose_name = "dragão"
        verbose_name_plural = "dragões"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name="nome")

    class Meta:
        verbose_name = "local"
        verbose_name_plural = "locais"

    def __str__(self):
        return self.name


class Rider(models.Model):
    name = models.CharField(max_length=100, verbose_name="nome")

    class Meta:
        verbose_name = "montador"
        verbose_name_plural = "montadores"

    def __str__(self):
        return self.name
