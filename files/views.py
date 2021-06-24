from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import File
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json, config

# Create your views here.

class upload(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('accounts:login'))

        return render(request, 'files/upload.html')

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('accounts:login'))
        fileObject = File(user=request.user, file=request.FILES['file'])
        if 'public' in request.POST:
            fileObject.public = True
        fileObject.save()
        return HttpResponseRedirect(reverse('files:list'))

class list(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('accounts:login'))
        context = {
            'files': File.objects.filter(user=request.user),
        }
        return render(request, 'files/list.html', context)

@method_decorator(csrf_exempt, name="dispatch")
class delete(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('accounts:login'))

        parameters = json.loads(request.body)
        files = File.objects.filter(id=parameters['id'])
        if files:
            files = files[0]
            if files.user == request.user:
                files.delete()
                return HttpResponse('successfully deleted')
            else:
                return HttpResponse("You're not author of this file.")
        else:
            return HttpResponse('not found')

class view(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('accounts:login'))
        files = File.objects.filter(id=id)
        if files:
            files = files[0]
            if files.user == request.user or files.public:
                return render(request, 'files/view.html', {
                    'file': files,
                })
            else:
                return HttpResponseRedirect(reverse('files:list'))