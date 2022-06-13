from django.urls import path, include
from . import views

app_name = 'Thoth_Gaming.urls'

urlpatterns =[
 path('', views.homepage, name='homepage'),
 path('', include('Blog.urls')),
 path('', include('users.urls')),
 path('cart/', views.cart, name='cart'),
 path('Store/', views.store, name='store'),
 path('update_item/', views.updateitem, name='update_item'),
 path('product/<int:product_id>', views.product_page, name='product_page')
]