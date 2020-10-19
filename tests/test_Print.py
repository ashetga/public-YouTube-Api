import sys

print('Hello World!')

print(f'Number of arguments: {len(sys.argv)}, arguments.')
print(f'Argument List: {str(sys.argv)} {len(sys.argv[0])} {len(sys.argv[2])}')
print(f'Matches? {sys.argv[2] == "AIzaSyBlk9y7rqdQEhuEpaZJR5JYgZTtUaziAg4"}')
