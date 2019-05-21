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


    vetor[inicio] = vetor[j] # o inicio vai receber onde o j parar
    vetor[j] = pivo # a posição da direita se torna o pivo

    return j # vai retornar a posição do inicio que será o pivo no caso




def quicksort(vetor, inicio, fim):
    if(fim > inicio):
        pivo = particionar(vetor, inicio, fim)
        quicksort(vetor,inicio, pivo-1)
        quicksort(vetor, pivo+1, fim)



# se eu ordenar cada "sliding window" eu saberei que o maior elemento seráo ultimo de cada "sliding window"

vetor = [1,3,-1,-3,5,3,6,7]

imprimir_dps = []

print("Digite um valor para k: ")
k = int(input())


for i in range(0, len(vetor)-1):
    
    if(i+k <= len(vetor)-1):# verificação pra não passar

        quicksort(vetor,0,i+k) # ordenar o vetor na posição da sliding window
        
        imprimir_dps.append(vetor[i+k])# vai jogar o maior elemento no vetor pra imprimir dps


print(imprimir_dps)
