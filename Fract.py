
import turtle

t = turtle.Turtle()
t.speed(1500)
scale = 300
colours = ['red', 'purple', 'blue', 'brown']
def draw_Pila(scale):
    if scale >= 5:

        draw_Pila(scale/4)
        t.left(90)
        draw_Pila(scale/4)
        t.right(90)
        draw_Pila(scale/4)
        t.right(90)
        draw_Pila(scale/4)
        draw_Pila(scale/4)
        t.left(90)
        draw_Pila(scale/4)
        t.left(90)
        draw_Pila(scale/4)
        t.right(90)
        draw_Pila(scale/4)
    else: t.forward(scale)

def SQ(scale):
    for i in range (4):
         t.color(colours[i%4])
         draw_Pila(scale) 
         t.left(90)   

    
SQ(scale)

turtle.done()