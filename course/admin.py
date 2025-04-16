from django.contrib import admin
from .models import Subject,Course,Module
# Register your models here.
@admin.register(Subject)
class SubjecAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Subject._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields
    prepopulated_fields = {'slug': ('title',)}

class ModuleInLine(admin.StackedInline):
    model=Module
    # all_fields = [f.name for f in Module._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    # list_display=all_fields
    
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
