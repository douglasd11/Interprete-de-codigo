# -*- coding: utf-8 -*-

import re

RESERVED_WORDS = ['SI','ENTONCES','SINO','FSINO','FSI','SEGUN','HACER','CASO','DEOTROMODO','FSEGUN']                       #Constante que guarda palabras reservadas de los condicionales SEGUN y SI    
X = re.compile(r'(\"(.+)\"$)|((-|)([0]|[1-9][0-9]*)(\.[0-9]+)*)')                                                          #Expresión regular que general todas las cadenas y números reales, las cadenas deben comenzar y terminar en comillas
all_var_name = re.compile(r'^[a-zA-Z][\w-]*')                                                                              #Expresión regular que genera todos los nombres de variables 

Y = ['&&','||']                                                                                                             #Constante que guarda los operadores logicos 
COMP = ['>','<','==','>=','<=','!=']                                                                                        #Constante que guarda los comparadores lógicos 

#Diccionario que traduce las palabras reservadas a su equivalente en java, los saltos de línea son para mejor orden
TRADUCIR = {
    'SI': 'if(',
    'ENTONCES': '){\n',
    'FSI': '\n}\n',
    'SINO': '\n}\nelse{\n',
    'FSINO': '\n}\n',
    'SEGUN': '\nswitch(',
    'HACER': '){',
    'CASO': '\n\tcase ',
    'DEOTROMODO:': '\n\tdefault: ',
    'FSEGUN': 'break;\n}\n'
}

"""# Funcion Condicion Unitaria

funcion que valida las condiciones unitarias, usada en la Estructura condicional SEGUN
"""

def CondicionUnitaria(cadena):                                                                        #Función que valida los condicionales unitarios, recibe la cadena a evaluar
    estado = 1                                                                                        #Inicialización de estado en 1
                                                                                          #Iterador que guarda las posiciones en memoria 
    for i in range(0, len(cadena)):                                                                   #Ciclo que recorre la cadena de la posición cero hasta su longitud
      # Se asigna una nueva transicion de la cadena por cada paso del for
      transicion = cadena[i]
      

      if estado == 1:                                                                                 #Evalua si el estado es igual a 1
        if transicion == '!':                                                                         #Se evalua si la transición es igual a diferente
          estado = 2                                                                                  #Cambia el estado a dos si la condición se cumple 
        
        elif re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO':
          estado = 3                                                                                  #Si la transición es diferente de dos, se evalua que el nombre de variable sea correcto y si es así se pasa al estado 3

        else:
          estado = 4                                                                                  #Si no se cumplen ningunas de las condiciones anteriores, se manda al estado de error

      elif estado == 2:                                                                               #Se evalua si el estado es igual a dos
        if re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO' and transicion != '!':
          estado = 3                                                                                  #Si se cumple la condición y ademas, el nombre de variable es correcto dentro de la definición, se pasa al estado tres

        else:                                                                                        
          estado = 4                                                                                  #Si no se cumple la condición anteriormente descrita, se envía al estado de error
      elif estado == 3:                                                                               #Si se llego al estado tres (De aceptación), se evalua si la siguiente transición es hacer y se guarda la posición en memoria en que finaliza 
            if transicion == 'HACER':
              break
            else:
                estado = 4
      
      elif estado == 4:
        break
      else:
        return False

    if estado == 3:                                                                                  #Si el estado es igual a tres, se retorna que la cadena fue aceptada y la posición en memoria en la que finalizó
        return {'aceptacion':'Entra'}
    else:
        return {'aceptacion':'No'}                                                                   #Si no, se retorna que la cadena no fue aceptada

"""# Funcion Condicion

Valida las condiciones dentro de la ESTRUCTURA SI 
"""

