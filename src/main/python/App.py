import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from MiListener import MiListener

def main(argv):
    archivo = "input/entrada.c"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    miListener = MiListener()
    parser.addParseListener(miListener)
    tree = parser.programa()


if __name__ == '__main__':
    main(sys.argv)