import pygame

class ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Animated_Farmer-head.png").convert_alpha()
        self.rect = self.image.get_rect(center=(10, 350))
    def update(self):
       self.rect.x += 5
