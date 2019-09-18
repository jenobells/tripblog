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
]
