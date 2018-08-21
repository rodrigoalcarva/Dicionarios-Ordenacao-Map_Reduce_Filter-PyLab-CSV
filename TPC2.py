# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Universidade de Lisboa
Faculdade de Ci�ncias
Departamento de Inform�tica
Licenciatura em Tecnologias da Informa��o 2016/2017

Programa��o II

Trabalho2

Sei que não era preciso testes, mas coloquei só para ter a certeza que estava a funcionar corretamente.
"""

__author__ = "Rodrigo Alcarva, 50011"
__email__ = "fc50011@alunos.fc.ul.pt"


def soma_raizes(n):
    """Uma função que recebe um número que vai ser o limite das raizes sumadas e assim
    vai somar todas as raizes de 1 a n+1.
    Requires: n > 0 e int.
    Ensures: Vai retornar o número total da soma de todas as raízes.
    
    >>> soma_raizes(4)
    6.146264369941973
    
    A complexidade algoritma vai ser: O(n), porque o reduce faz o mesmo de um for e é uma
    função de ordem superior.
    """
    
    soma = (reduce(lambda i,n: i + (n**(0.5)),range(0, n+1),0)) #O Reduce serve para executar alguma computação em uma lista e retornar o resultado. Assim vai somar as raizes de 0 a n+1, pondo cada resultado no acumulador. O mesmo podia ser feito com um sum(map()).
    return soma  



def lista_somas_raizes(n):
    """ Uma função que recebe um número que vai ser o limite das raízes e assim vai somar
    todas as raizes de 1 a n+1, esta vai colocar em cada posição de uma lista.
    Requires: n > 0 e int.
    Ensures: Retorna uma lista com a soma de raizes de 1 a n+1, sendo o primeiro elemento a primeira
    soma, o segundo elemento, a soma do primeiro com o segundo elemento e assim consecutivamente
    até n+1.
    
    >>> lista_somas_raizes(4)
    [1, 2.414213562373095, 4.146264369941973, 6.146264369941973]
    
    A complexidade algoritma vai ser: O(n^2) porque é tempo linear.
    Porque os valores na lista estão sempre a crescer, o que vai fazer um gráfico Linear.
    """
    
    listSoma = map(lambda n: soma_raizes(n), range(1,n+1)) # O Map vai pondo os resultados numa lista, a soma de cada passo, usando a função anterior.
    listSoma[0] = int(listSoma[0])
    return listSoma

def explora(function,lista, x):
    """ Esta função vai receber 3 argumentos, uma função, uma lista e um elemento. Que vai calcular
    os estados intermédios da soma de cada elemento da lista.
    Requires: len(lista) > 0 e x seja int.
    Ensures: Devolve todos os estados intermédios do acumulador na forma 
    de uma lista.
    
    >>> explora(lambda acc, x: acc + x, [3, 5, 2, 1], 0)
    [0, 3, 8, 10, 11]
    >>> explora(lambda acc, x: x - acc, [3, 5, 2, 1], 0)
    [0, 3, 2, 0, 1]
    >>> explora(lambda acc, x: x if x > acc else acc, [3, 4, 5, 3, 7, 9, 2, 1], 2)
    [2, 3, 4, 5, 5, 7, 9, 9, 9]
    
    A complexidade linear vai ser: O(n) porque ao ter um for vai percorrer cada elemento da lista.
    """
    
    listReturn = []
    listReturn.append(x)                        # Nesta linha vai colocar o primeiro elemento, já na lista.
    for elem in lista:                          # Vai percorrer cada elemento da lista 
        listReturn.append(function(x, elem))    # Vai fazer append das raizes de cada número.
        x = function(x, elem)                   # Esta linha vai ser a parte em que coloca em cada posição os passos intermédios          
    return listReturn


def lista_somas_raizes_explora(n):
    """ Esta função vai fazer o mesmo que a função lista_somas_raizes, mas em vez de utilizar
    a 1ª função, vai utilizae a 3ª função.
    Requires: n> 0 e que seja int.
    Ensures: Retorna uma lista com a soma de raizes de 1 a n+1, sendo o primeiro elemento a primeira
    soma, o segundo elemento, a soma do primeiro com o segundo elemento e assim consecutivamente
    até n.
    
    >>> lista_somas_raizes_explora(4)
    [1, 2.414213562373095, 4.146264369941973, 6.146264369941973]
    
    A complexidade algoritma vai ser: O(n) porque é tempo linear.
    Porque os valores na lista estão sempre a crescer, o que vai fazer um gráfico Linear.
    """
    
    listExplora = explora(lambda i,n: i + (n**(0.5)),range(2, n+1),1.0)  #Usando a função anterior vai fazer uma lista igual à segunda função mas sem utilizar o map.
    listExplora[0] = int(listExplora[0])
    return listExplora


if __name__ == "__main__":
    import doctest
    doctest.testmod()
