from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CreateUserView, UserLoginView

app_name = 'user'
urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout')
]