import pygame
import math
import random

# Intialize pygame
pygame.init()

# Creating a screen
screen = pygame.display.set_mode((800, 600))

# TITLE
pygame.display.set_caption("SHOOTING SHIPS")
# ICON
icon = pygame.image.load("laser.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Monster
monsterImg = pygame.image.load("monster.png")
monsterX = random.randint(0, 800)
monsterY = random.randint(50, 120)
monsterX_change = 0.3
monsterY_change = 40

# Bullet
bulletImg = pygame.image.load("bullet (1).png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def monster(x, y):
    screen.blit(monsterImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def collision(monsterX, monsterY, bulletX, bulletY):
    distance = math.sqrt(math.pow(monsterX - bulletX, 2) + math.pow(monsterY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
# infinite loop(while)
running = True
while running:

    screen.fill((0, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if some key pressed check if it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    monsterX += monsterX_change

    if monsterX <= 0:
        monsterX_change = 0.3
        monsterY += monsterY_change
    elif monsterX >= 736:
        monsterX_change = -0.3
        monsterY += monsterY_change

    # Shooting bullets
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collide
    collide = collision(monsterX, monsterY, bulletX, bulletY)
    if collide:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        monsterX = random.randint(0, 800)
        monsterY = random.randint(50, 120)
        
    player(playerX, playerY)
    monster(monsterX, monsterY)
    pygame.display.update()
