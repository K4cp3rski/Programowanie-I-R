from turtle import *

def gwiazda(len):
    speed("slow")
    for i in range(5):
        pensize(3)
        forward(len)
        left(180-108)
        forward(len)
        right(180-36)

def main():
    color("red")
    begin_fill()
    gwiazda(100)
    end_fill()
    done()

main()