from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Hayvan


# Create your views here.

def hayvanIndex(request):
    hayvans = Hayvan.objects.all()
    return render(request, 'Hayvan/index.html',{'hayvans':hayvans})

def hayvanDetail(request):
    hayvan = get_object_or_404(Hayvan, id=1) # idsi 1 olan hayvanı döndür ya da 404 döndür
    context = {
        'hayvan': hayvan
    }
    return render(request, 'Hayvan/detail.html',context)

def hayvanCreate(request):
    return HttpResponse('Create Sayfası.')

def hayvanUpdate(request):
    return HttpResponse('Update Sayfası.')

def hayvanDelete(request):
    return HttpResponse('Delete Sayfası.')


