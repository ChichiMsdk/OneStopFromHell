from player import *
from spritesheet import *
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

        fontx = players[1].currentX + 25
        fonty = players[1].currentY - 35
        if fonty <= 0:
            fonty = players[1].currentY + 70 + 35
        font_smooth.c2[0] = interpolate(font_smooth.pr2[0], fontx, smooth)
        font_smooth.c2[1] = interpolate(font_smooth.pr2[1], fonty, smooth)
        screen.blit(surface[1], (font_smooth.c2[0], font_smooth.c2[1]))
        font_smooth.pr2 = font_smooth.c2

# dogshit python won't allow me to have static variables otherwise
font_smooth.c1 = [0, 0]
font_smooth.c2 = [0, 0]
font_smooth.pr1 = [0, 0]
font_smooth.pr2 = [0, 0]

def mymain():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    app = App(1000, 1000)
    pygame.display.set_caption("One Step From Hell")


    key_p1 = [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE]
    key_p2 = [K_i, K_k, K_j, K_l, K_p]
    str_p = ["P1", "P2"]

    players = [Player([int(0), int(500)], RED, key_p1, check_p1, [400, 0], sala_png, str_p[0], 0),
               Player([int(900), int(500)], GREEN, key_p2, check_p2, [500, 900], goinfrex_png, str_p[1], 1)]

    surface = [pygame.font.Font.render(font, str_p[0], True, BLACK),
               pygame.font.Font.render(font, str_p[1], True, BLACK)]

    smooth = 0.08
    while RUNNING:
        events(players)
        pygame.event.get()
        app.screen.fill((255, 255, 255))

        app.grid.draw(app.screen)
        players[0].draw_atk(app.grid)
        players[1].draw_atk(app.grid)
        players[0].draw(app.grid)
        players[1].draw(app.grid)

        # displays the "P1" "P2" right above the players
        font_smooth(app.screen, players, smooth, surface)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
	mymain()
