#On initialise la librairie pygame
import pygame #On importe pygames
import sys #On importe sys
pygame.init() #On initialise pygame
mainClock = pygame.time.Clock() # on défini l'objet mainClock
from pygame.locals import * #faire les imports locaux de pygame


#On initialise l'application
longueur = 900 #mettre longueur a 900
largeur = 700 #mettre largeur a 700
Ecran = pygame.display.set_mode((longueur,largeur)) #on définit l'écran au nom "Ecran" sur une dimension x=700 et y=700
pygame.display.set_caption("Labyrinthe") #On définit le nom de l'application à Labyrinthe



#On définit les variables primordiales
slotj = sback = slotj2 = visible = caractere = lit = 0 #On initialise slotj sback slotj2 visible caractere lit à 0
mode_quadrillage = mode_changement = mode_joueur2 = False #on met mode_k a 0 (gestion de la touche)



#Liseur du fichier texte-
# On crée une liste pour composer le niveau 0=Mur de base 1=rien 2=Mur du joueur 3=Caisse 4=Drapeau rouge 5=Clef 6=block-clef 7=Trou 8= Plaque caisse 9 = plaque-blue a = plaque-rouge b = block blue c = block rouge
a = "a" #mettre a à "a"
b = "b" #mettre b à "b"
c = "c" #mettre c à "c"
d = "d" #mettre d à "d"
e = "e" #mettre e à "e"
#déclarer la liste de base du niveau de base
liste = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


fichier = open('sauvegarde/level.txt', 'r') #ouvre le fichier level et prend la sauvegarde
player = open('sauvegarde/joueur.txt', 'r') #ouvre le fichier joueur et prend le player
brouillard_save = open('sauvegarde/brouillard.txt', 'r') #ouvre le fichier brouillard et prend le brouillard_save

while caractere < 401 : #tant que caractère est inférieur à 401
    txt = fichier.read(1) #lit le premier caractère du fichier texte
    #pour ce qui va suivre on va lire le caractère et on va le mettre dans la liste a l'emplacement lit

    if txt == "a" : liste[lit] = a

    elif txt == "b" : liste[lit] = b

    elif txt == "c" : liste[lit] = c

    elif txt == "0" : liste[lit] = 0

    elif txt == "1" : liste[lit] = 1

    elif txt == "2" : liste[lit] = 2

    elif txt == "3" : liste[lit] = 3

    elif txt == "4" : liste[lit] = 4

    elif txt == "5" : liste[lit] = 5

    elif txt == "6" : liste[lit] = 6

    elif txt == "7" : liste[lit] = 7

    elif txt == "8" : liste[lit] = 8

    elif txt == "9" : liste[lit] = 9


    lit += 1 #Ajoute à lit 1
    caractere += 1 #ajoute a caractère 1


txt = player.read(3) #lit les trois premier caractère de player
slots = sback = slotj = int(txt) #on met slots sback et slotj a la valeur entière de txt

brouillard_etat = brouillard_save.read(1) #lit le premier caractère de brouillard save
brouillard = int(brouillard_etat)


fichier.close() #ferme le fichier
player.close() #ferme le player
brouillard_save.close() #ferme le brouillard_save



txtliste = liste[:] #créer une liste txtliste sur la liste
# On crée une liste pour faire le noir 0 = noir 1 = Eclaire
noir = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# On crée une liste spécialement pour y mettre les drapeaux bleux et trous remplie 0= Rien 1= drapeau bleux 2= Troue-remplie
autre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#On crée une liste pour y mettre les plaque 1=plaque-caisse 2=plaque-bleu 3=plaque-rouge 4=block bleu 5 = block rouge 6=block bleu
gplaque = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



