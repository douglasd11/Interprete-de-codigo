#Crear funcion Python (final con recursividad)     
from llamado import *
import re




expresion = r'((RETORNA)[ ]*)([a-zA-Z]+[a-zA-Z0-9_]*)[(][ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)*([,][ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*))*[ ]*[)]'

def recursividad(cadena, leng, pos, m):
    final = [True, []]
    def recursividadPython(cadena, pos, m):
        x=0
        n_tab = cadena.count('\t')
        error = False
        cadena_split = cadena.split()
        if(cadena_split[0] == "RETORNA"):

            if (re.search(expresion, cadena)):
                if (re.match('ENTERO\(', cadena_split[1]) or re.match('REAL\(', cadena_split[1]) or re.match('BOOLEANO\(', cadena_split[1]) or re.match('CARACTER\(', cadena_split[1]) or re.match('VACIO\(', cadena_split[1])):
                        final[0] = False
                        final[1] = ["Error en el retorno", pos+1]
                        return final
                if (error == False):
                    for n in cadena_split:
                        if (re.search('RETORNA', n)):
                            posicion = cadena_split.index(n)
                            x=1
                            cadena_split[posicion] = 'return'
                            resultado3 = ' '.join(cadena_split)
                            resultado3 = (n_tab * '\t') + resultado3
                        else:
                            return "syntax error"
                            # print(resultado3)
                        if(x == 1):
                            return resultado3
                            
            else:
                final[0] = False
                final[1] = ["Error en el retorno", pos+1]
                return final
        else:
            return "syntax error"



    # ---------------------------------------------------------------------------------------
    def recursividadJava(cadena, pos, m):
        x=0
        error = False
        cadena_split = cadena.split()
        if(cadena_split[0] == "RETORNA"):
            if(m==1):
                final[0] = False
                final[1] = ["Función tipo void no debe retornar", pos + 1]
                return final
            if (re.search(expresion, cadena)):
                if (re.search('ENTERO', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('REAL', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('BOOLEANO', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('CARACTER', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('VACIO', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final

                if (error == False):
                    for n in cadena_split:
                        posicion = cadena_split.index(n)
                        if(re.search('RETORNA',n)):
                            cadena_split[posicion] = 'return'
                            x = 1
                            resultado3 = ' '.join(cadena_split) + ';'
                        else:
                            return "syntax error"
                    # print(resultado3)
                        if(x == 1):
                            return resultado3
            else:
                final[0] = False
                final[1] = ["Error en el retorno", pos+1]
                return final

        else:
            return "syntax error"

    # ----------------------------------------------------------------------------------------
    def recursividadC(cadena, pos, m):
        x = 0
        error = False
        cadena_split = cadena.split()
        if(cadena_split[0] == "RETORNA"):
            if(m==1):
                final[0] = False
                final[1] = ["Función tipo void no debe retornar", pos + 1]
                return final
            if (re.search(expresion, cadena)):
                if (re.search('ENTERO', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('REAL', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('BOOLEANO', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('CARACTER', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                elif (re.search('VACIO', cadena_split[0])):
                    final[0] = False
                    final[1] = ["Error en el retorno", pos+1]
                    return final
                if (error == False):
                    for n in cadena_split:
                        posicion = cadena_split.index(n)
                        if (re.search('RETORNA', n)):
                            x = 1
                            cadena_split[posicion] = 'return'
                            resultado3 = ' '.join(cadena_split) + ';'
                        else:
                            return "syntax error"
                    # print(resultado3)
                        if (x == 1):
                            return resultado3
            else:
                final[0] = False
                final[1] = ["Error en el retorno", pos+1]
                return final

        else:
            return "syntax error"

    if (leng == 1):
        return recursividadPython(cadena, pos, m)
    elif (leng == 2):
        return recursividadJava(cadena, pos, m)
    elif (leng == 3):
        return recursividadC(cadena, pos, m)


