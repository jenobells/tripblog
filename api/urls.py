from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(
        'blogs/<int:pk>/',
        views.BlogDetail.as_view()
    ),
    path(
        'blogs/',
        views.BlogList.as_view(),
    ),
    path('blogs/<int:pk>/', views.BlogDetail.as_view(), name='blogs_detail'),
    path('', views.home, name='home'),
    path('', views.BlogList.post, name='create_blog'),
    path('blogs/create/', views.blogs_new, name='blogs_new')
]
