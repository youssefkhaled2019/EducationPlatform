from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from .models import InstructorProfile
from .forms import InstructorProfileForm
from course.models import Course
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  Group
# Create your views here.

def sign_up(request):
    
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            InstructorProfile.objects.create(user=user,jop=form.cleaned_data.get('role'))
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # ===================================
            role=form.cleaned_data.get('role')
            print("ffff",role)
            group = Group.objects.get(name__icontains=role)
            user.groups.add(group)
            # ==========================
            # Group.objects.get(name__icontains="Instructor")
            # ===================================
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('course:subject_courses_list')#account:view-profile

    context = {
        'form':form
    }
    return render(request, 'account/sign_up.html', context)

def sign_out(request):
    logout(request)
    return redirect('account:sign_in')

def sign_in(request):
    ERROR = None
    if request.user.is_authenticated:
        return redirect('course:subject_courses_list')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('course:subject_courses_list')
        else:
            ERROR = 'Invalid credentials!, Password or username is invalid!'
    
    
    context = {
        'error':ERROR
    }        
    
    return render(request, 'account/sing_in.html', context)



@login_required(login_url='account:sign_up')
def view_profile(request):
 


    try:
        profile = get_object_or_404(InstructorProfile, user=request.user)
        courses = Course.objects.filter(owner=request.user)
    except :
       profile=InstructorProfile.objects.create(user=request.user)
       courses = Course.objects.filter(owner=request.user)


    context = {
        'profile':profile,
        'courses': courses,
    }
    return render(request, 'account/view_profile.html', context)


@login_required(login_url='account:sign_up')
def edit_profile(request):
    profile = get_object_or_404(InstructorProfile, user=request.user)
    form = InstructorProfileForm(instance=profile)
    if request.method == 'POST':
        form = InstructorProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account:view-profile')
    
    context = {
        'form': form,
    }
    return render(request, 'account/edit_profile.html', context)
