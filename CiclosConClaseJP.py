import re
import os

class validarCiclosJP:

    def __init__(self, lines):
        self.lines = lines
        self.errores = [] # variable para alamcenar los errores.
        self.patronVarible = "^[A-Za-z0-9_-]*$"  # patron para nombre de variables.
        self.patronNumero = "^[0-9]*$"
        self.riservis = ["RETORNA", "FINF","FALSO","VERDADERO","SI","SINO","SEGUN","ENTONCES","FSIN","FSINO","SINO","HACER","CASO","DEOTROMODO","FSEGUN","HAZ","MIENTRAS","PARA","FINM","FINP","BOOLEANO","ENTERO","REAL","CARACTER"]

    # validar palabras del reservadas para el ciclo para.
    def valPalabrasCicloPara(self,linea):
        isValido = [True, ""]
        if ' HASTA ' in linea:
            if ' HACER' in linea:
                pos = linea.find("HACER")
                if len(linea) >= pos + 5:  # validar que no halla caracteres despues de la expresion Hacer
                    for index in range(pos + 5, len(linea)):
                        if linea[index] != " ":
                            print()
                            isValido = [False, ' error de sintaxis "despues de Hacer debe ir un salto de linea" ']
                            return isValido

                return isValido
            else:
                isValido = [False, ' error de sintaxis "Hacer" ']
                return isValido

        else:
            isValido = [False, ' error de sintaxis "Hasta" ']
            return isValido

    #validar palabras reservadas en el ciclo para.
    def valPalabrasReservadasPara(self, linea, indexlinea):
        posI = linea.find("PARA") + 4
        posF = linea.find("HASTA")
        rango = slice(posI, posF)
        inicializacion = linea[rango]

        if '=' in inicializacion:  # validar si tene una asignacion, para valdiar cada una de las variables.
            partesInicializacion = inicializacion.split('=')
            for i in partesInicializacion:
                aux = i.strip(" ")
                for palabra in self.riservis:
                    if palabra == aux:
                        self.errores.append(["error uso de palabra reservada: ", indexlinea + 1])
                        return False
        else:  # si no tiene asignacion validamos si la variable esta bien escrita
            aux = inicializacion.strip(" ")
            for palabra in self.riservis:
                if palabra == aux:
                    self.errores.append(["error uso de palabra reservada: ", indexlinea + 1])
                    return False

        rango = slice(linea.find("HASTA") + 5, linea.find("HACER"))
        condicion = linea[rango].strip(' ')
        partesCondicion = condicion.split(" ")

        if len(partesCondicion) == 1:  # evaluar si la condicion es valida
            for palabra in self.riservis:
                if palabra == partesCondicion[0]:
                    self.errores.append(["error uso de palabra reservada: ", indexlinea + 1])
                    return False
        if len(partesCondicion) == 2:
            for palabra in self.riservis:
                if palabra == partesCondicion[0]:
                    self.errores.append(["error uso de palabra reservada: ", indexlinea + 1])
                    return False
            for palabra in self.riservis:
                if palabra == partesCondicion[1]:
                    self.errores.append(["error uso de palabra reservada: ", indexlinea + 1])
                    return False

        return True

    # validar inicializacion variable ciclo para
    def valInicialozacionCicloPara(self, linea):
        posI = linea.find("PARA") + 4
        posF = linea.find("HASTA")
        rango = slice(posI, posF)
        inicializacion = linea[rango]

        if '=' in inicializacion:  # validar si tene una asignacion, para valdiar cada una de las variables.
            partesInicializacion = inicializacion.split('=')
            for i in partesInicializacion:
                aux = i.strip(" ")
                state = bool(re.match(self.patronVarible, aux))
                if state == False: return False
        else:  # si no tiene asignacion validamos si la variable esta bien escrita
            aux = inicializacion.strip(" ")
            state = bool(re.match(self.patronVarible, aux))
            if state == False: return False
        return True

    # evaluar condicion del ciclo para
    def valCondicionCicloPara(self, linea):
        rango = slice(linea.find("HASTA") + 5, linea.find("HACER"))
        condicion = linea[rango].strip(' ')
        partesCondicion = condicion.split(" ")

        if len(partesCondicion) > 2 or len(partesCondicion) < 1:  # en caso de que este mas escrita la condicion
            return False

        if len(partesCondicion) == 1:  # evaluar si la condicion es valida
            state = bool(re.match(self.patronVarible, partesCondicion[0]))
            if state == True:
                return True
            else:
                return False

        if len(partesCondicion) == 2:  # evaluar si la condicion es valdia y la indicacion de incremento
            isValido = True
            state = bool(re.match(self.patronVarible, partesCondicion[0]))
            if state == False: isValido = False
            state = bool(re.match(self.patronNumero, partesCondicion[1]))
            if state == False: isValido = False
            return isValido

    # valdiar que haya etiqueta de cierre para el ciclo.
    def validarcierreCiclo(self,cierre, ciclo, indexLinea):
        poCierreCiclo=-1
        for i in range(indexLinea + 1, len(self.lines)):
            linea = self.lines[i]
            if re.match(r'^( |~~~|\t)*'+cierre, linea):
                poCierreCiclo=i
        if poCierreCiclo> -1:return True
        return False

    # hallar el cieerre de un ciclo, retorna true o flase, si esta o no.
    def indexCierreCiclo(self, cierre, ciclo, indexLinea):
        aux=1
        poCierreCiclo=-1
        for i in range(indexLinea + 1, len(self.lines)):
            linea = self.lines[i]
            if re.match(r'^( |~~~|\t)*'+ciclo, linea):
                aux+=1
            if re.match(r'^( |~~~|\t)*'+cierre, linea) and aux>=1:
                aux-=1
                poCierreCiclo=i
            if aux==0:
                break
        if poCierreCiclo> -1:return poCierreCiclo
        return -1

    # funcion principal para validar sinaxis ciclo para
    def valCicloPara(self, linea, indexLinea):
        if self.valPalabrasCicloPara(linea)[0]:
            if self.valInicialozacionCicloPara(linea):
                if self.valCondicionCicloPara(linea):
                    if self.validarcierreCiclo("FINP", "PARA", indexLinea):
                        return True
                    else:
                        self.errores.append(["error etiqueta cierre ciclo para linea: ", indexLinea + 1])
                        return False

                else:
                    self.errores.append(["condicion mal escrita linea: ", indexLinea + 1])
                    return False
            else:
                self.errores.append(["inicializacion mal escrita linea: ", (indexLinea + 1)])
                return False
        else:
            self.errores.append([self.valPalabrasCicloPara(linea)[1], " | Error en la linea Numero: ", indexLinea + 1])
            return False

