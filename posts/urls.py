from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.index, name='home'),
    path('index/', views.index, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('main', views.main, name='main'),
    path('blog/<int:id>', views.open_blog, name='blog'),
    path('create_blog/<int:user_id>', views.create_blog, name='create_blog'),
    path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
]