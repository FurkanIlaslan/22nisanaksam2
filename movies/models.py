from django.db import models

# Create your models here.
class Movie(models.Model):
    isim = models.CharField(max_length = 100)
    aciklama = models.TextField()
    resim = models.FileField(upload_to="resimler/", verbose_name="Film Resmi", null=True, blank=True)
    yuklenme_tarih = models.DateTimeField(auto_now_add = True)