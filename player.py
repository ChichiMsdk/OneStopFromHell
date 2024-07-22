import pygame
from utils import *

# checks to prevent players to go out of bounds
# p1 = player1
def check_p1(x, nb):
    if x > nb[0]:
        return nb[0]
    if x < nb[1]:
        return nb[1]
    return x

def check_p2(x, nb):
    if x < nb[0]:
        return nb[0]
    if x > nb[1]:
        return nb[1]
    return x

class Timer:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.running = False

    def start_timer(self):
        self.start = pygame.time.get_ticks()
    
    def get_elapsed(self):
        self.end = (pygame.time.get_ticks() - self.start) / 1000
        return self.end

class Player:
    def __init__(self, position, color, keys, fn_check, limit, image, name, id):
        self.id = id
        self.x = position[0]
        self.y = position[1]
        self.currentX = self.x
        self.currentY = self.y
        self.previousX = self.currentX
        self.previousY = self.currentY
        self.color = color
        self.image = image
        self.name = name
        self.attacks = []
        self.attacking = False
        
        self.timer = Timer()
        # this is for the player to never cross the middle
        self.check = fn_check
        self.limit = limit

        self.health = 100
        self.mapping = Mapping(keys)

    def draw(self, grid):
        a = 3 # adjust the rect inside the grid
        # smooth transitions
        if self.attacks:
            pygame.draw.rect(grid.screen, RED, pygame.Rect(self.attacks[0], [100, 100]))

            if self.timer.get_elapsed() >= 0.5:
                del self.attacks[0]
                self.attacking = False

        self.currentX = interpolate(self.previousX, self.x, 0.1)
        self.currentY = interpolate(self.previousY, self.y, 0.1)
        self.previousX = self.currentX
        self.previousY = self.currentY
        grid.screen.blit(self.image, (self.currentX, self.currentY))

class Mapping:
    def __init__(self, keys):
        self.kUP = keys[0]
        self.kDOWN = keys[1]
        self.kLEFT = keys[2]
        self.kRIGHT = keys[3]
        self.kATK = keys[4]

    def up(self, player):
        player.y = player.y - 100
        if player.y < 0:
            player.y = 9 * 100
            player.currentY = player.y
            player.previousY = player.y

    def down(self, player):
        player.y = player.y + 100
        if player.y > 9 * 100:
            player.y = 0
            player.currentY = player.y
            player.previousY = player.y

    def left(self, player):
        player.x = player.x - 100
        player.x = player.check(player.x, player.limit)

    def right(self, player):
        player.x = player.x + 100
        player.x = player.check(player.x, player.limit)

#TODO: use attacks as entity that will hold their own start/end distance etc so its easier
    def attack(self, player):
        if not player.attacking == True:
            if player.id == 0:
                x = player.x + 100
            else:
                x = player.x - 100
            y = player.y
            player.attacks.append([x, y])
            player.timer.start_timer()
            player.attacking = True
            print(f"Player {player.name} attacks here -> x:{x} y:{y}")
