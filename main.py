import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((500, 650))
icon = pygame.image.load('b2.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("NOHZDYVE")
clock = pygame.time.Clock()

playerx = 250
playery = 250
playerx_change = 0
playery_change = 0

clothx = 0
clothy = 500
clothy_change = 0


def cloth(x, y):
    screen.blit(pygame.image.load('bgcloth.png'), (x, y))
    screen.blit(pygame.image.load('bgcloth2.png'), (x, y + 500))
    screen.blit(pygame.image.load('bgcloth3.png'), (x, y + 1000))
    screen.blit(pygame.image.load('bgcloth4.png'), (x, y + 1500))
    screen.blit(pygame.image.load('bgcloth5.png'), (x, y + 2000))



p1 = pygame.image.load('p1.png')
p2 = pygame.image.load('p2.png')
y1 = pygame.image.load('y1.png')
y2 = pygame.image.load('y2.png')

px = 50
py = 500
px_change = 0
py_change = 0

yx = 100
yy = 1000
yx_change = 0
yy_change = 0
score_value = 0
font = pygame.font.Font('pixel.ttf', 17)
fonts = pygame.font.Font('pixel.ttf', 50)

jawbx = 50
jawby = 500
jawgx = 50
jawgy = 1000
jawbx_change = 0
jawby_change = 0
jawgx_change = 0
jawgy_change = 0


def show_score():
    score = font.render("SCORE: " + str(score_value), True, (255, 0, 255))
    screen.blit(score, (200, 5))


def collisionp(playerx, playery, px, py):
    dist = math.sqrt(math.pow(playerx - px, 2) + math.pow(playery - py, 2))
    if dist < 70:
        return True
    else:
        return False


def collisiony(playerx, playery, yx, yy):
    dist = math.sqrt(math.pow(playerx - yx, 2) + math.pow(playery - yy, 2))
    if dist < 25:
        return True
    else:
        return False


def collisionb(playerx, playery, jawbx, jawby):
    dist = math.sqrt(math.pow(playerx - jawbx, 2) + math.pow(playery - jawby, 2))
    if dist < 30:
        return True
    else:
        return False


def collisiong(playerx, playery, jawgx, jawgy):
    dist = math.sqrt(math.pow(playerx - jawgx, 2) + math.pow(playery - jawgy, 2))
    if dist < 30:
        return True
    else:
        return False


def player(x, y):
    screen.blit(pygame.image.load('man.png'), (x, y))


fan1y = 250
fan2y = 900
fan1x = 30
fan2x = 400
fany1_change = 0


def fan(x, y):
    screen.blit(pygame.image.load('leftfan.png'), (x, y))


def fan2(x, y):
    screen.blit(pygame.image.load('rightfan.png'), (x, y))


def border():
    screen.blit(pygame.image.load('border.jpg'), (2, 0))
    screen.blit(pygame.image.load('border.jpg'), (2, 559))

    screen.blit(pygame.image.load('border1.png'), (468, 0))
    screen.blit(pygame.image.load('border1.png'), (468, 559))


ax = -22
ay = 100
ay_change = 0


def a(x, y):
    screen.blit(pygame.image.load('ledgeright.png'), (421, y + 70))
    screen.blit(pygame.image.load('ledgeright.png'), (421, y + 350))
    screen.blit(pygame.image.load('ledgeleft.png'), (5, y + 70))
    screen.blit(pygame.image.load('ledgeleft.png'), (5, y + 350))

    screen.blit(pygame.image.load('left.png'), (x, y))
    screen.blit(pygame.image.load('left.png'), (x, y + 600))
    screen.blit(pygame.image.load('right.png'), (432, y))
    screen.blit(pygame.image.load('right.png'), (432, y + 600))


currentimg = 1

life_val = 10


def life():
    life = font.render(" x " + str(life_val), True, (255, 0, 0))
    screen.blit(life, (52, 5))


def game_over():
    over = fonts.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over, (90, 200))
    score = fonts.render("SCORE: " + str(score_value), True, (153, 0, 76))
    screen.blit(score, (90, 260))


