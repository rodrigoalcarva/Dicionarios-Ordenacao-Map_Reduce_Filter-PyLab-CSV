# -*-coding:utf-8-*-
#!/usr/bin/env python

"""
Trabalho 4

Programa Erasmus

Contem 4 funcoes

Programacao II
"""

__author__= "Alexandre Nascimento, 50002 e Rodrigo Alcarva, "
__maintainer__ = "Alexandre Nascimento e Rodrigo Alcarva"
__email__ = "fc50002@alunos.fc.ul.pt"

import pylab
import csv

def acumula(lista_dicionarios, chave_pesquisa):
    """
    Requires: A chave_pesquisa ocorre em todos os dicionarios constantes na lista_dicionarios.
    Ensures: Devolve um dicionario onde a) as varias chaves sao os valores associados a chave_pesquisa na lista_dicionarios e 
    b) os valores do resultado  sao o numero de vezes que as chaves do resultado ocorrem na lista_dicionarios.
    
    #Caracteristicas:
    #1. Lista vazia (T/F) ?
    #2  len lista (1,1>) ?
    #3  Dicionario ordenado (T/F) ?
    #4  Caracteres da string (0,1)?

    >>> acumula ([{'x': 'a', 'y': 23}], 'x') == {'a': 1}    #(F,1,T,0)
    True
    >>> acumula ([{'xa': 'a', 'y': 23}], 'xa') == {'a': 1}    #(F,1,T,1)
    True
    >>> acumula ([{'x': 'a', 'y': 23}, {'x': 'b', 'y': 78}, {'x': 'a', 'y': 99}], 'x') == {'a': 2, 'b': 1}    #(F,1>,T,0)
    True
    >>> acumula ([{'xe': 'a', 'y': 23}, {'xe': 'b', 'y': 78}, {'xe': 'a', 'y': 99}], 'xe') == {'a': 2, 'b': 1}    #(F,1>,T,1)
    True
    >>> acumula ([{'r': 'a', 'c': 23}], 'r') == {'a': 1}    #(F,1,F,0)
    True
    >>> acumula ([{'ri': 'a', 'c': 23}], 'ri') == {'a': 1}    #(F,1,F,1)
    True
    >>> acumula ([{'r': 'a', 'c': 23},{'r': 'a', 'c': 23}], 'r') == {'a': 2}    #(F,1,F,0)
    True
    >>> acumula ([{'ro': 'a', 'c': 23},{'ro': 'a', 'c': 23}], 'ro') == {'a': 2}    #(F,1,F,1)
    True
    >>> l = [{'x': 'a', 'y': 23}, {'x': 'b', 'y': 78}, {'x': 'a', 'y': 99}]
    >>> acumula (l, 'x') == {'a': 2, 'b': 1}
    True
    """
    acumulaDict = {}
    for elDict in lista_dicionarios:
        if elDict[chave_pesquisa] not in acumulaDict:
            acumulaDict[elDict[chave_pesquisa]] = 1
        else:
            acumulaDict[elDict[chave_pesquisa]] += 1
    return acumulaDict


def soma (lista_dicionarios, chave_pesquisa, chave_soma):
    """
    Requires: A chave_pesquisa e a chave_soma ocorrem em todos os dicionarios constantes na lista_dicionarios. 
    O valor associado a  chave_soma a um numero.
    Ensures: Devolve um dicionario onde a) as varias chaves sao os valores associados a chave_pesquisa na lista_dicionarios e 
    b) os valores do resultado sao obtidos pela soma dos valores associados Ã  chave_pesquisa na lista_dicionarios.
    
    #Caracteristicas:
    #1. Lista vazia (T/F) ?
    #2  len lista (1,1>) ?
    #3  valores (1, 1>) ?

    >>> soma ([{'x': 'a', 'y': 23}], 'x','y') == {'a': 23} #(F,1,1)
    True
    >>> soma ([{'x': 'a', 'y': 23},{'x': 'a', 'y': 23}], 'x','y') == {'a': 46} #(F,1>,1)
    True
    >>> soma ([{'x': 'a', 'y': 23},{'x': 'b', 'y': 23},{'x': 'b', 'y': 78}], 'x','y') == {'a': 23, 'b': 101}  #(F,1>,1>)
    True
    >>> l = [{'x': 'a', 'y': 23}, {'x': 'b', 'y': 78}, {'x': 'a', 'y': 99}]
    >>> soma (l, 'x', 'y') == {'a': 122, 'b': 78}
    True
    """
    somaDict = {}
    for elDict in lista_dicionarios:
        if elDict[chave_soma] != '':
            if elDict[chave_pesquisa] not in somaDict:
                somaDict[elDict[chave_pesquisa]] = int(elDict[chave_soma])
            else:
                somaDict[elDict[chave_pesquisa]] += int(elDict[chave_soma])
    return somaDict

def sortList(dicti, maxi):
    """
    Esta função recebe 2 argumentos, um dicionario e um valor, vai ordenar uma lista decrescentemente, do valor maior até ao valor maxi.
    Requires: uma lista e um valor int do maxi-
    Ensures: Irá ordenar a lista do maior para o menor.

    """
    
    listSort = sorted(dicti.items(), key=lambda elem: elem[1], reverse=True)
    listSort = listSort[:maxi]
    
    numList = []
    countriesList = [] 
     
    for n in listSort:
        numList.append(n[1])
        countriesList.append(n[0])
        
    return [numList, countriesList]


