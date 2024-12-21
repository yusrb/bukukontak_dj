from django.urls import path
from .views import (
  daftar_kontak,
  tambah_kontak,
  edit_kontak,
  hapus_kontak,
)

urlpatterns = [
  path('', daftar_kontak, name="daftar_kontak"),
  path('tambah/', tambah_kontak, name="tambah_kontak"),
  path('edit/<int:kontak_id>', edit_kontak, name="edit_kontak"),
  path('hapus/<int:kontak_id>', hapus_kontak, name="hapus_kontak"),
]