#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação 2016/2017

Programação II

Trabalho1

"""

__author__ = "Rodrigo Alcarva, 50011"
__email__ = "fc50011@alunos.fc.ul.pt"

#Caracteristicas:
# 1. Dicionario vazio ? (T/F)
# 2. Caracteres da String (0,1,1>)
# 3. String estar no dicionario ? (T/F)
# 4. Dicionario estar ordenado ? (T/F)

def subdicionario(dicionario, palavra):
    """Uma função que recebe um dicionario e uma string, em que compara
    a key do dicionario com a string e verifica se corresponde ou nao, se
    corresponder vai para um sub-dicionario.
    Requires: Dicionario com keys e values, uma string de qualquer tamanho.
    Ensures: Devolve um dicionario são com as keys que tem a string dada.
    >>> subdicionario({},"") #(T,0,F,F)
    {}
    >>> subdicionario({},"m") #(T,1,F,F)
    {}
    >>> subdicionario({},"ma") #(T,1>,F,F)
    {}
    >>> subdicionario({'abilio': 123,'ana': 987,'leonor': 567,'pai': 468},"")=={'pai': 468, 'abilio': 123, 'ana': 987, 'leonor': 567} #(F,0,T,T)
    True
    >>> subdicionario({'sandra': 123,'leonor': 987,'ana': 567,'pai': 468},"")=={'sandra': 123,'leonor': 987,'ana': 567,'pai': 468} #(F,0,T,F)
    True
    >>> subdicionario({'abilio': 123,'ana': 987,'laura': 567,'leonor': 468},"l")=={'laura': 567,'leonor': 468} #(F,1,T,T)
    True
    >>> subdicionario({'tiago': 123,'edu': 987,'francisco': 567,'mae': 468},"t")=={'tiago': 123} #(F,1,T,F)
    True
    >>> subdicionario({'abilio': 123,'ana': 987,'leonor': 567,'pai': 468},"y")=={} #(F,1,F,T)
    True
    >>> subdicionario({'tiago': 123,'edu': 987,'francisco': 567,'mae': 468},"p")=={} #(F,1,F,F)
    True
    >>> subdicionario({'abilio': 123,'ana': 987,'maria': 567,'margarida': 468},"ma")=={'maria': 567, 'margarida': 468} #(F,1>,T,T)
    True
    >>> subdicionario({'tiago': 123,'edu': 987,'francisco': 567,'mae': 468},"edu")=={'edu': 987} #(F,1>,T,F)
    True
    >>> subdicionario({'abilio': 123,'ana': 987,'maria': 567,'margarida': 468},"ap")=={} #(F,1>,F,T)
    True
    >>> subdicionario({'tiago': 123,'gonÃ§alo': 987,'francisca': 567,'monica': 468},"rod")=={} #(F,1>,F,F)
    True
    """
    
    dicNew={}                                                                           # Criar o subdicionario
    for elem in dicionario:                                                             # Vai ver em cada key do dicionario        
        if len(palavra) > 0:          
            if elem[:len(palavra)] == palavra:                                          #Se a a palavra tiver palavra for igual aos n caracteres na key
                dicNew[elem] = dicionario[elem]                                         #Essa key irá para o subdicionario 
        else:                                                                           #Se não houver palavra retorna o dicionario
            return dicionario
    return dicNew

#Caracteristicas
# 1.0 dicionario está vazio ? (T/F)
# 2.O dicionario está ordenado ? (T/F)

def pares_ordenados(dicionario):
    """Esta função recebe como parametro um dicionario estando ele ordenado ou não, se nao tiver ordenado
    esta função ira ordena-lo de forma alfabetica.
    Requires: Um dicionario com keys e values.
    Ensures: Devolve um dicionario ordenado.
    >>> pares_ordenados({})==[] #(T/F)
    True
    >>> pares_ordenados({'mafalda': 12,'margarida': 14,'maria': 17}) #(F/T)
    [('mafalda', 12), ('margarida', 14), ('maria', 17)]
    >>> pares_ordenados({'ana': 10,'ambrosio': 123,'afonso': 97,'anabela': 21}) #(F/F)
    [('afonso', 97), ('ambrosio', 123), ('ana', 10), ('anabela', 21)]
    """
    
    l =[]
    for elem in dicionario:
            l.append((elem,dicionario[elem]))
    return sorted(l)
    
    
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
