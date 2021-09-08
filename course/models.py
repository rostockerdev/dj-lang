from django.db import models


class Course(models.Model):
    title = models.CharField("Title", max_length=128)
    description = models.TextField()
    date = models.DateField()
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.title
