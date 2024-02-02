import pygame
import os

class Block(pygame.sprite.Sprite):
	image =  pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets','crystal.jpeg'))
	rect = image.get_rect()

	def __init__(self, location):
		pygame.sprite.Sprite.__init__(self)
		self.rect.left, self.rect.top = location

	def draw(self, surface):
		""" Draw on surface """
		surface.blit(self.image, (self.rect.left, self.rect.top))