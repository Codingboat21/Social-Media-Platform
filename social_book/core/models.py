from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime 
User= get_user_model()
# Create your models here.
class Profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    id_user= models.IntegerField()
    bio=models.TextField(blank=True)
    profileimg= models.ImageField(upload_to="profile_images",default='Default_pfp.svg.png')
    location=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    caption= models.TextField()
    image= models.ImageField(upload_to='post_image')
    no_of_likes=models.IntegerField(default=0)
    created_at= models.DateField(default=datetime.now)

    def __str__(self):
        return self.user

class PImages(models.Model):
    title= models.CharField(max_length=200)
    image= models.ImageField(upload_to='P_Images')

    def __str__(self):
        return self.title
    
class postliker(models.Model):
    username=models.CharField(max_length=100)
    post_id= models.CharField(max_length=200)

    def __str__(self):
        return self.username    

class Follow_user(models.Model):
    follow =models.CharField(max_length=100)   
    user =models.CharField(max_length=100)

    def __str__(self):
        return self.user    
# class follow_user(models.Model):
#     follow= models.CharField(max_length=100)
#     user= models.CharField(max_length=100)

#     def __str__(self):
#         return self.user