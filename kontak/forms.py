from django import forms
from .models import Kontak

class KontakForm(forms.ModelForm):
  class Meta:
    model = Kontak
    fields = ('nama', 'nomor_telepon', 'email', 'catatan',)