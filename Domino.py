class peca :
    def __init__(self, lado1, lado2) :
        self.lado1 = lado1
        self.lado2 = lado2

class jogador :
    def __init__(self, nome, pecas, vez) :
        self.nome = nome
        self.pecas = pecas
        self.vez = vez
        self.contagem = 0

pecasDomino = []
jogo = []
jogadores = []
for i in range(7) :
    for j in range(7) :
        if (j >= i) :
            pecasDomino.append(peca(i, j))

import random

random.shuffle(pecasDomino)

for i in range(4) :
    nome = str(input("Digite o nome do %d° Jogador " % (+(i + 1))))
    jogadores.append(jogador(nome, [], None))

for i in range(len(pecasDomino)) :
    if (i < 7) :
        jogadores[0].pecas.append(pecasDomino[i])
        if (jogadores[0].pecas[i].lado1 == 6 and jogadores[0].pecas[i].lado2 == 6) :
            jogadores[0].vez = 0
            jogadores[1].vez = 1
            jogadores[2].vez = 2
            jogadores[3].vez = 3

    elif (i >= 7 and i <= 13) :
        jogadores[1].pecas.append(pecasDomino[i])
        for j in range(len(jogadores[1].pecas)) :
            if (jogadores[1].pecas[j].lado1 == 6 and jogadores[1].pecas[j].lado2 == 6) :
                jogadores[0].vez = 3
                jogadores[1].vez = 0
                jogadores[2].vez = 1
                jogadores[3].vez = 2

    elif (i >= 14 and i <= 20) :
        jogadores[2].pecas.append(pecasDomino[i])
        for j in range(len(jogadores[2].pecas)) :
            if (jogadores[2].pecas[j].lado1 == 6 and jogadores[2].pecas[j].lado2 == 6) :
                jogadores[0].vez = 2
                jogadores[1].vez = 3
                jogadores[2].vez = 0
                jogadores[3].vez = 1

    else :
        jogadores[3].pecas.append(pecasDomino[i])
        for j in range(len(jogadores[3].pecas)) :
            if (jogadores[3].pecas[j].lado1 == 6 and jogadores[3].pecas[j].lado2 == 6) :
                jogadores[0].vez = 1
                jogadores[1].vez = 2
                jogadores[2].vez = 3
                jogadores[3].vez = 0

def compara_pecas(jogo, peca, lado_jogo) :
    if (lado_jogo == 1) :
        if (jogo.lado2 == peca.lado1) :
            return 1
        elif (jogo.lado2 == peca.lado2) :
            return 2
        else :
            return 0
    elif (lado_jogo == 2) :
        if (jogo.lado1 == peca.lado2) :
            return 1
        elif (jogo.lado1 == peca.lado1) :
            return 2
        else :
            return 0

def imprimir_jogador_pecas(jogador) :
    print("Jogador: ", jogador.nome)
    for i in range(len(jogador.pecas)) :
        print("[" + str(jogador.pecas[i].lado1) + " : " + str(jogador.pecas[i].lado2) + "]")

def imprimir_jogo(lista) :
    resultado = "JOGO "
    for i in range(len(lista)) :
        resultado += ("[" + str(lista[i].lado1) + " : " + str(lista[i].lado2) + "] ")
    print(resultado)

def imprime_peca(peca):
    return "["+ str(peca.lado1)+" : "+ str(peca.lado2)+"]"

