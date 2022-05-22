import turtle                                   #here I am importing turtle

board=turtle.Turtle()

#this block is to setup my canvas for turtle to draw my turtle

turtle.title("Nahidur's Snakes and Ladders")    #this is my title
turtle.setup(850, 850, 0, 0)                    #this is the size of the window that pops up to play
turtle.bgcolor('white')                         #this is the background color 
turtle.color('black')                           #this is the colour of the turtle that will draw the border
board.speed(0)                                  #this is the speed of turtle drawing the border
turtle.pendown()                                #this is for the turtle to draw
board.width(3)                                  #this is the thickness for the border of the board
board.penup()
board.goto(-250,-250)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mainboard():                                #this is the name of my module

    
#this module is creating the outer border of the board ----------------------------------------------------------------------------------------------------------------


    for i in range(4):                          #This for loop allowed me to make the outer boarder using less lines of code
        board.pendown()
        board.forward(450)                      #I am moving the board forward by 450
        board.left(90)                          #I am making the board rotate 90 degrees to the left

#this module is creating the columns ----------------------------------------------------------------------------------------------------------------------------------
        
    for j in range(2):                          #This for loop allowed me to make the columns of the board without having to use too many lines of code
        board.forward(90)
        board.left(90)
        board.color('purple')
        board.forward(450)
        board.color('black')
        board.right(90)
        board.forward(90)
        board.right(90)
        board.color('purple')
        board.forward(450)
        board.color('black')
        board.left(90)
    board.penup()                               #To stop the turtle drawing a continuous line 
    board.goto(-250,-160)                       #The turtle is going to these coordinates to start making the rows
    board.pendown()

#this module is creating the rows -------------------------------------------------------------------------------------------------------------------------------------

    for k in range(2):                          #This for loop allowed me to make the rows of the board without also having to use too many lines of code
        board.color('purple')
        board.forward(450)
        board.color('black')
        board.left(90)
        board.forward(90)
        board.left(90)
        board.color('purple')
        board.forward(450)
        board.color('black')
        board.right(90)
        board.forward(90)
        board.right(90)

#this module is where I call my board functions and then hide the turtles ---------------------------------------------------------------------------------------------

mainboard()
turtle.hideturtle()
board.hideturtle()
