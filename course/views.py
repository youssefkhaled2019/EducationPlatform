from django.shortcuts import render,get_object_or_404,redirect
from .models import Subject,Course,Content
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CourseForm , TextForm, FileForm, ImageForm, VideoForm, ModuleForm
from django.contrib import messages
# Create your views here.

# def index(request):
#    return render(request,"x.html")
def subject_courses_list(request):
   subjects=Subject.objects.prefetch_related("courses").all()
   course=Course.objects.order_by("-num_enroll").all()[:10]
#    print(subjects)
   return render(request,"course/subject_course_list.html",{"subjects":subjects,"course":course})



def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if(request.user.is_authenticated ):
        test_enroll= Course.objects.filter(students=request.user,title=course.title).exists()
    else:
        test_enroll=True

    print("gggg",test_enroll)
    context = {
        'detail':course,
        "test_enroll":test_enroll

    }
    return render(request, 'course/course_detail.html', context)

# @login_required
@login_required(login_url='account:sign_up')
@permission_required('course.add_course', raise_exception=True)  #Course|course|Can add course
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


@login_required
def edit_course(request, slug):
    course = get_object_or_404(Course, slug=slug, owner=request.user)
    form = CourseForm(instance=course)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            try:
                 form.save() 
            except :    
                    print("error")
                    messages.error(request, " error:title is must uniqe")
                    return redirect(request.path)
           
            return redirect('account:view-profile')
        # else:
        #         for error in form.errors:
        #             messages.error(request, sign_in_form.errors[error])
        #         return redirect("course/edit_coures.html")        

    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'course/edit_coures.html', context)

@login_required 
@permission_required(['course.add_module',], raise_exception=True)
def add_module(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = form.save(commit=False)
            module.course = course
            module.save()
            return redirect('course:course_detail', slug=course.slug)
    else:
        form = ModuleForm()    
    context = {
        'form':form,
        'course':course
    }
    return render(request, 'course/add_module.html', context)    



def enroll_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.user.is_authenticated:
        course.students.add(request.user)
        course.num_enroll+=1
        course.save()    
        messages.success(request, 'You have successfully enrolled in the course.')
        return redirect('course:course_detail', slug=course.slug)

    return redirect('accounts:sign_in')    