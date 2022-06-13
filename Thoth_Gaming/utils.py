import json
from .models import *
from items.models import Item


def cartcookies(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    order = {'cart_total': 0, 'cart_total_items': 0}
    cartitems = order['cart_total_items']

    for i in cart:
        try:
            cartitems += cart[i]['quantity']

            product = Item.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['cart_total'] += total
            order['cart_total_items'] += cart[i]['quantity']

            item = {
                'items': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'picture': product.picture,
                    'rarities': product.rarities,
                    'type': product.type,
                },
                'quantity': cart[i]['quantity'],
                'total': total
            }
            items.append(item)
        except:
            pass
    return {'items': items, 'order': order, 'cartitems': cartitems}