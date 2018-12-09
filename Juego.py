print ("Te reto a un juego. Tenemos 13 piedras. Cada uno en su turno tiene que coger 1, 2 o 3. El juego consiste en no ser el último en coger la última piedra. Te aviso que siempre te voy a ganar")

total = 13
vp = 4

while total >=3:
    juego13= input ("Es tu turno, cuántas coges?:")
    try:
        ijuego13=int(juego13)
        if ijuego13<=3 and ijuego13>0:
            er = vp - ijuego13
            total = total - ijuego13 - er
            print ("Yo he cogido", er)
            print ("Quedan", total)
            continue

        else:
            print ("Por favor introduce un valor numérico entre el 1 y el 3: ")
            continue

    except:
        print ("Por favor introduce un valor numérico que sea 1, 2 o 3: ")
        continue
    total= total - ijuego13
print ("Lo siento sólo quedan", total, ". Has perdido!")
