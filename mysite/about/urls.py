from django.urls import path
from .views import about, info, resume

urlpatterns = [
    path('', about, name='about'),
    path('info', info, name='info'),
    path('resume', resume, name='resume'),
]
