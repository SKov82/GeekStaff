from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    """ Форма для регистрации пользователя """
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('role', 'email',)

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
