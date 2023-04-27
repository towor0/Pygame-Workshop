# Import Libraries
import pygame, sys

# Initialize Pygame
pygame.init()
# Create Pygame Window
screen = pygame.display.set_mode((400, 300))
# Set the Game Title
pygame.display.set_caption('Name of the Game')

# Create Game Objects Here...

running = True
# Game Loop
while running:
    # Update Here...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Checks if user have exited the game
            running = False  # Get out of the loop
    # Draw Here...
    pygame.display.flip()  # Draw everything on to the screen

pygame.quit()  # Quit Pygame
sys.exit()  # Quit Python
