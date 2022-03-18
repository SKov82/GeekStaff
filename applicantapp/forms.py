import django.forms as forms

from applicantapp.models import Resume


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Resume
        # fields = '__all__'
        exclude = ['user', 'is_cheked', 'moder_comment', 'created_at', 'updated_at', 'views_count',]

class ResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user', 'is_cheked', 'moder_comment']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'