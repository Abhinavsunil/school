from . import views
from django.urls import path,include
app_name='schoolapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('form',views.form,name='form'),
    path('/register',views.register,name='register'),
    path('result',views.result,name='result')
]
