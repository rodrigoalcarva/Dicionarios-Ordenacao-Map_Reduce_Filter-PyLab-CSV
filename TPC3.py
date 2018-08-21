# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação 2016/2017

Programação II

Trabalho3
"""

__author__ = "Rodrigo Alcarva, 50011"
__email__ = "fc50011@alunos.fc.ul.pt"

import csv
import pylab

def tremores(document_name,days):
    """ Esta funcão irá receber como parametros um fichiero csv e os dias, esta função
    irá ler o ficheiro que contem vários dados em que no 4 parametro estão os valores
    dos tremores de terra, assim esta função vai gerar um gráfico do tipo histograma
    com esses valores.
    Requires: um ficheiro do tipo csv.
    Ensures: Vai retornar um histograma de cor laranja com os valores do ficheiro csv.
    """
    tremors_values = []  
    zero = []                                               
    with open(document_name, 'rU') as document_csv:                 #Nesta linha vai-se abrir o ficheiro csv que contem os valores
        read = csv.reader(document_csv, delimiter = ',')            #Vai delimitar os valores por uma virgula
        read.next()                                                 # Para obter os sucessivos elementos no iterador.
        for line in read:       
            if line[4] == "":                                       
                zero.append("")
            else:
                tremors_values.append(float(line[4]))                               #Se o valor não estiver vazio vai fazer append desses valores para a lista
    lasClasses = (10 * (int(max(tremors_values)) - int(min(tremors_values))))       #Calcula-se o número de classes de modo a obtermos classes de dimensão 0,1
    pylab.xlabel("Magnitude")                                                       #Etiqueta das abcissas
    pylab.ylabel("Numero de tremores de terra")                                     #Etiqueta das ordenadas
    pylab.title("Magnitude dos tremores de terra (ultimos " + str(days) +" dias)")  #Titulo do gráfico
    pylab.hist(tremors_values ,lasClasses, facecolor = 'orange')                    #O gráfico vai ser um histograma que recebe a lista de valores, a classe e a cor do gráfico
    pylab.show()