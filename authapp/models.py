from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

import companyapp


class MyUserManager(BaseUserManager):
    def create_user(self, email, role=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role,
            **extra_fields
        )
        user.set_password(password)
        if role:
            extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password=password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователей
    """
    ROLE = (
        ('HR', 'Работодатель'),
        ('REC', 'Соискатель'),
    )

    role = models.CharField('Роль', max_length=3, choices=ROLE, default='REC', null=True, blank=False)
    email = models.EmailField('e-mail', blank=False, unique=True, max_length=64,
                              error_messages={'unique': "Ваш email уже занят!",})
    is_staff = models.BooleanField('Модератор', default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ('email',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


def create_company(instance, created, **kwargs):
    """
    После регистрации пользователя-работодателя,
    по сигналу, создается новая компания.
    """
    if created and instance.role == 'HR':
        companyapp.models.create(instance)


post_save.connect(create_company, sender=MyUser)