################################################################################################################################
    # fucion para mapear de pseudo-codigo a JAVA, el ciclo para
    def mapCicloParaJava(self,linea, indexLinea):

        variable = ""
        condicion = ""

        rangoCondicion = slice(linea.find("HASTA") + 5, linea.find("HACER"))
        condicion = linea[rangoCondicion].strip(' ')

        partesCondicion = condicion.split(" ")
        rangoInicializacion = slice(linea.find("PARA") + 4, linea.find("HASTA"))
        inicializacion = linea[rangoInicializacion].strip(' ')

        if '=' in inicializacion:
            partesInicializacion = inicializacion.split('=')
            variable = partesInicializacion[0]
        else:
            variable = inicializacion
        incremento = variable + "+= 1"
        if len(partesCondicion) == 2:
            condicion = variable + "<= " + partesCondicion[0]
            incremento = variable + "+= " + partesCondicion[1]
        if len(partesCondicion) == 1:
            condicion = variable + " <= " + partesCondicion[0]

        auxlinea = "for(" + inicializacion + " ;" + condicion + " ;" + incremento + ") {"
        self.lines[self.indexCierreCiclo("FINP", "PARA", indexLinea)] = "}"
        self.lines[indexLinea] = auxlinea
 
#######################################################################################################

    # fucion para mapear de pseudo-codigo a PYTHON, el ciclo para
    def mapCicloParaPython(self,linea, indexLinea):

        variable = ""
        condicion = ""
        inicializacionVariable="0"

        rangoCondicion = slice(linea.find("HASTA") + 5, linea.find("HACER"))
        condicion = linea[rangoCondicion].strip(' ')

        partesCondicion = condicion.strip(' ')
        rangoInicializacion = slice(linea.find("PARA") + 4, linea.find("HASTA"))
        inicializacion = linea[rangoInicializacion].strip(' ')

        if '=' in inicializacion:

            partesInicializacion = inicializacion.split('=')
            variable = partesInicializacion[0]
            inicializacionVariable= partesInicializacion[1]
        else:
            variable = inicializacion
        finLinea=self.indexCierreCiclo("FINP", "PARA", indexLinea)
        tabs=slice(0,self.lines[indexLinea].find("PARA"))
        auxlinea =self.lines[indexLinea][tabs]+"for " + variable + " in range("+inicializacionVariable+"," + partesCondicion +"):"
        self.lines[finLinea] = self.lines[finLinea].replace("FINP","~~~")
        self.lines[indexLinea] = auxlinea
        for i in range(indexLinea+1,finLinea):
            self.lines[i] = "~~~"+self.lines[i]


    #validar palabras reservadas ciclo mientras
    def valPalabrasReservadasMientras(self, linea,  inicio, incrementoInicio, final, indexLinea):
        rango = slice(linea.find(inicio) + incrementoInicio, final)
        condicion = linea[rango].strip(' ')
        partesCondicion = condicion.split("&")

        for parte in partesCondicion:
            partesCondicion2 = parte.split("|")
            for parte2 in partesCondicion2:
                if ">=" in  parte2:
                    aux = parte2.split(">=")
                    for i in aux:
                        stripSpace = i.strip(" ")
                        for palabra in self.riservis:
                            if palabra == stripSpace:
                                self.errores.append(["error uso de palabra reservada: ", indexLinea + 1])
                                return False
                if "<=" in parte2:
                    aux = parte2.split("<=")
                    for i in aux:
                        stripSpace = i.strip(" ")
                        for palabra in self.riservis:
                            if palabra == stripSpace:
                                self.errores.append(["error uso de palabra reservada: ", indexLinea + 1])
                                return False
                if "<" in parte2:
                    aux = parte2.split("<")
                    for i in aux:
                        stripSpace = i.strip(" ")
                        for palabra in self.riservis:
                            if palabra == stripSpace:
                                self.errores.append(["error uso de palabra reservada: ", indexLinea + 1])
                                return False
                if ">" in parte2:
                    aux = parte2.split(">")
                    for i in aux:
                        stripSpace = i.strip(" ")
                        for palabra in self.riservis:
                            if palabra == stripSpace:
                                self.errores.append(["error uso de palabra reservada: ", indexLinea + 1])
                                return False
                if "==" in parte2:
                    aux = parte2.split("==")
                    for i in aux:
                        stripSpace = i.strip(" ")
                        for palabra in self.riservis:
                            if palabra == stripSpace:
                                self.errores.append(["error uso de palabra reservada: ", indexLinea + 1])
                                return False
                if "!=" in parte2:
                    aux = parte2.split("!=")
                    for i in aux:
                        stripSpace = i.strip(" ")
                        for palabra in self.riservis:
                            if palabra == stripSpace:
                                self.errores.append(["error uso de palabra reservada: ", indexLinea + 1])
                                return False
                stripSpace = parte2.strip(" ")
                for palabra in self.riservis:
                    if palabra == stripSpace:
                        self.errores.append(["error uso de palabra reservada: ", indexLinea + 1])
                        return False
        return True



    # validar palabras reservadas para el ciclo mientras esten bien escritas
    def valPalabraCicloMientras(self, linea):
        isValido = [True, ""]
        if ' HACER' in linea:
            pos = linea.find("HACER")
            if len(linea) >= pos + 5:
                for index in range(pos + 5, len(linea)):
                    if linea[index] != " ":
                        print()
                        isValido = [False, ' error de sintaxis "despues de Hacer debe ir un salto de linea" ']
                        return isValido

            return isValido
        else:
            isValido = [False, ' error de sintaxis "Hacer" ']
            return isValido

    # validar la condicion del ciclo mientras este bien formulada.
    def valCondicionCicloMientras(self, linea, inicio, incrementoInicio, final):
        isValido = True
        listaCondiciones = []

        rango = slice(linea.find(inicio) + incrementoInicio, final)
        condicion = linea[rango].strip(' ')

        partesCondicion = condicion.split("&")

        for parte in partesCondicion:
            if "|" in parte:
                partesCondicion2 = parte.split("|")
                for parte2 in partesCondicion2:
                    if "<=" in parte2:
                        partesCondicion2 = parte2.split("<=")
                        for aux in partesCondicion2:
                            if aux.isspace() or len(aux) == 0: return False
                        if len(partesCondicion2) == 2:
                            state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                            if state == False: return False
                            state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                            if state == False: return False
                        else:
                            return False
                    elif ">=" in parte2:
                        partesCondicion2 = parte2.split(">=")
                        for aux in partesCondicion2:
                            if aux.isspace() or len(aux) == 0: return False
                        if len(partesCondicion2) == 2:
                            state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                            if state == False: return False
                            state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                            if state == False: return False
                        else:
                            return False
                    elif "<" in parte2:
                        partesCondicion2 = parte2.split("<")
                        for aux in partesCondicion2:
                            if aux.isspace() or len(aux) == 0: return False
                        if len(partesCondicion2) == 2:
                            state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                            if state == False: return False
                            state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                            if state == False: return False
                        else:
                            return False
                    elif ">" in parte2:
                        partesCondicion2 = parte2.split(">")
                        for aux in partesCondicion2:
                            if aux.isspace() or len(aux) == 0: return False
                        if len(partesCondicion2) == 2:
                            state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                            if state == False: return False
                            state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                            if state == False: return False
                        else:
                            return False
                    elif "==" in parte2:
                        partesCondicion2 = parte2.split("==")
                        for aux in partesCondicion2:
                            if aux.isspace() or len(aux) == 0: return False
                        if len(partesCondicion2) == 2:
                            state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                            if state == False: return False
                            state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                            if state == False: return False
                        else:
                            return False
                    elif "!=" in parte2:
                        partesCondicion2 = parte2.split("!=")
                        for aux in partesCondicion2:
                            if aux.isspace() or len(aux) == 0: return False
                        if len(partesCondicion2) == 2:
                            state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                            if state == False: return False
                            state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                            if state == False: return False
                        else:
                            return False
                    elif len(parte2) == 0:
                        return False
                    elif parte2.isspace():
                        return False
                    else:
                        state = bool(re.match(self.patronVarible, parte2.strip(' ')))
                        if not state: return False
            else:
                if "<=" in parte:
                    partesCondicion2 = parte.split("<=")
                    for aux in partesCondicion2:
                        if aux.isspace() or len(aux) == 0: return False
                    if len(partesCondicion2) == 2:
                        state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                        if state == False: return False
                        state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                        if state == False: return False
                    else:
                        return False
                elif ">=" in parte:
                    partesCondicion2 = parte.split(">=")
                    for aux in partesCondicion2:
                        if aux.isspace() or len(aux) == 0: return False
                    if len(partesCondicion2) == 2:
                        state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                        if state == False: return False
                        state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                        if state == False: return False
                    else:
                        return False
                elif "<" in parte:
                    partesCondicion2 = parte.split("<")
                    for aux in partesCondicion2:
                        if aux.isspace() or len(aux) == 0: return False
                    if len(partesCondicion2) == 2:
                        state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                        if state == False: return False
                        state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                        if state == False: return False
                    else:
                        return False
                elif ">" in parte:
                    partesCondicion2 = parte.split(">")
                    for aux in partesCondicion2:
                        if aux.isspace() or len(aux) == 0: return False
                    if len(partesCondicion2) == 2:
                        state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                        if state == False: return False
                        state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                        if state == False: return False
                    else:
                        return False
                elif "==" in parte:
                    partesCondicion2 = parte.split("==")
                    for aux in partesCondicion2:
                        if aux.isspace() or len(aux) == 0: return False
                    if len(partesCondicion2) == 2:
                        state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                        if state == False: return False
                        state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                        if state == False: return False
                    else:
                        return False
                elif "!=" in parte:
                    partesCondicion2 = parte.split("!=")
                    for aux in partesCondicion2:
                        if aux.isspace() or len(aux) == 0: return False
                    if len(partesCondicion2) == 2:
                        state = bool(re.match(self.patronVarible, partesCondicion2[0].strip(' ')))
                        if state == False: return False
                        state = bool(re.match(self.patronVarible, partesCondicion2[1].strip(' ')))
                        if state == False: return False
                    else:
                        return False
                elif len(parte) == 0:
                    return False
                elif parte.isspace():
                    return False
                else:
                    state = bool(re.match(self.patronVarible, parte.strip(' ')))
                    if not state: return False

        return [isValido, listaCondiciones]

    # funcion principal para validar sintaxis ciclo mientras
    def cicloMientras(self, linea, indexLinea):
        if self.valPalabraCicloMientras(linea)[0]:
            if self.valCondicionCicloMientras(linea, "MIENTRAS", 8, linea.find("HACER")):
                if self.validarcierreCiclo("FINM", "MIENTRAS", indexLinea):
                    return True
                else:
                    self.errores.append(["error etiqueta cierre ciclo mientras linea:", indexLinea + 1])
                    return False
            else:
                self.errores.append(["error condicion ciclo mientras", indexLinea + 1])
                return False
        else:
            self.errores.append([self.valPalabraCicloMientras(linea)[1], " | Error en la linea Numero: ", indexLinea + 1])
            return False

