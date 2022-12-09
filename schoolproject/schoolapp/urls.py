from . import views
from django.urls import path
app_name='schoolapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.log,name='login'),
    path('form',views.form,name='form'),
    path('register',views.reg,name='register'),
    path('result',views.result,name='result')
]
