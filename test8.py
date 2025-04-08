#write a program test8.py that implements a graphical quiz game.
#You are provided with a text file containing quiz questions animals.txt (source) 
#and a module readquiz.py with a function loadQuestions() able to read Yes/No questions from the questions file.

from tkinter import *
import random
import readquiz

# Load questions from the file animals.txt using the module readquiz.py
# You will need at least three global variables: the list of questions, 
# the number of times the player answered, and how many times they were correct:

questions = readquiz.loadQuestions()
total = 0
correct = 0

#Define two functions for the buttons, describing what should happen when the player presses the correct button, 
# and the incorrect one:

def goodAnswer():
    global total, correct
    correct += 1
    total += 1
    status['text'] = "Your answer was correct"
    status['bg'] = 'light green'
    score['text'] = "Score: {}/{}".format(correct, total)
    getNewQuestion()

def badAnswer():
    global total
    total += 1
    status['text'] = "Your answer was incorrect"
    status['bg'] = 'pink'
    score['text'] = "Score: {}/{}".format(correct, total)
    getNewQuestion()

#The function getNewQuestion() should sample a new question, update the question label, 
# and then reassign the ['command'] functions of the buttons. For example, if the question statement is False, 
# then the Yes button should now execute badAnswer, and the No button should now execute goodAnswer.
# So in the proposed solution strategy, each time we update the question, 
# we also update the behavior of the buttons.

def getNewQuestion():
    global current
    current = random.choice(questions)
    question['text'] = current[0]
    if current[1] == True:
        yesButton['command'] = goodAnswer
        noButton['command'] = badAnswer
    else:
        yesButton['command'] = badAnswer
        noButton['command'] = goodAnswer

# Create a Tkinter interface, arranging widgets as close as possible to the following layout 
# (you may use additional Frame widgets to help arrange buttons and labels)
# When creating a label for the quiz question, you may use a Message widget instead of Label 
# to get a multi-line text label. They are created the same way, 
# but for Message you additionally specify its width.

root = Tk()
root.title("Animal Quiz Game")

question = Message(root, width=300)
question['text'] = "Press Yes or No to start!"
question.pack()

frame = Frame(root)
frame.pack()

yesButton = Button(frame, text="Yes", width=10)
yesButton.pack(side=LEFT)

noButton = Button(frame, text="No", width=10)
noButton.pack(side=RIGHT)

bottom = Frame(root)
bottom.pack()

status = Label(bottom, text="Status", width=30)
status.pack(side=LEFT)

score = Label(bottom, text="Score: 0/0", width=15)
score.pack(side=RIGHT)

getNewQuestion()
root.mainloop()
