'''
The equivalent code to read the romeo.txt file from the web using urllib is as follows:
'''

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())