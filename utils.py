from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_i, K_j, K_k, K_l,
        K_BACKSPACE, K_SPACE,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        )

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

RUNNING = True
WIN_HEIGHT = 500
WIN_WIDTH = 500

def ease_in_out_quad(t):
    if t < 0.5:
        return 2.0 * t * t;
    else: 
        return -1.0 + (4.0 - 2.0 * t) * t;

def interpolate(start, end, factor):
    easedFactor = ease_in_out_quad(factor);
    return start + easedFactor * (end - start);

def increase_rect(rect, deltaW, deltaH):
    centerX = rect.x + rect.w / 2;
    centerY = rect.y + rect.h / 2;

    newW = rect.w + deltaW;
    newH = rect.h + deltaH;

    newX = centerX - newW / 2;
    newY = centerY - newH / 2;

    newRect = [newX, newY, newW, newH];
    return newRect;

