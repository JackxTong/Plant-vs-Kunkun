import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 600  # Window size
GRID_SIZE = 50  # Size of the grid cells
FONT_SIZE = 16  # Font size for coordinate labels
LINE_COLOR = (200, 200, 200)  # Light gray for the grid lines
TEXT_COLOR = (0, 0, 0)  # Black for the coordinate labels
BACKGROUND_COLOR = (255, 255, 255)  # White background

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Coordinate System")

# Load font
font = pygame.font.SysFont('Arial', FONT_SIZE)

def draw_grid():
    # Draw vertical grid lines
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, HEIGHT))
        label = font.render(str(x), True, TEXT_COLOR)
        screen.blit(label, (x, 0))
    
    # Draw horizontal grid lines
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, y), (WIDTH, y))
        label = font.render(str(y), True, TEXT_COLOR)
        screen.blit(label, (0, y))

def main():
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background
        screen.fill(BACKGROUND_COLOR)
        
        # Draw the grid
        draw_grid()
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
