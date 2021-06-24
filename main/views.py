from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from files.models import File
# Create your views here.

class home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'main/list.html', context={
                "files": File.objects.filter(public=True)
            })
        return HttpResponseRedirect(reverse('accounts:login'))