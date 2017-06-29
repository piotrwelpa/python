import turtle

def draw_square(some_turtle):
    #for i in range(4):
     #   some_turtle.forward(100)
      #  some_turtle.right(90)
    some_turtle.forward(100)
    some_turtle.right(90)
    some_turtle.forward(100)
    some_turtle.right(120)
    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(0)
    for i in range(36):
        draw_square(brad)
        brad.right(10)
    
    window.exitonclick()
    
draw_art()
