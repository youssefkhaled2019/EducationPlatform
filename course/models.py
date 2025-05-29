from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.utils.text import slugify

# Create your models here.
class Subject(models.Model): #categorías
    title=models.CharField(max_length=250)
    description=models.TextField(blank=True)
    slug=models.SlugField(max_length=250,unique=True)
    class Meta:
        ordering=["title"]
    def __str__(self):
        return self.title
    
class Course(models.Model): 
    class Status(models.TextChoices):
        AVAILABLE='AV','Avsilable'
        DEREFT='DF','Dreft'
    owner=models.ForeignKey(User,related_name="courses_created",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,related_name="courses",on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique=True)
    overview=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=2 ,choices=Status,default=Status.AVAILABLE)
    class Meta:
        ordering=["-created"]
    def __str__(self):
        return self.title        

        
    def save(self, *args, **kwargs):
        if not self.slug :#or self.title != Course.objects.get(pk=self.pk).title if self.pk else None
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)        



class Module(models.Model):
    course=models.ForeignKey(Course,related_name="modules",on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.title    
    
class Content(models.Model):
    module=models.ForeignKey(Module,related_name="contents",on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE,limit_choices_to={'model__in':('text','file','image','video')})
    objects_id=models.PositiveIntegerField()
    item=GenericForeignKey("content_type","objects_id")    


class ItemBase(models.Model):
    owner=models.ForeignKey(User,related_name="%(class)s_related",on_delete=models.CASCADE) 
    title=models.CharField(max_length=250) 
    creates=models.DateTimeField(auto_now_add=True)  
    update=models.DateTimeField(auto_now=True) 
    class Meta:
        abstract=True

    def __str__(self):
        return self.title     
    
class Text(ItemBase):
    text=models.TextField()      # https://stackoverflow.com/questions/40148630/understanding-django-genericforeignkey-and-genericrelation
    # relation= GenericRelation(Content, content_type_field='content_type', object_id_field='objects_id')
class File(ItemBase):
    file=models.FileField(upload_to="file")
class Image(ItemBase):
    image=models.ImageField(upload_to="images")
class Video(ItemBase):
    video=models.URLField()
    