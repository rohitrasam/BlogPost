from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Post, Likes
from datetime import datetime as dt
# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        password1 = request.POST['password1']

        user = User.objects.create_user(username, email, password1)
        user.first_name = f_name
        user.last_name = l_name
        user.save()

        messages.success(request, "Account creaetd successfully")
        return redirect('/login')

    return render(request, 'signup.html')


def user_login(request: HttpRequest):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')
    return render(request, 'login.html')

def main(request: HttpRequest):
    
    posts = Post.objects.filter(status=1)

    return render(request, 'main.html', {'posts':posts})

def signout(request):
    pass




def open_blog(request: HttpRequest, id:int):
    post = Post.objects.get(pk=id)
    return render(request, 'blogs.html', {'post': post})


def create_blog(request: HttpRequest, user_id: int):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        draft =  request.POST.get('isDraft', False)
        
        if draft:
            post = Post(title=title, content=content, author=User.objects.get(pk=user_id))
        else:
            post = Post(title=title, content=content, author=User.objects.get(pk=user_id), status=1, published_date=dt.isoformat(dt.now()))
        post.save()
        return redirect('main')

    return render(request, 'create_blog.html')


def edit_blog(request: HttpRequest, blog_id: int):
    post = Post.objects.get(pk=blog_id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        draft = request.POST.get('isDraft', False)
        if draft:
            post.status = 0
        else:
            post.status = 1
            post.published_date =  dt.isoformat(dt.now()) if not post.published_date else post.published_date
        post.save()
        return redirect('main')

    return render(request, 'create_blog.html', {'post':post, 'isEdit': True})


def drafts(request: HttpRequest, user_id: int):

    user = User.objects.get(pk=user_id)
    posts = user.blogs.filter(status=0)

    return render(request, 'drafts.html', {'posts': posts})