from django.urls import path
from .views import *

app_name = "files"

urlpatterns = [
    path('upload', upload.as_view(), name="upload"),
    path('list', list.as_view(), name="list"),
    path('delete', delete.as_view(), name="delete"),
    path('view/<int:id>', view.as_view(), name="view")
]