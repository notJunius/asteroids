import random
import circleshape
import pygame
import constants
class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position,self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            first_asteroid_vector = self.velocity.rotate(random_angle)
            second_asteroid_vector = self.velocity.rotate(-random_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_asteroid.velocity = first_asteroid_vector * 1.2
            second_asteroid.velocity = second_asteroid_vector * 1.2
