from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    password_1 = forms.CharField(max_length=100, required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'id': 'form3Example5',
                                         'type': 'password',
                                     }
                                 ))
    username = forms.CharField(required=True, max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'id': 'form3Example1'
                                   }
                               ))
    email = forms.EmailField(required=True, max_length=175,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'id': 'form3Example2'
                                 }
                             ))
    first_name = forms.CharField(required=True, max_length=50,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'id': 'form3Example3'
                                     }
                                 ))
    last_name = forms.CharField(required=True, max_length=50,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'id': 'form3Example4'
                                    }
                                ))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('this user name was taken')
        return username

    def clean_password_1(self):
        password1 = self.cleaned_data['password_1']
        if len(password1) < 8:
            raise forms.ValidationError('something went wrong')
        return password1


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example4'}))
    remember = forms.BooleanField(required=False,
                                  widget=forms.CheckboxInput(
                                      attrs={
                                          'class': 'form-check-input me-2',
                                          'id': 'form2Example33'
                                      }
                                  ))
    username = forms.CharField(
        required=True, max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form3Example1'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'username or password is incorrect'
        super().__init__(*args, **kwargs)
