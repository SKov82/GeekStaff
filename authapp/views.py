from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import MyUserCreationForm


class SignUp(CreateView):
    """ Регистрация нового пользователя """
    form_class = MyUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('authapp:login')


class Login(UserPassesTestMixin, LoginView):
    """ Логин и редирект в зависимости от роли """
    def test_func(self):
        return not self.request.user.is_authenticated

    def get_success_url(self):
        if self.request.user.role == 'HR':
            url = f'/company/{self.request.user.pk}/profile/'
        elif self.request.user.role == 'REC' and not self.request.user.is_staff:
            url = f'/applicant/{self.request.user.pk}/profile/'
        else:
            url = '/'
        return url


class Logout(LoginRequiredMixin, LogoutView):
    """ Выход из системы """
    def get_next_page(self):
        return super().get_next_page()


def forget_pass(request):
    return render(request, 'authapp/user-forget-pass.html')