#On initialise nos image
fond = pygame.image.load('textures/fond.png').convert_alpha()
joueur = pygame.image.load('textures/perso.png').convert_alpha()
joueur2 = pygame.image.load('textures/perso2.png').convert_alpha()
mur = pygame.image.load('textures/mur.png').convert_alpha()
mur2 = pygame.image.load('textures/mur2.png').convert_alpha()
brume = pygame.image.load('textures/noir.png').convert_alpha()
curseur = pygame.image.load('textures/selec.png').convert_alpha()
caisse = pygame.image.load('textures/caisse.png').convert_alpha()
drapeau = pygame.image.load('textures/drapeau.png').convert_alpha()
drapeau2 = pygame.image.load('textures/drapeau2.png').convert_alpha()
clef = pygame.image.load('textures/clef.png').convert_alpha()
verrou = pygame.image.load('textures/verrou.png').convert_alpha()
trou = pygame.image.load('textures/trou.png').convert_alpha()
remplie = pygame.image.load('textures/remplie.png').convert_alpha()
pcaisse = pygame.image.load('textures/pcaisse.png').convert_alpha()
pquadrillage = pygame.image.load('textures/quadrillage.png').convert_alpha()
millieu = pygame.image.load('textures/millieu.png').convert_alpha()
prouge = pygame.image.load('textures/prouge.png').convert_alpha()
pbleu = pygame.image.load('textures/pbleu.png').convert_alpha()
brouge = pygame.image.load('textures/rouge.png').convert_alpha()
bbleu = pygame.image.load('textures/bleu.png').convert_alpha()
fond_interface = pygame.image.load("textures/textures_interface/fond_interface.png").convert()
Ecran.blit(fond_interface, (700,0)) # on pose le background
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
facile = pygame.image.load("textures/textures_interface/facile.png").convert_alpha()
moyen = pygame.image.load("textures/textures_interface/moyen.png").convert_alpha()
difficile = pygame.image.load("textures/textures_interface/difficile.png").convert_alpha()
void = pygame.image.load("textures/textures_interface/void.png").convert_alpha()
interface_drapeau = pygame.image.load('textures/interface_drapeau.png').convert_alpha()
interface_caisse = pygame.image.load('textures/interface_caisse.png').convert_alpha()


supprInter = pygame.image.load("textures/textures_interface/suppr_interface.png").convert_alpha()
supprInter2 = pygame.image.load("textures/textures_interface/suppr_interface2.png").convert_alpha()
supprInterMouse = pygame.image.load("textures/textures_interface/textures_interface_mouse/suppr_interface_mouse.png").convert_alpha()




boutons_long = 70
boutons_larg = 70 # on défini la taille des boutons
#créer des variables boutons et les attribuer à des donnés boutons
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

font = pygame.font.SysFont(None, 20) # on défini l'objet font





#On initialise nos scores
flag = serrure = bug = pasbouge = passe = dep = clignote = forceMod = fini = score = 0 #met toute ces variable à 0
Mode = rouge = bleu = quadrillage = Visible = 1 #met toute ces variable a 1
time = 590 #On met le score time a 590
if slotj != 0 : slots = slotj # si slotj ne vaut pas 0 Initialise la variable slots a slotj
else : slots = 21 # Sinon initialise slots a 21



def draw_text(text, font, color, surface, x, y): #la fonction draw_text
    textobj = font.render(text, 1, color) #définir textobj par fond.render(text, 1, color)
    textrect = textobj.get_rect() #définir textrect par textobj.get_rect()
    textrect.topleft = (x, y) #définit textrect.topleft par x et y
    surface.blit(textobj, textrect) # on défini la police





#On définit nos fonctions
def pose(): #la fonction pose
    if slots != sback : liste[slots] = passe # #si slots ne vaut pas sback définir dans la liste le nombre slot à passe

def depcrea(slots, dep): #la fonction depcrea
    if liste[slots+dep] != 0 : #si dans la liste slots+dep fait pas 0
        pygame.time.delay(50) #Faire un delay de 50
        slots = slots+dep #définir slots à slots+dep
    return slots #renvoie slots



