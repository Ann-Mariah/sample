from django.db import models


class student(models.Model):
    student_fname= models.CharField(max_length=100,null=True)
    student_lname= models.CharField(max_length=100,null=True)
    age= models.IntegerField()
   
    gender= models.CharField(max_length=10,null=True)
    qualification= models.CharField(max_length=100,null=True)
    image= models.ImageField(blank=True,upload_to="image/",default='static/images/icon.png', null=True)

# Create your models here.
