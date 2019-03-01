def interet():

    try:      
        annees = int(input("Quelle est le nombre d'année où les intérets seront composés ?"))
        taux = float(input("Quel est le taux d'interet ?"))
        somme = float(input("Somme à placer"))
    
        total = somme*(1+taux)**annees
       
        if somme < 0 or annees < 0 or taux < 0: 
            raise ValueError
    
    except ValueError as erreur:
        print("La valeur insérée n'est pas valide \n")
        print(erreur)
     
    
    return print ("Vous allez recevoir {:.2F} euros".format(total))

