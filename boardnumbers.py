import turtle #Here I am importing turtle

num1=turtle.Turtle()#this is the name for turtle one
num2=turtle.Turtle()#this is the name for turtle two
num3=turtle.Turtle()#this is the name for turtle three
num4=turtle.Turtle()#this is the name for turtle four
num5=turtle.Turtle()#this is the name for turtle five

#My details -----------------------------------------------------------------------------------------------------------------------------------------------------------

num1.penup()
num1.goto(-80, 220)
num1.write('Nahidur Rahman      ID:19028866', font=('Calibri', 12))


num1.goto(-410, 100)
num1.write("To roll the dice press \n   the 'Enter' key in \n   the Python Shell", font=('Calibri', 12))



#This is the module that will write the numbers on my board -----------------------------------------------------------------------------------------------------------

def numbers(): 

#Row 1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    num1.penup() #To prevent the turtle drawing a continuous line
    num1.goto(-90,-105) #the coordinates for the turtle to write the number
    num1.write('1', font=('Calibri', 12), align=('right')) #the style of the font
    num1.goto(-20,-105) #the coordinates for the turtle to write the number
    num1.write('2', font=('Calibri', 12), align=('right')) #the style of the font
    num1.goto(50,-105) #the coordinates for the turtle to write the number
    num1.write('3', font=('Calibri', 12), align=('right')) #the style of the font
    num1.goto(120,-105) #the coordinates for the turtle to write the number
    num1.write('4', font=('Calibri', 12), align=('right')) #the style of the font
    num1.goto(190,-105) #the coordinates for the turtle to write the number
    num1.write('5', font=('Calibri', 12), align=('right')) #the style of the font

#Row 2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    num2.penup() #To prevent the turtle drawing a continuous line
    num2.goto(190,-35) #the coordinates for the turtle to write the number
    num2.write('6', font=('Calibri', 12), align=('right')) #the style of the font
    num2.goto(120,-35) #the coordinates for the turtle to write the number
    num2.write('7', font=('Calibri', 12), align=('right')) #the style of the font
    num2.goto(50,-35) #the coordinates for the turtle to write the number
    num2.write('8', font=('Calibri', 12), align=('right')) #the style of the font
    num2.goto(-20,-35) #the coordinates for the turtle to write the number
    num2.write('9', font=('Calibri', 12), align=('right')) #the style of the font
    num2.goto(-90,-35) #the coordinates for the turtle to write the number
    num2.write('10', font=('Calibri', 12), align=('right')) #the style of the font

#Row 3 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    num3.penup() #To prevent the turtle drawing a continuous line
    num3.goto(-90,35) #the coordinates for the turtle to write the number
    num3.write('11', font=('Calibri', 12), align=('right')) #the style of the font
    num3.goto(-20,35) #the coordinates for the turtle to write the number
    num3.write('12', font=('Calibri', 12), align=('right')) #the style of the font
    num3.goto(50,35) #the coordinates for the turtle to write the number
    num3.write('13', font=('Calibri', 12), align=('right')) #the style of the font
    num3.goto(120,35) #the coordinates for the turtle to write the number
    num3.write('14', font=('Calibri', 12), align=('right')) #the style of the font
    num3.goto(190,35) #the coordinates for the turtle to write the number
    num3.write('15', font=('Calibri', 12), align=('right')) #the style of the font

#Row 4 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    num4.penup() #To prevent the turtle drawing a continuous line
    num4.goto(190,105) #the coordinates for the turtle to write the number
    num4.write('16', font=('Calibri', 12), align=('right')) #the style of the font
    num4.goto(120,105) #the coordinates for the turtle to write the number
    num4.write('17', font=('Calibri', 12), align=('right')) #the style of the font
    num4.goto(50,105) #the coordinates for the turtle to write the number
    num4.write('18', font=('Calibri', 12), align=('right')) #the style of the font
    num4.goto(-20,105) #the coordinates for the turtle to write the number
    num4.write('19', font=('Calibri', 12), align=('right')) #the style of the font
    num4.goto(-90,105) #the coordinates for the turtle to write the number
    num4.write('20', font=('Calibri', 12), align=('right')) #the style of the font

#Row 5 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    num5.penup() #To prevent the turtle drawing a continuous line
    num5.goto(-90,175) #the coordinates for the turtle to write the number
    num5.write('21', font=('Calibri', 12), align=('right')) #the style of the font
    num5.goto(-20,175) #the coordinates for the turtle to write the number
    num5.write('22', font=('Calibri', 12), align=('right')) #the style of the font
    num5.goto(50,175) #the coordinates for the turtle to write the number
    num5.write('23', font=('Calibri', 12), align=('right')) #the style of the font
    num5.goto(120,175) #the coordinates for the turtle to write the number
    num5.write('24', font=('Calibri', 12), align=('right')) #the style of the font
    num5.goto(190,175) #the coordinates for the turtle to write the number
    num5.write('25', font=('Calibri', 12), align=('right')) #the style of the font

#Hiding the turtles ----------------------------------------------------------------------------------------------------------------------------------------------------

num1.hideturtle() 
num2.hideturtle() 
num3.hideturtle() 
num4.hideturtle() 
num5.hideturtle() 

turtle.hideturtle() # I had an extra turtle which I had to hide

numbers() #here I am calling the function
