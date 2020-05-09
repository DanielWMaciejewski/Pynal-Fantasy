import pygame
import math
import random
from pygame import mixer

#This chunk handles the basic initializations for sound and screen
#initialize pygame
pygame.init()
#soundtrack
pygame.mixer.music.load('314e Dancing Mad (part 5).mp3')
pygame.mixer.music.play(-1)
#create the screen
screen = pygame.display.set_mode((900,1000))
#Title and Icon
pygame.display.set_caption("Pynal Fantasy VI:KWE HEE HEE")
icon = pygame.image.load("40 - Kefka.gif")
pygame.display.set_icon(icon)
titleCard = pygame.image.load('TitleCard.png')

#background
background = pygame.image.load('background.png')

#effect stuff
boom =pygame.image.load('fire_bullet.gif')

#This chunk defines player and enemy parameters

#Kefka
kefka = pygame.image.load('40 - Kefka.gif')
kefkaX_position = 200
kefkaY_position = 10
kefkaX_Change = 0
kefka_hp = 666

#kefka's projectile
kefkaProjectile = pygame.image.load('Fire.gif')
kefkaProjectileX = kefkaX_position
kefkaProjectileY = kefkaY_position
kefkaProjectileYChange = 10
kefkaProjectileState = "ready"

#Terra(Player)
terra = pygame.image.load('Terra - Esper - Angry.gif')
terraX_position = 300
terraY_position = 900
terraX_velocity = 0
terra_hp = 10000

#Terra HP Display
terraHpDisplay = terra_hp
font = pygame.font.Font('freesansbold.ttf',32)
terraTextX = 300
terraTextY = 950

#Terra's projectile
weakBlast = pygame.image.load('White Sword (up).gif')
weakBlastX = terraX_position+10
weakBlastY = terraY_position+2
weakBlastY_change = 40
weakBlastState = "ready"

#effects
def weakExplosion(weakBlastX,weakBlastY):
    screen.blit(boom,(weakBlastX,weakBlastY+100))

def showTerraHP(terraTextX,terraTextY):
    terraHP = font.render("~*Life "+str(terra_hp)+"*~",True,(51,255,51))
    screen.blit(terraHP,(terraTextX,terraTextY))

#Player(Terra)
def Terra(terraX_position,terraY_position):
    screen.blit(terra, (terraX_position,terraY_position))

def terraWeakBlast(weakBlastX, weakBlastY):
    global weakBlastState
    weakBlastState = "fire"
    screen.blit(weakBlast, (weakBlastX - 7, weakBlastY + 10))

#terra collision
def weakBlastCollision(kefkaX_position,kefkaY_position,weakBlastX,weakBlastY):
    distance = math.sqrt((math.pow(kefkaX_position-weakBlastX,2) + math.pow(kefkaY_position-weakBlastY,2)))
    if distance <129:
        return True
    else:
        return False

#Kefka
def Kefka(kefkaX_position,kefkaY_position):
    screen.blit(kefka,(kefkaX_position,kefkaY_position))

def kefkasProjectile(kefkaProjectileX,kefkaProjectileY):
    global kefkaProjectileState
    kefkaProjectileState = "fire"
    screen.blit(kefkaProjectile,(kefkaProjectileX+230,kefkaProjectileY+130))

def terraCollision(terraX_position,terraY_position,kefkaProjectileX,kefkaProjectileY):
    distance = math.sqrt((math.pow(terraX_position-kefkaProjectileX,2) + math.pow(terraY_position-kefkaProjectileY,2)))
    if distance <terraX_position-100:
        return True
    else:
        return False
#Game Menu
# Game Loop
running = True
while running:
    
    screen.fill((0,200,255))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        #Player keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if weakBlastState is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    weakBlastX = terraX_position
                    terraWeakBlast(weakBlastX, weakBlastY)

            if event.key == pygame.K_LEFT:
                terra = pygame.image.load('Terra - Esper - Action.gif')
                terraX_velocity -= 5
            if event.key == pygame.K_RIGHT:
                terra = pygame.image.load('Terra - Esper - Hit.gif')
                terraX_velocity += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                terraX_velocity =0
            if event.key == pygame.K_RIGHT:
                terraX_velocity =0
        if event.type == pygame.QUIT:
            running = False

    #Kefka's motion
    if kefkaX_position >= 200:
        kefkaX_position += 1
    elif kefkaX_position == 50:
        kefkaX_position+= 1
    elif kefkaX_position == 550:
        kefkaX_position+= -1

    #Kefka Positions and inputs
    #enemy inputs
    kefkaX_position += kefkaX_Change
    if kefkaX_position <=0:
        kefkaX_position = 0
        kefkaX_Change += 1
    elif kefkaX_position >= 650:
        kefkaX_position = 650
        kefkaX_Change -= 1

    # Terra position
    terraX_position += terraX_velocity
    terraY_position
    if terraX_position <= 0:
        terraX_position = 0
    elif terraX_position >= 875:
        terraX_position = 875

    #Kefka's projectile
    kefkasProjectile(kefkaX_position,kefkaY_position)
    if kefkaProjectileState is "fire":
        kefkasProjectile(kefkaX_position,kefkaY_position)
        kefkaProjectileY += kefkaProjectileYChange
    if kefkaProjectileY >= 900:
        kefkaProjectileY = 200
        kefkaProjectileState = 'ready'
    if kefkaProjectileState is "fire":
        kefkasProjectile(kefkaX_position,kefkaProjectileY)
        kefkaProjectileY += kefkaProjectileYChange


    #weakblast movement
    if weakBlastState is "fire":
        terraWeakBlast(terraX_position,terraY_position)
        weakBlastY -= 1
    if weakBlastY <= 0:
        weakBlastY = 850
        weakBlastState = 'ready'
    if weakBlastState is "fire":
        terraWeakBlast(weakBlastX,weakBlastY)
        weakBlastY -= weakBlastY_change

    #weakBlast Collision
    weakCollision = weakBlastCollision(kefkaX_position + 120, kefkaY_position, weakBlastX, weakBlastY)
    if weakCollision:
        weakExplosion(weakBlastX, weakBlastY)
        weakBlastY = 480
        weakBlastState = "ready"
        kefka_hp -= 10
        bulletSound = mixer.Sound("435415__v-ktor__explosion10.wav")
        bulletSound.play()

    #Player/Opponent sprites positional updating
    Terra(terraX_position,terraY_position)
    Kefka(kefkaX_position,kefkaY_position)

    # Terra's HP display
    showTerraHP(terraTextX, terraTextY)

    # Terra collision
    terraCollide = terraCollision(terraX_position, terraY_position, kefkaProjectileX, kefkaProjectileY)
    if terraCollide:
        terra_hp -= 1
        if terra_hp < 0:
            running = False
    if kefka_hp < 0:
        running = False

    pygame.display.update()