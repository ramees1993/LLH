from django.db import models
from django. views.generic import ListView

class Department(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_des=models.TextField()

    def __str__(self):
        return self.dep_name



class Doctor(models.Model):
    doc_name=models.CharField(max_length=25)
    doc_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors/')
    fb_url=models.URLField(max_length=255)
    twitter_url=models.URLField(max_length=255)
    insta_url=models.URLField(max_length=255)
    
    def __str__(self):
        return self.doc_name
    
class Booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booked=models.DateField()
    time=models.TimeField()
    desc=models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=35)
    Phone=models.CharField(max_length=15,blank=True,null=True)
    message=models.CharField(max_length=350)

    def __str__(self):
        return self.name
class Doctor1(models.Model):
    name=models.CharField(max_length=35)
    speciality=models.CharField(max_length=150)
    image=models.ImageField(upload_to='doctors/')
    fb=models.URLField(max_length=255)
    twitter=models.URLField(max_length=255)
    instagram=models.URLField(max_length=250)
    def __str__(self):
        return self.name

    

    





    
    






      



       


