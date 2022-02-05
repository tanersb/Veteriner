from django.contrib import admin
from hayvan.models import Hayvan
# Register your models here.

class HayvanAdmin(admin.ModelAdmin):

    list_display = ['tür','dogumtarihi']
    list_display_links = ['tür','dogumtarihi']
    list_filter = ['tür'] #filtre uygular
    search_fields = ['tür', 'cisim', 'isim']
    #list_editable = [] #Admin panelinde değiştirme işlemini girmeden yapabilrsin.




    class Meta:
        model = Hayvan






admin.site.register(Hayvan,HayvanAdmin)