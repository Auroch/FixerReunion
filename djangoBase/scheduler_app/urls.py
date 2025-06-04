from django.urls import path
from . import views

urlpatterns = [
    path('creer/', views.create_meeting, name='create_meeting'),
    path('inviter/<int:demande_id>/', views.inviter, name='inviter'),
]
