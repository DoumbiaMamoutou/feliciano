from django.db import models

# Create your model

class Client(models.Model):
    ip = models.GenericIPAddressField()
    pays = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    reseau = models.CharField(max_length=50)
    page = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.ip 

