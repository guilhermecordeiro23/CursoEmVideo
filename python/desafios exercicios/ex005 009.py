print('==========EXERCÍCIO 005==========')
#Faça um programa que leia um número inteiro e mostre
# na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
a = n-1
s = n+1
print('Analizando o número {}, seu antecessor é {} e seu sucessor é {}'.format( n, a, s))

# ou...pode ser usado somente com uma váriavel

'''#n = int(input('Digite um número: '))
#print('Analizando o número {}, seu antecessor é {} e seu sucessor é {}'.format( n,(n-1),(n+1)))
'''

print('==========EXERCÍCIO 006===========')
#Crie um algoritmo que leia um número e mostre o seu dobro,
# seu triplo e sua raíz quadrada.

nu = int(input('Digite um número: '))
do = nu*2
tri = nu*3
ra = nu** (1/2)
print('O valor {} tem o dobro de {},triplo de {} e raíz quadrada de {:.3f}'.format( nu, do, tri, ra))

# ou... pode ser usado somente com uma váriavel

'''#nu = int(input('Digite um número: '))
#print('O valor {} tem o dobro de {},triplo de {} e raíz quadrada de {:.3f}'.format( nu,(nu*2),(nu*3),(nu** (1/2))))
'''

print('==========EXERCÍCIO 007==========')
#Desenvolva um programa que leia as duas notas de um aluno,
# calcula e mostre a sua média.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('A média das notas {} e {} é de :{:.1f}.'.format( n1, n2, m ))
if m >= 6 :
    print('Parabéns, você passou!')
else:
    print('Faltou pouco, tente na proxima.')


print('===========EXERCÍCIO 008==========')
#Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.


metros = float(input('Digite seu valor em metros: '))
centi = metros * 100
milí = metros * 1000
print('Seu valor de {} metros, convertido é igual a:'.format( metros))
print('{} centímetros.'.format( centi))
print('{} milímetros.'.format( milí))


print('==========EXERCÍCIO 009==========')
#Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada.

num = int(input('Digite um valor para ver a sua tabuada: '))
print('-'*12)
print('{} X {} = {}'.format(num, 1, num*1))
print('{} X {} = {}'.format(num, 2, num*2))
print('{} X {} = {}'.format(num, 3, num*3))
print('{} X {} = {}'.format(num, 4, num*4))
print('{} X {} = {}'.format(num, 5, num*5))
print('{} X {} = {}'.format(num, 6, num*6))
print('{} X {} = {}'.format(num, 7, num*7))
print('{} X {} = {}'.format(num, 8, num*8))
print('{} X {} = {}'.format(num, 9, num*9))
print('{} X {} = {}'.format(num, 10, num*10))
print('-'*12)











      
