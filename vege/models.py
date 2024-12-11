from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class Reciepe (models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null = True ,blank = True)
    Reciepe_name=models.CharField(max_length=100)
    Reciepe_description=models.TextField()
    Reciepe_image=models.ImageField(upload_to="reciepe")

