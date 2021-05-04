import turtle
import random
import os
import time

while(True):
    blud = turtle.Turtle()
    blud.shape("circle")
    blud.shapesize(3,3)
    blud.hideturtle()
    blud.penup()

    win = turtle.Screen()
    win.setup(width=800, height=600)
    win.bgcolor('grey')
    win.title("Turtler")
    win.tracer(0)   # Stops animation until win.update() - try game without this





    game_over = False
    shifting_yaxis = 0 

    car_list, car_list2, car_list3, car_list4 = [], [], [], []
    super_list = [car_list, car_list2, car_list3, car_list4] 

    amount_cars = 12

    # Initial y value
    yvalue1 = 0
    yvalue1r = 90
    yvalue2 = 180
    yvalue2r = 260
    yvalue3 = 340
    yvalue3r = 450
    yvalue4 = 560
    yvalue4r = 670
    road1 = turtle.Turtle()
    road12 = turtle.Turtle()
    road13 = turtle.Turtle()
    road14 = turtle.Turtle()
    road15 = turtle.Turtle()
    road2 = turtle.Turtle()
    road22 = turtle.Turtle()
    road23 = turtle.Turtle()
    road24 = turtle.Turtle()
    road25 = turtle.Turtle()
    road3 = turtle.Turtle()
    road32 = turtle.Turtle()
    road33 = turtle.Turtle()
    road34 = turtle.Turtle()
    road35 = turtle.Turtle()
    road4 = turtle.Turtle()
    road42 = turtle.Turtle()
    road43 = turtle.Turtle()
    road44 = turtle.Turtle()
    road45 = turtle.Turtle()
    road1.shape('square')
    road1.shapesize(1,3)
    road12.shape('square')
    road12.shapesize(1,3)
    road13.shape('square')
    road13.shapesize(1,3)
    road14.shape('square')
    road14.shapesize(1,3)
    road15.shape('square')
    road15.shapesize(1,3)
    road1.color('yellow')
    road12.color('yellow')
    road13.color('yellow')
    road14.color('yellow')
    road15.color('yellow')
    road2.shape('square')
    road2.shapesize(1,3)
    road22.shape('square')
    road22.shapesize(1,3)
    road23.shape('square')
    road23.shapesize(1,3)
    road24.shape('square')
    road24.shapesize(1,3)
    road25.shape('square')
    road25.shapesize(1,3)
    road2.color('yellow')
    road22.color('yellow')
    road23.color('yellow')
    road24.color('yellow')
    road25.color('yellow')
    road3.shape('square')
    road3.shapesize(1,3)
    road32.shape('square')
    road32.shapesize(1,3)
    road33.shape('square')
    road33.shapesize(1,3)
    road34.shape('square')
    road34.shapesize(1,3)
    road35.shape('square')
    road35.shapesize(1,3)
    road3.color('yellow')
    road32.color('yellow')
    road33.color('yellow')
    road34.color('yellow')
    road35.color('yellow')
    road4.shape('square')
    road4.shapesize(1,3)
    road42.shape('square')
    road42.shapesize(1,3)
    road43.shape('square')
    road43.shapesize(1,3)
    road44.shape('square')
    road44.shapesize(1,3)
    road45.shape('square')
    road45.shapesize(1,3)
    road4.color('yellow')
    road42.color('yellow')
    road43.color('yellow')
    road44.color('yellow')
    road45.color('yellow')
    road1.up()
    road12.up()
    road13.up()
    road14.up()
    road15.up()
    road2.up()
    road22.up()
    road23.up()
    road24.up()
    road25.up()
    road3.up()
    road32.up()
    road33.up()
    road34.up()
    road35.up()
    road4.up()
    road42.up()
    road43.up()
    road44.up()
    road45.up()

    turtler = turtle.Turtle()
    turtler.shape('turtle')
    turtler.left(90)
    turtler.color('green')
    turtler.up()
    turtler.speed(0)
    turtler.shapesize(2,2)
    turtler.goto(0, -130)
    turtler.up = 'ready'
    global points
    points = 0
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.up()
    pen.goto(0, 250)
    pen.color('black')
    pen.clear()
    
    def running_cars():
        global shifting_yaxis
        
        global yvalue1
        global yvalue2
        global yvalue3
        global yvalue4
        global yvalue1r
        global yvalue2r
        global yvalue3r
        global yvalue4r
        
        for i in super_list:
            
            road1.goto(0,yvalue1r+shifting_yaxis)
            road12.goto(200,yvalue1r+shifting_yaxis)
            road13.goto(-200,yvalue1r+shifting_yaxis)
            road14.goto(400,yvalue1r+shifting_yaxis)
            road15.goto(-400,yvalue1r+shifting_yaxis)
            road2.goto(0,yvalue2r+shifting_yaxis)
            road22.goto(200,yvalue2r+shifting_yaxis)
            road23.goto(-200,yvalue2r+shifting_yaxis)
            road24.goto(400,yvalue2r+shifting_yaxis)
            road25.goto(-400,yvalue2r+shifting_yaxis)
            road3.goto(0,yvalue3r+shifting_yaxis)
            road32.goto(200,yvalue3r+shifting_yaxis)
            road33.goto(-200,yvalue3r+shifting_yaxis)
            road34.goto(400,yvalue3r+shifting_yaxis)
            road35.goto(-400,yvalue3r+shifting_yaxis)
            road4.goto(0,yvalue4r+shifting_yaxis)
            road42.goto(200,yvalue4r+shifting_yaxis)
            road43.goto(-200,yvalue4r+shifting_yaxis)
            road44.goto(400,yvalue4r+shifting_yaxis)
            road45.goto(-400,yvalue4r+shifting_yaxis)
            delay = random.random()
            if len(i) < amount_cars and delay < 0.02:
                global car
                car = turtle.Turtle()
                car.shape('square')
                car.shapesize(2,2)
                car.up()
                car.list = i
                if car.list == car_list:
                    car.dx = -2
                    car.y = yvalue1
                    car.color('red')
                    car.goto(420, shifting_yaxis + car.y)
                elif car.list == car_list2:
                    car.dx = -2
                    car.y = yvalue2
                    car.color('blue')
                    car.goto(420, shifting_yaxis + car.y) 
                elif car.list == car_list3:
                    car.dx = 2
                    car.y = yvalue3
                    car.color('#5C4033')
                    car.goto(-420, shifting_yaxis + car.y) 
                elif car.list == car_list4:
                    car.dx = 2
                    car.y = yvalue4
                    car.color('Purple')
                    car.goto(-420, shifting_yaxis + car.y) 
                i.append(car)
            
    turned = False
    turned2 = False
    fow = False
    def move_left():
        if turtler.xcor()>-360: # Move left only if still in the screen
            global turned
            global turned2
            global fow
            turtler.setx(turtler.xcor()-40)
            if (turned == False and turned2==True): #Turning 
                turned = True
                turned2 = False
                fow = False
                turtler.left(180)
            elif (turned == False and turned2==False): #Turning 
                turned = True
                fow = False
                turtler.left(90)

    
    def move_right():
        if turtler.xcor()<= 340: # Move right only if still in the screen
            global turned2
            global turned
            global fow
            turtler.setx(turtler.xcor()+40)
            if (turned2 == False and turned==True):#Turning 
                turned2 = True
                turned = False
                fow = False
                turtler.right(180)
            elif (turned2 == False and turned==False):#Turning 
                turned2 = True
                fow = False
                turtler.right(90)
    
    
    def up():
        global turned2
        global turned
        global fow
        global shifting_yaxis
        global points
        if(turned == True and fow == False): #Turning 
            turtler.right(90)
            fow = True
            turned = False
            turned2 = False 
        if(turned2 == True and fow == False): #Turning 
            turtler.left(90)
            fow = True
            turned = False
            turned2 = False
        turtler.up = 'go'
        shifting_yaxis -= 30
        if(game_over == False):
            points+=1

        
        for i in super_list:  
            for j in i:    
                j.goto(j.xcor(), shifting_yaxis + j.y)
                

    def move_cars(): 
        global yvalue1
        global yvalue2
        global yvalue3
        global yvalue4
        global yvalue1r
        global yvalue2r
        global yvalue3r
        global yvalue4r
        
        for i in super_list:
            for j in i: 

                # Move cars left or right
                j.goto(j.xcor()+ j.dx, j.ycor())

                if j.xcor() < -420 and j.dx == -2: 
                    j.goto(1000,1000)
                    j.list.remove(j)
                elif j.xcor()>420 and j.dx == 2:
                    j.goto(1000,1000)
                    j.list.remove(j)

                if j.ycor()<-320:
                    if j.y == yvalue1:
                        yvalue1 += 800
                        yvalue1r += 800
                    elif j.y == yvalue2:
                        yvalue2 += 800
                        yvalue2r += 800
                    elif j.y == yvalue3:
                        yvalue3 += 800
                        yvalue3r += 800
                    elif j.y == yvalue4:
                        yvalue4 += 800
                        yvalue4r += 800
                       
               
    def collision_check():
        global game_over

        for i in super_list:
            for j in i:
                if j.distance(turtler)<40:
                    blud.goto(turtler.xcor(),turtler.ycor())
                    blud.showturtle()
                    blud.color("#8B0000")
                    game_over = True
                    
                
                
                
    win.listen()
    win.onkey(move_left, 'Left')
    win.onkey(move_right, 'Right')
    win.onkey(up, 'Up')

    
    while not game_over:
        win.update()
        time.sleep(0.01)
        
        running_cars()
        move_cars()
        collision_check()

    win.update() 
    pen.goto(0,0)
    pen.write('Points: '+str(points)+'''
Game Over!!!''', align='center', font=('Courier', 24, 'normal'))
    time.sleep(3)
    win.clear()
    continue

