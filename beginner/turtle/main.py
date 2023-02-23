import turtle as t
import random
import colorgram

lewiz_turtle = t.Turtle()
t.colormode(255)

# lewiz_turtle.shape("turtle")
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# !hirst paintings
# lewiz_turtle.penup()
# lewiz_turtle.hideturtle()
# extracted_colors = [(250, 249, 248), (236, 230, 233), (234, 242, 238), (228, 235, 241), (236, 34, 109), (
#     162, 19, 67), (234, 171, 44), (5, 147, 93), (240, 72, 33), (185, 158, 34), (21, 122, 191), (44, 190, 232)]

# lewiz_turtle.setheading(225)
# lewiz_turtle.forward(300)
# lewiz_turtle.setheading(225)

# number_of_dats = 100

# for dots_count in range(number_of_dats + 1):
#     lewiz_turtle.dot(20, random.choice(extracted_colors))
#     lewiz_turtle.forward(50)

#     if dots_count % 10 == 0:
#         lewiz_turtle.setheading(90)
#         lewiz_turtle.forward(50)
#         lewiz_turtle.setheading(180)
#         lewiz_turtle.forward(500)
#         lewiz_turtle.setheading(0)

# !draw circles
# def size_shape(size_of_gap):
#     for n in range(int(360 / size_of_gap)):
#         lewiz_turtle.color(random_color())
#         lewiz_turtle.circle(100)
#         current_heading = lewiz_turtle.heading()
#         lewiz_turtle.setheading(lewiz_turtle.heading() + size_of_gap)

# size_shape(5)

# !different_ directions
# directions = [0,90,180,270]
# lewiz_turtle.pensize(15)
# lewiz_turtle.speed("fastest")

# for _ in range(500):
#     lewiz_turtle.color(random_color())
#     lewiz_turtle.forward(30)
#     lewiz_turtle.setheading(random.choice(directions))


# !draw polygon
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         lewiz_turtle.forward(80)
#         lewiz_turtle.right(angle)

# for n in range(3, 10):
# lewiz_turtle.color(random.choice(colours))
#     draw_shape(n)


screen = t.Screen()
screen.exitonclick()
