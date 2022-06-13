from django.urls import path
from . import views

app_name = 'Blog.urls'

urlpatterns =[
 path('Blog/', views.homepage, name='homepage'),
 path('Post/<slug:slug>', views.post, name='post'),
]
