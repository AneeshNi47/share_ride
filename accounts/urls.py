from django.urls import path, include
from .api import RegisterAPI, LoginApi, UserAPI, ChangePasswordView, UpdateProfileView
from knox import views as knox_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginApi.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('api/update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name="knox_logout")
]
