


def busca_binaria(vetor, inicio, fim , alvo):
    
    meio = (inicio + fim) // 2
    
    if(vetor[meio] == alvo):
        return meio

    if(alvo < vetor[meio]):
        return busca_binaria(vetor, inicio, meio-1, alvo) # vai pesquisar do meio -1 pra tras -> até inicio do vetor -> pois o alvo é menor
    
    else:
        return busca_binaria(vetor , meio+1, fim, alvo) # vai pesquisar do meio +1 pra frente -> até o fim do vetor -> peio o alvo é maior









vetor = [1,5,7,10,15,17,26,37,39,42,54] 

print(vetor)


print("Digite o valor para achar:")
alvo = int(input())

inicio = 0
fim = len(vetor)


resultado = busca_binaria(vetor, inicio, fim, alvo)

print("Valor encontrado -> vetor[{}]".format(resultado))



