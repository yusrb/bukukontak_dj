from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kontak(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  nama = models.CharField(max_length=100)
  nomor_telepon = models.CharField(max_length=13)
  email = models.EmailField(blank=True, null=True)
  catatan = models.TextField(blank=True, null=True)
  tanggal_dibuat = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "Kontak"
    verbose_name_plural = "Kontak"
  
  def __str__(self):
    return self.nama