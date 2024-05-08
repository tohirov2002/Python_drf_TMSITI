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


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'


class Specialty(models.Model):
    sp_name = models.CharField(max_length=255)

    def __str__(self):
        return self.sp_name

    class Meta:
        db_table = 'specialty'
        verbose_name_plural = 'Specialty'


class Masters(models.Model):
    master_name = models.CharField(max_length=255)

    def __str__(self):
        return self.master_name

    class Meta:
        db_table = 'masters'
        verbose_name_plural = 'Masters'


class Leadership(models.Model):
    ld_name = models.CharField(max_length=255)
    ld_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ld_admission = models.CharField(max_length=255)
    ld_phone = models.CharField(max_length=255, default=1)
    ld_email = models.EmailField(unique=True, max_length=100)
    ld_image = models.ImageField(upload_to='images/', default=2)
    ld_bachelor = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    ld_masters = models.ForeignKey(Masters, on_delete=models.CASCADE)

    def __str__(self):
        return self.ld_name

    class Meta:
        db_table = 'leadership'
        verbose_name_plural = 'Leadership'


class ComponentCategory(models.Model):
    CnCategory_name = models.CharField(max_length=255)

    def __str__(self):
        return self.CnCategory_name

    class Meta:
        db_table = 'componentCategory'
        verbose_name_plural = 'componentCategories'


class Component(models.Model):
    cn_name = models.CharField(max_length=255)
    cn_category = models.ForeignKey(ComponentCategory, on_delete=models.CASCADE)
    cn_phone = models.CharField(max_length=255, default=1)
    cn_email = models.EmailField(unique=True, max_length=100)
    cn_image = models.ImageField(upload_to='images/', default=2)

    def __str__(self):
        return self.cn_name

    class Meta:
        db_table = 'component'
        verbose_name_plural = 'Components'


class Standards(models.Model):
    st_name = models.CharField(max_length=255)
    st_code = models.CharField(max_length=255)
    st_field = models.TextField(default=1)

    def __str__(self):
        return self.st_name

    class Meta:
        db_table = 'standards'
        verbose_name_plural = 'Standards'

