from django.db import models, transaction
from django.urls import reverse_lazy

from authapp.models import MyUser


class Company(models.Model):
    """
    Компания-работодатель
    """
    def user_directory_path(instance, filename):
        return f'logo/user_{instance.user.id}/{filename}'

    STATUS = (
        ('0', 'Отклонена модератором'),
        ('1', 'Заготовка'),
        ('2', 'На модерации'),
        ('3', 'Опубликована'),
        ('4', 'Черновик'),
        ('9', 'Удалена'),
    )

    user = models.OneToOneField(to=MyUser, on_delete=models.PROTECT, related_name='company', verbose_name="Пользователь")
    name = models.CharField('Наименование компании', max_length=255, blank=False, db_index=True)
    status = models.CharField('Статус', max_length=1, choices=STATUS, default='1', db_index=True)
    logo = models.ImageField('Логотип', upload_to=user_directory_path, blank=True, null=True)
    headline = models.CharField('Слоган', max_length=255, blank=True)
    short_description = models.CharField('Краткое описание', max_length=255, blank=False)
    detail = models.TextField('Подробное описание', blank=True)
    location = models.CharField('Местонахождение', max_length=255, blank=False, db_index=True)
    link = models.CharField('Ссылка на сайт / соц.сеть', max_length=255, blank=True)
    moder_comment = models.TextField('Заключение модератора', blank=False, default='Комментарий: ')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    views_count = models.PositiveIntegerField('Число просмотров', default=0)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def views_counter(self):
        """ Счетчик просмотров карточки компании """
        if Company.objects.filter(pk=self).exists():
            with transaction.atomic():
                self = Company.objects.get(id=self)
                self.views_count += 1
                self.save()


def create(instance):
    """
    Создание заготовки компании по сигналу вновь зарегистрированного работодателя
    """
    Company.objects.create(user=instance,)


class Job(models.Model):
    """
    Вакансии
    """
    STATUS = (
        ('0', 'Отклонена модератором'),
        ('1', 'Заготовка'),
        ('2', 'На модерации'),
        ('3', 'Опубликована'),
        ('4', 'Черновик'),
        ('5', 'Скрыта'),
        ('6', 'Закрыта'),
        ('9', 'Удалена'),
    )

    GRADE = (
        ('NO', ''),
        ('TR', 'Trainee'),
        ('JR', 'Junior'),
        ('MD', 'Middle'),
        ('SR', 'Senior'),
        ('TL', 'TeamLead'),
        ('TD', 'CTO'),
    )

    CATEGORY = (
        ('NO', ''),
        ('FLS', 'Full Stack'),
        ('FED', 'Front-end'),
        ('BED', 'Back-end'),
        ('SW', 'Software'),
        ('AI', 'AI & ML'),
        ('BD', 'Big Data'),
        ('AND', 'Android'),
        ('IOS', 'iOS'),
        ('IOT', 'IoT'),
        ('QA', 'QA Engineer'),
        ('GD', 'GameDev'),
        ('PJM', 'Project Manager'),
        ('PDM', 'Product Manager'),
    )

    EMPLOYMENT = (
        ('FT', 'Полная занятость'),
        ('PT', 'Частичная занятость'),
        ('PW', 'Проектная работа'),
        ('VL', 'Волонтерство'),
        ('WP', 'Стажировка'),
    )

    WORK_SCHEDULE = (
        ('FD', 'Полный день'),
        ('SSCH', 'Сменный график'),
        ('FSCH', 'Гибкий график'),
        ('RW', 'Удаленная работа'),
        ('RBW', 'Вахтовый метод'),
    )

    EXPERIENCE = (
        ('WE', 'Без опыта'),
        ('SM', 'До 1 года'),
        ('MD', '1-3 года'),
        ('BG', 'Более 3 лет'),
    )

    company = models.ForeignKey(to=Company, on_delete=models.PROTECT, related_name='jobs', verbose_name='Компания')
    status = models.CharField('Статус', max_length=1, choices=STATUS, default='1', db_index=True)
    grade = models.CharField('Классность', max_length=2, choices=GRADE, default='NO', db_index=True)
    category = models.CharField('Категория', max_length=3, choices=CATEGORY, default='NO', db_index=True)
    salary = models.PositiveIntegerField('Зарплата', null=True, blank=True, db_index=True)
    city = models.CharField('Город', max_length=255, blank=False, db_index=True)
    employment = models.CharField('Тип занятости', max_length=2, choices=EMPLOYMENT, default='FT', db_index=True)
    work_schedule = models.CharField('График работы', max_length=4, choices=WORK_SCHEDULE, default='FD', db_index=True)
    experience = models.CharField('Опыт работы', max_length=2, choices=EXPERIENCE, default='WE', db_index=True)
    short_description = models.CharField('Краткое описание', max_length=255, blank=False)
    description = models.TextField('Подробное описание', blank=True, null=True)
    skills = models.CharField('Навыки', max_length=255, blank=True)
    moder_comment = models.TextField('Заключение модератора', blank=False, default='Комментарий: ')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    views_count = models.PositiveIntegerField('Число просмотров', default=0)

    class Meta:
        ordering = ('status', '-created_at',)
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __repr__(self):
        dev, category = (
            'Разработчик', self.get_category_display()
        ) if self.grade not in ['TL', 'TD'] else ('', '')
        grade = self.get_grade_display()
        return f'{grade} {category} {dev}'

    def __str__(self):
        dev, category = (
            'Разработчик', self.get_category_display()
        ) if self.grade not in ['TL', 'TD'] else ('', '')
        grade = self.get_grade_display()
        return f'{grade} {category} {dev}'

    def get_absolute_url(self):
        return reverse_lazy('companyapp:profile', args=[self.company.pk])

    def change_status(self, status):
        """ Смена статуса вакансии """
        with transaction.atomic():
            self = Job.objects.get(id=self)
            self.status = status
            self.save()
