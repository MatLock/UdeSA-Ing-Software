import json

class NoneDiscount:
  def __init__(self, discount_rate=1):
        self.discount_rate = discount_rate
  
  def apply_discount(self, total):
      return self.discount_rate * total

class StudentDiscount(NoneDiscount):
  # 10% discount
  def __init__(self, discount_rate=0.9):
      super().__init__(discount_rate)
    
  
      
class BlackFridayDiscount(NoneDiscount):
  #30& discount
  def __init__(self, discount_rate=0.7):
      super().__init__(discount_rate)
      
      
      
