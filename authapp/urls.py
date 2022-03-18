from django.urls import path

from .views import SignUp, Login, Logout, forget_pass


app_name = 'authapp'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('forget-pass/', forget_pass, name='forget-pass'),
]
