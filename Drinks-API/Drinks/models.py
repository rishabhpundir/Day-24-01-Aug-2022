from django.db import models

class Drink(models.Model):
    drink_name = models.CharField(max_length=100)
    drink_description = models.CharField(max_length=200)

    def __str__(self):
        return self.drink_name