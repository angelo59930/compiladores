# Generated from /home/angelo/Facultad/Tercero/DHS/test/src/main/python/compiladores.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("p\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3&\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6;\n\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7D\n\7\3\b\3\b\3\t\3\t\3\t\3\t\5\tL\n\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r_\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("g\n\16\3\17\3\17\3\17\3\17\3\17\5\17n\n\17\3\17\2\2\20")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\2\2m\2\36\3\2\2")
        buf.write("\2\4%\3\2\2\2\6.\3\2\2\2\b\60\3\2\2\2\n:\3\2\2\2\fC\3")
        buf.write("\2\2\2\16E\3\2\2\2\20K\3\2\2\2\22M\3\2\2\2\24O\3\2\2\2")
        buf.write("\26R\3\2\2\2\30^\3\2\2\2\32f\3\2\2\2\34m\3\2\2\2\36\37")
        buf.write("\5\4\3\2\37 \7\2\2\3 \3\3\2\2\2!\"\5\6\4\2\"#\5\4\3\2")
        buf.write("#&\3\2\2\2$&\3\2\2\2%!\3\2\2\2%$\3\2\2\2&\5\3\2\2\2\'")
        buf.write("/\5\b\5\2()\5\f\7\2)*\7\7\2\2*/\3\2\2\2+,\5\n\6\2,-\7")
        buf.write("\7\2\2-/\3\2\2\2.\'\3\2\2\2.(\3\2\2\2.+\3\2\2\2/\7\3\2")
        buf.write("\2\2\60\61\7\5\2\2\61\62\5\4\3\2\62\63\7\6\2\2\63\t\3")
        buf.write("\2\2\2\64\65\7\16\2\2\65\66\7\b\2\2\66;\7\r\2\2\678\7")
        buf.write("\16\2\289\7\b\2\29;\5\20\t\2:\64\3\2\2\2:\67\3\2\2\2;")
        buf.write("\13\3\2\2\2<=\5\16\b\2=>\7\16\2\2>D\3\2\2\2?@\5\16\b\2")
        buf.write("@A\5\n\6\2AD\3\2\2\2BD\3\2\2\2C<\3\2\2\2C?\3\2\2\2CB\3")
        buf.write("\2\2\2D\r\3\2\2\2EF\7\f\2\2F\17\3\2\2\2GH\5\22\n\2HI\5")
        buf.write("\20\t\2IL\3\2\2\2JL\3\2\2\2KG\3\2\2\2KJ\3\2\2\2L\21\3")
        buf.write("\2\2\2MN\5\24\13\2N\23\3\2\2\2OP\5\26\f\2PQ\5\30\r\2Q")
        buf.write("\25\3\2\2\2RS\5\32\16\2ST\5\34\17\2T\27\3\2\2\2UV\7\t")
        buf.write("\2\2VW\5\26\f\2WX\5\30\r\2X_\3\2\2\2YZ\7\13\2\2Z[\5\26")
        buf.write("\f\2[\\\5\30\r\2\\_\3\2\2\2]_\3\2\2\2^U\3\2\2\2^Y\3\2")
        buf.write("\2\2^]\3\2\2\2_\31\3\2\2\2`g\7\16\2\2ag\7\r\2\2bc\7\3")
        buf.write("\2\2cd\5\24\13\2de\7\4\2\2eg\3\2\2\2f`\3\2\2\2fa\3\2\2")
        buf.write("\2fb\3\2\2\2g\33\3\2\2\2hi\7\n\2\2ij\5\32\16\2jk\5\34")
        buf.write("\17\2kn\3\2\2\2ln\3\2\2\2mh\3\2\2\2ml\3\2\2\2n\35\3\2")
        buf.write("\2\2\n%.:CK^fm")
        return buf.getvalue()


