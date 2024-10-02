from django.urls import re_path, include
from library.views import transactions
from users.views import dashboard, register


urlpatterns = [
    re_path(r"^users/", include("django.contrib.auth.urls")),
    re_path(r"dashboard/", transactions, name="dashboard"),    
    re_path(r"register/", register, name="register"),
]