#################################################################################################

    # funcion para mapear de pseudo-codigo a lenguaje Java, el ciclo mientras
    def mapCicloMientrasJava(self, linea, indexLinea):
        linea = linea.replace('|', '||')
        linea = linea.replace('&', '&&')
        rangoCondicion = slice(linea.find("MIENTRAS") + 8, linea.find("HACER"))
        condicion = linea[rangoCondicion].strip(' ')

        auxlinea = "while(" + condicion + ") {"
        self.lines[self.indexCierreCiclo("FINM", "MIENTRAS", indexLinea)] = "}"
        self.lines[indexLinea] = auxlinea

#################################################################################################

    # funcion para mapear de pseudo-codigo a lenguaje PYTHON, el ciclo mientras
    def mapCicloMientrasPython(self, linea, indexLinea):
        linea = linea.replace('|', '||')
        linea = linea.replace('&', '&&')
        rangoCondicion = slice(linea.find("MIENTRAS") + 8, linea.find("HACER"))
        condicion = linea[rangoCondicion].strip(' ')
        tabs=slice(0,self.lines[indexLinea].find("MIENTRAS"))
        auxlinea =self.lines[indexLinea][tabs]+"while " + condicion + ":"
        finLinea=self.indexCierreCiclo("FINM", "MIENTRAS", indexLinea)
        self.lines[indexLinea] = auxlinea
        for i in range(indexLinea+1,finLinea):
            self.lines[i] = "~~~"+self.lines[i]
        self.lines[finLinea] = self.lines[finLinea].replace("FINM","~~~")

    # funcion para mapear de pseudo-codigo a lenguaje PYTHON, el ciclo HAz
    def mapCicloHazPython(self, linea, indexLinea):
        linea = linea.replace('|', '||')
        linea = linea.replace('&', '&&')
        
        finLinea=self.indexCierreCiclo("HASTA", "HAZ", indexLinea)

        lineaCierreCiclo = self.lines[finLinea]
        rango = slice(lineaCierreCiclo.find("HASTA") + 5, len(lineaCierreCiclo))
        condicion = lineaCierreCiclo[rango].strip(' ')


        tabs=slice(0,self.lines[indexLinea].find("HAZ"))
        tabs=self.lines[indexLinea][tabs].replace("\t","~~~")

        

        self.lines[indexLinea] = tabs+"est=True"

        auxlinea =tabs+"while " + condicion + " or est:"
        self.lines.insert(indexLinea+1,auxlinea)

        auxlinea="~~~"+tabs+"if est:"
        self.lines.insert(indexLinea+2,auxlinea)
        ##tabs=""
        auxlinea="~~~"+tabs+"est=False"
        self.lines.insert(indexLinea+3,auxlinea)
        auxlinea="~~~"+tabs+"|"
        self.lines.insert(indexLinea+4,auxlinea)
        finLinea=self.indexCierreCiclo("HASTA", "HAZ", indexLinea)
        for i in range(indexLinea+5,finLinea):
            self.lines[i] = "~~~"+self.lines[i]
        
        self.lines[finLinea] = self.lines[finLinea][slice(0,lineaCierreCiclo.find("HASTA"))]
