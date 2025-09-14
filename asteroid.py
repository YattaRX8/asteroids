import pygame
import random
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        
        self.hp = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        if self.position.x > SCREEN_WIDTH + self.radius and self.velocity.x > 0:
            self.position.x = 0 - self.radius
        elif self.position.x < 0 - self.radius and self.velocity.x < 0:
            self.position.x = SCREEN_WIDTH + self.radius
        
        if self.position.y > SCREEN_HEIGHT + self.radius and self.velocity.y > 0:
            self.position.y = 0 - self.radius
        elif self.position.y < 0 - self.radius and self.velocity.y < 0:
            self.position.y = SCREEN_HEIGHT + self.radius
        

    def split(self):
        self.hp -=1
        if self.hp == 0:
            self.kill()
    
            if self.radius <= ASTEROID_MIN_RADIUS:
                return
        
            random_angle = random.uniform(20, 50)

            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)

            self.radius -= ASTEROID_MIN_RADIUS

            asteroid = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid.velocity = v1 * 1.2
            asteroid.calculate_hp(self.radius)

            asteroid = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid.velocity = v2 * 1.2
            asteroid.calculate_hp(self.radius)
    
    def calculate_hp(self, radius):
        if radius <= 20:
            self.hp = 1
        elif radius > 20 and self.radius <= 40:
            self.hp = 2
        else:
            self.hp = 4