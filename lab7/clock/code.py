import pygame, time, sys
pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
back = pygame.image.load("C:\\Users\\Daniyar\\Desktop\\PP2 2025\\lab7\\clock.png")
seconds = pygame.image.load("C:\\Users\\Daniyar\\Desktop\\PP2 2025\\lab7\\sec_hand.png")
minutes = pygame.image.load("C:\\Users\\Daniyar\\Desktop\\PP2 2025\\lab7\\min_hand.png")

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.blit(back, (0,0))

    now = time.localtime()

    minute_angle = 360 - (now.tm_min * 6)
    min_rotate = pygame.transform.rotate(minutes, minute_angle)
    min_pos = ((size[0] - min_rotate.get_width())/2, (size[1] - min_rotate.get_width())/2)
    screen.blit(min_rotate, min_pos)

    second_angle = 360 - (now.tm_sec * 6)
    sec_rotate = pygame.transform.rotate(seconds, second_angle)
    sec_pos = ((size[0] - sec_rotate.get_width())/2, (size[1] - sec_rotate.get_width())/2)
    screen.blit(sec_rotate, sec_pos)

    pygame.display.flip()

pygame.quit()
sys.exit()
