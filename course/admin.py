from django.contrib import admin
from .models import Subject,Course,Module ,Content,Text,File,Image,Video
# Register your models here.
@admin.register(Subject)
class SubjecAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Subject._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields
    prepopulated_fields = {'slug': ('title',)}

class ModuleInLine(admin.StackedInline):
    model=Module
    
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
   
    all_fields = [f.name for f in Module._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
     all_fields = [f.name for f in Course._meta.fields]  #+["id"]                   #SHOW ALL FILDES
     list_display=all_fields
     list_filter=["created"]
     search_fields=['title','overview']
     prepopulated_fields = {'slug': ('title',)}
     inlines=[ModuleInLine]
# admin.site.register(Course)



# ,Content,Text,File,Image,Video
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Content._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Text._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in File._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Image._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Video._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields