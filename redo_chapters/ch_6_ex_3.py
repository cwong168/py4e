'''
Exercise 3:

Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.


word = 'banana'
count = 0


def count(word):
    for letter in word:
        if letter == 'a':
            count = count + 1
            print(count)


count('word')

#print(count('word'))
'''




def count(word, letter):
    clock = 0
    for character in word:
        if character == letter:
            clock = clock + 1
    print(clock)

# count how many 'a' are in banana, you can change word and letter.
#count('banana', 'a')
# trying out other words
count('immutable', 'm')