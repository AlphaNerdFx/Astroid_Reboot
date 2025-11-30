import sys
import pygame
from player import Player
from shot import Shot
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHOOT_COOLDOWN_SECONDS

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.time.Clock()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)            
        for element in asteroids:
            if player.collides_with(element):
                log_event("Player collided with an asteroid!")
                print("Game Over!")
                sys.exit()
        for element in asteroids:
            for shot in shots:
                if shot.collides_with(element):
                    log_event("asteroid_shot")
                    element.split()
                    shot.kill()
        for element in drawable:
            element.draw(screen)
        pygame.display.flip()
        deltatime = clock.tick(60)
        dt = deltatime / 1000
        player.update(dt)  

if __name__ == "__main__":
    main()

