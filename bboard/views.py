from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb


def index(request):
    bbs = Bb.objects.order_by('-published')
    context = {'objects_bb': bbs}
    return render(request, 'index.html', context)
