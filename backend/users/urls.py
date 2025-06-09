from django.urls import path
from .views import UserInfoview, UserRegistrationView

urlpatterns = [
    path("user-info/", UserInfoview.as_view(), name="user-info"),
    path("register/", UserRegistrationView.as_view(), name="register-user" )
]
