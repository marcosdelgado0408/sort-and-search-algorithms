

def MergeSort(vetor , vetor_aux, inicio, fim):
    if(inicio < fim): # enquanto o vetor existir ele vai fazer isso
        meio = (inicio + fim) // 2
        MergeSort(vetor, vetor_aux, inicio, meio)
        MergeSort(vetor, vetor_aux,meio + 1, fim)
        intercalar(vetor, vetor_aux, inicio, meio, fim)    


def intercalar(vetor, vetor_aux, inicio, meio, fim):   
    for k in range(inicio,fim):
        vetor_aux[k] = vetor[k]

    i = inicio
    j = meio + 1

    for k in range(inicio,fim):
        if(i > meio):
            vetor[k] = vetor_aux[j+1]
       
        elif(j > fim):
            vetor[k] = vetor_aux[i+1]
       
        elif(vetor_aux[i] < vetor_aux[j]):
            vetor[k] = vetor_aux[i+1]

        else:
            vetor[k] = vetor_aux[j+1]







# ---MAIN---

vetor = [4,6,7,3,5,1,2,8]
vetor_aux = [len(vetor)]

tam = len(vetor)

print(len(vetor))

MergeSort(vetor, vetor_aux, 0, tam)

