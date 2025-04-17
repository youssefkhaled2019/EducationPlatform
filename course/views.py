from django.shortcuts import render,get_object_or_404
from .models import Subject,Course,Content
# Create your views here.

# def index(request):
#    return render(request,"x.html")
def subject_courses_list(request):
   subjects=Subject.objects.prefetch_related("courses").all()
#    print(subjects)
   return render(request,"course/subject_course_list.html",{"subjects":subjects})



def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'detail':course,
    }
    return render(request, 'course/course_detail.html', context)