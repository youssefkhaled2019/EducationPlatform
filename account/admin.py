from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import InstructorProfile
# Register your models here.
# admin.site.register(InstructorProfile)


admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in User._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields

admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Group._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields


@admin.register(InstructorProfile)
class ContentAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in InstructorProfile._meta.fields]  #+["id"]                   #SHOW ALL FILDES
    list_display=all_fields