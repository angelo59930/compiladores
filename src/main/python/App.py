import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from NewMyListener import compiladoresListener
from MyVisitor import MyVisitor

def main(argv):
    archivo = "input/entrada.c"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    miListener = compiladoresListener()
    miVisitor = MyVisitor()
    parser.addParseListener(miListener)
    tree = parser.programa()
    #miVisitor.visitPrograma(tree)
    #tree = parser.prog()

if __name__ == '__main__':
    main(sys.argv)