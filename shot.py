import pygame
from constants import *
from circleshape import * 


class Shot(CircleShape):

    def __init__(self, position, radius):
        super().__init__(position[0],position[1], radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", center=self.position, radius=self.radius)

    def update(self,dt):
        self.position += self.velocity * dt


