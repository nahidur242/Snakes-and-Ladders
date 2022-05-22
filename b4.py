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
board.goto(-150,-150)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mainboard():                                #this is the name of my module

    
#this module is creating the outer border of the board ----------------------------------------------------------------------------------------------------------------

    for i in range(4):                          #This for loop allowed me to make the outer boarder using less lines of code
        board.pendown()
        board.forward(350)                      #I am moving the board forward by 350
        board.left(90)                          #I am making the board rotate 90 degrees to the left


#this module is creating the columns ----------------------------------------------------------------------------------------------------------------------------------

    for i in range(1):
        board.forward(70)                       #I am moving the board forward by 70
        board.left(90)                          #I am making the board rotate 90 degrees to the left
        board.pencolor("purple")                #I have used the colour 'purple' for aesthetic purposes
        board.forward(350)                      #I am moving the board forward by 350
        board.pencolor("black")                 #I then switch to 'black' to stop the continuation of the use of 'purple' - I repeat this throughout the board
        board.right(90)                         #I am making the board rotate 90 degrees to the right
        board.forward(70)                       #I am moving the board forward by 70
        board.right(90)                         #I am making the board rotate 90 degrees to the right
        board.pencolor("purple")
        board.forward(350)                      #I am moving the board forward by 350
        board.left(90)                          #I am making the board rotate 90 degrees to the left
        board.pencolor("black")
        board.forward(70)                       #I am moving the board forward by 70
        board.left(90)                          #I am making the board rotate 90 degrees to the left
        board.pencolor("purple")
        board.forward(350)                      #I am moving the board forward by 350
        board.pencolor("black")
        board.right(90)                         #I am making the board rotate 90 degrees to the right
        board.forward(70)                       #I am moving the board forward by 70
        board.right(90)                         #I am making the board rotate 90 degrees to the right
        board.pencolor("purple")
        board.forward(350)                      #I am moving the board forward by 350
        board.pencolor("black")
        board.left(90)                          #I am making the board rotate 90 degrees to the left
        board.forward(70)                       #I am moving the board forward by 70
        board.left(90)                          #I am making the board rotate 90 degrees to the left


#this module is creating the rows -------------------------------------------------------------------------------------------------------------------------------------

    for i in range(1):
        board.forward(70)                       
        board.left(90)                          
        board.pencolor("purple")
        board.forward(350)                      
        board.pencolor("black")
        board.right(90)                         
        board.forward(70)                       
        board.right(90)                         
        board.pencolor("purple")
        board.forward(350)                      
        board.pencolor("black")
        board.left(90)                          
        board.forward(70)                       
        board.left(90)                          
        board.pencolor("purple")
        board.forward(350)
        board.right(90) 
        board.pencolor("black")
        board.forward(70)                       
        board.right(90) 
        board.pencolor("purple")
        board.forward(350) 
        board.pencolor("black")
        board.left(90) 
        board.forward(70)                       
        board.left(90)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

board.hideturtle()                              #this is to hide the board's cursor after it has finished drawing the board
turtle.hideturtle()    
mainboard()                                     #this is calling the mainboard function

    
    
