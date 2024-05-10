from django.db import models

# Create your models here.


class DocumentTypes(models.Model):
    DcType_name = models.CharField(max_length=255)

    def __str__(self):
        return self.DcType_name

    class Meta:
        db_table = 'documentTypes'
        verbose_name_plural = 'DocumentTypes'


class ElectronicFond(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    content = models.CharField(max_length=255)
    description = models.FileField(upload_to='media/files/')
    types = models.ForeignKey(DocumentTypes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'electronicFond'
        verbose_name_plural = 'ElectronicFond'
