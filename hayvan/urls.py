from django.urls import path
from .views import *







urlpatterns = [

    path('index/',hayvanIndex),
    path('detail/',hayvanDetail),
    path('create/',hayvanCreate),
    path('update/',hayvanUpdate),
    path('delete/',hayvanDelete)


]