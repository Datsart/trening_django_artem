from django.contrib import admin
from django.urls import path
from .views import index, by_rubric, BbCreateView

urlpatterns = [
    path('bboard/<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('bboard/', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add')
]
