from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def sign_up(request):
    
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # InstructorProfile.objects.create(user=user)
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
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