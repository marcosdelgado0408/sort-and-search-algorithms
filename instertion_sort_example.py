vetor = [6,5,3,1,8,7,2,4]

print(vetor)

auxiliar = 0

for i in range(1,len(vetor)):
    auxiliar = vetor[i]
    j=i
    while j > 0 and vetor[j-1] > auxiliar:#vai repetir esse laço até chegar no primeiro elemento
        vetor[j] = vetor[j-1]
        j -=1
    vetor[j] = auxiliar # vai trocar o primerio elemento com o da posição i


print(vetor)
