from django.urls import path, include

from . import views

app_name = 'django_app'
urlpatterns = [
    # The main view at path /
    path('', views.index, name='index'),
    # Detail of ressource ex: /5/
    path('<int:res_id>/', views.detail, name='detail'),
    # Profil of user
    path('profile/', views.user_profile, name="profile"),
    # Login user
    path('login', views.login, name='login'),
    # Register user
    path('register', views.register, name='register'),
    # Logout
    path('logout/', views.logout, name="logout"),
    # Change language of website
    path('set_language/', views.set_language, name="set_language"),
    # path('i18n/', include('django.conf.urls.i18n')),

    # PART BOOKING
    # Add booking for one user for one ressource
    path('booking_add/<int:res_id>', views.booking_add, name="booking_add"),
    # Delete booking for one user for one ressource
    path('booking_delete/<int:booking_id>', views.delete_booking, name="booking_delete"),
    # Modify booking for one user for one ressource
    path('booking_modify/<int:booking_id>', views.modify_booking, name="booking_modify"),

]
