from doctest import OPTIONFLAGS_BY_NAME
from tkinter import * 
from collections import deque
from tkinter.filedialog import askopenfile, asksaveasfile
import tkinter as tk

from Variable import *
from pip import main
from CiclosConClase import validarCiclos
from CiclosConClaseJP import *
from condicionales_java import *
from condicionales_python import *
import condicionales_C as con
from run import *
import os
import re

expresion_JAVA = r'((static)[ ]+((int)|(float)|(boolean)|(char)|(void))([ ]([\[])[a-zA-Z0-9_]*[\]])*[ ]+([a-zA-Z]+[a-zA-Z0-9_]*)([(][ ]*(((int)|(float)|(boolean)|(char)|(void))[ ]+([a-zA-Z]+[a-zA-Z0-9_]*)([ ]([\[])[a-zA-Z0-9_]*[\]])*)*([,][ ]((int)|(float)|(boolean)|(char)|(void))*[ ]([a-zA-Z]+[a-zA-Z0-9_]*)([ ]([\[])[a-zA-Z0-9_]*[\]])*)*[ ][)][{]))'

class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget
        
    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

class Window:
    def __init__(self, master):
        self.master = master
        self.master.option_add("*Font", "Verdana 12")

        self.Main = Frame(self.master)
        
        self.stack = deque(maxlen = 10)  #Creacion y configuracion de la ventana del editor
        self.stackcursor = 0
 
        self.L1 = Label(self.Main, text = "INTERPRETE")
        self.L1.pack(padx = 5, pady = 5)
 
        self.T1 = Text(self.Main, width = 90, height = 25)
        self.T2 = Text(self.Main, width = 90, height = 10, state='disable')
        self.listado = TextLineNumbers(width=30, height = 500)
        self.listado.attach(self.T1)
        self.listado.place(x=0, y=45)
        #---------

        self.v1 = Scrollbar(orient="vertical", command=self.T1.yview)
        self.v1.pack(side=RIGHT, fill='y')
        self.T1.configure(yscrollcommand=self.v1.set)

        self.T1.tag_configure("red", foreground = "red", font = ("Verdana", "12", "bold"))
        self.T1.tag_configure("orange", foreground = "orange", font = ("Verdana", "12", "bold"))
        self.T1.tag_configure("blue", foreground = "blue", font = ("Verdana", "12", "bold"))
        self.T1.tag_configure("purple", foreground = "purple", font = ("Verdana", "12", "bold"))  #Configuracion de las etiquetas que permiten
        self.T1.tag_configure("green", foreground = "green", font = ("Verdana", "12", "bold"))    #resaltar las palabras reservadas
        self.T1.tag_configure("gold", foreground = "gold", font = ("Verdana", "12", "bold"))
        self.T1.tag_configure("brown", foreground = "brown", font = ("Verdana", "12", "bold"))
        self.T1.tag_configure("error", foreground= "white", background= "red")
        
 
        self.tags = ["orange", "blue", "purple", "green", "red", "gold", "brown"]
 
        self.wordlist = [ ["RETORNA", "FSI", "SI", "SINO","FSINO","ENTONCES", "SEGUN", "CASO", "ROMPER", "HAZ", "HACER", "MIENTRAS", "DEOTROMODO", "FSEGUN", "FINM","FUNCION", "PARA", "HASTA", "FINP", "FHAZ", "FPARA", "ESCRIBIR", "LEER", "FINF"],
                          ["ENTERO", "CARACTER", "REAL", "BOOLEANO", "VACIO"],
                          ["INICIO", "FINAL"],                          #Conjuntos de las palabras reservadas
                          ["VERDADERO", "FALSO"],
                          ["&&", "||", ">", "<", ">=", "<=", "!=", "==", "!"]]
 
        self.T1.bind("<Return>", lambda event: self.indent(event.widget))
         
        self.T1.pack(side=TOP,padx = 5, pady = 5)
        self.T2.pack(side=BOTTOM,padx = 5, pady = 5)
 
        #---------

        self.menu = Menu(self.Main)
        self.menu.add_command(label = "Abrir", command = self.print_stack)
        self.menu.add_command(label = "Deshacer", command = self.undo)          
        self.menu.add_command(label = "Rehacer", command = self.redo)
 
        self.master.config(menu = self.menu)
 
        self.B1 = Button(self.Main, text = "Guardar", width = 8, command = self.save)
        self.B1.pack(padx = 5, pady = 5, side = LEFT)
        
        self.B2 = Button(self.Main, text = "Limpiar", width = 8, command = self.clear)
        self.B2.pack(padx = 5, pady = 5, side = LEFT)
                                                                                        #Creacion de los botones que realizan algunas
        self.B3 = Button(self.Main, text = "Deshacer", width = 8, command = self.undo)  #de las funciones del editor
        self.B3.pack(padx = 5, pady = 5, side = LEFT)
 
        self.B4 = Button(self.Main, text = "Rehacer", width = 8, command = self.redo)
        self.B4.pack(padx = 5, pady = 5, side = LEFT)

        self.B4 = Button(self.Main, text = "Traducir", width = 8, command = self.menu_option)
        self.B4.pack(padx = 5, pady = 5, side = LEFT)

        self.Main.pack(padx = 5, pady = 5)

    def menu_option(self):
        self.desplegable=tk.Tk()
        self.desplegable.title("TRADUCCIÓN") #Creacion de ventana emergente para la traduccion a cualquiera de los tres lenguajes

        self.desplegable.geometry('400x150+500+300')

        self.L2 = Label(self.desplegable, text = "TRADUCCIÓN DE PSEUDOCODIGO ESPAÑOL A:")

        self.B5 = Button(self.desplegable, text = "Verificar C/C++", width = 15, command = self.verificarC)
        self.B5.pack(padx = 10, pady = 10, side = TOP)

        self.B6 = Button(self.desplegable, text = "Verificar JAVA", width =15, command = self.verificarJAVA)
        self.B6.pack(padx = 10, pady = 10, side = TOP)

        self.B7 = Button(self.desplegable, text = "Verificar Python", width = 15, command = self.verificarPy)
        self.B7.pack(padx = 10, pady = 10, side = TOP)


    def redrawLineNumber(self):
        self.listado.redraw()

    def verificarC(self):                        #Funcion que se encargara de verificar que el texto ingresado
        self.T2.configure(state='normal')       #este c-orrecto mediante los automatas diseñados y programados                                  
        texto1 = self.T1.get("1.0", "end")      #por los otros grupos 
        x = texto1.split("\n")
        x.pop(len(x)-1)
        self.T2.delete("1.0","end")
        noReconocidas = []

        if(x[0] != "" or x[len(x)-1] != ""):
            while (x[len(x)-1] == ""):
                x.pop(len(x)-1)


            inicio = x[0].replace(" ", "")
            final = x[len(x)-1].replace(" ", "")

            if inicio !="INICIO": 
                self.T2.insert(INSERT, "No inicia\n")    
                self.error(1)           
                return 0                #Editor v2

            if final !="FINAL":
                self.T2.insert(INSERT, "No Finaliza")
                self.error(len(x))
                return 0                #Editor v2

            x.pop(0)
            x.pop(len(x)-1) 

            y = x.copy()
            z = x

            print ("TEXTO: \n\n")
            print (x)

            text4 = run(x,3)

            print ("\nTRADUCCION FUNCIONES: \n\n")
            print (text4)

            for c in text4:
                if (len(c) == 2 and c[0] == False):
                    self.error(c[1][1]+1)
                    self.T2.config(state="normal")
                    self.T2.insert(INSERT, c[1][0] + "\n")
                

            text1 = validarCiclos(x)
            text1.mapCiclos()

            print ("\nTRADUCCION CICLOS: \n\n")
            print (text1.lines)
           
            print ("\nERRORES CICLOS: \n\n")
            print (text1.errores)
            if(text1.errores):
                for a, b in zip(text1.lines, text1.errores):
                    self.error(b[1]+1)
                    self.T2.config(state="normal")
                    self.T2.insert(INSERT, b[0] + str(b[1]+1))
                    self.T2.insert(INSERT, "\n")
                    self.T2.config(state="disable")

            text2, t2 = run_v(x,0)     #Validacion de las variables
            print ("\nTRADUCCION VARIABLES: \n\n")
            print (t2)

            if(not text2):
                a = t2
                self.error(a[0]+1)
                self.T2.config(state="normal")
                self.T2.insert(INSERT, a[1])
                self.T2.insert(INSERT, "\n")
                self.T2.config(state="disable")

    
            text3 = con.validarCondicionales(z)     #validacion de los condicionales

            print ("\nTRADUCCION CONDICIONALES: \n\n")
            print (text3)

            if(not text3[0]):
                a = text3[1]
                for linea in a:
                    
                    self.error(linea[1]+1)
                    self.T2.config(state="normal")
                    self.T2.insert(INSERT, linea[0]+" "+str(linea[1]+1))
            

            if((not text1.errores) and (text2 == True) and (text3[0]) and (text4[0])):
                
                traduccionCiclos = validarCiclos(text4)
                print ("TRADUCCION CICLOS: \n\n")
                print (traduccionCiclos)
                traduccionCiclos.mapCiclos()                 #Editor v2
                val, traduccionVariables = run_v(traduccionCiclos.lines, 0)
                if (val):
                    traduccionCondicionales = con.validarCondicionales(traduccionVariables)

                cont=1
                correccion = 1

                try:
                    i = y.index("")
                    y.remove("")
                except ValueError:
                    correccion = 0
                    i = 0

                for lines1, lines2 in zip(traduccionCondicionales[1], y):
                    if(lines1 == (lines2+" ")):
                        if(lines1 != "" and lines1 != " "):
                            if(cont >= i+1):
                                    noReconocidas.append(cont+correccion)
                            elif(cont < i+1):
                                    noReconocidas.append(cont)
                    cont +=1

                if(noReconocidas):
                    for line in noReconocidas:
                        self.error(line+1)
                        self.T2.config(state="normal")
                        self.T2.insert(INSERT, "Linea no reconocida # "+str(line+1)+"\n")
                        self.T2.config(state="disable")
                    
                    return 0

                self.T2.config(state="normal")
                self.T2.insert(INSERT, "Traduciendo...")
                self.T2.config(state="disable")


                files = [('Archivo C', '*.c')]
                file = asksaveasfile(filetypes = files, defaultextension = files)
                f = open(file.name, "w")
                
                f.write("#include <stdio.h>\n#include <stdbool.h>\n\nint main(){\n")
                for line in traduccionCondicionales[1]:
                    f.write(line + "\n")

                f.write("\nreturn 0;\n}")
                os.startfile(file.name)
                
            
        elif(x[0] == ""):
            self.error(1)
            self.T2.config(state="normal")
            self.T2.insert(INSERT, "No inicia \nNo finaliza")
            self.T2.config(state="disable")
        
        self.T2.config(state='disable')

    def verificarJAVA(self):                        #Funcion que se encargara de verificar que el texto ingresado
        self.T2.configure(state='normal')       #este c-orrecto mediante los automatas diseñados y programados                                  
        texto1 = self.T1.get("1.0", "end")      #por los otros grupos 
        x = texto1.split("\n")
        x.pop(len(x)-1)
        self.T2.delete("1.0","end")
        noReconocidas = []

        if(x[0] != "" or x[len(x)-1] != ""):
            while (x[len(x)-1] == ""):
                x.pop(len(x)-1)


            inicio = x[0].replace(" ", "")
            final = x[len(x)-1].replace(" ", "")

            if inicio !="INICIO": 
                self.T2.insert(INSERT, "No inicia\n")    
                self.error(1)           
                return 0                #Editor v2

            if final !="FINAL":
                self.T2.insert(INSERT, "No Finaliza")
                self.error(len(x))
                return 0                #Editor v2
            

            x.pop(0)
            x.pop(len(x)-1) 

            y = x.copy()

            text4 = run(x, 2)

            print (text4)

            for c in text4:
                if (len(c) == 2 and c[0] == False):
                    self.error(c[1][1]+1)
                    self.T2.config(state="normal")
                    self.T2.insert(INSERT, c[1][0] + "\n")

            text1 = validarCiclosJP(x) 
            text1.mapCiclosJava()
            
            print ("\nERRORES CICLOS\n\n")
            print (text1.errores)
            print ("\nTRADUCCION CICLOS: \n\n")
            print (text1.lines)
           
            if(text1.errores):
                for a, b in zip(text1.lines, text1.errores):
                    self.error(b[2]+1)
                    self.T2.config(state="normal")
                    self.T2.insert(INSERT, b[0] + b[1] + str(b[2]+1))
                    self.T2.insert(INSERT, "\n")
                    self.T2.config(state="disable")
    
            text2, t2 = run_v(x,0)     #Validacion de las variables

            if(not text2):
                a = t2
                print("\nERROR VARIABLES\n\n")
                print(a)
                self.error(a[0]+1)
                self.T2.config(state="normal")
                self.T2.insert(INSERT, a[1])
                self.T2.insert(INSERT, "\n")
                self.T2.config(state="disable")
            
            print ("\nTRADUCCION Variables: \n\n")
            print (t2)
            text3 = validarCondicionalesJAVA(x)
            print ("\nTRADUCCION Condicionales: \n\n")
            print (text3)

            if(not text3[0]):
                a = text3[1]
                for linea in a:
                    
                    self.error(linea[1]+1)
                    self.T2.config(state="normal")
                    self.T2.insert(INSERT, linea[0]+" "+str(linea[1]+1))

            if((not text1.errores) and (text2 == True) and (text3[0]) and (text4[0])):
                
                traduccionCiclos = validarCiclosJP(text4)
                traduccionCiclos.mapCiclosJava()
                val, traduccionVariables = run_v(traduccionCiclos.lines, 1)
                if (val):
                    traduccionCondicionales = validarCondicionalesJAVA(traduccionVariables)

                cont=1
                correccion = 1

                try:
                    i = y.index("")
                    y.remove("")
                except ValueError:
                    correccion = 0
                    i = 0

                for lines1, lines2 in zip(traduccionCondicionales[1], y):
                    if(lines1 == (lines2+" ")):
                        if(lines1 != "" and lines1 != " "):
                            if(cont >= i+1):
                                    noReconocidas.append(cont+correccion)
                            elif(cont < i+1):
                                    noReconocidas.append(cont)
                    cont +=1

                if(noReconocidas):
                    for line in noReconocidas:
                        self.error(line+1)
                        self.T2.config(state="normal")
                        self.T2.insert(INSERT, "Linea no reconocida # "+str(line+1)+"\n")
                        self.T2.config(state="disable")
                    
                    return 0
                
                
                auxiliar = []
                cont_f = 0
                list_x = traduccionCondicionales[1]
                traduccion_final = []

                for i in traduccionCondicionales[1]:
                    traduccion_final.append(i)

                print ("\nTRADUCCION FINAL: \n\n")
                print (traduccion_final)

                for j in traduccionCondicionales[1]:
                    if (re.search(expresion_JAVA, j)):
                        cont_f += 1

                print ("\nCONTADOR DE FUNCIONES: \n")
                print (cont_f)

                while (cont_f != 0):
                    cont = 0
                    cont_a = 0
                    cont_b = 0
                    inicio = False
                    for j in traduccion_final:
                        if (re.search(expresion_JAVA, j)):
                            auxiliar.append(j)
                            cont_a = cont
                            inicio = True
                        elif ((j == "}// ") and (inicio)):
                            cont_b = cont
                            break
                        cont += 1

                    for x in range (cont_a+1, cont_b+1):
                        auxiliar.append(list_x[x])
                    
                    print ("\nContador A: ")
                    print (cont_a)

                    print ("\nContador B: ")
                    print (cont_b)

                    print ("\nTamaño lista: \n\n")
                    print (len(traduccion_final))
                    print ("\n")

                    for w in range (cont_a, cont_b+1):
                        print (w)
                        del traduccion_final[cont_a]
                    cont_f = cont_f - 1
                    list_x = traduccion_final

                print ("\nCADENA AUXILIAR: \n\n")
                print (auxiliar)

                print ("\nTRADUCCION FINAL: \n\n")
                print (traduccion_final)

                self.T2.config(state="normal")
                self.T2.insert(INSERT, "Traduciendo...")
                self.T2.config(state="disable")

                separador = os.path.sep
                dir_actual = os.path.dirname(os.path.abspath(__file__))
                dir = separador.join(dir_actual.split(separador)[:-1])
                print(dir)

                existe_directorio = os.path.exists(dir+'\Proyecto JAVA')
                print(existe_directorio)

                if existe_directorio==False:
                    os.mkdir(dir+'\Proyecto JAVA')
                    exist_directorio = os.path.exists(dir+'Proyecto JAVA\Proyecto Codigo Traducido')
                    if exist_directorio==False:
                        os.makedirs(dir+'Proyecto JAVA/Proyecto Codigo Traducido')

                files = [('Archivo JAVA', '*.java')]
                file = asksaveasfile(filetypes = files, defaultextension = files)
                rut_arch = os.path.basename(file.name)
                nom_arch = os.path.splitext(rut_arch)
                f = open(file.name, "w")
                
                f.write("import java.util.Scanner;\n\npublic class "+ nom_arch[0] +"{\n\n")
                for line in auxiliar:
                    f.write("\t"+ line + "\n")
                f.write ("\tpublic static void main(String[] args){\n\n\t\tScanner LEER = new Scanner(System.in);\n")            
                for line in traduccion_final:
                    f.write("\t\t"+ line + "\n")
                f.write("\n\n\t}\n\n}")
                os.startfile(file.name)


        elif(x[0] == ""):
            self.error(1)
            self.T2.config(state="normal")
            self.T2.insert(INSERT, "No inicia \nNo finaliza")
            self.T2.config(state="disable")
        
        self.T2.config(state='disable')

    def verificarPy(self):                        #Funcion que se encargara de verificar que el texto ingresado
        self.T2.configure(state='normal')       #este c-orrecto mediante los automatas diseñados y programados                                  
        texto1 = self.T1.get("1.0", "end")      #por los otros grupos 
        x = texto1.split("\n")
        x.pop(len(x)-1)
        self.T2.delete("1.0","end")
        noReconocidas = []

        if(x[0] != "" or x[len(x)-1] != ""):
            while (x[len(x)-1] == ""):
                x.pop(len(x)-1)

            inicio = x[0].replace(" ", "")
            final = x[len(x)-1].replace(" ", "")

            if inicio !="INICIO": 
                self.T2.insert(INSERT, "No inicia\n")    
                self.error(1)           
                return 0                #Editor v2

            if final !="FINAL":
                self.T2.insert(INSERT, "No Finaliza")
                self.error(len(x))
                return 0                #Editor v2
            

            x.pop(0)
            x.pop(len(x)-1) 

            y = x.copy()

            text4 = run(x, 1)

            for c in text4:
                if (len(c) == 2 and c[0] == False):
                    self.error(c[1][1]+1)
                    self.T2.config(state="normal")
                    self.T2.insert(INSERT, c[1][0] + "\n")
            
            print("\ntraduccion de funciones: \n")
            print (text4)

            text1 = validarCiclosJP(x) 
            text1.mapCiclosPython()
            text1.lines = text1.getLine()
           
            if(text1.errores):
                for a, b in zip(text1.lines, text1.errores):
                    self.error(b[2]+1)
                    self.T2.config(state="normal")
                    self.T2.insert(INSERT, b[0] + b[1] + str(b[2]+1))
                    self.T2.insert(INSERT, "\n")
                    self.T2.config(state="disable")
    
            text2, t2 = run_v(x,0)     #Validacion de las variables

            if(not text2):
                a = t2
                print("\nERROR VARIABLES\n\n")
                print(a)
                self.error(a[0]+1)
                self.T2.config(state="normal")
                self.T2.insert(INSERT, a[1])
                self.T2.insert(INSERT, "\n")
                self.T2.config(state="disable")

            text3 = validarCondicionalesPython(text1.lines)
            if(not text3[0]):
                a = text3[1]
                for linea in a:
                    self.error(linea[1]+1)
                    self.T2.config(state="normal")
                    self.T2.insert(INSERT, linea[0]+" "+str(linea[1]+1))
            print("\nValidacion ciclos, variables y condicionales: \n")
            print(text1.errores)
            print(text2)
            print(text3[0])

            if((not text1.errores) and (text2 == True) and (text3[0]) and text4[0]):
                
                traduccionCiclos = validarCiclosJP(text4)
                traduccionCiclos.mapCiclosPython()
                traduccionCiclos.lines = traduccionCiclos.getLine()
                print ("\nTraduccion de ciclos: \n")
                print (traduccionCiclos.lines)
                val, traduccionVariables = run_v(traduccionCiclos.lines, 2)
                print ("\nTraduccion de variables: \n")
                print (traduccionVariables)
                if (val):
                    traduccionCondicionales = validarCondicionalesPython(traduccionVariables)

                cont=1
                correccion = 1

                try:
                    i = y.index("")
                    y.remove("")
                except ValueError:
                    correccion = 0
                    i = 0

                for lines1, lines2 in zip(traduccionCondicionales[1], y):
                    if(lines1 == (lines2+" ")):
                        if(lines1 != "" and lines1 != " "):
                            if(cont >= i+1):
                                    noReconocidas.append(cont+correccion)
                            elif(cont < i+1):
                                    noReconocidas.append(cont)
                    cont +=1

                if(noReconocidas):
                    for line in noReconocidas:
                        self.error(line+1)
                        self.T2.config(state="normal")
                        self.T2.insert(INSERT, "Linea no reconocida # "+str(line+1)+"\n")
                        self.T2.config(state="disable")
                    
                    return 0

                print ("\nTraduccion condicionales: \n")
                print (traduccionCondicionales)


                self.T2.config(state="normal")
                self.T2.insert(INSERT, "Traduciendo...")
                self.T2.config(state="disable")


                separador = os.path.sep
                dir_actual = os.path.dirname(os.path.abspath(__file__))
                dir = separador.join(dir_actual.split(separador)[:-1])
                print("\n"+dir)

                existe_directorio = os.path.exists(dir+'\Proyecto Python')
                print(existe_directorio)

                if existe_directorio==False:
                    os.mkdir(dir+'\Proyecto Python')
                    exist_directorio = os.path.exists(dir+'Proyecto Python\Proyecto Codigo Traducido')
                    if exist_directorio==False:
                        os.makedirs(dir+'Proyecto Python/Proyecto Codigo Traducido')
                
                files = [('Archivo Python', '*.py')]
                file = asksaveasfile(filetypes = files, defaultextension = files)
                
                f = open(file.name, "w")
                
                f.write("class codigotraducido:\n\n")
                
                for line in traduccionCondicionales[1]:
                    f.write("\t" + line + "\n")
                #f.write("\n\n\t}")

                os.startfile(file.name)
                
            
        elif(x[0] == ""):
            self.error(1)
            self.T2.config(state="normal")
            self.T2.insert(INSERT, "No inicia \nNo finaliza")
            self.T2.config(state="disable")
        
        self.T2.config(state='disable')                              
    
    def error(self, linea):
        inicio = str(float(linea))
        print(inicio)
        self.T1.tag_add("error", inicio, inicio + "+1line")

    def tagHighlight(self):
        start = "1.0"                   #Funcion que se encarga de identificar las palabras
        end = "end"                     #reservadas y resaltarlas segun las etiquetas previamente
                                        #definidas
        for mylist in self.wordlist:
            num = int(self.wordlist.index(mylist))
 
            for word in mylist:
                self.T1.mark_set("matchStart", start)
                self.T1.mark_set("matchEnd", start)
                self.T1.mark_set("SearchLimit", end)
 
                mycount = IntVar()
                 
                while True:
                    index= self.T1.search(word,"matchEnd","SearchLimit", count=mycount, regexp = False)
 
                    if index == "": break
                    if mycount.get() == 0: break
 
                    self.T1.mark_set("matchStart", index)
                    self.T1.mark_set("matchEnd", "%s+%sc" % (index, mycount.get()))
 
                    preIndex = "%s-%sc" % (index, 1)
                    postIndex = "%s+%sc" % (index, mycount.get())
                     
                    if self.check(index, preIndex, postIndex):
                        self.T1.tag_add(self.tags[num], "matchStart", "matchEnd")
                         

    def check(self, index, pre, post):
        letters1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        letters2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                   "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        if self.T1.get(pre) == self.T1.get(index):
            pre = index
        else:
            if self.T1.get(pre) in letters1:
                return 0
            elif self.T1.get(pre) in letters2:    #Funcion que se encarga de validar las letras
                return 0                          #en una cadena para evitar resaltar palabras 
        if self.T1.get(post) in letters1:         #que contienen palabras reservadas
            return 0
        elif self.T1.get(post) in letters2:
            return 0
        return 1
 
 
    def scan(self):
        start = "1.0"
        end = "end"
        mycount = IntVar()
                                            #Funcion para resaltar comentarios y cadenas
        regex_patterns = [r'".*"', r'#.*']  #mediante expresiones regulares
 
        for pattern in regex_patterns:
            self.T1.mark_set("start", start)
            self.T1.mark_set("end", end)
 
            num = int(regex_patterns.index(pattern))
 
            while True:
                index = self.T1.search(pattern, "start", "end", count=mycount, regexp = True)
 
                if index == "": break
 
                if (num == 1):
                    self.T1.tag_add(self.tags[5], index, index + " lineend")
                elif (num == 0):
                    self.T1.tag_add(self.tags[6], index, "%s+%sc" % (index, mycount.get()))
 
                self.T1.mark_set("start", "%s+%sc" % (index, mycount.get()))
 
 
    def indent(self, widget):       
 
        index1 = widget.index("insert")      #Funcion que permite separar bloques de codigo
        index2 = "%s-%sc" % (index1, 1)      #mediante indentado
        prevIndex = widget.get(index2, index1)
 
        prevIndentLine = widget.index(index1 + "linestart")
        print("prevIndentLine ",prevIndentLine)
        prevIndent = self.getIndex(prevIndentLine)
        print("prevIndent ", prevIndent)
 
 
        if prevIndex == ":":
            widget.insert("insert", "\n" + "     ")
            widget.mark_set("insert", "insert + 1 line + 5char")
 
            while widget.compare(prevIndent, ">", prevIndentLine):
                widget.insert("insert", "     ")
                widget.mark_set("insert", "insert + 5 chars")
                prevIndentLine += "+5c"
            return "break"
         
        elif prevIndent != prevIndentLine:
            widget.insert("insert", "\n")
            widget.mark_set("insert", "insert + 1 line")
 
            while widget.compare(prevIndent, ">", prevIndentLine):
                widget.insert("insert", "     ")
                widget.mark_set("insert", "insert + 5 chars")
                prevIndentLine += "+5c"
            return "break"
 
 
    def getIndex(self, index):
        while True:
            if self.T1.get(index) == " ":       #Funcion directamente relacionada a la anterior
                index = "%s+%sc" % (index, 1)   #que permite obtener la ubicacion del ultimo indentado
            else:                               
                return self.T1.index(index)
            
                    
    def update(self):
        self.stackify()
        self.tagHighlight()                 #Funcion que contiene las 3 funciones que
        self.scan()                         #permiten la actualizacion del texto segun se 
        self.redrawLineNumber()              #ingresa
        self.T1.tag_remove("error", "1.0", "end")           
                                                            
    def save(self):     #Funcion que se encarga de guardar el texto en txt.
                                
        files = [('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        f = open(file.name, "a")                
        f.write(self.T1.get("1.0", "end"))   
 
    def clear(self):            #Funcion para borrar todo el texto
        self.T1.delete("1.0", "end")
 
    def stackify(self):                                     #Funcion que guarda los ultimos cambios 
        self.stack.append(self.T1.get("1.0", "end - 1c"))   #aplicados al texto 
        if self.stackcursor < 9: self.stackcursor += 1
 
    def undo(self):
        if self.stackcursor != 0:       #Funcion la cual mediante los cambios almacenados
            self.clear()                #por la funcion anterior deshace lo ultimo que se agrego
            if self.stackcursor > 0: self.stackcursor -= 1
            self.T1.insert("0.0", self.stack[self.stackcursor])
 
    def redo(self):                                 
        if len(self.stack) > self.stackcursor + 1:  #Funcion la cual mediante los cambios almacenados
            self.clear()                            #por la funcion anterior rehace lo ultimo que se elimino
            if self.stackcursor < 9: self.stackcursor += 1
            self.T1.insert("0.0", self.stack[self.stackcursor])
 
    def print_stack(self):  #Funcion de prueba para mostrar el funcionamiento
        filename = askopenfile(mode='r', filetypes=[('Texto', '*.txt')])

        if filename == None:
            return 0

        self.T1.delete("0.0", END)
        f = open(filename.name, "r")
        text = f.read()
        self.T1.insert("0.0", text)
        self.update()


root = Tk()
root.title("Editor de texto")
window = Window(root)
root.geometry("1024x800")
root.bind("<Key>", lambda event: window.update())
root.bind("<B1-Motion>", lambda event: window.redrawLineNumber())
root.bind("<Button-1>", lambda event: window.redrawLineNumber())
root.bind("<MouseWheel>", lambda event: window.redrawLineNumber())
root.mainloop()