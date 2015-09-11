import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from .helper_menu import get_menu
from .helper_item_form import get_item_form
from .helper_order import make_order
from .helper_restaurant_details import get_info


@require_GET
def menu(request):
    restaurant = request.GET.get('restaurant')
    menu = request.GET.get('menu')
    url = "https://www.leapset.com/order/restaurant/{0}/session/{1}".format(restaurant, menu)
    menu = get_menu(url)
    return JsonResponse(menu)


@require_GET
def product_details(request):
    act = request.GET.get('act')
    type = request.GET.get('type')
    merchantid = request.GET.get('merchantid')
    productpath = request.GET.get('productpath')
    checkoutMerchant = request.GET.get('checkoutMerchant')
    sessionId = request.GET.get('sessionId')

    data = {
        'act': act,
        'type': type,
        'merchantid': merchantid,
        'productpath': productpath,
        'checkoutMerchant': checkoutMerchant,
        'sessionId': sessionId
    }

    url = "https://www.leapset.com/order/ajax/add_item_form"
    form = get_item_form(url, data)
    return JsonResponse(form)


@require_POST
def make_the_order(request):
    data = json.loads(request.body.decode('utf-8'))
    make_order(data)
    return HttpResponse()


@require_GET
def restaurant_info(request):
    restaurant = request.GET.get('restaurant')
    url = "https://www.leapset.com/order/restaurant/{0}".format(restaurant)
    info = get_info(url)
    return JsonResponse(info)
