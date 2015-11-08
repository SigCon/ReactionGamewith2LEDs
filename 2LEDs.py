import time
import random
from datetime import datetime
import RPi.GPIO as GPIO

# set a score for each player
scores = [0, 0]
listoftimes = []
names = []

# Say who won
def wingame(player):
    """The function wingame accepts the player who won as the only parameter
    player = index number of array names, 0 = left player, 1 = right player, based on order of input with raw_input
    """
    print names[player] + ' won!'
    scores[player] += 1
    # if player == 0:
    #    GPIO.output(leftGreenLED, 1)
    # else:
    #     GPIO.output(rightGreenLED, 1)

def printline(repetition):
    output = '---' * repetition
    print output

# Print date and time
def printdate(repetition):
    '''The function printdate accepts the number
    of repetitions for the '---' string as the only parameter'''
    now = datetime.now()
    print '%s-%s-%s %s:%s:%s' % (now.day, now.month, now.year, now.hour, now.minute, now.second)
    printline(repetition)

def printscore():
    print ""
    print ''
    print "Scores:"
    print "  " + names[0] + ": " + str(scores[0])
    print "  " + names[1] + ": " + str(scores[1])
    print "The LED went out after the following times in seconds: " + str(listoftimes)

print printdate(6)

# Make sure the GPIO pins are ready
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

# Choose which GPIO pins to use
TimeLED = 23
rightButton = 3
leftButton = 5
leftGreenLED = 19
rightGreenLED = 21

# Set the buttons as input and the LED as an output
GPIO.setup(TimeLED, GPIO.OUT)
GPIO.setup(leftGreenLED, GPIO.OUT)
GPIO.setup(rightGreenLED, GPIO.OUT)
GPIO.setup(rightButton, GPIO.IN)
GPIO.setup(leftButton, GPIO.IN)

# Find out the names of the players
leftPlayerName = raw_input("What is the left player's name? ")
rightPlayerName = raw_input("What is the right player's name? ")
numberOfGames = int(raw_input("How many games do you want to play? "))
printline(10)

# Put the names in a list
names = [leftPlayerName, rightPlayerName]

# Play all the games
for game in range(0, numberOfGames):
    # make sure the green LEDs are off
    GPIO.output(leftGreenLED, 0)
    GPIO.output(rightGreenLED, 0)
    printline(6)
    print 'Game ' + str(game +1) + ' out of ' + str(numberOfGames)
    # Turn the TimeLED on
    GPIO.output(TimeLED, 1)

    # Generate a random time the led will be on
    randnumber = int(random.uniform(1, 5))
    # randnumber = random.uniform(1, 5)
    listoftimes.append(randnumber)
    # print randnumber
    print ''

    # Wait for a random length of time, between 1 and 5 seconds
    time.sleep(randnumber)

    '''One odd thing is that the buttons are on if they are not pressed and off when they are. This is why
    the code says 'Left button pressed' when it finds that 'leftButton' is 'False'.
    '''

    # Check to see if a button is pressed
    # If so, the other player wins
    if GPIO.input(leftButton) == False:
        print names[0] + " cheated!!!"
        wingame(1)
    elif GPIO.input(rightButton) == False:
        print names[1] + " cheated!!!"
        wingame(0)
    else:
        # Turn the led off
        GPIO.output(TimeLED, 0)
        # Wait until a button has been pressed
        # while GPIO.input(leftButton) and GPIO.input(rightButton):
        #      pass # Do nothing!
        # See if the left button has been pressed
        if GPIO.input(leftButton) == False:
            wingame(0)
        # See if the right button has been pressed
        if GPIO.input(rightButton) == False:
            wingame(1)

printscore()

# answerEndGame = raw_input("Do you want to end the game? (y/n) ")
# if answerEndGame == "y":
    # Cleanup
#    GPIO.cleanup()
# else:
#     pass


