from django.contrib import admin

from .models import Company, Job


class JobInline(admin.TabularInline):
    """ Отрисовка списка вакансий внутри профиля компании """
    model = Job
    fk_name = 'company'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Поля таблицы Компания в админке + вакансии
    """
    list_display = ('id', 'name', 'status', 'location', 'link',
                    'created_at', 'updated_at', 'views_count',)
    inlines = (JobInline,)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """
    Поля таблицы Вакансии в админке
    """
    list_display = ('id', 'company', 'status', 'grade', 'category', 'salary', 'city', 'employment',
                    'work_schedule', 'experience', 'created_at', 'updated_at', 'views_count',)
