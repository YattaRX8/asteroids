import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)

        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        
        self.radius -= ASTEROID_MIN_RADIUS
        clockwise_split_asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        clockwise_split_asteroid.velocity = v1 * 1.2
        anticlockwise_split_asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        anticlockwise_split_asteroid.velocity = v2 * 1.2