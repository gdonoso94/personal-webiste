from . import views
from django.urls import path

urlpatterns = [
    path('me', views.Me.as_view(), name='me'),
    #path('post_detail/<slug>', views.PostDetail.as_view(), name='post_detail'),
]