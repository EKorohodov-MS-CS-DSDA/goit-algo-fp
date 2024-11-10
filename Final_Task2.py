import turtle

def draw_tree(size, depth, t=turtle.Turtle()):
    if depth == 0:
        return

    next_size = size * 0.5 * (2 ** 0.5)
    t.forward(size)
    t.left(45)
    draw_tree(next_size, depth - 1, t=t)
    t.right(90)
    draw_tree(next_size, depth - 1, t=t)
    t.left(45)
    t.backward(size)


def draw_pythagoras_tree(size, depth=7, animation=False):
    window = turtle.Screen()
    window.bgcolor('white')

    t = turtle.Turtle(visible=False)
    t.pencolor('red')
    t.speed('fastest')
    t.penup()
    t.goto(0 , -size)
    t.left(90)
    t.pendown()
    t.hideturtle()

    if not animation:
        window.tracer(False)

    t.begin_fill()
    draw_tree(size, depth, t=t)
    t.end_fill()

    if not animation:
        window.tracer(True)
    window.mainloop()


def main():
    draw_size = int(input("Enter the size of the tree (default 100): ") or 100)
    decusion_depth = int(input("Enter the depth of the tree (default 7): ") or 7)
    draw_pythagoras_tree(draw_size, decusion_depth)


if __name__ == "__main__":
    main()