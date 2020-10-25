import pygame #On importe pygames
import sys #On importe sys
from pygame.locals import *

mainClock = pygame.time.Clock() # on défini l'objet mainClock

pygame.init()
pygame.display.set_caption('Maze runner') # on donne un nom à la fenetre



font = pygame.font.SysFont(None, 20) # on défini l'objet font



click = False # on fait en sorte que le click ai une valeur négative
longueur = 900 # on défini la largeur de la fenetre
largeur = 700 # on défini la largeur de la fenetre
screen = pygame.display.set_mode((longueur, largeur),0,32) #on défini la fenetre

murInter = pygame.image.load("textures/textures_interface/mur_interface.png").convert_alpha()
persoInter = pygame.image.load("textures/textures_interface/perso_interface.png").convert_alpha()
bleuInter = pygame.image.load("textures/textures_interface/bleu_interface.png").convert_alpha()
pbleuInter = pygame.image.load("textures/textures_interface/pbleu_interface.png").convert_alpha()
rougeInter = pygame.image.load("textures/textures_interface/rouge_interface.png").convert_alpha()
prougeInter = pygame.image.load("textures/textures_interface/prouge_interface.png").convert_alpha()
caisseInter = pygame.image.load("textures/textures_interface/caisse_interface.png").convert_alpha()
pcaisseInter = pygame.image.load("textures/textures_interface/pcaisse_interface.png").convert_alpha()
clefInter = pygame.image.load("textures/textures_interface/clef_interface.png").convert_alpha()
verrouInter = pygame.image.load("textures/textures_interface/verrou_interface.png").convert_alpha()
drapeauInter = pygame.image.load("textures/textures_interface/drapeauR_interface.png").convert_alpha()
trouInter = pygame.image.load("textures/textures_interface/trou_interface.png").convert_alpha()
supprInter = pygame.image.load("textures/textures_interface/suppr_interface.png").convert_alpha()

murInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/mur_interface_mouse.png").convert_alpha()
persoInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/perso_interface_mouse.png").convert_alpha()
bleuInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/bleu_interface_mouse.png").convert_alpha()
pbleuInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/pbleu_interface_mouse.png").convert_alpha()
rougeInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/rouge_interface_mouse.png").convert_alpha()
prougeInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/prouge_interface_mouse.png").convert_alpha()
caisseInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/caisse_interface_mouse.png").convert_alpha()
pcaisseInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/pcaisse_interface_mouse.png").convert_alpha()
clefInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/clef_interface_mouse.png").convert_alpha()
verrouInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/verrou_interface_mouse.png").convert_alpha()
drapeauInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/drapeauR_interface_mouse.png").convert_alpha()
trouInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/trou_interface_mouse.png").convert_alpha()
supprInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/suppr_interface_mouse.png").convert_alpha()

titre_tuto = pygame.image.load("textures/textures_tutoriel/titre_tuto.png").convert_alpha()

