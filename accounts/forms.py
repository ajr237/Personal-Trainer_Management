from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateform(UserCreationForm):
    class Meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'
