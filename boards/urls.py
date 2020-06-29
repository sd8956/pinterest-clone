"""Boards Urls"""

# Django 
from django.urls import path

# View
from boards import views

urlpatterns = [
    path(
        route='boards/new/',
        view=views.CreateBoardView.as_view(),
        name='create'
    ),
    path(
        route='board/<int:pk>',
        view=views.DetailPostView.as_view(),
        name='detail'
    )
]