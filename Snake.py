from turtle import Turtle, Screen


STARTING_POSITIONS = [(0, 0), (20, 0), (40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        # To create snake immediately
        self.create_snake()

    def create_snake(self):
        for s in STARTING_POSITIONS:
            self.addsegment(s)

    def forward(self):
        for i in range(len(self.segment)-1, 0, -1):
            self.segment[i].goto(self.segment[i-1].xcor(),
                                 self.segment[i-1].ycor())
        self.segment[0].fd(20)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def addsegment(self, position):
        t = Turtle("square")
        t.penup()
        t.goto(position)
        self.segment.append(t)

    def atefood(self):
        self.addsegment(self.segment[-1].position())

    def new_game(self):
        for segment in self.segment:
            segment.goto(12312, 12312)
        self.segment.clear()
        self.create_snake()
