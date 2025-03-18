#Write a program called test4.py that plays the following card game:
# The game starts with certain initial amount of dollars.
# At each round of the game, instead of flipping a coin, the player shuffles a deck and draws 6 cards. 
# If the drawn hand contains at least one ace, the player gains a dollar, otherwise they lose a dollar.
# The game runs until the player either runs out of money or doubles their initial amount.
# To test the game, given the initial amount, run it 1000 times to determine how many rounds does the game last on average.
# Provide a user with an interface to enter the initial bankroll. 
# For each entered number, the program should respond with the average duration of the game for that initial bankroll.

import cards

def oneGame(initial):
    rounds = 0
    bankroll = initial
    while (bankroll > 0) and (bankroll < 2 * initial):
        deck = cards.shuffledDeck()
        rounds += 1
        cardFound = False
        for number in range(6):
            if cards.faceValueOf(deck.pop()) == "ace":
                cardFound = True
        if cardFound:
            bankroll += 1
        else:
            bankroll -= 1
    return rounds

def average(initial):
    for initial in initialValues:
        totalRounds = 0
        for number in range(1000):
            totalRounds += oneGame(initial)
        print('Enter initial amount:', initial)
        print('Average number of rounds:', totalRounds / 1000) 

initialValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
average(initialValues)
