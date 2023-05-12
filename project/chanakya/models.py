from django.db import models

# Create your models here.
class Teacher(models.Model):
    image=models.ImageField(upload_to='images/')
    
class Event(models.Model):
    image=models.ImageField(upload_to='images/')
    
class Sport(models.Model):
    image=models.ImageField(upload_to='images/')
    
class Achievement(models.Model):
    image=models.ImageField(upload_to='images/')
  
JOB_CHOICES = (
    ('select','SELECT'),
    ('prt','PRT'),
    ('tgt', 'TGT'),
    ('other','OTHER'),
    
)
    
class Career(models.Model):
    Name = models.CharField( max_length=10)
    email = models.EmailField()
    phone = models.CharField(  max_length=10)
    post = models.CharField(max_length=20, choices=JOB_CHOICES, default='SELECT')
    resume = models.FileField(upload_to='files/')
    def __str__(self):
            return self.post
    
class Registration(models.Model):
        FirstName = models.CharField( max_length=10)
        LastName = models.CharField( max_length=10)
        email = models.EmailField()
        LastSchool = models.CharField(blank=True, max_length=30)
        FatherName = models.CharField( max_length=20)
        phone = models.CharField( max_length=10)
        Address = models.CharField( max_length=50)
        SiblingName = models.CharField(blank=True, max_length=20)
        Class = models.CharField(blank=True, max_length=10)
        def __str__(self):
            return self.FirstName   
        
class NoticeBoard(models.Model):
    title = models.CharField(max_length=100)
    message= models.TextField()
    def __str__(self):
            return self.title         