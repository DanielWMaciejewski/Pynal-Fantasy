#Daniel Maciejewski Beta Version 1.0 Pynal Fantasy 6:Kwehehe
#INFOST 350-001 Final Project
#Things unfixed ;_; @_@ :
#Player collision doesn't work
#gameLose screen bugs sometimes.
import math, random, os, pygame,sys
from pygame import mixer
#This centers the game window on Windows10
os.environ['SDL_VIDEO_CENTERED'] = '1'

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

#background
background = pygame.image.load('background.png')

#effect stuff
boom = pygame.image.load('fire_bullet.gif')

#Kefka
kefka = pygame.image.load('40 - Kefka.gif')
kefkaX_position = 200
kefkaY_position = 10
kefkaX_Change = 5
kefka_hp = 666

#kefka's projectile
kefkaProjectile = pygame.image.load('Red Star - Falling.gif')
kefkaProjectileX = 0
kefkaProjectileY = 0
kefkaProjectileYChange = 5
kefkaProjectileState = "ready"

#Terra(Player)
terra = pygame.image.load('Terra - Esper - Angry.gif')
terraX_position = 300
terraY_position = 900
terraX_velocity = 0
terraY_velocity = 0
terraHP = 100
population = 1500

#Terra HP Display
terraHpDisplay = population
font = pygame.font.Font('freesansbold.ttf',32)

#Terra's projectile
weakBlast = pygame.image.load('White Sword (up).gif')
weakBlastX = terraX_position+10
weakBlastY = terraY_position+2
weakBlastY_change = 20
weakBlastState = "ready"

def endKefka(kefka,kefkaX_position,kefkaY_position):
    screen.blit(kefka, (kefkaX_position, kefkaY_position))
def gameOver():
    kefkaX_position = 300
    kefkaY_position = 10
    kefka = pygame.image.load('40 - Kefka.gif')
    pygame.mixer.music.load('314a Dancing Mad (part 1).mp3')
    pygame.mixer.music.play(-1)


    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
            endKefka(kefka, kefkaX_position, kefkaY_position)
            gameOverStatement =font.render("Game Over!", True,(255, 51, 51) )
            screen.blit(gameOverStatement,(300,400))
            gameOverStatement = font.render("Kefka cleansed the Earth", True, (255, 51, 51))
            screen.blit(gameOverStatement, (300,430))
            gameOverStatement = font.render("of all human life", True, (255, 51, 51))
            screen.blit(gameOverStatement, (300, 460))
            gameOverStatement = font.render("in a nihilistic frenzy!", True, (255, 51, 51))
            screen.blit(gameOverStatement, (300, 490))
            gameOverStatement = font.render("KWE HEHEHEHE!!!!!", True, (255, 51, 51))
            screen.blit(gameOverStatement, (300, 520))

            pygame.display.update()

def endTerra(terra,terraX_position, terraY_position):
    screen.blit(terra, (terraX_position, terraY_position))
def gameWon(population):
    terra = pygame.image.load('Terra - Esper - Laugh.gif')
    terraX_position = 470
    terraY_position = 20
    pygame.mixer.music.load('106 Fanfare.mp3')
    pygame.mixer.music.play(-1)


    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
            endTerra(terra, terraX_position, terraY_position)
            gameOverStatement = font.render("YOU DID IT!!!", True, (0,0,153))
            screen.blit(gameOverStatement, (400, 400))
            gameOverStatement = font.render("The remaining "+str(population)+" humans", True, (0,0,153))
            screen.blit(gameOverStatement, (300, 430))
            gameOverStatement = font.render("shall carve out a new home", True, (0,0,153))
            screen.blit(gameOverStatement, (300, 460))
            gameOverStatement = font.render("in this World of Ruin!!", True, (0,0,153))
            screen.blit(gameOverStatement, (300, 490))
            gameOverStatement = font.render("Credits:", True, (0,0,153))
            screen.blit(gameOverStatement, (400, 520))
            gameOverStatement = font.render("Made by Dan Maciejewski", True, (0,0,153))
            screen.blit(gameOverStatement, (300, 610))
            gameOverStatement = font.render("Music: Nobuo Uematsu", True, (0,0,153))
            screen.blit(gameOverStatement, (300, 550))
            gameOverStatement = font.render("Sprites: Yoshitaka Amano ", True, (0,0,153))
            screen.blit(gameOverStatement, (300, 580))

            pygame.display.update()
def gameTips():
    tip1 = font.render("Arrow Keys to Move",True,(127,0,255))
    tip2 = font.render("SPACE to shoot",True,(127,0,255))
    screen.blit(tip1,(10,10))
    screen.blit(tip2, (10, 40))
#effects
def weakExplosion(weakBlastX,weakBlastY):
    screen.blit(boom,(weakBlastX,weakBlastY+100))

def showPopulation(population):
    populationRemaining = font.render("~~~~*Population Remaining" + str(population) + "*~~~~", True, (51, 255, 51))
    screen.blit(populationRemaining, (180, 970))

def showTerraHP(terraHP):
    terrasHP = font.render("Terra HP "+str(terraHP),True,(255,0,255))
    screen.blit(terrasHP,(350,940))
