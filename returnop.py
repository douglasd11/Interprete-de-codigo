#Crear funcion Python (final con operacion)         Ej: Return operacion (a+b)

import re

def operacion(cadena, leng):

    ##varialbe anterior:
    exp = r'(([a-zA-Z]+[a-zA-Z0-9_]*[ ]*[=])|((RETORNA)[ ]*))([ ]*(([a-zA-Z]+[a-zA-Z0-9_]*)|([0-9]+)))(([ ]*[-+*/%])([ ]*(([a-zA-Z]+[a-zA-Z0-9_]*)|([0-9]+))))+'

    if("ENTERO" in cadena): ##este bloque de código es para identificar si existen palabras reservadas dentro de la cadena ingresada
        return "syntax error"
    elif("REAL" in cadena):
        return "syntax error"
    elif("CARACTER" in cadena):
        return "syntax error"
    elif("BOOLEANO" in cadena):
        return "syntax error"
    elif("VACIO" in cadena):
        return "syntax error"
    elif("FUNCION" in cadena):
        return "syntax error"
    elif("FINF" in cadena):
        return "syntax error"
    elif("return" in cadena):
        return "syntax error"
    elif("RETURN" in cadena):
        return "syntax errordsf"

    flag_retor = 0
    resul = "" ##donde se van a concatenar los resultados traducidos
    if(re.search(exp, cadena)): ##verifica si la cadena cumple con la expresión regular que está en la variable operacion
        c = cadena.split() ##guarda en aux una lista con cada palabra en la variable cadena y divide la cadena (teniendo en cuenta los espacios como divisores)
        ##print(c)
        for x in c:
            if(x == "RETORNA" and flag_retor == 0): ##así con cada palabra definida en estos if anidados por cada palabra que encuentre que coincida acumulará en resultado la traducción correspondiente 
                resul = "return"
                flag_retor = 1     ## se identifica que la palabra RETORNA ya fue gestionada, por lo tanto en la cadena no debe existir otra palabra RETORNA, este flag es para identificar eso
            else:
                if("RETORNA" in x or "return" in x):
                    return "syntax error" ##si se vuelve a encontrar por 2da vez la palabra RETORNA entonces termina todo y dice que hay error
                else:
                    resul = resul + " "+x
        if(leng == 1):
            resul = '  ' + resul
        elif(leng == 2 or leng == 3):
            resul = resul +";" ##concatenación final

        ##print(resul) 
        return resul ##retorna la cadena traducida
        
    else:
        return "syntax error" ##error si la cadena no cumple con la expresion regular
