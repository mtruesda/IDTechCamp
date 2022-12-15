import pygame
import sys
from pygame.locals import *

pygame.init()
# All the above is required to make a pygame.

#///////////////////////////////////////////////////////////////////////////////

screen = pygame.display.set_mode((640,460))
#The above makes the screen 640 pixels by 460 pixels, super important.

#running the program now would crash it there is another group of code needed to
#-prevent this.

screen.fill((25,50, 200))#Makes the screen blue. This involves  combining colors
#the first number defines how much red, the second number defines the amount of
#green and the third number defines how much blue.

pygame.display.set_caption("Bubble Buster")
#This sets the caption to cow jumper.

#///////////////////////////////////////////////////////////////////////////////

player = pygame.Rect(300, 400, 60, 10)
#This sets the player at 300x, 400y. And the player has a width of sixty and a height
#of ten.
player_speed = 3
#This makes the playerspeed to 10

move_left = False
move_right = False
#Keeps the player from moving when he's not doing anythin

#///////////////////////////////////////////////////////////////////////////////

def draw_screen():
    screen.fill((25, 50, 200))

def draw_player():
    pygame.draw.rect(screen, (0, 0, 0), player)

#///////////////////////////////////////////////////////////////////////////////

#values for all bubbles to use
all_bubbles = []

bubble_radius = 20
bubble_edge = 1
initial_bubble_position = 70
bubble_spacing = 60
#This creates the bubbles

#///////////////////////////////////////////////////////////////////////////////

def create_bubbles():
    bubble_x = initial_bubble_position
    bubble_y = initial_bubble_position
#This creates two variables, bubble_x and bubble_y. it defines the positions of the bubbles.

    for rows in range(0, 3):
        for columns in range(0, 10):
        #Creates a for loop that creates bubbles between rows 0 and 10.
            bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble_x, bubble_y), bubble_radius, bubble_edge)
            bubble_x += bubble_spacing
            all_bubbles.append(bubble)
#lines 57 and 59 are required for the drawing of sed bubbles.
        bubble_y += bubble_spacing
        bubble_x = initial_bubble_position

create_bubbles()
#creates the bubbles

def draw_bubbles():

    for bubble in all_bubbles:
        bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble.x, bubble.y), bubble_radius, bubble_edge)

#The above will redraw the screen and player to make it so that the player is no
#longer just painting the screen black and it makes the player actually move altogether

while True:
    # check for events

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#The above right here will keep this game from crashing when I run it. It makes
#it so that only the player can open and close this game.
            #Keyboard input for players

        if event.type == KEYDOWN:
            #Keydown means that this will occur when the key is down.

            if event.key == K_a:
                move_right = False
                move_left = True
                #This says that when a is pressed, moving left is possible and
                #moving right is NOT.


            if event.key == K_d:
                move_left = False
                move_right = True
                #this is the opposite, when d is pressed, moving right is possible,
                #Moving left is NOT

        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False
                #This altogether says when the keys aren't being pressed they
                #are not moving.

        if move_left and player.left > 0:
            player.x -= player_speed
        if move_right and player.right < 640:
            player.x += player_speed

        draw_screen()
        draw_player()
        draw_bubbles()
        pygame.display.update()
    #draws a player.


#part of making the screen blue ^^

