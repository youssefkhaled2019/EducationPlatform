from django.shortcuts import render,get_object_or_404,redirect
from .models import Subject,Course,Content
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CourseForm #, TextForm, FileForm, ImageForm, VideoForm, ModuleForm
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


# @login_required
# @permission_required('courese.can_add_course', raise_exception=True)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = request.user
            course.save()
            return redirect('course:subject_courses_list')
    else:
        form = CourseForm()    
    
    context = {
        'form':form
    }
    
    return render(request, 'course/add_course.html', context)
