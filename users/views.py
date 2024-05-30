from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .pforms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
from news.models import Headline
def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    profile = request.user.profile  
    saved_news = profile.saved_news.all()  

    context = {
        'user': request.user,
        'saved_news': saved_news,
    }
    return render(request, 'users/profile.html', context)

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, 'users/profile_update.html', context)


@login_required
def save_news(request, news_id):
    news = get_object_or_404(Headline, id=news_id)
    profile = request.user.profile
    profile.saved_news.add(news)
    messages.success(request, 'News article saved to your profile!')
    return redirect('profile')  

@login_required
def remove_news(request, news_id):
    news = get_object_or_404(Headline, id=news_id)
    profile = request.user.profile
    profile.saved_news.remove(news)
    messages.success(request, 'News article removed from your profile!')
    return redirect('profile')




