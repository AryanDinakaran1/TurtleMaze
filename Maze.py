"""
    This program has been made to test the logical skills of the user . It also tests the performance ratio by putting
    timer and calculating performance ratio to check the progress of the user. This maze has been created without using maze.py. 
    A menu has been created for the purpose of controlling the sprite . The background color of orange gives a hint of ancientness
    to this theme. Since we could not use curse.py module we have used w,a,s,d keys to make it more user friendly. As the sprite moves 
    Its path is highlighted to show the user the path traced by it.


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

start_time = time.time()

end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
"""

import turtle as t
import time
import math
import random

screen = t.Screen()
screen.bgcolor("tomato")
tur = t.Turtle()
tur.penup()
tur.setpos(225,225)
tur.pendown()
tur.speed(0)

sum = 0

index = 0

path = []

print("Loading......\nGenerating Maze......")
print("Reach the red dot to win the game!")
"""
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0} : {1}".format(int(mins),round(sec)))
"""
for i in range(2):
    for i in range (4):
        tur.rt(90)
        if(i%2 == 1):
            tur.fd(210)
            tur.penup()
            tur.fd(30)
            tur.pendown()
            tur.fd(210)
        else :
            tur.fd(450)

def horiz(n, color_name, length, quantity):
    tur.pensize(n) 
    tur.color(color_name)
    for k in range(quantity):
        tur.pendown()
        tur.fd(length)
        tur.penup()
        tur.backward(length)
        tur.rt(90)
        tur.fd(n*15)
        tur.lt(90)

tur.penup()
tur.goto(-225,195)
horiz(2, "black", 450, 14)

tur.goto

def vertiz(n, color_name, length, quantity):
    tur.pensize(n) 
    tur.color(color_name)
    for k in range(quantity):
        tur.setheading(270)
        tur.pendown()
        tur.fd(length)
        tur.penup()
        tur.backward(length)
        tur.rt(90)
        tur.fd(n*15)
        tur.lt(90)
tur.penup()
tur.goto(195,225)
vertiz(2,"black",450,14)

def break_horiz(x,y):
    tur.penup()
    tur.pensize(3)
    tur.goto(x,y)
    tur.color("tomato")
    tur.setheading(0)
    tur.pendown()
    tur.fd(24)
    tur.setheading(180)
    tur.fd(24)
    tur.penup()

def break_vert(x,y):
    tur.penup()
    tur.pensize(3)
    tur.goto(x,y)
    tur.color("tomato")
    tur.setheading(270)
    tur.pendown()
    tur.fd(24)
    tur.setheading(90)
    tur.fd(24)
    tur.penup()


