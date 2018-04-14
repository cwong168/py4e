'''Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.'''



def count(word, letter):
    clock = 0
    for character in word:
        if character == letter:
            clock = clock + 1
    print(clock)


count('apple', 'a')
