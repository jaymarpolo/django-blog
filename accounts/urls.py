from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.ProfilePageView.as_view(), name='profile'),
    path('edit-profile/', views.UserEditView.as_view(), name='edit-profile'),
    path('create-info/', views.CreateProfileView.as_view(), name='create-info'),
    path('edit-info/<int:pk>/', views.InfoEditView.as_view(), name='edit-info'),
    path('password/', views.ChangePasswordView.as_view(), name='password'),
]
