# Crear funcion Python (inicio)                      Ej: def Daniel(a, b):

import re



exp_java = r'((FUNCION)[ ]+((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER)|(VACIO))([ ]([\[])[a-zA-Z0-9_]*[\]])*[ ]+([a-zA-Z]+[a-zA-Z0-9_]*)([(][ ]*(((ENTERO)|(REAL)|(BOOLEAN)|(CARACTER)|(VACIO))[ ]+([a-zA-Z]+[a-zA-Z0-9_]*)([ ]([\[])[\]])*)*([,][ ]((ENTERO)|(REAL)|(BOOLEAN)|(CARACTER)|(VACIO))*[ ]([a-zA-Z]+[a-zA-Z0-9_]*)([ ]([\[])[\]])*)*[ ][)]))'

expresion = r'((FUNCION)[ ]+((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER)|(VACIO))([ ]([\[])[a-zA-Z0-9_]*[\]])*[ ]+([a-zA-Z]+[a-zA-Z0-9_]*)([(][ ]*(((ENTERO)|(REAL)|(BOOLEAN)|(CARACTER)|(VACIO))[ ]+([a-zA-Z]+[a-zA-Z0-9_]*)([ ]([\[])[a-zA-Z0-9_]*[\]])*)*([,][ ]((ENTERO)|(REAL)|(BOOLEAN)|(CARACTER)|(VACIO))*[ ]([a-zA-Z]+[a-zA-Z0-9_]*)([ ]([\[])[a-zA-Z0-9_]*[\]])*)*[ ][)]))'
mod_acceso1 = ""

def general(cadena,leng, pos):
    final = [True, []]
    def CrearFuncionInicio(cadena, pos):
        n_tab = cadena.count('\t')
        error = False
        cadena_split = cadena.split()
        if(cadena_split[0] == "FUNCION"):
            if (re.search(expresion, cadena)):
                if (cadena_split[0] == "FUNCION"):
                    cadena_split[0] = "def"
                    if (re.match('ENTERO\(', cadena_split[2]) or re.match('REAL\(', cadena_split[2]) or re.match('BOOLEANO\(', cadena_split[2]) or re.match('CARACTER\(', cadena_split[2]) or re.match('VACIO\(', cadena_split[2])):
                        final[0] = False
                        final[1] = ["Error en declaracion de funcion", pos+1]
                        return final
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
                        if (re.search('[)]',n)):
                            cadena_split[posicion] = '):'
                        if (re.search('\[',n)):
                            cadena_split[posicion] = ''
                        if (re.search('],',n)):
                            cadena_split[posicion] = ','
                    resultado2 = ' '.join(cadena_split)
                    resultado2 = (n_tab * '\t') + resultado2
                    return resultado2
            else:
                final[0] = False
                final[1] = ["Error en declaracion de funcion", pos+1]
                return final
                
            
        else:
            return "syntax error"
        #return error
#---------------------------------------------------------------------------------------
    def CrearFuncionInicioJava(cadena, pos):
        error = False
        cadena_split = cadena.split()
        if(cadena_split[0] == "FUNCION"):
            if (re.search(exp_java, cadena)):  # If 1
                if (cadena_split[0] == "FUNCION"):
                    cadena_split[0] = "static"
                    # -------------------------------------
                if (re.match('ENTERO\(', cadena_split[2]) or re.match('REAL\(', cadena_split[2]) or re.match('BOOLEANO\(', cadena_split[2]) or re.match('CARACTER\(', cadena_split[2]) or re.match('VACIO\(', cadena_split[2])):
                        final[0] = False
                        final[1] = ["Error en declaracion de funcion", pos+1]
                        return final
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
                final[0] = False
                final[1] = ["Error en declaracion de funcion", pos+1]
                return final
        else:  # else del if 1
            return "syntax error"
#----------------------------------------------------------------------------------------
    def CrearFuncionInicioC(cadena, pos):
        error = False
        cadena_split = cadena.split()
        if(cadena_split[0] == "FUNCION"):
            if (re.search(expresion, cadena)):  # If 1
                if (cadena_split[0] == "FUNCION"):
                    cadena_split[0] = ''
                    # -------------------------------------
                    if (re.match('ENTERO\(', cadena_split[2]) or re.match('REAL\(', cadena_split[2]) or re.match('BOOLEANO\(', cadena_split[2]) or re.match('CARACTER\(', cadena_split[2]) or re.match('VACIO\(', cadena_split[2])):
                        final[0] = False
                        final[1] = ["Error en declaracion de funcion", pos+1]
                        return final
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
                final[0] = False
                final[1] = ["Error en declaracion de funcion", pos+1]
                return final
        else:  # else del if 1
            return "syntax error"

    if(leng == 1):
        return CrearFuncionInicio(cadena, pos)
    elif(leng == 2):
        return CrearFuncionInicioJava(cadena, pos)
    elif(leng == 3):
        return CrearFuncionInicioC(cadena, pos)




