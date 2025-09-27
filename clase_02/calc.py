import argparse



def save_file(file_name, result):
  with open(file_name, "w") as f:
    f.write(str(result)+"\n")
    print(f"💾 operation requested saved in file {file_name}")


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
    print(result)
    if args.save:
      save_file(file_name=args.save, result=result)

if __name__ == '__main__':
    execute()
    
    
    