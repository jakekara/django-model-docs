from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shoeStyle = models.CharField(
        max_length=30, choices=[("LO", "LOAFER"), ("BO", "BOOT"), ("DR", "DRESS")]
    )
