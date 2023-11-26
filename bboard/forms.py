from django.forms import ModelForm
from .models import Bb , Rubric


class BbForm(ModelForm):
    class Meta:
        model = Bb  # имя модели
        fields = ['title', 'content', 'price', 'rubric']  # поля которые будем добавлять

class RubricForm(ModelForm):
    class Meta:
        model = Rubric
        fields = ['name']