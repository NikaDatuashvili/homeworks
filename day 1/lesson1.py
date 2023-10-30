from turtle import*

shape("circle")
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


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)              #drawing a door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()                       #roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
left(30)


penup()
goto(10,120)
left(90)
pendown()
color("brown")
begin_fill()               #left window
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


penup()
goto(190,120)
right(90)
pendown()
color("brown")
begin_fill()               #right window
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()






exitonclick()