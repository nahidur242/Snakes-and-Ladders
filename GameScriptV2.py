from turtle import *                                            # Here I am importing turtle
import random                                                   # I am importing random to help me generate a randomised dice function


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#random.randint(1,6) 1 is for the minimum and 6 being the max amount someone can roll on the game's dice


                          
def dice_roll():                                                # this is my dice roll function
    return random.randint(1,6)
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def init():
    vis = Screen()                                              # Here I am using 'vis' to be classified as my new screen                        

    bull = Turtle()                                             # Here I am initialising a new Turtle object as bull
    bull.penup()                                                # To stop the turtle drawing a continuous line I used penup()


    vis.addshape("bull.gif")                                    # This is adding the bull to the screen
    # print(vis.getshapes()) --> For debug
    bull.shape("bull.gif")
    bull.speed(2)
    bull.goto(-122,-125)

    cow = Turtle()                                              # Here I am initialising a new Turtle object as cow
    cow.penup()
    vis.addshape("cow.gif")
    # print(vis.getshapes()) --> Debug
    cow.shape("cow.gif")
    cow.speed(2)
    cow.goto(-122,-100)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    dice = Turtle()                                             # Here I am initialising a new Turtle object as the dice
    dice.penup()                                                # I am setting up its parameters for where its location will be
    dice.goto(-350,35)
    dice.speed(0)


    dice1 = Turtle()                                            # For the 6 rolls on dice, I introduced 6 new turtles to help me import and display the picture
    vis.addshape("dice1.gif")                                   # of which dice will show when the dice is rolled
    print(vis.getshapes())
    dice1.shape("dice1.gif")
    dice1.speed(0)
    dice1.penup()
    dice1.goto(-350,35)

    dice2 = Turtle()
    vis.addshape("dice2.gif")
    print(vis.getshapes())
    dice2.shape("dice2.gif")
    dice2.speed(0)
    dice2.penup()
    dice2.goto(-350,35)

    dice3 = Turtle()
    vis.addshape("dice3.gif")
    print(vis.getshapes())
    dice3.shape("dice3.gif")
    dice3.speed(0)
    dice3.penup()
    dice3.goto(-350,35)

    dice4 = Turtle()
    vis.addshape("dice4.gif")
    print(vis.getshapes())
    dice4.shape("dice4.gif")
    dice4.speed(0)
    dice4.penup()
    dice4.goto(-350,35)

    dice5 = Turtle()
    vis.addshape("dice5.gif")
    print(vis.getshapes())
    dice5.shape("dice5.gif")
    dice5.speed(0)
    dice5.penup()
    dice5.goto(-350,35)

    dice6 = Turtle()
    vis.addshape("dice6.gif")
    print(vis.getshapes())
    dice6.shape("dice6.gif")
    dice6.speed(0)
    dice6.penup()
    dice6.goto(-350,35)


    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    game(bull, cow, dice)


                                                    # Here I am defining the the head, tail and the drop of each snake: for example '8' being the head, 
snakes = [[8, 3, 1],                                # '3' being the tail and 1 being the drop if it drops you by one row, the drop is 1
          [24, 17, 1],
          [20, 1, 3]]

ladders = [[5, 15, 2],                              #Here I am defining the the head, tail and the drop of each ladder: for example '15' being the top of the ladder,  
           [9, 12, 1],                              # '5' being the bottom and '2' being if it raises you by two rows, the character rises by 2
           [18, 23, 1]]

def make_a_move(n, roll, player, direction):        # n is the current grid position (just a counter of all the dice rolls and adjust for snakes and ladders),

    vis = Screen()
    winner = Turtle()
    vis.addshape("win.gif")
    print(vis.getshapes())


                                                    # player is the Turtle object (so input the cow or bull objects here), 
                                                    # direction is the direction (1 for right, -1 for left)
    for i in range(roll):
        if n % 5 == 0:  # Are we on an edge? ----- This for loop will be used for the change in direcrtion when the player is going up the board 
            print("I'm on an edge?")
            player.left(90 * direction)     # If we are going left, the direction is 1 so we make a left turn to go upwards...
                                            # If instead we are going right, direction is -1 so we make a -90 left turn... which is just a right turn!
            player.forward(70)              # Move to the block above
            player.left(90 * direction)     # Same idea as above!
            direction *= -1                 # I swapped the direction variable! Just need to multiply by -1 to swap them

        else:
            player.forward(70)

        
        n += 1                              # this adds one everytime!

        if n >=25:
            player.forward(0)


        
        if n == 25:                         #Now... did I win?! ----- So if the player lands on the 25th square python will display the 'Win' gif
            print("We have a winner!")
            winner.shape("win.gif")
            exit()                          #As the gif is shown, python will exit immediately
            



    for snake in snakes:                    # Iterate through each snake
        if n == snake[0]:                   # When you land on a snake 
            n = snake[1]                    # Get demoted! I change n to match the tail coordinate of the snake

            player.right(90 * direction)    # Point downwards...
            player.forward(70 * snake[2])   # ... then move down by the length of the snake
            print("Snake height", snake[2])
            if snake[2] % 2 != 0:           # Is the drop height odd? If so, the travelling direction swaps
                direction *= -1             # We do that in the same way as before
            
            player.left(90 * direction)     # And correct the turtle heads towards the correct direction 

    for ladder in ladders:                  # Same idea as before but for the ladders...
        if n == ladder[0]:                  # When you go up a ladder
            n = ladder[1]                   # Get promoted! I change n to match the tail coordinate of the ladder
            print("Yay")
            print(direction)

            player.left(90 * direction)     # Point upwards...
            player.forward(70 * ladder[2])  # ... then move up by the length of the ladder!
            print("Ladder height", ladder[2])
            if ladder[2] % 2 != 0:          # Is the rise height odd? If so, the travelling direction swaps
                direction *= -1

            player.right(90 * direction)     # And correct the turtle heads towards the correct direction 



    # Returning to the iterator block
    return n, direction


def game(bull, cow, dice):
        
    direction_bull = 1                  # Both the bull and cow start off going to the right, from above you can see 1 is defined as right
    direction_cow = 1
    n_bull = 1                          # Both the bull and cow start off at square 1
    n_cow = 1

    while True:                         # Repeat this thing forever until you have a winner

        # Starting with the bull
        input("Please hit ENTER to roll the dice!")
        roll = dice_roll()
        print("You rolled:", roll)
        dice.shape(f"dice{roll}.gif")   # Changes the shape to match the rolled number - Syntax is called f-strings

        # Running the function above and update the bull's coordinate and direction!
        n_bull, direction_bull = make_a_move(n_bull, roll, bull, direction_bull)        
        print(n_bull)
        print(direction_bull)

        # Now for the cow
        input("Please hit ENTER to roll the dice!")
        roll = dice_roll()
        print("You rolled:", roll)
        dice.shape(f"dice{roll}.gif")
        
        n_cow, direction_cow = make_a_move(n_cow, roll, cow, direction_cow)