def Condicion(cadena):                                                                                         #Función que valida las condiciones dentro de la estructura SI
  estado = 1                                                                                                   #Se inicializa el iterador en uno                                                                                             #Iterador para guardar las posiciones en memoria en las que finaliza 
  
  for i in range(0, len(cadena)):                                                                              #Ciclo que recorre la cadena de la posición cero hasta su longitud
    transicion = cadena[i]
    #print(transicion)

    if estado == 1:
                                                                                                              #Se evalua si se cumple alguna de las cuatro condiciones siguientes
      if transicion == '!':                                                                                   #Se evalua si la transición es igual a diferente, si se cumple se envia al estado tres                                                                                    
        estado = 3
      elif transicion == 'VERDADERO' or transicion == 'FALSO':                                                #Se evalua si la transición es una variables booleana, si se cumple se envía al estado cuatro
        estado = 4
      elif re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP:      #se evalua si la transición es un nombre de variable, se evalua que esté correcto y si se cumple se pasa al estado 2
        estado = 2                                                                                                                            #Sirve para condiciones unitarias y múltiples 
      elif re.match(X,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP:                 #se evalua si la transición es un nombre de variable, se evalua que esté correcto y si se cumple se pasa al estado 2
        estado = 2                                                                                                                            #Sirve para condiciones unitarias y múltiples
          
      else:
          estado = 10                                                                                         #Si no se cumple ninguna de las condiciones anteriores se manda al estado de error

    elif estado == 2:                                                                                         #Se evalua si el estado es igual a dos, y de ser así se cumple alguna de las siguientes condiciones
      if transicion in COMP:                                                                                  #Si la transición es un comparador logico se cambia al estado tres
            estado = 3
      elif transicion in Y:                                                                                   #Si la transición es un operador lógico se cambia al estado seis
            estado = 6
      elif transicion == 'ENTONCES':                                                                          #Si la transición es igual a la palabra reservada entonces (Estado de aceptación), se iguala el iterador a la posición en que finalice 
            break
      else:
            estado = 10                                                                                      # Si no se cumple ninguna de las condiciones anteriores, se manda a estado de error y quiere decir que la cadena no fue aceptada

    elif estado == 3:                                                                                        #Se evalua si el estado es igual a tres (Condición unitaria o condición múltiple), y se evaluan las dos condiciones siguientes
      if re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO' and transicion != '!':
        estado = 5                                                                                           #Si la transisicón es un nombre de variable se evalua el nombre con la expresión reguladora y si es correcta se pasa al estado cinco
      elif re.match(X,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO' and transicion != '!':
        estado = 5                                                                                           #Si la transisicón es un caracter o número real se evalua con la expresión reguladora y si es correcta se pasa al estado cinco
          
      else:
        estado = 10                                                                                          #Si no se cumplen ninguna de las condiciones anteriores se pasa al estado de error y quiere decir que la cadena no fue aceptada

    elif estado == 4:                                                                                        #Se evalua si el estado es igual a 4
      if transicion == 'ENTONCES':                                                                           #Se evalua si la transición es igual a entonces, si es así se le asigna a la variable iterador la posición en memoria con la que se finaliza
        
        break
      else:
        estado = 10
        
    elif estado == 5:                                                                                        #Se evalua si el estado es igual a cinco, de ser así se pueden presentar dos casos 
      if transicion in Y:                                                                                    #La transición es un operador lógico y se envía al tado seis
        estado = 6
      elif transicion == 'ENTONCES':                                                                         #La transición es la palabra reservada entonces, si es así se le asigna a la variable iterador la posición en memoria con la que se finaliza
        
        break
      else:
        estado = 10

    elif estado == 6:                                                                                        #Esto sucede si existen condiciones anidadas, se vuelve a repetir el mismo proceso descrito anteriormente cuantas veces sea necesario
      if transicion == '!':
        estado = 8
      elif re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO':
        estado = 7 
      elif re.match(X,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO':
        estado = 7 
      else:
        estado = 10

    elif estado == 7:
      if transicion in Y:
        estado = 6
      elif transicion in COMP:
        estado = 8
      elif transicion == 'ENTONCES':
        
        break
      else:
        estado = 10

    elif estado == 8:
      if re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO' and transicion != '!':
        estado = 9
      elif re.match(X,transicion) and transicion not in RESERVED_WORDS and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO' and transicion != '!':
        estado = 9
      else:
        estado = 10

    elif estado == 9:
      if transicion in Y:
        estado = 6
      elif transicion == 'ENTONCES':
        
        break
      else:
        estado = 10

        #ESTADO DE ERROR

    elif estado == 10:
      break
        
    else:
      break
  
  if estado == 2 or estado == 4 or estado == 5 or estado == 7 or estado == 9:                                                         #Se evalua si la cadena quedó en un estado de aceptación (Se precesó completamente)
    return {'aceptacion':'Entra'}                                                                                #Si se cumple lo anterior, se retorna que la cadena entró 
  else:
    return {'aceptacion':'No'}                                                                                                        #Si no, se retorna que la cadena no entró

"""#Funcion validar cierre

Valida si toda estructura condicional que fue abierta tuvo su cierre correspondiente
"""

def validarCierre(cierre,inicio,indexLinea,lineas,excepcion=''):                                                            #Función que valida los cierres de las estructuras SI Y SEGUN, se recibe como parámetros de entrada, las palabras reservadas de cierre y de inicio, la línea a evaluar, el archivo txt completo y una excepción en caso de presentarse 
        aux = 1;                                                                                                            #Se inicializa en uno porque nos encontramos dentro de una estructura SI, SINO o SEGUN
        for i in range(indexLinea + 1, len(lineas)):                                                                        #Ciclo que lee desde la línea siguiente donde se encontró una palabra reservada de inicio hasta el final del archivo
            linea = lineas[i].strip('\t\n').split(' ')                                                                      #Convierte cada linea en un arry list
            if excepcion:
                if excepcion in linea:                                                                                      #Si existe una excepción, y se encuntra en la línea que se está leyendo se resta uno al auxiliar (Un SI no puede cerrar con FSI si existe un SINO)
                    aux -= 1
            if inicio in linea: aux += 1                                                                                    #Si se encuentra una palabra de inicio se suma uno a la variable auxiliar
            if cierre in linea: aux -= 1                                                                                    #Si se encuentra una palabra de cierre se le resta uno al auxiliar 
            if aux == 0: return True                                                                                        #Si el auxiliar se encuentra en cero, quiere decir que cada estructura abierta tuvo su respectivo cierre
        return False

"""#Funcion Validar

Esta recibe un array con las lineas de un archivo de texto, y va validando una por una si contiene un condicional (ya sea SI o SEGUN), valida que su estructura esta bien escrita y lo transforma a lenguaje java

Finalmente retorna una array con dos posiciones:
* la primera con valor booleano, esta indica si se escribieron correctamente las estructuras condicionales (TRUE) o no (FALSE) 
* La segunda devuelve un array con las lineas que fueron validadas y transformadas con las que no, mantieniendo su orden o un array con todos los errores que se encontraron en la sintaxis
"""

def validarCondicionalesJAVA(lineas):                                                                                       #Función para validar las estructuras que contengan condicionales dentro de un archivo de texto

    #Valida si hay una estructura SI abierta 
    entro_si = False

    # Guarda la cantidad de estructuras SI que se encuentran abiertas
    conteo_si = 0

    # Guarda si hay una estructura SI con SINO abierta
    entro_sino = False

    # Guarda la cantidad de estructuras SI con SINO que se encuentran abiertas
    conteo_sino = 0

    # Guarda si hay una estructura SEGUN abierta
    entro_segun = False

    # Guarda la cantidad de estructuras SEGUN que se encuentran abiertas
    conteo_segun = 0
    
    RESULT = [True, []]                                                                                                 #Función que retorna si hubo o no errores, y en caso de existir errores retorna estos y la linea en las que se encuentran, ademas retorna la traducción a C
    # print(lineas)
    for line in lineas:                                                                                                 #Ciclo para leer el archivo de texto línea por línea
        
        sentence = line.strip('\t\n').split(' ')                                                                        #Convierte cada línea del archivo de texto en un arraylist
        print(line,entro_si)

        # Sentancia de codigo que valida que el caracter vacio se toma como una cadena
        """if '"' in sentence:
            idx = sentence.index('"')
            if('"' in sentence[idx+1]):
                sentence[idx] = sentence[idx]+' '+sentence[idx+1]
                sentence.remove(sentence[idx+1])
            elif ('"' in sentence[idx-1]):
                sentence[idx] = sentence[idx-1]+' '+sentence[idx]
                sentence.remove(sentence[idx])"""

        if 'SI' in sentence:
           
            result = Condicion(sentence[1:])                                                                            #Se valida que se esté dentro de una estructura SI y que termine en un ENTONCES
            entro_si = True
            conteo_si += 1
            if(result['aceptacion'] == 'Entra'):
                pos = line.find('ENTONCES')
                if len(line) >= pos + 8:
                    for idx in range(pos+8, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])     #Si no termina en ENTONCES, se almacena el siguiente error dentro del array de errores
                            break

                if not validarCierre('FSI', 'SI', lineas.index(line), lineas, 'SINO'):                                              #Se valida que cada estructura SI abierta tenga su respectivo cierre 
                    RESULT[0] = False
                    RESULT[1].append(['Error: No se encontro la palabra de cierre "FSI": ',lineas.index(line)+1])                   #Si alguna estructura SI no se encuentra cerrada, se almacena el siguiente error dentro del array de errores

                if RESULT[0]:
                
                    traduccion = ''                                                                                                 #Se traduce el código al lenguaje java
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')

                    RESULT[1].append(traduccion)   
            else:
                if 'ENTONCES' not in sentence:                                                                                      #Este error es cuando no se escribió la palabra ENTONCES
                    RESULT[0] = False
                    RESULT[1].append(['ERROR: No se encontro la palabra "ENTONCES" en la linea: ',lineas.index(line)+1])
                else:
                    RESULT[0] = False
                    RESULT[1].append(['ERROR: Condicion mal escrita en la linea: ',lineas.index(line)+1])                           #Este error es cuando no se ha escrito de forma correcta la condición 
                    


        
        elif 'SINO' == sentence[0]:
            #print(f"entrosi: {entro_si}")
            if entro_si or conteo_si>0:

                if len(line) >= 5:                                                                                                  #Se evalua que se este dentro de una estructura SI, y se evalua que despues de la palabra SINO no se escriba mas nada si no que venga un salto de línea
                    for idx in range(5, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])     #Si no se termina con salto de línea, se almacena el siguiente error dentro del array de errores
                            break

                entro_si = False                                                                                                    #Si hay un SINO, el fin no debe ser FSI si no FSINO
                entro_sino = True
                conteo_sino += 1

                if not validarCierre('FSINO', 'SINO', lineas.index(line), lineas):                                                  #Se valida que se cierren todas las estructuras SINO
                    RESULT[0] = False
                    RESULT[1].append(['Error: No se encontro la palabra de cierre "FSINO": ',lineas.index(line)+1])                 #Si hay alguna estructura SINO sin cierre, se almacena el siguiente error dentro del array de errores

                if RESULT[0]:                                                                                                       #Traducción del código a lenguaje java
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')
                    
                    RESULT[1].append(traduccion)

            elif entro_sino:                                                                                                        #Si se encuentra más de un SINO dentro de un SI
                RESULT[0] = False
                RESULT[1].append(['ERROR: palabra SINO repetida en la linea: ',lineas.index(line)+1])                               #Si hay más de un SINO en un SI, se almacena el siguiente error dentro del array de errores
    
            else:
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SI en la linea: ',lineas.index(line)+1])                        #No puede haber una estructura SINO, sin un SI, si esto sucede se muestra este error, y se almacena el siguiente error dentro del array de errores
                return RESULT
            
            
            
            
            
        
        elif 'FSINO' == sentence[0]:                                                                                                
            if entro_sino:                                                                                                            
                
                if len(line) >= 6:
                    for idx in range(6, len(line)):                                                                                 #Se valida que después del FSINO, no exista más nada, es decir que después de este vemga un salto de línea
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])     #De no ser así, se almacena el siguiente error dentro del array de errores
                            break

                if RESULT[0]:                                                                                                       #Traducción al lenguaje java
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')
                    RESULT[1].append(traduccion)

                if conteo_sino > 0:
                    conteo_sino -= 1

                if conteo_sino == 0:
                   entro_sino = False
            else:                                                                                                                 #Se debe tener una estructura SINO para poder cerrar la misma
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SINO en la linea: ',lineas.index(line)+1])                    #Si no se encuentra la palabra SINO, se almacena el siguiente error dentro del array de errores
                
            

        elif 'FSI' == sentence[0]:
            if entro_si:
                
                if len(line) >= 4:
                    for idx in range(4, len(line)):                                                                               #Se valida que después del FSI, no exista más nada, es decir que después de este venga un salto de línea
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])   #Si no se termina en un salto de línea, se almacena el siguiente error dentro del array de errores
                            break

                if RESULT[0]:                                                                                                     #Traducción al lenguaje java
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')
                    RESULT[1].append(traduccion)

                if conteo_si > 0:                                                                                               #Si el conteo de FSI es mayor a cero, alguno no está cerrado y se debe cerrar
                    conteo_si -= 1

                if conteo_si == 0:                                                                                              #Todos los si están cerrados y se cambia el valor de entro_si a falso
                   entro_si = False

                
            elif entro_sino:
                entro_sino = False                                                                                              #No se ha cerrado un SINO
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra FSINO en la linea: ',lineas.index(line)+1])                 #Si no se encuentra un SINO cerrado, se almacena el siguiente error dentro del array de errores
            else:
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SI en la linea: ',lineas.index(line)+1])                    #No hay ningún SI definido 
                return RESULT
                   

        elif 'SEGUN' == sentence[0]:
            entro_segun = True                                                                                                  #Se encuentra una estructura según abierta
            conteo_segun += 1                                                                                                   #Se suma uno al conteo de según 

            result = CondicionUnitaria(sentence[1:])
            
            if(result['aceptacion'] == 'Entra'):
                pos = line.find('HACER')                                                                                        #Se valida que luego del según y la condicción venga un hacer y luego un salto de línea 
                if len(line) >= pos + 5:
                    for idx in range(pos+5, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1]) #Si no termina en salto de línea luego del según, se almacena el siguiente error dentro del array de errores
                            break

                if not validarCierre('FSEGUN', 'SEGUN', lineas.index(line), lineas):                                          #Se valida que se cierre cada según encontrado 
                    RESULT[0] = False
                    RESULT[1].append(['Error: No se encontro palabra de cierre "FSEGUN": ',lineas.index(line)+1])             #Si algún según se encuentra sin cierre, se almacena el siguiente error dentro del array de errores


                if RESULT[0]:                                                                                                 #Traducción al lenguaje java
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')

                    RESULT[1].append(traduccion)
            else:
                if 'HACER' not in sentence:                                                                                   #La estrructura no termina en la palabra HACER
                    RESULT[0] = False
                    RESULT[1].append(['ERROR: No se encontro la palabra "HACER" en la linea: ',lineas.index(line)+1])         #Si no se encuentra un HACER despues de la condición, se almacena el siguiente error dentro del array de errores
                else:
                    if 'HACER' in sentence[1]:                                                                                #En la posición en la que va la condición, no se encuentra esta
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: Condicion a evaluar no escrita: ',lineas.index(line)+1])                   #Si no se encuentra escrita la condición, se almacena el siguiente error dentro del array de errores
                    else:
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: Condicion a evaluar mal escrita: ',lineas.index(line)+1])                  #Si la condición no se escribe de forma correcta, se almacena el siguiente error dentro del array de errores
                
            

        elif 'CASO' in sentence[0]:
            if entro_segun:

                if '' in sentence:
                    sentence.remove('')                                                                                     #Sirve para eliminar todos los espacios en blanco en la definición de los casos

                if len(sentence) == 1:
                    if ':' not in sentence[0]:                                                                              #Validar que se encuentre :
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: No se encontro la palabra ":" en la linea: ',lineas.index(line)+1])       #Si no se encuentra :, se almacena el siguiente error dentro del array de errores
                    else:
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: caso mal escrito en la linea: ', lineas.index(line)+1])                   #Si se presenta otra excepción dónde la estructura esté mal escrita 
                   
                elif len(sentence) == 2:                                                                                    #Se valida que : se encuentre en la posición correcta 
                    if ':' in sentence[1]:
                        
                        if not re.match(X,sentence[1][:len(sentence[1])-1]):                                                #Valida si el valor a evaluar en el caso es una cadena o número real 
                            RESULT[0] = False
                            RESULT[1].append(['ERROR: caso mal escrito en la linea: ', lineas.index(line)+1]) 
                       
                        if '::' in sentence[1]:                                                                             #Valida si los : están escritos más de una vez 
                            RESULT[0] = False
                            RESULT[1].append(['ERROR: palabra ":" repetida en la linea: ', lineas.index(line)+1])
                        
                    else:
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: No se encontro la palabra ":" en la linea: ',lineas.index(line)+1])        #No se encontró : en la posición, se almacena el siguiente error dentro del array de errores
                elif len(sentence) == 3:
                    if ':' not in sentence[1]:
                        if not re.match(X,sentence[1]):
                            RESULT[0] = False
                            RESULT[1].append(['ERROR: caso mal escrito en la linea: ', lineas.index(line)+1])               #Valida si el valor a evaluar está escrito de forma correcta, si no, se almacena el error dentro del array de errores
                       

                        if sentence[2] == '::':                                                                             #Validar si : están escritos más de una vez         
                            RESULT[0] = False
                            RESULT[1].append(['ERROR: palabra ":" repetida en la linea: ', lineas.index(line)+1])
                        
                        elif sentence[2] != ':':                                                                            #Valida si : se encuentra en la estructura 
                            RESULT[0] = False
                            RESULT[1].append(['ERROR: No se encontro la palabra ":" en la linea: ',lineas.index(line)+1])

                        
                           
                    else:
                        if sentence[2] == ':' or  '::' in sentence[1]:                                                      #Validar si : están escritos más de una vez 
                            
                            RESULT[0] = False
                            RESULT[1].append(['ERROR: palabra ":" repetida en la linea: ',lineas.index(line)+1])
               
                pos = line.find(':')                                                                                        #Valida que despues de : venga un salto de línea 
                if len(line) >= pos + 1:
                    for idx in range(pos+1, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                            break

                if RESULT[0]:                                                                                               #Traducción a java 
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                                traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')

                    RESULT[1].append(traduccion)

            else:                                                                                                          #En caso de no encontrar ninguna estructura SEGUN abierta
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SEGUN en la linea: ',lineas.index(line)+1])
            

        elif 'DEOTROMODO' in sentence[0]:                                                                                  #Si no se cumple ninguno de los casos descritos

            if entro_segun:

                                                                                                                          #Valida que la linea termine en ":"
                if len(sentence) == 1:
                    if ':' not in sentence[0]:
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: No se encontro la palabra ":" en la linea: ',lineas.index(line)+1])     #Valida si el array tiene una sola posición, debe estar DEOTROMODO:
                elif len(sentence) == 2:
                    if ':' not in sentence[1]:
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: No se encontro la palabra ":" en la linea: ',lineas.index(line)+1])     #Valida si el array tiene dos posiciones, debe estar DEOTROMODO : 

                                                                                                                        #Valida que no haya ningun caracter en la linea despues del ":"
                pos = line.find(':')
                if len(line) >= pos + 1:
                    for idx in range(pos+1, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                            break

                if RESULT[0]:                                                                                           #Traducción a lenguaje java
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')

                    RESULT[1].append(traduccion)
            else:
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SEGUN en la linea: ',lineas.index(line)+1])         #No se encontró ninguna estructura SEGUN 
                
            

        elif 'FSEGUN' == sentence[0]:

            if entro_segun:

                                                                                                                        #Valida que no haya ningun caracter en la linea despues de la palabra "FSEGUN"
                if len(line) >= 7:
                    for idx in range(7, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                            break
                if RESULT[0]:                                                                                           #Traducción al lenguaje java
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')
                    RESULT[1].append(traduccion)

                if conteo_segun > 0:                                                                                     #Si el conteo de SEGUN es mayor a cero, cierra cada SEGUN que exista 
                    conteo_segun -= 1

                if conteo_segun == 0:                                                                                    #Todos los SEGUN tienen su respectivo cierre 
                    entro_segun = False
                
            else:
                RESULT[0] = False                                                                                        #No se encuentra ningún SEGUN de inicio
                RESULT[1].append(['ERROR: No se encontro la palabra SEGUN en la linea:  ',lineas.index(line)+1])
            
        else:
            if RESULT[0]:                                                                                                #Traducción a lenguaje java
                traduccion = ''
                for palabra in sentence:
                        traduccion += (palabra+' ')

                RESULT[1].append(traduccion)
        
    cambios = 0                                                                                                            

    RESULT[1] = [linea for linea in RESULT[1] if linea != ""]                                                           #Elimina los caracteres vacios del array
    RESULT[1] = [linea for linea in RESULT[1] if linea != " "]

    copiaResultado = RESULT[1].copy()

    for i in range(len(RESULT[1])):
        if not RESULT[0]:                                                                                              #Si tuvo errores, elimina todas las lineas que no sean errores

            if not isinstance(RESULT[1][i], list):                                                                    
                copiaResultado.remove(RESULT[1][i])
        else:
            
            if 'case' in copiaResultado[i]:                                                                             #Sirve para colocar cada break en los case
                cambios += 1

                if cambios > 1 and 'switch' not in copiaResultado[i-1]:
                    copiaResultado[i] = 'break;\n'+copiaResultado[i]
            elif 'default' in copiaResultado[i] and 'switch' not in copiaResultado[i-1]:
                
                copiaResultado[i] = 'break;\n'+copiaResultado[i]                                                        
        
    RESULT[1] = copiaResultado                                                                                          #Al macenar los cambios que se hicieron a los case

        


    return RESULT

"""CODIGO de ejemplo
el nombre del archivo de la estructura puede ser cambiado por el que escoja

estructura = open('estructura.txt', 'r')
lineas = estructura.read().split('\n')

r = open('resultado.txt','w')
resultado = validarCondicionales(lineas)
if(resultado[0]):
        r.writelines(resultado[1])
        r.close()
        print('COMPILADO EXITOSAMENTE')
else:
        print(resultado[1])"""

