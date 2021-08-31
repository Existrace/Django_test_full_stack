from django.urls import path

from . import views

app_name = 'django_app'
urlpatterns = [
    # The main view at path /
    path('', views.index, name='index'),
    # Detail of ressource ex: /5/
    path('<int:res_id>/', views.detail, name='detail'),
    # Login user
    path('login', views.login, name='login'),
    # Register user
    path('register', views.register, name='register'),
    # Logout
    path('logout/', views.logout, name="logout"),
    # Profil of user
    path('profile/', views.user_profile, name="profile"),

    # Add booking for one user
    path('booking_add/', views.booking_add, name="booking_add"),
]
