# Generated from /home/angelo/Facultad/Tercero/DHS/test/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#prog.
    def visitProg(self, ctx:compiladoresParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prototipado.
    def visitPrototipado(self, ctx:compiladoresParser.PrototipadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcion.
    def visitFuncion(self, ctx:compiladoresParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parametro.
    def visitParametro(self, ctx:compiladoresParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tdato.
    def visitTdato(self, ctx:compiladoresParser.TdatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#valor.
    def visitValor(self, ctx:compiladoresParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqif.
    def visitBloqif(self, ctx:compiladoresParser.BloqifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqwhile.
    def visitBloqwhile(self, ctx:compiladoresParser.BloqwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqfor.
    def visitBloqfor(self, ctx:compiladoresParser.BloqforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#modificacion.
    def visitModificacion(self, ctx:compiladoresParser.ModificacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#comprobacion.
    def visitComprobacion(self, ctx:compiladoresParser.ComprobacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#control.
    def visitControl(self, ctx:compiladoresParser.ControlContext):
        return self.visitChildren(ctx)



del compiladoresParser