import pygame

pygame.init()
visina_prozora = 650
sirina_prozora = 1000
prozor=pygame.display.set_mode((sirina_prozora, visina_prozora))

CRNA = (0, 0, 0)

slike = [pygame.image.load('il2.png'), pygame.image.load('il3.png'), pygame.image.load('il4.png'), pygame.image.load('il5.png'), pygame.image.load('il6.png'), pygame.image.load('il7.png'), pygame.image.load('il1.png')]


buttons = []
#font dugmadi
font_dugmad = pygame.font.SysFont("courier", 20)

sound = 'hangman.mp3'
pygame.mixer.init()
pygame.mixer.music.load(sound)
pygame.mixer.music.play(-1, 0.0)

#ovom funkcijom iscrtavamo prozor igre
def crtanje_prozora():
    global slike
    ZUTA = (238, 232, 170)
    SVETLOZELENA=(208,240,192)
    prozor.fill(SVETLOZELENA)
    
    #dodavanje dugmadi - odredjivanje oblika(kvadrat), fonta slova na njima, pozicije u prozoru - pozicija mozda nije dobra, gledacemo ponovo
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.rect(prozor, CRNA, (buttons[i][1], buttons[i][2], buttons[i][3], buttons[i][3]),4)
            pygame.draw.rect(prozor, buttons[i][0], (buttons[i][1], buttons[i][2], buttons[i][3], buttons[i][3]))
            label = font_dugmad.render(chr(buttons[i][5]), 1, CRNA)
            prozor.blit(label, (buttons[i][1] + (label.get_width()/1.5), buttons[i][2] + (label.get_height() / 6)))
    
    pygame.display.update()

     
igra = True

while igra:
    crtanje_prozora()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            igra = False    
    

   
pygame.quit()
