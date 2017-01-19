import random
import Players
import pygame
from assets.modules.gui import *
from pygame.locals import *
from EventsHelper import EventExist

# Set fps
FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# Initialise screen
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('INFPRJ02')

def startmenu():
    # Initialize menu buttons
    startButton = Button("START", (width / 2 - 100), (height / 2), 150, 50)
    exitButton = Button("EXIT", (width / 2 + 100), (height / 2), 150, 50)
    optionsButton = Button("OPTIONS", (width * 0.875), (height * 0.1), 100, 33)
    diceButton = Button("THROW ME", (width / width * 100), (height / height * 50), 75, 75)
    optionsButton.action = not optionsButton.action

    # Initialize background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(color_pallete.indigo500)


    # Initialize text to display
    font = pygame.font.Font(None, 72)
    text = font.render('INFPRJ02', 1, color_pallete.grey50)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - (height/4)
    background.blit(text, textpos)

    # Initialize Players
    player1 = Players.Player((0,255,0),400,550,25,25, 'Player 1')

    # Run menu loop
    runStartmenu = True;

    while runStartmenu:
        events = pygame.event.get()
        if EventExist(events, pygame.QUIT) or (exitButton.action):
            pygame.quit()
            exit()

        if (startButton.action):
            startButton.action = not startButton.action
            runStartmenu = False

        # Display background
        screen.blit(background, (0, 0))


        # Menu buttons
        # Update buttons
        startButton.trackMouse()
        exitButton.trackMouse()
        optionsButton.trackMouse()

        # Display buttons
        # startButton.display()
        pygame.draw.rect(screen, startButton.color, (
        startButton.posx - startButton.sizew / 2, startButton.posy - startButton.sizeh / 2, startButton.sizew,
        startButton.sizeh))
        screen.blit(startButton.textSurfaceObj, startButton.textRectObj)

        # exitButton.display()
        pygame.draw.rect(screen, exitButton.color, (
        exitButton.posx - exitButton.sizew / 2, exitButton.posy - exitButton.sizeh / 2, exitButton.sizew,
        exitButton.sizeh))
        screen.blit(exitButton.textSurfaceObj, exitButton.textRectObj)

        # optionsButton.display()
        pygame.draw.rect(screen, optionsButton.color, (
        optionsButton.posx - optionsButton.sizew / 2, optionsButton.posy - optionsButton.sizeh / 2, optionsButton.sizew,
        optionsButton.sizeh))
        screen.blit(optionsButton.textSurfaceObj, optionsButton.textRectObj)

        pygame.display.update()
        fpsClock.tick(FPS)

    # GAME
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(color_pallete.indigo500)

    # MAIN GAME LOOP
    while True:
        events = pygame.event.get()
        if EventExist(events, pygame.QUIT):
            pygame.quit()
            exit()

        # IF YOU PRESS OPTIONS, RUN STARTMENU
        if (optionsButton.action):
            optionsButton.action = not optionsButton.action
            startmenu()

        # Get mouse values
        mouseX, mouseY = pygame.mouse.get_pos()
        mousePressed1, mousePressed2, mousePressed3 = pygame.mouse.get_pressed()

        screen.blit(background, (0, 0))

        # Button update
        optionsButton.trackMouse()

        # optionsButton.display()
        pygame.draw.rect(screen, optionsButton.color, (optionsButton.posx - optionsButton.sizew / 2, optionsButton.posy - optionsButton.sizeh / 2,optionsButton.sizew,optionsButton.sizeh))
        screen.blit(optionsButton.textSurfaceObj, optionsButton.textRectObj)

        # DICE BUTTON
        # Button update
        diceButton.trackMouse()
        pygame.draw.rect(screen, diceButton.color, (diceButton.posx - diceButton.sizew / 2, diceButton.posy - diceButton.sizeh / 2, diceButton.sizew,diceButton.sizeh))
        screen.blit(diceButton.textSurfaceObj, diceButton.textRectObj)

        if diceButton.action:
            pygame.time.wait(100)
            diceNumber = random.randint(1,6)
            diceButton.text = str(diceNumber)
            diceButton.updateText()
            diceButton.action = False
            player1.posy -= player1.sizeh*diceNumber


        # Update Player1
        player1.update()
        ## draw Player1
        pygame.draw.rect(screen, player1.color,(player1.posx - player1.sizew/2,player1.posy - player1.sizeh/2,player1.sizew,player1.sizeh))
        #pygame.draw.rect(screen, player1.color, (200, 200, 100, 100))

        # Display screen, according to framerate
        pygame.display.update()
        fpsClock.tick(FPS)

startmenu()
