from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import alumno
from .forms import nuevoAlumno

def index(request):
    latest_question_list = alumno.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'alumnos': latest_question_list,
    })
    return HttpResponse(template.render(context))

def nuevo(request):
    if request.method=='GET':
        formulario=nuevoAlumno()
        template = loader.get_template('nuevo.html')
        context = RequestContext(request, {
            'form': formulario,
        })
        return HttpResponse(template.render(context))
    else:
        nombres=""
        apellp=""
        apellm=""
        edad=""
        carrera=""
        formulario=nuevoAlumno(request.POST)
        if formulario.is_valid():
            nombres=formulario.cleaned_data['nombres']
            apellp=formulario.cleaned_data['apellidop']
            apellm=formulario.cleaned_data['apellidom']
            edad=formulario.cleaned_data['edad']
            carrera=formulario.cleaned_data['carrera']
            alum=alumno()
            alum.nombres=nombres
            alum.apellp=apellp
            alum.apellm=apellm
            alum.edad=edad
            alum.carrera=carrera
            alum.save()

        return HttpResponseRedirect('/inicio/')


def modificar(request,question_id):
    if request.method=='GET':

        alumnosss=alumno.objects.get(id=question_id)
        template = loader.get_template('modificar.html')
        context = RequestContext(request, {
            'alumno': alumnosss,
        })
        return HttpResponse(template.render(context))
    else:
        nombres=""
        apellp=""
        apellm=""
        edad=""
        carrera=""
        formulario=nuevoAlumno(request.POST)
        if formulario.is_valid():
            nombres=formulario.cleaned_data['nombres']
            apellp=formulario.cleaned_data['apellidop']
            apellm=formulario.cleaned_data['apellidom']
            edad=formulario.cleaned_data['edad']
            carrera=formulario.cleaned_data['carrera']
            alum=alumno.objects.get(id=question_id)
            alum.nombres=nombres
            alum.apellp=apellp
            alum.apellm=apellm
            alum.edad=edad
            alum.carrera=carrera
            alum.save()

        return HttpResponseRedirect('/inicio/')

def inicio(request):
    return HttpResponseRedirect('/inicio/')

def eliminar(request,question_id):
    alu = alumno.objects.get(id=question_id)
    alu.delete()
    return HttpResponseRedirect('/inicio/')
