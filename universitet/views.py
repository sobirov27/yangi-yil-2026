from django.shortcuts import render
from .models import Universitet, Direktor, Oqituvchi
# Create your views here.
def universitet_list(request):
    universitetlar = Universitet.objects.all()
    context = {
        'universitetlar': universitetlar
    }
    return render(request, 'universitet/universitet_list.html', context)




def direktor_list(request):
    direktorlar = Direktor.objects.select_related('user')
    context = {
        'direktorlar': direktorlar
    }
    return render(request, 'universitet/direktor_list.html', context)




def oqituvchi_list(request):
    oqituvchilar = Oqituvchi.objects.select_related('user')
    context = {
        'oqituvchilar': oqituvchilar
    }
    return render(request, 'universitet/oqituvchi_list.html', context)