for horizLoop in range(2):

    #1

    break_horiz(-222,195)
    break_horiz(-162,195)
    break_horiz(-42,195)
    break_horiz(-12,195)
    break_horiz(18,195)
    break_horiz(48,195)
    break_horiz(78,195)
    break_horiz(138,195)
    break_horiz(168,195)
    break_horiz(198,195)

    #2

    break_horiz(-222,165)
    break_horiz(-192,165)
    break_horiz(-162,165)
    break_horiz(-72,165)
    break_horiz(-42,165)
    break_horiz(138,165)

    #3

    break_horiz(-192,135)
    break_horiz(-132,135)
    break_horiz(-102,135)
    break_horiz(-72,135)
    break_horiz(-12,135)
    break_horiz(138,135)
    break_horiz(168,135)
    break_horiz(198,135)

    #4

    break_horiz(-162,105)
    break_horiz(-102,105)
    break_horiz(-72,105)
    break_horiz(18,105)
    break_horiz(78,105)
    break_horiz(138,105)
    break_horiz(198,105)

    #5

    break_horiz(-222,75)
    break_horiz(-132,75)
    break_horiz(-102,75)
    break_horiz(18,75)
    break_horiz(108,75)
    break_horiz(168,75)
    break_horiz(198,75)

    #6

    break_horiz(-192,45)
    break_horiz(-132,45)
    break_horiz(-102,45)
    break_horiz(-72,45)
    break_horiz(78,45)

    #7

    break_horiz(-222,15)
    break_horiz(-162,15)
    break_horiz(-102,15)
    break_horiz(-12,15)
    break_horiz(48,15)
    break_horiz(78,15)
    break_horiz(108,15)
    break_horiz(198,15)

    #8

    break_horiz(-222,-15)
    break_horiz(-192,-15)
    break_horiz(-162,-15)
    break_horiz(-72,-15)
    break_horiz(18,-15)
    break_horiz(78,-15)
    break_horiz(108,-15)
    break_horiz(138,-15)

    #9

    break_horiz(-222,-45)
    break_horiz(-192,-45)
    break_horiz(-162,-45)
    break_horiz(-132,-45)
    break_horiz(-72,-45)
    break_horiz(-12,-45)
    break_horiz(108,-45)
    break_horiz(138,-45)
    break_horiz(198,-45)

    #10

    break_horiz(-162,-75)
    break_horiz(-72,-75)
    break_horiz(-42,-75)
    break_horiz(78,-75)
    break_horiz(168,-75)
    break_horiz(198,-75)

    #11

    break_horiz(-222,-105)
    break_horiz(-162,-105)
    break_horiz(18,-105)
    break_horiz(168,-105)
    break_horiz(198,-105)

    #12

    break_horiz(-222,-135)
    break_horiz(-42,-135)
    break_horiz(48,-135)
    break_horiz(198,-135)

    #13

    break_horiz(-222,-165)
    break_horiz(-192,-165)
    break_horiz(-72,-165)
    break_horiz(-42,-165)
    break_horiz(108,-165)
    break_horiz(138,-165)
    break_horiz(168,-165)

    #14

    break_horiz(-192,-195)
    break_horiz(-162,-195)
    break_horiz(-132,-195)
    break_horiz(-102,-195)
    break_horiz(-42,-195)
    break_horiz(-12,-195)
    break_horiz(18,-195)
    break_horiz(48,-195)
    break_horiz(78,-195)
    break_horiz(198,-195)

for vertizLoop in range(2):

    #1
    break_vert(-195,222)
    break_vert(-195,132)
    break_vert(-195,102)
    break_vert(-195,72)
    break_vert(-195,-48)
    break_vert(-195,-78)
    break_vert(-195,-198)

    #2
    break_vert(-165,222)
    break_vert(-165,192)
    break_vert(-165,42)
    break_vert(-165,12)
    break_vert(-165,-78)
    break_vert(-165,-108)
    break_vert(-165,-138)

    #3
    break_vert(-135,222)
    break_vert(-135,192)
    break_vert(-135,162)
    break_vert(-135,132)
    break_vert(-135,102)
    break_vert(-135,72)
    break_vert(-135,12)
    break_vert(-135,-18)
    break_vert(-135,-108)
    break_vert(-135,-138)
    break_vert(-135,-198)

    #4
    break_vert(-105,222)
    break_vert(-105,192)
    break_vert(-105,12)
    break_vert(-105,-18)
    break_vert(-105,-48)
    break_vert(-105,-78)
    break_vert(-105,-138)
    break_vert(-105,-168)

    #5
    break_vert(-75,222)
    break_vert(-75,192)
    break_vert(-75,72)
    break_vert(-75,-18)
    break_vert(-75,-78)
    break_vert(-75,-108)
    break_vert(-75,-138)
    break_vert(-75,-198)

    #6
    break_vert(-45,222)
    break_vert(-45,132)
    break_vert(-45,102)
    break_vert(-45,72)
    break_vert(-45,42)
    break_vert(-45,-18)
    break_vert(-45,-78)
    break_vert(-45,-108)
    break_vert(-45,-168)
    break_vert(-45,-198)

    #7
    break_vert(-15,192)
    break_vert(-15,132)
    break_vert(-15,102)
    break_vert(-15,72)
    break_vert(-15,42)
    break_vert(-15,12)
    break_vert(-15,-18)
    break_vert(-15,-78)
    break_vert(-15,-138)
    break_vert(-15,-168)

    #8
    break_vert(15,192)
    break_vert(15,162)
    break_vert(15,72)
    break_vert(15,-18)
    break_vert(15,-48)
    break_vert(15,-78)
    break_vert(15,-108)
    break_vert(15,-138)
    break_vert(15,-168)

    #9
    break_vert(45,222)
    break_vert(45,162)
    break_vert(45,132)
    break_vert(45,102)
    break_vert(45,42)
    break_vert(45,12)
    break_vert(45,-48)
    break_vert(45,-78)
    break_vert(45,-138)
    break_vert(45,-198)

    #10
    break_vert(75,192)
    break_vert(75,162)
    break_vert(75,102)
    break_vert(75,72)
    break_vert(75,-18)
    break_vert(75,-48)
    break_vert(75,-108)
    break_vert(75,-138)
    break_vert(75,-168)

    #11
    break_vert(105,222)
    break_vert(105,162)
    break_vert(105,132)
    break_vert(105,102)
    break_vert(105,72)
    break_vert(105,-48)
    break_vert(105,-78)
    break_vert(105,-108)
    break_vert(105,-138)
    break_vert(105,-198)

    #12
    break_vert(135,192)
    break_vert(135,162)
    break_vert(135,132)
    break_vert(135,42)
    break_vert(135,-78)
    break_vert(135,-108)
    break_vert(135,-168)
    break_vert(135,-198)

    #13
    break_vert(165,222)
    break_vert(165,162)
    break_vert(165,102)
    break_vert(165,72)
    break_vert(165,42)
    break_vert(165,12)
    break_vert(165,-48)
    break_vert(165,-78)
    break_vert(165,-108)
    break_vert(165,-138)
    break_vert(165,-198)

    #14
    break_vert(195,192)
    break_vert(195,132)
    break_vert(195,12)
    break_vert(195,-18)
    break_vert(195,-108)
    break_vert(195,-198)

