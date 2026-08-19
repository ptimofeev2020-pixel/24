from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from catalog.forms import ProductForm
from catalog.models import Product, Contact


def home(request):
    products = Product.objects.all()

    latest_products = products.order_by('-created_at')[:5]
    print('Последние 5 созданных продуктов:')
    for product in latest_products:
        print(f'- {product.name}')

    paginator = Paginator(products, 6)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'catalog/home.html', {'page_obj': page_obj})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})


def contacts(request):
    contact = Contact.objects.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефон: {phone}, Сообщение: {message}')
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')
    return render(request, 'catalog/contacts.html', {'contact': contact})
