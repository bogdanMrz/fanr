from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from datetime import datetime

#from django.core.urlresolvers import reverse

from .forms import *
from .models import *
# Create your views here.



def paginate(request, list_object, number):
    paginator = Paginator(list_object, number)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj


def index(request):
    return redirect('schimb-list-date')



def create_client_ro(request):
    if request.method == "POST":
        form = CreateClient1Form(request.POST)
        if form.is_valid():
            form.save()

            return redirect('client-list')

    form = CreateClient1Form()

    return render(request, 'casa/create_client_ro.html', {'form':form})


def create_client_strain(request):
    if request.method == "POST":
        form = CreateClient2Form(request.POST)

        if form.is_valid():
            form.save()

            return redirect('client-list')

    form = CreateClient2Form()

    return render(request, 'casa/create_client_strain.html', {'form':form})



def create_valuta(request):
    if request.method == "POST":
        form = CreateValutaForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('valuta-list')

    form = CreateValutaForm()

    return render(request, 'casa/create.html', {'form':form})


def create_cotatie(request):
    if request.method == "POST":
        form = CreateCotatieForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('cotatie-list')

    form = CreateCotatieForm()

    return render(request, 'casa/create.html', {'form':form})



def create_schimb(request):
    if request.method == "POST":
        form = CreateBuletinDeSchimbForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('schimb-list')

    form = CreateBuletinDeSchimbForm()

    return render(request, 'casa/create.html', {'form':form})



def client_list(request):
    lis = Client.objects.all()
    lis = paginate(request=request,list_object=lis,number=10)

    return render(request, 'casa/client_list.html', {'list': lis, 'name':'Client'})



def valuta_list(request):
    lis = Valuta.objects.all()
    lis = paginate(request=request,list_object=lis,number=10)

    return render(request, 'casa/valuta_list.html', {'list': lis, 'name':'Valuta'})



def cotatie_list(request):
    lis = Cotatie.objects.all()
    lis = paginate(request=request,list_object=lis,number=10)

    return render(request, 'casa/cotatie_list.html', {'list': lis, 'name':'Cotatie'})


def schimb_list(request):
    lis = BuletinDeSchimb.objects.all()
    lis = paginate(request=request,list_object=lis,number=10)

    calendar = Calendar()
    return render(request, 'casa/schimb_list.html', {'list': lis, 'name':'Schimb', 'calendar':calendar})

def schimb_list_date(request):
    date = request.GET.get('calendar') 
    if not date:
        date = datetime.now()

    lis = BuletinDeSchimb.objects.filter(data=date)
    lis = paginate(request=request,list_object=lis,number=10)
    
    calendar = Calendar()

    return render(request, 'casa/schimb_list.html', {'list': lis, 'name':'Schimb', 'calendar':calendar})

def edit_client(request,id):
    client = get_object_or_404(Client, pk=id)

    if client.adresa:
        form = CreateClient1Form(request.POST or None, instance=client)
    else:
        form = CreateClient2Form(request.POST or None, instance=client)
    
    if form.is_valid():
        form.save()
        return redirect('client-list')
    
    return render(request, 'casa/create.html', {'form':form})



def edit_valuta(request,id):
    valuta = get_object_or_404(Valuta, pk=id)
    form = EditValutaForm(request.POST or None, instance=valuta)
    
    sold = Soldform(initial={'sold':valuta.sold})
    

    if form.is_valid():
        form.save()
        return redirect('valuta-list')

    return render(request, 'casa/create.html', {'form':form, 'sold':sold})

def edit_cotatie(request,id):
    cotatie = get_object_or_404(Cotatie, pk=id)
    form = CreateCotatieForm(request.POST or None, instance=cotatie)    
    
    if form.is_valid():
        form.save()
        return redirect('cotatie-list')

    return render(request, 'casa/create.html', {'form':form})


def edit_schimb(request,id):
    schimb = get_object_or_404(BuletinDeSchimb, pk=id)
    form = CreateBuletinDeSchimbForm(request.POST or None, instance=schimb)
    
    if form.is_valid():
        form.save()
        return redirect('schimb-list')

    return render(request, 'casa/create.html', {'form':form})



def delete_client(request, id):
    client = get_object_or_404(Client, pk=id)
    client.delete()

    return redirect('client-list')


def delete_valuta(request, id):
    valuta = get_object_or_404(Valuta, pk=id)
    valuta.delete()

    return redirect('valuta-list')

def delete_cotatie(request, id):
    cotatie = get_object_or_404(Cotatie, pk=id)
    cotatie.delete()

    return redirect('cotatie-list')

def delete_schimb(request, id):
    schimb = get_object_or_404(BuletinDeSchimb, pk=id)
    schimb.delete()

    return redirect('schimb-list')