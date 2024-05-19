from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),

    path('', include('django.contrib.auth.urls')),
    path('', views.account_profile, name='account_profile'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('search/', views.search, name='search'),
    path('profile/<uuid:profile_uuid>/', views.ProfileDetailView.as_view(), name='profile'),
]
