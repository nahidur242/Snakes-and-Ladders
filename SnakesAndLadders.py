from turtle import *                        #I am importing turtle this way to allow me to add my chosen gifs
vis = Screen()                              #'vis' stands for visual and I used this to help me import my gifs

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def snakes():                               #This the module for my snakes
    snake1 = Turtle()
    vis.addshape("snake.gif")               #This command is used to add in the picture of the snake
    print(vis.getshapes())                  #This command prints the picture of the snake onto the board
    snake1.shape("snake.gif")               #To make the turtle into the shape of my gif I used this command
    snake1.speed(0)                         #This is the speed of the snake being imported

    snake2 = Turtle()                       #I repeated the same lines of codes for the other 2 snakes that I will use in my game
    vis.addshape("snake2.gif")
    print(vis.getshapes())
    snake2.shape("snake2.gif")
    snake2.speed(0)

    snake3 = Turtle()
    vis.addshape("snake3.gif")
    print(vis.getshapes())
    snake3.shape("snake3.gif")
    snake3.speed(0)

    snake1.penup()
    snake1.goto(90,128)
    snake2.penup()
    snake2.goto(25,-75)
    snake3.penup()
    snake3.goto(-125,5)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ladders():                              #This is the module for my ladders
    ladder1 = Turtle()                      #I reused the same format of code for my ladders due to the idea of importing images
    vis.addshape("ladder.gif")              #I repeated this for my other 2 ladders
    print(vis.getshapes())
    ladder1.shape("ladder.gif")
    ladder1.speed(0)

    ladder2 = Turtle()
    vis.addshape("ladder2.gif")
    print(vis.getshapes())
    ladder2.shape("ladder2.gif")
    ladder2.speed(0)

    ladder3 = Turtle()
    vis.addshape("ladder3.gif")
    print(vis.getshapes())
    ladder3.shape("ladder3.gif")
    ladder3.speed(0)

    ladder1.penup()
    ladder1.goto(-60,-10)
    ladder2.penup()
    ladder2.goto(10,125)
    ladder3.penup()
    ladder3.goto(155,-50)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
snakes()                                    #Here I am calling my module for my snakes
ladders()                                   #Here I am calling my module for my ladders
