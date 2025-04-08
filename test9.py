from tkinter import *
import random

# ---------- Card & Deck Classes ----------
class Card:
    def __init__(self, face, suit):
        self.myFaceValue = face
        self.mySuit = suit

    def faceValue(self):
        return self.myFaceValue

    def suit(self):
        return self.mySuit

    def __str__(self):
        return self.myFaceValue + " of " + self.mySuit

class Deck:
    faceValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'jack', 'queen', 'king', 'ace']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self.theCards = [Card(f, s) for f in Deck.faceValues for s in Deck.suits]
        random.shuffle(self.theCards)

    def deal(self, n):
        return [self.theCards.pop() for i in range(n)]

# ---------- Deal and Evaluate ----------
def deal(n):
    d = Deck()
    return d.deal(n)

def evaluate(hand):
    faces = {}
    for card in hand:
        fv = card.faceValue()
        if fv in faces:
            faces[fv] += 1
        else:
            faces[fv] = 1
    score = 0
    for count in faces.values():
        if count == 2:
            score += 1
        elif count == 3:
            score += 10
        elif count == 4:
            score += 100
    return score

# ---------- Custom Widgets ----------
class enhancedEntry(Frame):
    def __init__(self, parent, prompt, actionText, action):
        Frame.__init__(self, parent)

        self.inputBoxLabel = Label(self, text=prompt)
        self.inputBoxLabel.pack(side=LEFT)

        self.inputBox = Entry(self)
        self.inputBox.pack(side=LEFT)

        self.button = Button(self, text=actionText, command=action)
        self.button.pack(side=LEFT)

    def get(self):
        return self.inputBox.get()

class CardsFrame(Frame):
    def __init__(self, parent, cardList):
        Frame.__init__(self, parent)
        for card in cardList:
            Button(self, text=str(card)).pack()

# ---------- GUI Setup ----------
def makeHand():
    global cardsFrame
    entryText = entry.get()
    if entryText.isdigit():
        n = int(entryText)
        if 0 <= n <= 52:
            hand = deal(n)
            scoreVal = evaluate(hand)
            scoreLabel['text'] = "Score: {}".format(scoreVal)
            if cardsFrame:
                cardsFrame.destroy()
            cardsFrame = CardsFrame(root, hand)
            cardsFrame.pack()

root = Tk()
root.title("Card Hand Evaluator")

cardsFrame = None

entry = enhancedEntry(root, "Number of cards:", "Deal", makeHand)
entry.pack()

scoreLabel = Label(root, text="Score: 0")
scoreLabel.pack()

root.mainloop()
