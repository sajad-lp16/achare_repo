from django.urls import path, include


app_name = 'accounts'

urlpatterns = [
    path('api/', include('core_apps.accounts.api.urls', namespace='api')),
]