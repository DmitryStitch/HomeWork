import numpy as np
import requests

a = np.arange(15)
print(a)

s = slice(3, 12, 2)
print(a[s])

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11],[12, 13, 14]])
print ('Массивы:')
print (x)
print ('\n')
print ('Элементы в массивах больше 5:')
print (x[x > 5])

requests.get('https://github.com/')
response = requests.get('https://github.com/')
print(response.status_code)
print(response.headers)
print(response.headers['Date'])

url = 'https://github.com/'
response = requests.options(url)
print(response.url)


