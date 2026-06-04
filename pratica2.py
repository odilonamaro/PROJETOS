#calculadora de desconto para delivery

valor = float(input("Digite um valor: "))

desconto_1 = 10
desconto_2 = 20
sem_desconto = 0

if valor > 100:
    desconto = desconto_2
elif valor >= 50:
    desconto = desconto_1
else:
    desconto = sem_desconto
valor_com_desconto = valor - (valor * desconto / 100)
print(f"Valor original: R${valor:.2f}")
print(f"Desconto aplicado: {desconto}%")
