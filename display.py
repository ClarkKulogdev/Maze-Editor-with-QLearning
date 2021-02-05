import pygame
import keyboard
import sys
import time

pygame.init()
size = (305,305)
screen = pygame.display.set_mode(size)
clock =pygame.time.Clock()

class MainRun(object):
    def __init__(self,size):
	    self.size = size

        # self.Main()

    def Main(self):
        
        #Put all variables up here
        #stopped = False
        BLACK    = (   0,   0,   0)
        WHITE    = ( 255, 255, 255)
        GREEN    = (   0, 255,   0)
        RED      = ( 255,   0,   0)
        YELLOW   = (255, 211, 0)
        ORANGE   = (255 , 100, 10)
        width = 55
        height = 55
        margin = 5
        grid = [[0 for x in range(5)] for y in range(5)]
        done = False

        while not done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop

                elif keyboard.is_pressed('Enter') and self.goal == True:
                    self.iGrid = grid
                    done = True

                elif keyboard.is_pressed('s'):
                    ###Reset Game####
                    grid = [[0 for x in range(5)] for y in range(5)]

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        column = pos[0] // (width + margin)
                        row = pos[1] // (height + margin)
                        # Debug prints
                        # print("Click ", pos, "Grid coordinates: ", row, column)
                        if grid[row][column] ==1:
                            grid[row][column] = 2
                            
                        elif grid[row][column] ==0:
                            grid[row][column] = 1
                        elif grid[row][column] ==2:
                            grid[row][column]=3
                            
                        elif grid[row][column]==3:
                            grid[row][column]=0
                            self.goal = False
                    except:
                        print("Non Grid was clicked!")

            # --- Game logic should go here
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            
            # --- Drawing code should go here

            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            screen.fill(BLACK)

            for row in range(5):
                for column in range(5):
                    if grid[row][column] == 1:
                        color = GREEN

                    elif grid[row][column] ==3:
                        color= YELLOW
                        self.goal = True
                    elif grid[row][column] ==0:
                        color = WHITE
                    elif grid[row][column]==2:
                        color = RED

                    pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
                
        
        # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

                # --- Limit to 60 frames per second
            clock.tick(60)

# if __name__ == __main__:
#     MainRun()
    def displaytraining(self,thisgrid,speed):
        # print("Test")
        # print(thisgrid)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                None 
            elif keyboard.is_pressed('space'):
                print("Speed down!")
                speed += 0.1
            elif keyboard.is_pressed('s'):
                print("Speed up!")
                speed -= 0.1
                if speed < 0.0:
                    speed = 0.1
            elif keyboard.is_pressed('Enter'):
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        BLACK    = (   0,   0,   0)
        WHITE    = ( 255, 255, 255)
        GREEN    = (   0, 255,   0)
        RED      = ( 255,   0,   0)
        YELLOW   = (255, 211, 0)
        BLUE = (0 , 0, 255)
        ORANGE = (255, 100,10)
        width = 55
        height = 55
        margin = 5
        grid = thisgrid
        for row in range(5):
            for column in range(5):
                if grid[row][column] == 1:
                    color = GREEN
                elif grid[row][column] ==3:
                    color= YELLOW
                elif grid[row][column] ==0:
                    color = WHITE
                elif grid[row][column]==2:
                    color = RED
                elif grid[row][column]==4:
                    color = BLUE
                elif grid[row][column]==5:
                    color = ORANGE
                pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
                

        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        time.sleep(speed)
                # --- Limit to 60 frames per second
        clock.tick(60)
        return speed


    def after_training(self,ai_learn,current_grid):
        done = False

        while not done:
            static_grid = current_grid
            
            for data in range(len(ai_learn)):
                for event in pygame.event.get():
                    if keyboard.is_pressed('Enter'):
                        done = True
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
                temp = static_grid[ai_learn[data][0]][ai_learn[data][1]]
                static_grid[ai_learn[data][0]][ai_learn[data][1]]=5
                self.displaytraining(static_grid,1)
                static_grid[ai_learn[data][0]][ai_learn[data][1]] = temp

