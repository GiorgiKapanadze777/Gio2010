from turtle  import *  


#we want to point a house

#step 1:  draw a square
begin_fill()
speed(3)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)
end_fill()
#end of square

#drawing door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)    #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(145)
forward(180)
left(112)
forward(180)
end_fill()

#window 1
penup()
goto(170,170)
pendown()
color("black","blue")
begin_fill()
right(57)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()


#window 2
penup()
goto(30,170)
pendown()
color("black","blue")
begin_fill()
right(180)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()


















exitonclick()