import turtle
import os


# Tela
wn = turtle.Screen()
wn.title("Pong Python")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Objeto desenho
class Box(turtle.Turtle):
    def __init__(self, x, y, w, h):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.shapesize(w, h)

    # Função movimento
    def up(self):
        self.sety(self.ycor() + (self.ycor() < 220) * 20)

    def dw(self):
        self.sety(self.ycor() - (self.ycor() > -220) * 20)

    def draw(self):
        self.write("{}              {}".format(self.pts, self.ptsPc), font=("comicsans", 40, "normal"), align=("center"))

class Score(Box):
    def __init__(self, x, y, w, h):
        Box.__init__(self, x, y, w, h)
        self.goto(x, y)
        self.pts = 0
        self.ptsPc = 0
        self.hideturtle()
        self.draw()

# Objeto bola
class Ball(Box):
    def __init__(self, x, y, w, h):
        Box.__init__(self, x, y, w, h)
        self.pcy = 0
        self.bx = 0
        self.by = 0
        self.vx = 1
        self.vy = 1

    # Função movimento e colisão da bola
    def update(self):
        self.bx += self.vx
        self.by += self.vy
        ball.goto(self.bx, self.by)
        paddle_b.goto(paddle_b.xcor(), self.pcy)
        if self.bx >=paddle_b.xcor() -30 and self.by < paddle_b.ycor() + 100 and self.by < paddle_b.ycor() + 100:
            self.vx *= -1
        elif self.bx <= paddle_a.xcor() +30 and self.by < paddle_a.ycor() + 100 and self.by > paddle_a.ycor() - 100:
            self.vx *= -1
        elif self.bx < paddle_a.xcor():
            self.vx *= -1
            self.bx = 0
            score.ptsPc += 1
            score.clear()
            score.draw()
        elif self.bx > paddle_b.xcor():
            self.vx *= -1
            self.bx = 0
            score.pts += 1
            score.clear()
            score.draw()
        if self.by >= 280 or self.by <= -280:
            self.vy *= -1
        if self.bx > 20:
            if paddle_b.ycor() < self.by and self.pcy < 220:
                self.pcy += 1
            elif paddle_b.ycor() > self.by and self.pcy > -220:
                self.pcy -= 1

# Raquete A
paddle_a = Box(-350, 0, 8, 1)
# Raquete B
paddle_b = Box(350, 0, 8, 1)
# Bola
ball = Ball(0, 0, 2, 2)
# Pontuação
score = Score(0, 230, 10, 10)

# Mover com o teclado
wn.listen()
wn.onkeypress(paddle_a.up, "Up")
wn.onkeypress(paddle_a.dw, "Down")

# Main game loop
while True:
    wn.update()
    ball.update()