import argparse

def main():
    parser = argparse.ArgumentParser(description="Process some inputs with different operations.")
    
    subparsers = parser.add_subparsers(dest='command', required=True, help='Available commands')
    
    sum_parser = subparsers.add_parser('sum', help='Sum all the provided numbers')
    sum_parser.add_argument('numbers', type=float, nargs='+', help='Numbers to sum')
    
    reverse_parser = subparsers.add_parser('reverse', help='Reverse the provided text')
    reverse_parser.add_argument('text', nargs='+', help='Text to reverse')
    
    args = parser.parse_args()
    
    if args.command == 'sum':
        total = sum(args.numbers)
        print(f"The sum is: {total}")
    elif args.command == 'reverse':
        reversed_text = ' '.join(args.text)[::-1]
        print(f"Reversed text: {reversed_text}")

if __name__ == "__main__":
    main()