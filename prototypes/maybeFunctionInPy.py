#!/usr/bin/python

### TODO ###
# everything


### IMPORTS ###
import sys
import random as rng
import curses

### ANSWER BANK ###
def readAnswerBank(filename):
    # open file
    answerBank = open(filename,'r')

    answers = []
    
    # interpret file
    isStarted = False

    for line in answerBank:
        # determine when to start and stop
        # scanning file 
        if line[0:4] == "$end":
            break
        elif line[0:6] == "$start":
            isStarted = True
            continue


        if isStarted:
            # don't append if first space is blank
            if line[0] == " ":
                continue

            # don't append comments
            ind = line.find("#")

            if ind == -1:
                # no comment found
                answers.append(line)
            elif ind == 0:
                # whole line is commented
                continue
            else:
                # part of the line is commented
                answers.append(line[0:ind])

    # close files
    answerBank.close()

    # return answers
    return answers

### LANGUAGE PROCESSING ###

# statistical based approach ideas
# pair words with answers,
# Ben in question increases likelihood of Ben in answer


# hard coded approach ideas
# 'what? question' - answer cannot be yes or no


### MAIN IMPLEMENTATION ###
if __name__ == "__main__":

    # print software info
    screen = curses.initscr()
    screen.addstr("--- The Maybe Function ---\n")
    screen.refresh()
    
    # initialize answer bank
    answers = readAnswerBank("answerBank.txt")
    N = len(answers)-1

    
    # loop
    while True:

        # seed rng
        rng.seed()
        
        # prompt user for question
        question = raw_input(">> ")
        # screen.addstr(">> ")
        # screen.refresh()

        # question = screen.getch()
        # screen.addstr(question)
        # screend.refresh()
        
        # track keywords, help/exit/up arrow/down arrow
        if question == "help":
            print "ask a question to the maybe function"
        elif question == "exit":
            break

        # start timer

        # dissect question

        # determine which answer is appropriate
        ind = rng.randint(0,N)
        answer = answers[ind]
        
        # output
        print answer,
        
        # end timer

        # convert to paulina blinks
        

    curses.endwin()

