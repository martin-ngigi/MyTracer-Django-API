from django.db import models

# Create your models here.
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    backup_phone = models.CharField(max_length=20)
    registeredDate = models.DateTimeField(auto_now_add=True, blank=True)
    userLocationID = models.IntegerField(blank=True, null=True) #This id will intially be blank, but registering the user location details, it will be updated


    def __str__(self):
        return self.first_name+' '+self.last_name
