import pygame #On importe pygames
import sys #On importe sys
from pygame.locals import *


mainClock = pygame.time.Clock() # on défini l'objet mainClock
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Maze runner') # on donne un nom à la fenetre



font = pygame.font.SysFont(None, 20) # on défini l'objet font



click = False # on fait en sorte que le click ai une valeur négative
longueur = 775 # on défini la largeur de la fenetre
largeur = 600 # on défini la largeur de la fenetre
screen = pygame.display.set_mode((longueur, largeur),0,32) #on défini la fenetre



titre = pygame.image.load("textures/textures_menu/titre.png").convert_alpha()

jouer = pygame.image.load("textures/textures_menu/jouer.png").convert_alpha()
quit = pygame.image.load("textures/textures_menu/quitter.png").convert_alpha()
retour = pygame.image.load("textures/textures_menu/retour.png").convert_alpha()
option = pygame.image.load("textures/textures_menu/options.png").convert_alpha()
resolutions = pygame.image.load("textures/textures_menu/resolution.png").convert_alpha()
son_off = pygame.image.load("textures/textures_menu/son_off.png").convert_alpha()
éditeur = pygame.image.load("textures/textures_menu/editeur.png").convert_alpha()
tuto = pygame.image.load("textures/textures_menu/tutoriel.png").convert_alpha()
resolution_1 = pygame.image.load("textures/textures_menu/resolution_1.png").convert_alpha()
resolution_2 = pygame.image.load("textures/textures_menu/resolution_2.png").convert_alpha()
resolution_3 = pygame.image.load("textures/textures_menu/resolution_3.png").convert_alpha()


jouer_bleu = pygame.image.load("textures/textures_menu/jouer_bleu.png").convert_alpha()
quit_bleu = pygame.image.load("textures/textures_menu/quitter_bleu.png").convert_alpha()
retour_bleu = pygame.image.load("textures/textures_menu/retour_bleu.png").convert_alpha()
option_bleu = pygame.image.load("textures/textures_menu/options_bleu.png").convert_alpha()
resolutions_bleu = pygame.image.load("textures/textures_menu/resolution_bleu.png").convert_alpha()
son_off_bleu = pygame.image.load("textures/textures_menu/son_off_bleu.png").convert_alpha()
éditeur_bleu = pygame.image.load("textures/textures_menu/editeur_bleu.png").convert_alpha()
tuto_bleu = pygame.image.load("textures/textures_menu/tutoriel_bleu.png").convert_alpha()
son_bleu = pygame.image.load("textures/textures_menu/son_bleu.png").convert_alpha()
resolution_1_bleu = pygame.image.load("textures/textures_menu/resolution_1_bleu.png").convert_alpha()
resolution_2_bleu = pygame.image.load("textures/textures_menu/resolution_2_bleu.png").convert_alpha()
resolution_3_bleu = pygame.image.load("textures/textures_menu/resolution_3_bleu.png").convert_alpha()





def main_menu():

    while True:



            screen.fill((0,0,0)) # On défini le cadre

            fond = pygame.image.load("fond.png").convert()# on défini le background
            screen.blit(fond, (0,0)) # on pose le background

            onglet_long = 200 #----
            onglet_larg = 50  # on défini la taille des bouton

            pos_long = (longueur/2)-(onglet_long/2) #---
            pos_larg = (largeur/2) # on défini la position des bouton

            screen.blit(titre ,((longueur/2)-244,pos_larg - 225))




            mx, my = pygame.mouse.get_pos() # on défini les coordonnées des curseurs

            bouton_1 = pygame.Rect(pos_long , pos_larg - 110, onglet_long, onglet_larg)
            bouton_2 = pygame.Rect(pos_long , pos_larg , onglet_long, onglet_larg)
            bouton_3 = pygame.Rect(pos_long , pos_larg + 110, onglet_long, onglet_larg)


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
                    selection_niveaux() # on défini l'affectation du bouton selections niveaux
            if bouton_2.collidepoint((mx, my)):
                if click:
                    options()
            if bouton_3.collidepoint((mx, my)):
                if click:
                    quitter() # on défini l'affection du bouton éditeur


            if bouton_1.collidepoint((mx, my)):
                screen.blit(jouer_bleu, (pos_long, pos_larg - 110))
            else:
                screen.blit(jouer, (pos_long, pos_larg - 110))

            if bouton_2.collidepoint((mx, my)):
                screen.blit(option_bleu, (pos_long, pos_larg))
            else:
                screen.blit(option, (pos_long, pos_larg))

            if bouton_3.collidepoint((mx, my)):
                screen.blit(quit_bleu, (pos_long, pos_larg + 110))
            else:
                screen.blit(quit, (pos_long, pos_larg + 110))

                                                             # on défini la surbrillance des boutons

            pygame.display.update()
            mainClock.tick(60) # on défini les FPS



