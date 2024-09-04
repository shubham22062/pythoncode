import turtle
import time

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.title("Analog Clock")

# Create a turtle to draw the clock
clock = turtle.Turtle()
clock.speed(0)
clock.hideturtle()
clock.pensize(3)

# Draw the clock face
def draw_clock(radius):
    # Draw the outer circle
    clock.penup()
    clock.goto(0, -radius)
    clock.pendown()
    clock.circle(radius)

    # Draw the hour marks
    clock.penup()
    clock.goto(0, 0)
    for hour in range(12):
        clock.penup()
        angle = hour * 30
        clock.setheading(angle)
        clock.forward(radius - 20)
        clock.pendown()
        clock.forward(20)
        clock.penup()
        clock.goto(0, 0)

    # Draw the center of the clock
    clock.penup()
    clock.goto(0, 0)
    clock.dot(12)

# Draw the clock hands
def draw_hand(length, angle):
    clock.penup()
    clock.goto(0, 0)
    clock.setheading(angle)
    clock.pendown()
    clock.forward(length)
    clock.penup()
    clock.goto(0, 0)

# Update the clock hands
def update_time():
    while True:
        clock.clear()

        # Draw the clock face with a radius of 210 units
        draw_clock(210)

        # Get the current time
        hours = int(time.strftime("%I"))
        minutes = int(time.strftime("%M"))
        seconds = int(time.strftime("%S"))

        # Calculate the angles of the hands
        second_angle = 6 * seconds
        minute_angle = 6 * minutes + seconds / 10
        hour_angle = 30 * hours + minutes / 2

        # Draw the hands
        draw_hand(100, hour_angle)    # Hour hand
        draw_hand(150, minute_angle)  # Minute hand
        draw_hand(170, second_angle)  # Second hand

        # Update every second
        time.sleep(1)
        wn.update()

# Set the tracer to 0 to manually update the screen
wn.tracer(0)

# Start the clock
update_time()

# Keep the window open
wn.mainloop()
