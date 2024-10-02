from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages
from django.views.generic import View
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy


class RegisterUser(View):
    form_class = UserRegisterForm
    template_name = 'Accounts/register.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {'form': self.form_class})

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = User.objects.create_user(username=data['username'],
                                            email=data['email'],
                                            last_name=data['last_name'],
                                            first_name=data['first_name'],
                                            password=data['password_1'])
            Profile.objects.create(
                user=user,
                phone=data['phone_number'],
            )
            login(self.request, user)
            messages.success(self.request, f"welcome", 'success')
            return redirect('accounts:user_profile')
        return render(self.request, self.template_name, {"form": form})


class LoginUser(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'Accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:user_profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(172800)  # expired after 2 days
        else:
            self.request.session.set_expiry(0)  # expired after user close the browser
        self.request.session.modified = True

        messages.success(self.request, f"welcome", 'success')
        return super(LoginUser, self).form_valid(form)


class ProfileUser(View):
    def get(self, *args, **kwargs):
        request = self.request
        profile = get_object_or_404(Profile, user=request.user)
        context = {
            'profile': profile
        }
        return render(request, 'Accounts/profile.html', context)


class LogoutUser(View):

    def get(self, request):
        logout(request)
        messages.success(self.request, f"We Hope See You Again !!", 'success')
        return redirect('accounts:user_login')


class ChangePasswordUser(SuccessMessageMixin, PasswordChangeView):
    template_name = 'Accounts/change_password.html'
    success_message = 'Password was changed successfully'
    success_url = reverse_lazy('accounts:user_profile')

