import json

from clase_04.DiscountBuilder import create_discount
from clase_04.ProductBuilder import create_product


def calculate_invoice(products, eligible_discount):
  subtotal = sum([product.calculate_price_with_tax() for product in products])
  return subtotal, eligible_discount.apply_discount(subtotal)


''' sin strategy, (sin haber creado las clases como diseniando el strategy). Entonces tomaria directamente el json '''
''' en comparacion con la version strategy. Fijense que puedo agregar mas tipos de producto con distintos impuesto
    y distintos descuentos, que la funcion que calcula el total no cambia. En cambio, la version de strategy seria muy
    afectada. ademas de que seria imposible de seguir
'''
def calculate_invoice_no_strategy(product_list, discount):
  subtotal = 0
  for product in product_list:
    if product['product_category'] == 'food_item':
      subtotal = subtotal + product['price'] * 1 # sin impuesto
    if product['product_category'] == 'imported_car':
      subtotal = subtotal + product['price'] * 1.56 #impuesto 30%
    # ... asi con cada tipo de producto
  total = 0
  if discount == 'student':
    total = subtotal * 0.9 #10% de descuento
  if discount == 'black_friday':
    total = subtotal * 0.7 #30% descuento
  return subtotal, total



if __name__ == '__main__':
  with open('resources.json', 'r') as f:
    input = json.load(f)
    items = input['items']
    discount = create_discount(input['discount'])
    product_list = list(map(lambda item: create_product(item['id'], item['product_category'], item['price']), input['items']))
    subtotal, eligible_discount = calculate_invoice(product_list, discount)
    print(f"strategy subtotal = {subtotal}")
    print(f"strategy discount = {eligible_discount}")
    
    ######## SIN STRATEGY
    n_subtotal, n_total = calculate_invoice_no_strategy(input['items'], input['discount'])
    print(f"sin strategy subtotal = {n_subtotal}")
    print(f"sin strategy discount = {n_total}")