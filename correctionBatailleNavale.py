#Création de deux champs pour l'exercice 4
champ1=[['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X']]
champ2=[['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X']]
#Exercice 1        
def placerBateau (i,j,champ):
    champ[i-1][j-1]='O'
    return champ
#Exercice 2
def attaque(i,j,champ):
    if champ[i-1][j-1]=='O':
        print("Touché!")
    else:
        print("Raté")
    champ[i-1][j-1]="x"
    return champ
#Exercice 3
def nbSurvivant (champ) :
    compteur=0
    for i in champ :
        for j in i :
            if j=='O' :
                compteur+=1
    return compteur