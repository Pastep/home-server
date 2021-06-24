from django.contrib import admin
from .models import User

# Register your models here.

def register(models: list):
    for model in models:
        admin.site.register(model)

register([User])