import turtle
import random
import time

# Game settings
delay = 0.1
score = 0
high_score = 0
bodies = []

# Create the screen
s1 = turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("black")
s1.setup(width=600, height=600)

# Create the snake head
head = turtle.Turtle()
head.shape("circle")
head.color("white")
head.fillcolor("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"
head.speed(0)  # Fastest animation speed

# Create the food
food = turtle.Turtle()
food.shape("square")
food.color("green")
food.penup()
food.goto(100, 100)
food.speed(0)

# Create the scoreboard
score_board = turtle.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(-280, 250)
score_board.color("white")
score_board.write("Score: 0 | Highest Score: 0", align="left", font=("Arial", 24, "normal"))

# Functions to move the snake
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# Event handling
s1.listen()
s1.onkeypress(moveup, "Up")
s1.onkeypress(movedown, "Down")
s1.onkeypress(moveleft, "Left")
s1.onkeypress(moveright, "Right")
s1.onkeypress(movestop, "space")

# Main game loop
while True:
    s1.update()  # Update the screen

    # Check for collision with borders (wrap around)
    if head.xcor() > 280:
        head.setx(-280)
    elif head.xcor() < -280:
        head.setx(280)
    if head.ycor() > 280:
        head.sety(-280)
    elif head.ycor() < -280:
        head.sety(280)

    # Check for collision with food
    if head.distance(food) < 20:
        # Move food to a random position
        x = random.randint(-280, 280) // 20 * 20  # Align to grid
        y = random.randint(-280, 280) // 20 * 20  # Align to grid
        food.goto(x, y)

        # Add a new body segment
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("white")
        new_body.fillcolor("white")
        new_body.penup()
        bodies.append(new_body)

        # Update score
        score += 10
        if score > high_score:
            high_score = score
        score_board.clear()
        score_board.write(f"Score: {score} | Highest Score: {high_score}", align="left", font=("Arial", 24, "normal"))

        # Increase speed (cap at 0.05 to avoid being too fast)
        delay = max(0.05, delay - 0.005)

    # Move the snake body
    for i in range(len(bodies) - 1, 0, -1):
        bodies[i].goto(bodies[i - 1].xcor(), bodies[i - 1].ycor())
    if bodies:
        bodies[0].goto(head.xcor(), head.ycor())

    # Move the head
    move()

    # Check for collision with snake body
    for b in bodies[1:]:  # Skip the first segment to avoid false collision
        if head.distance(b) < 20:
            time.sleep(1)  # Pause briefly
            # Reset game state
            head.goto(0, 0)
            head.direction = "stop"
            for body in bodies:
                body.hideturtle()  # Hide all body segments
            bodies.clear()  # Clear the body list
            score = 0  # Reset score
            delay = 0.1  # Reset delay
            score_board.clear()
            score_board.write(f"Score: {score} | Highest Score: {high_score}", align="left", font=("Arial", 24, "normal"))

    time.sleep(delay)

s1.mainloop()