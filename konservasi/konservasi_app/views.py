from django.shortcuts import render, redirect
from django.core import serializers
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *

# Create your views here.
@login_required(login_url='login')
def konservasi(request):
      konser = kawasan.objects.all()
      titik_json = serializers.serialize('json', konser)
      konteks = {
          "Judul"   : "Konservasi",
          'konser' : konser,
          'titik_json' : titik_json,
      }
      return render(request, "konservasi.html", konteks)

@login_required(login_url='login')
def add_konservasi(request):
      if request.POST:
          form = FormKonservasi(request.POST)
          if form.is_valid():
              form.save()
              form = FormKonservasi()
              konser = kawasan.objects.all()
              konteks = {
                  "Judul"   : "Add Data",
                 'Title' : "Form Add Data",
                 'konser' : konser,
                 'form'    : form,
                 'pesan'   : "Data berhasil ditambahkan"
              }
              return render(request, "add_konservasi.html", konteks)
      else:
          form  = FormKonservasi()
          konser = kawasan.objects.all()
          konteks = {
             "Judul"   : "Add Data",
             'Title'   : "Form Add Data",
             'konser' : konser,
             'form'    : form,
          }
          return render(request, "add_konservasi.html", konteks)

@login_required(login_url='login')
def edit_konservasi(request, id):
      konser = kawasan.objects.get(pk=id)
      if request.POST:
          form = FormKonservasi(request.POST, instance=konser)
          if form.is_valid():
              form.save()
              konteks = {
                  "Judul"   : "Edit Data",
                  'Title' : "Form Edit Data",
                  'konser' : konser,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "edit_konservasi.html", konteks)
      else:
          form = FormKonservasi(instance=konser)
          konteks = {
          "Judul"   : "Edit Data",
          'Title' : "Form Edit Data",
          'konser' : konser,
          'form'  : form,
           }
      return render(request, "edit_konservasi.html", konteks)

@login_required(login_url='login')
def delete_konservasi(request, id):
    konser = kawasan.objects.get(pk=id)
    konser.delete()
    
    return redirect("/konservasi/")

@login_required(login_url='login')
def biota(request):
      jenis = hewan.objects.all()
      konteks = {
          "Judul"   : "Biota",
          'jenis' : jenis,
      }
      return render(request, "biota.html", konteks)

@login_required(login_url='login')
def add_biota(request):
      if request.POST:
          form = FormBiota(request.POST, request.FILES)
          if form.is_valid():
              form.save()
              form = FormBiota()
              jenis = hewan.objects.all()
              konteks = {
                  "Judul"   : "Add Data",
                 'Title' : "Form Add Data",
                 'jenis' : jenis,
                 'form'    : form,
                 'pesan'   : "Data berhasil ditambahkan"
              }
              return render(request, "add_biota.html", konteks)
      else:
          form  = FormBiota()
          jenis = hewan.objects.all()
          konteks = {
             "Judul"   : "Add Data",
             'Title'   : "Form Add Data",
             'jenis' : jenis,
             'form'    : form,
          }
          return render(request, "add_biota.html", konteks)

@login_required(login_url='login')
def edit_biota(request, id):
      jenis = hewan.objects.get(pk=id)
      if request.POST:
          form = FormBiota(request.POST, request.FILES, instance=jenis)
          if form.is_valid():
              form.save()
              konteks = {
                  "Judul"   : "Edit Data",
                  'Title' : "Form Edit Data",
                  'jenis' : jenis,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "edit_biota.html", konteks)
      else:
          form = FormBiota(instance=jenis)
          konteks = {
          "Judul"   : "Edit Data",
          'Title' : "Form Edit Data",
          'jenis' : jenis,
          'form'  : form,
           }
      return render(request, "edit_biota.html", konteks)

@login_required(login_url='login')
def delete_biota(request, id):
    jenis = hewan.objects.get(pk=id)
    jenis.delete()
    
    return redirect("/biota/")

def Pagelogin(request):
    if request.user.is_authenticated:
        return redirect ("/konservasi/")
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('pass')
            user=authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('/konservasi/')
            
        return render(request, "login.html")

def Pageregistrasi(request):
    if request.user.is_authenticated:
        return redirect ("/konservasi/")
    else:
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            my_user=User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('/login/')

        return render(request, "registrasi.html")

def Pagelogout(request):
    logout(request)
    return redirect('/login/')