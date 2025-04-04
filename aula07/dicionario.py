lista_produto = ["ipad" , "iphone " , "airpod"]
lista_preco = [7000 , 5000 , 2000]

disc = {"ipad": 7000 , "iphone": 5000 , "airpod": 2000}

#Pegar um item 
produto = "iphone "
posicao = lista_produto.index(produto)
preco = lista_preco[posicao]
print(produto , preco)

print(disc["ipad"])


dic_venda = {"lira" : [1000 , 500 , 1500] , "joao" : [500 , 400 , 500]}
print(dic_venda["lira"])

#adicionar um item 
#editar um item

disc["iphone"] = disc["iphone"] * 1.1

disc["macbook"] = 12000
print(disc)


#Remover um item

disc.pop("macbook")
print(disc)

#Verificar se existe um item no dicionario 

print("iphone" in disc)
print("iphone" in disc.keys())
print(2000 in disc.values())
print(preco)

#Contagem de itens no Dicionários

qtde = len(disc)
print(qtde)


