faturamento = 1200 
custo = 750.0  

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto = faturamento * 0.1
lucro = faturamento - custo - imposto

MargemLucro = lucro / faturamento

print('Faturamento foi de ', faturamento)
print('O custo foi de ' , custo)
print('O lucro foi de ' , lucro)
print('A margem de lucro foi de ' , round(MargemLucro , 2))

