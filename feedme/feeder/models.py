from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    zip_code = models.IntegerField()
    rating = models.IntegerField()
    categories = models.CharField(max_length=100)

class Feedme_Users(models.Model):
 	username = models.CharField(max_length= 100)
 	email = models.CharField(max_length=20)




