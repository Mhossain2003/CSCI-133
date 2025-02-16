#For this test, you will write a program that performs some analysis of the novel Alice’s Adventures in Wonderland by Lewis Carroll. 
#First, please download the provided file alice.txt, which is the full text of the novel. \
#Then, write a program called test2.py that reads the provided file and reports the following information about it:
#1. The total number of words:

words = 0
with open('alice.txt') as book:
    for line in book:
        words += len(line.split()) 
    print('Total number of words:', words)

#2: The average number of words in a line (total number of words / total number of lines)

lines = 0
with open('alice.txt') as book:
    for line in book:
        lines += 1
    print('Average number of words in a line:', words / lines)

#3: The line with the most words and the number of words in that line:

max_words = 0
total_count = 0
with open('alice.txt') as book:
    for line in book:
        count = len(line.split())
        if count > max_words:
            max_count = line
            total_count = len(max_count.split())
            max_words = count
print('Longest line has', total_count, 'words:', max_count)

#4: The total number of lines in your Python source code

total_lines = 0
with open('test2.py') as program:
    for line in program:
        total_lines += 1
    print('Total number of lines in Python source code:', total_lines)

#5: Provide an interface that allows the user enter a word to look up how many lines contain that word 
#and to see up to the first ten such lines. If no lines contain that word, then your program must output Not found.

intake = input('Enter word: ')
total_intake_words = 0
with open('alice.txt') as book:
    for line in book:
        if intake in line:
            if total_intake_words < 10:
                print(line)
            total_intake_words += 1
if total_intake_words > 0:
    print(total_intake_words, 'lines contain', intake)
else:
    print('Not found.')