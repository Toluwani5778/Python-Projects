# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()  # Initialize the pygame library
    clock = pygame.time.Clock()  # Create a clock object to manage frame rate
    dt = 0  # Initialize delta time variable
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()  # Create a group for updating sprites
    drawable = pygame.sprite.Group()  # Create a group for drawing sprites
    asteroids = pygame.sprite.Group()  # Create a group for asteroids
    shots = pygame.sprite.Group()  # Create a group for shots
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)  # Set the containers for the AsteroidField class
    asteroid_field = AsteroidField()  # Create an instance of the AsteroidField
    Player.containers = (updatable, drawable)  # Set the containers for the Player class
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create a player instance at the center of the screen

    while True:
        screen.fill((0, 0, 0))
        
        updatable.update(dt)  # Update the player state with the delta time
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                exit()
        for draw in drawable:
            draw.draw(screen) # Draw the player on the screen
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        # Limit the frame rate to 60 FPS
        dt = clock.tick(120)/1000  # Update the display
        

if __name__ == "__main__":
    main()

 