num_testes = int(input())
aux = []
aux2 = []
v = []

while(num_testes > 0):
  n_k = input().split()
  numeros = input().split()
  for i in range(len(numeros)):
    v.append(numeros[i])
  ans = 0 

  for j in range(30,-1,-1):
      qtde = 0

      bit = 1 << j

      for k in range(len(v)-1, -1,-1):
        if(bit & int(v[k])):
          qtde += 1
          aux.append(k)
        else:
          aux2.append(k)
      if(qtde >= int(n_k[1])):
        aux_ans = int(v[aux[0]])
        for l in range(1,qtde, 1):
          aux_ans &= int(v[aux[l]])

        ans = max(ans, aux_ans)

        for m in range(len(aux2)):
          v.remove(v[aux2[m]])
        
      aux.clear()
      aux2.clear()  

  print (ans)
  v.clear()
  num_testes -= 1     