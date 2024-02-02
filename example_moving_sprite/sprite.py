import pygame

COLOR = (255, 100, 98)

# Sprite generalization class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.set_colorkey(COLOR)
        
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()