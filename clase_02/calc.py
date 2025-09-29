import argparse

'''
helper function to save content in given filepath
'''
def save_file(file_path, result):
  with open(file_path, "w") as f:
    f.write(str(result) + "\n")
    print(f"💾 operation requested saved in file {file_path}")


'''
given two numbers 'a' and 'b' returns string with division result
'''
def div(a, b):
  return f'{a} / {b} = {a / b}'


'''
given two numbers 'a' and 'b' returns string with sum result
'''
def sum(a,b):
  return f'{a} + {b} = {a + b}'



'''
given two numbers 'a' and 'b' returns string with multiplication result
'''
def mul(a, b):
  return f'{a} * {b} = {a * b}'



'''
given two numbers 'a' and 'b' returns string with substraction result
'''
def sub(a, b):
  return f'{a} - {b} = {a - b}'

'''
functions that parses cli command and execute operations requested
'''
def execute():
  parser = argparse.ArgumentParser(description='calculator')
  parser.add_argument('first_number', type=int, help='first number')
  parser.add_argument('second_number', type=int, help='second number')
  parser.add_argument('--op', choices=['+', '-', '*', '/'], help='operation')
  parser.add_argument('--save', help='result file')
  args = parser.parse_args()
  


  result = ''
  if args.op == '+':
    result = f'{args.first_number} + {args.second_number} = {args.first_number + args.second_number}'
  if args.op == '*':
    result = mul(a=args.first_number, b=args.second_number)
  if args.op == '/':
    result = div(a=args.first_number, b=args.second_number)
  if args.op == '-':
    result = sub(a=args.first_number, b=args.second_number)
  print(result)
  if args.save:
    save_file(file_path=args.save, result=result)


if __name__ == '__main__':
  execute()
