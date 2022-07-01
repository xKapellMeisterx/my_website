from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from product.models import Product, Order

User = get_user_model()


def home_page(request):
    list_obj = Product.objects.all()
    context = {'title': 'Главная страница',
               'list_obj': list_obj
               }
    return render(request, 'products/home_page.html', context)


def category_product(request, slug):
    return HttpResponse('Страница категории товара')


def profile(request, username):
    customer = get_object_or_404(User, username=username)
    order = Order.product.all()
    page_obj = customer.ordering
    context = {
        'customer': customer,
        'order': order,
        'page_obj': page_obj
    }
    return render(request, 'customers/orders.html', context=context)