def erasmus(erasmus_csv, paises_csv, max_paises_por_grafico):
    """
    Esta função tem 3 argumentos, 2 deles são dois ficheiros csv, que contêm a informação toda para os grádicos, o outro argumento é o
    número máximo de países em cada gráfico. Esta função vai servir para ler os ficheiros recebidos e ir às linhas certas buscar a
    informação.
    Requires: Ficheiros do tipo csv com informção sobre erasmus e outra de países, e um valor int do valor máximo de países.
    Ensures: Uma lista com a vária informção para os gráficos e outra lista com os países.

    """
    erasmusList = []
    with open(erasmus_csv, 'rU') as ficheiro_erasmus:
        reader = csv.reader(ficheiro_erasmus, delimiter = ';')
        reader.next()
        for line in reader:
            personDict = {}
            
            if len(line[3]) == 0 or line[3] == "???":
                line[3] = "LU"
                
            if len(line[25]) == 0 or line[25] == "???":
                line[25] = 750
                
            if len(line[28]) == 0 or line[28] == "???":
                line[28] = "DE"
                
            if len(line[3]) == 4:
                line[3] = line[3][:2]
                 
            personDict["HOME_INSTITUTION_CTRY_CDE"] = line[3].upper()
            personDict["TOTAL_ECTS_CREDITS_AMT"] = line[25]
            personDict["LANGUAGE_TAUGHT_CDE"] = line[28].upper()
            personDict["STUDY_START_DATE"] = line[20]
            
            erasmusList.append(personDict)
            
    countries = []
    
    with open(paises_csv, 'rU') as ficheiro_paises:
        reader = csv.reader(ficheiro_paises, delimiter = ';')
        reader.next()
        for line in reader:
            counDict = {}
            
            if  line[3].upper() == "GB":
                line[3] = "UK"
            
            counDict["Country code"] = line[3].upper()
            counDict["Population"] = int(line[6])
            
            countries.append(counDict)
    
    makeGraph(erasmusList, countries, max_paises_por_grafico)
            

def makeGraph(erasmusList, countries,max_paises_por_grafico):
    """
    Esta função tem 3 argumentos, dois deles são duas listas que vêem da função erasmus, e outra é o número máximo de países.
    Esta função serve para dar origem aos 4 gráficos, todos na mesma janela.
    Requires: Duas listas de valor não nulo, e um int do número máixmo de países.
    Ensures: Origem a 4 gráficos, todos na mesma janela, de cor laranja, 2 por 2.
    """
    studentsNum = acumula(erasmusList, "HOME_INSTITUTION_CTRY_CDE")

    studentsList = sortList(studentsNum, max_paises_por_grafico)
    
    pylab.subplot(2,2,1)
    pylab.bar(range(len(studentsList[1])),studentsList[0], 1/1.35, color="orange")
    pylab.xticks(range(len(studentsList[1])), studentsList[1])
    pylab.xlabel('Paises')
    pylab.ylabel('Numero de Intercambios')
    pylab.title('Distribuicao dos estudantes Erasmus em intercambio')    
     
    perMilionNum = {}
    
    for el in countries:
        if el['Country code'] in studentsNum:
            perMilionNum[el['Country code']] = studentsNum[el['Country code']]/(el['Population']/1000000.0)
            
    milionList = sortList(perMilionNum, max_paises_por_grafico)
  
    pylab.subplot(2,2,2)
    pylab.bar(range(len(milionList[1])),milionList[0], 1/1.35, color="orange")
    pylab.xticks(range(len(milionList[1])), milionList[1])
    pylab.xlabel('Paises')
    pylab.ylabel('Intercambios / milhao habitantes')
    pylab.title('Estudantes Erasmus por milhao de habitantes')
    

    langNum = acumula(erasmusList, "LANGUAGE_TAUGHT_CDE")
    
    langList = sortList(langNum, max_paises_por_grafico)
    
    pylab.subplot(2,2,3)
    pylab.bar(range(len(langList[1])),langList[0], 1/1.35, color="orange")
    pylab.xticks(range(len(langList[1])), langList[1])
    pylab.xlabel('Lingua')
    pylab.ylabel('Numero de Intercambios')
    pylab.title('Linguas utilizadas nos intercambios')
 
    ectNum = soma(erasmusList, 'HOME_INSTITUTION_CTRY_CDE', 'TOTAL_ECTS_CREDITS_AMT')
    
    for el in ectNum:
        ectNum[el] = (ectNum[el]/studentsNum[el])
        
    ectList = sortList(ectNum, max_paises_por_grafico)
    
    pylab.subplot(2,2,4)
    pylab.bar(range(len(ectList[1])),ectList[0], 1/1.35, color="orange")
    pylab.xticks(range(len(ectList[1])), ectList[1])
    pylab.xlabel('Paises')
    pylab.ylabel('Numero medio de ECTS')
    pylab.title('Numero medio de ECTS obtidos')
    
    inDate = int(erasmusList[0]["STUDY_START_DATE"][-2:])
    pylab.suptitle("Algumas estatisticas sobre o programa Erasmus para o ano de 20" + str(inDate) + "-20" + str(inDate + 1))
    pylab.show()

if __name__ == "__main__":
    import doctest
    doctest.testmod()