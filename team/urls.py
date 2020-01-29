from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_persons,name='team_list'),
    path("<int:pk>/", views.person_detail, name="person_detail"),
]