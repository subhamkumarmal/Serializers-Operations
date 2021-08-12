from django.db import models

# Create your models here.

class Course(models.Model):
    cname=models.CharField(max_length=30)
    cfees=models.IntegerField()
    cduration=models.CharField(max_length=30)

    def __str__(self):
        return self.cname

    class Meta:
        db_table='course'
