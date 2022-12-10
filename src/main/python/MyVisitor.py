# Generated from /home/kyanesdev/Facultad/DHS/compiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *


if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser


#TODO:FALTAN CORREGIR LOS IF, IF ELSE, ESLE
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
        self.f.write("goto MAIN \n")
        
        self.visitChildren(ctx)
        self.f.close()



    def visitCabezera(self, ctx:compiladoresParser.CabezeraContext):
        tmp = str(ctx.getChild(1).getText()).upper()
        self.f.write(f'{tmp}:\n')
        self.visitChildren(ctx.getChild(3))
    

    def visitRetorno(self, ctx:compiladoresParser.RetornoContext):
        self.f.write("pop return-" + str(self.cont)  + "\n")
        self.f.write(f"push {ctx.getChild(0).getText()}-{str(self.cont)}\n")
        self.f.write("goto return-" + str(self.cont) + "\n")
        self.cont = self.cont - 1


    def visitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        self.f.write("pop " + str(ctx.getChild(1)) + "\n")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcion.
    def visitFuncion(self, ctx:compiladoresParser.FuncionContext):
        return self.visitChildren(ctx)


    def visitParametros(self, ctx:compiladoresParser.ParametrosContext):
        self.f.write("push " + str(ctx.getChild(0))+ "\n")
        return self.visitChildren(ctx)

    def visitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        self.cont = self.cont + 1
        self.currentLoop.append(self.cont)
        
        #   t1 := 0                     ; inicializa i
        #   L1:                         ; etiquieta
        #   if t1 >= 10 goto L2         ; salto condicional
        #   ...                         ; codigo
        #   goto L1                     ; salto al loop
        #   L2:                         ; continuacion del programa
        #   ...
        
        # Escribimos la declaracion del iterador
        self.f.write("t" + str(self.tmp) + "=" + ctx.getChild(2).getChild(1).getText().split('=')[1] + "\n")
        self.tmp = self.tmp + 1
        
        # Escribimos la label que corresponde
        self.f.write("LOOP-" + str(self.currentLoop[-1]) + ":\n")
        
        # Escribimos la comprobacion para el salto condicional
        self.f.write(f'if t{self.tmp - 1}{ctx.getChild(4).getChild(1)}{ctx.getChild(4).getChild(2)} ')
        
        # Realizamos el salto si hace falta
        self.f.write(f'goto CONTPROG-{self.currentLoop[-1]} \n')
        
        # CODIGO INTERMEDIO PARA EL INTERIOR DEL LOOP
        # visitamos el hijo donde estan las instrucciones -> el hijo 8
        self.visitChildren(ctx.getChild(8))
        
        
        # CODIGO INTERMEDIO PARA EL INCREMENTO O DECREMENTO DEL ITERADOR 
        # visitar el hijo donde este el incremento/decremento -> 6

        iterador = ctx.getChild(6).getChild(0)
        operacion = str(ctx.getChild(6).getChild(1))
        
        if '=' in operacion:
            self.visitChildren(ctx.getChild(6))
        elif '-' in operacion:
            self.f.write(f"t{self.tmp}=t{self.tmp}-1\n")            
        elif '+' in operacion:
            self.f.write(f"t{self.tmp}=t{self.tmp}+1\n")            

        # Salto al loop
        self.f.write(f'goto LOOP-{self.currentLoop[-1]} \n')
        
        
        self.f.write(f'CONTPROG-{self.currentLoop[-1]}: \n')        
        self.currentLoop.pop()
        
        

    # Visit a parse tree produced by compiladoresParser#bloquewhile.
    def visitBloquewhile(self, ctx:compiladoresParser.BloquewhileContext):
        

        # while(x<10 && y>=0){
        # x=x+1;
        # y=y-1;
        # }
        # 
        # Su código de 3 direcciones equivalente va como sigue:
        # 
        # L1: //etiqueta de salto de retorno
        # if(x<10) goto L2;
        # goto L3;
        # L2:if(y>=0)goto L4;
        # goto L3;
        # L4: //si es verdadera la condicion
        # x=x+1;
        # y=y-1;
        # goto L1; //salto para volver a evaluar la condicion
        # L3
        self.cont = self.cont + 1
        self.currentLoop.append(self.cont)

        # Etiqueta de retorno al bucle
        self.f.write(f'LOOP-{self.currentLoop[-1]}:\n')
        
        # Escribimos la comprobacion para el salto condicional
        self.f.write(f'if {ctx.getChild(1).getChild(1).getText()} ')
        
        # Realizamos el salto si hace falta
        self.f.write(f'goto CONTPROG-{self.currentLoop[-1]} \n')
        
        # CODIGO INTERMEDIO PARA EL INTERIOR DEL LOOP
        # visitamos el hijo donde estan las instrucciones -> el hijo 2
        self.visitChildren(ctx.getChild(2))
        
        
        # Salto al loop
        self.f.write(f'goto LOOP-{self.currentLoop[-1]} \n')
        self.f.write(f'CONTPROG-{self.currentLoop[-1]}: \n')        
        self.currentLoop.pop()
        

    #TODO::REVISAR
    def visitBloqueif(self, ctx:compiladoresParser.BloqueifContext):
        
        self.cont = self.cont + 1
        
        self.f.write("ifnot " + ctx.getChild(2).getText() + " goto ELSE-" + str(self.cont) + "\n")
        
        self.f.write(f"goto ENDIF {str(self.lastLabel[-1])}\n")
        self.f.write(f"ELSE-{str(self.lastLabel[-1])}:\n")

        if(ctx.getChild(5)):
            self.visitChildren(ctx.getChild(5))

        self.f.write("ENDIF-" + str(self.lastLabel[-1]) + ":\n")
        self.lastLabel.pop()


    #TODO::REVISAR
    def visitBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
        self.visitChildren(ctx)
        self.f.write("ENDIF-" + str(self.lastLabel[-1]) + ":\n")


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#conDeclaracion.
    def visitConDeclaracion(self, ctx:compiladoresParser.ConDeclaracionContext):
        return self.visitChildren(ctx)


    def visitInit(self, ctx:compiladoresParser.InitContext):
        self.visitChildren(ctx)
        self.f.write(ctx.getText() + "\n")
        self.rollback = False


    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        self.visitChildren(ctx)
        self.f.write(str(ctx.getChild(0)) + "= t" + str(self.tmp) + "\n")
        self.tmp = 0


    def visitAsignarFuncion(self, ctx:compiladoresParser.AsignarFuncionContext):
        self.f.write("push PC\n")
        self.visitChildren(ctx)
        if(self.lastLabel):
            self.lastLabel.pop()
        
        self.f.write("goto " + str(ctx.getChild(2).getChild(0)).upper() + "\n")
        self.f.write("pop " + str(ctx.getChild(0))+ "\n")


    # Visit a parse tree produced by compiladoresParser#tdato.
    def visitTdato(self, ctx:compiladoresParser.TdatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#itop.
    def visitItop(self, ctx:compiladoresParser.ItopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oparit.
    def visitOparit(self, ctx:compiladoresParser.OparitContext):
        return self.visitChildren(ctx)


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


    def visitT(self, ctx:compiladoresParser.TContext):
        self.visitChildren(ctx)
        
        if ctx.getChildCount() and not self.rollback:
            self.f.write("t" + str(self.tmp) + "=" + ctx.getChild(1).getText() + "\n")
            self.tmp = self.tmp + 1
            
        elif self.rollback and ctx.getChildCount():
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