class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "'+'", "'*'", "'-'", "'int'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "ASSIG", 
                      "SUMA", "MULT", "REST", "INT", "NUMERO", "ID", "WS" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_bloque = 3
    RULE_asignacion = 4
    RULE_declaracion = 5
    RULE_tdato = 6
    RULE_itop = 7
    RULE_oparit = 8
    RULE_exp = 9
    RULE_term = 10
    RULE_t = 11
    RULE_factor = 12
    RULE_f = 13

    ruleNames =  [ "programa", "instrucciones", "instruccion", "bloque", 
                   "asignacion", "declaracion", "tdato", "itop", "oparit", 
                   "exp", "term", "t", "factor", "f" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    ASSIG=6
    SUMA=7
    MULT=8
    REST=9
    INT=10
    NUMERO=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladoresParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.instrucciones()
            self.state = 29
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladoresParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.LLA, compiladoresParser.PYC, compiladoresParser.INT, compiladoresParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.instruccion()
                self.state = 32
                self.instrucciones()
                pass
            elif token in [compiladoresParser.EOF, compiladoresParser.LLC]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladoresParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.LLA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.bloque()
                pass
            elif token in [compiladoresParser.PYC, compiladoresParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.declaracion()
                self.state = 39
                self.match(compiladoresParser.PYC)
                pass
            elif token in [compiladoresParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.asignacion()
                self.state = 42
                self.match(compiladoresParser.PYC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladoresParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(compiladoresParser.LLA)
            self.state = 47
            self.instrucciones()
            self.state = 48
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASSIG(self):
            return self.getToken(compiladoresParser.ASSIG, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def itop(self):
            return self.getTypedRuleContext(compiladoresParser.ItopContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladoresParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(compiladoresParser.ID)
                self.state = 51
                self.match(compiladoresParser.ASSIG)
                self.state = 52
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(compiladoresParser.ID)
                self.state = 54
                self.match(compiladoresParser.ASSIG)
                self.state = 55
                self.itop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladoresParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracion)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.tdato()
                self.state = 59
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.tdato()
                self.state = 62
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TdatoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tdato

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTdato" ):
                listener.enterTdato(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTdato" ):
                listener.exitTdato(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTdato" ):
                return visitor.visitTdato(self)
            else:
                return visitor.visitChildren(self)




    def tdato(self):

        localctx = compiladoresParser.TdatoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tdato)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(compiladoresParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def oparit(self):
            return self.getTypedRuleContext(compiladoresParser.OparitContext,0)


        def itop(self):
            return self.getTypedRuleContext(compiladoresParser.ItopContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_itop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItop" ):
                listener.enterItop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItop" ):
                listener.exitItop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItop" ):
                return visitor.visitItop(self)
            else:
                return visitor.visitChildren(self)




    def itop(self):

        localctx = compiladoresParser.ItopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_itop)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.PA, compiladoresParser.NUMERO, compiladoresParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.oparit()
                self.state = 70
                self.itop()
                pass
            elif token in [compiladoresParser.PYC]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OparitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_oparit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOparit" ):
                listener.enterOparit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOparit" ):
                listener.exitOparit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOparit" ):
                return visitor.visitOparit(self)
            else:
                return visitor.visitChildren(self)




    def oparit(self):

        localctx = compiladoresParser.OparitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_oparit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladoresParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.term()
            self.state = 78
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def f(self):
            return self.getTypedRuleContext(compiladoresParser.FContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladoresParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.factor()
            self.state = 81
            self.f()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


        def REST(self):
            return self.getToken(compiladoresParser.REST, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladoresParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_t)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.SUMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(compiladoresParser.SUMA)
                self.state = 84
                self.term()
                self.state = 85
                self.t()
                pass
            elif token in [compiladoresParser.REST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(compiladoresParser.REST)
                self.state = 88
                self.term()
                self.state = 89
                self.t()
                pass
            elif token in [compiladoresParser.PA, compiladoresParser.PC, compiladoresParser.PYC, compiladoresParser.NUMERO, compiladoresParser.ID]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladoresParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_factor)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(compiladoresParser.ID)
                pass
            elif token in [compiladoresParser.NUMERO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [compiladoresParser.PA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(compiladoresParser.PA)
                self.state = 97
                self.exp()
                self.state = 98
                self.match(compiladoresParser.PC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def f(self):
            return self.getTypedRuleContext(compiladoresParser.FContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_f

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF" ):
                listener.enterF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF" ):
                listener.exitF(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF" ):
                return visitor.visitF(self)
            else:
                return visitor.visitChildren(self)




    def f(self):

        localctx = compiladoresParser.FContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_f)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.MULT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(compiladoresParser.MULT)
                self.state = 103
                self.factor()
                self.state = 104
                self.f()
                pass
            elif token in [compiladoresParser.PA, compiladoresParser.PC, compiladoresParser.PYC, compiladoresParser.SUMA, compiladoresParser.REST, compiladoresParser.NUMERO, compiladoresParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





