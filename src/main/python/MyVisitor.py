# Generated from /home/kyanesdev/Facultad/DHS/compiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *


if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class MyVisitor(ParseTreeVisitor):
    cont = 0
    functions = dict()
    lastLabel = [0]
    currentLoop = [0]
    tmp = 0
    rollback = False

    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.f = open("./output/CodigoIntermedio.txt", "w")
        self.f.write("push EOF\n")
        self.f.write("jump main \n")
        
        self.visitChildren(ctx)
        self.f.close()


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#retorno.
    def visitRetorno(self, ctx:compiladoresParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prototipado.
    def visitPrototipado(self, ctx:compiladoresParser.PrototipadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumentos.
    def visitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumento.
    def visitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcion.
    def visitFuncion(self, ctx:compiladoresParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parametros.
    def visitParametros(self, ctx:compiladoresParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloquefor.
    def visitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        self.cont = self.cont + 1
        self.currentLoop.append(self.cont)

        self.f.write(ctx.getChild(2).getChild(1).getText() + "\n")
        self.f.write("label loop" + str(self.currentLoop[-1]) + "\n")
        self.visitChildren(ctx.getChild(7))

        self.f.write(ctx.getChild(5).getText() + "\n")
        self.f.write("ifnot " + ctx.getChild(3).getText() + " jump loop" + str(self.currentLoop[-1]) + "\n")
        self.currentLoop.pop()
        


    # Visit a parse tree produced by compiladoresParser#bloquewhile.
    def visitBloquewhile(self, ctx:compiladoresParser.BloquewhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqueif.
    def visitBloqueif(self, ctx:compiladoresParser.BloqueifContext):
        self.cont = self.cont + 1
        
        self.f.write("ifnot " + ctx.getChild(2).getText() + " jump else" + str(self.cont) + "\n")
        self.visitChildren(ctx.getChild(4))
        self.f.write("jump endif" + str(self.lastLabel[-1]) + "\n")
        self.f.write("label else" + str(self.lastLabel[-1]) + "\n")

        if(ctx.getChild(5)):
            self.visitChildren(ctx.getChild(5))

        self.f.write("label endif" + str(self.lastLabel[-1]) + "\n")
        self.lastLabel.pop()


    # Visit a parse tree produced by compiladoresParser#bloqueElse.
    def visitBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
        self.visitChildren(ctx)
        self.f.write("label endif" + str(self.lastLabel[-1]) + "\n")


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#conDeclaracion.
    def visitConDeclaracion(self, ctx:compiladoresParser.ConDeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#init.
    def visitInit(self, ctx:compiladoresParser.InitContext):
        self.visitChildren(ctx)
        self.f.write(ctx.getChild(0).getText() + ctx.getChild(1).getText() + "t" + str(self.tmp) +  "\n")
        self.rollback = False
        self.tmp = 0


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        self.visitChildren(ctx)
        self.f.write(str(ctx.getChild(0)) + "= t" + str(self.tmp) + "\n")
        self.tmp = 0


    # Visit a parse tree produced by compiladoresParser#asignarFuncion.
    def visitAsignarFuncion(self, ctx:compiladoresParser.AsignarFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tdato.
    def visitTdato(self, ctx:compiladoresParser.TdatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#itop.
    def visitItop(self, ctx:compiladoresParser.ItopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oparit.
    def visitOparit(self, ctx:compiladoresParser.OparitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#exp.
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        self.visitChildren(ctx)
        if(ctx.getChildCount()):
            self.f.write("t" + str(self.tmp) + "=" + ctx.getChild(0).getText() + "\n")
        self.rollback = True
        self.tmp = 0
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#t.
    def visitT(self, ctx:compiladoresParser.TContext):
        self.visitChildren(ctx)
        if(ctx.getChildCount() and not self.rollback):
            self.f.write("t" + str(self.tmp) + "=" + ctx.getChild(1).getText() + "\n")
            self.tmp = self.tmp + 1
        if(self.rollback):
            if(ctx.getChildCount()):
                self.f.write("t" + str(self.tmp + 1) + "=" + "t" + str(self.tmp + 1))
                self.f.write(ctx.getChild(0).getText() + "t" + str(self.tmp) + "\n")
                self.tmp = self.tmp + 1     


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#f.
    def visitF(self, ctx:compiladoresParser.FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#control.
    def visitControl(self, ctx:compiladoresParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#cmps.
    def visitCmps(self, ctx:compiladoresParser.CmpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#cmp.
    def visitCmp(self, ctx:compiladoresParser.CmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#incrementoUnario.
    def visitIncrementoUnario(self, ctx:compiladoresParser.IncrementoUnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#decrementoUnario.
    def visitDecrementoUnario(self, ctx:compiladoresParser.DecrementoUnarioContext):
        return self.visitChildren(ctx)



del compiladoresParser