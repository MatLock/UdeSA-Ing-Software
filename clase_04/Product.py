class Product():
  def __init__(self, price, product_id, tax):
    self.id = product_id
    self.price = price
    self.tax = tax
  
  def calculate_price_with_tax(self):
    return self.price * self.tax
    
  
class FoodProduct(Product):
  def __init__(self, price, product_id):
    super().__init__(price, product_id, 1)
    
    
class CellPhoneProduct(Product):
  def __init__(self, price, product_id):
    super().__init__(price, product_id, 1.56)
    
    
class ComputerProduct(Product):
  def __init__(self, price,product_id):
    super().__init__(price,product_id, 1.56)
    

class CarProduct(Product):
  def __init__(self, price, product_id):
    super().__init__(price, product_id, 1.2)
    

class ImportedCarProduct(Product):
  def __init__(self, price, product_id):
    super().__init__(price, product_id, 1.56)
    
