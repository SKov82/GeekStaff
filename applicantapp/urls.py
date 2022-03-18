"""
Urls for applicant
"""
from django.urls import path

from applicantapp.views import ProfileView, ResumeList, CreateResume, UpdateResume


app_name = 'applicantapp'

urlpatterns = [
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    # path('resume-list', ResumeList.as_view(), name='resume-list'),
    path('createresume', CreateResume.as_view(), name='createresume'),
    path('resume-list', ProfileView.as_view(), name='resume-list'),
    path('resumes-list/update_resume/<int:pk>/', UpdateResume.as_view(), name='update_resume'),
]
