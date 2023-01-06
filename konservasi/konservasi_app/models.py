from django.db import models

# Create your models here.

class kawasan(models.Model):
     nama_konservasi        = models.CharField(max_length=75)
     lintang = models.FloatField(null=True)
     bujur = models.FloatField(null=True)

     def __str__(self):
         return self.nama_konservasi

class hewan(models.Model):
     nama_biota  = models.CharField(max_length=75)
     gambar     = models.ImageField(null=True, blank=True, upload_to="images/")
     deskripsi  = models.CharField(max_length=750)
     
     def __str__(self):
         return self.nama_biota