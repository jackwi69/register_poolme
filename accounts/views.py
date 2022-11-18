from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from . forms import UserRegistrationForm
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f'user: {user}')
            login(request, user)
            return HttpResponseRedirect(reverse('todoapp:index'))
        else:
            messages.error(request, 'Bad uername or password')

    return render(request, 'accounts/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('todoapp:index'))


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            # password = form.cleaned_data["password2"]
            print(form.cleaned_data)
            user = User.objects.create_user(username=username, email=email, password=password)
            print(user)
            messages.success(request, 'Thanks for registering {}'.format(user.username))
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)
