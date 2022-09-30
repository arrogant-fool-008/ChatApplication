import imp
from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import context
from django.template import loader
from .forms import RegistrationForm 



# Create your views here.
def registration(request):
    if request.user.is_authenticated:
        return redirect('Welcome')
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            u = User( username = form.cleaned_data.get('username'), first_name = form.cleaned_data.get('first_name'), last_name = form.cleaned_data.get('last_name'),
            email = form.cleaned_data.get('email'), password = form.cleaned_data.get('password1'))
            u.save()
            # form.save()
            user = form.cleaned_data.get('username')
            msg_str = "Whoaaa...Congratulations " +str(user) + "!! You are in."
            messages.success(request, msg_str)

    context = {'form': form}
    template = loader.get_template('registration/registration.html')
    return render(request, 'registration/registration.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('Message:Welcome')
    if request.method == "POST":
        user_name = request.POST.get('username')
        paswd = request.POST.get('password')
        user = authenticate(username = user_name, password = paswd)

        if user is not None:
            login(request, user)
            return redirect('Message:index')
        else:
            messages.error(request, "oops... Either username or Password is wrong!!")
            # return render(request, 'registration/login.html', context= {})

    return render(request, 'registration/login.html', context= {})

@login_required(login_url='Login')
def logOutUser(request):
    logout(request)
    return redirect('Login')

# @login_required(login_url='Login')
# def welcome(request):
#     return render(request, 'registration/welcome.html', context= {})