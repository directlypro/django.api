from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class ChangeStaffStatusForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    is_staff = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(ChangeStaffStatusForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = 'User'
        self.fields['is_staff'].label = 'Staff Status'

    def clean(self):
        cleaned_data = super(ChangeStaffStatusForm, self).clean()
        user = cleaned_data.get('user')
        is_staff = cleaned_data.get('is_staff')

        if user and is_staff is None:
            raise forms.ValidationError('Please select the staff status for the user.')

        return cleaned_data
