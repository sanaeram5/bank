from django.db import models

# Create your models here.
class Bank(models.Model):
    account_number=models.CharField(max_length=18)
    IFSCCode=models.CharField(max_length=11)
    city=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    name_of_bank=models.CharField(max_length=100)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username