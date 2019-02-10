from django.db import models

# Create your models here.

class Stocks(models.Model):

    ticker=models.CharField(max_length=50)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()


    def __str__(self):
        return self.ticker


