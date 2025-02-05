from turtle import * #import turtle
import colorsys #import color system

h=0.7 #buat besar(height)
speed(0) #speed untuk buat garisnya
bgcolor("black") #warna background
pensize(2) #untuk size pen nya (tebal)

for i in range(100): #ulangi 100 kali
    c=colorsys.hsv_to_rgb(h,1,1) #meberikan warna random
    pencolor("pink") #warna pencil pink
    fillcolor(c) #untuk warnanya random sesuai var c
    begin_fill()
    h+=0.004 
    fd(i) #forwardnya ke var I (100 kali)
    rt(20) #right turn 20 derajat
    circle(190-i,90) # jadi 190 derajat - 100kali, 90 steps
    lt(80) #left turn 80 derajat
    circle(190-i,90)
    for i in range (2):
        rt(40)
        lt(20)
        rt(120)
    end_fill()