from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

from .models import Profile, Post, Like
from .forms import PostForm, ProfileForm, RegisterForm, LikeForm

from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

from  django.views import View



# Create your views here.
def home(request): # ok

    posts = Post.objects.filter(status='active')
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)


def about(request): # ok
    return render(request, 'about.html')


def register(request): # ok
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def profile(request): # ok

    if not request.user.is_authenticated:
        return redirect('login')

    posts = Post.objects.filter(user = request.user.id)
    try:
        profile = Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
        profile = None
    
    context = {
        'posts': posts,
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def profileadd(request): # ok

    if not request.user.is_authenticated:
        return redirect('login')    

    form = ProfileForm()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        # id otomatik olarak buradan yüklenir
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.user = User.objects.get(pk=request.user.id)

        if form.is_valid():
            
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'profileadd.html', context)


def profileupdate(request): # ok
    if not request.user.is_authenticated:
        return redirect('login')

    user = Profile.objects.get(user = request.user.id)
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('profile')

    context = {
        'form': form,
    }
    return render(request, 'profileupdate.html', context)


def postadd(request): # ok
    if not request.user.is_authenticated:
        return redirect('login')

    form = PostForm()

    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)

        # id otomatik olarak buradan yüklenir
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.user = User.objects.get(pk=request.user.id)

        if(form.is_valid()):
            form.save()
            return redirect('profile')
            
    context = {
        'form': form,
    }
    return render(request, 'postadd.html', context)


def postupdate(request, id): # ok
    if not request.user.is_authenticated:
        return redirect('login')

    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'postupdate.html', context)


def postdelete(request, id): # ok
    if not request.user.is_authenticated:
        return redirect('login')

    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'postdelete.html', context)



# Action views
def like(request, id):
    
    if request.user.is_authenticated:
        
        user = User.objects.get(id=request.user.id)
        post = Post.objects.get(id=id)
        b1 = Like(user=user, posts=post)

        instance = Like.objects.filter(user=b1.user, posts=b1.posts)
        # print(instance)

        if instance:
            instance.delete()
        else:
            b1.save()
            # print("saved")
    
    return redirect('home')


def postdetail(request, slug):

    post = Post.objects.get(slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'postdetail.html', context)