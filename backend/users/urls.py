from django.urls import path
from .views import UserInfoview

urlpatterns = [
    path("user-info/", UserInfoview.as_view(), name="user-info")
]
