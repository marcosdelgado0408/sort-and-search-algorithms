
def particionar(vetor, inicio, fim):
    i = inicio # esquerda do vetor 
    j = fim # direita do vetor 
    pivo = vetor[inicio] # escolha do pivo

    while(i < j):# um indice não pode ser maior que outro
        
        while(vetor[i] <= pivo): # coloquei >=  pois peguei o pivo como a primeira posição
            i += 1  # i++
        
        while(vetor[j] > pivo):
            j -= 1 # j--
        
        if(i < j):
            vetor[j],vetor[i] = vetor[i], vetor[j] # trocando as posições que estão "paradas"
        

    vetor[inicio] = vetor[j] # o inicio vai receber onde a direita parar
    vetor[j] = pivo # a posição da direita se torna o pivo
    
    return j # vai retornar a posição do inicio que será o pivo no caso




def quicksort(vetor, inicio, fim):
    if(fim > inicio):
        pivo = particionar(vetor, inicio, fim)
        quicksort(vetor,inicio, pivo-1)
        quicksort(vetor, pivo+1, fim)














vetor = [2,1,96,24,107,20,15,32,54,45]


print(vetor)

inicio = 0
fim = len(vetor)-1


quicksort(vetor, inicio, fim)

print(vetor)





