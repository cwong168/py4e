'''
Exercise 1: [wordlist2]

Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn't matter what the values are. 
Then you can use the in operator as a fast way to check whether a string is in the dictionary.

'''

word_list = dict()
file = open('words.txt')
for word in file:
    item = word.strip()
    oldcount = word_list.get(word,0)
    print(word,'old',oldcount)
    newcount = oldcount + 1
    word_list[word] = newcount
    print(word,'new', newcount)
    #print(word,word_list.get(word,-99))
    #word_list[item] = True
    #vals = list(word_list())

#print(word_list)
#vals = list(word_list())

check_word = input('Type in a word to check if in dictionary:',)

if check_word in word_list:
#if check_word in vals:
    print(check_word + ' is in dictionary')
else:
    print(check_word + ' is not in dictionary')


#'Day' in word_list
#print(word_list['Apple'])   


#list_lenght = len(word_list)
#print(list_lenght)
#word_list.sort()
#print(word_list)
