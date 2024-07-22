from player import *
from spritesheet import *
from spritesheets import *
import time

CLOCK = pygame.time.Clock()

class App:
    def __init__(self, height, width):
        pygame.init()
        self.screen = pygame.display.set_mode([height, width])
        self.height = height
        self.width = width
        self.grid = Grid([self.height, self.width], [0,0], 10, self.screen)

class	Grid:
    def __init__(self, size, position, blockNumber, screen):
        self.height = int(size[0])
        self.width = int(size[1])
        self.x = int(position[0])
        self.y = int(position[1])
        self.blockNumber = blockNumber
        self.blockSize = self.width / self.blockNumber
        self.screen = screen

    def draw(self, screen):
        blockNumber = 10
        blockSize = self.width / blockNumber
        for x in range(int(self.x), self.width, int(blockSize)):
            for y in range(int(self.y), self.height, int(blockSize)):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, BLACK, rect, 1)

def events(players):
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                RUNNING = False
            for player in players:
                if event.key == player.mapping.kUP:
                    player.mapping.up(player)
                if event.key == player.mapping.kDOWN:
                    player.mapping.down(player)
                if event.key == player.mapping.kLEFT:
                    player.mapping.left(player)
                if event.key == player.mapping.kRIGHT:
                    player.mapping.right(player)
                if event.key == player.mapping.kATK:
                    player.mapping.attack(player)

def font_smooth(screen, players, smooth, surface):
        fontx = players[0].currentX + 25
        fonty = players[0].currentY - 35
        if fonty <= 0:
            fonty = players[0].currentY + 70 + 35

        font_smooth.c1[0] = interpolate(font_smooth.pr1[0], fontx, smooth)
        font_smooth.c1[1] = interpolate(font_smooth.pr1[1], fonty, smooth)
        screen.blit(surface[0], (font_smooth.c1[0], font_smooth.c1[1]))
        font_smooth.pr1 = font_smooth.c1
        draw_health_bar(screen, [font_smooth.c1[0] - 25, font_smooth.c1[1] + 30], players[0].health)

        fontx = players[1].currentX + 25
        fonty = players[1].currentY - 35
        if fonty <= 0:
            fonty = players[1].currentY + 70 + 35
        font_smooth.c2[0] = interpolate(font_smooth.pr2[0], fontx, smooth)
        font_smooth.c2[1] = interpolate(font_smooth.pr2[1], fonty, smooth)
        screen.blit(surface[1], (font_smooth.c2[0], font_smooth.c2[1]))
        font_smooth.pr2 = font_smooth.c2
        draw_health_bar(screen, [font_smooth.c2[0] - 25, font_smooth.c2[1] + 30], players[1].health)

# dogshit python won't allow me to have static variables otherwise
font_smooth.c1 = [0, 0]
font_smooth.c2 = [0, 0]
font_smooth.pr1 = [0, 0]
font_smooth.pr2 = [0, 0]

def check_dmg(player):

    if player[1].attacks2 and player[0].mal == False:
        for i in range(len(player[1].attacks2[0].position)):
            if player[0].x == player[1].attacks2[0].position[i][0] and player[0].y == player[1].attacks2[0].position[i][1]:
                player[0].health = player[0].health - player[1].attacks2[0].damage
                print(f"{player[0].id} {player[0].health}pv")
                player[0].mal = True
                player[0].timer2.start_timer()

    if player[0].attacks1 and player[1].mal == False:
        for i in range(len(player[0].attacks1[0].position)):
            if player[1].x == player[0].attacks1[0].position[i][0] and player[1].y == player[0].attacks1[0].position[i][1]:
                player[1].health = player[1].health - player[0].attacks1[0].damage
                print(f"{player[1].id} {player[1].health}pv")
                player[1].mal = True
                player[1].timer2.start_timer()

HEALTH_BAR_WIDTH = 100
HEALTH_BAR_HEIGHT = 10
MAX_HEALTH = 100

def draw_health_bar(screen, pos, current_health):
    health_ratio = current_health / MAX_HEALTH
    health_bar_width = HEALTH_BAR_WIDTH * health_ratio
    pygame.draw.rect(screen, RED, (pos[0], pos[1], HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    pygame.draw.rect(screen, GREEN, (pos[0], pos[1], health_bar_width, HEALTH_BAR_HEIGHT))

BLEU = (0, 128, 128)

def mymain():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    app = App(1000, 1000)
    pygame.display.set_caption("One Step From Hell")


    key_p1 = [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE]
    key_p2 = [K_i, K_k, K_j, K_l, K_p]
    str_p = ["P1", "P2"]

    anim1 = pygame.image.load('./image/atk1-19-22.png')
    anim2 = pygame.image.load('./image/atk2-27-29.png')
    anim3 = pygame.image.load('./image/atk3-38-38.png')
    anim4 = pygame.image.load('./image/atk4-47-52.png')
    anim5 = pygame.image.load('./image/atk5-57-54.png')
    anim6 = pygame.image.load('./image/atk6-58-58.png')
    anim7 = pygame.image.load('./image/atk7-61-43.png')
    anim1.set_colorkey(BLEU)
    anim2.set_colorkey(BLEU)
    anim3.set_colorkey(BLEU)
    anim4.set_colorkey(BLEU)
    anim5.set_colorkey(BLEU)
    anim6.set_colorkey(BLEU)
    anim7.set_colorkey(BLEU)
    anims = [anim1, anim2, anim3, anim4, anim5, anim6, anim7]

    players = [Player([int(0), int(500)], RED, key_p1, check_p1, [400, 0], sala_png, str_p[0], 0, anims),
               Player([int(900), int(500)], GREEN, key_p2, check_p2, [500, 900], goinfrex_png, str_p[1], 1, anims)]

    surface = [pygame.font.Font.render(font, str_p[0], True, BLACK),
               pygame.font.Font.render(font, str_p[1], True, BLACK)]


    smooth = 0.08
    while RUNNING:
        events(players)
        pygame.event.get()
        app.screen.fill((255, 255, 255))

        app.grid.draw(app.screen)
        players[0].draw(app.grid)
        players[1].draw(app.grid)
        players[0].draw_atk(app.grid)
        players[1].draw_atk(app.grid)
        check_dmg(players)
        for player in players:
            if player.timer2.get_elapsed() >= 0.5:
                player.mal = False
        # displays the "P1" "P2" right above the players
        font_smooth(app.screen, players, smooth, surface)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
	mymain()
