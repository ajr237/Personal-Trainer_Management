from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    class Meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

# class UserCreationForm(UserCreationForm):
#
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget = TextInput(attrs = {'class': 'form-control',})
#         self.fields['password1'].widget = PasswordInput(attrs = {'class': 'form-control',})
#         self.fields['password2'].widget = PasswordInput(attrs = {'class': 'form-control',})
#
#     class Meta:
#         model = User
#         fields = UserCreationForm.Meta.fields
