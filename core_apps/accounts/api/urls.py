from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('v1/', include('core_apps.accounts.api.v1.urls')),
]
