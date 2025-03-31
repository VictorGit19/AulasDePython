#Aprendendo condicionais

faturamento = 1000
custo = 6000

lucro = faturamento - custo

if lucro >= 0:
    print("O lucro foi de " , lucro)

else:
    print("O prejuizo foi de " , lucro)

#Aprendendo adicionar produto na lista através de condicionais
produtos = ["iphone" , "ipaad" , "airpod"]
novos_produto = input("Digite um nome do produto:")

if novos_produto in produtos :
    print("Produto já existente!")

else:
    print(f"{novos_produto} cadastrado com sucesso")
    produtos.append(novos_produto)

    print(produtos)


#Diferença entre if , elif e else

vendas = 20000

if vendas >= 15000 :
   bonus = 500

else:
   if vendas >= 5000:
      bonus = 100
   else:
    bonus = 0

print(f"Bonûs do funcionario: {bonus}")

#Usando elif para simplicar o codigo sem usar muito if dentro else
vendas = 5000

if vendas >= 15000:
   bonus = 500

elif vendas >= 5000:
   bonus = 100

else:
   bonus = 0

print(f"Bonûs do funcionario: {bonus}")


#Resolvendo questão que aprendi na aula de Condicionais
vendas_empresa = 200_000
meta_empresa = 100_000
vendas_funcionario = 20000

if vendas_funcionario >= 15000 and vendas_empresa >= meta_empresa:
    bonus = 500

elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 100

else:
    bonus = 0


print(f"Bonûs do funcionario: {bonus}")