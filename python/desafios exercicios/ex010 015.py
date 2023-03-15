print('==========EXERCÍCIO 010==========')
#Crie um programa que leia quanto uma pessoa tem na
#carteira e mostre quantos Dólares ela pode comprar.
#Considere USS1,00 = R$4,70

valorR = float(input('Digite quanto de dinheiro você tem na carteira: R$ '))
valorD = valorR / 4.70
print('Com R$:{:.2f} você pode comprar US:{:.2f}'.format( valorR, valorD ))

print('==========EXERCÍCIO 011==========')
#Crie um programa que leia alargura e a altura de uma parede
#em metros, calcule suaárea e a quantidade de tinta necessária
#para pintá-la, sabendo que cada litro de tinta, pinta uma área de
# 2m².

larg = float(input('Quanto de largura sua parede tem?: '))
alt = float(input('Quanto de altura sua parede tem?: '))
área = larg*alt
print('Sua parede tem as dimensões de {} X {} e uma área de {}m²'.format( larg, alt, área))
tinta = área / 2
print('Será necessario {} litros de tinta para sua parede'.format( tinta))

print('==========EXERCÍCIO 012==========')
#Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

prod = float(input('Qual o preço do seu produto? R$: '))
desc = prod - (prod * 5 / 100)
print('Seu produto de R$:{:.2f}, com 5% de desconto fica de R$:{:.2f}'.format( prod, desc ))

print('==========EXERCÍCIO 013==========')
#Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de desconto.

sala = float(input('Qual o valor do seu salário? R$: '))
novo = sala + (sala * 15 / 100)
print('Seu novo salário será de R$:{}'.format( novo ))

print('==========EXERCÍCIO 014==========')
#Escreva um programa que converta uma temperatura de ºC
# para ºF.

c = float(input('Temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC,corresponde a {}ºF'.format( c, f ))

print('==========EXERCÍCIO 015==========')
#Escreva um programa que pergunte a quantidade de Km percorrido
# por um carro alugado e a quantidade de dias pelo quais ele foi
# alugado. Calcule o preço a pagar, sabendo queo carro custa
# R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram percorridos? '))
valor = (dias*60) + (km*0.15)
print('Seu total a pagar é de R${:.2f}'.format( valor ))

