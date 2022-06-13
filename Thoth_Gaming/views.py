from django.shortcuts import render, redirect
from .models import Order, OrderItem
from Blog.models import Post
from django.contrib.auth.models import User
from items.models import Item
from users.models import Customer
from django.http import JsonResponse
import json
from .forms import OrderForm
from .filter import ItemFilter
from .utils import cartcookies
from django.core.paginator import Paginator
# Create your views here.


def homepage(request):
    items_filter = ItemFilter(request.GET, queryset=Item.objects.all().order_by('-date'))
    post_filter = Post.objects.all().order_by('-post_date')
    paginator_item = Paginator(items_filter.qs, 8)
    paginator_post = Paginator(post_filter, 4)
    page_number = request.GET.get('page')
    page_number_1 = request.GET.get('page')

    items = paginator_item.get_page(page_number)
    posts = paginator_post.get_page(page_number_1)


    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(user=customer, complete=False)
        cartitems = order.cart_total_items
    else:
        Cookiedata = cartcookies(request)
        order = Cookiedata['order']
        cartitems = Cookiedata['cartitems']

    context ={'items': items, 'cartitems': cartitems, 'order': order, 'items_filter': items_filter, 'posts': posts}
    return render(request, 'Thoth_Gaming/homepage.html', context)


def store(request):
    items_filter = ItemFilter(request.GET, queryset=Item.objects.all().order_by('-date'))
    paginator = Paginator(items_filter.qs, 6)
    page_number = request.GET.get('page')

    items = paginator.get_page(page_number)

    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(user=customer, complete=False)
        cartitems = order.cart_total_items
    else:
        Cookiedata = cartcookies(request)
        order = Cookiedata['order']
        cartitems = Cookiedata['cartitems']

    context = {'items': items, 'cartitems': cartitems, 'order': order, 'items_filter': items_filter}
    return render(request, 'Thoth_Gaming/store.html', context)

def cart(request):
    form = OrderForm()
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(user=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.cart_total_items

    else:
        Cookiedata = cartcookies(request)
        if request.method == 'POST':
            form = OrderForm(data=request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                trading_link = form.cleaned_data.get('trade_link')
                customer = Customer(name=email, trading_link=trading_link, user=User.objects.get(id=1))
                customer.save()
                print(customer)
        items = Cookiedata['items']
        order = Cookiedata['order']
        cartitems = Cookiedata['cartitems']

    context ={'items': items, 'order': order, 'cartitems': cartitems, 'form': form}
    return render(request, 'Thoth_Gaming/cart.html', context)


def updateitem(request):
    data = json.loads(request.body)
    itemid = data['itemId']
    print(itemid)
    action = data['action']
    customer = request.user
    item = Item.objects.get(id=itemid)
    order, create = Order.objects.get_or_create(user=customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, items=item)

    if action == 'add':
        orderitem.quantity = orderitem.quantity + 1
    elif action == 'remove':
        orderitem.quantity = orderitem.quantity - 1
    elif action == 'delete':
        orderitem.quantity = 0

    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('Item Was Updated', safe=False)


def product_page(request, product_id):
    product = Item.objects.get(id=product_id)

    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(user=customer, complete=False)
        cartitems = order.cart_total_items
    else:
        Cookiedata = cartcookies(request)
        order = Cookiedata['order']
        cartitems = Cookiedata['cartitems']

    context = {'product': product, 'cartitems': cartitems, 'order': order,}
    return render(request, 'Thoth_Gaming/product_page.html', context)
