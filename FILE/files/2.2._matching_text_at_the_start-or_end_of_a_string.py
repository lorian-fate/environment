#PROBLEM: You need to check the start or end of a string for specific text patterns, such as filename extensions, URL scheme, and so on


#===================================== SOLUTION =====================================
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.endswith('dfd'))
print(url.startswith('http:'))
