"""Users urls"""

# Django
from django.urls import path

# View 
from users import views

urlpatterns = [
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='sigup/',
        view=views.SignupView,
        name='signup'
    ),
    path(
        route='<str:username>/board',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),
    path(
        route='<str:username>/pin',
        view=views.UserDetailViewPins.as_view(),
        name='detailPin'
    ),
]