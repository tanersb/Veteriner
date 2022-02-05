from django.contrib import admin
from hayvan.models import Hayvan
# Register your models here.

class HayvanAdmin(admin.ModelAdmin):

    class Meta:
        model = Hayvan




admin.site.register(Hayvan,HayvanAdmin)