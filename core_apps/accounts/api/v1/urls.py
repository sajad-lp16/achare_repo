from django.urls import path

from core_apps.accounts.api.v1 import views

app_name = 'v1'

urlpatterns = [
    path('login-request/', views.LoginRequestAPIView.as_view(), name='login_request'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
]
