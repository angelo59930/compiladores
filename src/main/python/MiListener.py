# Generated from /home/angelo/Facultad/Tercero/DHS/test/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser
    
from TablaSimbolos import TablaSimbolos
from TablaSimbolos import Funcion 
from TablaSimbolos import Variable

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class MiListener(ParseTreeListener):
        
    tabalSimbolos = TablaSimbolos()
    i = 0;
    out = open("output/ts.txt", "w")
    

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        '''-> { '''
        self.tabalSimbolos.addContex()

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        ''' -> }'''
        
        self.out.write(str(self.tabalSimbolos.ts)+ "\n")

        tmp = []
        
        for i in self.tabalSimbolos.ts[-1]:
            if(str(i).startswith("var_")):
                tmp.append(str(i)[4:])
                
        for i in tmp:
            aux, obj = self.tabalSimbolos.searchId(i)
        
        self.tabalSimbolos.removeContex()
        
        if(len(self.tabalSimbolos.ts) == 0):
            self.out.close()
        


    # Enter a parse tree produced by compiladoresParser#retorno.
    def enterRetorno(self, ctx:compiladoresParser.RetornoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#retorno.
    def exitRetorno(self, ctx:compiladoresParser.RetornoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#prototipado.
    def enterPrototipado(self, ctx:compiladoresParser.PrototipadoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prototipado.
    def exitPrototipado(self, ctx:compiladoresParser.PrototipadoContext):
        fuc = Funcion()
        datos = ctx.getText()
        fuc.setInit(True)
        fuc = self.generateFunc(fuc,datos)
        self.isUsed(fuc.getName(), fuc.toDictionay(), 0)



    # Enter a parse tree produced by compiladoresParser#argumentos.
    def enterArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumentos.
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        pass

    # Enter a parse tree produced by compiladoresParser#argumento.
    def enterArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass


    # Exit a parse tree produced by compiladoresParser#argumento.
    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass

    # Enter a parse tree produced by compiladoresParser#funcion.
    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#funcion.
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        pass

    # Enter a parse tree produced by compiladoresParser#parametros.
    def enterParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parametros.
    def exitParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass



    # Enter a parse tree produced by compiladoresParser#bloquefor.
    def enterBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloquefor.
    def exitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloquewhile.
    def enterBloquewhile(self, ctx:compiladoresParser.BloquewhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloquewhile.
    def exitBloquewhile(self, ctx:compiladoresParser.BloquewhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloqueif.
    def enterBloqueif(self, ctx:compiladoresParser.BloqueifContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloqueif.
    def exitBloqueif(self, ctx:compiladoresParser.BloqueifContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext): 

        var = Variable()
        
        tmp = ctx.getText()
        datos = ""
        
        if tmp.startswith('int'):
            var.setTipo("int")
            datos = tmp[3:]
            #var.setName(tmp[3:])

        if "," in datos:
            '''  datos -> a = 2, b, c, d = 4 '''
            dato = datos.split(',')
            
            ''' 
                datos -> a = 2, b, c, d = 4
                datos.split(",")
                dato [a = 2 , b , c , d = 4 ]
            '''
            
            for i in dato:
                d = i.split("=")
                varTmp = var.cloneType()
                varTmp.setName(d[0])
                '''
                    d -> nombreVar || nombreVar = 213
                    d [ , ] -> d [ ] || d [ , ]
                '''

                if(len(d)>1):
                    valor = d[1]
    
                    posiblesVariables = []
                
                    aux1 = valor.split('+')
                    for i in aux1:
                        aux2 = i.split('-')
                        for j in aux2:
                            aux3 = j.split('*')
                            for k in aux3:
                                aux4 = k.split('/')
                                for m in aux4:
                                    if not m.isnumeric() and m != "":
                                        posiblesVariables.append(m)
                    
                    for i  in posiblesVariables:
                        index, var = self.tabalSimbolos.searchId(str(i))

                        if var == False:
                            print('ERROR: La variable \"'+ str(d[1]) +'\" no existe')
                            return
                        
                    
                    varTmp.setInit(True)

                self.isUsed(d[0],varTmp.toDictionay(),0)         
        
        else:
            d = datos.split("=")
            varTmp = var.cloneType()
            varTmp.setName(d[0])
            if(len(d)>1):
                valor = d[1]
    
                posiblesVariables = []
            
                aux1 = valor.split('+')
                for i in aux1:
                    aux2 = i.split('-')
                    for j in aux2:
                        aux3 = j.split('*')
                        for k in aux3:
                            aux4 = k.split('/')
                            for m in aux4:
                                if not m.isnumeric() and m != "":
                                    posiblesVariables.append(m)
                
                for i  in posiblesVariables:
                    index, nose = self.tabalSimbolos.searchId(str(i))
                    if nose == False:
                        print('ERROR: La variable \"'+ str(d[1]) +'\" no existe')
                        return
                    
                
                varTmp.setInit(True)

            self.isUsed(d[0], varTmp.toDictionay(),0)


     # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        pass
   
    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
       pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        var = Variable()
        datos = ctx.getText()
        d = datos.split("=")
        v = var.cloneType()
        v.setName(d[0])

        i , varTmp = self.tabalSimbolos.searchId(str(d[0]))
        
        if varTmp == False: 
            print('ERROR: La variable \"'+ str(d[0]) +'\" no existe')
            return

        varTmp['initialized'] = True

        valor = d[1].split("(")
        
        if(len(d) > 1):
            self.isUsed(d[0], v.toDictionay(), 1)
            valor = d[1]
    
            posiblesVariables = []
            
            test = valor.split("(")
            
            if(len(test)>1):
                test = test[1].split(")")
                test = test[0].split(",")
                for i in test:
                    self.exist(i)

        else: 
            aux1 = valor.split('+')
            for i in aux1:
                aux2 = i.split('-')
                for j in aux2:
                    aux3 = j.split('*')
                    for k in aux3:
                        aux4 = k.split('/')
                        for m in aux4:
                            if not m.isnumeric() and m != "":
                                posiblesVariables.append(m)
            
            
            
            for i  in posiblesVariables:
                self.isUsed(i," ",1)
       

    # Enter a parse tree produced by compiladoresParser#tdato.
    def enterTdato(self, ctx:compiladoresParser.TdatoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tdato.
    def exitTdato(self, ctx:compiladoresParser.TdatoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#itop.
    def enterItop(self, ctx:compiladoresParser.ItopContext):
        pass

    # Exit a parse tree produced by compiladoresParser#itop.
    def exitItop(self, ctx:compiladoresParser.ItopContext):
        pass


    # Enter a parse tree produced by compiladoresParser#oparit.
    def enterOparit(self, ctx:compiladoresParser.OparitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#oparit.
    def exitOparit(self, ctx:compiladoresParser.OparitContext):
        pass


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#term.
    def enterTerm(self, ctx:compiladoresParser.TermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#t.
    def enterT(self, ctx:compiladoresParser.TContext):
        pass

    # Exit a parse tree produced by compiladoresParser#t.
    def exitT(self, ctx:compiladoresParser.TContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#f.
    def enterF(self, ctx:compiladoresParser.FContext):
        pass

    # Exit a parse tree produced by compiladoresParser#f.
    def exitF(self, ctx:compiladoresParser.FContext):
        pass


    # Enter a parse tree produced by compiladoresParser#control.
    def enterControl(self, ctx:compiladoresParser.ControlContext):
        pass

    # Exit a parse tree produced by compiladoresParser#control.
    def exitControl(self, ctx:compiladoresParser.ControlContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cmp.
    def enterCmp(self, ctx:compiladoresParser.CmpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cmp.
    def exitCmp(self, ctx:compiladoresParser.CmpContext):
        pass


    def generateFunc(self,func,datos):
        
        func.arguments = []

        if datos.startswith("int"):
            func.setTipo("int")
            datos = datos[3:]

        datos = datos.split("(")
        func.setName(datos[0])

        datos = datos[1].split(")")[0]

        if "," in datos:
            dato = datos.split(",")
            tipo = ""
            for i in dato:
                if "int" in i:
                    tipo = "int"
                    nombre = i[3:]
                func.addArguments(nombre,tipo)
        return func


    '''
        Crear o inizializar = 0
        caso funcion o uso de variable = 1
    '''
    def isUsed(self, id, var, case):
        i, exist = self.tabalSimbolos.searchId(id)

        if exist == False:
            # caso funcion
            if case == 1: 
                if "(" in id:
                    self.isUsed(id.split("(")[0], var, 1)
                else:
                    print("ERROR: \""+ id + "\" no existe.")
            
            # caso agregar una variable
            if case == 0:
                self.tabalSimbolos.addId(id, var, " " ) 


        #  esta en la tabla de simbolos 
        else:
            if case == 1:
                exist['used'] = True
                if exist['initialized'] == False:
                    print('WARNING: La variable \"' + str(id) + '\" no esta inicializada')
                
                self.tabalSimbolos.addId(id, str(exist), i)
            else: 
                print("ERROR : \""+str(id) + "\" la variable ya existe.")
            
    def exist(self, id):
        print(id)
        i, test = self.tabalSimbolos.searchId(id)
        #test = False
        if test == False:
            print("ERROR : \""+str(id) + "\" la variable NO existe.")
            return
           

del compiladoresParser