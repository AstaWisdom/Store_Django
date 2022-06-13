from django.urls import path, include
from . import views

app_name = 'users.urls'

urlpatterns =[
 path('', include('django.contrib.auth.urls')),
 # user register path
 path('Register/', views.register, name='register'),
 path('user-dashboard/<int:user_id>', views.user_dashboard, name='user_dashboard'),
 path('users/<str:ref_code>/', views.ref_code, name='ref_code'),
 path('Special-order/', views.special_order, name='sepcial_order'),
]