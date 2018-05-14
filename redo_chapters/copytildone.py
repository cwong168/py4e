'''
 suppose you want to take input from the user until they type done. You could write:

'''


while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')