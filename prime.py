import pygame,sys,os,math,time,random
pygame.init()
displayW = 451
displayH = 451

gameDisplay = pygame.display.set_mode((displayW,displayH))
clock = pygame.time.Clock()
RED = (255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
CYAN = (4,219,213)
MAGENTA = (255,0,255)
CAPTION = "PRIME SPIRAL"

primes= []
def is_prime(number: int) -> bool:
    """Checks if a number is prime or not"""
    # number must be integer
    if type(number) != int:
        raise TypeError("Non-integers cannot be tested for primality.")
    # negatives aren't prime, 0 and 1 aren't prime either
    if number <= 1:
        return False
    # 2 and 3 are prime
    elif number <= 3:
        return True
    # multiples of 2 and 3 aren't prime
    elif number % 2 == 0 or number % 3 == 0:
        return False
    # only need to check if divisible by potential prime numbers
    # all prime numbers are of form 6k +/- 1
    # only need to check up to square root of number
    for i in range(5, int(number**0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True

middleX = int((displayW-1)/2)+1
middleY = int((displayH-1)/2)+1
absCord = [middleX,middleY]
d = [0,0]
step = 0
pixelS = []
class PrimePixel(object):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self,rect):
        rect.set_at((self.x,self.y),self.color)
    def update(self,rect):
        self.draw(rect)
class Game(object):
    def __init__(self,displayW,displayH):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.dw = displayW
        self.dh = displayH
        self.objects = pygame.sprite.Group()
        self.Main()
    def text_objects(self,text,font):
        textSurface = font.render(text,True,WHITE)
        return textSurface,textSurface.get_rect()
    def text_display(self,text,x,y):
        normalText = pygame.font.Font("font.ttf",10)
        TextSurf , TextRect = self.text_objects(text,normalText)
        TextRect.center = (x,y)
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
    def update(self):
        self.objects.update(self.screen_rect)
    def spiralStep(self,stepS):
        global d,absCord
        turn = 0
        stepN = 0
        for i in range(0,stepS):
            #print(absCord,"  ",d)
            if (d[0] >=0 and d[1] >=0) and (d[0] == d[1]):
                #print("another start")
                turn += 1
                absCord[0]+=1
                d[0] +=1
                stepN +=1
                print(stepN)
                if is_prime(stepN):
                    primes.append(stepN)
                    self.drawPixel(absCord,BLUE)
                    pygame.display.update()
                #print(absCord,"  ",d)
                for i in range(0,abs(d[0])+turn):
                    absCord[1]-=1
                    d[1]-=1
                    stepN +=1
                    print(stepN)
                    if is_prime(stepN):
                        primes.append(stepN)
                        self.drawPixel(absCord,BLUE)
                        pygame.display.update()
                    #print(absCord,"  ",d)
            for i in range(0,abs(d[0])+turn):
                absCord[0]-=1
                d[0]-=1
                stepN +=1
                print(stepN)
                if is_prime(stepN):
                    primes.append(stepN)
                    self.drawPixel(absCord,BLUE)
                    pygame.display.update()
                #print(absCord,"  ",d)
            for i in range(0,abs(d[1])+turn):
                absCord[1]+=1
                d[1]+=1
                #print(absCord,"  ",d)
                stepN +=1
                if is_prime(stepN):
                    primes.append(stepN)
                    self.drawPixel(absCord,BLUE)
                    pygame.display.update()
            for i in range(0,abs(d[0])+turn):
                absCord[0]+=1
                d[0]+=1
                #print(absCord,"  ",d)
                stepN +=1
                print(stepN)
                if is_prime(stepN):
                    primes.append(stepN)
                    self.drawPixel(absCord,BLUE)
                    pygame.display.update()
        #print(primes)
        self.drawPixel((middleX,middleY),RED)

    def drawPixel(self,cord,color):
        pixelS.append(PrimePixel(cord[0],cord[1],color))
        pixelS[-1].draw(gameDisplay)
    def Main(self):
        global middleX,middleY,dX,dY,pixelS
        error = False
        gameDisplay.fill(WHITE)
        while not error:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.spiralStep(225)
            self.update()
            self.objects.draw(self.screen)
            caption = "{} - FPS :{:.2f}".format(CAPTION,clock.get_fps())
            pygame.display.set_caption(caption)
            pygame.display.update()
            clock.tick(60)
if __name__ == '__main__':
    Game(displayH,displayW)