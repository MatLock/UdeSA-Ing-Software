from clase_04.Product import *


def create_product(id,product_category, price):
  if product_category == 'food_item':
    return FoodProduct(price, id)
  if product_category == 'cellphone':
    return CellPhoneProduct(price, id)
  if product_category == 'computer':
    return ComputerProduct(price, id)
  if product_category == 'car':
    return CarProduct(price, id)
  if product_category == 'imported_car':
    return ImportedCarProduct(price, id)
  return None
  
  