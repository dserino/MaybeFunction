#!/usr/bin/python

### TODO ###
# everything


import sys

### ANSWER BANK ###
def readAnswerBank(filename):
    answerBank = open(filename,'r')
    # interpret file

    answerBank.close()

### MAIN IMPLEMENTATION ###
if __name__ == "__main__":

    # initialize answer bank
    readAnswerBank("answerBank.txt")

    # initialize RNG

    # loop
    while True:
        
        # prompt user for question
        question = raw_input(">> ")

        # track keywords, help/exit/up arrow/down arrow
        if question == "help":
            print "ask a question to the maybe function"
        elif question == "exit":
            break


        # start timer

        # dissect question

        # determine which answer is appropriate

        # output

        # end timer

        # convert to paulina blinks
        
        pass


