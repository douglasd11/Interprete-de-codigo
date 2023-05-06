import re

expresion = r'((RETORNA)[ ]+)(([a-zA-Z]+[a-zA-Z0-9_]*)|([0-9]+))'

def CrearFuncionFinal(cadena,leng, pos, m):
    #final = []
    final = [True, []]
    def CrearFuncionFinalPython(cadena, pos, m):
        n_tab = cadena.count('\t')
        error = False
        cadena_split = cadena.split()
        if(cadena_split[0] == "RETORNA"):

            if (re.search(expresion, cadena)):
                if (re.match('ENTERO', cadena_split[1]) or re.match('REAL', cadena_split[1]) or re.match('BOOLEANO', cadena_split[1]) or re.match('CARACTER', cadena_split[1]) or re.match('VACIO', cadena_split[1])):
                        final[0] = False
                        final[1] = ["Error en el retorno", pos+1]
                        return final
                
                if(error == False):
                    for n in cadena_split:
                        posicion = cadena_split.index(n)
                        if (re.search('RETORNA', n)):
                            cadena_split[posicion] = 'return'
                    resultado3 = ' '.join(cadena_split)
                    resultado3 = (n_tab * '\t') + resultado3
                    return resultado3
            else:
                final[0] = False
                final[1] = ["Error en el retorno", pos+1]
                return final
        else:
            return "syntax error"



#---------------------------------------------------------------------------------------
    def CrearFuncionFinalJava(cadena, pos, m):  #---- ojo aqui
        error = False
        x =0
        resultado3 = ''
        cadena_split = cadena.split()
        if(cadena_split[0] == "RETORNA"):
            if(m==1):
                final[0] = False
                final[1] = ["Funcion tipo void no debe retornar", pos + 1]
                return final
            if (re.match(expresion, cadena)):
                if (re.search('ENTERO', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('REAL', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('BOOLEANO', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('CARACTER', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('VACIO', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                if (error == False):
                    for n in cadena_split:
                        posicion = cadena_split.index(n)
                        if (re.search('RETORNA', n)):
                            cadena_split[posicion] = 'return'
                            x =1
                            resultado3 = ' '.join(cadena_split) + ';'


                    if(x == 1):

                        return resultado3
            else:
                final[0] = False
                final[1] = ["Error en el retorno", pos+1]
                return final
        else:
            return "syntax error"

#----------------------------------------------------------------------------------------
    def CrearFuncionFinalC(cadena, pos, m):
        error = False
        resultado3 = ''
        x= 0
        cadena_split = cadena.split()
        if(cadena_split[0] == "RETORNA"):
            if(m==1):
                final[0] = False
                final[1] = ["Funcion tipo void no debe retornar", pos + 1]
                return final
            if (re.match(expresion, cadena)):
                if (re.search('ENTERO', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('REAL', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('BOOLEANO', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('CARACTER', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('VACIO', cadena_split[1])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final

                if (error == False):
                    for n in cadena_split:
                        posicion = cadena_split.index(n)
                        if (re.search('RETORNA', n)):
                            cadena_split[posicion] = 'return'
                            x = 1
                            resultado3 = ' '.join(cadena_split) + ';'

                    if(x ==1):
                        return resultado3
            else:
                final[0] = False
                final[1] = ["Error en el retorno", pos+1]
                return final
        else:
            return "syntax error"

    if(leng == 1):
        return CrearFuncionFinalPython(cadena, pos, m)
    elif(leng == 2):
        return CrearFuncionFinalJava(cadena, pos, m)
    elif(leng == 3):
        return CrearFuncionFinalC(cadena, pos, m)
