import pygame
import time
import random
import game.obtain_para as n
import test_image.processor as p
import test_image.create_image_from_cam as c
pygame.init()

white = (240, 248, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
yellow = (255, 215, 0)
orange = (255, 140, 0)
blue = (0, 0, 255)


display_width = 640
display_height = 900

gameDisplay = pygame.display.set_mode((display_width, display_height))
#窗口标题
pygame.display.set_caption('FaceRecognization')
background = pygame.image.load('C:/Users/huang/Desktop/project/image/background.jpg').convert()
clock = pygame.time.Clock()
#暂停标志
pause = False
#文字显示
def text_objects(text, font):
    #将文本生成一个图片
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

#生成按钮
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont('Bauhaus 93', 25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False

#暂停
def paused():

    while pause:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            ##        gameDisplay.fill(white)
        button("Play Again", 85, 700, 150, 80, orange, yellow, game_intro)
        button("Quit", 405, 700, 150, 80, orange, yellow, quitgame)
        pygame.display.update()
        clock.tick(15)

#游戏进入画面
def game_intro():
    c.CatchPICFromVideo("CatchFace", 0, 0, "C:\\Users\\huang\\Desktop\\project\\image\\")
    p.process()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        img = pygame.image.load("C:\\Users\\huang\\Desktop\\project\\image\\background.jpg").convert()
        img_rect = img.get_rect()
        img_rect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(img, img_rect)
        largeText = pygame.font.SysFont('Bauhaus 93', 60)
        TextSurf, TextRect = text_objects('Welcome to our game!', largeText)
        TextRect.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(TextSurf, TextRect)
        button("Start", 85, 560, 150, 80, orange, yellow, game_loop)
        button("Quit", 405, 560, 150, 80, orange, yellow, quitgame)
        pygame.display.update()
        clock.tick(15)



#游戏执行画面
def game_loop():
    global pause
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        img = pygame.image.load("C:\\Users\\huang\\Desktop\\project\\image\\background.jpg").convert()
        img_rect = img.get_rect()
        img_rect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(img, img_rect)
        largeText = pygame.font.SysFont('Bauhaus 93', 70)
        TextSurf, TextRect = text_objects('your emotion is:', largeText)
        TextRect.center = ((display_width / 2), (display_height / 6))
        gameDisplay.blit(TextSurf, TextRect)

        a = n.number()
        if (a == 0):
            img = pygame.image.load("C:\\Users\\huang\\Downloads\\fer2013-master\\emoji\\angry.png")
            img_rect = img.get_rect()
            img_rect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(img, img_rect)
        elif (a == 1):
            img = pygame.image.load("C:\\Users\\huang\\Downloads\\fer2013-master\\emoji\\disgusted.png")
            img_rect = img.get_rect()
            img_rect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(img, img_rect)
        elif (a == 2):
            img = pygame.image.load("C:\\Users\\huang\\Downloads\\fer2013-master\\emoji\\fearful.png")
            img_rect = img.get_rect()
            img_rect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(img, img_rect)
        elif (a == 3):
            img = pygame.image.load("C:\\Users\\huang\\Downloads\\fer2013-master\\emoji\\happy.png")
            img_rect = img.get_rect()
            img_rect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(img, img_rect)
        elif (a == 4):
            img = pygame.image.load("C:\\Users\\huang\\Downloads\\fer2013-master\\emoji\\sad.png")
            img_rect = img.get_rect()
            img_rect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(img, img_rect)
        elif (a == 5):
            img = pygame.image.load("C:\\Users\\huang\\Downloads\\fer2013-master\\emoji\\surprised.png")
            img_rect = img.get_rect()
            img_rect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(img, img_rect)
        else:
            img = pygame.image.load("C:\\Users\\huang\\Downloads\\fer2013-master\\emoji\\neutral.png")
            img_rect = img.get_rect()
            img_rect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(img, img_rect)

        pygame.display.update()
        pause = True
        paused()
        clock.tick(60)

game_intro()