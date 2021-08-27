from django.urls import path

from . import views

app_name = 'django_app'
urlpatterns = [
    # The main view at path /
    path('', views.index, name='index'),
    # Detail of ressource ex: /5/
    path('<int:res_id>/', views.detail, name='detail'),
]