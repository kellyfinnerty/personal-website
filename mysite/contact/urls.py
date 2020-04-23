from django.urls import path
from . import views

urlpatterns = [
    path('my-info', views.show_info, name='my-info'),
    path('', views.contact, name='contact'),
    path('success', views.success, name='success')
]
