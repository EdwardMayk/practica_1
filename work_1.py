def presentacion():
    print(" Ruta Optima" )

    print("           B          ")
    print("         / | \        ")
    print("       /   |   \      ")
    print("     /     |     \    ")
    print("   F  ---  | ---  J  ")
    print("     \     |     /    ")
    print("       \   |   /      ")
    print("         \ | /      ")
    print("           A          ")

def distancia():
    print("\nIngresa la distancia entre: ")
    distancia_FB = int(input("F y B: "))
    distancia_FJ = int(input("F y J: "))
    distancia_FA = int(input("F y A: "))
    distancia_BA = int(input("B y A: "))
    distancia_BJ = int(input("B y J: "))
    distancia_AJ = int(input("A y J: "))

    suma = 0
    
    print("\nIndicar punto de partida: ")
    partida = input("-> F // B //J // A: ")


    if partida == "F":
        if distancia_FB <= distancia_FJ and distancia_FB <= distancia_FA and distancia_BA <= distancia_BJ:
                suma = distancia_FB + distancia_BA + distancia_AJ + distancia_FJ
                print("\nMejor ruta: F -> B -> A -> J -> F")

        elif distancia_FA <= distancia_FJ and distancia_FA <= distancia_FB and distancia_BA <= distancia_AJ:
                suma = distancia_FA + distancia_BA + distancia_BJ + distancia_FJ
                print("\nMejor ruta: F -> A -> B -> J -> F")

        elif distancia_FJ <= distancia_FB and distancia_FJ <= distancia_FA and distancia_BJ <= distancia_AJ:
                suma = distancia_FJ + distancia_BJ + distancia_BA + distancia_FA
                print("\nMejor ruta: F -> J -> B -> A -> F")

        elif distancia_FJ <= distancia_FB and distancia_FJ <= distancia_FA and distancia_AJ <= distancia_BJ:
                suma = distancia_FJ + distancia_AJ + distancia_BA + distancia_FB
                print("\nMejor ruta: F -> J -> A -> B -> F")

        elif distancia_FB <= distancia_FJ and distancia_FB <= distancia_FA and distancia_BJ <= distancia_BA:
                suma = distancia_FB + distancia_BJ + distancia_AJ + distancia_FA
                print("\nMejor ruta: F -> B -> J -> A -> F")

        elif distancia_FA <= distancia_FJ and distancia_FA <= distancia_BJ and distancia_AJ <= distancia_BA:
                suma = distancia_FA + distancia_AJ + distancia_BJ + distancia_FB
                print("\nMejor ruta: F -> A -> J -> B -> F")

    if partida == "B":
        if distancia_FB <= distancia_BA and distancia_FB <= distancia_BJ and distancia_FJ <= distancia_FA:
                suma = distancia_FB + distancia_FJ + distancia_AJ + distancia_BA
                print("\nMejor ruta: B -> F -> J -> A -> B")

        elif distancia_BJ <= distancia_BA and distancia_BJ <= distancia_FB and distancia_FJ <= distancia_AJ:
                suma = distancia_BJ + distancia_FJ + distancia_FA + distancia_BA
                print("\nMejor ruta: B -> J -> F -> A -> B")

        elif distancia_BA <= distancia_FB and distancia_BA <= distancia_BJ and distancia_AJ <= distancia_FA:
                suma = distancia_BA + distancia_AJ + distancia_FJ + distancia_FB
                print("\nMejor ruta: B -> A -> J -> F -> B")

        elif distancia_BA <= distancia_FB and distancia_BA <= distancia_BJ and distancia_FA <= distancia_AJ:
                suma = distancia_BA + distancia_FA + distancia_FJ + distancia_BJ
                print("\nMejor ruta: B -> A -> F -> J -> B")

        elif distancia_BJ <= distancia_BA and distancia_BJ <= distancia_FB and distancia_AJ <= distancia_FJ:
                suma = distancia_BJ + distancia_AJ + distancia_FA + distancia_FB
                print("\nMejor ruta: B -> J -> A -> F -> B")

        elif distancia_FB <= distancia_BA and distancia_FB <= distancia_BJ and distancia_FA <= distancia_FJ:
                suma = distancia_FB + distancia_FA + distancia_AJ + distancia_BJ
                print("\nMejor ruta: B -> F -> A -> J -> B")

    if partida == "J":
        if distancia_BJ <= distancia_FJ and distancia_BJ <= distancia_AJ and distancia_BA <= distancia_FB:
                suma = distancia_BJ + distancia_BA + distancia_FA + distancia_FJ
                print("\nMejor ruta: J -> B -> A -> F -> J")

        elif distancia_AJ <= distancia_FJ and distancia_AJ <= distancia_BJ and distancia_BA <= distancia_FA:
                suma = distancia_AJ + distancia_BA + distancia_FB + distancia_FJ
                print("\nMejor ruta: J -> A -> B -> F -> J")

        elif distancia_FJ <= distancia_BJ and distancia_FJ <= distancia_AJ and distancia_FB <= distancia_FA:
                suma = distancia_FJ + distancia_FB + distancia_BA + distancia_AJ
                print("\nMejor ruta: J -> F -> B -> A -> J")

        elif distancia_FJ <= distancia_BJ and distancia_FJ <= distancia_AJ and distancia_FA <= distancia_FB:
                suma = distancia_FJ + distancia_FA + distancia_BA + distancia_BJ
                print("\nMejor ruta: J -> F -> A -> B -> J")

        elif distancia_BJ <= distancia_FJ and distancia_BJ <= distancia_AJ and distancia_FB <= distancia_BA:
                suma = distancia_BJ + distancia_FB + distancia_FA + distancia_AJ
                print("\nMejor ruta: J -> B -> F -> A -> J")

        elif distancia_AJ <= distancia_FJ and distancia_AJ <= distancia_BJ and distancia_FA <= distancia_BA:
                suma = distancia_BJ + distancia_FA + distancia_FB + distancia_BJ
                print("\nMejor ruta: J -> A -> F -> B -> J")

    if partida == "A":
        if distancia_FA <= distancia_BA and distancia_FA <= distancia_AJ and distancia_FJ <= distancia_FB:
                suma = distancia_FA + distancia_FJ + distancia_BJ + distancia_BA
                print("\nMejor ruta: A -> F -> J -> B -> A")

        elif distancia_AJ <= distancia_BA and distancia_AJ <= distancia_FA and distancia_FJ <= distancia_BJ:
                suma = distancia_AJ + distancia_FJ + distancia_FB + distancia_BA
                print("\nMejor ruta: A -> J -> F -> B -> A")

        elif distancia_BA <= distancia_FA and distancia_BA <= distancia_AJ and distancia_FB <= distancia_BJ:
                suma = distancia_BA + distancia_FB + distancia_FJ + distancia_AJ
                print("\nMejor ruta: A -> B -> F -> J -> A")

        elif distancia_BA <= distancia_FA and distancia_BA <= distancia_AJ and distancia_FB <= distancia_BJ:
                suma = distancia_BA + distancia_FB + distancia_FJ + distancia_AJ
                print("\nMejor ruta: A -> B -> F -> J -> A")

        elif distancia_BA <= distancia_FA and distancia_BA <= distancia_AJ and distancia_BJ <= distancia_FB:
                suma = distancia_BA + distancia_BJ + distancia_FJ + distancia_FA
                print("\nMejor ruta: A -> B -> J -> F -> A")

        elif distancia_FA <= distancia_BA and distancia_FA <= distancia_AJ and distancia_FB <= distancia_FJ:
                suma = distancia_FA + distancia_FB + distancia_BJ + distancia_AJ
                print("\nMejor ruta: A -> F -> B -> J -> A")

        elif distancia_AJ <= distancia_BA and distancia_AJ <= distancia_FA and distancia_BJ <= distancia_FJ:
                suma = distancia_AJ + distancia_BJ + distancia_FB + distancia_FA
                print("\nMejor ruta: A -> J -> B -> F -> A")

    print("Ruta optima:", suma, "km. ")

if __name__ =="__main__":

    recorrido = distancia()
    menu = presentacion()


