import turtle
import random
import time
import numpy as np
import math


window=turtle.Screen()
window.setup(500,500)
window.tracer(0)
window.bgcolor("green")

middle=turtle.Turtle()
middle.hideturtle()
middle.goto(0,0)

t_3=turtle.Turtle()
t_2=turtle.Turtle()
t_2.penup()
color_list=["red","blue","green","grey","yellow","purple","orange","silver"]
t_2.hideturtle()
t_3.hideturtle()
t_3.penup()



color_number=0

t=turtle.Turtle()
ai=turtle.Turtle()
t.penup()
ai.penup()
t.goto(1,1)
ai.goto(random.randint(-150,150),random.randint(-150,150))
t.goto(random.randint(-150,150),random.randint(-150,150))

def turn_left():
  t.left(25)
def turn_right():
 t.right(25)
 

def freeze():
  if counter==0:
    t_3.forward(1)
window.onkey(turn_left,"Left")
window.onkey(turn_right,"Right")
window.onkey(freeze,"space")
window.listen()

my_list_of_turtles=list()
number_of_turtles=10
ai_num=""
ai_position=""
counter=0
ai.color("red")
t.color("yellow")


for number in range(number_of_turtles):
 bubble=turtle.Turtle()
 bubble.shape("circle")
 bubble.penup()
 bubble.goto(random.randint(-200,200),random.randint(-200,200))
 my_list_of_turtles.append(bubble)

