from turtle import Turtle

S_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for position in S_POSITION:
            self.add_segment(position)

    def add_segment(self, position):

        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtle.append(new_turtle)
    def extend(self):

        self.add_segment(self.all_turtle[-1].position())

    def move(self):
        for seg in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[seg - 1].xcor()
            new_y = self.all_turtle[seg - 1].ycor()
            self.all_turtle[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
