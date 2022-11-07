from django.urls import path
from user_profile.views import profile_view, login_view, logout_view, register_view


urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
]