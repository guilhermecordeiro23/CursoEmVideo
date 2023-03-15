'''print('------------------------------EXERCÍCIO 016------------------------------')
#Crie um programa que leia um número Real qualquer pelo teclado e
#mostre na tela a sua porção inteira
# Ex: digite um número 6.147
# o número 6.147 tem a aprte inteira 6.

import math
num = float(input('Digite um número: '))
print('O número {} tem como parte inteira {}'.format(num, math.trunc(num)))

num = float(input('Digite um valor: '))
print('O número {} tem como parte inteira {}'.format(num, int(num)))


print('---------------------------EXERCÍCIO 017---------------------------------')
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hip = (co**2 + ca**2) **(1/2)
print('O valor da hipotenusa é de:{:.2f}'.format(hip))

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(co, ca)
print('O valor da hipotenusa é de: {:.2f}'.format(hip))

print('-----------------------------EXERCÍCIO 018--------------------------------')
#Faça um progrma que leia um ângulo qualquer e mostre na tela
#o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Coloque o valor de um ângulo qualquer: '))
seno = math.sin(math.radians(ang))
print('SENO = {:.2f}'.format(seno))
cos = math.cos(math.radians(ang))
print('COSSENO = {:.2f}'.format(cos))
tang = math.tan(math.radians(ang))
print('TANGENTE = {:.2f}'.format(tang))

print('---------------------------EXERCÍCIO 019---------------------------------')
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele, lendo onome deles e escolhendo o nome do escolhido.

from random import choice
a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

print('---------------------------EXERCÍCIO 020---------------------------------')
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
#trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre
#a ordem sorteada.

from random import shuffle
n1 = str(input('Nome do aluno: '))
n2 = str(input('Nome do aluno: '))
n3 = str(input('Nome do aluno: '))
n4 = str(input('Nome do aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
'''
print('--------------------------EXERCÍCIO 021----------------------------------')
#Faça um programa em Python que abra e reproduza o áudio de
#um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('nome do arquivo')
pygame.mixer.music.play()
pygame.event.wait()


















      
