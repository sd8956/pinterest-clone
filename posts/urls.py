"""Posts urls"""

# Django
from django.urls import path

# View
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),
    
    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create'
    ),
    
    path(
        route='pin/<int:pk>',
        view=views.DetailPostView.as_view(),
        name='detail'
    ),

    path(
        route='board/pin/',
        view=views.CreatePostBoardView.as_view(),
        name='addToBoard'
    )
]