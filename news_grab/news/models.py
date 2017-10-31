from django.db import models

# Create your models here.

class News(models.Model):

    uni_id = models.CharField(max_length=64)
    news_source = models.CharField(max_length=32, default='undefined')
    title = models.CharField(max_length=256, default='undefined')
    url = models.CharField(max_length=256)
    pub_time = models.DateTimeField()

    class Meta:
        ordering = ('-pub_time',)

class KeyWordList(models.Model):

    keyword = models.CharField(max_length=32)
    power = models.FloatField(max_length=16)

    class Meta:
        ordering = ('-power',)

class News_Source(models.Model):

    News_Source = models.CharField(max_length=32)