vetor = [1,5,7,10,15,17,26,37,39,42,54]

print(vetor)

print("Digite o numero alvo: ")
alvo = int(input())



inicio = 0 # posição do inicio do vetor

final = len(vetor) # posição final do vetor

tamanho = final - inicio

while(tamanho > 0):
    
    meio = tamanho // 2 # o meio sempre será uma divisão inteira
    
    if(alvo == vetor[meio]):
        print("Alvo localizado = {}\nVetor[{}]".format(vetor[meio],meio))
        break
    elif(alvo < vetor[meio]):
       final = meio # vai descartar tudo de vetor[meio] pra frente
    else:
        inicio = meio + 1 # vai ser +1 pois eu quero descartar o elemento de vetor[meio]
    tamanho = final - inicio # redefinindo o tamanho pois foram alterados o final e o incio
       

