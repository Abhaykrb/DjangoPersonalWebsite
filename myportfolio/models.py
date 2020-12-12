from django.db import models
# Create your models here.
class Projects(models.Model):   
    title=models.CharField(max_length=50)
    topicc=models.CharField(max_length=50)
    about=models.CharField(max_length=150)
    img=models.ImageField(upload_to='myportfolio')

class Meta:
        verbose_name_plural = "Project"
        db_table = 'myportfolio_db'

class contact(models.Model):   
     firstname= models.CharField(max_length=50)
     lastname= models.CharField(max_length=50)
     email= models.EmailField(max_length=50)
     message=models.TextField()

