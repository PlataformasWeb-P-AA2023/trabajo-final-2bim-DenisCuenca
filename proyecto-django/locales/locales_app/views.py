from django.shortcuts import render, redirect
from .models import  Barrio, LocalesRepuestos, LocalesComida, Persona
from .forms import  LocalesComidaForm, LocalesRepuestosForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .serializer import LocalesComidaSerializer, LocalesRepuestosSerializer, PersonaSerializer, BarrioSerializer
from rest_framework import viewsets, permissions
# def list_locales_comida(request):
#     locales_comida = LocalesComida.objects.all()
#
#     return render(request, 'LocalesComida_list.html', {'locales_comida': locales_comida })

class ListLocalesComida(ListView):
    template_name= "LocalesComida_list.html"
    model = LocalesComida

def LocalesComida_create(request):
    if request.method == 'POST':
        form = LocalesComidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_LocalesComidas")
    else:
        form = LocalesComidaForm()
    return render(request, 'LocalesComida_form.html', {'formulario': form})


@login_required(login_url="/admin")
def LocalesComida_edit(request, id):
    e = LocalesComida.objects.get(pk=id)
    if request.method == 'POST':
        form = LocalesComidaForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return redirect("list_LocalesComidas")
    else:
        form = LocalesComidaForm(instance=e)
    return render(request, 'LocalesComida_form.html', {'formulario': form})


@login_required(login_url="/admin")
def eliminar_LocalesComida(request, id):
    """
    """
    e = LocalesComida.objects.get(pk=id)
    e.delete()
    return redirect("list_LocalesComidas")






# def list_LocalesRepuestoss(request):
#     LocalesRepuestoss = LocalesRepuestos.objects.all()
#
#     return render(request, 'LocalesRepuestos_list.html', {'LocalesRepuestoss': LocalesRepuestoss,  })
class ListLocalesRepuestos(ListView):
    template_name= "LocalesRepuestos_list.html"
    model = LocalesRepuestos


def LocalesRepuestos_create(request):
    if request.method == 'POST':
        form = LocalesRepuestosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_LocalesRepuestoss")
    else:
        form = LocalesRepuestosForm()
    return render(request, 'LocalesRepuestos_form.html', {'formulario': form})

@login_required(login_url="/admin")
def LocalesRepuestos_edit(request, id):
    e = LocalesRepuestos.objects.get(pk=id)
    if request.method == 'POST':
        form = LocalesRepuestosForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return redirect("list_LocalesRepuestoss")
    else:
        form = LocalesRepuestosForm(instance=e)
    return render(request, 'LocalesRepuestos_form.html', {'formulario': form})

@login_required(login_url="/admin")
def eliminar_LocalesRepuestos(request, id):
    """
    """
    e = LocalesRepuestos.objects.get(pk=id)
    e.delete()
    return redirect("list_LocalesRepuestoss")










# API VIEWS:

class LocalesComidaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = LocalesComida.objects.all()
    serializer_class = LocalesComidaSerializer
    permission_classes = [permissions.IsAuthenticated]




class LocalesRepuestosSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = LocalesRepuestos.objects.all()
    serializer_class = LocalesRepuestosSerializer
    permission_classes = [permissions.IsAuthenticated]




class PersonaSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    # permission_classes = [permissions.IsAuthenticated]




class BarrioSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]



