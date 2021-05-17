from random_words import *
from Dictionnaire import *
from Player1 import *
from Player2 import *
from random import *
import sys


# variable

liste_insulte=[]
global XPj1
XPj1 = 0
global XPj2
XPj2 = 0

# def
def ListeAffichage():
    display = ""
    for value in liste_insulte:
        display = display + " " + str(value)
    print(display)

def Proposition_Sujet():
    A = random_Sujet()
    B = random_Sujet()
    print("Proposition : ")
    print("A : {}, B : {}".format(A, B))
    T = input("Votre choix ? ")
    if T == 'A': liste_insulte.append(A)
    if T == 'B': liste_insulte.append(B)

def Proposition_Verbe():
    A = random_Verbe()
    B = random_Verbe()
    print("Proposition : ")
    print("A : {}, B : {}".format(A, B))
    T = input("Votre choix ? ")
    if T == 'A': liste_insulte.append(A)
    if T == 'B': liste_insulte.append(B)

def Proposition_Complement():
    A = random_Complement()
    B = random_Complement()
    print("Proposition : ")
    print("A : {}, B : {}".format(A, B))
    T = input("Votre choix ? ")
    if T == 'A': liste_insulte.append(A)
    if T == 'B': liste_insulte.append(B)


def GamePlay():

    #Joueur 1 
    print("Bonjour joueur 1, quel personnage choisissez vous ? ")
    print("Paysan, Seigneur, Chevalier ou Bourgeois")
    value = input("Votre choix ? ")
    j1 = joueur1(value)
    print("")

     #Joueur 2
    print("Bonjour joueur 2, quel personnage choisissez vous ? ")
    print("Paysan, Seigneur, Chevalier ou Bourgeois")
    value = input("Votre choix ? ")
    j2 = joueur2(value)
    
    Current_Player = 1
    GameIsActive = 0
    Active = 0
    
    while Active ==0:
        print("Pitier Monsieur, le jeu qui n'en contient pas")
        while GameIsActive !=3:
        
            if Current_Player == 1:
                print("Votre insulte joueur 1 : " + j1.insulte) 
                Proposition_Sujet()
                ListeAffichage()
                Proposition_Verbe()
                ListeAffichage()
                Proposition_Complement()
                ListeAffichage()
                calculj1 = round((len(liste_insulte)*j1.repartie_lvl*j1.loquacite_lvl)/3)
                global XPj1
                XPj1 += calculj1
                print (XPj1)
                del liste_insulte[:]
                Current_Player += 1

            if Current_Player == 2:
                print("Votre insulte joueur 2 :" + j2.insulte)
                Proposition_Sujet()
                ListeAffichage()
                Proposition_Verbe()
                ListeAffichage()
                Proposition_Complement()
                ListeAffichage()
                calculj2 = round((len(liste_insulte)*j2.repartie_lvl*j2.loquacite_lvl)/3)
                global XPj2
                XPj2 += calculj2
                print (XPj2)
                del liste_insulte[:]
                Current_Player -= 1
                GameIsActive+=1
        if XPj1>XPj2:
            print("Bravo joueur 1, tu as gagné ! Avec un score de :",XPj1)
            continuer=int(input("Choisissez entre 1 pour continuer ou 2 pour stop"))
            if continuer ==1:
                GamePlay()
            elif continuer ==2:
                sys.exit()
        if XPj2>XPj1:
            print("Bravo joueur 2, tu as gagné ! Avec un score de :",XPj2)
            continuer=int(input("Choisissez entre 1 pour continuer ou 2 pour stop"))
            if continuer ==1:
                GamePlay()
            elif continuer ==2:
                sys.exit()
            GamePlay()
        else:
            print("Vous êtes à ex aequo, pas top ")
            continuer=int(input("Choisissez entre 1 pour continuer ou 2 pour stop"))
            if continuer ==1:
                GamePlay()
            elif continuer ==2:
                sys.exit()
            GamePlay()

GamePlay()