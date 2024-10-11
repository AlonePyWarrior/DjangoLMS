from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/edit/', views.UserUpdateProfile.as_view(), name='update_user'),
]
