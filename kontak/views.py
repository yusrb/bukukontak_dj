from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Kontak
from .forms import KontakForm

# Create your views here.
@login_required
def daftar_kontak(request):
  all_kontak = Kontak.objects.filter(user=request.user)

  search_query = request.GET.get('q', '')

  all_kontak = all_kontak.filter(
    Q(nama__icontains=search_query) |
    Q(nomor_telepon__icontains=search_query) |
    Q(email__icontains=search_query)
  )

  context = {
    'search_query': search_query,
    'kontaks': all_kontak
  }

  return render(request, 'kontak/daftar_kontak.html', context)

@login_required
def tambah_kontak(request):
  if request.method == 'POST':
    form = KontakForm(request.POST)
    if form.is_valid():
      kontak = form.save(commit=False)
      kontak.user = request.user
      kontak.save()
      messages.success(request, 'Kontak Berhasil Dibuat.')
      return redirect('kontak:daftar_kontak')
  else:
    form = KontakForm()
  
  context = {
    'form': form
  }

  return render(request, 'kontak/tambah_kontak.html', context)

@login_required
def edit_kontak(request, kontak_id):
  get_kontak = get_object_or_404(Kontak, id=kontak_id)
  if request.method == 'POST':
    form = KontakForm(request.POST, instance=get_kontak)
    if form.is_valid():
      form.save()
      messages.success(request, 'Kontak Berhasil Diedit.')
      return redirect('kontak:daftar_kontak')
  else:
    form = KontakForm(instance=get_kontak)

  context = {
    'form': form
  }

  return render(request, 'kontak/edit_kontak.html', context)

@login_required
def hapus_kontak(request, kontak_id):
  get_kontak = get_object_or_404(Kontak, id=kontak_id)

  if request.method == 'POST':
    get_kontak.delete()
    messages.success(request, 'Kontak Berhasil Dihapus.')
  else:
    messages.error(request, 'Kontak Gagal Dihapus.')

  return redirect('kontak:daftar_kontak')