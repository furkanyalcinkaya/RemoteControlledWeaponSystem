#!/usr/bin/env python
import os, sys, pygame
from pygame import locals
import time

pygame.init()
pygame.joystick.init()

j = pygame.joystick.Joystick(0)
j.init()
print 'enable joystick: ' +j.get_name()
x1=0.0


for e in pygame.event.get():
	#if e.type == pygame.locals.JOYAXISMOTION: #joystick harekei varsa
	x1 = j.get_axis(0)
	y1 = j.get_axis(1)
	x2 = j.get_axis(3)
	y2 = j.get_axis(2)
	arrow = j.get_hat(0)
			
	x1 = x1*32768
	y1 = y1*(-32768)
	x2 = x2*32768
	y2 = y2*(-32768)
			
	print("x1: {} \ty1: {} \tx2: {} \ty2: {} \tl/r:{} \tu/d:{}".format(x1,y1,x2,y2,arrow[0],arrow[1]))
			
	b1 = j.get_button(0)
	b2 = j.get_button(1)
	b3 = j.get_button(2)
	b4 = j.get_button(3)
	b5 = j.get_button(4)
	b6 = j.get_button(5)
	b7 = j.get_button(6)
	b8 = j.get_button(7)
	b9 = j.get_button(8)
	b10 = j.get_button(9)
	b11 = j.get_button(10)
	b12 = j.get_button(11)
			
			#print("Buton 1:{} 2:{} 3:{} 4:{} 5:{} 6:{} 7:{} 8:{} 9:{} 10:{} 11:{} 12:{}".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12))
			#print ""

