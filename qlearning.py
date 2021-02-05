import numpy as np
import time
import pygame
from display import MainRun

class Qlearning:


    def __init__(self):
        self.environment_rows = 5
        self.environment_columns = 5
        self.epsilon = 0.9
        self.discount_factor = 0.9
        self.learning_rate = 0.9
        self.q_values = np.zeros((self.environment_rows,self.environment_columns,4))
        self.actions = ['up','right','down','left']
        self.rewards = np.full((self.environment_rows, self.environment_columns),-1)
        self.totalcheese = 0

        self.start_location = {}
        self.end_location = {}
        self.maze_box = {}
        self.maze_box[0] = [i for i in range(0,5)]
        self.maze_box[1] = [i for i in range(0,5)]
        self.maze_box[2] = [i for i in range(0,5)]
        self.maze_box[3] = [i for i in range(0,5)]
        self.maze_box[4] = [i for i in range(0,5)]
        self.end_of_maze = list()
        self.start_of_maze = list()
        self.location_of_cheese = list()


    def set_environment(self,input_grid):
        self.secret_grid = input_grid
        self.orig_grid = input_grid
        for i in range(len(input_grid)):
            for j in range(len(input_grid[i])):
                if input_grid[i][j]==1:
                    self.start_row = i
                    self.start_column = j
                    

                elif input_grid[i][j] == 3:
                    self.rewards[i][j] = 1000.0
                    self.totalcheese +=1

                elif input_grid[i][j]==2:
                    self.end_location[i]=j
                    self.rewards[i][j] = -100.0
        #printing the rewards layout for debugging
        print(self.rewards)

    def is_the_end_location(self,current_row_index, current_column_index):
        ### Check if Mr. Mouse is now in the exit ###
        if self.rewards[current_row_index][current_column_index] == 1000.0:
            return True
        else:
            False

    def this_is_the_start_location(self):
        current_row_index = np.random.randint(self.environment_rows)
        current_column_index = np.random.randint(self.environment_columns)
        while self.is_the_end_location(current_row_index,current_column_index):
            current_row_index = np.random.randint(self.environment_rows)
            current_column_index = np.random.randint(self.environment_columns)
        
        return current_row_index,current_column_index

    def get_next_action(self,current_row_index,current_column_index,epsilon):
        if np.random.random() < epsilon:
            return np.argmax(self.q_values[current_row_index,current_column_index])

        else:
            return np.random.randint(4)

    def get_next_location(self,current_row_index,current_column_index,action_index):
        new_row_index = current_row_index
        new_column_index = current_column_index
        if self.actions[action_index] == 'up' and current_row_index > 0:
            new_row_index -= 1
        elif self.actions[action_index] == 'right' and current_column_index < self.environment_columns-1:
            new_column_index += 1
        elif self.actions[action_index] == 'down' and current_row_index < self.environment_rows -1:
            new_row_index += 1
        elif self.actions[action_index] == 'left' and current_column_index > 0:
            new_column_index -= 1

        return new_row_index,new_column_index

    def find_my_cheese(self):

        current_row_index, current_column_index = self.start_row, self.start_column
        cheese = list()
        cheese.append([current_row_index,current_column_index])
        
        while not self.is_the_end_location(current_row_index,current_column_index):
            action_index = self.get_next_action(current_row_index, current_column_index,0.9)
            current_row_index,current_column_index = self.get_next_location(current_row_index,current_column_index,action_index)
            # print(current_row_index,end=" "),print(current_column_index,end="ac:"),print(action_index)
            cheese.append([current_row_index,current_column_index])

        return cheese


    def saitama_training(self,hehe_grid):
        self.speed = 0.01
        for episode in range(0,2000,1):
            # row_index,column_index = self.this_is_the_start_location()
            row_index,column_index = self.start_row, self.start_column
            self.hehe = hehe_grid
            # print("index:",end=" "),print(row_index,end=" "),print(column_index,end=" ")
            print("Episode: "+ str(episode))
            while not self.is_the_end_location(row_index,column_index) and self.rewards[row_index][column_index] != -100.0:
                grid = self.hehe
                
                action_index = self.get_next_action(row_index,column_index,self.epsilon)
                # print("Index:"+str(row_index)+str(column_index))
                # print("Action:",end=" "),print(action_index)
                old_row_index, old_column_index = row_index, column_index
                row_index, column_index = self.get_next_location(row_index, column_index,action_index)
                # if self.rewards[row_index][column_index] >= -1.0:
                if grid[row_index][column_index] < 5:
                    temp = grid[row_index][column_index]
                    grid[row_index][column_index]=4

                    reward = self.rewards[row_index,column_index]
                    self.speed = self.training_grid(grid,self.speed)


                    if temp ==2:
                        grid[row_index][column_index]=2
                    if temp ==0:
                        grid[row_index][column_index]=0
                    if self.is_the_end_location(row_index,column_index):
                        grid[row_index][column_index]=3
                    elif row_index == self.start_row and column_index == self.start_column or temp==1:
                        grid[row_index][column_index]=1
                    # print("Reward:",end=" "),print(reward)
                    old_q_value = self.q_values[old_row_index, old_column_index,action_index]
                    temporal_difference = reward + ( self.discount_factor * np.max(self.q_values[row_index,column_index])) - old_q_value

                    new_q_value = old_q_value + (self.learning_rate * temporal_difference)
                    self.q_values[old_row_index,old_column_index,action_index] = new_q_value
                    # print("Index:" + str(row_index) + str(column_index))

                else:
                    row_index, column_index = old_row_index, old_column_index 
        # print(self.rewards)
        print("Training Complete!")

    def training_grid(self,grid,speed):
        dp = MainRun((305,305))
        speed = dp.displaytraining(grid,speed)
        return speed
        




            







    

    



