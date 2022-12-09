# Generated from /home/angelo/Facultad/Tercero/DHS/compiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
from TablaSimbolos import TablaSimbolos
from TablaSimbolos import Function 
from TablaSimbolos import Variable
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

class compiladoresListener(ParseTreeListener):
    contador = 0;
    tablaSimbolos = TablaSimbolos()
    ids = dict()
    parametros = []
    
    
    
    # abrimos el archivo para escribir los contextos
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # escribinos y por ultimo cerramos el archivos
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # cuando entramos en un bloque AÑADIMOS un contexto
    # se entra en un bloque cuando encontramos -> '{'
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.contador = self.contador + 1
        self.tablaSimbolos.addContex()

    # cuando salimos de un bloque REMOVEMOS un contexto
    # se sale de un bloque cuando encontramos -> '}'
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        #print('Contexto ' + str(self.contador) + ':{')
        #for context in self.tablaSimbolos.ts:
        #    for elements in context:
        #        print(f'{elements}:{context[elements].toString()},')
        #        
        #print('}')
        print("CTX-BLOQUE -> " +self.tablaSimbolos.ts.__str__())
        
        self.tablaSimbolos.removeContex()


    # Exit a parse tree produced by compiladoresParser#retorno.
    def exitRetorno(self, ctx:compiladoresParser.RetornoContext):
        pass
        
        
    # Exit a parse tree produced by compiladoresParser#prototipado.
    def exitPrototipado(self, ctx:compiladoresParser.PrototipadoContext):
        tipo = str(ctx.getChild(0).getChild(0))
        nombre = str(ctx.getChild(1))
        funcion = Function(nombre, tipo, self.parametros.copy())
        self.tablaSimbolos.ts[-1][nombre] = funcion
        self.parametros.clear()
    
    def exitCabezera(self, ctx:compiladoresParser.CabezeraContext):
        name = str(ctx.getChild(1))
        # Si el nombre de la funcion es "main" omitimos las comprobaciones
        if name == 'main':
            # añadimos a la tabla de simbolos los posibles argumentos que pueda tener el main como arg y argv
            for param in self.parametros:
                param.initialized = True
                self.tablaSimbolos.ts[-1][str(param.name)] = param
            return
        
        # Si no es la funcion "main"
        # Verificamos que se encuentra en el contexto global el prototipo
        if self.tablaSimbolos.findByKey(name) and self.tablaSimbolos.returnKey(name).varFunc == 'function':
            # Si se encuentra la key
            # Y si es una funcion  
            # decimos que la funcion esta inicializada/creada
            self.tablaSimbolos.returnKey(name).initialized = True
            
        else:
            print(f'ERROR: La funcion "{name}" no se encuentra prototipada')


    # Exit a parse tree produced by compiladoresParser#argumento.
    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0))
        var.initialized = True 
        self.tablaSimbolos.ts[-1][str(var.name)] = var
      


    def exitArgumentoProto(self, ctx:compiladoresParser.ArgumentoContext):
        var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0))   
        var.initialized = True     
        self.parametros.append(var)     


    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        # Aqui se crea un nuevo contexto
        # Esto se debe a que necesitamos alguna forma para almacenar
        # los argumentos de las funciones (en el caso de "main" tenemos: "arg" y "argv")
        # Al crear un nuevo contexto sabemos que este siempre sera el anteUltimo
        # por lo tanto siempre que busquemos un ID vamos a tener en cuenta los argumentos de la funcion
        self.tablaSimbolos.addContex()
        
    # Exit a parse tree produced by compiladoresParser#funcion.
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        # Sabemos que aqui acaban las funciones
        # por ese motivo podemos borrar el contexto de argumenos de la funcion
        # ----------------------------------------------------------------
        # Para hacer esto hay que tener en cuenta varias cosas:
        #     1- La funcion 'removeContex' solo borra el ULTIMO contexto
        #     2- Cuando salimos de un bloque hacemos un removeContext        
        # ----------------------------------------------------------------
        # Sabiendo esto tenemos que tener en cuenta que si borramos un contexto aca
        # SIEMPRE se borraran 2 contextos.
        # Esto nos sirve debido a que por cada funcion generamos 2 contextos
        # 1 contexto de argumentos
        # 1 contexto del bloque
        self.tablaSimbolos.removeContex()
        print("CTX-RETORNO -> " +self.tablaSimbolos.ts.__str__())


    # Exit a parse tree produced by compiladoresParser#parametros.
    def exitParametros(self, ctx:compiladoresParser.ParametrosContext):
        tmp = ctx.getText()
        tmp = tmp.split(',')
        
        if self.tablaSimbolos.findByKey(str(tmp[0])):
            self.tablaSimbolos.returnKey(str(tmp[0])).used = True   
              
            if not self.tablaSimbolos.returnKey(str(tmp[0])).initialized:
                print(f'WARNING: La variable "{str(tmp[0])}" no esta inicializada')
                
        else:
            print(f'ERROR: La variable "{str(tmp[0])}" no existe')
        
        
    # Exit a parse tree produced by compiladoresParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        key = str(ctx.getChild(0))
        #print(f'TS -> {self.tablaSimbolos.ts}')
        if not self.tablaSimbolos.findByKey(key):
            print(f'ERROR: La funcion "{key}" no existe')

    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        tipo = str(ctx.getChild(0).getChild(0)) # tipo de todas las variables
        tmp = ctx.getText()
        tmpData = ''
        dataType = ''
        
        if tmp.startswith('int'):
            dataType = 'int'
            datosTmp = tmp[3:]
            tmpData = datosTmp.split(',')[0]        
        else:
            dataType = 'float'
            datosTmp = tmp[5:]
            tmpData = datosTmp.split(',')[0]
        
        if not '=' in tmpData:
            id = Variable(tmpData, dataType)
            self.ids[tmpData] = id

        for id in self.ids:
            value = self.ids[id]
            value.type = dataType
        
        
        for id in self.ids:
            value = self.ids[id]
        
        for id in self.ids:
            self.tablaSimbolos.ts[-1][id] = self.ids[id]
        
        
        #print(f'TS IN DECLARACION -> {self.tablaSimbolos.ts}')
        self.ids.clear()
        
        
    # Exit a parse tree produced by compiladoresParser#conDeclaracion.
    def exitConDeclaracion(self, ctx:compiladoresParser.ConDeclaracionContext):
        
        if not ctx.getText() == "" and not '=' in ctx.getText() :
           nombre = str(ctx.getChild(1))
           id = Variable(nombre, None)
           self.ids[nombre] = id
            

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        name = str(ctx.getChild(0))
        
        if name in self.ids:
            print(f'ERROR: La variable "{name}" ya ha sido creada')
            return
        
        id = Variable(name, None)
        id.initialized = True
        
        self.ids[name] = id
        

    # asignacion de UNICAMENTE variables a variables, operaciones, valores
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        # hijo 0 -> la variable 
        # hijo 1 -> la asignacion ( el = )
        # hijo 2 -> lo asignado ( numero, otra variable, funcion )
        key = str(ctx.getChild(0))
        if self.tablaSimbolos.findByKey(key):
            var = self.tablaSimbolos.returnKey(key)
            var.initialized = True
        else:
            print(f'ERROR: La variable "{key}" no existe')

    
    # asignacion de UNICAMENTE variables a funciones
    def exitAsignarFuncion(self, ctx:compiladoresParser.TdatoContext):
        keyVar = str(ctx.getChild(0))
        
        if self.tablaSimbolos.findByKey(keyVar):
            self.tablaSimbolos.returnKey(keyVar).initialized = True    
        else:
            print(f'ERROR: La variable "{keyVar}" no existe')
            

    # Exit a parse tree produced by compiladoresParser#tdato.
    def exitTdato(self, ctx:compiladoresParser.TdatoContext):
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
        tmp = str(ctx.getChild(0))
        try:
            if tmp.isdigit() or float(tmp):
                return
        except:
            pass
        
        if self.tablaSimbolos.findByKey(tmp):
            var = self.tablaSimbolos.returnKey(tmp)
            if var.initialized:
                var.used = True
            else:
                print(f'WARNING: La variable "{tmp}" no fue inicializada')
        else:
            print(f'ERROR: La variable "{tmp}" no existe')

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


    # Enter a parse tree produced by compiladoresParser#cmps.
    def enterCmps(self, ctx:compiladoresParser.CmpsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cmps.
    def exitCmps(self, ctx:compiladoresParser.CmpsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cmp.
    def enterCmp(self, ctx:compiladoresParser.CmpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cmp.
    def exitCmp(self, ctx:compiladoresParser.CmpContext):
        pass


del compiladoresParser