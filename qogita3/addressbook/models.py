from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    street_name = models.CharField(max_length=200)
    house_number = models.IntegerField()
    zip_code = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
      return self.street_name + ' ' + str(self.house_number) + ' ' + self.zip_code

    #User will not be able to add a duplicated address to their account
    class Meta:
        unique_together = ('street_name','house_number','zip_code')