""" stoplight.py -- an event-driven implementation of the
canonical finite state machine (FSM) example.

This code is an edited and extended copy of what was presented
in __How to Think Like a Computer Scientist__ by Peter Wentworth,
Jeffrey Elkner, Allen B. Downey, and Chris Meyers (Oct. 2012).
http://openbookproject.net/thinkcs/python/english3e/events.html

If you want to play with Python Turtle, a good reference to the
basics can be found at:
https://realpython.com/beginners-guide-python-turtle/
"""

import turtle

# Initialize our turtle world.
wn = turtle.Screen()     # get a reference to the turtle window
wn.setup(400, 500)       # set the window size
wn.title("A FSM implementing a traffic light")
wn.bgcolor("lightblue")
tess = turtle.Turtle()   # create our main turtle


def draw_housing():
    """ Draws a nice housing to hold the traffic lights """
    # Move Tess so the light is centered.
    tess.penup()
    tess.goto(-40, -120)
    tess.pendown()

    # Draw the housing.
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def draw_lights():
    """ Draws the three lights within the housing.
    Assumes Tess starts at the lower lefthand corner of the
    housing.  Leaves Tess's position unchanged. """
    # Draw the green light off, using a cloned turtle.
    g = tess.clone()
    g.penup()
    g.forward(40)
    g.left(90)
    g.forward(50)
    g.shape("circle")
    g.shapesize(3)
    g.fillcolor("darkgrey")

    # Draw the orange light off.
    y = tess.clone()
    y.penup()
    y.forward(40)
    y.left(90)
    y.forward(120)
    y.shape("circle")
    y.shapesize(3)
    y.fillcolor("darkgrey")

    # Draw the red light off.
    r = tess.clone()
    r.penup()
    r.forward(40)
    r.left(90)
    r.forward(190)
    r.shape("circle")
    r.shapesize(3)
    r.fillcolor("darkgrey")


draw_housing()
draw_lights()

tess.penup()
# Position Tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn Tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
tess.speed(10)


def advance_stoplight():
    """ A traffic light is a state machine with three states,
    Green, Orange, Red.  When the machine changes state, we move 
    Tess and change her fillcolor. """
    global current_state

    if current_state == 'Green':
        tess.penup()
        tess.forward(70)
        tess.pendown()
        tess.fillcolor("orange")
        current_state = 'Orange'
        wn.ontimer(advance_stoplight, 2000)

    elif current_state == 'Orange':
        tess.penup()
        tess.forward(70)
        tess.pendown()
        tess.fillcolor("red")
        current_state = 'Red'
        wn.ontimer(advance_stoplight, 5000)

    elif current_state == 'Red':
        tess.penup()
        tess.back(140)
        tess.pendown()
        tess.fillcolor("green")
        current_state = 'Green'
        wn.ontimer(advance_stoplight, 5000)
        
    else:
        # Attempted transition to an unknown state
        raise ValueError


# Start the stoplight.
current_state = 'Green'
wn.ontimer(advance_stoplight, 5000)
wn.mainloop()