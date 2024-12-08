import pgzrun 
import random 

TITLE = 'Flappy ball By: Avira'
WIDTH = 1000 
HEIGHT = 800
gravity = 2000
#pixels per second

class Ball():
    def __init__(self,intial_x, intial_y, color, radius):
        self.x = intial_x
        self.y = intial_y
        self.color = color
        self.vx = 200
        self.vy = 0
        self.radius = radius
    
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,self.color)

ball1 = Ball(400,300, 'pink', 50)
ball2 = Ball(300,400, 'light blue' , 40)
ball3 = Ball(500,400, 'white' , 30)
ball4 = Ball(100,800, 'light green' , 35)
ball5 = Ball(800,100, 'cyan' , 45)
ball6 = Ball(200,600, 'red' , 27)
ball7 = Ball(678,530, 'violet' , 40)
ball8 = Ball(584,982, 'light green' , 50)
ball9 = Ball(340,903, 'yellow' , 30)
ball10 = Ball(493,934, 'orange' , 48)

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()
    ball3.draw()
    ball4.draw()
    ball5.draw()
    ball6.draw()
    ball7.draw()
    ball8.draw()
    ball9.draw()
    ball10.draw()

def update(dt):

    uy = ball1.vy
    ball1.vy += gravity*dt
    ball1.y += (uy+ball1.vy)*0.5*dt
    
    if ball1.y > HEIGHT - ball1.radius:
        ball1.y = HEIGHT - ball1.radius
        ball1.vy = - ball1.vy * 0.9
    
    ball1.x += ball1.vx * dt
    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius:
        ball1.vx = - ball1.vx

    uy = ball1.vy
    ball1.vy += gravity*dt
    ball1.y += (uy+ball1.vy)*0.5*dt

    uy = ball2.vy
    ball2.vy += gravity * dt
    ball2.y += (uy + ball2.vy) * 0.5 * dt

    if ball2.y > HEIGHT - ball2.radius:
        ball2.y = HEIGHT - ball2.radius
        ball2.vy = - ball2.vy * 0.9

    ball2.x += ball2.vx * dt
    ball2.x += ball2.vx * dt
    if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius:
        ball2.vx = - ball2.vx

    uy = ball2.vy
    ball2.vy += gravity * dt
    ball2.y += (uy + ball2.vy) * 0.5 * dt

    uy = ball3.vy
    ball3.vy += gravity * dt
    ball3.y += (uy + ball3.vy) * 0.5 * dt

    if ball3.y > HEIGHT - ball3.radius:
        ball3.y = HEIGHT - ball3.radius
        ball3.vy = - ball3.vy * 0.9

    ball3.x += ball3.vx * dt
    ball3.x += ball3.vx * dt
    if ball3.x > WIDTH - ball3.radius or ball3.x < ball3.radius:
        ball3.vx = - ball3.vx

    uy = ball3.vy
    ball3.vy += gravity * dt
    ball3.y += (uy + ball3.vy) * 0.5 * dt

    uy = ball4.vy
    ball4.vy += gravity * dt
    ball4.y += (uy + ball4.vy) * 0.5 * dt

    if ball4.y > HEIGHT - ball4.radius:
        ball4.y = HEIGHT - ball4.radius
        ball4.vy = - ball4.vy * 0.9

    ball4.x += ball4.vx * dt
    ball4.x += ball4.vx * dt
    if ball4.x > WIDTH - ball4.radius or ball4.x < ball4.radius:
        ball4.vx = - ball4.vx

    uy = ball4.vy
    ball4.vy += gravity * dt
    ball4.y += (uy + ball4.vy) * 0.5 * dt

    uy = ball5.vy
    ball5.vy += gravity * dt
    ball5.y += (uy + ball5.vy) * 0.5 * dt

    if ball5.y > HEIGHT - ball5.radius:
        ball5.y = HEIGHT - ball5.radius
        ball5.vy = - ball5.vy * 0.9

    ball5.x += ball5.vx * dt
    ball5.x += ball5.vx * dt
    if ball5.x > WIDTH - ball5.radius or ball5.x < ball5.radius:
        ball5.vx = - ball5.vx

    uy = ball5.vy
    ball5.vy += gravity * dt
    ball5.y += (uy + ball5.vy) * 0.5 * dt

    uy = ball6.vy
    ball6.vy += gravity * dt
    ball6.y += (uy + ball6.vy) * 0.5 * dt

    if ball6.y > HEIGHT - ball6.radius:
        ball6.y = HEIGHT - ball6.radius
        ball6.vy = - ball6.vy * 0.9

    ball6.x += ball6.vx * dt
    ball6.x += ball6.vx * dt
    if ball6.x > WIDTH - ball6.radius or ball6.x < ball6.radius:
        ball6.vx = - ball6.vx

    uy = ball6.vy
    ball6.vy += gravity * dt
    ball6.y += (uy + ball6.vy) * 0.5 * dt

    uy = ball7.vy
    ball7.vy += gravity * dt
    ball7.y += (uy + ball7.vy) * 0.5 * dt

    if ball7.y > HEIGHT - ball7.radius:
        ball7.y = HEIGHT - ball7.radius
        ball7.vy = - ball7.vy * 0.9

    ball7.x += ball7.vx * dt
    ball7.x += ball7.vx * dt
    if ball7.x > WIDTH - ball7.radius or ball7.x < ball7.radius:
        ball7.vx = - ball7.vx

    uy = ball7.vy
    ball7.vy += gravity * dt
    ball7.y += (uy + ball7.vy) * 0.5 * dt

    uy = ball8.vy
    ball8.vy += gravity * dt
    ball8.y += (uy + ball8.vy) * 0.5 * dt

    if ball8.y > HEIGHT - ball8.radius:
        ball8.y = HEIGHT - ball8.radius
        ball8.vy = - ball8.vy * 0.9

    ball8.x += ball8.vx * dt
    ball8.x += ball8.vx * dt
    if ball8.x > WIDTH - ball8.radius or ball8.x < ball8.radius:
        ball8.vx = - ball8.vx

    uy = ball8.vy
    ball8.vy += gravity * dt
    ball8.y += (uy + ball8.vy) * 0.5 * dt

    uy = ball9.vy
    ball9.vy += gravity * dt
    ball9.y += (uy + ball9.vy) * 0.5 * dt

    if ball9.y > HEIGHT - ball9.radius:
        ball9.y = HEIGHT - ball9.radius
        ball9.vy = - ball9.vy * 0.9

    ball9.x += ball9.vx * dt
    ball9.x += ball9.vx * dt
    if ball9.x > WIDTH - ball9.radius or ball9.x < ball9.radius:
        ball9.vx = - ball9.vx

    uy = ball9.vy
    ball9.vy += gravity * dt
    ball9.y += (uy + ball9.vy) * 0.5 * dt

    uy = ball10.vy
    ball10.vy += gravity * dt
    ball10.y += (uy + ball10.vy) * 0.5 * dt

    if ball10.y > HEIGHT - ball10.radius:
        ball10.y = HEIGHT - ball10.radius
        ball10.vy = - ball10.vy * 0.9

    ball10.x += ball10.vx * dt
    ball10.x += ball10.vx * dt
    if ball10.x > WIDTH - ball10.radius or ball10.x < ball10.radius:
        ball10.vx = - ball10.vx

    uy = ball10.vy
    ball10.vy += gravity * dt
    ball10.y += (uy + ball10.vy) * 0.5 * dt


def on_key_down(key):
    
    if key == keys.SPACE:
        ball1.vy = -456
        ball2.vy = -560
        ball3.vy = -500
        ball4.vy = -600
        ball5.vy = -450
        ball6.vy = -500
        ball7.vy = -600
        ball8.vy = -550
        ball9.vy = -485
        ball10.vy = -500

pgzrun.go()