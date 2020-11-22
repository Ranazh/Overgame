from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/Bye.html'), name="logout"),
    path('success/', views.SuccessLoginView.as_view(), name="success"),
    path('user/', views.userprofile, name='user'),
    path('user/edit/', views.update_profile, name='editProfile'),
    path('user/password/', views.change_password, name='changePassword')
]
