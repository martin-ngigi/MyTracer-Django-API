from django.db import models

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

    def __str__(self):
        return self.first_name+' '+self.last_name


class Location(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=400)
    #NB: "user", "immunizations" must be the same as the one used in the serializers
    user = models.ForeignKey(User, related_name="locations", on_delete= models.CASCADE) #i.e  1

    class Meta:
        ordering = ("date", "time")
        def __str__(self):
            return self.latitude +' '+ self.longitude