#Player(Terra)
def Terra(terraX_position,terraY_position):
    screen.blit(terra,(terraX_position,terraY_position))

def terraWeakBlast(weakBlastX, weakBlastY):
    global weakBlastState
    weakBlastState = "fire"
    screen.blit(weakBlast,(weakBlastX - 7, weakBlastY + 10))

#collision
def weakBlastCollision(kefkaX_position,kefkaY_position,weakBlastX,weakBlastY):
    distance = math.sqrt((math.pow(kefkaX_position-weakBlastX,2)) + (math.pow(kefkaY_position-weakBlastY,2)))
    if distance <129:
        return True
    else:
        return False

def terraCollision(terraX_position,terraY_position,kefkaProjectileX,kefkaProjectileY):
    distance = math.sqrt((math.pow(terraX_position-kefkaProjectileX-36,2)) + (math.pow(terraY_position-kefkaProjectileY,2)))
    if distance <=30:
        return True
    else:
        return False

def earthCollision(kefkaProjectileY):
    if kefkaProjectileY >= 900:
        return True
    else:
        return False
#Kefka
def Kefka(kefkaX_position,kefkaY_position):
    screen.blit(kefka,(kefkaX_position,kefkaY_position))

def kefkasProjectile(kefkaProjectielX,kefkaProjectileY):
    global kefkaProjectileState
    kefkaProjectileState = "fire"
    screen.blit(kefkaProjectile,(kefkaProjectileX+230,kefkaProjectileY+130))

#Game Menu
gameWin = False
# Game Loop
running = True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Player keystroke events
        if event.type == pygame.KEYDOWN:
            #Terras projectile
            if event.key == pygame.K_SPACE:
                if weakBlastState is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    weakBlastX = terraX_position
                    terraWeakBlast(weakBlastX, weakBlastY)
            #terras movement
            if event.key == pygame.K_UP:
                terra =pygame.image.load('Terra - Esper - Victory (Front).gif')
                terraY_velocity -= 5
            if event.key == pygame.K_DOWN:
                terra =pygame.image.load('Terra - Esper - Down.gif')
                terraY_velocity += 5
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
            if event.key == pygame.K_UP:
                terraY_velocity =0
            if event.key == pygame.K_DOWN:
                terraY_velocity = 0
    #Kefka's motion
    if kefkaX_position >= 200:
        kefkaX_position += 1
    elif kefkaX_position == 50:
        kefkaX_position+= 1
    elif kefkaX_position == 550:
        kefkaX_position+= -1

    #Kefka Position
    kefkaX_position += kefkaX_Change
    #Kefka boundaries
    if kefkaX_position <=0:
        kefkaX_position = 0
        kefkaX_Change += random.randint(1,5)
    elif kefkaX_position >= 650:
        kefkaX_position = 650
        kefkaX_Change -= random.randint(1,5)

    # Terra position
    terraX_position += terraX_velocity
    terraY_position += terraY_velocity
    #terra boundaries
    if terraX_position <= 0:
        terraX_position = 0
    elif terraX_position >= 875:
        terraX_position = 875
    elif terraY_position >= 900:
        terraY_position = 900
    elif terraY_position <= 0:
        terraY_position = 0

    #Kefka's projectile
    kefkasProjectile(kefkaX_position,kefkaY_position)
    if kefkaProjectileY >= 950:
        kefkaProjectileY = 200
        kefkaProjectileState = 'ready'
    elif kefkaProjectileY >= 1000:
        kefkaProjectileState = 'ready'
    if kefkaProjectileState is "fire":
        kefkasProjectile(kefkaX_position,kefkaProjectileY)
        kefkaProjectileX = kefkaX_position
        kefkaProjectileY += kefkaProjectileYChange

    #Terra's Projectile
    if weakBlastState is "fire":
        terraWeakBlast(terraX_position,terraY_position)
    if weakBlastY <= 0:
        weakBlastState = 'ready'
    if weakBlastState is "fire":
        terraWeakBlast(weakBlastX,weakBlastY)
        weakBlastY -= weakBlastY_change

    # collision
    # terra collision
    terraSmack = terraCollision(terraX_position, terraY_position, kefkaProjectileX, kefkaProjectileY)
    if terraSmack:
        terra = pygame.image.load('Terra - Esper - Shocked.gif')
        terraHP -= 1

    #kefka collision
    weakCollision = weakBlastCollision(kefkaX_position+120, kefkaY_position, weakBlastX, weakBlastY)
    if weakCollision:
        weakExplosion(weakBlastX, weakBlastY)
        weakBlastY = terraY_position
        weakBlastState = "ready"
        kefka_hp -= 10
        bulletSound = mixer.Sound("435415__v-ktor__explosion10.wav")
        bulletSound.set_volume(.25)
        bulletSound.play()

    earthCollide = earthCollision(kefkaProjectileY)
    if earthCollide:
        population -= random.randint(0, 10)

    #Player/Opponent sprites positional updating
    Terra(terraX_position,terraY_position)
    Kefka(kefkaX_position,kefkaY_position)

    #player stats updating
    showPopulation(population)
    showTerraHP(terraHP)
    if kefka_hp < 0:
        gameWon(population)
    if population < 0 or terraHP < 0:
        gameOver()
    gameTips()
    pygame.display.update()