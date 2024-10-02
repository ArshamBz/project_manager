from django.urls import path
from .views import LoginUser, ProfileUser, RegisterUser

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='user_login'),
    path('profile/', ProfileUser.as_view(), name='user_profile'),
    path('register/', RegisterUser.as_view(), name='user_register'),

]
