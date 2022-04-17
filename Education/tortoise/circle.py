from turtle import Screen, Turtle

s = Screen()
turtle = Turtle()
turtle.shape('turtle')


def square():
    size = 100
    turn = 90
    turtle.forward(size)
    turtle.right(turn)
    turtle.forward(size)
    turtle.right(turn)
    turtle.forward(size)
    turtle.right(turn)
    turtle.forward(size)
    turtle.right(turn)


if __name__ == "__main__":
    square()
    wait = input("waiting")
