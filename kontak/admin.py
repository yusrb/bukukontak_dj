from django.contrib import admin
from .models import Kontak

# Register your models here.
@admin.register(Kontak)
class KontakAdmin(admin.ModelAdmin):
  list_display = ('nama','nomor_telepon','email',)