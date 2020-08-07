import turtle
import random
Hanu = turtle.Turtle()



def createsquare(size, color):
  Hanu.color(color)
  for i in range(4):
    Hanu.forward(size)
    Hanu.right(90)

def createtriangle(size, color):
  Hanu.color(color)
  for i in range(3):
    Hanu.forward(size)
    Hanu.right(120)

def createhexagon(size, color):
  Hanu.color(color)
  for i in range(6):
    Hanu.forward(size)
    Hanu.right(60)

def createcircle(size, color):
  Hanu.color(color)
  Hanu.circle(size)

def location():
  b = random.randint(-300, 300)
  d = random.randint(-300, 300)
  Hanu.penup()
  Hanu.goto(b, d)
  Hanu.pendown()


shapes = {
  'circle': createcircle,
  'triangle': createtriangle,
  'square': createsquare,
  'hexagon': createhexagon
  }


playagain = 'Y'

while playagain == 'Y':
  shape = input ('what shape would you like to draw?')
  color = input ('what color do you want your shape to be?')
  siz = input ('what size would you like your shape to be?')

  location
  
  shapes[shape](siz, color)

  playagain = input ('do you want to make another shape?\nY/N')


