disc = {"ipad": 7000 , "iphone": 5000 , "airpod": 2000 , "macbook" : 12000}


produto_buscado = input("Digite um nome do produto?")

produto_buscado = produto_buscado.strip()
produto_buscado = produto_buscado.lower()

if produto_buscado in disc :
    preco = disc[produto_buscado]
    print("Produto encontrado")
    print(f"Produto : {produto_buscado} , preço : R${preco}")
else:
    print("Produto não encontrado")