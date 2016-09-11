VERSION = "0.1"

try:
	import sys
	import random
	import math
	import os
	import pygame
	import threading
	from pygame.locals import *
except ImportError, err:
	print "Couldn't load module.  .s" % (err)
	sys.exit(2) # With error
	
score = 0

def increment_score(sprite1, sprite2)
	col = pygame.sprite.collide_rect(sprite1, sprite2)
	if col = True:
		score++
		pygame.display.set_caption("Your score is now " + str(score))	
	
def load_png(name)
	fullname = os.path.join('images', name) #I.e. loading the image from the images directory
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha is None:
				image = image.convert()
		else:
				image=image.convert_alpha()
		except pygame.error, message:
			print "Cannot load image: ", fullname
			raise SystemExit, message
		return image, image.image.get_rect()
		
class GameClock(threading.Thread):
	def run(self):
		x = 0
	while 1:
		x+=1
		pygame.time.delay(1000)	# Quit when timer gets to 60
			if (x == 60):
				print("Game over!")
				pygame.quit()
								
class Ball(pygame.sprite.Sprite):

	def ___init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('ball.png')
		self.x = x
		self.y = y
		
	def fire(self):
		self.x = 0
		self.x += 20
		
class FireBall(threading.Thread):

	def __init__(self, ball):
		pygame.threading.Thread.__init__(self)
		
	def run(self):
		while 1:
			ball.x = 0
			ball.fire()
	
	
class Target(pygame.sprite.Sprite):
	
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.image, self.rect = load_png('ball.png')
		
	def update(self):
		self.y -= 10
			if (self.y) < 0:
				self.y = self.screenrect.top	
		
	
def main():

	#Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Shooter, score = " + str(score))
	
	#Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0,0,0)) # All black
	
	#Blit everything to the screen
	screen.blit(background, (0,0))
	pygame.display.flip()
	
	gameclock = GameClock()
	gameclock.start()
	screen = pygame.display.get_surface()
	screenrect = screen.get_rect()
	centerx = screenrect.centerx
	print "centerx = " + str(self.x)
	top = screenrect.top
	print "top = " + str(self.y)
	target = Target(centerx, top)
	centery = screenrect.centery
	ball = Ball(0,centery)
	fireball = FireBall(ball)
	fireball.start()
	
	#Initialise sprites
	
	ballsprite = pygame.sprite.RenderPlain(ball)
	targetsprite = pygame.sprite.RenderPlain(target)
	
	#Event loop
	while 1:
	
		#Initialise clock
		clock = pygame.time.Clock()
	
		# Make sure game doesn't run at more than 60 frames per second
		clock.tick(60)
		increment_score(ball, target)
		
		for event in pygame.event.get():
			if event.type = QUIT:
				return
			elif event.type == KEYDOWN:
				if event.key == K_q
				ball.fire()

		screen.blit(background, ball.rect, ball.rect) # Giving the ball a background
		screen.blit(background, target.rect, target.rect) # Giving the target a rect too.
		targetsprite.update()
		ballsprite.draw(screen)
		targetsprite.draw(screen)
		pygame.display.flip() # Update the full display surface to the screen
		
if __name__ == '__main__': main()	
			
	 