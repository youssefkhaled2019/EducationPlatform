from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class InstructorProfile(models.Model):

    class type(models.TextChoices):
        student='student','Student'
        instructor='instructor','Instructor'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio  = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='instructors/photos', blank=True, null=True,default="43790986.jpg")
    contact_email = models.EmailField(blank=True, null=True)
    header = models.CharField(max_length=255, blank=True, null=True)
    jop=models.CharField(max_length=30 ,choices=type,default=type.student)
    
    
    
    def __str__(self) -> str:
        return str(f"Profile of {self.user.username}")
    

class SocialMediaAccounts(models.Model):
    user = models.OneToOneField(InstructorProfile, on_delete=models.CASCADE, related_name='socialmedia')
    linkedin = models.URLField(blank=True, null=True)
    github   = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)          