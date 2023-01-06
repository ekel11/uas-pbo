from django.forms import ModelForm
from django import forms
from .models import *

class FormKonservasi(ModelForm):
    class Meta:
        model = kawasan
        fields = '__all__'

        widgets = {
            'nama_konservasi' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Kawasan', 'required':'required'}),
            'lintang' : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Lintang', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
            'bujur'   : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Bujur', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
        }


class FormBiota(ModelForm):
    class Meta:
        model = hewan
        fields = '__all__'

        widgets = {
            'nama_biota'   : forms.TextInput({'class':'form-control', 'placeholder':'Nama Biota', 'required':'required'}),
            'gambar'       : forms.FileInput({'class':'form-control', 'required':'required'}),
            'deskripsi'    : forms.Textarea({'class':'form-control',  'placeholder':'Deskripsi Singkat', 'required':'required'}),
        }