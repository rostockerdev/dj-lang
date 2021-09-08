from django.db import models
from django.utils.translation import ugettext_lazy as _


class Course(models.Model):
    title = models.CharField(
        _("Title"), max_length=128, help_text=_("This is the Course title")
    )
    description = models.TextField()
    date = models.DateField()
    price = models.DecimalField(
        _("Price"), max_digits=10, decimal_places=2, help_text=_("This is the price")
    )

    def __str__(self) -> str:
        return self.title
