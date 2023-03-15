nome = str(input('Qual o seu nome?:'))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te comhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
so = n1+n2
div = n1/n2
sub = n1-n2
divint = n1//n2
exp = n1**n2
print('A soma é de {}, a divisão é {:.2f}, a subtração é {}.'.format(so, div, sub), end='>>>>>> ')
print('A divisão inteira é {} e a potência é {}.'.format(divint, exp))

# ( end='') == não ter quebra de linha
# ( \n ) == nova quebra de linha
''' operadores algébricos
+ == soma
- == subtração
* == multiplicação
/ == divisão
** == potência
// == divisão inteira
% == resto da divisão'''


