"""Users URLs."""

# Django
from django.urls import path

# View
from users import views
from users.views import UserDetailView


urlpatterns = [

    # Posts
    path(
        route='profile/<str:username>/',
        view=UserDetailView.as_view(template_name='users/detail.html'),
        name='detail'
    ),

    # Management
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
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    )

]