lives=1
lives_2=2
score=1
ai_score=0
speed=0.2
ai_speed=0.6+speed/2
ai_pos=[" "," "]
pos=1
freeze_counter=0
death=False
while True:
  font_type=("Arial",5)
  # t_2.write('ai:'+str(ai_score)+'\n Turtle:'+str(score), font=font_type, align='centre')
  t_2.hideturtle()
  if freeze_counter<score:
    if freeze=="a":
        counter=counter+1
        print("yes_1")
    if t_3.xcor()==pos:
      ai_speed=-0.01
      ai.color("blue")
      freeze="a"
      if counter>200:
        ai.color("red")
        pos=pos+1
        ai_speed=0.6+speed/2
        freeze=""
        counter=0
        freeze_counter=freeze_counter+1

  t.forward(0.6 + speed/2)
  ai.forward(ai_speed+0.01)
  ai.setheading(90)
  if ai.ycor()-t.ycor()==0:
    t.sety(t.ycor()+1)
  if ai.xcor()-t.xcor()==0:
    t.setx(t.xcor()+1)
  if ai.xcor()>t.xcor():
    ai_pos[0]=("l")
  else:
    ai_pos[0]=("r")
  if ai.ycor()<t.ycor():
    ai_pos[1]=("a")
  else:
    ai_pos[1]=("b")
 
  if ai_pos==["r","a"] :
    h_line=abs(t.xcor()- ai.xcor())#gives you the horizontal line of triangle
    v_line=abs(t.ycor()-ai.ycor())#gives you vertical line of triangle
    right=np.arctan(v_line/h_line)
    right=right * 180/math.pi
    ai.setheading(right)
  
  if ai_pos==["l","a"]:
    h_line=abs(t.xcor()- ai.xcor())#gives you the horizontal line of triangle
    v_line=abs(t.ycor()-ai.ycor())#gives you vertical line of triangle
    left=np.arctan(v_line/h_line)
    left=left*180/math.pi
    left=180-left
    ai.setheading(left)

  if ai_pos==["l","b"]:
    h_line=abs(t.xcor()- ai.xcor())#gives you the horizontal line of triangle
    v_line=abs(t.ycor()-ai.ycor())#gives you vertical line of triangle
    left=np.arctan(v_line/h_line)
    left=left*180/math.pi
    left=180+left
    ai.setheading(left)

  if ai_pos==["r","b"]:
    h_line=abs(t.xcor()- ai.xcor())#gives you the horizontal line of triangle
    v_line=abs(t.ycor()-ai.ycor())#gives you vertical line of triangle
    left=np.arctan(h_line/v_line)
    left=left*180/math.pi
    left=270+left
    ai.setheading(left)
    
  for i in range (number_of_turtles):
    if ai.distance(my_list_of_turtles[i])<t.distance(ai):
      if ai.xcor()>my_list_of_turtles[i].xcor():
        ai_pos[0]=("l")
      else:
        ai_pos[0]=("r")
      if ai.ycor()<my_list_of_turtles[i].ycor():
        ai_pos[1]=("a")
      else:
        ai_pos[1]=("b")
    
      if ai_pos==["r","a"] :
        t_xcor=t.xcor()
        h_line=abs(my_list_of_turtles[i].xcor()- ai.xcor())#gives you the horizontal line of triangle
        v_line=abs(my_list_of_turtles[i].ycor()-ai.ycor())#gives you vertical line of triangle
        right=np.arctan(v_line/h_line)
        right=right * 180/math.pi
        ai.setheading(right)
  
      if ai_pos==["l","a"]:
        h_line=abs(my_list_of_turtles[i].xcor()- ai.xcor())#gives you the horizontal line of triangle
        v_line=abs(my_list_of_turtles[i].ycor()-ai.ycor())#gives you vertical line of triangle
        left=np.arctan(v_line/h_line)
        left=left*180/math.pi
        left=180-left
        ai.setheading(left)

      if ai_pos==["l","b"]:
        h_line=abs(my_list_of_turtles[i].xcor()- ai.xcor())#gives you the horizontal line of triangle
        v_line=abs(my_list_of_turtles[i].ycor()-ai.ycor())#gives you vertical line of triangle
        left=np.arctan(v_line/h_line)
        left=left*180/math.pi
        left=180+left
        ai.setheading(left)

      if ai_pos==["r","b"]:
        h_line=abs(my_list_of_turtles[i].xcor()- ai.xcor())#gives you the horizontal line of triangle
        v_line=abs(my_list_of_turtles[i].ycor()-ai.ycor())#gives you vertical line of triangle
        left=np.arctan(h_line/v_line)
        left=left*180/math.pi
        left=270+left
        ai.setheading(left)
  
  rand=random.randint(1,100)
  if number_of_turtles==0:
   break 
  
  for i in range(number_of_turtles):
   if lives_2%2:
     lives_2=lives_2+1
     lives=lives+0.5
   if score%1:
    lives=lives
   if middle.distance(t)>350:
     window.update()
     lives=lives-1
     print("lives="+str(lives))
     t.goto(0,0)
   if lives<=0:
    print("you dead")
    t.hideturtle()
    my_list_of_turtles.remove(my_list_of_turtles[i])
    break
   my_list_of_turtles[i].forward(speed)
   if rand==3:
    my_list_of_turtles[random.randint(0,number_of_turtles-1)].left(90)
   if rand==4:
    my_list_of_turtles[random.randint(0,number_of_turtles-1)].right(90)
   if  middle.distance(my_list_of_turtles[i])>250:
     my_list_of_turtles[i].hideturtle()
     my_list_of_turtles[i].goto(random.randint(-250,250),random.randint(-250,250))
     my_list_of_turtles[i].showturtle()
   if my_list_of_turtles[i].distance(t)<15:
     lives_2=lives_2+1
     while color_number<8:
      color_number=color_number+1
      my_list_of_turtles[i].color(color_list[color_number-1])
      window.update()
      time.sleep(0.05)
     score=score+1
     print("score="+str(score-1)) 
     color_number=0
     my_list_of_turtles[i].hideturtle()
     my_list_of_turtles.remove(my_list_of_turtles[i])
     number_of_turtles=number_of_turtles-1
     break 
   if my_list_of_turtles[i].distance(ai)<15:
     while color_number<8:
      color_number=color_number+1
      my_list_of_turtles[i].color(color_list[color_number-1])
      window.update()
      time.sleep(0.05)
     color_number=0
     ai_score=ai_score+1
     my_list_of_turtles[i].hideturtle()
     my_list_of_turtles.remove(my_list_of_turtles[i])
     number_of_turtles=number_of_turtles-1
     break 
   if ai.distance(t)<6:
     death=True
     break 
  if death==True:
    for i in range(number_of_turtles):
      my_list_of_turtles[i].hideturtle()
    break
  window.update()
t.hideturtle()
ai.hideturtle()
print("you win")
for hi in range(0,8):
 window.bgcolor(color_list[hi])
 time.sleep(0.2)
 window.update()
style = ('Arial', 30)
if death==False and ai_score< score-1:
  t_2. write('You Win!\n AI:'+str(ai_score)+'\n Turtle:'+str(score-1), font=style, align='center')
  t_2. hideturtle()
elif ai_score> score-1 or death==True:
  style = ('Arial', 30, 'italic')
  t_2. write('You Lose!\n AI:'+str(ai_score)+'\nTurtle:'+str(score-1), font=style, align='center')
  t_2. hideturtle()
else:
  style = ('Arial', 30, 'italic')
  t_2. write('You Draw!\n AI:'+str(ai_score)+'\n Turtle:'+str(score-1), font=style, align='center')
  t_2. hideturtle()




window.update()


    
