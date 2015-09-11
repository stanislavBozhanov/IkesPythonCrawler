from collections import OrderedDict
from bs4 import BeautifulSoup
import requests


def get_block_content(soup):
    return soup.find('div', {'class': 'cont1-details'})


def get_heading(block):
    return block.find('h2').text


def get_delivery_details(block):
    list_items = block.find('ul', {'class': 'delivery-details'}).find_all('li')
    info = {}
    for list_item in list_items:
        key = list_item.find('span').text.strip().replace(':', '')
        value = list_item.find('p').text.strip()
        info[key] = value
    return info


def get_time_table(block):
    time_table_items = block.find('ul', {'class': 'time-table'})
    info = {
        'Heading': time_table_items.find('h3').text.strip().replace(':', ''),
        'Ordering days': time_table_items.find('span').text.strip().replace('\n', '').replace(' ', ''),
        'Ordering hours': time_table_items.find('p').text.strip().replace('\n', '').replace(' ', '')
    }
    return info


def get_info(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    block = get_block_content(soup)
    info = OrderedDict()
    info['heading'] = get_heading(block)
    info['time table'] = get_time_table(block)
    info['delivery_details'] = get_delivery_details(block)
    return info
