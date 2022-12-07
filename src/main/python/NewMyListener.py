# Generated from /home/angelo/Facultad/Tercero/DHS/compiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
from TablaSimbolos import TablaSimbolos
from TablaSimbolos import Function 
from TablaSimbolos import Variable
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# TODO: 
# En el contexto GLOBAL se pueden guardar las referencias a las FUNCIONES
# esto nos sirve para identificar si existe la funion 'main', las variables y los prototipos
# a su vez con esto podriamos saber si un prototipo esta implementado o no
# o si una funcion despues del main se encuentra declarada y no prototipada
class compiladoresListener(ParseTreeListener):

    tablaSimbolos = TablaSimbolos()
    ids = dict()
    
    
    
    # abrimos el archivo para escribir los contextos
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # escribinos y por ultimo cerramos el archivos
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


    # cuando entramos en un bloque AÑADIMOS un contexto
    # se entra en un bloque cuando encontramos -> '{'
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tablaSimbolos.addContex()

    # cuando salimos de un bloque REMOVEMOS un contexto
    # se sale de un bloque cuando encontramos -> '}'
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        #print(self.tablaSimbolos.ts.__str__())
        self.tablaSimbolos.removeContex()


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
        pass


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


    # Enter a parse tree produced by compiladoresParser#parametros.
    def enterParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parametros.
    def exitParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
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


    # Enter a parse tree produced by compiladoresParser#bloqueElse.
    def enterBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloqueElse.
    def exitBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

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
            id = Variable(tmpData[0], dataType)
            self.ids[tmpData[0]] = id

        for id in self.ids:
            value = self.ids[id]
            value.type = dataType
        
        
        for id in self.ids:
            value = self.ids[id]
            print(f'DATATYPE -> {value.type}')
        
        self.tablaSimbolos.ts[-1] = self.ids.copy()
        
        self.ids.clear()
        
        

    # Enter a parse tree produced by compiladoresParser#conDeclaracion.
    def enterConDeclaracion(self, ctx:compiladoresParser.ConDeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#conDeclaracion.
    def exitConDeclaracion(self, ctx:compiladoresParser.ConDeclaracionContext):
        
        if not ctx.getText() == "" and not '=' in ctx.getText() :
           nombre = str(ctx.getChild(1))
           id = Variable(nombre, None)
           self.ids[nombre] = id
            


    # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        name = str(ctx.getChild(0))
        
        if name in self.ids:
            print(f'ERROR: la variable {name} ya ha sido creada')
            return
        
        id = Variable(name, None)
        
        self.ids[name] = id
        


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # asignacion de UNICAMENTE variables a variables, operaciones, valores
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        # hijo 0 -> la variable 
        # hijo 1 -> la asignacion ( el = )
        # hijo 2 -> lo asignado ( numero, otra variable, funcion )
        
        key = str(ctx.getChild(0))
                
        if self.tablaSimbolos.findByKey(key):
            pass
        else:
            print(f'la variable {key} no existe')

    def enterAsignarFuncion(self, ctx:compiladoresParser.TdatoContext):
        pass
    
    # asignacion de UNICAMENTE variables a funciones
    def exitAsignarFuncion(self, ctx:compiladoresParser.TdatoContext):
        key = str(ctx.getChild(2).getText())
        
        if not self.tablaSimbolos.findByKey(key):
            print(f'la funcion {key} no existe')
            

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