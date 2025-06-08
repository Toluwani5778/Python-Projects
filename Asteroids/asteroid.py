from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        random_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            asteroid_1_velo = self.velocity.rotate(random_angle)
            asteroid_2_velo = self.velocity.rotate(-random_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_1.velocity = asteroid_1_velo * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_2.velocity = asteroid_2_velo * 1.2
