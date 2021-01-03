import pygame
from random import randint
from random import seed

winw = 400
winh = 400

pygame.font.init()
win = pygame.display.set_mode((winw, winh + 20))
myfont = pygame.font.SysFont('Calibri bold', 30)
lose = pygame.font.SysFont('Comic Sans MS', winw // 13)

seed()

WALLCOLOR = (255, 0, 0)
def setFood():
    global ax, ay
    ax = randint(2, winw // 20 - 1) * 20
    ay = randint(2, (winh // 20 - 1)) * 20 + 20

def drawWalls():
    pygame.draw.line(win, WALLCOLOR, [1, 20], [1, winh - 1 + 20], 6)
    pygame.draw.line(win, WALLCOLOR, [1, 20], [winw - 1, 20], 6)
    pygame.draw.line(win, WALLCOLOR, [1, winh - 1 + 20], [winw - 1, winh - 1 + 20], 6)
    pygame.draw.line(win, WALLCOLOR, [winw - 1, 20], [winw - 1, winh - 1 + 20], 6)

def update():
    win.fill((40, 44, 52))
    drawWalls()
    pygame.draw.circle(win, (0, 255, 0), (ax, ay), radius)
    pygame.draw.circle(win, (255, 0, 0), (x, y), radius)
    if leng >= 1:
        for i in range(leng):
            pygame.draw.circle(win, (255, 255, 0), (tailx[i], taily[i]), radius)
    win.blit(textsurface, (1, 1))
    pygame.display.update()

def losing():
    run1 = True
    win.fill((40, 44, 52))
    win.blit(losesurface, (5, winh // 2 - winh // 4))
    win.blit(losesurface2, (5, winw // 2 + winw // 4))
    pygame.display.update()
    while run1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global run
                run = False
                run1 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    global x, y, leng, vx, vy, ax, ay
                    leng = 0
                    x = winw // 2
                    y = winh // 2
                    vx = 0
                    vy = 0
                    setFood()
                    update()
                    run1 = False

x = winw // 2
y = winh // 2
radius = 10
speed = 20
vx = 0
vy = 0
setFood()
run = True
leng = 0
tailx = list(range(200))
taily = list(range(200))
foodInS = False
run1 = False

while run:
    pygame.time.delay(100)
    textsurface = myfont.render(str(leng), True, (255, 255, 255))
    losesurface = lose.render("You lose. Your score: " + str (leng), True, (255, 255, 255))
    losesurface2 = lose.render("Press TAB for restart", True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and vx == 0:
        vx = -speed
        vy = 0
    elif keys[pygame.K_RIGHT] and vx == 0:
        vx = speed
        vy = 0
    elif keys[pygame.K_UP] and vy == 0:
        vx = 0
        vy = -speed
    elif keys[pygame.K_DOWN] and vy == 0:
        vx = 0
        vy = speed

    if x == ax and y == ay:
        foodInS = True
        while foodInS:
            setFood()
            for i in range (leng + 1):
                if ax == tailx[i] and ay == taily[i]:
                    setFood()
                else:
                    foodInS = False
        leng += 1

    for i in range(1, leng + 1):
        if x == tailx[i] and y == taily[i]:
            losing()

    if x >= winw or x <= 0 or y >= winh + 20 or y <= 20:
        losing()

    for i in range(leng, 0, -1):
        tailx[i] = tailx[i - 1]
        taily[i] = taily[i - 1]

    tailx[0] = x
    taily[0] = y

    x += vx
    y += vy

    update()

