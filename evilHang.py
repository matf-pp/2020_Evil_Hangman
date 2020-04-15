import pygame

pygame.init()
visina_prozora = 650
sirina_prozora = 1000
prozor=pygame.display.set_mode((sirina_prozora, visina_prozora))

CRNA = (0, 0, 0)


rec = ''
buttons = [] #dugmad
slike = [pygame.image.load('il2.png'), pygame.image.load('il3.png'), pygame.image.load('il4.png'), pygame.image.load('il5.png'), pygame.image.load('il6.png'), pygame.image.load('il7.png'), pygame.image.load('il1.png')]


delovi = 0

font_dugmad = pygame.font.SysFont("courier", 20)



#ovom funkcijom iscrtavamo prozor igre
def crtanje_prozora():
    global pokusana_slova
    global slike
    global delovi
    ZUTA = (238, 232, 170)
    SVETLOZELENA=(208,240,192)
    prozor.fill(SVETLOZELENA)
    # dugmad
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.rect(prozor, CRNA, (buttons[i][1], buttons[i][2], buttons[i][3], buttons[i][3]),4)
            pygame.draw.rect(prozor, buttons[i][0], (buttons[i][1], buttons[i][2], buttons[i][3], buttons[i][3]))

            label = font_dugmad.render(chr(buttons[i][5]), 1, CRNA)
            prozor.blit(label, (buttons[i][1] + (label.get_width()/1.5), buttons[i][2] + (label.get_height() / 6)))
    pygame.display.update()



# namestanje dugmica
d = round(sirina_prozora / 13) #uvecanje prilikom iscrtavanja kvadratica
ZELENA=(85, 107, 47)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (d * i)
    else:
        x = 25 + (d * (i - 13))
        y = 85
    buttons.append([ZELENA, x, y, 30, True, 97 + i])


     
igra = True

while igra:
    crtanje_prozora()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            igra = False
    

   
pygame.quit()