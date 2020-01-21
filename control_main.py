#!/usr/bin/env python
import os, sys, pygame
from pygame import locals
import time

pygame.init()
pygame.joystick.init()

j = pygame.joystick.Joystick(0)
j.init()
print 'enable joystick: ' +j.get_name()

x1=x2=0
y1=y2=0
arrow = (0,0)

b1=b2=b3=0
b4=b5=b6=0
b7=b8=b9=0
b10=b11=b12=0

pan=0
tilt=0
mod =0
shot=0
safe=1
while 1:
	for e in pygame.event.get():
		#if e.type == pygame.locals.JOYAXISMOTION: #joystick harekei varsa
		x1 = j.get_axis(0)
		y1 = j.get_axis(1)
		x2 = j.get_axis(3)
		y2 = j.get_axis(2)
		arrow = j.get_hat(0)
			
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
	
	def angles(x,y):
		global pan 
		global tilt
		pan = pan + x
		pan = round(pan,3)
		tilt = tilt + ((-1)*y)
		tilt = round(tilt,3)
		if pan > 200:
			pan = -160
		elif pan < -200:
			pan = 160
		if tilt > 60:
			tilt = 60
		elif tilt < -30:
			tilt = -30
		
	def system_status(a):
		# mod = 0 otomatic mod
		# mod = 1 manuel mod
		if a == 1:
			if mod == 1:
				mod = 0
			elif mod == 0:
				mod = 1 
		
	def shot_status(b,c,d):
		# shot = 1 , semi shot
		# shot = 2 , auto shot
		# shot = 0 , no shot
		# safe = 1 , no shot
		# safe = 0 , free throw
		if d == 1:
			if safe == 0:
				safe = 1
			else:
				safe = 0
		
		if b == 1 and safe == 0:
			shot = 1
		elif c == 1 and safe == 0:
			shot = 2
		else:
			shot = 0  
			
		

	#print("x1: {} \ty1: {} \tx2: {} \ty2: {} \tl/r:{} \tu/d:{}".format(x1,y1,x2,y2,arrow[0],arrow[1]))	
	#print("Buton 1:{} 2:{} 3:{} 4:{} 5:{} 6:{} 7:{} 8:{} 9:{} 10:{} 11:{} 12:{}".format(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12))
	#print ""
	
	angles(x1,y1)
	system_status(b1)
	shot_status(b2,b3,b4)
	#print pan
	#print tilt
	#print""		
	time.sleep(0.02)
	

