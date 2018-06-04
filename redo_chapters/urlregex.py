'''
We add parentheses to our regular expression to indicate which part of our matched string 
we would like to extract, and produce the following program:
'''

# Search for lines that start with From and have an at sign
import urllib.request, urllib.parse, urllib.error
import re

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())