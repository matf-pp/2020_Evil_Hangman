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

pokusana_slova = []
#font ispisa
font_pogodak = pygame.font.SysFont("courier", 24)

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
      
    #dodavanje labele za ispis slova na prozoru
    label1 = font_pogodak.render(ispis(pokusana_slova,rec), 1, CRNA)
    prozor.blit(label1,(200, 450)) #moze da se promeni, videcemo na kraju
    
    pygame.display.update()
    
#definisem funkciju koja ce da ispisuje slova reci na prozoru - crtice su na pocetku jer nije bilo pogodaka
def ispis(rec, pogodak=[]): 
    pog_slova= pogodak
    r_ispis = ''
    for x in range(len(rec)):
        r_ispis += '_ ' #stavicu onoliko crtica koliko imam slova u reci koju pogadjam
        for i in range(len(pog_slova)): 
            if rec[x] == pog_slova[i]: #ako je slovo reci koje se pogadja bas ono koje smo izabrali..
                r_ispis = r_ispis[:-2] # ovo radim da bih izbisala crticu i belinu, i umesto nje dodala slovo
                r_ispis += rec[x].upper() + ' ' # .. ovde zamenim crticu velikim slovom koje smo izabrali (moze i malo, ali deluje mi lepse da je veliko :))

    return r_ispis    



def vrati_duzinu(reci):
    duzine_reci =[]
    for r in reci:
        duz = r.__len__()
        if(duz not in duzine_reci):
            duzine_reci.append(duz) #lista duzina reci
             
    duzine_reci.sort()
    
    duz = duzine_reci[int( random.randint(3,len(duzine_reci)-1))]
    return duz

#postavljanje pocetnih stanja reci - zelimo ovom funkcijom da dobijemo odredjen oblik reci koji koristimo da bismo ostigli da bude evil
def postavi_stanje(duzina_reci):
    stanje = ""
    while duzina_reci > 0:
        stanje += "-"
        duzina_reci = duzina_reci- 1 #ovo su zapravo stanja na pocetku, pa su samo crtice, menjacemo ih slovima kasnije u programu, to je ideja
    return stanje

# vrati listu svih reci sa datom duzinom
def postavi_preostale(lines, duzina):
    words = []
    for r in lines:
        if(r.__len__() == duzina):
            words.append(r)
    return words
    
# namestanje dugmica
d = round(sirina_prozora / 13) #uvecanje prilikom iscrtavanja kvadratica
ZELENA=(85, 107, 47)
for i in range(27):
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
