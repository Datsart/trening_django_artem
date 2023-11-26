from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb, Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm, RubricForm
from django.urls import reverse_lazy


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}  # собради инфу
    return render(request, 'bboard/index.html', context)  # здесь куда мы передали инфу


def by_rubric(request, rubric_id):  # rubric_id создается само в БД , так как мы использовали FK
    # и создается так: имя_чего_либо + _id
    bbs = Bb.objects.filter(rubric=rubric_id)  # при обращении к БД фильтруем записи только те у которых
    # есть поле rubric (из модельки), а rubric_id это число , возвращает много записей
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)  # метод ГЕТ возвращает только одну запись!
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)
    # контекст - то что мы передаем в шаблон


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm  # из форм моделька
    success_url = reverse_lazy('index')  # здесь куда будем возвращаться после сохранения ,

    # в скобках имя name из урлов

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # получили контекст швблона от базового класса
        context['rubrics'] = Rubric.objects.all() # добавили в него рубрики
        return context

class RubricCreateView(CreateView):
    template_name = 'bboard/create_rubric.html'
    form_class = RubricForm  # из форм моделька
    success_url = reverse_lazy('index')  # здесь куда будем возвращаться после сохранения ,

    # в скобках имя name из урлов

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # получили контекст швблона от базового класса
        context['rubrics'] = Rubric.objects.all() # добавили в него рубрики
        return context