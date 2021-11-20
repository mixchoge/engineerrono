from django.shortcuts import render, redirect
from .models import Respond, Message, Chat, Private
from django.contrib import messages
from django.contrib.auth.models import User, auth


def index(request):
    return render(request, 'index.html')


def me(request):
    return render(request, 'me.html')


def comment(request):
    responds = Respond.objects.all()
    return render(request, 'testi.html', {'responds': responds})


def commenting(request):
    if request.method == 'POST':
        new_comment = Respond()
        new_comment.img = request.FILES['img']
        new_comment.comment = request.POST['comment']
        new_comment.name = request.POST['name']
        new_comment.about = request.POST['about']
        new_comment.save()
        return redirect('comment')


def contact(request):
    if request.method == 'POST':
        new_message = Message()
        new_message.name = request.POST['name']
        new_message.email = request.POST['email']
        new_message.message = request.POST['message']
        new_message.save()
        messages.success(request, f"Message sent successfully!!")
        return redirect('index')


def chat(request):
    chats = Chat.objects.all()
    if request.method == 'POST':
        new_chat = Chat()
        new_chat.name = request.POST['name']
        new_chat.text = request.POST['text']
        new_chat.save()
        messages.success(request, f"Message sent successfully!!")
    return render(request, 'contact.html', {'chats': chats})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken!!')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email,
                                                password=password1)
                user.save()
                print('account successfully created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching....')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'invalid credentials!!!!')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def private(request):
    return render(request, 'private.html')


def texts(request):
    if request.method == 'POST':
        text = request.POST['text']
        new_message = Private.objects.create(
            user=request.user,
            text=text)
        new_message.save()
        message = Private.objects.filter(user=request.user)
        return render(request, 'private.html', {'message': message})
