import copy, random

def greedy(cMax, gananciaPeso):
    gananciaPeso = copy.deepcopy(gananciaPeso)
    gananciaPeso.sort(key=lambda x: x[0]/x[1], reverse=True)
    pesoMochila = 0
    mochila = []
    while pesoMochila < cMax and len(gananciaPeso) > 0:
        pesoMochila += gananciaPeso[0][1]
        gananciaPeso.pop(0)
        mochila.append(gananciaPeso[0])
    return mochila, sum(x[0] for x in mochila)

def greedyAleatorio(cMax, gananciaPeso):
    gananciaPeso = copy.deepcopy(gananciaPeso)
    gananciaPeso.sort(key=lambda x: x[0]/x[1], reverse=True)
    pesoMochila = 0
    mochila = []
    posEleccionRandom = random.randint(0, len(gananciaPeso)-1)
    pesoMochila += gananciaPeso[posEleccionRandom][1]
    gananciaPeso.pop(posEleccionRandom)
    while pesoMochila < cMax and len(gananciaPeso) > 0:
        pesoMochila += gananciaPeso[0][1]
        gananciaPeso.pop(0)
        mochila.append(gananciaPeso[0])
    return mochila, sum(x[0] for x in mochila)

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

print(greedy(int(cMax), gananciaPeso))
print(greedyAleatorio(int(cMax), gananciaPeso))