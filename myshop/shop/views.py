from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(Category=category)
    return render(request, 'shop/product/list.html',{'category': category, 'categories': categories, 'products': products})

