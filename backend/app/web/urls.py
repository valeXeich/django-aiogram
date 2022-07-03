from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import LoginView, UserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user-info'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
