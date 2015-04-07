from django import forms

class nuevoAlumno(forms.Form):
    nombres=forms.CharField(label='Nombre',widget=forms.TextInput())
    apellidop=forms.CharField(label='Ape Paterno',widget=forms.TextInput())
    apellidom=forms.CharField(label='Ape Materno',widget=forms.TextInput())
    edad=forms.IntegerField(label='Edad',widget=forms.TextInput())
    carrera=forms.CharField(label='Carrera',widget=forms.TextInput())
