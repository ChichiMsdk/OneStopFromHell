#%%
import random
from utils import *
#pv : max 100 (spell max : 30)
#pa : max 10 

class Card:
    list_spells = []

    def __init__(self, name, pa, damage = 0, position = 0, timer = 0.5):
        self.name = name
        self.pa = pa
        self.damage = damage
        self.position = position
        self.timer = timer
        Card.list_spells.append(self)

    @staticmethod
    def shuffle_3():
        return random.choices(Card.list_spells, k=3)
    
    @staticmethod
    def shuffle_1():
        return random.choice(Card.list_spells)
    

class Attack:
    def __init__(self, start):
        self.start = start
        self.duration = start + 3

    


#%% spells

# def create_spells():


venom = Card('venom', 2, 10, [[400, 0], [400, -100], [400, 100], [500, 0], [300, 0], [200, 0], [600, 0]])
swords = Card('swords', 3, 15, [[200, 0], [200, -100], [200, 100], [300, 0], [300, -100], [300, 100], [400, 0]])
fireball = Card('fireball', 5, 10, [[400, 0], [400, -100], [400, 100], [300, 0], [500, 0]])
blizzard = Card('blizzard', 8, 20, [[100, 0], [200, 0], [300, 0], [400, 0], [500, 0]])
tornado = Card('tornado', 10, 30, [[500, 200], [500, 100], [500, 300], [400, 200], [600, 200], [600, 300], [600, 100], [400, 300], [400, 100], [300, 400], [300, 0], [700, 400], [700, 0]])
rockfall = Card('rockfall', 9, 15, [[200, 0], [200, 100], [200, 200], [200, 300], [200, 400], [200, -100], [200, -200], [200, -300]])
ice_throw = Card('ice_throw', 2, 2, [[600, 0]])
lane_fire = Card('lane_fire', 4, 8, [[100, 0], [200, 0], [300, 0], [400, 0], [500, 0], [600, 0], [700, 0]])
tsunami = Card('tsunami', 5, 12, [[100, -200], [100, -100], [100, 0], [100, 100], [100, 200], [200, -200], [200, -100], [200, 0], [200, 100], [200, 200]])
sun_burn = Card('sun_burn', 4, 10, [[300, 0], [300, -100], [300, 100], [400, 0], [500, 0]])


# #%% for testing

# map = [[' ' for _ in range(10)] for _ in range(5)]

# def affiche_map():
#     for i in map:
#         print(i)

# def place(pos, spell):
#     for i in spell:
#         try :
#             map[pos[1] + i[1]][pos[0] + i[0]] = 'X'
#         except:
#             pass
#     map[pos[1]][pos[0]] = 'O'
#     affiche_map()



# place((0,0), tsunami.position)

# # %%

# print(Card.shuffle_3())

# # %%
# print(Card.list_spells)
