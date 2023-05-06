import re

RE_DATO = re.compile('ENTERO|REAL|CARACTER|BOOLEANO')  # TIPO DE DATO
RE_IO = re.compile('LEER|ESCRIBIR')

# PALABRAS RESERVADAS
RE_LATTER_RES_PSU = re.compile('ENTERO|CARACTER|REAL|BOOLEANO|FUNCION|RETORNA|FINF|SI|FSI|SINO|FSINO|HAZ|FHAZ|'
                               'MIENTRAS|FINM|ENTONCES|PARA|FPARA|SEGUN|FSEGUN|HACER|CASO|ROMPER|DEOTROMODO|'
                               'HASTA|FINP|ESCRIBIR|LEER|INICIO|FINAL|VERDADERO|FALSO')  # IDENTIFICADOR RESERVADAS
RE_LATTER_RES_PSU_B = re.compile('ENTERO|CARACTER|REAL|BOOLEANO|FUNCION|RETORNA|FINF|SI|FSI|SINO|FSINO|HAZ|FHAZ|'
                                 'MIENTRAS|FINM|ENTONCES|PARA|FPARA|SEGUN|FSEGUN|HACER|CASO|ROMPER|DEOTROMODO|'
                                 'HASTA|FINP|ESCRIBIR|LEER|INICIO|FINAL')  # IDENTIFICADOR RESERVADAS

# PALABRAS
RE_WORD = re.compile(r'[a-zA-Z]+(\w)*')  # PALABRA
RE_VS = re.compile(r'([a-zA-Z]+(\w)*)((,)([a-zA-Z]+(\w)*))*')   # COSA
RE_VAR = re.compile(r'(([a-zA-Z]+(\w)*)((\[(([a-zA-Z]+(\w)*)|([0-9]+))])|'
                    r'((\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))]))|))')  # VARIABLE
RE_VARS = re.compile(r'((([a-zA-Z]+(\w)*)((\[(([a-zA-Z]+(\w)*)|([0-9]+))])|'
                     r'((\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))]))|))((,)'
                     r'(([a-zA-Z]+(\w)*)((\[(([a-zA-Z]+(\w)*)|([0-9]+))])|'
                     r'((\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))]))|)))*)')  # VARIABLES
RE_NUM_REL = re.compile(r'((-|)[0-9]+)((.[0-9]+)|)')  # NUMERO
RE_VAL = re.compile(r'((([a-zA-Z]+(\w)*)((\[(([a-zA-Z]+(\w)*)|([0-9]+))])|'
                    r'((\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))]))|'
                    r'))|(((-|)[0-9]+)((\.[0-9]+)|))|(\'[^\\\n]\'))')  # VARIABLE/VALOR
RE_FUN = re.compile(r'([a-zA-Z]+(\w)*)' + r'(\(((' + RE_VAL.pattern +
                    '((,)' + RE_VAL.pattern + ')*' + r')|)\)' + '|' + r'(\(\)))')  # FUNCION
RE_SYM = re.compile(r'(\+|-|\*|/|\*\*|%)')  # SIMBOLO
RE_ES = re.compile(r'( )+')  # ESPACIOS
RE_TEXT = re.compile(r'((\"([^\\\n"])+\")|"")')  # TEXTO
RE_STR = re.compile(r'((\"([^\\\n" ])+\")|"")')  # TEXTO para variables

# GENERICOS
RE_VEC_GEN = re.compile(r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))]))((,)'
                        r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])))*')
RE_MAT_GEN = re.compile(r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))]))((,)'
                        r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])))*')
RE_MATT = re.compile(r'([a-zA-Z]+(\w)*)(([a-zA-Z]+(\w)*)(\[]))(\[(([a-zA-Z]+(\w)*)|([0-9]+))])')
RE_VM_GEN = re.compile('(' + RE_VEC_GEN.pattern + '|' + RE_MAT_GEN.pattern + ')')
RE_ASI_GEN = re.compile(r'(([a-zA-Z]+(\w)*)|)')
RE_VGI = re.compile(r'((([a-zA-Z]+(\w)*)(\[]))|' + RE_VEC_GEN.pattern + ')')
RE_OP = re.compile('(' + RE_VAR.pattern + '|' + RE_NUM_REL.pattern + '|' + RE_FUN.pattern + ')(' + RE_SYM.pattern +
                   '(' + RE_VAR.pattern + '|' + RE_NUM_REL.pattern + '|' + RE_FUN.pattern + '))*')
RE_VO = re.compile(r'(' + RE_VAR.pattern + '|' + RE_NUM_REL.pattern + '|' + RE_FUN.pattern + ')')

# ENTEROS
RE_VAR_ENT = re.compile(r'([a-zA-Z]+(\w)*(=(([a-zA-Z]+(\w)*)|((-|)[0-9]+))|))((,)'
                        r'([a-zA-Z]+(\w)*(=(([a-zA-Z]+(\w)*)|((-|)[0-9]+))|)))*')
RE_VEC_ENT = re.compile(r'(([a-zA-Z]+(\w)*)(\[])(={((([a-zA-Z]+(\w)*)|((-|)[0-9]+))((,)(([a-zA-Z]+(\w)*)'
                        r'|((-|)([0-9]+))))*)}))((,)([a-zA-Z]+(\w)*)(\[])(={((([a-zA-Z]+(\w)*)|((-|)[0-9]+))'
                        r'((,)(([a-zA-Z]+(\w)*)|((-|)([0-9]+))))*)}))*')
