# Crear funcion Python (inicio)                      Ej: def Daniel(a, b):

import re


expresion = r'((FUNCION)[ ]+((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER)|(VACIO))[ ]+([a-zA-Z]+[a-zA-Z0-9_]*)([(][ ]*(((ENTERO)|(REAL)|(BOOLEAN)|(CARACTER)|(VACIO))[ ]+([a-zA-Z]+[a-zA-Z0-9_]*))*([,][ ]((ENTERO)|(REAL)|(BOOLEAN)|(CARACTER)|(VACIO))[ ]([a-zA-Z]+[a-zA-Z0-9_]*))*[ ][)]))'  # expresión regular que valida el pseudocódigo hasta el inicio de la función y antes de entrar al cuerpo de esta.
mod_acceso1 = ""
#error = ''
#leng = ''

def general(cadena,leng):
    def CrearFuncionInicio(cadena):  # En esta función, el nombre de la función no puede empezar por ninguna palabra en mayuscula que aparezca en la lista 'tipo_dato'
        error = False
        cadena_split = cadena.split()  # La cadena que recibimos (pseudocódigo), la dividimos en varias partes.
        resultado1 = ""  # Variable donde vamos a guardar nuestro resultado (la traducción)
        if (re.search(expresion, cadena)):  # Validamos que la cadena es aceptada por la expresión regular
            if (cadena_split[0] == "FUNCION"):  # Verificamos que el pseudocódigo tenga la palabra reservada FUNCION
                cadena_split[0] = "def"  # Hacemos el remplazo de la palabra 'FUNCION' por 'def'
                if (re.search('ENTERO', cadena_split[2])):
                    error = True
                elif (re.search('REAL', cadena_split[2])):
                    error = True
                elif (re.search('BOOLEANO', cadena_split[2])):
                    error = True
                elif (re.search('CARACTER', cadena_split[2])):
                    error = True
                elif (re.search('VACIO', cadena_split[2])):
                    error = True
            if (error == False):
                for n in cadena_split:
                    posicion = cadena_split.index(n)
                    if (re.search('ENTERO', n)):
                        cadena_split[posicion] = ''
                    if (re.search('REAL', n)):
                        cadena_split[posicion] = ''
                    if (re.search('BOOLEANO', n)):
                        cadena_split[posicion] = ''
                    if (re.search('CARACTER', n)):
                        cadena_split[posicion] = ''
                    if (re.search('VACIO', n)):
                        cadena_split[posicion] = ''

                resultado2 = ' '.join(cadena_split)
                return resultado2

            else:
                return "syntax error"
        else:
            return "syntax error"
        return error
#---------------------------------------------------------------------------------------
    def CrearFuncionInicioJava(cadena):
        error = False
        cadena_split = cadena.split()
        resultado2 = ""
        if (re.search(expresion, cadena)):  # If 1
            if (cadena_split[0] == "FUNCION"):
                cadena_split[0] = "Public"
                # -------------------------------------
                if (re.search('ENTERO', cadena_split[2])):
                    error = True
                elif (re.search('REAL', cadena_split[2])):
                    error = True
                elif (re.search('BOOLEANO', cadena_split[2])):
                    error = True
                elif (re.search('CARACTER', cadena_split[2])):
                    error = True
                elif (re.search('VACIO', cadena_split[2])):
                    error = True
                    # -------------------------------------------
            if (error == False):
                for n in cadena_split:
                    posicion = cadena_split.index(n)
                    if (re.search('ENTERO', n)):
                        cadena_split[posicion] = 'int'
                    if (re.search('REAL', n)):
                        cadena_split[posicion] = 'float'
                    if (re.search('BOOLEANO', n)):
                        cadena_split[posicion] = 'boolean'
                    if (re.search('CARACTER', n)):
                        cadena_split[posicion] = 'char'
                    if (re.search('VACIO', n)):
                        cadena_split[posicion] = 'void'
                    if (re.search('[)]',n)):
                        cadena_split[posicion] = '){'
                resultado2 = ' '.join(cadena_split)
                return resultado2

            else:
                return "syntax error"
        else:  # else del if 1
            return "syntax error"
#----------------------------------------------------------------------------------------
    def CrearFuncionInicioC(cadena):
        error = False
        cadena_split = cadena.split()
        resultado2 = ""
        if (re.search(expresion, cadena)):  # If 1
            if (cadena_split[0] == "FUNCION"):
                cadena_split[0] = ''
                # -------------------------------------
                if (re.search('ENTERO', cadena_split[2])):
                    error = True
                elif (re.search('REAL', cadena_split[2])):
                    error = True
                elif (re.search('BOOLEANO', cadena_split[2])):
                    error = True
                elif (re.search('CARACTER', cadena_split[2])):
                    error = True
                elif (re.search('VACIO', cadena_split[2])):
                    error = True
                    # -------------------------------------------
            if (error == False):
                for n in cadena_split:
                    posicion = cadena_split.index(n)
                    if (re.search('ENTERO', n)):
                        cadena_split[posicion] = 'int'
                    if (re.search('REAL', n)):
                        cadena_split[posicion] = 'float'
                    if (re.search('BOOLEANO', n)):
                        cadena_split[posicion] = 'boolean'
                    if (re.search('CARACTER', n)):
                        cadena_split[posicion] = 'char'
                    if (re.search('VACIO', n)):
                        cadena_split[posicion] = 'void'
                resultado2 = ' '.join(cadena_split)
                return resultado2

            else:
                return "syntax error"
        else:  # else del if 1
            return "syntax error"

    if(leng == 1):
        return CrearFuncionInicio(cadena)
    elif(leng == 2):
        return CrearFuncionInicioJava(cadena)
    elif(leng == 3):
        return CrearFuncionInicioC(cadena)




