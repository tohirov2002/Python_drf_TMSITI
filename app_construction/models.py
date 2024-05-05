from django.db import models

# Create your models here.


class NewsModel(models.Model):
    news_name = models.CharField(max_length=255)
    news_content = models.CharField(max_length=255)
    news_description = models.CharField(max_length=255)
    news_image = models.ImageField(upload_to='images/', default=1)
    news_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_name

    class Meta:
        db_table = 'news'
        verbose_name_plural = 'News'


class AdsModel(models.Model):
    ads_name = models.CharField(max_length=255)
    ads_description = models.CharField(max_length=255)
    ads_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ads_name

    class Meta:
        db_table = 'ads'
        verbose_name_plural = 'Ads'
