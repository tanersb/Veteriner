from django.db import models

# Create your models here.

class Hayvan(models.Model):
    tür = models.CharField(max_length=50,verbose_name='Türü')
    cins = models.CharField(max_length=50,verbose_name='Cinsi')
    isim = models.CharField(max_length=50,verbose_name='İsmi')
    açıklama = models.TextField(verbose_name='Açıklaması')
    dogumtarihi = models.DateField('Doğum Tarihi')

    def __str__(self):
        return self.tür


