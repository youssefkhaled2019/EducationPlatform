from django import forms
from .models import Course, Text, Video, Image, File, Module





class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['subject', 'title',"img1",'overview', 'status']



class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module  
        fields = ['title', 'description']      
        
        
        
class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['text']        
        

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']        


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']        


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video']        
                                
        
        
        
        

