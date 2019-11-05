import turtle
def snow(size,n):  # 利用递归的思想
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            snow(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    
    level=2  #还可以是3阶，4阶，5阶等
    snow(400,level)
    turtle.right(120)
    snow(400,level)
    turtle.right(120)
    snow(400,level)
    turtle.hideturtle()

main()