def tutoriel():

    while True:

        screen.fill((0,0,0))

        fond_interface = pygame.image.load("textures/textures_interface/fond_interface.png").convert()# on défini le background
        screen.blit(fond_interface, (700,0)) # on pose le background


        screen.blit(titre_tuto ,(710,15))

        boutons_long = 70
        boutons_larg = 70 # on défini la taille des boutons





        mx, my = pygame.mouse.get_pos() # on défini les coordonnées des curseurs

        bouton_1 = pygame.Rect(805 , 85, boutons_long, boutons_larg)
        bouton_2 = pygame.Rect(805 , 170, boutons_long, boutons_larg)
        bouton_3 = pygame.Rect(805 , 255, boutons_long, boutons_larg)
        bouton_4 = pygame.Rect(805 , 340, boutons_long, boutons_larg)
        bouton_5 = pygame.Rect(805 , 425, boutons_long, boutons_larg)
        bouton_6 = pygame.Rect(805 , 510, boutons_long, boutons_larg)
        bouton_7 = pygame.Rect(720 , 85, boutons_long, boutons_larg)
        bouton_8 = pygame.Rect(720 , 170, boutons_long, boutons_larg)
        bouton_9 = pygame.Rect(720 , 255, boutons_long, boutons_larg)
        bouton_10 = pygame.Rect(720 , 340, boutons_long, boutons_larg)
        bouton_11 = pygame.Rect(720 , 425, boutons_long, boutons_larg)
        bouton_12 = pygame.Rect(720 , 510, boutons_long, boutons_larg)
        bouton_13 = pygame.Rect(720 , 585, 160, 70)



        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit() # si on appuie sur la croix rouge on quitte
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu() # si on appuie sur echap on retourne en arrière
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True # si on clique sur clique gauche on donne la valeur vraie au clique




        if bouton_1.collidepoint((mx, my)):
            if click:
                pass

        if bouton_2.collidepoint((mx, my)):
            if click:
                pass

        if bouton_3.collidepoint((mx, my)):
            if click:
                pass

        if bouton_4.collidepoint((mx, my)):
            if click:
                pass

        if bouton_5.collidepoint((mx, my)):
            if click:
                pass

        if bouton_6.collidepoint((mx, my)):
            if click:
                pass

        if bouton_7.collidepoint((mx, my)):
            if click:
                pass

        if bouton_8.collidepoint((mx, my)):
            if click:
                pass

        if bouton_9.collidepoint((mx, my)):
            if click:
                pass

        if bouton_10.collidepoint((mx, my)):
            if click:
                pass

        if bouton_11.collidepoint((mx, my)):
            if click:
                pass

        if bouton_12.collidepoint((mx, my)):
            if click:
                pass

        if bouton_13.collidepoint((mx, my)):
            if click:
                pass


        if bouton_1.collidepoint((mx, my)):
            screen.blit(murInterMouse, (805, 85))
        else:
            screen.blit(murInter, (805, 85))

        if bouton_2.collidepoint((mx, my)):
            screen.blit(persoInterMouse, (805, 170))
        else:
            screen.blit(persoInter, (805, 170))

        if bouton_3.collidepoint((mx, my)):
            screen.blit(bleuInterMouse, (805, 255))
        else:
            screen.blit(bleuInter, (805, 255))

        if bouton_4.collidepoint((mx, my)):
            screen.blit(pbleuInterMouse, (805, 340))
        else:
            screen.blit(pbleuInter, (805, 340))

        if bouton_5.collidepoint((mx, my)):
            screen.blit(rougeInterMouse, (805, 425))
        else:
            screen.blit(rougeInter, (805, 425))

        if bouton_6.collidepoint((mx, my)):
            screen.blit(prougeInterMouse, (805, 510))
        else:
            screen.blit(prougeInter, (805, 510))

        if bouton_7.collidepoint((mx, my)):
            screen.blit(caisseInterMouse, (720, 85))
        else:
            screen.blit(caisseInter, (720, 85))

        if bouton_8.collidepoint((mx, my)):
            screen.blit(pcaisseInterMouse, (720, 170))
        else:
            screen.blit(pcaisseInter, (720, 170))

        if bouton_9.collidepoint((mx, my)):
            screen.blit(clefInterMouse, (720, 255))
        else:
            screen.blit(clefInter, (720, 255))

        if bouton_10.collidepoint((mx, my)):
            screen.blit(verrouInterMouse, (720, 340))
        else:
            screen.blit(verrouInter, (720, 340))

        if bouton_11.collidepoint((mx, my)):
            screen.blit(drapeauInterMouse, (720, 425))
        else:
            screen.blit(drapeauInter, (720, 425))

        if bouton_12.collidepoint((mx, my)):
            screen.blit(trouInterMouse, (720, 510))
        else:
            screen.blit(trouInter, (720, 510))

        if bouton_13.collidepoint((mx, my)):
            screen.blit(supprInterMouse, (720, 595))
        else:
            screen.blit(supprInter, (720, 595))


        pygame.display.update()
        mainClock.tick(60) # on défini les FPS



                                                   # on défini la surbrillance des boutons
tutoriel()