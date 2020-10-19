import sys
import os

print('Hello World!')

print(f'Number of arguments: {len(sys.argv)}, arguments.')
print(f'Argument List: {str(sys.argv)} {len(sys.argv[0])} {len(sys.argv[2])}')
print(f'Matches? {sys.argv[2] == "AIzaSyBlk9y7rqdQEhuEpaZJR5JYgZTtUaziAg4"}')

API_KEY = os.getenv('API_KEY')
print(f'API_KEY: {API_KEY} {len(API_KEY)}')
print(f'Matches? {API_KEY == "AIzaSyBlk9y7rqdQEhuEpaZJR5JYgZTtUaziAg4"}')
