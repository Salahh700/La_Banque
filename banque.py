a =  9393
b=0
i=0
echec = True
choix=0
A = 0
B = 0
C = 0
D = 0
Fin = False
while a != b and i!=3:
    b=int(input("Quel est ton code: "))
    if a!= b:
        print("c'est pas ca ")
        i=i+1
    else:
        print("bien joué")
        echec = False

if echec == True:
    print("Trop de tentatives raté")
else:
    while Fin != True :
        solde=100000
        choix=int(input("Que veux tu faire : 1 = Consulter le solde 2 = Débiter 3 = Créditer 4 = Quitter "))
        if choix == 1:
            print(solde)
        elif choix == 2:
            soldemoins=int(input("Combien veux tu débiter? "))
            soldemoinss= solde - soldemoins
            print(soldemoinss)
        elif choix == 3:
            soldeplus=int(input("Combien veux tu ajouter? "))
            soldepluss= solde + soldeplus
            print(soldepluss)
        else:
            Fin=True
            print("Au revoir et à bientôt à la banquos")







