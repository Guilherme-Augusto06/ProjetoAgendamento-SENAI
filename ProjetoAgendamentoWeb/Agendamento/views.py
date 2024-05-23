from django.shortcuts import render
from .models import Senai
def homepage(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    return render(request,'homepage.html', context)