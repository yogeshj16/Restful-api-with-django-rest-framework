from django.db import models


class employees(models.Model):
    firstName=models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstName

# Create your models here.
