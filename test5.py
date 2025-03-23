#Task: We will write a program for finding the most frequently mentioned usernames in each of the provided files. 
# To correctly identify mentions, we have to cleanup each tweet, keeping only letters, digits, and symbols @ and _. 
# After each tweet is cleaned up, we have to go through its words, and if the word starts with @, it is a mention.
#Step-by-step:
#Modify function cleanedup so that it keeps not only letters, but also digits 0123456789 and symbols @ and _

import os

def cleanedup(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz@_0123456789"
    cleanline = ""
    for character in s.lower():
        if character in alphabet:
            cleanline += character
        else:
            cleanline += ' '
    return cleanline

#Write a new function findMentions that takes a filename as a parameter and reports 3 usernames most frequently mentioned in that file. 
# The function should create a dictionary of counts for all username mentions (words starting with @). 
# After reading through the file and accumulating the counts for all mentioned usernames, use the dictionary to create a list like this:
#  [[15: '@alice'], [20, '@bob'], [7, '@carol'], ... ]
#Use sort to sort the above list and print out 3 most frequently mentioned usernames.

def findMentions(filename):
    counts = {}
    with open(filename, encoding='utf-8') as tweets:
        for line in tweets:
            for word in cleanedup(line).split():
                if word.startswith('@'):
                    counts[word] = counts.get(word, 0) + 1

    mentions = []
    for word in counts:
        mentions.append([counts[word], word])

    mentions.sort()
    mostfrequent = mentions[-3:]

    print(filename)
    for i in range(3):
        user = mostfrequent[i]
        print("    " + user[1], user[0])
    print()

#3. Check each file in the current folder (using os.listdir('.')), if the file name ends with .tweets, 
# call findMentions on the file to find its most frequent mentions.

for filename in os.listdir('.'):
    if filename[-7:] == '.tweets':
        findMentions(filename)