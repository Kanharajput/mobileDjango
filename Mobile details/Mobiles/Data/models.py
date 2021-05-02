from django.db import models

# Create your models here.

class Info(models.Model):
    phone_img = models.ImageField(upload_to='pics')
    Name = models.CharField(max_length=70)
    RAM = models.IntegerField(default= None)
    ROM = models.IntegerField(default= None)
    Cost = models.IntegerField(default= None)
    Link = models.URLField(max_length=250)
    para1 = models.CharField(max_length=400)
    para2 = models.CharField(max_length=400)
    para3 = models.CharField(max_length=400)
    para4 = models.CharField(max_length=400)
    para5 = models.CharField(max_length=400)
    para6 = models.CharField(max_length=400)
    para7 = models.CharField(max_length=500)

    def __str__(self):
        return self.Name;

   
