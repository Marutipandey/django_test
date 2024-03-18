from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  
    mobile = models.CharField(max_length=15)   
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    MARITAL_STATUS_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    )
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    education = models.BooleanField(default=False) 
    dob = models.DateField()
    age = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')  
    description = models.TextField() 
