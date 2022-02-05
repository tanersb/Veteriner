from django.shortcuts import render, HttpResponse


# Create your views here.

def hayvanIndex(request):
    return HttpResponse('Index Sayfası.')

def hayvanDetail(request):
    return HttpResponse('Detail Sayfası.')

def hayvanCreate(request):
    return HttpResponse('Create Sayfası.')

def hayvanUpdate(request):
    return HttpResponse('Update Sayfası.')

def hayvanDelete(request):
    return HttpResponse('Delete Sayfası.')