RE_MAT_ENT = re.compile(r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={({((([a-zA-Z]+(\w)*)|((-|)[0-9]+))((,)(([a-zA-Z]+(\w)*)|((-|)[0-9]+)))*)}'
                        r'((,)({((([a-zA-Z]+(\w)*)|((-|)[0-9]+))((,)(([a-zA-Z]+(\w)*)|((-|)[0-9]+)))*)}))*)}))((,)'
                        r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={({((([a-zA-Z]+(\w)*)|((-|)[0-9]+))((,)(([a-zA-Z]+(\w)*)|((-|)[0-9]+)))*)}'
                        r'((,)({((([a-zA-Z]+(\w)*)|((-|)[0-9]+))((,)(([a-zA-Z]+(\w)*)|((-|)[0-9]+)))*)}))*)})))*')
RE_ENT = re.compile('(' + RE_VAR_ENT.pattern + '|' + RE_VEC_ENT.pattern + '|' + RE_MAT_ENT.pattern + ')')

# REALES
RE_VAR_REL = re.compile(r'([a-zA-Z]+(\w)*(=(([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|)))|)((,)'
                        r'([a-zA-Z]+(\w)*(=(([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|)))|)))*)')
RE_VEC_REL = re.compile(r'(([a-zA-Z]+(\w)*)(\[])(={((([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|)))'
                        r'((,)(([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|))))*)}))((,)(([a-zA-Z]+(\w)*)(\[])'
                        r'(={((([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|)))'
                        r'((,)(([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|))))*)})))*')
RE_MAT_REL = re.compile(r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={({((([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|)))((,)'
                        r'(([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|))))*)}((,)'
                        r'({((([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|)))((,)'
                        r'(([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|))))*)}))*)}))((,)'
                        r'([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={({((([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|)))((,)'
                        r'(([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|))))*)}((,)'
                        r'({((([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((.[0-9]+)|)))((,)'
                        r'(([a-zA-Z]+(\w)*)|(((-|)[0-9]+)((\.[0-9]+)|))))*)}))*)}))*')
RE_REL = re.compile('(' + RE_VAR_REL.pattern + '|' + RE_VEC_REL.pattern + '|' + RE_MAT_REL.pattern + ')')

# CARACTER
RE_VAR_CAR = re.compile(r'([a-zA-Z]+(\w)*(=(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|))((,)'
                        r'([a-zA-Z]+(\w)*(=(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|)))*')
RE_VEC_CAR = re.compile(r'(([a-zA-Z]+(\w)*)(\[])((={(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))((,)'
                        r'(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\')))*})|=(\"(([^´\'\n\\])|( ))+\")|=("")))((,)'
                        r'(([a-zA-Z]+(\w)*)(\[])((={(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))((,)'
                        r'(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\')))*})|=(\"(([^´\'\n\\])|( ))+\")|=(""))))*')
RE_MAT_CAR = re.compile(r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={({(((([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|(\"(([^´\'\n\\])|( ))+\"))((,)'
                        r'((([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|(\"(([^´\'\n\\])|( ))+\")))*)}((,)'
                        r'({(((([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|(\"(([^´\'\n\\])|( ))+\"))((,)'
                        r'((([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|(\"(([^´\'\n\\])|( ))+\")))*)}))*)}))((,)'
                        r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={({(((([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|(\"(([^´\'\n\\])|( ))+\"))((,)'
                        r'((([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|(\"(([^´\'\n\\])|( ))+\")))*)}((,)'
                        r'({(((([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|(\"(([^´\'\n\\])|( ))+\"))((,)'
                        r'((([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))|(\"(([^´\'\n\\])|( ))+\")))*)}))*)})))*')
RE_MAT_CRC = re.compile(r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={(({(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))((,)(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))))|'
                        r''
                        r')}((,)'
                        r'({(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))((,)(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\')))}'
                        r'))*)})((,)(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={({(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))((,)(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))))}((,)'
                        r'({(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\'))((,)(([a-zA-Z]+(\w)*)|(\'[^´\'\n\\]\')))}))*)}))')
RE_CAR = re.compile('(' + RE_VAR_CAR.pattern + '|' + RE_VEC_CAR.pattern + '|' + RE_MAT_CAR.pattern + ')')

# BOOLEANO
RE_VAR_BOO = re.compile(r'([a-zA-Z]+(\w)*(=(([a-zA-Z]+(\w)*)|0|1)|))((,)'
                        r'([a-zA-Z]+(\w)*(=(([a-zA-Z]+(\w)*)|0|1)|)))*')
RE_VEC_BOO = re.compile(r'((([a-zA-Z]+(\w)*)(\[])(={((([a-zA-Z]+(\w)*)|0|1)((,)(([a-zA-Z]+(\w)*)|0|1))*)}))((,)'
                        r'(([a-zA-Z]+(\w)*)(\[])(={((([a-zA-Z]+(\w)*)|0|1)((,)(([a-zA-Z]+(\w)*)|0|1))*)})))*)')
RE_MAT_BOO = re.compile(r'(([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={({((([a-zA-Z]+(\w)*)|0|1)((,)(([a-zA-Z]+(\w)*)|0|1))*)}'
                        r'((,)({((([a-zA-Z]+(\w)*)|0|1)((,)(([a-zA-Z]+(\w)*)|0|1))*)}))*)})((,)'
                        r'([a-zA-Z]+(\w)*)(\[(([a-zA-Z]+(\w)*)|([0-9]+))])(\[(([a-zA-Z]+(\w)*)|([0-9]+))])'
                        r'(={({((([a-zA-Z]+(\w)*)|0|1)((,)(([a-zA-Z]+(\w)*)|0|1))*)}'
                        r'((,)({((([a-zA-Z]+(\w)*)|0|1)((,)(([a-zA-Z]+(\w)*)|0|1))*)}))*)}))*)')
RE_BOO = re.compile('(' + RE_VAR_BOO.pattern + '|' + RE_VEC_BOO.pattern + '|' + RE_MAT_BOO.pattern + ')')

RE_TDATA = re.compile('(' + RE_ENT.pattern + '|' + RE_REL.pattern + '|' + RE_CAR.pattern + '|' + RE_BOO.pattern + '|' +
                      RE_VM_GEN.pattern + ')')

# ASIGNACION
RE_ASI = re.compile('(' + '(' + RE_VAL.pattern + '|' + RE_FUN.pattern + ')' +
                    '(' + RE_SYM.pattern + '(' + RE_VAL.pattern + '|' + RE_FUN.pattern + ')' + ')*)')
RE_ASI_PAR = re.compile(r'\(' + '(' + RE_VAL.pattern + '|' + RE_FUN.pattern + ')' +
                        '(' + RE_SYM.pattern + '(' + RE_VAL.pattern + '|' + RE_FUN.pattern + ')' + r'\)*)')
RE_ASI_VAL = re.compile(RE_VAR.pattern + '=' + '(' + RE_ASI.pattern + '|' + RE_ASI_PAR.pattern + ')((' + RE_SYM.pattern
                        + ')(' + RE_ASI.pattern + '|' + RE_ASI_PAR.pattern + '))*')

# I/O
RE_WRITE = re.compile(RE_TEXT.pattern + RE_ES.pattern + RE_VAR.pattern + '|' + RE_TEXT.pattern + '|' + RE_VAR.pattern)
RE_WRT = re.compile(RE_TEXT.pattern + RE_ES.pattern + RE_OP.pattern + '|' + RE_OP.pattern)
RE_READ = re.compile(RE_VAR.pattern)
RE_I_O = re.compile(RE_WRITE.pattern + '|' + RE_READ.pattern)


# Funcion para pegar la lista en una cadena
def paste_string(cadena, tipo):
    string = ""
    if tipo == "ND":
        string = ''.join(cadena)
    elif tipo == "C":
        string = ','.join(cadena)
    elif tipo == "E":
        string = ' '.join(cadena)
    elif tipo == "CE":
        string = ', '.join(cadena)
    elif tipo == "LCE":
        string = '}, '.join(cadena)
    return string


# Funcion que verifica las expresiones
def val_dec(lista, tipo):
    # VALIDAR DECLARACION
    val = False
    string_aux = paste_string(lista, "ND")
    if tipo == "ENTERO":
        if val_let(string_aux, tipo):
            val = True
    elif tipo == "REAL":
        if val_let(string_aux, tipo):
            val = True
    elif tipo == "CARACTER":
        if val_let(string_aux, tipo):
            val = True
    elif tipo == "BOOLEANO":
        if val_let(string_aux, tipo):
            val = True
    else:
        if val_let(string_aux, tipo):
            val = True
    return val


# Funcion que verifica las palabras reservadas
def val_let(cadena, tipo):
    val = False
    lista_aux = cadena.split(',')
    for x in lista_aux:
        string_aux = x.split('=')
        for y in string_aux:
            cc_aux = y.replace('{', '').replace('}', '')
            # print("ANALIZANDO: ", cc_aux)
            if tipo == "BOOLEANO":
                if re.search(r'\[', cc_aux):
                    val = val_cor(cc_aux)
                    if not val:
                        break
                else:
                    if re.fullmatch(RE_LATTER_RES_PSU_B, cc_aux.upper()):
                        val = False
                        break
            else:
                if re.search(r'\[', cc_aux):
                    val = val_cor(cc_aux)
                    if val:
                        break
                else:
                    if re.fullmatch(RE_LATTER_RES_PSU, cc_aux.upper()):
                        # print("ENTRE DE NUEVO")
                        val = True
                        break
        if val:
            # print("PALABRA RESERVADA")
            break
    return val


# Funcion que verifica las palabras reservadas dentro de corchetes
def val_cor(cadena):
    val = False
    lista_aux = cadena.split('[')
    if re.fullmatch(RE_LATTER_RES_PSU, lista_aux[0].upper()):
        val = True
    else:
        for z in lista_aux:
            if re.search(r']$', z):
                z = z.replace(']', '')
                if re.fullmatch(RE_LATTER_RES_PSU, z.upper()):
                    val = True
                    break
    return val


def ver_memoria(l_memoria, cadena, formato):
    val_ver = False
    l_mm = l_memoria
    l_aux = []
    if formato == "C":
        new_form = "S"
    else:
        new_form = formato
    for w in l_mm:
        l_aux.append(w[0])
    print("MIRA CADENA:", cadena)
    print("#######################################################################")
    if re.fullmatch(RE_VS, cadena.split('=')[0]):
        lista_palabras = cadena.split(',')
        print("ENTRE VARIABLE")
        for x in range(len(lista_palabras)):
            lista_aux = lista_palabras[x].split('=')
            for y in range(len(lista_aux)):
                name = lista_aux[0]
                if y == 0:
                    if len(l_mm) == 0:
                        l_mm.append([name, formato, "VA"])
                        l_aux.append(name)
                    else:
                        # l_m = list(map(str.upper, l_aux))
                        if name.upper() not in l_aux:
                            l_mm.append([name, formato, "VA"])
                            l_aux.append(name)
                        else:
                            val_ver = True
                            break
            if val_ver:
                break
        print("MEMORIA ACTUAL", l_mm)
    elif re.fullmatch(RE_VGI, cadena.split('=')[0]):
        if re.fullmatch(RE_VEC_GEN, cadena):
            print("ENTRE VECTOR G")
            lista_palabras = cadena.split(',')
            for x in range(len(lista_palabras)):
                lista_aux = lista_palabras[x].split("[")
                for y in range(len(lista_aux)):
                    name = lista_aux[0]
                    if y == 0:
                        if len(l_mm) == 0:
                            l_mm.append([name, new_form, "VT"])
                            l_aux.append(name)
                        else:
                            # l_m = list(map(str.upper, l_aux))
                            if name.upper() not in l_aux:
                                l_mm.append([name, new_form, "VT"])
                                l_aux.append(name)
                            else:
                                val_ver = True
                                break
                if val_ver:
                    break
            print("MEMORIA ACTUAL", l_mm)
        else:
            print("ENTRE VECTOR IN")
            lista_palabras = cadena.split('},')
            for x in range(len(lista_palabras)):
                lista_aux = lista_palabras[x].split("=")
                for y in range(len(lista_aux)):
                    name = lista_aux[0]
                    name = name.replace('[', '').replace(']', '')
                    if y == 0:
                        if len(l_mm) == 0:
                            l_mm.append([name, new_form, "VT"])
                            l_aux.append(name)
                        else:
                            # l_m = list(map(str.upper, l_aux))
                            if name.upper() not in l_aux:
                                l_mm.append([name, new_form, "VT"])
                                l_aux.append(name)
                            else:
                                val_ver = True
                                break
                if val_ver:
                    break
            print("MEMORIA ACTUAL", l_mm)
    else:
        if re.fullmatch(RE_MAT_GEN, cadena.split('=')[0]):
            print("ENTRE MATRIZ G")
            lista_palabras = cadena.split(',')
            for x in range(len(lista_palabras)):
                lista_aux = lista_palabras[x].split('[')
                for y in range(len(lista_aux)):
                    name = lista_aux[0]
                    if y == 0:
                        if len(l_mm) == 0:
                            l_mm.append([name, new_form, "MT"])
                            l_aux.append(name)
                        else:
                            # l_m = list(map(str.upper, l_aux))
                            if name.upper() not in l_aux:
                                l_mm.append([name, new_form, "MT"])
                                l_aux.append(name)
                            else:
                                val_ver = True
                                break
                if val_ver:
                    break
            print("MEMORIA ACTUAL", l_mm)
        else:
            print("ENTRE MATRIZ IN")
            lista_palabras = cadena.split('}},')
            for x in range(len(lista_palabras)):
                lista_aux = lista_palabras[x].split('[')
                for y in range(len(lista_aux)):
                    name = lista_aux[0]
                    if y == 0:
                        if len(l_mm) == 0:
                            l_mm.append([name, new_form, "MT"])
                            l_aux.append(name)
                        else:
                            # l_m = list(map(str.upper, l_aux))
                            if name.upper() not in l_aux:
                                l_mm.append([name, new_form, "MT"])
                                l_aux.append(name)
                            else:
                                val_ver = True
                                break
                if val_ver:
                    break
            print("MEMORIA ACTUAL", l_mm)
    return val_ver


def buscar_m(l_memoria, variable):
    cen = False
    ind = None
    for fila in range(len(l_memoria)):
        if l_memoria[fila][0] == variable:
            cen = True
            ind = fila
            break
    return cen, ind


def del_lis(lista):
    ls_vvm = []
    va = None
    for a in range(len(lista)):
        if re.fullmatch(RE_VO, lista[a]):
            if not re.fullmatch(RE_NUM_REL, lista[a]):
                ls_vvm.append(lista[a])
            else:
                if va is None:
                    if lista[a].isdigit():
                        va = "E"
                    else:
                        va = "R"
    return va, ls_vvm


def translator_dato(cadena, word, gen, tab):
    lista_aux = cadena.split()
    cadena_aux = ''.join(lista_aux)
    cadena_c = ""
    cadena_j = ""
    cadena_p = ""
    l_retorno = []
    lista_var = []
    lista_arg = []
    lista_argp = []
    lista_lim = []
    lista_py = []
    sym_tab = '\t'
    stab = sym_tab * tab
    if gen:
        if word == "ENTERO":
            tipo = "int "
        elif word == "REAL":
            tipo = "float "
        elif word == "CARACTER":
            tipo = "char "
        else:
            tipo = "bool "
        if re.fullmatch(RE_VEC_GEN, cadena_aux):
            cadena_c = tipo + cadena_aux + ";"
            cadena_c = cadena_c.replace(',', ', ')
            for itr in lista_aux:
                lista_ax = itr.split(',')
                for it in lista_ax:
                    cc_aux = it.replace(']', '')
                    l_aux = cc_aux.split('[')
                    lista_var.append(l_aux[0])
                    lista_arg.append(l_aux[1])
            cadena_p = stab + paste_string(lista_var, "CE") + " = "
            if word == "BOOLEANO":
                tipo = "boolean "
            for itr in range(len(lista_var)):
                if itr == 0:
                    cadena_j = tipo + lista_var[itr] + "[] = new " + tipo + "[" + lista_arg[itr] + "]"
                else:
                    cadena_j = cadena_j + lista_var[itr] + "[] = new " + tipo + "[" + lista_arg[itr] + "]"
                if itr <= (len(lista_var) - 1):
                    if itr != (len(lista_var) - 1):
                        cadena_j = cadena_j + ", "
                    if itr > 0:
                        cadena_p = cadena_p + ", "
                cadena_p = cadena_p + "[]"
            cadena_j = cadena_j + ";"
            lista_py.append(cadena_p)
        else:
            cadena_c = tipo + cadena_aux + ";"
            cadena_c = cadena_c.replace(',', ', ')
            lista_aux = cadena_aux.replace('][', '|').replace(']', '').split(',')
            if word == "BOOLEANO":
                tipo = "boolean "
            for it in lista_aux:
                l_ax = it.split('[')
                lista_var.append(l_ax[0])
                cc_aux = "[" + l_ax[1] + "]"
                cc_aux = cc_aux.replace('|', '][')
                lista_arg.append(cc_aux)
            for itr in range(len(lista_var)):
                cadena_p = ""
                if itr == 0:
                    cadena_j = tipo + lista_var[itr] + "[][] = new " + tipo + lista_arg[itr]
                    limpy = (paste_string(lista_arg[itr], "ND")).split('][')
                    nf = limpy[0].replace('[', '')
                    nc = limpy[1].replace(']', '')
                    cadena_p = stab + lista_var[itr] + " = []"
                    lista_py.append(cadena_p)
                    cadena_p = stab + "for i in range(" + nf + "):"
                    lista_py.append(cadena_p)
                    cadena_p = stab + "\t" + lista_var[itr] + stab + ".append([None] * " + nc + ")"
                    lista_py.append(cadena_p)
                else:
                    limpy = (paste_string(lista_arg[itr], "ND")).split('][')
                    nf = limpy[0].replace('[', '')
                    nc = limpy[1].replace(']', '')
                    cadena_j = cadena_j + lista_var[itr] + "[][] = new " + tipo + lista_arg[itr]
                    cadena_p = stab + lista_var[itr] + " = []"
                    lista_py.append(cadena_p)
                    cadena_p = stab + "for i in range(" + nf + "):"
                    lista_py.append(cadena_p)
                    cadena_p = stab + "\t" + lista_var[itr] + stab + ".append([None] * " + nc + ")"
                    lista_py.append(cadena_p)
                if itr < len(lista_var) - 1:
                    cadena_j = cadena_j + ", "
                else:
                    cadena_j = cadena_j + ";"
    else:
        if word == "ENTERO":
            if re.fullmatch(RE_VAR_ENT, cadena_aux):
                cadena_c = ("int " + cadena_aux + ";").replace('=', ' = ').replace(',', ', ')
                cadena_j = ("int " + cadena_aux + ";").replace('=', ' = ').replace(',', ', ')
                lista_aux = cadena_aux.split(',')
                for itr in lista_aux:
                    lista_ax = itr.split('=')
                    if len(lista_ax) > 1:
                        lista_var.append(lista_ax[0])
                        lista_arg.append(lista_ax[1])
                    else:
                        lista_var.append(lista_ax[0])
                        lista_arg.append("None")
                cad_var = paste_string(lista_var, "CE")
                cad_arg = paste_string(lista_arg, "CE")
                cadena_p = stab + cad_var + " = " + cad_arg
            elif re.fullmatch(RE_VEC_ENT, cadena_aux):
                cadena_c = ("int " + cadena_aux + ";").replace('=', ' = ').replace('},', '}, ')
                cadena_j = ("int " + cadena_aux + ";").replace('=', ' = ').replace('},', '}, ')
                for itr in lista_aux:
                    lista_ax = itr.split('},')
                    for it in lista_ax:
                        l_aux = it.split('[]=')
                        lista_var.append(l_aux[0])
                        lista_arg.append(l_aux[1])
                cadena_p = stab + paste_string(lista_var, "CE") + " = " + paste_string(lista_arg, "LCE")
                cadena_p = cadena_p.replace('{', '[').replace('}', ']')
            elif re.fullmatch(RE_MAT_ENT, cadena_aux):
                cadena_c = ("int " + cadena_aux + ";").replace('=', ' = ').replace('},', '}, ')
                lista_aux = cadena_aux.split('}},')
                for it in lista_aux:
                    l_aux = it.split('=')
                    for ite in l_aux:
                        if re.fullmatch(RE_MAT_GEN, ite):
                            l_ax = ite.split('[')
                            lista_var.append(l_ax[0])
                        else:
                            lista_arg.append(ite + "}}")
                lista_arg[len(lista_arg) - 1] = lista_arg[len(lista_arg) - 1].replace('}}}}', '}}')
                for itr in range(len(lista_var)):
                    if itr == 0:
                        cadena_j = "int " + lista_var[itr] + " [][] = " + lista_arg[itr]
                    else:
                        cadena_j = cadena_j + lista_var[itr] + " [][] = " + lista_arg[itr]
                    if itr < len(lista_var) - 1:
                        cadena_j = cadena_j + ", "
                    else:
                        cadena_j = cadena_j + ";"
                cadena_j = cadena_j.replace('},{', '}, {')
                cadena_p = stab + paste_string(lista_var, "CE") + " = " + paste_string(lista_arg, "CE")
                cadena_p = cadena_p.replace('{', '[').replace('}', ']')
        if word == "REAL":  # Pegar traducciones
            if re.fullmatch(RE_VAR_REL, cadena_aux):
                cc_axj = ""
                cadena_c = ("float " + cadena_aux + ";").replace('=', ' = ').replace(',', ', ')
                lista_aux = cadena_aux.split(',')
                for itr in lista_aux:
                    lista_ax = itr.split('=')
                    if len(lista_ax) > 1:
                        lista_var.append(lista_ax[0])
                        lista_arg.append(lista_ax[1])
                    else:
                        lista_var.append(lista_ax[0])
                        lista_arg.append("None")
                for w in range(len(lista_var)):
                    cc_axj = cc_axj + lista_var[w]
                    if lista_arg[w] == "None":
                        cc_axj = cc_axj + ","
                    else:
                        if re.fullmatch(RE_NUM_REL, lista_arg[w]):
                            cc_axj = cc_axj + " = " + lista_arg[w] + "f,"
                        else:
                            cc_axj = cc_axj + " = " + lista_arg[w] + ","
                if cc_axj[-1] == ',':
                    cc_axj = cc_axj[:-1]
                cadena_j = ("float " + cc_axj + ";").replace(',', ', ')
                cadena_p = stab + paste_string(lista_var, "CE") + " = " + paste_string(lista_arg, "CE")
            elif re.fullmatch(RE_VEC_REL, cadena_aux):
                cadena_c = ("float " + cadena_aux + ";").replace('=', ' = ').replace('},', '}, ')
                lista_aux = cadena_aux.split('},')
                for x1 in lista_aux:
                    l_ax = x1.split('=')
                    for y in range(len(l_ax)):
                        if y == 1:
                            cc_aux = l_ax[y]
                            cc_aux = cc_aux.replace('{', '')
                            l_aux = cc_aux.split(',')
                            cont = 0
                            cc_ax = ""
                            cc_axp = ""
                            for z in l_aux:
                                if re.fullmatch(RE_NUM_REL, z):
                                    cc_ax = cc_ax + z + "f"
                                    cc_axp = cc_axp + z
                                else:
                                    cc_ax = cc_ax + z.replace('}', 'f}')
                                    cc_axp = cc_axp + z.replace('}', '')
                                if cont < (len(l_aux) - 1):
                                    cc_ax = cc_ax + ", "
                                    cc_axp = cc_axp + ", "
                                cont += 1
                            lista_arg.append(cc_ax)
                            cc_axp = "[" + cc_axp + "]"
                            lista_argp.append(cc_axp)
                        else:
                            cc_aux = l_ax[y]
                            lista_var.append(cc_aux)
                for z in range(len(lista_var)):
                    if z == 0:
                        cadena_j = "float " + lista_var[z] + " = {" + lista_arg[z]
                    else:
                        cadena_j = cadena_j + lista_var[z] + " = {" + lista_arg[z]
                    if z < (len(lista_var) - 1):
                        cadena_j = cadena_j + "}, "
                cadena_j = cadena_j + ";"
                cadena_p = stab + paste_string(lista_var, "CE").replace('[]', '') + " = "
                cadena_p = cadena_p + paste_string(lista_argp, "CE")
            elif re.fullmatch(RE_MAT_REL, cadena_aux):
                cadena_c = "float " + cadena_aux + ";"
                cadena_c = cadena_c.replace('},', '}, ').replace('=', ' = ')
                lista_aux = cadena_aux.split('}},')
                for a in lista_aux:
                    l_aux = a.split('=')
                    for b in l_aux:
                        if re.fullmatch(RE_MAT_GEN, b):
                            l_ax = b.split('[')
                            lista_var.append(l_ax[0])
                        else:
                            lista_argp.append(b + "}}")
                lista_argp[len(lista_argp) - 1] = lista_argp[len(lista_argp) - 1].replace('}}}}', '}}')
                for c in lista_argp:
                    cadena_aux = c.replace('{', '').replace('}}', '')
                    lista_aux = cadena_aux.split('},')
                    lista_axj = []
                    for d in lista_aux:
                        l_ax = d.split(',')
                        lista_ax = []
                        for e in l_ax:
                            if re.fullmatch(RE_NUM_REL, e):
                                cc_aux = e + "f"
                            else:
                                cc_aux = e
                            lista_ax.append(cc_aux)
                        cc = "{" + paste_string(lista_ax, "CE") + "}"
                        lista_axj.append(cc)
                    cc = paste_string(lista_axj, "CE")
                    lista_arg.append(cc)
                for it in range(len(lista_var)):
                    if it == 0:
                        cadena_j = "float " + lista_var[it] + "[][] = {" + lista_arg[it] + "}"
                    else:
                        cadena_j = cadena_j + lista_var[it] + "[][] = {" + lista_arg[it] + "}"
                    if it < len(lista_var) - 1:
                        cadena_j = cadena_j + ", "
                    else:
                        cadena_j = cadena_j + ";"
                cadena_p = stab + paste_string(lista_var, "CE") + " = " + paste_string(lista_argp, "CE")
                cadena_p = cadena_p.replace('{{', '[[').replace('}}', ']]').replace('},{', '], [')
        if word == "CARACTER":
            if re.fullmatch(RE_VAR_CAR, cadena_aux):
                cadena_c = ("char " + cadena_aux + ";").replace('=', ' = ').replace(',', ', ')
                cadena_j = ("char " + cadena_aux + ";").replace('=', ' = ').replace(',', ', ')
                lista_aux = cadena_aux.split(',')
                for v in lista_aux:
                    lista_ax = v.split('=')
                    if len(lista_ax) > 1:
                        lista_var.append(lista_ax[0])
                        lista_arg.append(lista_ax[1])
                    else:
                        lista_var.append(lista_ax[0])
                        lista_arg.append("None")
                cad_var = paste_string(lista_var, "CE")
                cad_arg = paste_string(lista_arg, "CE")
                cadena_p = stab + cad_var + " = " + cad_arg
            elif re.fullmatch(RE_VEC_CAR, cadena_aux):
                cadena_c = ("char " + cadena_aux + ";").replace('=', ' = ').replace('}', ',\'\\0\'}')
                cadena_c = cadena_c.replace('},', '}, ').replace('",', '", ')
                cadena_j = ("char " + cadena_aux + ";").replace('=', ' = ')
                cadena_j = cadena_j.replace('},', '}, ').replace('",', '", ')
                for x in lista_aux:
                    lista_ax = x.split("=")
                    for y in lista_ax:
                        ll_ax = y.split('},')
                        lc_ax = y.split('",')
                        if len(ll_ax) > len(lc_ax):
                            lax = y.split('},')
                            cc_r = lax[0] + "]"
                            cc_r = (cc_r[::-1][:-1] + "[")[::-1]
                            lista_arg.append(cc_r)
                            cc_r = lax[1].replace('[]', '')
                            lista_var.append(cc_r)
                        elif len(lc_ax) > len(ll_ax):
                            lax = y.split('",')
                            cc_r = lax[0] + "\""
                            lista_arg.append(cc_r)
                            cc_r = lax[1].replace('[]', '')
                            lista_var.append(cc_r)
                        else:
                            cc_r = y.replace('[', '').replace(']', '')
                            if re.fullmatch(RE_WORD, cc_r):
                                lista_var.append(cc_r)
                            else:
                                lista_arg.append(y)
                cadena_p = paste_string(lista_var, "CE") + " = " + paste_string(lista_arg, "CE")
            elif re.fullmatch(RE_MAT_CAR, cadena_aux):
                cadena_c = "char " + cadena_aux + ";"
                cadena_c = cadena_c.replace('},', '}, ').replace('}}', '}}').replace('=', ' = ')
                lista_aux = cadena_aux.split('}},')
                for a in lista_aux:
                    l_aux = a.split('=')
                    for b in l_aux:
                        if re.fullmatch(RE_MAT_GEN, b):
                            l_ax = b.split('[')
                            lista_var.append(l_ax[0])
                        else:
                            lista_arg.append(b + "}}")
                lista_arg[len(lista_arg) - 1] = lista_arg[len(lista_arg) - 1].replace('}}}}', '}}')
                for c in range(len(lista_var)):
                    if c == 0:
                        cadena_j = "char " + lista_var[c] + " [][] = " + lista_arg[c]
                    else:
                        cadena_j = cadena_j + lista_var[c] + " [][] = " + lista_arg[c]
                    if c < len(lista_var) - 1:
                        cadena_j = cadena_j + ", "
                    else:
                        cadena_j = cadena_j + ";"
                cadena_j = cadena_j.replace('},{', '}, {')
                cadena_p = stab + paste_string(lista_var, "CE") + " = " + paste_string(lista_arg, "CE")
                cadena_p = cadena_p.replace('{{', '[[').replace('}}', ']]').replace('},{', '], [')
        if word == "BOOLEANO":
            if re.fullmatch(RE_VAR_BOO, cadena_aux):
                cadena_c = "bool "
                cadena_j = "boolean "
                lista_aux = cadena_aux.split(',')
                for v in lista_aux:
                    lista_ax = v.split('=')
                    if len(lista_ax) > 1:
                        lista_var.append(lista_ax[0])
                        lista_arg.append(lista_ax[1])
                    else:
                        lista_var.append(lista_ax[0])
                        lista_arg.append("None")
                cad_var = paste_string(lista_var, "CE")
                cadena_p = stab + cad_var + " = "
                for a in range(len(lista_var)):
                    if not lista_arg[a] == "None":
                        if lista_arg[a].upper() == "VERDADERO" or lista_arg[a] == '1':
                            cadena_c = cadena_c + lista_var[a] + " = true"
                            cadena_j = cadena_j + lista_var[a] + " = true"
                            cadena_p = cadena_p + "True"
                        elif lista_arg[a].upper() == "FALSO" or lista_arg[a] == '0':
                            cadena_c = cadena_c + lista_var[a] + " = false"
                            cadena_j = cadena_j + lista_var[a] + " = false"
                            cadena_p = cadena_p + "False"
                        else:
                            cadena_c = cadena_c + lista_var[a] + " = " + lista_arg[a]
                            cadena_j = cadena_j + lista_var[a] + " = " + lista_arg[a]
                            cadena_p = cadena_p + lista_arg[a]
                    else:
                        cadena_c = cadena_c + lista_var[a]
                        cadena_j = cadena_j + lista_var[a]
                        cadena_p = cadena_p + lista_arg[a]
                    if a < len(lista_var) - 1:
                        cadena_c = cadena_c + ", "
                        cadena_j = cadena_j + ", "
                        cadena_p = cadena_p + ", "
                cadena_c = cadena_c + ";"
                cadena_j = cadena_j + ";"
            elif re.fullmatch(RE_VEC_BOO, cadena_aux):
                for a in lista_aux:
                    lista_ax = a.split('},')
                    for b in lista_ax:
                        l_aux = b.split('[]=')
                        lista_var.append(l_aux[0])
                        lista_arg.append(l_aux[1].replace('{', '').replace('}', ''))
                cadena_c = "bool "
                cadena_j = "boolean "
                cadena_p = paste_string(lista_var, "CE") + " = "
                for b in range(len(lista_var)):
                    lista_ax = lista_arg[b].split(',')
                    cadena_c = cadena_c + lista_var[b] + "[] = {"
                    cadena_j = cadena_j + lista_var[b] + "[] = {"
                    cadena_p = cadena_p + "["
                    for c in range(len(lista_ax)):
                        if lista_ax[c].upper() == "VERDADERO" or lista_ax[c] == '1':
                            cadena_c = cadena_c + "true"
                            cadena_j = cadena_j + "true"
                            cadena_p = cadena_p + "True"
                        elif lista_ax[c].upper() == "FALSO" or lista_ax[c] == '0':
                            cadena_c = cadena_c + "false"
                            cadena_j = cadena_j + "false"
                            cadena_p = cadena_p + "False"
                        else:
                            cadena_c = cadena_c + lista_ax[c]
                            cadena_j = cadena_j + lista_ax[c]
                            cadena_p = cadena_p + lista_ax[c]
                        if c < (len(lista_ax) - 1):
                            cadena_c = cadena_c + ", "
                            cadena_j = cadena_j + ", "
                            cadena_p = cadena_p + ", "
                    if b < (len(lista_var) - 1):
                        cadena_c = cadena_c + "}, "
                        cadena_j = cadena_j + "}, "
                        cadena_p = cadena_p + "], "
                cadena_c = cadena_c + "};"
                cadena_j = cadena_j + "};"
                cadena_p = cadena_p + "]"
            elif re.fullmatch(RE_MAT_BOO, cadena_aux):
                lista_arx = []
                for x in lista_aux:
                    lista_ax = x.split('}},')
                    for y in lista_ax:
                        l_aux = y.split('=')
                        l_vc = l_aux[0].split('[')
                        lista_var.append(l_vc[0])
                        lista_lim.append('[' + l_vc[1] + '[' + l_vc[2])
                        l_ar = l_aux[1].replace('{{', '').replace('}}', '').split('},{')
                        lista_arx.append(l_ar)
                cadena_c = "bool "
                cadena_j = "boolean "
                cadena_p = paste_string(lista_var, "CE") + " = "
                for a in range(len(lista_var)):
                    cadena_c = cadena_c + lista_var[a] + lista_lim[a] + " = {"
                    cadena_j = cadena_j + lista_var[a] + lista_lim[a] + " = {"
                    cadena_p = cadena_p + "["
                    for b in range(len(lista_arx[a])):
                        lb = lista_arx[a][b].split(',')
                        ssb = ""
                        sbpy = ""
                        for c in range(len(lb)):
                            if lb[c] == "VERDADERO" or lb[c] == '1':
                                ssb = ssb + "true"
                                sbpy = sbpy + "True"
                            elif lb[c] == "FALSO" or lb[c] == '0':
                                ssb = ssb + "false"
                                sbpy = sbpy + "False"
                            else:
                                ssb = ssb + lb[c]
                                sbpy = sbpy + lb[c]
                            if c < (len(lb) - 1):
                                ssb = ssb + ", "
                                sbpy = sbpy + ", "
                        cadena_c = cadena_c + "{" + ssb
                        cadena_j = cadena_j + "{" + ssb
                        cadena_p = cadena_p + "[" + sbpy
                        if b < (len(lista_arx[a]) - 1):
                            cadena_c = cadena_c + "}, "
                            cadena_j = cadena_j + "}, "
                            cadena_p = cadena_p + "], "
                    if a < (len(lista_var) - 1):
                        cadena_c = cadena_c + "}}, "
                        cadena_j = cadena_j + "}}, "
                        cadena_p = cadena_p + "]], "
                cadena_c = cadena_c + "}};"
                cadena_j = cadena_j + "}};"
                cadena_p = cadena_p + "]]"
    if gen:
        l_retorno.append(cadena_c)
        l_retorno.append(cadena_j)
        l_retorno.append(lista_py)
    else:
        l_retorno.append(cadena_c)
        l_retorno.append(cadena_j)
        l_retorno.append(cadena_p)
    return l_retorno


def translator_io(l_io, cc_cor, word, tab, l_memoria, cinta):
    sym_tab = '\t'
    stab = sym_tab * tab
    formato = ""
    lt_io = []
    if word == "ESCRIBIR":
        if cinta:
            if len(l_io) == 2:
                cadena_c = "printf(" + l_io[0][:-1][::-1][::-1] + "%i" + "\\n\", " + l_io[1] + cc_cor + ");"
                cadena_j = "System.out.println(" + l_io[0][:-1][::-1][::-1] + "\" + " + l_io[1] + cc_cor + ");"
                cadena_p = stab + "print(" + l_io[0][:-1][::-1][::-1] + "\", " + l_io[1] + cc_cor + ")"
                lt_io.append(cadena_c)
                lt_io.append(cadena_j)
                lt_io.append(cadena_p)
            else:
                # print("1")
                cadena_c = "printf((float)(" + l_io[0] + ")\\n\");"
                cadena_j = "System.out.println((" + l_io[0] + ").floatValue());"
                cadena_p = stab + "print(" + l_io[0] + ")"
                lt_io.append(cadena_c)
                lt_io.append(cadena_j)
                lt_io.append(cadena_p)
        else:
            if re.fullmatch(RE_WORD, l_io[0]):
                cen, ind = buscar_m(l_memoria, l_io[0])
                if l_memoria[ind][1] == "E":
                    formato = "d"
                elif l_memoria[ind][1] == "R":
                    formato = "f"
                elif l_memoria[ind][1] == "C":
                    formato = "c"
                else:
                    formato = "s"
                tipo = 0
            else:
                if len(l_io) == 2:
                    cen, ind = buscar_m(l_memoria, l_io[1])
                    if l_memoria[ind][1] == "E":
                        formato = "d"
                    elif l_memoria[ind][1] == "R":
                        formato = "f"
                    elif l_memoria[ind][1] == "C":
                        formato = "c"
                    else:
                        formato = "s"
                    tipo = 1
                else:
                    tipo = 2
            if tipo == 0:
                # print("TIPO 0")
                cadena_c = "printf(\"%" + formato + "\\n\", " + l_io[0] + cc_cor + ");"
                cadena_j = "System.out.println(" + l_io[0] + cc_cor + ");"
                cadena_p = stab + "print(" + l_io[0] + cc_cor + ")"
                lt_io.append(cadena_c)
                lt_io.append(cadena_j)
                lt_io.append(cadena_p)
            elif tipo == 1:
                # print("TIPO 1")
                cadena_c = "printf(" + l_io[0] + "%" + formato + "\\n\", " + l_io[1] + cc_cor + ");"
                cadena_j = "System.out.println(" + l_io[0] + "\" + " + l_io[1] + cc_cor + ");"
                cadena_p = stab + "print(" + l_io[0] + "\", " + l_io[1] + cc_cor + ")"
                lt_io.append(cadena_c)
                lt_io.append(cadena_j)
                lt_io.append(cadena_p)
            else:
                # print("TIPO 2")
                cadena_c = "printf(" + l_io[0][:-1] + "\\n\");"
                cadena_j = "System.out.println(" + l_io[0] + ");"
                cadena_p = stab + "print(" + l_io[0] + ")"
                lt_io.append(cadena_c)
                lt_io.append(cadena_j)
                lt_io.append(cadena_p)
    else:
        cc_buff = ""
        cen, ind = buscar_m(l_memoria, l_io)
        if l_memoria[ind][1] == "E":
            formato = "d"
            scanner = "LEER.nextInt();"
            pycast = " = int(input("
        elif l_memoria[ind][1] == "R":
            formato = "f"
            scanner = "LEER.nextFloat();"
            pycast = " = float(input("
        elif l_memoria[ind][1] == "C":
            formato = "c"
            scanner = "LEER.next().charAt();"
            pycast = " = str(input("
        else:
            formato = "s"
            scanner = "LEER.nextLine();"
            cc_buff = "LEER.nextLine();"
            pycast = " = str(input("
        if l_memoria[ind] != "MT":
            cadena_c = "scanf(\"%" + formato + "\", &" + l_io + cc_cor + ");"
            cadena_j = cc_buff + l_io + cc_cor + " = " + scanner
            cadena_p = l_io + cc_cor + pycast + "))"
        else:
            cadena_c = "scanf(\"%" + formato + "\", &" + l_io + cc_cor + ");"
            cadena_j = cc_buff + l_io + cc_cor + " = " + scanner
            cadena_p = l_io + cc_cor + pycast + "))"
        lt_io.append(cadena_c)
        lt_io.append(cadena_j)
        lt_io.append(cadena_p)
    return lt_io


# Funcion que verifica las cadenas y ejecuta las traducciones
def ver(copia):
    val = True
    lista_t = []  # Lista total
    lista_error = []  # Lista de errores
    mem = []  # Memoria
    for x in range(len(copia)):
        l_ax = []
        string_ax = ""
        tab = copia[x].count('\t')
        sym_tab = '\t'
        stab = sym_tab * tab
        cc_org = copia[x]
        lista_py = []
        ll_ax = []
        lax_py = []
        if tab > 0:
            lista_prueba = copia[x].replace('\t', '').split()
            lista_aux = copia[x].replace('\t', '').split()
        else:
            lista_prueba = copia[x].split()
            lista_aux = copia[x].split()
        ss_asig = paste_string(lista_prueba, "ND")
        if len(lista_prueba) > 0:
            if re.fullmatch(RE_DATO, lista_prueba[0]):
                lista_aux.pop(0)
                if lista_prueba[0] == "ENTERO":
                    size = len(lista_aux)
                    if size == 1:
                        if not val_let(lista_aux[0], "ENTERO"):

                            print("MANDO ESTO: ", lista_aux[0])

                            var_ver = ver_memoria(mem, lista_aux[0], "E")
                            if not var_ver:
                                if re.fullmatch(RE_ENT, lista_aux[0]):
                                    lista_t.append(translator_dato(lista_aux[0], "ENTERO", False, tab))
                                elif re.fullmatch(RE_VM_GEN, lista_aux[0]):
                                    lista_py.append(translator_dato(lista_aux[0], "ENTERO", True, tab))
                                    ll_ax.append(lista_py[0][0])
                                    ll_ax.append(lista_py[0][1])
                                    for a in range(len(lista_py[0][2])):
                                        lax_py.append(lista_py[0][2][a])
                                    ll_ax.append(lax_py)
                                    lista_t.append(ll_ax)
                                else:
                                    mem.clear()
                                    lista_t.clear()
                                    linea = x + 1
                                    error = "Error en la línea " + str(linea) + ". La expresión: \"" + lista_aux[0] + \
                                            "\" no es válida como declaración de ENTERO."
                                    lista_error.clear()
                                    lista_error.append(linea)
                                    lista_error.append(error)
                                    val = False
                                    break
                            else:
                                mem.clear()
                                lista_t.clear()
                                linea = x + 1
                                error = "Error en la línea " + str(linea) + \
                                        ". Multiples declaraciones de una misma variable."
                                lista_error.clear()
                                lista_error.append(linea)
                                lista_error.append(error)
                                val = False
                                break
                        else:
                            mem.clear()
                            lista_t.clear()
                            linea = x + 1
                            error = "Error en la línea " + str(linea) + ". La expresión: \"" + lista_aux[0] + \
                                    "\" no es válida, posee palabras reservadas."
                            lista_error.clear()
                            lista_error.append(linea)
                            lista_error.append(error)
                            val = False
                            break
                    else:
                        mem.clear()
                        lista_t.clear()
                        ss_error = paste_string(lista_aux, "E")
                        linea = x + 1
                        error = "Error en la línea " + str(linea) + ". La expresión: \"" + ss_error + \
                                "\" posee espacios."
                        lista_error.clear()
                        lista_error.append(linea)
                        lista_error.append(error)
                        val = False
                        break
                elif lista_prueba[0] == "REAL":
                    size = len(lista_aux)
                    if size == 1:
                        if not val_let(lista_aux[0], "REAL"):
                            var_ver = ver_memoria(mem, lista_aux[0], "R")
                            if not var_ver:
                                if re.fullmatch(RE_REL, lista_aux[0]):
                                    lista_t.append(translator_dato(lista_aux[0], "REAL", False, tab))
                                elif re.fullmatch(RE_VM_GEN, lista_aux[0]):
                                    lista_py.append(translator_dato(lista_aux[0], "ENTERO", True, tab))
                                    ll_ax.append(lista_py[0][0])
                                    ll_ax.append(lista_py[0][1])
                                    for a in range(len(lista_py[0][2])):
                                        lax_py.append(lista_py[0][2][a])
                                    ll_ax.append(lax_py)
                                    lista_t.append(ll_ax)
                                else:
                                    mem.clear()
                                    lista_t.clear()
                                    linea = x + 1
                                    error = "Error en la línea " + str(linea) + ". La expresión: \"" + lista_aux[0] + \
                                            "\" no es válida como declaración de REAL."
                                    lista_error.clear()
                                    lista_error.append(linea)
                                    lista_error.append(error)
                                    val = False
                                    break
                            else:
                                mem.clear()
                                lista_t.clear()
                                linea = x + 1
                                error = "Error en la línea " + str(linea) + \
                                        ". Multiples declaraciones de una misma variable."
                                lista_error.clear()
                                lista_error.append(linea)
                                lista_error.append(error)
                                val = False
                                break
                        else:
                            mem.clear()
                            lista_t.clear()
                            linea = x + 1
                            error = "Error en la línea " + str(linea) + ". La expresión: \"" + lista_aux[0] + \
                                    "\" no es válida, posee palabras reservadas."
                            lista_error.clear()
                            lista_error.append(linea)
                            lista_error.append(error)
                            val = False
                            break
                    else:
                        mem.clear()
                        lista_t.clear()
                        ss_error = paste_string(lista_aux, "E")
                        linea = x + 1
                        error = "Error en la línea " + str(linea) + ". La expresión: \"" + ss_error + \
                                "\" posee espacios."
                        lista_error.clear()
                        lista_error.append(linea)
                        lista_error.append(error)
                        val = False
                        break
                elif lista_prueba[0] == "CARACTER":
                    size = len(lista_aux)
                    if size == 1:
                        if not val_let(lista_aux[0], "CARACTER"):
                            var_ver = ver_memoria(mem, lista_aux[0], "C")
                            if not var_ver:
                                if re.fullmatch(RE_CAR, lista_aux[0]):
                                    lista_t.append(translator_dato(lista_aux[0], "CARACTER", False, tab))
                                elif re.fullmatch(RE_VM_GEN, lista_aux[0]):
                                    lista_py.append(translator_dato(lista_aux[0], "ENTERO", True, tab))
                                    ll_ax.append(lista_py[0][0])
                                    ll_ax.append(lista_py[0][1])
                                    for a in range(len(lista_py[0][2])):
                                        lax_py.append(lista_py[0][2][a])
                                    ll_ax.append(lax_py)
                                    lista_t.append(ll_ax)
                                else:
                                    mem.clear()
                                    lista_t.clear()
                                    linea = x + 1
                                    error = "Error en la línea " + str(linea) + ". La expresión: \"" + lista_aux[0] + \
                                            "\" no es válida como declaración de CARACTER."
                                    lista_error.clear()
                                    lista_error.append(linea)
                                    lista_error.append(error)
                                    val = False
                                    break
                            else:
                                mem.clear()
                                lista_t.clear()
                                linea = x + 1
                                error = "Error en la línea " + str(linea) + \
                                        ". Multiples declaraciones de una misma variable."
                                lista_error.clear()
                                lista_error.append(linea)
                                lista_error.append(error)
                                val = False
                                break
                        else:
                            mem.clear()
                            lista_t.clear()
                            linea = x + 1
                            error = "Error en la línea " + str(linea) + ". La expresión: \"" + lista_aux[0] + \
                                    "\" no es válida, posee palabras reservadas."
                            lista_error.clear()
                            lista_error.append(linea)
                            lista_error.append(error)
                            val = False
                            break
                    else:
                        mem.clear()
                        lista_t.clear()
                        ss_error = paste_string(lista_aux, "E")
                        linea = x + 1
                        error = "Error en la línea " + str(linea) + ". La expresión: \"" + ss_error + \
                                "\" posee espacios."
                        lista_error.clear()
                        lista_error.append(linea)
                        lista_error.append(error)
                        val = False
                        break
                elif lista_prueba[0] == "BOOLEANO":
                    size = len(lista_aux)
                    if size == 1:
                        if not val_let(lista_aux[0], "BOOLEANO"):
                            var_ver = ver_memoria(mem, lista_aux[0], "E")
                            if not var_ver:
                                if re.fullmatch(RE_BOO, lista_aux[0]):
                                    lista_t.append(translator_dato(lista_aux[0], "BOOLEANO", False, tab))
                                elif re.fullmatch(RE_VM_GEN, lista_aux[0]):
                                    lista_py.append(translator_dato(lista_aux[0], "ENTERO", True, tab))
                                    ll_ax.append(lista_py[0][0])
                                    ll_ax.append(lista_py[0][1])
                                    for a in range(len(lista_py[0][2])):
                                        lax_py.append(lista_py[0][2][a])
                                    ll_ax.append(lax_py)
                                    lista_t.append(ll_ax)
                                else:
                                    mem.clear()
                                    lista_t.clear()
                                    linea = x + 1
                                    error = "Error en la línea " + str(linea) + ". La expresión: \"" + lista_aux[0] + \
                                            "\" no es válida como declaración de BOOLEANO."
                                    lista_error.clear()
                                    lista_error.append(linea)
                                    lista_error.append(error)
                                    val = False
                                    break
                            else:
                                mem.clear()
                                lista_t.clear()
                                linea = x + 1
                                error = "Error en la línea " + str(linea) + \
                                        ". Multiples declaraciones de una misma variable."
                                lista_error.clear()
                                lista_error.append(linea)
                                lista_error.append(error)
                                val = False
                                break
                        else:
                            mem.clear()
                            lista_t.clear()
                            linea = x + 1
                            error = "Error en la línea " + str(linea) + ". La expresión: \"" + lista_aux[0] + \
                                    "\" no es válida, posee palabras reservadas."
                            lista_error.clear()
                            lista_error.append(linea)
                            lista_error.append(error)
                            val = False
                            break
                    else:
                        mem.clear()
                        lista_t.clear()
                        ss_error = paste_string(lista_aux, "E")
                        linea = x + 1
                        error = "Error en la línea " + str(linea) + ". La expresión: \"" + ss_error + \
                                "\" posee espacios."
                        lista_error.clear()
                        lista_error.append(linea)
                        lista_error.append(error)
                        val = False
                        break
            elif re.fullmatch(RE_IO, lista_prueba[0]):
                lista_aux.pop(0)
                ss_io = paste_string(lista_aux, "E")
                if lista_prueba[0] == "ESCRIBIR":
                    if re.fullmatch(RE_WRITE, ss_io):
                        lista_io = ss_io.split('" ')
                        if len(lista_io) == 2:
                            l_man = []
                            if lista_io[1].count('[') > 0:
                                cax_io = ss_io.split('[')
                                cad_var = cax_io[0]
                                ssax = cad_var.split("\" ")
                                cc_var = ssax[1]
                                cax_io.pop(0)
                                if len(cax_io) > 1:
                                    cc_cor = "[" + cax_io[0] + "[" + cax_io[1]
                                else:
                                    cc_cor = "[" + cax_io[0]
                                """
                                print("CC_COR", cc_cor)
                                print("CC_VAR", cc_var)
                                """
                            else:
                                cc_var = lista_io[1]
                                cc_cor = ""
                            l_man.append(cc_var)
                            l_man.append(cc_cor)
                            io_cen, indice = buscar_m(mem, cc_var)
                            if io_cen:
                                lista_t.append(translator_io(l_man, cc_cor, "ESCRIBIR", tab, mem, False))
                            else:
                                mem.clear()
                                lista_t.clear()
                                linea = x + 1
                                error = "Error en la línea " + str(linea) + ". La variable: \"" + lista_io[1] + \
                                        "\" no esta declarada."
                                lista_error.clear()
                                lista_error.append(linea)
                                lista_error.append(error)
                                val = False
                                break
                        else:
                            if re.fullmatch(RE_VAR, lista_io[0]):
                                l_man = []
                                if ss_io.count('[') == 2:
                                    cax_io = ss_io.split('[')
                                    cc_var = cax_io[0]
                                    cc_cor = "[" + cax_io[1] + "[" + cax_io[2]
                                elif ss_io.count('[') == 1:
                                    cax_io = ss_io.split('[')
                                    cc_var = cax_io[0]
                                    cc_cor = "[" + cax_io[1]
                                else:
                                    cc_var = ss_io
                                    cc_cor = ""
                                l_man.append(cc_var)
                                l_man.append(cc_cor)
                                io_cen, indice = buscar_m(mem, cc_var)
                                if io_cen:
                                    lista_t.append(translator_io(l_man, cc_cor, "ESCRIBIR", tab, mem, False))
                                else:
                                    mem.clear()
                                    lista_t.clear()
                                    linea = x + 1
                                    error = "Error en la línea " + str(linea) + ". La variable: \"" + lista_io[0] + \
                                            "\" no esta declarada."
                                    lista_error.clear()
                                    lista_error.append(linea)
                                    lista_error.append(error)
                                    val = False
                                    break
                            elif re.fullmatch(RE_TEXT, lista_io[0]):
                                lista_t.append(translator_io(lista_io, "", "ESCRIBIR", tab, mem, False))
                    elif re.fullmatch(RE_WRT, ss_io):
                        l_man = []
                        cc_op = ss_io.split("\" ")
                        if len(cc_op) == 2:
                            l_man.append(cc_op[0] + "\"")
                            l_man.append(cc_op[1])
                        else:
                            l_man.append(ss_io)
                        if len(l_man) > 1:
                            # (\+ | - | \ * | / | \ * \ * | %)
                            cc_arv = l_man[1].replace('**', '|').replace('+', '|').replace('-', '|')
                            cc_arv = cc_arv.replace('*', '|').replace('/', '|').replace('%', '|')
                            ls_arv = cc_arv.split('|')
                            tdata, ls_arv = del_lis(ls_arv)
                            if len(ls_arv) > 0:
                                vcc = None
                                ind = None
                                for itt in range(len(ls_arv)):
                                    vcc, indice = buscar_m(mem, ls_arv[itt])
                                    if not vcc:
                                        ind = itt
                                        break
                                if vcc:
                                    lista_t.append(translator_io(l_man, "", "ESCRIBIR", tab, mem, True))
                                else:
                                    mem.clear()
                                    lista_t.clear()
                                    linea = x + 1
                                    error = "Error en la línea " + str(linea) + ". La variable: \"" + ls_arv[ind] + \
                                            "\" no esta declarada."
                                    lista_error.clear()
                                    lista_error.append(linea)
                                    lista_error.append(error)
                                    val = False
                                    break
                        else:
                            lista_t.append(translator_io(l_man, "", "ESCRIBIR", tab, mem, True))
                    else:
                        mem.clear()
                        lista_t.clear()
                        linea = x + 1
                        error = "Error en la línea " + str(linea) + ". La sentencia: \"" + ss_io + \
                                "\" no es válida."
                        lista_error.clear()
                        lista_error.append(linea)
                        lista_error.append(error)
                        val = False
                        break
                elif lista_prueba[0] == "LEER":
                    if re.fullmatch(RE_READ, ss_io):
                        cc_var = ss_io
                        cc_cor = ""
                        if re.fullmatch(RE_VM_GEN, ss_io):
                            cax_io = ss_io.split('[')
                            cc_var = cax_io[0]
                            cax_io.pop(0)
                            if len(cax_io) > 1:
                                cc_cor = "[" + cax_io[0] + "[" + cax_io[1]
                            else:
                                cc_cor = "[" + cax_io[0]
                        io_cen, indice = buscar_m(mem, cc_var)
                        if io_cen:
                            lista_t.append(translator_io(cc_var, cc_cor, "LEER", tab, mem, False))
                        else:
                            mem.clear()
                            lista_t.clear()
                            linea = x + 1
                            error = "Error en la línea " + str(linea) + ". La variable: \"" + ss_io + \
                                    "\" no esta declarada."
                            lista_error.clear()
                            lista_error.append(linea)
                            lista_error.append(error)
                            val = False
                            break
                    else:
                        mem.clear()
                        lista_t.clear()
                        ss_error = paste_string(lista_aux, "E")
                        linea = x + 1
                        error = "Error en la línea " + str(linea) + ". La expresión: \"" + ss_error + \
                                "\" no es valida para LEER."
                        lista_error.clear()
                        lista_error.append(linea)
                        lista_error.append(error)
                        val = False
                        break
            elif re.fullmatch(RE_ASI_VAL, ss_asig):
                ss_asig = ss_asig.replace('=', ' = ').replace('*', ' * ').replace('%', ' % ').replace('/', ' / ')
                ss_asig = ss_asig.replace('-', ' - ').replace('+', ' + ').replace(' *  * ', ' ** ')
                cc_tab = stab + ss_asig
                l_ax.append(ss_asig + ";")
                l_ax.append(ss_asig + ";")
                l_ax.append(cc_tab)
                lista_t.append(l_ax)
            else:
                l_ax.append(cc_org)
                l_ax.append(cc_org)
                l_ax.append(cc_org)
                lista_t.append(l_ax)
        else:
            cc_tab = stab + string_ax
            l_ax.append(cc_tab)
            l_ax.append(cc_tab)
            l_ax.append(cc_tab)
            lista_t.append(l_ax)
    if not val:
        lista_t.append(lista_error)
    return lista_t, val


def run_v(texto, num):
    lista_f, vali = ver(texto)
    lista_s = []
    if len(lista_f[0]) == 2:
        line = lista_f[0][0]
        ter = lista_f[0][1]
        lista_s.append(line)
        lista_s.append(ter)
    else:
        if 0 <= int(num) <= 2:
            for x in range(len(lista_f)):
                aux = lista_f[x]
                for y in range(len(aux)):
                    if y == num:
                        if num != 2:
                            lista_s.append(aux[y])
                        else:
                            ax = aux[y]
                            if isinstance(ax, list):
                                for z in range(len(ax)):
                                    lista_s.append(ax[z])
                            else:
                                lista_s.append(ax)
    return vali, lista_s
