num_testes = input()
jogos = []
print("")

for i in range (int(num_testes)):
    matriz = []
    j = 0
    while j < 5:
        linha = input().split()
        if(linha):
            matriz.append(linha)
            j+=1
    jogos.append(matriz)
    print ("")
    
def roda_matriz(k, l, m, jogo):
    result1 = False
    result2 = False

    if(l == 4 and m == 4):
        return True
    else:
        if((m+1) < 5):
            if(int(jogo[l][m+1]) == 0):
                result1 = roda_matriz(k, l, (m+1), jogo)
        if((l+1) < 5):
            if(int(jogo[l+1][m]) == 0):
                result2 = roda_matriz(k, (l+1), m, jogo) 
    return False or result1 or result2

for jogo in jogos:
    if(roda_matriz(0,0,0, jogo) == True):
        print ("COPS")
    else:
        print ("ROBBERS")