#############################################################################################

    ##funcion para mapear de pseudo-codigo a lenguaje JAVA, el ciclo haz
    def mapCicloHazJava(self, linea, indexLinea):
        self.lines[indexLinea] = "do{"
        lineaCierreCiclo = self.lines[self.indexCierreCiclo("HASTA", "HAZ", indexLinea)]
        rango = slice(lineaCierreCiclo.find("HASTA") + 5, len(lineaCierreCiclo))
        condicion = lineaCierreCiclo[rango].strip(' ')
        condicion = condicion.replace('|', '||')
        condicion = condicion.replace('&', '&&')
        auxlinea = "}while(" + condicion + ")"
        self.lines[self.indexCierreCiclo("HASTA", "HAZ", indexLinea)] = auxlinea

    # funcion para validar las palabras reservadas para el ciclo haz
    def cicloHaz(self, linea, indexLinea):
        if self.indexCierreCiclo("HASTA", "HAZ", indexLinea) != -1:
            lineaCierreCiclo = self.lines[self.indexCierreCiclo("HASTA", "HAZ", indexLinea)]
            if self.valCondicionCicloMientras(lineaCierreCiclo, "HASTA", 5, len(lineaCierreCiclo)):
                return True
            else:
                self.errores.append(["error condicion ciclo haz", indexLinea + 1])
                return False
        else:
            self.errores.append(["error etiqueta cierre ciclo haz linea:", indexLinea + 1])
            return False

    # funcion para recorrer linea a linea y validar si hay ciclos y pasar a mapear a (Java).
    def mapCiclosJava(self):
        for i in range(0, len(self.lines)):
            line = self.lines[i] #.strip(' ')
            if re.match(r'^( |~~~)*PARA', line):
                if self.valCicloPara(line, i):  # validar si el ciclo para esta bien escrito
                    if self.valPalabrasReservadasPara(line, i): #validar que no contenga palabras reservadas
                        self.mapCicloParaJava(line, i)  # mapear ciclo para a sintaxis en Java

            if re.match(r'^( |~~~)*MIENTRAS',line):
                if self.cicloMientras(line, i):  # validar si el ciclo para esta bien escrito
                    if self.valPalabrasReservadasMientras(line,"MIENTRAS",8,line.find("HACER"), i):
                        self.mapCicloMientrasJava(line, i)  # mapear ciclo mientras a sintaxis en Java

            if re.match(r'^( |~~~)*HAZ',line):
                if self.cicloHaz(line, i):  # validar si el ciclo para esta bien escrito
                    lineaCierreCiclo = self.lines[self.indexCierreCiclo("HASTA", "HAZ", i)]
                    if self.valPalabrasReservadasMientras(lineaCierreCiclo,  "HASTA", 5, len(lineaCierreCiclo), i):
                        self.mapCicloHazJava(line, i)  # mapear ciclo Haz a sintaxis en Java


   # funcion para recorrer linea a linea y validar si hay ciclos y pasar a mapear a (Python).
    def mapCiclosPython(self):
        for i in range(0, len(self.lines)):
            line = self.lines[i] #.strip(' ')
            print(line)
            if re.match(r'^( |~~~|\t)*PARA', line):
                if self.valCicloPara(line, i):  # validar si el ciclo para esta bien escrito
                    if self.valPalabrasReservadasPara(line, i): #validar que no contenga palabras reservadas
                        self.mapCicloParaPython(line, i)  # mapear ciclo para a sintaxis en Python

            if re.match(r'^( |~~~|\t)*MIENTRAS',line):
                if self.cicloMientras(line, i):  # validar si el ciclo para esta bien escrito
                    if self.valPalabrasReservadasMientras(line,"MIENTRAS",8,line.find("HACER"), i):
                        self.mapCicloMientrasPython(line, i)  # mapear ciclo mientras a sintaxis en Python
            
            if re.match(r'^( |~~~|\t)*HAZ',line):
                if self.cicloHaz(line, i):  # validar si el ciclo para esta bien escrito
                    lineaCierreCiclo = self.lines[self.indexCierreCiclo("HASTA", "HAZ", i)]
                    if self.valPalabrasReservadasMientras(lineaCierreCiclo,  "HASTA", 5, len(lineaCierreCiclo), i):
                        size=len(self.lines)
                        self.mapCicloHazPython(line, i)  # mapear ciclo Haz a sintaxis en Python
                        if(size<len(self.lines)):
                            self.mapCiclosPython()

    def getLine(self):
        for i in range(0, len(self.lines)):
            self.lines[i]=self.lines[i].replace("~~~ ","\t")
            self.lines[i]=self.lines[i].replace("~~~","\t")
           
        return self.lines
 