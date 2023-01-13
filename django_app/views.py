from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

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