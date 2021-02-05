import pygame
import keyboard
from qlearning import Qlearning
from display import MainRun

size = (305,305)
main = MainRun(size)
main.Main()
game = Qlearning()
game.set_environment(main.iGrid)

print("Instructions:")
print("Click the white box to change color:")
print("White = Path")
print("Green = Starting point (only one)")
print("Yellow = end point (if no yellow box, the training will not start")
print("Red = Block ")
print("Press Enter key to begin")
game.saitama_training(main.iGrid)
cheese = game.find_my_cheese()
main.after_training(cheese,main.iGrid)
