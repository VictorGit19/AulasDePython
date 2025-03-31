faturamento = 1000
custo = 600
lucro = faturamento - custo

texto = f"O lucro foi de R${lucro} e o faturamento foi de R${faturamento}"

print(texto)

email = "EMAILFALSO@GMAIL.COM"

email = email.lower()
email = email.strip()
print(email)

print(len(email))

posicao = email.find("@")
print(posicao)

servidor = email[posicao + 1:]
print(servidor)

novo_email = email.replace("gmail.com" , "hotmail.com")
print(novo_email)

nome = "victor hugo"
nome = nome.capitalize()
print(nome)

nome = nome.title()
print(nome)


nome = nome.upper()
print(nome)




faturamento = 1_000
custo = 600
lucro = faturamento - custo
margem = lucro / faturamento

texto = f"O lucro foi de R${lucro:,.2f} e o faturamento foi de R${faturamento :,.2f} e a margem foi de {margem:.0%}"

print(texto)








# Exercicio

nome = "Victor hugo"
email = "emailfalso@gmail.com"


# Descubra o servidor do email

posicao = email.find("@")
servidor = email[posicao+1 : ]
print(servidor)


# Descubra o 1º nome do usuario

pos = nome.find(" ")
prim_nome = nome[ : pos]
prim_nome = prim_nome.upper()
print(prim_nome)


# Criar uma mensagem personalizada 

mensagem = f"Usuario {prim_nome} foi cadastrado com sucesso no  {email}"
print(mensagem)



 