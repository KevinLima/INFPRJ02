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
    
    startButton = Button("START", (width / 2 - 100), (height / 2), 150, 50)
    exitButton = Button("EXIT", (width / 2 + 100), (height / 2), 150, 50)
    optionsButton = Button("OPTIONS", (width * 0.875), (height * 0.1), 100, 33)
    diceButton = Button("THROW ME", (width / width * 100), (height / height * 50), 75, 75)
    nextTurn = Button("NEXT TURN", (width / width * 200), 50, 75, 75)
    directionButton = Button("DIRECTION", (width / width * 300), 50, 75, 75)
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
    player1 = Players.Player((0,255,0),375,550,25,25,"GREEN")
    player2 = Players.Player((0, 0, 255), 400, 550, 25, 25,"BLUE")

    # Initialize whose turn
    turn = 1
    noPlayers = 2 # Number of players

    # Initialize direction
    direction = 1

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
        pygame.draw.rect(screen, diceButton.color, (
        diceButton.posx - diceButton.sizew / 2, diceButton.posy - diceButton.sizeh / 2, diceButton.sizew,
        diceButton.sizeh))
        screen.blit(diceButton.textSurfaceObj, diceButton.textRectObj)

        nextTurn.trackMouse()
        pygame.draw.rect(screen, nextTurn.color, (
        nextTurn.posx - nextTurn.sizew / 2, nextTurn.posy - nextTurn.sizeh / 2, nextTurn.sizew, nextTurn.sizeh))
        screen.blit(nextTurn.textSurfaceObj, nextTurn.textRectObj)

        directionButton.trackMouse()
        pygame.draw.rect(screen, directionButton.color, (
        directionButton.posx - directionButton.sizew / 2, directionButton.posy - directionButton.sizeh / 2,
        directionButton.sizew, directionButton.sizeh))
        screen.blit(directionButton.textSurfaceObj, directionButton.textRectObj)

        if directionButton.action:
            pygame.time.wait(100)
            direction += 1
            direction = direction % 4
            if (direction == 0):
                directionButton.text = "LEFT"
            elif (direction == 1):
                directionButton.text = "UP"
            elif (direction == 2):
                directionButton.text = "RIGHT"
            elif (direction == 3):
                directionButton.text = "DOWN"

            directionButton.updateText()
            directionButton.action = False

        if diceButton.action:
            pygame.time.wait(100)
            diceNumber = random.randint(1, 6)
            diceButton.text = str(diceNumber)
            diceButton.updateText()
            diceButton.action = False

            if (direction == 0):
                if turn == 0:
                    player1.posx -= player1.sizeh * diceNumber
                if turn == 1:
                    player2.posx -= player2.sizeh * diceNumber

            if (direction == 1):
                if turn == 0:
                    player1.posy -= player1.sizeh * diceNumber
                if turn == 1:
                    player2.posy -= player2.sizeh * diceNumber

            if (direction == 2):
                if turn == 0:
                    player1.posx += player1.sizeh * diceNumber
                if turn == 1:
                    player2.posx += player2.sizeh * diceNumber

            if (direction == 3):
                if turn == 0:
                    player1.posy += player1.sizeh * diceNumber
                if turn == 1:
                    player2.posy += player2.sizeh * diceNumber

        if nextTurn.action:
            pygame.time.wait(100)
            turn += 1
            turn = turn % noPlayers
            nextTurn.text = "Player " + str(turn + 1)
            nextTurn.updateText()
            nextTurn.action = False

        # Update Players
        player1.update()
        player2.update()
        ## draw Player1
        pygame.draw.rect(screen, player1.color, (
        player1.posx - player1.sizew / 2, player1.posy - player1.sizeh / 2, player1.sizew, player1.sizeh))
        pygame.draw.rect(screen, player2.color, (
        player2.posx - player2.sizew / 2, player2.posy - player2.sizeh / 2, player2.sizew, player2.sizeh))
        # pygame.draw.rect(screen, player1.color, (200, 200, 100, 100))

        # Display screen, according to framerate
        pygame.display.update()
        fpsClock.tick(FPS)

startmenu()
