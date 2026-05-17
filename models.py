from django.db import models
from anonymous .models import user_master

# Create your models here.
class profile_master(models.Model):
    email=models.ForeignKey(user_master,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Image/')
    document=models.FileField(upload_to='Document/')