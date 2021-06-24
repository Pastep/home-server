from django.urls import path
from .views import *
app_name = "accounts"

urlpatterns = [
    path('login', login.as_view(), name="login"),
    path('register', register.as_view(), name="register"),
    path('logout', logout.as_view(), name="logout"),
    path('clientarea', clientArea.as_view(), name="clientarea")
]