def jogar(jogador) :
    if len(jogo) == 0 :
        for i in range(len(jogador.pecas)) :
            if ((len(jogo) == 0)
                and (jogador.pecas[i].lado1 == 6)
                and (jogador.pecas[i].lado2 == 6)) :
                jogo.append(jogador.pecas[i])
                imprimir_jogador_pecas(jogador)
                print("O "+jogador.nome+" Jogou "+ imprime_peca(jogador.pecas[i]))
                imprimir_jogo(jogo)
                jogador.pecas.pop(i)
                return False
    else :
        for i in range(len(jogador.pecas)) :
            lado = compara_pecas(jogo[len(jogo)-1], jogador.pecas[i], 1)
            if (lado != 0) :
                if lado == 1 :
                    jogo.append(jogador.pecas[i])
                    imprimir_jogador_pecas(jogador)
                    print("O " + jogador.nome + " Jogou " + imprime_peca(jogador.pecas[i]))
                    imprimir_jogo(jogo)
                    jogador.pecas.pop(i)
                    return False
                elif lado == 2 :
                    jogo.append(peca(jogador.pecas[i].lado2, jogador.pecas[i].lado1))
                    imprimir_jogador_pecas(jogador)
                    print("O " + jogador.nome + " Jogou " + imprime_peca(jogador.pecas[i]))
                    imprimir_jogo(jogo)
                    jogador.pecas.pop(i)
                    return False
            else :
                lado = compara_pecas(jogo[0], jogador.pecas[i], 2)
                if (lado != 0) :
                    if lado == 1 :
                        jogo.insert(0, jogador.pecas[i])
                        imprimir_jogador_pecas(jogador)
                        print("O " + jogador.nome + " Jogou " + imprime_peca(jogador.pecas[i]))
                        imprimir_jogo(jogo)
                        jogador.pecas.pop(i)
                        return False
                    elif lado == 2 :
                        jogo.insert(0, peca(jogador.pecas[i].lado2, jogador.pecas[i].lado1))
                        imprimir_jogador_pecas(jogador)
                        print("O " + jogador.nome + " Jogou " + imprime_peca(jogador.pecas[i]))
                        imprimir_jogo(jogo)
                        jogador.pecas.pop(i)
                        return False
                elif (i == (len(jogador.pecas)-1)) :
                    print(jogador.nome+" Tocou")
                    return True
    if len(jogador.pecas) == 0 :
        print(jogador.nome + " ganhou!!!")
        return True


fechou = False
while (not fechou) :
    fechou = True
    contador = 0
    for minha_vez in range(4) :
        if (jogadores[0].vez == minha_vez) :
            fechou = jogar(jogadores[0])
            if(fechou == True):
                contador+=1
            if (len(jogadores[0].pecas)==0):
                break

        if (jogadores[1].vez == minha_vez) :
            fechou = jogar(jogadores[1])
            if (fechou == True) :
                contador += 1
            if (len(jogadores[1].pecas)==0):
                break

        if (jogadores[2].vez == minha_vez) :
            fechou = jogar(jogadores[2])
            if (fechou == True) :
                contador += 1
            if (len(jogadores[2].pecas)==0):
                break

        if (jogadores[3].vez == minha_vez) :
            fechou = jogar(jogadores[3])
            if (fechou == True) :
                contador += 1
            if (len(jogadores[3].pecas)==0):
                break

        if(contador < 4):
            fechou = False

        elif(contador >= 4 and  fechou == True):
            for i in range(4) :
                for j in range(len(jogadores[i].pecas)):
                    jogadores[i].contagem += jogadores[i].pecas[j].lado1 + jogadores[i].pecas[j].lado2
            print("Jogo trancado")
            if (jogadores[0].contagem < jogadores[1].contagem and jogadores[0].contagem < jogadores[2].contagem and jogadores[0].contagem < jogadores[3].contagem):
                print("O Jogador "+jogadores[0].nome+" ganhou na contagem de pontos!!!")
            elif(jogadores[1].contagem < jogadores[0].contagem and jogadores[1].contagem < jogadores[2].contagem and jogadores[1].contagem < jogadores[3].contagem):
                print("O Jogador " + jogadores[1].nome + " ganhou na contagem de pontos!!!")
            elif (jogadores[2].contagem < jogadores[0].contagem and jogadores[2].contagem < jogadores[1].contagem and jogadores[2].contagem < jogadores[3].contagem):
                print("O Jogador " + jogadores[2].nome + " ganhou na contagem de pontos!!!")
            elif (jogadores[3].contagem < jogadores[0].contagem and jogadores[3].contagem < jogadores[1].contagem and jogadores[3].contagem < jogadores[2].contagem):
                print("O Jogador " + jogadores[3].nome + " ganhou na contagem de pontos!!!")
            else:
                Print("Empate")
