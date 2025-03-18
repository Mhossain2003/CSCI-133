#Task: Write a program called test3.py that reads the provided file and reports the following information about Elon Musk’s tweets:
#1: The total number of tweets

total_tweets = 0
with open('elon-musk.txt') as tweets:
    for line in tweets:
        total_tweets += 1
    print('Number of tweets:', total_tweets)

#2: The tweet that contains the most words (don’t use cleanedup for preprocessing here)

max_words = 0
with open('elon-musk.txt') as tweets:
    for line in tweets:
        count = len(line.split())
        if count > max_words:
            max_count = line
            max_words = count
print('Tweet with max number of words:', max_count)

#3: Finally, a username is a word that starts with an @ symbol (for example, @MarkTwain). 
# For simplicity, we will assume that any word that contains @ at any position is a username (that is, consider Mark@Twain or @Mark@Twain@ to be valid usernames). 
# Your program should compile the information on how many times different usernames are mentioned in Elon Musk’s tweets, 
# then provide an interface that allows a user to quickly look up how many times any particular username is mentioned.
total_username = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz@'
with open('elon-musk.txt') as tweets:
    max_tweets = ''
    max_word_count = 0
    for line in tweets:
        line = line.lower()
        cleaned_line = ''
        for character in line:
            if character in alphabet:
                cleaned_line += character
            else:
                cleaned_line += ' '

        words = cleaned_line.split()
        word_count = len(words)
        if word_count > max_word_count:
            max_word_count = word_count
            max_tweets = line
        for word in words:
            if "@" in word:
                if word in total_username:
                    total_username[word] += 1
                else:
                    total_username[word] = 1
while True:
    username = input('Enter username: ')
    if username in total_username:
        print('Mentioned', total_username[username], 'times.')
    else:
        print('Not mentioned.')