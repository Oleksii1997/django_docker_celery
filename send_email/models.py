from django.db import models


class Contact(models.Model):
    """ Підписка по e-mail """
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт: "
        verbose_name_plural = "Контакти"