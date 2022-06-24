#Jeu en Turtle Python
import turtle
import math
import random
import os
import time

#Création de la fenêtre
wn = turtle.Screen()
wn.bgcolor("Lightgreen")
wn.bgpic("fond.gif")
wn.tracer(6)

#Création de la bordure
mypen = turtle.Turtle()
mypen.color("White")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Créer la tortue du joueur
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)

#Créer la variable du score
score = 0


#Créer les objectifs
maxGoals = 12
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))



#Définir la vitesse
speed = 1

#Définir les fonctions des touches de déplacement

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def lowspeed():
    global speed
    speed -= 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False


#Définir les touches de déplacement
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(lowspeed, "Down")



#Boucle
while True:
    player.forward(speed)

    #Vérification des collisions de bordures joueur
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        

    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        
        
    #Faire bouger les objectifs
    for count in range(maxGoals):
        goals[count].forward(2)

        #Vérification des collisions de bordures objectifs
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)

        #Vérification des collisions joueur/objectifs
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0,360))
            score += 1
            #Ecrire le score dans la fenêtre
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align="left", font=("Arial",14, "normal"))
    
    
     
    

    
    





delay = raw_input("Appuyez sur Entrée pour terminer.")
