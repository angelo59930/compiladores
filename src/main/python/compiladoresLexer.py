# Generated from /home/angelo/Facultad/Tercero/DHS/test/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\16\6\16=\n\16\r\16\16\16>\3")
        buf.write("\17\3\17\5\17C\n\17\3\17\3\17\3\17\7\17H\n\17\f\17\16")
        buf.write("\17K\13\17\3\20\3\20\3\20\3\20\2\2\21\3\2\5\2\7\3\t\4")
        buf.write("\13\5\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35\16\37")
        buf.write("\17\3\2\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2R\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3")
        buf.write("!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2")
        buf.write("\2\r+\3\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23\61\3\2\2\2\25")
        buf.write("\63\3\2\2\2\27\65\3\2\2\2\31\67\3\2\2\2\33<\3\2\2\2\35")
        buf.write("B\3\2\2\2\37L\3\2\2\2!\"\t\2\2\2\"\4\3\2\2\2#$\t\3\2\2")
        buf.write("$\6\3\2\2\2%&\7*\2\2&\b\3\2\2\2\'(\7+\2\2(\n\3\2\2\2)")
        buf.write("*\7}\2\2*\f\3\2\2\2+,\7\177\2\2,\16\3\2\2\2-.\7=\2\2.")
        buf.write("\20\3\2\2\2/\60\7?\2\2\60\22\3\2\2\2\61\62\7-\2\2\62\24")
        buf.write("\3\2\2\2\63\64\7,\2\2\64\26\3\2\2\2\65\66\7/\2\2\66\30")
        buf.write("\3\2\2\2\678\7k\2\289\7p\2\29:\7v\2\2:\32\3\2\2\2;=\5")
        buf.write("\5\3\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?\34\3\2")
        buf.write("\2\2@C\5\3\2\2AC\7a\2\2B@\3\2\2\2BA\3\2\2\2CI\3\2\2\2")
        buf.write("DH\5\3\2\2EH\5\5\3\2FH\7a\2\2GD\3\2\2\2GE\3\2\2\2GF\3")
        buf.write("\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\36\3\2\2\2KI\3\2")
        buf.write("\2\2LM\t\4\2\2MN\3\2\2\2NO\b\20\2\2O \3\2\2\2\7\2>BGI")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class compiladoresLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PA = 1
    PC = 2
    LLA = 3
    LLC = 4
    PYC = 5
    ASSIG = 6
    SUMA = 7
    MULT = 8
    REST = 9
    INT = 10
    NUMERO = 11
    ID = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "';'", "'='", "'+'", "'*'", "'-'", 
            "'int'" ]

    symbolicNames = [ "<INVALID>",
            "PA", "PC", "LLA", "LLC", "PYC", "ASSIG", "SUMA", "MULT", "REST", 
            "INT", "NUMERO", "ID", "WS" ]

    ruleNames = [ "LETRA", "DIGITO", "PA", "PC", "LLA", "LLC", "PYC", "ASSIG", 
                  "SUMA", "MULT", "REST", "INT", "NUMERO", "ID", "WS" ]

    grammarFileName = "compiladores.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


