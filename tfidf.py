import os
import math

dictionary = []
frecuency = []
arrayTf = []
arrayPesado = []
arrayN = []
arrayIdf = []


def run():
    count = 0
    countN = 0
    countL = 0
    countS = 0
     
    f =  open("Preprocesamiento.txt", 'r')
    for line in f:
        for word in line.split():
            dictionary.append(word)
    
    uniqueWords = repeat(dictionary)
    print("\nPalabras sin repetir de los documentos: \n",uniqueWords, "\n")

    f =  open("Preprocesamiento.txt", 'r')
    for line in f:
        for u in uniqueWords:
            for word in line.split():
                if u == word:
                    count = count + 1
            frecuency.append(count)
            count = 0
    print("f: ", frecuency, "\n")

    #Calcular Tf
    for f in frecuency:
        if f != 0:
            log = calculateLog(f) + 1
        else:
            log = 0
        arrayTf.append(log)
    print("TF: ", arrayTf, "\n")

    #Calcular n
    f =  open("Preprocesamiento.txt", 'r')
    wordlist = f.read().splitlines()
    for u in uniqueWords:
        for line in wordlist:
            if u  in line:
                countN = countN + 1
        arrayN.append(countN)
        countN = 0
    print("n: ", arrayN, "\n")

    #Calcular IDF
    f =  open("Preprocesamiento.txt", 'r')
    for line in f:
        countL = countL + 1
    
    for n in arrayN:
        if n!=0:
            idf = calculateLog(countL/n)
        else:
            idf = 0   
        arrayIdf.append(idf)
    print("IDF: ", arrayIdf, "\n")

    cont = 1
    
    for i in range(1,countL+1):
        for idf in arrayIdf:
            for tf in arrayTf[0:i*len(arrayIdf)]:
                countS = countS + 1
                if countS == cont:
                    mult = tf * idf
                    arrayPesado.append(mult)
            countS = 0
            cont = cont + 1
        print("Array TF/IDF pesado : ",arrayPesado)


def calculateLog(x):
    return math.log(x, 2)
        

def repeat(x): 
    _size = len(x)
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] != x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return(repeated)

def calculateLog(x):
    return math.log(x, 2)


if __name__ == '__main__':
    run()
