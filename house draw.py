import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's/ Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0,00, 00)

# Function to draw a line using Breshenham algorithm
def draw_line_bresh(x1, y1, x2, y2):
    dx=abs(int(x2-x1))
    dy=abs(int(y2-y1))
    x = x1
    y = y1
    if (x2>x1):
        lx = 1
    else:
        lx = ly
    if (y2>y1):
        ly = 1
    else:
        ly = -1
    if(dx>dy):
        p = 2*dy - dx
        screen.set_at((round(x), round(y)), WHITE) 
        while(not(x==x2)):
            if(p<0):
                p = p + 2*dy
            else:
                y = y + ly
                p = p + 2*dy - 2*dx
                x = x + lx
            screen.set_at((round(x), round(y)), WHITE) 
    else:
        p = 2*dx - dy
        while(not(y==y2)):
            if(p<0):
                p = p + 2*dx
            else:
                x = x + lx
                p = p + 2*dx - 2*dy
            y = y + ly
            screen.set_at((round(x), round(y)), WHITE)       
      
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        #Drawing a house
        draw_line_bresh(20,10 ,10, 20)
        draw_line_bresh(20,10 ,30, 20)
        draw_line_bresh(10,20 ,30, 20)
        draw_line_bresh(10,20 ,10, 50)
        draw_line_bresh(10,50 ,30, 50)
        draw_line_bresh(30,20 ,30, 50)
        draw_line_bresh(30,35 ,50, 35)
        draw_line_bresh(30,50 ,50, 50)
        draw_line_bresh(50,20 ,50, 50)
        draw_line_bresh(50,50 ,70, 50)
        draw_line_bresh(70,50 ,70, 20)
        draw_line_bresh(50,20 ,70, 20)
        draw_line_bresh(50,20 ,60, 10)
        draw_line_bresh(60,10 ,70, 20)
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
   
   
   
   
   
   