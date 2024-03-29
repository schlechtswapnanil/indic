from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
from blog.models import Post
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'                    Account created for {username}. Login with your credentials now.')
            return redirect('login')
        else:
            messages.error(request, f'Incompatible inputs ! Read the Instructions carefully and re-enter !')

    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
    
@login_required
def profile(request):
    posts=[]
    posts=Post.objects.filter(author=request.user)
    context={
        "posts": posts,
    }
    return render(request, 'users/profile.html',context=context)



def profileupdate(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated !')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile)
    context={
        "u_form": u_form,
        "p_form": p_form
        }
    return render(request, 'users/profileupdate.html',context=context)


