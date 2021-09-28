#PROBLEM: You need to split a string into fields, but the delimiters (and spacing around them) arent consistent throughout the string


#===================================== SOLUTION =====================================
import re

line = 'asdf fjkl; afed, fjek, asdf,      foo'

a = re.split(r'[;,\s]\s*', line)
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)


print("coma", "\s")