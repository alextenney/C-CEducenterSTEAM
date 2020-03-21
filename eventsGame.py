# Get started with interactive Python
import turtle

wn = turtle.Screen()
wn.setup(700,700)
wn.bgcolor("black")

#create pen
class Pen(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("white")
    self.penup()
    self.speed(0)
    
class Player(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("yellow")
    self.penup()
    self.speed(0)
    
  def go_up(self):
    move_to_x=player.xcor()
    move_to_y=player.ycor() + 24
    
    if (move_to_x,move_to_y) not in walls:
        self.goto(move_to_x, move_to_y)
  
  def go_down(self):
    move_to_x=player.xcor()
    move_to_y=player.ycor() - 24
    
    if (move_to_x,move_to_y) not in walls:
        self.goto(move_to_x, move_to_y)  
        
  def go_right(self):
    move_to_x=player.xcor()
    move_to_y=player.ycor() + 24
    
    if (move_to_x,move_to_y) not in walls:
        self.goto(move_to_x, move_to_y) 
        
  def go_left(self):
    move_to_x=player.xcor()
    move_to_y=player.ycor() - 24
    
    if (move_to_x,move_to_y) not in walls:
        self.goto(move_to_x, move_to_y) 

#create Levels list
levels = [""]

#define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXX            XX",
"X  XXXXXXX  XXXXXX  XX XX",
"X       XX  XXXXXX  X XXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Add maze to mazes list
levels.append(level_1)

#Create Level Setup Function

def setup_maze(level):
  for y in range(len(level)):
    for x in range(len(level[y])):
      #Get the Character at each x,y coordinate
      #NOTE the order of the y and x in the next line
      character = level[y][x]
      #Calculate the screen x, y coordinates
      screen_x = -288 + (x * 24)
      screen_y = 288 - (y * 24)
      
      #Check if it is an X (representing a wall)
      if character == "X":
        pen.goto(screen_x, screen_y)
        pen.stamp()
        walls.append((screen_x,screen_y))
        
      if character == "P":
        player.goto(screen_x, screen_y)
        
#Create class instances
pen = Pen()
player=Player()

# Walls
walls=[]
print(walls)

#Set up the level
setup_maze(levels[1])
print(walls)


'''
Add the correct command to move the character around below this comment
'''

#Turn off screen upates
wn.tracer(0)


#Main Game Loop
while True:
  # Update Screen
    wn.update()

