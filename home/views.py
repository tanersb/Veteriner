from django.shortcuts import render, HttpResponse

# Create your views here.

def homeView(request):
    if False:
        context={
            'isim': 'Taner'
        }
    else:
        context={
            'isim': 'Kullanıcı'
        }
    return render(request, 'home.html', context)


