'''
We can use the find string method to simulate a text editor search that finds lines where the search string is anywhere in the line. 
Since find looks for an occurrence of a string within another string and either returns the position of the string or -1 
if the string was not found, we can write the following loop to show lines which contain the string "@uct.ac.za" 
(i.e., they come from the University of Cape Town in South Africa):
'''

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)