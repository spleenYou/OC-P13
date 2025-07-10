from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Represents a physical address

    Attributes:
        number (int): street number
        street (str): name of the street
        city (str): name of the city
        state (str): state in 2 letters
        zip_code (int): between 0 and 99999
        country_iso_code (str): iso code of the country
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        "Displays plural name for admin page"
        verbose_name_plural = 'Adresses'

    def __str__(self):
        "Returns a string containig the street number and name"
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Represents a letting

    Attributes:
        title (str): letting name
        address (obj): Address object
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        "Returns a string containing the title"
        return self.title
