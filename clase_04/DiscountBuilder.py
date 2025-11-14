from clase_04.Discount import StudentDiscount, BlackFridayDiscount, NoneDiscount


def create_discount(description):
  if description == 'student':
    return StudentDiscount()
  if description == 'blackfriday':
    return BlackFridayDiscount()
  return NoneDiscount()