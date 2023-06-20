from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ChangeStaffStatusForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url="/login/")
def home(request):
    return render(request, 'core/home.html', {})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'core/signup.html', {'form':form})

@login_required(login_url="/login/")
def profiles(request):
    profiles = User.objects.exclude(username=request.user)
    return render(request, 'core/profiles.html', {"profiles":profiles})

@login_required(login_url="/login/")
def change_staff_status(request):
    if request.method == 'POST':
        form = ChangeStaffStatusForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            is_staff = form.cleaned_data['is_staff']
            
            user.is_staff = is_staff
            user.save()
            
            return redirect('profiles')  # Redirect to a success page
    else:
        form = ChangeStaffStatusForm()

    return render(request, 'core/change_staff_status.html', {'form': form})
