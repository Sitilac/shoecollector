from django.shortcuts import render, redirect
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import *


class ShoeCreate(CreateView):
  model = Shoe
  fields = '__all__'
  success_url = '/shoes/'

class ShoeCreate(CreateView):
  model = Shoe
  fields = ['name', 'description', 'price']
  success_url = '/shoes/'

class ShoeUpdate(UpdateView):
  model = Shoe
  fields = ['name', 'description', 'price']

class ShoeDelete(DeleteView):
  model = Shoe
  success_url = '/shoes/'
  
class OutfitCreate(CreateView):
  model = Outfit
  fields = '__all__'

class OutfitList(ListView):
  model = Outfit

class OutfitDetail(DetailView):
  model = Outfit
  
class OutfitUpdate(UpdateView):
  model = Outfit
  fields = ['name', 'top', 'bottom']

class OutfitDelete(DeleteView):
  model = Outfit
  success_url = '/outfits/'

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def shoes_index(request):
  shoes = Shoe.objects.all()
  return render(request, 'shoes/index.html', { 'shoes': shoes })

def shoes_detail(request, shoe_id):
  shoe = Shoe.objects.get(id=shoe_id)
  outfits_not_included = Outfit.objects.exclude(id__in = shoe.outfits.all().values_list('id'))
  cleaning_form = CleaningForm()
  return render(request, 'shoes/detail.html', { 
    'shoe': shoe, 
    'cleaning_form': cleaning_form,
    'outfits': outfits_not_included, 
  })

def add_cleaning(request, shoe_id):
  # create a ModelForm instance using the data in request.POST
  form = CleaningForm(request.POST)
  print(form)
  # validate the form
  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.shoe_id = shoe_id
    new_cleaning.save()
  return redirect('detail', shoe_id=shoe_id)

def assoc_outfit(reques,shoe_id, outfit_id):
  Shoe.objects.get(id=shoe_id).outfits.add(outfit_id)
  return redirect('detail', shoe_id=shoe_id)