tur.penup()
tur.goto(-1,-240)
tur.pendown()
tur.penup()
tur.goto(4,-240)
tur.pendown()
tur.begin_fill()
tur.color("red")
tur.circle(4)
tur.end_fill()
tur.penup()
tur.goto(4,-240)
tur.color("red")
tur.pendown()
tur.circle(5)
tur.hideturtle()

mt = t.Turtle()
mt.shape('turtle')
mt.color('white')
mt.penup()
mt.setheading(270)
mt.goto(0,240)

start_time = time.time()


menu = ["1] To move the sprite back enter : w","2] To move the sprite down enter : s","3] To move the sprite right enter : d","4] To move the sprite left enter : a"]
for menus in menu:
    print(menus)

while True:
     
    command = input("Enter Movement")

            
    if command == "w":
                
        if mt.xcor() == 0 and mt.ycor() ==240 :
                print("Wrong Direction Given")
        else :   
            mt.pendown()
            mt.color("white")
            mt.setheading(90)
            mt.forward(30)
            path.append("w")
            if path[index-1]=="s":
                del path[index-1 : index+1]
                index-=2

    elif command == "s":

        if mt.xcor() == 0 and mt.ycor() <= -195:
            mt.fd(30)
            path.append("s")
            break
        else:    
            mt.pendown()
            mt.color("white")
            mt.setheading(270)
            mt.forward(30)
            path.append("s")
            if path[index-1]=="w":
                del path[index-1 : index+1]
                index-=2

    elif command == "d":
        if mt.xcor() == 0 and mt.ycor() == 240 :
            print("Wrong Direction Given")
        else :   
            mt.pendown()
            mt.color("white")
            mt.setheading(0)
            mt.forward(30)
            path.append("d")
            if path[index-1]=="a":
                del path[index-1 : index+1]
                index-=2
            

    elif command == "a":

            
        if mt.xcor() == 0 and mt.ycor() == 240 :
            print("Wrong Direction Given")
        else :   
            mt.pendown()
            mt.color("white")
            mt.setheading(180)
            mt.forward(30)
            path.append("a")
            if path[index-1]=="d":
                del path[index-1 : index+1]
                index-=2

    elif command == "exit":
        print("Ejected")
        break
        
    else:
        continue
    index+=1



if path == ['s','s','a','w','a','a','a','a','s','d','d','d','s','s','d','d','w','d','d','d','d','d','s','a','a','s','a','a','s','a','a','a','a','s','s','a','a','s','d','d','d','d','d','s','d','d','d','s','d','d','d','s','a','a','a','a','s','a','a','a','s','d','s','s']:
    end_time = time.time()
    time_lapsed = end_time - start_time
    print("You made it in "+round(time_lapsed,2)+" seconds")
    print("Hurray!!! You Won!")
else :
    print("Please redo the maze in a correct manner!!")
    

tur.hideturtle()