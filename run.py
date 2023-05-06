from llamado import *
from CrearFuncion import *
from retorno import *
from recursividad import *
from tabulacion import *

resultado = []

copia = ['FUNCION ENTERO suma( ENTERO A [2] [], REAL C [] )', 'Aa', 'RETORNA C', 'FINF']
leng = 1


def C_Java(copia, leng):
    memi = 0
    lista_aux = copia
    traduccion = []
    cont = 0
    if (leng == 1):
        lista_aux = tab(copia)

    for x in lista_aux:
        num = lista_aux.index(x)
        prob = x.split()
        #print(prob)
        if (x == ''):
            pass
        elif (len(prob) > 0):
            if (prob[0] == "FUNCION"):
                if (general(x, leng, num) != "syntax error"):
                    if (prob[1] == "VACIO"):
                        memi = 1
                    traduccion.append(general(x, leng, num))
                    cont = cont + 1
            elif (x == "FINF"):
                if (leng == 2 or leng == 3):
                    traduccion.append("}//")
                else:
                    cont = cont + 1  # Qué hace el contador?
            elif (CrearFuncionFinal(x, leng, num, memi) != "syntax error"):
                traduccion.append(CrearFuncionFinal(x, leng, num, memi))
                cont = cont + 1
            elif (recursividad(x, leng, num, memi) != "syntax error"):
                traduccion.append(recursividad(x, leng, num, memi))
                cont = cont + 1


            elif (llamado(x, leng, num) != "syntax error"):
                traduccion.append(llamado(x, leng, num))
                cont = cont + 1

            else:
                traduccion.append(x)
                cont = cont + 1

    return traduccion


# --------------------------------------------------------------------------------


def pyton(copia, leng):
    lista = C_Java(copia, leng)
    lista_py = []
    #for x in lista:
        #cadena = x.replace("FINF", "")
        #lista_py.append(cadena)

    return lista


def run(copia, leng):
    lista_final = []
    if (leng == 1):
        lista_final = pyton(copia, leng)
    else:
        lista_final = C_Java(copia, leng)

    return lista_final


# print(C_Java(copia, leng))
print(run(copia, leng))
numero = run(copia, leng)

for c in numero:
    if (len(c) == 2 and c[0] == False):
        print(c)

