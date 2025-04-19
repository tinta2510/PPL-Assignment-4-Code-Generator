# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13@\n\13")
        buf.write("\r\13\16\13A\3\f\6\fE\n\f\r\f\16\fF\3\r\6\rJ\n\r\r\r\16")
        buf.write("\rK\3\r\3\r\6\rP\n\r\r\r\16\rQ\3\16\3\16\3\16\3\16\3\17")
        buf.write("\6\17Y\n\17\r\17\16\17Z\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23\3\2\5\4")
        buf.write("\2C\\c|\3\2\62;\5\2\13\13\17\17\"\"\2h\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5)\3\2")
        buf.write("\2\2\7-\3\2\2\2\t/\3\2\2\2\13\61\3\2\2\2\r\66\3\2\2\2")
        buf.write("\178\3\2\2\2\21:\3\2\2\2\23<\3\2\2\2\25?\3\2\2\2\27D\3")
        buf.write("\2\2\2\31I\3\2\2\2\33S\3\2\2\2\35X\3\2\2\2\37^\3\2\2\2")
        buf.write("!`\3\2\2\2#b\3\2\2\2%&\7x\2\2&\'\7c\2\2\'(\7t\2\2(\4\3")
        buf.write("\2\2\2)*\7k\2\2*+\7p\2\2+,\7v\2\2,\6\3\2\2\2-.\7?\2\2")
        buf.write(".\b\3\2\2\2/\60\7=\2\2\60\n\3\2\2\2\61\62\7h\2\2\62\63")
        buf.write("\7w\2\2\63\64\7p\2\2\64\65\7e\2\2\65\f\3\2\2\2\66\67\7")
        buf.write("*\2\2\67\16\3\2\2\289\7+\2\29\20\3\2\2\2:;\7}\2\2;\22")
        buf.write("\3\2\2\2<=\7\177\2\2=\24\3\2\2\2>@\t\2\2\2?>\3\2\2\2@")
        buf.write("A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\26\3\2\2\2CE\t\3\2\2DC")
        buf.write("\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\30\3\2\2\2HJ\t")
        buf.write("\3\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2")
        buf.write("\2MO\7\60\2\2NP\t\3\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2")
        buf.write("QR\3\2\2\2R\32\3\2\2\2ST\7\f\2\2TU\3\2\2\2UV\b\16\2\2")
        buf.write("V\34\3\2\2\2WY\t\4\2\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z")
        buf.write("[\3\2\2\2[\\\3\2\2\2\\]\b\17\2\2]\36\3\2\2\2^_\13\2\2")
        buf.write("\2_ \3\2\2\2`a\13\2\2\2a\"\3\2\2\2bc\13\2\2\2c$\3\2\2")
        buf.write("\2\b\2AFKQZ\3\b\2\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    ID = 10
    INTLIT = 11
    FLOATLIT = 12
    NL = 13
    WS = 14
    ERROR_CHAR = 15
    ILLEGAL_ESCAPE = 16
    UNCLOSE_STRING = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'int'", "'='", "';'", "'func'", "'('", "')'", "'{'", 
            "'}'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "FLOATLIT", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "ID", "INTLIT", "FLOATLIT", "NL", "WS", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


