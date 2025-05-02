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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\5\2\u008d\n\2\3\2\3\2\3\2\3\2\3\3\6")
        buf.write("\3\u0094\n\3\r\3\16\3\u0095\3\3\3\3\3\4\3\4\3\4\3\4\7")
        buf.write("\4\u009e\n\4\f\4\16\4\u00a1\13\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\7\5\u00aa\n\5\f\5\16\5\u00ad\13\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\79\u0175\n9\f9\169\u0178\13")
        buf.write("9\3:\3:\7:\u017c\n:\f:\16:\u017f\13:\3:\5:\u0182\n:\3")
        buf.write(";\3;\3<\3<\3<\6<\u0189\n<\r<\16<\u018a\3=\3=\3=\6=\u0190")
        buf.write("\n=\r=\16=\u0191\3>\3>\3>\6>\u0197\n>\r>\16>\u0198\3?")
        buf.write("\6?\u019c\n?\r?\16?\u019d\3?\3?\7?\u01a2\n?\f?\16?\u01a5")
        buf.write("\13?\3?\5?\u01a8\n?\3@\3@\5@\u01ac\n@\3@\6@\u01af\n@\r")
        buf.write("@\16@\u01b0\3A\3A\7A\u01b5\nA\fA\16A\u01b8\13A\3A\3A\3")
        buf.write("B\3B\3B\5B\u01bf\nB\3C\3C\3D\3D\7D\u01c5\nD\fD\16D\u01c8")
        buf.write("\13D\3D\3D\3D\3E\3E\7E\u01cf\nE\fE\16E\u01d2\13E\3E\5")
        buf.write("E\u01d5\nE\3E\3E\5E\u01d9\nE\3E\3E\3\u00ab\2F\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w<y={>")
        buf.write("}?\177\2\u0081@\u0083\2\u0085A\u0087B\u0089C\3\2\22\5")
        buf.write("\2\13\13\16\17\"\"\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\62")
        buf.write("9\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\5\2\f\f$$^^\7\2")
        buf.write("$$^^ppttvv\2\u01ee\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0081\3\2\2\2\2\u0085\3\2")
        buf.write("\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008c\3\2\2\2\5")
        buf.write("\u0093\3\2\2\2\7\u0099\3\2\2\2\t\u00a4\3\2\2\2\13\u00b3")
        buf.write("\3\2\2\2\r\u00b6\3\2\2\2\17\u00bb\3\2\2\2\21\u00bf\3\2")
        buf.write("\2\2\23\u00c6\3\2\2\2\25\u00cb\3\2\2\2\27\u00d0\3\2\2")
        buf.write("\2\31\u00d7\3\2\2\2\33\u00e1\3\2\2\2\35\u00e8\3\2\2\2")
        buf.write("\37\u00ec\3\2\2\2!\u00f2\3\2\2\2#\u00fa\3\2\2\2%\u0100")
        buf.write("\3\2\2\2\'\u0104\3\2\2\2)\u010d\3\2\2\2+\u0113\3\2\2\2")
        buf.write("-\u0119\3\2\2\2/\u011d\3\2\2\2\61\u0122\3\2\2\2\63\u0128")
        buf.write("\3\2\2\2\65\u012a\3\2\2\2\67\u012c\3\2\2\29\u012e\3\2")
        buf.write("\2\2;\u0130\3\2\2\2=\u0132\3\2\2\2?\u0135\3\2\2\2A\u0138")
        buf.write("\3\2\2\2C\u013a\3\2\2\2E\u013d\3\2\2\2G\u013f\3\2\2\2")
        buf.write("I\u0142\3\2\2\2K\u0145\3\2\2\2M\u0148\3\2\2\2O\u014a\3")
        buf.write("\2\2\2Q\u014c\3\2\2\2S\u014f\3\2\2\2U\u0152\3\2\2\2W\u0155")
        buf.write("\3\2\2\2Y\u0158\3\2\2\2[\u015b\3\2\2\2]\u015e\3\2\2\2")
        buf.write("_\u0160\3\2\2\2a\u0162\3\2\2\2c\u0164\3\2\2\2e\u0166\3")
        buf.write("\2\2\2g\u0168\3\2\2\2i\u016a\3\2\2\2k\u016c\3\2\2\2m\u016e")
        buf.write("\3\2\2\2o\u0170\3\2\2\2q\u0172\3\2\2\2s\u0181\3\2\2\2")
        buf.write("u\u0183\3\2\2\2w\u0185\3\2\2\2y\u018c\3\2\2\2{\u0193\3")
        buf.write("\2\2\2}\u019b\3\2\2\2\177\u01a9\3\2\2\2\u0081\u01b2\3")
        buf.write("\2\2\2\u0083\u01be\3\2\2\2\u0085\u01c0\3\2\2\2\u0087\u01c2")
        buf.write("\3\2\2\2\u0089\u01cc\3\2\2\2\u008b\u008d\7\17\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\u008f\7\f\2\2\u008f\u0090\3\2\2\2\u0090\u0091\b")
        buf.write("\2\2\2\u0091\4\3\2\2\2\u0092\u0094\t\2\2\2\u0093\u0092")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2\u0095")
        buf.write("\u0096\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\b\3\3\2")
        buf.write("\u0098\6\3\2\2\2\u0099\u009a\7\61\2\2\u009a\u009b\7\61")
        buf.write("\2\2\u009b\u009f\3\2\2\2\u009c\u009e\n\3\2\2\u009d\u009c")
        buf.write("\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a2\u00a3\b\4\3\2\u00a3\b\3\2\2\2\u00a4\u00a5\7\61")
        buf.write("\2\2\u00a5\u00a6\7,\2\2\u00a6\u00ab\3\2\2\2\u00a7\u00aa")
        buf.write("\5\t\5\2\u00a8\u00aa\13\2\2\2\u00a9\u00a7\3\2\2\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ab\u00a9\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3")
        buf.write("\2\2\2\u00ae\u00af\7,\2\2\u00af\u00b0\7\61\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\u00b2\b\5\3\2\u00b2\n\3\2\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7h\2\2\u00b5\f\3\2\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\16\3\2\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7t\2\2\u00be\20\3\2\2\2\u00bf\u00c0")
        buf.write("\7t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7w\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7p\2\2\u00c5\22")
        buf.write("\3\2\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\u00ca\7e\2\2\u00ca\24\3\2\2\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\u00cd\7{\2\2\u00cd\u00ce\7r\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\26\3\2\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5")
        buf.write("\7e\2\2\u00d5\u00d6\7v\2\2\u00d6\30\3\2\2\2\u00d7\u00d8")
        buf.write("\7k\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7h\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7e\2\2\u00df\u00e0\7g\2\2\u00e0\32")
        buf.write("\3\2\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7i\2\2\u00e7\34\3\2\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7v\2\2\u00eb\36\3\2\2\2\u00ec\u00ed")
        buf.write("\7h\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00f1\7v\2\2\u00f1 \3\2\2\2\u00f2\u00f3")
        buf.write("\7d\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6")
        buf.write("\7n\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9")
        buf.write("\7p\2\2\u00f9\"\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc")
        buf.write("\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff$\3\2\2\2\u0100\u0101\7x\2\2\u0101\u0102")
        buf.write("\7c\2\2\u0102\u0103\7t\2\2\u0103&\3\2\2\2\u0104\u0105")
        buf.write("\7e\2\2\u0105\u0106\7q\2\2\u0106\u0107\7p\2\2\u0107\u0108")
        buf.write("\7v\2\2\u0108\u0109\7k\2\2\u0109\u010a\7p\2\2\u010a\u010b")
        buf.write("\7w\2\2\u010b\u010c\7g\2\2\u010c(\3\2\2\2\u010d\u010e")
        buf.write("\7d\2\2\u010e\u010f\7t\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write("\7c\2\2\u0111\u0112\7m\2\2\u0112*\3\2\2\2\u0113\u0114")
        buf.write("\7t\2\2\u0114\u0115\7c\2\2\u0115\u0116\7p\2\2\u0116\u0117")
        buf.write("\7i\2\2\u0117\u0118\7g\2\2\u0118,\3\2\2\2\u0119\u011a")
        buf.write("\7p\2\2\u011a\u011b\7k\2\2\u011b\u011c\7n\2\2\u011c.\3")
        buf.write("\2\2\2\u011d\u011e\7v\2\2\u011e\u011f\7t\2\2\u011f\u0120")
        buf.write("\7w\2\2\u0120\u0121\7g\2\2\u0121\60\3\2\2\2\u0122\u0123")
        buf.write("\7h\2\2\u0123\u0124\7c\2\2\u0124\u0125\7n\2\2\u0125\u0126")
        buf.write("\7u\2\2\u0126\u0127\7g\2\2\u0127\62\3\2\2\2\u0128\u0129")
        buf.write("\7-\2\2\u0129\64\3\2\2\2\u012a\u012b\7/\2\2\u012b\66\3")
        buf.write("\2\2\2\u012c\u012d\7,\2\2\u012d8\3\2\2\2\u012e\u012f\7")
        buf.write("\61\2\2\u012f:\3\2\2\2\u0130\u0131\7\'\2\2\u0131<\3\2")
        buf.write("\2\2\u0132\u0133\7?\2\2\u0133\u0134\7?\2\2\u0134>\3\2")
        buf.write("\2\2\u0135\u0136\7#\2\2\u0136\u0137\7?\2\2\u0137@\3\2")
        buf.write("\2\2\u0138\u0139\7>\2\2\u0139B\3\2\2\2\u013a\u013b\7>")
        buf.write("\2\2\u013b\u013c\7?\2\2\u013cD\3\2\2\2\u013d\u013e\7@")
        buf.write("\2\2\u013eF\3\2\2\2\u013f\u0140\7@\2\2\u0140\u0141\7?")
        buf.write("\2\2\u0141H\3\2\2\2\u0142\u0143\7(\2\2\u0143\u0144\7(")
        buf.write("\2\2\u0144J\3\2\2\2\u0145\u0146\7~\2\2\u0146\u0147\7~")
        buf.write("\2\2\u0147L\3\2\2\2\u0148\u0149\7#\2\2\u0149N\3\2\2\2")
        buf.write("\u014a\u014b\7?\2\2\u014bP\3\2\2\2\u014c\u014d\7<\2\2")
        buf.write("\u014d\u014e\7?\2\2\u014eR\3\2\2\2\u014f\u0150\7-\2\2")
        buf.write("\u0150\u0151\7?\2\2\u0151T\3\2\2\2\u0152\u0153\7/\2\2")
        buf.write("\u0153\u0154\7?\2\2\u0154V\3\2\2\2\u0155\u0156\7,\2\2")
        buf.write("\u0156\u0157\7?\2\2\u0157X\3\2\2\2\u0158\u0159\7\61\2")
        buf.write("\2\u0159\u015a\7?\2\2\u015aZ\3\2\2\2\u015b\u015c\7\'\2")
        buf.write("\2\u015c\u015d\7?\2\2\u015d\\\3\2\2\2\u015e\u015f\7\60")
        buf.write("\2\2\u015f^\3\2\2\2\u0160\u0161\7<\2\2\u0161`\3\2\2\2")
        buf.write("\u0162\u0163\7*\2\2\u0163b\3\2\2\2\u0164\u0165\7+\2\2")
        buf.write("\u0165d\3\2\2\2\u0166\u0167\7}\2\2\u0167f\3\2\2\2\u0168")
        buf.write("\u0169\7\177\2\2\u0169h\3\2\2\2\u016a\u016b\7]\2\2\u016b")
        buf.write("j\3\2\2\2\u016c\u016d\7_\2\2\u016dl\3\2\2\2\u016e\u016f")
        buf.write("\7.\2\2\u016fn\3\2\2\2\u0170\u0171\7=\2\2\u0171p\3\2\2")
        buf.write("\2\u0172\u0176\t\4\2\2\u0173\u0175\t\5\2\2\u0174\u0173")
        buf.write("\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177r\3\2\2\2\u0178\u0176\3\2\2\2\u0179")
        buf.write("\u017d\t\6\2\2\u017a\u017c\5u;\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u0182\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0182\7")
        buf.write("\62\2\2\u0181\u0179\3\2\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("t\3\2\2\2\u0183\u0184\t\7\2\2\u0184v\3\2\2\2\u0185\u0186")
        buf.write("\7\62\2\2\u0186\u0188\t\b\2\2\u0187\u0189\t\t\2\2\u0188")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u0188\3\2\2\2")
        buf.write("\u018a\u018b\3\2\2\2\u018bx\3\2\2\2\u018c\u018d\7\62\2")
        buf.write("\2\u018d\u018f\t\n\2\2\u018e\u0190\t\13\2\2\u018f\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192z\3\2\2\2\u0193\u0194\7\62\2\2\u0194")
        buf.write("\u0196\t\f\2\2\u0195\u0197\t\r\2\2\u0196\u0195\3\2\2\2")
        buf.write("\u0197\u0198\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3")
        buf.write("\2\2\2\u0199|\3\2\2\2\u019a\u019c\5u;\2\u019b\u019a\3")
        buf.write("\2\2\2\u019c\u019d\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a3\7\60\2\2\u01a0")
        buf.write("\u01a2\5u;\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a7\3\2\2\2")
        buf.write("\u01a5\u01a3\3\2\2\2\u01a6\u01a8\5\177@\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8~\3\2\2\2\u01a9\u01ab")
        buf.write("\t\16\2\2\u01aa\u01ac\t\17\2\2\u01ab\u01aa\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01af\5u;\2\u01ae")
        buf.write("\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u0080\3\2\2\2\u01b2\u01b6\7")
        buf.write("$\2\2\u01b3\u01b5\5\u0083B\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7")
        buf.write("$\2\2\u01ba\u0082\3\2\2\2\u01bb\u01bf\n\20\2\2\u01bc\u01bd")
        buf.write("\7^\2\2\u01bd\u01bf\t\21\2\2\u01be\u01bb\3\2\2\2\u01be")
        buf.write("\u01bc\3\2\2\2\u01bf\u0084\3\2\2\2\u01c0\u01c1\13\2\2")
        buf.write("\2\u01c1\u0086\3\2\2\2\u01c2\u01c6\7$\2\2\u01c3\u01c5")
        buf.write("\5\u0083B\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c9\3\2\2\2")
        buf.write("\u01c8\u01c6\3\2\2\2\u01c9\u01ca\7^\2\2\u01ca\u01cb\n")
        buf.write("\21\2\2\u01cb\u0088\3\2\2\2\u01cc\u01d0\7$\2\2\u01cd\u01cf")
        buf.write("\5\u0083B\2\u01ce\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d8\3\2\2\2")
        buf.write("\u01d2\u01d0\3\2\2\2\u01d3\u01d5\7\17\2\2\u01d4\u01d3")
        buf.write("\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write("\u01d9\7\f\2\2\u01d7\u01d9\7\2\2\3\u01d8\u01d4\3\2\2\2")
        buf.write("\u01d8\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01db\b")
        buf.write("E\4\2\u01db\u008a\3\2\2\2\31\2\u008c\u0095\u009f\u00a9")
        buf.write("\u00ab\u0176\u017d\u0181\u018a\u0191\u0198\u019d\u01a3")
        buf.write("\u01a7\u01ab\u01b0\u01b6\u01be\u01c6\u01d0\u01d4\u01d8")
        buf.write("\5\3\2\2\b\2\2\3E\3")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NL = 1
    WS = 2
    LINE_COMMENT = 3
    MULTI_LINE_COMMENT = 4
    IF = 5
    ELSE = 6
    FOR = 7
    RETURN = 8
    FUNC = 9
    TYPE = 10
    STRUCT = 11
    INTERFACE = 12
    STRING = 13
    INT = 14
    FLOAT = 15
    BOOLEAN = 16
    CONST = 17
    VAR = 18
    CONTINUE = 19
    BREAK = 20
    RANGE = 21
    NIL = 22
    TRUE = 23
    FALSE = 24
    PLUS = 25
    MINUS = 26
    STAR = 27
    SLASH = 28
    MOD = 29
    EQUALS = 30
    NOT_EQUALS = 31
    LESS_THAN = 32
    LESS_THAN_OR_EQUAL = 33
    GREATER_THAN = 34
    GREATER_THAN_OR_EQUAL = 35
    AND = 36
    OR = 37
    NOT = 38
    ASSIGN = 39
    COLON_ASSIGN = 40
    PLUS_ASSIGN = 41
    MINUS_ASSIGN = 42
    STAR_ASSIGN = 43
    SLASH_ASSIGN = 44
    MOD_ASSIGN = 45
    DOT = 46
    COLON = 47
    L_PAREN = 48
    R_PAREN = 49
    L_BRACE = 50
    R_BRACE = 51
    L_BRACKET = 52
    R_BRACKET = 53
    COMMA = 54
    SEMICOLON = 55
    IDENTIFIER = 56
    DECIMAL_INT = 57
    BINARY_INT = 58
    OCTAL_INT = 59
    HEX_INT = 60
    FLOAT_LIT = 61
    STRING_LIT = 62
    ERROR_CHAR = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "NL", "WS", "LINE_COMMENT", "MULTI_LINE_COMMENT", "IF", "ELSE", 
            "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
            "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
            "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", "STAR", "SLASH", 
            "MOD", "EQUALS", "NOT_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
            "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "AND", "OR", "NOT", 
            "ASSIGN", "COLON_ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "STAR_ASSIGN", 
            "SLASH_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", "L_PAREN", "R_PAREN", 
            "L_BRACE", "R_BRACE", "L_BRACKET", "R_BRACKET", "COMMA", "SEMICOLON", 
            "IDENTIFIER", "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", "HEX_INT", 
            "FLOAT_LIT", "STRING_LIT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "NL", "WS", "LINE_COMMENT", "MULTI_LINE_COMMENT", "IF", 
                  "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                  "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", 
                  "STAR", "SLASH", "MOD", "EQUALS", "NOT_EQUALS", "LESS_THAN", 
                  "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "COLON_ASSIGN", "PLUS_ASSIGN", 
                  "MINUS_ASSIGN", "STAR_ASSIGN", "SLASH_ASSIGN", "MOD_ASSIGN", 
                  "DOT", "COLON", "L_PAREN", "R_PAREN", "L_BRACE", "R_BRACE", 
                  "L_BRACKET", "R_BRACKET", "COMMA", "SEMICOLON", "IDENTIFIER", 
                  "DECIMAL_INT", "DIGIT", "BINARY_INT", "OCTAL_INT", "HEX_INT", 
                  "FLOAT_LIT", "EXPONENT", "STRING_LIT", "STRING_CHAR", 
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
            result = super().emit();
            self.preceding_token = result;
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.NL_action 
            actions[67] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                accepted_tokens_before_newline_char = [
                    self.IDENTIFIER, self.DECIMAL_INT, self.BINARY_INT, self.OCTAL_INT, 
                    self.HEX_INT, self.FLOAT_LIT, self.TRUE, self.FALSE, self.STRING_LIT, 
                    self.INT, self.FLOAT, self.BOOLEAN, self.STRING, self.RETURN, 
                    self.CONTINUE, self.BREAK, self.R_PAREN, self.R_BRACKET, self.R_BRACE
                ]
                if hasattr(self, 'preceding_token') and self.preceding_token and self.preceding_token.type in accepted_tokens_before_newline_char:
                    self.text = ';';
                    self.type = self.SEMICOLON;
                else:
                    self.skip();

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                if (self.text[-1] == '\n' and self.text[-2] == '\r'):
                    self.text = self.text[:-2];
                elif (self.text[-1] == '\n'):
                    self.text = self.text[:-1];
                else:
                    self.text = self.text[:]

     