def selection_niveaux():

    while True:

            screen.fill((0,0,0)) # On défini le cadre

            fond = pygame.image.load("fond.png").convert()# on défini le background
            screen.blit(fond, (0,0)) # on pose le background

            onglet_long = 200 #----
            onglet_larg = 50  # on défini la taille des bouton

            pos_long = (longueur/2)-(onglet_long/2) #---
            pos_larg = (largeur/2) # on défini la position des boutons


            mx, my = pygame.mouse.get_pos() # on défini les coordonnées des curseurs

            bouton_1 = pygame.Rect(pos_long , pos_larg - 110, onglet_long, onglet_larg)
            bouton_2 = pygame.Rect(pos_long , pos_larg , onglet_long, onglet_larg)
            bouton_3 = pygame.Rect(pos_long , pos_larg + 110, onglet_long, onglet_larg)




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
                    import tutoriel # on défini l'affectation du bouton selections niveaux
            if bouton_2.collidepoint((mx, my)):
                if click:
                    import Main# on défini l'affectation du bouton options
            if bouton_3.collidepoint((mx, my)):
                if click:
                    main_menu() # on défini l'affection du bouton éditeur



            if bouton_1.collidepoint((mx, my)):
                screen.blit(tuto_bleu, (pos_long, pos_larg - 110))
            else:
                screen.blit(tuto, (pos_long, pos_larg - 110))

            if bouton_2.collidepoint((mx, my)):
                screen.blit(éditeur_bleu, (pos_long, pos_larg))
            else:
                screen.blit(éditeur, (pos_long, pos_larg))

            if bouton_3.collidepoint((mx, my)):
                screen.blit(retour_bleu, (pos_long, pos_larg + 110))
            else:
                screen.blit(retour, (pos_long, pos_larg + 110))

                                                             # on défini la surbrillance des boutons

            pygame.display.update()
            mainClock.tick(60) # on défini les FPS

def options():

    while True:

            screen.fill((0,0,0)) # On défini le cadre

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

            fond = pygame.image.load("fond.png").convert() # on défini le background
            screen.blit(fond, (0,0)) # on pose le background

            onglet_long = 200 #----
            onglet_larg = 50  # on défini la taille des bouton

            pos_long = (longueur/2)-(onglet_long/2) #---
            pos_larg = (largeur/2) # on défini la position des bouton


            mx, my = pygame.mouse.get_pos() # on défini les coordonnées des curseurs

            bouton_1 = pygame.Rect(pos_long , pos_larg - 110, onglet_long, onglet_larg)
            bouton_2 = pygame.Rect(pos_long , pos_larg , onglet_long, onglet_larg)
            bouton_3 = pygame.Rect(pos_long , pos_larg + 110, onglet_long, onglet_larg)
            bouton_4 = pygame.Rect(pos_long , pos_larg + 220, onglet_long, onglet_larg)

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
                    resolution() # on défini l'affectation du bouton selections resolution
            if bouton_2.collidepoint((mx, my)):
                if click:
                    import Menu
                    Menu() # on défini l'affectation du bouton son
            if bouton_3.collidepoint((mx, my)):
                if click:
                    main_menu() # on défini l'affectation du bouton retour



            if bouton_1.collidepoint((mx, my)):
                screen.blit(resolutions_bleu, (pos_long, pos_larg - 110))
            else:
                screen.blit(resolutions, (pos_long, pos_larg - 110))

            if bouton_2.collidepoint((mx, my)):
                screen.blit(son_off_bleu, (pos_long, pos_larg))
            else:
                screen.blit(son_off, (pos_long, pos_larg))

            if bouton_3.collidepoint((mx, my)):
                screen.blit(retour_bleu, (pos_long, pos_larg + 110))
            else:
                screen.blit(retour, (pos_long, pos_larg + 110))




                                                             # on défini la surbrillance des boutons

            pygame.display.update()
            mainClock.tick(60) # on défini les FPS

def resolution():



    while True:

            screen.fill((0,0,0)) # On défini le cadre

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

            fond = pygame.image.load("fond.png").convert() # on défini le background
            screen.blit(fond, (0,0)) # on pose le background

            onglet_long = 200 #----
            onglet_larg = 50  # on défini la taille des bouton

            pos_long = (longueur/2)-(onglet_long/2) #---
            pos_larg = (largeur/2) # on défini la position des bouton


            mx, my = pygame.mouse.get_pos() # on défini les coordonnées des curseurs

            bouton_1 = pygame.Rect(pos_long , pos_larg - 110, onglet_long, onglet_larg)
            bouton_2 = pygame.Rect(pos_long , pos_larg , onglet_long, onglet_larg)
            bouton_3 = pygame.Rect(pos_long , pos_larg + 110, onglet_long, onglet_larg)
            bouton_4 = pygame.Rect(pos_long , pos_larg + 220, onglet_long, onglet_larg)

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
                    pass # on défini l'affectation du bouton resolution1
            if bouton_2.collidepoint((mx, my)):
                if click:
                    import Menu_son_res_2
                    Menu_son_res_2() # on défini l'affectation du bouton resolution2
            if bouton_3.collidepoint((mx, my)):
                if click:
                    import Menu_son_res_3
                    Menu_son_res_3() # on défini l'affectation du bouton resolution3
            if bouton_4.collidepoint((mx, my)):
                if click:
                    options() # on défini l'affectation du bouton retour



            if bouton_1.collidepoint((mx, my)):
                screen.blit(resolution_1_bleu, (pos_long, pos_larg - 110))
            else:
                screen.blit(resolution_1, (pos_long, pos_larg - 110))

            if bouton_2.collidepoint((mx, my)):
                screen.blit(resolution_2_bleu, (pos_long, pos_larg))
            else:
                screen.blit(resolution_2, (pos_long, pos_larg))

            if bouton_3.collidepoint((mx, my)):
                screen.blit(resolution_3_bleu, (pos_long, pos_larg + 110))
            else:
                screen.blit(resolution_3, (pos_long, pos_larg + 110))

            if bouton_4.collidepoint((mx, my)):
                screen.blit(retour_bleu, (pos_long, pos_larg + 220))
            else:
                screen.blit(retour, (pos_long, pos_larg + 220))

                                                             # on défini la surbrillance des boutons

            pygame.display.update()
            mainClock.tick(60) # on défini les FPS




def quitter():
    pygame.quit()


main_menu()