# On crée une boucle infini
fin = False #On définit la variable fin a faux
while not fin: #Tant que fin n'est pas vraie
    mainClock.tick(30)





    #Configuration des controles avec le pc
    click = 0
    mx, my = pygame.mouse.get_pos()  # on défini les coordonnées des curseurs
    for event in pygame.event.get(): #Pour les évenement obtenue
        if event.type == pygame.QUIT: #Si on obtient l'évenement quitter
            fin = True #On quitte l'application
        if event.type == KEYDOWN: #si l'event est de type clavier
            if event.key == K_F1: #si F1 est pressier
                import Menu # on retourne en arrière
        if event.type == MOUSEBUTTONDOWN: #si l'event est de type clavier
            if event.button == 1: #si c'est un bouton
                click = 1 # si on clique sur clique gauche on donne la valeur 1 au click




    #Touches
    keys = pygame.key.get_pressed() #On obtient la touche pressé

    #Changement de mode construction à joueur
    if keys[pygame.K_ESCAPE] or forceMod == 1 : #Si le joueur touche echap en azerty

        mode_changement = not mode_changement #inverer le changement de mode
        pygame.time.delay(20) #Faire un delay de 20
        if mode_changement == True : #si le changement de mode est vraie

            Ecran.blit(fond_interface, (700,0)) # on pose le background
            if Mode == 1 : #Si Mode vaut 1
                if slotj != 0 : #si slotjne vaut pas 0
                    backup = liste[:] #définit backup par la liste
                    pygame.mixer.music.stop() #On stoppe toute les musiques
                    time = 590 #On met le temps a 690
                    Visible = serrure = Mode = 0 #Met la variable visible et serrure et mode a 0
                    noir = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            else : #sinon
                liste = backup[:] #définit la liste a backup
                Mode = 1 # Mode vaut 1
                pygame.mixer.music.stop() #On stoppe toute les musiques
                time = 590 #On met le temps a 590
                slots = 21 #Initialise la variable slots a la première case
                slotj = sback #slotj vaut sback
                slotj2 = serrure = 0 #met slotj2 et serrure a 0
                #remplis de 0 la liste autre
                autre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                forceMod = 0 #mettre forceMod à 0

    if keys != (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) :

        #Le mode joueur
        if Mode == 0 : #Si le mode de jeu vaut 0
        #Déplacement du joueur 1
            if gplaque[slotj2] != 4 and pasbouge != 1 : #si gplaque au slotj2 ne vaut pas 4 et pasbouge ne vaut pas 1

                if keys[pygame.K_a]: dep = -1 #Si le joueur touche q en azerty Met dep a - 1
                if keys[pygame.K_d]: dep = 1 #Si le joueur touche d en azerty Met dep a 1
                if keys[pygame.K_w]: dep = -20 #Si le joueur touche z en azerty Met dep a -20
                if keys[pygame.K_s]: dep = 20 #Si le joueur touche s en azerty Met dep a 20

                if dep != 0 : #si dep ne vaut pas 0
                    pygame.time.delay(50) #Faire un delay de 50
                    if liste[slotj+dep] == 1 or liste[slotj+dep] == 8 : slotj += dep #si dans la liste slotj+dep fait 1 ou si slotj+dep fait 8 définir slotj à slotj-dep
                    elif liste[slotj+dep] == 3 : #sinon si dans la liste slotj-dep fait 3
                        if liste[slotj+(dep*2)] == 7 : #si dans la liste slotj-2 fait 7
                            liste[slotj+dep] = liste[slotj+(dep*2)] = 1 #mettre dans liste slotj+dep et slotj+2dep à 1
                            autre[slotj+(dep*2)] = 2 #mettre dans autre slotj+2dep a 2
                            slotj += dep #définir slotj à slotj+dep
                        elif liste[slotj+(dep*2)] == 1 and autre[slotj+(dep*2)] != 1 and slotj+(dep*2) != slotj2: #si dans la liste slotj+dep fait 1 et que dans la liste slotj+2dep ne fait pas 1
                            liste[slotj+dep] = 1 #mettre slotj+dep à 0
                            liste[slotj+(dep*2)] = 3 #mettre slotj+(dep*2) à 3
                            slotj += dep #définir slotj à slotj+dep
                    elif liste[slotj+dep] == 5 : #si dans la liste slotj+dep vaut 5
                        slotj += dep #définir slotj à slotj+dep
                        liste[slotj] = 1 #on définit dans la liste slotj à 1
                        serrure += 1 #On ajoute 1 à serrure
                    elif liste[slotj+dep] == 6 and serrure > 0 : #sinon est si dans la liste slotj+dep vaut 6 et serrure est supérieur à 0
                            slotj += dep #définir slotj à slotj+dep
                            liste[slotj] = 1 #on définit dans la liste slotj à 1
                            serrure -= 1 #on enleve 1 a serrure
                    dep = 0 #mettre dep à 0



            #Joueur 2
            if Visible == 1 : #Si visible vaut 1

                #Déplacement joueur 2
                if gplaque[slotj] != 5  and pasbouge !=2: #si dans gplaque slotj ne vaut pas 5

                    if keys[pygame.K_j]: dep = -1 #Si le joueur touche j en azerty met dep a -1

                    if keys[pygame.K_l]: dep = 1 #Si le joueur touche l en azerty met dep a 1

                    if keys[pygame.K_i]: dep = -20 #Si le joueur touche i en azerty met dep a -20

                    if keys[pygame.K_k]: dep = 20 #Si le joueur touche k en azerty met dep a 20

                    if dep != 0 : #si dep ne vaut pas 0
                        pygame.time.delay(50) #Faire un delay de 50
                        if liste[slotj2+dep] == 1 or liste[slotj2+dep] == 8 : slotj2 += dep #si dans la liste slotj2+dep fait 1 ou si slotj2+dep fait 8 définir slotj2 à slotj2+dep
                        elif liste[slotj2+dep] == 3 : #sinon si dans la liste slotj2+dep fait 3
                            if liste[slotj2+(dep*2)] == 7 : #si dans la liste slotj2 fait 7
                                liste[slotj2+dep] = liste[slotj2+(dep*2)] = 1 #mettre dans liste slotj2+dep et slotj2+2dep à 1
                                autre[slotj2+(dep*2)] = 2 #mettre dans autre slotj2+2dep a 2
                                slotj2 += dep #définir slotj2 à slotj2+dep
                            elif liste[slotj2+(dep*2)] == 1 and autre[slotj2+(dep*2)] != 1 and slotj2+(dep*2) != slotj : #si dans la liste slotj2+dep fait 1 et que dans la liste slotj2+2dep ne fait pas 1
                                liste[slotj2+dep] = 1 #mettre slotj2+dep à 0
                                liste[slotj2+(dep*2)] = 3 #mettre slotj2+(dep*2) à 3
                                slotj2 += dep #définir slotj2 à slotj2+dep
                        elif liste[slotj2+dep] == 5 : #si dans la liste slotj2+dep vaut 5
                            slotj2 += dep #définir slotj2 à slotj2+dep
                            liste[slotj2] = 1 #on définit dans la liste slotj2 à 1
                            serrure += 1 #On ajoute 1 à serrure
                        elif liste[slotj2+dep] == 6 and serrure > 0 : #sinon est si dans la liste slotj2+dep vaut 6 et serrure est supérieur à 0
                                slotj2 += dep #définir slotj2 à slotj2+dep
                                liste[slotj2] = 1 #on définit dans la liste slotj2 à 1
                                serrure -= 1 #on enleve 1 a serrure
                        dep = 0 #mettre dep à 0



            #Apparition joueur 2
            if keys[pygame.K_RETURN]: #Si le joueur touche La touche entrée en azerty
                mode_joueur2 = not mode_joueur2 #inverer le changement de mode
                pygame.time.delay(20) #Faire un delay de 20
                if mode_joueur2 == True : #si le changement de mode est vraie
                    if gplaque[slotj] != 5 : #si dans gplaque slotj ne vaut pas 5
                        pygame.time.delay(200) #Crée un delay de 100 tick
                        Visible = (Visible+3)%2 ##Calcul permettant si visible vaut 0 de la passer à 1 et si visible vaut 1 de le passer à 0
                        slotj2 = slotj #slotj2 vaut slotj



            #brume
            #on enleve de la brume comme suivant : liste noir  en (cordonné souhaite + 1) = 1 si brouillard vaut 1
            if brouillard == 1 :
                noir[slotj] = noir[slotj+20] = noir[slotj-20] = noir[slotj-1] = noir[slotj+1] = noir[slotj+21] = noir[slotj-21] =  noir[slotj+19] = noir[slotj-19] =1
                if Visible == 1 : noir[slotj2] = noir[slotj2+20] = noir[slotj2-20] = noir[slotj2-1] = noir[slotj2+1] = noir[slotj2+21] = noir[slotj2-21] =  noir[slotj2+19] = noir[slotj2-19] =1 #Si visible vaut 1 (joueur 2 existant)

            #changement de couleur du drapeau si dans la liste slotj+valeur vaut 4 alors on met dans la liste sloj+1 et autre slotj+1 à 1
            if liste[slotj+1] == 4 : liste[slotj+1] = autre[slotj+1] = 1
            if liste[slotj-1] == 4 : liste[slotj-1] = autre[slotj-1] = 1
            if liste[slotj+20] == 4 : liste[slotj+20] = autre[slotj+20] = 1
            if liste[slotj-20] == 4 : liste[slotj-20] = autre[slotj-20] =1
            if liste[slotj2+1] == 4 : liste[slotj2+1] = autre[slotj2+1] = 1
            if liste[slotj2-1] == 4 : liste[slotj2-1] = autre[slotj2-1] =1
            if liste[slotj2+20] == 4 : liste[slotj2+20] = autre[slotj2+20] = 1
            if liste[slotj2-20] == 4 : liste[slotj2-20] = autre[slotj2-20] = 1



            #systeme de plaque rouge et bleue
            if gplaque[slotj] == 2 : bleu = 0  #si dans gplaque slotj vaut 2 alors bleu vaut 0
            else : bleu = 1 #sinon bleu vaudra 1

            if gplaque[slotj2] == 3 : rouge = 0 #si dans gplaque slotj2 vaut 3 alors rouge vaut 0
            else : rouge = 1 #sinon rouge vaudra 1


            #déterminer a qui est la faute du bug
            pasbouge = 0 #mettre pas bouge à 0
            if bug > 0 and bleu == 0 : pasbouge = 1 #si bug est supérieur à 0 et bleu vaut 1 mettre pas bouge à 1
            elif bug > 0 and rouge == 0 : pasbouge = 2 #si bug est supérieur à 0 et bleu vaut 2 mettre pas bouge à 2



        #Pour le mode création
        if Mode == 1 : #Si le mode de jeu vaut 1

            #Apparition quadrillage
            if event.type == pygame.KEYDOWN and event.key == K_LALT : #Si le joueur touche La touche alt gr en azerty
                pygame.time.delay(20) #Faire un delay de 20
                mode_quadrillage = not mode_quadrillage
                if mode_quadrillage == True : quadrillage = (quadrillage+3)%2 #Calcul permettant si quadrillage vaut 0 de la passer à 1 et si quadrillage vaut 1 de le passer à 0


            #Déplacement
            if keys[pygame.K_a]: dep = -1 #Si le joueur touche q en azerty alors dep vaut -1

            elif keys[pygame.K_d]: dep = 1 #Si le joueur touche d en azerty alors dep vaut 1

            elif keys[pygame.K_w]: dep = -20 #Si le joueur touche z en azerty alors dep vaut -20

            elif keys[pygame.K_s]: dep = 20 #Si le joueur touche s en azerty alors dep vaut 20

            if dep != 0 : #si dep ne vaut pas 0
                slots = depcrea(slots, dep) #définir slots par la fonction depcrea prenant les paramètres slots et dep
                dep = 0 #mettre dep à 0



            #Construction
            if keys[pygame.K_RETURN] :
                if passe != 0 and passe != d and passe != e: #si passe ne vaut pas 0 ou d ou e
                    pose() #faire la fonction pose
                if  passe == d and liste[slots] != 2 and liste[slots] != 3 and liste[slots] != 4 and liste[slots] != 5 and liste[slots] != 6 and liste[slots] != 7 and liste[slots] != 8  and liste[slots] != 9  and liste[slots] != a  and liste[slots] != b  and liste[slots] != c: slotj = sback = slots #si dans la liste slots ne vaut pas ... slotj vaut sback qui vaut slots
            if keys[pygame.K_SPACE] : #si la touche espace est presser
                liste[slots] = 1 #Définir dans la liste le nombre slot à 1
                gplaque[slots] = 0 #Définir dans gplaque nombre slot à 0
                if slots == sback : slotj = sback = 0 #si slots vaut sback alors slotj et sback valent 0







    #Système de lecture de case (Graphisme principalement mais aussi des fonctionnalités)

    #Initialisation de la lecture
    Ecran.blit(fond,(35,35)) #On place sur l'Ecran l'image fond en x=35 et y=35

    slot = qd = zs = qcaisse = bug = 0 #On définit la variable slot à 0



    while slot < 400 : # Tant que slot est inférieur à 400






        if liste[slot] == 0 : #si dans la liste slot vaut 0
            Ecran.blit(mur, (qd, zs)) #Si le slot dans la liste vaut 0 alors On place sur l'Ecran l'image mur défini au début en qd et en zs


        elif liste[slot] == 2 : #si dans la liste slot vaut 2
            Ecran.blit(mur2, (qd, zs)) #Si le slot dans la liste vaut 2 alors On place sur l'Ecran l'image mur2 défini au début en qd et en zs
            score = score + 1 #ajouter 1 à score

        elif liste[slot] == 4 : #Si le slot dans la liste vaut 4 alors
            Ecran.blit(drapeau, (qd, zs)) #On place sur l'Ecran l'image drapeau défini au début en qd et en zs
            flag += 1 #ajoute 1 au score drapeau
            score = score + 1 #ajouter 1 à score

        elif liste[slot] == 5 : #si le slot dans la liste vaut 5
            Ecran.blit(clef, (qd, zs)) #Si le slot dans la liste vaut 5 alors On place sur l'Ecran l'image clef défini au début en qd et en zs
            score = score + 1 #ajouter 1 à score

        elif liste[slot] == 6 : #si dans la liste slot vaut 6
            Ecran.blit(verrou, (qd, zs)) #Si le slot dans la liste vaut 6 alors On place sur l'Ecran l'image verrou défini au début en qd et en zs
            score = score + 1 #ajouter 1 à score

        elif liste[slot] == 7 : #si dans la liste slot vaut 7
            Ecran.blit(trou, (qd, zs)) #Si le slot dans la liste vaut 7 alors On place sur l'Ecran l'image trou défini au début en qd et en zs
            score = score + 1 #ajouter 1 à score

        elif liste[slot] == 8 : #si dans la liste slot vaut 8
            if Mode == 0 : gplaque[slot] = liste[slot] = 1 #si le mode vaut 0 mettre le slot de gplaque et de liste[slot] à 1
            Ecran.blit(pcaisse, (qd, zs)) #On place sur l'Ecran l'image pcaisse défini au début en qd et en zs
            qcaisse += 1 #ajotuer 1 à qcaisse
            score = score + 1 #ajouter 1 à score

        elif liste[slot] == 9 : #Si le slot dans la liste vaut 9 alors
            Ecran.blit(pbleu, (qd, zs)) #On place sur l'Ecran l'image pbleu défini au début en qd et en zs
            score = score + 1 #ajouter a score 1
            if Mode == 0 : #si le mode vaut 0
                gplaque[slot] = 2 #le slot gplaque vaut 2
                liste[slot] = 1 #dans la liste slot vaut 1

        elif liste[slot] == a : #Si le slot dans la liste vaut a alors
            Ecran.blit(prouge, (qd, zs)) #On place sur l'Ecran l'image prouge défini au début en qd et en zs
            score = score + 1 #ajouter à score 1
            if Mode == 0 : #si le mode vaut 0
                gplaque[slot] = 3 #dans gplaque slot vaut 3
                liste[slot] = 1 #dans la liste slot vaut 1

        elif liste[slot] == b : #Si le slot dans la liste vaut b alors
            score = score + 1 #ajouter a score 1
            Ecran.blit(bbleu, (qd, zs)) #On place sur l'Ecran l'image bbleu défini au début en qd et en zs
            if Mode == 0 : gplaque[slot] = 4 #si le mode vaut 0 dans gplaque slot vaut 4

        elif liste[slot] == c : #Si le slot dans la liste vaut c alors
            score = score + 1 #ajouter a score 1
            Ecran.blit(brouge, (qd, zs)) #On place sur l'Ecran l'image brouge défini au début en qd et en zs
            if Mode == 0 :  gplaque[slot] = 5 #si le mode vaut 0 dans gplaque slot vaudra 5

        if gplaque[slot] == 1 : #si gplaque dans le slot vaut 1
            score = score + 1 #ajouter a score 1
            Ecran.blit(pcaisse, (qd, zs)) #On place sur l'Ecran l'image pcaisse défini au début en qd et en zs
            qcaisse += 1 #ajoute 1 a qcaisse
            if liste[slot] == 3 : qcaisse -= 1 #si dans la liste slot vaut 3 alors enleve 1 a qcaisse

        elif gplaque[slot] == 2 : #si dans gplaque slot vaut 2
            Ecran.blit(pbleu, (qd, zs)) #si gplaque dans le slot vaut 1 On place sur l'Ecran l'image pcaisse défini au début en qd et en zs
            score = score + 1 #ajoute a score 1

        elif gplaque[slot] == 3 : #si dans gplaque slot vaut 3
            Ecran.blit(prouge, (qd, zs)) #si gplaque dans le slot vaut 1 On place sur l'Ecran l'image pcaisse défini au début en qd et en zs
            score = score + 1 #ajouter 1 a score

        elif gplaque[slot] == 4 :#si gplaque dans le slot vaut 1
            score = score + 1 #ajouter a score 1
            if bleu == 0 : #si bleu vaut 0
                if liste[slot] != 3 : #si dans la liste slot ne vaut pas 3
                    liste[slot] = 1 #mettre dans la liste slot a 1
            else : liste[slot] = b #sinon mettre liste au slot a b

        elif gplaque[slot] == 5 : #si gplaque dans le slot vaut 1
            score = score + 1 #ajouter a score 1
            if rouge == 0 : #si rouge vaut 0
                if liste[slot] != 3 : liste[slot] = 1 #si dans la liste au slot sa vaut pas 3 alors dans liste slot vaut 1
            else : liste[slot] = c #sinon dans la liste slot vaut C

        if autre[slot] == 1 : #si dans autre slot vaut 1
            Ecran.blit(drapeau2, (qd, zs)) #Si le slot dans autre vaut 1 alors On place sur l'Ecran l'image drapeau2 défini au début en qd et en zs
            score = score + 1 #ajouter a score 1

        elif autre[slot] == 2 : #si dans autre slot vaut 2
            Ecran.blit(remplie, (qd, zs)) #Si le slot dans la liste vaut 8 alors On place sur l'Ecran l'image remplie défini au début en qd et en zs
            score = score + 1 #ajouter a score 1

        if liste[slot] == 3 : #Si le slot dans la liste vaut 3 alors
            score = score + 1 #ajouter a score 1
            Ecran.blit(caisse, (qd, zs)) #On place sur l'Ecran l'image caisse défini au début en qd et en zs
            if gplaque[slot] == 4 or gplaque[slot] == 5 : bug += 1 #si dans la liste gplaque au slot vaut 4 ou 5 Ajouter 1 a bug

        if noir[slot] == 0 and Mode == 0 and brouillard == 1: #si noir slot vaut 0 et que mode vaut 0 et que brouillard vaut 1
            Ecran.blit(brume, (qd, zs)) #Si le slot dans noir vaut 0 et que le mode de jeu vaut 0 alors On place sur l'Ecran l'image brume défini au début en qd et en zs

        if Mode == 1 : #si le mode vaut 1
            txtliste[slot] = str(liste[slot]) #mettre dans txtliste au slot par son caractère
            if quadrillage == 0 : #si le quadrillage vaut 0
                Ecran.blit(pquadrillage, (qd, zs)) #On place sur l'Ecran l'image quadrillage défini au début en qd et en zs
                Ecran.blit(millieu, (332, 332)) #On place sur l'Ecran l'image brume défini au début en 332 332

        slot += 1 #On ajoute 1 a la variable slot
        qd += 35 #On ajoute a qd 35
        if qd == 700 : #si qd =700
            qd = 0 #On définit qd à 0
            zs += 35 #On ajoute a zs 35




    if Mode == 0 : #si le mode vaut 0
        Ecran.blit(fond_interface, (700,0)) # on pose le background
        if flag > 0 : #si flag est supérieur à 0
            Ecran.blit(interface_drapeau,(710,10)) #On place sur l'Ecran l'image interface drapeau fond en x=710 et y=10
            fini = 0 #fini vaut 0


        if qcaisse > 0 : #si qcaisse est supérieur à 0
            Ecran.blit(interface_caisse,(710,360)) #On place sur l'Ecran l'image fond en x=710 et y=10
            fini = 0 #fini vaut 0

        qcaisse = flag = 0 #qcaisse vaut flag qui vaut 0

        if fini == 1 : #si fini vaut 1
            forceMod = 1 #mettre forcemod a 1
        fini = 1 #mettre fini a 1




    #Joueur pour ce qui va suivre on va calculer les positions en x, y on définit x par le slot division euclidienne 20*35 on définit y par le slot reste par 20 * 35



    if slotj != 0 and Visible == 1 and Mode == 0 : Ecran.blit(joueur2, ((slotj2%20)*35, (slotj2//20)*35)) #Si slotj ne vaut pas 0 que visible vaut 1 et que Mode vaut 0 On place sur l'Ecran l'image joueur2 défini au début à sa position

    if slotj != 0 : Ecran.blit(joueur, ((slotj%20)*35, (slotj//20)*35)) #si slotj ne vaut pas 0 On place sur l'Ecran l'image joueur défini au début à sa position

    if Mode == 1 : #si le mode de jeu vaut 1
        clignote += 0.5 #ajoute 0.5 a clignote
        if clignote >= 80 : clignote = 0 #si clignote est supérieur à 80 alors clignote vaudra 0
        if clignote >= 20 : Ecran.blit(curseur, ((slots%20)*35, (slots//20)*35)) #si clignote est supérieur a 20 On place sur l'Ecran l'image joueur2 défini au début à sa position
    pygame.display.update() #On rafraichit l'écran



    #joue musique d'ambiance
    if Mode == 0 and time >= 700 : #si le mode de jeu vaut 0 et que time est supérieur à 700
            jeu = pygame.mixer.music.load('sons/Texxit/3.wav') #On prend un son dans le répertoire et on l'associe à jeu
            pygame.mixer.music.queue('sons/Texxit/3.wav') #mettre le sons Texxit 3.wav dans la queue
            pygame.mixer.music.play() #jouer le son
            time = 0 #mettre son a 0

    elif Mode == 1 and time >= 500 : #sinon si le mode de jeu vaut 1 et que le temps est supérieur à 600
            build = pygame.mixer.music.load('sons/Texxit/1.wav') #On prend un son dans le répertoire et on l'associe à jeu
            pygame.mixer.music.queue('sons/Texxit/1.wav') #mettre le sons Texxit 3.wav dans la queue
            pygame.mixer.music.play() #jouer le son
            time = 0 #mettre son a 0
    time += 0.75 #son vaut son+0.75

    if Mode == 1 : #si le mode vaut 1
        #pour chaque bouton si ce dernier est sélectionner
        #afficher la version sélectionner de ce bouton
        #et si click vaut 1 donner une valeur à passe
        if bouton_1.collidepoint((mx, my)):
            Ecran.blit(murInterMouse, (805, 85))
            if click == 1:
                passe = 2
        else:
            Ecran.blit(murInter, (805, 85))

        if bouton_2.collidepoint((mx, my)):
            Ecran.blit(persoInterMouse, (805, 170))
            if click:
                passe = d
        else:
            Ecran.blit(persoInter, (805, 170))

        if bouton_3.collidepoint((mx, my)):
            Ecran.blit(bleuInterMouse, (805, 255))
            if click:
                passe = b
        else:
            Ecran.blit(bleuInter, (805, 255))

        if bouton_4.collidepoint((mx, my)):
            Ecran.blit(pbleuInterMouse, (805, 340))
            if click:
                passe = 9
        else:
            Ecran.blit(pbleuInter, (805, 340))

        if bouton_5.collidepoint((mx, my)):
            Ecran.blit(rougeInterMouse, (805, 425))
            if click:
                passe = c
        else:
            Ecran.blit(rougeInter, (805, 425))

        if bouton_6.collidepoint((mx, my)):
            Ecran.blit(prougeInterMouse, (805, 510))
            if click:
                passe = a
        else:
            Ecran.blit(prougeInter, (805, 510))

        if bouton_7.collidepoint((mx, my)):
            Ecran.blit(caisseInterMouse, (720, 85))
            if click:
                passe = 3
        else:
            Ecran.blit(caisseInter, (720, 85))

        if bouton_8.collidepoint((mx, my)):
            Ecran.blit(pcaisseInterMouse, (720, 170))
            if click:
                passe = 8
        else:
            Ecran.blit(pcaisseInter, (720, 170))

        if bouton_9.collidepoint((mx, my)):
            Ecran.blit(clefInterMouse, (720, 255))
            if click:
                passe = 5
        else:
            Ecran.blit(clefInter, (720, 255))

        if bouton_10.collidepoint((mx, my)):
            Ecran.blit(verrouInterMouse, (720, 340))
            if click:
                passe = 6
        else:
            Ecran.blit(verrouInter, (720, 340))

        if bouton_11.collidepoint((mx, my)):
            Ecran.blit(drapeauInterMouse, (720, 425))
            if click:
                passe = 4
        else:
            Ecran.blit(drapeauInter, (720, 425))

        if bouton_12.collidepoint((mx, my)):
            Ecran.blit(trouInterMouse, (720, 510))
            if click:
                passe = 7
        else:
            Ecran.blit(trouInter, (720, 510))




        if bouton_13.collidepoint((mx, my)):
            Ecran.blit(supprInterMouse, (720, 595))
            if click:
                brouillard = (brouillard+3)%2 #change brouillard état de 1 à 0 ou de 0 à 1
        else:
            if brouillard == 0 : Ecran.blit(supprInter, (720, 595)) # si brouillard vaut 0 alors mettre l'interface supprInter
            if brouillard == 1 : Ecran.blit(supprInter2, (720, 595)) #si brouillard vaut 1 alors mettre l'interface supprinter2





        if score < 30 : #si score est inférieur a 30
            Ecran.blit(facile, (700, 10)) #afficher facile

        elif  30 < score < 100 : #si score est compris entre 30 et 100
            Ecran.blit(moyen, (700, 10)) #afficher moyen

        elif  100 < score  : #si score est supérieur à 100
            Ecran.blit(difficile, (700, 10)) #afficher difficile

        score = 0



    #sauvegarde
    if Mode == 1 and clignote == 79 : #si le mode vaut 1 et clignote vaut 79 (optimisation)
        fichier = open('sauvegarde/level.txt', 'w') #Ouvre le fichier
        fichier.writelines(txtliste) #Ecrit dans le fichier la txtliste
        fichier.close() #ferme le fichier


        player = open('sauvegarde/joueur.txt', 'w') #Ouvre le fichier
        playslot = [0] #définit playslot
        playslot[0] = str(slotj) #transforme playslot en texte de slotj
        player.writelines(playslot) #Ecrit dans le fichier playslot
        player.close() #ferme le fichier

        brouillard_save = open('sauvegarde/brouillard.txt', 'w') #Ouvre brouillard_save
        brouillard_etat = str(brouillard) #définit brouillard état par le string de brouillard
        brouillard_save.writelines(brouillard_etat) #Ecrit dans brouillard_save la variable brouillard
        brouillard_save.close() #ferme brouillard_save


pygame.quit() #On quitte pygames