from . import views
from django.urls import path

urlpatterns = [
    path('me', views.Me.as_view(), name='me'),
]