from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Todo
from django.contrib import messages
import requests

# Create your views here.


def home(request):
    if 'username' in request.session:
        username = request.session['username']
        items = Todo.objects.filter(username=username)
        context = {'items': items, 'username': username}
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')


def weather(request):
    if request.method == 'POST':
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5875d3887f5a4cbd863d58dd375a6818'
        city = request.POST['city']

        r = requests.get(url.format(city)).json()
        print(r)

        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        return render(request, 'weather.html', city_weather)
    else:
        return render(request, 'weather.html')


def edit(request, pk):
    task = Todo.objects.get(id=pk)
    context = {'item': task}
    return render(request, 'edit.html', context)


def update_task(request, pk):
    item = request.POST['item']
    if 'completed' in request.POST:
        Todo.objects.filter(id=pk).update(item=item, complete=True)
    else:
        Todo.objects.filter(id=pk).update(item=item, complete=False)
    return redirect('/')


def delete(request, pk):
    item = Todo.objects.get(id=pk)
    item.delete()
    return redirect('/')


def login_page(request):
    return render(request, 'login.html')


def signup_page(request):
    return render(request, 'signup.html')


def add_item(request, pk):
    if request.POST['item'] == '':
        return redirect('/')
    else:
        user = User.objects.get(id=pk)
        username = user.username
        item = request.POST['item']
        task = Todo(username=username, item=item)
        task.save()
        return redirect('/')


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    if User.objects.filter(username=username).exists():
        messages.info(request, 'Username taken')
        return render(request, 'signup.html')
    if User.objects.filter(email=email).exists():
        messages.info(request, 'Email Id already Exists')
        return render(request, 'signup.html')
    else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        request.session['username'] = username
        return redirect('/')


def login(request):
    username = request.GET['username']
    password = request.GET['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        request.session['username'] = username
        return redirect('/')
    else:
        messages.info(request, 'Invalid Username or Password')
        return render(request, 'login.html')


def logout(request):
    del request.session['username']
    auth.logout(request)
    return redirect('/')
