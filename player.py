import pygame
from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_START_SPEED, PLAYER_MAX_SPEED, 
    PLAYER_ACCELERATION, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN,
    SCREEN_WIDTH, SCREEN_HEIGHT
)

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.current_speed = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
                self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot()
    
    def move(self, dt):
        if self.current_speed == 0:
            self.current_speed = PLAYER_START_SPEED

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.current_speed * dt

        if self.current_speed < PLAYER_MAX_SPEED:
            self.current_speed += PLAYER_ACCELERATION

        if self.current_speed > PLAYER_MAX_SPEED:
            self.current_speed = PLAYER_MAX_SPEED

        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = 0 - self.radius
        elif self.position.x < 0 - self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = 0 - self.radius
        elif self.position.y < 0 - self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        a = self.position + forward * self.radius
        shot = Shot(a[0], a[1])
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