run = True
while run:
    screen.fill((0, 0, 0))
    mixer.music.load('music.mp3')
    mixer.music.play(-1)

    screen.blit(pygame.image.load('life.png'), (35, 5))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            fany1_change = -15
            ay_change = -15
            clothy_change = -15

            if event.key == pygame.K_LEFT:
                playerx_change = -20

            if event.key == pygame.K_RIGHT:
                playerx_change = 20

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass

    collision1 = collisionp(playerx, playery, px, py)
    if collision1:
        px = random.randint(50, 400)
        py = random.randint(500, 700)
        score_value += 10
        mixer.music.load('hit.mp3')
        mixer.music.play(0)
    collision2 = collisiony(playerx, playery, yx, yy)
    if collision2:
        yx = random.randint(50, 400)
        yy = random.randint(700, 1000)
        score_value += 10
        mixer.music.load('hit.mp3')
        mixer.music.play(0)

    collision3 = collisionb(playerx, playery, jawbx, jawby)
    collision4 = collisiong(playerx, playery, jawgx, jawgy)

    if collision3 or collision4:
        #playerx = 250
        #playery = 250
        life_val -= 1
        mixer.music.load('hit.mp3')
        mixer.music.play(0)
    playerx += playerx_change
    clothy += clothy_change

    if clothy <= -2100:
        clothy = 600

    if playerx <= 20:
        playerx = 20
        life_val-=1
        mixer.music.load('hit.mp3')
        mixer.music.play(0)

    if playerx >= 420:
        playerx = 420
        life_val-=1
        mixer.music.load('hit.mp3')
        mixer.music.play(0)

    if (currentimg == 1):
        screen.blit(p1, (px, py))
        screen.blit(y1, (yx, yy + 100))
        screen.blit(pygame.image.load('bluejaw1.png'), (jawbx + 50, jawby + 50))
        screen.blit(pygame.image.load('greenjaw1.png'), (jawgx, jawgy))

    if (currentimg == 2):
        screen.blit(p2, (px, py))
        screen.blit(y2, (yx, yy + 100))
        screen.blit(pygame.image.load('bluejaw2.png'), (jawbx + 50, jawby + 50))
        screen.blit(pygame.image.load('greenjaw2.png'), (jawgx, jawgy))

    if (currentimg == 2):
        currentimg = 1
    else:
        currentimg += 1

    py_change = -10
    py += py_change

    if px >= 400:
        px_change = -10
    elif px <= 60:
        px_change = 10
    px += px_change
    if py <= -10:
        py = 600

    yy_change = -10
    yy += yy_change
    if yx >= 400:
        yx_change = -10
    elif yx <= 110:
        yx_change = 10
    yx += yx_change
    if yy <= -200:
        yy = 600

    jawby_change = -5
    jawby += jawby_change
    if jawbx >= 300:
        jawbx_change = -10
    elif jawbx <= 60:
        jawbx_change = 10
    jawbx += jawbx_change
    if jawby <= -10:
        jawby = 600

    jawgy_change = -7

    jawgy += jawgy_change
    if jawgx >= 300:
        jawgx_change = -15
    elif jawgx <= 60:
        jawgx_change = 15
    jawgx += jawgx_change
    if jawgy <= -10:
        jawgy = 600

    if life_val == 0:
        game_over()
        jawgy = 10000
        jawby = 10000
        px = 10000
        yx = 10000
        playerx = 250

        playerx_change = 0
        playery_change = 10
        mixer.music.load('fall.mp3')
        mixer.music.play(0)

    playery += playery_change

    fan1y += fany1_change
    fan2y += fany1_change
    if fan1y < -80:
        fan1y = 1500
    if fan2y < -80:
        fan2y = 2500
    ay += ay_change
    if ay < -600:
        ay = 600

    player(playerx, playery)

    cloth(clothx, clothy)

    border()
    a(ax, ay)
    fan(fan1x, fan1y)
    fan2(fan2x, fan2y)

    show_score()
    life()
    pygame.display.update()
    clock.tick(10)
