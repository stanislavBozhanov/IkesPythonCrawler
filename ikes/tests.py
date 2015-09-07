# import json
# import pprint
# from django.core.urlresolvers import reverse
# from django.test import TestCase
#
#
#
# class IkesTests(TestCase):
#
#     def test_menu(self):
#         data = {
#             'restaurant': 'c20-ikesls285283',
#             'menu': '38c2f7ff-38f3-4a45-a432-50bcdd7edcde'
#         }
#         url = reverse('menu')
#         response = self.client.get(url, data)
#         print(response.content)
#
#     def test_product_details(self):
#         data_for_form = {
#             'act': 'add',
#             'type': 'product',
#             'merchantid': 'lpIkesCup',
#             'productpath': '449f66d4-0a1a-4f5e-f19c-6813ffe28df5',
#             'checkoutMerchant': 'bHBJa2VzQ3Vw',
#             'sessionId': '1b82fbc1-cbf6-4bb9-a4d5-59d16c6a8628'
#         }
#         data = json.dumps(data_for_form)
#         url = reverse('product_details')
#         response = self.client.get(url, data=data)
#         pp = pprint.PrettyPrinter(indent=4)
#         pp.pprint(response.content)
#
#         self.assertGreater(len(response.content), 0)
#
#
#     def test_full_order(self):
#         data_for_order = {
#             'merchantid': 'lpIkesCup',
#             'productid': 'bd091a04-e7d5-40f4-f2a8-941b73f737dd                     ',
#             'act': 'add',
#             'checkoutMerchant': 'bHBJa2VzQ3Vw',
#             'sessionId': '1b82fbc1-cbf6-4bb9-a4d5-59d16c6a8628',
#             'quantity': 1,
#             'options[bd091a04-e7d5-40f4-f2a8-941b73f737dd][attribs][0:2bd1b2a2-cca0-478f-dd14-dc040806ac26]': '0299a4c4-adf0-4c90-a187-2687c3bb740e',
#             'options[bd091a04-e7d5-40f4-f2a8-941b73f737dd][attribs][0:1]': ''
#         }
#
#
#     def test_make_order(self):
#         data = {
#             'restaurant': 'lpIkesCup',
#             'session': '1b82fbc1-cbf6-4bb9-a4d5-59d16c6a8628',
#             'username': 'stanislav.bozhanov@gmail.com',
#             'password': 'leapsetyoyo91',
#             'order_time': 1441131300,
#             'order_type': 'pickup',
#             'discount_code': '',
#             'first_name': 'Stanislav',
#             'second_name': 'Bozhanov',
#             'phone_1': 414,
#             'phone_2': 323,
#             'phone_3': 1131,
#             'list_with_orders': [
#                 {
#                     'merchantid': 'lpIkesCup',
#                     'productid': 'da0b75cf-032b-47b9-be84-967af3a12715',
#                     'act': 'add',
#                     'checkoutMerchant': 'bHBJa2VzQ3Vw',
#                     'sessionId': 'fb1703d8-bb58-4857-8ab0-3efde549f878',
#                     'quantity': 1,
#                     'options' : {
#                         'options[da0b75cf-032b-47b9-be84-967af3a12715][attribs][0:1]': ''
#                     }
#                 }
#             ],
#             'nameoncard': 'Stanislav Bozhanov',
#             'cctype': 'VISA',
#             'ccnumber': 1111111111111111,
#             'expdatem': 11,
#             'expdatey': 15,
#             'cvvcode': 111,
#             'tippr': 0,
#             'tip': 0.00
#         }
#         url = reverse('make_the_order')
#         self.client.post(url, json.dumps(data), content_type='application/json')
