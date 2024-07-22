import copy
import pygame
import random
from utils import *
from card import *

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

class Player:
    def __init__(self, position, color, keys, fn_check, limit, image, name, id, anims):
        self.id = id
        self.x = position[0]
        self.y = position[1]
        self.c= 0
        self.currentX = self.x
        self.currentY = self.y
        self.previousX = self.currentX
        self.previousY = self.currentY
        self.color = color
        self.image = image
        self.mal = False
        self.timer2 = Timer()
        self.timer3 = Timer()
        self.anims = anims
        self.name = name
        self.spells = Card.shuffle_3()
        self.attacks1 = []
        self.attacks2 = []
        self.attacking = False
        self.pa = 100
        
        self.timer = Timer()
        # this is for the player to never cross the middle
        self.check = fn_check
        self.limit = limit

        self.health = 100
        self.mapping = Mapping(keys)

    def draw_atk(self, grid):
        if self.id == 0:
            if len(self.attacks1) != 0:
                for atk in self.attacks1:
                    for pos in atk.position:
                        # pygame.draw.rect(grid.screen, RED, pygame.Rect([pos[0], pos[1]], [100, 100]))
                        grid.screen.blit(self.anims[self.c], (pos[0] + 20, pos[1] + 20))
                        if atk.timer2.get_elapsed() >= 0.1:
                            self.c = self.c + 1
                            if self.c > 6:
                                self.c = 0
                            atk.timer2.start_timer()

                    if atk.timer.get_elapsed() >= 0.5:
                        # self.attacks1.remove(atk)
                        del self.attacks1[0]
                        self.attacking = False
                        self.c = 0
        else:
            if len(self.attacks2) != 0:
                for atk in self.attacks2:
                    for pos in atk.position:
                        # pygame.draw.rect(grid.screen, GREEN, pygame.Rect([pos[0], pos[1]], [100, 100]))
                        grid.screen.blit(self.anims[self.c], (pos[0] + 20, pos[1] + 20))
                        if atk.timer2.get_elapsed() >= 0.1:
                            self.c = self.c + 1
                            if self.c > 6:
                                self.c = 0
                            atk.timer2.start_timer()

                if atk.timer.get_elapsed() >= 0.5:
                    # self.attacks2.remove(atk)
                    del self.attacks2[0]
                    self.attacking = False
                    self.c = 0

    def draw(self, grid):
        a = 3 # adjust the rect inside the grid
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

    def attack(self, player):
        # spell_chosen = copy.deepcopy(random.choice(player.spells))
        # spell_chosen2 = copy.deepcopy(random.choice(player.spells))

        elems = []
        elems2 = []
        if not player.attacking == True:
            if player.id == 0:
                # spell_chosen = copy.deepcopy(ice_throw)
                spell_chosen = copy.deepcopy(random.choice(player.spells))
                spell_pos = spell_chosen.position
                atk1 = [None] * 2
                for i in range(len(spell_pos)):
                    atk1[0] = player.x + spell_pos[i][0]
                    atk1[1] = player.y + spell_pos[i][1]
                    elems.append([atk1[0], atk1[1]])
                spell_chosen.position = elems.copy()
                spell_chosen.timer.start_timer()
                spell_chosen.timer2.start_timer()
                player.attacks1.append(spell_chosen)
            else:
                spell_chosen2 = copy.deepcopy(random.choice(player.spells))
                spell_pos2 = spell_chosen2.position
                atk2 = [None] * 2
                for i in range(len(spell_pos2)):
                    atk2[0] = player.x - spell_pos2[i][0]
                    atk2[1] = player.y - spell_pos2[i][1]
                    elems2.append([atk2[0], atk2[1]])
                spell_chosen2.position = elems2.copy()
                spell_chosen2.timer.start_timer()
                spell_chosen2.timer2.start_timer()
                player.attacks2.append(spell_chosen2)
            
            player.attacking = True
