from _ast import expr

from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from django.contrib import auth
import config

# Create your views here.

class login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('files:list'))
        else:
            return render(request, 'accounts/login.html')

    def post(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('main:home'))

        if 'email' in request.POST:
            users = User.objects.all()
            for user in users:
                if user.email.lower() == request.POST['email'].lower():
                    if auth.authenticate(request, username=user.username, password=request.POST['password']):
                        auth.login(request, user)
                        return HttpResponseRedirect(reverse('main:home'))
                    return render(request, 'accounts/login.html', {'error': 'password is incorrect'})
            return render(request, 'accounts/login.html', {'error': 'email is incorrect'})
        elif 'username' in request.POST:
            users = User.objects.all()
            for user in users:
                if user.username.lower() == request.POST['username'].lower():
                    if auth.authenticate(request, username=user.username, password=request.POST['password']):
                        auth.login(request, user)
                        return HttpResponseRedirect(reverse('main:home'))
                    return render(request, 'accounts/login.html', {'error': 'password is incorrect'})
            return render(request, 'accounts/login.html', {'error': 'username is incorrect'})

class register(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('files:list'))

        return render(request, 'accounts/register.html')

    def post(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('files:list'))

        try:
            userObject = User(
                username=request.POST['username'],
                email=request.POST['email']
            )
            userObject.set_password(request.POST['password'])
            userObject.save()
            return HttpResponseRedirect(reverse('accounts:login'))
        except:
            return render(request, 'accounts/register.html', {
                'error': "Email/Username is already used before."
            })
class logout(View):

    def get(self, request):
        if request.user.is_authenticated:
            auth.logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))


class clientArea(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'accounts/clientarea.html')
        return HttpResponseRedirect(reverse('accounts:login'))

    def post(self, request):
        if request.user.is_authenticated:
            try:
                request.user.username = request.POST['username']
                request.user.email = request.POST['email']
                if request.FILES:
                    for extension in config.extensions['photo']:
                        if extension in str(request.FILES['avatar']):
                            request.user.avatar = request.FILES['avatar']
                            break
                if request.POST['password']:
                    request.user.set_password(request.POST['password'])
                request.user.save()
                return render(request, 'accounts/clientarea.html', {
                    'success': 'Account updated.'
                })
            except:
                return render(request, 'accounts/clientarea.html', {
                    'error': "Email or username is already used."
                })
        return HttpResponseRedirect(reverse('accounts:login'))