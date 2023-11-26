from django.contrib import admin
from django.urls import path
from .views import index, by_rubric, BbCreateView, RubricCreateView
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('qwert/<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('add_object/', BbCreateView.as_view(), name='add'),
    path('add_rubric/', RubricCreateView.as_view(), name='add_rubric'),
    #     as_view() - для класса вьюшки, так как это не функция, а класс

]
# здесь name=index , урлы называются как угодно, но в шаблоне будем указывать что в 'name'
# типа <a href="{% url 'by_rubric' rubric.pk %}">{{ rubric.name }}</a>
# то есть в какой path попадаем и соответственно в какую вьющку
