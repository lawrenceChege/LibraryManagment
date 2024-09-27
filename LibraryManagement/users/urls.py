from django.urls import re_path, include
from users.views import dashboard, register


urlpatterns = [
    re_path(r"^users/", include("django.contrib.auth.urls")),
    re_path(r"dashboard/", dashboard, name="dashboard"),    
    re_path(r"register/", register, name="register"),
]