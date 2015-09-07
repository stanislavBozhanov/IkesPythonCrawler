import requests
from bs4 import BeautifulSoup

def make_order(data):
    s = requests.Session()
    login_url = 'https://www.leapset.com/order/login'
    restaurant_page = 'https://www.leapset.com/order/restaurant/{0}'.format(data['restaurant'])
    restaurant_menu_page = "https://www.leapset.com/order/restaurant/{0}/session/{1}".format(data['restaurant'], data['session'])
    checkout_url = 'https://www.leapset.com/order/cart/checkout'
    payment_url = 'https://www.leapset.com/order/cart/checkout/payment'
    fetch_cart = 'https://www.leapset.com/order/ajax/fetch_cart'

    r = s.get(login_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    csrf_token_login = soup.find('input', {'id': 'signin__csrf_token'}).attrs['value']

    checkin_data = {
        'signin[redir]': '',
        'signin[_csrf_token]': csrf_token_login,
        'signin[email]': data['username'],
        'signin[pwd]': data['password']
    }
    r = s.post(login_url, data=checkin_data)
    print(r)
    s.get(restaurant_menu_page)
    orders = data['list_with_orders']
    for order in orders:
        data_for_cart = {
            'merchantid': order['merchantid'],
            'productid': order['productid'],
            'act': order['act'],
            'checkoutMerchant': order['checkoutMerchant'],
            'sessionId': order['sessionId'],
            'quantity': order['quantity'],
        }
        for key, value in order['options'].items():
            data_for_cart[key] = value
        r = s.post(fetch_cart, data_for_cart)
        print(r)

    r = s.get(restaurant_menu_page)
    soup = BeautifulSoup(r.content, 'html.parser')
    csrf_token_cart = soup.find('input', {'id': 'cart_checkout__csrf_token'}).attrs['value']
    data_for_checkout_one = {
        'cart_checkout[checkout_confirm]': '',
        'cart_checkout[_csrf_token]': csrf_token_cart,
        'cart_checkout[order_type]': data['order_type'],    #  'pickup',
        'cart_checkout[order_time]': data['order_time']   #  1441131300
    }
    r = s.post(restaurant_menu_page, data_for_checkout_one)
    print(r)

    r = s.get(checkout_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    csrf_token_delivery = soup.find('input', {'id': 'delivery__csrf_token'}).attrs['value']
    data_for_checkout_two = {
        'pickup[checkout_confirm]': '',
        'pickup[_csrf_token]': csrf_token_delivery,
        'pickup[order_type]': data['order_type'],
        'pickup[order_time]': data['order_time'],
        'pickup[discount_code]': '',
        'pickup[first_name]': data['first_name'],
        'pickup[last_name]': data['second_name'],
        'pickup[email]': data['username'],
        'pickup[phone1]': data['phone_1'],
        'pickup[phone2]': data['phone_2'],
        'pickup[phone3]': data['phone_3'],
    }
    r = s.post(checkout_url, data_for_checkout_two)
    print(r)

    r = s.get(payment_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    csrf_token_delivery = soup.find('input', {'id': 'payment__csrf_token'}).attrs['value']
    data_for_payment = {
        'payment[userstatus]': '',
        'payment[pwd]': '',
        'payment[checkout_confirm]': '',
        'payment[_csrf_token]': csrf_token_delivery,
        'payment[nameoncard]': data['nameoncard'],
        'payment[cctype]': data['cctype'],
        'payment[ccnumber]': data['ccnumber'],
        'payment[expdatem]': data['expdatem'],
        'payment[expdatey]': data['expdatey'],
        'payment[cvvcode]': data['cvvcode'],
        'payment[tippr]': data['tippr'],
        'payment[tip]': data['tip']
    }
    r = s.post(payment_url, data=data_for_payment)
    print(r)
    return r
