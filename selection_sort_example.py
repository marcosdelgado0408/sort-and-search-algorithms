
vetor = [9,7,8,1,2,0,4]

print(vetor)

for i in range(0,len(vetor)):# vai escolher o elemento pra comparar depois
    min_index = i # o min _index vai guardar apenas a posição
    
    for j in range(i+1,len(vetor)): # vai achar o menor elemento possivel em comparação com o i
       
        if vetor[min_index] > vetor[j]:             
            
            min_index = j     
            
            vetor[min_index],vetor[i] = vetor[i], vetor[min_index]  # no final do for ele vai trocar esses fois elementos 
   

print(vetor)
