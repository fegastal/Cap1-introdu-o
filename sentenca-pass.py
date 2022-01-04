'''A sentença pass
Eis um comando que não faz nada, mas é muito importante.
Suponha que no desenvolvimento de um programa você tenha uma instrução if, mas
ainda não definiu as instruções a serem realizadas caso ocorra este if:

if x > 1:
   ????

Se você não inserir nenhuma linha após o if, vai confundir o interpretador Python. Porém se você fizer o seguinte:

if x>1:
    pass

O programa irá executar corretamente.

Esta situação ocorre repetidamente quando estamos criando um novo método ou função, que ainda não foi implementado:

def minhaFuncao():
    pass

'''