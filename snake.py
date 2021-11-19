from turtle import Turtle


class Snake:
    def snake(self):
        # create three separate turtles in a line. they should be white squares. turtles are 20x20 pixels.

        starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        segments = []

        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            segments.append(new_segment)

        return segments

    def move(self):
        # segment[0] is not included in the for loop. it moves independently of the other segments.
        # then the segments in the for loop will follow the first segment.
        # move the snake forward
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)