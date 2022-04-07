from django.db import models

# Create your models here.

class Lead(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField(null=True, blank=True, max_length=50)
    contact = models.IntegerField(null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="profiles/", default="profiles/user-default.png")

    def __str__(self):
        return self.name

