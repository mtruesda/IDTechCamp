import pygame
import sys
from pygame.locals import *

pygame.init()

#/////////////////////////////////////////////////////////////////////////

screen = pygame.display.set_mode((640, 460))
screen.fill((255, 255, 255))
pygame.display.set_caption('Bubble Buster!')

#///////////////////////////////////////////////////////////////////////

#create and set up values for the player
player = pygame.Rect(300, 400, 60, 10)
player_speed = 3

move_left = False
move_right = False

#///////////////////////////////////////////////////////////////////////

def draw_screen():
    screen.fill((255, 255, 255))
def draw_player():
    pygame.draw.rect(screen, (0, 0, 0), player)

#///////////////////////////////////////////////////////////////////////

#values for all bubbles to use
all_bubbles = []

bubble_radius = 20
bubble_edge = 1
initial_bubble_position = 70
bubble_spacing = 60

#////////////////////////////////////////////////////////////////////////

def create_bubbles():
    bubble_x = initial_bubble_position
    bubble_y = initial_bubble_position

    for rows in range(0, 3):
        for columns in range(0, 10):
            bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble_x, bubble_y), bubble_radius, bubble_edge)
            bubble_x += bubble_spacing
            all_bubbles.append(bubble)
        bubble_y += bubble_spacing
        bubble_x = initial_bubble_position



create_bubbles()

def draw_bubbles():
    for bubble in all_bubbles:
        bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble.x, bubble.y), bubble_radius, bubble_edge)

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Keyboard input for players
        if event.type == KEYDOWN:
            if event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_d:
                move_left = False
                move_right = True
        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False

    #Move the player
    if move_left and player.left > 0:
        player.x -= player_speed
    if move_right and player.right < 640:
        player.x += player_speed

    draw_screen()
    draw_player()
    draw_bubbles()
    pygame.display.update()
