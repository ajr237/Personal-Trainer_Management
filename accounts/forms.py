# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
#
# class SignUpForm(UserCreationForm):
#
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
#     password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Password'}))
#     password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Re-enter Password'}))
#
#     class Meta():
#         fields = UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2')
#         model = User

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
