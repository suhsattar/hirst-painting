# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# 10x10, dotsize = 20, spaced by 50 paces?

import turtle as turtle_module
import random

color_list = [(40, 3, 179), (85, 251, 187), (224, 151, 108), (158, 3, 80), (5, 211, 91), (4, 139, 66), (240, 43, 125),
              (112, 103, 240), (251, 250, 57), (47, 239, 55), (185, 181, 247), (209, 102, 6),
              (37, 33, 250), (219, 117, 168), (140, 2, 1), (249, 37, 34), (83, 245, 251), (202, 33, 111), (25, 2, 106),
              (39, 113, 143), (104, 2, 52), (10, 209, 217), (226, 167, 206), (222, 121, 16), (2, 115, 34)]

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
screen = turtle_module.Screen()


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen.exitonclick()





