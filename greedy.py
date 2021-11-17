import copy, random

def greedy(cMax:int, gananciaPeso:list) -> tuple:
    gananciaPeso = copy.deepcopy(gananciaPeso)
    gananciaPeso.sort(key=lambda x: x[0]/x[1], reverse=True)
    pesoMochila = 0
    mochila = []
    while pesoMochila + gananciaPeso[0][1]  <= cMax and len(gananciaPeso) > 0:
        pesoMochila += gananciaPeso[0][1]
        mochila.append(gananciaPeso[0])
        gananciaPeso.pop(0)
    return mochila, sum(x[0] for x in mochila), sum(x[1] for x in mochila)

def greedyNuevaFuncionMiope(cMax:int, gananciaPeso:list) -> tuple:
    gananciaPeso = copy.deepcopy(gananciaPeso)
    gananciaPeso.sort(reverse=True)
    pesoMochila = 0
    mochila = []
    while pesoMochila + gananciaPeso[0][1]  <= cMax and len(gananciaPeso) > 0:
        pesoMochila += gananciaPeso[0][1]
        mochila.append(gananciaPeso[0])
        gananciaPeso.pop(0)
    return mochila, sum(x[0] for x in mochila), sum(x[1] for x in mochila)

def greedyAleatorio(cMax:int, gananciaPeso:list) -> tuple:
    gananciaPeso = copy.deepcopy(gananciaPeso)
    gananciaPeso.sort(key=lambda x: x[0]/x[1], reverse=True)
    pesoMochila = 0
    mochila = []
    selected = False
    while not selected:
        posEleccionRandom = random.randint(0, len(gananciaPeso)-1)
        if gananciaPeso[posEleccionRandom][1] + pesoMochila <= cMax:
            selected = True
            pesoMochila += gananciaPeso[posEleccionRandom][1]
            mochila.append(gananciaPeso[posEleccionRandom])
            gananciaPeso.pop(posEleccionRandom)
    while pesoMochila + gananciaPeso[0][1] <= cMax and len(gananciaPeso) > 0:
        pesoMochila += gananciaPeso[0][1]
        mochila.append(gananciaPeso[0])
        gananciaPeso.pop(0)
    return mochila, sum(x[0] for x in mochila), sum(x[1] for x in mochila)

def greedyAleatorioNuevaFuncionMiope(cMax:int, gananciaPeso:list) -> tuple:
    gananciaPeso = copy.deepcopy(gananciaPeso)
    gananciaPeso.sort(reverse=True)
    pesoMochila = 0
    mochila = []
    selected = False
    while not selected:
        posEleccionRandom = random.randint(0, len(gananciaPeso)-1)
        if gananciaPeso[posEleccionRandom][1] + pesoMochila <= cMax:
            selected = True
            pesoMochila += gananciaPeso[posEleccionRandom][1]
            mochila.append(gananciaPeso[posEleccionRandom])
            gananciaPeso.pop(posEleccionRandom)
    while pesoMochila + gananciaPeso[0][1] <= cMax and len(gananciaPeso) > 0:
        pesoMochila += gananciaPeso[0][1]
        mochila.append(gananciaPeso[0])
        gananciaPeso.pop(0)
    return mochila, sum(x[0] for x in mochila), sum(x[1] for x in mochila)

def modifiedGreedyAleatorio(cMax:int, gananciaPeso:list, alpha:int) -> tuple:
    gananciaPeso = copy.deepcopy(gananciaPeso)
    gananciaPeso.sort(key=lambda x: x[0]/x[1], reverse=True)
    pesoMochila = 0
    mochila = []
    selected = False
    while not selected:
        posEleccionRandom = random.randint(0, len(gananciaPeso)-1)
        if gananciaPeso[posEleccionRandom][1] + pesoMochila <= cMax:
            selected = True
            pesoMochila += gananciaPeso[posEleccionRandom][1]
            mochila.append(gananciaPeso[posEleccionRandom])
            gananciaPeso.pop(posEleccionRandom)
    bestAlphaElements = []
    while len(bestAlphaElements) < alpha and len(gananciaPeso) > 0:
        for i in range(alpha):
            bestAlphaElements.append(gananciaPeso[i])
        selected = random.choice(bestAlphaElements)
        if selected[1] + pesoMochila <= cMax:
            pesoMochila += selected[1]
            mochila.append(selected)
            gananciaPeso.remove(selected)
            bestAlphaElements = []
        else:
            break
    return mochila, sum(x[0] for x in mochila), sum(x[1] for x in mochila)

fp = open("mochila.txt", "r")
primero = True
gananciaPeso = []
for linea in fp:
    linea = linea.strip()
    if primero:
        n, cMax = (list(int(x) for x in linea.split(" ")))
        primero = False
    else:
        gananciaPeso.append(list(int(x) for x in linea.split(" ")))
fp.close()

mochila, ganancia, peso = greedy(cMax, gananciaPeso)
print("Algoritmo Greedy.")
print("La mochila contiene", mochila)
print("La ganancia es", ganancia)
print("El peso es", peso)
mochila, ganancia, peso = greedyNuevaFuncionMiope(cMax, gananciaPeso)
print("Algoritmo greedyNuevaFuncionMiope.")
print("La mochila contiene", mochila)
print("La ganancia es", ganancia)
print("El peso es", peso)
mochila, ganancia, peso = greedyAleatorio(cMax, gananciaPeso)
print("Algoritmo greedyAleatorio.")
print("La mochila contiene", mochila)
print("La ganancia es", ganancia)
print("El peso es", peso)
mochila, ganancia, peso = greedyAleatorioNuevaFuncionMiope(cMax, gananciaPeso)
print("Algoritmo greedyAleatorioNuevaFuncionMiope.")
print("La mochila contiene", mochila)
print("La ganancia es", ganancia)
print("El peso es", peso)
mochila, ganancia, peso = modifiedGreedyAleatorio(cMax, gananciaPeso, 5)
print("Algoritmo modifiedGreedyAleatorio alpha = 5.")
print("La mochila contiene", mochila)
print("La ganancia es", ganancia)
print("El peso es", peso)
mochila, ganancia, peso = modifiedGreedyAleatorio(cMax, gananciaPeso, 10)
print("Algoritmo modifiedGreedyAleatorio alpha = 10.")
print("La mochila contiene", mochila)
print("La ganancia es", ganancia)
print("El peso es", peso)