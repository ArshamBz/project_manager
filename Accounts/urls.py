from django.urls import path
from .views import LoginUser, ProfileUser

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='user_login'),
    path('profile/', ProfileUser.as_view(), name='user_profile')

]
