from django.db import models

# Create your models here.


class CityPlansCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cityplanscategory'
        verbose_name_plural = 'CityPlans'


class CitySubPlans(models.Model):
    name = models.CharField(max_length=255)
    guruh_id = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'citysubplans'
        verbose_name_plural = 'CitySubPlans'


class CityMinSubPlans(models.Model):
    name = models.CharField(max_length=255)
    shnq_code = models.CharField(max_length=30)
    content = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cityminsubplans'
        verbose_name_plural = 'CityMinSubPlans'
