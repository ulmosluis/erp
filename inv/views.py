# from django.shortcuts import render

# # Create your views here.

# from .models import Product

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'inv/product_list.html', {'products': products})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, ProductDeleteForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inv/product_list.html', {'products': products})

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'inv/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'inv/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductDeleteForm(request.POST or None, instance=product)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inv/product_confirm_delete.html', {'form': form})