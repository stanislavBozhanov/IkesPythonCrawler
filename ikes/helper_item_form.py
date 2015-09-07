from collections import OrderedDict
import requests
from bs4 import BeautifulSoup


def get_soup(url, data):
    r = requests.post(url, data=data)
    return BeautifulSoup(r.content, 'html.parser')

def get_form_sections(form):
    return form.find_all('div', {'class': 'cls_attrib_envilop'})

def get_section_label(section):
    return section.find('label').text.strip()

def get_all_inputs(section):
    inputs = section.find_all('input')
    length = len(inputs) - 1
    while length >= 0:
        if inputs[length].attrs['type'] == 'hidden':
            inputs.pop(length)
        length -= 1
    return inputs

def has_input_quantity(form):
    if form.find('input', {'id': 'id_add_item_dlg_quantity'}):
        print('found')
        return True
    else:
        print('not found')
        return False

def get_input_name(input):
    return input.parent.text.strip()

def get_input_value(input):
    return input.attrs['value']

def get_input_options(input):
    return input.attrs['name']

def get_input_type(input):
    return input.attrs['type']

def get_item_form(url, data):
    soup = get_soup(url, data)
    sections = get_form_sections(soup)
    form = OrderedDict()
    if has_input_quantity(soup):
        form['Quantity'] = [{
            'quantity': 1,
            'type': 'text'
        }]
    for section in sections:
        label = get_section_label(section)
        for inp in get_all_inputs(section):
            if label not in form.keys():
                form[label] = [{
                        'name': get_input_name(inp),
                        'options': get_input_options(inp),
                        'value': get_input_value(inp),
                        'type': get_input_type(inp)
                    }]
            else:
                form[label].append({
                    'name': get_input_name(inp),
                    'options': get_input_options(inp),
                    'value': get_input_value(inp),
                    'type': get_input_type(inp)
                })
    return form
