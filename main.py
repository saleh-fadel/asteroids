# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
    
    # Initialize pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game loop
    while True:
        # Check for player inputs (step 1 of game loop)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Draw the game to the screen (step 3 of game loop)
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()