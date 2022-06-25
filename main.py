import pygame
import sys
from playsound import playsound

from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def onePlayer():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        PLAY_TEXT = get_font(70).render("Controls", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 60))

        PLAY_CONTROLS = get_font(50).render("W - Move Forward \n A - Move Left \n"
                                            "S - Move Down \n"
                                            "D - Move Right", True, "White")
        PLAY_RECT_CONTROLS = PLAY_CONTROLS.get_rect(center=(640, 130))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(PLAY_CONTROLS, PLAY_RECT_CONTROLS)
        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def twoPlayer():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Controls.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def threePlayer():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("Tank Cooperative", True, "#118fff")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 215),
                             text_input="1 Player", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        TWO_PLAYER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 355),
                                   text_input="2 Player", font=get_font(60), base_color="#d7fcd4",
                                   hovering_color="White")
        THREE_PLAYER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 505),
                                     text_input="3 Player", font=get_font(60), base_color="#d7fcd4",
                                     hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 645),
                             text_input="Exit", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, TWO_PLAYER_BUTTON, THREE_PLAYER_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):

                    onePlayer()
                if TWO_PLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):

                    twoPlayer()
                if THREE_PLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):

                    threePlayer()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
