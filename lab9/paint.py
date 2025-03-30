import pygame

#Initialize pygame

pygame.init()
FPS = 120
FramePerSec = pygame.time.Clock()
win_x = 900
win_y = 700
win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Paint')

#Class for drawing shapes

class drawing(object):
    def __init__(self):
        self.color = (0, 0, 0)
        self.width = 10
        self.height = 10
        self.rad = 6
        self.shape = 'circle'
    
    #Function to draw the selected shape

    def draw(self, win, pos):
        if self.shape == 'circle':
            pygame.draw.circle(win, self.color, pos, self.rad)
        elif self.shape == 'square':
            pygame.draw.rect(win, self.color, (pos[0] - self.rad, pos[1] - self.rad, 2 * self.rad, 2 * self.rad), )
        elif self.shape == 'right_triangle':
            pygame.draw.polygon(win, self.color, [(pos[0], pos[1]), (pos[0] + 2 * self.rad, pos[1]), (pos[0], pos[1] - 2 * self.rad)])
        elif self.shape == 'equilateral_triangle':
            pygame.draw.polygon(win, self.color, [(pos[0], pos[1] - self.rad), (pos[0] - self.rad, pos[1]+self.rad), (pos[0] + self.rad, pos[1] + self.rad)])
        elif self.shape == 'rhombus':
            pygame.draw.polygon(win, self.color, [(pos[0], pos[1] - self.rad), (pos[0]- self.rad,pos[1]), (pos[0], pos[1] + self.rad), (pos[0] + self.rad, pos[1])])
    
    #Function to handle mouse clicks

    def click(self, win, list, list2):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if pos[1] > 103: 
                self.draw(win, pos)
            for button in list:
                if button.x <= pos[0] <= button.x + button.width and button.y <= pos[1] <= button.y + button.height:
                    self.color = button.color2
            for button in list2:
                if button.x <= pos[0] <= button.x + button.width and button.y <= pos[1] <= button.y + button.height:
                    self.shape = button.action if button.action in ['circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'] else self.shape
                    if button.action == 1:
                        win.fill((255, 255, 255))
                    if button.action == 2 and self.rad > 4:
                        self.rad -= 1
                    if button.action == 3 and self.rad < 20:
                        self.rad += 1

#Button Class

class button(object):
    def __init__(self, x, y, width, height, color, color2, outline=0, action=0, text=''):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.outline = outline
        self.color2 = color2
        self.action = action
        self.text = text
    #To draw button
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.outline)
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, self.color2)
        win.blit(text, (self.x + self.width // 2 - text.get_width() // 2, self.y + self.height // 2 - text.get_height() // 2))
        if self.action == 'circle':
            pygame.draw.circle(win, (0,0,0), (self.x + 20, self.y + 20), 10)
        elif self.action == 'square':
            pygame.draw.rect(win, (0,0,0), (self.x + 10, self.y + 10, 20, 20))
        elif self.action == 'right_triangle':
            pygame.draw.polygon(win, (0,0,0), [(self.x + 10, self.y + 30), (self.x + 30, self.y + 30), (self.x + 10, self.y + 10)])
        elif self.action == 'equilateral_triangle':
            pygame.draw.polygon(win, (0,0,0), [(self.x + 20, self.y + 10), (self.x + 10, self.y + 30), (self.x+30, self.y + 30)])
        elif self.action == 'rhombus':
            pygame.draw.polygon(win, (0, 0, 0), [(self.x + 20, self.y + 10), (self.x + 30, self.y + 20), (self.x + 20, self.y + 30), (self.x + 10, self.y + 20)])

#Function to draw the header

def drawHeader(win):
    pygame.draw.rect(win, (201,201,201), (0, 0, win_x, 50))
    pygame.draw.rect(win, (0, 0, 0), (0, 0,win_x, 50), 2)
    pygame.draw.rect(win, (201,201,201), (2, 50, win_x - 4, 50))
    font = pygame.font.SysFont('comicsans', 30)
    canvasText = font.render('Canvas', 1, (0, 0, 0))
    win.blit(canvasText, (win_x/2 - canvasText.get_width() // 2, 20 - canvasText.get_height() // 2))

#To draw elements

def draw(win):
    player1.click(win, Buttons_color, Buttons_other)
    pygame.draw.rect(win, (0, 0, 0), (810, 55, 86, 40))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, win_x, win_y), 2)
    drawHeader(win)
    for button in Buttons_color + Buttons_other:
        button.draw(win)
    pygame.display.update()

#Main game

def main_loop():
    run = True
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
        draw(win)
    pygame.quit()
#Start program
player1 = drawing()
win.fill((255, 255, 255))
#Color buttons
Buttons_color = [
    button(10, 55, 40, 40, (255, 0, 0), (255, 0, 0)),
    button(60, 55, 40, 40, (0, 0, 255), (0, 0, 255)),
    button(110, 55, 40, 40, (0, 255, 0), (0, 255, 0)),
    button(160, 55, 40, 40, (255, 192, 0), (255, 192, 0)),
    button(210, 55, 40, 40, (255, 255, 0), (255, 255, 0)),
    button(260, 55, 40, 40, (112, 48, 160), (112, 48, 160)),
    button(310, 55, 40, 40, (0, 0, 0), (0, 0, 0)),
    button(360, 55, 40, 40, (255, 255, 255) ,(255, 255, 255)),
]
#Tools buttons
Buttons_other = [
    button(810, 55, 86, 40, (255, 255, 255), (0, 0, 0), 0, 1, 'Clear'),
    button(750, 55, 40, 40, (201, 201, 201), (0, 0, 0), 0, 2, '-'),
    button(700, 55, 40, 40, (201, 201, 201), (0, 0, 0), 0, 3, '+'),
    button(410, 55, 40, 40, (201, 201, 201), (0,0,0), 5, 'circle'),
    button(450, 55, 40, 40, (201, 201, 201), (0,0,0), 5, 'square'),
    button(500, 55, 40, 40, (201, 201, 201), (0,0,0), 5, 'right_triangle'),
    button(550, 55, 40, 40, (201, 201, 201), (0,0,0), 5, 'equilateral_triangle'),
    button(600, 55, 40, 40, (201, 201, 201), (0,0,0), 5, 'rhombus'),

]
#Start also
main_loop()
FramePerSec.tick(FPS)
