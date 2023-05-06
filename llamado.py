##Invocar funcion Python/Java

import re


expresion = r'([a-zA-Z]+[a-zA-Z0-9_]*)[(][ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)*([,][ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*))*[ ]*[)]'  # exp= expresion regular (No es seguro que este sea el inidicado)

def llamado(cadena, leng, pos):
    final = [True, []]
    def llamadoPython(cadena, pos):
        #resultado3 = ""
        n_tab = cadena.count('\t')
        error = False
        cadena_split = cadena.split()
        if (re.match(expresion, cadena)):
            if (re.search('ENTERO\(', cadena_split[0]) or re.match('REAL\(', cadena_split[0]) or re.match('BOOLEANO\(', cadena_split[0]) or re.match('CARACTER\(', cadena_split[0]) or re.match('VACIO\(', cadena_split[0])):
                        final[0] = False
                        final[1] = ["Error en  llamado de la función", pos+1]
                        return final
            if (error == False):
                for n in cadena_split:
                    resultado3 = ' '.join(cadena_split)
                    resultado3 = (n_tab * '\t') + resultado3

                return resultado3
        

        else:
            return "syntax error"



    # ---------------------------------------------------------------------------------------
    def llamadoJava(cadena, pos):
        x=0
        error = False
        cadena_split = cadena.split()
        if (re.search(expresion, cadena)):
            if (re.search('ENTERO', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
            elif (re.search('REAL', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
            elif (re.search('BOOLEANO', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
            elif (re.search('CARACTER', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
            elif (re.search('VACIO', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
        if (error == False):
            for n in cadena_split:
                if(re.search('\(',n) and re.search("\)", cadena_split[-1])):
                    x = 1
                    resultado3 = ' '.join(cadena_split) + ';'
                else:
                    return "syntax error"
            # print(resultado3)
                if(x == 1):
                    #print(resultado3)
                    return resultado3
        else:
            return "syntax error"

    # ----------------------------------------------------------------------------------------
    def llamadoC(cadena, pos):
        x = 0
        error = False
        cadena_split = cadena.split()
        if (re.search(expresion, cadena)):
            if (re.search('ENTERO', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
            elif (re.search('REAL', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
            elif (re.search('BOOLEANO', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
            elif (re.search('CARACTER', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
            elif (re.search('VACIO', cadena_split[0])):
                final[0] = False
                final[1] = ["Error en  llamado de la función", pos+1]
                return final
        if (error == False):
            for n in cadena_split:
                if(re.search('\(',n) and re.search("\)", cadena_split[-1])):
                    x = 1
                    resultado3 = ' '.join(cadena_split) + ';'
                else:
                    return "syntax error"
            # print(resultado3)
                if (x == 1):
                    return resultado3
        else:
            return "syntax error"

    if (leng == 1):
        return llamadoPython(cadena, pos)
    elif (leng == 2):
        return llamadoJava(cadena, pos)
    elif (leng == 3):
        return llamadoC(cadena, pos)



