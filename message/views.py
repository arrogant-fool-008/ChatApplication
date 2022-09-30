from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='Login')
def welcome(request):
    return render(request, 'message/welcome.html', context= {})

@login_required(login_url='Login')
def index(request):
    return render(request, 'message/room2.html', {})

@login_required(login_url='Login')
def room(request, room_name):
    u = User.objects.get(username = request.user)
    name = str(u.first_name) + " "+ str(u.last_name)
    print(name)
   
    # un = User.objects.all()
    # print(un.all)
    
    return render(request, 'message/room.html', {
        'room_name': room_name,
        'user_name': str(name) 
        
    })

