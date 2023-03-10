from django.shortcuts import render
from django.views.generic import ListView, \
    DetailView, \
    CreateView, \
    UpdateView, \
    DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import ProductCreationForm

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class FruitListView(ListView):
    model = Fruit
    template_name = 'fruit.html'
    context_object_name = 'fruits'

class FruitDetailView(DetailView):
    model = Fruit
    template_name = 'fruit_detail.html'
    context_object_name = 'fruit'

class ProductCreateView(CreateView):
    form_class = ProductCreationForm
    model = Product
    template_name = 'product_new.html'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    fields = ['name', 'description', 'price', 'image']

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('home')

class FruitCreateView(CreateView):
    model = Fruit
    template_name = 'fruit_new.html'
    fields = '__all__'

class FruitUpdateView(UpdateView):
    model = Fruit
    template_name = 'fruit_update.html'
    fields = ['name', 'description', 'price', 'image']

class FruitDeleteView(DeleteView):
    model = Fruit
    template_name = 'fruit_delete.html'
    success_url = reverse_lazy('fruits')

class ManufacturersListView(ListView):
    model = Manufacturer
    template_name = 'manufacturers.html'
    context_object_name = 'manufacturers'

class ManufacturersDetailView(DetailView):
    model = Manufacturer
    template_name = 'manufacturer_detail.html'
    context_object_name = 'manufacturer'

class ManufacturersCreateView(CreateView):
    model = Manufacturer
    template_name = 'manufacturer_new.html'
    fields = '__all__'

class ManufacturersUpdateView(UpdateView):
    model = Manufacturer
    template_name = 'manufacturer_update.html'
    fields = '__all__'