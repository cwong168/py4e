'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''

def getfile_contents(filename):
    
    token = 'X-DSPAM-Confidence:'
    # read file and return contents

    contents = ''
    file = open(filename, 'r')
    #contents = file.read()
    for line in file:
        index = line.find(token)

        if index > 0:
            number = line[index+1:]
            
        contents = contents + line.upper()

    file.close()
    return contents

def main():
    filename = input('Enter a file name: ')
    contents = getfile_contents(filename)
    print(contents)

main()
