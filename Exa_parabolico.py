# -*- coding: utf-8 -*-
"""
Created on Tue March 08 16:55:55 2021

@author: JOEL
"""   
import pygame,math # as pyg
from pygame.locals import *



from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from random import*
from math import*


pygame.init() 
 
size = (1200,800)
width= 940
height =  700 

blanco = (255,255,255)
cafe = (90,50,15) 
negro = (0, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
color_fondo = (0, 0, 0)
 
 #dibujamos puntos
def bola(surface, text, x, y, color, font):
    text_in_lines = text.split('\n')
    for line in text_in_lines:
        new = font.render(line, 1, color)
        surface.blit(new, (x, y))
        y += new.get_height()
 
def arrow(screen, color, x, y, ang):
    pygame.draw.line(screen, color, (x, y), (x + 20*math.cos(math.radians(ang + 150.0)), y - 20*math.sin(math.radians(ang + 150.0))))
    pygame.draw.line(screen, color, (x, y), (x + 20*math.cos(math.radians(ang + 210.0)), y - 20*math.sin(math.radians(ang + 210.0))))
 
def vector(screen, color, x, y, ang):
    w, z = x + v0*10*math.cos(math.radians(ang)), y - v0*10*math.sin(math.radians(ang))
    x, y, w, z = int(x), int(y), int(w), int(z)
    arrow(screen, color, w, z, ang)
    pygame.draw.line(screen, blanco, (x, y), (w, z))
#inicalizamos la pantalla
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("lanza tu bola") 
 
 
radio = 15
x = 10
y = height - radio
 
pygame.font.init() 
font = pygame.font.Font(None, 30) 
 
clock = pygame.time.Clock()
#declaramos variables que utilizaremos en el lanzamiento
 
t = 0.0
t1=1
dt = 0.5

 
v0 = 22.0
a = 1.0
ang = 45.0
 
vx = 0
vy = 0
dist = 1
 
lock = True
joel = True
lock1 = False
second = False
x = 15
sig=1
joel = 0
while 1: 
  #color fondo
    screen.fill(color_fondo)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            exit()
    teclado = pygame.key.get_pressed()
    if(tuple(set(teclado)) == (0,1) and lock): 
      #direcionamos el vector a la pocicion que querramos con las flechas
        if (teclado[pygame.K_UP]):
            ang += 1
            if(ang >= 90):
                ang = 90
        if (teclado[pygame.K_DOWN]): 
            ang -= 1
            if(ang < 0):
                ang = 0
        if (teclado[pygame.K_RIGHT] and v0 < 100): 
            v0 += 1
        if (teclado[pygame.K_LEFT] and v0 > 1):
            v0 -= 1
          #con esta disparamos la bola en un angulo dedicado
        if (teclado[pygame.K_SPACE]):
            lock = False
            lock1 = True

    bola(screen, "pulse espacio para disparar, flechas para controlar el vector", 0, 80, blanco, font)
    # tecla para finalizar la pantalla
    if (teclado[pygame.K_ESCAPE]): 
        break
    vy0 = v0*math.sin(math.radians(ang))
    vx0 = v0*math.cos(math.radians(ang))
    vy  = a*t - v0*math.sin(math.radians(ang))  

    if(lock1):
        y = (height - radio) - vy0*t + .5*a*(t**2)     
        x = joel+radio+vx0*t 
        t =t+ dt
        if(y > (height - radio)):
            dist = ((v0**2)*(math.sin(math.radians(2*ang))))
            joel = joel+ ((v0**2)*(math.sin(math.radians(2*ang))))
            v0=v0-5
            sig =-1
            t=0.5
            if(height - radio - y<-7):
              lock1 = False
              second = True
            else:
              lock1 = True
      #condicion para un segundo lanzamiento
    if(second):
        bola(screen, "empezar nuevo lanzamiento s y n para cancelar?", 0, 60, blanco, font)
        if(teclado[pygame.K_s]):
            lock = True
            second = False
            x = radio
        elif(teclado[pygame.K_n]):
            break


    bola(screen, "x = %d y = %d ang = %d"%(x - radio, height - radio - y, ang), 0, 0, blanco, font)    
    pygame.draw.circle(screen, blanco, (int(x), int(y)), radio)
    pygame.draw.line(screen, cafe, (0,720),(1200,720), 40) 
    vector(screen, blanco, x, y, ang)
    pygame.display.flip()
    clock.tick(30)