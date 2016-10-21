from django.shortcuts import render, HttpResponse, redirect
from .models import User, Item
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "belt_exam/index.html")


def create(request):
    result = User.objects.register(request.POST)
    if result[0] == True:
        return render(request, "belt_exam/wall.html")
    else:
        for message in result[1]:
            messages.add_message(request, messages.INFO, message)
        return redirect('/')

def login(request):
    result = User.objects.login(request.POST)
    if result[0] == True:
        return render(request, 'belt_exam/wall.html')
    else:
        for message in result[1]:
            messages.add_message(request, messages.INFO, message)
        return redirect('/')


def login_success(request, user):
    request.session['user'] = {
    'id': user.id,
    "name": user.name,
    "user_name": user.user_name,
    "date": user.date
    }
    return render (request, "belt_exam/wall.html")

def result(request):

    return render(request, 'belt_exam/wall.html')

def add(request):
    context = {
    "item" : Item.objects.all()
    }
    return render(request, "belt_exam/add.html", context)

def items(request):
    return redirect('/result')
