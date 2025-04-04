for i in range(10):
    print("victor")

list_preco = [1500 , 1000 , 800 , 2000]

#taxa_imposto = 0.1

#for preco in list_preco:
    #imposto = preco * taxa_imposto
    #print(f"Preço do produto {preco} , imposto é de {imposto}")


            #Exemplo 1


#Produtos de até 1000 pagam 15% de imposto

#for preco in list_preco :
    #if preco > 1000 :
        #taxa = 0.15
    #else :
        #taxa = 0.1
        #imposto = taxa * preco 
        #print(f"Preço do produto: {preco}, Imposto: {imposto}")


          
          #Exemplo 2
#Mesma regra de imposto mas eu quero conseguir calcular o total de imposto somado de todos os Produtos

total_imposto = 0

for preco in list_preco:
    if preco > 1000 :
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preco

    total_imposto = total_imposto + imposto

    print(f"Preço do produto: {preco}, Imposto: {imposto}")

    print("Total de Imposto " , total_imposto)