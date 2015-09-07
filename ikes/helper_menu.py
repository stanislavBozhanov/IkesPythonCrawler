from collections import OrderedDict
import requests
import json
import re
from bs4 import BeautifulSoup


def get_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html.parser')

def get_categories_html(soup):
    return soup.find_all('div', {'class': 'cat_section_row'})

def get_category_heading(category):
    return category.find_all('a')[0].text

def get_category_description(category):
    result = category.find_all('span', {'class': 'des-text'})
    return result[0].text if result else []

def get_category_items(category):
    return category.find_all('li')

def item_name(item):
    return item.find_all('div', {'class': 'meal-menu-des'})[0].find_all('span')[0].text

def item_des(item):
    result = item.find_all('div', {'class': 'meal-menu-des'})[0].find_all('p')
    return result[0].text if result else []

def item_price(item):
    price = item.find_all('div', {'class': 'meal-menu-price'})[0].find_all('span')[0].text
    return float(price.replace('$', '').replace('+', ''))

def get_items_with_prices(category):
    items = category.find_all('li')
    return {item_name(item): item_price(item) for item in items}

def get_item_id(item):
    onclick = item.attrs['onclick']
    return re.search("itemPath:'(.+?)'", onclick).group(1)

def get_merchant_id(item):
    onclick = item.attrs['onclick']
    return re.search("merchantId:'(.+?)'", onclick).group(1)

def get_session_id(item):
    onclick = item.attrs['onclick']
    return re.search("sessionId:'(.+?)'", onclick).group(1)

def get_type(item):
    onclick = item.attrs['onclick']
    if 'isSubCat' in onclick:
        return 'subcat'
    return 'product'

def get_menu(url):
    soup = get_soup(url)
    categories = get_categories_html(soup)
    menu = OrderedDict()
    for category in categories:
        heading = get_category_heading(category)
        description = get_category_description(category)
        items = get_category_items(category)
        menu[heading] = {
            'description': description,
            'items': [{
                'name': item_name(item),
                'type': get_type(item),
                'productPath': get_item_id(item),
                'checkoutMerchant': get_merchant_id(item),
                'sessionId': get_session_id(item),
                'description': item_des(item),
                'price': item_price(item)
            } for item in items]
        }
    return menu
