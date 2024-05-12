from django.db import models

# Create your models here.


class DictionaryModel(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)
    name_turk = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name_uz} {self.name_ru} {self.name_eng} {self.name_turk}"

    class Meta:
        db_table = 'dictionary'
        verbose_name_plural = 'Dictionary'

