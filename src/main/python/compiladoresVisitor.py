# Generated from /home/angelo/Facultad/Tercero/DHS/compiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by compiladoresParser#argumentosProto.
    def visitArgumentosProto(self, ctx:compiladoresParser.ArgumentosProtoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumentos.
    def visitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumento.
    def visitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumentoProto.
    def visitArgumentoProto(self, ctx:compiladoresParser.ArgumentoProtoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcion.
    def visitFuncion(self, ctx:compiladoresParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#cabezera.
    def visitCabezera(self, ctx:compiladoresParser.CabezeraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parametros.
    def visitParametros(self, ctx:compiladoresParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:compiladoresParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloquefor.
    def visitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloquewhile.
    def visitBloquewhile(self, ctx:compiladoresParser.BloquewhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqueif.
    def visitBloqueif(self, ctx:compiladoresParser.BloqueifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqueElse.
    def visitBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#conDeclaracion.
    def visitConDeclaracion(self, ctx:compiladoresParser.ConDeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#init.
    def visitInit(self, ctx:compiladoresParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#t.
    def visitT(self, ctx:compiladoresParser.TContext):
        return self.visitChildren(ctx)


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