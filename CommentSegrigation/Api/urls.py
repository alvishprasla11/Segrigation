from django.urls import  path
from . import views

app_name = 'Api'

urlpatterns = [
    path('api/', views.Segrigation, name='SegrigationAPI'),
    path('',views.Index, name='index')
]